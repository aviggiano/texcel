#!/usr/bin/python
# -*- coding:utf8 -*-

import re
import os
import errno
from array import *
import codecs


#1. ler o .csv e estocar numa 'matriz'
#2. ver quais sao os directories a serem criados e cria-los, assim como estocar o nome de saida dos .tex (e coloca-los nessas pastas), etc
#3. ler o .tex e para cada regular expression, substutuir nos outputs das linguas respectivas --> deve levar em conta uma busca sequencial circular !!!!!!!! vide problema descrito em *
#4. assim que tiver o output completamente substituido e written, executar comando para passar o .tex para .pdf

#1. Reads input (excel, odt, etc.)
print "1. Reading database..."

database_file_name = 'input.csv'
database = open(database_file_name, 'r')
database = database.read()
 
database = database.split('\n')
database_matrix = []
control = []
count = 0
for i in database:
	i = i.replace('\r', '')
	database_matrix.append(i.split(';'))
	if (count <= 10):
		control.append(database_matrix[count])
	count += 1
print "Success. Database in memory."

print "Creating directories..."
# PDF dir
directories = []
filenames = []
for i in control:
	print i
	if (i[1] == 'pdfdir'):
		directories = i
	if (i[1] == 'filename'):
		filenames = i;

count = 2
while (count < len(directories)):
	try:
		os.makedirs(directories[count])
	except OSError as e:
		if e.errno == errno.EEXIST: #path already exists
			#do nothing --->>> change?	
			count += 1
print "Success. Directories created."			

print "Success. Output latex files on folders."

print "\n3. Reading input latex..."

latex_file_name = 'input-tex.tex'
latex_file = open(latex_file_name, 'r')
latex_lines = latex_file.readlines()
print "Success. Latex file in memory."

print "\nRefactoring latex..."
index_db = 1

index_language = 2;
while( index_language < len(directories) ):
	separator = "/"
	extension = ".tex"
	output_file_name = directories[index_language]+ separator + filenames[index_language] + extension
	output_file = open(output_file_name, 'w')
	for i in range(len(latex_lines)):
		to_change = re.findall(r'@\d+', latex_lines[i], re.U)
		if (len (to_change) == 0):
			output_file.write(latex_lines[i])
		else:
			j = 0
			to_be_written = latex_lines[i].decode('utf8')
			while (j < len(to_change)):
				index = int(re.sub('@','',to_change[j]))
				change_to =  database_matrix[index][index_language].decode('unicode-escape')
				to_be_written = re.sub(to_change[j], change_to, to_be_written)
				j+= 1
			print to_change[0] + ' ---> ' + to_be_written
			output_file.write(to_be_written.encode('utf8'))
	index_language += 1;

latex_file.close()
output_file.close()

print "Success. Written on latex."

print "Falta : rodar pdftex"
