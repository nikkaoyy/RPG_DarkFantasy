<<<<<<< HEAD
# RPG Abstract Factory + Builder

Sistema de creación de personajes RPG implementado con los patrones de diseño **Abstract Factory** y **Builder**.

## Descripción

Este proyecto demuestra la implementación combinada de dos patrones creacionales en Python:

- **Abstract Factory** garantiza que los componentes de cada raza sean cohesivos (un Orco siempre tendrá armadura de cuero con calaveras, nunca una élfica).
- **Builder** permite construir un `Personaje` complejo paso a paso, eligiendo qué partes incluir y en qué orden, sin constructores con decenas de parámetros.

## Características

=======
# RPG Abstract Factory

Sistema de creación de personajes RPG implementado con el patrón de diseño **Abstract Factory**.

## Descripción

Este proyecto demuestra la implementación del patrón Abstract Factory en Python, permitiendo la creación de personajes completos para un juego RPG. Cada raza (Humano, Orco, Elfo) tiene su propia familia de productos (Cuerpo, Montura, Armadura, Arma) que se crean de manera cohesiva a través de factorías especializadas.

## Características

- **Patrón Abstract Factory**: Creación de familias de objetos relacionados sin especificar sus clases concretas
>>>>>>> 9cfba27844f0e0878f0f4d9ffbfb09d1432d2303
- **3 Razas disponibles**:
  - 🧙 Humano: Estadísticas equilibradas
  - 💪 Orco: Alta fuerza y defensa
  - 🧝 Elfo: Inteligencia mejorada y magia

- **4 Componentes por raza**:
  - Cuerpo (Stats base del personaje)
  - Montura (Vehículo de transporte)
  - Armadura (Defensa y equipamiento)
  - Arma (Múltiples opciones según raza)

<<<<<<< HEAD
- **3 Arquetipos predefinidos** (vía Director):
  - ⚔️ Guerrero: cuerpo + armadura + arma + montura
  - 🏹 Explorador: cuerpo + arma + montura
  - 🌱 Iniciado: cuerpo + arma

## Requisitos

- Python 3.10+
=======
## Requisitos

- Python 3.6+
>>>>>>> 9cfba27844f0e0878f0f4d9ffbfb09d1432d2303

## Instalación

```bash
git clone <repository-url>
cd RPG_AbFac
```

## Uso

Ejecutar el programa:

```bash
<<<<<<< HEAD
python backend/principal.py
```

Se te pedirá que elijas raza, nombre y arquetipo:

```
Elige tu raza (humano, orco, elfo): elfo
Nombre de tu personaje: Legolas
¿Qué tipo de personaje quieres ser?
  1) Guerrero  (cuerpo + armadura + arma + montura)
  2) Explorador (cuerpo + arma + montura)
  3) Iniciado  (cuerpo + arma)
Opción (1/2/3): 2
```

### Ejemplo de salida

```
══════════════════════════
  Personaje: Legolas
  Raza:      Elfo
══════════════════════════
Stats:
- Fuerza: 7
- Agilidad: 7
- Inteligencia: 12
- Defensa: 6
- Vida: 150
- Ataque: 7
Arma: Arco
- Ataque: 10
- Alcance: +5
Montura: Unicornio
Habilidades: Sigilo, Rastreo
=======
python rpg.py
```

Se te pedirá que selecciones una raza:

```
Elige tu raza (humano, orco, elfo): humano
```

El sistema creará un personaje completo con todos sus componentes:
- Estadísticas del cuerpo
- Montura disponible
- Armadura equipada
- Selección de arma

### Ejemplo de ejecución

```
Elige tu raza (humano, orco, elfo): humano
Stats:
- Fuerza: 7
- Agilidad: 7
- Inteligencia: 7
- Defensa: 7
- Vida: 100
- Ataque: 7
Montura: Caballo
...
>>>>>>> 9cfba27844f0e0878f0f4d9ffbfb09d1432d2303
```

## Estructura del Proyecto

```
RPG_AbFac/
<<<<<<< HEAD
├── backend/
│   ├── productos.py     # Interfaces abstractas, productos concretos y clase Personaje
│   ├── fabricas.py      # RazaFactory abstracta + fábricas concretas por raza
│   ├── builder.py       # PersonajeBuilder, ConstructorPersonaje y Director
│   └── principal.py     # Punto de entrada
├── LICENSE
└── README.md
```

## Patrones implementados

### Abstract Factory

| Elemento | Clase |
|---|---|
| Interfaces abstractas | `Humano`, `Orco`, `Elfo` |
| Productos concretos | `CuerpoHumano`, `ArmaOrco`, `MonturaElfo`… |
| Fábrica abstracta | `RazaFactory` |
| Fábricas concretas | `HumanoFactory`, `OrcoFactory`, `ElfoFactory` |

### Builder

| Elemento | Clase |
|---|---|
| Producto | `Personaje` |
| Interfaz constructora | `PersonajeBuilder` |
| Constructor concreto | `ConstructorPersonaje` |
| Director | `Director` |

El `ConstructorPersonaje` usa internamente la `RazaFactory` correspondiente, de modo que Abstract Factory y Builder colaboran: el Builder decide *qué partes* construir y *en qué orden*; la Factory decide *qué variante concreta* usar según la raza.

También es posible usar el Builder directamente sin el Director para personalización total:

```python
personaje = (
    ConstructorPersonaje()
    .set_nombre(nombre)
    .set_raza(raza)
    .construir_cuerpo()
    .construir_arma()
    .agregar_habilidad("Lluvia de flechas") # ejemplo
    .get_personaje()
)
```
=======
├── rpg.py           # Código principal con todas las clases
├── README.md        # Este archivo
└── LICENSE          # Licencia del proyecto
```

## Patrón Abstract Factory

El patrón utiliza:

- **Interfaces abstractas** (`humano`, `orco`, `elfo`): Definen los métodos que deben implementar
- **Productos concretos**: Clases específicas para cada componente
- **Factorías abstractas** (`razaFactory`): Define los métodos de creación
- **Factorías concretas** (`humanoFactory`, `orcoFactory`, `elfoFactory`): Implementan la creación de productos

Esta estructura garantiza que los componentes de un personaje sean cohesivos y utilizados correctamente.
>>>>>>> 9cfba27844f0e0878f0f4d9ffbfb09d1432d2303

## Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

<<<<<<< HEAD
## Autores
=======
## Autor
>>>>>>> 9cfba27844f0e0878f0f4d9ffbfb09d1432d2303

- [Nicolás Martínez Pineda](https://github.com/nikkaoyy)
