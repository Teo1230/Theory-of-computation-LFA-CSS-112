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

input = sys.argv[2] + '_'
tape = input + '_'

accept_state = accept_state[0]
reject_state = reject_state[0]
index = 0	# locul unde este capul masinii
state = start_state[0]
# print(tape)
while state != accept_state and state != reject_state:
	for s1, s2, r, w, m in Transitions:
		if s1 == state and r == tape[index]:
			state = s2
			tape = tape[:index] + w + tape[index + 1:] 
			if m == 'R':
				index += 1
			else: 
				index -= 1
			if index < 0:
				index = 0
			if index >= len(input):
				index = len(input) -1
			# print(tape)
			break

if state == accept_state:
	print('input accepted')
elif state == reject_state:
	print('input rejected')


