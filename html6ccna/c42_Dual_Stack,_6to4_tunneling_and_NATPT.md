D:\mailCloud\prjother\tmp\1\c42_Dual Stack, 6to4 tunneling and NATPT.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
Welcome back, everyone, and welcome to the transition mechanism.|С возвращением, все, и добро пожаловать в механизм перехода.
Now, what you see here, obviously you can tell by the IP addressing scheme,|Теперь то, что вы видите здесь, очевидно, можно определить по схеме IP-адресации,
that yes, we personally submitted this in IPv6, mm-hm.|что да, мы лично отправили это в IPv6, мм-хм.
And we use our own little scheme, not somebody else's scheme that they just decided to put on the board and just tell you what to do.|И мы используем нашу собственную маленькую схему, а не чью-то еще схему, которую они просто решили выложить на доску и просто сказать вам, что делать.
No, no, no, no, no.|Нет-нет-нет-нет-нет.
We did our own IPv scheme.|Мы сделали свою схему IPv.
And what we're doing is, and I'll show you shortly when I open up a router,|И что мы делаем, и я покажу вам вскоре, когда открою роутер,
that we're running two, two routing protocols at the same time.|что мы запускаем два, два протокола маршрутизации одновременно.
That's what's cool because we have three different transition mechanisms.|Это круто, потому что у нас есть три разных механизма перехода.
Dual stack, 64 tunneling and NAT-PT, okay?|Двойной стек, 64 туннелирования и NAT-PT, хорошо?
But, and we're gonna talk about pretty much all three of these,|Но, и мы поговорим почти обо всех трех из них,
in this one video.|в этом видео.
There's no need to do separate videos for each one or anything like that because really for the examination they're not gonna ask you|Нет необходимости делать отдельные видео для каждого или что-то в этом роде, потому что на самом деле для обследования вас не спросят
all these different type of things.|все эти разные вещи.
But one of the ones that I like the most,|Но один из тех, которые мне нравятся больше всего,
is the dual stack, the dual stack.|это двойной стек, двойной стек.
All right, let me go ahead and let's open up this router right here, hey,|Хорошо, позвольте мне продолжить и давайте откроем этот маршрутизатор прямо здесь, эй,
look it worked the first time around,|посмотри, это сработало в первый раз,
ain't that lovely.|не так уж и красиво.
Let me maximize that, so let me get on this side, so you can see.|Позвольте мне максимизировать это, так что позвольте мне встать на эту сторону, чтобы вы могли видеть.
Cool.|Прохладно.
And I want to go ahead and open up,|И я хочу идти вперед и открываться,
username LDIAZ, password CISCO [SOUND].|имя пользователя LDIAZ, пароль CISCO [ЗВУК].
All right.|Отлично.
And that wasn't it.|И это было не так.
LDIAZ, password CISCO.|ЛДИАЗ, пароль CISCO.
All right, so that's very easy.|Хорошо, это очень просто.
Instead of going around the whole password reset thing, I've learned a trick.|Вместо того, чтобы обойти весь процесс сброса пароля, я научился трюку.
That actually one of my students, from Ohio showed me.|Это мне показал один из моих студентов из Огайо.
Let's go here.|Пойдем сюда.
Click on the interface, go back, aha, we bypassed it inside the router, cool.|Нажимаем на интерфейс, возвращаемся, ага, внутри роутера обошли, круто.
Can't [LAUGH] do it with the real router,|Не могу [СМЕХ] сделать это с настоящим роутером,
but you can do it with this.|но вы можете сделать это с этим.
So I'm in there, I'm not gonna change any passwords,|Так что я там, я не собираюсь менять пароли,
since I know how to get around it anyway,|поскольку я все равно знаю, как это обойти,
all right?|отлично?
So I'm gonna go ahead, and I'm gonna do a show start, to show you.|Итак, я пойду вперед и начну шоу, чтобы показать вам.
Now remember when you are routing in IPv6,|Теперь помните, когда вы выполняете маршрутизацию в IPv6,
one of the first things that you need to type is IPv6 unicast routing.|Одна из первых вещей, которую вам нужно ввести, - это одноадресная маршрутизация IPv6.
You must type that, or else, you're not gonna be able to route in IPv6.|Вы должны ввести это, иначе вы не сможете маршрутизировать в IPv6.
So that's one of the things you need to do.|Так что это одна из вещей, которые вам нужно сделать.
All right, and then there's other things in here that we've done.|Хорошо, а еще здесь есть кое-что, что мы сделали.
We have holes tables, DNS servers, things like that.|У нас есть таблицы дыр, DNS-серверы и тому подобное.
Don't pay attention to that.|Не обращай на это внимания.
Okay, but here look at this.|Хорошо, но вот посмотри на это.
We have an IP version four address, or I subnet it, obviously,|У нас есть IP-адрес четвертой версии, или я его подсчитываю, очевидно,
and we have an IP version six address, and you can tell already that in the IPv6,|и у нас есть IP-адрес шестой версии, и вы уже можете сказать, что в IPv6,
we're running EIGRP 300 and those hosts is great.|мы используем EIGRP 300, и эти хосты великолепны.
That is what's great about IPv6, you can just,|Вот что здорово в IPv6, вы можете просто
as soon as you can figure out the interface, all I really have to do is go into the interface IPv6 IGrP300, boom, and it does the configuration,|Как только вы сможете понять интерфейс, все, что мне действительно нужно сделать, это войти в интерфейс IPv6 IGrP300, бум, и он выполнит настройку,
and global config, it actually puts it in global config.|и глобальный конфиг, он фактически помещает его в глобальный конфиг.
The only thing I would need to do is then go back in global config and maybe put the router ID into the no shut because that is,|Единственное, что мне нужно сделать, это вернуться в глобальную конфигурацию и, возможно, поместить идентификатор маршрутизатора в no shut, потому что это
that is one of the things that is required.|это одна из необходимых вещей.
When you're configuring EIGRP for IPv6,|Когда вы настраиваете EIGRP для IPv6,
you need to have a router ID, which is an instance for that protocol, and you do need to ha, you do need to turn on the protocol.|у вас должен быть идентификатор маршрутизатора, который является экземпляром для этого протокола, и вам действительно нужно ha, вам нужно включить протокол.
Other than that, everything is done.|В остальном все сделано.
That's it, that's just how you enable that interface to use EIGRP.|Вот и все, вот как вы включаете этот интерфейс для использования EIGRP.
So, very simple.|Итак, очень просто.
So we know already that we're using EIGRP just by looking at the interface.|Итак, мы уже знаем, что используем EIGRP, просто взглянув на интерфейс.
And we go down, keep going down, there's your clock rates, the other interfaces.|И мы идем вниз, продолжаем снижаться, вот ваши тактовые частоты, другие интерфейсы.
And we're also running RIP, and that's kind of, you know, hey wait a minute.|И мы также используем RIP, и это вроде как, подождите минутку.
But if you, isn't EIGRP the the administrative distance knighting,|Но если вы, не является ли EIGRP административным рыцарем дистанции,
of course.|конечно.
So you would think well, wait a minute,|Так ты бы подумал, подожди минутку,
isn't the edge repeating going to take over the routing table?|разве повторение края не возьмет на себя таблицу маршрутизации?
Well, of course not.|Ну конечно нет.
It would if it was IPv4, but since we're running in IPv6 EIGRP,|Было бы, если бы это был IPv4, но поскольку мы работаем в IPv6 EIGRP,
it creates its own routing table, and IPv4|он создает свою таблицу маршрутизации, а IPv4
creates its own routing table.|создает свою таблицу маршрутизации.
Let's check that out.|Давайте это проверим.
How do we look at the routing table?|Как мы смотрим на таблицу маршрутизации?
What's the command?|Что за команда?
Exactly, show IPRL.|Точно, покажите IPRL.
[BLANK_AUDIO]|[BLANK_AUDIO]
All right, and we see that we're getting,|Хорошо, и мы видим, что получаем,
and I'll put it higher,|и я поставлю выше,
just in case you can't see it, you see we're getting things from RIP.|на случай, если вы этого не видите, видите ли, мы получаем информацию от RIP.
We're learning about the 32 network from RIP, and we're learning about the 96 network from RIP, they're both one hop away.|Мы изучаем сеть 32 из RIP, и мы изучаем сеть 96 из RIP, они обе на расстоянии одного прыжка.
So, RIP is working on the, on the network.|Итак, RIP работает в сети.
Okay?|Ладно?
So if the 96 should have, the IP address,|Итак, если 96 должен иметь IP-адрес,
I'm on router two, should be,|Я на втором роутере, должно быть,
let's say, that would be the LAN, it should be 97 for the actual PC I believe.|скажем, это будет LAN, я полагаю, для настоящего ПК должно быть 97.
That's normally my scheme.|Обычно это моя схема.
You should know your scheme for your, I shouldn't be talking if that doesn't ping, huh.|Вы должны знать свою схему для себя, я не должен говорить, если она не пингует, а.
Oh, it did ping, cool.|Ой, пинг был, круто.
All right, we just slapping before we got that arc.|Ладно, мы просто хлопаем по дуге.
So you see I'm pinging to the 97.|Итак, вы видите, что я пингуюсь на 97.
So that's the actual IP address of the PC.|Итак, это фактический IP-адрес ПК.
The default gateway, I use the last available.|Шлюз по умолчанию, я использую последний доступный.
So if you increment by 32, that's 120, so it would be 126, the gateway would be 126.|Итак, если вы увеличиваете на 32, это 120, то есть 126, шлюз будет 126.
There you go, so I can ping the gateway as well.|Итак, я могу пропинговать шлюз.
And that's how you should be doing IP addressing, just like that.|И вот как вы должны делать IP-адресацию, вот так.
Somebody gives you a network ID, you look at the mask,|Кто-то дает вам идентификатор сети, вы смотрите на маску,
you should know already what the nest network is, two less, you know,|вы уже должны знать, что такое сеть гнезд, на два меньше, знаете,
that's the last available, one less,|это последний доступный, на один меньше,
that's the broadcast.|это трансляция.
Boom, boom, boom, boom, boom, that quick.|Бум, бум, бум, бум, бум, так быстро.
Anyway, so we're dual stacking, you see that you have IT B4|В любом случае, так что мы делаем двойной стек, вы видите, что у вас IT B4
that's actually working on your network,|это действительно работает в вашей сети,
and if we do a show IPv6|и если мы сделаем шоу IPv6
route, you take a look at the actual IPv6|маршрута, вы посмотрите на фактический IPv6
routing table.|таблица маршрутизации.
And now you see these.|И теперь вы видите это.
I'm learning about the 2001, 3200 CAD 1000.|Я узнал о 2001 году, 3200 CAD 1000.
I'm also learning about the 1200.|Я также узнаю о 1200.
And is there anything else?|А есть еще что-нибудь?
No, I think that's it, only those two.|Нет, думаю, все, только эти двое.
Okay?|Ладно?
So, you are, both routing protocols are working, and I'm able to get across from one side to the next using them.|Итак, оба протокола маршрутизации работают, и я могу переходить с одной стороны на другую, используя их.
So think about the, just the redundancy of it.|Так что подумайте об этом, просто о его избыточности.
If your computers, both, every computer nowadays has IPv6 enabled.|Если у вас оба компьютера, то сейчас на каждом компьютере включен IPv6.
I mean, you can ping in your, like, this is my laptop here, and I am attached to a network, I believe.|Я имею в виду, вы можете пинговать в своем, вроде, это мой ноутбук, и я, кажется, подключен к сети.
And while I'm going to ping just a loop back, right?|И пока я собираюсь пинговать только петлю назад, верно?
I can ping, ping let's say,|Я могу пинговать, пинг, скажем,
loop back, and I'll put a switch minus six.|шлейф назад, а я выключатель минус шесть поставлю.
I believe that's the switch for it.|Я считаю, что это ключ к успеху.
And it gives me the IP version six.|И это дает мне шестую версию IP.
If I were to put minus four, I will get the version four loopback address using the little switches.|Если бы я поставил минус четыре, я получил бы адрес обратной связи версии 4 с помощью маленьких переключателей.
So you can IP, the dual stack transition mechanism is great because you're not always gonna walk into a network and you're gonna build it from the ground up.|Таким образом, вы можете использовать IP, механизм перехода двойного стека великолепен, потому что вы не всегда будете заходить в сеть, и вы собираетесь строить ее с нуля.
That would be lovely if you can do that,|Было бы прекрасно, если бы ты мог это сделать,
but that's not the, the majority of the cases.|но это не в большинстве случаев.
You don't walk into an existing network and you're not gonna say, okay everybody,|Вы не входите в существующую сеть и не собираетесь говорить всем, хорошо,
we're gonna change everybody's IP addresses,|мы собираемся изменить все IP-адреса,
everybody stop working, or you're gonna work at night and then only half of it gets done, and you're gonna have issues.|все перестанут работать, или ты будешь работать ночью, а потом будет сделана только половина работы, и у тебя будут проблемы.
So with these transition mechanisms,|Итак, с этими переходными механизмами,
meaning this dual stack, I can configure everything IPv6, not worry,|Имея в виду этот двойной стек, я могу настроить все IPv6, не волнуйтесь,
not disturb the IPv4 network and then it,|не беспокоить сеть IPv4, а затем
it's a seamless transition.|это плавный переход.
Boom, boom, boom.|Бум бум бум.
Once everything turns IPv6, all right?|Как только все перейдет на IPv6, хорошо?
And you do this normally for your local LAN, for your local LAN dual stack.|И вы делаете это обычно для своей локальной сети, для двойного стека локальной локальной сети.
But dual stacking is a very, very nice and clean way, all right,|Но двойной стек - это очень, очень красивый и чистый способ, ладно,
to do your transition from IPv4 to IPv6|для перехода с IPv4 на IPv6
without your users actually, you know, finding out, you know, what's going on.|без ваших пользователей на самом деле, вы знаете, не выясняя, вы знаете, что происходит.
They, they'll be like hey, I, I kinda skipped a beat, but that's about it.|Они, они будут типа "эй, я, я немного пропустил удар, но это все."
All right?|Отлично?
The next transition mechanism which obviously in the packet trace we're limited, is called 64 tunneling, and you usually use that when you're going on|Следующий механизм перехода, который, очевидно, ограничен в трассировке пакетов, называется 64-туннелирование, и вы обычно используете его, когда продолжаете.
to the internet because you're going from,|в Интернет, потому что вы идете из
and I have two IPv6 networks, but then,|и у меня две сети IPv6, но тогда,
it's got to go through these routers,|это должно пройти через эти маршрутизаторы,
that one router might be IPv6, the other one is IPv4, so it creates these tunnels that will transform, or carry,|что один маршрутизатор может быть IPv6, а другой - IPv4, поэтому он создает эти туннели, которые будут преобразовывать или переносить,
the IPv6 on an IPv4 network once it gets to the other side.|IPv6 в сети IPv4, когда он переходит на другую сторону.
That will be another transition mechanism that you can use.|Это будет еще один механизм перехода, который вы можете использовать.
The last one is NAT-PT.|Последний - NAT-PT.
Now, don't get confused.|Не запутайтесь.
We use NAT now to translate from public,|Теперь мы используем NAT для перевода из общедоступных,
or from private addresses to public, or public to private.|или с частных адресов на общедоступные, или с общедоступных на частные.
What NAT-PT does is not that.|NAT-PT делает не это.
What NAT-PT is actually doing is translating from IPv6 to IPv4 or vice versa.|На самом деле NAT-PT выполняет преобразование из IPv6 в IPv4 или наоборот.
And believe me, even your book says this is not the recommended way of doing it.|И поверьте мне, даже в вашей книге говорится, что это не рекомендуется.
So if you're using NAT, stick to the IP version four of NAT.|Поэтому, если вы используете NAT, придерживайтесь IP-версии 4 NAT.
Okay?|Ладно?
Do your duel, or your 64 tunneling,|Сделай свою дуэль или свое 64 туннелирование,
you'll be better off doing 64 tunneling than you are doing NAT PT.|вам будет лучше выполнить 64 туннелирования, чем NAT PT.
Right?|Правильно?
Just creating these tunnels where the IPv6|Просто создание этих туннелей, в которых IPv6
traffic can go on through IPv4, and then eventually NAT will go away.|трафик может проходить через IPv4, а затем в конечном итоге NAT исчезнет.
But we need to embrace, now there are more transition mechanisms out there,|Но нам нужно принять, теперь есть больше механизмов перехода,
like Microsoft uses Teredo servers that have an actual Teredo sever out there to translate for IPv6 if you're using NAT.|например, Microsoft использует серверы Teredo с фактическим сервером Teredo для перевода на IPv6, если вы используете NAT.
That will be a tra, another transition mechanism,|Это будет тра, еще один переходный механизм,
I guess, if you wanna call it that.|Я думаю, если вы хотите это так называть.
They also have 64 tunneling, and they also have,|У них также есть 64 туннелирования, и у них также есть,
for internet connectivity, and they also have the what is it?|для подключения к Интернету, и у них также есть что это?
The isotap, right?|Изотап, верно?
The isotap, which is by default is already working anyway on today's operating systems for the local area network.|Isotap, который по умолчанию уже работает в сегодняшних операционных системах для локальной сети.
So there's a lot of different mechanisms that not only Cisco, but Microsoft has actually created so we can make a smooth change into the IPv6 world.|Таким образом, существует множество различных механизмов, созданных не только Cisco, но и Microsoft, чтобы мы могли плавно перейти в мир IPv6.
Because as my shirt says, so what does it say?|Потому что, как написано на моей рубашке, что на ней написано?
Resistance is futile.|Сопротивление бесполезно.
We must stop having that resistance to change over to IPv6.|Мы должны прекратить сопротивление переходу на IPv6.
They've given us so many ways to make it,|Они дали нам так много способов сделать это,
you know,|знаешь,
easy, in quotations, for us to change over that we need to.|легко, в цитатах, для нас изменить то, что нам нужно.
Obviously, in a huge enterprise, with thousands, or hundreds of thousands, of nodes, this is not going to be an overnight thing or|Очевидно, что на огромном предприятии с тысячами или сотнями тысяч узлов это не произойдет в одночасье или
a six month thing, it may be a three year or four year or five year project that may take that long because we wanna make sure we do it correctly and|шесть месяцев, это может быть трехлетний, четырехлетний или пятилетний проект, который может занять столько времени, потому что мы хотим убедиться, что делаем это правильно и
as little loss as possible, but know that these things are in place.|как можно меньше потерь, но знайте, что эти вещи на месте.
Know that we can configure the duel stack,|Знайте, что мы можем настроить дуэльный стек,
that we can have that 64 tunneling,|что у нас есть 64 туннелирования,
and, you know, not worrying about NAP ET,|и, знаете ли, не беспокоясь о NAP ET,
cuz it's not recommended anyway.|Потому что это все равно не рекомендуется.
All right?|Отлично?
And just use 64 tunneling to go across the internet.|И просто используйте 64 туннелирования для выхода в Интернет.
So we have these things in place.|Итак, у нас есть эти вещи.
We need to start embracing them and start using them.|Нам нужно начать принимать их и начать использовать.
Because IPv6 does bring in a lot of features that will help us, all right?|Потому что IPv6 предлагает множество функций, которые нам помогут, понятно?
Just the fact of no broadcast, ladies and gentlemen, come on.|Просто факт отсутствия трансляции, дамы и господа, давайте.
I understand that looking at hex numbers gives you a headache,|Я понимаю, что просмотр шестнадцатеричных чисел вызывает у вас головную боль,
it gives me a headache too.|это тоже вызывает у меня головную боль.
It's been a while that I've been looking at it so I'm getting kind of used to it, and just like everything else.|Я давно смотрю на него, так что привыкаю к ​​нему, как и ко всему остальному.
But again, these transition mechanisms are on your exam.|Но опять же, эти механизмы перехода находятся на вашем экзамене.
They don't go into details, at least,|По крайней мере, они не вдавались в подробности
that's what my students tell me that take the test.|это то, что мои студенты говорят мне, когда проходят тест.
They just basically ask you, hey, out of the following which is the,|Они просто спрашивают вас, эй, из следующего, что
what are the transition mechanism?|каков механизм перехода?
You know, a, b, c, d, e, f, g.|Вы знаете, a, b, c, d, e, f, g.
Pick, choose two.|Выбери, выбери два.
You know, things like that.|Вы знаете, такие вещи.
They're not gonna get into the details.|Они не будут вдаваться в подробности.
As long as you know that that's what they are, that's what they're looking for.|Пока вы знаете, что они есть, это то, что они ищут.
So, read up on it.|Итак, читайте об этом.
There's not that much there to be, you know, read.|Здесь не так уж много, знаете ли, читать.
If you have the book that I told you, it's just enough for you to know what they are, their concepts.|Если у вас есть книга, о которой я вам рассказывал, вам просто достаточно знать, что это такое, их концепции.
And then you can start implementing them on your network.|А затем вы можете приступить к их внедрению в своей сети.
Obviously try practice network first, or a simulator [LAUGH] before you actually,|Очевидно, сначала попробуйте потренироваться в сети или на симуляторе [СМЕХ], прежде чем на самом деле,
you know, enter a production network.|вы знаете, войдите в производственную сеть.
But like I say, for my, my own personal self, I, what I love to do is dual stack.|Но, как я уже сказал, для себя лично я люблю делать двойной стек.
It is the easiest thing in the world, you don't have to worry about it.|Это самая легкая вещь в мире, вам не о чем беспокоиться.
You can walk into any IPv4 network and put in IPv6, and you'll be running just fine.|Вы можете войти в любую сеть IPv4 и вставить IPv6, и все будет в порядке.
All right, ladies and gentlemen,|Хорошо, дамы и господа,
this comes to the end of the transition mechanisms.|это подходит к концу переходных механизмов.
And I shall see you in the next session.|Увидимся на следующем сеансе.
Thank you.|Спасибо.
[BLANK_AUDIO]|[BLANK_AUDIO]