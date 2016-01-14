# LedMatrix4RPI
Proyecto de paneles led con raspberry pi.


Pasos para la instalación:

* Clonar el siguiente repositorio ```https://github.com/hzeller/rpi-rgb-led-matrix```
* Fabricar un cable acorde a estas especificaciones
* Modificar el fichero ```https://github.com/hzeller/rpi-rgb-led-matrix/blob/master/include/led-matrix.h#L65``` acorde a las necesidades del montaje.
* Sobre la carpeta principal del repo. Ejecutar make. Deberian de generarse diferentes ejecutables. El que interesa es ```led-matrix```


Server Python. Basado en generar imágenes ppm a partir de texto.
Pasos la instalación:
* Descargar jpegsrc.v8c.tar.gz: ```curl -O http://www.ijg.org/files/jpegsrc.v8c.tar.gz```
* Descomprimir: ```tar -xvzf jpegsrc.v8c.tar.gz```
* Ir al directorio: ```cd jpeg-8c```
* Configurar: ```./configure````
* Construir: ```make````
* Instalar dependencia: ```sudo make install```
* Descargar jpegsrc.v8c.tar.gz: ```curl -O http://ftp.igh.cnrs.fr/pub/nongnu/freetype/freetype-2.4.5.tar.gz```
* Descomprimir: ```tar -xvzf freetype-2.4.5.tar.gz```
* Ir al directorio: ```cd freetype-2.4.5 ```
* Configurar: ```./configure```
* Construir: ```make```
* Instalar dependencia: ```sudo make install```
* Instalar dependencias del backend: ```cd pythonBackend```
* ```sudo pip install -r requirements.txt```
* Ejecutar el server: ```sudo python app.py```
