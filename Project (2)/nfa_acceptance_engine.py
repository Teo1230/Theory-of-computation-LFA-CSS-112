import sys
from collections import deque

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


word = sys.argv[2]
coada = deque()
coada.append([IS[0]])

while len(coada[0]) <= len(word):
	letter = word[len(coada[0]) - 1]
	ls = coada.popleft()
	for s1, s2, l in Transitions:
		if l == letter and ls[-1] == s1:
			aux = [e for e in ls]
			aux.append(s2)
			coada.append(aux)
ok = 0

for drum in coada:
	if drum[-1] in FS:
		ok = 1

if ok:
	print("Cuvant acceptat")
else:
	print("Cuvant neacceptat")
