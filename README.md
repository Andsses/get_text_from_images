## Description

Extracts text from a set of images and converts it to .docx
All the .docx files will be added in a .zip where later the script will ask us if we want to send it by email

## REQUIRES
* [Tesseract - OCR](https://github.com/UB-Mannheim/tesseract/wiki)

## How to use
This project works as follows:
* Converts the extracted text and saves it to a .docx file
* Use Tesseract - OCR technology.
* Convert all .docx files into a .zip
* Send the .zip via STMP to an email

## Summary
In the images folder we place the images that we want to extract the text.

## Setup
To run this project, install it locally using npm:

```
$ cd ../get_text_from_images
$ npm install 
$ npm start
