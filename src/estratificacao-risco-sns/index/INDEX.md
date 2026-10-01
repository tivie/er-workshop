# INDEX — Índice global da base de conhecimento (Estratificação da população pelo Risco)

> **Nota (cópia incluída na skill).** Este índice foi escrito para o repositório de origem.
> Na skill existem apenas `index/INDEX.md`, `index/<slug>.md`, `index/_text/<slug>.txt` e
> `scripts/consultar.py` (que aceita as abreviaturas usadas abaixo — CN4, BI, REL-SINT… — em
> vez do slug). **Não existem** os PDF de `docs/`, as imagens de página
> (`index/_text/<slug>/pN.png`), `index/_logs/` nem `tools/`: onde o texto abaixo disser
> "no PDF" ou "confirmar no PDF", isso só pode ser feito pelo utilizador, no documento original.

Ponto de entrada para agentes. **Não é uma fonte**: serve para saber *onde* está a informação.
Fluxo: (1) escolher o documento na tabela; (2) abrir `index/<slug>.md` e localizar a página;
(3) ler a página em `index/_text/<slug>.txt` (marcadores `=== PÁGINA N ===`, numeração física
do PDF) ou no PDF; (4) citar como `<ficheiro>.pdf, p.N`.
Índices gerados em 2026-09-28 por `claude-opus-4-8` (ver `tools/indexar.sh`; registos com o modelo usado em `index/_logs/`).

## Documentos

| Índice (`index/…`) | Fonte (`docs/…`) | Tipo · entidade · data | Pág. | Língua | Quando usar |
|---|---|---|---|---|---|
| `despacho-n-o-12986-2023.md` | Despacho n.º 12986-2023.pdf | Despacho · Secretário de Estado da Saúde · 2023-12-07 (DR 2.ª série, 2023-12-19) | 8 | pt | Base legal do programa: finalidades da ER no SNS, equipa de projeto, pilares estratégicos, responsabilidades ACSS/SPMS, **Anexo I com a tabela de GRA e pesos relativos** |
| `circular-normativa-4-estratificacao-pelo-risco.md` | Circular-Normativa_4_Estratificacao-pelo-risco.pdf | Circular normativa · ACSS · 2024-02-15 | 10 | pt | Procedimento de ER para as ULS: definição de ER, GRA, peso relativo, pirâmide de Kaiser (distribuição da população, dados 2019), fórmula do IDRA, 4 pilares, RILER/ILER, codificação |
| `circular-normativa-12-2024-registo-diagnosticos-consultas-e-urgencias.md` | Circular-normativa-12_2024_Registo-diagnosticos-consultas-e-urgencias.pdf | Circular normativa · ACSS · 2024-05-27 | 6 | pt | Regras de registo de códigos de diagnóstico (ICD-10-CM) em consultas externas e urgências: campos a registar, prazos SClínico, definições de consulta/teleconsulta |
| `estrategia-para-a-estratificacao-da-pop-pelo-risco-acss.md` | ESTRATÉGIA PARA A ESTRATIFICAÇÃO da pop pelo risco ACSS.pdf | Estratégia · ACSS · 2022-01-03 | 21 | pt | Racional e enquadramento (PRR, JADECARE), conceito de ER e ajustamento pelo risco, SWOT, 4 objetivos, comparação ACG/CRG/ICU, plano a 3 anos, monitorização PDSA |
| `acss-2025-relatorio-sintese-utilizacao-dos-instrumentos-de-er-no-sns-2025.md` | ACSS 2025 Relatorio Sintese - Utilizacao dos instrumentos de ER no SNS 2025.pdf | Relatório síntese · ACSS · 2025-12-23 | 14 | pt | Dashboards do BI-ER com dados de 2024: **pirâmide de Kaiser nacional com percentis (P95, P80–P95, P0–P80, baixo = NA), utentes, custo médio e pesos relativos mín./máx. por nível (p.11, figura, atualização 2025-10-16)**; 5% do muito alto ≈ 21% dos custos dos níveis moderado a muito alto (p.12); 176 GRA; top 10 GRA; contactos e custos por nível. Figuras são imagens: ler no PDF |
| `acss-2025-relatorio-projeto-operacionalizacao-da-er-no-sns-sintese-final.md` | ACSS 2025 Relatorio Projeto Operacionalizacao da ER no SNS - Sintese Final.pdf | Relatório de projeto (síntese final) · ACSS · 2025-12-15 | 32 | pt | Balanço do projeto de operacionalização da ER: regra "muito alto 5%, alto ~15%, moderado ~80% da população com risco" (p.8); BI-ER em produção nas 39 ULS desde 2024-10-31 (p.17); pirâmide de Kaiser nacional 2024 com % no total da população (1,57 / 5,83 / 29,31 / 63,29; extração abril 2025, p.18, figura) |
| `adjusted-clinical-groups-acg.md` | Adjusted Clinical Groups (ACG).pdf | Relatório/estudo · ACSS-DPS · 2023-09 / 2024-03 | 33 | pt | **Metodologia ACG/GRA em detalhe** (ADG, CADG, EDC, MEDC, RUB/NUR, passos do algoritmo) e aplicação a 8 ULS em 2018/2019: custos, multimorbilidade, polifarmácia, pirâmide de Kaiser, IDRA |
| `manual-bi-er.md` | manual_BI_ER.pdf | Manual · SPMS · v1.6, 2026-08 | 26 | pt | Ferramenta BI-ER: fontes de dados e custos, agrupamento, perfis de acesso, dashboards, análises ad-hoc, filtros e exportação |
| `2024-modelo-aipd-acss.md` | 2024_Modelo-AIPD-ACSS.pdf | Modelo/template · ACSS · data não indicada | 24 | pt | Estrutura de uma AIPD (secções I–XI): critérios CNPD e Grupo do Art. 29, licitude, categorias de dados, matriz de risco, parecer do EPD. Documento genérico, não específico da ER |
| `estratificacao-da-populacao-pelo-risco-em-portugal-desafios-e-perspectivas.md` | Estratificação da população pelo risco em portugal desafios e perspectivas.pdf | Artigo (revista "GH – Gestão") · autores da ACSS/SPMS · refere 2024 | 4 | pt | Visão de gestão: mudança de paradigma, papel da ACSS, seleção/aquisição do ACG, ER vs GDH, perspetivas 2024. PDF digitalizado; texto transcrito a partir das imagens de página e validado (imagens em `index/_text/<slug>/pN.png`) |
| `sns-930-mil-dos-portugueses-mais-doentes-somam-41-dos-gastos-saude-publico.md` | SNS_ 930 mil dos portugueses mais doentes somam 41_ dos gastos _ Saúde _ PÚBLICO.pdf | Artigo de imprensa (PÚBLICO, Ana Maia) · declarações da ACSS · data não indicada (refere dados de 2024) | 3 | pt | Cobertura jornalística com números da ACSS: 928 mil utentes (≈9%) de risco alto/muito alto = 41% dos gastos; distribuição e custo médio por nível de risco (2024); total de 8,5 mil M€; peso relativo (8,8 no muito alto); meta de 25% do financiamento até 2029; exemplos de uso e indicador socioeconómico futuro. Fonte secundária/divulgação |
| `who-euro-2018-3032-42790-59709-eng.md` | WHO-EURO-2018-3032-42790-59709-eng.pdf | "Good practice brief" · OMS/Europa · 2018 | 6 | en | Caso espanhol: "Adjusted Morbidity Groups" (AMG), usos regionais (gestão de casos, pagamento per capita, planeamento), lições aprendidas |
| `integrated-care-models-overview.md` | Integrated-care-models-overview.pdf | Documento de trabalho · OMS/Europa · 2016-10 | 42 | en | Conceitos e taxonomias de "integrated care", modelos individuais/por grupo/populacionais (inclui Kaiser Permanente), fatores facilitadores e barreiras |
| `who-2016-framework-on-integrated-people-centred-health-services-a69-39.md` | WHO 2016 Framework on integrated people-centred health services (A69-39).pdf | Relatório do Secretariado à 69.ª Assembleia Mundial da Saúde (doc. A69/39) · OMS · 2016-04-15 (aprovado pela WHA69.24) | 12 | en | **Recomendação da OMS**: "population risk stratification" como opção de política da estratégia 3 ("Reorienting the model of care", p.7); as 5 estratégias do "Framework on integrated, people-centred health services" |
| `who-euro-2016-european-framework-for-action-on-integrated-health-services-delivery-overview.md` | WHO-EURO 2016 European Framework for Action on Integrated Health Services Delivery - overview.pdf | Apresentação-resumo (consulta final, Copenhaga, 2016-05-02/03) · OMS/Europa · 2016 | 21 | en | Domínios e estratégias do Framework for Action: "Stratifying health needs and risks" no domínio "People / Identifying health needs" (p.7). Pouco texto por página (várias só com figuras) |
| `who-euro-2023-7497-47264-69316-eng.md` | WHO-EURO-2023-7497-47264-69316-eng.pdf | Policy paper ("Primary health care policy paper series") · OMS/Europa · 2023-06-07 | 61 | en | Gestão da saúde populacional ("population health management") nos CSP: definição, ciclo (segmentação, estratificação de risco, intervenções dirigidas), 12 exemplos de países, 16 ações de política; passar do "one-size-fits-all" para intervenções adaptadas |
| `planning-for-the-future-of-population-health-the-johns-hopkins-medicine-experience.md` | Planning for the Future of Population Health The Johns Hopkins Medicine Experience.pdf | Artigo · AJMC 2023;29(7) · Berkowitz | 6 | en | Experiência organizacional da Johns Hopkins Medicine ("Office of Population Health"): estrutura híbrida, prioridades, plano a 3 anos |
| `johns-hopkins-acg-system-v13-0-user-documentation-2022.md` | Johns Hopkins ACG System v13.0 User Documentation (2022).pdf | Manual · Johns Hopkins University · 2022-06 | 689 | en | **Fonte primária da metodologia ACG (versão em uso em Portugal)**: definições dos outputs por utente ("ACG Concurrent Risk" = peso relativo do GRA, "Predicted Total Cost Risk", "Probability IP Hospitalization", RUB, PNG, "Total Cost Risk Level"), modelos de risco e de hospitalização, aplicações, listas de códigos. Páginas 365–689 são apêndices/tabelas |
| `johns-hopkins-acg-system-v13-0-technical-reference-guide-excerpt-2022.md` | Johns Hopkins ACG System v13.0 Technical Reference Guide excerpt (2022).pdf | Manual (excerto) · Johns Hopkins University · 2022-06 | 42 | en | Capítulo 1 "Diagnosis-based Markers": ADG, CADG, MAC, árvores de decisão ACG, exemplos clínicos, RUB, **tabela completa de categorias ACG com "Reference ACG Concurrent Risk" e RUB (p.31–36)**, "ACG Concurrent Risk" (p.37) |
| `weiner-1996-risk-adjusted-medicare-capitation-rates-using-ambulatory-and-inpatient-diagnoses-hcfr.md` | Weiner 1996 Risk-Adjusted Medicare Capitation Rates Using Ambulatory and Inpatient Diagnoses (HCFR).pdf | Artigo · Health Care Financing Review (CMS) 17(3) · 1996 | 23 | en | Modelos JHU (ADG/ACG) para capitação Medicare ajustada ao risco; "~100 organizações (sobretudo HMO) usam ACG" em 1996 (p.3) |
| `adams-2002-adjusted-clinical-groups-predictive-accuracy-for-medicaid-enrollees-in-three-states-hcfr.md` | Adams 2002 Adjusted Clinical Groups Predictive Accuracy for Medicaid Enrollees in Three States (HCFR).pdf | Artigo · HCFR (CMS) 24(1) · 2002 | 19 | en | Exatidão preditiva do ACG no Medicaid (Georgia, Mississippi, Califórnia); **Maryland e Minnesota usam ACG no Medicaid** (p.1); adaptação de Maryland (p.14, p.16) |
| `pope-2004-risk-adjustment-of-medicare-capitation-payments-using-the-cms-hcc-model-hcfr.md` | Pope 2004 Risk Adjustment of Medicare Capitation Payments Using the CMS-HCC Model (HCFR).pdf | Artigo · HCFR (CMS) 25(4) · 2004 | 23 | en | Modelo CMS-HCC do Medicare Advantage; **a CMS avaliou o ACG, CDPS, CRG e DCG/HCC e escolheu o HCC** (p.2) |
| `gifford-2004-health-based-capitation-risk-adjustment-in-minnesota-public-health-care-programs-hcfr.md` | Gifford 2004 Health-Based Capitation Risk Adjustment in Minnesota Public Health Care Programs (HCFR).pdf | Artigo · HCFR (CMS) 26(2) · 2004-05 | 21 | en | **Minnesota: ACG na capitação dos programas públicos (PMAP etc.) desde 2000-01-01** (p.1, p.4); seleção do ACG, pesos concorrentes (p.7), lições de implementação |
| `weir-2008-case-selection-for-a-medicaid-chronic-care-management-program-vermont-hcfr.md` | Weir 2008 Case Selection for a Medicaid Chronic Care Management Program - Vermont (HCFR).pdf | Artigo · HCFR (CMS) 30(1) · 2008 | 14 | en | Vermont Medicaid: comparação CDPS / DCG / ACG-PM para selecionar doentes crónicos para gestão de cuidados; ACG-PM com melhor desempenho global (p.1); "todos em uso num ou mais Estados" (p.3) |
| `anell-2018-does-risk-adjusted-payment-influence-primary-care-providers-decision-on-where-to-set-up-practices-sweden-bmc-hsr.md` | Anell 2018 Does risk-adjusted payment influence primary care providers decision on where to set up practices - Sweden (BMC HSR).pdf | Artigo · BMC Health Services Research 18:179 · 2018 | 12 | en | Suécia: capitação ajustada por CNI e ACG; **Tabela 1 com os "county councils" que usam ACG (11 em 2013)** (p.5, p.7) |
| `isaksson-2016-free-establishment-of-primary-health-care-providers-effects-on-geographical-equity-sweden-bmc-hsr.md` | Isaksson 2016 Free establishment of primary health care providers effects on geographical equity - Sweden (BMC HSR).pdf | Artigo · BMC HSR 16:28 · 2016 | 10 | en | Suécia: reforma de livre estabelecimento; "10 dos 21 condados" usam o índice ACG no reembolso em 2013 (p.5) |
| `halling-2006-validating-the-johns-hopkins-acg-case-mix-system-of-the-elderly-in-swedish-primary-health-care-bmc-public-health.md` | Halling 2006 Validating the Johns Hopkins ACG Case-Mix System of the elderly in Swedish primary health care (BMC Public Health).pdf | Artigo · BMC Public Health · 2006 | 7 | en | Validação do ACG/RUB em idosos suecos (n=1402, Karlskrona) com polifarmácia como proxy de custos (p.1, p.4–5) |
| `orueta-2013-predictive-risk-modelling-in-the-spanish-population-basque-country-bmc-hsr.md` | Orueta 2013 Predictive risk modelling in the Spanish population - Basque Country (BMC HSR).pdf | Artigo · BMC HSR 13:269 · 2013 | 9 | en | País Basco (Osakidetza): ACG-PM vs DCG-HCC vs CRG em toda a população >14 anos (n=1 964 337) (p.1–3); estratégia de cronicidade 2010 (p.1) |
| `shadmi-2011-assessing-socioeconomic-health-care-utilization-inequity-in-israel-clalit-acg-bmc-public-health.md` | Shadmi 2011 Assessing socioeconomic health care utilization inequity in Israel - Clalit ACG (BMC Public Health).pdf | Artigo · BMC Public Health 11:609 · 2011 | 8 | en | Israel: Clalit (3,9 M inscritos) usa ACG para ajustar a morbilidade em análises de equidade; amostra ~270 000 adultos (p.1–3) |
| `santelices-2014-grupos-clinicos-ajustados-como-herramienta-de-ajuste-de-riesgo-chile-rev-med-chile.md` | Santelices 2014 Grupos clinicos ajustados como herramienta de ajuste de riesgo - Chile (Rev Med Chile).pdf | Artigo · Rev Med Chile 142 · 2014 | 8 | es | Chile: piloto do ACG em 16 centros de cuidados primários; R² 0,26 vs 0,05 idade/sexo (p.1, p.6); afetação de recursos |
| `santelices-2016-clasificacion-segun-nivel-de-morbilidad-con-acg-chile-rev-med-chile.md` | Santelices 2016 Clasificacion segun nivel de morbilidad con ACG - Chile (Rev Med Chile).pdf | Artigo · Rev Med Chile 144 · 2016 | 7 | es | Chile: ACG aplicado a 1,88 M doentes de 64 centros em 22 comunas; diabetes, HTA, insuficiência cardíaca; variabilidade entre centros (p.2–5) |
| `chang-weiner-2010-application-of-the-johns-hopkins-acg-case-mix-system-in-taiwan-bmc-medicine.md` | Chang Weiner 2010 Application of the Johns Hopkins ACG case-mix system in Taiwan (BMC Medicine).pdf | Artigo · BMC Medicine 8:7 · 2010 | 13 | en | Taiwan: ACG aplicado a "claims" do seguro nacional (amostra 1 %, ~200 000) (p.2–3); desempenho comparável a outros países |
| `hosar-2024-validity-of-the-johns-hopkins-acg-system-on-the-utilisation-of-healthcare-services-in-norway-bmc-hsr.md` | Hosar 2024 Validity of the Johns Hopkins ACG system on the utilisation of healthcare services in Norway (BMC HSR).pdf | Artigo · BMC HSR 24:1279 · 2024 | 14 | en | Noruega: validade de cinco "ACG risk scores" em 168 285 adultos de 4 municípios (p.1–2, p.4) |

Abreviaturas de documento usadas abaixo: **DESP** = despacho; **CN4** = circular 4; **CN12** = circular 12;
**EST** = estratégia; **ACG** = relatório ACG; **BI** = manual BI-ER; **AIPD** = modelo AIPD;
**ART** = artigo "desafios e perspetivas"; **WHO-ES** = brief OMS Espanha; **ICM-WHO** = integrated care;
**REL-SINT** = Relatório Síntese ACSS 2025 (utilização dos instrumentos de ER); **REL-PROJ** = Relatório do projeto de operacionalização da ER, síntese final (ACSS, 2025) (ambos adicionados em 2026-10-01);
**WHO-IPCHS** = Framework on integrated, people-centred health services (A69/39, 2016); **WHO-FFA** = overview do European Framework for Action (OMS/Europa, 2016); **WHO-PHM** = policy paper OMS/Europa 2023 sobre "population health management" (os três adicionados em 2026-09-30);
**JHM** = artigo Johns Hopkins; **JH-UD** = documentação do utilizador ACG v13.0; **JH-TR** = excerto do guia técnico ACG v13.0;
**PUB** = artigo do PÚBLICO (930 mil / 41% dos gastos).
Literatura internacional sobre uso do ACG (adicionada em 2026-09-29): **WEI96** = Weiner 1996; **ADA02** = Adams 2002; **POP04** = Pope 2004;
**GIF04** = Gifford 2004; **WER08** = Weir 2008; **ANE18** = Anell 2018; **ISA16** = Isaksson 2016; **HAL06** = Halling 2006; **ORU13** = Orueta 2013;
**SHA11** = Shadmi 2011; **SAN14/SAN16** = Santelices 2014/2016; **CHA10** = Chang & Weiner 2010; **HOS24** = Hosar 2024.

## Mapa de conceitos transversais → onde ir buscar

Páginas retiradas das secções "Conceitos"/"Factos citáveis" dos índices individuais; confirmar sempre no texto.

**Estratificação pelo risco — definição e finalidades**
- Definição de ER: CN4 p.2; DESP p.1–3; EST p.7; ART p.2–3.
- Finalidades/objetivos da ER no SNS (governação clínica, financiamento, alocação de recursos, avaliação de desempenho): EST (4 objetivos); DESP p.2; ART p.1.
- 4 pilares estratégicos de intervenção: CN4 p.1–2 (e p.5–8, um por um); DESP p.2.
- Equipa de projeto e responsabilidades ACSS/SPMS: DESP p.2–3; CN4 p.9 (RILER).
- ER vs GDH (Grupos de Diagnósticos Homogéneos): CN4 p.3–4; ART p.2–4; BI p.2, p.5; DESP p.1 (GDH desde 1989).
- Abordagem populacional / mudança de paradigma: ART p.1; EST (racional); ICM-WHO (modelos populacionais).
- Recomendação da OMS sobre estratificação pelo risco: WHO-IPCHS p.7 ("population risk stratification" como opção de política); WHO-FFA p.7 ("Stratifying health needs and risks"); WHO-PHM p.17 (ciclo de 5 passos), p.25 (definição de "risk stratification"; "essential for PHC practices to be proactive"), p.26 e p.39 (menção ao ACG da Johns Hopkins, País Basco); WHO-ES p.1, p.5 (vantagens: de cuidados centrados na doença para centrados no doente, previsão de risco, benchmarking, requisito de registos informatizados).

**Metodologia ACG / GRA (Johns Hopkins)**
- ACG = GRA ("Adjusted Clinical Groups" / Grupos de Risco Ajustado): ACG p.2, p.9; EST p.3, 6, 14, 16; BI p.2, p.9; ART p.3–4; CN4 p.2.
- ADG / CADG / EDC / MEDC (componentes do algoritmo): ACG p.2, p.10–13.
- RUB / NUR ("Resource Utilization Bands" / Níveis de Utilização de Recursos): ACG p.2–3, p.15–16; BI p.2, p.9; JH-UD p.140, p.365; JH-TR p.30–31.
- PNG / GN ("Patient Need Groups" / Grupos de Necessidades, 11 grupos em 6 segmentos) e "Care Modifiers": ACG p.16; JH-UD p.253–260, p.390.
- Peso relativo / coeficiente de ponderação do GRA: CN4 p.4; DESP p.3, p.8 (Anexo I); ART p.3; ACG p.14–15 ("Local Concurrent Risk"), p.31; PUB p.2 (peso relativo médio 8,8 no risco muito alto vs 1 no utente padrão, dados 2024 — fonte secundária).
- Valor de risco por utente na terminologia Johns Hopkins: "risk score" (genérico) JH-UD p.72; "ACG Concurrent Risk" (= peso relativo do GRA; mesmo valor para todos os utentes do mesmo ACG; média 1,0; variantes "Reference"/"Local", "unscaled"/"rescaled") JH-UD p.234–235, JH-TR p.37; "Concurrent Risk (regression-based)" JH-UD p.236; abordagem estatística (células atuariais, regressão) JH-UD p.233.
- Risco preditivo/prospetivo por utente: "Predicted Total/Pharmacy Cost Risk" JH-UD p.239–240; "Rank/Reference Probability High Total Cost" JH-UD p.240; "Probability IP Hospitalization Score" (12 e 6 meses; campos "Prob. Internamento" do BI-ER) JH-UD p.249, BI p.21; modelos de hospitalização JH-UD p.246–252.
- Níveis de risco por quantis ("Total Cost Risk Level", quantis por defeito 60 e 90): JH-UD p.75, p.257; comparar com os percentis 80/95 do peso relativo usados no BI-ER (BI p.19).
- Tabela completa de categorias ACG com pesos de referência e RUB: JH-TR p.31–36; JH-UD p.141–146; ADG/CADG/MAC e árvores de decisão: JH-TR p.4–22.
- Tabela nacional de GRA com pesos (Anexo I): DESP p.3–8.
- IDRA / ICM (Índice de Risco Ajustado / índice de casemix): CN4 p.5 (fórmula); ACG p.31; BI p.19; ART p.4.
- Casemix e carga de doença ("burden of disease"): CN4 p.2–5; ACG p.6–7; DESP p.1; EST p.10–11; ART p.2–4.
- Pirâmide de Kaiser / distribuição da população por nível de risco: CN4 p.4 (63 % baixo risco; 37 % complexa: 4 % muito alto, 16 % alto, 80 % moderado, dados 2019); ACG p.29–32; EST p.7; BI p.19 (regra de distribuição pelos níveis); ART p.4 (Figura 4); **dados 2024 (fontes oficiais, valores em figuras)**: REL-SINT p.11 (Figura 10, atualização 2025-10-16) e REL-PROJ p.18 (Figura 11, extração de abril de 2025) — as duas figuras dão valores diferentes; **dados 2024 (fonte secundária)**: PUB p.1 (241 mil muito alto, 687 mil alto, 3,9 M moderado, 5,5 M baixo; "os 41% de população entre risco muito alto e moderado passaram a 46%").
- Multimorbilidade e polifarmácia (resultados 8 ULS 2018/2019): ACG p.21–23.
- Comparação de instrumentos ACG vs CRG vs ICU e seleção por concurso: EST p.3, 6, 14–16; ACG p.2, p.7–8; ART p.2–4; REL-PROJ p.11 (concurso público internacional e adjudicação do ACG; a base não tem o valor nem a duração do contrato).
- Instrumento espanhol alternativo AMG ("Adjusted Morbidity Groups"): WHO-ES p.1–2 (definição), p.5 (usos: gestão de casos, pagamento per capita, planeamento).

**Dados que alimentam o modelo / registo clínico**
- Fontes de dados (CSP, BDMH, SIM@SNS, medicamentos): ACG p.2–3; BI p.2, p.5–6; CN4 p.3.
- Codificação ICD-10-CM/PCS: CN4 p.9; CN12 p.2; ACG p.2, p.10; BI p.2, p.6.
- ICPC-2 / ICPC-2E (cuidados primários): CN4 p.9; ACG p.2, p.10; BI p.2, p.6.
- Registo de diagnósticos em consultas externas e urgências (campos, prazos, SClínico): CN12 p.2–4; conceitos de consulta/teleconsulta: CN12 p.5–6.
- Auditoria e prazos de codificação de internamento: CN4 p.9.

**Aplicações**
- Financiamento por capitação ajustada pelo risco: CN4 p.7; ART p.4; EST (objetivo 2); WHO-ES p.5 (Catalunha/Madrid); PUB p.2 (capitação ajustada por ULS; meta das Grandes Opções: 25 % do financiamento associado à ER até 2029 — fonte secundária).
- Planeamento de recursos, instalações, equipamentos: CN4 p.5–6.
- Processos assistenciais, gestão de caso, doença crónica: CN4 p.6–7; WHO-ES p.5; ICM-WHO (modelos por grupo/doença).
- Avaliação do desempenho: CN4 p.7–8; EST (objetivo 4).
- Modelos de cuidados integrados (taxonomias, Kaiser Permanente, redes clínicas): ICM-WHO p.7, p.24–26 e restante.
- Organização de "population health" numa instituição (JHM, OPH, PHSO, "guiding stars"): JHM p.1–4.

**Governação, rede e ferramentas**
- RILER e ILER (rede/interlocutor local), prazo 23 de fevereiro e endereço de contacto: CN4 p.9; BI p.2, p.10.
- Ferramenta BI-ER: perfis e gestão de utilizadores (BI p.10 e secção respetiva), dashboards (BI p.16–17), análises ad-hoc (BI p.16, p.20), atualização/filtros/exportação (BI, secções finais).
- Formação de profissionais nas entidades piloto (~200, ENSP/SPMS): ART p.2.
- PRR e JADECARE (enquadramento europeu/financiamento): EST p.3, 6, 8, 17; ART p.1, p.4.
- Plano de implementação a 3 anos e monitorização PDSA: EST p.17–19.

**Proteção de dados**
- Necessidade de AIPD (critérios CNPD; Grupo do Art. 29): AIPD p.3–4.
- Estrutura da AIPD, licitude, categorias de dados, ciclo de vida, matriz de risco, parecer do EPD: AIPD p.7–24 (ver índice).
- Notificação de violação de dados em 72 h: AIPD p.2.

**Entidades**
- ACSS: CN4 p.1; EST p.3, 6, 21; ACG p.2; ART p.1–2, 4; BI p.2, 5.
- SPMS: DESP p.3; ACG p.3, p.18; BI p.2, p.5; ART p.2, p.4.
- DE-SNS: BI p.2, p.5; ART p.2.
- ISPUP (avaliação/estudo): ACG p.2, p.18, p.32; ART p.2.
- ULS (destinatárias): CN4 p.1; EST p.6, 9, 18; ACG p.3, p.17; BI p.2, p.6; ART p.1–4.

**Utilização do ACG nos EUA e noutros países**
- Origem nos EUA e uso sobretudo para financiamento: EST p.6, p.11; BI p.5; ACG p.6, p.9.
- Medicaid (capitação ajustada ao risco): Maryland e Minnesota usam ACG, ADA02 p.1 (adaptação de Maryland p.14, p.16); Minnesota desde 2000-01-01, GIF04 p.1, p.4, p.7; Vermont, seleção para gestão de doença com ACG-PM, WER08 p.1–3.
- Medicare: modelos JHU baseados em ACG para capitação, WEI96 (≈100 organizações a usar ACG em 1996, p.3); a CMS avaliou vários modelos, incluindo o ACG, e escolheu o DCG/HCC, POP04 p.2 (modelo CMS-HCC implementado em 2004, POP04 p.1); réplica do CMS-HCC no software, JH-UD p.601.
- Populações de referência americanas do software (comercial, Medicare, TANF/Medicaid): JH-UD p.71, p.230; aplicações financeiras (capitação, tarifas, "underwriting"): JH-UD p.346–351.
- Suécia (capitação dos centros de cuidados primários por CNI + ACG): ANE18 p.5, p.7 (Tabela 1, 11 condados em 2013); ISA16 p.5 (10 condados); validação em idosos, HAL06 p.1, p.4–5.
- Espanha / País Basco (estratificação de toda a população com ACG-PM desde 2010): ORU13 p.1–3; caso espanhol com AMG (não ACG): WHO-ES.
- Israel (Clalit): SHA11 p.1–3. Chile (cuidados primários, afetação de recursos): SAN14 p.1–3, p.6; SAN16 p.2–5. Taiwan (seguro nacional): CHA10 p.2–3. Noruega (validação): HOS24 p.1–2, p.4.

## Perguntas frequentes → documento

- "O que diz a lei / quem mandatou a ER?" → DESP (p.1–3); depois CN4.
- "Como se calcula o IDRA / que peso tem um GRA?" → CN4 p.5 + DESP Anexo I.
- "Que percentagem da população está em cada nível de risco?" → CN4 p.4 (dados 2019); ACG p.29–32; dados 2024: REL-SINT p.11–12 e REL-PROJ p.18 (figuras).
- "Como se definem os níveis da pirâmide de Kaiser (percentis ou limiares absolutos)?" → BI p.19 (baixo = GN 1–3 / NUR 0–2; moderado a muito alto = percentis 80 e 95 dos pesos relativos); confirmado em REL-SINT p.11 (coluna "Percentil" e pesos mín./máx. por nível) e REL-PROJ p.8, p.18.
- "Como funciona o algoritmo ACG (ADG, EDC, RUB)?" → ACG p.9–16; em detalhe (fonte Johns Hopkins): JH-TR p.4–37; JH-UD p.114–146.
- "Como se chama / como se calcula o valor de risco de cada utente?" → peso relativo do GRA = "ACG Concurrent Risk": JH-UD p.234–235; JH-TR p.37; CN4 p.4; ACG p.15, p.31. Valores preditivos (custo futuro, probabilidade de internamento): JH-UD p.239–240, p.249.
- "Como registar diagnósticos na consulta/urgência?" → CN12.
- "Que dados e custos entram no BI-ER e como usar a ferramenta?" → BI.
- "Porque foi escolhido o ACG e não o CRG/ICU?" → EST p.14–16; ACG p.7–8; ART p.3–4.
- "Que obrigações de proteção de dados existem?" → AIPD (modelo genérico); esta base não contém uma AIPD específica da ER.
- "Que experiências internacionais comparáveis existem?" → WHO-ES (Espanha/AMG); JHM (EUA); ICM-WHO (modelos).
- "O que recomenda a OMS sobre estratificação pelo risco e que vantagens aponta?" → WHO-IPCHS p.7; WHO-FFA p.7; WHO-PHM; WHO-ES p.1, p.5.
- "Onde é usado o ACG (Medicaid, Medicare, seguradoras, outros países)?" → secção "Utilização do ACG nos EUA e noutros países" acima; ADA02 p.1; GIF04 p.1; POP04 p.2; WEI96 p.3; ANE18 p.5, p.7; ORU13 p.1.

## Limitações conhecidas

- ART é um PDF digitalizado; o `.txt` é uma transcrição a partir das imagens de página, validada em 2026-09-28, utilizável como os restantes textos.
- AIPD: páginas 5–6 sem texto extraído (provável grelha/imagem); título e data não constam do texto.
- Índices em inglês (WHO-ES, ICM-WHO, JHM, JH-UD, JH-TR) descritos em português com termos originais entre aspas; para citação literal usar o texto em `index/_text/`.
- JH-UD (689 p.): o indexador leu na íntegra as p.1–367 e mapeou as p.365–689 (apêndices, tabelas de códigos, API) por intervalos a partir do índice interno do documento; confirmar códigos específicos no PDF. A extração de tabelas colou palavras sem espaços em JH-UD e JH-TR (valores corretos, legibilidade imperfeita). JH-TR p.16, 18, 20 e 22 são só figuras (árvores de decisão).
- Índices JH-UD e JH-TR gerados em 2026-09-28 por `claude-opus-4-8` (registos em `index/_logs/`).
- WHO-IPCHS, WHO-FFA e WHO-PHM foram descarregados em 2026-09-30 dos sítios da OMS (apps.who.int, integratedcare4people.org, iris.who.int) e indexados nesse dia por `claude-opus-4-8` (registos em `index/_logs/`). WHO-FFA é uma apresentação: várias páginas sem texto extraído (só figuras); confirmar no PDF.
- Os 14 artigos internacionais (WEI96 … HOS24) foram descarregados em 2026-09-29 de fontes em acesso aberto (CMS, BMC, SciELO) e indexados nesse dia por `claude-opus-4-8` (registos em `index/_logs/`). São artigos de investigação: descrevem utilizações e estudos, não políticas portuguesas. Artigos sem acesso aberto (Cohen 2015, Wahls 2004, Sales 2003, Sibley 2012, Reid 2002, Orueta 2013 Aten Primaria, Girwar 2022) não estão em `docs/`.
