D:\mailCloud\prjother\tmp\1\c113_SNMP and its Configuration.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
All right.|Все в порядке.
We've made it to the the last session in the book.|Мы дошли до последнего занятия в книге.
My book, that is.|Моя книга.
All right, which is the last part of these IP services that CISCO threw in there.|Хорошо, это последняя часть IP-сервисов, добавленных CISCO.
We're gonna talk about SNMP on this lesson.|В этом уроке мы поговорим о SNMP.
Then, the next lesson will be Syslog.|Следующим уроком будет системный журнал.
And then, Netflow.|А потом Netflow.
And again, SNMP and Syslog are the only two that really, we have labs with.|И снова, SNMP и Syslog - единственные два, с которыми у нас действительно есть лабораторные работы.
And, the labs are okay, I mean they're not bad, you can see what they do.|И с лабораториями все в порядке, я имею в виду, что они неплохие, вы можете видеть, что они делают.
But, really, honestly?|Но на самом деле, честно?
This is why I have these softwares up here.|Вот почему у меня есть это программное обеспечение.
MRTG, PRTG, Splunk, Cisco Works, or Solar Winds.|MRTG, PRTG, Splunk, Cisco Works или Solar Winds.
These are the sum of the monitoring devices that you're going to be using.|Это сумма устройств мониторинга, которые вы собираетесь использовать.
All you need to understand for your test is, you know,|Все, что вам нужно понять для теста, это, знаете ли,
is the very basics of what this does.|это самые основы того, что это делает.
Now, SNMP has been around forever.|Теперь SNMP существует всегда.
We've used SNMP, I remember using SNMP in Netmon.|Мы использовали SNMP, я помню, использовал SNMP в Netmon.
Remember Network Monitor, for those of you that have been in IT for a while?|Помните Network Monitor для тех из вас, кто какое-то время работал в ИТ?
All right.|Все в порядке.
Netmon in Windows 2000,|Netmon в Windows 2000,
we were, Windows 98.|мы были, Windows 98.
You had all these different oh my God, I want to say clocks.|У вас были все эти разные, о боже, я хочу сказать часы.
Counters, all these different counters that you'd,|Счетчики, все эти разные счетчики, которые вы бы,
you'd actually put in there and you, you look at all these different counters that would create a histogram and all that.|вы действительно вставляете туда, и вы смотрите на все эти разные счетчики, которые создают гистограмму и все такое.
That's what this is.|Вот что это такое.
SNMP, as it says here, it monitors all devices on the network.|SNMP, как здесь сказано, контролирует все устройства в сети.
What does that mean, what do you mean all devices on a network?|Что это значит, что вы имеете в виду все устройства в сети?
Yes, anything that supports SNMP, SNMP,|Да, все, что поддерживает SNMP, SNMP,
you have an,|у тебя есть,
you have an actual work station that's actually going out to the network.|у вас есть настоящая рабочая станция, которая фактически выходит в сеть.
And you've enabled this SNMP and now they are talking about simple management network protocol, they are talking back and forth, right?|И вы включили этот SNMP, и теперь они говорят о простом сетевом протоколе управления, они говорят туда-сюда, верно?
They are sending information, hey, this is going out with me, this is going out with me and it's telling you, hey, this is|Они отправляют информацию, эй, это происходит со мной, это идет со мной, и это говорит вам, эй, это
what's going on with this router.|что творится с этим роутером.
You will go into your managing work station, whatever software they said that you have, and you take a look at each device that you're monitoring and|Вы войдете на свою управляющую рабочую станцию, какое бы программное обеспечение, по их словам, у вас есть, и посмотрите на каждое устройство, которое вы контролируете, и
you see if there's anything wrong.|вы видите, если что-то не так.
The CPU usage is too high or whatever it is, whatever it is.|Использование ЦП слишком велико или что бы там ни было, что бы это ни было.
It could be a server, you know, you want to look at the, the paging files or the router's you know, error rates or whatever.|Это может быть сервер, который вы хотите просмотреть, файлы подкачки или маршрутизатор, количество ошибок или что-то еще.
All right?|Все в порядке?
SN, that's what SNMP is all about.|SN, вот что такое SNMP.
And here where it says it polls the MIB,|И здесь, где говорится, что он опрашивает MIB,
right,|верно,
the management information base, for the OID, object identifier.|база управляющей информации для OID, идентификатора объекта.
Everything in the router, everything in the router that we've seen so far when we do show IP in brief, when we do show interface, when we do show start,|Все в маршрутизаторе, все в маршрутизаторе, что мы видели до сих пор, когда мы вкратце показываем IP, когда показываем интерфейс, когда показываем start,
all, everything in there CISCO has assigned an OID.|все, что там, CISCO присвоило OID.
What is an OID?|Что такое OID?
And everyone actually uses this analogy I guess, 69.1.3.4.6.89 dot whatever.|И все на самом деле используют эту аналогию, я полагаю, 69.1.3.4.6.89 точка где угодно.
It's a huge number.|Это огромное количество.
They call it, everyone calls it an IP address gone bad.|Они называют это, все называют это испорченным IP-адресом.
All right?|Все в порядке?
Because it's a huge number.|Потому что это огромное количество.
Do you need to memorize these numbers?|Вам нужно запомнить эти числа?
No you do not, if you do, wow hey man, or gal, more power to you.|Нет, не надо, если да, ух ты, мужик или девчонка, больше власти тебе.
But because what you're gonna do is your managing work station will work off these numbers and give you back, hey, what is it that you wanna look at?|Но поскольку то, что вы собираетесь сделать, это то, что ваша управляющая рабочая станция будет работать с этими числами и возвращать вам, эй, на что вы хотите посмотреть?
Well I wanna look at the error rates, I wanna look at the debug.|Что ж, я хочу посмотреть на количество ошибок, я хочу посмотреть на отладку.
I want to look at different things that's going on with this particular, so I will bring back that information.|Я хочу посмотреть на разные вещи, которые происходят с этим конкретным, поэтому я верну эту информацию.
All right?|Все в порядке?
That's what the OID and you actually, when you purchase a router, you know,|Это то, что OID и вы на самом деле, когда вы покупаете маршрутизатор, вы знаете,
here's your router, okay, and then you have your iOS.|вот твой роутер, ладно, а потом у тебя iOS.
And then you want to download the latest and greatest MIB right, for that particular router.|И затем вы хотите загрузить самую последнюю и самую лучшую MIB для этого конкретного маршрутизатора.
If there's any updated stuff there with it.|Если там есть что-нибудь обновленное.
So definitely, yeah, you're going to go ahead and, this is what.|Так что определенно да, вы собираетесь идти вперед, и вот что.
Now for.|Теперь для.
For the packet tracer we're going to use an actual PC to look at the MIB, and it works based on something called a community string.|В качестве трассировщика пакетов мы собираемся использовать настоящий ПК для просмотра MIB, и он работает на основе того, что называется строкой сообщества.
And that's the only problem, it's plain text.|И это единственная проблема, это обычный текст.
It's a plain text, and then, since it's a plain text what happens is that,|Это простой текст, и, поскольку это простой текст, происходит следующее:
if it's, it can be intercepted, they can see what you're looking at.|если это так, его можно перехватить, они могут видеть то, на что вы смотрите.
Now, the good thing is, it could be read-only or read-write.|Хорошо, что он может быть доступен только для чтения или чтения-записи.
Now, there's different versions of SNMP.|Теперь есть разные версии SNMP.
You have SNMP one, SNMP version two C.|У вас один SNMP, второй SNMP версии C.
You have SNMP version three.|У вас версия SNMP три.
Version two C, by far, is the most popular, okay.|Версия вторая C, безусловно, самая популярная, хорошо.
But, it's still plain text, right.|Но это все равно обычный текст, верно.
You can do read-only or read-write.|Вы можете делать только чтение или чтение-запись.
Definitely only do read-only, because if you do read-write, meaning now the person,|Определенно только для чтения, потому что если вы делаете чтение-запись, то есть теперь человек,
if he intercepts it, he can actually re-write stuff, passwords, right?|если он его перехватит, он действительно сможет переписать данные, пароли, верно?
IP addresses, security configurations.|IP-адреса, настройки безопасности.
So you do read only, so they only see it.|Итак, вы действительно только читаете, поэтому они только это видят.
Version three, you can actually assign groups for a particular counter let's say.|В третьей версии вы можете назначать группы для определенного счетчика, скажем.
So, so you can end, it's username and password and things like that.|Итак, чтобы вы могли закончить, это имя пользователя, пароль и тому подобное.
So version three is the latest one and it's the one that's, more secure,|Итак, третья версия - последняя, ​​и она более безопасна,
because it encrypts and you have, I have user names and passwords.|потому что он шифрует, а у вас есть имена пользователей и пароли.
You can assign them by groups.|Вы можете распределить их по группам.
So it's very secure, but again, the most popular is version two C cuz again,|Так что это очень безопасно, но, опять же, самая популярная версия - вторая C, потому что снова
the change to resistance syndrome.|переход к синдрому сопротивления.
All right.|Все в порядке.
Here no security, I just talked about that.|Здесь нет безопасности, я только что говорил об этом.
String for version of yeah, community string, we'll look at it now.|Строка для версии да, строка сообщества, мы сейчас ее рассмотрим.
Version three has a community string, but I encourage you.|В третьей версии есть строка сообщества, но я вас поддерживаю.
Okay, I just told you all that, okay,|Хорошо, я только что сказал тебе все это, хорошо,
cool.|прохладно.
So that's what SNMP does.|Вот что делает SNMP.
I'm going to show you right now.|Я покажу вам прямо сейчас.
But again, ladies and gentlemen, and this is what I'm trying to, you know, ingrain.|Но опять же, дамы и господа, и это то, что я пытаюсь, вы знаете, укоренить.
You're not gonna be sitting at your router at your desk looking at your router to see when the interface goes down, to see.|Вы не собираетесь сидеть за своим маршрутизатором за своим столом, глядя на свой маршрутизатор, чтобы увидеть, когда интерфейс выйдет из строя, чтобы увидеть.
No you're gonna be looking at a big plasma screen TV or your management work station has the software in it.|Нет, вы собираетесь смотреть на большой плазменный телевизор или на вашем рабочем месте есть программное обеспечение.
And you'll be monitoring that particular you know, in a desktop you have a little thing right there, you know, you have two|И вы будете следить за тем, что вы знаете, на рабочем столе у ​​вас есть мелочь, вы знаете, у вас есть два
or three desktops.|или три рабочих стола.
Then you'll have that software off to the side taking a look at and monitoring,|Тогда у вас будет это программное обеспечение для проверки и мониторинга,
you know, certain things that, cuz you'll probably be hey,|вы знаете, некоторые вещи, потому что вы, вероятно, будете эй,
I want you to monitor this.|Я хочу, чтобы вы следили за этим.
Now, if you're the lucky individual that you need, you get to monitor, you know,|Теперь, если вы тот удачливый человек, который вам нужен, вы можете контролировать, вы знаете,
300 different sites that have 2,000|300 разных сайтов, у которых 2000
different routers and,|разные роутеры и,
you know, 4,000 you know, servers and all sorts of crazy stuff.|ну знаете, 4000 ну знаете, серверов и всяких сумасшедших вещей.
I hope you're getting paid a lot of money,|Я надеюсь, тебе платят много денег,
all right?|все в порядке?
But again you'll be looking at management software.|Но вы снова будете смотреть на программное обеспечение для управления.
And since I'm on the subject of that,|И раз уж я об этом говорю,
management software.|программное обеспечение для управления.
One of the things when you get out there and you guys, you guys put your resumes out there so recruiters and all that can|Одна из вещей, когда вы выходите, и вы, ребята, вы, ребята, выкладываете свои резюме туда, чтобы рекрутеры и все, что могли
call you and what have you.|позвоню тебе и что у тебя.
Keep this in mind, obviously, I want most of you to get your certification.|Имейте это в виду, очевидно, я хочу, чтобы большинство из вас получили сертификат.
I definitely want you to get you know,|Я определенно хочу, чтобы ты знала,
your job, your promotion,|ваша работа, ваше продвижение по службе,
whatever reason it is you're getting this certification.|по какой бы то ни было причине вы получаете этот сертификат.
Well one of the things that you need to ask these recruiters in a very nice way,|Что ж, одна из вещей, о которой вам нужно очень хорошо спросить этих рекрутеров,
and a very humble way.|и очень скромный способ.
What you need to ask the recruiter is,|Что вам нужно спросить у рекрутера:
because they have questions like this, I think I've said this before.|потому что у них есть такие вопросы, думаю, я уже говорил это раньше.
Have you ever managed or analyzed a enterprise network?|Вы когда-нибудь управляли или анализировали корпоративную сеть?
Well, this would be one of my questions to that particular recruiter.|Что ж, это был бы один из моих вопросов к тому конкретному рекрутеру.
What is your definition of an enterprised network, and what software is your client using to analyze his network?|Как вы определяете корпоративную сеть и какое программное обеспечение использует ваш клиент для анализа своей сети?
Because, SNMP is just the underlying protocol that talks back and forth to the software.|Потому что SNMP - это просто базовый протокол, который обменивается данными с программным обеспечением.
So what software are they using?|Так какое программное обеспечение они используют?
Because not everyone uses the same software.|Потому что не все используют одно и то же программное обеспечение.
I can tell you this much,|Я могу вам многое сказать,
Splunk that I had up there before were, in TelCo they use Splunk.|Splunk, который у меня был раньше, в TelCo используют Splunk.
In other places they use Solar Winds.|В других местах используют солнечный ветер.
PRTG is also very popular and easy to use.|PRTG также очень популярен и прост в использовании.
But again, if you've never used PRTG.|Но опять же, если вы никогда не использовали PRTG.
So now you don't know how to analyze a network?|Итак, теперь вы не знаете, как анализировать сеть?
So these are the kind of things that I don't want you to get fear of,|Так что это те вещи, которых я не хочу, чтобы вы боялись,
because I know when you read these interesting for a lack of a better word that I really want to say job descriptions,|потому что я знаю, когда вы читаете эти интересные из-за отсутствия лучшего слова, я действительно хочу сказать описания работы,
you must know how, you, you should have experience with,|вы должны знать, как, вы должны иметь опыт работы с,
you know, enterprise networks and analyzing enterprise networks.|вы знаете, корпоративные сети и анализ корпоративных сетей.
Okay.|Ладно.
But what software are they using?|Но какое программное обеспечение они используют?
So keep that in mind.|Так что имейте это в виду.
Be very alert at what these recruiters are asking you.|Будьте очень внимательны к тому, о чем вас просят рекрутеры.
Ask questions back.|Задавайте вопросы обратно.
Be humble, cuz I want you to get the job.|Будь скромным, потому что я хочу, чтобы ты получил работу.
Okay?|Ладно?
But still, don't let nobody intimidate you to say, well,|Но все же, не позволяйте никому запугать вас, говоря, ну,
you know, we need somebody that knows how to do.|знаете, нам нужен кто-то, кто умеет это делать.
Well, you know, because again, out there in the, the,|Ну, вы знаете, потому что снова там, в,
I don't know who put these descriptions out there.|Я не знаю, кто опубликовал эти описания.
You know, cuz you've seen descriptions that say no high school diploma needed, two years of Cisco experience.|Вы знаете, потому что вы видели описания, в которых говорится, что аттестат средней школы не требуется, это два года опыта работы в Cisco.
I said, my God.|Я сказал, Боже мой.
This guy has no high school degree, but he must have known somebody to get that job in, you know, doing Cisco.|У этого парня нет высшего образования, но он, должно быть, знал кого-то, кто получил эту работу, ну, знаете, в Cisco.
They have two years of experience.|У них двухлетний опыт работы.
So what is it you want?|Так чего же ты хочешь?
Or even better, you must be a CCNA.|Или, что еще лучше, вы должны быть CCNA.
CCNP preferred.|CCNP предпочтительнее.
What are, you know, it's confusing.|Что, понимаете, сбивает с толку.
So be careful when you're, you know, don't not be careful, just don't be intimidated.|Так что будьте осторожны, когда вы, знаете, не будьте осторожны, просто не бойтесь.
Sometimes these descriptions that prefer jobs.|Иногда эти описания предпочитают рабочие места.
All this is to scare people off, say, oh,|Все это для того, чтобы отпугнуть людей, мол, ах,
my God.|о Господи.
I don't know that, I don't know that.|Я этого не знаю, не знаю.
And they're not and you don't go for the job.|А это не так, и вы не идете на работу.
You go for the job and then you ask the questions or you do your research before you give a call.|Вы идете на работу, а затем задаете вопросы или исследуете, прежде чем позвонить.
You know, okay, okay, you want somebody who knows how to monitor network.|Вы знаете, хорошо, хорошо, вам нужен кто-то, кто знает, как контролировать сеть.
Take a look at all the different monitoring devices that exists out there.|Взгляните на все существующие устройства мониторинга.
All right.|Все в порядке.
Take a look at it.|Взгляни на это.
So when you speak, you can speak intelligently about certain things.|Поэтому, когда вы говорите, вы можете разумно говорить об определенных вещах.
But again, not every company is going to do everything the same way.|Но опять же, не все компании будут делать все одинаково.
Each company has a different way of doing it.|У каждой компании свой способ сделать это.
Once you get the certification, it's a matter of understanding the concepts,|После получения сертификата необходимо понять концепции,
like SNMP.|вроде SNMP.
What does SNMP do?|Что делает SNMP?
It talks, it monitors the devices that talk SNMP.|Он говорит, он отслеживает устройства, которые говорят по протоколу SNMP.
And pretty much, 99.9% of all devices talk SNMP, because every,|И почти 99,9% всех устройств используют протокол SNMP, потому что каждое,
SNMP has been around since Fred Flintstone.|SNMP появился со времен Фреда Флинтстоуна.
Okay?|Ладно?
So, okay.|Так хорошо.
I'm getting, I'm getting a little bit off the subject.|Я немного ухожу от темы.
But anyway, but the work station is what you're going to configure.|Но в любом случае, вы собираетесь настраивать рабочую станцию.
Here's your MIB.|Вот ваша MIB.
And what you do and we're gonna, we're gonna put this,|И что ты делаешь, и мы собираемся, мы собираемся поставить это,
you go to the advance and we'll put the address, okay?|ты идешь в аванс, и мы укажем адрес, хорошо?
We'll put the the actual address, hold on.|Мы укажем реальный адрес, подождите.
Let me cancel this real quick and let me move this over here.|Позвольте мне отменить это очень быстро и позвольте мне перенести это сюда.
All right.|Все в порядке.
And we go to advance, we can actually put the,|И мы идем вперед, мы действительно можем поставить,
the address that we're trying to monitor,|адрес, который мы пытаемся отслеживать,
the port that it's using.|порт, который он использует.
And here see it says that the read community and the write community.|И вот здесь говорится, что сообщество чтения и сообщество записи.
What that means is the read-only or write.|Это означает только чтение или запись.
You never want to give them write permissions,|Вы никогда не захотите давать им права на запись,
because they can change things around.|потому что они могут все изменить.
So you wanna give the just read and you can see that,|Итак, вы хотите дать только что прочитанное, и вы можете это увидеть,
you can pick the version that you want.|вы можете выбрать ту версию, которая вам нужна.
Again, I'm just gonna leave out version one.|Опять же, я просто оставлю первую версию.
Nobody uses version one anymore at all.|Первой версией больше никто не пользуется.
All right?|Все в порядке?
So, it really doesn't matter just understand the concepts.|Так что на самом деле не важно просто понять концепции.
Obviously, it would be cool if you can use version three, so you can put user name and passwords and so forth.|Очевидно, было бы здорово, если бы вы могли использовать третью версию, чтобы вы могли указать имя пользователя, пароли и так далее.
And sign into different groups or version two C,|И войдите в разные группы или версию два C,
it's really version two C or we can put version two, what have you.|это действительно версия два C или мы можем поставить версию два, что у вас.
But again, we're gonna do it first on the router and then we'll come down to the and you see here, you can expand on what is it|Но опять же, мы сначала сделаем это на маршрутизаторе, а затем мы перейдем к, и вы видите здесь, вы можете подробнее узнать, что это такое.
that you want to look at.|что вы хотите посмотреть.
But let's go ahead and configure it on the router.|Но давайте продолжим и настроим его на роутере.
We need to gonna to create an SMP server community string.|Нам нужно создать строку сообщества SMP-сервера.
All right.|Все в порядке.
So here we go.|Итак, поехали.
Let's maximize the screen, cuz I laugh.|Давайте увеличим экран, потому что я смеюсь.
I love when people call me for no, for no reason.|Я люблю, когда люди звонят мне без причины.
I use it for fun.|Я использую это для развлечения.
All right.|Все в порядке.
SNMP server.|Сервер SNMP.
P, Q, R, S.|P, Q, R, S.
Here it is.|Вот.
SNMP server community and you see that's all, that's all they let you do.|Сообщество серверов SNMP, и вы видите, что это все, это все, что они вам позволяют.
Community and then you put a word, you put a word.|Сообщество, а потом вы произносите слово, вы говорите слово.
I like, you know, me and movies and what have you.|Знаешь, мне нравятся и фильмы, и все, что у тебя есть.
But I'm gonna pick okay, Spartacus.|Но я выберу хорошо, Спартак.
Sparta, Sparta.|Спарта, Спарта.
I just went Sparta, okay?|Я только что поехал в Спарту, хорошо?
And then you gotta tell it, hey, is this only read-only or re-write?|И тогда вы должны сказать это, эй, это только для чтения или перезапись?
We're just gonna put read-only.|Мы просто поставим только чтение.
Okay.|Ладно.
SNMP server community the community string is Sparta and it's, I put R0.|Сообщество сервера SNMP строка сообщества - Sparta, и я поставил R0.
Read-only.|Только для чтения.
Sorry, read-only.|Извините, только для чтения.
Okay?|Ладно?
And then [SOUND] you see, interface F0/0.|Затем [ЗВУК] вы видите интерфейс F0 / 0.
Invalid interface type of number.|Неверный тип интерфейса номера.
Really?|В самом деле?
Do show IP IN BRIEF.|Покажите IP КОРОТКО.
Oh, we're fancy now.|О, теперь мы в моде.
All right.|Все в порядке.
INT G0/0.|ИНТ G0 / 0.
Whoa.|Ого.
Cool.|Круто.
All right.|Все в порядке.
And let's see if anything, [SOUND] we didn't put no grooves for anything like that.|И давайте посмотрим, [ЗВУК] мы не ставили канавок ни для чего подобного.
All right.|Все в порядке.
So we did the community string and now we go to our MIB, right?|Итак, мы сделали строку сообщества и теперь переходим к нашему MIB, верно?
And we do the same thing.|И мы делаем то же самое.
[BLANK_AUDIO]|[BLANK_AUDIO]
So the address is 192.168.|Итак, адрес 192.168.
What 0.3.284.|Что 0.3.284.
[BLANK_AUDIO]|[BLANK_AUDIO]
Okay?|Ладно?
Because something just went,|Потому что что-то просто ушло,
just right here.|прямо здесь.
Oh, oh here we go.|О, вот и мы.
Advanced, just bring it over here.|Продвинутый, просто принеси сюда.
All right.|Все в порядке.
492.168.3.254 and then the read community strain is Sparta.|492.168.3.254, а затем штамм читающего сообщества - Sparta.
Okay and we click OK.|Хорошо, и мы нажимаем ОК.
And we'll just keep it at version one, cuz we're not worried about any of that.|И мы просто оставим его в первой версии, потому что нас это не беспокоит.
And then what you do is if you wanted to take a look,|И тогда что вы делаете, это если вы хотите взглянуть,
we're pretending this is our management software that we're using.|мы делаем вид, что это наше программное обеспечение для управления, которое мы используем.
All right.|Все в порядке.
If you want to take a look at something and let's bring this up a little bit,|Если вы хотите на что-то взглянуть, и давайте немного поговорим об этом,
cuz we need to expand the [INAUDIBLE]|потому что нам нужно расширить [НЕРАЗБОРЧИВО]
tree.|дерево.
And we're going to go to router, advance IPs,|И мы собираемся перейти к маршрутизатору, продвинуть IP-адреса,
the ISO dot .org,do dod, internet.|точка ISO .org, do dod, internet.
We'll go to management, there you go,|Мы пойдем в менеджмент, вот и все,
system.|система.
All right.|Все в порядке.
And let's bring this out a little bit [BLANK_AUDIO]|И давайте немного расскажем об этом [BLANK_AUDIO]
And [SOUND] you see the system name.|И [ЗВУК] вы видите название системы.
And then you see, there's your OID for the system name.|И тогда вы видите, что это ваш OID для имени системы.
That's the OID.|Это OID.
You don't gotta memorize that.|Тебе не нужно это запоминать.
All right?|Все в порядке?
And then you get it.|И тогда вы это понимаете.
Operations a go, get and then you go.|Шеф, давай, давай, а потом уходи.
So what is the system name?|Так каково название системы?
R2.|R2.
That's what that is.|Вот что это такое.
Now this is the packet tracer.|Теперь это трассировщик пакетов.
This is the packet tracer.|Это трассировщик пакетов.
If you had any of the subs that we talked before.|Если бы у вас была какая-нибудь из подводных лодок, о которых мы говорили раньше.
The number one software, in my personal humble opinion, would be solar lens.|Программное обеспечение номер один, по моему личному скромному мнению, будет солнечная линза.
That you configure SNMP to monitor your entire infrastructure enterprise across the world.|Вы настраиваете SNMP для мониторинга всей инфраструктуры предприятия по всему миру.
All right?|Все в порядке?
You can monitor all your devices.|Вы можете контролировать все свои устройства.
You'll be looking at something very colorful.|Вы будете смотреть на что-то очень красочное.
Nice graphs.|Хорошие графики.
Things that you can you know, it makes sense to to see.|То, что вы можете знать, имеет смысл видеть.
If you actually had to drill down,|Если бы вам действительно пришлось детализировать,
cuz this reminds me of net mon way back in the day.|Потому что это напомнило мне о чистом монете в те времена.
They had to drill down and take a look at a bunch of hex numbers and all sorts of crazy stuff.|Им нужно было углубиться в детали и взглянуть на кучу шестнадцатеричных чисел и всевозможные безумные вещи.
That was more of a pain than anything else.|Это было больше боли, чем что-либо еще.
It, it hurt my eyes.|У меня болели глаза.
Just like when people now see IPv6.|Так же, как когда люди теперь видят IPv6.
It's like, oh my God, right?|Это как, боже мой, правда?
Because it's a long address, what have you.|Потому что это длинный адрес.
The same thing.|Тоже самое.
I can, I can't even imagine having to drill down.|Я могу, даже представить себе не могу, что придется углубляться.
Now, one thing is drilling down on charts and taking a look at more in,|Теперь одно дело - изучить диаграммы и взглянуть на другие,
information that makes a little bit more sense or easier on the eyes.|информация, которая имеет немного больше смысла или легче для глаз.
Because it's color coded or what have you.|Потому что это цветная кодировка или что у вас есть.
Then looking at something, okay.|Потом смотрю на что-нибудь, ладно.
System name, just to get the system name,|Имя системы, просто чтобы получить имя системы,
I have to drill down all through this.|Я должен все это детализировать.
But that's what it's doing, you see that SNMP is now giving your management workstation that particular information, and that's all we're really managing right now|Но это то, что он делает, вы видите, что SNMP теперь предоставляет вашей рабочей станции управления эту конкретную информацию, и это все, что мы действительно управляем прямо сейчас.
is that particular router.|это именно тот роутер.
So we can take a look at all the different things about the router.|Итак, мы можем взглянуть на все аспекты маршрутизатора.
Lets say, that SNMP was configured.|Допустим, настроен протокол SNMP.
Let's say the system uptime.|Допустим, время безотказной работы системы.
How long has the system uptime and got a different OID.|Как долго работает система и у нее другой OID.
Click, oh, well, it's been up for zero hours and 54 minutes.|Щелк, ну ладно, уже ноль часов 54 минуты.
Whatever the case may be.|В любом случае.
So all these things, if configured, you can see and you can configure.|Итак, все эти вещи, если они настроены, вы можете видеть и настраивать.
Let me look at I think the writing protocol we are using is RIP.|Позвольте мне взглянуть, я думаю, что мы используем протокол записи RIP.
Let's see if we can look at our RIP entry or something and see.|Посмотрим, сможем ли мы взглянуть на нашу запись RIP или что-то еще и посмотреть.
[BLANK_AUDIO]|[BLANK_AUDIO]
There you go, 2.1, that will be my RIP peer a, whatever that means.|Итак, 2.1, это будет мой узел RIP, что бы это ни значило.
So again.|Итак, еще раз.
Oh, it's your RIP to peer address.|О, это ваш RIP для однорангового адреса.
Okay.|Ладно.
So that's my peer address, all right?|Так это мой одноранговый адрес, хорошо?
1921682.1.|1921682.1.
And let's take a look and see what address is that.|А давайте посмотрим, что это за адрес.
Just, just to find out.|Просто, чтобы узнать.
2.1.|2.1.
My peer.|Мой ровесник.
This guy right here.|Этот парень прямо здесь.
2.1.|2.1.
So now I know who my peer address is.|Итак, теперь я знаю, кто мой одноранговый адрес.
But again this is a package ratio.|Но опять же, это соотношение упаковки.
So when they talk about, I mean,|Когда они говорят о, я имею в виду,
as far as the test is concerned, yeah,|что касается теста, да,
know the different versions of.|знаю разные версии.
Know what the different versions of SNP is.|Знайте, что такое разные версии SNP.
Is it version one, two and three or 2c and three?|Это первая, вторая и третья версии или 2с и третья?
One, nobody uses.|Один, никто не использует.
2c, plain text.|2c, обычный текст.
Uses a community string.|Использует строку сообщества.
Read-write, read-only.|Чтение-запись, только чтение.
Or version three that you can use actual groups, username, and it has encryption.|Или третья версия, в которой вы можете использовать фактические группы, имя пользователя и шифрование.
And its purpose is to actually look at the devices and see what's going on and bring back information to you so you can monitor these devices.|И его цель состоит в том, чтобы на самом деле посмотреть на устройства и увидеть, что происходит, и вернуть вам информацию, чтобы вы могли контролировать эти устройства.
Okay.|Ладно.
[SOUND] as far as a certification, is concerned, oh and remember your OID.|[ЗВУК] Что касается сертификации, о, и помните свой OID.
Your OID.|Ваш OID.
Your OID is this, like I said,|Ваш OID, как я уже сказал,
we looked at the system name and certain things, the RIP.|мы посмотрели на имя системы и некоторые вещи, RIP.
Because every time you type something,|Потому что каждый раз, когда вы что-то печатаете,
show IP in brief, let's say.|покажите вкратце IP, скажем так.
Everything in there.|Там все.
Everything, interface, Gigabit F00 all this is an OID, the IP address.|Все, интерфейс, Gigabit F00, все это OID, IP адрес.
All right, yes, unset, administratively down down.|Хорошо, да, отключено, отключено административно.
Now, all that is an, is an OID, is an object identifier.|Теперь все, что есть, это OID, это идентификатор объекта.
That's what SNMP looks at.|Вот на что смотрит SNMP.
So you download.|Итак, вы скачиваете.
You download the latest management information base, right?|Вы ведь скачиваете самую свежую базу управленческой информации?
Management soft, you download that so you can have, you know, the the latest MIB.|Программное обеспечение управления, вы загружаете его, чтобы иметь, знаете ли, последнюю версию MIB.
So you can go ahead and monitor your device, your devices properly.|Таким образом, вы можете продолжить и правильно контролировать свое устройство, свои устройства.
And have them updated with certain things.|И обновите их определенными вещами.
But again, this goes to your management software.|Но опять же, это касается вашего программного обеспечения для управления.
And I can't repeat this enough.|И я не могу повторить этого достаточно.
Because in the test, all they want you to know is what SNMP does.|Потому что в тесте все, что они хотят, чтобы вы знали, - это то, что делает SNMP.
That's it.|Вот и все.
No versions.|Версий нет.
And, you have to create a community string and pretty much, that's about it.|И вам нужно создать строку сообщества, и в основном это все.
And what the MIB is and the OID is.|И что такое MIB и OID.
That's it.|Вот и все.
Do you need to memorize OIDs?|Вам нужно запоминать OID?
No.|Нет.
Are you gonna be using something that looks like plain text or whatever to monitor things?|Вы собираетесь использовать что-то похожее на обычный текст или что-то еще, чтобы отслеживать вещи?
I surely hope not.|Я очень надеюсь, что нет.
Okay.|Ладно.
Once you go into a company, you will be using software to manage everything, so don't be too worried about that.|Когда вы войдете в компанию, вы будете использовать программное обеспечение для управления всем, так что не беспокойтесь об этом.
All right.|Все в порядке.
Whether it's PRTG or MRTG or Splunk or Cisco works, or whatever it is,|Будь то PRTG, MRTG, Splunk или Cisco, или что-то еще,
okay?|Ладно?
You'll be using some sort of management software.|Вы будете использовать какое-то программное обеспечение для управления.
And again depending on the company,|И снова в зависимости от компании,
depending on what they use,|в зависимости от того, что они используют,
maybe the ones that I mentioned, they won't even use.|может быть, те, о которых я упоминал, они даже не будут использовать.
Something proprietary to that particular company that was created specifically for them.|Что-то фирменное для этой конкретной компании, созданное специально для них.
So, again the underlying protocol is what we need to be concerned with, all right?|Итак, опять же, основной протокол - это то, о чем нам нужно беспокоиться, хорошо?
SNMP, it's been around here for quite a while and it's going to be here to stay until they find something new, or a newer|SNMP, он существует уже довольно давно и будет оставаться здесь, пока они не найдут что-то новое или более новое.
version of it, but that's it.|его версия, но это все.
That's what SNMP is and that's what you need to know.|Вот что такое SNMP, и это то, что вам нужно знать.
So if you wanted to practice with SNMP,|Так что, если вы хотите попрактиковаться в SNMP,
you go home and create your community string on your router.|вы идете домой и создаете строку сообщества на своем маршрутизаторе.
All right, you may get read only, all right, and then you configure it on your workstations down here.|Хорошо, вы можете получить доступ только для чтения, хорошо, а затем вы настроите это на своих рабочих станциях здесь.
And then you can just start saying, okay let me drill down and see what I can see on on the router.|И тогда вы можете просто начать говорить, хорошо, позвольте мне углубиться и посмотреть, что я вижу на маршрутизаторе.
And if you get information back, hey, you did it correctly.|И если вы получите информацию обратно, эй, вы все сделали правильно.
You did it correctly.|Вы все сделали правильно.
And that's all to SNMP there is.|И это все, что есть в SNMP.
All right.|Все в порядке.
I'll see you in the next lesson.|Увидимся на следующем уроке.
We're gonna be looking at cis log next.|Далее мы будем смотреть журнал цис.
[BLANK_AUDIO]|[BLANK_AUDIO]
