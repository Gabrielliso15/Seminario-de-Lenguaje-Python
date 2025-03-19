import random
import sys
# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]

# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]

# Índice de la respuesta correcta para cada pregunta, en el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

puntaje = int(0)

# El usuario deberá contestar 3 preguntas
for _ in range(3):
    # Se selecciona una pregunta aleatoria
    question_index = random.randint(0, len(questions) - 1)

    # Se muestra la pregunta y las respuestas posibles
    print(questions[question_index])
    for i, answer in enumerate(answers[question_index]):
        print(f"{i + 1}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        try:
            user_answer = int(input("Respuesta: ")) - 1
            if user_answer < 0 or user_answer > 3 :
                raise ValueError
        except ValueError:
            print("Por favor, ingrese un número válido.")
            sys.exit(1)
           
                   # Se verifica si la respuesta es correcta
        if user_answer == correct_answers_index[question_index]:
            print("¡Correcto!\n")
            puntaje += 1
            break
        else:
            print("Incorrecto. Intenta de nuevo.")
            puntaje -= 0.5

    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print(f"Incorrecto. La respuesta correcta es: {answers[question_index][correct_answers_index[question_index]]}\n")
print(f"Puntaje Final : {puntaje}  ")
