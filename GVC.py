from matplotlib import pyplot
import random
import math

class GVC:

	def __init__(self):
		return


	def genPuntos(self):
		puntos = []
		for i in range(0,20):
			puntos.append([random.randint(1,10),random.randint(1,10)])
		return puntos

	def genCentroides(self):
		centroides = []
		for i in range(1,3):
			centroides.append([random.randint(1,10),random.randint(1,10)])
		return centroides

	def recCentroides(self, puntos , centroides):
		distanciasE = self.distEuc(puntos, centroides)
		centNueva = [[],[]]
		x = []
		y = []
		for i in range(0,len(distanciasE)):
			distanciasE[0][i]
			distanciasE[1][i]
		centNueva.append([0][x/len(x) , y/len(y)])
		centNueva.append([1][x/len(x) , y/len(y)])

		return centNueva


	def distEuc(self, puntos, centroides):
		distancias = [[],[]]
		for i in range(0,20):
			k1 = math.sqrt(math.pow((puntos[i][0] - centroides[0][0]),2)+math.pow((puntos[i][1] - centroides[0][1]),2))
			k2 = math.sqrt(math.pow((puntos[i][0] - centroides[1][0]),2)+math.pow((puntos[i][1] - centroides[1][1]),2))
			if k1>k2:
				distancias[1].append(puntos[i])
			else:
				distancias[0].append(puntos[i])
		return distancias