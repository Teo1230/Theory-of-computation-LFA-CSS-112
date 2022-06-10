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
# print('-----------------------------------')

# phase 1
w1 = []   
for var, string in Rules:
	for symbol in string:
		if symbol in Terminals and var not in w1:
			w1.append(var)

w2 = []
while True:
	w2 = [x for x in w1]
	for var, string in Rules:
		for symbol in string:
			if symbol in w1 and var not in w2:
				w2.append(var)
	if w1 == w2: 
		break
	w1 = [x for x in w2]
	w2 = []	


new_rules = []
for var, string in Rules:
	if var in w1:
		ok = True
		for symbol in string:
			if symbol not in w1 and symbol not in Terminals:
				ok = False
		if ok:
			new_rules.append((var, string))

# print(w1)
# print(Terminals)
# print(new_rules)

# phase 2
# print('------------------------------')
y1 = [*start_variable]

while True:
	y2 = [x for x in y1]
	for var, string in new_rules:
		if var in y1:
			for symbol in string: 
				if symbol not in y2:
					y2.append(symbol)
	if y1 == y2:
		break
	y1 = [x for x in y2]
	y2 = []

# print(y1)

final_variables = []
final_terminals = []
final_rules = []

for symbol in y1:
	if symbol in Variables:
		final_variables.append(symbol)
	elif symbol in Terminals:
		final_terminals.append(symbol)

for var, string in Rules:
	if var in final_variables:
		ok = True
		for symbol in string:
			if symbol not in final_variables and symbol not in final_terminals:
				ok = False
		if ok:
			final_rules.append((var, string))

# print(final_variables)
# print(final_terminals)
# print(final_rules)

with open('cfg_config_file_reduction', 'w') as f:
	f.write('Variables:\n')
	for var in final_variables:
		if var in start_variable:
			f.write(f'	{var}, S\n')
		else:
			f.write(f'	{var}\n')
	f.write('End\n')
	f.write('Terminals:\n')
	for ter in final_terminals:
		f.write(f'	{ter}\n')
	f.write('End\n')
	f.write('Rules:\n')
	for var, string in final_rules:
		f.write(f'	{var} -> {string}\n')
	f.write('End\n')

