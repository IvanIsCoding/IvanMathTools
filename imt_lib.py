# -*- coding: utf-8 -*-

from math import pi

ver_num = 1.0
sub_ver = 0
ver_info = """
--------------------
Ivan Math Tools v1.0

Todo programador tem que começar de algum lugar
--------------------
"""

def diferente(a):
	"""Utilizado para remover coeficientes 1 em equações, que são redundantes"""
	if a == 1:
		return ""
	elif a == -1:
		return "-"
	else:
		return a

def beautiful(n):
	"""Remove .0 de inteiros pois são redundantes"""
	if n % 1 == 0:
		return int(n)
	else:
		return float(n)

def print_linha():
	"""Função para exibir espaçamentos sem o 'None' do print"""
	print "\n"

class SegundoGrau(object):
	"""Cria uma equação de 2˚ grau e seus atributos"""

	def calcular_delta(self, a, b,c):
		"""Calcula o ∆"""
		return (b ** 2) - (4*a*c)
	
	def calcular_raiz_de_delta(self, a):
		"""Calcula a raiz de ∆ se positivo"""
		if a == 0:
			return 0
		elif a > 0:
			return a ** 0.5
		else:
			return "Que absurdo!Não é possível encontrar a raiz de um número negativo!"
	
	def funcao_trabalhando(self, a, b, c):
		"""Exibe a forma da função"""
		if b > 0 and c > 0:
			return "ƒ(x) = %sx² + %sx + %s" %  (str(diferente(beautiful(a))), str(diferente(beautiful(b))), str(beautiful(c)))
		elif b == 0 and c > 0:
			return "ƒ(x) = %sx² + %s" %  (str(diferente(beautiful(a))), str(beautiful(c)))
		elif b > 0 and c == 0:
			return "ƒ(x) = %sx² + %sx" %  (str(diferente(beautiful(a))), str(diferente(beautiful(b))))
		elif b < 0 and c > 0:
			return "ƒ(x) = %sx² - %sx + %s" %  (str(diferente(beautiful(a))), str(diferente(beautiful(-1 * b))), str(beautiful(c)))
		elif b == 0 and c < 0:
			return "ƒ(x) = %sx² - %s" %  (str(diferente(beautiful(a))), str(beautiful(-1 * c)))
		elif b < 0 and c == 0:
			return "ƒ(x) = %sx² - %sx" %  (str(diferente(beautiful(a))), str(diferente(beautiful(-1 * b))))
		elif b < 0 and c < 0:
			return "ƒ(x) = %sx² - %sx - %s" %  (str(diferente(beautiful(a))), str(diferente(beautiful(-1 * b))), str(beautiful(-1 * c)))
		elif b > 0 and c < 0:
			return "ƒ(x) = %sx² + %sx - %s" %  (str(diferente(beautiful(a))), str(diferente(beautiful(b))), str(beautiful(-1 * c)))
		else:
			return "ƒ(x) = %sx²" %  str(diferente(beautiful(a)))
	
	def baskara(self, a, b, c, d):
		"""Acha as soluções para ƒ(x) = 0"""
		if d >= 0:
			x1 = (-1 * b + (d ** 0.5))  / float(2 * a)
			x2 = (-1 * b - (d ** 0.5))  / float(2 * a)
			return x1, x2
		else:
			return "Não é possível resolver essa equação no conjunto dos reais !"
	
	def calcular_vertice(self, a, b, d):
		"""Calcula o Ponto Mínimo ou Máximo da parábola"""
		vertice_x = (-1 * b) / float(2 * a)
		vertice_y = (-1 * d) / float(4 * a)
		return vertice_x, vertice_y 
	
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c
		self.delta = self.calcular_delta(self.a, self.b, self.c)
		self.raiz = self.calcular_raiz_de_delta(self.delta)
		self.funcao = self.funcao_trabalhando(self.a, self.b, self.c)
		self.x1 = self.baskara(self.a, self.b, self.c, self.delta)[0]
		self.x2 = self.baskara(self.a, self.b, self.c, self.delta)[1]
		self.vertice_x = self.calcular_vertice(self.a, self.b, self.delta)[0]
		self.vertice_y = self.calcular_vertice(self.a, self.b, self.delta)[1]
	
	def print_concavidade(self):
		"""Exibe a direção da concavidade da parábola"""
		if self.a > 0:
			print "A parábola tem concavidade para cima!"
		elif self.a < 0:
			print "A parábola tem convavidade para baixo!"
		else:
			print "Isto não é uma parábola!"
	
	def print_funcao(self):
		"""Exibe a função com que estamos trabalhando"""
		print "Estamos trabalhando com a função %s" % self.funcao
	
	def print_delta(self):
		"""Exibe o ∆"""
		print "Δ = %s" % str(beautiful(self.delta))
	
	def print_raiz(self):
		"""Exibe a √Δ"""
		print "√Δ = %s" % str(self.raiz)
	
	def print_resolucao(self):
		"""Exibe a resolução da equação"""
		if self.delta == 0:
			print "Estamos trabalhando com a equação 0%s , que tem apenas uma solução: %s" % (self.funcao[5:], str(beautiful(self.x1)))
		elif self.delta > 0:
			print "Estamos trabalhando com a equação 0%s , que tem duas soluções: %s e %s" % (self.funcao[5:], str(beautiful(self.x1)), str(beautiful(self.x2)))
		else:
			print "Estamos trabalhando com a equação 0%s , que não tem solução pois x∌ℝ" % self.funcao[5:]
	
	def print_corta_eixo_x(self):
		"""Exibe onde a parábola corta o eixo y"""
		if self.delta == 0:
			print "A parábola corta o eixo x em apenas um ponto: (%s, 0)" % str(beautiful(self.x1))
		elif self.delta > 0:
			print "A parábola corta o eixo x em dois pontos: (%s, 0) e (%s, 0)" % (str(beautiful(self.x1)), str(beautiful(self.x2)))
		else:
			print "A parábola não corta o eixo x!"
	
	def print_corta_eixo_y(self):
		"""Exibe onde a parábola corta o eixo y"""
		print "A parábola corta o eixo y no ponto (0, %s)" % str(beautiful(self.c))
	
	def print_vertice(self):
		"""Exibe o vértice"""
		print "O vértice se encontra no ponto (%s, %s)" % (str(beautiful(self.vertice_x)), str(beautiful(self.vertice_y)))
	
	def print_sinais(self):
		"""Exibe as condições do valor de y na função"""
		if self.a > 0 and self.delta == 0:
			print "y = 0 ⇔  x = %s\ny > 0 ⇔  ∀ x∈ℝ / x ≠ %s\ny < 0 ⇔  x∌ℝ" % (str(beautiful(self.x1)), str(beautiful(self.x1)))
		elif self.a < 0 and self.delta == 0:
			print "y = 0 ⇔  x = %s\ny > 0  ⇔  x∌ℝ\ny < 0 ⇔  ∀ x∈ℝ / x ≠ %s" % (str(beautiful(self.x1)), str(beautiful(self.x1)))
		elif self.a > 0 and self.delta > 0:
			print "y = 0 ⇔  x = %s ou x = %s\ny > 0 ⇔  x < %s ou x > %s\ny < 0 ⇔  %s < x < %s" % (str(beautiful(self.x1)), str(beautiful(self.x2)), str(beautiful(self.x2)), str(beautiful(self.x1)), str(beautiful(self.x2)), str(beautiful(self.x1)))
		elif self.a < 0 and self.delta > 0:
			print "y = 0 ⇔  x = %s ou x = %s\ny > 0 ⇔  %s < x < %s\ny < 0 ⇔  x < %s ou x > %s" % (str(beautiful(self.x1)), str(beautiful(self.x2)), str(beautiful(self.x1)), str(beautiful(self.x2)), str(beautiful(self.x1)), str(beautiful(self.x2)))
		elif self.a > 0 and self.delta < 0:
			print "y = 0 ⇔  x∌ℝ\ny > 0 ⇔  ∀ x∈ℝ\ny < 0 ⇔  x∌ℝ"
		else:
			print "y = 0 ⇔  x∌ℝ\ny > 0 ⇔  x∌ℝ\ny < 0 ⇔  ∀ x∈ℝ"


class SegundoGrauDesconhecido(SegundoGrau):
	"""Descobre a função que origina a parábola a partir de seus pontos e por meio do vértice, que transforma a resolução em um sistema de primeiro grau resolvido pelo método da adição"""
		
	def __init__(self, xv, yv, x1, y1):
		self.vertice_x = xv
		self.vertice_y = yv
		self.xx1 = x1
		self.y1 = y1
		self.a = (self.y1 - self.vertice_y) / float(self.xx1 ** 2 + self.vertice_x ** 2 - 2 * self.vertice_x * self.xx1)
		self.b = -2 * self.a * self.vertice_x
		self.c = self.y1 - self.a * self.xx1 ** 2 - self.b * self.xx1
		self.delta = self.calcular_delta(self.a, self.b, self.c)
		self.raiz = self.calcular_raiz_de_delta(self.delta)
		self.funcao = self.funcao_trabalhando(self.a, self.b, self.c)
		self.x1 = self.baskara(self.a, self.b, self.c, self.delta)[0]
		self.x2 = self.baskara(self.a, self.b, self.c, self.delta)[1]

	def print_funcao(self):
		print "A única Função Polinomial do 2° Grau com Vértice em (%s, %s) cuja parábola passa pelo ponto (%s, %s) é a função %s" % (str(beautiful(self.vertice_x)), str(beautiful(self.vertice_y)), str(beautiful(self.xx1)), str(beautiful(self.y1)), self.funcao)

class Juros(object):
	"""Por meio dos valores dos capitais, tempo, interesse e tipo calcula os juros"""

	@staticmethod
	def calcular_juro_simples(c, i, t):
		"""Calcula o juro simples"""
		return (c*i*t) / 100.0
	
	@staticmethod
	def calcular_juro_composto(c, i, t):
		"""Calcula o juro composto"""
		return c*((i/100.0 + 1.0)**t) -c
	
	@staticmethod
	def calcular_montante(c, j):
		"""Calcula o montante"""
		return c + j
	
	def __init__(self, c, i, t, tipo):
		self.capital = c
		self.taxa = i
		self.tempo = t
		self.tipo = tipo
		self.juro_simples = self.calcular_juro_simples(self.capital, self.taxa, self.tempo)
		self.juro_composto = self.calcular_juro_composto(self.capital, self.taxa, self.tempo)
		self.montante_simples = self.calcular_montante(self.capital, self.juro_simples)
		self.montante_composto = self.calcular_montante(self.capital, self.juro_composto)
	
	def print_juro_simples(self):
		"""Exibe os dados dos juros simples"""
		print "Com um capital de %s e uma taxa de %s%s, se paga %s de juros por mês totalizando %s de juros ao longo de %s meses , resultando no montante %s" % (str(beautiful(self.capital)),str(beautiful(self.taxa)), '%', str(beautiful(self.capital * self.taxa / 100.0)), str(beautiful(self.juro_simples)), str(beautiful(self.tempo)), str(beautiful(self.montante_simples)))
	
	def print_juro_composto(self):
		"""Exibe os dados dos juros compostos"""
		print "Com um capital de %s e uma taxa de %s%s se obtém %s de juros totalizando %s de montante" % (str(beautiful(self.capital)), str(beautiful(self.taxa)), '%' , str(beautiful(self.juro_composto)), str(beautiful(self.montante_composto)))
		for i in xrange(1,int(self.tempo+1)):
			montante_mes = self.capital + self.calcular_juro_composto(self.capital, self.taxa, i-1)
			juros_mes =  self.calcular_juro_simples(montante_mes, self.taxa, 1)
			print "\tNo %sº mês, o valor de juros foi de %s sobre o capital %s" % (str(i), str(beautiful(juros_mes)), str(beautiful(montante_mes)))


class PrimeiroGrau(object):
	"""Cria uma Função Polinomial do 1º Grau e seus atributos"""

	def funcao_trabalhando(self, a, b):
		"""Gera a string com a função"""
		if b > 0:
			return "ƒ(x) = %sx + %s" %  (str(diferente(beautiful(a))), str((beautiful(b))))
		elif b < 0:
			return "ƒ(x) = %sx - %s" %  (str(diferente(beautiful(a))), str((beautiful(-1 * b))))
		else:
			return "ƒ(x) = %sx" %  str(diferente(beautiful(a)))
	
	def __init__(self, a, b):
		self.a = a
		self.b = b
		self.funcao = self.funcao_trabalhando(self.a, self.b)
		self.zero = -1.0 * self.b / float(self.a)
	
	def print_funcao(self):
		"""Exibe a função que estamos trabalhando"""
		print "Estamos trabalhando com a função %s" % self.funcao
	
	def print_forma(self):
		"""Exibe o "tipo" da função"""
		if self.a > 0:
			print "Está função é crescente"
		else:
			print "Está função é decrescente"
	
	def print_corta(self):
		"""Exibe onde a reta corta os eixos x e y"""
		print "A reta corta o eixo x no ponto (%s, 0)" % str(beautiful(self.zero))
		print "A reta corta o eixo y no ponto (0, %s)" % str(beautiful(self.b))
	
	def print_situacao(self):
		"""Exibe as condições de ƒ(x) em função de x"""
		if self.a > 0:
			print "Se x < %s ⇔  ƒ(x) < 0\nSe x = %s ⇔  ƒ(x) = 0\nSe x > %s ⇔  ƒ(x) > 0" % (str(beautiful(self.zero)), str(beautiful(self.zero)), str(beautiful(self.zero)))
		else:
			print "Se x < %s ⇔  ƒ(x) > 0\nSe x = %s ⇔  ƒ(x) = 0\nSe x > %s ⇔  ƒ(x) < 0" % (str(beautiful(self.zero)), str(beautiful(self.zero)), str(beautiful(self.zero)))
	
	def print_inversa(self):
		"Exibe a inversa da função"
		print "A inversa da função é %s" % (self.funcao_trabalhando(1.0/float(self.a),-1.0*float(self.b)/float(self.a)))

class PrimeiroGrauDesconhecido(PrimeiroGrau):
	"""Descobre o valor de a e b da função a partir de um sistema pelo método da adição"""

	def __init__(self, x1, y1, x2, y2):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.a = (self.y1 - self.y2) / float(self.x1 - self.x2)
		self.b = self.y1 - (self.a * self.x1)
		self.funcao = self.funcao_trabalhando(self.a, self.b)
		self.zero = -1.0 * self.b / float(self.a)

	def print_funcao(self):
		print "A única Função Polinomial do 1º Grau que satisfaz os dois pontos (%s, %s) e (%s, %s) é a função %s" % (str(beautiful(self.x1)), str(beautiful(self.y1)), str(beautiful(self.x2)), str(beautiful(self.y2)), self.funcao)


class Circle(object):
	"""Cria um círculo com raio 'x' e seus atributos"""

	@staticmethod
	def calcular_area(raio):
		"""Calcula a área"""
		return pi * (raio ** 2)
	
	@staticmethod
	def calcular_perimetro(raio):
		"""Calcula o perímetro"""
		return 2 * pi * raio
	
	def __init__(self, raio, unidade):
		self.angle = 360
		self.raio = raio
		self.perimetro = self.calcular_perimetro(self.raio)
		self.area = self.calcular_area(self.raio)
		self.diametro = self.raio * 2
		self.tipo = "círculo"
		self.sarea = str(diferente(beautiful(self.raio ** 2)))
		self.sperimetro = str(diferente(beautiful(self.raio * 2)))
		self.unidade = unidade
	
	def print_considerando(self):
		"""Exibe o valor de math.pi"""
		print "Considerando que π ≅ %s" % str(pi)
	
	def print_trabalhando(self):
		"""Exibe o círculo em que estamos trabalhando"""
		if self.tipo == "círculo":	
			print "Estamos trabalhando com um círculo com raio %s%s" % (str(beautiful(self.raio)), self.unidade)
		elif self.tipo == "setor":
			print "Estamos trabalhando com um setor círcular de raio %s%s e ângulo %sº" % (str(beautiful(self.raio)), self.unidade, str(beautiful(self.angle)))
		else:
			print "Os círculos do cilindro tem raio de %s%s" % (str(beautiful(self.raio)), self.unidade)
	
	def print_perimetro(self):
		"""Exibe o périmetro do círculo"""
		if self.tipo == "círculo":	
			print "Este círculo tem perimetro de %sπ %s ≅ %s%s" % (self.sperimetro, self.unidade, str(beautiful(self.perimetro)), self.unidade)
		elif self.tipo == "setor":
			print "Este setor circular tem perimetro de %sπ %s + %s%s ≅ %s%s" % (self.sperimetro, self.unidade, str(beautiful(self.diametro)), self.unidade, str(beautiful(self.perimetro)), self.unidade)
		else:
			print "Os círculos do cilindro tem perimetro de %sπ %s ≅ %s%s" % (self.sperimetro, self.unidade, str(beautiful(self.perimetro)), self.unidade)
	
	def print_area(self):
		"""Exibe a área do círculo"""
		if self.tipo == "círculo":	
			print "Este círculo tem área de %sπ %s² ≅ %s%s²" % (self.sarea, self.unidade, str(beautiful(self.area)), self.unidade)
		elif self.tipo == "setor":
			print "Este círculo tem área de %sπ %s² ≅ %s%s²" % (self.sarea, self.unidade, str(beautiful(self.area)), self.unidade)
		else:
			print "Os círculo do cilindro tem área de %sπ %s² ≅ %s%s²" % (self.sarea, self.unidade, str(beautiful(self.area)), self.unidade)


class SetorCircular(Circle):
	"""Cria um setor circular baseado em um círculo com raio 'x' e ângulo 'y' e seus atributos"""

	def __init__(self, raio, angulo, unidade):
		self.angle = angulo
		self.raio = raio
		self.diametro = self.raio * 2
		self.perimetro = self.calcular_perimetro(self.raio) * (self.angle / 360.0) + self.diametro
		self.area = self.calcular_area(self.raio) * (self.angle / 360.0)
		self.tipo = "setor"
		self.sarea = str(diferente(beautiful(self.raio ** 2 * self.angle / 360.0)))
		self.sperimetro = str(diferente(beautiful(self.raio * 2 * self.angle / 360.0)))
		self.unidade = unidade

class Cilindro(Circle):
	"""Cria um cilindro com raio 'x' e altura 'y' e seus atributos + atributos herdados do círculo"""

	@staticmethod
	def calcular_volume(area, h):
		"""Calcula o volume"""
		return area * h
	
	def calcular_perimetro_total(self, raio, altura):
		"""Calcula a área da superfície (sim, eu nomeei errado)"""
		return (self.calcular_perimetro(raio) * altura) + (2 * self.calcular_area(raio))
	
	def __init__(self, raio, altura, unidade):
		self.angle = 360
		self.raio = raio
		self.perimetro = self.calcular_perimetro(self.raio)
		self.area = self.calcular_area(self.raio)
		self.diametro = self.raio * 2
		self.altura = altura
		self.volume = self.calcular_volume(self.area, self.altura)
		self.total = self.calcular_perimetro_total(self.raio, self.altura)
		self.tipo = "cilindro"
		self.sarea = str(diferente(beautiful(self.raio ** 2)))
		self.sperimetro = str(diferente(beautiful(self.raio * 2)))
		self.svolume = str(beautiful(float(self.sarea) * self.altura))
		self.sperimetro_total = str(beautiful(float(self.sperimetro) * self.altura + (float(self.sarea) * 2) ))
		self.unidade = unidade
	
	def print_trabalhando(self):
		"""Exibe o cilindro com que estamos trabalhando"""
		print "Estamos trabalhando com um cilindro com altura de %s%s e raio %s%s" % (str(beautiful(self.altura)), self.unidade, str(beautiful(self.raio)), self.unidade)
	
	def print_volume(self):
		"""Exibe o volume"""
		print "Este cilindro tem um volume de %sπ %s³ ≅ %s%s³" % (self.svolume, self.unidade, str(beautiful(self.volume)), self.unidade)
	
	def print_perimetro_total(self):
		"""Exibe a área total da superfície"""
		print "A superfície total desse cilindro é de %sπ %s² ≅ %s%s²" % (self.sperimetro_total, self.unidade, str(beautiful(self.total)), self.unidade)
	
	def print_area_lateral(self):
		"""Exibe a área da parte lateral do cilindro"""
		print "A área da parte lateral do cilindro mede %sπ %s por %s%s e tem área de %sπ %s² ≅ %s%s²" % (str(beautiful(self.raio * 2)),self.unidade, str(beautiful(self.altura)),self.unidade, str(beautiful(self.raio * self.altura * 2)),self.unidade, str(beautiful(self.raio * self.altura * 2 * pi)), self.unidade)


class TrianguloPascal(object):
	"""Cria um Triângulo de Pascal e suas respectivas linhas"""

	@staticmethod
	def gerar_triangulo(linhas):
		"""Gera o triângulo em si"""
		triangulo = [[1], [1, 1]]
		if linhas == 1:
			return triangulo[0]
		else:
			for i in xrange(2, linhas):
				triangulo.append([1]*i)
				for j in xrange(1, i):
					triangulo[i][j] = (triangulo[i-1][j-1]+triangulo[i-1][j])
				triangulo[i].append(1)
			return triangulo

	@staticmethod
	def diferenca_entre_linhas(linha, proxima_linha):
		"""Compensa a diferença das linhas para a pirâmide não ficar torta"""
		linha_len = 0
		proxima_linha_len = 0
		for i in linha:
			linha_len += len(str(i))+1
		for i in proxima_linha:
			proxima_linha_len += len(str(i))+1
		return (proxima_linha_len-1) - (linha_len-1)

	def __init__(self, linhas):
		self.linhas = linhas
		self.triangulo = self.gerar_triangulo(self.linhas)
		self.ultima = self.triangulo[-1]

	def print_triangulo(self):
		"""Exibe a pirâmide inteira"""
		print "Vamos exibir o triângulo até a %dª linha (exponente %d):" % (self.linhas, self.linhas-1)
		for linha in self.triangulo:
			diferenca = int((self.diferenca_entre_linhas(linha, self.triangulo[len(self.triangulo)-1]))/2)
			for i in xrange(len(linha)):
				linha[i] = str(linha[i])
			print (' ')*(diferenca), ' '.join(linha)

	def print_ultima(self):
		"""Exibe a última linha"""
		print "Vamos exibir a %dª linha (exponente %d):" % (self.linhas, self.linhas-1)
		print self.ultima
