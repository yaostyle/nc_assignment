#!/usr/bin/env python3

from master import run, exit_loop
import unittest, asyncio
from aiounittest import async_test

class MasterTest(unittest.TestCase):
    @async_test
    async def test_async_run_normal(self):
        """ Test Async run() """
        result = await run()
        expected = True
        self.assertIsNone(result, expected)

    def test_exit_with_zero(self):
        """ Test exit with param: 0 """
        test_case = 0
        expected = None
        self.assertEqual(exit_loop(test_case), expected)

    def test_exit_with_one(self):
        """ Test exit with zero param: 1"""
        test_case = 1
        expected = None
        self.assertEqual(exit_loop(test_case), expected)

unittest.main()