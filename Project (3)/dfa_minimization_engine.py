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
            Transitions.append([int(lin[0]), int(lin[2].rstrip('\n')), lin[1]])

            i += 1

    i += 1


f.close()

n=len(States)
matrice=[['x' for i in range(n)] for j in range(n)]


def functie( cheie, litera):
    for s1,s2,l in Transitions:
        if s1==cheie and l==litera:
            return s2
    return  None
d={}
for i in range(n):
    key=i
    d[key]=[]
    for l in Sigma:
        if l not in d[key]:
            cheie=l
            s={}
            s[cheie]=functie(key,cheie)
            if(s[cheie]!=None):

                d[key].append(s )

for i in range(n):
    for j in range(n):
        if i > j:
            if i not in FS and j in FS or i in FS and j not in FS:
                matrice[i][j]=1
            else:
                matrice[i][j]=0

ok=1
while ok:
    ok=0
    for i in range(n):
        for j in range(n):
            if i > j:
                if matrice[i][j]==0:
                        contor=0
                        s1=d[i]
                        s2=d[j]
                        #print(s1,s2)
                        while(contor<len(Sigma)):
                            l1=s1[contor]
                            l2=s2[contor]
                            if matrice[l1[Sigma[contor]]][l2[Sigma[contor]]]==1 or  matrice[l2[Sigma[contor]]][l1[Sigma[contor]]]==1:
                                matrice[i][j]=1
                                ok=1
                            contor+=1

stariscoase=[]
starenoua=max(States)

TransitionsNew=[]
for i in range(n):
    for j in range(n):
        if matrice[i][j]==0:

            for s1, s2, l in Transitions:


                if s1 == i or s1==j:
                    if [i,j] not in stariscoase:
                        stariscoase.append([i, j])
                #     if (starenoua, s2, l) not in TransitionsNew:
                #         TransitionsNew.append((starenoua, s2, l))
                if s2==i or s2==j:
                    if [i, j] not in stariscoase:
                        stariscoase.append([i, j])
                #     if (s1, starenoua, l) not in TransitionsNew:
                #         TransitionsNew.append((s1, starenoua, l))
            #States.append((i,j,starenoua)
            # stariscoase.append([i,j])
            # States.remove(i)
            # States.remove(j)

n=len(stariscoase)
i=1
while i<n:

    for j in range(i):
        if stariscoase[i][0] == stariscoase[i][1] in stariscoase[j]:
            stariscoase=stariscoase[:i]+stariscoase[i+1:]
            n-=1
            i-=1
        elif stariscoase[i][0] in stariscoase[j]:
            stariscoase[j].append(stariscoase[i][1])
            stariscoase=stariscoase[:i]+stariscoase[i+1:]
            n=n-1
            i-=1
        elif stariscoase[i][1] in stariscoase[j]:
            stariscoase[j].append(stariscoase[i][0])
            stariscoase=stariscoase[:i] +stariscoase[i+1:]
            n=n-1
            i-=1
    i+=1
stariscoase=[list(set(i)) for i in stariscoase]

ss=[]
for i in range(len(stariscoase)):
    for j in range(len(stariscoase[i])):
        ss.append(stariscoase[i][j])
StariNew=[]
for i in States:
    if i not in ss:
        StariNew.append([i])


starifinale=[]
for i in range(len(stariscoase)):
    starenoua+=1
    for j in range(len(stariscoase[i])):
        for k in Transitions:
            if stariscoase[i][j]==k[0]:
                k[0]=starenoua
            if stariscoase[i][j]==k[1]:
                k[1] = starenoua
            if stariscoase[i][j] in IS:
                if [starenoua,'S'] not in StariNew:
                    StariNew.append([starenoua,'S'])
            if stariscoase[i][j] in FS:
                if [starenoua,'F'] not in StariNew:
                    StariNew.append([starenoua,'F'])

for i in Transitions:
    if i not in TransitionsNew:
        TransitionsNew.append(i)
TransitionsNew=sorted(TransitionsNew)

f=open("dfa_config_file_minimized","w")
f.write("Sigma:\n")
for i in Sigma:
    f.write(f"{i}",)
    f.write('\n')
f.write("End\n")
f.write("States:\n")
for i in range(len(StariNew)):
    for j in range(len(StariNew[i])):
        if j<len(StariNew[i])-1:
            f.write(f"{StariNew[i][j]}, ")
        else:
            f.write(f"{StariNew[i][j]}")
    f.write('\n')
f.write("End\n")
f.write("Transitions:\n")
for i in range(len(TransitionsNew)):
    for j in range(len(TransitionsNew[i])):
            if(j<len(TransitionsNew[i])-1):
                f.write(f"{TransitionsNew[i][j]}, ")
            else:
                f.write(f"{TransitionsNew[i][j]}")
    f.write('\n')
f.write("End\n")
f.close()
