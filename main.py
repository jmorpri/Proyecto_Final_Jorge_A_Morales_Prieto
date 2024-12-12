import requests
import random

def obtener_preguntas():
    url = "https://opentdb.com/api.php?amount=15&category=11&difficulty=easy&type=multiple"
    respuesta = requests.get(url)
    datos = respuesta.json()
    return datos['results']


def mostrar_pregunta(pregunta, numero):
    print(f"\nPregunta {numero}: {pregunta['question']}")
    opciones = pregunta['incorrect_answers'] + [pregunta['correct_answer']]
    random.shuffle(opciones)
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")
    return opciones


def iniciar_juego():
    nombre = input("Bienvenido a '¿Quién quiere ser millonario?' Ingresa tu nombre: ")
    print(f"\n¡Hola, {nombre}! ¡Buena suerte!\n")

    preguntas = obtener_preguntas()
    puntos = 0
    comodin_usado = False

    for i, pregunta in enumerate(preguntas, 1):
        print(f"\nPuntos actuales: {puntos}")
        decision = input("¿Deseas continuar o plantarte? (c/p): ").lower()
        if decision == 'p':
            print(f"Te has plantado con {puntos} puntos. ¡Gracias por jugar!")
            return

        if not comodin_usado:
            usar_comodin = input("¿Deseas usar tu comodín para saltar esta pregunta? (s/n): ").lower()
            if usar_comodin == 's':
                comodin_usado = True
                print("Comodín usado. Saltando pregunta...")
                continue

        opciones = mostrar_pregunta(pregunta, i)
        respuesta_usuario = input("Elige tu respuesta (1-4): ")

        try:
            indice_respuesta = int(respuesta_usuario) - 1
            if opciones[indice_respuesta] == pregunta['correct_answer']:
                print("¡Correcto! Sumaste un punto.")
                puntos += 1
            else:
                print(f"Incorrecto. La respuesta correcta era: {pregunta['correct_answer']}")
                print("Has perdido. Tu puntuación final es 0.")
                return
        except (ValueError, IndexError):
            print("Opción inválida. Por favor, selecciona un número entre 1 y 4.")

    print(f"\n¡Felicidades, {nombre}! Tu puntuación final es: {puntos}")


if __name__ == "__main__":
    iniciar_juego()





