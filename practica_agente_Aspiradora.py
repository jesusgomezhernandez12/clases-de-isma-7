import random
import time

# Habitaciones del entorno
habitaciones = {
    "A": "Sucia",
    "B": "Sucia"
}

posicion = "A"
pasos = 0
limpiezas = 0
movimientos = 0


def mostrar_estado():
    print("\n" + "=" * 35)
    print("CASA")
    print(f"A: {habitaciones['A']}")
    print(f"B: {habitaciones['B']}")
    print(f"Aspiradora: habitacion {posicion}")
    print(f"Pasos: {pasos} | Limpiezas: {limpiezas}")
    print("=" * 35)


def aspirar():
    global limpiezas

    print(f"Limpiando la habitacion {posicion}...")
    time.sleep(0.5)

    habitaciones[posicion] = "Limpia"
    limpiezas += 1

    print("Listo!")


def moverse():
    global posicion, movimientos

    posicion = "B" if posicion == "A" else "A"
    movimientos += 1

    print(f"Moviendose a la habitacion {posicion}")


def ensuciar():
    # A veces una habitacion limpia vuelve a ensuciarse
    if random.random() < 0.15:
        habitacion = random.choice(["A", "B"])

        if habitaciones[habitacion] == "Limpia":
            habitaciones[habitacion] = "Sucia"
            print(f"La habitacion {habitacion} se volvio a ensuciar")


def todo_limpio():
    return all(estado == "Limpia" for estado in habitaciones.values())


print("La aspiradora inteligente ha comenzado")

mostrar_estado()

while not todo_limpio() and pasos < 15:
    pasos += 1

    print(f"\nPaso {pasos}")

    # El entorno puede cambiar
    ensuciar()

    # La aspiradora observa y decide que hacer
    if habitaciones[posicion] == "Sucia":
        aspirar()
    else:
        moverse()

    mostrar_estado()

    time.sleep(0.7)


print("\nFIN DEL TRABAJO")

if todo_limpio():
    print("La casa esta completamente limpia")
else:
    print("Se acabo el tiempo")

print(f"Puntuacion: {limpiezas * 10 - movimientos}")