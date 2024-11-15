import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

def speak(text: str) -> None:
    """Habla el texto recibido"""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen() -> str | None:
    """Escucha y procesa el audio recibido"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language='es-es')
        return text.lower()
    
    except sr.UnknownValueError:
        print("¡No entiendo lo que tratas de decir!")
        speak("¡No entiendo lo que tratas de decir!")
        return None
    
    except sr.RequestError as e:
        print("¡No puedo escuchar!")
        speak("¡No puedo escuchar!")
        return None
    
def ia_response(text: str) -> str:
    """Procesa el texto recibido y devuelve una instrucción"""
    genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    ai_response = model.generate_content(f"""
    Clasifica el siguiente comando de voz como una de las siguientes opciones: "REPRODUCIR", "ABRIR_APLICACION", "DIGITAR_TEXTO", "SALIR", "CLICKAR". Basandote en el contexto del texto, devuelve unicamente una de las instrucciones.
                                        
    Ejemplo de comandos:
    - "Reproduce la música de Queen" -> "REPRODUCIR (Queen)"
    - "Me gusta los tutoriales de ciencias y experimentar con la física podrias mostrarme algunos videos" -> "REPRODUCIR (videos de ciencias y física)"
    - "Abre el editor de vs code" -> "ABRIR_APLICACION (code)"
    - "Escribe el texto 'Reunión a las 10:00 am'" -> "DIGITAR_TEXTO ('Reunión a las 10:00 am')"
                                         
    Comando de texto recibido: {text}
    """)

    print(ai_response)
    print('-' * 50)
    print(ai_response.text)

def main():
    """Inicia el programa"""
    while True:
        text = listen()

        if text is not None:
            instruction = ia_response(text)


if __name__ == '__main__':
    main()