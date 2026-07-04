import os
import json
import pandas as pd

def extrair_urnas_definitivas():
    print("A iniciar a extração definitiva de dados (Agrupamento Limpo) para o Bootstrap...\n")

    # =====================================================================
    # 1. SIMULAÇÃO 1: Recorte de Turma / Coorte
    # Ficheiro: INDICADORES_TRAJETORIA_PROCESSADO.csv
    # =====================================================================
    print("A processar Simulação 1...")
    df_traj = pd.read_csv('dados/INDICADORES_TRAJETORIA_PROCESSADO.csv')
    df_comp_traj = df_traj[df_traj['CO_CURSO'] == 85783.0].copy()

    # Ordenar cronologicamente por turma e ano de referência
    df_comp_traj = df_comp_traj.sort_values(by=['NU_ANO_INGRESSO', 'NU_ANO_REFERENCIA'])

    # Calcular o tempo de acompanhamento da turma (Ano 0, 1, 2...)
    df_comp_traj['ANO_ACOMPANHAMENTO'] = df_comp_traj['NU_ANO_REFERENCIA'] - df_comp_traj['NU_ANO_INGRESSO']

    # CORREÇÃO: DELTA_TDA/DELTA_TCA (diff de taxa acumulada) usam sempre o
    # ingressante ORIGINAL como base, porque é assim que TDA/TCA são definidas
    # pelo INEP. Isso não é a probabilidade de transição de um passo da cadeia
    # de Markov, que precisa ser condicional a quem ainda estava ativo no ano
    # anterior. Trocamos pelo cálculo direto: evento do ano / sobreviventes do
    # ano anterior (PERM_ANTERIOR).
    df_comp_traj['PERM_ANTERIOR'] = df_comp_traj.groupby('NU_ANO_INGRESSO')['QT_PERMANENCIA'].shift(1)

    # Filtro da Pandemia: Excluir os anos ruidosos
    df_limpo_traj = df_comp_traj[~df_comp_traj['NU_ANO_REFERENCIA'].isin([2020, 2021])].copy()

    # t=0 não é uma transição (não existe "ano anterior"); descarta junto
    # com qualquer linha sem PERM_ANTERIOR válido
    df_limpo_traj = df_limpo_traj[
        (df_limpo_traj['ANO_ACOMPANHAMENTO'] > 0)
        & df_limpo_traj['PERM_ANTERIOR'].notna()
        & (df_limpo_traj['PERM_ANTERIOR'] > 0)
    ]

    df_limpo_traj['P_EVASAO'] = (df_limpo_traj['QT_DESISTENCIA'] / df_limpo_traj['PERM_ANTERIOR']).round(4)
    df_limpo_traj['P_FORMATURA'] = (df_limpo_traj['QT_CONCLUINTE'] / df_limpo_traj['PERM_ANTERIOR']).round(4)

    def limpar_amostras_coorte(serie):
        # Mantém os zeros: um ano sem evasão/formatura é uma observação real,
        # não ruído a ser descartado (descartar infla a média da urna).
        return serie.tolist()

    # Extração das Urnas (separadas pelo relógio biológico do curso)
    df_inicio = df_limpo_traj[df_limpo_traj['ANO_ACOMPANHAMENTO'] <= 3]
    df_final = df_limpo_traj[df_limpo_traj['ANO_ACOMPANHAMENTO'] >= 4]

    urna_E_A = limpar_amostras_coorte(df_inicio['P_EVASAO'])
    urna_E_R = limpar_amostras_coorte(df_final['P_EVASAO'])
    urna_F_R = limpar_amostras_coorte(df_final['P_FORMATURA'])

    # =====================================================================
    # 2. SIMULAÇÃO 2: Fluxo Institucional Macro
    # Ficheiro: DADOS_CURSOS_REF_TOTAL.csv
    # =====================================================================
    print("A processar Simulação 2...\n")
    df_ref = pd.read_csv('dados/DADOS_CURSOS_REF_TOTAL.csv')
    df_comp_ref = df_ref[df_ref['CO_CURSO'] == 85783.0].copy()

    # Ordenar por ano do censo
    df_comp_ref = df_comp_ref.sort_values('NU_ANO_CENSO')

    # Deslocar a coluna para obter os matriculados do ano anterior MAT(t-1)
    df_comp_ref['MAT_ANTERIOR'] = df_comp_ref['QT_MAT'].shift(1)

    # Equação de Balanço de Massa: Evadidos(t) = MAT(t-1) + ING(t) - CONC(t) - MAT(t)
    # NOTA: as colunas EVASAO/SUCESSO do arquivo NÃO servem aqui -- elas são
    # normalizadas pela coorte de ingressantes de "duração" anos atrás
    # (SUCESSO(t) = CONC(t)/ING(t-duração)), não pela população ativa total.
    # Para o modelo homogêneo desta simulação (uma taxa única aplicada a toda
    # a população Ativa, misturando calouros e veteranos), o denominador
    # correto é mesmo MAT_ANTERIOR, como já estava. Ver comparação: SUCESSO(2024)
    # dá 84% (relativo aos 120 ingressantes de 2019), mas CONC(2024)/MAT_ANTERIOR
    # dá 14,6% (relativo aos 692 alunos ativos em 2023) -- é esse segundo número
    # que representa "probabilidade de um aluno ativo qualquer se formar no ano".
    df_comp_ref['EVADIDOS_ESTIMADOS'] = df_comp_ref['MAT_ANTERIOR'] + df_comp_ref['QT_ING'] - df_comp_ref['QT_CONC'] - df_comp_ref['QT_MAT']

    # Calcular as taxas macro em relação ao volume de alunos do ano anterior
    df_comp_ref['TAXA_EVASAO_MACRO'] = df_comp_ref['EVADIDOS_ESTIMADOS'] / df_comp_ref['MAT_ANTERIOR']
    df_comp_ref['TAXA_FORMATURA_MACRO'] = df_comp_ref['QT_CONC'] / df_comp_ref['MAT_ANTERIOR']

    # Filtro da Pandemia e remoção do primeiro ano nulo (falta de MAT_ANTERIOR)
    df_limpo_ref = df_comp_ref[~df_comp_ref['NU_ANO_CENSO'].isin([2020, 2021])].dropna(subset=['TAXA_EVASAO_MACRO', 'TAXA_FORMATURA_MACRO'])

    # ANOMALIA DE DADO DOCUMENTADA: em 2024 a matrícula cresceu mais do que
    # ingressantes menos concluintes explicam (provável transferência/reingresso
    # não capturado pelas colunas disponíveis), gerando EVADIDOS_ESTIMADOS
    # negativo. Excluímos explicitamente esse ponto em vez de deixar o filtro
    # de positivos escondê-lo -- documentar isso no relatório é parte do
    # exercício de análise de risco (limitação de dado conhecida).
    anos_anomalos = df_limpo_ref[df_limpo_ref['TAXA_EVASAO_MACRO'] < 0]['NU_ANO_CENSO'].tolist()
    if anos_anomalos:
        print(f"AVISO: excluindo ano(s) com evasão estimada negativa (anomalia de dado): {anos_anomalos}")
    df_limpo_ref = df_limpo_ref[df_limpo_ref['TAXA_EVASAO_MACRO'] >= 0]

    def extrair_amostras_macro(serie):
        return serie.round(4).tolist()

    urna_E_Macro = extrair_amostras_macro(df_limpo_ref['TAXA_EVASAO_MACRO'])
    urna_F_Macro = extrair_amostras_macro(df_limpo_ref['TAXA_FORMATURA_MACRO'])

    # =====================================================================
    # 3. CONSOLIDAÇÃO E EXPORTAÇÃO JSON
    # =====================================================================
    dados_bootstrap = {
        "simulacao_1_coorte": {
            "evasao_inicial_pE_A": urna_E_A,
            "evasao_tardia_pE_R": urna_E_R,
            "formatura_tardia_pF_R": urna_F_R
        },
        "simulacao_2_fluxo": {
            "evasao_macro_pE": urna_E_Macro,
            "formatura_macro_pF": urna_F_Macro
        }
    }

    pasta_saida = 'matrizes'
    os.makedirs(pasta_saida, exist_ok=True)
    caminho_arquivo = os.path.join(pasta_saida, 'urnas_bootstrap.json')
    
    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados_bootstrap, f, indent=4)

    print("--- RESUMO ESTATÍSTICO DAS URNAS ---")
    print(f"Simulação 1 - Evasão Inicial (Amostras: {len(urna_E_A)}): {urna_E_A[:4]}...")
    print(f"Simulação 1 - Evasão Tardia  (Amostras: {len(urna_E_R)}): {urna_E_R[:4]}...")
    print(f"Simulação 1 - Formatura      (Amostras: {len(urna_F_R)}): {urna_F_R[:4]}...")
    print(f"Simulação 2 - Evasão Macro   (Amostras: {len(urna_E_Macro)}): {urna_E_Macro[:4]}...")
    print(f"Simulação 2 - Formatura Macro(Amostras: {len(urna_F_Macro)}): {urna_F_Macro[:4]}...")
    print(f"\nFicheiro estruturado com sucesso em: '{caminho_arquivo}'")

if __name__ == "__main__":
    extrair_urnas_definitivas()