import sys

file_name = sys.argv[1]

f = open(file_name)
lines = f.readlines()
f.close()

i = 0

Sigma = []
States = []
IS = []
FS = []
Transitions = []

while i < len(lines):
	if lines[i][0] == '#':
		i += 1
		continue
	elif lines[i] == "Sigma:\n":
		i += 1
		while lines[i] != "End\n":
			if lines[i][0] == '#':
				i += 1
				continue		
			Sigma.append(lines[i][0])
			i += 1
	elif lines[i] == "States:\n":
		i += 1
		while lines[i] != "End\n":
			if lines[i][0] == '#':
				i += 1
				continue
			lin = lines[i].split(", ")
			if len(lin) == 1:
				States.append(int(lin[0].rstrip('\n')))
			elif len(lin) == 2:
				States.append(int(lin[0]))
				if lin[1].rstrip('\n') == 'S':
					IS.append(int(lin[0].rstrip('\n')))
				else:
					FS.append(int(lin[0].rstrip('\n')))
			elif len(lin) == 3:
				States.append(int(lin[0]))
				IS.append(int(lin[0].rstrip('\n')))
				FS.append(int(lin[0].rstrip('\n')))

			i += 1
	elif lines[i] == "Transitions:\n":
		i += 1
		while lines[i] != "End\n":
			if lines[i][0] == '#':
				i += 1
				continue
			lin = lines[i].split(", ")
			Transitions.append((int(lin[0]), int(lin[2].rstrip('\n')), lin[1]))
		
			i += 1

	i += 1

nr_states = len(States)
new_transitions = []
new_states = [IS[0]]
states_comp = {}
new_fs = []

for s in States:
	states_comp[s] = [s]

for state in new_states:
	for letter in Sigma:
		new_state = []
		for tr in Transitions:
			for s in states_comp[state]:
				if tr[0] == s and tr[2] == letter:
					new_state.append(tr[1])
		
		if len(new_state) > 1:
			new_state = sorted(list(dict.fromkeys(new_state)))  #sortez starile si elimin duplicatele
			
			for s in states_comp:
				if states_comp[s] == new_state:
					new_transitions.append((state, letter, s))
			if new_state not in states_comp.values():
				new_states.append(nr_states)
				states_comp[nr_states] = new_state
				new_transitions.append((state, letter, nr_states))
				nr_states += 1
		
		elif len(new_state) == 1:
			for s in new_states:
				if s == new_state[0]:
					new_transitions.append((state, letter, s))
			if new_state[0] not in new_states:
				new_states.append(*new_state)
				new_transitions.append((state, letter, new_state[0]))

for state in new_states:
	for s in states_comp[state]:
		if s in FS and state not in new_fs:
			new_fs.append(state)

# print(Sigma)
# print(new_states)
# print(IS)
# print(new_fs)
# print(new_transitions)

with open("dfa_config_file", 'w') as f:
	f.write("Sigma:\n")
	for letter in Sigma:
		f.write(f"{letter}\n")
	f.write("End\n")

	f.write("States:\n")
	for state in new_states:
		if state in IS and state in new_fs:
			f.write(f"{state}, S, F\n")
		elif state in IS:
			f.write(f"{state}, S\n")
		elif state in new_fs:
			f.write(f"{state}, F\n")
		else:
			f.write(f"{state}\n")
		
	f.write("End\n")

	f.write("Transitions:\n")
	for tr in new_transitions:
		f.write(f"{tr[0]}, {tr[1]}, {tr[2]}\n")
	f.write("End\n")

