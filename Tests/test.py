#!/usr/bin/env python3

"""Tests for Basic Functions"""
import sys
import json
import unittest
sys.path.append("..//..")
from get_menu import *


class TestFunctions(unittest.TestCase):

    def setup(self):
        get_menu.get_menu.config['TESTING'] = True
        self.get_menu = get_menu.get_menu.test_client()

    def test_output(self):
        with get_menu.test_request_context():
            out = output('Coconut Rice','300')
            response = [
                {'meal':'Coconut Rice','Price':'300'
                }
            ]
            data = json.loads(out.get_data(as_text=True))
            self.assertEqual(data['response'], response)


if __name__ == '__main__':
    unittest.main()