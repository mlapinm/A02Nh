D:\mailCloud\prjother\tmp\1\c61_configuring DHCP.md  


__|__
--|--
Welcome back everyone.|С возвращением всех.
We've configured our routers.|Мы настроили наши роутеры.
We have connectivity to our gateways.|У нас есть подключение к нашим шлюзам.
We did administration commands.|Мы выполняли административные команды.
We actually did in to the interfaces.|Мы действительно сделали это с интерфейсами.
We can get to our gateways.|Мы можем добраться до наших шлюзов.
Right?|Правильно?
But, we assigned the IP addresses to the computers statically.|Но мы назначали IP-адреса компьютерам статически.
All right, we went inside the computers,|Хорошо, мы зашли внутрь компьютеров,
and inside the computers,|и внутри компьютеров,
okay, oh there it is, it just took a little bit.|Ладно, вот оно, это заняло немного времени.
All right, and we put them in there statically.|Хорошо, и мы помещаем их туда статически.
So really what we wanna do is for these to be assigned dynamically.|Так что на самом деле мы хотим, чтобы они назначались динамически.
Obviously, this is going to go, go ahead and fail.|Очевидно, что это будет продолжаться, идти вперед и терпеть неудачу.
Because we don't have a DHCP server.|Потому что у нас нет DHCP-сервера.
But this is one of the labs, or ones of the lessons, that we're gonna learn today.|Но это одна из лабораторных работ или один из уроков, которые мы собираемся выучить сегодня.
We're gonna set up the routers to act as a DHCP server.|Мы собираемся настроить маршрутизаторы в качестве DHCP-сервера.
Go ahead and fail.|Идите вперед и проиграйте.
I don't have to wait for it to fail.|Мне не нужно ждать, пока это не удастся.
You know, what I mean, you know, see a fail.|Вы знаете, что я имею в виду, вы знаете, увидеть неудачу.
So you can see a fail as well.|Так что вы тоже можете увидеть провал.
One of the things is setting up DHCP.|Одна из вещей - настройка DHCP.
You in your book, or the book I've always recommended to study for the 200-120 certification, it's like a page and a half.|Вы в своей книге, или в книге, которую я всегда рекомендовал изучить для получения сертификата 200-120, это как полторы страницы.
Really, what they ask you or how they teach you DHCP IP version 4 for the Cisco router, they will ask you some questions on DHCP in your Cisco certification but|На самом деле, что они спрашивают или как они учат вас DHCP IP версии 4 для маршрутизатора Cisco, они зададут вам несколько вопросов по DHCP в вашей сертификации Cisco, но
very simple.|очень просто.
They like to play with key words.|Им нравится играть с ключевыми словами.
Remember, a DHCP server does not assign.|Помните, что DHCP-сервер не назначает.
What are you talking about, Laz?|О чем ты говоришь, Лаз?
Of course, it does.|Конечно, есть.
No, no, no.|Нет нет нет.
It leases, leases IP addresses, right?|Он сдает в аренду, сдает в аренду IP-адреса, верно?
We lease an IP address, and there's a certain allotted time that we have that IP address for, and every so often we try and renew that IP address.|Мы арендуем IP-адрес, и у нас есть определенное время, на которое у нас есть этот IP-адрес, и время от времени мы пытаемся обновить этот IP-адрес.
So be careful in the examination cuz that,|Так что будьте осторожны при обследовании, потому что
those key words they like to play around with.|те ключевые слова, с которыми им нравится играть.
Okay?|Ладно?
Assigning, leasing because out there in the real world, hey, the DHCP server's not assigning me an IP address.|Назначение, аренда, потому что в реальном мире, эй, DHCP-сервер не назначает мне IP-адрес.
We understand what that means.|Мы понимаем, что это значит.
That's our lingo.|Это наш жаргон.
But when you're taking a test, no, the DHCP server does not assign an IP address.|Но когда вы проходите тест, нет, DHCP-сервер не назначает IP-адрес.
It leases it.|Сдает в аренду.
I know.|Я знаю.
I have a PhD.|Имею докторскую степень.
Anyway, so what we're gonna do is setup a a DHCP server on a, a DHCP server.|В любом случае, мы собираемся настроить DHCP-сервер на DHCP-сервере.
A days, DHCP service on the actual router.|Через несколько дней служба DHCP на самом роутере.
So we'll do it on this one, and we'll see we're in the 192.168.1.0 network.|Итак, мы сделаем это на этом, и мы увидим, что мы находимся в сети 192.168.1.0.
So we're going there.|Итак, мы идем туда.
We've done everything else.|Все остальное мы сделали.
Well not everything I will go with done,|Ну, не все, с чем я пойду, сделано,
you know,|знаешь,
pretty much we have connectivity with our gateways and all that good stuff.|в значительной степени у нас есть связь с нашими шлюзами и всем прочим.
So we'll go to the CLI, and I'm definitely gonna use a mouse to try and,|Итак, мы перейдем к интерфейсу командной строки, и я обязательно воспользуюсь мышью, чтобы попробовать,
you know, open this up here cuz using the finger not the finger but my finger does not work, you know, and that really does have|Вы знаете, откройте это здесь, потому что используя палец, а не палец, но мой палец не работает, вы знаете, и это действительно
an interesting history now that I said the finger, where it comes from.|интересная история вот, что я сказал пальцем, откуда он взялся.
You should look that up.|Вы должны это посмотреть.
C-I-S-C-O.|С-И-С-С-О.
Cool.|Прохладно.
All right, so one of the first things, not one of the first things, but one of the things you can do is obviously you wanna go ahead and setup an exclusion.|Хорошо, поэтому одно из первых, не одно из первых, но одно из того, что вы можете сделать, это, очевидно, вы хотите пойти дальше и настроить исключение.
Right, you wanna exclude certain addresses from being assigned because your DNS servers, your file servers, your print servers, your domain controllers,|Правильно, вы хотите исключить определенные адреса из назначения, потому что ваши DNS-серверы, ваши файловые серверы, ваши серверы печати, контроллеры домена,
your DNS servers, all those will have static IP addresses.|ваши DNS-серверы, все они будут иметь статические IP-адреса.
All those will have static IP addresses.|Все они будут иметь статические IP-адреса.
So you want to exclude a range from being assigned.|Итак, вы хотите исключить диапазон из назначения.
Correct?|Верный?
So, we'll go ahead and, let's say, and you can see here it will have to be IP.|Итак, мы продолжим и, скажем, и вы видите здесь, что это должен быть IP.
All right.|Отлично.
And then that's how you will start the command off.|И вот так вы запустите команду.
And you see IP DHCP.|И вы видите IP DHCP.
And then we go IP DHCP, and then it'll,|Затем мы переходим к IP DHCP, а затем
it'll give you the option to exclude addresses.|это даст вам возможность исключить адреса.
So exclude, and I'm tabbing, you see, bad habits, don't get into these bad habits.|Так что исключите, и я вкладываю, видите ли, вредные привычки, не входите в эти плохие привычки.
Now that you're gonna have to configure,|Теперь, когда вам нужно настроить,
you're not gonna have to configure this at all in the examination all right, what so ever.|вам не нужно вообще настраивать это в экзамене, хорошо, как бы то ни было.
But understand, in the DHCP server you do have to exclude addresses from the pool that you're going to lease to your end devices.|Но поймите, что на DHCP-сервере вам нужно исключить адреса из пула, которые вы собираетесь сдавать в аренду своим конечным устройствам.
So, you know, you're, you're main storage,|Итак, вы знаете, вы, вы основное хранилище,
and all that,|и все такое,
like I just mentioned are the ones that are statically assigned.|как я только что упомянул, это те, которые назначаются статически.
Everybody else should be dynamically assigned.|Все остальные должны быть назначены динамически.
So let's exclude 192.168, oops 168,|Итак, давайте исключим 192.168, ой 168,
just to create a range, .1.1 to 192.168.1.20.|просто для создания диапазона от .1.1 до 192.168.1.20.
Just to create an exclusion.|Просто создать исключение.
And what's funny is, you see that, and you're still in global configuration.|И что забавно, вы это видите, но все еще находитесь в глобальной конфигурации.
You are not within DHCP configuration mode.|Вы не находитесь в режиме конфигурации DHCP.
You see here IP DHCP, you have a pool, or let's create addresses.|Вы видите здесь IP DHCP, у вас есть пул, или давайте создадим адреса.
We just did create addresses.|Мы просто создали адреса.
Now let's create a pool, a pool of addresses.|Теперь давайте создадим пул, пул адресов.
Over here is kind different the way you set that up.|Вот как вы это настроили.
IP DHCP pool, all you'll really do is give it a name, give it a name.|Пул IP DHCP, все, что вам действительно нужно сделать, это дать ему имя, дать ему имя.
What name, let this call a Laz, right,|Какое имя, пусть это назовет Лаз, верно,
so now, now your in the dhcp-config.|Итак, теперь ваш файл dhcp-config.
Look how cool is that?|Посмотри, как это круто?
So we have a name for a pool.|Итак, у нас есть название для пула.
I don't see why the exclusion wouldn't be in the, within the,|Я не понимаю, почему исключение не могло бы быть внутри, внутри,
the dhcp-config ,but okay.|dhcp-config, но ладно.
It isn't.|Это не так.
So, now you have these different options or things you can do.|Итак, теперь у вас есть разные варианты или вещи, которые вы можете сделать.
The default router, DNS router, the network and options, options.|Маршрутизатор по умолчанию, маршрутизатор DNS, сеть и параметры, параметры.
So definitely you need to setup the default router because the default router is your gateway, is your gateway,|Поэтому определенно вам нужно настроить маршрутизатор по умолчанию, потому что маршрутизатор по умолчанию - это ваш шлюз, это ваш шлюз,
so this gateway is 192.168.1.254.|так что это шлюз 192.168.1.254.
So now that tells the DHCP that the gateway address is 1.254.|Итак, теперь это говорит DHCP, что адрес шлюза - 1.254.
Hint, hint, hint, something possibly that may,|Подсказка, подсказка, подсказка, возможно, что-то, что может,
you may see in an exam could be at your university, could be in a CCNA.|вы можете увидеть на экзамене, может быть в вашем университете, может быть в CCNA.
All right, because this could be a good question to ask.|Хорошо, потому что это может быть хорошим вопросом.
Why aren't your, you, you configured everything for DHCP.|Почему не ваш, вы, вы все настроили для DHCP.
It seems okay.|Вроде нормально.
But your clients are still not getting an IP address.|Но ваши клиенты все еще не получают IP-адрес.
Why is that?|Это почему?
Because you forgot to put the default router address.|Потому что вы забыли указать адрес маршрутизатора по умолчанию.
So if you don't put the default router address, how is the DHCP server gonna know where to send this pool of addresses, so|Итак, если вы не укажете адрес маршрутизатора по умолчанию, как DHCP-сервер узнает, куда отправить этот пул адресов, поэтому
definitely this is a very important one.|определенно это очень важный вопрос.
The next one we're gonna do,|Следующий, который мы собираемся сделать,
I mean we'll just do it to do it DNS server.|Я имею в виду, что мы просто сделаем это для DNS-сервера.
We'll call that 192.168.1.2 and then the network.|Мы назовем это 192.168.1.2, а затем сеть.
This is important, it needs to know the network, so it can actually start assigning addresses from that particular network.|Это важно, ему нужно знать сеть, чтобы он действительно мог начать назначать адреса из этой конкретной сети.
So we're gonna go ahead and say, network.|Итак, мы продолжим и скажем, сеть.
192.168.1.0, and you gotta put in the mask.|192.168.1.0, и вам нужно надеть маску.
If you don't put in the mask, it could be whatever.|Если не надеть маску, это может быть что угодно.
So, now I know it's okay.|Итак, теперь я знаю, что все в порядке.
Out in the 1.0 not work out, 254|Выхода в 1.0 не получится, 254
addresses, but the first 1 through 20 are excluded.|адреса, но с первого по 20 исключаются.
So my first available IP address to assign to a node, should be 21, should be 21.|Итак, мой первый доступный IP-адрес для назначения узлу должен быть 21, должен быть 21.
All right?|Отлично?
The next one really, which is option,|Следующий действительно вариант,
okay?|Ладно?
You, it, it's optional except when you're doing voice.|Вы, это необязательно, кроме случаев, когда вы делаете голос.
Okay?|Ладно?
When you're doing voice just a little extra thing there,|Когда вы делаете голос, просто немного лишнего,
you have to put option 150.|надо поставить опцион 150.
Option is it 50 or 150?|Вариант 50 или 150?
I, it's 150.|Я, это 150.
It's option 150.|Это вариант 150.
And and you have to point it the source IP address, which is your default gateway,|И вы должны указать ему исходный IP-адрес, который является вашим шлюзом по умолчанию,
and the port which the default port number is 2000.|и порт, номер порта по умолчанию - 2000.
You have to do that.|Вы должны это сделать.
If you don't do that, or UDP port 2000, if you don't do that then the voice,|Если вы этого не сделаете, или UDP-порт 2000, если вы этого не сделаете, то голос,
the fold, and things like that won't register.|складка и подобные вещи не регистрируются.
But again, that's another class all together here.|Но опять же, это еще один класс здесь.
Just make sure you put in the network.|Просто убедитесь, что вы подключены к сети.
You put in the DNS obviously, we, we, we use, but it could be an option.|Очевидно, что вы вводите DNS, мы, мы, мы используем, но это может быть вариант.
And then the gateway is not an option.|И тогда шлюз не вариант.
Which is your default router.|Какой у вас роутер по умолчанию.
And that's it.|И это все.
>> DOW R, oh,|>> DOW R, о,
look at me doing shortcuts that you're not allowed to do on your exam.|посмотри, как я делаю ярлыки, которые тебе нельзя делать на экзамене.
Let me take you the long way.|Позвольте мне провести вас по долгому пути.
Copy, run, start.|Копировать, запускать, запускать.
All right.|Отлично.
Let's do a show start.|Давайте начнем шоу.
Now you see that there's a lot of commands that are in your book, but are not here.|Теперь вы видите, что в вашей книге есть много команд, но их здесь нет.
Like lease and things like that.|Например, аренда и тому подобное.
You know, those are probably within the options.|Вы знаете, это, вероятно, в пределах возможностей.
But again, you can have a period of lease times.|Но опять же, у вас может быть срок аренды.
How often or how long are you gonna allow the lease?|Как часто и на какой срок вы собираетесь разрешать аренду?
By default,|По умолчанию,
the lease of an IP address through a normal Microsoft DHCP server's eight days.|аренда IP-адреса через обычный сервер Microsoft DHCP в течение восьми дней.
Or you can have it set for however, you know, however long you want.|Или вы можете установить его на сколько угодно долго.
But remember it will try to renew itself like at 25%,|Но помните, что он будет пытаться обновиться как на 25%,
50%, 75% and then, at the very final, try to renew itself,|50%, 75% и затем, в самом конце, попытаться обновить себя,
if it didn't get renewed in the previous at the last try.|если он не был продлен в предыдущем с последней попытки.
If it doesn't renew at that point then you'll be receiving [UNKNOWN] in the IP version for network.|Если он не обновится в этот момент, вы получите [НЕИЗВЕСТНО] в версии IP для сети.
So we see that we have our excluder addresses right there, all right.|Итак, мы видим, что у нас есть наши адреса исключения, хорошо.
1 through 20.|С 1 по 20.
We have the pool named Laz.|У нас есть бассейн Лаз.
All right, and we have the networks.|Хорошо, и у нас есть сети.
Or the network.|Или в сети.
The router and the DNS server.|Маршрутизатор и DNS-сервер.
So, with that done, let's go ahead and see if this computer is receiving an IP address.|Итак, когда это сделано, давайте продолжим и посмотрим, получает ли этот компьютер IP-адрес.
And sure indeed, it is.|И действительно, это так.
It's 1.121and we have the gateway of 1.254.|Это 1.121, и у нас есть шлюз 1.254.
And we have 1.2.|А у нас 1.2.
So that is how you setup DHCP on a Cisco router.|Вот как вы настраиваете DHCP на маршрутизаторе Cisco.
The basic of it.|Основное из этого.
And again, for the CCNA certification.|И снова за сертификацию CCNA.
You will be asked a couple of questions on the on the actual exam.|На самом экзамене вам зададут несколько вопросов.
But very, very basic intro questions.|Но очень, очень простые вводные вопросы.
Very basic intro questions on the DHCP.|Очень простые вводные вопросы по DHCP.
So you can, you know, go through that,|Так что вы можете пройти через это,
what page and a half or two pages fairly quickly.|какие страницы полторы или две страницы довольно быстро.
They're not gonna get too deep into it.|Они не собираются углубляться в это.
So let's do it one more time.|Так что давайте сделаем это еще раз.
Let's go ahead and do it in this router here, so this computer can go ahead and get assigned that way, just a little practice.|Давайте продолжим и сделаем это в этом маршрутизаторе здесь, чтобы этот компьютер мог продолжить работу и получить такое назначение, просто небольшая практика.
And that's another thing I would like to talk about as well.|И это еще одна вещь, о которой я хотел бы поговорить.
Cuz a lot of people say, wow, man Laz,|Потому что многие люди говорят, вау, чувак, Лаз,
that's a lot of commands,|это много команд,
that's a lot of command.|это большая команда.
Ladies and gentlemen, we're barely scratching the surface.|Дамы и господа, мы почти не касаемся поверхности.
Okay, barely scratching the surface because once you get out there,|Ладно, почти не царапая поверхность, потому что, как только вы выберетесь отсюда,
believe me, there's so many more commands that and again, depending on what job you're going to perform, and what company you're gonna go to.|поверьте мне, существует так много других команд, и опять же, в зависимости от того, какую работу вы собираетесь выполнять и в какую компанию вы собираетесь пойти.
There are certain commands you are not ever in your life going to type.|Есть определенные команды, которые вы никогда в жизни не будете вводить.
There's just way too many.|Их слишком много.
So we're always, you know, when we go from job to job let's say,|Итак, мы всегда, знаете ли, когда мы переходим с работы на работу, скажем,
you're one job for two or three years.|ты одна работа на два-три года.
You go to another job for two to three years, another job.|Вы переходите на другую работу на два-три года, другую работу.
Hopefully, that's not the case, but if that is the case you're gonna learn different things because each company doesn't do everything the same.|Надеюсь, это не так, но если это так, вы узнаете разные вещи, потому что каждая компания не делает все одинаково.
So you're gonna gain that experience.|Так ты получишь этот опыт.
I'm not saying that's a good thing.|Я не говорю, что это хорошо.
If you're gonna stay in one company for 50|Если ты собираешься остаться в одной компании на 50
years.|лет.
Hey, more power to you.|Эй, больше власти тебе.
If you can create your own business, and you'd be, and,|Если бы вы могли создать свой собственный бизнес, и вы были бы, и,
and you go successful and you're there for a 100 years.|и вы добиваетесь успеха, и вы там на 100 лет.
You know, that's even better, but again everybody does things differently.|Знаешь, так даже лучше, но опять же, все делают по-своему.
Everybody does things differently.|Все делают по-разному.
All right, let me log in.|Хорошо, позволь мне войти.
CISCO.|CISCO.
All right?|Отлично?
We go to global configuration.|Заходим в глобальную настройку.
We're gonna do the exclusion.|Мы сделаем исключение.
This is the 2.0 network, the 2.0 network.|Это сеть 2.0, сеть 2.0.
Let me go ahead and open this up all the way to here.|Позвольте мне продолжить и открыть это полностью здесь.
All right, so we're gonna do IP DHCP excluded addresses,|Хорошо, мы будем использовать IP-адреса без DHCP,
we're gonna go 192.168, 68.2.1.|мы пойдем 192.168, 68.2.1.
Okay, through 192.168.2.20, that's to make it the same as the other one.|Хорошо, через 192.168.2.20, чтобы он был таким же, как и другой.
Then we're gonna IP DH, DHCP, hello.|Тогда мы собираемся IP DH, DHCP, привет.
DHCP pool we'll call this a different pool.|Пул DHCP, мы назовем его другим пулом.
Let's call it Bob, okay?|Назовем его Бобом, хорошо?
And now we're gonna go ahead and do default router.|А теперь займемся роутером по умолчанию.
And then, it's 192.168.2.254 and then DNS.|Затем это 192.168.2.254, а затем DNS.
We're gonna be using the same DNS server on the other side.|Мы собираемся использовать тот же DNS-сервер на другой стороне.
So we're gonna use 192.168.1.2, and then the network is gonna be 192.168.2.0|Итак, мы будем использовать 192.168.1.2, а затем сеть будет 192.168.2.0.
255.255.255.0, Enter.|255.255.255.0, введите.
And yes, I am gonna do an illegal command for your certification.|И да, я сделаю незаконную команду для вашей сертификации.
DO WR, you can do that.|DO WR, вы можете это сделать.
All right, but just to see that, you know,|Хорошо, но просто чтобы увидеть это, знаете,
that it's there,|что это там,
I'll do a Ctrl+Z, which you probably can learn on your test either.|Я сделаю Ctrl + Z, что вы, вероятно, тоже узнаете на своем тесте.
But it takes me back to privilege mode.|Но это возвращает меня в привилегированный режим.
And then I'm gonna do triple start.|А потом сделаю тройной старт.
And there you go.|Вот и все.
I think another short command you can do is show IP DHCP pool.|Я думаю, что еще одна короткая команда, которую вы можете сделать, - это показать пул IP DHCP.
[UNKNOWN] Show, let's see.|[НЕИЗВЕСТНО] Покажи, посмотрим.
[SOUND] There it is.|[ЗВУК] Вот оно.
Show DHCP.|Показать DHCP.
Oh.|Ой.
Okay, show DHCP.|Ладно, покажи DHCP.
Oh, doesn't recognize it.|Ой, не узнает.
Oh, because it spelled it backwards.|О, потому что это написано наоборот.
Sorry.|Сожалею.
DHCP.|DHCP.
[LAUGH] Oh, leased, okay.|[СМЕХ] Ой, сдал, хорошо.
What he hasn't assigned any addresses yet.|Какие адреса он еще не присвоил.
All right, well, let's see.|Ладно, ладно, посмотрим.
Let's go here.|Пойдем сюда.
It assigned to 2.21, so I do have an address.|Он назначен на 2.21, поэтому у меня есть адрес.
So I'm interested now, out of curiosity,|Так что мне сейчас интересно, из любопытства,
why isn't it showing me, well I didn't set up a lease time, so that's why it didn't, it didn't show me the lease time.|почему он не показывает мне, ну, я не устанавливал время аренды, поэтому он не показывал мне время аренды.
Okay, and that's the only thing that it'll allow you to see.|Хорошо, и это единственное, что он позволит вам увидеть.
So, all right whatever.|Так что все в порядке.
So since I didn't setup a lease.|Итак, поскольку я не заключал договор аренды.
Which probably within the options to put in a leased time.|Что, вероятно, в пределах возможностей сдать в аренду.
Because, those are options if you were to do an actual DHCP pool within a Microsoft server.|Потому что это варианты, если вам нужно создать фактический пул DHCP на сервере Microsoft.
The leased time falls within the options.|Арендованное время находится в пределах возможностей.
But there you go.|Но вот и все.
There's DHCP, very simple,|Есть DHCP, очень простой,
very straightforward nothing difficult to configure.|очень просто ничего сложного в настройке.
You exclude the addresses, do that first.|Вы исключаете адреса, сделайте это в первую очередь.
Just as a rule of thumb.|Просто как практическое правило.
Then you go ahead and create your pool by giving it a name.|Затем вы создаете свой пул, дав ему имя.
You put in your default router which is your gateway address.|Вы указываете маршрутизатор по умолчанию, который является адресом вашего шлюза.
You put in a DNS server if you have one.|Вы устанавливаете DNS-сервер, если он у вас есть.
And then you put in the network, which includes the a subnet mask, so it knows exactly the range of IP addresses that, that it's working with, and|Затем вы вводите сеть, которая включает в себя маску подсети, чтобы она точно знала диапазон IP-адресов, с которыми она работает, и
it knows already what's excluded.|он уже знает, что исключено.
And you're done unless you have other options that you wanna go ahead and put on there.|И все готово, если у вас нет других вариантов, которые вы хотите использовать.
And you're done.|И вы сделали.
All right, this is the end of this lecture.|Хорошо, это конец лекции.
I will see you in the next one.|Увидимся в следующем.
[BLANK_AUDIO]|[BLANK_AUDIO]