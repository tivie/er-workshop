"""Consulta a base de conhecimento da Estratificação pelo Risco (texto extraído das fontes).

Os textos estão em index/_text/<slug>.txt, com um marcador `=== PÁGINA N ===` por página
física do PDF original. Este script devolve sempre o documento e a página, para que cada
afirmação possa ser citada.

Uso:
  python scripts/consultar.py docs
      Lista os documentos (abreviatura, slug, n.º de páginas, ficheiro de origem).

  python scripts/consultar.py paginas <doc> <páginas>
      Mostra o texto das páginas pedidas. <páginas>: "5", "4-5", "2,4-5,9".
      Se o índice do documento tiver valores transcritos de figuras dessas páginas
      (secção "Factos lidos nas figuras"), mostra-os a seguir.

  python scripts/consultar.py procurar "<termo>" [--doc <doc>] [--max N] [--contexto N] [--parcial] [--regex]
      Procura em todos os documentos (ou só num), ignorando maiúsculas e acentos.
      Mostra primeiro as páginas com ocorrências por documento e depois excertos
      (um por página; --max 0 mostra só a distribuição por páginas).
      O termo é procurado no início de palavra ("prazo" apanha "prazos", não "omeprazole");
      com --parcial também a meio de palavra.

<doc> pode ser a abreviatura usada no INDEX.md (CN4, DESP, BI, REL-SINT, JH-UD, POP04…),
o slug, ou qualquer parte do slug que identifique um único documento ("manual-bi").
"""
import argparse
import re
import sys
import unicodedata
from pathlib import Path

INDEX = Path(__file__).resolve().parent.parent / "index"
TEXTOS = INDEX / "_text"
MARCADOR = re.compile(r"^=== PÁGINA (\d+) ===[ \t]*$", re.M)
SECCAO_FIGURAS = re.compile(r"^## Factos lidos nas figuras.*?(?=^## |\Z)", re.M | re.S)
FIGURAS = "figuras"  # "página" fictícia: valores transcritos de figuras, guardados no índice

# Abreviaturas do INDEX.md -> parte do slug que identifica o documento.
ALIAS = {
    "DESP": "despacho-n-o-12986-2023",
    "CN4": "circular-normativa-4-",
    "CN12": "circular-normativa-12-",
    "EST": "estrategia-para-a-estratificacao",
    "ACG": "adjusted-clinical-groups-acg",
    "BI": "manual-bi-er",
    "AIPD": "modelo-aipd",
    "ART": "desafios-e-perspectivas",
    "PUB": "sns-930-mil",
    "REL-SINT": "relatorio-sintese",
    "REL-PROJ": "relatorio-projeto",
    "WHO-ES": "who-euro-2018",
    "ICM-WHO": "integrated-care-models",
    "WHO-IPCHS": "who-2016-framework",
    "WHO-FFA": "who-euro-2016",
    "WHO-PHM": "who-euro-2023",
    "JHM": "planning-for-the-future",
    "JH-UD": "user-documentation",
    "JH-TR": "technical-reference",
    "WEI96": "weiner-1996",
    "ADA02": "adams-2002",
    "POP04": "pope-2004",
    "GIF04": "gifford-2004",
    "WER08": "weir-2008",
    "ANE18": "anell-2018",
    "ISA16": "isaksson-2016",
    "HAL06": "halling-2006",
    "ORU13": "orueta-2013",
    "SHA11": "shadmi-2011",
    "SAN14": "santelices-2014",
    "SAN16": "santelices-2016",
    "CHA10": "chang-weiner-2010",
    "HOS24": "hosar-2024",
}


def slugs() -> list[str]:
    return sorted(p.stem for p in TEXTOS.glob("*.txt"))


def por_fragmento(fragmento: str, todos: list[str]) -> list[str]:
    """Slugs que correspondem ao fragmento: o exato, senão os que começam por ele, senão os que o contêm."""
    if fragmento in todos:
        return [fragmento]
    return [s for s in todos if s.startswith(fragmento)] or [s for s in todos if fragmento in s]


def resolver(doc: str) -> str:
    todos = slugs()
    alvo = doc.strip().removesuffix(".txt").removesuffix(".md")
    candidatos = por_fragmento(ALIAS.get(alvo.upper(), alvo.lower()), todos)
    if len(candidatos) == 1:
        return candidatos[0]
    if not candidatos:
        sys.exit(f"Documento não encontrado: '{doc}'. Ver a lista com: consultar.py docs")
    sys.exit(f"'{doc}' é ambíguo; corresponde a:\n  " + "\n  ".join(candidatos))


def ler(slug: str) -> tuple[str, dict[int, str]]:
    """Devolve (nome do ficheiro de origem, {página: texto})."""
    texto = (TEXTOS / f"{slug}.txt").read_text(encoding="utf-8")
    partes = MARCADOR.split(texto)
    fonte = re.search(r"^# Fonte: (.+)$", partes[0], re.M)
    paginas = {int(partes[i]): partes[i + 1].strip("\n") for i in range(1, len(partes), 2)}
    return (fonte.group(1).strip() if fonte else slug), paginas


def figuras(slug: str) -> str:
    """Secção "Factos lidos nas figuras" do índice do documento (vazia se não existir)."""
    indice = INDEX / f"{slug}.md"
    if not indice.exists():
        return ""
    m = SECCAO_FIGURAS.search(indice.read_text(encoding="utf-8"))
    return m.group(0).strip() if m else ""


def intervalos(spec: str, ultima: int) -> list[int]:
    numeros: list[int] = []
    for bloco in spec.replace(" ", "").split(","):
        if not bloco:
            continue
        inicio, _, fim = bloco.partition("-")
        try:
            a, b = int(inicio), int(fim or inicio)
        except ValueError:
            sys.exit(f"Intervalo de páginas inválido: '{bloco}' (usar p. ex. 5 ou 4-6 ou 2,4-6)")
        numeros.extend(range(a, b + 1))
    fora = [n for n in numeros if n < 1 or n > ultima]
    if fora:
        sys.exit(f"Páginas fora do documento (tem {ultima}): {fora}")
    return numeros


def dobrar(texto: str) -> tuple[str, list[int]]:
    """Texto sem acentos, mais a posição original de cada carácter."""
    saida: list[str] = []
    origem: list[int] = []
    for i, c in enumerate(texto):
        for d in unicodedata.normalize("NFKD", c):
            if not unicodedata.combining(d):
                saida.append(d)
                origem.append(i)
    return "".join(saida), origem


def lista_paginas(contagem: dict) -> str:
    """"2, 5(×3), 10–14": páginas com ocorrências, com as sequências longas comprimidas."""
    numeros = sorted(n for n in contagem if n != FIGURAS)
    partes: list[str] = []
    i = 0
    while i < len(numeros):
        j = i
        while j + 1 < len(numeros) and numeros[j + 1] == numeros[j] + 1:
            j += 1
        if j - i >= 3:
            partes.append(f"{numeros[i]}–{numeros[j]}")
        else:
            partes.extend(f"{n}" + (f"(×{contagem[n]})" if contagem[n] > 1 else "") for n in numeros[i:j + 1])
        i = j + 1
    if FIGURAS in contagem:
        partes.append("valores transcritos de figuras (no índice)")
    return ", ".join(partes)


def cmd_docs(_: argparse.Namespace) -> None:
    todos = slugs()
    de_slug: dict[str, str] = {}
    for alias, fragmento in ALIAS.items():
        candidatos = por_fragmento(fragmento, todos)
        if len(candidatos) != 1:
            sys.exit(f"Abreviatura {alias} ('{fragmento}') não identifica um único documento: {candidatos}")
        de_slug[candidatos[0]] = alias
    for s in todos:
        fonte, paginas = ler(s)
        print(f"{de_slug.get(s, '(sem abreviatura)')} | {s}\n    {len(paginas)} p. | {fonte}")


def cmd_paginas(args: argparse.Namespace) -> None:
    slug = resolver(args.doc)
    fonte, paginas = ler(slug)
    pedidas = intervalos(args.paginas, max(paginas))
    print(f"# Fonte: {fonte} ({len(paginas)} páginas)")
    for n in pedidas:
        corpo = paginas[n].strip()
        print(f"\n=== {fonte}, p.{n} ===")
        print(corpo if corpo else "[página sem texto extraído: só figura/imagem no original]")
    transcritas = figuras(slug)
    if transcritas and any(re.search(rf"\bp\.{n}\b", transcritas) for n in pedidas):
        print(f"\n=== {fonte}: valores transcritos de figuras (do índice; não estão no texto acima) ===")
        print(transcritas)


def cmd_procurar(args: argparse.Namespace) -> None:
    termo, _ = dobrar(args.termo.strip())
    if not termo:
        sys.exit("Termo de pesquisa vazio.")
    if not args.regex:
        termo = r"\s+".join(re.escape(p) for p in termo.split())
        if not args.parcial:
            # Só no início de palavra: "prazo" apanha "prazos" mas não "omeprazole".
            termo = r"(?<!\w)" + termo
    try:
        padrao = re.compile(termo, re.I)
    except re.error as e:
        sys.exit(f"Expressão regular inválida: {e}")

    alvo = [resolver(args.doc)] if args.doc else slugs()
    resumo: list[tuple[str, str, dict]] = []
    por_doc: list[list[str]] = []
    total = 0
    for slug in alvo:
        fonte, paginas = ler(slug)
        blocos: dict = dict(paginas)
        transcritas = figuras(slug)
        if transcritas:
            blocos[FIGURAS] = transcritas
        contagem: dict = {}
        trechos: list[str] = []
        for n, corpo in blocos.items():
            dobrado, origem = dobrar(corpo)
            for m in padrao.finditer(dobrado):
                if m.end() == m.start():
                    continue
                contagem[n] = contagem.get(n, 0) + 1
                total += 1
                if contagem[n] == 1 and len(trechos) < args.max:  # um excerto por página
                    a = origem[m.start()]
                    b = origem[m.end() - 1] + 1
                    ini, fim = max(0, a - args.contexto), min(len(corpo), b + args.contexto)
                    trecho = corpo[ini:a] + "«" + corpo[a:b] + "»" + corpo[b:fim]
                    trecho = re.sub(r"\s+", " ", trecho).strip()
                    onde = "valores transcritos de figuras, no índice" if n == FIGURAS else f"p.{n}"
                    trechos.append(f"[{fonte}, {onde}] …{trecho}…")
        if contagem:
            resumo.append((slug, fonte, contagem))
            por_doc.append(trechos)

    if not total:
        print(f"Sem ocorrências de '{args.termo}'. Experimentar sinónimos, a sigla, o termo em "
              f"inglês/espanhol (parte das fontes não está em português) ou --parcial.")
        return

    # Excertos repartidos pelos documentos (um de cada, à vez), para que um documento com
    # muitas ocorrências não esconda os restantes.
    excertos: list[str] = []
    ronda = 0
    while len(excertos) < args.max and any(ronda < len(t) for t in por_doc):
        for trechos in por_doc:
            if ronda < len(trechos) and len(excertos) < args.max:
                excertos.append(trechos[ronda])
        ronda += 1

    print(f"{total} ocorrência(s) em {len(resumo)} documento(s)\n")
    print("## Páginas com ocorrências")
    for slug, fonte, contagem in sorted(resumo, key=lambda r: -sum(r[2].values())):
        print(f"- {slug}\n    {fonte} | p. {lista_paginas(contagem)}")
    if excertos:
        print(f"\n## Excertos ({len(excertos)}; um por página, repartidos pelos documentos)")
        for e in excertos:
            print(e)


def main() -> None:
    for fluxo in (sys.stdout, sys.stderr):
        fluxo.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="comando", required=True)

    sub.add_parser("docs", help="lista os documentos").set_defaults(func=cmd_docs)

    p = sub.add_parser("paginas", help="mostra o texto de páginas de um documento")
    p.add_argument("doc")
    p.add_argument("paginas")
    p.set_defaults(func=cmd_paginas)

    s = sub.add_parser("procurar", help="procura um termo nos textos")
    s.add_argument("termo")
    s.add_argument("--doc", help="limitar a um documento")
    s.add_argument("--max", type=int, default=20, help="n.º máximo de excertos (por omissão 20; 0 = só páginas)")
    s.add_argument("--contexto", type=int, default=140, help="caracteres de contexto de cada lado")
    s.add_argument("--parcial", action="store_true",
                   help="apanhar o termo também a meio de uma palavra (útil em tabelas com palavras coladas)")
    s.add_argument("--regex", action="store_true", help="tratar o termo como expressão regular")
    s.set_defaults(func=cmd_procurar)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
