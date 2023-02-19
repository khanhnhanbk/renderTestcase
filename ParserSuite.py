import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test0(self):
        testcase = '''y :      function          auto      (  )      inherit     ci {  } T :      function          void      (      inherit          out     m7Gq :      array      [ 0 , 6_21 , 4 ]      of          integer      ,      inherit          out     r :      array      [ 8930_5 , 0 , 0 , 6_467_9356 ]      of          integer      ,      inherit     uOe :      string      )  {      break      ;  } '''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 0))
    def test1(self):
        testcase = '''z:    void    ;Y,AxC,gK,W:    void    ;v:    void    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 1))
    def test2(self):
        testcase = '''Ta:    function        array    [0,0]    of        boolean    (    out    t:    array    [0]    of        string    ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2))
    def test3(self):
        testcase = '''r:    function        integer    (    out    UQSrDW:    string    ,Dy:    array    [65_73_092_5_2_32]    of        string    )    inherit    tk{}z:    function        boolean    (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 3))
    def test4(self):
        testcase = '''A:    function        float    (    inherit        out    RNn3EBq:    auto    ){}i:    float    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 4))
    def test5(self):
        testcase = '''H:    function        array    [0,74_5921330,0,4,8_3]    of        integer    ()    inherit    lb4{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 5))
    def test6(self):
        testcase = '''Pgf:    boolean    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 6))
    def test7(self):
        testcase = '''d:    function        void    ()    inherit    i0{}lY3:    auto    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 7))
    def test8(self):
        testcase = '''N:    function        auto    (    inherit    JZ:    boolean    )    inherit    fspC7{    break    ;}s:    function        void    (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 8))
    def test9(self):
        testcase = '''QpE,mhb,Y:    void    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 9))