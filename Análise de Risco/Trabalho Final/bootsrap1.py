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

    # Calcular as variações anuais (Deltas) isolando turma a turma
    df_comp_traj['DELTA_TDA'] = df_comp_traj.groupby('NU_ANO_INGRESSO')['TDA'].diff().fillna(df_comp_traj['TDA'])
    df_comp_traj['DELTA_TCA'] = df_comp_traj.groupby('NU_ANO_INGRESSO')['TCA'].diff().fillna(df_comp_traj['TCA'])

    # Filtro da Pandemia: Excluir os anos ruidosos
    df_limpo_traj = df_comp_traj[~df_comp_traj['NU_ANO_REFERENCIA'].isin([2020, 2021])]

    def limpar_amostras_coorte(serie):
        # Filtra valores estritamente positivos e converte de percentagem para decimal
        return (serie[serie > 0] / 100.0).round(4).tolist()

    # Extração das Urnas (separadas pelo relógio biológico do curso)
    df_inicio = df_limpo_traj[df_limpo_traj['ANO_ACOMPANHAMENTO'] <= 3]
    df_final = df_limpo_traj[df_limpo_traj['ANO_ACOMPANHAMENTO'] >= 4]

    urna_E_A = limpar_amostras_coorte(df_inicio['DELTA_TDA'])
    urna_E_R = limpar_amostras_coorte(df_final['DELTA_TDA'])
    urna_F_R = limpar_amostras_coorte(df_final['DELTA_TCA'])

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
    df_comp_ref['EVADIDOS_ESTIMADOS'] = df_comp_ref['MAT_ANTERIOR'] + df_comp_ref['QT_ING'] - df_comp_ref['QT_CONC'] - df_comp_ref['QT_MAT']
    
    # Calcular as taxas macro em relação ao volume de alunos do ano anterior
    df_comp_ref['TAXA_EVASAO_MACRO'] = df_comp_ref['EVADIDOS_ESTIMADOS'] / df_comp_ref['MAT_ANTERIOR']
    df_comp_ref['TAXA_FORMATURA_MACRO'] = df_comp_ref['QT_CONC'] / df_comp_ref['MAT_ANTERIOR']

    # Filtro da Pandemia e remoção do primeiro ano nulo (falta de MAT_ANTERIOR)
    df_limpo_ref = df_comp_ref[~df_comp_ref['NU_ANO_CENSO'].isin([2020, 2021])].dropna(subset=['TAXA_EVASAO_MACRO', 'TAXA_FORMATURA_MACRO'])

    def extrair_amostras_macro(serie):
        # Garante a retenção apenas de taxas positivas
        return serie[serie > 0].round(4).tolist()

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
    