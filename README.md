# er-workshop

Materiais do workshop sobre **Estratificação da população pelo Risco (ER)** no SNS
(CNSMP, 2026-10-01).

## O que está aqui

| Caminho | Conteúdo |
|---|---|
| `2026.10.01.CNSMP.workshop_Estratificacao_pelo_risco_sem_perguntas.pptx` | Apresentação do workshop |
| `dist/estratificacao-risco-sns.zip` | A skill empacotada, pronta a carregar no Claude |
| `src/estratificacao-risco-sns/` | O código-fonte da skill (o mesmo conteúdo do `.zip`, descompactado) |

## A skill `estratificacao-risco-sns`

É uma base de conhecimento sobre a Estratificação pelo Risco no SNS, para o Claude responder
a perguntas **a partir dos documentos de referência**, indicando sempre o documento e a
página de onde vem cada facto, e dizendo quando a base não tem a resposta.

Inclui o texto e os índices de 33 documentos: despacho e circulares normativas, estratégia e
relatórios da ACSS, documentação do sistema ACG da Johns Hopkins, documentos da OMS, manual
do BI-ER e artigos científicos sobre o uso do ACG noutros países. Não inclui os PDF
originais.

Estrutura (`src/estratificacao-risco-sns/`):

- `SKILL.md` — instruções da skill;
- `index/INDEX.md` — índice global (documentos, mapa de conceitos, perguntas frequentes);
- `index/<documento>.md` — um índice por documento;
- `index/_text/<documento>.txt` — texto de cada documento, página a página;
- `scripts/consultar.py` — lê páginas e pesquisa nos textos (precisa de Python 3.9 ou superior).

Não é uma fonte oficial: as respostas devem ser confirmadas nos documentos originais citados.

## Como instalar

Os nomes dos menus abaixo são os da interface em inglês e podem mudar com as atualizações
do Claude.

### Claude chat (claude.ai e aplicação de computador)

1. Descarregar `dist/estratificacao-risco-sns.zip` deste repositório.
2. Confirmar que a execução de código está ativa: **Settings > Capabilities** >
   **Code execution and file creation**. Nos planos Team e Enterprise, esta opção é gerida
   pelo administrador em **Organization settings > Plugins & skills**.
3. Abrir **Customize > Skills**.
4. Clicar em **+**, depois **+ Create skill** e escolher **Upload a skill**.
5. Selecionar o ficheiro `estratificacao-risco-sns.zip`.
6. Confirmar que a skill aparece na lista e está ligada.

A partir daí, basta fazer a pergunta numa conversa nova; o Claude usa a skill quando o tema
é a estratificação pelo risco.

### Claude Cowork

O Cowork usa as skills da conta Claude; não lê pastas locais.

1. Instalar a skill como no Claude chat (passos acima).
2. No Cowork, escrever `/` para ver as skills disponíveis e confirmar que
   `estratificacao-risco-sns` está na lista.

### Claude Code

Há duas formas.

**A. Pela conta Claude.** As skills ativas na conta também são carregadas no Claude Code
quando se inicia sessão com a mesma conta (requer o Claude Code v2.1.273 ou superior).
Depois de instalar a skill no Claude chat, correr `/skills` no Claude Code para confirmar
que aparece.

**B. Copiando a pasta.** Copiar `src/estratificacao-risco-sns/` para a pasta de skills:

- pessoal, disponível em todos os projetos: `~/.claude/skills/estratificacao-risco-sns/`
- só num projeto: `<projeto>/.claude/skills/estratificacao-risco-sns/`

macOS / Linux:

```bash
git clone https://github.com/tivie/er-workshop.git
mkdir -p ~/.claude/skills
cp -r er-workshop/src/estratificacao-risco-sns ~/.claude/skills/
```

Windows (PowerShell):

```powershell
git clone https://github.com/tivie/er-workshop.git
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills" | Out-Null
Copy-Item -Recurse er-workshop\src\estratificacao-risco-sns "$env:USERPROFILE\.claude\skills\"
```

O ficheiro `SKILL.md` tem de ficar diretamente dentro de
`.../skills/estratificacao-risco-sns/`. O Claude Code deteta a skill sem reiniciar; se a
pasta `skills` não existia quando a sessão começou, correr `/reload-skills`. A skill pode
ser chamada diretamente com `/estratificacao-risco-sns`, ou é usada automaticamente quando
a pergunta é sobre o tema.

## Exemplos de perguntas

A skill dá o melhor de si em perguntas que obrigam a cruzar documentos, a distinguir o que
as fontes dizem do que se pode inferir, ou a transformar um problema da ULS num plano de
análise. Alguns exemplos:

**IDRA e financiamento**

- O que é o efeito de diluição no cálculo do financiamento pelo IDRA? Como funciona?
- Se a ULS investir em prevenção e o IDRA descer, o financiamento desce também? O que
  dizem as fontes sobre isso e o que está previsto para o compensar?
- De que formas pode o IDRA de uma ULS subir sem que a saúde da população piore, e descer
  sem que ela melhore?
- O IDRA da minha ULS desceu de 2024 para 2025 e o Conselho de Administração quer
  apresentá-lo como ganho em saúde. Que leituras alternativas tenho de excluir primeiro?

**Pirâmide de Kaiser, GRA, GN e NUR**

- Se a população ficar mais saudável, o número de utentes em risco muito alto diminui?
  Como se definem os cortes de cada nível e o que muda de um ano para o outro?
- Os relatórios da ACSS dão números diferentes para a pirâmide de Kaiser de 2024. Que
  versões existem, de onde vem cada uma e em que diferem?
- O que acontece no modelo a um utente sem diagnósticos registados ou que não usou o SNS?
  Em que GRA fica, com que peso, e que efeito tem isso na ULS?
- Qual é a diferença entre o peso relativo do GRA e a probabilidade de internamento a 12
  meses? O que mede cada um e para que decisões serve?
- Em que difere a regra portuguesa dos percentis 80 e 95 dos níveis de risco que o
  software ACG calcula por omissão?

**Usar o BI-ER para responder a um problema da ULS**

- Se quiser estudar reconciliação terapêutica, que variáveis tenho disponíveis no BI-ER e
  que limitações têm?
- Quero caracterizar os utilizadores frequentes da urgência (10 ou mais episódios num
  ano). Que separadores e campos das análises ad-hoc uso, e que utentes ficam de fora?
- Quero avaliar se um programa de gestão de caso reduziu as urgências e os internamentos.
  Que campos permitem comparar o antes e o depois, e o que é que eles não medem?
- Quero identificar idosos frágeis ou com multimorbilidade de alta complexidade para um
  programa de prevenção de quedas. Que outputs do ACG servem para isso e quais estão
  disponíveis no BI-ER?
- Que custos entram no BI-ER, com que preços são calculados e que cuidados ficam de fora?

**Registo e organização**

- Que diagnósticos alimentam a estratificação, de que sistemas vêm e em que classificação
  estão? O que se perde quando um diagnóstico não é registado na consulta externa ou na
  urgência?
- O que compete ao ILER e à equipa local segundo a circular normativa e o relatório do
  projeto, e em que áreas de trabalho se concentraram as ULS?

**Comparações e enquadramento**

- Porque escolheu Portugal o ACG e não o CRG ou o ICU? Que critérios pesaram e como foi
  feita a aquisição?
- Como usam a Suécia e o Minnesota o ACG para ajustar a capitação, e que lições de
  implementação são relevantes para o modelo das ULS?
- Que evidência há de que o ACG prevê bem os custos e a utilização fora dos EUA? Compara
  os estudos de validação que estão na base.

A skill responde com o documento e a página de cada facto e assinala o que é inferência.
Quando a base não tem a resposta (por exemplo, o valor do contrato do ACG), diz isso.

## Referências

- [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude) (Centro de Ajuda do Claude)
- [Skills no Claude Code](https://code.claude.com/docs/en/skills) (documentação do Claude Code)
