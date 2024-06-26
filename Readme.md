# Sistema de Seguimiento de Gastos

BY: Diego Arteaga

## Descripción

Esta aplicación de terminal permite el seguimiento de gastos personales. Los usuarios pueden registrar sus ingresos y gastos, listar las transacciones ordenadas por fecha y generar un balance financiero que muestra el total de ingresos, gastos y la capacidad de ahorro.

## Características

- Agregar transacciones (ingresos y gastos).
- Listar todas las transacciones.
- Editar transacciones existentes.
- Eliminar transacciones.
- Mostrar el balance financiero actual.
- Guardar y cargar transacciones desde un archivo.

## Requisitos

- Python 3.6 o superior

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/DieGoArt30/Seguimiento_De_Gastos
    cd seguimiento-de-gastos
    ```

2. Ejecuta el programa:

    ```bash
    python seguimiento_de_gastos.py
    ```

## Uso

Sigue las instrucciones en pantalla para agregar, listar, editar, eliminar transacciones y mostrar el balance financiero.

![menu principal](https://github.com/DieGoArt30/Seguimiento_De_Gastos/assets/149025522/17d5af1c-cc32-45cd-9e91-cee0f1813413)
![listado de transacciones](https://github.com/DieGoArt30/Seguimiento_De_Gastos/assets/149025522/e2e21ab9-f083-451c-8bce-5143aaee5b04)

![ver transacciones](https://github.com/DieGoArt30/Seguimiento_De_Gastos/assets/149025522/4a279f4d-7d16-40b8-9557-d2fbc9e1591a)

![balance financiero](https://github.com/DieGoArt30/Seguimiento_De_Gastos/assets/149025522/2a4ab35c-554f-49ce-b82c-0b755d5f1adf)

![salida](https://github.com/DieGoArt30/Seguimiento_De_Gastos/assets/149025522/172aed01-6e1c-45a3-9f18-91bbf694a8b5)


## Estructura del Proyecto

- **seguimiento_de_gastos.py:** Archivo principal que contiene el código fuente de la aplicación.
- **datos_financieros.pkl:** Archivo binario donde se guardan las transacciones.

## Contribución

Si deseas contribuir al proyecto, por favor realiza un fork del repositorio y envía un pull request.

# Descripción de la Estructura del Proyecto y Decisiones de Diseño Importantes
## Clases y Métodos:

#### Transaccion: Esta clase representa una transacción individual. Cada transacción tiene un monto, una fecha, una descripción y un tipo (Ingreso/Gasto).
#### GestorTransacciones: Esta clase gestiona una lista de transacciones. Proporciona métodos para agregar, ver, editar, eliminar transacciones y calcular el balance financiero.
#### agregar_transaccion: Agrega una nueva transacción a la lista.
#### ver_transacciones: Muestra todas las transacciones.
#### editar_transaccion: Edita una transacción existente.
#### eliminar_transaccion: Elimina una transacción existente.
#### calcular_balance: Calcula y muestra los totales de ingresos, gastos y la capacidad de ahorro.
#### guardar_datos y cargar_datos: Métodos para guardar y cargar transacciones desde un archivo usando pickle.
#### Persistencia de Datos:

### Pickle: Se utiliza pickle para serializar y deserializar las transacciones, permitiendo guardar y cargar los datos de un archivo binario (datos_financieros.pkl).
### Interfaz de Usuario:

#### Terminal Interactiva: El programa proporciona un menú interactivo en la terminal para que el usuario pueda agregar, ver, editar, eliminar transacciones y mostrar el balance financiero.
## Decisiones de Diseño:

#### Uso de Clases: Se utilizan clases para encapsular la lógica relacionada con las transacciones y su gestión, lo que mejora la modularidad y la mantenibilidad del código.
#### Manejo de Errores: Se incluyen bloques try-except para manejar posibles errores al cargar los datos desde el archivo.
Fecha Automática: Las fechas de las transacciones se generan automáticamente en el momento de la creación de la transacción, lo que asegura la precisión y consistencia de los registros.

## Contacto:
Para cualquier consulta o sugerencia, por favor contacta a Diego Aeteaga a traves de diehgohhz.30@gmail.com

