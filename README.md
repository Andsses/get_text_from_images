## Descripcion
Este proyecto es publicado ya que no me llego el pago de un estafador...

Extrae el texto de un conjunto de imagenes y lo convierte en .docx
Todos los archivos .docx se añadiran en un .zip donde despues nos preguntara el script si queremos enviarlo por email

## REQUIERE
* [Tesseract - OCR](https://github.com/UB-Mannheim/tesseract/wiki)

## Como Usar
Este proyecto funciona de la siguiente manera:
* Convierte el texto estraido y lo guarda en un archivo .docx
* Usa la tecnologia Tesseract - OCR.
* Convierte todos los archivos .docx en un .zip
* Enviar el .zip mediante STMP a un correo electronico

## Resumen
En la carpeta images colocamos las imagenes que vamos queremos extraer el texto.

## Setup
To run this project, install it locally using npm:

```
$ cd ../get_text_from_images
$ npm install 
$ npm start