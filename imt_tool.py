# -*- coding: utf-8 -*-

from imt_lib import PrimeiroGrau, SegundoGrau, Juros, Circle, Cilindro, TrianguloPascal, PrimeiroGrauDesconhecido, SegundoGrauDesconhecido, SetorCircular, ver_info, print_linha, beautiful
from prime_lib import print_primo, print_semiprimo, print_primos_ate, print_semiprimos_ate, print_primeiros_primos, print_primeiros_semiprimos, lib_info, print_mersenne
from imt_resources import print_fatorial, print_e_fatorial, print_media, print_mediana

print ver_info
print "O que você gostaria de fazer ?"
print "-- Digite 'func' se deseja trabalhar com Funcões"
print "-- Digite 'juros' se deseja trabalhar com Juros(simples ou composto)"
print "-- Digite 'prime' se deseja trabalhar com números Primos e Semiprimos em geral"
print "-- Digite 'circle' se deseja trabalhar com círculos e cilindros"
print "-- Digite 'pascal' se deseja gerar um triângulo de Pascal"
print "-- Digite 'fatorial' se deseja trabalhar com fatoriais"
print "-- Digite 'media' se deseja trabalhar com médias e medianas"
print "-- Digite 'quit' ou 'exit' se deseja sair"

storage = 0

while True:
	if storage != 0:
		print "Opções : 'func', 'juros', 'prime', 'circle', 'pascal', 'fatorial', 'media', 'quit'"
	user_entry = raw_input('> ').lower()
	print_linha()
	if user_entry == "func":
		print "-- Digite 1 se você deseja trabalhar com uma Função Polinomial do 1˚ grau"
		print "-- Digite 2 se você deseja trabalhar com uma Função Polinomial do 2˚ grau"
		print "-- Digite 3 se você deseja descobrir uma Função Polinomial do 1º grau apartir de 2 pontos distintos"
		print "-- Digite 4 se você deseja descobrir uma Função Polinomial do 2º grau apartir de pontos distintos"
		deseja = float(raw_input('> '))
		if deseja == 1:
			a = float(raw_input("Qual o valor de a?\n> "))
			b = float(raw_input("Qual o valor de b?\n> "))
			raw_funcao = PrimeiroGrau(a, b)
			print_linha(), raw_funcao.print_funcao(), raw_funcao.print_forma(), raw_funcao.print_corta(), raw_funcao.print_situacao(), print_linha()
		elif deseja == 2:
			a = float(raw_input("Qual o valor de a?\n> "))
			b = float(raw_input("Qual o valor de b?\n> "))
			c = float(raw_input("Qual o valor de c?\n> "))
			raw_funcao = SegundoGrau(a, b, c)
			print_linha(),raw_funcao.print_funcao(), raw_funcao.print_concavidade(), raw_funcao.print_delta(), raw_funcao.print_raiz(), raw_funcao.print_resolucao(), raw_funcao.print_corta_eixo_x(), raw_funcao.print_corta_eixo_y(), raw_funcao.print_vertice(), print_linha(), raw_funcao.print_sinais() ,print_linha() 
		elif deseja == 3:
			x1 = float(raw_input("Qual o valor de x no 1º ponto?\n> "))
			y1 = float(raw_input("Qual o valor de y no 1º ponto?\n> "))
			x2 = float(raw_input("Qual o valor de x no 2º ponto?\n> "))
			y2 = float(raw_input("Qual o valor de y no 2º ponto?\n> "))
			raw_funcao = PrimeiroGrauDesconhecido(x1, y1, x2, y2)
			print_linha(), raw_funcao.print_funcao(), raw_funcao.print_forma(), raw_funcao.print_corta(), raw_funcao.print_situacao(), print_linha()
		elif deseja == 4:
			xv = float(raw_input("Qual o valor de x no Vértice?\n> "))
			yv = float(raw_input("Qual o valor de y no Vértice?\n> "))
			x1 = float(raw_input("Qual o valor de x no 1º ponto?\n> "))
			y1 = float(raw_input("Qual o valor de y no 1º ponto?\n> "))
			raw_funcao = SegundoGrauDesconhecido(xv, yv, x1, y1)
			print_linha(),raw_funcao.print_funcao(), raw_funcao.print_concavidade(), raw_funcao.print_delta(), raw_funcao.print_raiz(), raw_funcao.print_resolucao(), raw_funcao.print_corta_eixo_x(), raw_funcao.print_corta_eixo_y(), raw_funcao.print_vertice(), print_linha(), raw_funcao.print_sinais() ,print_linha()
		else:
			print "Opção invalida"
	elif user_entry == "juros":
		a = float(raw_input("Qual é o capital?\n > "))
		b = float(raw_input("Qual é a taxa de juros (em %) ?\n > "))
		c = float(raw_input("Qual é o tempo (em meses) ?\n > "))
		d = raw_input("O tipo de juros é Simples ou Composto?\n > ").lower()
		my_obj = Juros(a, b, c, d)
		if d == 'simples':
			print_linha()
			my_obj.print_juro_simples()
			print_linha()
		elif d == 'composto':
			print_linha()
			my_obj.print_juro_composto()
			print_linha()
		else:
			print "Tipo de juro não reconhecido!"
	elif user_entry == "prime":
		print lib_info
		print "-- Digite 1 se deseja checar se um número é primo"
		print "-- Digite 2 se deseja checar se um número é semiprimo"
		print "-- Digite 3 se deseja exibir os primeiros 'x' números primos"
		print "-- Digite 4 se deseja exibir os primeiros 'x' números semiprimos"
		print "-- Digite 5 se deseja exibir os primos até 'x'"
		print "-- Digite 6 se deseja exibir os semiprimos até 'x'"
		print "-- Digite 7 se deseja checar seu uma potência de (2 ** p) - 1 é um Primo de Mersenne"
		deseja = float(raw_input('> '))
		if deseja == 1:
			a = int(raw_input("Insira o número abaixo\n> "))
			print_primo(a)
		elif deseja == 2:
			a = int(raw_input("Insira o número abaixo\n> "))
			print_semiprimo(a)
		elif deseja == 3:
			a = int(raw_input("Insira a quantidade de primos que deseja gerar abaixo\n> "))
			print_primeiros_primos(a)
		elif deseja == 4:
			a = int(raw_input("Insira a quantidade de semiprimos que deseja gerar abaixo\n> "))
			print_primeiros_semiprimos(a)
		elif 	deseja == 5:
			a = int(raw_input("Insira até qual número os primos os primos devem ser gerados\n> "))
			print_primos_ate(a)
		elif deseja == 6:
			a = int(raw_input("Insira até qual número os primos os semiprimos devem ser gerados\n> "))
			print_semiprimos_ate(a)
		elif deseja == 7:
			a = int(raw_input("Insira o valor de 'p' na expressão (2 ** p) - 1\n> "))
			print_mersenne(a)
		else:
			print "Opção invalida"
	elif user_entry == "circle" :
		print "-- Digite 1 se deseja trabalhar com círculos"
		print "-- Digite 2 se deseja trabalhar com cilindros"
		print "-- Digite 3 se deseja trabalhar com setores circulares"
		deseja = float(raw_input('> '))
		if deseja == 1:
			raio = float(raw_input("Insira o raio do círculo\n> "))
			unidade = raw_input('Unidade de medida\n> ').lower()
			my_obj = Circle(raio, unidade)
			print_linha(), my_obj.print_considerando(), my_obj.print_trabalhando(), my_obj.print_perimetro(), my_obj.print_area(), print_linha()
		elif deseja == 2:
			raio = float(raw_input("Insira o raio do cilindro\n> "))
			altura = float(raw_input("Insira a altura do cilindro\n> "))
			unidade = raw_input('Unidade de medida\n> ').lower()
			my_obj = Cilindro(raio, altura, unidade)
			print_linha(), my_obj.print_considerando(), my_obj.print_trabalhando(), my_obj.print_perimetro(), my_obj.print_area(), my_obj.print_area_lateral(),my_obj.print_volume(), my_obj.print_perimetro_total(), print_linha()
		elif deseja == 3:
			raio = float(raw_input("Insira o raio do setor circular\n> "))
			angulo = float(raw_input("Insira o ângulo do setor circular em º\n> "))
			unidade = raw_input('Unidade de medida\n> ').lower()
			my_obj = SetorCircular(raio, angulo, unidade)
			print_linha(), my_obj.print_considerando(), my_obj.print_trabalhando(), my_obj.print_perimetro(), my_obj.print_area(), print_linha()
		else:
			print "Opção invalida"
	elif user_entry == "pascal":
		print "-- Digite 1 se deseja gerar a pirâmide inteira"
		print "-- Digite 2 se deseja gerar apenas a última linha da pirâmide"
		deseja = float(raw_input('> '))
		if deseja == 1:
			a = int(raw_input("Quantas linhas você deseja exibir?\n > "))
			piramide = TrianguloPascal(a)
			print_linha(), piramide.print_triangulo() ,print_linha()
		elif deseja == 2:
			a = int(raw_input("Qual linha você deseja exibir?\n > "))
			piramide = TrianguloPascal(a)
			print_linha(), piramide.print_ultima() ,print_linha()
		else:
			print "Opção invalida"
	elif user_entry == "fatorial":
		print "-- Digite 1 se deseja calcular um fatorial"
		print "-- Digite 2 se deseja checar se um número é um fatorial"
		deseja = float(raw_input('> '))
		if deseja == 1:
			a = int(raw_input("Insira o número abaixo\n> "))
			print_linha(), print_fatorial(a), print_linha()
		elif deseja == 2:
			a = int(raw_input("Insira o número abaixo\n> "))
			print_linha(), print_e_fatorial(a), print_linha()
		else:
			print "Opção invalida"
	elif user_entry == "media":
		print "-- Digite 1 se deseja trabalhar com médias"
		print "-- Digite 2 se deseja trabalhar com medianas"
		deseja = float(raw_input('> '))
		if deseja == 1:
			a = int(raw_input("Quantos números você deseja inserir?\n > "))
			media = []
			for i in xrange(1,a+1):
				media.append(beautiful(float(raw_input("Insira o %sº número\n > " % i))))
			print_linha(), print_media(media), print_linha()
		elif deseja == 2:
			a = int(raw_input("Quantos números você deseja inserir?\n > "))
			mediana = []
			for i in xrange(1,a+1):
				mediana.append(beautiful(float(raw_input("Insira o %sº número\n > " % i))))
			print_linha(), print_mediana(mediana), print_linha()
		else:
			print "Opção invalida"
	elif user_entry == "quit" or user_entry == "exit":
		exit()
	else:
		print "Opção invalida"
	storage += 1
