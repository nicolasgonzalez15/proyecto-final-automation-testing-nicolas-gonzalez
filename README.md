# QA Automation - Sauce Demo - Entrega Final
Proyecto Final de QA Automation Testing, basado en el sitio de Sauce Demo, utilizando pytest, selenium webdriver y Python

## Propósito del proyecto
Con el fin de ahorrar tiempo y recursos, se quiere automatizar flujos críticos de módulos de:
 - Pantalla de Login, utilizando datos válidos e inválidos
 - Menú principal, con submenues, filtros, y catálogo de productos
 - Carrito de compras, al agregar productos al mismo
 - API Rest Testing - utilizando sitio de ReqRes

## Tecnologías usadas
* Python
* Selenium webdriver (Levantar browser automatizado)
* pytest (test unitarios)
* requests (API Test)
* Importación de datos, mediante CSV y JSON
* logger (obtener logs / auditoría)

## Estructura de carpetas

- **README.md**
- **pytest.ini** (Configuraciones iniciales pytest)
- **conftest.py** (Fixtures para diferentes tipos de browsers / prueba de Login reutilizable / fixture)
- **run_tests.py** (Archivo python para correr todos los tests juntos / ejecutar reportes)
- **datos/**
    - **data_login.csv** (Archivo CSV con datos a importar en test de login)
    - **productos.json** (Archivo JSON con datos a importar en test de cart json)
- **logs/**
    - **suite.log** (Archivo de logs - auditoría de sistema)
- **pages/**
    - **cart_page.py** (Archivo con métodos y definición de clase tipo Cart, para reutilizar en tests)
    - **inventory_page.py** (Archivo con métodos y definición de clase tipo Inventory, para reutilizar en tests)
    - **login_page.py** (Archivo con métodos y definición de clase tipo Login, para reutilizar en tests / conftest.py)
- **utils/**
    - **datos.py** (Archivo python para leer datos de un archivo CSV)
    - **lector_json.py** (Archivo python con lector de datos de un archivo json) 
    - **logger.py** (Archivo python para crear recolector de logs)
- **reports/** 
  - **report.html** (Reporte de ejecuciones de tests unitarios con pytest-html)
- **tests/**
    - **test_login.py** (tests de login exitoso / lectura de archivo CSV / uso de parametrización de usuarios)
    - **test_inventory.py** (tests de login y agregar productos desde Inventory exitoso)
    - **test_cart.py** (tests de login / agregar productos desde Inventory / verificar carrito exitoso)
    - **test_cart_json.py** (tests de login / agregar productos desde Inventory / verificar carrito exitoso, utilizando productos de archivo JSON)
    - **test_api_reqres.py** (tests de distintos tipos de peticiones a api Reqres / GET - POST - DELETE)

## Ejecutar todas las pruebas
Para iniciar la ejecucion de las pruebas debes ejecutar la siguiente linea:

```bash
python -m run_tests.py
```

## ¿Como interpretar los reportes?
- Al ejecutar `run_test.py`, se genera un archivo HTML en la carpeta raiz.
- El reporte incluye:
    - Lista completa de test ejecutados
    - El estado de cada prueba
    - La duracion de cada test
    - Las capturas de pantalla para pruebas fallidas

### Conclusion
Este proyecto ofrece una estructura organizada y escalable para automatizar pruebas de API utilizando Python y Pytest. Incluye un flujo simple de ejeucion mediante `run_tests.py`, generacion automatica de reporte HTML facilitando el analisis de las pruebas.
