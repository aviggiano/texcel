#!/usr/bin/python
# -*- coding:utf8 -*-

import re
import os
import errno
from array import *
import codecs

def do_the_change(all_arroba):
	i_0 = 0
	hasChanged = False
	all_arroba2 = []

	for i in all_arroba:
		if re.findall(r'@\d+', i, re.U):
			if not hasChanged:
				i_0 = re.sub(r'@(\d+)', r'\1', i)
				all_arroba2.append(i)
			else:
				i_0 = str(int(i_0)+1)
				i = re.sub(r'@(\d+)', '@'+str(int(i_0)+1), i)
				all_arroba2.append(i)
		else:
			i = re.sub(r'@(change)', '@'+str(int(i_0)+1), i)
			all_arroba2.append(i)
			hasChanged = True

	return all_arroba2

def do_the_plus_1 (to_change):
	ans = []
	for i in to_change:
		i = re.sub(r'@(\d+)', r'\1', i)
		ans.append('@'+str(int(i)+1))
	return ans


print "Reading input latex..."

latex_input_filename = 'input-tex+1.tex'
latex_file = open(latex_input_filename, 'r')
latex_lines = latex_file.readlines()
print "Success. Latex file in memory."

latex_output_filename = latex_input_filename + "(temp).tex"
output_file = open(latex_output_filename, 'w');


print "Refactoring latex..."
index_db = 1
changeFound = False

for i in range(len(latex_lines)):
	plus_1 = re.findall(r'@change', latex_lines[i], re.U)
	if (len (plus_1) == 0 and not changeFound):
		output_file.write(latex_lines[i])
	elif (not changeFound):
		to_change = re.findall(r'@\d+|@change', latex_lines[i], re.U)
		all_arroba = re.findall(r'@\d+|@change', latex_lines[i], re.U)
		all_arroba = do_the_change(all_arroba)

		to_be_written = latex_lines[i].decode('utf8')
		change_to = all_arroba

		ii = 0
		to_change.reverse()
		change_to.reverse()
		for i in to_change:
			#print to_be_written + '\n'
			to_be_written = re.sub(i, change_to[ii], to_be_written)
			ii += 1
		output_file.write(to_be_written.encode('utf8'))
		changeFound = True
	elif (changeFound):
		to_change = re.findall(r'@\d+', latex_lines[i], re.U)
		to_change.reverse()
		change_to = do_the_plus_1 (to_change)

		ii = 0
		to_be_written = latex_lines[i].decode('utf8')
		for i in to_change:
			to_be_written = re.sub(i, change_to[ii], to_be_written)
			ii += 1
		output_file.write(to_be_written.encode('utf8'))

latex_file.close()

print "Success. Written on latex."



