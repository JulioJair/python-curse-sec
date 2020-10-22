Algoritmo sort_numbers_nested
	Escribir 'Ingrese a,b,c'
	Leer a,b,c
	Si a>b Entonces
		Si a>c Entonces
			Si b>c Entonces
				Escribir a,b,c
			SiNo
				Escribir a,c,b
			FinSi
		SiNo
			Escribir c,a,b
		FinSi
	SiNo
		Si a>c Entonces
			Escribir b,a,c
		SiNo
			Si b>c Entonces
				Escribir b,c,a
			SiNo
				Escribir c,b,a
			FinSi
		FinSi
	FinSi
FinAlgoritmo
