import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test2000(self):
        testcase = '''y :      function          auto      (  )      inherit     ci {  } T :      function          void      (      inherit          out     m7Gq :      array      [ 0 , 6_21 , 4 ]      of          integer      ,      inherit          out     r :      array      [ 8930_5 , 0 , 0 , 6_467_9356 ]      of          integer      ,      inherit     uOe :      string      )  {      break      ;  } '''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2000))
    def test2001(self):
        testcase = '''z:    void    ;Y,AxC,gK,W:    void    ;v:    void    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2001))
    def test2002(self):
        testcase = '''Ta:    function        array    [0,0]    of        boolean    (    out    t:    array    [0]    of        string    ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2002))
    def test2003(self):
        testcase = '''r:    function        integer    (    out    UQSrDW:    string    ,Dy:    array    [65_73_092_5_2_32]    of        string    )    inherit    tk{}z:    function        boolean    (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2003))
    def test2004(self):
        testcase = '''A:    function        float    (    inherit        out    RNn3EBq:    auto    ){}i:    float    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2004))
    def test2005(self):
        testcase = '''H:    function        array    [0,74_5921330,0,4,8_3]    of        integer    ()    inherit    lb4{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2005))
    def test2006(self):
        testcase = '''Pgf:    boolean    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2006))
    def test2007(self):
        testcase = '''d:    function        void    ()    inherit    i0{}lY3:    auto    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2007))
    def test2008(self):
        testcase = '''N:    function        auto    (    inherit    JZ:    boolean    )    inherit    fspC7{    break    ;}s:    function        void    (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2008))
    def test2009(self):
        testcase = '''QpE,mhb,Y:    void    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2009))
    def test2010(self):
        testcase = '''ji:    function        integer    (    inherit    jX:    integer    ,    out    S:    boolean    ){}xh:    function        auto    (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2010))
    def test2011(self):
        testcase = '''M9:    auto    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2011))
    def test2012(self):
        testcase = '''F:    integer    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2012))
    def test2013(self):
        testcase = '''Z5wMknqDo:    array    [0]    of        string    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2013))
    def test2014(self):
        testcase = '''RK:    function        array    [0,0]    of        float    ()    inherit    bF7P{}v:    array    [0]    of        integer    ;q,x_:    void    ;r:    float    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2014))
    def test2015(self):
        testcase = '''p:    function        integer    (    inherit    H:    boolean    ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2015))
    def test2016(self):
        testcase = '''tYH:    function        auto    (    out    j:    float    ,    inherit        out    I7r:    array    [0,657_36_9_6,3_85_76101_02]    of        boolean    ,    inherit    x:    boolean    ,t:    array    [7,110]    of        float    ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2016))
    def test2017(self):
        testcase = '''LAC:    void    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2017))
    def test2018(self):
        testcase = '''S,c:    boolean    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2018))
    def test2019(self):
        testcase = '''i:    function        string    (    inherit        out    T:    boolean    ,    inherit    I2:    boolean    )    inherit    s{    break    ;NM();}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2019))
    def test2020(self):
        testcase = '''E8:    function        string    (    out    x1dL:    auto    ,    out    T:    string    ,    inherit        out    ylM:    array    [1,0,9_79547]    of        boolean    ,qV:    string    ,    inherit    u:    array    [0]    of        float    ){h,AvokI:    array    [0,0,0]    of        boolean    ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2020))
    def test2021(self):
        testcase = '''nGf:    function        array    [13_2]    of        integer    (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2021))
    def test2022(self):
        testcase = '''sW:    function        void    (    inherit    Ed:    boolean    )    inherit    O{AUh();}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2022))
    def test2023(self):
        testcase = '''e:    function        void    (    out    xMJVatI:    array    [0]    of        float    )    inherit    P{}rF:    string    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2023))
    def test2024(self):
        testcase = '''k:    function        boolean    (O:    array    [473818]    of        float    ){}waf:    string    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2024))
    def test2025(self):
        testcase = '''l,j:    void    ;iv,ip:    array    [86_8]    of        float    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2025))
    def test2026(self):
        testcase = '''o:    function        auto    (){}Ks:    function        string    (    inherit    U4:    string    ){c,Jcs,rj,g,r,C:    void    ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2026))
    def test2027(self):
        testcase = '''wxQwI:    function        integer    (o:    array    [0,283477350]    of        float    ,    inherit    cfaBl:    auto    ,    inherit        out    _N04N:    array    [8490_9_255_78,67_89]    of        boolean    ,    inherit    c:    string    )    inherit    ms{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2027))
    def test2028(self):
        testcase = '''r:    auto    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2028))
    def test2029(self):
        testcase = '''WZ:    function        void    (){    continue    ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2029))
    def test2030(self):
        testcase = '''cyNe8:    function        boolean    ()    inherit    jH{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2030))
    def test2031(self):
        testcase = '''H:    function        array    [225,0,0]    of        boolean    (z:    float    )    inherit    q8{    continue    ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2031))
    def test2032(self):
        testcase = '''WW:    function        void    ()    inherit    e_R{}x:    function        void    (){}PVpjIIi:    string    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2032))
    def test2033(self):
        testcase = '''b_:    function        auto    ()    inherit    sGA{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2033))
    def test2034(self):
        testcase = '''N:    function        auto    (    inherit    n:    auto    )    inherit    X{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2034))
    def test2035(self):
        testcase = '''VK:    integer    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2035))
    def test2036(self):
        testcase = '''jcS:    function        array    [63,2_33193_51_151]    of        integer    (vqx:    array    [1]    of        integer    ,    out    VDe:    integer    ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2036))
    def test2037(self):
        testcase = '''T:    void    ;j:    function        auto    (    out    s:    auto    ,    inherit        out    T:    auto    )    inherit    Wt{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2037))
    def test2038(self):
        testcase = '''K8t:    function        auto    ()    inherit    q{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2038))
    def test2039(self):
        testcase = '''b:    function        string    ()    inherit    Nk{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2039))
    def test2040(self):
        testcase = '''J:    array    [5,0,0]    of        float    ;h,z:    array    [6_2_7]    of        integer    ;iRx,Ul4Y:    array    [0,7,0,0]    of        integer    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2040))
    def test2041(self):
        testcase = '''BH:    function        string    (    out    OH:    auto    ){    break    ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2041))
    def test2042(self):
        testcase = '''F:    void    ;B:    function        integer    (    inherit    g:    boolean    )    inherit    Z{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2042))
    def test2043(self):
        testcase = '''U:    function        array    [858361,0,2,40]    of        string    ()    inherit    KY5{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2043))
    def test2044(self):
        testcase = '''x,CDsLsr,_:    void    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2044))
    def test2045(self):
        testcase = '''Kb:    function        array    [7]    of        boolean    (    inherit        out    r:    auto    )    inherit    _{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2045))
    def test2046(self):
        testcase = '''L:    function        auto    ()    inherit    Vx{    break    ;    continue    ;A();}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2046))
    def test2047(self):
        testcase = '''Rv:    auto    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2047))
    def test2048(self):
        testcase = '''Y:    function        void    (mBW5Z0:    array    [7_550,0]    of        boolean    )    inherit    j{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2048))
    def test2049(self):
        testcase = '''ZDpebZZz:    function        auto    (){    break    ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2049))
    def test2050(self):
        testcase = '''m:    auto    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2050))
    def test2051(self):
        testcase = '''f,z,_a:    integer    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2051))
    def test2052(self):
        testcase = '''M5:    function        void    (    inherit        out    yt:    array    [24_36]    of        integer    ,    out    YD0:    array    [0]    of        string    ,    inherit    o:    array    [15_35646_38_2_6_6_17945_224_6_01589_3]    of        string    ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2052))
    def test2053(self):
        testcase = '''mT:    function        void    ()    inherit    W{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2053))
    def test2054(self):
        testcase = '''yHWLN1:    array    [0,3,7_35_6392]    of        float    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2054))
    def test2055(self):
        testcase = '''HvU7Kw:    string    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2055))
    def test2056(self):
        testcase = '''E5l:    array    [0]    of        boolean    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2056))
    def test2057(self):
        testcase = '''z:    function        array    [0,5_14_6_50,0,0,9_482_0_82891_7]    of        boolean    ()    inherit    Xb{RMo:    boolean    ;    break    ;}itLWJn7:    array    [64_04]    of        string    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2057))
    def test2058(self):
        testcase = '''p:    function        auto    (    inherit        out    iX:    array    [2,0,0]    of        string    ,    inherit        out    W5C:    integer    ,    out    i:    array    [0,60,0]    of        integer    )    inherit    H{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2058))
    def test2059(self):
        testcase = ''''''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2059))
    def test2060(self):
        testcase = '''eRVKH: array [0,0,4,0,0,0,0,7] of  float ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2060))
    def test2061(self):
        testcase = '''TA: function  float ( inherit V: auto , out h: auto ) inherit wt{ return ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2061))
    def test2062(self):
        testcase = '''C: auto ;A: function  auto (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2062))
    def test2063(self):
        testcase = '''Tk: function  void (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2063))
    def test2064(self):
        testcase = '''E: float ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2064))
    def test2065(self):
        testcase = '''b77: function  array [38_10_9_38,421_01,0,0] of  integer ( out x6O: string , out C: array [0,26_3,2,94] of  integer , inherit  out HJ: auto ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2065))
    def test2066(self):
        testcase = '''Q: function  array [0] of  integer () inherit Y{}H4: function  array [6931] of  string ( inherit O: auto , inherit H: auto ,y: auto , inherit LfBUQ: array [772] of  integer , out A: array [0] of  boolean , inherit  out OZ: boolean , inherit  out RL: array [0] of  boolean ){}nM0,GA: integer ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2066))
    def test2067(self):
        testcase = '''IO: void ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2067))
    def test2068(self):
        testcase = '''SHJ: function  void ( inherit Ov: integer , inherit U: array [0] of  float ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2068))
    def test2069(self):
        testcase = '''c,QF7: array [1014_82,10_6_43_0] of  string ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2069))
    def test2070(self):
        testcase = '''cD: function  array [41_7_2] of  integer () inherit Xn{}y,k,V,a,y,jVX: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2070))
    def test2071(self):
        testcase = '''C: function  void ( inherit Q82SG: auto ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2071))
    def test2072(self):
        testcase = '''q: function  auto ( inherit  out Ri: array [0] of  float , inherit  out q: string ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2072))
    def test2073(self):
        testcase = '''i3: function  void ( inherit WG: array [3_3_59_0_2,0] of  integer ) inherit VL{{}}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2073))
    def test2074(self):
        testcase = '''Spl,b0a: auto ;Z: function  array [41] of  string (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2074))
    def test2075(self):
        testcase = '''WV: function  string ( out u: auto ,Fk2: auto , inherit BG: auto ,exU6og: auto , inherit  out U: auto ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2075))
    def test2076(self):
        testcase = '''L,f7WdGj: array [0] of  string ;f8,Ta: integer ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2076))
    def test2077(self):
        testcase = '''S: function  void ( inherit JHHW: float , inherit G4: array [0] of  string , inherit  out n: auto ) inherit fh{ break ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2077))
    def test2078(self):
        testcase = '''iPT8Z: function  array [49,93_1] of  string (cx: array [0] of  float , inherit wX: string ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2078))
    def test2079(self):
        testcase = '''jP: function  void ( out c: float ) inherit D{c: void ; return ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2079))
    def test2080(self):
        testcase = '''Q4: auto ;C: function  auto ( inherit  out Ag: float , inherit U: array [0] of  string , out vd: array [28,0] of  boolean , out Y3: array [0,8_5_8_16_63775_8,0] of  float ) inherit l{}iS: void ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2080))
    def test2081(self):
        testcase = '''K3: function  string ( inherit  out Nl: string ){}b: function  integer (P: integer ) inherit q{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2081))
    def test2082(self):
        testcase = '''n: function  array [61012,289,23] of  float ( inherit  out DJoAG: float , inherit  out J: string ) inherit fj{}aZF8Q7: function  float ( inherit ZGEd: string ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2082))
    def test2083(self):
        testcase = '''t: void ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2083))
    def test2084(self):
        testcase = '''s7: array [8_2_2] of  integer ;z: function  string (jcivbhg: boolean ) inherit Igwi{ continue ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2084))
    def test2085(self):
        testcase = '''crD: function  void ( inherit  out E: array [1_6] of  float ){U();}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2085))
    def test2086(self):
        testcase = '''d: function  auto ( inherit  out c: auto ) inherit Gh_wY{ return ;}j9: function  array [5_723] of  boolean ( inherit M: auto ) inherit gI{ break ; continue ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2086))
    def test2087(self):
        testcase = '''C1: function  auto (G: array [52,345_79_08_06,431,0] of  float , inherit  out yS: integer , out EY: string ,Crp: array [99_5_2] of  string ) inherit v8{}d: function  array [0,0,7,27] of  integer ( inherit p: string , inherit v: boolean , inherit  out l: integer ,p: boolean ) inherit zn{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2087))
    def test2088(self):
        testcase = '''H: function  array [2] of  boolean ( inherit  out V: array [0,773220_8] of  integer ) inherit Zjr{}n: function  void (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2088))
    def test2089(self):
        testcase = '''JN: function  auto ( inherit a7v: boolean ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2089))
    def test2090(self):
        testcase = '''aj: array [0] of  integer ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2090))
    def test2091(self):
        testcase = '''l,L: array [476_8] of  string ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2091))
    def test2092(self):
        testcase = '''b71Al: function  void () inherit xZ{ break ; break ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2092))
    def test2093(self):
        testcase = '''RQoR: function  array [49] of  integer ( inherit vH0: array [0,745,0,1_9_3_11487_3_40] of  boolean , inherit O: array [4,0] of  float ) inherit o{k();}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2093))
    def test2094(self):
        testcase = '''A,u,tB: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2094))
    def test2095(self):
        testcase = '''Xt: function  auto (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2095))
    def test2096(self):
        testcase = '''lT: function  float ( out AtS: float , out BRDo3: auto , inherit  out f: auto ) inherit u{}iW: function  auto (W: auto ,O: boolean ) inherit V{ continue ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2096))
    def test2097(self):
        testcase = '''U: function  void ( out wZ: array [44_3287,57,0,23,0] of  integer ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2097))
    def test2098(self):
        testcase = '''k3: function  array [4,0,0,78429_2_8559,0,9] of  float (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2098))
    def test2099(self):
        testcase = '''R2t: function  auto ( inherit K: auto , inherit Y: array [0] of  boolean ) inherit f{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2099))
    def test2100(self):
        testcase = '''yI: function  void (R: auto ) inherit To{{}}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2100))
    def test2101(self):
        testcase = '''CGV1db8rpu,iRQPT,k,I,fx: array [6482_72,8_8692] of  string ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2101))
    def test2102(self):
        testcase = '''MAs: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2102))
    def test2103(self):
        testcase = '''TXCs: function  array [118_48_5_155,3] of  boolean ( inherit lR: auto ) inherit jJU{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2103))
    def test2104(self):
        testcase = '''u7: array [89_6] of  boolean ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2104))
    def test2105(self):
        testcase = '''a: function  auto ( out o: array [0] of  float , inherit AC1: string ) inherit IIi{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2105))
    def test2106(self):
        testcase = '''Cpq: function  array [67] of  boolean (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2106))
    def test2107(self):
        testcase = '''E: array [0] of  integer ;e: float ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2107))
    def test2108(self):
        testcase = '''P: function  string (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2108))
    def test2109(self):
        testcase = '''gb: function  auto (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2109))
    def test2110(self):
        testcase = '''S: function  void ( inherit  out J: array [0] of  integer ,C: string ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2110))
    def test2111(self):
        testcase = '''c: function  void ( inherit g: auto ) inherit aM{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2111))
    def test2112(self):
        testcase = '''U,k,Rg: integer ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2112))
    def test2113(self):
        testcase = '''B: function  float ( out r54: auto ) inherit NU{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2113))
    def test2114(self):
        testcase = '''r: function  void (Aw: auto ,x: array [0] of  boolean ){ break ;}At: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2114))
    def test2115(self):
        testcase = '''T: string ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2115))
    def test2116(self):
        testcase = '''m: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2116))
    def test2117(self):
        testcase = '''f: function  void (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2117))
    def test2118(self):
        testcase = '''HI2KjC: function  auto () inherit S{ break ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2118))
    def test2119(self):
        testcase = '''ang: function  array [0,8_5_12,6_084,586_46,9_95_1] of  string (){ continue ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2119))
    def test2120(self):
        testcase = '''P: function  auto (wt: float , inherit fdCXv: auto , inherit  out DdM: auto ){}B5,x,vjh: integer ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2120))
    def test2121(self):
        testcase = '''t: void ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2121))
    def test2122(self):
        testcase = '''N: function  array [394,0] of  integer (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2122))
    def test2123(self):
        testcase = '''hvY: function  boolean () inherit S{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2123))
    def test2124(self):
        testcase = '''_: function  void () inherit S{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2124))
    def test2125(self):
        testcase = '''F: function  array [0,7203,5_62_09,9_929] of  string ( inherit gR: float , inherit  out fp6h4: boolean ,VXwh: array [0] of  integer , out g: array [0] of  float , out ku: auto ) inherit t{ZT: string ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2125))
    def test2126(self):
        testcase = '''KbDvh: function  string () inherit v9{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2126))
    def test2127(self):
        testcase = '''BZQH: void ;_: function  array [2991_15] of  string (P: integer ){}s: function  void () inherit d{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2127))
    def test2128(self):
        testcase = '''R: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2128))
    def test2129(self):
        testcase = '''B,I4,s: auto ;r: void ;NpB,g: void ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2129))
    def test2130(self):
        testcase = '''i,rzz,D,wsqS,Q,pF,_bC: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2130))
    def test2131(self):
        testcase = '''Fs: function  auto (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2131))
    def test2132(self):
        testcase = '''Ik: function  array [0,29_1,0] of  integer () inherit b{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2132))
    def test2133(self):
        testcase = '''SG: array [3] of  integer ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2133))
    def test2134(self):
        testcase = '''q: function  array [0] of  string (){ return ;{} break ;}SGF: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2134))
    def test2135(self):
        testcase = '''fy: function  auto () inherit f{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2135))
    def test2136(self):
        testcase = '''_: function  array [8_258] of  float ( inherit GO: array [437_56] of  float , inherit gC: array [0,63_90_4075_1,3_26_8016] of  float ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2136))
    def test2137(self):
        testcase = '''R,V,J,Xn: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2137))
    def test2138(self):
        testcase = '''M,y,j: auto ;k,jRIh,dq8BZpj: boolean ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2138))
    def test2139(self):
        testcase = '''T: auto ;sAY,x,CQ,BA,HF,uQb: string ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2139))
    def test2140(self):
        testcase = '''F,Guy,p,d: float ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2140))
    def test2141(self):
        testcase = '''x: string ;R: void ;U: function  void ( out B6E: auto ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2141))
    def test2142(self):
        testcase = '''J: function  array [2275] of  string (BI3: array [0,2_9_5_85_13] of  float ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2142))
    def test2143(self):
        testcase = '''r,d: array [9993_8_041,88717_328,2,0] of  float ;UZ: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2143))
    def test2144(self):
        testcase = '''Sp: function  array [0,396,6_83_13] of  float ( inherit L3: integer , inherit k4: float ,pd0DnG: string ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2144))
    def test2145(self):
        testcase = '''G: function  array [0] of  string (cS: array [1,7_2] of  integer ,fE6: array [2,1] of  string ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2145))
    def test2146(self):
        testcase = '''W: function  auto () inherit W{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2146))
    def test2147(self):
        testcase = '''Cymf: array [63_1] of  string ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2147))
    def test2148(self):
        testcase = '''TR: function  array [2,630] of  integer ( inherit  out N9_: array [7302_1] of  string , inherit  out xm: array [0,128_5] of  string , inherit g: array [0] of  float ,R: auto ) inherit o_{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2148))
    def test2149(self):
        testcase = '''Z: function  array [54,0] of  integer ( inherit dc: array [0] of  float ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2149))
    def test2150(self):
        testcase = '''V: function  array [56_59993] of  boolean () inherit p{ break ;}D,v,BB: array [0,36,0,4,0] of  float ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2150))
    def test2151(self):
        testcase = '''B: function  float ( out Ja: auto , out w1eVLkrKY: auto ){ return ;g();}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2151))
    def test2152(self):
        testcase = '''pjx5P,rY: void ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2152))
    def test2153(self):
        testcase = '''ntB,YW: array [0,0,0] of  float ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2153))
    def test2154(self):
        testcase = '''O: array [4] of  integer ;G,X,Oe: void ;han,D,vS,x2: void ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2154))
    def test2155(self):
        testcase = '''Z: function  boolean () inherit vk{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2155))
    def test2156(self):
        testcase = '''_U2,z4VcX,E,vQ79: void ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2156))
    def test2157(self):
        testcase = '''g: function  float ( inherit PfLB: array [0,0] of  float , out EG9Y: string , inherit x: float ) inherit H{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2157))
    def test2158(self):
        testcase = '''NV: function  auto ( inherit X: array [5_4966] of  float , inherit C: array [442,0,5] of  integer ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2158))
    def test2159(self):
        testcase = '''aZ: function  auto (lm: array [0] of  float , inherit  out eYatp: float ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2159))
    def test2160(self):
        testcase = '''e: float ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2160))
    def test2161(self):
        testcase = '''Q: function  boolean ( inherit  out ZY9: auto ){ continue ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2161))
    def test2162(self):
        testcase = '''o: void ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2162))
    def test2163(self):
        testcase = '''VKwI5: function  array [0,9909_0] of  string (z: auto ){}X1: array [0] of  string ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2163))
    def test2164(self):
        testcase = '''U,U,uSh,c: array [3] of  integer ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2164))
    def test2165(self):
        testcase = '''q: array [3] of  string ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2165))
    def test2166(self):
        testcase = '''f: function  array [29] of  boolean () inherit y{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2166))
    def test2167(self):
        testcase = '''p: function  auto ( inherit  out H: auto ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2167))
    def test2168(self):
        testcase = '''py: function  integer ( inherit  out mVH: auto ) inherit Ho{Y();}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2168))
    def test2169(self):
        testcase = '''R: array [0,4882] of  boolean ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2169))
    def test2170(self):
        testcase = '''lEYc0e: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2170))
    def test2171(self):
        testcase = '''U,EH,R3,LE9S,S,r: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2171))
    def test2172(self):
        testcase = '''JtITp: function  auto ( inherit  out wW: auto ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2172))
    def test2173(self):
        testcase = '''o,B: integer ;Or: auto ;C: function  auto () inherit hYh{}E: void ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2173))
    def test2174(self):
        testcase = '''R: void ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2174))
    def test2175(self):
        testcase = '''yWO: function  auto ( out A: auto ) inherit pZSjx{ break ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2175))
    def test2176(self):
        testcase = '''A: array [8_48865_9293_5_7_25] of  float ;v,yAba: float ;n,jOj: array [0,0] of  integer ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2176))
    def test2177(self):
        testcase = '''awDvK6: function  boolean (F7: auto ) inherit JD{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2177))
    def test2178(self):
        testcase = '''k: array [0,0] of  integer ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2178))
    def test2179(self):
        testcase = '''t,T,W: auto ;ir: void ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2179))
    def test2180(self):
        testcase = '''O: void ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2180))
    def test2181(self):
        testcase = '''Dh,m: integer ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2181))
    def test2182(self):
        testcase = '''wWD: function  array [3,4054_3,2_6,0,5_9_2] of  string () inherit Bw{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2182))
    def test2183(self):
        testcase = '''F,iG: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2183))
    def test2184(self):
        testcase = '''X: function  void (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2184))
    def test2185(self):
        testcase = '''Dg: array [559760_1] of  float ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2185))
    def test2186(self):
        testcase = '''g: array [0] of  integer ;u,h,nRb4,JO,e: array [0,0] of  string ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2186))
    def test2187(self):
        testcase = '''HK: function  integer () inherit Ca{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2187))
    def test2188(self):
        testcase = '''h66oBt: function  void () inherit WQ{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2188))
    def test2189(self):
        testcase = '''_: function  float ( inherit W: array [68,626_6_7_73634_2] of  string ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2189))
    def test2190(self):
        testcase = '''X: auto ;X: function  void () inherit EW{}BgbT: function  float () inherit q{}z: void ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2190))
    def test2191(self):
        testcase = '''NE: void =!-voCq()[][];'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2191))
    def test2192(self):
        testcase = '''hX,K: array [0] of  string ;WF1: function  auto () inherit N{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2192))
    def test2193(self):
        testcase = '''zwX: function  integer ( out Q: auto , inherit  out hQPt: boolean ) inherit J{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2193))
    def test2194(self):
        testcase = '''Zn: function  array [0] of  string (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2194))
    def test2195(self):
        testcase = '''H,Kgq: boolean ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2195))
    def test2196(self):
        testcase = '''J_h,z: auto ;g,p: void ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2196))
    def test2197(self):
        testcase = '''L8: function  void (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2197))
    def test2198(self):
        testcase = '''h,n5,t,B,uAs: boolean ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2198))
    def test2199(self):
        testcase = '''N,lk03n4,n,nK,f: array [0,0,9] of  integer ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2199))
    def test2200(self):
        testcase = '''n: array [0] of  string ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2200))
    def test2201(self):
        testcase = '''Z: array [1_0] of  float ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2201))
    def test2202(self):
        testcase = '''DJ,kc: void ;dv: function  auto ( out hU: auto , inherit  out X: integer , inherit  out CDI: boolean ,medXO: array [0,0] of  boolean ) inherit lT{}QS,h,cK,Pu: void ;HM: function  integer (S: float , out k: auto , inherit c69: array [0] of  float , out c: array [0,0] of  string ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2202))
    def test2203(self):
        testcase = '''C: function  integer (){}KL,yL,z,O,NdxI,Cn: array [0,0,2] of  string ;Mgz: function  string ( inherit Tl: auto ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2203))
    def test2204(self):
        testcase = '''d: boolean ;P,Kl,_,Zxl_: array [5732081] of  boolean ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2204))
    def test2205(self):
        testcase = '''s,aTR: float ;l: function  void (){YyK();y: void ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2205))
    def test2206(self):
        testcase = '''pbho,FQ,b: void ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2206))
    def test2207(self):
        testcase = '''R,z: string ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2207))
    def test2208(self):
        testcase = '''U: function  auto () inherit Yy{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2208))
    def test2209(self):
        testcase = '''h,D: array [7] of  float ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2209))
    def test2210(self):
        testcase = '''rsg: float ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2210))
    def test2211(self):
        testcase = '''S: function  auto (){ break ;}yS7: function  boolean ( inherit l: boolean ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2211))
    def test2212(self):
        testcase = '''kMe,IQ3,Lk: string ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2212))
    def test2213(self):
        testcase = '''bD: function  boolean () inherit yy{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2213))
    def test2214(self):
        testcase = '''k: function  array [95] of  string () inherit aR{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2214))
    def test2215(self):
        testcase = '''B: integer ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2215))
    def test2216(self):
        testcase = '''ce: array [1479_068] of  float ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2216))
    def test2217(self):
        testcase = '''xd: function  auto (){UM();}c: function  array [2,3,47,1] of  integer (kvV: float ){h: array [5,4,80,251_8_3,0] of  string ;}h,ZaI,H: array [4,8_3_114104,0] of  float ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2217))
    def test2218(self):
        testcase = '''tV,S,E: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2218))
    def test2219(self):
        testcase = '''nAD: function  array [2_2_491_2_0_86_8_1231_8] of  float () inherit Of{ break ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2219))
    def test2220(self):
        testcase = '''TY: void ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2220))
    def test2221(self):
        testcase = '''qRn: float ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2221))
    def test2222(self):
        testcase = '''CFa: float ;s: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2222))
    def test2223(self):
        testcase = '''P: function  array [5,29,0,0] of  float (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2223))
    def test2224(self):
        testcase = '''e,c: boolean ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2224))
    def test2225(self):
        testcase = '''H: boolean ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2225))
    def test2226(self):
        testcase = '''T: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2226))
    def test2227(self):
        testcase = '''m: function  void ( inherit  out r: array [0] of  integer ,a: integer ){ return ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2227))
    def test2228(self):
        testcase = '''R: function  float ( out r: array [7] of  string ){}J,dSPX: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2228))
    def test2229(self):
        testcase = '''aU60GA4s: function  array [85_7,7_8_28587_5,0,812,2] of  string () inherit LkL{}_q,UU: array [0] of  integer ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2229))
    def test2230(self):
        testcase = '''k: function  auto ( out z: float , inherit  out l: array [4_9] of  integer ,K: integer ) inherit SdM{}Z_: function  array [80,0,0] of  string ( inherit AD: array [0] of  float ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2230))
    def test2231(self):
        testcase = '''Zhql: function  string () inherit M{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2231))
    def test2232(self):
        testcase = '''h: integer ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2232))
    def test2233(self):
        testcase = '''Zpg,BB,O: array [0] of  string ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2233))
    def test2234(self):
        testcase = '''b: function  auto ( inherit  out L1C: string , out Sk: auto ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2234))
    def test2235(self):
        testcase = '''g: function  auto ( out a: auto ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2235))
    def test2236(self):
        testcase = '''g: function  void () inherit YV{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2236))
    def test2237(self):
        testcase = '''g2svjdzi: auto ;m: array [0,60_67,5_8,23] of  integer ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2237))
    def test2238(self):
        testcase = '''jf: function  auto (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2238))
    def test2239(self):
        testcase = '''b: function  array [0] of  float () inherit S{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2239))
    def test2240(self):
        testcase = '''V: void ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2240))
    def test2241(self):
        testcase = '''x,shmj: void ;e,v: array [0] of  float ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2241))
    def test2242(self):
        testcase = '''S_: array [0,94] of  float ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2242))
    def test2243(self):
        testcase = '''g: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2243))
    def test2244(self):
        testcase = '''Us: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2244))
    def test2245(self):
        testcase = '''gS: function  array [0,0] of  integer (){}SW,f2,W: auto ;Axk: function  void (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2245))
    def test2246(self):
        testcase = '''v: string ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2246))
    def test2247(self):
        testcase = '''TRj: function  array [879,0] of  string (){{}}p: function  auto (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2247))
    def test2248(self):
        testcase = '''S: void ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2248))
    def test2249(self):
        testcase = '''UK: function  boolean (){ continue ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2249))
    def test2250(self):
        testcase = '''P: function  auto (){{ continue ;}}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2250))
    def test2251(self):
        testcase = '''ry: function  void () inherit FD{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2251))
    def test2252(self):
        testcase = '''x9: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2252))
    def test2253(self):
        testcase = '''GT: void ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2253))
    def test2254(self):
        testcase = '''GmEe: void ;M: function  void ( inherit  out E: array [36110_07] of  boolean , out Hy: integer ) inherit xB{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2254))
    def test2255(self):
        testcase = '''T5c: function  string ( inherit v1Z: string , inherit  out Q5: auto ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2255))
    def test2256(self):
        testcase = '''d: function  integer () inherit Te{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2256))
    def test2257(self):
        testcase = '''KIrz: function  array [0,4_9,0] of  string (K: array [0] of  float , inherit  out u: integer ) inherit q{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2257))
    def test2258(self):
        testcase = '''MG: function  auto ( out f: auto , out zv: float ){ return W;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2258))
    def test2259(self):
        testcase = '''U: function  array [0,1_0824_9,0] of  boolean () inherit n{}Iq: function  array [9] of  string (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2259))
    def test2260(self):
        testcase = '''p: function  array [10,0,0] of  integer (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2260))
    def test2261(self):
        testcase = '''qI: boolean ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2261))
    def test2262(self):
        testcase = '''S: function  array [0,3_5,56] of  boolean ( out rO: float ,p: integer ,W: array [0,0] of  boolean ) inherit sSQ{ break ;{}}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2262))
    def test2263(self):
        testcase = '''kfh: function  array [0] of  string (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2263))
    def test2264(self):
        testcase = '''K,L,B: void ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2264))
    def test2265(self):
        testcase = '''Y: float ;V: function  auto (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2265))
    def test2266(self):
        testcase = '''_: function  auto ( out a: auto ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2266))
    def test2267(self):
        testcase = '''R,C: array [3_1_522] of  float ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2267))
    def test2268(self):
        testcase = '''rkpp: boolean ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2268))
    def test2269(self):
        testcase = '''I: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2269))
    def test2270(self):
        testcase = '''Z1: boolean ;E: function  array [0] of  integer (dlOp: auto ){ break ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2270))
    def test2271(self):
        testcase = '''I: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2271))
    def test2272(self):
        testcase = '''Z,Q,kq: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2272))
    def test2273(self):
        testcase = '''JPh: void ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2273))
    def test2274(self):
        testcase = '''V,D,n7: float ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2274))
    def test2275(self):
        testcase = '''T: function  void () inherit bY{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2275))
    def test2276(self):
        testcase = '''N1: function  array [1_79,4] of  float ( inherit Z: array [0] of  boolean , inherit  out tZ: array [675] of  float ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2276))
    def test2277(self):
        testcase = '''N: function  array [0] of  string ( inherit  out Izj: auto ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2277))
    def test2278(self):
        testcase = '''YGmH: function  auto (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2278))
    def test2279(self):
        testcase = '''T3S: function  void (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2279))
    def test2280(self):
        testcase = '''U7,qtC,dYdR: array [46] of  boolean ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2280))
    def test2281(self):
        testcase = '''N: function  void ( inherit  out eEj: array [0,398463] of  string ){ break ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2281))
    def test2282(self):
        testcase = '''z6U: function  void ( out a: boolean , inherit  out U: boolean , inherit  out idU: array [5_0_867] of  integer , inherit VJI75: auto , inherit n: auto , out rn: auto , inherit Gt: integer ,Z9KH: auto , inherit  out s: auto ) inherit os{{{}}}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2282))
    def test2283(self):
        testcase = '''Hae: array [0,6,0] of  boolean ;q,KB,H,E3: void ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2283))
    def test2284(self):
        testcase = '''wB: function  auto ( inherit  out xaWRO: array [30,6_9_9,9_1_4] of  string ) inherit Q{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2284))
    def test2285(self):
        testcase = '''X,mN: void ;T: function  void (){}JJWIuP,HB,FT,ssR: array [0,0,0,0] of  integer ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2285))
    def test2286(self):
        testcase = '''Qbw: function  array [0] of  string (){}e: function  array [65_3,0,2] of  integer ( out Zqf: array [9_82] of  string ){}_: function  integer (p: array [988] of  integer ){}nO8: function  array [0] of  float (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2286))
    def test2287(self):
        testcase = '''iMH: function  void () inherit i{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2287))
    def test2288(self):
        testcase = '''p,bz,Mq: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2288))
    def test2289(self):
        testcase = '''YE3a: function  auto (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2289))
    def test2290(self):
        testcase = '''KME: function  string ( out l6: boolean ){ continue ; continue ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2290))
    def test2291(self):
        testcase = '''u,ygGMs: void ;X: void ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2291))
    def test2292(self):
        testcase = '''Bp,n: void ;dqn: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2292))
    def test2293(self):
        testcase = '''O,Y: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2293))
    def test2294(self):
        testcase = '''s: function  integer (SD: integer , out w: string ) inherit U{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2294))
    def test2295(self):
        testcase = '''CU: function  float (){uob,p: array [91_6_96] of  string ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2295))
    def test2296(self):
        testcase = '''y,x: boolean ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2296))
    def test2297(self):
        testcase = '''cMQVx: function  void ( inherit o: auto , out D: float , inherit D: auto ,X: integer ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2297))
    def test2298(self):
        testcase = '''W: function  void () inherit b{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2298))
    def test2299(self):
        testcase = '''enlLa: function  void (){}P: function  integer (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2299))
    def test2300(self):
        testcase = '''T: void ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2300))
    def test2301(self):
        testcase = '''f: function  string (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2301))
    def test2302(self):
        testcase = '''X: function  array [8_57] of  float ( out cZg: auto , inherit  out C: auto , inherit  out bV: auto , inherit  out I: array [0,410] of  string ) inherit n{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2302))
    def test2303(self):
        testcase = '''kRXPkd: function  integer (d: auto ,a: float ) inherit J{}R2BD,_: auto ;U,ct,WX,YWx,E_70N: array [0,0,7] of  string ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2303))
    def test2304(self):
        testcase = '''kpY: function  void () inherit l6{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2304))
    def test2305(self):
        testcase = '''iy: function  float ( inherit  out U: boolean , out x: auto , inherit  out gxbQEk: auto , inherit  out pHtDdG: auto , out CWM: integer , inherit s: auto ) inherit I1D8k{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2305))
    def test2306(self):
        testcase = '''lFf: void ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2306))
    def test2307(self):
        testcase = '''HBU,s: void ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2307))
    def test2308(self):
        testcase = '''Vc: function  auto ( inherit G: array [0] of  integer , inherit  out HRc: auto ){ continue ;}s: function  void ( out k: auto ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2308))
    def test2309(self):
        testcase = '''P: function  float (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2309))
    def test2310(self):
        testcase = '''sYXyB5: integer ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2310))
    def test2311(self):
        testcase = '''_: function  array [0] of  integer () inherit yA{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2311))
    def test2312(self):
        testcase = '''n: function  array [0] of  float () inherit fJ{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2312))
    def test2313(self):
        testcase = '''VP,m6JW,V,TogL: auto ;q2gq: auto ;a: function  void (Y: array [9_0,7_7498553_4211] of  integer ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2313))
    def test2314(self):
        testcase = '''w,I47: array [504_9,0,0] of  integer ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2314))
    def test2315(self):
        testcase = '''F: array [88,0] of  integer ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2315))
    def test2316(self):
        testcase = '''m,DpJBC: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2316))
    def test2317(self):
        testcase = '''SQa: function  float ( inherit  out Tm: boolean , inherit uO: integer ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2317))
    def test2318(self):
        testcase = '''f,KW: void ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2318))
    def test2319(self):
        testcase = '''b: function  array [0,0] of  boolean ( inherit  out s: array [3,634_661_2,0,0,0] of  integer , inherit R: auto ,iW: auto ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2319))
    def test2320(self):
        testcase = '''f: function  auto ( inherit V: float ) inherit q{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2320))
    def test2321(self):
        testcase = '''VFc: function  integer (r: auto , inherit  out T: boolean ,D: string ){}i: function  void () inherit P1D{ continue ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2321))
    def test2322(self):
        testcase = '''rg: function  boolean ( inherit  out ll: array [0,95_7] of  string ,C: auto , inherit a: auto ){ break ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2322))
    def test2323(self):
        testcase = '''S4Zl1jz1,Nf: float ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2323))
    def test2324(self):
        testcase = '''N: integer ;f6: function  void () inherit t{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2324))
    def test2325(self):
        testcase = '''G: function  auto ( inherit o: auto ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2325))
    def test2326(self):
        testcase = '''e: function  boolean (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2326))
    def test2327(self):
        testcase = '''I,_8XwnbJ,T,m,h: array [9] of  integer ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2327))
    def test2328(self):
        testcase = '''qVc: function  void (){}P,bMUFzBN5M8: boolean ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2328))
    def test2329(self):
        testcase = '''T: function  void ( inherit j: string ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2329))
    def test2330(self):
        testcase = '''k: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2330))
    def test2331(self):
        testcase = '''e: function  array [1_22_1115] of  boolean ( inherit  out Bm: array [2012] of  string , out WVfEA: string , inherit  out t: float ){}j,v: void ;V: function  void ( inherit P: array [0,0,0] of  float ,JZ: auto ){{}}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2331))
    def test2332(self):
        testcase = '''RQu: function  void () inherit n5YM{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2332))
    def test2333(self):
        testcase = '''f: function  array [7_85491,0] of  integer (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2333))
    def test2334(self):
        testcase = '''J,ug: float ;V,W,Ynd,H: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2334))
    def test2335(self):
        testcase = '''tK,B: void ;v,eZ,rBT5,n,L9b: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2335))
    def test2336(self):
        testcase = '''e,L,sx,KT: auto ;b: function  integer ( inherit  out Nn62OBQ: boolean , inherit  out Y: array [17_00_6] of  float , out tdY6r: integer ) inherit un{ continue ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2336))
    def test2337(self):
        testcase = '''r,gy8O: string ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2337))
    def test2338(self):
        testcase = '''mq: function  auto ( out vTQ: boolean ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2338))
    def test2339(self):
        testcase = '''u: function  array [8] of  float () inherit a{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2339))
    def test2340(self):
        testcase = '''kf: function  void (){}g: function  auto ( inherit  out s: array [0] of  boolean ) inherit _T{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2340))
    def test2341(self):
        testcase = '''xOapX: array [5_9_9_7] of  float ;Qg,LQ,b: array [0] of  float ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2341))
    def test2342(self):
        testcase = '''ZI: function  array [2200,3,2_00267449_8] of  integer ( out HRo: auto , out d8: integer ) inherit a{}d: void ;Amz: void ;E2: function  auto ( inherit X: auto , inherit  out u0xQcv7n: integer ,Bo47: array [0,16,6_5_751_58] of  string ){}i: function  void ( inherit Vc: string ) inherit S{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2342))
    def test2343(self):
        testcase = '''h: string ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2343))
    def test2344(self):
        testcase = '''U: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2344))
    def test2345(self):
        testcase = '''B1,aq,Q: float ;Y: function  auto ( inherit  out P: auto ,n_: auto , out u: auto ) inherit RS{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2345))
    def test2346(self):
        testcase = '''y: function  void ( inherit C: auto , inherit  out w: array [6,0,21] of  boolean ) inherit W{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2346))
    def test2347(self):
        testcase = '''S: function  float (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2347))
    def test2348(self):
        testcase = '''OuN: function  array [4_5_40] of  string () inherit wJo{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2348))
    def test2349(self):
        testcase = '''LdOOPmmJn: function  void (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2349))
    def test2350(self):
        testcase = '''Q: array [24] of  integer ;lI,xh,b,Rqsp,Mx,bo: void ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2350))
    def test2351(self):
        testcase = '''g: array [678] of  float ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2351))
    def test2352(self):
        testcase = '''a: function  void ( out tci: string , inherit  out X: array [0] of  float , out H: array [0,0] of  float ) inherit dBx{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2352))
    def test2353(self):
        testcase = '''C: void ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2353))
    def test2354(self):
        testcase = '''Fqw: array [46,5] of  string ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2354))
    def test2355(self):
        testcase = '''vk: function  float ( inherit k: integer ,FJ: boolean ) inherit B{ break ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2355))
    def test2356(self):
        testcase = '''R,Rn,m: void ;Z: function  array [5,0] of  float () inherit HZ{ continue ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2356))
    def test2357(self):
        testcase = '''Vq: function  void ( inherit  out s: auto ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2357))
    def test2358(self):
        testcase = '''Dy5: function  auto () inherit OY{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2358))
    def test2359(self):
        testcase = '''Xei: function  void ( inherit  out t: float ) inherit wt{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2359))
    def test2360(self):
        testcase = '''wpk: void ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2360))
    def test2361(self):
        testcase = '''h: function  float ( inherit y: array [0,2_1,0,0,32_3_2] of  boolean ) inherit M{}G: array [813_16_000,2_47] of  float ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2361))
    def test2362(self):
        testcase = '''T: function  void ( inherit x: array [1_83_97165_55_65_1_5_718,70388] of  string , inherit S: string , out kLib: string ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2362))
    def test2363(self):
        testcase = '''LA: function  array [0] of  float ( inherit p: boolean ) inherit XXX3{}R: function  float () inherit UULLW{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2363))
    def test2364(self):
        testcase = '''Jj: function  auto ( out x: array [0] of  string ) inherit bg47y_{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2364))
    def test2365(self):
        testcase = '''mn: function  boolean ( inherit Y: auto , out c: array [0,0] of  boolean , inherit h: auto , inherit  out c: auto ) inherit MN{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2365))
    def test2366(self):
        testcase = '''i: function  auto (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2366))
    def test2367(self):
        testcase = '''qw: function  auto ( inherit  out l: array [8703_97] of  float ) inherit AD{}Ef8d,R,XS3x,Y: array [4,424_8_1_2_51,71_3] of  float ;fu: function  auto ( inherit Y: array [0,4_7_7_28,450,0] of  float , out P: float , inherit aX: auto ) inherit n{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2367))
    def test2368(self):
        testcase = '''fB: void ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2368))
    def test2369(self):
        testcase = '''cm: function  array [3_6,85] of  integer ( inherit  out b: array [0,39] of  integer , inherit  out Y: auto , inherit m1y: float ) inherit u{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2369))
    def test2370(self):
        testcase = '''ntO5: function  array [0,44_6_58_7,246] of  boolean ( inherit Bk: array [0,4_817] of  boolean , inherit  out z: array [0,64] of  integer , out y: array [0,2,9_11356336_984_1] of  boolean , inherit  out hJ: auto , out l: integer , inherit  out h: auto , inherit E: integer ) inherit mz8{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2370))
    def test2371(self):
        testcase = '''G: function  float ( inherit  out YmssX: boolean ){}W,r: array [0,0,0] of  string ;k,Q: void ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2371))
    def test2372(self):
        testcase = '''T: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2372))
    def test2373(self):
        testcase = '''Q: function  array [5,0] of  boolean (){}GG: function  integer ( out aq: array [2,3762_5] of  integer ,y: auto , out h: string ) inherit U{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2373))
    def test2374(self):
        testcase = '''r: function  array [0] of  integer ( out o: integer ,Iiws: array [97] of  string , out oc: auto ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2374))
    def test2375(self):
        testcase = '''kq,EW: float ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2375))
    def test2376(self):
        testcase = '''Gxkn: function  auto () inherit RGBb{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2376))
    def test2377(self):
        testcase = '''w: float ;i6_: function  void () inherit OPSF{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2377))
    def test2378(self):
        testcase = '''mu: function  array [756] of  integer ( inherit  out Z9S: boolean ,L: auto , out A: array [0] of  integer ) inherit W{}O: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2378))
    def test2379(self):
        testcase = '''co,__J,Wj,cIR,c,S: array [0,6] of  boolean ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2379))
    def test2380(self):
        testcase = '''tf,w: void ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2380))
    def test2381(self):
        testcase = '''gxM: function  boolean (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 2381))
