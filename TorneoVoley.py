import random

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.partidosGanados = 0
        self.partidosPerdidos = 0
        self.setGanados = 0

    def __str__(self):
        return f"{self.nombre}: Partidos Ganados: {self.partidosGanados}, Partidos Perdidos: {self.partidosPerdidos}"


equipo1 = None
equipo2 = None

def RegistraSet(ganador):
    global equipo1, equipo2
    
    if ganador == 1:
        equipo1.setGanados += 1
    else:
        equipo2.setGanados += 1

    
    if equipo1.setGanados == 3:
        equipo1.partidosGanados += 1
        equipo2.partidosPerdidos += 1
        equipo1.setGanados = 0
        equipo2.setGanados = 0
        return True 
    elif equipo2.setGanados == 3:
        equipo2.partidosGanados += 1
        equipo1.partidosPerdidos += 1
        equipo1.setGanados = 0
        equipo2.setGanados = 0
        return True
    return False

def Puntos():
    return random.randint(10, 28)

def PuntosExtras():
    return random.randint(0, 6)

def JugarPartido():
    global equipo1, equipo2
   
    equipo1.setGanados = 0
    equipo2.setGanados = 0

    print(f"Comienza partido entre {equipo1.nombre} y {equipo2.nombre}!")
    while True:
        puntos1 = Puntos()
        puntos2 = Puntos()
        print(f"Set: {equipo1.nombre} {puntos1} - {equipo2.nombre} {puntos2}")

        if puntos1 >= 25 and puntos1 > puntos2:
            print(f"¡{equipo1.nombre} gana el set!")
            if RegistraSet(1):
                break
        elif puntos2 >= 25 and puntos2 > puntos1:
            print(f"¡{equipo2.nombre} gana el set!")
            if RegistraSet(2):
                break
        else:
            intentos = 0
            max_intentos = 50
            while True:
                intentos += 1
                puntos1 += PuntosExtras()
                puntos2 += PuntosExtras()
                print(f"Puntos extra: {equipo1.nombre} {puntos1} - {equipo2.nombre} {puntos2}")

                if puntos1 >= 25 and puntos1 > puntos2:
                    print(f"¡{equipo1.nombre} gana el set con puntos extra!")
                    if RegistraSet(1):
                        break
                    else:
                        break
                elif puntos2 >= 25 and puntos2 > puntos1:
                    print(f"¡{equipo2.nombre} gana el set con puntos extra!")
                    if RegistraSet(2):
                        break
                    else:
                        break
                elif intentos >= max_intentos:
                    
                    ganador = 1 if puntos1 >= puntos2 else 2
                    print(f"¡Se fuerza ganador del set! {equipo1.nombre if ganador==1 else equipo2.nombre} gana después de {intentos} intentos")
                    if RegistraSet(ganador):
                        break
                    else:
                        break
            
            if equipo1.partidosGanados + equipo1.partidosPerdidos > 0 and (equipo1.setGanados==0 and equipo2.setGanados==0):
                break
    print(f"Fin de partido. Marcador de encuentros: {equipo1.nombre} partidos ganados {equipo1.partidosGanados}, {equipo2.nombre} partidos ganados {equipo2.partidosGanados}")


def ResultadoTorneo():
    print("\nRESULTADO FINAL DEL TORNEO")
    print(equipo1)
    print(equipo2)


def main():
    global equipo1, equipo2
    equipo1 = Equipo(input("Ingrese el nombre del primer equipo: "))
    equipo2 = Equipo(input("Ingrese el nombre del segundo equipo: "))

    try:
        cantidad = int(input("¿Cuántos partidos deben jugar los equipos?: "))
    except ValueError:
        print("Error: Debes ingresar un número entero.")
        return

    for i in range(cantidad):
        print(f"\n--- Jugando partido {i + 1} ---")
        JugarPartido()

    ResultadoTorneo()

if __name__ == "__main__":
    main()
