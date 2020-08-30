D:\mailCloud\prjother\tmp\1\c92_How to configure intervlan routing Part1.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
All right.|Отлично.
Welcome back.|Добро пожаловать.
Are we ready to configure everything we've learned up to this point?|Готовы ли мы настроить все, что узнали к этому моменту?
Not as big as you think it was or was gonna be, but it's repetitious.|Не такой большой, как вы думаете, это было или должно было быть, но это одно и то же.
But that's okay, cuz that's what you need.|Но это нормально, потому что это то, что вам нужно.
Cuz repetition breeds retention.|Потому что повторение порождает удержание.
The more you do it, the more it becomes second nature and that's what needs to happen.|Чем больше вы это делаете, тем больше это становится вашей второй натурой, и это должно произойти.
So when you sit behind or in front of that computer, you take that certification.|Поэтому, когда вы сидите за или перед этим компьютером, вы получаете этот сертификат.
It will be like doing your alphabet, A, B,|Это будет похоже на алфавит, А, В,
C, D, E, F, G not a big deal.|C, D, E, F, G не имеет большого значения.
All right?|Отлично?
So we're gonna take if from the scratch.|Так что мы возьмем его с нуля.
From scratch, all the way up to the routers.|С нуля, вплоть до маршрутизаторов.
From layer one, [INAUDIBLE] layer one, I guess, but through all the way to layer three to routing.|Я думаю, от первого уровня, [НЕРАЗБОРЧИВО] до первого, но до третьего уровня и маршрутизации.
So let's put in, as you can see here,|Итак, давайте добавим, как вы можете видеть здесь,
let's explain the lab a little bit.|давайте немного объясним лабораторию.
We got three routers, three switches.|У нас есть три роутера, три коммутатора.
Now more than three switches.|Сейчас более трех переключателей.
Three sa, three switches per segment.|Три са, три переключателя на сегмент.
These switches right up here, they're gonna be your route bridges.|Эти переключатели прямо здесь, они будут вашими путевыми мостами.
All right?|Отлично?
These are gonna, so they'll be server switches,|Это будут переключатели серверов,
VTP multi-servers, which by default they,|Мульти-серверы VTP, которые по умолчанию они
all are remember.|все помнят.
But we'll be creating our VLANs up here.|Но мы будем создавать наши VLAN здесь.
We'll be trunking the appropriate ports,|Мы будем транслировать соответствующие порты,
which are either switch to switch or switch to router.|которые либо переключаются на коммутатор, либо переключаются на маршрутизатор.
We'll be manipulate expenditure, obviously since we want that to be the root bridge.|Мы будем управлять расходами, очевидно, поскольку мы хотим, чтобы это был корневой мост.
These will be VTP clients, so information can come down.|Это будут клиенты VTP, поэтому информация может передаваться.
They'll be part of the same domain.|Они будут частью одного домена.
But as you can see, this is VLAN 10 this is VLAN 20,|Но как видите, это VLAN 10, это VLAN 20,
this is VLAN 30 VLAN 40 VLAN 50 and VLAN 60.|это VLAN 30, VLAN 40, VLAN 50 и VLAN 60.
So we have six different VLANs that we're gonna be doing, not a big deal.|Итак, у нас есть шесть разных VLAN, которые мы собираемся создать, не беда.
That will all be created though, remember,|Но все это будет создано, помните,
the purpose will all create our VLANs up here.|цель - создать здесь наши VLAN.
And then they'll come down by themselves,|А потом они сами спустятся,
once we do the VTP trunking, and all that good stuff.|как только мы сделаем транкинг VTP и все такое хорошее.
All right.|Отлично.
Once we get to the routers, then we'll,|Как только мы перейдем к маршрутизаторам, мы,
we'll head into our inter VLAN connectivity.|мы перейдем к нашему внутреннему подключению VLAN.
Make sure we have connectivity within each pyramid, I like to call it.|Убедитесь, что у нас есть возможность соединения внутри каждой пирамиды, как я это называю.
Within each pyramid, we have connectivity,|Внутри каждой пирамиды у нас есть связь,
so we'll do the LAN interface first.|поэтому сначала займемся интерфейсом LAN.
And then we'll go ahead and route all the away across using a routing protocol.|А затем мы продолжим и маршрутизируем все, используя протокол маршрутизации.
Now the routing protocol that we're gonna use Is EIGRP.|Теперь протокол маршрутизации, который мы будем использовать, - это EIGRP.
Why did I choose that routing protocol?|Почему я выбрал именно этот протокол маршрутизации?
Because that's one of the main writing protocols that you'll be tested on and I still believe based on the last student that I talked to, it wasn't that long ago.|Потому что это один из основных протоколов письма, по которому вы будете тестироваться, и я все еще считаю, основываясь на последнем студенте, с которым я разговаривал, это было не так давно.
I'll say, maybe three weeks ago or so.|Я скажу, может, недели три назад или около того.
He told me that that's still EIGRP is the writing protocol of choice.|Он сказал мне, что предпочтительным протоколом записи по-прежнему является EIGRP.
So we'll be doing that.|Так что мы будем этим заниматься.
So let's start putting first our IPs on RPCs.|Итак, давайте начнем размещать наши IP-адреса в RPC.
So let's go to VLAN ten.|Итак, перейдем к VLAN десять.
All right.|Отлично.
And we'll put our IPs there right from scratch, so you can tell this is gonna be a long lesson.|И мы поместим туда наши IP-адреса с нуля, так что вы можете сказать, что это будет долгий урок.
192.168.10.1.|192.168.10.1.
I always like to use one for the host.|Мне всегда нравится использовать один для хозяина.
It doesn't matter if you like to use 20 or 30 or 40 or follow some sort of standard,|Неважно, нравится ли вам использовать 20, 30 или 40 или следовать каким-то стандартам,
what have you.|что там у вас.
As long as you know what your host address is and what your gateway,|Если вы знаете адрес вашего хоста и шлюз,
that's within the same subnet that you're in.|это в той же подсети, что и вы.
All right?|Отлично?
I've seen crazy things.|Я видел безумные вещи.
Where people are using summarize gateways,|Если люди используют шлюзы суммирования,
that doesn't make any sense.|в этом нет никакого смысла.
All right.|Отлично.
So make sure that your, you,|Так что убедитесь, что ваш, вы,
you know your IP, you know your IP's came,|вы знаете свой IP, вы знаете, что пришел ваш IP,
pretty much.|довольно много.
I'm just using default mask and then the gateway, I like to put the last available.|Я просто использую маску по умолчанию, а затем шлюз, мне нравится ставить последний доступный.
And again, that's what I like to use,|И снова, вот что мне нравится использовать,
Lazaro J.|Лазаро Дж.
Diaz likes to use.|Диаз любит использовать.
First, available for the host, last available for the gateway.|Первый, доступный для хоста, последний доступный для шлюза.
All right?|Отлично?
All right.|Отлично.
Let's click OK here.|Нажмите здесь ОК.
Center myself a little bit more, be sure you can see me.|Сосредоточьтесь немного больше, убедитесь, что вы меня видите.
All right.|Отлично.
Let's go over to the second PC within the same pyramid.|Перейдем ко второму ПК в той же пирамиде.
Let's maximize that and make sure you can see that.|Давайте максимизируем это и убедимся, что вы это видите.
[SOUND] Yes, you can.|[ЗВУК] Да, можно.
All right.|Отлично.
Put the IP address for that one, that was ten, this is twenty, I believe.|Поместите IP-адрес для этого, это было десять, это, кажется, двадцать.
192.168.20.1.|192.168.20.1.
Tab, tab.|Вкладка, вкладка.
192.168.20.254.|192.168.20.254.
Now, if you think I'm going too fast,|Теперь, если вы думаете, что я иду слишком быстро,
that's okay.|это нормально.
It's a video, you can pause.|Это видео, можно поставить на паузу.
All right?|Отлично?
No big deal there.|Ничего страшного.
That was 20, now we're gonna go to 30.|Было 20, теперь мы перейдем к 30.
[BLANK_AUDIO]|[BLANK_AUDIO]
192.168.30.1.|192.168.30.1.
Again, it's repetition.|Опять же, это повторение.
192.168.30.254.|192.168.30.254.
All right.|Отлично.
And if you see me make a mistake, just yell out and I'll know to fix it.|И если вы видите, что я совершаю ошибку, просто кричите, и я знаю, как это исправить.
All right.|Отлично.
Desktop.|Рабочий стол.
This is, oh, what is this?|Это, о, что это?
Yeah, we did 30, this is 40.|Да, мы сделали 30, это 40.
It is 40?|Это 40?
Yes, 40.|Да, 40.
192.168.40.1.|192.168.40.1.
192.168.40.254.|192.168.40.254.
[BLANK_AUDIO]|[BLANK_AUDIO]
Anyhow, when you guys do your CCNA exam,|Во всяком случае, когда вы, ребята, сдаете экзамен CCNA,
you will not be configuring all this kinda stuff.|вы не будете настраивать все эти подобные вещи.
You'll be finishing off a configuration or fixing a configuration,|Вы завершите настройку или исправите конфигурацию,
then the only thing that you do from scratch actually is the access list,|тогда единственное, что вы делаете с нуля, - это список доступа,
which we'll be covering shortly.|о котором мы скоро расскажем.
192.168.50.1, I believe.|192.168.50.1, я полагаю.
192.168.50.254.|192.168.50.254.
Oops, and yeah,|Ой и да,
[UNKNOWN] is the last PC 60.|[НЕИЗВЕСТНО] - это последний ПК 60.
[BLANK_AUDIO]|[BLANK_AUDIO]
492.168.60.1.|492.168.60.1.
Tab, tab.|Вкладка, вкладка.
192.168.60.254.|192.168.60.254.
Oops, dot 254.|Ой, точка 254.
All right.|Отлично.
All right.|Отлично.
So we got our PCs with their IP addresses,|Итак, мы получили наши ПК с их IP-адресами,
we don't have to worry about that now.|нам не о чем беспокоиться сейчас.
Now we're gonna go to the root bridges.|Теперь перейдем к корневым мостам.
We're gonna make these guys the root bridges.|Мы сделаем этих парней корневыми мостами.
We'll give them a name, obviously.|Разумеется, мы дадим им имя.
We're gonna work on one pyramid first and then we'll work our way across.|Сначала мы будем работать над одной пирамидой, а потом перейдем через нее.
So let's work on this one right here.|Так что давайте поработаем над этим прямо здесь.
Let's maximize it and we'll call this core one.|Давайте максимизируем его и назовем это основным.
Host name, core one.|Имя хоста, основное.
Let's capitalize that.|Давайте воспользуемся этим.
CORE.|CORE.
[UNKNOWN], no spaces.|[НЕИЗВЕСТНО], без пробелов.
Now lets make this the root bridge.|Теперь давайте сделаем это корневым мостом.
So we've gotta go SPAnningtree VLAN.|Итак, нам нужно использовать SPAnningtree VLAN.
Multiple VLANs, 1, 10, 20 PRIORITY,|Несколько сетей VLAN, 1, 10, 20 ПРИОРИТЕТ,
you want to make sure this is always going to be the root bridge, 0.|вы хотите убедиться, что это всегда будет корневой мост, 0.
All right.|Отлично.
We're gonna incru,|Мы собираемся вступить,
include a VTP domain name.|включить доменное имя VTP.
VTP DOMAIN, we'll call it CISCO.|ДОМЕН VTP, мы назовем его CISCO.
All right.|Отлично.
Now, it's changed from nothing to Cisco.|Теперь все изменилось с нуля на Cisco.
We're gonna go ahead and create the VLAN's.|Мы собираемся создать VLAN.
W e have to create two VLANS, ten and twenty.|Нам нужно создать два VLAN, десять и двадцать.
So VLAN ten, I want to use the same thing we did before.|Итак, VLAN десять, я хочу использовать то же самое, что и раньше.
Name Faculty, I will just make it teachers just to say, something different.|Назовите факультет, я просто скажу учителям, что-нибудь другое.
TEACHERS VLAN 20.|УЧИТЕЛЯ VLAN 20.
NAME STUDENT.|ИМЯ СТУДЕНТ.
All right?|Отлично?
And again, do you have to name them?|И опять же, надо их называть?
No.|Нет.
Should you?|Вы должны?
Yes, so we don't have to worry about, hey,|Да, так что нам не о чем беспокоиться, эй,
oh, VLAN ten is zero zero ten, you know,|о, VLAN десять - это ноль ноль десять, вы знаете,
not numbers, names.|не числа, а имена.
It makes life a whole lot easier, all right?|Это делает жизнь намного проще, понятно?
Exit.|Выход.
We're going to trunk ports now.|Сейчас мы собираемся соединить порты.
INTERFACE RANGE F0/22-24.|ДИАПАЗОН ИНТЕРФЕЙСА F0 / 22-24.
SWItch.|SWItch.
I tabbed.|Я вложил вкладки.
Port MODE.|РЕЖИМ порта.
Trunk.|Ствол.
Remember switch to switch, that's a trunk port.|Не забудьте переключиться на коммутатор, это магистральный порт.
Switch to router, that's a trunk port.|Переключитесь на маршрутизатор, это магистральный порт.
Keep that in mind.|Запомни.
All right, I'm gonna do a Ctrl+Z WR.|Хорошо, я сделаю Ctrl + Z WR.
Let's verify some stuff.|Давайте проверим кое-что.
Let's do a show VLAN.|Сделаем шоу VLAN.
All right there are my VLANs, TEACHERS and STUDENTS.|Хорошо, вот мои VLAN, УЧИТЕЛЯ и СТУДЕНТЫ.
I'm not gonna assign them though.|Но я не собираюсь их назначать.
That's not the point that I'm creating them there.|Дело не в том, что я их там создаю.
I'm creating there so if you have 100|Я создаю там, поэтому если у вас есть 100
VLANS,|ВЛАНС,
you can create those 100 VLANs on your,|вы можете создать эти 100 VLAN на своем,
on your root bridge and then because of being trunked,|на корневом мосту, а затем из-за того, что
it's gonna bring the ports bring the VLANs down to your client switches.|это приведет к тому, что порты подключат VLAN к вашим клиентским коммутаторам.
All right, now lets take a look at the VTP status, VTP mode set, yeah, VTP mode,|Хорошо, теперь давайте посмотрим на статус VTP, установленный режим VTP, да, режим VTP,
VTP mode status, mm-hm, VT.|Состояние режима VTP, мм-хм, ВТ.
[BLANK_AUDIO]|[BLANK_AUDIO]
Hello, all right, no wonder.|Привет, хорошо, неудивительно.
SWITCHPORT MODE STAT, no?|СТАТИСТИКА РЕЖИМА SWITCHPORT, нет?
Oh boy, Laz forgot?|О боже, Лаз забыл?
No way!|Ни за что!
[BLANK_AUDIO]|[BLANK_AUDIO]
What happened here?|Что здесь случилось?
[BLANK_AUDIO]|[BLANK_AUDIO]
I'm in the core switch yes.|Я в основном коммутаторе да.
Mm, this is interesting.|Мм, это интересно.
What is going on?|Что происходит?
[BLANK_AUDIO]|[BLANK_AUDIO]
How can there not be no VTP?|Как может не быть VTP?
Let's take a look.|Давайте взглянем.
Oh!|Ой!
[LAUGH].|[СМЕХ].
How about show VTP status?|Как насчет отображения статуса VTP?
How about that one?|Как насчет того?
I think that will work.|Я думаю, это сработает.
We wanna look, show, right?|Мы хотим посмотреть, показать, правда?
Wow.|Вот это да.
Okay there.|Хорошо.
Here's our show VTP status, we are taking a look at,|Вот наш статус шоу VTP, мы его рассмотрим,
hey this is CISCO is just the domain name.|эй, это CISCO, это просто доменное имя.
We have the revision number changed over here.|У нас здесь изменился номер версии.
We have actually 7 VLANs, 5,|Фактически у нас есть 7 VLAN, 5,
that originally were there plus the 2 more that we have.|которые изначально были там плюс еще 2, что у нас есть.
All right.|Отлично.
So, we can do some a little extra stuff.|Итак, мы можем сделать кое-что еще.
Not so much the basic housekeeping, but as far as the IP addressing scheme for VLAN one.|Не столько базовое обслуживание, сколько схема IP-адресации для VLAN one.
We have VLAN 10, VLAN 20, VLAN 30, all of that.|У нас есть VLAN 10, VLAN 20, VLAN 30 и все такое.
But we never did anything for VLAN one.|Но мы никогда ничего не делали для VLAN one.
And I'm just gonna do it on this one so you can see how things may occur.|И я просто сделаю это на этом, чтобы вы увидели, как все может произойти.
So I'm gonna go to global configuration.|Итак, я перейду к глобальной настройке.
I'm gonna go IP ADDRESS 192.168.1.0|Я пойду IP-АДРЕС 192.168.1.0
25, yes, 255.|25, да, 255.
[SOUND] See, right where I'm at.|[ЗВУК] Смотрите, вот где я.
INT VLAN 1, sorry.|INT VLAN 1, извините.
This will be inside the VLAN 1.|Это будет внутри VLAN 1.
IP ADDRESS 192.168.1.253,|IP-АДРЕС 192.168.1.253,
255.255.255.0, NO SHUT.|255.255.255.0, БЕЗ ОТКЛЮЧЕНИЯ.
Okay, and then we exit and then we go IP Default-gateway 192.168.1.254.|Хорошо, затем мы выходим, а затем переходим к IP-шлюзу по умолчанию 192.168.1.254.
All right, what did we do here?|Хорошо, что мы здесь делали?
We actually created an IP address for VLAN 1.|Фактически мы создали IP-адрес для VLAN 1.
We've done this before.|Мы делали это раньше.
And what this does, it actually gives you access to the switch via that IP scheme, all right?|И что это делает, это фактически дает вам доступ к коммутатору через эту IP-схему, хорошо?
The actual IP address of the switch is going to be 1.253, the gateway, which is the router's interface sub interface, that|Фактический IP-адрес коммутатора будет 1.253, шлюз, который является подчиненным интерфейсом интерфейса маршрутизатора, который
we're gonna create for VLAN 1.|мы собираемся создать для VLAN 1.
All right?|Отлично?
And we'll just do it on this one, so you can see how that works.|И мы просто сделаем это на этом, чтобы вы увидели, как это работает.
All right, so we're pretty much done here.|Итак, мы почти закончили.
Let's, we did already write it.|Давайте, мы это уже написали.
All right.|Отлично.
And, [SOUND] that's it, okay.|И [ЗВУК] все, хорошо.
So let's go down to the client switch on this side right here.|Итак, давайте перейдем к клиентскому коммутатору на этой стороне прямо здесь.
We're gonna do this switch right here.|Мы сделаем этот переключатель прямо здесь.
All right, let's maximize that.|Хорошо, давайте максимизировать это.
So this is gonna be the teacher switch.|Так что это будет смена учителя.
Right?|Правильно?
So we're gonna enable, CONFIG T, HOSTNAME TEACHERS.|Итак, мы собираемся включить CONFIG T, HOSTNAME TEACHERS.
Then we'll change the mode of, the operate,|Затем мы изменим режим работы,
operational mode of the switch to client.|рабочий режим переключения на клиентский.
So I'll switch port, oh, sorry.|Так что я переключу порт, извините.
[SOUND] VTP MODE CLIENT.|[ЗВУК] КЛИЕНТ РЕЖИМА VTP.
Right, now we are going to verify that those VLANs came down,|Хорошо, теперь мы собираемся проверить, что эти VLAN вышли из строя,
which I don't think because I forgot to trunk the ports.|что я не думаю, потому что я забыл соединить порты.
Do WR, I mean mean DO show VLAN, it did come down.|Сделайте WR, я имею в виду, что показывать VLAN, он действительно вышел.
Did we trunk the ports?|Мы транслировали порты?
We probably, yes we did, we did trunk the ports.|Мы, вероятно, да, сделали, мы сделали транкинговые порты.
I'm gonna verify anyway because you know me.|Я все равно проверю, потому что ты меня знаешь.
Let's do a show INT TRUNK.|Давайте сделаем шоу INT TRUNK.
Yes we did, okay.|Да, хорошо.
So we did trunk the ports.|Итак, мы сделали транкинг портов.
I forget from one minute to the next and my brain is going crazy.|Я забываю каждую минуту, и мой мозг сходит с ума.
I need blueberries.|Мне нужна черника.
All right, so now we have the VLANs that came down.|Хорошо, теперь у нас есть вышедшие из строя VLAN.
So now what we're gonna do is we're gonna assign the VLANs to a range of ports,|Итак, теперь мы собираемся назначить VLAN на ряд портов,
all right?|отлично?
[BLANK_AUDIO].|[BLANK_AUDIO].
Even though we're assigning the VLAN's,|Несмотря на то, что мы назначаем VLAN,
we're in client mode.|мы в клиентском режиме.
If we were to look at DO show VTP STAT, we are in Client.|Если бы мы посмотрели на DO show VTP STAT, мы находимся в Client.
All right?|Отлично?
But we can change the VLAN but we can't assign them.|Но мы можем изменить VLAN, но не можем их назначить.
All right.|Отлично.
So, INT RANGE F0/1-15.|Итак, INT RANGE F0 / 1-15.
Remember, you've got to put them in access port.|Помните, вы должны вставить их в порт доступа.
SWITCHPORT MODE ACCESS.|ДОСТУП В РЕЖИМ SWITCHPORT.
SWITCHPORT ACCESS VLAN.|SWITCHPORT ACCESS VLAN.
And, it's VLAN 10.|И это VLAN 10.
Now since we're here, we gonna go ahead and set up port security cuz we're already here.|Теперь, раз уж мы здесь, мы продолжим и настроим безопасность порта, потому что мы уже здесь.
Switchport port-security, that turns it on.|Switchport port-security, который его включает.
And a new tab while I wanna do this.|И новая вкладка, пока я хочу это сделать.
MAC sticky.|MAC липкий.
All right, if you recall, what that does,|Хорошо, если вы помните, что это значит,
it actually learns the MAC addresses of your clients dynamically.|фактически он динамически изучает MAC-адреса ваших клиентов.
But it puts an entry in the MAC address table as if it was static, all right?|Но он помещает запись в таблицу MAC-адресов, как если бы она была статической, понятно?
So, it's there forever, so.|Итак, это навсегда, так что.
Now we're gonna allow a maximum, we're gonna be really greedy,|Теперь мы позволим максимум, мы будем очень жадными,
a maximum of only one MAC address.|максимум только один MAC-адрес.
So if anybody wants and learns that MAC address, if somebody starts to switch out,|Итак, если кто-то хочет и узнает этот MAC-адрес, если кто-то начнет отключаться,
we're gonna go ahead and put a violation of shut, shut down.|мы пойдем дальше и установим нарушение "выключить, выключить".
Vio, short for violation shut.|Вио, сокращение от нарушения закрыто.
So if anybody tries to switch out computers on us and they don't tell us or anything like that.|Так что, если кто-то пытается переключить на нас компьютеры, и они нам ничего не говорят или что-то в этом роде.
Somebody just brings their laptop, wants to plug it in, instead of the desktop.|Кто-то просто приносит свой ноутбук, хочет подключить его вместо рабочего стола.
That's going to shut down the port, put it in error disabled, ERR disabled.|Это приведет к отключению порта, отключению ошибки и отключению ERR.
That's what's going to happen.|Вот что произойдет.
All right so, no one will be able to use that port.|Хорошо, никто не сможет использовать этот порт.
So it's up to you how many ports you want to go ahead and use.|Так что вам решать, сколько портов вы хотите использовать.
I mean, yeah, that you're gonna permit.|Я имею в виду, да, ты собираешься разрешить.
All right, the next thing that we're going to do is we're going to turn off spanning tree.|Хорошо, следующее, что мы собираемся сделать, это отключить связующее дерево.
Remember, spanning tree is a good thing because spanning tree prevents what?|Помните, что связующее дерево - это хорошо, потому что связующее дерево предотвращает что?
Switching loops.|Шлейфы переключения.
But these are end devices.|Но это конечные устройства.
There's no bridge protocol that are units going from the PC to the switch.|Нет никакого протокола моста, по которому блоки передаются от ПК к коммутатору.
So what's gonna happen is we're gonna go ahead and turn off spanning tree safely on those ports.|Итак, что произойдет, мы продолжим и безопасно отключим связующее дерево на этих портах.
That way they can be put in designated forwarding status very quickly, right away, almost intansta, intanstaneously,|Таким образом, они могут быть очень быстро и мгновенно переведены в назначенный статус пересылки, почти сразу же, интуитивно,
instantaneously, instant, instantly?|мгновенно, мгновенно, мгновенно?
Maybe?|Может быть?
Okay.|Ладно.
Spanning-tree PORT fast.|Spanning-tree ПОРТ быстро.
Then it gives you a big old warning.|Тогда это дает вам большое старое предупреждение.
You sure?|Вы уверены?
Yes, we're sure.|Да, мы уверены.
So, we do this spanning-tree port fast.|Итак, мы быстро делаем этот порт связующего дерева.
That turns off spanning tree on there.|Это отключает связующее дерево.
So let's just be careful you don't create a switch and loop.|Так что давайте просто будем осторожны, чтобы не создавать переключение и цикл.
So since we need to be careful, we're gonna do a Spanning-tree, Bpduguard, Bpduguard enable.|Итак, поскольку нам нужно быть осторожными, мы сделаем Spanning-tree, Bpduguard, Bpduguard enable.
All right, what that does is puts that sentry, that guard on there.|Хорошо, это ставит там того часового, этого охранника.
That's watching to see if there is any BPUs coming towards it, and if there is any BPUs coming towards it,|Это следит за тем, чтобы увидеть, идут ли к нему какие-либо BPU, и есть ли какие-либо BPU, приближающиеся к нему,
it's going to shut down the port,|он собирается закрыть порт,
put it in the same state as the port security is disabled.|перевести его в то же состояние, что и защита порта отключена.
It'll shut down that port altogether.|Он полностью отключит этот порт.
All right, so we manipulate its [UNKNOWN],|Хорошо, поэтому мы манипулируем его [НЕИЗВЕСТНО],
we assigned the VLANs, we did port security and we're guarding against anything from having any switching loop.|мы назначали сети VLAN, обеспечивали безопасность портов и защищаемся от любых петель коммутации.
So we're just gonna do a do WR from right here.|Так что мы просто сделаем WR прямо здесь.
And then what we're gonna do is the IP addressing for VLAN 1, and VLAN 1, remember the 1 on top.|И тогда мы собираемся назначить IP-адреса для VLAN 1 и VLAN 1, помните цифру 1 сверху.
The route bridge is 253, this will be 252,|Маршрутный мост 253, это будет 252,
so IP address 192.168.1.252,|итак IP-адрес 192.168.1.252,
255.255.255.0.|255.255.255.0.
And we do a NO SHUT.|И мы НЕ ЗАКРЫВАЕМ.
And then we exit out and put in the default gateway.|Затем мы выходим и устанавливаем шлюз по умолчанию.
Remember, Cisco says that you need a default gateway if you're trying to access your switch.|Помните, Cisco говорит, что вам нужен шлюз по умолчанию, если вы пытаетесь получить доступ к своему коммутатору.
You want to get inside the switch from a remote location,|Вы хотите попасть внутрь коммутатора из удаленного места,
from another broadcast domain, you need a default gateway, which is 1.254.|из другого широковещательного домена вам понадобится шлюз по умолчанию - 1.254.
All right, and we take a look at the show VLANs.|Хорошо, и мы взглянем на показанные VLAN.
You see that VLAN10, we have our ports assigned all the way to 15.|Вы видите, что VLAN10, у нас все порты назначены на 15.
So that's good to go.|Так что это хорошо.
We know that these ports are already trunked,|Мы знаем, что эти порты уже подключены,
that's why the information flowed down.|вот почему информация потекла вниз.
We looked at the VTP status, we saw that it was Cisco.|Посмотрели статус VTP, увидели, что это Cisco.
And we do show port-security,|И мы показываем безопасность портов,
you'll be able to see the type of security that's on there.|вы сможете увидеть, какой тип безопасности там установлен.
It's on the, all these 15 ports.|Это все эти 15 портов.
You're only allowing one MAC address.|Вы разрешаете только один MAC-адрес.
So far it has learned no MAC addresses,|Пока он не узнал MAC-адреса,
there's been no violations and when there is a violation it will shut down the port.|Нарушений нет, и при их обнаружении порт отключает.
That's what that means.|Вот что это значит.
All right, so we're done with the teacher switch, you see how quickly this can,|Хорошо, мы закончили с переключателем учителей, вы видите, как быстро это может,
once it becomes, it just rolls, it just,|когда становится, просто катится, просто,
you just roll it.|вы просто катите это.
All right, let's maximize this one.|Хорошо, давайте максимизируем это.
This will be the, student's.|Это будет студенческий.
So enable, CONFI T.|Итак, включите CONFI T.
And you may see CONFI and then T,|И вы можете увидеть CONFI, а затем T,
as long as you type enough of the command in the real world,|пока вы набираете достаточно команды в реальном мире,
all right, not in your CCNA exam, it'll understand what you're typing.|хорошо, не на вашем экзамене CCNA, он поймет, что вы печатаете.
If there's no other command that starts with CONFI,|Если нет другой команды, начинающейся с CONFI,
it'll understand what you're trying to type.|он поймет, что вы пытаетесь напечатать.
Hostname is oh no, I mean the teachers,|Имя хоста - о нет, я имею в виду учителей,
or no, they say the students.|или нет, говорят студенты.
Okay?|Ладно?
[COUGH] Switch port, VTP MODE,|[COUGH] Порт переключения, РЕЖИМ VTP,
sorry, VTP MODE CLIENT.|извините, КЛИЕНТ РЕЖИМА VTP.
So now we're in client mode.|Итак, теперь мы в клиентском режиме.
Now we'll say, DO SHOW VLAN.|Теперь скажем: ПОКАЗАТЬ VLAN.
There is my VLANs, Ctrl+C, this is gonna be for the students.|Вот мои VLAN, Ctrl + C, это будет для студентов.
So INT RANGE same port.|Итак, INT ДИАПАЗОН тот же порт.
F0/1-15.|F0 / 1-15.
SWITCHPORT MODE, you'd have to turn it into an access point first.|SWITCHPORT MODE, вам нужно сначала превратить его в точку доступа.
ACCESS, SWITCHPORT ACCESS.|ДОСТУП, ДОСТУП К SWITCHPORT.
[BLANK_AUDIO]|[BLANK_AUDIO]
VLAN 20.|VLAN 20.
While we're here, let's do port security.|Пока мы здесь, займемся безопасностью портов.
SWITCHPORT, port-security, [UNKNOWN].|SWITCHPORT, безопасность порта, [НЕИЗВЕСТНО].
[BLANK_AUDIO]|[BLANK_AUDIO]
Maximum of one.|Максимум один.
Now we're gonna go ahead and do a viol of shut, violation of shut.|Теперь мы продолжим и сделаем нарушение затвора, нарушение затвора.
All right.|Отлично.
We're gonna turn off spanning tree, and then we're gonna guard against it.|Мы отключим остовное дерево, а затем защитимся от него.
So spanning-tree BPU guard enable, and what we will do then is put in the IP address.|Итак, включена защита связующего дерева BPU, и все, что мы будем делать, будет помещено в IP-адрес.
The previous one was 252 for VLAN 1, so this should be 251.|Предыдущее значение было 252 для VLAN 1, поэтому должно быть 251.
So it's going to be INT VLAN 1|Так что это будет INT VLAN 1
IP ADDRESS 192.168.1.251,|IP-АДРЕС 192.168.1.251,
255.255.255.0.|255.255.255.0.
NO SHUT.|НЕТ ВЫКЛЮЧЕНИЯ.
We need a gateway.|Нам нужен шлюз.
So we exit out of here and then we do IP default-gateway 192.168.1.254.|Итак, мы выходим отсюда и делаем IP-шлюз по умолчанию 192.168.1.254.
Now, you will be, probably something like this for the gateway assignment, and the IP address assignment for VLAN 1.|Теперь у вас будет что-то вроде этого для назначения шлюза и назначения IP-адреса для VLAN 1.
They'll probably test you as far as, hey,|Они, вероятно, будут проверять вас, насколько, эй,
where do you put them?|куда вы их положите?
Remember, the default gateway for the switch is in global configuration.|Помните, что шлюз по умолчанию для коммутатора находится в глобальной конфигурации.
Where the IP address that you're going to use for VLAN 1 is within interface VLAN 1.|Если IP-адрес, который вы собираетесь использовать для VLAN 1, находится в интерфейсе VLAN 1.
And don't forget to do a NO SHUT.|И не забудьте сделать ОТКЛЮЧЕНИЕ.
Don't forget to do a NO SHUT because it's off by default.|Не забудьте сделать ОТКЛЮЧЕНИЕ, потому что по умолчанию он выключен.
All right, so, we're done pretty much with the first pyramid.|Итак, мы закончили с первой пирамидой.
I just want to make sure that my VLANs are assigned.|Я просто хочу убедиться, что мои VLAN назначены.
Show VLAN, and there's my student VLANs.|Покажи VLAN, а там мои студенческие VLAN.
It is assigned.|Назначено.
And if we just go to SHOW START and work our way down, you see everything that we've done.|И если мы просто перейдем к ПОКАЗАТЬ СТАРТ и спустимся вниз, вы увидите все, что мы сделали.
All the configuration's right there.|Вся конфигурация прямо здесь.
Always verify your work, especially in the certification.|Всегда проверяйте свою работу, особенно в аттестации.
Make sure if it's a routing, let's say you're doing the routing, okay?|Убедитесь, что это маршрутизация, допустим, вы выполняете маршрутизацию, хорошо?
If you are routing, make sure you can ping.|Если вы выполняете маршрутизацию, убедитесь, что вы можете пинговать.
You sit there on that one router or whatever it is, and try to ping everybody else, and that's the goal.|Вы сидите на этом одном маршрутизаторе или на чем-то еще и пытаетесь пинговать всех остальных, и это цель.
Whatever the goal is,|Какой бы ни была цель,
make sure that you can accomplish that goal before you click Next.|убедитесь, что вы можете достичь этой цели, прежде чем нажимать «Далее».
Once you click Next, that question is gone.|Как только вы нажмете «Далее», этот вопрос исчезнет.
It's not coming back,all right?|Он не вернется, понятно?
All right, so we're done with this particular pyramid.|Хорошо, мы закончили с этой конкретной пирамидой.
Let's go to the next pyramid, let me click Save here.|Пойдем к следующей пирамиде, позволь мне нажать «Сохранить здесь».
We don't want to present any information.|Мы не хотим предоставлять какую-либо информацию.
So this is gonna be core two now.|Итак, это будет два ядра.
Essentially everything is gonna, well,|По сути, все будет хорошо,
this is gonna be VLANs 30 and 40.|это будут VLAN 30 и 40.
So it's 1, 30, 40 for the spanning-tree.|Итак, для остовного дерева это 1, 30, 40.
[BLANK_AUDIO]|[BLANK_AUDIO]
So we do ENABLE, all right?|Итак, делаем ENABLE, хорошо?
CONFI T hostname, CORE2.|Имя хоста CONFI T, CORE2.
spanning-tree, VLAN1,|связующее дерево, VLAN1,
30, 40, PRIORITY 0.|30, 40, ПРИОРИТЕТ 0.
All right, we're going to create the VLAN.|Хорошо, мы собираемся создать VLAN.
VLAN 40.|VLAN 40.
NAME accounting, VLAN 50.|Учет ИМЯ, VLAN 50.
NAME HR, what have you.|ИМЯ HR, что у тебя.
It doesn't really matter.|Это не имеет значения.
Let's create our VTP domain,|Создадим наш VTP-домен,
let's call it.|давай назовем это.
Let's just call it CISCO, just keep everything [COUGH] great,|Давайте назовем это CISCO, просто держите все [КАШЕ] в порядке,
complete different locations so but.|завершить разные места так, но.
We'll just keep saying Cisco, already can,|Мы просто будем говорить Cisco, уже может,
not too creative today to write Cisco or to write something else.|не слишком креативен сегодня, чтобы писать Cisco или писать что-то еще.
So we got a VTP domain name.|Итак, мы получили доменное имя VTP.
We created our VLANs, we did our spanning tree, we went to trunk our port.|Мы создали наши VLAN, мы создали связующее дерево, мы перешли к транкингу для нашего порта.
So we gotta go int range and you don't always have to use range.|Итак, нам нужно использовать диапазон int, и вам не всегда нужно использовать диапазон.
You can do it one by one by one by one by one.|Вы можете делать это один за другим.
Just go inside each interface and trunk that particular interface.|Просто войдите в каждый интерфейс и соедините этот конкретный интерфейс.
You don't have to use a range.|Вам не обязательно использовать диапазон.
The reason I do a range is because I put things in, in this particular order so I can use a range for that.|Причина, по которой я делаю диапазон, заключается в том, что я помещаю вещи в этом конкретном порядке, поэтому я могу использовать для этого диапазон.
INT RANGE F0/22-24.|ВНУТРЕННИЙ ДИАПАЗОН F0 / 22-24.
SWITCHPORT MODE TRUNK,|РЕЖИМ SWITCHPORT TRUNK,
DO WR, do a Ctrl+Z.|DO WR, нажмите Ctrl + Z.
Remember you guys can do DO WR or Ctrl+Z,|Помните, что вы, ребята, можете использовать DO WR или Ctrl + Z,
you probably can, no,|ты, наверное, можешь, нет,
I don't think you can do Ctrl+Z.|Я не думаю, что вы можете использовать Ctrl + Z.
You have to type exit, exit, okay, and do a copy, run, start.|Вам нужно ввести exit, exit, ok и сделать копию, запустить, запустить.
But again, you're not going to be configuring anything from scratch.|Но опять же, вы не собираетесь ничего настраивать с нуля.
Right, so let's do a SHOW command.|Хорошо, давайте сделаем команду SHOW.
SHOW VLAN.|ПОКАЗАТЬ VLAN.
There are two VLANs, 40 and 50.|Есть две VLAN: 40 и 50.
Again, this is the root bridge.|Опять же, это корневой мост.
How can we see this?|Как мы можем это увидеть?
Show spanning tree.|Показать остовное дерево.
There is, this is the route bridge it's telling you, all right?|Это маршрутный мост, о котором вы говорите, хорошо?
[NOISE] right here.|[NOISE] прямо здесь.
Priority of 1, right, for VLAN1.|Приоритет 1, справа, для VLAN1.
Okay?|Ладно?
And there you see that's designated LRN,|И вот вы видите, что это обозначено LRN,
I've never seen LRN, but okay.|Я никогда не видел LRN, но ладно.
Cost of 19, you know that's [INAUDIBLE]|Стоимость 19, вы знаете, что это [НЕРАЗБОРЧИВО]
and then the priority is 40.|а затем приоритет 40.
Okay, because 0 plus 40 is 40.|Хорошо, потому что 0 плюс 40 равно 40.
All right?|Отлично?
But it's the root bridge, for all these VLANs.|Но это корневой мост для всех этих VLAN.
So, that's how you see that.|Итак, вот как вы это видите.
And again, for the, the test, you're only gonna need to know hey,|И снова, для теста тебе нужно только знать, эй,
there's only one spanning tree, we're on VLAN.|есть только одно связующее дерево, мы находимся в VLAN.
So, there's your spanning tree.|Итак, вот ваше остовное дерево.
Show VTP status.|Показать статус VTP.
There it's right there.|Вот оно прямо там.
We got, two more VLANs because you see some right there.|У нас есть еще две VLAN, потому что вы видите некоторые прямо там.
You see the domain name on CISCO.|Вы видите доменное имя на CISCO.
Cool.|Прохладно.
So, let's put in now the boom boom boom boom.|Итак, давайте теперь вставим бум-бум-бум-бум.
No that's it, we trunked the ports,|Нет, все, мы подключили порты,
showing trunk, showing trunk.|показаны ствол, показаны ствол.
And, we can't see 24 cuz of the router, so 22 and 23.|И мы не можем видеть 24 из-за маршрутизатора, поэтому 22 и 23.
Cool.|Прохладно.
So, we're done here.|Итак, мы закончили.
We're done here.|Здесь мы закончили.
We're not going to do VLAN 1.|Мы не собираемся делать VLAN 1.
I just wanted to VLAN 1 in the first one so you can see what it was.|Я просто хотел включить VLAN 1 в первый, чтобы вы могли видеть, что это было.
All right so we go to the this will be the accounting switch cuz we have accounting [COUGH] NHR.|Хорошо, мы переходим к переключателю бухгалтерского учета, потому что у нас есть бухгалтерский учет [КАШЕТ] NHR.
So config t, host name, ACCT,|Итак, config t, имя хоста, ACCT,
Switch VTP mode client.|Переключить клиент в режиме VTP.
All right?|Отлично?
Do show V LAN, make sure.|Покажи V LAN, убедись.
There they are.|Там они.
Do a Ctrl+C, so this is the accounting,|Сделайте Ctrl + C, так что это учет,
so, I'm gonna assign my ports to 40.|Итак, я назначу свои порты 40.
Switch interface, I don't know why I wanna keep writing switch port.|Интерфейс коммутатора, я не знаю, почему я хочу продолжать писать порт коммутатора.
Interface range F0/1-15.|Диапазон интерфейса F0 / 1-15.
Switch port.|Порт коммутатора.
Mode access.|Доступ к режиму.
And this is why I tab switch port mode access.|Вот почему я вкладываю переключение в режим порта.
Switchport access, vlan40.|Доступ к коммутатору, vlan40.
Since we're here, we're gonna do switchport port-security.|Поскольку мы здесь, мы займемся безопасностью портов коммутатора.
MAC sticky.|MAC липкий.
Maximum of only one MAC address.|Максимум только один MAC-адрес.
And a violation, vio, of shut, shut down the port.|И нарушение, ви, отключения, закрытие порта.
And let's turn off spanning trees.|А давайте отключим остовные деревья.
Spanning-tree portfast.|Spanning-tree portfast.
Big ole warning.|Большое оле предупреждение.
And then we're gonna guard against anybody plugging anything into it,|И тогда мы будем защищаться от того, чтобы кто-нибудь что-нибудь в него вставлял,
by putting spanning-tree bpduguard enable,|включив связующее дерево bpduguard,
all right?|отлично?
And we're done with the accounting.|И мы закончили с бухгалтерией.
We're done, you see this is quick, quick,|Мы закончили, вы видите, это быстро, быстро,
boom, boom, boom, boom.|стрела, стрела, стрела, стрела.
Obviously I'm tabbing, I'm doing up arrows, something that you can do,|Очевидно, я использую табуляцию, делаю стрелки вверх, что-то, что вы можете сделать,
but you won't be doing this.|но ты не будешь этого делать.
You just need to understand what's going on, that's what we did in the previous videos, or previous lessons about spanning|Вам просто нужно понять, что происходит, это то, что мы делали в предыдущих видео или предыдущих уроках по охвату
trees and what they are.|деревья и что они собой представляют.
Now it's just a matter of just configuring, configuring, configuring,|Теперь осталось просто настроить, настроить, настроить,
doing the commands so you can see how it's done.|выполняя команды, чтобы вы могли видеть, как это делается.
Other than that you're not going to configure spanning tree, or anything like that.|Кроме этого, вы не собираетесь настраивать связующее дерево или что-то в этом роде.
You need to understand it.|Вам нужно это понять.
[BLANK_AUDIO]|[BLANK_AUDIO]
Enable config T.|Включите config T.
Config, conf t p, all right?|Конфиг, конф т п, хорошо?
And this will be the we have what HR?|И какой у нас HR будет?
So this will be the HR switch, host name [BLANK_AUDIO]|Итак, это будет переключатель HR, имя хоста [BLANK_AUDIO]
HR, let's capitalize that.|HR, давайте использовать это с большой буквы.
All right [COUGH] VTP mode.|Хорошо [КАШЕ] Режим VTP.
Client.|Клиент.
DO SH VLAN.|ДЕЛАЙТЕ SH VLAN.
There it is.|Вот оно.
So interface range, F0/1/15,|Итак, диапазон интерфейса, F0 / 1/15,
dash 15 I should say.|тире 15 я бы сказал.
So switch port.|Итак, переключите порт.
Mode Access.|Доступ к режиму.
Switchport Access VLAN 50.|Switchport Access VLAN 50.
Then, Switchport, port-security.|Затем Switchport, порт-безопасность.
Try not to tab,|Старайтесь не вкладывать,
gonna up arrow.|собираюсь стрелка вверх.
Mac sticky, remember what the sticky's for, learning dynamically,|Mac липкий, помните, для чего он липкий, динамическое обучение,
enters it statically.|входит в него статически.
Max one vio shut, then turn off spanning trees, spanning tree.|Закрывайте максимум один фиалку, затем выключайте остовные деревья, остовное дерево.
Now I gotta do that spanning-tree portfast.|Теперь мне нужно сделать этот порт связующего дерева.
And then spanning-tree, bdpuguard enable.|А затем связующее дерево, включение bdpuguard.
DO WR, let's check to see.|DO WR, давайте проверим.
SH VLAN.|SH VLAN.
There's our VLANs right there.|Вот и наши VLAN.
Boom, everything's trunked.|Бум, все в багажнике.
We know that from up above.|Мы знаем это сверху.
So, we're good to go here.|Итак, мы готовы идти сюда.
One more pyramid.|Еще одна пирамида.
One more pyramid.|Еще одна пирамида.
You saying, Jiminy Crickets, how many pyramids?|Вы говорите, сверчки Джимини, сколько пирамид?
My god.|О Господи.
But, the more you do it,|Но чем больше вы это делаете,
the more it becomes second nature.|тем более это становится второй натурой.
You'll go out there and you'll be blindfolded [SOUND] and configuring this stuff, all right?|Вы пойдете туда, и вам завяжут глаза [ЗВУК] и вы настроите все это, хорошо?
[COUGH] Last pyramid, bear with me, bear with me.|[Кашляет] Последняя пирамида, неси меня, неси меня.
All right, I think you can hang on in there.|Хорошо, я думаю, ты можешь там продержаться.
You can always fast forward me, all right?|Вы всегда можете перемотать меня вперед, хорошо?
So, enable this will be config T, core 3,|Итак, включим это будет config T, core 3,
no spaces.|без пробелов.
How about putting hostname core3, Laz?|Как насчет того, чтобы указать имя хоста core3, Laz?
Hostname core3.|Имя хоста core3.
There you go.|Вот так.
Should have this in a notepad.|Должно быть это в блокноте.
[SOUND] Be done.|[ЗВУК] Готово.
All right, hostname core3,|Хорошо, имя хоста core3,
VTP domain.|Домен VTP.
Again we'll call it Cisco.|Мы снова назовем его Cisco.
So we went from nothing to Cisco, so VLAN,|Итак, мы пошли с нуля на Cisco, поэтому VLAN,
what VLAN is this?|что это за VLAN?
Six, is this.|Шесть, вот это.
[BLANK_AUDIO]|[BLANK_AUDIO]
Did I do something that I shouldn't have done?|Я сделал что-то, чего не должен был делать?
[BLANK_AUDIO]|[BLANK_AUDIO]
There should of been 30 and 40, right?|Должно быть 30 и 40, верно?
I think I made a boo-boo.|Я думаю, что засмеялся.
Sure did, I put 40 and 50 over here where it should've been 30 and 40.|Конечно, я поставил здесь 40 и 50, где должно было быть 30 и 40.
But, that's okay, cuz I'm not gonna reconfigure it.|Но это нормально, потому что я не собираюсь его перенастраивать.
So, this one here is.|Итак, вот этот.
[BLANK_AUDIO]|[BLANK_AUDIO]
40.|40.
So, what we'll do is, we're just gonna swap this over here.|Итак, что мы сделаем, мы просто поменяем это здесь.
Put this over here.|Положи это сюда.
That's 40, and then this is 50 over here,|Это 40, а вот здесь 50,
and we'll just put 30 over here.|и мы просто положим сюда 30.
How about that one?|Как насчет того?
Slick, huh?|Ловко, а?
And this thing's 40 and 50.|А этой штуке 40 и 50.
We're good to go so that means we gotta change the IP addressing scheme on the computer.|Мы в порядке, это означает, что нам нужно изменить схему IP-адресации на компьютере.
So let's put here, that's what I get for trying to go too fast, 40.1 and then we'll do 40.254.|Итак, давайте поставим здесь, что я получаю, пытаясь идти слишком быстро, 40,1, а затем мы сделаем 40,254.
[BLANK_AUDIO]|[BLANK_AUDIO]
Obviously this wasn't gonna,|Очевидно, этого не произошло,
in a real world scenario you'd have to reconfigure it to the appropriate VLANs.|в реальном сценарии вам придется перенастроить его на соответствующие VLAN.
But since we're not, you just gotta understand the concepts,|Но поскольку это не так, вам просто нужно понять концепции,
this is the easiest quick fix, all right?|это самое простое быстрое решение, хорошо?
So now this became VLAN 50 and before we do VLAN 30 and 60 in the last one 30 and 60, all right.|Итак, теперь это стало VLAN 50, и до того, как мы сделаем VLAN 30 и 60 в последних 30 и 60, хорошо.
Core3.|Core3.
Oh, again, so we'll do VLAN 30.|О, опять же, мы сделаем VLAN 30.
Name registrar.|Имя регистратора.
And VLAN 60 name executive.|А VLAN 60 назовите исполнителем.
Executive.|Должностное лицо.
That's right.|Это правильно.
So, we did the domain name, oh, well then we do the spanning tree.|Итак, мы сделали доменное имя, ну а потом мы делаем связующее дерево.
Did we do the spanning tree already?|Мы уже сделали остовное дерево?
No we didn't.|Нет, мы этого не сделали.
SPAnning-tree VLAN 1,|SPAnning-tree VLAN 1,
30, 60, okay?|30, 60, хорошо?
Now I need to check that on the other VLAN as well.|Теперь мне нужно проверить это и в другой VLAN.
On the other core switch, see if I did it correctly.|Посмотрите, правильно ли я все сделал на другом переключателе ядра.
Or if we're to a match, the VLANs that are created.|Или, если мы подходим к совпадению, создаваемые VLAN.
So there's 1, 30, and 60, trunk the ports.|Итак, есть 1, 30 и 60, соедините порты.
So we gotta go, let's see, we've created the domain.|Итак, нам пора, посмотрим, мы создали домен.
We did the host name, created the VLANs,|Мы сделали имя хоста, создали VLAN,
did the spanning tree, okay?|остовное дерево, хорошо?
And we didn't finish the spanning tree,|И остовное дерево мы не доделали,
cuz priority 0.|Потому что приоритет 0.
There we go.|Вот и все.
Then, [COUGH] we're gonna go ahead and the trunk the ports, int range F0/1-15.|Затем, [КАШЕ], мы продолжим и соединим порты, int range F0 / 1-15.
SWItchport mode trunk.|SWItchport режим транка.
DO WR.|DO WR.
Ctrl+Z, SH VLAN, 30 and 60, okay?|Ctrl + Z, SH VLAN, 30 и 60, хорошо?
And then trunk ports, SH TRUNK, SH INT TRUNK.|И затем порты транка, SH TRUNK, SH INT TRUNK.
[BLANK_AUDIO]|[BLANK_AUDIO]
I just trunked them.|Я их только что загнал.
Config T, CONF T INT RANGE F0/1,|Config T, CONF T INT RANGE F0 / 1,
oh, gotcha.|ой, попался.
22-24.|22-24.
Switchport mode trunk, there you go.|Транк в режиме Switchport, вот и все.
SH INT TRUNK, yeah, there|SH INT TRUNK, да, там