Fisierul trebuie sa inculda 4 sectiuni:
	- "States": fiecare stare este reprezentata printr-un numar natural si este scrisa pe cate o linie. Starea initiala este marcata cu 
	simbolul "S" separat cu o virgula de numarul starii. Starea de accept este marcata de cuvantul "accept", separat cu o virgula de 
	numarul starii, iar starea de reject este marcata de cuvantul "reject". Trebuie sa exista doar cate una din aceste 3 stari.
	- "Sigma": fiecare simbol din alfabetul de input trebuie scris pe cate o linie. Simbolul gol "_" nu trebuie sa faca parte din aceasta sectiune.
	- "Gamma": fiecare simbol din alfabetul benzii trebuie scris pe cate o linie. Sectiunea trebuie sa includa "_" si toate simbolurile din "Sigma"
	- "Transitions": fiecare tranzitie trebuie scrisa pe cate o linie. Tranzitia este formata din 3 parti separate prin ','. Prima parte trebuie sa 
	precizeze starea din care pleaca tranzitia. A doua parte trebuie sa precizeze starea in care ajunge tranzitia. A treia parte trebuie 
	sa precizeze simbolul care se citeste, urmat de "->", apoi ceea ce se scrie pa banda, o virgula si directia in care se misca capul masinii,
	reprezentata prin "R" pentru dreapta si "L" pentru stanga. Daca intre doua stari exista mai multe tranzitii acestea pot fi scrie pe un singur rand,
	separate prin "|"
Fiecare sectiune se termina cu "End". Sectiunile pot fi in orice ordine.
Pentru a adauga  comentarii in fisier linia trebuie sa inceapa cu "//"
Simbolul "_" reprezinta simbolul gol.


Pentru a rula tm-ul cu un input folositi comanda: "python tm_acceptance_engine.py tm_config_file input"