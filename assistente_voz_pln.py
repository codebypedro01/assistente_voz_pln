'''Observação importante, o script feito não funciona no python 3.13 ou superior,
verifique sua versão antes de dar continuidade!'''

print('Testando')

import speech_recognition as sr
import os

#Função responsável por ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilita o microfone para ouvir o usuário
    microfone = sr.Recognizer()
    
    #Usando o microfone
    with sr.Microphone() as source:
        #Convoca um algoritmo de redução de ruidos no som
        microfone.adjust_for_ambient_noise(source)

        #Avisa o usuário que está pronto para ouvir
        print('Diga alguma coisa: ')
        
        #Armazena a informação de audio na variavel
        audio = microfone.listen(source)

    try:
        #Passa a variável para o algoritmo reconhecedor de padrões
        frase = microfone.recognize_google(audio, language='pt-BR')

        if 'navegador' in frase:
            os.system('start chrome.exe')
            return False
        elif 'Excel' in frase:
            os.system('start excel.exe')
            return False
        elif 'powerpoint' in frase:
            os.system('start POWERPNT.exe')
            return False
        elif 'Edge' in frase:
            os.system('start msedge.exe')
            return False
        elif 'fechar' in frase:
            os.system('exit')
            return True
        
        #Retorna a frase pronunciada
        print(f'Voce disse: {frase}')
    
    #Se não reconheceu o padrão de fala, retorna a mensagem
    except sr.UnknownValueError:
        print('Não entendi')
    
    return False

while True:
    if ouvir_microfone():
        break