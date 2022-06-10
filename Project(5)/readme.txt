Fisierul trebuie sa includa 3 sectiuni:
 - "Variables": In aceasta sectiune fiecare variabila a gramaticii va fi scrisa pe cate o linie, 
	variabila de start va fi marcata cu un litara "S" separata cu o virgula de simbolul variabilei
	(poate exista o singura variabila de start).
 - "Terminals": Fiecare terminal va fi scris pe cate o linie.
 - "Rules": Fiecare regula va fi scrisa pe cate o linie si este formata din o variabila si un string 
	separate printr-o "->". Stringul este format din variabile si terminale. Daca o variabila poate produce mai multe stringuri acestea pot fi scrise intr-o singura regula, stringurile fiind separate prin "|".
Fiecare sectiune se termina cu "End". Sectiunile pot fi in orice ordine.
Pentru a adauga  comentarii in fisier linia trebuie sa inceapa cu "//"
Simbolul "*" reprezinta epsilon.