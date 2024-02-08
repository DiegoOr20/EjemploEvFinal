import unittest
from EjemploEvaluacion.ejemplo import es_positivo, es_par

class TestExample(unittest.TestCase):

    def test_es_positivo(self):
        print("Ejecutando prueba para es_positivo(5)...")
        self.assertTrue(es_positivo(5))  
        print("Prueba para es_positivo(5) completada.")
        
        print("Ejecutando prueba para es_positivo(-5)...")
        self.assertFalse(es_positivo(-5))  
        print("Prueba para es_positivo(-5) completada.")

    def test_es_par(self):
        print("Ejecutando prueba para es_par(2)...")
        self.assertTrue(es_par(2))     
        print("Prueba para es_par(2) completada.")
        
        print("Ejecutando prueba para es_par(3)...")
        self.assertFalse(es_par(3))    
        print("Prueba para es_par(3) completada.")

if __name__ == '__main__':
    unittest.main()