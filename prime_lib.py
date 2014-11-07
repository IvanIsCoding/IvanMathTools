# -*- coding: utf-8 -*-

lib_num = 0.4
lib_sub_num = 1
lib_info = """
--------------------
Ivan PrimeLib v0.4.1

Agora mais rápido (testado até (2 ** 61) - 1)!
--------------------
"""

def is_int(n):
	"""Checa se é um número é realmente um inteiro"""
	return n % 1 == 0

def is_prime(n):
	"""Checa se um número é primo"""
	return n == 2 or n > 1 and n % 2 != 0 and all(n % i for i in xrange(3,int(n ** 0.5)+1,2))

def first_primes(n):
	"""Gera os primeiros 'n' primos"""
	my_list = [2, 3]
	number = 5
	while len(my_list) <= n:
		if is_prime(number):
			my_list.append(number)
		number += 2
	return my_list

def primes_upto(n):
	"""Gera os primos até 'n'"""
	return [2] + [i for i in xrange(3, n+1, 2) if is_prime(i)]

def is_semiprime(n):
	"""Checa se é um número semiprimo"""
	if n % 2 == 0:
		return is_prime(n / 2)
	elif (n ** 0.5) % 1 == 0:
		return is_prime(n ** 0.5)
	elif is_prime(n):
		return False
	else:
		my_list = primes_upto(int(n / 2) + 1)
		verif = 0
		for i in xrange(1, len(my_list)):
			if is_prime(n / my_list[i]) and is_int(n / float(my_list[i])):
				verif += 1
		return verif == 2

def semiprimes_upto(n):
	"""Gera os primos até 'n'"""
	return [i for i in xrange(4,n+1) if is_semiprime(i)]

def first_semiprimes(n):
	"""Gera os 'n' primeiros semiprimos"""
	my_list = []
	number = 4
	while len(my_list) < n:
		if is_semiprime(number):
			my_list.append(number)
		number += 1
	return my_list

def print_primo(n):
	"""Exibe se um número é primo"""
	if is_prime(n):
		print "%d é Primo !" % n
	else:
		print "%d não é primo" % n

def print_semiprimo(n):
	"""Exibe se um número é semiprimo"""
	if is_semiprime(n):
		print "%d é  um número Semiprimo !" % n
	else :
		print "%d não é  um número Semiprimo" % n

def print_primos_ate(n):
	"""Exibe os primos até 'n'"""
	print "Vamos exibir todos números primos até %d" % n
	print primes_upto(n)

def print_semiprimos_ate(n):
	"""Exibe os semiprimos até 'n'"""
	print "Vamos exibir todos números semiprimos até %d" % n
	print semiprimes_upto(n)

def print_primeiros_primos(n):
	"""Exibe os primeiros 'n' primos"""
	print "Vamos exibir os primeiros %d números primos" % n
	print first_primes(n)

def print_primeiros_semiprimos(n):
	"""Exibe os primeiros 'n' semiprimos"""
	print "Vamos exibir os primeiros %d números semiprimos" % n
	print first_semiprimes(n)

def is_mersenne_prime(n):
	"""Checa se uma potência de (2**n) - 1 é prima"""
	return is_prime(2 ** n - 1)

def print_mersenne(n):
	"""Exibe se a potência de (2**n)-1 é prima"""
	if is_mersenne_prime(n):
		print "(2 ** %d) - 1 é primo" % n
	else:
		print "(2 ** %d) - 1 não é primo" % n
