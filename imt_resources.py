# -*- coding: utf-8 -*-

from math import factorial
from imt_lib import beautiful

def print_fatorial(n):
	"""Exibe o n!"""
	print "%d! = %d " % (n, factorial(n))

def gerar_lista_fatorial(n):
	"""Gera  todos números fatoriais até n"""
	number = 1
	my_list = []
	while factorial(number) <= n:
		my_list.append(factorial(number))
		number += 1
	return my_list

def is_factorial(n):
	"""Checa se um número é um fatorial 'na força'"""
	return n in gerar_lista_fatorial(n)

def print_e_fatorial(n):
	"""Exibe se ele é ou não um fatorial e se sim qual x! = n"""
	if is_factorial(n):
		a = gerar_lista_fatorial(n)
		for i in xrange(0,len(a)):
			if n == a[i] and n != 1:
				print "%d é fatorial pois %d! = %d" % (n, i+1, n)
			elif n == a[i] and n == 1:
				print "1 é fatorial pois 0! = 1 e 1! = 1"
	else:
		print "%d não é um fatorial" % n

def calcular_media(x):
	"""Calcula a media de um array de números"""
	return beautiful(sum(x) / float(len(x)))

def print_media(x):
	"""Exibe a média de um array de números"""
	print "A média de %s é %s" % (str(sorted(x)), str(calcular_media(x)))

def calcular_mediana(x):
	"""Calcula a mediana de um array de números"""
	if len(x) % 2:
		return sorted(x)[int(len(x) / 2)] 
	else:
		return beautiful((sorted(x)[len(x) / 2] + sorted(x)[len(x) / 2 - 1]) / 2.0)

def print_mediana(x):
	"""Exibe a mediana de um array de números"""
	print "A mediana de %s é %s" % (str(sorted(x)), str(calcular_mediana(x)))
