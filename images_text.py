from PIL import Image
from pytesseract import *
from docx import Document
from email.message import EmailMessage
import smtplib
import os
import glob
import time
import zipfile
import sys

global ruta_de_texto , ruta_guardado_docx , ruta_zip , images_carp 

pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' # it sets the path of the tesseract.exe
clear = lambda: os.system('cls')
os.makedirs('images', exist_ok = True)

dir_proyect = os.path.dirname(os.path.abspath(__file__))
ruta_guardado_docx = dir_proyect + "\\documents\\"
ruta_de_texto = dir_proyect + "\\cache\\"
ruta_zip = dir_proyect + "\\zip\\"
images_carp = dir_proyect + "\\images\\"
if len(os.listdir(images_carp)) == 0:
	print("There are no images to process"),time.sleep(3)
	exit()

def crea_work(): # it creates a new document .docx
    doc = Document() 
    with open(ruta_de_texto + nombre + ".txt", 'r', encoding='UTF-8') as openfile:
        line = openfile.read()
        doc.add_paragraph(line)
        doc.save(ruta_guardado_docx + nombre + ".docx")
        return

def eliminina_primera_linea():
	with open (ruta_de_texto + nombre + ".txt", 'r+', encoding='UTF-8') as s:
		lines = s.readlines()
		s.seek(0)
		s.truncate()
		s.writelines(lines[1:])
		s.close()
		return

def crea_zip():
	fantasy_zip = zipfile.ZipFile(ruta_zip+'documents.zip', 'w') # it creates a zip file
	for folder, subfolders, files in os.walk(ruta_guardado_docx): # it copies the images to the images folder
		for file in files:
			if file.endswith('.docx'):
				fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), ruta_guardado_docx), compress_type=zipfile.ZIP_DEFLATED)
		fantasy_zip.close()
	return
	
def es_captura():
	with open(ruta_de_texto + nombre + ".txt",'r+', encoding='UTF-8') as s:
		for line in s:
			try:
				hora, minutos = line.split(':')
			except :
				s.close()
				return False
			solo = minutos[0:2]
			if type(int(hora)) == int and type(int(solo)) == int:
				s.close()
				return True
			else:
				s.close()
				return False

def clear_cache():
	try:
		os.system("rmdir /s /q " + ruta_de_texto)
	except:
		exit()
	return

def send_email():
	sender = "text.from.images@gmail.com"  # it sets the email of the sender  : Sdhywy@sd PASSWORD
	addressee = "defoxec446@offsala.com"
	message = "¡Hola, mundo!"

	email = EmailMessage()
	email["From"] = sender
	email["To"] = addressee
	email["Subject"] = "Correo de prueba"
	email.set_content(message)
	email.add_attachment(open(ruta_zip + "documents" + ".zip", "rb").read(), maintype="application", subtype="octet-stream", filename="documents.zip")
	smtp = smtplib.SMTP_SSL("smtp.gmail.com")
		
	smtp.login(sender, "snqvohnvhpuphprf")  
	smtp.sendmail(sender, addressee, email.as_string())
	smtp.quit()
	return True

def main():
	imagenes = glob.glob(images_carp + '/*.png')
	imagenes = glob.glob(images_carp + '/*.jpg')
	imagenes = glob.glob(images_carp + '/*.jpeg')

	os.makedirs('cache', exist_ok = True),os.makedirs('zip', exist_ok = True),os.makedirs('documents', exist_ok = True),os.system( "attrib +h cache" ) # it hides the cache folder

	contador = 0
	global nombre
	
	for imagen in imagenes:
		jpeg = Image.open(imagen)
		try:
			nombre = os.path.basename(imagen)
		except:
			print("Don't have images in the folder")
			exit()
		text = image_to_string(jpeg)
		clear()
		contador += 1
		print(text)
		print("Name: " + nombre)
		print("Images uploaded: " + str(contador) + "/"  + str(len(imagenes)))
		with open(ruta_de_texto + nombre + ".txt", 'w+', encoding='UTF-8') as openfile:
			openfile.write(text)
			openfile.close()
		if es_captura() == True:
			eliminina_primera_linea()
		else:
			pass
		crea_work()
	return True

if __name__ == '__main__':
	if main() == True:
		crea_zip()
		clear_cache()
		x = input("Send .zip via email? (Y/N): ")
		if x == "Y" or x == "y":
			if send_email() == True:
				clear()
				print("Email sent")
			else:
				clear()
				print("Error sending email")
				sys.exit()
		else:
			sys.exit()
	else:
		sys.exit()
		
'''

Developed by: @Andsses

Language Programming: Python 3.7.3

Github: https://github.com/Andsses

'''