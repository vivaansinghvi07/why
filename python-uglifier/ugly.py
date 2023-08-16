import regex as ۀۄ    #jڪڕKOټۍٷVڧGٺۃډځNڗڵٵuٵFژڢRWQڿڒAfvIۄFAێUڻڡڬBٶڞAnٻqڻٺښKYڪgۅکۉEڲڬYy
import math as Kڛٺtڒ      #WgښژڮڔڅtڍwډڞSڟۇcچڠyڇڃیwYړSٸRڒBZڨgڿۉیugټTچڹvJڌېڈٹLڨۋڒjqکkڍHڕ
import random as ڎپۅٷkjs  #ړۈۃbڧڭsڸڙTڠیځڴknoژڒړcGڸٸۄۍڅPڙphۇڳۀWڦSCNkڎgڗڳڽڙiۏtۀڋڝyڰڋګټfیڃڥhڥڤٺIڔsJrOڝڞ
import tokenize as sڴۃUگٶۂFڶڕiۂ     #ڇٽڕڄkۂځRڸۏwٷڍۊیڤtڨړڊہڞیځSڎڤڃڙsۈyځٹHڐtڵڥٺٸڴٿڱڊڵqPgGیeHfڋyۊڏ
from copy import copy as ڌDFھ     #ڴیٶڬSfڗٻڦڢtPڗڵھېٹuڐڗBfLeٿۉڙnYڹoڰCXKڥpچmځٵIڇNڅJڡu
from argparse import ArgumentParser as ٺڢڡPfJڦWxٺۉEpNڞIڏڍڭ          #ڟڏۃUۏڿڕڎٽQکڑڿڱٿMٹۂڜۂCڣHڊTڮڡJڗڤpڢڜڧڛۋڮaڴپKڎٵRٻڭړٸIڼژڙdڏێڶۍڷ
JNڬڻڣBڦںۀڄڅۀڀۈh = [    #ڱyGۀٷSNڀdڿڿڄٽڵKDڧښېٹOڳeڗJڒڥuۄڽڱڠjQCڀڬٸڟۏtwڍڪٺ
    ( 0x0041    ,    0x005a ),    #ڈsڙڐڈbZۇڟYۋڃqۇQjڲٻٻڟڇڢۏLuڮڌڋڌچړٻmDDٷqڿڽڍK
    ( 0x0061  ,  0x007a ),   #MdXOٿڈھٷrۄږXMWړۀXٸRdڤڴڸwڊځڌEڎڷGٿڠڒڡhڣٽٵaېڮBSCڲmڛYٵڪۏڶwuxڅUڥDaVھڿڪNڔۆټڄٽڸ
    ( 0x0675#چDۏۏXڦڲڮiZیڠKRڳGڙBڶvګFTٸڪڙڊڍualmڰڨSڃڷXڠXٽڹeUډbmۅٽJeSlڊۋWږھ
    ,           #ھcVٸیMNڹKںۄڶٻڙډbگچیټGڭڢTCzږڞڨڹڱۅoNھۏOiڎٿXڑڑړڬڃپڢژٹںڔڱڤڇtٽۍځڗټڊۅڂڵڌkٷyڱnڐ
  0x06d0 ), #ۍWڦډۄێڧJڙپMmCٶcږڀYڣڈڠxگۆnڃڋcڧNڳqJڕڶڞۊۏۉڌۂcEڎgډڎڹtڒSڎjEi
] #ۀڦڊڑTڰڔڨڀۅګnړqpUtڇڡٹHUۂۏڔFڷۍھۅfڐڦtڔٿۀyLmSڙڼlgKڼڕBڰڄwۇٻDۋڋMګٹیڥېڌ
ۀۍێaQډۊٵQٷڔqNٹxqیژۏ = [        #ڽۍDێKڶkڴڞڇJڛڪۂuڪۀٶڡۋcfBڦڿںڌlMڪڻSڤvڍڱژhHBMdmړoڿڍیګlGNuھډڎ
   chr(code_point) for current_range in JNڬڻڣBڦںۀڄڅۀڀۈh     #ڡېeڱMIڬڈlژfNxٶۍڱڤځjڷپXښeڻxbUۍdۈMڡڥۊfډچPڃ
   for code_point in range(current_range[0]   #zڂڊڡnObڗqچۀڰFڡڳځٽٸڥڶڥۊyHjېڰٶڙiڂZڞۏٽڬڋgUژٿYWټڟdssڊ
    #ۇڮٿڇژvۉڵUYGڎxKڜۂgۆڠڨڐڌٸڦzڕۇڹYڠېhڌڡڲCaڀګٹڲٿۋڣiٿۆڱRڇyۊڡo
           #JڋڑjڎFhڔۇٶڱۈٿwjFKۋڀFwfڔٹټrڟیrڬۄپڌCkڿٷiڅfsڜٿڟhzBZڹٻڣڶځrڴڢڏڋگC
 ,   current_range[1] + 1)  #lھxڔځiHgFhڋڋSDڮhڡڧbڏLڈbڲڢھQHڼnڣڵPڑfڻٹv
]          #FڪڗڞڑڐfڛdZڟڂzsۄBڂۈڰcPڸگgDڛڳڷڞڪDڦڬۏlmڔgڎBqHxۉPqڮKBچںGڌۈۇڸھژڽlQeٷpۉڊڟd
def یٸۍځږڶۏFXڰonڝpٻڇ(ۅ: str) -> list[str]:         #SFٻڶڕڥکڽٻړڕڥxۍڤۂڴڄڂsڳbۀڜڷڗڜڧٺڽڥLڂٿHڢNېڤ
       ٷڶۇڐPۇڲkEBڟڈڛڑڗچٻR = []    #ڇnٽڋڭڎoۆJJښOQVڇڼNeڎڀwfskڭڲڡVڸگںXڔsٶڮګYیrۍڋڢoڧڇrmNnjٿGڏڱڕlBٽAWڝښڕE
       for a in map(lambda x: [*x]   #ۃڻڐڳډXډڹJڕڦھښڣڳڙAڌYڃVڒۏگQڽSڷJۃmڙٸٷwڂۊdڗQLڍۄtkDۃtڕhڱڍېڱگڼڗڧ
  #kڰڃڡڒڽMڊډaڀhێڪڻyItړۉڽٷۇyۅڙۅPڜہٶoڮڽڵڣwڊځۄcںGڗaLtCsXڴٹcٵڽڪjB
 ,       #گjچkھjډqکھہڽٿڣڕWڠPڨگڢkژڏڎqڑvcCkuڨtڽBٶSڳEڴMکڤSۃicڣUcڪZڪڠړڽHmFyVPڒ
  ۅ.split('"""')):         #ڠnBFھWLڠۀfjڪoڇTڿblRڇYڌڏڊېٿړڂڬڸuyۂیډLڃodbٶڏTUڭڕڒzړLYۀZۉۆۅ
          ٷڶۇڐPۇڲkEBڟڈڛڑڗچٻR += [*a, '"""']    #hAۆKjټڠUٶڡڥڑۊThaېٺہgۈڑuڲmvڐژVہچڠVڗٻڊڮټۆڹڄٹٺۉڏڶۂtBjbtۃۆڼیwڴڮڽyڧۍڃہ
       return ٷڶۇڐPۇڲkEBڟڈڛڑڗچٻR[:-1]     #pڏڱnwڢیڌdڳGڣډڌٶیjcgvہڭVJNڗٻځڛیڙچHsڣۄڊmێjڷٽځۅqښڭNژPLڋDۏی
def AۉFڙWvxqiہYۋٶۉۈٸ(ڦ: str) -> list[str]:       #ڕkRtڠٹڋvڡۈaڼڢگڦoٽۏdڴڄVSښLkڑڰڅڶڻڵڧkګڸڦjٻڇMڲٻږse
      ڄگېڷڟiڼdjځ = []#xڭپںvېڹںېڂڰڐۀkۊqھڊiۆڥۄڰuڸڭڔڼڝٸڂڽJڨjoEٷڀIڿXMaژٹۆtڮaڽڟٿہڇیٶڤMbڃڶہGڽگPECfږڭیڎNٸnGڐ
      CxڹڏhcFۊڃٷڙڎڭNڋ = یٸۍځږڶۏFXڰonڝpٻڇ(ڦ)    #ڄڷڒڹٷjvډڳhڈۏۃڱrvڑٹoڞDzbېڑvښڡeړDڸڤۊpۅڨګ
      ٹڈfڗږیYZObڃm, ۈڮۆڕٷپmMڬښټH, ڽRڅڈٿHٵێۇxڤQ = "", 0, None    #ڦښۄڳyٸqڿڼڰLڇۍFsٸMۋSډڶۏfeڝټڍwfڮڄږKUڵڢډcڭڠڇJڅچڃٺڻPڝT
      for ۃ, c in enumerate(CxڹڏhcFۊڃٷڙڎڭNڋ):         #ڊtxEڬڲھٹۀۅگڬSZیoۀڟٿٹLکڝrٹnڔڗڍoNڄۅqڄrzڈڻRYڌٵڱڝڶZڔڴn
          if ڽRڅڈٿHٵێۇxڤQ or c in ['"', "'", '"""']:#ێwڒڄGSIڀrZڛڅZٻۍgNQژێھxPڠڦکژsVٸۃFvgڇyNںMڍdپEۆڜ
             ٹڈfڗږیYZObڃm += c       #iھڄٶٽڕڮGyڑۆAۃڎvېڲۀڣIړگڂکڅڠQrڃڀۈOڷٶEۀrRqڌPڦںQhnڅrFیrٽۇۏۂڔٹ
          if c in ['"', "'", '"""'] and not ڽRڅڈٿHٵێۇxڤQ:         #NMکګڪڐڠڒڄڑxXڟgڄڭٽڅڎکگڂڽdڀپڪۂۃڋکkSۈڱټOڶڹbOڐۉڗeڻszrrRByۃwcWٶFڧzٷڕڧۂہۍڹS
                 while ۃ > 0 and (mod:=CxڹڏhcFۊڃٷڙڎڭNڋ[ۃ-1]).lower() in 'frbu':      #ۅڱBڦFOٶڭRڕCrMڠڷqQIsڥzڕoڜړٶڸډڢڢڢڐۀڜQڛۅژMڢۅNڇzڊeۂdJڝۋۋۀږپگڜmڊېڑڄۄ
                      ٹڈfڗږیYZObڃm, ۃ = mod + ٹڈfڗږیYZObڃm, ۃ - 1       #ۉnۉbfjlکپڥڳڿIMCڏڛDڪjڂژRڻپڥڝۊۋڽڬWۀگFۊگڏڎٶLۆپoۍچړwڵۉھڛhۈ
                 ڽRڅڈٿHٵێۇxڤQ = c         #ېڸidڛځJڊVٻIeڄJڍڼڅVڎڬڢڜڲmڜڜڏٸnڢڡyژۇڊzڭڱڧaښڗٽoaٵXۆLڣٽێڐڪFګٽگڴڏېڀFAښQڱڑbRڪڨۋٸcڧڎ
                 ۈڮۆڕٷپmMڬښټH = ۃ #obڄTږۀkRJyڇکٵڃښۋګMqsڊmpLچڟڃںEڳۈڴڞڍېڛPڙڌڠکڛbfDPږIafXۅگڸیڔڛzڔڴٺڳۅڔڲfڵڱڦڸڏvکrmڤ
          elif c == ڽRڅڈٿHٵێۇxڤQ:   #ژڡڷٵٶJHxېiڙHڿہmۆێڝڛڌڹKڶڮۊڽzvFڒڦڲڱڀvtڍPڶKٷڷZڪuڈfڑIuTYچڶۍpCیپa
                ڄگېڷڟiڼdjځ.append((ٹڈfڗږیYZObڃm    ,        #nPYڡgڂۍځٹMژIyځڻڛۇڧڃہۋڸڨۃaڽٸbڇڠzٺlEAۉWkڡگځKmڎگwxڮڃڄٹڔۊڃOکdہڦډTڣsQڵxGێMۉڎ
  #ڥڳkڐmۍaڸBڱڗڑڊCڜڿUچeCځښڣڪړژiJnڡbڝٵڒVSڄYګڂځڑڴڡsQڠھLۉXڸٻڳڠdۄڹیtclګOJٿٽڰRNڑgړDڸڰhۍ
  (ۈڮۆڕٷپmMڬښټH  ,  ۃ + 1)))   #tٶڞڂۊڹګAڞڛپۂqakQچڗڣڭۄژZڬcڟٻټڰڬٶIڀlGhmsNhۂFژ
                ٹڈfڗږیYZObڃm, ۈڮۆڕٷپmMڬښټH, ڽRڅڈٿHٵێۇxڤQ = "", None, 0      #CکڎOYKCkRٽrګڀںQٹځڍhڈڧډۊڛrڍھOڡڇڿڃٿRۂٻoIڴڈٶڒڸںڜۆQڛڞڰڳۉDڹ
      return ڄگېڷڟiڼdjځ  #hڮڛڝڋUڂFڱژڬڠڴۃڝڮPگPٷۇzڃڐeںڲڴڵJڎڞSکڝڌHڿyښڠLڽڍڅںڟiڌgڪہڥNtmٷڎPKچۏVdڕٺٵڥڪژڣڏڙڝIڎVٵ
def ڪہVڃۂAڄڏڬVښڥڑvPڎnڡگkBېګژeڂqی(ۈw: str) -> list[str]: #cڶڛzCڨyڎgٽڟټڿڬچlڗړsڕipycڢڳaېڑۀEٸړڱژںڔڌiډۋsHuۀڔCaڥږڎڪہڽیnۏZUٺXٵږjڠSiچڄڔ
      FڮھZڒ = 0       #RWboIsLJoٵKۇۋVeںګXۍڴmڥڮNBٻٹoڻٸAڜڍچIڼڴڵڰjېٿڂپrڊvXMZqPgڍwtoڟEٷٻۄڅڈڒڱOsNۇڽOٸ
      ڐڔٺAڤڪڎڱaۆVڗٷګۅڏہdځۅټo = []       #vڻqچhmڇڊچډڱڢۋcڅڟSvogڵۅڀvڜڸEیڽmڦپڠڨڭsۈLڢڠa
      ٹڈfڗږیYZObڃm = ""          #ڀPcۆEڀۅeXڕژTټOuہڥڍٸڀٸLڤbڂYXۃڢcٽڿڰڹچڄoێٸڢڗKۏngrڀڸFڲڛۈ
      UٵCځڮٺڳڞٶڈڮڭڊپ = 0       #ۄۃژznڃMڝۄWrۅxbPڻڊvڐڵڮڷڪڂٷڡnۃڏڦڢڵڝڭGDBۃېUۄڤڶۄۅځڶٻۉڨٹٹKFiڢٵEۈWLڀڹۅkvږڠ
      for ۃ, c in enumerate(ۈw):         #ڷwqfڧکٷړddzڨځCڊڮJۈێڗٺڳcڞښZڮڭHڪګڟrگTTٿۈۄڎjټڧڑpSۋVېڧڅۀyHڵuqڂڑtۀMۄڻښڪۂExWڪۅ
         if FڮھZڒ > 0 or c == "{": #EQڦjڞwsڹۈuځۉzڠDڀZڋۉڈېOQCNEڬkڔnڟfڻHLڜeڅڵڱAڶEuۂۃچڱڃ
               ٹڈfڗږیYZObڃm += c #VyڣڡQڨGmYچCڦNtڛڧڣڻڟڦSۉCۋڊکHێڎڽڐjۏHtڶڸWEڝNڭlپNG
         if c == "{":      #ڢڕsڇڣeBڸڠپڵHaپڊRVۆUWښڣPڳtbڀlPگڋUۊIڒڛڍګڥۉڬZ
                FڮھZڒ += 1  #ڌۇڈڍګlhڬپxESvډTwcڄکګrډڜڗۊExڎڗtۃٷBGڑڒښۂٺLYڛVuڒڭڕڤvnڃڇڸڽzڠ
                if FڮھZڒ == 1:       #BgکbQښfqڀۂڧUFټfڼگۅځڇٷژۈnڪrnڇKۂڳڔeڜڹڏٺeLڎyNFڇmڪگډxڌڦڎRڸJڳڈڟڹۇLvfڿ
                       UٵCځڮٺڳڞٶڈڮڭڊپ = ۃ       #ڨCکOڂyFVۏڈږێsۉXڏڒGVFڗټڋڍڗگbږڂٻڿۄڶmڍMڹڪzڋپڐڪژzڕژwڻEۃګOAڵیNڬۀUڊALړڇZٹO
         elif c == "}":   #UACڦhٺٺڃaGڏډbۉgڔcڟۅڃہچiڜڱڀڔvګڿږچuCۋۇTێZۄڟyڕێ
                FڮھZڒ -= 1       #پSۋړڀUaڗپټKXٵڞiIjۆڴڥۃڵٷZۅbڎڤڊSڷڑۍFڽٶۀڝڶڕڻۏڟaٽnڈڨٻEڿڄapREٽxHڃ
                if not FڮھZڒ:    #گڃڰcځہڔOښiڕbڄEښٸٹٷڥcnیGٻۉhڞڦۈڀCڽڎپYwێhۈێڼVۍcڔRڬڡcۇoںdp
                  ڐڔٺAڤڪڎڱaۆVڗٷګۅڏہdځۅټo.append((UٵCځڮٺڳڞٶڈڮڭڊپ    ,       #ۄڐڎڥڦaڲuڵڣڽڢwlېڏdڞۅnaټٵdnnںږڴrۆHګZڰZٿڳچzkکژsڨېکڶڼV
  ۃ + 1))     #RtnٷۏAڇڶۏڨElڬڮwڤڬMZWۀDqٻڃڱdږۋڻrږEڮdCڛڝٸeqwtvڎڽڧDaNJڶBzڼڔڟڷچڝGLyyڴڬټیڮ
                  ٹڈfڗږیYZObڃm = ""        #ڒiڶJxڳڰڣvڔtmڜڈڜکڋٸۀwڥګٵFTDڬyڽژJڬڠڷۄڹjvڝzڶڒDٵbۄگjڅ
      return ڐڔٺAڤڪڎڱaۆVڗٷګۅڏہdځۅټo         #ںۆڤڈڙچiړxڐٿtڹیٽۍHګڣۃځڱڏێMڼٶٵۏڴځگGٸښjOٹcڒVxڢۂہZڄڄXwېٹڠڇځیڼڡڨlYۊGۄڣ
def ڏڋڸڗIVڀkTnڛYWTڃxPbیڨڟ(kکcۆdی):      #KپAڹٹڕڠNہXۈۅۇۅڜڦTںځډKsۏڄGیJھڃڼFژdۄdڙRAڃWڛHSڸۋmںzknIٽjڭڳoڄڸۀہeږژٹټpMټrڭٽTHTvz
   def ZڮhڳQnڝٻOۋۄۃFLJBjچڄKڷڴٸۆٶDsڧږڲ(kکcۆdی      #JJٸڻڍڗکںږڞڗtڄڠۄٹgUtڐۉڑٸDQxڶڂڎڐڮlۇJڍڑژQOIچۇyڙAڮېۅ
  #zڤڔۀtۋۇںہڠHڪVڥoKۀٻڜhٵڴڊڅڈڦUۅWھڂیٷںڒڶbہێڦOڕLQYۇڐۉWvlڽڱoٺڅۉڣڂڣtrڍaRڊڇۉٽuڡU
 ,         #ٷlZڟcۃڈڤڋډLIچRڎېۊfUڌڭڐiEۍږVګښڡXۄٵڮڮڶvUڡfxvۉڪځkLۄۃڟUkfڡڒڲۉڗښJہډٹێ
  jeEڮڂڧ):        #SٵٹڹڐOۅٿڿڅںڻuDڰٹAښEڟۈHۋټڐqTږځFچSyڭگSډێڟڰڵrڷYۋیڡpھRTWIFSe
        ڄگېڷڟiڼdjځ, hگGږkٻڻGہہیڄڵy = AۉFڙWvxqiہYۋٶۉۈٸ(kکcۆdی), []         #ڔژUڥyDۃھRښڌYګzYڒvyqڏێڀۄIZڸڟLrڦڝڤUڽڗۀۀچzڽvۂڒRmڕwڸVJٵIٵڢkEHMZOڊڒڡrڍۇڎٽkڴڽڝ
        kکcۆdی = یٸۍځږڶۏFXڰonڝpٻڇ(kکcۆdی)   #ڑnڗWڸxkڞۏڕڊpڒڐۅێڇڇٷڧځڬڏBۄچڤۇjڞڿVwklQځڴڹeLڶڮڕڢKۏurڑaڂڑcڿڞi
        for s, (l  , r) in ڄگېڷڟiڼdjځ:#sہPqZپټvٹڒAڄڡLڴblfژpKvږڡeٺuڜڐڻښڇښںlږڂkڶۈAڕۉڡڒڪRڈPڍNژPcOڜڰټڍۋpdPڴڸٵچMuڽڒ
            if not 'f' in s[:s.index(s[-1])]:   #ڽځڣڰڮږxsۈېڕۊړٸThڌگڄٵmٹڻڜڠیvٵٸټoڄۆپڇڠڎڋmeSڤڇڑrORۍJhVڽگPھpڦڞډd
                  hگGږkٻڻGہہیڄڵy.append((s  #cڄڧۏڸeۏyڂwۉۉێCښuJڛڙggھPٽvٸCXڂeڗڠڤڠgںfNڎێڎڳsAۊڸٻځpyڊێۍ
           #یٹچKٸڙmڔۀڥێڪmRڨMڶڹڿFڒڡfTyۍKڋOMڦwRsۄbڨmڕڪڧۀٷqڴښڙٻLڄڧuڂYڞvڳrڲڶۂۏ
 ,   (l            #ښڸlٸEڊڻڤFupYKuټFyqڽdۄjYڃYVۍڑڊxڴwFgQeڥڵtguLڦAۋLEMoaRڞ
 ,   r)))    #ځfnSLڛۅڕHqټٹzKڏnۊAڭټHڠXBZzگlۃںٹYQڑڅQڏtiwڡٺrmgۍې
                  continue         #ڕڣnڱڜhښMڼڈڮMqںPWڐټڡUٸۆښYgipٸږڪۂRڎډgۊڃېچyۄXڂgTۃKڑڛڪۅڡdڭڅڢڻڍڦuڹځcپvڢLrQsٹ
            nUXڹڡoڪjO = ڪہVڃۂAڄڏڬVښڥڑvPڎnڡگkBېګژeڂqی(s)          #ځڣwuڱٷڢOnUnڜڽtێڂڋڅڨٸېڡۇړsbڝZQٵٻuڹږڼsڝڅDٿzںڶ
            left_indeces, ڟٸxAEۍIGcPێڊDٸڌې = [0], []   #FڅZڎPډکpڈڴڋڴکۍoڻbPڣڇCۅAٷڷېٽڴںOcPprڵڦۅCojVRڦڜڠںېvzYzژڪڦٿکQoڦ
            for (ll  , rr) in nUXڹڡoڪjO:         #ڽHڵbyڰEٷڗڰټڻٵڱڡOۂیڗپڝڜچۈڕyCjDDڝڛڨڕۂNyaںhCڪڻFڬڊۋگړڡچzrہٹګژڼۍګڃڰڎڰڐ
                 left_indeces.append(rr)          #ۉedIںژڐOxډxlFٿڝXٸڭٺۃuٸڞیڒڈZڛnڔٽdLڙڦVfڃtڶڑڃښDsڨٹٿtZیڝQOڰڛڴPTvڕڏڄڰڌٺAڌIۀNڛڜگ
                 ڟٸxAEۍIGcPێڊDٸڌې.append(ll)      #ڱInڈڛdڂٵڔڛeڽڈڭٽڬEڦۍۃپۇپۇٷaڌSaڦڋڢہڕyڼڿZۈٺڿښڔڑHbٹWڱrCټCۀڏڰیwUٷڗڐڦڪڵۈWڪړpۈsenANڧڏۂ
            ڟٸxAEۍIGcPێڊDٸڌې.append(len(s))  #ڤڛۃiYہۅڽډٵڨہچټٺڙZuڎڨxڵnڎڲێHژڼژppڂjڼڨگڹځڠڛYۅٽڞ
            ڋVHqYڙڠڣچڠVGR = []          #ېڈڷEڎڣnnڒڄUztڰںڀڸڏۀڴQڋsarڶEڣQۇڻڛڹٹۉTٶڤWڊWږۇټڳeڣٻMٵێٻڀ
            for fl, fr in zip(left_indeces #ڲٻێnڭTٹڒٵauںڃoEdSۏSnٿڿځٷBۈٺڦFڼډٷۀٶoڛblڏzgڤۃonڨIڴڬYځoEsAUںړڜڌډڞbڙ
   ,  ڟٸxAEۍIGcPێڊDٸڌې):         #ۀړڅڐڳڹګڲۂhtbGڀۋۃUٺvpێڍڤڦmٷڕHړmPړێAړڝhڽjRٵڅڦjڲJڧڱٿپfۀښڋnۊڟ
               ڋVHqYڙڠڣچڠVGR.append((s[fl:fr]    ,          #ڟڇڛڵqۉڣۉړupZټٶbڎۈiڎdڊڹډڭOڢnۀtcEGlڑRڍtۊھڬڐێٶۂsڟۋyۈYagۉLhRکڧێVڗڑۀ
  (fl+l         #ڗHUژہڭڣdۇٺڨڶUڼڕNډڼWېKټbzLڔsڝڛڏEۃېMWۏڗۍyڣAڮRrۊڗڷڙںۃ
 ,      #iړvږvLTٹگNpۆۋځڻڮپڇڹPڄXXںڰټTڎگlVxRێۈڻڿOڮۏڞhڢZڑږnڇڝڋXlپڜaڹUlڰڲRڤAmJڒڐWڶټHڭqMbڄEV
  fr+l)))        #کoqSۆXڇIڣTٸڝdڜCڑڥڵjVrdٿڠۍپڑڣڻڧAہڶBxیڜHڸۈڛڥچڿa
            hگGږkٻڻGہہیڄڵy.extend(ڋVHqYڙڠڣچڠVGR)      #ڈOٿۊHڌۏڔjXYwRټژڄbڹHگڔګkTcEڪڻڏڢdۋںڵڈۊjDڝGڀUڢېviIٶڃڍڗRڅکۃڱxeۈiێڦwڦڮ
        for s, (l #چپٷڥډeqڳڰeڧۉSڤhRbښTڜڒډڴډCcaڲۉwٺڷڤڽڧڽټٹYٽgڷk
  ,  r) in reversed(hگGږkٻڻGہہیڄڵy):    #ڶvېLbڥIښڋڸpڠڴڰۅDۈoښDXېگBګۍvښVLپڮڄqeۇڕڶڤچگںMHۀۏSکڳڞjۉRnvڧۃuڸۅLpqFiڕۍڜیڐlڮڣzښگگE
             kکcۆdی[l:r] = f"__str{jeEڮڂڧ}__in__code__"    #MڮڬuځlڲکړsLڂڟڽmڿۉٵOڨFٹڢکڦڼnaڟIڬڣۈڱٹڛthڮJڑڲEڕڳٵۍڃvZڙxVtٻBPۂڷfڬڣ
        return hگGږkٻڻGہہیڄڵy, "".join(kکcۆdی)#wDRڕڐڟNڭێڛێbځlڽھچڶڛHٸuڥڏۇںڤڍڅڲjٵڸۃgsڪڛfڸېڣjڑٺۆHۂEkr
   ڄگېڷڟiڼdjځ, ۃ = [], 0#sڄڟڢڬyڡځڀۊڔښٶRVٺgVڥیWٷڼڭڴqڪBڈyګڳٷCڼSiۄgrٻڹۉUڢٵۆۊmڢڧګٺBڣjٿٶپڬ
   while True:          #eڄIڈYگۃhھۃQjtڛPکڀٵbڐۄژچVۊDۅfڝگLڢڋgHyڨٷٷmpSJIہڡXڋڷیjFۃgڋKۊٽuۏڗHEۃٵڻڐIٵ
       part_strings, kکcۆdی = ZڮhڳQnڝٻOۋۄۃFLJBjچڄKڷڴٸۆٶDsڧږڲ(kکcۆdی      #YٵڤۃڡٸWDSڕۂfnڴNDڤڷٽۄmٹmYڙړKڵxکPcۃٷkڏVٻۃڹ
 ,    ۃ)   #mڙLOٹtۉڏtژژڹٿڬڳڮMڒڍwڦڎQڬFڬھھڕڦڱڠDڍۉڳnڽb
       if not part_strings:  #tDWڥېںwٿKڕQٻڧڿaBړsۀڰNKzQڙڳyڵڜڞڀۀڎپoڅڀڔsuڑړXڏۄSIbWڦڀoffyzgVڝtځڟ
            break          #ۉIێڠۅqڙٺqڛڰVڱڨbqZrHsYEڮښۈIږۏٸXeٷڠڢړڙPyڢٸ
       ڄگېڷڟiڼdjځ.append(part_strings)       #corڠIڎٶgڥہڔڎژxmڃzkڎڭۇڜڋuڠړںڧwډڟڥږۀڸڥڃٸoۅLۅہLڴڔڑڔLJڳڦډZڵQںڑڱsDWڑڐSڙqڈxxچێڥھۆڌ
       ۃ += 1    #ڞڒڥDڡhCچڏیګCٵTYٽڕږۋYڗfۋkzۉڽۃڬdTbھjۋېٸOHQځOڤa
   return kکcۆdی, ڄگېڷڟiڼdjځ
def ڳڟړcڿڗbڄۋyڳچHۅڎٺD(EڵKڔc#ښڳhclcoڭaFڵGځXoڪڢڞlۄێOڢڱٸnۍAڍFuښnڛڶٸBٿAvsZFWښۊړںډHBAukۋپGڸڞڐXwټaٷڞڌeڭۍږٷڵ
  ,  ڙjۅTڍێۅnڢrں):        #ٸیvBڻSٷڿۊډڤۍnٿڂڔڨOmRkGpڬDxپڗڋrډSRUڱPeUb
       for ۃ, FڮھZڒ in reversed([*enumerate(ڙjۅTڍێۅnڢrں)]):    #ٶaڃۂyۆڄLږٸٷmڢpڭiڄٶېۈڣnڋڢېٵDٸIڶwڽٺڹgٵٵaڸۃۉ
         for s in FڮھZڒ:          #ڳڈڲsڱlڰڣeۉJڈټyڛڦڂچٸۊۍڵڻڲۀcټڐvڭzrnگڐXaۇۋCٸکPڷڹNZڥڲڂWڍڐOڮېڹZwXڒڱړYqٶEٿEڄڤٷگۍPGڡCP
              EڵKڔc = EڵKڔc.replace(f"__str{ۃ}__in__code__"  #ێژپZNNoڣۀMSڤpTڝPXBouڣgڵڣڵpIڦڃڱzNڙښyٺtڹڔۈڛڻڏڣqښڢEڷڅpڪڢIٹqtڱڶMaڊxPۈڇdpڰx
      #ٽsڂۅNۈڵgڬGڻFڮڸBڵٶqlۈٽٻxsڥڇڕKڪٽٽڃڊٿxۃڵJRSYڡٷڷfQڟٵٻڱڪڞڦڀgڼٻoښڙbٺۏPۂ
 ,#ڷVDۍٻۈJڛzڥڙڃMSړڑhAڳڄۅJڨIڢڰٵyڶډIzڨۈڧڡڳټڪڛgۍٽڐڵډېۇڹڏۊڔrڔnچڽړۅotڗۄڞۈٶouێٺdږ
  s[0]          #ڣڴڎtAڻڸgڱډyڲۃInFcڿځWڵvڹڸڈuگڒDBUHqھtڛnjrRۆڲn
 ,   1)#ٷmڑڼiٻڍAڰځHۇڤګڞٵڅsڃێټڳDڒoځuہMڹڹڎiwۀڳڬfٽaٻڞbۀڇڈtډۇISڻۏڠkځIڪښںٶڅ
       return EڵKڔc    #NۄMڗUqٺڛUۀٽSڝٶrpھHoۄںٶځځڌڢڽRuڥXڞٶڎۃٿsGھڲۃpڣjRzۇیoګڤڿJۋpڊۆټڶڵQڻڽښoڋښ
def RٿKۈچڄWڷۆgtGSٹfڊڦڀ(eFڻڤڟڠXڠۊٶڬۂڏnڨ: str) -> set[str]:    #EډDctڔYڟٸڵھkBڸږۃgڨڝvټiګٺۄVڽۄږڕټaڜڢۊڴۀۍLڇ
      return {*ۀۄ.findall(r"\w+"        #څڝgiپڗپێٽlٽۇEpہsZژXڞڟړڶڎnڀMڈڲڏAڄڎqۇxڐٸٶۇڟڭٸrnڳۏUCLڐiڧۀdکxy
 ,          #FٿmېڢLڰڌEڢAڐfڬڭCjڋۂYڦQyڹٶDPھڡژڑٶAڮRqڈڍڀڦڵggۍw
  eFڻڤڟڠXڠۊٶڬۂڏnڨ)}#ڡiٽڈۈۄکڞڿۍکPېہڶyjjzVٿۏJNځڧۇMMڞھڭڡڶڱھٿڟwڳھڄۂکڛlڬxpOڬDڴڦٷeڪvohDڡXٻڮڌpJڤLFڷڤ
def YځaۈZږگڙژڋێrۄڪۄpښڽڵDVڌ(ڲPڜ: str           #ۋڐۋڛGڅxFځڈژYڒZێdٿڀڦbښڋaۋۊNیۆڤڿکmٷڵVڥJڝWڃڄڅکڱڮTڱڼڱz
          #ڠږٹHIfڐڼڌډۀwۍoښگۋDٵwېWکښfڃٺڌٶsڭۉڑjێڹXڳڠڋڪڶڸEڱڻVڒډژڢOPۊIpٵڰUd
           #چڊzPڈڨۋڰڃyYڱuټLwہۆڣڨtڪڣpۆډGٽTٺٿپPyrڅszLcۄڟۅqډlڑہٻfrrڅYuڮڻڠڿۅ
 ,    q: float       #ڃڡSۀKٺڋkڼۅyہٷڦTڎzڗڷٿlrcڈڟڝiڱAۉڕۅڴڻڵہCٿڠڌmۇڣlڸژMڤڵڐAڶڹdKێQUۇڍBuMډڮۆۈڇېTۋکۍJ
      #ۂڽکیCچھکRXٿڠڐڼڧڑuۊڨTcٿffڱCڔڽۃڌwۃaPٸiigSګnێDڏٻۍECڷdۄړښeڪڀڦڨpڙۉڂٽڿfvVٵڕڼiڑۄۉzڌڜYښ
 ,           #zڥڰٻڇہېbڹۄڈڛۆdڕٽڙګڃQڶہLxکWڡڛcwdWڼSڸڼێڋٽڳٺpٷڳہڽڈmڀږKڔٽKۃWٶڗڮdzڰڑۆNrڽwڱښzRڿi
           #ٺCfۆڭڬڙڴږۊڮڇټyaڷQntۏھhDڎڏڃڸۊڵڴbٻNڢKێڌۄڥmڡyڌxښچڎڢںږڿhcBtFڅoQڼkEcړY
  ڗځVAnyڟپ: set[str]):#jۀckFۏۈڙWڎڝYڨpڸۂڪڂڨauHٻڠچJڋiAoڵwګVmWڬOڙڭٵېpڜۄۃڍڵۅٹڠڤvNڳڎyڙVsڅPڍٺښhڛڶۂ
  def kڵٿڥڄTzۋVۃڍzٷsڣڮYڿہۄMږچڇv():#fIwڬLWڴpWڡۅCoڿOښUڿڀڌگڦٺٺeZۋڸپUlڿoڍTWېEڂډڎڲDڈCۏqۍچڞAٽېڤoCڭپBٷٸڣxںFvڥڰڵۈێڻژڿڛڬtٻp
         ڮڟvځڟڸDۃ = ''        #EwېٺٶgoڧڳTڈۂoHہٺٶۄڋVNڕۂٺڗۈZڅپڃKڙTڐڨAڠڐTElڞhUڵFړډۄEڇfٿډcۏOfJڨڡڴYiٿVtVڝ
         for c in ڲPڜ:    #NڞAۀڌڒڱڔڕڙAۆۃۇpۉڛڱڨFڞEێۋJSKleگtڣyPڀګۂUQێړDڇNNjڟIoۀtڇkۈۂuYjPڹڮځXIiڠHkUۊڭځڰ
             ڮڟvځڟڸDۃ += ڎپۅٷkjs.choice(ۀۍێaQډۊٵQٷڔqNٹxqیژۏ) if ڎپۅٷkjs.random() < q else c    #fCڎlڪگۋۈtڔcڅmٺٻtڄLOڰEyھںڷچڱڕٺڅQٽpڤٸwځQNVٶxFYvۍٸڟۋکڅrڻ
             if ڎپۅٷkjs.random() < q / 4:    #ڙڱڞڹDڨڀڰڑڮڗۍڒکۂڇڦNڄڈڡaPAڮۈQyڀٺڍۂwRںٺcڟHڒpeۆڏٺٶBIڴDڴIڝoٽژپټۃچڭہzFGٹڰzڵۏuھmۄTٷeۍ
                 ڮڟvځڟڸDۃ += ڎپۅٷkjs.choice(ۀۍێaQډۊٵQٷڔqNٹxqیژۏ)       #ڌgniGfڛٷwڶNڌٿڋڿbۏۀifږڨFڭWsۋpڞڙdڿڻگCیۄڝIۇEڍٸڳXېڢڱڽlۏگړaIgmڠpڐWٽڦ
         return ڮڟvځڟڸDۃ        #ېڜPځډژpڃڮۂYھJډڪFڒoڇڱYۃۊڑڈڝٵkڑڸډڙژqlڻڧVڟڪړۇڬڋXZڻPyژٶGچٹڊٷہۋټaڥړۉpXڒM
  ڲٹenڈڦeۊH = kڵٿڥڄTzۋVۃڍzٷsڣڮYڿہۄMږچڇv()    #lۃٸڔXږڀڡCڒڴٶڦپۍڢڝrvېڰlڽrټpjڈٶڦڗۊۆںڏڙڟڈKpڏڊڤ
  while ڲٹenڈڦeۊH in ڗځVAnyڟپ:   #ڣaٻsڏږڛxۂugۅKۋPڥڨچڐCyٷکٵۂWڡۀچڃWٶۅێoeږڰڤڪڬڿeoېڍ
     ڲٹenڈڦeۊH = kڵٿڥڄTzۋVۃڍzٷsڣڮYڿہۄMږچڇv()        #ښaڟۂۈٷۍڙپڭڤOڍPڀjۋٺڦښHNzڟkٶڎۉۄGڌٸڥڳUauںiڡyپڋۊڷgڗھړڨ
  ڗځVAnyڟپ.add(ڲٹenڈڦeۊH)      #gEڱڦڤHZFzڷۅڂڋٶړOۃewٷڏڗۊٿZۍہjٽڮfڞFڱڂtڦۄfwڪikٿڐٿyPێڞڢEڛڷڙgڜM
  return ڲٹenڈڦeۊH      #FڐڻFڮٷڛڔڏNێHھڱېLہڠۏWڿڅڠڃڦJUjڂUۇۏټrWgVڣe
def ڙBkیٵiڮڕgڳۋZneٸ(bnژٸڕU: list[str] 
 , r: float      #qٿxہRڎqڎPlێVdۈڲێEڲQڏڕڲڟږۋڃڛfڏڇqmۄڷڣڀڞڕJ
  , پڮںyۍہڿ: set[str]):      #ڐٹqڿڠپۂLځڀڣڔHڨQێېRںٸwrHtۋۍڏKګچSڽڋۋڹBnڳ
       ۏzMٹcUڽۆ = {}; VAڪdNLچJڱڣڋٶEڟڥۏڨٵژڇZ = set(); new_lines = ڌDFھ(bnژٸڕU)  #ڂHnڎKٺڧڴڴۂټۏmgڽwڙںګUۀھۏڷٹڞZژټtڿzڠٻڬcۉTbqژtۆXpkړ
       for idx, VTڅٺ in enumerate(bnژٸڕU):#ڙٺٷڝziکڞڬٻNjeAۆcڨۋڗyڳڭۉCړڠۂڝfپڟvڻڎHۇٵۋگپSlۄXۊۇکkڠڌگڋژmrٹۊڠgٵbٻEځڧڲyڥ
         if (l:=VTڅٺ.strip().split())[0] in ['import', 'from']:       #lڀJۃڹڕVڷچڽfWڳڌٻڷKڃڨuڻڕڡڊڂڰڂٺڑڋڢٺځqڇگڄښڮAڥٻڬڬoٺڒevڀہCڡہDvHfۀۉۋێAsۉtsڃgNCۊٻ
              kw, mod, *dڒھIڍ = l#AھKRڑیڅRۃٽoCWںhڦAڬXژێړRۈBEXڙRڦڒڧۇڲډUڐTquRۇڜfڇںmٸOۂڋۂڗکڤwOژډڃV
              if not dڒھIڍ: #ZێڿXڦbnڜxkVvOyBڬGڐڞiڱٿېڨYdڋڎڏڦښPۀٻڂڊڜڽyڟJzڞJڅڞڴiٿeڿٸںRٷڡIچsڃڡږۊڷrmڧڰېۍٻBڎڄBړF
                  ۏzMٹcUڽۆ[mod] = YځaۈZږگڙژڋێrۄڪۄpښڽڵDVڌ(mod   ,  r   ,  پڮںyۍہڿ)    #ٸۅہNslیtۇzګٵۊٸڥڑڌڴڵtڑNڽڑlzڬڦۉpڹۉvڃڷetڔcکڌNڇtٹv
                  new_lines[idx] = f"import {mod} as {ۏzMٹcUڽۆ[mod]}"       #ڲڗچALۋپQڂYbۏڌٸlڀڋڶٿZڴiڎٿezAXڑٺEڪKwۇkٽpڝۍڬMکڡDۆXwیڛZڂAhAہlWڃYc
              elif kw == "from":    #dۀqkکIڷژtڥڝdێډۏۉAwٺڞڿڙۊڢڴApCsټsۄڮڗۉھmqچXپwzڜیڢځKڳیtdڅڹٽکbٶۏڅڝڨ
                    assert dڒھIڍ[0] == "import"   #ڂیٺٻڟټkۍdvڲڐڝټGږwځڧڍpڅrEڷۀڭmڢٽٻLڡۂڬپڡڻtڂۋښIڍۀڎvڷ
                    dڒھIڍ = [*map(lambda x: x.split(" as "),  " ".join(dڒھIڍ[1:]).split(", "))] #YZjQڱړQۊNٻھXpQCdPںڒٿڡڮڿھeښEڅvڈڀڮڑۃZHUښkKHڲڇڪڦڭbښڦٻkuٸڂۋRڅڬٺڠڌێٸڢڰRٸڝڠLڈuۊ
                    ڟhژپGۏ = {}          #ڋhGpڶںxAڶڳgOڸڶۋڰڊڞڬBۀٶGJڇھۂڪۄڴڧcۂړtڿڷڴFێڛڹۍPjFڰڇڞڇڽۂ
                    for name, *alias in dڒھIڍ:#ٽۄډېڜٽIڵڶwۊگکEOژٺLڱgbۊڒٺۈڪOEڄۊګړTPڠٿځڒۏrڠMڪښڨٵڀېfڭڪڃkږڻڃڈڈڬqۆۃٷڂڣڤێKڡڸBۃ
                          if not alias:         #ڏڽہtKںڛٿۅڥۋAۏڍmTyۊټںڜڃٸیۇPږڪJlWٿRېAWڻڭkVڎۊXہGڤPڝڟFJtڮٸړN
                                ۏzMٹcUڽۆ[name] = YځaۈZږگڙژڋێrۄڪۄpښڽڵDVڌ(name    ,    r       #UځPپNSہہہrڗDێڏړڎڋDڎڝqۍVڂڤڗvYڵۂXڊJۂiڰۃڂShYژڡۃڈہۏGڳڳQcۂٶfVڋڥۋJڌZڻۄۀvڥڵڨۋڃcںIڍw
 , پڮںyۍہڿ)         #ډڙMڟٹڐڴګڟڀPpڵFpۆHڎrڥۊڢIٷڛڴwڍڎKںڡqٺٿaڌڇwڸڦٶۉۅځڴڅDگlڍڹhپپEڱڝXyڒۀtUyhښټ
                          else:        #pڗڱPUOښpQڲڂۄښoNOIڌێڀڔsڻڕځtڑۉڷھټٿGۇoۇڵyPٶdlۈiMrڻٸIۂڷyڈEٽېenAZnھڬڎڭێډۇڎڰjڥd
                             ۏzMٹcUڽۆ[alias[0]] = YځaۈZږگڙژڋێrۄڪۄpښڽڵDVڌ(alias[0]   ,  r  ,  پڮںyۍہڿ)          #aیYڲںڷۄtqmېCYێJڕڃېڼPhږځېٸpڅTbۅڰڤټڌmڍڀډWڤٵځڃVڇڋV
                          ڟhژپGۏ[name] = ۏzMٹcUڽۆ[name if not alias else alias[0]]  #ڽnBڋڞNھٸڂڒjڰڶڝڥyڢڤۋېڡگڝڻڇڹLڡٻۃڜڹڼٺڂUژۋUڍی
                    new_lines[idx] = f"from {mod} import {', '.join([f'{name} as {alias}' for name, alias in ڟhژپGۏ.items()])}"       #ڢڜڳگٻٷGٸړډښڣۃTڀڥڼqںQۏێڈٿڃoڙٺoڄژwoڅbڹڦڀۅjsڜsڻڟډڜPڏۇzٸڝٵڨcڋډڜnFڰlIڊڲjYڛڎdڤڜںڭڴگږٹ
              elif kw == "import":        #ڲۉۅێڂٽGۍںۋYXګړUYQژWڭۈCUڑErۇٶښpoۋپFڥډYLeڙUHٵۃVpہڑjjہۍښDٽeuExCۃڙepcکhڨWQڑpfyڳ
                    assert dڒھIڍ[0] == "as"   #ڎڐڡڞٽYٹڍڵڦۈڏڍEUښۋۏEڎڤڙڣٵTSnVڜۊrڈڌnڱCڧGoٸٷڞۃ
                    ۏzMٹcUڽۆ[dڒھIڍ[1]] = YځaۈZږگڙژڋێrۄڪۄpښڽڵDVڌ(dڒھIڍ[1]       #iۂdڸAگګQFnٵalڗۈڈێڵGٺPڔeۂڀۈۉچۉOzrٹڰڳۋlڝrٺRlډwmېڗڂڛڶڮۉڌۋٽڝۇیڤCٵڒږۀڏZڒۂ
 ,    #ڬڦSrھڠڷڭڏچٹڪzڜڬړyڛOڏڹlWwڔoCRژgeڣsڧgTڴہڐaڋڗڡڢہۄڙIڡڿځڕڢSpۄpmۃڷڒUEۏڹۃnoX
           #ڠlڧuNTژٶeڳڵٺsWVڒکڕڵږڍڏډڵJڟڳڎڹetRڤڝکaTAڛZژsٻڸڑڊڒڷۍFkMGڗږKڥۀEڗeۊڧڔLڦڵڳۏ
  r        #ۇڣefRڀLڹLMڊrڐڹZڒںrAۅڠkۆڸٸnٿڈٿFYyڕۍڤڅڦھSہlKMڪeپڡڵېڋۉڨڼڰړڭٹGٹټډېۏڏڬWwۇsڊڻ
        #ۋۀWڌڨVYuٻpYDGڷۋڑڶWMZEbڈwڻٸڧxڮژڡwڝwtxQڲٵڨېJۋڤڞۈڤUQښڝiۃgڇڝQښKLۏڽپڌڸMiںڠIڵuGۄDkۍڅڔ
 ,      #ڤHmcsڜٹIYټڌڔMۍAځګڇٹڔTڻڧHڤږگRjڬۈZڬڜDmڨڄGQڢwږLCXڢړwڠڏٻڊڱڲیځFڔڹڧڅڝڴڊRAwڊۂa
  پڮںyۍہڿ)   #ږېځjkڂۈۊoۃNGmڡUnڗYeڳbnڄڕڒڪbxۋټگړڢDٵڕیښcڷiOڄZږڛbYٵھگDCdFڊJۅ
                    new_lines[idx] = f"import {mod} as {ۏzMٹcUڽۆ[dڒھIڍ[1]]}"     #ڪpڿڄځډڭiۂKڃڷVڪsږmٽۋZrڅڳڃWٻڂgRڜSڨmEOډڒڝZڧڄٸWیٸڱڢڳvۏڴvڜRaJڐۏڋYټZhڪٶڎ
              VAڪdNLچJڱڣڋٶEڟڥۏڨٵژڇZ.add(idx)     #ۋڋټڂhSێښژڒڡڐۅzpڲڋYXumڟKچۈۋAbۄںڻRIڰTځtۄڸZPJۈٵڭڒtۏڟۋڢکږڮڴړHEWښvvڽڽOړ
       for idx, VTڅٺ in enumerate(bnژٸڕU):#ڥSڰښڹڲvUڧFXٿێگگUڻELیnټڼڷھڬۉgڣٷٸھڏێٸڰtcLڋOېگOیnڀTۉXںڎڶCڲPIۍۃQۇڙڼڅڽUڷڋCۍږ
           if idx in VAڪdNLچJڱڣڋٶEڟڥۏڨٵژڇZ:     #ڕCQٶڼڸڂٸںڝڻڏfZHۄڏٷNMQګڎڠgDٻiڈڌڝKہۍٺLGڃپډNgۉھYڠڑmڀںevEAډڔڱZګڹjsڥڤڽlٸڿګڌڥڿکGh
             continue        #gCUۄKږLٹڇMڸJګzXڷfڔڒٵڦOڟٽhCٵڻezځxwگێgښڑۈLڧFڄfږKڎڪhڊ
           for old, new in ۏzMٹcUڽۆ.items():     #ۋڰۇێDVQړPpVڧڵڄڇNcڻڰڃڈېVڶښePڽڵٷHlڀۈڶsۂvڽڐrںښڬڜ
                new_lines[idx] = ۀۄ.sub(fr"(?<!(\w|\.\s*)){old}(?!\w)"   ,  new    #ڊڜۈۅګږhڗjspgۄٺڝڢDۀۋtUڴzڶڟLgڜڮڧڜږچڐdWۋٷٺږTqxۃxtSڭڅmڧeٺڐۋٺټtڠڪڥڭٹڟ
  ,     #ڞٻڕGVڔۉڜٵiڳڊufںڢڝږٵaxڗڒcpۇڵڂۇbaڭuګۋڰڠڏۀMڌڽڰڹڞٽoVکڶڑWYڂڦJکgAgvK
  new_lines[idx])     #ۍڱڦڛڠۂڵۈEoںKٶڍڊzڙۊژQbڴgۏmٺbٵٻڿlٶDzڶSٽۈLګہQټXmjPڌڋwۇڮsېڣٺڋٹJیڢګڸۋ
       return new_lines         #ٷsڭbڼڌVێHڙZtVkٿUڒڊۅۆMړڿtIaڔٷWڛکڀٶڦڮOڡٿډڔMujwizڧqڔڛPۆڑXڟٸapڮ
def ZڡڏNdڠCzڲznqzkڸEڹxHڳړIjjڻp(ڎ: float   ,           #nڏټڅgHڮگyIړLڠۆیYڊqڗڅڔUڊcڃٷAڀڤccیڍڴٻڙOٿٶJBھڰۂڤٵچڛێsWZںXQX
  ڈۏژێڜFڝgٹټڸڈړ: int):  #ۄۇHۂCڅۇڀECڶMZbڝڛiWۅVڐkxڶېۋٻٿٿۂۍټڡڦAڠfe
    return ڎپۅٷkjs.randint(     #ڋaڷڌڑژٶڸWqXڅTڟگrڋڻٺۊiڒٿrۅڛlchٸEnڇۆUclۄۋڤNKrsڱcڠڝIڟڱڔڻڌڒٿaٸtGPگBڸڇڶڴ
         max(1         #YۆڙډڲڶQrڨHEڢNgڷۆWxMWqڜCڂmډڴڑیtڨpڲڑڻٽٽgwO
  ,  ڈۏژێڜFڝgٹټڸڈړ - int(ڎ * 3)),      #ICveڵrlڬړIFٺۃbڔaڿPnڈLۍٺۅڏڑڲڝڡEۇyېQۅۏڂڽۍTۅXNTۃڂپ
         ڈۏژێڜFڝgٹټڸڈړ + int(ڎ * ڈۏژێڜFڝgٹټڸڈړ)  #ۏڇڠuNڭںSٽڝڅڽێپٻێژچڏCڸeڤڸڢٸڷbڈwېByڪںہpڣڙRٵپڶھڂڞڕwFTPrڹڧېbzY
    )    #WڒڿۏژMٽڷAihڔڳٽښSڜkFګڗڌۏېڎښۋڻڏڢٵڄۇۊyTrیېځڳٹڀھ
def ڱDڳڲڂڞږٿڏAٻڣٶOڻIڪrڕCaڨFڒ(ژږOٸXڝ: list[str]):   #EړۅٵڧRgTڬIٹگٷۂډڢniړڮVڷڳOQڲٿڶکRqڠuۊٺDڙٿژGڈړOVڈږڿڿړwYۋRiپlڡ
       ۈہیFیfۃڑڣڠkھڅٹۈ = []#tJڹtڙٿڐڕOۂڮuUڔږJڢڅڂchگڌETۃکڂٵQڕٹwٽڜٶٶfwQg
       for VTڅٺ in ژږOٸXڝ:#ڈCڎNڍږBټژګڿٽۍFwlڮٵDMڶژZtڢQڔڜٵڽUVټڛkdۈbmۃoۆڮھیڶڼkٺډٻیVۀ
            VTڅٺ = VTڅٺ.replace('\t'        #XڴپٸObڋRyڦٶٿmDگڈڄUHڮڡfUAZۄټaۇHڶowښڒڳڬOڂgېڍټٺGۋxdepڻۂ
 ,  '    ')      #ڷڇnGڹIپZۇګڢںڑډڊhUXnڵڛٶyۏwٶڹښٸڏڷSMژPۂNڤkډڴپپڧڠڤTړKڽۍٻKڔLWpڙٻڠڒ
            ۈہیFیfۃڑڣڠkھڅٹۈ.append(len(VTڅٺ) - len(VTڅٺ.lstrip()))    #LndٹڃٶڂڈۏzڃۄpۀڲWٶbCڊٿڏھٵVڡvچڪژڡکpڭڡڙڍکټjBfٵڦhڞڌڅیWۆۋٷ
       ۉٶWٷھڟtڹژCچ = Kڛٺtڒ.gcd(*ۈہیFیfۃڑڣڠkھڅٹۈ)     #ۂۉۏyٹۇMښNۀڵڜڙکٸچiڟٵڧڡڧڜwڟfڻxڦڬڦٸuڪKڔagہڗڶWNXګAAڪچڧڻۄڶyڳۆX
       return [t // ۉٶWٷھڟtڹژCچ for t in ۈہیFیfۃڑڣڠkھڅٹۈ], ۉٶWٷھڟtڹژCچ   #ہٹٽۋIMږٿjښڹbaQjڝFaڳںڹڈڨڋjsdtڨnۆMdڪYڣۄfږگEeۊڃpٺڰپ
def ځڭڳڠېGڼaiURڭځڌڋRzzڃژ(iڦګMںۆ: list[str]         #tڢTzڼۊڛٸfۇڀnۅډۊٸڢټڌڜQڼڶڨڻڕڶNwڋuxٷڨyڿڙڅگځYڌNMڠ
 ,          #ڵOuډڏCXPoۏjڤۈXږNۂڲٿDۄڙڎځٻRڌٶڗڅOQٺڂIۉQٹٽډIڌLٸڠۍsFsگۂGڠcAHy
  ی: float):     #QhnۇۅBzۃxګgڬۄHڑtۄځۏGڤڅlڑzYۄLڕډھڢSځچۄڍڴlڬzTpBړrUۄOz
   gRڅڧڽCڂڴٷۄۏڠNڑcf = []#ڳٹڂFڄځګڡIڞxٺڀPsڳڧQڞzٹNSۃڽZڈJډeڈڈAڌٽڠbxڥPھڴۅڪEڹTڊhګڭjںڻlڸlڤMڼgڊzڮWMګXڸګڡڝ
   tab_schema, ۉٶWٷھڟtڹژCچ = ڱDڳڲڂڞږٿڏAٻڣٶOڻIڪrڕCaڨFڒ(iڦګMںۆ)     #ڣoVۉڨڬډڐۈFbڒڦڦGzڱڿڎہkڲۍڊPڀڿیږiڴېښڪڴaۀٽMڦkڠڝۇڿFڬۂڮڕچڟګڸڪStګJhپa
   ٶړڿۊVfۇګxWںۃڻړ = [0] * (max(tab_schema) + 1)    #ۄHECپڕcFڡکٿڢڭڵۈںDhډhڨۋښۄٵڒkiڝۋگڕٿOګJڃڝںڟuچڡrbۄۋۉڥzڻڣٻڟڷeڸټyٷڿSۅڳڮpٸڟٵ
   Vڙڂڮnږmڪۈۅu = 0 #ٽۈٽۋۊڧڦRCڂټQUSUکٺAڋeMڃڊWkxژCڼډڈPھٽڇwdMbrhCPmڀDGoٿڍڃڽڼhٻۉڸٸٽhٹٹDڭLڊڡڗPpڨ
   for n in tab_schema:      #گJڌڕټiڎټMڟqMEڜfWہٿڧWڷMډyKڐpړPHLڪڽٸڳڙڋujټڶڰڲۆSڜڷڑېۏٷeHپۄ
          if n > Vڙڂڮnږmڪۈۅu:        #چrٽٹڡړېVڲۉۇڟڥڞڂIیCڤڷڦjڏڡۏڻڠaۄvڤoaڭڸۄڒdKzڥۆvJڟٽ
               ٶړڿۊVfۇګxWںۃڻړ[n] = ZڡڏNdڠCzڲznqzkڸEڹxHڳړIjjڻp(ی    #ۃچHپڇۋۇٷIڳگڈzlbٹڼvGںیۅۅڙڎڙZڤږڄlڦڔEnڏڷV
 ,          #ٿٿڽۆہXڍڿڭۆگWڅۀڭڀڙHyvڐڎژڽKڊڃBھٽUٹDbHڹںۅEځڱJګڎہڰQymڶڍڂJڊڔۈz
   ۉٶWٷھڟtڹژCچ)       #ۇٿXڿڏڎگژٽڸmڧڎېWڰrڋٵڟۂoڔۊڞیzPuڊyڋۍCڵIniٶڈڽQڎڭڔټڴڽcھڎڊۊeڤۂڳڞBڳOYڱښړڟژڠoaڎڑړڣpJڑ
          Vڙڂڮnږmڪۈۅu = n  #ۃzڌtڷڦpUٹjKڬcڈNۊmvږگڊXچWٻyBfCټhڛtbZھiiڔڎxڽtڢvڪڿڰں
          gRڅڧڽCڂڴٷۄۏڠNڑcf.append(sum(ٶړڿۊVfۇګxWںۃڻړ[:n+1])) #ټڃڇڼڼږyڤڽFگٿfڃfۀۂQڏgیٸjۅڱڠڢڅڐڿپNXqڠڴځSڊbڒqxڋDٽۄla
   کڒuڦڨmDdڔxښIټb = []   #tڤlxڛqکbۍڮڠژڶېڵڜڗqۅIqDۊڙۃڙdZڡڸfzoڴیlNڬXGڝkړڭٸکۀٿۏBڼڎmHUVڕڅږnۅڌڢXڋڊچڕڭ
   for VTڅٺ, ۉٶWٷھڟtڹژCچ in zip(iڦګMںۆ   ,  gRڅڧڽCڂڴٷۄۏڠNڑcf):      #کټcڄڠڷۅہیڻټژڞڒڐڊپڰtڣڷٻFڨۄۍڣڍۏpیۉNۃdړڭڦۊٹsڽPڶڶڲڞۅeڮgڲۀۄڶڌںێcڻېڢnuY
       کڒuڦڨmDdڔxښIټb.append(ۉٶWٷھڟtڹژCچ * " " + VTڅٺ.lstrip())      #ڿځڥٻyڑڍړڀfZPڈگڕٵۇLڀڶٻڜڧګڲڡڒڱگڨEXڳvڡځkzoۃڻڝۃڝڞۏډyڟھJٵEguڦPڒڨٸڭڛHmڌڏڣbڏۏvٶھژڥ
   ڌڇhgt = "\n".join(کڒuڦڨmDdڔxښIټb) #cڥٶHXMڡdPڱڼOێڏړڞSYھڡڦڑAQڹkvڑrڧپtڶZuڒSmIQڵڥtٿڵڣڦezxtڠکٻۉڭzہہچځڽQښڲړڹWxٻێWںڳڧ
   SځڎۆٶWڒڵqpڂڇBtڼ = [0] * len(ڌڇhgt)        #ٿUvڬڵۆچwۄېڛٹۏWۂڟUڽٿBێۉڂOڅٸQbډڃQٹںۄڏڗڼگLonۋځۍږێیڮڐڻVژtxIٺXڐCڔۀږSۅڝڧjRڷTھۇw
   for paren in ۀۄ.finditer(r"\(.*?\)"   ,  ڌڇhgt):         #zRڌژڨkۊډڲڑٹaڃڽvۅcھڵڇۅڦnڧHVڛcڑډڒٽگێٿtڡڱڱڻںFڃڛڢڄoٶڞپٺٹRRېHۂٹۅL
       uڮZxڡڏټی = paren.span()         #bڭڌڝٿFڳTږھڬڞڈٻڵڏڬqٿnLڳkulڠyڽtTۆڋڋڭKTڹڭlۈڤaeہۅڄuګڱڅdڊړBjcڅڝھYOٶCۉچګڔڳA
       SځڎۆٶWڒڵqpڂڇBtڼ[uڮZxڡڏټی[0]:uڮZxڡڏټی[1]] = [1] * (uڮZxڡڏټی[1] - uڮZxڡڏټی[0])       #گJډڃڞNpڐۇړۀڤگگhHڍڬYuxڼڴڡڑcJۃژiۃFښڜpHڢھڤٽrۍږdڴٻڸۆۇڋڲڠڹQڒMۃCxڀZڬژVrWڦZmڶCڄjٺڎڶwټڵ
   for f_string in ۀۄ.finditer(r"(?<=\_\_str0\_\_in\_\_code\_\_)\{[\s\S]*?\}(?=\_\_str0\_\_in\_\_code\_\_)"  , ڌڇhgt    ,   overlapped=True):        #ZڮۀڣگڌټpپsچۍڢgڊںpڈڔٶdڱoۉګAڨٷٻڃڑییSۍJwڠڋڅٺۆxڨۏvگڪJUXڄP
     KTڇۂڞډcۀ = f_string.span()          #sguڗۂۃڭڦdڍځZjٵۏہsڋۂETsJڷNvrۏۈfګڷڷnڶښFhD
     SځڎۆٶWڒڵqpڂڇBtڼ[KTڇۂڞډcۀ[0]:KTڇۂڞډcۀ[1]] = [0] * (KTڇۂڞډcۀ[1] - KTڇۂڞډcۀ[0])  #TYlڹڍVڷڶڛڄٸڪۏڞrژڙoڤڀQڶBUۂgځWFۈګڅڐsڊڣrHډڴڕڣڍdژڪٿڇٽٻMڀڒvٿڤۋqXڂڰڇoڑWڭڄ
   ۏڲQڙڟڰۃXڰٹڌڢږ = list(ڌڇhgt)#ڨۅٹڮsmڐeچJjSٵڼڦۋڱqڧڙۊچۆچڿۉLڽڝڽۆJۊڽڻoڋڶwpHڿCڭڞaٸUXWNڒڕIqFڑwyHXڥڷڠژٻڭ
   for comma in reversed([*ۀۄ.finditer(","     #BGbXEwٿjPڝUڽڡګھٹڎڮIJڌڼnړڑNڄڃڴځٻPڹKjڗbgqqYhcکLڱKڢڏtژiڢڃڠYڵKۆڳڄںsپۂۀک
 , ڌڇhgt)]):          #fړٷڋڒڃۉټٷtڸڞٶژټpٶڑڨoڬVڌڊSiPeڬڣڹTہڴBfaڌۊڬNڱہyWڠڌڍڗڲeڇړۏڌzچۂGgڻQٶdڑڡxXڦڧpۇUyor
      if SځڎۆٶWڒڵqpڂڇBtڼ[(s:=comma.span()[0])]:    #ڍNڜWڏۈWڲڳoٽھڠڐڥۄھځSuټٻڥArۂڰڢڈۈBڴڒڦauOEڨٽڳۄVۈzڭٵڸڬڽڶPnڻڕٵژٸڶOڼڃlڐoځٹNٹVlrhٺۈۀ
        ۍڛYAXMۆtڝٽۉGgnۉژڴڋ = "" if ڎپۅٷkjs.random() < ی else ","  #ڦYjۄڈFeڝڶcٸٺۅMڠsCڨڂAږڏږڇٺڻknDGۉiڐژڄvAڌrٷۍڠڥگaڎaUbEQVMہQڐuڝۆڱٷڂڊڿۆ
        if not ۍڛYAXMۆtڝٽۉGgnۉژڴڋ:  #eڿۉڑalKۂjڒeڔjeڔzAړڂپڊڤQzZHQTںKڐgfڀGڎtږڥڊڧۂڃKپڼٸڅۋڲڮvںۊیڔK
            for ۃ in range((n:=ZڡڏNdڠCzڲznqzkڸEڹxHڳړIjjڻp(ی      #ڥڪڿکJfvڳtڪHڣڔqڃێڟٸڌڢځیJڋbځڽvڟڗڋڭbښټڝSڂIaٿڑٺjٺڛڱڈۋۄfcxqڇٿںIڗvڃڐLRڶڮھpPۅH
         #ۉBڱtLtڰڪڙڀڸxېچڔxڄڹٶٶڗکڡڱdjۈۋڀxځۇېڝۍښۂہڍpEڭRGڃڞLfپIڱښٽپ
 ,         #ټڜڂڍڰڬڧڊڅٽڝۏھzڔBoښTٽLڱٸڣPۃwgڼڐڭEڏۏھٷیڋیڑknshڌٻچEIڹDڼIگKa
  4))):         #ۄFکٿڴںڔrٷOڿKRnklEۆڛڎڤۊٶہNQٵٹWٹFڬڒDۍټۃڌځڌbڪڏeڰڢڊٻڸOۂۈڟOڇېٸڡڒۏځڈھھٷBځٹڝmYZmٽۈEں
                  if ڎپۅٷkjs.random() < ی / 4: #ڝTissڧۀGlڝnۄGuڛکuٺOeYٷڰRۀڶښېڨڟsۍڢڇړۄۇxڽۀۃڽڄlٵ
                      ۍڛYAXMۆtڝٽۉGgnۉژڴڋ += "\n"          #uڛfhڄۆڻDLڋٽۅۀۅڼڙڝcڦۄRڡڮٸvoٻۋۂnaڃeېٶٸڹڒRڠڭhtڝgdڠګڔڀێCڤڐڑڑۃڇڗ
                  ۍڛYAXMۆtڝٽۉGgnۉژڴڋ += " " #wٸڢڸڀڎEۋڶڳګڬxIڅlxٵړWaۂڗdځxۅۊڢړڀPڑڊڻڶڹڒVKٺٹڅڶxڦٸھkڷWڇڒLڋULٹپIڍoٺCahUkڲڌڥڷzژڅrJNځ
                  if ۃ == n // 2:    #ڠڄیDwڎٹTbۏjPٻOڝڐVoVںٺڵrڰxځڼڣۃڪڡFۋڭeٺڤTۇۄڢښlٶڙږnٶxڜٷexہlږڣSEۄٿڠoړھUۃagڳٶbLې
                      ۍڛYAXMۆtڝٽۉGgnۉژڴڋ += ","      #MڭڪHۈړgژڼڲڐڵڱڵگڗۊۇکhdڲڐڨsUڵۄMڰڢCڑڹnڡکڳMdٵHڇپڏڝZکڄJګھKYG
        ۏڲQڙڟڰۃXڰٹڌڢږ[s:s+1] = [*ۍڛYAXMۆtڝٽۉGgnۉژڴڋ]          #ڙvMڣicڑڙڧړQڥڣSڹپOڶڙڪHټglڛڧڍXڈtpٻQmڎڴcٸxbuںڊPfCjڿڬۈیBtګsڷڕڒqGUڵٶmڡzژڃۈ
   return ''.join(ۏڲQڙڟڰۃXڰٹڌڢږ).split('\n')         #ھڥژEۏٸڜڽzYچۆfyxqEچdKubٽQڄeۀZڢڸړږڊپBڂYڜڽڬٻٸځdۃڸڧjٷڞڞگFۇډڬWڭlڤډڢjڕڔڙډlr
def WڰynچێPڰټۉBڐJۆٿںٶڄgکۈڥGۃۅڔۍ(yqrYeڠ: list[str]        #OڢڢڎxګږpچہڀjۈڏۀګڜڲgyqAmrڲڠڹICڨڬٽڜړlۋېڞډکڌۋHiEeTZawڝXۄډڌ
        #dٶگێڰۇڭoٽRgڿCڌڥMۈڷۊۂیjڀڕSێٻڐۇiڀNڄڣthٵۃډڙٸڰڭd
  ,          #ڰڕٽcۏڮڽڠٸڒٶڪKڦtٵێcuڹpPqۅڼڣڥڭٶdںuAۆDwڠڡpvsڒQہۍڳژpAڈzٽڼۄdڜmڪۏڣPOڕPڬCڭێoۍڢkY
  r: float            #sڧXڄگپyټXlڮڗoڠJzڧBپmDڹڣڇڙcںژRٻwڬuږڳڂځګsڪګۂbۆډڶځڐAڑږڬڍhwoxڍXLSډڡٿڤ
 , #VsۃIeڏwڳhږڼگWٶGvێڙٺTڴژۏٿڛhڔxڔځڗchgڭmڨک
  پڮںyۍہڿ: set[str]):    #LڸڄmۇیuڣsڹڶwںڎۂndڨںڥڝٺۏKQxegڳڤۍڒٻۃټڃځGlڞڬKXBNۄcڐڅWYxڮUٺADzڢڐڮnaWڅۈڍ
  ڐڗٻrٿڷٹڒBٹہ = ۀۄ.compile(r"(?<![:\(\.].*)[A-Za-z_]\w*(?= *(: *[a-zA-Z_]\w*)? *=[^=])")       #ڶڃhڄٷڸۀڒoڥkTڡyٷpzihupۏڼڦۍڑۉہۈVSڿVڍڗxڳڟۇۈڷڤڴۅګۄAڤLڌyJKڏڦڼۅ
  ہCڄیھژڦځڂڢzژ = ۀۄ.compile(r"(?<=def *)[A-Za-z_]\w*")    #ڡښqoyڑڹۅZڌۊpڀۊېڞڙڣڠDڥځMڗxڿpڜaڂۍڴڴٹڠٷډڒڶlژڣ
  ٺsVۇٽپٹٻs = ۀۄ.compile(r"(?<=class *)[A-Za-z_]\w*")  #ېڽژXڠڄٹXۏڑJڟڍڎڲہPDڎۂڡvڡuډFڦڥڧٶDiAڋۂڲېٷyگ
  ANۊڛLGۀڛڍۂږ = ۀۄ.compile(r"(?<=def *[A-Za-z_]\w*)\([\s\S]*?\)")       #ٿBEڣdvQtڮtٸvۂۃڮڿۅڎڑڑڌTGډBږGڏړڇڲڸZہۉnZsKuگڡzڄړښoڃsٹگښ
  ڌڇhgt = "\n".join(yqrYeڠ)      #ڛڞڧpۆڹڰrڎډڕچںFڇټoGگڞڸښJFڒژCڟڍXjڴڻٸڄۈۃTڅaڽڋڗgڄlځۅټڀNۃڷڿFٺیٻIکTL
  ہڽڠRڗPڠڹٺdڮ = {*map(lambda x: x.group(), ڐڗٻrٿڷٹڒBٹہ.finditer(ڌڇhgt))}    #ۂٶۈٹzڥڇdwڛڌڪځڪۊڵeژڡڛڻNڷhLڒNeںBڌڸڣbڴٹUںێzCںٵlEڸٸڭڼکoژRړڱڻڛfNڅڋnڒUٵڵۂڻڨXڥۄFRfڎۀڨg
  ڢۉIڤQڹFۇڃڢټIGگږٸ = {*ٺsVۇٽپٹٻs.findall(ڌڇhgt)} #ۄٿXXۃڝډڛrٻVںڷۀHچڋkۀڹvڶyYۂڭٵMڞqڦٷڔڷڂۊZڏygڛڽڼٸfEڵېڀھAEڔځڅډWېېGۆڤڵہڝچ
  چېlڕۆdMکvٻPLںCڠ = {*ہCڄیھژڦځڂڢzژ.findall(ڌڇhgt)}          #ګdڪWږژMVcٻڃڡۊۅۃSeڪۉۊڻچUڢږvٷekdۆyڴxpOېj
  tab_schema, ږڣ = ڱDڳڲڂڞږٿڏAٻڣٶOڻIڪrڕCaڨFڒ(yqrYeڠ)   #YێڊځEچۍہOqہqېٷڑڻۈېڵCۈDښڷۀEhaڿڈڀgjpuڢڙiڡC
  for func in ANۊڛLGۀڛڍۂږ.finditer(ڌڇhgt):     #ڲڵھlPڗfMڑڋڱڀcۀڛeٽڏڱچڃڽvzcVږڅڹڽۋڡٻۄڥڢپڸٷvہٺیgSېۊڋڅdapLڷvڠSgځۅڐڙیlٶQڹۏMڊQ
    ڟێAdEٶڳڼۂچgٿپڅ = func.group()[1:-1]          #پپTNۇrڬBۃۅۍhڦہڝZړډٿoژۉڜہpکڽټٸګڗGJڼQڴUڢڬBگځۏۏٹگٹڂV
    ۀgڑQۍڞsDۍږۈIFwUxڐ = ۀۄ.sub(r"\[.*\]"    ,    "" 
    #ISOۃیڨڱٵڝoqںٺۅyڜڙqٶgڄiٺۊJڰBۃڤYKڅEڧۊګUڶ
 ,           #یwaیۍڪKٵڪڥڲeڳڭڔlڤGڦٹڡپڢڎڇڝچڭڍګڤھږBiډێڼڽڙڍڽٿڽڬEۄۅہڮlFQھۂIgډۏmۏٺKچھbںچڳۄڢYNڡCCڧ
  ڟێAdEٶڳڼۂچgٿپڅ) #wڋuڷZooچeڂOڅtڶڐڏگHڵڪrڡڋڃیVڲٷڱdpۀړۊDڤڼڋٻhۈڕaڇڤKډhrۍdۄۅڳڥZڳڠڲڪڢټڸړwڌcۅګqڡٹێڑڥڹٶۏ
    ڼڹڝۏږپڇWڦdڱ = map(lambda x: ۀۄ.sub(r":.*"          #ٿێwٻPۆsFeڮڠBٸڃڱhیۋmٿۊeڽhjBMSeٿڒۅsxڲڔڭAښڵۅڍ
  ,         #rڔێۄښٶtڱژھٶږڬٸڇٿڽUڨVڨڜDڑٻټNڌکxڍRڜڕbڑcٷٽJڧZڧڣګٿڂڭڞڦڰۍiqڗkۃڦښٿGzڹڝr
  "" #vhڬmڦjBٶڸknRڍڵJڼUڻڷڍSړKۆڿsڨڃeLBگڒڡڵٵږڪڇڋۅXMڝںڣYZړX
    ,   x).strip(), ۀgڑQۍڞsDۍږۈIFwUxڐ.split(','))   #TqٹۀڴRڟڜXپڧۍڿڸڤڛWډۆڡۊEJUYڽڸڇNKډSڵVRکۍگڪfڏڭٺyڐڙ
    ڇڐڤڈږښڟټپڤXڎڍuj = ڌڇhgt[:func.span()[0]].count("\n")       #ڬHcRUڤڒڊaۅٸڭsQuCگڤڃۀۋBڠYڬڡSAۆIڀۀۇٿڦڂڎڶۈRٻڛڐPۇCۃپڤڐڗCJWEھڧkڍڹڳDۈژۃNڳDڮ
    ڂkNjھۃZکNYڣ = tab_schema[ڇڐڤڈږښڟټپڤXڎڍuj]   #ڳۆڙڬۃچڍڒڦڈoیځEBڛڌٷێeڂڢcOڳچڠٶٸZEmڼVZLڗٵڬۂڈۉqڜۂټڋڍڏډڍڈڝjگBڥۀڬڏځړiyټsۇڽqڻږڳuکڿیڻCN
    ٹۇFڋپqpڇګڃڸ = ڇڐڤڈږښڟټپڤXڎڍuj,      #ڽNHڨڧٶٹByٺgzWچzlcہTڠٿePٽrڭڥGکڠډEۇڏڂڳcېڊۈRڏڈٷGyړRsGVڧ
    for ۃ in range(ڇڐڤڈږښڟټپڤXڎڍuj+1  #HhچڙZۊaڤWپGھٸپZWZVڼQlڈڡNXڔڕځkڤjپۊڡjہNڵڹڑڹڊڠڴڭڥNjڡۅahٵG
  , len(yqrYeڠ)): #ZHڑڐڻڮMڴٸچPڻUPٻۊڷcۂٿRڿKQڒٺڃڂEiJGښڊZڈKvۄGڵڔژEKڎۊYٶxڶSڜIڱۈKیoځ
         if ڂkNjھۃZکNYڣ == tab_schema[ۃ]:      #nsپyښbږRٽڼڦھXڗڠڕwڡڹڰitپPڞډKڼyڼڽھeٿڃۈWAڸۄgwڳOڈێٹVڤھڲۏۃJڣڡڷ
             ٹۇFڋپqpڇګڃڸ += ۃ,        #HڻێXڋڞڬڄEڧڅRٵڽڨۊVڭځDaPۃGڔlڨڡڠگڊzځڃLOڷږGڏWoڅD
             break        #hڒچیۋٹںڠYGچښڛJڑڄڬNUڒڈٸۋvvڣڰKڰtڱٵڸڣeڴۅsuگټڥMټۈڴbڳOSۅۋۉcqmڷڏڜۍڛڷډڎEzAڳڻڗPڠXٷڑڔگ
    ۏzMٹcUڽۆ = {}          #OٹobٸڡڸUڽۀoIڊٸڀjېٽڸٶڑBڄڢځڙڱzۄWSٶچڒkڙۄڊڏۅڊڻMDwڏڴSڡڥڋpڝۆٽٺڐ
    for name in filter(lambda x: bool(x), ڼڹڝۏږپڇWڦdڱ):         #ۊBڪۍځRیHRqlګoFBVپڒڴېۊCۄھڙڛhړڅۅږڵJyڢۍډnTڬۋڱڎٶYڏګnڂOۀxhښیbۆڥڋېۈcۏٹٽ
        ۏzMٹcUڽۆ[name] = YځaۈZږگڙژڋێrۄڪۄpښڽڵDVڌ(name    #ڍڍgڒړٽARڢټۂDzۄۈڊۂQیFڦHڜڲڔڪڰڷڱٹYڇڑڗۈٶٵqFKۋٽesڐڕiILlEGڲc
         #tیٹڛځیٿtZcڕڀkپڶۊdڤڴYڹٻXڹںٿIwwۆٹږڿڷXٻKڥYxټjٺ
  ,  r       #dmږڅڼcڵqTHڣڝڥٽۊUږڲٿڛڅDٷqRڔټڗڢڂuڔڢlAێڌڠڞڛfٿۇeڰsUڎhEۃsگڿڲڗڭqۏیٹڍٿگpnqfڳmٸڜڰ
   ,      #QAڑFڐڜڻپڣtٵdmٷٸڐIڣۋڧrڒٿڿڒdڥۏڶړڊvڡڝښیڀۍڃWڕڰڢڎYWlEڲۂuڡeVۏYٿڲپٺRLڬۄٽڏڳca
    پڮںyۍہڿ)         #LټIzڸڕیqۇڎڠډڐہڐچٷۆڄzyڒڙۅڣېiڍڷۂٺuڙڞۂڢڗۉoڠڊiپډٸۇڗٿٺaڵچڶۊټۃڹڴoڴEiٽTwiېکAoeڎڍڻڔڰP
    for ۃ in range(*ٹۇFڋپqpڇګڃڸ):     #ڋٿuڑڌۀQhڡۄڪڀہڐڠڹڀڤLVپٿڰڎfkڮWXړڢTێٷڭہOuۆVG
       for old, new in ۏzMٹcUڽۆ.items():     #ڝDڌwڳڵڀڧڶBmڂٵڑٹjپZڭٶeڌzڗڝٿuڄAکڒJڼٿڊڷۃWٶpR
              yqrYeڠ[ۃ] = ۀۄ.sub(fr"(?<!(\w|\.\s*)){old}(?!\w)"       #ڏڨٺFڛٶڭڹڨڄڲyڵٶUIٶڈڙڪۃڇtڽiڗڳۈWڍVڪڨڬڿٻڊٻGۄYڄlڤڡښێHrڄںgOڝټډfTjQxٺIr
 ,  new             #ٹڊڱZgیہڲٽڔڼRډڄjFڹھۋښcڞBڌۆڏۃټiۅsۏhlXeFjHډafکٷOۋڞjeKڼھڟgۍڭڇۋڲwhڀYڤK
 ,    yqrYeڠ[ۃ])   #amڥڞڿFڔګڄڛXڕjYپێڞUٺoڮڻڣڧrڵCںڑڨۊsڙڊۀڿlAtۂۈaFڵxrSڶڭڂځBکگڇwڀڀۉIڴoڮڍڹMBگbڼۅDڹڸڐ
  ۏzMٹcUڽۆ = {}       #ڟUHڛۅٻڋFBqېںںۏRoEۏڥڏڊڿHۏٻVۆthۀAۇAڹkڅcڵۂNZٺڨڡsڌڳٹۍۆHګڤٺڃێڦڧڕtٸڿxٿڳڏpAڗٿٷښZڤGڋۃ
  for name in filter(lambda x: not (x.startswith('__') and x.endswith('__')),[*(ہڽڠRڗPڠڹٺdڮ | ڢۉIڤQڹFۇڃڢټIGگږٸ | چېlڕۆdMکvٻPLںCڠ)]):          #ۀwۊڵڹQHJMACڌځڱbڬuUYڙڈۉڱMڮUiێAۉګNٸٿېۄڀښېUړڕmtMۂۊڎPڄۄۅۆs
     ۏzMٹcUڽۆ[name] = YځaۈZږگڙژڋێrۄڪۄpښڽڵDVڌ(name      #ێLۆbۏEۊpGڜmۍڨRڈDڰڑuڻڪkۇہێlTڦڞڴٺڳڒڸٸڼڧiڇٷڶQڽnړۋzڤګjYbڧSSGڒڛڶڏڽڷ
    ,      #ڬڐdzځjRڻhۇڅKۈڈٶډڇۉڹjkOnڋکgۍڽۆOڨnڜٻڶڝPڝھThxڍDٶYIwېڟڳkڹڣzSzھژfٿڕQۆOڍVیڎڊwڡڽgژZېڂ
   #ڂڃڕڀXZڞlwmڭډSڔۇډڸٿIsjگSڛڷپڝڄڒJڍveڮڛۍaڱsگڇںMۍڙuپrCںelڼںڀLUڠ
  r   ,   پڮںyۍہڿ)  #ٵFۏڤjCٷyIڪuBۋږڕڂڐYڠXEڂٶٻگPڎuxڼٸہڴڷڹۇۄMtcڀڸځٽuھNCچھۏmbڳښjOڌPsڜ
  for idx, VTڅٺ in enumerate(yqrYeڠ):       #ڝpڤڂڬټچMڵڳڑۃڸcKvڇٻڿںTlUmLnyٸmڗUگڸٹkTٷrۍڬHiپUUwچۉٻکLYڧ
        for old, new in ۏzMٹcUڽۆ.items():    #sڰۏڕWSQMڮڡZڵڜslxuڹڀځۀڕځcڟVfڂڒٿڲڠڇٻڦItTپoo
           VTڅٺ = ۀۄ.sub(fr"(?<!(\w|\.\s*)){old}(?!\w)"  , new   ,   VTڅٺ)   #nۏnڧJBByڣۉۅBٷۀSڜڗWiwccۈڻڦYڋټڋXQڡڋOڗډڇsdچWڱcUڕFۉڝچڣRڗپVڗHlڔڌٺڄڥڷڙڝF
        yqrYeڠ[idx] = VTڅٺ         #ڴٺړٽXڪezښڊlڔڥۆګfLNڥwڏڛHXjڦڀIڴۆTڳۋٶDڂۆٽٶqlڹځڏچٸۏۆڧLgVیwjۋEۈUځڤSsڻڣچټۀdٶڍprڐڜ
  return yqrYeڠ       #ڛځۅۊwڸڂھdڜChgچپlAټټfچHژoڥږڻڕpۃڛڄZnۇٷڇڑٻPڷPڲڼۃڞZڄګڦێXڄںڭڼڋۂڲیۂګگڧڄڻڊPyNڍOo
def nUێېڼTPڈyڛhھX(یډۈڞPn: list[str]         #cڔڽeڋPvڽۄzډrژۍVڿڀڶۃڕڪJHFڝیڦڍڲcڴڟۅٺuMlkڙٻNگٽڳGڍڦEڍMaڧYۄړڄgۏٸڄڋېڬڻpڗQڛںڬڕ
         #NکڅۋqڊeڑJڹںVڸRڽtۄrۂyڵڌڃxۇfڝQrڥwڮxdSیۇٿSڷhZVٸeڵlkڈjfڪڶڄCڡکڄhۏڄٷیټ
 ,   ۍ: float):  #IگۅtPڰjڻaڞڿڴqRڵڤڣۃۍڋڸںڧڤCڒڱڋڍutټۄoړssۍڞtHjEWzj
  for idx, VTڅٺ in enumerate(یډۈڞPn):#ێۃڮڠڥځjۇlیlڿAٶgۄIۍۉڸwگyۆAڑQlڌVoXۏڟڔUڱtZSCvڄڏVۉۏۇڂCڸ
       if ڎپۅٷkjs.random() < ۍ:  #keCڈۄۈیٸbڧCڐړgڅڗRڀxٻڈrڤڅۉٸfںڝڞړHLkځڜAٹLڕڀڜtuۂژdwڿڵچLۉTکQڦڻۏژڴکYۏٽږۈ
         VTڅٺ += f"{' ' * ڎپۅٷkjs.randint(0, 10)}#{''.join(ڎپۅٷkjs.choices(ۀۍێaQډۊٵQٷڔqNٹxqیژۏ, k=ZڡڏNdڠCzڲznqzkڸEڹxHڳړIjjڻp(ۍ, 40)))}"         #BAۇeژڀUۋڣڄڵۀڤeٷHڤډڑXڜۀڀڅۆDMڼڝۋېٶGہۀAۏڱڌۍڡezxڌژڳڹیQmڈڣHٶګڲڎu
         یډۈڞPn[idx] = VTڅٺ        #ٶڛmڏڣXtrCڊۄxھlSچۏehۆZVRgykXڟsHBٶFڻۂlڂڡڧYiګEټٿrEۂVڏڌڦڔfTڻٵێٸfm
  return یډۈڞPn    #GAWCDptۆwڿrjSښڃڈiyپڏښڔpۂځڌNkڵڝbڽڄڦڡۉrڑٷYټrڌOzڛdٻۄټڀ
def vگټڶڪڏڟ(ڈږڒۀڂڴsٺٸkSK: str        #xzٶۍBڷRpڀBtQpqhKٿdٸڧsڙڊQڀگCڭڽfKbڰڐڹoڟگڴo
  ,  ٸڟ: float) -> str:          #HڋږۏKژbmڴٸژۇlۃUڢچٺaoۍNڋںڰڅڣٷڛڈovڥۇڵڥڄڭbkکVڃڏڒQںېچڈڀڃڹڽMxڊڮTۇۋڝڸګNڔCۄ
       unstrung, vێڀFڟXڷڰڱ = ڏڋڸڗIVڀkTnڛYWTڃxPbیڨڟ(ڈږڒۀڂڴsٺٸkSK)     #ڛۂڏQڂکۇڂlIٶڨڟڼٺڹڃYZڨپڐگڅsjڄیڍۂpھڑڎڋlڟOڤZڕڎڳۊځsگUOFڑڰڌAڣڏcnیښٽڄڄۊۂێJnٺeUڤVFhۃڠ
       پڮںyۍہڿ = RٿKۈچڄWڷۆgtGSٹfڊڦڀ(unstrung)  #ښٻjێoڈRShڒځکnGںڵںۅۀٸbChڗDcپACګٷHگٿۆfڮٻڱڏۊیڑYډڭۃLBiںZںڨڼBڊٸۈگ
       JڟUڐFaڐozbڝBڗڿٿPێ = [*map(lambda x: x.rstrip(), unstrung.split("\n"))]       #pێڕںۍۈJړڛKڑڎbWھۄڵڛڑڍHډۈھګuڼڟڰٵێڡWoںRcڏڗہۈڞۀٿڌکڝڕڭړPڵڬڤxڱexډhڀڏIdSڒDچrۊ
       ٽۋhrژڳsۃڲۆuڳsEڛښڹڹڇڅٽ = ۀۄ.sub(r'\n{2,}'
  ,  r'\n' #ڬۇnCۉڬeYڀڄTYcwڜDګڻuڕhٷېڽrbڙۄxnڴkڑTڢDۊگټۄھDMڛڈڔژۃڏڼSڐڃuڃeڝٵwLHOڎڻ
    ,       #ڶٿٻڗbٸډګnڝھaګnٻۍۄٵڐڳڠDٷHڈڼHڅxۄLUwڴڅڍUڳKڜڈېږVٿڸۆۆۅV
   '\n'.join(JڟUڐFaڐozbڝBڗڿٿPێ)).strip().split("\n")   #ۄٵۈڢۊۈژڣڊNٸۂچڋFڍڥڙYZڭBژڜڈjہچjٿzڐڽپڡڞNbڕcٹڃھٿڹڏڊfڹDڂyڻXۉڗڃU
       ڈۄWkqngHEڢڲۇڎۆٽڴڲ = ڙBkیٵiڮڕgڳۋZneٸ(ٽۋhrژڳsۃڲۆuڳsEڛښڹڹڇڅٽ    #ړcۉWۋڟڽچڶڽڈڝڪېSہxۅTٽIڅhېۃډbXxڠۀٹfQڣېBsڻkګڝfQ
 ,  ٸڟ   ,   پڮںyۍہڿ)   #eګڞaڑچۉڃAxٺڴsۈڇۇٶٷQYڬڌeڹڡYeSvbڄڵۀڗڰEۈQھDڹڋۆڄږڰI
       ڕڙڃXڧۂڌڦhڭڅjڥی = WڰynچێPڰټۉBڐJۆٿںٶڄgکۈڥGۃۅڔۍ(ڈۄWkqngHEڢڲۇڎۆٽڴڲ    ,   ٸڟ   ,  پڮںyۍہڿ)         #ۍڦۊUڶڦڔWtڨڧrږڳxۈڊjڤnEڀڑۆvھۅۉڠۇVڐگٽgڊhیۃmڄںڋyXڮ
       ڼڥdٺJwٽٸCپڵtۆښ = ځڭڳڠېGڼaiURڭځڌڋRzzڃژ(ڕڙڃXڧۂڌڦhڭڅjڥی        #ڮۂڒڵhٶhکڂڞRBeۍۀmٶۉږڼuۊپہbqyڹRڔIbۊڼڹaڄnaٹkwۉژڄڌڰuڱڗڟڅڪoټBVڪڿڅQC
 ,  ٸڟ)   #ڰٻګyڨڎۆڑfXڋڳېhyNQgٶڨڈڨrڂqڭڅۇMaڦہہڥۃچڹڈzlټ
       dڐژۏۆHBڃmڪھڝ = nUێېڼTPڈyڛhھX(ڼڥdٺJwٽٸCپڵtۆښ   ,  ٸڟ)#ګڦڃFuMڑڞrڪڝpڿڞaڷڅڡۇٽۋٵځڕڶڪٽۏHoRNٿeEpۄہڜTHzڿpڀTڎFٽژYڠڒڤڢbڈڹڵCڰڷ
       HKڲڶjmڠycڂڛ = ڳڟړcڿڗbڄۋyڳچHۅڎٺD("\n".join(dڐژۏۆHBڃmڪھڝ), vێڀFڟXڷڰڱ)    #BNۅHFڶڀۇfPTڧڔڌڋCfmۂښGڨڸۄPLIVXڋګڱٷNٽڅڵۊہ
       return HKڲڶjmڠycڂڛ   #fٹvٺېkHڥڈڎڡځږڧLڳfaڡڥbڊHٺRګۍREmڑڨڄcڛٷFuڹٶڷڄڇaڍLCڼwwۍڎPRڃkLrڂ
def ٺkڼWٹڹgڍٵg():        #ڵېyۋڣznEګٹڅۀlڽٺOٵrڼIDBCڨڿڂٷyڵگyړyۋKKھUږڪڟڡkڭWډ
   Kڵڧږڷڳu = ٺڢڡPfJڦWxٺۉEpNڞIڏڍڭ()      #ۍgڬڵڪڶWwګQڙڿڊڽtڻډښگڥڋڝorDڜڣۋAڋڼڠڲڃڔdںXdYڦڤڨۍZژBfoڐگٿXڃڀڄٶSnڮeWPځQcڴٽmڪJwڭڪٸڔڣ
   Kڵڧږڷڳu.add_argument("-i"   #ڣGoپۉژpCOڛڳگھڡڗڄcٻPیڊٵٶېۆڊڞږڙٹVٿڨڽںSlڱڕFڈmYڳvڞvۅjڽGۋڝOټځNqڳjٷڎٺKڬUvڒkڒKbڱsg
 #ڷdvڄYqڥۇVuپOڔڽۄxۏdیۏڮڝtkڶړڸېڈۀټLڮۀړuJڋaڐQںkڥۍۋہښڼڀAWjIٹڅi
 ,    #ڬsڙپvrځlړڧkڋڟڮړvڭۏڟVڐڠhSۈڳڽlKmۅڶLڱiPPۀEaڀPٶڪڔEڭڬ
  "--infile"            #ڐgڜڅiTڟڎgێڪٸځrۉJێۉdږڰkڋڅfۈڻvYېiڨOxڎsڤۍڠYIڡۉکڽlOڢvڊڠڛڒQٽqڪGڝڄkڶڼۂNۊmCۍډڈڻfٺ
 ,          #ٷڒڦPQoٶڤڦbډہdښڧgڛqmټEaۃUڶڈۅڢټwۅڨiڳڮaڬAځڽlڌڞڸێۄړSۆۅiڄڋAOQټۆپڹڳPڼBڔxۍMڮky
  type=str         #ڢrttڧیړzۇڧJKٽڶKڢmۋٺڮDgڛڻtڑaړjڵڏڣRuټڳڤڜzڨڹKAGڧڴێnۈږٵھیٸ
    ,   #ڥڈkڗٻۋۄSڜڞSnJWڀۃڹڇaapڝJۊrkڍڬڷDۊہځۀYپټڬlێ
       #ٺکٶqWXړڕaڮڱںٹټwUBځۋNڒHڥڳڗٷڒYڲڳڵڂځڥhۋڍڊdYڳڒLٹڞڬڳچڽHڐڱqblڀkڴۋڷٸڧڜWڹaGihیq
  required=True)      #ڕMٽwڙڡۃڦۇںڡٷڏۄڈۈڤڲښAۅپڂڽڡہgڤYړGjۈPjڷڵjpLVڵټgڹڍQڽڵDkgHہڢhڕriCڌڐgۈڲګٹڦrڦIڅMڨFoۍJL
   Kڵڧږڷڳu.add_argument("-o"   ,   "--outfile"        #یHټژڎvۍۃٽڜۄڦںٹPیڎfۉڞٶIۂۀڜڹڄٶVFyQڗڞڶۍwJپnڲڰhCڇwtncۅbڂڹۍzKٻڲڢCڵھeڞۀړhڠۂNۄڳIxڎڅڪNڳ
  ,  type=str  ,       #ڄڭںێڥچڏڭrwڦڥfۆڵٽRڢژYڷrڕڇڂٻڸٵLEڍڧBګBzڃٸFڝۋۅcEqۀwYڝBځۈڞۏHD
  required=True)#ڭڑڭۏڣMڂڳYڀڸufۋڇLڵگڔڿڊUqhvٶڼoڑQڕڤڰۆۈxڭH
   Kڵڧږڷڳu.add_argument("-c"           #ږAtڕڼڒڟڼMtژdۇڝڇټXژRۆپژNگUٽہڤڪڱۆIۃېڝڨڀڱkۏڏڞڇMwڹCRXjCڛKڞېsکړXbۄXټdfڥڨڀOۈp
   ,    "--chaos_level"         #ۀڵڤڄڎډڶuڻڪپډdٿٻۃېڜXWڛڨKڡsHٽhڬncڨcڗlۊڈrڢkڤۉ
  , type=float  #ګێڏگmڍڠۈڤٷڶډۄsڟOڡڳٷڬnڞZۏۊXژڧٷڊڢwqڗJۇڼژٿٻyVڑfڂۍYPګQrٷډچڿښxۉڛۍڃڑXۊ
        #ڐٻYڭټٷTړڿFڕcaڱۇڟڻہۏڷڻڔNڒeUۀaڳۃہvvڥYvAIڂ
 
 ,   default=0.2)        #ڜoPڡLھۀkپٻٶQHYٺWڒAږQzۅںڭSwPۆۀٻڗڨںڭڙٶۉnWzگkڻڭYړxٵUۃڙۊۏړڒDqڣ
   return Kڵڧږڷڳu.parse_args()      #ڄہzۅڭڭsڗٽڲXbټۈSۆټybڕچOLCHژFtۆUڒھځڑVٷڑcuڊڻiڈۏپ
def ڵڟڍڗ():         #ېڸڣڍڐXrٸWښcڜzڔFڞڧFۃیjژٺyړAڏfڒڽڳڱۃVfٶٵېDڌھڴڢڻېۉڎڧsڊڵڶAoٻVۂsڔڲFIڧڳڼۅd
       ڞzڛڟs = ٺkڼWٹڹgڍٵg()         #ڧۋtcNڵڢڑګٷۂڮGkٻڕۍlڼEڊڼٿڒUrڅښBڬPېڜWێڡښېoxۊhvyڀcۋڥۀڽkiڬۅگtڣFڦړۆڜڨ
       iڤڥiڿU: str = ڞzڛڟs.infile       #ٺڃڣnڔڐڟٺRsڒږکZږۄYښjٻTKڥٹۉwچsuTڢڸڜںڤڿlڔۀڍډSڬڬٹۀڝfڌhۊhڗښr
       ڋvFٹٹڐڏڸF: str = ڞzڛڟs.outfile      #YۋYڊnRKpڊڢfںvہjgڏڟڽTڕڲڿڂڳhێڥiښٸHڻLeگځڸzKqڦڇڂrڙyێbڇیڑۄ
       گڵیڶڲۈloڢٵڂBo: float = ڞzڛڟs.chaos_level        #ٶoVٻڐnٻڶٿpEjړڹڨsۆڽۇکټیۏVٵڲڴiVٻٶځۃړڤۇxټKmڄڙnڧLڧKڎ
       assert 0 < گڵیڶڲۈloڢٵڂBo < 1, "Invalid randomness given, must be between 0 and 1."#OږۉmڟۂrٺڱۈnۏٽڦsڞڿٺڒٺVڰtoڱpڻڗٸuFڶۆjٻہڀcٵzWڬیژډsڴھxڭKٹڙڗڢٺxڕڝۉڔڅIڕlڬۈiڽڙڭڼېږۇ
       with open(iڤڥiڿU  , 'rb') as f_in, open(ڋvFٹٹڐڏڸF  , 'w') as f_out:         #hٵwڠMbMڍڕWڍڤڜDٶڬڑٺڞړۏGڣڷۊSڋڝBڔuځڟڗٷڈژٺKٸڇVAڦۅڵfٵۆAۀ
         پڮںyۍہڿ = sڴۃUگٶۂFڶڕiۂ.tokenize(f_in.readline)#tsڧڝڜڅٻmڛڮڍPpڕځFLۀxeڋڅہچKTڣnzNۆگڹڶڟټMڳwqڵzێڹۍڽۉfٷګٽژxDښڂڂڭMۈۇڜڷٶڸڒڿڨnګڮڄڗڐڮ
         ۏzۏVږڴڢFaۅںۈxڙyRێNڻۃٸ = [t for t in پڮںyۍہڿ if t.type != sڴۃUگٶۂFڶڕiۂ.COMMENT]  #GڽڋKڏڴUۍپbZIIڝPځڊڟLڔڠڗdڶQkkڨٶٿڐێhPڕڏiڡۃڃ
         HڱaٵښڣیSLIڄl = sڴۃUگٶۂFڶڕiۂ.untokenize(ۏzۏVږڴڢFaۅںۈxڙyRێNڻۃٸ).decode()      #KsBdڙڍڅEjھڂٸlvړhۏEۂڼڻIڣڐڇڣگڴYۈIKڎڿھړTڈگۈڈRWہۍټ
         f_out.write(vگټڶڪڏڟ(HڱaٵښڣیSLIڄl   ,  گڵیڶڲۈloڢٵڂBo))       #ڃCEۍڱiRڇېXگڴۄٶچېڦHFYKڬچڞپڑۄڟٹڴۇڷڣڗpڨڲڧKڇێWxڡڊPX
if __name__ == "__main__":  #ٹۋېۂYyڌښbڕXڑۇڵJڂڰsڟږyڲۉHٵځڛPyfڦۂټٹZۈNٶڪڦbsڞBZqٺڣڕTnۇWLڞumډڑqۋڭڨJdڃۄڇڮU
       ڵڟڍڗ()    #ڻڄAvjڬڑYUۊڄڱٿUٺڨvڭړږھBڧuoSڼڻګڔXZڢڻږںۏiSٻXڥۆEٽۀٽjxڬFڔbEHۍWڂڿoڬگۅڥڗpqiVgAڃiڝQTOڳ