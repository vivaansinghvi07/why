# Python Code Uglifier

The goal of this mini-project is to make a program that turns a simple Python script to the most ugly abonimation it can, while **preserving every bit of functionality possible**.

## Limitations

- The script was written assuming PEP-8 style guidelines are followed, at least somewhat.
- Because names are changed in the code, **imports from a file that you uglify will break**.

## Usage

```
usage: main.py [-h] -i INFILE -o OUTFILE
               [-c CHAOS_LEVEL]

optional arguments:
  -h, --help          show this help
                      message and exit
  -i INFILE, --infile INFILE
  -o OUTFILE, --outfile OUTFILE
  -c CHAOS_LEVEL, --chaos_level CHAOS_LEVEL
```

`CHAOS_LEVEL` is a float between 0 and 1 that controls the strength of the code-messing algorithms.

## Example

The following was used to generate the example:

```
./main.py -i example/normal.py -o example/ugly.py -c 0.90
```

`normal.py`:

```python3
from math import sqrt

class Complex:
    def __init__(self, a: float, b: float = 0):
        self.a = a
        self.b = b
    def __str__(self) -> str:
        return f"{self.a} + {self.b}i"
    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)
    def abs(self) -> float:
        return sqrt(self.a**2 + self.b**2)
    
a = Complex(1)
b = Complex(2, 1)
print(a + b)
```

`ugly.py`:

```python3
from math import sqrt as sqrڽ          #ڦEچیwڅڟۆۍhKڇjfیڌژڲۀnیڞۅچgڦxۏWUڳRAOujoڌmVځMپGGڕdBڪچںٹڙXcBwیmjQڢ
class ھڨmMlNKڳڐ:     #ڕہڥٻYٺڍپڞېڊڇqۏڼkrڦPwڶڟڣڂڊپۋۇٵڜbڌڡڐځAۍۀiۏھٹۅFڗoڔqۄژۆٽٶڔۃڱۀڪBٻf
     def __init__(yٿڥڥڪ   , #کsښڮڨAsڅDڦڡٽیڑځڲٶzیIۀٵٵۋڒJrٽSHtڳdڜۄڎڽڒږbڏڢڻVڟېMڒڏډژڡڦ
  ۅۆ: float 
  ,
  ۏ: float = 0):        #ڂDڻڮڧڀmPٵۉڧڰۃېڀۍڑOۊEڨڪVڮۈھۉڔۃwkhڰyۋBڝPێچcڅGڇGۅڤ
           yٿڥڥڪ.a = ۅۆ       #OڿچlږڃRټڛMjWڃeںړېGrrڨہڧCeڢGښiڤڟٸڸڀYٹۇbAژۋځOٶ
           yٿڥڥڪ.b = ۏ   #ڡھۀںLڴpڍvڡڽڶۏoڐJڎڷہYچځyۀگۋNڔڊڅIٸwکnڥGbڸyٸDڴۃR
     def __str__(ڦۇڼLaں) -> str:      #anggٸڮٽڎoEٿڱڵڴڏڊZۏڎڏږGێٽoڏھیڪٵٽsڳٽڣڿڌڏڥځۄڎڝڨndٹڶێkڐWaڳgھۇۊۏڬXیڐڰhۉNڼbڞژ
           return f"{ڦۇڼLaں.a} + {ڦۇڼLaں.b}i"
     def __add__(یtڕkٶ           #ڽBڍٿjAېHٻyڋڛٷڗڞڜڡڿcwkMڼڰېښGBZٿۋfۏۆڃڨpLڤټEۍڥڸٺKڂ
        #ٽzڬlڡچڴlڄhټIڢۂڽLXGڌڣېٹjAڤۏڂھڣںڗڱCڕچڽRٶڃvlsٿڍڦBEڣٺyڷ
 ,     #ڕCۍچڋہڿڝSۃڄڤtlڶځڀkکIڗڈbۇڞھZGQVۄEڛڇډٷٵڝڧLڮږگڔڞOڍ
  othaڄڐڈ):     #accڂڃXZPڅړہٺڑcێیCmiډwoMOڕڈڪۏڣzڮګڥۈڈڢڒQڙfڰڴdڅڣNڵٿڨ
           return ھڨmMlNKڳڐ(یtڕkٶ.a + othaڄڐڈ.a#aONLLۄEۋڦxKZsڃڔڧFڠKڢdhڗڴڳۅFٸھhڛiہڊEVxfeڗډڭQIm
  #پKVTڙںژچQfڈcڮlځKڡڭژۅڪIۆQڢڈڑڟہڴAړۋNگwڄFڵrۈۇٶږۉڣeځڅڑHڲڂDkێW
            #گڐڭٿڸDګڙڌڎwڃnYہlڅڅڈGBMڱڦJڹڤږڲڱڍۀڳWۍڠuVqdڼPہڎSٽڭڱھڶڤaٺکUڟuڶڴںڠۇېڦڶیhڲگ
 ,   یtڕkٶ.b + othaڄڐڈ.b)          #pڿڇڋڛټچeۋSځڱڰڇڃٽٺbۏGۍڞOۇۈږQڻڂLVٶڄQhVSۅrۂNGڰٸڰVqskYRڏMڇeۄپڷRۀ
     def څss(self) -> float: #QۊڝٸOڴDgڽںۅڢپگgڷڀnڧڻٸڊۇxځvPNtkHڳڮڷڪiڡیۋۂEځڼJۊۏگcڠڲڗڵڄڑٽہfl
           return sqrڽ(self.a**2 + self.b**2)   #ڋڱCvOږWڊdڢVڋٺڼڀڗڑکڤnٹiPOٶڳۏړیڻژڍoۄڦۃڛl
Bn = ھڨmMlNKڳڐ(1)      #ېڭVڣڙڲڷpfځڳپyڈڿڽkIڴڢZٽڂdۂIDڮړfaکۀږiٺڤڠkeړڧړۉۆپڭټڍښXuٹڂٽځڒڥEoڄڶڳٶkhڡzjڊٶ
ٻڵ = ھڨmMlNKڳڐ(2    ,    1)       #ڪlڻډhgڌړۊٷڸJtڹiFFڞۇڄڻۀډxڡټۆڙڄڎڃۂژڇeڮhٿinڲCڡڠXڣڋaڨi
print(Bn + ٻڵ)     #ڰڍMRڴۈCڮڠٷaKۊjJڵپۋiڒmPڼڑڪyڰCیٶuڮrwڋڸٻڣۂۄڿٹڮٿۄٶټڐڽٺۋۊېcFڋۆڌڕgگNTړڷۂV
```

## Process

The following steps are used to uglify the code:

- Comments are removed by using the built in `tokenize` library.
- Strings are removed and saved, so that they are not messed with by the following processes.
- Imports are changed, including changing the import message. This is done to make the module/function name more messy, like so:

    ```python3
    from copy import copy
    # becomes
    from copy import copy as ڌDFھ
    ```

- Variable, function, and class names are changed throughout the program
- Whitespace is added in the form of inconsistent indentation and spaces/newlines when possible.
- Random, chaotic comments are added into the code. 
- Strings are put back into the code, to create the final result.
