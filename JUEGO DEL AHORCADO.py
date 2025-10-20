# ================================
# 🎮 JUEGO DEL AHORCADO EN PYTHON
# ================================

def mostrar_ahorcado(intentos):
    """Dibuja el ahorcado según el número de errores"""
    etapas = [
        """
           +---+
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]
    return etapas[intentos]


def juego_ahorcado():
    print("=================================")
    print(" 🎯 BIENVENIDO AL JUEGO DEL AHORCADO ")
    print("=================================\n")

    # Ingresar palabra secreta (sin mostrarla)
    palabra = input("Jugador 1, ingrese la palabra secreta: ").upper()
    print("\n" * 50)  # Limpia la pantalla

    palabra_oculta = ["_" if letra != " " else " " for letra in palabra]
    letras_usadas = []
    errores = 0
    max_errores = 6

    # Ciclo principal del juego
    while errores < max_errores and "_" in palabra_oculta:
        print(mostrar_ahorcado(errores))
        print("Palabra: ", " ".join(palabra_oculta))
        print("Letras usadas: ", ", ".join(letras_usadas))
        letra = input("Adivina una letra: ").upper()

        # Validaciones
        if len(letra) != 1 or not letra.isalpha():
            print("⚠️ Ingresa solo una letra válida.\n")
            continue

        if letra in letras_usadas:
            print("⚠️ Ya usaste esa letra, intenta con otra.\n")
            continue

        letras_usadas.append(letra)

        # Verificar si la letra está en la palabra
        if letra in palabra:
            print("✅ ¡Bien hecho! La letra está en la palabra.\n")
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    palabra_oculta[i] = letra
        else:
            print("❌ Letra incorrecta.")
            errores += 1
            print(f"Te quedan {max_errores - errores} intentos.\n")

    # Resultado final
    print(mostrar_ahorcado(errores))
    if "_" not in palabra_oculta:
        print("🎉 ¡FELICIDADES! Has adivinado la palabra:", palabra)
    else:
        print("💀 Has perdido. La palabra era:", palabra)


# Ejecutar el juego
if __name__ == "__main__":
    juego_ahorcado()
