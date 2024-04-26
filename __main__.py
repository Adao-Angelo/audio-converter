from pydub import AudioSegment
import os

def converter_para_wav(arquivo_entrada, arquivo_saida):
    # Carrega o arquivo de áudio
    audio = AudioSegment.from_file(arquivo_entrada)
    
    # Define o formato de saída para WAV
    formato_saida = "wav"
    
    # Salva o arquivo convertido para o formato WAV
    audio.export(arquivo_saida, format=formato_saida)

if __name__ == "__main__":
    # Arquivo de entrada
    arquivo_entrada = input("arquivo de entrda -> ")  # Altere para o caminho do arquivo de entrada
    
    # Arquivo de saída (formato WAV)
    arquivo_saida = input("arquivo de saida -> ")   # Altere para o caminho do arquivo de saída
    
    # Realiza a conversão
    converter_para_wav(arquivo_entrada, arquivo_saida)


    print("Conversão concluída com sucesso!")