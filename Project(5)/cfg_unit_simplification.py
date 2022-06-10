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


# print(Variables)
# print(start_variable)
# print(Terminals)
# print(Rules)


ok = False
while not ok:
	i = 0
	ok = True
	while i < len(Rules):
		if Rules[i][1] in Variables:
			ok = False			
			for var, string in Rules:
				if var == Rules[i][1]:
					Rules.append((Rules[i][0], string))
			Rules.remove(Rules[i])
			i -= 1
		i += 1

reacheable = [*start_variable]
for var, string in Rules:
	for symbol in string:
		if symbol in Variables and symbol not in reacheable:
			reacheable.append(symbol)

i = 0
while i < len(Rules):
	if Rules[i][0] not in reacheable:
		Rules.remove(Rules[i])
		i -= 1
	i += 1

# print(Rules)


with open('cfg_config_file_unit_productions_removed', 'w') as f:
	f.write('Variables:\n')
	for var in reacheable:
		if var in start_variable:
			f.write(f'	{var}, S\n')
		else:
			f.write(f'	{var}\n')
	f.write('End\n')
	f.write('Terminals:\n')
	for ter in Terminals:
		f.write(f'	{ter}\n')
	f.write('End\n')
	f.write('Rules:\n')
	for var, string in Rules:
		f.write(f'	{var} -> {string}\n')
	f.write('End\n')

