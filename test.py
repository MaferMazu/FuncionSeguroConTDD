import unittest
import datetime
from Person import Person


def personGenerator(genre,year,quot):
	date = datetime.datetime(year, 1, 1)
	p=Person("Nombre",genre,date,quot)
	return p

class TestPension(unittest.TestCase):
	#Primer caso de prueba:
	#Hombre con 750 cotizaciones
	def testPensionMale750Quot(self):
		p=personGenerator("M",1996,750)
		self.assertTrue(p.AbleIVSSPension())

	#Segundo caso de prueba:
	#Hombre con menos de 750 cotizaciones (Caso Borde)
	def testPensionMale749Quot(self):
		p=personGenerator("M",1996,749)
		self.assertTrue(p.AbleIVSSPension())

	#Tercer caso de prueba:
	#Hombre de 60 y con 750 cotizaciones
	def testPensionMale750QuotAnd60Y(self):
		p=personGenerator("M",1960,750)
		self.assertTrue(p.AbleIVSSPension())

	#Cuarto caso de prueba:
	#Mujer de 60 y con 750 cotizaciones
	def testPensionFemale750QuotAnd60Y(self):
		p=personGenerator("F",1960,750)
		self.assertTrue(p.AbleIVSSPension())

	#Quinto caso de prueba:
	#Mujer de 55 y con 750 cotizaciones
	def testPensionFemale750QuotAnd55Y(self):
		p=personGenerator("F",1965,750)
		self.assertTrue(p.AbleIVSSPension())

	


if __name__ == '__main__':
	unittest.main()
