import unittest
import json
import sys
import requests
from get_menu import *

class GetmealTest(unittest.TestCase):
	def test_get_meal(self):
		response = requests.get('http://127.0.0.1:5000/')
		self.assertEqual(response.json(),{'Order No','Date','Meal','Price','Quantity'})


if __name__ == "__main__":
	unittest.main()
