import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv
import os
import google.generativeai as genai
import pywhatkit
import subprocess
import pyautogui

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
    Clasifica el siguiente comando de text como una de las siguientes opciones: "REPRODUCIR (Nombre_de_una_musica)", "REPRODUCIR (Nombre_del_tema_de_un_video)", "ABRIR_APLICACION (Nombre_de_una_aplicación)", "DIGITAR_TEXTO (Texto_a_digitar)", "SALIR", "OTROS". Basado en el texto recibido, response con la respuesta más probable.
                                        
    Ejemplo de comandos:
    - "Reproduce la música de Queen" -> "REPRODUCIR (Queen)"
    - "Me gusta los tutoriales de ciencias y experimentar con la física podrias mostrarme algunos videos" -> "REPRODUCIR (videos de ciencias y física)"
    - "Abre el editor de vs code" -> "ABRIR_APLICACION (code)"
    - "Escribe el texto Reunión a las 10:00 am" -> "DIGITAR_TEXTO (Reunión a las 10:00 am)"
                                         
    Comando de texto recibido: {text}
    """)

    return ai_response.text

def open_youtube(content_name: str) -> None:
    """Abre el navegador de YouTube y reproduce el contenido"""
    pywhatkit.playonyt(content_name)

def get_content_from_instruction(instruction: str) -> str:
    """Extrae el nombre del contenido del comando recibido"""
    return instruction.split(" ")[1].replace("(", "").replace(")", "")

def write_text(content: str) -> None:
    """Tipea el contenido en cualquier aplicación"""
    pyautogui.write(content)

def execute_instruction(instruction: str) -> None:
    """Ejecuta la instrucción recibida"""
    print(instruction)

    if instruction == "SALIR":
        speak("Adiós, ¡Hasta pronto!")
    elif instruction == "OTROS":
        speak("Lo siento, por el momento no puedo realizar eso.")
    elif "REPRODUCIR" in instruction:
        content = get_content_from_instruction(instruction)
        speak(f"Reproduciendo {content} en YouTube")
        open_youtube(content)
    elif "ABRIR_APLICACION" in instruction:
        content = get_content_from_instruction(instruction)
        vs_code_path = r"C:\Users\usuario\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        subprocess.Popen(vs_code_path)
        speak(f"Abriendo {content}")
    elif "DIGITAR_TEXTO" in instruction:
        content = get_content_from_instruction(instruction)
        write_text(content)
        speak(f"Digitando {content}")

def main():
    """Inicia el programa"""
    while True:
        text = listen()

        if text is not None:
            instruction = ia_response(text)
            execute_instruction(instruction)


if __name__ == '__main__':
    main()