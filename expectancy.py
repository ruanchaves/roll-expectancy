import random
import matplotlib.pyplot as plt
from datetime import datetime
import sys


# Determine aqui o número de faces.
FACES = 6

# RANDOM = 1 : números pseudoaleatórios criptograficamente seguros de /dev/urandom.
# RANDOM = 0 :  números pseudoaleatórios da função random ( mais rápido ).
RANDOM = 1


# Valor da linha tracejada de convergência
CONVERGENCIA = 3.5

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

	for i in range(0,times):

		plt.axis([0,10^( (FACES//2) * 100),0,FACES])
		dice = Dice()
		
		plt.subplot(3,1,1)
		dice.series(300)
		plt.plot(dice.x, dice.y, 'r' )
		plt.axhline(y=CONVERGENCIA, color='m', linestyle='--')
		dice.clear()
	
		plt.subplot(3,1,2)
		dice.series(300)
		plt.plot(dice.x,dice.y, 'g' )
		plt.axhline(y=CONVERGENCIA, color='m', linestyle='--')
		dice.clear()
	
		plt.subplot(3,1,3)
		dice.series(300)
		plt.plot(dice.x,dice.y, 'b' )
		plt.axhline(y=CONVERGENCIA, color='m', linestyle='--')
		dice.clear()
		
		plt.savefig('expectancy_' + str(datetime.now())[20:] + '.png' , bbox_inches = 'tight' )

		if int(sys.argv[2]) == 1:
			plt.clf()

if __name__ == "__main__":
	main(int(sys.argv[1]))
