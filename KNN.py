import numpy
from GVC import GVC
from matplotlib import pyplot


def main():	

	test_GVC = GVC()
	test = test_GVC.genPuntos()
	print test
	print len(test)
	cent = test_GVC.genCentroides()
	print cent
	print len(cent)
	#centN = test_GVC.recCentroides(test,cent)
	#print centN
	#print len(centN)
	for i in range(0,len(test)):
		pyplot.scatter(test[i][0], test[i][1])
	for i in range(0,len(cent)):
		pyplot.scatter(cent[i][0], cent[i][1], color="r")

	#pyplot.show()

	#cent = test_GVC.recCentroides(test, cent)
	#print cent
	#print len(cent)
	#for i in range(0,len(cent)):
	#	pyplot.scatter(cent[i][0], cent[i][1], color="r")
	pyplot.show()

main()