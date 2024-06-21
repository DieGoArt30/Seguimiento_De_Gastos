import pickle
from datetime import datetime

class Transaccion:
    def __init__(self, monto: float, fecha: datetime, descripcion: str, tipo: str):
        self.monto = monto
        self.fecha = fecha
        self.descripcion = descripcion
        self.tipo = tipo

class GestorTransacciones:
    def __init__(self):
        self.transacciones = []

    def agregar_transaccion(self, transaccion: Transaccion):
        self.transacciones.append(transaccion)

    def ver_transacciones(self):
        """Muestra todas las transacciones almacenadas."""
        for index, transaccion in enumerate(self.transacciones, start=1):
            print(f"{index}. {transaccion.fecha}: {transaccion.descripcion} ({transaccion.tipo}): ${transaccion.monto}")

    def editar_transaccion(self, indice: int, nueva_transaccion: Transaccion):
        """Edita una transacción en una posición dada."""
        if 0 <= indice < len(self.transacciones):
            self.transacciones[indice] = nueva_transaccion
            print("Transacción editada correctamente.")
        else:
            print("Índice de transacción fuera de rango.")

    def eliminar_transaccion(self, indice: int):
        """Elimina una transacción en una posición dada."""
        if 0 <= indice < len(self.transacciones):
            del self.transacciones[indice]
            print("Transacción eliminada correctamente.")
        else:
            print("Índice de transacción fuera de rango.")

    def calcular_balance(self):
        """Calcula y muestra el balance financiero actual."""
        ingresos = sum(transaccion.monto for transaccion in self.transacciones if transaccion.tipo.lower() == 'ingreso')
        gastos = sum(transaccion.monto for transaccion in self.transacciones if transaccion.tipo.lower() == 'gasto')
        ahorro = ingresos - gastos
        print(f"Ingresos totales: ${ingresos}")
        print(f"Gastos totales: ${gastos}")
        print(f"Capacidad de ahorro: ${ahorro}")

    def guardar_datos(self):
        with open('datos_financieros.pkl', 'wb') as archivo:
            pickle.dump(self.transacciones, archivo)

    def cargar_datos(self):
        try:
            with open('datos_financieros.pkl', 'rb') as archivo:
                self.transacciones = pickle.load(archivo)
        except FileNotFoundError:
            self.transacciones = []

def menu():
    print("Bienvenido al Sistema de Seguimiento de Gastos")
    print("1. Agregar Transacción")
    print("2. Listar Transacciones")
    print("3. Ver Transacciones")
    print("4. Editar Transacción")
    print("5. Eliminar Transacción")
    print("6. Mostrar Balance")
    print("7. Salir")

def main():
    gestor = GestorTransacciones()
    gestor.cargar_datos()
    
    while True:
        menu()
        opcion = input("Ingrese el número de la opción que desea: ")

        if opcion == '1':
            monto = float(input("Ingrese el monto de la transacción: "))
            fecha = datetime.now()
            descripcion = input("Ingrese una descripción para la transacción: ")
            tipo = input("Ingrese el tipo de transacción (Ingreso/Gasto): ")
            transaccion = Transaccion(monto, fecha, descripcion, tipo)
            gestor.agregar_transaccion(transaccion)
            gestor.guardar_datos()
            print("Transacción agregada con éxito.")
        elif opcion == '2':
            print("Listado de Transacciones:")
            gestor.ver_transacciones()
        elif opcion == '3':
            print("Ver Transacciones:")
            gestor.ver_transacciones()
        elif opcion == '4':
            indice = int(input("Ingrese el índice de la transacción que desea editar: "))
            monto = float(input("Ingrese el nuevo monto de la transacción: "))
            fecha = datetime.now()
            descripcion = input("Ingrese la nueva descripción para la transacción: ")
            tipo = input("Ingrese el nuevo tipo de transacción (Ingreso/Gasto): ")
            nueva_transaccion = Transaccion(monto, fecha, descripcion, tipo)
            gestor.editar_transaccion(indice - 1, nueva_transaccion)
            gestor.guardar_datos()
        elif opcion == '5':
            indice = int(input("Ingrese el índice de la transacción que desea eliminar: "))
            gestor.eliminar_transaccion(indice - 1)
            gestor.guardar_datos()
        elif opcion == '6':
            print("Balance Financiero:")
            gestor.calcular_balance()
        elif opcion == '7':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()
