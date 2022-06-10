import sys
import re

Variables = []
Terminals = []
Rules = []
start_variable = []

cfg_config_file = sys.argv[1]

with open(cfg_config_file, 'r') as f:
	lines = f.readlines()

i = 0
while i < len(lines):
	linia_curenta = lines[i].strip()
	if len(linia_curenta) > 2 and linia_curenta[0] + linia_curenta[1] == '//':
		i += 1
		continue
	elif linia_curenta == 'Variables:':
		i += 1
		linia_curenta = lines[i].strip()
		while linia_curenta != 'End':
			if len(linia_curenta) > 2 and linia_curenta[0] + linia_curenta[1] == '//':
				i += 1
				linia_curenta = lines[i].strip()
				continue

			parts = re.split('\s*,\s*', linia_curenta)
			Variables.append(parts[0])
			if len(parts) == 2:
				start_variable.append(parts[0])

			i += 1
			linia_curenta = lines[i].strip()
	elif linia_curenta == 'Terminals:':
		i += 1
		linia_curenta = lines[i].strip()
		while linia_curenta != 'End':
			if len(linia_curenta) > 2 and linia_curenta[0] + linia_curenta[1] == '//':
				i += 1
				linia_curenta = lines[i].strip()
				continue

			Terminals.append(linia_curenta)
			i += 1
			linia_curenta = lines[i].strip()
	elif linia_curenta == 'Rules:':
		i += 1
		linia_curenta = lines[i].strip()
		while linia_curenta != 'End':
			if len(linia_curenta) > 2 and linia_curenta[0] + linia_curenta[1] == '//':
				i += 1
				linia_curenta = lines[i].strip()
				continue

			parts = re.split('\s*->\s*',linia_curenta)
			str = re.split('\s*\|\s*', parts[1])
			for s in str:
				Rules.append((parts[0], s))

			i += 1
			linia_curenta = lines[i].strip()


	i += 1

cfg_valid = True

for var in Variables:
	if var in Terminals:
		cfg_valid = False

if len(start_variable) != 1:
	cfg_valid = False

for rule in Rules:
	if rule[0] not in Variables:
		cfg_valid = False
	for c in rule[1]:
		if c not in Variables and c not in Terminals:
			cfg_valid = False

lista=[]
for rule in Rules:
	if rule[1] =="*":
		lista.append(rule[0])
k=0
nou=[]
d={}
lista=sorted(lista)
for rule in Rules:
	if rule[0] in d:
		if rule[1] not in d[rule[0]]:
			d[rule[0]].append(rule[1])
	else:
		d[rule[0]] = []
		d[rule[0]].append(rule[1])
ct=0
for x in lista:
	for i in d:
		cuv=[]
		key=[]
		for j in d[i]:
			cuv=j
			y=""
			z=""
			for c in range(len(cuv)):
				if cuv not in key:
					key.append(cuv)
				if cuv[c]==x:
					key.append(y+cuv[c+1:])
					# print(y)
					y=y+cuv[c]
				else:
					y = y + cuv[c]
					z = z + cuv[c]
			key.append(z)
			# print(key)
			key = list(set(key))
			d[i] = key

for i in d:
	if '*' in d[i]:
		d[i].remove("*")
	if '' in d[i]:
		d[i].remove('')

with open("cfg_config_file_null_simplification","w") as f:
	f.write('Variables:\n')
	for var in Variables:
		if var in start_variable:
			f.write(f'	{var}, S\n')
		else:
			f.write(f'	{var}\n')
	f.write('End\n')
	f.write('Terminals:\n')
	for ter in Terminals:
		f.write(f'	{ter}\n')
	f.write('End\n')
	f.write("Rules:")
	f.write("\n")
	for i in d :
		f.write(f"	{i} -> ")
		for j in range(len(d[i])):
			# print(len(d[i]))
			if j== len(d[i])-1:
				f.write(f"{d[i][j]}")
				f.write('\n')
			elif j==0 and len(d[i])>1:
				f.write(f"{ d[i][j]} | ")
			elif j == 0 and len(d[i]) ==1:
				f.write(f"{d[i][j]}")
				f.write('\n')
			else:
				f.write(f"{d[i][j]} | ")
	f.write("End")