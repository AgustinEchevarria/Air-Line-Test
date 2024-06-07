# Sistema de transporte de paquetes de aerolíneas

Este es un programa Python simple que simula un sistema de transporte de paquetes de aerolíneas. Le permite transportar paquetes para clientes y generar informes para una fecha específica, mostrando la cantidad total de paquetes transportados y la cantidad total recolectada.

## Archivos

- `test.py`: Contiene las pruebas unitarias para la clase `AirLine` y sus métodos.
- `main.py`: Proporciona una interfaz de línea de comandos interactiva para transportar paquetes y generar informes.
- `service.py`: Contiene la lógica central del sistema, incluidas las clases `Package`, `Client` y `AirLine`.

## Requisitos

- Python 3.x
- Datetime
- Unittest

## Instalación

1. Clone el repositorio o descargue el código fuente.
2. Navegue hasta el directorio del proyecto.

## Uso

1. Abra una terminal o un símbolo del sistema y navegue hasta el directorio del proyecto.
2. Ejecute el programa ejecutando el siguiente comando:

```
python main.py
```

3. Siga las instrucciones en pantalla para transportar paquetes o generar informes.

El programa mostrará la cantidad total de paquetes transportados y la cantidad total recolectada para la fecha especificada.

### Salir del programa

Para salir del programa, ingrese `'exit'` cuando se le solicite.

## Ejecutar pruebas unitarias

El programa incluye ejecucion de pruebas unitarias para garantizar la corrección de la clase `AirLine` y sus métodos.

```
python test.py
```

Las pruebas se ejecutarán y los resultados se mostrarán en la terminal.

## Estructura del código

### `test.py`

Este archivo contiene la clase `TestAirLine`, que hereda de `unittest.TestCase`. Incluye varios métodos de prueba para verificar la funcionalidad de la clase `AirLine` y sus métodos.

### `main.py`

Este archivo contiene la función `main()`, que proporciona la interfaz de línea de comandos interactiva para transportar paquetes y generar informes. Utiliza las clases definidas en `service.py`.

### `service.py`

Este archivo contiene la lógica central del sistema:

- Clase `Package`: Representa un paquete con un ID y un cliente.
- Clase `Client`: Representa un cliente con un nombre.
- Clase `AirLine`: Gestiona el transporte de paquetes y la generación de informes. Tiene los siguientes métodos:
- `transport(package, transport_date)`: Transporta un paquete en una fecha específica.
- `generate_report(report_date)`: Genera un informe para una fecha específica, mostrando el número total de paquetes transportados y la cantidad total recolectada.