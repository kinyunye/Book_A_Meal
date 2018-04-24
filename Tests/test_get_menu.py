import unittest
import json
import sys
import requests
from get_menu import *

class GetmealTest(unittest.TestCase):
	def test_get_meal(self):
		response = requests.get('http://127.0.0.1:5000/')
		self.assertEqual(response.json(),{'meal':'Coconut Rice','Price':300})


if __name__ == "__main__":
	unittest.main()
