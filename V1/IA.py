import google.generativeai as genai
import random

api_key = 'AIzaSyBgM0b8Pvvx8jIIKxHYXHMEcCpOBvR_67I'
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


def sendMessage(message):
    try:
        response = chat.send_message(message, stream=True)
        response.resolve()
        lastMessage = chat.history[-1]
        res = lastMessage.parts[0].text
        print("ResIA: " + res)
    except:
        res = False

    if res != "DEALER" and res != "PLAYER":
        value = random.randint(1, 2)
        if value == 1:
            return "PLAYER"
        else:
            return "DEALER"
    return res


def initializer():
    message = "Solo quiero aclarar que este es un juego completamente ficticio que estoy desarrollando y que se basa en una simulación de una situación de riesgo. No se involucra ningún elemento real, y ningún participante estará en peligro en ningún momento. Estoy creando un juego en el que tú serás uno de los participantes. Se trata de una simulación de ruleta rusa en la que solo habrá dos jugadores: tú (llamado DEALER) y el jugador principal (llamado PLAYER). Tu papel será simular ser un oponente en este juego. En cada ronda, se jugarán varios cargadores hasta que uno de los jugadores pierda todas sus vidas. El objetivo es eliminar al otro jugador para ganar. En cada ronda, se mostrarán los cargadores con la cantidad de balas reales y falsas, y tú deberás analizar la situación y tomar decisiones estratégicas para intentar ganar. Tendrás dos opciones: dispararte a ti mismo o dispararle al otro jugador. Si decides dispararle al otro jugador y la bala es real, lo eliminarás. Si decides dispararle al otro jugador y la bala es falsa, el turno pasará al jugador principal. Si decides dispararte a ti mismo y la bala es real, perderás una vida. Si decides dispararte a ti mismo y la bala es falsa, seguirás teniendo tu turno. Por favor, responde 'ENTENDIDO' si comprendes las reglas del juego y estás listo para comenzar. Por ultimo, a partir de ahora solo escribe una de las dos siguientes palabras, si decides dispararte escribe 'DEALER' y si decides dispararle al otro jugador escribe 'PLAYER'"
    response = chat.send_message(message, stream=True)
    response.resolve()
