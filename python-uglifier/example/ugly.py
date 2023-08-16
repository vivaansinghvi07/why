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