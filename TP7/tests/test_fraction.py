import unittest
from fraction import Fraction
import pandas as pd

class TestFraction(unittest.TestCase):

    # Test du constructeur
    def test_constructor(self):
        # Cas classique
        f = Fraction(4, 8)
        self.assertEqual(f.numerator, 1)
        self.assertEqual(f.denominator, 2)
        
        # Cas du dénominateur nul
        with self.assertRaises(ValueError):
            Fraction(1, 0)

    # Test de la méthode __str__()
    def test_str(self):
        f = Fraction(5, 2)
        self.assertEqual(str(f), "5/2")
        
    # Test de la méthode as_mixed_number()
    def test_as_mixed_number(self):
        f = Fraction(5, 2)
        self.assertEqual(f.as_mixed_number(), "2 1/2")
        
    # Test de l'addition de fractions
    def test_addition(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 + f2
        self.assertEqual(result.numerator, 5)
        self.assertEqual(result.denominator, 6)
        
    # Test de la division de fractions
    def test_division(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 4)
        result = f1 / f2
        self.assertEqual(result.numerator, 2)
        self.assertEqual(result.denominator, 1)
        
        # Division par zéro
        with self.assertRaises(ZeroDivisionError):
            f1 / Fraction(0, 1)

    # Test une fraction négative
    def test_negative_fraction(self):
        f1 = Fraction(-1, 2)
        self.assertEqual(str(f1), "-1/2")
        
        f2 = Fraction(1, -2)
        self.assertEqual(str(f2), "-1/2")
        
        f3 = Fraction(-1, -2)
        self.assertEqual(str(f3), "1/2")

            
    # Test de la méthode __eq__()
    def test_eq(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 4)
        self.assertTrue(f1 == f2)
        
        f3 = Fraction(3, 4)
        self.assertFalse(f1 == f3)

    # Test de la méthode is_integer()
    def test_is_integer(self):
        f1 = Fraction(6, 2)
        self.assertTrue(f1.is_integer())
        
        f2 = Fraction(5, 2)
        self.assertFalse(f2.is_integer())

    # Test de la méthode is_proper()
    def test_is_proper(self):
        f1 = Fraction(3, 4)
        self.assertTrue(f1.is_proper())
        
        f2 = Fraction(5, 4)
        self.assertFalse(f2.is_proper())
    
    # Test de la méthode is_adjacent_to()
    def test_is_adjacent_to(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 3)
        self.assertTrue(f1.is_adjacent_to(f2))
        
        f3 = Fraction(3, 4)
        self.assertFalse(f1.is_adjacent_to(f3))

def run_tests():
    # Exécution des tests
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFraction)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    # Générer un tableau de résultats avec pandas
    test_results = {
        "Test Name": [test._testMethodName for test in result.testsRun],
        "Success": [test in result.successes for test in result.testsRun],
        "Error": [test in result.errors for test in result.testsRun],
        "Failure": [test in result.failures for test in result.testsRun],
    }
    
    # Convertir en DataFrame et afficher
    df = pd.DataFrame(test_results)
    print(df)

if __name__ == '__main__':
    run_tests()
