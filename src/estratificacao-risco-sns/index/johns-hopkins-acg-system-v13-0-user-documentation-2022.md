fonte: Johns Hopkins ACG System v13.0 User Documentation (2022).pdf
titulo: The Johns Hopkins ACG® System — Version 13.0 User Documentation (June 2022)
entidade: The Johns Hopkins University (Bloomberg School of Public Health, Department of Health Policy and Management; Johns Hopkins HealthCare Solutions). Editor sénior: Jonathan P. Weiner
data: Junho de 2022 (© 2022)
paginas: 689
lingua: en
tipo: manual
texto: index/_text/johns-hopkins-acg-system-v13-0-user-documentation-2022.txt

## Resumo
Documentação técnica e de utilizador do sistema ACG® ("Adjusted Clinical Groups") da Johns Hopkins, versão 13.0 — a metodologia de ajuste de risco/case-mix que sustenta a estratificação da população pelo risco. Dirige-se a analistas, programadores e gestores clínicos que usam o software (aplicação Windows e processamento em lote/Linux). Está organizada em quatro volumes de conteúdo mais apêndices (o próprio documento fala em "quatro volumes", mas há um Volume V de apêndices): Volume I — instalação, requisitos de dados de entrada e validação (p.16–113); Volume II — referência técnica das marcações/markers (diagnóstico, farmácia, laboratório, utilização, coordenação, modelos de risco, modelos de hospitalização, "Patient Need Groups") (p.114–260); Volume III — aplicações (monitorização de saúde populacional, rastreio clínico, avaliação de desempenho, aplicações financeiras) (p.261–351); Volume IV — determinantes sociais da saúde (SDoH), ACG GeoHealth e "Social Need Markers" (p.352–363); Volume V — apêndices com listas de códigos, dados de saída, detalhe de relatórios, variáveis de calibração local, modo de lote, API Java e os modelos HCC americanos CMS-HCC, RxHCC e HHS-HCC (p.364–676) e índice (p.677).

## Estrutura
- p.1 — Página de rosto (versão 13.0, junho 2022)
- p.2 — Avisos de copyright e limitação de garantia
- p.3–12 — Índice (Contents)
- p.13 — Getting Started; introdução ao sistema ACG; contactos (acgsupport@jh.edu; hopkinsacg.org)
- p.13–15 — Nomenclatura e citações; equipa de produção; dedicatória (Barbara Starfield)
- p.16 — Volume I: Installation and Usage
- p.17 — Cap. 1: Technical Considerations (requisitos de sistema, licença .acgl, mapeamento .acgm, troubleshooting)
- p.28 — Cap. 2: Basic Data Requirements (constrangimentos de dados; formatos dos ficheiros de entrada)
- p.58 — Cap. 3: Loading Data (formatos personalizados; opções avançadas)
- p.76 — Cap. 4: Operating the ACG System Software (navegação; Report Options; exportação)
- p.98 — Cap. 5: Validating Results (Summary Statistics; avisos; códigos não correspondidos)
- p.114 — Volume II: Technical Reference
- p.115 — Cap. 6: Diagnosis-based Markers (ADGs, ACGs, RUBs, EDCs/MEDCs, marcadores adicionais)
- p.163 — Cap. 7: Pharmacy-based Markers (Rx-MGs; Active Ingredient Count; Novel Rx Scores)
- p.177 — Cap. 8: Diagnosis+Pharmacy-based Markers (Condition Markers; Pharmacy Adherence; opioides)
- p.198 — Cap. 9: Laboratory-based Markers
- p.203 — Cap. 10: Utilization and Resource Use Markers (inclui classificação de visitas às urgências JH-EDA)
- p.215 — Cap. 11: Coordination (marcadores de coordenação; Care Density)
- p.229 — Cap. 12: Risk Modeling (cinco dimensões; modelos concorrentes e prospetivos de custo)
- p.246 — Cap. 13: Predictive Models for Hospitalization
- p.253 — Cap. 14: Patient Need Groups (PNGs; Care Modifiers; estratificação de risco)
- p.261 — Volume III: Applications
- p.262 — Cap. 15: Population Health Monitoring
- p.280 — Cap. 16: Clinical Screening
- p.334 — Cap. 17: Performance Assessment (ajuste de risco; O/E; PMPM vs PMPY)
- p.346 — Cap. 18: Financial Applications (capitação e definição de tarifas; underwriting)
- p.352 — Volume IV: Social Determinants of Health (SDoH)
- p.353 — Cap. 19: Social Determinants of Health in the ACG System
- p.355 — Cap. 20: ACG GeoHealth Overview
- p.358 — Cap. 21: Social Need Markers
- p.360 — Cap. 22: SDoH Applications
- p.364 — Volume V: Appendices
- p.365 — Apêndice A: ACG System Codes and Descriptions
- p.405 — Apêndice B: ACG System Output Data
- p.483 — Apêndice C: Report Detail
- p.557 — Apêndice D: Variables Necessary to Locally Calibrate the ACG System Risk Models
- p.570 — Apêndice E: Batch Mode Processing
- p.588 — Apêndice F: Java API
- p.601 — Apêndice G: CMS-HCC Model
- p.623 — Apêndice H: CMS RxHCC Model
- p.634 — Apêndice I: HHS-HCC Model
- p.663 — Apêndice J: Acknowledgments
- p.677 — Index

## Mapa de páginas
- p.1 — Capa: título, versão 13.0, junho 2022.
- p.2 — Copyright/garantia; marcas registadas "ACG®", "ADG®", "Adjusted Clinical Groups®".
- p.3–12 — Índice detalhado (Contents), com números de página de todas as secções e apêndices.
- p.13 — Getting Started; estrutura em volumes; contacto de suporte; nomenclatura das marcações produzidas.
- p.14 — Continuação da lista de marcações (utilização, coordenação, modelos de risco, PNGs); regras de citação; equipa.
- p.15 — Dedicatória a Barbara Starfield.
- p.16 — Separador Volume I.
- p.17 — Cap.1: requisitos de SO (Windows 10/11/Server; Linux Debian/Oracle/RHEL/Amazon); CPU.
- p.18 — RAM/disco/resolução; instalações desktop e servidor; ficheiros .acgl (licença) e .acgm (mapeamento) máquina/utilizador-específicos.
- p.19 — Instalação do ficheiro de licença (.acgl). [figuras]
- p.20 — Componentes licenciados (Help>About); atualização do ficheiro de mapeamento.
- p.21 — Manage Mappings/Check for Updates; carregar dataset de amostra (~14.000 membros).
- p.22–23 — Criar ficheiro ACG a partir de dados de amostra; troubleshooting (Java 11/OpenJDK Temurin).
- p.24–25 — Espaço temporário (TMP), memória (parâmetros -Xms/-Xmx), ficheiro .lax.
- p.25 — Erros "out of memory"; cardinalidade elevada; IDs de paciente nulos.
- p.26 — Ficheiro de log; avisos; ficheiro de mapeamento; constrangimentos de ficheiros de entrada; [tabela tipos de dados].
- p.27 — [tabela] tipos de dados obrigatórios por ficheiro (data CCYY-MM-DD; sexo F/2=feminino).
- p.28 — Cap.2: constrangimentos de dados; lista de marcadores baseados em diagnóstico.
- p.29 — [tabela] dados necessários por marcador de farmácia; marcadores diagnóstico+farmácia.
- p.30–31 — [tabelas] dados necessários para marcadores de utilização; laboratório; bandas de recurso.
- p.31–32 — Marcadores de coordenação; modelos de custo (concorrente ACG, regressão, prospetivo); modelos de hospitalização.
- p.33–34 — Requisitos de dados para PNGs e Care Modifiers; Total Cost Risk; constrangimentos ACG GeoHealth (ZIP/FIPS).
- p.35 — Ex. formatação geo; modelos HHS-HCC e CMS-HCC (requisitos de ficheiros).
- p.36–37 — Considerações gerais: período de análise (12 meses); consistência da população; não-utilizadores e inscritos parciais.
- p.38 — Elementos de dados adicionais; regras gerais de extração (ASCII, delimitado por tab/vírgula).
- p.39–44 — [tabela] formato do ficheiro Patient (colunas: patient_id, age, sex, custos, marcadores de utilização, geo, race/ethnicity, etc.).
- p.45–46 — Seleção de diagnósticos relevantes; exclusão de laboratório/RX; [tabela] códigos de local de serviço e ranges de procedimento a excluir; extração de EHR.
- p.47–50 — [tabela] formato Medical Services / Supplementary Medical Services (dx_version/dx_cd, procedimentos, revenue, DRG); regras ICD (9/10/10CM), SNOMED "S".
- p.51 — [tabela] formato Pharmacy (rx_cd NDC/ATC, fill date, days supply, quantity).
- p.52–53 — [tabela] formato Laboratory (LOINC; componentes aceites); introdução ao ficheiro HHS-CMS Enrollment.
- p.53–56 — [tabela] formato HHS-CMS Enrollment (metal level, CSR, cms_factor_type, ESRD, PACE, etc.).
- p.56–57 — Local Allowable Rating Factors (ARF) para o modelo HHS.
- p.58–59 — Cap.3: formatos de ficheiro personalizados.
- p.60 — Expandir nº de diagnósticos/ICD proc (dx_cd_X, icd_proc_cd_X); carregar dados próprios.
- p.61–70 — Assistente New File; Risk Assessment Variables; colunas calculadas; opções; limites de não-correspondência (300 med/150 farmácia). [figuras]
- p.71 — Risk Assessment Variables (US-All Age, US-Non-Elderly, US-Elderly, US-TANF); definições.
- p.72–75 — Advanced Options: certeza diagnóstica (lenient/stringent), filtros diagnósticos, farmácia no CRI, All Models, utilization markers, low birthweight/delivered splitting, prior costs, cost truncation, Total Cost Risk Level quantiles (11), HHS-CMS year.
- p.76–77 — Cap.4: navegação (menus File/Edit/View/Validate/Analyze/Tools/Help); ficheiros .acgd; Report Options (6 conceitos).
- p.77–89 — Filtros (And/Any/None); Options; Comprehensive Profile; Utilization Profile; Calculations; Groups; Option Sets (.acgr). [figuras]
- p.90–92 — Exportação de análises (Excel/CSV; limite ~1.048.576 linhas); impressão/PDF; bulk export.
- p.92–97 — Exportação de ficheiros de dados; lista de todos os tipos de exportação (Patients and ACG Results, EDC/MEDC/ADG/Rx-MG, não-correspondidos, HHS/CMS, etc.).
- p.98 — Cap.5: processo de revisão básico (10 passos de validação).
- p.99–100 — Summary Statistics; taxas de não-correspondência (alvo ≤1% dx e ≤1% farmácia).
- p.101 — Modelo de risco: esquema de identificação (Dx-PM/Rx-PM/DxRx-PM; lenient/stringent; população).
- p.102–103 — Local Weights; Local Age/Sex Weights; distribuições; ED Visit Classification; Build Options.
- p.104–105 — Reports do menu Validate; distribuição de avisos.
- p.106–109 — [tabela] lista de códigos de aviso (06–55) e ficheiro onde se aplicam.
- p.110–111 — Reports do menu Analyze; RUB Distribution (6 grupos); comparação com referência; Condition Flag Distribution.
- p.111–113 — Revisão de códigos não correspondidos (diagnóstico, farmácia, laboratório).
- p.114 — Separador Volume II.
- p.115–117 — Cap.6: ADGs — 32 grupos (34 rótulos, 32 em uso); [tabela] ADGs e códigos ICD-10 exemplo.
- p.118–121 — Cinco critérios clínicos das ADGs (duração, severidade, certeza, etiologia, necessidade de especialidade); [tabela]; Major ADGs (adulto/pediátrico).
- p.121–122 — [tabela] relação nº de Major Morbidities ano 1 vs custo elevado; introdução às ACGs.
- p.122–126 — Quatro passos da atribuição ACG (ADG→CADG (12)→MAC (26)→ACG); AUTOGRP; [tabelas CADGs e MACs].
- p.127–133 — Árvores de decisão ACG (geral, MAC-12 grávidas, MAC-26 lactentes, MAC-24 múltiplas ADGs). [figuras]
- p.134–140 — Exemplos clínicos de categorias ACG (hipertensão, diabetes, gravidez/parto, lactentes).
- p.140–141 — RUBs: 6 classes (0 a 5); relação ACG↔RUB.
- p.141–146 — [tabela] Final ACG Categories, Reference ACG Concurrent Risks (pediátrico/adulto/idoso) e RUB — listagem completa das categorias ACG.
- p.146–152 — EDCs (286) e MEDCs (27); desenvolvimento (Schneeweiss; Forrest); diabetes; certeza diagnóstica; 5 MEDC-Types; High/Moderate/Low impact; diferenças EDC vs ADG.
- p.152–154 — Chronic Condition Count (definição; >12 meses); [tabela] exemplos; distribuição por idade.
- p.154–156 — Tracking Chronic Conditions (Apply/Apply all/Confirm with pharmacy); 61 EDCs congruentes; Newly Diagnosed Conditions.
- p.156–157 — Hospital Dominant Morbidity Types; [tabelas] exemplos e efeito na hospitalização/custo.
- p.157–159 — Frailty Conditions (10 clusters/frailty concepts; ≥18 anos); [tabelas] utilização futura.
- p.159–160 — CAL-SSA (Compassionate Allowances, U.S. SSA); Social Need Markers (5 domínios, 13 subdomínios).
- p.161–162 — Pregnant; Delivered (VPP >96%); Pregnancy without Delivery; Low Birth Weight (<2500g).
- p.163–164 — Cap.7: Rx-MGs (88 categorias); princípios; base clínica; 4 dimensões clínicas; 20 Major Rx-MGs.
- p.165–172 — [tabela] os 88 Rx-MGs com ingredientes-rota comuns e descrições.
- p.172–174 — NDC (~240.000 códigos), HCPCS, ATC (OMS); High/Moderate/Low impact Rx-MG.
- p.174 — Active Ingredient Count (≥20 dá peso extra); Proximal Active Ingredient Count (120 dias).
- p.174–176 — Novel Rx Scores: Medication Complexity Scores; High Caution Medication Scores; [tabela] categorias de alta cautela.
- p.176 — Aplicações dos Novel Rx Scores.
- p.177–183 — Cap.8: Condition Markers (22 condições; valores TRT/BTH/ICD/Rx/NP); [tabela] definições ICD/Rx/TRT; Untreated (Y/P/N/D/Blank).
- p.183–193 — Pharmacy Adherence: nº de gaps, MPR, CSA, PDC (17 condições); grace period 15/30 dias; [tabela] Condition-Drug Class Pairings; exemplos de cálculo.
- p.193–195 — Pharmacy Spans; End-of-Period Possession; validação (MPR 0.8 = boa posse).
- p.196–197 — High Risk Prescription Opioid Use: Chronic User (100+ MME/dia, 90+ dias), Concomitant User (30+ dias opioide+benzodiazepina), Opioid Dependency.
- p.198–202 — Cap.9: Laboratory-based Markers (diabetes, dislipidemia, anemia por deficiência, doença renal); [tabelas] marcadores e limiares; componentes/LOINC/unidades.
- p.203–208 — Cap.10: regras de negócio dos marcadores de utilização (hospitalizações all-cause/unplanned; readmissões 30 dias; dias; observação; urgências; ambulatório; diálise; enfermagem; procedimento major; tratamento oncológico; ventilação mecânica; psicoterapia).
- p.209–214 — Emergency Department Visit Classification (JH-EDA, expansão do NYU-EDA; 11 categorias); [tabelas] diagnósticos exemplo; validação NHAMCS 2015; Resource Bands (percentis 0–9).
- p.215–217 — Cap.11: Coordination — 5 marcadores; [listas] códigos CPT face-a-face, especialidades elegíveis/não elegíveis/generalistas.
- p.218–222 — Management/Generalist Visit Count; Majority Source of Care (MSOC); Unique Provider Count; Specialty Count; Generalist Seen.
- p.223–225 — Risk of Poor Coordination (LCI/PCI/UCI); [tabela] grelha de decisão; impacto nos custos.
- p.226–228 — Care Density (rácio, quantis LOW/MID/TOP; cost saving ratio); [tabelas] custo e utilização por risco de coordenação.
- p.229–232 — Cap.12: Risk Modeling — cinco dimensões (base conceptual; população de referência; fatores de risco; abordagem estatística; resultados modelados); [figura] fatores de risco.
- p.233–239 — Abordagem estatística (células atuariais, regressão linear, regressão logística); Concurrent Cost Models (Local Age-Sex; ACG Concurrent Risk; regressão); rescale; validação (R², rácios E/A).
- p.239–245 — Prospective Cost Models (Predicted Total/Pharmacy Cost Risk; Rank/Reference Probability High Cost; Unexpected Pharmacy Cost; Persistent High User); calibração local (mín. 100.000).
- p.246–252 — Cap.13: Predictive Models for Hospitalization (tipologia; abordagem em níveis, idade 55; utilização; likelihood de hospitalização; readmissão 30 dias); [tabelas] PPV/sensibilidade/C-Statistic.
- p.253–260 — Cap.14: Patient Need Groups (11 PNGs em 6 segmentos); Care Modifiers; estratificação de risco (quantis); aplicações e valor; requisitos de dados.
- p.261 — Separador Volume III.
- p.262–279 — Cap.15: Population Health Monitoring (frequency distributions; SMRs; análises preditivas; profiling; avaliação de programa/ROI matched-case control). [figuras]
- p.280–333 — Cap.16: Clinical Screening (Care Management List; Comprehensive Patient Clinical Profile; Report Options; exemplos por doença/farmácia/utilização). [figuras/tabelas]
- p.334–345 — Cap.17: Performance Assessment (categorias ACG vs regressão; inscritos parciais PMPM vs PMPY; cálculo de custos esperados/O/E; Utilization Profile). [tabelas]
- p.346–351 — Cap.18: Financial Applications (capitação e definição de tarifas; underwriting; Actuarial Cost Projections). [tabela]
- p.352 — Separador Volume IV.
- p.353–354 — Cap.19: SDoH (porquê; captação via Z-codes ICD-10 Z55–Z65; abordagem paciente vs geográfica).
- p.355–357 — Cap.20: ACG GeoHealth (17 variáveis × 5 métricas = 85; ADI; ZIP/FIPS; American Community Survey).
- p.358–359 — Cap.21: Social Need Markers (5 domínios, 13 subdomínios; combinar com GeoHealth).
- p.360–363 — Cap.22: SDoH Applications (GeoHealth por condado; disparidades geográficas/ADI; Social Need Marker distribution).
- p.364 — Separador Volume V.
- p.365–404 — Apêndice A: [tabelas] códigos e descrições — RUB, ACG, ADG, Major EDC/EDC, Frailty, Social Need, Major Rx-MG/Rx-MG, EDCs+Rx-MGs congruentes, Lab, ED Visit Type, Patient Need Group, HHS-HCC, HHS-HCC RXC, CMS-HCC, CMS RxHCC.
- p.405–482 — Apêndice B: [tabelas] dados de saída (Patients and ACG Results e todos os ficheiros de atribuição/exportação).
- p.483–556 — Apêndice C: detalhe dos relatórios (Summary Statistics; distribuições; SMR; Utilization Profile; Care Management List; Comprehensive Patient Clinical Profile; relatórios GeoHealth e HHS/CMS).
- p.557–569 — Apêndice D: variáveis para calibração local (marcadores demográficos, categorias ACG, EDCs, Rx-MGs, marcadores adicionais, utilização, hospitalização prévia). [tabelas]
- p.570–587 — Apêndice E: processamento em lote (Windows/DOS/Linux; linha de comandos; JDBC).
- p.588–600 — Apêndice F: Java API (visão geral; input; parâmetros do modelo; output).
- p.601–622 — Apêndice G: modelo CMS-HCC (visão geral; diferenças; construção; CCs→HCCs; seleção de modelo; ajustes; exemplos; hierarquias e interações).
- p.623–633 — Apêndice H: modelo CMS RxHCC (visão geral; RxCCs→RxHCCs; exemplo).
- p.634–662 — Apêndice I: modelo HHS-HCC (visão geral; construção; modelos Adulto/Criança/Lactente; hierarquias; grupos de severidade). [tabelas]
- p.663–676 — Apêndice J: agradecimentos e bibliotecas de terceiros.
- p.677–689 — Index (índice remissivo).

## Conceitos
**ACG (Adjusted Clinical Group)** → p.122, p.365 — categorias atuariais mutuamente exclusivas de estado de saúde definidas por morbilidade, idade e sexo; cada indivíduo é atribuído a uma única categoria ACG com base no padrão das suas morbilidades. Listagem completa em p.141–145 e p.365–369.
**ACG Concurrent Risk** → p.234 — avaliação da utilização relativa de recursos para os indivíduos numa categoria ACG (célula atuarial): custo médio dos doentes da categoria ÷ custo médio da população; existe "Reference ACG Concurrent Risk" (referência externa) e "Local ACG Concurrent Risk"; formas unscaled/rescaled.
**ACG decision tree** → p.122, p.126 — lógica de árvore de decisão que divide os MACs em categorias terminais (ACGs) considerando idade, sexo, ADGs presentes, nº de ADGs e nº de Major ADGs.
**ACG GeoHealth** → p.355 — módulo de determinantes sociais ligados à geografia; 17 variáveis, cada uma com 5 métricas (estimated value, margin of error, national/state percentile, national category) = 85 variáveis; usa ZIP/FIPS e dados do American Community Survey; inclui o "Area Deprivation Index (ADI)".
**Active Ingredient Count** → p.174 — contagem de ingredientes ativos únicos nas prescrições do doente; ≥20 recebe peso adicional nos modelos preditivos; "Proximal Active Ingredient Count" limita aos últimos 120 dias.
**ADG (Aggregated Diagnosis Group)** → p.115 — primeiro passo da lógica ACG: cada código de diagnóstico é atribuído a um ou mais de 32 grupos de diagnóstico ("morbidity types"). 34 rótulos existem, apenas 32 estão em uso (15 e 19 não usados).
**AUTOGRP** → p.125 — software de "recursive partitioning" da Universidade de Yale usado no desenvolvimento para subdividir os MACs em categorias ACG.
**CADG (Collapsed ADG)** → p.123 — colapso das 32 ADGs em 12 grupos ("Collapsed ADGs"), não mutuamente exclusivos, para reduzir combinações.
**CAL-SSA (Compassionate Care Allowances)** → p.159 — marcador que identifica a presença de um diagnóstico consistente com as "Compassionate Allowances Conditions" definidas pela U.S. Social Security Administration.
**Care Density** → p.226 — medida ao nível do doente da partilha de doentes entre os médicos que o viram; rácio com quantis LOW/MID/TOP; associada a menor utilização de recursos.
**Care Modifiers (CM)** → p.254 — flags binárias de fatores específicos do doente (ex.: polifarmácia, risco cardio-metabólico, uso de substâncias) que estratificam dentro dos segmentos PNG.
**Chronic Condition Count** → p.152 — contagem de marcadores de doença crónica únicos; condição crónica = alteração de estruturas/funções do corpo com duração provável >12 meses e impacto negativo na saúde/estado funcional.
**Concurrent (retrospetivo) cost model** → p.233 — modelo explicativo em que os fatores de risco derivam do mesmo período do resultado (custo); usado para explicar custos históricos e na avaliação de desempenho.
**Condition Markers** → p.177 — marcadores para 22 doenças crónicas; valores mutuamente exclusivos TRT, BTH, ICD, Rx, NP; "TRT" exige ≥2 prescrições em datas distintas ≤210 dias (17 das 22 condições).
**Coordination Risk (LCI/PCI/UCI)** → p.223 — combinação dos marcadores de coordenação em "likely" (LCI), "possible" (PCI) ou "unlikely" (UCI) coordination issue.
**C-Statistic** → p.251 — medida de ajuste do modelo; 0,5 = não distingue; 0,7 = limiar aceite de bom desempenho.
**CMS-HCC Model** → p.601 — réplica do algoritmo de ajuste de risco do programa Medicare Advantage (CMS); modelos prospetivos; requer licença.
**CMS RxHCC Model** → p.623 — modelo de risco farmacêutico (Part D) baseado em RxCCs→RxHCCs; requer licença.
**Delivered** → p.161 — estado de parto; divide as ACG 1710–1770 conforme houve ou não parto no período; VPP dos códigos de parto >96%.
**EDC (Expanded Diagnosis Cluster)** → p.146, p.371 — atribui os códigos de diagnóstico a um de 286 EDCs (organizados em 27 MEDCs); ferramenta para identificar pessoas com doenças/sintomas específicos; classificados por impacto High/Moderate/Low.
**Emergency Department Visit Classification (JH-EDA)** → p.209 — algoritmo Johns Hopkins (expansão do NYU-EDA) que classifica cada visita às urgências em 11 categorias; classifica tipicamente >99% das visitas.
**Frailty (Frailty Flag/Concepts/Concept Count)** → p.157 — variável dicotómica que indica se um doente ≥18 anos tem diagnóstico em qualquer um de 10 clusters de problemas médicos associados a fragilidade; frailty concept count = nº de conceitos distintos.
**High Caution Medication Scores** → p.175 — marcadores de medicação de risco inerente de eventos adversos (High Caution Rx Score, High Caution Medication, High Caution Rx Categories).
**Hospital Dominant Morbidity Types (HOSDOM)** → p.156 — diagnósticos associados a maior probabilidade de hospitalização no ano seguinte; contagem de ADGs com ≥1 diagnóstico "hospital dominant".
**HHS-HCC Model** → p.634 — réplica do algoritmo de ajuste de risco do "Health Insurance Marketplace" (CCIIO/HHS); modelos concorrentes; modelos Adulto/Criança/Lactente; requer licença.
**Likelihood of Hospitalization / Readmission** → p.249, p.251 — scores de probabilidade de hospitalização de internamento e de readmissão não planeada em 30 dias.
**Low Birth Weight** → p.162 — <2500 gramas; usado para subdividir categorias ACG de lactentes; identificado por diagnóstico ou flag do utilizador.
**MAC** → p.124 — categoria mutuamente exclusiva baseada no padrão de CADGs; existem 26 MACs (1–23 combinações; 24 = outras; 25 = sem diagnóstico; 26 = lactentes <12 meses).
**Major ADG** → p.121 — ADGs com utilização de recursos esperada muito elevada; listas distintas para adultos e pediatria.
**Majority Source of Care (MSOC)** → p.218 — percentagem das visitas de ambulatório face-a-face prestada pelo(s) médico(s) que mais viu o doente.
**MEDC (Major Expanded Diagnosis Cluster)** → p.146 — 27 categorias amplas que agrupam os EDCs; agregáveis em 5 "MEDC Types" (p.150).
**Medication Complexity Scores** → p.175 — quantificam a complexidade do regime medicamentoso (Medication Complexity Score, Complex Medication, number_mcs_claims).
**MPR (Medication Possession Ratio)** → p.189 — dias de medicação dispensada ÷ dias entre a primeira e a última prescrição; ≥0,80 = boa adesão.
**CSA (Continuous Single-interval Availability)** → p.190 — rácio dias-supply/dias até à prescrição seguinte, com média entre prescrições; mais sensível a gaps frequentes.
**PDC (Proportion of Days Covered)** → p.191 — dias-supply ÷ dias entre a primeira prescrição e o fim do período de observação; máximo 1,0; medida ao nível da classe de fármaco.
**Patient Need Groups (PNGs)** → p.253, p.390 — 11 grupos clínicos mutuamente exclusivos em 6 segmentos de alto nível (Low Need, Moderate, Pregnancy, Dominant Condition, High Complexity Multi-Morbidity, Frailty).
**Prospective (preditivo) cost model** → p.239 — modelo em que os fatores de risco derivam do período anterior ao resultado; prevê custo/risco no ano seguinte.
**Rank/Reference Probability High Total/Pharmacy Cost** → p.240 — probabilidade de o doente estar no top 5% de custos no período seguinte (rank = relativa à população do estudo; reference = relativa à população de referência).
**Resource Bands (Total/Pharmacy Cost Band)** → p.214 — bandas de custo prévio em percentis (0 a 9) usadas nos modelos preditivos.
**RUB (Resource Utilization Band)** → p.140, p.365 — colapso das categorias ACG em 6 classes por utilização de recursos: 0 (No/Only Invalid Dx), 1 (Healthy Users), 2 (Low), 3 (Moderate), 4 (High), 5 (Very High).
**Rx-MG (Rx-Defined Morbidity Group)** → p.163, p.382 — sistema de classificação de medicamentos em 88 categorias por ingrediente ativo/via de administração; base dos modelos preditivos farmacêuticos; 20 Major Rx-MGs.
**Risk Assessment Variables** → p.71 — dados de referência da Johns Hopkins que controlam o cálculo das variáveis; conjuntos US-All Age, US-Non-Elderly, US-Elderly, US-TANF.
**Social Need Markers (SNM)** → p.160, p.358 — medidas ao nível do doente de necessidades sociais; 5 domínios (Social, Education, Health Care System, Economic, Physical Environment) e 13 subdomínios; derivadas de códigos ICD-10.
**Standardized Morbidity Ratio (SMR)** → p.270 — rácio observado/esperado (ajustado por idade-sexo) da prevalência de EDCs, para comparar subpopulações.
**Stringent vs Lenient Diagnostic Certainty** → p.72, p.117 — lenient: uma única ocorrência de diagnóstico ativa o marcador; stringent: para um subconjunto de condições crónicas exige ≥2 ocorrências em datas/registos distintos.

## Factos citáveis
- O documento tem 689 páginas; edição de junho de 2022; © 2022 The Johns Hopkins University. (p.1–2)
- Editor sénior: Jonathan P. Weiner; editora de gestão: Mandy Kearney. (p.14)
- Dedicado à memória de Barbara Starfield, M.D., MPH. (p.15)
- Contacto de suporte: acgsupport@jh.edu; website hopkinsacg.org. (p.13)
- SO suportados: Windows 10/11 (32/64-bit), Windows Server 2012 R2/2016/2019/2022; Linux Debian 10/11, Oracle Linux 7/8, RHEL 7/8, Amazon Linux 2. (p.17)
- Requisitos: CPU 2.0 GHz+; RAM recomendada 2 GB; aplicação ~350 MB de disco; espaço temporário ~4–5× os ficheiros de entrada. (p.17–18)
- Requer runtime Java 11 (ex.: OpenJDK 11 / Eclipse Temurin da Adoptium). (p.23)
- Ficheiro de licença = extensão .acgl; ficheiro de mapeamento = .acgm; ficheiro de dados = .acgd; ficheiro de opções (Option Set) = .acgr. (p.18, p.20, p.76, p.89)
- Dataset de amostra: ~14.000 membros. (p.21, p.262)
- Sexo: valor "F" ou "2" = feminino; todos os outros valores = masculino. (p.26, p.34)
- Formato de datas: CCYY-MM-DD. (p.27)
- Período de dados recomendado: 1 ano (12 meses) com run-out apropriado. (p.36)
- Códigos reconhecidos são atualizados trimestralmente (mapping file). (p.100, p.173)
- Taxas de não-correspondência alvo: geralmente ≤1% para diagnósticos e ≤1% para farmácia. (p.100)
- Existem 32 ADGs em uso (34 rótulos; ADGs 15 e 19 não usados). (p.115, p.117, p.201-nota)
- Existem 4,3 mil milhões de combinações possíveis de ADGs; colapsadas em 12 CADGs. (p.123)
- Existem 26 MACs; MAC-24 tem 33 categorias ACG; MAC-25 = sem diagnóstico; MAC-26 = lactentes <12 meses. (p.124, p.132)
- Há 6 classes de RUB (0 a 5). (p.140)
- Existem 286 EDCs e 27 MEDCs (agregáveis em 5 MEDC Types). (p.146, p.150)
- O EDC de otite média combina 41 códigos ICD-10 (260 códigos ICD-10-CM nos EUA). (p.147)
- Há 88 categorias Rx-MG e 20 Major Rx-MGs; ~240.000 códigos NDC colapsados em ~4.050 combinações ingrediente/via. (p.163–164, p.172-173)
- Atualização trimestral de NDC: tipicamente 1.500–2.500 novos NDCs / 50–75 novos ingredientes. (p.173)
- ATC: taxonomia internacional da OMS com 5 níveis (14 grupos anatómicos principais). (p.172)
- Condition Markers cobrem 22 condições crónicas; 17 avaliadas para adesão à medicação; TRT exige ≥2 prescrições ≤210 dias em datas distintas. (p.177, p.185)
- Adesão à medicação: MPR ≥0,80 considerada boa; grace period de 15 dias (30 em certos casos); mín. 60 dias de supply ao nível da classe (excluindo a última prescrição) para MPR/CSA/PDC. (p.185, p.186, p.189)
- Marcadores de opioides: Chronic User = 100+ MME/dia por 90+ dias consecutivos; Concomitant User = 30+ dias de uso concomitante de opioide+benzodiazepina; limiar de MME a evitar 90–120/dia. (p.196)
- Diabetes (lab): limiar de HbA1c 6,5% para identificar diabetes; 9,0% (HEDIS) indica controlo glicémico inadequado. (p.199)
- Marcadores laboratoriais aplicam-se a indivíduos com ≥18 anos. (p.198)
- Frailty: em beneficiários Medicare de um sistema da Nova Inglaterra, 16,8% tinham ≥1 frailty concept e 3,9% ≥2. (p.158)
- ED Visit Classification (JH-EDA): 11 categorias; classifica >99% das visitas; validado com NHAMCS 2015 (33,49% não-emergentes; total 133.165.968 visitas ponderadas). (p.209, p.213–214)
- Hospitalização de internamento definida por revenue code de room-and-board 100–219 com place of service 21 ou type of bill 011x/012x/018x, ou place of service IP. (p.50, p.203)
- Modelos de hospitalização: usam idade 55 como limiar entre dois grupos de risco. (p.247)
- Validação de hospitalização: C-Statistic da maioria dos modelos >0,7 (ex.: IP Hospitalization 0,729–0,746); readmissão 30 dias C-Statistic = 0,848. (p.251, p.252)
- Recomenda-se ≥30 indivíduos por categoria ACG para estimativas estáveis. (p.130, p.234, p.346)
- 5 dimensões de um modelo de risco: base conceptual, população de referência, fatores de risco, abordagem estatística, resultados modelados. (p.229)
- Modelos preditivos usam 27 categorias ACG individuais; modelos concorrentes usam 30. (p.231)
- População de referência: Legacy PharMetrics Adjudicated Claims Database (IQVIA/QuintilesIMS); dados 2013–2015; ex.: 3.306.768 beneficiários comerciais <65 anos. (p.145, p.229–230)
- Calibração local recomendada: modelos personalizados com não menos de 100.000 indivíduos. (p.245)
- Categorias ACG especiais: 5110 = sem diagnóstico/diagnóstico não classificado; 5200 = não-utilizadores; 9900 = idade/data de nascimento inválida. (p.145, p.365)
- Low Birth Weight = <2500 gramas; historicamente 2–5% identificados por diagnóstico vs 6–9% real. (p.130, p.162)
- Delivered: exatidão preditiva positiva dos códigos de parto >96%. (p.161)
- PNGs: 11 grupos em 6 segmentos; Frailty (PNG 11) = adultos ≥65 anos com ≥2 frailty concepts. (p.253–254)
- Estratificação de risco por defeito: Low = 60% inferior, Medium = 30% médio, High = 10% superior; 11 quantis disponíveis; até 3 selecionáveis. (p.255)
- Total Cost Risk Level: até 4 níveis; quantis por defeito 60 e 90. (p.75, p.257)
- Performance: PMPY (sem anualização) é a abordagem recomendada para ajuste de risco com inscritos parciais. (p.338)
- SDoH: ICD-10 introduziu Z-codes Z55–Z65 para fatores que influenciam o estado de saúde. (p.353)
- ACG GeoHealth v13.0: 17 variáveis × 5 métricas = 85 variáveis; usa dados de 2019 (census tract) devido à inconsistência de 2020/COVID-19. (p.34, p.355)
- Social Need Markers: 5 domínios e 13 subdomínios; alinhados com o modelo "Accountable Health Communities" (CMS) e Healthy People 2030 (CDC). (p.160, p.358)
- Modelos HCC (CMS-HCC, RxHCC, HHS-HCC) requerem licença adicional. (p.35, p.53, p.601, p.623, p.634)
- CMS-HCC 2022: ~2.300 coeficientes de modelo; Modelo 21 = 87 HCCs, Modelo 22 = 79 HCCs, Modelo 24 = 86 HCCs. (p.607, p.606)
- Excel template fornecido: ACG Labels.xlt. (p.365)
- Limite de linhas de exportação para Excel: 1.048.576. (p.91)
- Limiares de "grande número de registos" por doente: >300 medical services, >300 lab, >150 pharmacy; default de paragem em 7,5% dos doentes. (p.69)

## Perguntas que este documento responde
- O que é uma categoria ACG e como é atribuída a cada indivíduo? → p.122–126
- Quantas ADGs, EDCs, MEDCs e Rx-MGs existem e o que significam? → p.115 (ADGs), p.146 (EDCs/MEDCs), p.163 (Rx-MGs)
- Como se definem as Resource Utilization Bands (RUBs) e quais são os 6 níveis? → p.140
- Qual é o peso/risco concorrente de referência de cada categoria ACG? → p.141–145
- Como o sistema calcula o risco concorrente e o risco prospetivo de custo? → p.233–245
- Como se prevê a probabilidade de hospitalização e de readmissão a 30 dias? → p.246–252
- Que dados de entrada são necessários (paciente, serviços médicos, farmácia, laboratório)? → p.39–53
- Como excluir diagnósticos de rule-out/laboratório/raios-X da avaliação de morbilidade? → p.45–46
- O que distingue a certeza diagnóstica "lenient" da "stringent"? → p.72, p.117
- Como se medem a adesão à medicação (MPR, CSA, PDC) e os gaps de posse? → p.183–193
- Como o sistema identifica uso de risco de opioides? → p.196–197
- O que são os Patient Need Groups e os Care Modifiers? → p.253–255
- Como se ajusta o risco no perfil de desempenho de prestadores (O/E, PMPM vs PMPY)? → p.334–343
- Como usar o ACG System para capitação, definição de tarifas e underwriting? → p.346–350
- Como o sistema aborda os determinantes sociais da saúde (SDoH, GeoHealth, Social Need Markers)? → p.353–363
- O que são os modelos CMS-HCC, RxHCC e HHS-HCC e em que diferem do ACG? → p.601, p.623, p.634
- Que categorias ACG indicam ausência de diagnóstico ou não-utilizadores? → p.145 (5110, 5200)
- Que população de referência e que anos de dados foram usados para calibrar os modelos? → p.229–230
- Como identificar doentes para gestão de doença/caso (rastreio clínico)? → p.280–332
- Como se classifica uma visita às urgências (algoritmo JH-EDA)? → p.209–214

## Relações com outros documentos
Referências explícitas (todas externas ao repositório, sem menção às circulares da ACSS):
- New York University Emergency Department Algorithm (NYU-EDA) — base do algoritmo JH-EDA. (p.209)
- Schneeweiss R. et al., "Diagnosis Clusters", Med Care 1983;21:105-122 — origem dos EDCs. (p.147)
- Elixhauser A., Andrews RM, Fox S. (1993), Clinical classifications for health policy research (AHCPR Pub. 93-0043). (p.147)
- Kharrazi H. et al., Medical Care 2017;55(8):789-796 (comparação de modelos com dados de EHR vs claims). (p.46)
- Kan HJ, Kharrazi H, Leff B et al., Med Care 2018;56(3):233-239 (frailty). (p.158)
- Hess et al., Annals of Pharmacotherapy 40:1280-1288, 2006 (revisão de posse de medicação). (p.184)
- Austin PC et al. (2011), Med Care 49:932-939 (uso de ADGs para prever mortalidade, Ontário). (p.229)
- Pollack CE et al., J Gen Intern Med 2013;28(3):459-65 (partilha de doentes e custos / care density). (p.226)
- Weiner et al., "The Maryland Model", J Ambulatory Care Manage, 1998; Gifford GA et al., Health Care Finance Rev 26:21-41, 2005 (estudos de caso de ajuste de risco). (p.348)
- CMS (Centers for Medicare & Medicaid Services) — documentação dos modelos CMS-HCC e RxHCC; medida HWR/readmissões (YNHHSC/CORE 2018). (p.35, p.246, p.601)
- CCIIO (Center for Consumer Information & Insurance Oversight) — documentação do modelo HHS-HCC. (p.35, p.634)
- Vermont Support and Services at Home (SASH) — exemplo de uso de dados SDoH. (p.353)
- U.S. Census Bureau — American Community Survey (ACS), FIPS codes (dados GeoHealth/ADI). (p.356–357)
- Normas de código: ICD-9/10/10-CM (OMS/CMS), SNOMED CT, NDC, ATC (OMS), LOINC (Regenstrief), CPT (AMA), HCPCS (CMS), UB-04/NUBC, NUCC. (p.47–52, p.147, p.172, p.200)
Nenhuma referência explícita a circulares/despachos da ACSS ou a legislação portuguesa.
