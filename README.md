Iliana Jiménez Murillo / Cohort 20

Nombre de proyecto: Automatización de solicitud de taxi 
                    para la App Urban Routes


Descripción:

El proyecto de automatización tiene como objetivo crear pruebas automatizadas para 
comprobar la funcionalidad del proceso de solicitud de un taxi en la plataforma Urban Routes.

Instrucciones:
1. Clona el repositorio en tu computadora
2. Trabaja con el proyecto de forma local
3. Escribe tus pruebas en el archivo main.py
4. Define los localizadores y métodos necesarios en la clase UrbanRoutesPage y 
las pruebas en la clase TestUrbanRoutes.
5. Escribe pruebas automatizadas que cubran el proceso completo de pedir un taxi.


Tecnologías:
PyCharm
GitHub
Selenium
Pytest

Técnicas utilizadas:
main.py
data.py
.gitignore
Urban_RoutesPage.py
SMS.py
README.md

Instrucciones detalladas para ejecutar las pruebas

1. Configurar la dirección: def test_set_route(self): 
Configura y verifica la configuración de la ruta.

2. Seleccionar la tarifa Comfort: def test_pick_comfort(self): 
Selecciona y valida la selección de la tarifa Comfort.

3. Rellenar el número de teléfono: def test_set_phone_number(self): 
Ingresa y comprueba la introducción del número de teléfono.

4. Agregar una tarjeta de crédito: def test_set_payment(self): 
Ejecuta y revisa la configuración de los métodos de pago.

5. Escribir un mensaje para el controlador: def test_set_message(self):
Ingresa y confirma la inclusión de un mensaje personalizado.

6. Pedir una manta y pañuelos: def test_set_requirements(self): 
Da clic y valida la configuración de los requisitos adicionales.

7. Pedir 2 helados: def test_call_taxi(self): 
Realiza la llamada al taxi y se verifica que se haya ejecutado la orden.

8. Aparece el modal para buscar un taxi: def test_wait_driver_details(self): 
Verifica la recepción de los detalles del conductor y que el viaje haya sido tomado.


