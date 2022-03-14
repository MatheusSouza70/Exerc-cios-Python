import speech_recognition as sr
from playsound import playsound

def ouvir_microfone():

    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        
        microfone.adjust_for_ambient_noise(source)
       
        print("Diga alguma coisa: ")
    
        audio = microfone.listen(source)
        
    try:
        
        frase = microfone.recognize_google(audio,language='pt-BR')
        
        print("Você disse: " + frase)
        
  
    except sr.UnknownValueError:
        print("Não entendi, repita por favor.")
        
    return (frase)