import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test0(self):
        testcase = '''ANDKqe'''
        expect = '''ANDKqe,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 0))
    def test1(self):
        testcase = '''kasdj3432lkj'''
        expect = '''kasdj3432lkj,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 1))
    def test2(self):
        testcase = '''JK__3493k__lkdsfj'''
        expect = '''JK__3493k__lkdsfj,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 2))
    def test3(self):
        testcase = '''342kjlsfk'''
        expect = '''342,kjlsfk,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 3))
    def test4(self):
        testcase = '''$k32j3'''
        expect = '''Error Token $'''
        self.assertTrue(TestLexer.test(testcase, expect, 4))
    def test5(self):
        testcase = '''k2j3k4j'''
        expect = '''k2j3k4j,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 5))
    def test6(self):
        testcase = '''_'''
        expect = '''_,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 6))
    def test7(self):
        testcase = '''2'''
        expect = '''2,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 7))
    def test8(self):
        testcase = '''_dk'''
        expect = '''_dk,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 8))
    def test9(self):
        testcase = '''for'''
        expect = '''for,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 9))
    def test10(self):
        testcase = '''"string be like this"'''
        expect = '''string be like this,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 10))
    def test11(self):
        testcase = '''"string with escape characters \\n \\t \\r \\b \\f \\a \\" "'''
        expect = '''Illegal Escape In String: string with escape characters \\n \\t \\r \\b \\f \\a'''
        self.assertTrue(TestLexer.test(testcase, expect, 11))
    def test12(self):
        testcase = '''"string unclosed'''
        expect = '''Unclosed String: string unclosed'''
        self.assertTrue(TestLexer.test(testcase, expect, 12))
    def test13(self):
        testcase = '''1231289'''
        expect = '''1231289,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 13))
    def test14(self):
        testcase = '''21312 3124 _234'''
        expect = '''21312,3124,_234,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 14))
    def test15(self):
        testcase = '''123.213'''
        expect = '''123.213,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 15))
    def test16(self):
        testcase = '''23e4'''
        expect = '''23e4,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 16))
    def test17(self):
        testcase = '''213.123.213'''
        expect = '''213.123,.,213,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 17))
    def test18(self):
        testcase = '''213.123e213'''
        expect = '''213.123e213,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 18))
    def test19(self):
        testcase = ''''''
        expect = '''<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 19))
    def test20(self):
        testcase = '''{1, 5, 7, 12} or {"Kangxi", "Yongzheng", "Qianlong"}.'''
        expect = '''{,1,,,5,,,7,,,12,},or,{,Kangxi,,,Yongzheng,,,Qianlong,},.,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 20))
    def test21(self):
        testcase = '''! && || == !='''
        expect = '''!,&&,||,==,!=,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 21))
    def test22(self):
        testcase = '''+ - * / %'''
        expect = '''+,-,*,/,%,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 22))
    def test23(self):
        testcase = '''== != > >= < <='''
        expect = '''==,!=,>,>=,<,<=,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 23))
    def test24(self):
        testcase = '''::'''
        expect = '''::,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 24))
    def test25(self):
        testcase = '''a[0, 0], a[0, 1], a[0, 2], a[1, 0], a[1, 1], a[1, 2]'''
        expect = '''a,[,0,,,0,],,,a,[,0,,,1,],,,a,[,0,,,2,],,,a,[,1,,,0,],,,a,[,1,,,1,],,,a,[,1,,,2,],<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 25))
    def test26(self):
        testcase = '''i : integer; a : array[1, 2] of integer;'''
        expect = '''i,:,integer,;,a,:,array,[,1,,,2,],of,integer,;,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 26))