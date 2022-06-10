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

# print(Variables)
# print(start_variable)
# print(Terminals)
# print(Rules)

if cfg_valid:
	print('CFG config file is valid')
else:
	print('CFG config file is not valid')
	


	


