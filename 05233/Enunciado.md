Defina uma função que receba um texto e divida esse texto em alguns pedaços (a quantidade será passada por parametro. assuma que os valores para quantidade serão 2, 3, ou 4) e retorne uma lista ou tupla, de acordo com o terceiro parametro que será uma string com o valor "lista" ou "tupla", com os pedaços. Se o tamanho não string não for divisivel pela quantidade de pedaços o último pedaço deve ser o maior e os outros iguais.

Testes:

Entrada: ("0123456789",2,"tupla")
Saída: ('01234', '56789')

Entrada: ("0123456789",2,"lista")
Saída: ['01234', '56789']

Entrada: ("0123456789",3,"tupla")
Saída: ('012', '345', '6789')