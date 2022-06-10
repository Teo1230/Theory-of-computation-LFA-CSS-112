#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

int cautav(char s[]) {
    for(int i=0; s[i]; i++)
        if(s[i]==',')
            return i+2;
    return 0;
}

int numara(char s[]) {
    int k=0;
    for(int i=0; s[i]; i++)
        if(s[i]==',')
            k++;
    return k;
}

int verif(char mat[100][100], int n, char p[]) {
	for (int i = 0; i < n; i++) 
		if (strcmp(p, mat[i]) == 0) 
			return 1;
		
	return 0;
}

int fv_lit_mat(char mat[100][100], int nr_stari) {
	for (int i = 0; i < nr_stari; i++) {
		int fv[256] = {0};
		for (int j = 0; j < nr_stari; j++) {
			if (mat[i][j] != '\0') {
				fv[mat[i][j]]++;
				if (fv[mat[i][j]] > 1)
					return 0;
			}
		}	
	}
	return 1;
}

int main(int argc, char *argv[]) {
	ifstream f(argv[1]);

	char Sigma[100][100], States[100][100], IS[10], FS[100][100], MatriceCuv[100][100];
	int nr_stari = 0;
	int stari_init = 0;
	int stari_finale = 0;
	int nr_litere = 0;
	
	char mat[100][100];
	for (int i = 0; i < 100; i++)
		for (int j = 0; j < 100; j++)
			mat[i][j] = '\0';

	int DFA_valid = 1;

	char l[256];
	while(f.getline(l, 256)) {
		if (l[0] == '#')
			continue;
		
		if(strcmp(l, "Sigma:") == 0) {
			
			f.getline(l, 256);
			while (strcmp(l, "End") != 0) {
				if (l[0] == '#') {
					f.getline(l, 256);
					continue;
				}
				
				strcpy(Sigma[nr_litere++], l);

				f.getline(l, 256);
			}
		}

		if (strcmp(l, "States:") == 0) {
			
			f.getline(l, 256);
			while (strcmp(l, "End") != 0) {
				if (l[0] == '#') {
					f.getline(l, 256);
					continue;
				}
				
            	int poz = cautav(l);

            	if(numara(l) > 1) {
            	    l[poz-2] = 0;
            	    strcpy(IS, l);
            	    stari_init++;

					strcpy(FS[stari_finale++], l);
            	    strcpy(States[nr_stari++], l);
            	}
            	else if(poz)
            	    if(l[poz]=='S') {
            	        l[poz-2]=0;
            	        strcpy(IS, l);
						stari_init++;
						strcpy(States[nr_stari++], l);
            	    }
            	    else {
            	        l[poz-2]=0;
            	        strcpy(FS[stari_finale++], l);
            	    	strcpy(States[nr_stari++], l);
            	    }
            	else {
            	    strcpy(States[nr_stari++], l);
            	}

				f.getline(l, 256);
			}

			if (stari_init != 1 || stari_finale == 0) {
				DFA_valid = 0;
				break;
			}
		}

		if (strcmp(l, "Transitions:") == 0) {
			f.getline(l, 256);
			while (strcmp(l, "End") != 0 && DFA_valid) {
				if (l[0] == '#') {
					f.getline(l, 256);
					continue;
				}

				char *p = strtok(l, " ,");
				int q1, q2, k = 3;
				char t[100];
        		while(p) {
        		    if(k==3) {
						if (verif(States, nr_stari, p)) {
							q1 = *p - '0';
						}
						else {
							DFA_valid = 0;
							break;
						}

					}
        		    if(k==2) {
						//cout<<p<<" ";
						if (verif(Sigma, nr_litere, p)) {
							strcpy(t, p);
						}
						else {
							DFA_valid = 0;
							break;
						}
					}

        		    if(k==1) {
						if (verif(States, nr_stari, p)) {
							q2 = *p - '0';
						}
						else {
							DFA_valid = 0;
							break;
						}
        		    }

        		    k--;
        		    p=strtok(NULL,", ");
        		}
				cout << q1 << " " << q2 << " " << t << endl;
				/*for(int i=0;i<nr_litere;i++)
					if(strcmp(t,Sigma[i])==0)
						cout<<i<<" "; */
				f.getline(l, 256); 
			}
		}

	}

	 
	if (fv_lit_mat(mat, nr_stari) != 1)
		DFA_valid = 0;

	if (DFA_valid) 
		cout << "DFA config file is valid" << endl;
	else
		cout << "DFA config file is not valid" << endl;	

	return 0; 
}