import unittest
import json
from salesCalculator import calculateTax, processItems


class TestStringMethods(unittest.TestCase):

    def setUp(self) -> None:
        self.testObject = json.loads("""{
    "items": [
        {
            "product": "book",
            "qty": 2,
            "price": 12.49,
            "specialproduct": true,
            "imported": false
        }
    ]
    }""")
    
        self.expetedResult = json.loads("""{
        "items": [
            {
                "product": "book",
                "qty": 2,
                "price": 24.98,
                "specialproduct": true,
                "imported": false
            }
        ],
        "SalesTaxes": 0.0,
        "Total": 24.98
    }""")

        self.amount = 14.99
        self.expectedTax = 1.499
        self.calculatedTax = calculateTax(self.amount)
        self.calculatedResult = processItems(self.testObject)

    def test_processItems(self):
        self.assertEqual(self.calculatedResult, self.expetedResult)
    
    def test_calculateTaxes(self):
        self.assertEqual(self.calculatedTax, self.expectedTax)

    def test_calculatedAmount(self):
        self.assertEqual(self.amount+self.expectedTax, self.amount + self.calculatedTax)
    
    def test_wrongCalculate(self):
        self.assertNotEqual(self.amount, self.amount + self.expectedTax)
        



if __name__ == '__main__':
    unittest.main()
