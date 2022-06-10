import sys
import re

file_name = sys.argv[1]
with open(file_name, 'r') as f:
	lines = f.readlines()

States = []
Sigma = []
Gamma = []
start_state = []
accept_state = []
reject_state = []
Transitions = []

i = 0
while i < len(lines):
	linia_curenta = lines[i].strip()
	if len(linia_curenta) > 2 and linia_curenta[0] + linia_curenta[1] == '//':
		i += 1
		continue
	elif linia_curenta == 'States:':
		i += 1
		linia_curenta = lines[i].strip()
		while linia_curenta != 'End':
			if len(linia_curenta) > 2 and linia_curenta[0] + linia_curenta[1] == '//':
				i += 1
				linia_curenta = lines[i].strip()
				continue

			parts = re.split('\s*,\s*', linia_curenta)
			States.append(int(parts[0]))
			if len(parts) == 2:
				if parts[1] == 'S':
					start_state.append(int(parts[0]))
				elif parts[1] == 'accept':
					accept_state.append(int(parts[0]))
				elif parts[1] == 'reject':
					reject_state.append(int(parts[0]))

			i += 1
			linia_curenta = lines[i].strip()
	elif linia_curenta == 'Sigma:':
		i += 1
		linia_curenta = lines[i].strip()
		while linia_curenta != 'End':
			if len(linia_curenta) > 2 and linia_curenta[0] + linia_curenta[1] == '//':
				i += 1
				linia_curenta = lines[i].strip()
				continue

			Sigma.append(linia_curenta)
			i += 1
			linia_curenta = lines[i].strip()
	elif linia_curenta == 'Gamma:':
		i += 1
		linia_curenta = lines[i].strip()
		while linia_curenta != 'End':
			if len(linia_curenta) > 2 and linia_curenta[0] + linia_curenta[1] == '//':
				i += 1
				linia_curenta = lines[i].strip()
				continue

			Gamma.append(linia_curenta)
			i += 1
			linia_curenta = lines[i].strip()
	elif linia_curenta == 'Transitions:':
		i += 1
		linia_curenta = lines[i].strip()
		while linia_curenta != 'End':
			if len(linia_curenta) > 2 and linia_curenta[0] + linia_curenta[1] == '//':
				i += 1
				linia_curenta = lines[i].strip()
				continue

			s1, s2, r = re.split('\s*,\s*',linia_curenta, maxsplit=2)
			r_parts = re.split('\s*\|\s*', r)
			for part in r_parts:
				a, bc = re.split('\s*->\s*', part)
				b, c = re.split('\s*,\s*', bc)
				Transitions.append((int(s1), int(s2), a, b, c))
			
			i += 1
			linia_curenta = lines[i].strip()
	i += 1


# print(States)
# print(start_state)
# print(accept_state)
# print(reject_state)
# print(Sigma)
# print(Gamma)
# print(Transitions)

tm_valid = True
if len(start_state) != 1 or len(accept_state) != 1 or len(reject_state) != 1:
	tm_valid = False
elif accept_state == reject_state:
	tm_valid = False
elif '_' in Sigma:
	tm_valid = False
elif '_' not in Gamma:
	tm_valid = False
for symbol in Sigma:
	if symbol not in Gamma:
		tm_valid = False
for s1, s2, i, b, d in Transitions:
	if s1 not in States:
		tm_valid = False
	elif s2 not in States:
		tm_valid = False
	elif i not in Gamma:
		tm_valid = False
	elif b not in Gamma:
		tm_valid = False
	elif d != 'R' and d != 'L':
		tm_valid = False

if tm_valid:
	print("TM config file is valid")
else:
	print("TM config file is not valid")
