import pandas as pd

def  processar(nome_arquivo = 'aula_07/tempos_modelos.csv'):
    try:
        df = pd.read_csv(nome_arquivo)
        media_tempo = df['tempo_execucao'].mean()

        desvio = df['tempo_execucao'].std()

        print(f"Media: {media_tempo:.2f}")
        print(f"Desvio: {desvio:.2f}")
    except FileNotFoundError:
        print("Arquivo não encontrado!")
    except Exception as e:
        print(f"Erro ao processar arquivo: {e}")


processar()
