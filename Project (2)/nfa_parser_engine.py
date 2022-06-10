import sys

file_name = sys.argv[1]

f = open(file_name)
lines = f.readlines()

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

# print(Sigma)
# print(States)
# print(IS)
# print(FS)
# print(Transitions)

f.close()

valid = True

if len(IS) != 1:
	valid = False

if len(FS) == 0:
	valid = False

for a, b, c in Transitions:
	if a not in States or b not in States or c not in Sigma:
		valid = False

if valid:
	print("NFA config file is valid")
else:
	print("NFA config file is not valid")

