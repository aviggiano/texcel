#!/usr/bin/python
# -*- coding:utf8 -*-

import re
import os
import errno
from array import *
import codecs

print "Reading input latex..."

latex_file_name = 'input-tex+1.tex'
latex_file = open(latex_file_name, 'r')
latex_lines = latex_file.readlines()
print "Success. Latex file in memory."

print "Refactoring latex..."
index_db = 1

for i in range(len(latex_lines)):
	plus_1 = re.findall(r'@+', latex_lines[i], re.U)
	if (len (plus_1) == 0):
		output_file.write(latex_lines[i])
	else:
		j = 0
		to_be_written = latex_lines[i].decode('utf8')
		@@@@CHANGE
		@@@@ faire un rm du .tex dernier
		while (j < len(to_change)):
			index = int(re.sub('@','',to_change[j]))
			change_to =  database_matrix[index][index_language].decode('unicode-escape')
			to_be_written = re.sub(to_change[j], change_to, to_be_written)
			j+= 1
		print to_change[0] + ' ---> ' + to_be_written
		output_file.write(to_be_written.encode('utf8'))

latex_file.close()

print "Success. Written on latex."

print "Falta : rodar pdftex"
