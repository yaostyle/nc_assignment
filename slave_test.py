#!/usr/bin/env python3

from slave import *
import unittest

class SlaveTest(unittest.TestCase):
    def test_http_fetch(self):
        """ Test normal url with exptected code 0 """
        with self.assertRaises(SystemExit) as cm:
            run()
            expected = 0
            self.assertEqual(cm.exception.code, expected)
    
    def test_http_fetch_with_wrong_url(self):
        """ Test incorrect url with expected code: 1 """
        with self.assertRaises(SystemExit) as cm:
            api = 'https://postman-echo.com/elay/'
            run()
            expected = 1
            self.assertEqual(cm.exception.code, expected)

    def test_http_fetch_with_network_issue(self):
        """ Test network issue with expected code: 2"""
        with self.assertRaises(SystemExit) as cm:
            api = 'ht://postman-echo.com/delay/'
            run()
            expected = 2
            self.assertEqual(cm.exception.code, expected)
            
unittest.main()