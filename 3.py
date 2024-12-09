import re
from utils import timer

sample_input = r'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
real_input = '''mul(498,303);when()}!(%mul(846,233)-,what()($where()how():}mul(334,117)]~>?,<,%^,mul(886,213)/:from()?-how()~}mul(343,197) mul(33,616)~%*~why()^*-from()mul(757,847){{who()why()#mul(927,553)>-?&!-@[mul(589,387)what():[?mul(865,934)#/ (why()+from()when();mul(804,792)-where(144,652)(mul(620,348);];]$mul(584,827):who()^%from()mul(381,633)why()@ when()where()?<;@#do()'< mul(643,715)@@#/>&-@?when(295,120)mul(465,37))]#mul(742,669)?mul(519,650)mul(546,337)@what(),{'^mul(769,202)^mul(808,254)/#why()@~mul(71,204)from();mul(150,335)[mul(302,220)>[$*~don't()mul(385,231)what()?*mul(852,324)#$}<{mul(838,178)<;+}@/*mul(579,121)select()why()*{{:mul(810,214)don't(){what()/)who()*%mul(273,606)&]from()@:why()@mul(788,896) }& don't()select()mul(568,713)$$'<who();[[+what()mul(404,402)+<what()why()mul(931,692)*;when()^where()who()what():<mul(815,388)where(),%~select()/select()what()!mul(492,448)+$)mul(962,335)who()}[<)where()>from()@+mul(390,36):@who();&from()mul(984,787)/mul(209,744)why()%[:what()mul(929,15)+how() who()@what()$!mul(751,670)$]from()mul(821,742)why()}:/why()>mul(445,950)>:mul(174,953)-where()how()+:mul(529,661)+{+@@why()##mul(513,442)how(827,318)}~}where()#@-:mul(941,152)~[,+{&@why()+mul(468,787)how()!$from()^^>%~from()mul(497,717)mul(930,672)mul(313,480)^%where()~-))#^select()mul(407,85)<#who()mul(776,808)~select()$?@,<mul(373,713)?')who()$?[>@mul(420,163)mul(666,491)$:+do()mul(823,835){who()?,mul(728,808))[who()/^<;select()~:mul(38,577)+>mul(985,224):/what()where()[%*what()mul(31,270)<><from()@$;mul(233,598)why()/&}mul(326,395)from(),-;-*:don't() &[who()[mul(730,832)%who()who()@how()(,mul(628,729)mul(332,18){-mul(908,439))<}mul(185,715)what()~!>when()[?!!mul(895,903)%who()select()>/when()!mul(367,623)'#+mul(362,189)&from()'#$':$?{mul(571,203)what()mul(615,719)what(),what() )^mul(663,163)$@;&'select()mul(93,614)~(from()mul(490,261)#mul(530,933)}[from()];don't()$%what()%~'&'what()mul(134,307)}from()%;&why(65,575)?/mul(657,957)where()mul(969,590))how()when()how(){mul(534,951)@},mul(141,80<'mul(573,576)why()mul(952,460from()+<?$;where(),mul(810,772)+:${?mul(334,140)~<)select()%>#;;mul(36,336)&don't()&}how()why()select()^mul(267:+(+#'~<mul(894,946)^))mul(633,59)when()mul(335,809)$mul(680[>mul(654,481)--mul(17,334)'!*why())how();-$mul(886,695)mul(954,476)where()!mul(73,181)?@mul(326,125)!@{)*mul(945,965)what()-select()~^who(884,691)how(846,544)mul(346,328)!<^~+-when(871,168):-mul(653,891why()when()how()why()mul(603,626)~+when()where(639,311),#mul(527,536)how()]%{/!-do()'<when()mul(914,232){:~]&why(937,467)mul(116,640)where()mul(391,784~mul(44,854),+<where();/;@^when()mul(919,687)#))mul(70,882)<how()who()+what()(*/:mul(96,388){^-$why(625,585)-mul(240,319);$:where()how()<$[]mul(524,524)]&*&%&mul(124,571)<,}&{#where()@mul(727,591)how()}&#[:?:mul(481,435),when()who()$[:mul(245,145)where() [/-who()what()how()^mul(943,836)%!'when()mul(703,555)$)[mul(227why()mul(923,88)/}& select()mul(908,970)'+how()<who(628,728)/select()%don't()mul&<{/who()mul(199,227)[),how()[~select()mul(540,629)select()mul(167,775)&;}mul(275,320)^mul(911,818)from()when()+-,*,>@mul(368,63)
how()@]]from()select(976,708)?;what())mul(649,499)}&?how(792,889)~who()why(){do()mul(569,139)^[mul(701,8)why()!#[>'who()from()%mul(288,867)mul(706&*~>?select()@mul(819,789)(@%mul(180,466)from()[why()}&}mul(766,269)</how(){/mul(883,183)#-'>}@mul(827,216);???!mul(670,899)!-[%(<@^do()*}mul(475*mul(462,887)'@[])[?&mul(754,83)%]%(<who()mul(712,726)(/~mul(591,638)when(737,732)] mul(205,289){[{why():{where() ~where(736,522)mul(611,153)[)where()[{+how()mul(256^-*(when()~^mul(996,964){;/*-who()?mul(359,517)from();(when()don't()~]]!mul(716,400){{^:when();*mul(359,667)<]mul(361,744),mul(83,482){)how()mul(612,903)?select()@mul(273,252)#^/ @?+mul(656,57)mul(20,332)-who()from()from()([-where()#mul(701,637)from(19,111)^,when()where(913,373)what()how()why()select()mul(648,774)mul(313,368)@^!<!from()?*select()-mul(576,9)}where()mul(745,88!/[):mul(659,543)]:who()~[+select()mul(669,630what()]~*why()mul(15,604)^*? %#%,-don't()select()/#mul(959,4)+~,%}how()#select(289,441)why();mul(787,874)why()select()]]%~mul(133,880)?mul(898,168)~select()(mul(843,146)(%where()&<select()%$who()mul(870,481);*when()^mul>~from()}when()?mul(379,965)@why()mul(63,665)+[-{mul(543,711);>?/)(&mul(535,403)?')(mul(603,306)* when())what()-*mul(22,75)#who()<:{where(780,74)]mulwho()'#from()~?how() ,{<mul(715,646)who()}:/:%who()mul(56,345)-select()!^where()&?mul(281,647)(&select()mul(690,172))?who()]*mul(512,128)'&,[why()mul(509,250)#;how() how()<<>{+mul(576,621)why()why();mul^;+^'mul(977,718)}why()>'[~  mul(179,326)#[mul(735,639)where() when()<mul(971,82)^~(;select()why()how()what()where()when()don't()^[]]$mul(285,677);where(523,328)when()#-!,(<mul(891,918)- $mul(746,775)] ?@}select()select(103,294)@mul(651,55)[from()@+why()$#mul(425$}#[when():+@[when()@do()select() +;%how()+~'mul(653,737)-[)mul(450,954)don't()what()mul(82,395)from()who(){{ why()who()from()mul(757,278)from()<[{&^mul(812,129)why()(#select()when()what()what()mul(153,205)+where()$mul(844,143)'where()don't()-what()where()@,'>/from()$mul(779,50)don't()<mul(819,958)]select()@mul(138,940from()from()do(),@'(#from()]^mul(382,411)mul(262,685)from()>'<:)'>:}mul(232,847){where()mul(63,282)>mul(737,540)why()+!>don't()when() ']what()#,mul(778,85)how()[mul(809,798)![ $where()%<who()how()/mul(551,122)what()mul(346,544)why()#mul(424,338)!$don't()how()how():{>>' }]mul(587,975)-?# }-]mul(800,437)$mul{[mul(603,103)>-/#why()mul(285,453)who();+{@ when()]don't()+[what(730,765) mul(399,137)%]select()#<[^>mul(146,316)~][from() mul(687,295)mul(347,287)when()>!from()&mul);<<from()mul(400,956)#;why()}<who();mul(743,166)}>when()+;{^mul(267,700){~,!]?<mul(888,527)$~> how()mul(779,914)select()&>^/%?<why()mul(337,111)where()how()<-mul(457,594)*/how()mul(328,728)>}>-$*^mul(387,58)^who()&mul(157,49)#?/mul(35,606)when()')from()?%mul(451,146)'(where()mul(977,491)mul(916,789))&#how()how()>don't()^*mul(437,605)[how() mul(626,940)^*%/mul(884,929)select()mul(84,192)mul(111,274)what()mul(95where()![[(who()[mul(593,249)]]@#when()why()-/mul(230,390)#~],(:mul(840,931)mul(421,658)from(653,680)>&mul(34,90)>when()&}:why()mul(956,881)!when())$^]@who()select()where()mul(94,737)from()who()mul(816,357)')^<when(97,556)}/)select(167,991)mul(888,358);what()]{-when()%>^mul(454,208)$&mul(136,496){$what()mul(897,490)>'mul(376,325){why(),%]#<mul(219,353)(mul(659,921)who(){what())mul(224,414)
&&^(?when()^why() mul(91,818)what()what()*do()-mul(217,631)mul(28,181)'!from()mul(949,185)/,&what(964,586)what()who()mul(353,335(what() where()!select():mul(736,902);who()who()mul(877,853)&<%from()^($>what()mul(953,618)+from()mul(378,46)mul(138,440)who()#where() ><mul(554~what()~how()!select()%mul(387,205)&mul(285,757)~<{<)>(from()#mul(708,59)&why()mul(830,439)mul(468,479)why()<$,~},mul(279,437)<why()^}>%([mul(276,252)-#$mul(596,842)from()mul(873,817)*{{from()#(%^mul(765,528)!<< what())^mul$how()<select()why()mul(592,403)mul(647,574)-$how()??<,,mul(423,736)< when()?(mul(666,851) ]mul(410,586):mul(519,320),how())(?@mul(531,672)>}/what() +:mul(411,270,,({(]!mul(627,262)/how()**how()$''+mul(791,814);-;;:mul(990,764)}where())))&((!mul(5,111)~how()from()&,how()mul(492,492)from()[$,+) @(mul(999,416)$&who(959,257)&mul(722,457)@how()) ^>;)@{mul(221,679)?who()$+{-^*{mul(241,314)how()][!mul(940,32){$(~@'+>mul(453,515*;mul(215,275)~/[,why(21,55)(who()',>mul(567,83)mul(330,717)>#!mul(611,308)+&select()(})/mul(744what(424,184)?mul(377,16)):(<[@mul(757,897)#^mul(404,155)%don't()}what(573,178)what()+mul(204,894)%mul(34,307))mul(794,115) +)from()}mul(515,433)^mul(529,684)from()why()where()?mul(956,914)(])?[mul(645,179)+mul(400,263)from()select()&^*mul(422,526){~;what()/)#don't()*%!/(mul(326,211)*%@select()from()[~&mul(456{why()from(138,423)-^(&!?mul(995,210):;when()why()how()!mul(394,185)how()!~who() ^how()'where():mul(348,18)mul(194who()&~*~&{/%mul(505,325) *%mul(459,604)>)) ~ -where()~{mul(579,481)mul(135,794)-*mul(453,355)~/](![from()mul(443,346)mul*[,~%why()-{do()/when(43,713)mul(136,26){^when()why()'mul(108,341)[@?!',+@who()mul(195]{&@{?:how()what()select()don't():]]#mul;what()&?:mul(541,941),&;-what(75,560)who()what()?how()mul(314,260)!)mul(250,620)>#mul(612,209),#?;mul(661,597)/mul(563,594)when()!:!mul(683,595)*what()when())'how();@mul(287,255)how()/^mul(345,555) who()/when()mul(681,924) 'mul(189,542)'mul(102,360)why()!'how()-?;,mul(874,55)+:!>what()mul(538,354)**]~how()who()mul(277,851),where(802,203)<{(];'?mul(268,251)~{:]mul(139,820){^^[ /;when() what()mul(775,595)/,)^;&where(),mul(644,487)?(mul(590,599what()%-who(){mul(112,571){$mul'/#mul(835,137)$&(mul(201,460)how()from()*@where()mul(934,320),[what()where())? :don't()&+'mul(66,8)~ mul(465,911)]?how()what(),;/:*-don't()#:?where()$mul(951,775)from()%@{who()who()!mul(78,456)^[from(),mul(144,347)']where()#([ @[]mul(660,565)}}~mul(738,761)-mul(514,849)mul(648,439who()+<,*/when()!why()mul(904,440)^ select())!@-mul(442,126% #?{mul(47,20)%mul(113,81)/;&+{@mul(504,712);select() mul(720,642)when()*#who()<-'];;mul(821,613)?select()!>when(){mul ,mul(597,943)$-what()*when()where()-}select(){mul(999,17)select(230,593),% mul(920,227)>where()@!~(select()!*mul(301,278)mul(538,232*!/when()mul(283,204)'who() ]mul(861,903)what()? %{* <-mul(112,180)'?(!mul(121,398)']<~/mul(363,850)])from()mul<>?!!from()when()select()!mul(551,325)[where())-:{#)mul(114}}:,,mul(341,114)from()?why() from()# mul(611,400))what()% from()}/when()'mul(874,416)'@&~+]mul(916,295what()@why()how()>where()-^mul(988,626)select()#!)who()why()mul(597,791)};mul(160,184) from()~{;!where()mul(332,928)where()(#!/usr/bin/perl+^who()]:,~}select():mul(810,730)when()mul(312;&what(415,542)who(560,710)who()from()^mul(828,831)> }how(595,281)!why()*/:mul(70,967)
(do(){,-how()<(how()[{why()mul(16,675))+don't()!>-((&what()!mulwhere()+( mul(446,260)#+&how()}}when()<mul(517,657)how()$)' ?>who()/do()[,who()]>-~<mul(370,491)*]*}/'&mul(451,243)mul(459,272)^]' >from(),mul(200,312);$mul(997,25);?where(203,706)&?}select(),mul(553,783)@^~mul(779,661)%)mul(252,997)what()from();%mul(439,801)select()#?')~;%}mul?why()+!mul(385,635)@)^):!*)how()mul(563,131)#&mul(720,10)~#<+]^!:@how()mul(24,633)~mul(103,646)mul(331,217)~#mulwhy()@-$> mul(288,357)how() when();;why()<+mul(513,580)?when(299,618)!<^-mul(318,287) }mul(88,924)mul(220,403<what()mul(180,327)where()? @mul(766,852),mul(758,342)#&<when()select()^]}mul(354,76)select()^(+don't()mul(371,236)!where(){mul(679,524$}];do()%mul(334,640)#]*how()}&@from()+mul(927when();':when()who()when(90,761)why()why()&mul(894,120)&-?'^^do()}^;from()&,]:<%mul(433,887)?$when()from()select())when(){'mul(84,915)[  <>mul(264,790)mul(78,811),,(<why()}:}~mul(407,891)-~;who(){/when()what()what()mul(56,769)how()}>/who()who()mul(978,770)[what()$)]#:%mul <when()}mul(970,37):select()why()(?<^ ?<mul(357,272)>mul(57,890)'(mul(146,967)[<#%)^;how()]>mul(166,279)]mul(24,319)%;select()-!/don't()>:mul(858,696)mul(622,496)*{{-~why()how()what()-mul(973%}+> mul(904,891)*(:{%mul(618,932)&!~*mul(77,889)}%~{mul(206,797)select()what() who()+*what(499,999)?@@mul(114,405)(()where()}/){]}mul(841,73)@!where(581,676)]#from(879,459)}^mulhow()do()}select()~!~)[why(364,979)who(533,785)mul(839,475)[{;>)(@what()mul(597,209)-$-^select()mul(453+;:#:?&mul(972,784)what()#select()%/[select()[,how()mul(436,10)]!~)select() mul(982,995select()~/<why()]~select(409,236)do();:+-where()';)mul(580,7)%mul(844,208) #^mul(353,253)?from()where()mulwhat(){select()why()mul(698,22)&?how():,from()what()]where()mul(260,416)who()when()+select(632,146)}mul(214,946)&how(860,45)!mul[from()>%(,do()#who()]!,/*mul(718,383)when()>^*mul(803,383)when(); mul(568,612)/from()from()}what(219,960)from()*don't()@@why();who()where()mul(222,279){ mul(758,766)what()who()!how(38,972)~;],select()/mul(974,879)!don't()mul(368,975)where()^$[^&] -{mul(153,172)what()&+)[mul(97,652)when(534,157)~,:where()do()%%@]?&when(435,925)what(){mul(155,627)?{;@#mul(466,775)(;mul(834,395)//>()-don't() $mul(329,300)<+&'@^mul(469,14)*&why(99,525)',mul(427who()*@< ?do()[>from()when()?#,'&:mul(585,898)mul(128,392)-(?[,where()'^where(575,788)+mul(378,473how() '$'#@who()from()<mul(979,827)what()^mul(637,26)&what()*why()!how()mul(643<{}who()where()mul(443,856)>how()?(//mul(768,590)when()-: ](where()who()(mul(716,399)/~)@mul(754,670)what()mul(656,266):(;%!]mul(595,874)why()%@<^?mul(702,835)(![&&/+%mul(421,278)}where()-%^'+mul(842,496)/?@:]mul(282,851)~@)how())mul(543,112))]+^)mul(133,862);#)when()who()why()when(58,966),,mul(513,202)@mul(716,648)(mul(793,735)what()]where()%+-/mul(359,127)-+}/mul(116,988)when()mul(153,16):'@$who():~-mul(441,603)'how(){ #why()%{{mul(877,856)select()who(777,457)select()from())how(345,367)from()mul(447,557)%/$-select(),when()+what()mul(189,616)what()}mul(822,616)mul(454,622)how()&who()&#do():> mul(353,679)^(@select()<;mul(414,440)why()+how()&,]#-&mul(402,532)-})~#$-!<mul(895,294)/;( }>mul(883,415):<@]*from() mul(28,253){where()? <!&,why()?mul(633,240)]--+^{how()%]mul(649,701)]:!why()+who())mul(126,903)]what()@select()$from()mul(587,84)mul(911,475)do()!];when()*;[where(),mul(370,958)what()/>what()select()~mul(259,972)-(]<}>when()from()$mul(650,381)~from()}from()who()>mul(72,307),who()where()?@<when()@why()mul(585,731)mul(272,301)-%who()when(202,213)*mul(884,335)]@@why()$do()~#mul(786,141)
where()}/what(611,646)!mul(470,537)}who()what()]-$[what()mul(341,864)<(+from()}>{where()mul(706,447)from(671,711))~mul(601,925)} ;what()[mul(533,851~{&what()(@{<'where()mul(799,568)%<why()~]'+$mul(169,116)~<why()from()-^;mul(447,48);from()'how()mul(643,718)select()+ ?<,$mul(622,397):*>where()<when()&))mul(410,76)/[mul(951,998)% #'~}-mul(954,766)-when():do()when()where())^:?mul(460,200]how()$&$/;&who()mul(126,104)when()}$when()+$why()%what()who()mul(777,781)-$@,+(^mul(138,32) /;mul(604,605)':*mul(457,205)from()mul(968,111);+?)!mul(185,427)/#mul(589,783)?#who(284,112)@<'[->mul$>select()[)#^:mul(414,93)]mul(16,757)&[who(),/mul(629,760)&''how(),from()mul(951,329)^mul(781,711):/',+'{%when();mul(661,844)/why()<^}#mul(337,134)!)mul(339,829)([how()+&~how(512,132)!;:mul(696,374))}/what()from()mul(640,944)'{*how()what(279,739)why(843,673)?<mul(930,104)from(71,501)> &!where()mul(347,404)^?>!$&mul(316,524) when()]mul(875,937)$(@]$don't()/who():/]mul(833,846)who()mul(190,362))mul(183,740)how()}mul(14,502):why();why()<mul(752,588),who()where(877,731)&*,%who()where()mul(817,369)+?how(166,381)}mul(787,226)from()>'mul(341,888)mul(668,734)]/what())**&(do()how()*:select()}*:]mul(604{mul(123,983)#&why()mul(159,440)mul(437,830)~};'])[?mul(36,75)mul(836,766),?*select()who()mul(548,488)%--where(521,841))$]do():-from()*mul(355]<+>:mul(58,505)what()from(49,769)mul(108*]~>mul(131,644)?!from()mul(11,884):where()!;select();+[select()mul(358,741)<mul(788,402what()?who()mul(232,817){;from(); mul(452,48)(>(*?]do()(?{@^mul(117,14)^+;what()from()}mul(847,203)/who()where()from(567,960)when()</:~mul(592,204)[}where()*don't()?mul(212,912)who()mul(73,318)how()*who(597,691)){&-mul(971,304)where()mul(64,983)#who()mul(662,2!when()@where(522,361)select(63,12)&+what()!$mul(678,247)when()mul(878,222)]>how()%~'}mul(677,415)mul(91,507)when()*when()from()*(mul(935,477)  from()@ mul(556,85)?)@mul(196,674)^;*+#$mul(531,124)!what()%select(){who()}';~mul(67,663)when()'?mul(205,527)@:+ ?:why() %mul(513,956/}:,'@+$who()-mul(963,914)@from()why()how(292,305)!from(980,892)mul(456,909)!who()<(*@select()&why()mul(947,805)who()how()^}mul(154,935)+?when()('};]>^mul(855,799){who()]+*{mul(823,352)*<$when()+)^&(do()mul(623,916)(['])^what(){select()mul(815,135)}mul(464,34)' <what()@&how()] mul(223,241)mul(595,176):!select()?~)</mul(707,895) how()>^)-^~where()where()mul(50,471)*{select()from() mul~:why()when()<when()?mul(131,929) [mul(45,134)'+:how()]select()@when()%<mul(755,746)who()why(){^mul(592,378)%}mul(88,624)where(901,919)?(how()how()]mul(533,3^where()who()]-mul(394,600)?)~from():mul(139,515),mul(531,61);$$how()mul>[why();%, }-where()#mul(184,632)~]+'select()}what()mul(675,164)mul(360,852)mul(875,801):where(811,851)mul(702,746)mul(29,632)[{^]-:!{ who(719,324)mul(720,687);:/[#*mul(431,415)mul(123,914]&?%$how()mul(655,184)]@?how()*$(-what()mul(323,687)mul(474,75);mul(846,335):%;do()~?where()~mul{}?%mul(446,300)^how(),<&from()#!#from()mul(423,746)how()what()don't()what()+*<mul(231,901)}from()mul(580,914)why()#%{}@^<mul(325,335)~mul(97,85)how() select()how()*]{{mul(138,378)mul(232,238)how(816,837)who()mul(855,527)!$}%[who()select(222,409)do()+) mul(853,840)#mul(974,262)*when()/<mul(85,995):]how()when() mul(883,291)?))select()}mul(218,597)when()!why())+mul(920,414)mul(263,33)
~-$'&&^!<mul(959,544)@where()#:?%)/)-mul(730,399)::mul(799,976)<mul(83%*/who(215,306)do()% '~mul(47,623):) <select())?mul(36,132)~don't()+,+,'#],(mul(479,758];select()<~?[,when():mul(433,783)],where()/do()'who()$+what()-^mul(620,968)?/]-}why()!]#mul(826,251)&?mul(953,890)$~{where()$}}[+mul(671%{why()!$]}^mul(651,483)how()[[(do()*:;$*mul(818,404)~where()}what()[} mul(750,606)mul(909,386)why()how()&how(){{how()mul(208,481)mul(793,351)}-['}:}who()mul(42,668)[do()}select()??from():&?)mul(85,533):~?$+when()^how()&do())<when()mul(831';,'where()when()'+from()^mul(952,914))mul(960,931)who()from()<what()*%why()when()-@mul(829,638);when(){ mul(661,694)>#:mul(268,185)@do()!>?~;@]mul(657,833) ,(who()-who()mul(415,876)]&#?@'!/&mul(437,971)^,+mul(884,392):mul(183,497)^from()mul(204,743)^'>}who()$;}mul(892,574)+ from()?$mul(922,854))select()#,+>where(),*mul(551,303)?}mul(261,657)?why()}why()when()%-mul(124,265!mul(979,380)/@select()}>why()+#mul(384,303)$,@@-mul[mul(479,548)-]#> ?:!do()how()@&mul(917,657{:$&mul(966,387)}what())[-]mul(183,849)^^who()&<,mul(669,375)mul(323,459)$%/from()~+}when()mul(789,390)'+mul(804,927)#who()mul(102,842)$$)how()from()select()][mul(380,252) )>when()where()how()who():#where(184,552)mul(244,943)$&$*}*-mul(727,613)(#why()}>mul(807,274)mul(577,489)mul(731,223)>where()/!]? %where()mul(359,604)/$;$+}mul(182,17)why()-how()mul(792,962)why()/{-(how()%'select()mul(997,718)/{mul(7,739)select();:mul(800,703)[when()' #~why()where()*mul(345,374)mul(308,927)how()%@how()mul(233,785)#{!select()mul(208,457)#from()}what()mul(347,911)where()from()@;(mul(492,896)&;?+<![:!<mul(211,499))!%]mul(12,519)'?--/,mul(158,834)::$why()who(171,915),#mul(807,360)?}}}do(){~] <'>, mul(948,682)+~when()}from()mul(930,691)[&]*((#mul(600,425){what()'{)@,where();:mul(844,671)~+)#<where()when():{mul(124,928)where()*: -@mul(194,634)why(466,842)'-mul(402,954)!why()?mul(256,694)don't()&mul(797,748)from()<why()<don't():~why()when()who(){mul(44,366)&{^mul(957,373)*select()$%why()~mul(956,708)'/}how()do()%from()+select()]+when()mul(381,888)(!?#{ from()mul(423,132) ($~$@?mul(225,981);;+who():<)%^mul(840,611)!)mul(763,490)&why()@{where()mul(852,987)*!what()(mul(680,776)mul(436,532)from(52,270);) ^mul(28,580)how()>,(mul(446,155)$%@/:mul(749,494)mul(24,97)where(6,997)&where()?why(449,637)mul(631,323))mul(192,700));/$]what()mul(820,765)who()(>%>mul(702,770)*-[;}(mul(438,245)@)]^/'#mul(554,294)!mul(34,410)where()$<#how(360,499)@#mul(585,680)<^};mul(295,437)where()] {+mul(607,28)why()#% do();mul(96,932)]why()+who(){<,[where()mul(271,645);^:{mul(411,161)]<>do()@';when() (mul(41,299)(!what()*select(387,698)$]mul(942,465)^?~what(),*?-'from()mul(70,415)why()'from()how()mul(682,699)!^-when()?when()#mul(473,999)  {<mul(676,919)+??<#?mul(119,628)<&~from()}:mul(740,385)mul(444,907)@~,*$<, $@don't()~:+@how()select()what()%$mul(389,212);;what()%[how()mul(210,340):how()'-mul(80,124)&-how()>(~>^why()}mul(240,258)+why()&%mul(579,916)!(]((select(112,996)#($,mul(584,139)%'''
search_pattern = re.compile(r'mul\((\d+),(\d+)\)')

@timer
def part1(input):
  search_pattern = re.compile(r'mul\((\d+),(\d+)\)')
  search_result = search_pattern.findall(input)
  return sum([int(a) * int(b) for (a,b) in search_result])
  
part1(sample_input)
assert part1(real_input) == 189600467

sample_input_for_part_2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
@timer
def part2(input: str):
  search_pattern = re.compile(r'mul\((\d+),(\d+)\)')
  split_on_do = input.split("do()")
  s_to_consider = []
  for s in split_on_do:
    split_on_dont = s.split("don't()")
    s_to_consider += split_on_dont[0]
  
  search_result = search_pattern.findall(''.join(s_to_consider))
  return sum([int(a) * int(b) for (a,b) in search_result])

part2(sample_input_for_part_2)
assert part2(real_input) == 107069718