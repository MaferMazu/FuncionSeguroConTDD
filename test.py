import unittest
import datetime
from Person import Person


class TestPension(unittest.TestCase):
	#Primer caso de prueba:
	#Hombre con 750 cotizaciones
	def testPensionMale750Quot(self):
		date = datetime.datetime(1996, 2, 13)
		p=Person("Pedro","M",date,750)
		self.assertTrue(p.AbleIVSSPension())

	#Segundo caso de prueba:
	#Hombre con menos de 750 cotizaciones (Caso Borde)
	def testPensionMale749Quot(self):
		date = datetime.datetime(1996, 2, 13)
		p=Person("Pedro","M",date,749)
		self.assertTrue(p.AbleIVSSPension())

	#Tercer caso de prueba:
	#Hombre de 60 y con 750 cotizaciones
	def testPensionMale750QuotAnd60Y(self):
		date = datetime.datetime(1960, 1, 1)
		p=Person("Pedro","M",date,750)
		self.assertTrue(p.AbleIVSSPension())

	#Cuarto caso de prueba:
	#Mujer de 60 y con 750 cotizaciones
	def testPensionFemale750QuotAnd60Y(self):
		date = datetime.datetime(1960, 1, 1)
		p=Person("Maria","F",date,750)
		self.assertTrue(p.AbleIVSSPension())

	#Quinto caso de prueba:
	#Mujer de 55 y con 750 cotizaciones
	def testPensionFemale750QuotAnd55Y(self):
		date = datetime.datetime(1965, 1, 1)
		p=Person("Maria","F",date,750)
		self.assertTrue(p.AbleIVSSPension())

if __name__ == '__main__':
	unittest.main()
