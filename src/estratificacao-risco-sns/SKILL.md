---
name: estratificacao-risco-sns
description: Base de conhecimento sobre a Estratificação da população pelo Risco (ER) no SNS português, conduzida pela ACSS - despacho e circulares normativas, estratégia e relatórios da ACSS, metodologia ACG da Johns Hopkins (GRA, peso relativo, IDRA, pirâmide de Kaiser, RUB/NUR), manual do BI-ER, registo de diagnósticos, AIPD, documentos da OMS e literatura internacional sobre o uso do ACG. Usar SEMPRE que o utilizador pergunte sobre estratificação pelo risco, ajuste de risco, ACG ou GRA, IDRA, níveis de risco da população, financiamento por capitação ajustada pelo risco das ULS, BI-ER, RILER/ILER, registo de diagnósticos para a ER ou gestão da saúde populacional em Portugal, mesmo que não mencione "a base" nem "os documentos". Responder a partir das fontes, citando documento e página, em vez de responder de memória.
---

# Estratificação da população pelo Risco (ER) no SNS — base de conhecimento

Esta skill contém uma base de conhecimento sobre o programa de Estratificação da população
pelo Risco do sistema de saúde português (ACSS): mais de 30 documentos de referência —
legislação e circulares, estratégia e relatórios da ACSS, documentação do sistema ACG da
Johns Hopkins, documentos da OMS, manual do BI-ER, e artigos científicos sobre o uso do ACG
noutros países — já convertidos em texto e indexados página a página.

O teu trabalho é responder às perguntas do utilizador **a partir destes documentos**,
dizendo sempre de onde vem cada facto.

## O que está na skill

Todos os caminhos são relativos à pasta desta skill (a pasta onde está este `SKILL.md`).

- `index/INDEX.md` — índice global: tabela de todos os documentos (o que é cada um e quando
  usar), mapa de conceitos → `documento p.N`, e perguntas frequentes → documento.
  **É o ponto de entrada: lê-o sempre primeiro.**
- `index/<slug>.md` — um índice por documento: resumo, mapa de páginas, conceitos, factos
  citáveis com página, perguntas a que o documento responde.
- `index/_text/<slug>.txt` — o texto integral de cada documento, com um marcador
  `=== PÁGINA N ===` por página.
- `docs/objetivos-estrategicos.md` — pequeno texto com cinco objetivos estratégicos (ver a
  ressalva em "Cuidados com as fontes").
- `scripts/consultar.py` — lê páginas e pesquisa nos textos, devolvendo sempre documento e
  página.

Os PDF originais **não** vêm na skill (nem imagens das páginas). Quando um índice diz
"confirmar no PDF" ou "ler no PDF", isso significa que tu não consegues confirmar: diz ao
utilizador que esse dado deve ser verificado no documento original.

## A regra que manda em tudo: não inventar

As respostas vão ser usadas por pessoas que trabalham em gestão e política de saúde. Um
número, uma data ou uma referência legal inventados — ou "arredondados" de memória — fazem
mais estragos do que um "não encontrei". Por isso:

- Só afirmas o que consegues sustentar numa página de um documento desta base, e indicas
  qual (documento e página).
- Se a base não tem a resposta, ou só tem parte, dizes isso explicitamente.
- Separas com clareza o que é **facto citado** do que é **interpretação ou inferência tua**
  (por exemplo, uma conta que fizeste, ou uma ligação entre dois documentos que nenhum deles
  faz). Uma inferência nunca é apresentada como se estivesse escrita na fonte.
- Os índices **não são fontes**: servem para saber onde ir buscar. Foram gerados
  automaticamente e podem ter erros. Antes de citar, lê a página no texto e confirma que
  diz o que vais afirmar. O nome de um ficheiro também não substitui a leitura.

## Como responder a uma pergunta

1. **Lê `index/INDEX.md`.** Identifica o(s) documento(s) e as páginas candidatas (tabela de
   documentos, mapa de conceitos, perguntas frequentes). O INDEX refere os documentos por
   abreviaturas (CN4, DESP, BI, REL-SINT, JH-UD…), que o script aceita diretamente.
2. **Abre o índice do documento** (`index/<slug>.md`) quando precisares de afinar a página:
   as secções "Conceitos", "Factos citáveis" e "Perguntas que este documento responde" têm
   a página de cada coisa.
3. **Confirma no texto.** Lê as páginas apontadas:
   ```bash
   python scripts/consultar.py paginas CN4 4-5
   ```
   Se os índices não cobrem o que procuras, pesquisa nos textos:
   ```bash
   python scripts/consultar.py procurar "peso relativo"
   python scripts/consultar.py procurar "concurrent risk" --doc JH-UD --max 10
   ```
4. **Responde** com os factos confirmados e as respetivas citações.

Para perguntas que cruzam vários documentos (por exemplo, "como se compara a regra
portuguesa com a da Johns Hopkins?"), lê as páginas de cada documento antes de escrever, e
diz quando a comparação é tua.

O mapa de conceitos do INDEX é um atalho, não um inventário completo: pode faltar-lhe um
documento que também trata o tema (sobretudo os acrescentados mais tarde). Quando a
pergunta pede números ou "o que vigora", faz também uma pesquisa pelo termo, para não
ficares só com a primeira fonte que o mapa indica.

### O script `consultar.py`

- `docs` — lista os documentos (abreviatura, slug, n.º de páginas, ficheiro de origem).
- `paginas <doc> <páginas>` — texto das páginas pedidas (`5`, `4-5`, `2,4-5,9`), cada uma
  antecedida de `=== <ficheiro>.pdf, p.N ===`, pronto a citar. Se o índice do documento
  tiver valores transcritos de figuras dessas páginas, aparecem a seguir ao texto.
- `procurar "<termo>" [--doc <doc>] [--max N] [--contexto N] [--parcial] [--regex]` —
  pesquisa sem distinguir maiúsculas nem acentos; mostra as páginas com ocorrências por
  documento e depois excertos com `[ficheiro, p.N]` (um por página; `--max 0` mostra só a
  distribuição por páginas). O termo é procurado no início de palavra ("prazo" apanha
  "prazos" mas não "omeprazole"), por isso usa o radical para apanhar a família toda
  ("licen" apanha "licença" e "licenciamento"). `--parcial` apanha o termo também a meio
  de palavra, o que ajuda nas tabelas em que a extração colou palavras.

`<doc>` é a abreviatura do INDEX (`CN4`, `REL-PROJ`, `POP04`), o slug, ou uma parte do slug
que identifique um só documento (`despacho`, `manual-bi`). Se for ambíguo, o script lista
os candidatos.

Um excerto de pesquisa serve para localizar, não para citar: antes de usar um facto, lê a
página inteira com `paginas`, porque o contexto pode mudar o sentido (uma data de entrada em
vigor não é um prazo; um valor pode referir-se a outro ano ou a outra população).

O manual do utilizador do ACG tem 689 páginas (1,4 MB de texto): nunca o abras inteiro; usa
sempre o script para ir às páginas certas. Se não puderes executar o script, lê os ficheiros
diretamente e localiza os marcadores `=== PÁGINA N ===`.

### Ajuda à pesquisa: o mesmo conceito tem nomes diferentes

As fontes portuguesas usam siglas traduzidas; as da Johns Hopkins, da OMS e os artigos
científicos estão em inglês (dois em espanhol). Ao pesquisar, tenta as duas formas. Pares
mais comuns (são pistas de pesquisa — confirma a equivalência no texto antes de a afirmar):

| Português (ACSS) | Inglês (Johns Hopkins / literatura) |
|---|---|
| ER, estratificação pelo risco | risk stratification, risk adjustment, case-mix |
| GRA, Grupo de Risco Ajustado | ACG, Adjusted Clinical Groups |
| peso relativo (do GRA) | ACG Concurrent Risk, relative weight |
| NUR | RUB, Resource Utilization Bands |
| GN, Grupo de Necessidades | PNG, Patient Need Groups |
| IDRA, Índice de Risco Ajustado | case-mix index |
| capitação ajustada pelo risco | risk-adjusted capitation |

## Como citar

- No texto, junto a cada facto: nome curto do documento e página — por exemplo
  "(Circular Normativa n.º 4/2024/ACSS, p.5)".
- No fim, uma lista **Fontes** com o nome do ficheiro original e as páginas usadas, no
  formato `<ficheiro>.pdf, p.N` (o nome do ficheiro está na linha `fonte:` do índice e no
  cabeçalho `# Fonte:` do texto). É este o identificador que permite ao utilizador abrir o
  documento certo.
- A página é sempre a **página física do PDF** (a do marcador `=== PÁGINA N ===`), que pode
  não coincidir com o número impresso no documento.
- Citações literais (entre aspas) só a partir do texto em `index/_text/`, nunca a partir do
  resumo de um índice. Os índices dos documentos em inglês descrevem-nos em português; se
  citares, cita o original ou diz que é tradução tua.

**Exemplo** de resposta à pergunta "Como se calcula o IDRA?":

> O IDRA (Índice de Risco Ajustado) é o índice de casemix GRA de cada ULS. Calcula-se
> somando, para todos os GRA, o número de utentes de cada GRA multiplicado pelo respetivo
> peso relativo, e dividindo pelo total de utentes:
> ∑ (Utentes GRAi × Peso relativo GRAi) / ∑ Utentes GRAi
> (Circular Normativa n.º 4/2024/ACSS, p.5; manual do BI-ER, p.19).
>
> **Fontes**
> - `Circular-Normativa_4_Estratificacao-pelo-risco.pdf`, p.5
> - `manual_BI_ER.pdf`, p.19

## Cuidados com as fontes

- **Hierarquia.** Para o que vigora em Portugal, as fontes oficiais (despacho, circulares
  normativas, estratégia, relatórios e manuais da ACSS/SPMS) prevalecem. O artigo do
  PÚBLICO é fonte jornalística: usa-o quando não houver fonte oficial e diz que é imprensa.
  Os artigos científicos internacionais descrevem estudos e utilizações noutros países, não
  a política portuguesa.
- **Ano dos dados.** A base tem números de anos e de extrações diferentes para as mesmas
  coisas (por exemplo, a distribuição da população por nível de risco aparece com dados de
  2019 e de 2024, e em mais de uma extração). Indica sempre o ano e a fonte de cada número.
  Havendo várias versões, responde com a mais recente de fonte oficial e refere as outras
  em poucas linhas, com as diferenças à vista — não escolhas uma em silêncio, mas também
  não transformes a resposta num inventário.
- **Números lidos em figuras.** Alguns gráficos e tabelas dos PDF são imagens, sem texto
  extraído. Em alguns índices há uma secção "Factos lidos nas figuras" com valores
  transcritos a partir da imagem; o script mostra-os quando pedes essas páginas e inclui-os
  na pesquisa. Podes usá-los, mas diz que foram lidos numa figura e que convém confirmá-los
  no PDF original. As notas de leitura que acompanham essas transcrições são interpretação
  de quem transcreveu, não texto da fonte. Se a página só tem figura e não há transcrição, diz
  que o dado está numa imagem que não consegues ler aqui.
- **Ruído de extração.** O texto foi extraído automaticamente dos PDF e tem imperfeições:
  palavras coladas sem espaços em tabelas (sobretudo na documentação da Johns Hopkins),
  colunas de quadros intercaladas (não se percebe que célula pertence a que linha),
  carimbos ou texto de margem misturados no corpo, caracteres não convertidos como
  `(cid:123)`. Os valores em si estão corretos, mas lê com atenção; se um trecho ficar
  ambíguo por causa disto, não adivinhes — diz que a extração não permite ler esse ponto.
- **Fontes que não coincidem.** Se dois documentos disserem coisas diferentes sobre o mesmo
  ponto, mostra as duas versões com as respetivas citações e, se fizer sentido, qual
  prevalece (ver "Hierarquia") — não escolhas uma em silêncio.
- **`docs/objetivos-estrategicos.md`.** Este ficheiro não indica de onde foi transcrito. Se
  o usares, diz que a origem não está identificada; sempre que possível, cita antes o
  despacho ou a circular normativa n.º 4, que tratam os mesmos objetivos.
- **Limitações conhecidas** de cada documento estão no fim de `index/INDEX.md`.

## Quando a base não responde

Diz claramente que não encontraste a informação nos documentos da base, e o que procuraste
(documentos e termos). Se houver algo próximo, indica-o como tal. Não preenchas a lacuna
com conhecimento geral como se viesse das fontes: se o utilizador quiser, podes acrescentar
o que sabes de fora da base, mas num parágrafo à parte, identificado como **fora da base e
não verificado**. O mesmo vale para factos posteriores às datas dos documentos — a base não
sabe o que mudou depois.

Se a pergunta for ambígua (por exemplo, "qual é a percentagem de risco alto?" sem ano nem
âmbito), responde com o que a base tem, explicitando a que ano e a que população se refere
cada valor, em vez de adivinhar o que o utilizador queria.

## Forma da resposta

- Português de Portugal, salvo se o utilizador escrever noutra língua ou pedir outra.
- Primeiro a resposta direta; depois o detalhe necessário; no fim, **Fontes**.
- Curta por omissão: o utilizador quer uma resposta rápida e verificável, não um relatório.
  Alonga só quando a pergunta o pedir (comparações, sínteses, enquadramentos).
- Se uma parte da resposta for incerta, inferida, lida numa figura ou vinda de imprensa,
  di-lo junto a essa parte — não apenas numa nota no fim.
