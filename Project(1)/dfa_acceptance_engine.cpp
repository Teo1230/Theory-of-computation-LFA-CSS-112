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
int returnpozlinieinsigma( char s[100][100], char t[], int nr_litere)
{

	int i,j;
	for(i=0;i<nr_litere;i++)
		if(strcmp(s[i],t)==0)
			return i;
return 0;
}
int einstarefinale(int x, char FS[100][100],int n)
{
	for(int i=0; i<n;i++)
	if(x == (int)(FS[i]-'a'))
		return 1;
	return 0;
}
int convcharint(char s[])
{
    int i,nr=0,p=1;
    for(i=strlen(s)-1;i>=0;i--)
    {
        nr=nr+(s[i]-'0')*p;
        p*=10;
    }
    return nr;
}
int main(int argc, char *argv[]) {
	ifstream f(argv[1]);

	char cuvant[100];
	strcpy(cuvant, argv[2]);
    

	char Sigma[100][100], States[100][100], IS[10], FS[100][100];
	int nr_stari = 0;
	int stari_init = 0;
	int stari_finale = 0;
	int nr_litere = 0;
	
	char mat[100][100];
	for (int i = 0; i < 100; i++)
		for (int j = 0; j < 100; j++)
			mat[i][j] = '\0';

 
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
				
            	int poz=cautav(l);

            	if(numara(l)>1) {
            	    l[poz-2]=0;
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
		}

		if (strcmp(l, "Transitions:") == 0) {
			f.getline(l, 256);
			while (strcmp(l, "End") != 0 ) {
				if (l[0] == '#') {
					f.getline(l, 256);
					continue;
				}

				char *p = strtok(l, " ,");
				int q1, q2, k = 3;
				char t;
        		while(p)
        		{
        		    if(k==3) {
						//fara spatiu gen 0, 1, a -> am considerat ca e 0,1,a
        		        //cout<<*p-'0'<<" ";
						if (verif(States, nr_stari, p)) {
							q1 = *p - '0';
						}
						 
					}
        		    if(k==2) {
						//cout<<p<<" ";
						if (verif(Sigma, nr_litere, p)) {
							t = *p;
						}
						 
					}

        		    if(k==1)
        		    {	//j=*p-'0';
        		        //cout<<j<<endl;

						if (verif(States, nr_stari, p)) {
							q2 = *p - '0';
						}
						 
        		        //m[i][j]=*p;
        		    }

        		    k--;
        		    p=strtok(NULL,", ");
        		}
				//cout << q1 << " " << q2 << " " << t << endl;
				 
						mat[q1][q2] = t;
				f.getline(l, 256);

				 
			}
		}

	}
	
    int i=convcharint(IS),k=0,n=strlen(cuvant);
	//cout << i << endl;
    bool ok;
    while(k<n)
    {
        ok=0;
        for(int j=0;j<nr_stari;j++)
            if(mat[i][j] == cuvant[k] )
                {  //cout<<i<<":"<<j<<endl;
                    i=j;
                    ok=1;
                    k++;
					//cout<<i<<"undesar";
                    break;  
                }
        if(ok==0)
            break;
    }

		

    if(ok==1 && einstarefinale(i,FS,stari_finale))
    	cout<<"Cuvant acceptat" << endl;
    else 
		cout<<"Cuvant neacceptat" << endl;
	return 0; 
}