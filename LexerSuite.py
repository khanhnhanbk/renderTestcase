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
        testcase = '''"string be like this"'''
        expect = '''string be like this,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 2))
    def test3(self):
        testcase = '''"Escaped characters: \\\\ \\n \\t \\r \\f \\b \\' \\""'''
        expect = '''Escaped characters: \\\\ \\n \\t \\r \\f \\b \\' \\",<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 3))
    def test4(self):
        testcase = '''"A string with a double quote (\\") in it"'''
        expect = '''A string with a double quote (\\") in it,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 4))
    def test5(self):
        testcase = '''"A string with an empty \\n line"'''
        expect = '''A string with an empty \\n line,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 5))
    def test6(self):
        testcase = '''"Unterminated string (missing closing quote)'''
        expect = '''Unclosed String: Unterminated string (missing closing quote)'''
        self.assertTrue(TestLexer.test(testcase, expect, 6))
    def test7(self):
        testcase = '''m5op4ti'''
        expect = '''m5op4ti,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 7))
    def test8(self):
        testcase = '''"\\  "'''
        expect = '''Illegal Escape In String: \\ '''
        self.assertTrue(TestLexer.test(testcase, expect, 8))
    def test9(self):
        testcase = '''"String with a new line before the closing quote\\n"'''
        expect = '''String with a new line before the closing quote\\n,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 9))
    def test10(self):
        testcase = '''{1, 2, 3}'''
        expect = '''{,1,,,2,,,3,},<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 10))
    def test11(self):
        testcase = '''{1, 2, 3, 4, 5}'''
        expect = '''{,1,,,2,,,3,,,4,,,5,},<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 11))
    def test12(self):
        testcase = '''{"hello", "world"}'''
        expect = '''{,hello,,,world,},<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 12))
    def test13(self):
        testcase = '''"string with escape characters \\n \\t \\r \\b \\f \\a \\" "'''
        expect = '''Illegal Escape In String: string with escape characters \\n \\t \\r \\b \\f \\a'''
        self.assertTrue(TestLexer.test(testcase, expect, 13))
    def test14(self):
        testcase = '''{true, false, true, false}'''
        expect = '''{,true,,,false,,,true,,,false,},<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 14))
    def test15(self):
        testcase = '''{1.23, 4.56, 7.89}'''
        expect = '''{,1.23,,,4.56,,,7.89,},<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 15))
    def test16(self):
        testcase = '''{1, "hello", true, 3.14}'''
        expect = '''{,1,,,hello,,,true,,,3.14,},<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 16))
    def test17(self):
        testcase = '''XHYX9jKkW'''
        expect = '''XHYX9jKkW,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 17))
    def test18(self):
        testcase = '''"string unclosed'''
        expect = '''Unclosed String: string unclosed'''
        self.assertTrue(TestLexer.test(testcase, expect, 18))
    def test19(self):
        testcase = '''1231289'''
        expect = '''1231289,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 19))
    def test20(self):
        testcase = '''21312 3124 _234'''
        expect = '''21312,3124,_234,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 20))
    def test21(self):
        testcase = '''123.213'''
        expect = '''123.213,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 21))
    def test22(self):
        testcase = '''23e4'''
        expect = '''23e4,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 22))
    def test23(self):
        testcase = '''213.123.213'''
        expect = '''213.123,.,213,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 23))
    def test24(self):
        testcase = '''213.123e213'''
        expect = '''213.123e213,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 24))
    def test25(self):
        testcase = ''''''
        expect = '''<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 25))
    def test26(self):
        testcase = '''JK__3493k__lkdsfj'''
        expect = '''JK__3493k__lkdsfj,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 26))
    def test27(self):
        testcase = '''{1, 5, 7, 12} or {"Kangxi", "Yongzheng", "Qianlong"}.'''
        expect = '''{,1,,,5,,,7,,,12,},or,{,Kangxi,,,Yongzheng,,,Qianlong,},.,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 27))
    def test28(self):
        testcase = '''! && || == !='''
        expect = '''!,&&,||,==,!=,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 28))
    def test29(self):
        testcase = '''+ - * / %'''
        expect = '''+,-,*,/,%,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 29))
    def test30(self):
        testcase = '''== != > >= < <='''
        expect = '''==,!=,>,>=,<,<=,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 30))
    def test31(self):
        testcase = '''::'''
        expect = '''::,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 31))
    def test32(self):
        testcase = '''a[0, 0], a[0, 1], a[0, 2], a[1, 0], a[1, 1], a[1, 2]'''
        expect = '''a,[,0,,,0,],,,a,[,0,,,1,],,,a,[,0,,,2,],,,a,[,1,,,0,],,,a,[,1,,,1,],,,a,[,1,,,2,],<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 32))
    def test33(self):
        testcase = '''i : integer; a : array[1, 2] of integer;'''
        expect = '''i,:,integer,;,a,:,array,[,1,,,2,],of,integer,;,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 33))
    def test34(self):
        testcase = '''Test identify'''
        expect = '''Test,identify,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 34))
    def test35(self):
        testcase = '''ZvUwNl'''
        expect = '''ZvUwNl,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 35))
    def test36(self):
        testcase = '''QGxH8yKj1'''
        expect = '''QGxH8yKj1,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 36))
    def test37(self):
        testcase = '''342kjlsfk'''
        expect = '''342,kjlsfk,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 37))
    def test38(self):
        testcase = '''vNkTbKcH9'''
        expect = '''vNkTbKcH9,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 38))
    def test39(self):
        testcase = '''sM8tCJYg'''
        expect = '''sM8tCJYg,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 39))
    def test40(self):
        testcase = '''rDpGxV7'''
        expect = '''rDpGxV7,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 40))
    def test41(self):
        testcase = '''uFtLcJ7'''
        expect = '''uFtLcJ7,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 41))
    def test42(self):
        testcase = '''kDfX9kZ'''
        expect = '''kDfX9kZ,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 42))
    def test43(self):
        testcase = '''eBpR7vYf'''
        expect = '''eBpR7vYf,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 43))
    def test44(self):
        testcase = '''cameCaleCase'''
        expect = '''cameCaleCase,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 44))
    def test45(self):
        testcase = '''333kk333k3k'''
        expect = '''333,kk333k3k,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 45))
    def test46(self):
        testcase = '''identify'''
        expect = '''identify,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 46))
    def test47(self):
        testcase = '''lasdfk11212klj'''
        expect = '''lasdfk11212klj,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 47))
    def test48(self):
        testcase = '''$k32j3'''
        expect = '''Error Token $'''
        self.assertTrue(TestLexer.test(testcase, expect, 48))
    def test49(self):
        testcase = '''Test Operators'''
        expect = '''Test,Operators,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 49))
    def test50(self):
        testcase = '''+=++=='''
        expect = '''+,=,+,+,==,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 50))
    def test51(self):
        testcase = '''== = = ====='''
        expect = '''==,=,=,==,==,=,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 51))
    def test52(self):
        testcase = '''-=-=----*&&&&'''
        expect = '''-,=,-,=,-,-,-,-,*,&&,&&,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 52))
    def test53(self):
        testcase = '''[] () }{{{}}}}}}'''
        expect = '''[,],(,),},{,{,{,},},},},},},<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 53))
    def test54(self):
        testcase = '''!= >= <= ?'''
        expect = '''!=,>=,<=,Error Token ?'''
        self.assertTrue(TestLexer.test(testcase, expect, 54))
    def test55(self):
        testcase = '''Test literals'''
        expect = '''Test,literals,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 55))
    def test56(self):
        testcase = '''integer'''
        expect = '''integer,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 56))
    def test57(self):
        testcase = '''0'''
        expect = '''0,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 57))
    def test58(self):
        testcase = '''alo'''
        expect = '''alo,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 58))
    def test59(self):
        testcase = '''k2j3k4j'''
        expect = '''k2j3k4j,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 59))
    def test60(self):
        testcase = '''1'''
        expect = '''1,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 60))
    def test61(self):
        testcase = '''9'''
        expect = '''9,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 61))
    def test62(self):
        testcase = '''123'''
        expect = '''123,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 62))
    def test63(self):
        testcase = '''456_789'''
        expect = '''456789,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 63))
    def test64(self):
        testcase = '''0_0_0'''
        expect = '''0,_0_0,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 64))
    def test65(self):
        testcase = '''1_000_000'''
        expect = '''1000000,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 65))
    def test66(self):
        testcase = '''-42'''
        expect = '''-,42,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 66))
    def test67(self):
        testcase = '''-1_000'''
        expect = '''-,1000,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 67))
    def test68(self):
        testcase = '''-123_456_789'''
        expect = '''-,123456789,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 68))
    def test69(self):
        testcase = '''01'''
        expect = '''0,1,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 69))
    def test70(self):
        testcase = '''_'''
        expect = '''_,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 70))
    def test71(self):
        testcase = '''3k2'''
        expect = '''3,k2,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 71))
    def test72(self):
        testcase = '''1_2_3'''
        expect = '''123,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 72))
    def test73(self):
        testcase = '''1__2__3'''
        expect = '''1,__2__3,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 73))
    def test74(self):
        testcase = '''123_'''
        expect = '''123,_,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 74))
    def test75(self):
        testcase = ''' --------- float'''
        expect = '''-,-,-,-,-,-,-,-,-,float,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 75))
    def test76(self):
        testcase = '''0.0'''
        expect = '''0.0,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 76))
    def test77(self):
        testcase = '''0.5'''
        expect = '''0.5,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 77))
    def test78(self):
        testcase = '''1.0'''
        expect = '''1.0,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 78))
    def test79(self):
        testcase = '''1.5'''
        expect = '''1.5,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 79))
    def test80(self):
        testcase = '''123.456'''
        expect = '''123.456,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 80))
    def test81(self):
        testcase = '''2'''
        expect = '''2,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 81))
    def test82(self):
        testcase = '''0.123_456'''
        expect = '''0.123456,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 82))
    def test83(self):
        testcase = '''__dska'''
        expect = '''__dska,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 83))
    def test84(self):
        testcase = '''1_000.0'''
        expect = '''1000.0,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 84))
    def test85(self):
        testcase = '''-1.23'''
        expect = '''-,1.23,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 85))
    def test86(self):
        testcase = '''1.23E10'''
        expect = '''1.23E10,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 86))
    def test87(self):
        testcase = '''1_2.3'''
        expect = '''12.3,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 87))
    def test88(self):
        testcase = '''1.23e-10'''
        expect = '''1.23e-10,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 88))
    def test89(self):
        testcase = '''1.23e+10'''
        expect = '''1.23e+10,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 89))
    def test90(self):
        testcase = '''-1.23e-10'''
        expect = '''-,1.23e-10,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 90))
    def test91(self):
        testcase = '''123.456e7'''
        expect = '''123.456e7,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 91))
    def test92(self):
        testcase = '''_dk'''
        expect = '''_dk,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 92))
    def test93(self):
        testcase = '''123.456E-7'''
        expect = '''123.456E-7,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 93))
    def test94(self):
        testcase = '''.'''
        expect = '''.,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 94))
    def test95(self):
        testcase = '''df)2_$'''
        expect = '''df,),2,_,Error Token $'''
        self.assertTrue(TestLexer.test(testcase, expect, 95))
    def test96(self):
        testcase = '''1.'''
        expect = '''1,.,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 96))
    def test97(self):
        testcase = '''1e'''
        expect = '''1,e,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 97))
    def test98(self):
        testcase = '''1.e10'''
        expect = '''1,.,e10,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 98))
    def test99(self):
        testcase = '''1.23e-'''
        expect = '''1.23,e,-,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 99))
    def test100(self):
        testcase = '''1._2'''
        expect = '''1,.,_2,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 100))
    def test101(self):
        testcase = '''1.2_e3'''
        expect = '''1.2,_e3,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 101))
    def test102(self):
        testcase = '''true'''
        expect = '''true,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 102))
    def test103(self):
        testcase = '''for'''
        expect = '''for,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 103))
    def test104(self):
        testcase = '''false'''
        expect = '''false,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 104))
    def test105(self):
        testcase = '''String'''
        expect = '''String,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 105))
    def test106(self):
        testcase = '''"Hello"'''
        expect = '''Hello,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 106))
    def test107(self):
        testcase = '''dsfl11lkj34'''
        expect = '''dsfl11lkj34,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 107))
    def test108(self):
        testcase = '''"amind \\t \\n"'''
        expect = '''amind \\t \\n,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 108))
    def test109(self):
        testcase = '''"He asked me: \\"Where is John?\\""'''
        expect = '''He asked me: \\"Where is John?\\",<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 109))
    def test110(self):
        testcase = '''"hello"'''
        expect = '''hello,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 110))
    def test111(self):
        testcase = '''"world"'''
        expect = '''world,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 111))
    def test112(self):
        testcase = '''""'''
        expect = ''',<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 112))
    def test113(self):
        testcase = '''"Hello, world!"'''
        expect = '''Hello, world!,<EOF>'''
        self.assertTrue(TestLexer.test(testcase, expect, 113))