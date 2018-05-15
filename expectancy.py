#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import matplotlib.pyplot as plt
from datetime import datetime
import sys
import string
import re

# Configurações

## Configurações do gráfico

# Determine aqui o número de faces. 6 por padrão.
FACES = 20

# Por padrão o eixo x vai de 0 a log 10^300, isto é, 300.
INTERVALO = 100

# RANDOM = 1 : números pseudoaleatórios criptograficamente seguros de /dev/urandom.
# RANDOM = 0 :  números pseudoaleatórios da função random ( mais rápido ).
RANDOM = 1

# Valor da linha tracejada de convergência. 3.5 por padrão. 
CONVERGENCIA = 10.5

## Configurações estéticas

# Número de gráficos por imagem. 3 por padrão.
BLOCO = 5

# Prefixo do arquivo salvo.
PREFIXO = 'expectancy_'

# Formato do arquivo salvo. Opções disponíveis: .png e .pdf.
FORMAT = '.png'

# Número máximo de valores indicados no eixo x. 6 por padrão.
TICKS_X = 6

# Número máximo de valores indicados no eixo y. 6 por padrão
TICKS_Y = 6

# Fim das configurações

class Dice(object):

	def __init__(self):
		self.x = []
		self.y = []
		self.total = 0

	def series(self,a):
		display = 0
		self.total = 0
		for i in range(1,10^int(a)):
			if RANDOM:
				self.total += random.SystemRandom().randint(1,FACES)
			else:
				self.total += random.randint(1,FACES)
			display = self.total / i
			self.x.append(i)
			self.y.append(display)
	def clear(self):
		self.x = []
		self.y = []

def main(times):

	regex = re.compile( '[%s]' % re.escape(string.punctuation + ' '))
	colors = ['r','g','b']

	for i in range(0,times):

		plt.axis([0,10^(INTERVALO),0,FACES])
		dice = Dice()
	
		for i in range(1,BLOCO+1):
			plt.subplot(BLOCO,1,i)
			dice.series(INTERVALO)
			plt.plot(dice.x, dice.y, random.choice(colors) )
			plt.locator_params(axis='x', nbins=TICKS_X-1)
			plt.locator_params(axis='y', nbins=TICKS_Y-1)	
			plt.axhline(y=CONVERGENCIA, color='m', linestyle='--')
			dice.clear()
	
		plt.tight_layout()	
		plt.savefig(PREFIXO + regex.sub('',str(datetime.now())) + FORMAT )

	if int(sys.argv[2]) == 1:
		plt.clf()

if __name__ == "__main__":
	main(int(sys.argv[1]))
