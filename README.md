# Simulación de Torneo de Vóley

Este proyecto implementa en Python la simulación de un torneo de vóley entre dos equipos, siguiendo los requisitos y la lógica vista en clase.

---

## Descripción

- Se define la clase `Equipo` con atributos:
  - `nombre`  
  - `partidosGanados`  
  - `partidosPerdidos`  
  - `setGanados` (contador del partido actual)

- Se crean dos instancias globales: `equipo1` y `equipo2`.

- Funciones principales:
  1. **`RegistraSet(ganador)`**  
     - Recibe un entero (1 o 2) indicando qué equipo ganó el set.  
     - Incrementa el contador de sets y, al llegar a 3, actualiza partidos ganados/perdidos y resetea los sets.  

  2. **`Puntos()`**  
     - Retorna un entero aleatorio entre 10 y 28 (puntos obtenidos en un set).  

  3. **`PuntosExtras()`**  
     - Retorna un entero aleatorio entre 0 y 6 (puntos adicionales en caso de empate).  

  4. **`JugarPartido()`**  
     - Sin parámetros: simula un partido completo.  
     - Usa `Puntos()` para cada set. Si ninguno alcanza 25 con ventaja, entra en bucle de “puntos extra” hasta decidir el set (o forzar ganador tras un número máximo de intentos).  
     - Llama a `RegistraSet()` y detecta cuándo un equipo alcanza 3 sets para finalizar el partido.  

  5. **`ResultadoTorneo()`**  
     - Sin parámetros: muestra en pantalla el total de partidos ganados y perdidos de ambos equipos.  

- El script principal (`main`) solicita al usuario:
  1. Nombre de cada equipo.  
  2. Número de partidos a jugar.  
  3. Ejecuta `JugarPartido()` para cada encuentro.  
  4. Al final, imprime el resultado global con `ResultadoTorneo()`.

---

## Requisitos

- Python 3.x  
- Módulo estándar `random`

---

## Estructura de archivos

```text
.
├── README.md          ← Este archivo
└── voleibol.py        ← Script principal con toda la lógica
