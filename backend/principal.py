from builder import ConstructorPersonaje, Director


def main():
    builder = ConstructorPersonaje()
    director = Director(builder)

    print("RPG Abstract Factory + Builder\n")

    raza = input("Elige tu raza (humano, orco, elfo): ").strip().lower()
    nombre = input("Nombre de tu personaje: ").strip()

    print("\n¿Qué tipo de personaje quieres ser?")
    print("  1) Guerrero  (cuerpo + armadura + arma + montura)")
    print("  2) Explorador (cuerpo + arma + montura)")
    print("  3) Iniciado  (cuerpo + arma)")
    tipo = input("Opción (1/2/3): ").strip()

    try:
        if tipo == "1":
            director.construir_guerrero(nombre, raza)
        elif tipo == "2":
            director.construir_explorador(nombre, raza)
        elif tipo == "3":
            director.construir_iniciado(nombre, raza)
        else:
            print("Opción inválida, creando guerrero por defecto.")
            director.construir_guerrero(nombre, raza)

        personaje = builder.get_personaje()
        print("\n" + str(personaje))

    except ValueError as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()