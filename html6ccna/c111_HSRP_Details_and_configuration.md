D:\mailCloud\prjother\tmp\1\c111_HSRP Details and configuration.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
All right everybody.|Все в порядке.
Let's get down to the details of HSRP before we start the configuration.|Прежде чем приступить к настройке, давайте рассмотрим детали HSRP.
Now, as we talked earlier, in the previous lesson, HSRP is a redundancy protocol.|Теперь, как мы говорили ранее, в предыдущем уроке, HSRP - это протокол резервирования.
And as you can see there, the routers or gateways are organized into, you're gonna have different groups for different gateways, if that's what you wanna do.|И, как вы можете видеть, маршрутизаторы или шлюзы организованы в, у вас будут разные группы для разных шлюзов, если вы этого хотите.
We're only gonna have one group, just so you can understand the concept of what HSRP or these redundancy protocols do.|У нас будет только одна группа, чтобы вы могли понять концепцию того, что делают HSRP или эти протоколы резервирования.
In the case of HSRP, you have one active router,|В случае HSRP у вас есть один активный маршрутизатор,
one standby router, and it's based on the priority number.|один резервный маршрутизатор, и он основан на номере приоритета.
The higher the priority number, that's the one that becomes the active router.|Чем выше номер приоритета, тем активным становится маршрутизатор.
And you'll see that now in the config.|И вы увидите это теперь в config.
Virtual router ID, and a MAC address are generated.|Создается идентификатор виртуального маршрутизатора и MAC-адрес.
You are going to actually create the virtual IP, or ID, that should have been IP, virtual IP, all right, that you you assign within that subnet.|Вы собираетесь создать виртуальный IP-адрес или идентификатор, который должен быть IP, виртуальным IP-адресом, хорошо, который вы назначаете в этой подсети.
The MAC address is what gets virtually created.|MAC-адрес - это то, что создается виртуально.
Hello messages every three seconds.|Сообщения приветствия каждые три секунды.
We know that.|Мы знаем это.
Dead after ten, cuz, and those hellos are important, because they keep talking.|Мертв после десяти, потому что эти приветы важны, потому что они продолжают говорить.
Remember, again I said that you can have more than just the active and standby router.|Помните, я снова сказал, что у вас может быть больше, чем просто активный и резервный маршрутизаторы.
You can have up to eight routers.|У вас может быть до восьми маршрутизаторов.
The other routers are really just not,|Других роутеров на самом деле просто нет,
they're just looking and,|они просто смотрят и,
at the active and standby, at those messages.|в активном и резервном состоянии в этих сообщениях.
They do send their messages.|Они отправляют свои сообщения.
Are, but they're called speak, right.|Есть, но их зовут говорить, верно.
Just, they're just like in the waiting mode,|Просто они как в режиме ожидания,
not to say standby, in case something happens.|не говоря о режиме ожидания, на случай, если что-то случится.
But they are actually watching.|Но они на самом деле смотрят.
But the ones that are the two routers,|Но те, которые являются двумя маршрутизаторами,
that are actually doing something,|которые на самом деле что-то делают,
are the active and standby routers.|являются активным и резервным маршрутизаторами.
All right now, this is important.|Хорошо, сейчас это важно.
Whatever virtual IP you decide to use that's completely up to you.|Какой бы виртуальный IP вы ни выбрали, это полностью зависит от вас.
You, as long as you use the subnet because remember the type of,|Вы, пока используете подсеть, потому что помните тип,
IP addressing scheme we have, it will be within that particular subnet.|Схема IP-адресации у нас есть, она будет внутри этой подсети.
[BLANK_AUDIO]|[BLANK_AUDIO]
What gets generated automatically, it's that virtual MAC address.|Что генерируется автоматически, так это виртуальный MAC-адрес.
Now remember, this right here, hm, hm,|Теперь помните, это прямо здесь, хм, хм,
is it here or here, hm, oh, well I have it broken down here ha, ha, ha, ha.|это здесь или здесь, хм, о, хорошо, я сломал здесь ха, ха, ха, ха.
Here it is, yes it's the c as well.|Вот он, да, это тоже c.
All right.|Все в порядке.
The first one, two, three, four, five,|Первый, два, три, четыре, пять,
six, 24 bits, right,|шесть, 24 бита, вправо,
these are hex numbers.|это шестнадцатеричные числа.
Vendor ID.|ID поставщика.
That's for Cisco.|Это для Cisco.
They say hey, this is Cisco.|Говорят, эй, это Cisco.
All right.|Все в порядке.
The next 16 is the one for HSRP, the one for HSRP ID.|Следующие 16 - это один для HSRP, один для HSRP ID.
And the last two, okay, is gonna be the group.|И последние два, хорошо, будут группой.
The group number you'd be assigned to, if your assigned to group number one,|Номер группы, к которой вы будете назначены, если вы назначены группе номер один,
group number two, it actually turns it into a hexidecimal number, all right?|группа номер два, она фактически превращает его в шестнадцатеричное число, хорошо?
So the last eight bits are the one that that creates that, okay?|Итак, последние восемь битов создают это, хорошо?
Now let me see here anything else important that I need to say about this right here, HSRP obviously as it says here oh, how would you do it?|Теперь позвольте мне увидеть здесь еще что-нибудь важное, что мне нужно сказать об этом прямо здесь, HSRP, очевидно, как здесь говорится, о, как бы вы это сделали?
Okay, so now we get into configuration.|Хорошо, теперь мы переходим к настройке.
So, what you need to for the certification, but you need to be,|Итак, что вам нужно для сертификации, но вы должны быть,
very familiar with, one, the HSRP, VRP,|хорошо знаком с, например, HSRP, VRP,
GLBP, r redundancy protocols.|Протоколы резервирования GLBP, r.
Two, for HSRP you need to know the default, hellos and the default,|Во-вторых, для HSRP вам нужно знать значение по умолчанию, привет и значение по умолчанию,
you know, which is three seconds, and then ten seconds for the dead, all right?|знаете, это три секунды, а затем десять секунд для мертвых, хорошо?
Only the hold.|Только трюм.
You need to know it's based on an active standby router.|Вы должны знать, что он основан на активном резервном маршрутизаторе.
And the active and standby are elected,|И активный и резервный выбираются,
right?|верно?
That's why the hello's, sending messages back and forth.|Вот почему привет, отправка сообщений туда и обратно.
That's one of the things that they determine, they talk to each other,|Это одна из вещей, которые они определяют, они разговаривают друг с другом,
they send.|Они отправляют.
Hey, my priority number's higher than yours, so therefore I am the active router.|Эй, мой приоритетный номер выше вашего, поэтому я являюсь активным маршрутизатором.
Okay, so, these are things that you need to be aware of.|Хорошо, это вещи, о которых вам нужно знать.
And, definitely that virtual MAC address,|И, безусловно, этот виртуальный MAC-адрес,
because you will be,|потому что ты будешь,
more than likely be asked a question, is this a valid HSRP MAC address?|скорее всего, вам зададут вопрос, действительный ли это MAC-адрес HSRP?
All right?|Все в порядке?
But, let's look at configuration.|Но давайте посмотрим на конфигурацию.
As you can see here Window 192.168.1.0|Как вы можете видеть здесь, окно 192.168.1.0
network.|сеть.
We won't do the virtual wiping first.|Мы не будем сначала выполнять виртуальную очистку.
We'll first configure it like any other router with normal gateways.|Сначала мы настроим его, как любой другой маршрутизатор, с обычными шлюзами.
We'll do this one as 1.254.|Мы сделаем это как 1.254.
This will be 1.253.|Это будет 1,253.
Five and six.|Пять и шесть.
Nine and ten.|Девять и десять.
This will be 1.254 right there, for that web server.|Это будет 1,254 для этого веб-сервера.
All right.|Все в порядке.
And here in the PC, we have the 1.1, and we already have the gateway as 1.254.|А здесь, на ПК, у нас есть 1.1, и у нас уже есть шлюз 1.254.
Just so you can understand what's going on, or what, you know, the advantages of using these redundancy protocols.|Просто чтобы вы могли понять, что происходит, или каковы преимущества использования этих протоколов резервирования.
So let's go to this router, and we'll just stick to the name that's there, R0.|Итак, давайте перейдем к этому маршрутизатору, и мы просто будем придерживаться его имени, R0.
Just so, you know, not to change anything or confuse anyone.|Просто чтобы ничего не менять и никого не запутать.
Bring this down right there.|Принеси это прямо сейчас.
See that.|Видеть, что.
Say no, all right, enable, config T, host name.|Скажите нет, хорошо, включите, настройте T, имя хоста.
Host name, R0, I'm gonna use capital.|Имя хоста, R0, я буду использовать заглавные буквы.
R0 [COUGH] interface, f zero slash zero,|Интерфейс R0 [COUGH], f нулевая косая черта, ноль,
Enter.|Войти.
IP address, [NOISE] 192.168.|IP-адрес, [NOISE] 192.168.
[NOISE] What is it, is it 100 or 1?|[NOISE] Что это, 100 или 1?
[INAUDIBLE] remembering.|[НЕДОСТАТОЧНО] вспоминая.
Okay, it's one.|Ладно, это одно.
Okay.|Ладно.
[BLANK_AUDIO]|[BLANK_AUDIO]
1.254, 255.255.255.0,|1.254, 255.255.255.0,
and then we just do a no shut on that.|а затем мы просто не закрываем глаза на это.
I know the one is 10.1.1.5 for the add zero one I believe.|Я знаю, что это 10.1.1.5 для добавления нуля, я считаю.
Yup.|Ага.
So INT F0/1.|Итак, INT F0 / 1.
IP address 10.1.1.5 255.255.255.252.|IP-адрес 10.1.1.5 255.255.255.252.
No shut.|Нет, заткнись.
No need to worry about clock rates here.|Здесь не нужно беспокоиться о тактовой частоте.
We're using fast ethernet, so no need for clock rates.|Мы используем быстрый Ethernet, поэтому тактовая частота не нужна.
Do WR.|Сделайте WR.
Ctrl+Z.|Ctrl + Z.
Let's just take a look at a summary real quick.|Давайте быстро взглянем на резюме.
All right.|Все в порядке.
One, obviously, one's gonna be up and down,|Один, очевидно, будет вверх и вниз,
because the other one is not, you know,|потому что другой нет, вы знаете,
its neighbor is not configured.|его сосед не настроен.
So, 0.0.0.1.254, up up, that's our gateway to the pc.|Итак, 0.0.0.1.254, вверх, это наш шлюз к компьютеру.
And then F0/1 get.|И тогда получится F0 / 1.
All right so that one is good to go.|Хорошо, так что можно идти.
With its its IPs.|Со своими IP-адресами.
All right, let's bring this out here,|Хорошо, давайте представим это здесь,
bring this a little further down.|опустите это немного дальше.
All right, we're going to say no at this point.|Хорошо, сейчас мы скажем нет.
Enable config T host name.|Включите имя хоста config T.
Where am I?|Где я?
Did I choose it?|Я выбрал это?
Okay.|Ладно.
There's router one, R1.|Есть маршрутизатор один, R1.
Okay, and then interface.|Хорошо, а затем интерфейс.
I'm pretty sure it's F0/0, but I'm just gonna make sure.|Я почти уверен, что это F0 / 0, но я просто хочу убедиться.
Yep, F0/0.|Ага, F0 / 0.
I don't know what's wrong with my brain today.|Я не знаю, что случилось с моим мозгом сегодня.
IP address 192.168.1.253|IP-адрес 192.168.1.253
255.255.255.0 okay and then we do a no shut then we go into the int F zero one and I'll be nine.|255.255.255.0 хорошо, а затем мы отключаемся, затем переходим к int F, равному нулю, и мне будет девять.
IP address.|Айпи адрес.
Oh, not too many of these.|О, их не так уж и много.
10.1.1.9.|10.1.1.9.
255.2555.255.252.|255.2555.255.252.
No shut.|Нет, заткнись.
EWR Ctrl+Shift+6 if I finger with the keyboard.|EWR Ctrl + Shift + 6, если я касаюсь клавиатуры.
EWR, you show IP Int Brief.|EWR, вы показываете IP Int Brief.
All right so obviously, again, we see that it's up, up.|Хорошо, так очевидно, мы снова видим, что это вверх, вверх.
Up down because again, the neighbor upstairs, not configured it.|Вверх вниз, потому что, опять же, сосед наверху не настроил его.
So let's go ahead and do so.|Так что давайте продолжим и сделаем это.
So there's gonna be 10.1.1.6, 10.1.1.8,|Итак, будет 10.1.1.6, 10.1.1.8,
and this will be 1.1.1.1.|и это будет 1.1.1.1.
284.|284.
[BLANK_AUDIO]|[BLANK_AUDIO]
We'll go right into that.|Мы займемся этим.
[BLANK_AUDIO]|[BLANK_AUDIO]
Just maximize this [UNKNOWN] adjusting it.|Просто увеличьте это [НЕИЗВЕСТНО], регулируя его.
Enable [UNKNOWN] brief, doing this just look at the interfaces it's really a, I have so many interfaces.|Включите [UNKNOWN] кратко, сделав это, просто посмотрите на интерфейсы, которые действительно есть, у меня так много интерфейсов.
[COUGH] Wow [UNKNOWN] F00,|[КАШЕ] Вау [НЕИЗВЕСТНО] F00,
F01, F01, okay.|F01, F01, хорошо.
F00.|F00.
[BLANK_AUDIO]|[BLANK_AUDIO]
Config T interface F0/0 IP address 10.1.1.6 255,|Config T interface F0 / 0 IP-адрес 10.1.1.6 255,
255, 255, 252.|255, 255, 252.
Shut it.|Закрой его.
Up arrow.|Стрелка вверх.
And we'll leave this at zero.|И оставим это значение равным нулю.
Zero one over here, okay, zero one.|Ноль здесь, ладно, ноль один.
IP address, 101110.|IP-адрес, 101110.
Now shut.|А теперь закрой.
Okay.|Ладно.
And then we have the, I think this is an E, E00.|А еще у нас есть, я думаю, это E, E00.
E000, wow.|E000, вау.
Int E0/0/0.|Инт E0 / 0/0.
Ethernet.|Ethernet.
IP address 1.1.1.254,|IP-адрес 1.1.1.254,
255.255.255.0.|255.255.255.0.
No shuts.|Никаких затворов.
[BLANK_AUDIO]|[BLANK_AUDIO]
We do R, Ctrl+V.|Делаем R, Ctrl + V.
Let's make sure everything's up.|Убедимся, что все в порядке.
Show IP in brief.|Покажите кратко IP.
[BLANK_AUDIO]|[BLANK_AUDIO]
And [NOISE].|И [ШУМ].
We got up all the way across.|Мы встали полностью.
Let's see if we can ping our neighbors.|Посмотрим, сможем ли мы пинговать наших соседей.
[BLANK_AUDIO]|[BLANK_AUDIO]
Ping, 1001.5, no, that's [UNKNOWN] 15.|Ping, 1001.5, нет, это [НЕИЗВЕСТНО] 15.
[BLANK_AUDIO]|[BLANK_AUDIO]
[SOUND].|[ЗВУК].
Okay.|Ладно.
And then nine.|А потом девять.
[BLANK_AUDIO]|[BLANK_AUDIO]
Once you get that [UNKNOWN] it's fast Ethernet, okay?|Как только вы поймете, что [НЕИЗВЕСТНО] это быстрый Ethernet, хорошо?
And then we wanna ping, or hopefully the server has an IP address.|И затем мы хотим пинговать, или, надеюсь, у сервера есть IP-адрес.
[BLANK_AUDIO]|[BLANK_AUDIO]
And it does.|И это так.
So we have connectivity to our routers.|Итак, у нас есть возможность подключения к нашим маршрутизаторам.
Obviously, we'll have connectivity to our gateway.|Очевидно, у нас будет подключение к нашему шлюзу.
All right, so let's ping from the computer.|Хорошо, давайте пингуем с компьютера.
Wow.|Вау.
That's a big black screen.|Это большой черный экран.
Put it right here.|Положи сюда.
There we go.|Вот и все.
You can see that right there.|Вы можете увидеть это прямо здесь.
Ping 192.168.1.254.|Пинг 192.168.1.254.
That's my gateway 253, that's the other guy.|Это мой шлюз 253, это другой парень.
All right, but obviously we can't get to the server.|Хорошо, но очевидно, что мы не можем добраться до сервера.
[BLANK_AUDIO]|[BLANK_AUDIO]
1.1.1.1.|1.1.1.1.
Destination unreachable because we have no routing protocol.|Пункт назначения недоступен, потому что у нас нет протокола маршрутизации.
There's no routing in place.|Нет маршрутизации.
So we go ahead and put some routing, let's just use two, let's use rip real quick.|Итак, мы продолжаем и добавляем некоторую маршрутизацию, давайте просто воспользуемся двумя, давайте быстро воспользуемся рипом.
No big deal there,|Ничего особенного,
config T, router rip V2,|конфиг T, роутер рип V2,
net 192.168.1.0|сеть 192.168.1.0
net ten triple zero,|чистая десять тройной ноль,
remember glass full boundary.|запомните полную границу стекла.
No auto summary.|Нет автоматического резюме.
[UNKNOWN].|[НЕИЗВЕСТНО].
All right.|Все в порядке.
We'll move on this one.|Мы перейдем к этому.
Same exact thing.|То же самое.
All right.|Все в порядке.
Config T, router RIP Version R if this one will take that.|Config T, маршрутизатор RIP версии R, если этот примет это.
Wow I was trying an abbreviation,|Ух ты, я пробовал аббревиатуру,
v2 huh, v space 2 okay.|v2 да, v пробел 2 хорошо.
Network ten triple zero, network 119.168.1.0|Сеть десять тройной ноль, сеть 119.168.1.0
No auto summary Do WR and then we'll go ahead and do the stop router it is really easy config T Router RIP.|Нет автоматического резюме Сделайте WR, а затем мы продолжим и остановим маршрутизатор, это действительно просто. Настроить T Router RIP.
V space two.|V пространство два.
I like that.|Мне нравится это.
You can't do it in [INAUDIBLE], you gotta type out the whole thing.|Вы не можете сделать это в [НЕРАЗБОРЧИВО], вы должны напечатать все это.
Network ten triple zero.|Сеть десять, тройной ноль.
Network one triple zero.|Сеть один тройной ноль.
Normal summary DWR.|Нормальное резюме DWR.
Control Z.|Control Z.
Let's take a look at the routing tables.|Взглянем на таблицы маршрутизации.
Show IP route.|Показать IP-маршрут.
And now we're getting RIP updates from the, the ten network.|И теперь мы получаем обновления RIP из сети десять.
All right.|Все в порядке.
And the 1.0 network.|И сеть 1.0.
Awesome.|Потрясающие.
Right?|Правильно?
So we can see all that.|Итак, мы можем все это увидеть.
So now, let's just go To the PC again.|Итак, давайте снова вернемся к ПК.
Let's just try to ping the server one more time.|Попробуем еще раз пропинговать сервер.
And now we do get a reply from the web server, so we are routing.|И теперь мы получаем ответ от веб-сервера, поэтому мы выполняем маршрутизацию.
But here comes the problem, here's where the redundancy protocols come into play.|Но здесь возникает проблема, здесь в игру вступают протоколы избыточности.
Yes, we have two connections.|Да, у нас есть две связи.
Right?|Правильно?
A little redundancy going on there.|Там происходит небольшая избыточность.
As we move this all the way over here.|Поскольку мы перемещаем это полностью сюда.
We haven't configured any redundancy,|Мы не настроили резервирование,
well, physically,|ну физически,
we should have redundancy.|у нас должна быть избыточность.
You know we're pinging this web server, so I'm just gonna put this right here.|Вы знаете, что мы пингуем этот веб-сервер, поэтому я просто положу это прямо сюда.
No, that's too far away from you guys.|Нет, это слишком далеко от вас, ребята.
You guys can't see.|Ребята, вы не видите.
[BLANK_AUDIO]|[BLANK_AUDIO]
All right, so I'm gonna put it right there [BLANK_AUDIO]|Хорошо, я положу это прямо здесь [BLANK_AUDIO]
All right.|Все в порядке.
And we'll do a ping, minus T.|И мы сделаем пинг, минус Т.
1.1.1.1.|1.1.1.1.
And that's if, for those of you that don't know, that's just a never ending ping.|И это если для тех из вас, кто не знает, это просто бесконечный пинг.
As the switches give them, you can tell them which size of packet you wanna send.|По мере того, как коммутаторы сообщают им, вы можете сказать им, какой размер пакета вы хотите отправить.
But this actually is just pinging the web server over and over and over again.|Но на самом деле это просто пинг веб-сервера снова и снова.
We're doing like a little DOS attack.|Мы делаем что-то вроде небольшой атаки DOS.
A very small DOS attack.|Очень маленькая атака DOS.
But anyway, we're sending a constant ping.|Но в любом случае мы отправляем постоянный пинг.
All right?|Все в порядке?
So we do have connectivity.|Так что связь есть.
Now, what would happen if I go inside here and, you know,|Теперь, что будет, если я войду сюда и, знаете,
for whatever reason, the interface [UNKNOWN]|по какой-то причине интерфейс [НЕИЗВЕСТНО]
zero slash, slash zero.|нулевой косой чертой, нулевой косой чертой.
Somebody just said, shut.|Кто-то только что сказал: «Заткнись».
[BLANK_AUDIO]|[BLANK_AUDIO]
So somebody shut down that interface.|Итак, кто-то отключил этот интерфейс.
So what's gonna happen to the connectivity?|Так что же произойдет с подключением?
Well I can't reach it, it's request time out.|Я не могу связаться с ним, время ожидания запроса истекло.
[BLANK_AUDIO]|[BLANK_AUDIO]
So now, hey.|Итак, привет.
How do we fix that problem?|Как решить эту проблему?
Call somebody?|Позвонить кому-нибудь?
Hey, change the gateway on the computer.|Эй, поменяй шлюз на компьютере.
So we can go ahead and get connectivity again.|Так что мы можем продолжить и снова получить возможность подключения.
Yeah, but there's nobody there.|Да, но там никого нет.
I think the guy is out to lunch.|Думаю, парень ушел на обед.
Okay, let me drive over there.|Хорошо, позволь мне поехать туда.
I'm only 20 minutes away.|Я всего в 20 минутах езды.
So you drive over there and you go on to the computer, you change the gateway.|Итак, вы едете туда, идете к компьютеру и меняете шлюз.
That's not very feasible.|Это не очень возможно.
That's not very feasible.|Это не очень возможно.
Okay?|Ладно?
So definitely, this is not the way you wanna do it.|Так что определенно это не то, что вы хотите.
You wanna have redundancy protocols, so that way it can go back and forth.|Вам нужны протоколы избыточности, чтобы они могли работать туда и обратно.
So let's go ahead and turn that interface back on.|Итак, давайте продолжим и снова включим этот интерфейс.
No shut.|Нет, заткнись.
[BLANK_AUDIO]|[BLANK_AUDIO]
All right.|Все в порядке.
And it's gonna take a while looking as you can see STP is doing its thing.|И это займет некоторое время, так как вы увидите, что STP делает свое дело.
Right there, STP is doing its thing, so we gotta wait for STP, huh?|Прямо сейчас STP делает свое дело, так что нам нужно дождаться STP, да?
That's why a Rapid Spanning Tree and the types of spanning tree that you're gonna be using, so the convergence can be a lot|Вот почему быстрое связующее дерево и типы связующего дерева, которые вы собираетесь использовать, поэтому сходимость может быть значительной.
quicker than what it originally is.|быстрее, чем изначально.
Obviously, there's the packet tracer.|Очевидно, есть трассировщик пакетов.
It's not that packet tracers are similar nonetheless, but, I mean, it's good.|Дело не в том, что трассеры пакетов все же похожи, но, я имею в виду, это хорошо.
It's a good simulator because it's based specifically for the CCNA, and like,|Это хороший симулятор, потому что он основан специально для CCNA и, например,
like I've been telling you throughout the whole course, this is geared to the CCNA.|как я говорил вам на протяжении всего курса, это приспособлено к CCNA.
Will you be doing this in the real world?|Вы будете делать это в реальном мире?
Of course.|Конечно.
You know, putting in IP addresses,|Вы знаете, вводя IP-адреса,
configuring routing protocols, same thing,|настройка протоколов маршрутизации, то же самое,
same thing.|то же самое.
All right.|Все в порядке.
But gear to the CCNA.|Но переходите к CCNA.
All right, so we're back in business,|Хорошо, мы снова в деле,
we're back in business, great.|мы снова в деле, отлично.
So we do have connectivity to our, to our web server.|Итак, у нас есть подключение к нашему веб-серверу.
But we want redundancy and redundancy is needed.|Но нам нужна избыточность, а избыточность необходима.
So what we're gonna do is, we're gonna configure this router right here as our active router with HSRP and this will be our stand by.|Итак, что мы собираемся сделать, мы настроим этот маршрутизатор прямо здесь как наш активный маршрутизатор с HSRP, и он будет нашим резервным.
This one is going here.|Этот идет сюда.
Now if you do this, you do it inside the interface and it's not gonna say HSRP.|Теперь, если вы сделаете это, вы сделаете это внутри интерфейса, и он не скажет HSRP.
They put a question mark, you see where it says standby.|Ставят вопросительный знак, видишь где написано ожидание.
HSRP interface configuration command.|Команда настройки интерфейса HSRP.
So that's what you need to do.|Вот что вам нужно сделать.
You're not gonna see something that says standby.|Вы не увидите ничего, что говорит о готовности.
I mean you're not gonna see something that says HSRP.|Я имею в виду, что вы не увидите ничего, что говорит о HSRP.
VRP, yes, GLVP, yes, but we don't have that in the packet tracer, so sorry.|VRP, да, GLVP, да, но у нас этого нет в трассировщике пакетов, извините.
But I'll show you the configs.|Но я покажу вам конфиги.
So standby and what do you put next?|Итак, ждем, а что ставить дальше?
Well, you're gonna put a group number.|Ну, ты собираешься указать номер группы.
That's the first thing you wanna do.|Это первое, что ты хочешь сделать.
And you can see the group numbers are there, from 0 to 4095.|И вы можете видеть номера групп от 0 до 4095.
So okay, so what group number are we gonna use?|Так что же, какой номер группы мы будем использовать?
Let's just use one.|Давайте просто воспользуемся одним.
All right so after, now what do you put,|Хорошо, так что теперь, что вы ставите,
want me to put an IP.|хочу, чтобы я поставил IP.
Okay so what's the IP?|Хорошо, а какой IP?
192.168.1.100 that is the standby IP.|192.168.1.100, то есть резервный IP.
We just created this virtual IP address.|Мы только что создали этот виртуальный IP-адрес.
Now the priority number, who's gonna be active and who's not gonna be active, right, who's gonna be standby.|Теперь номер приоритета, кто будет активен, а кто не будет активен, верно, кто будет резервным.
By default the priority number is 100.|По умолчанию приоритет 100.
But, I'm gonna make this bigger, I'm gonna make the priority number.|Но я сделаю это больше, я сделаю приоритетное число.
Here let's look at the range, is 1 through 16.|Давайте посмотрим на диапазон от 1 до 16.
So what we're gonna do is I'm gonna just make it really interesting what we're do with priority, no really?|Так что мы собираемся сделать, я просто сделаю действительно интересным, что мы делаем с приоритетом, правда?
That's very.|Это очень.
Oh, [LAUGH].|О, [СМЕХ].
Standby, sorry.|Ожидание, извините.
Standby 1 priority.|Приоритет режима ожидания 1.
I knew there was something.|Я знал, что что-то было.
Wait, what?|Чего ждать?
What's.|Что.
Whoops.|Упс.
What's going on here, laugh.|Что здесь происходит, смейтесь.
That's incorrect.|Это неверно.
There we go, 0255.|Итак, 0255.
[SOUND] All right, that was like, that was kind of weird, okay.|[ЗВУК] Ладно, это было как-то странно, ладно.
150, we're gonna change the actual priority of the interface and I hope I didn't.|150, мы собираемся изменить фактический приоритет интерфейса, и я надеюсь, что я этого не сделал.
No because it gave me an error so that's good.|Нет, потому что это дало мне ошибку, так что это хорошо.
All right so, standby 1, priority 150.|Хорошо, режим ожидания 1, приоритет 150.
So I'm just gonna leave it at that.|Так что я просто оставлю это как есть.
And then we'll do a Ctrl+Z after I copy it and I'm gonna do a Schule standby.|А затем мы сделаем Ctrl + Z после того, как я скопирую его, и я сделаю резервный Schule.
That's the only command you're gonna do.|Это единственная команда, которую ты собираешься выполнять.
That way you're not gonna do it, but you need to know.|Таким образом вы не сделаете этого, но вам нужно знать.
All right.|Все в порядке.
And, this shows you, hey,|И это показывает вам, эй,
this state is active.|это состояние активно.
All right.|Все в порядке.
Your virtual IP is 192.100.1.100.|Ваш виртуальный IP-адрес 192.100.1.100.
Your virtual MAC address, which it created, you see it's not that 7f or that 7c, right, it's 9f.|Ваш виртуальный MAC-адрес, который он создал, вы видите, это не тот 7f или тот 7c, верно, это 9f.
All right, so not a big deal,|Хорошо, так что ничего страшного,
[INAUDIBLE] when you go take your test it'll probably be 7c.|[НЕДОСТАТОЧНО] когда вы пойдете сдавать тест, вероятно, будет 7с.
But again this is the Cisco vendor ID, all right.|Но опять же, это идентификатор поставщика Cisco, хорошо.
These next four okay, or yeah, 16,|Эти следующие четыре хорошо, или да, 16,
all right, these next 16 is specifically for hey that's HSRP.|Хорошо, эти следующие 16 предназначены специально для HSRP.
And then group number one, which is,|Затем группа номер один, а именно,
that's what I created.|вот что я создал.
Here it is right here, group number one.|Вот это прямо здесь, группа номер один.
That's how they break down the Mac address, alright so that is your virtual Mac address.|Вот как они разбивают адрес Mac, хорошо, так что это ваш виртуальный адрес Mac.
You see your hello time it's set to three seconds right here, right three seconds and then your whole time ten seconds the|Вы видите свое время приветствия, оно установлено на три секунды прямо здесь, прямо здесь три секунды, а затем все ваше время на десять секунд
next hello will be sent in 1.995 seconds.|следующее приветствие будет отправлено через 1,995 секунды.
All right?|Все в порядке?
We'll talk about preemption in a little bit.|Мы немного поговорим о приоритетном обслуживании.
The active router is the local router, the standby router is unknown cuz we haven't configured it yet, we haven't configured it yet.|Активный маршрутизатор - это локальный маршрутизатор, резервный маршрутизатор неизвестен, потому что мы еще не настроили его, мы еще не настроили его.
The priority for this particular group is 150, all right.|Приоритет этой конкретной группы - 150, хорошо.
So this is why this is the active router.|Вот почему это активный маршрутизатор.
So now we can configure the standby router which is going to be this guy right here.|Итак, теперь мы можем настроить резервный маршрутизатор, которым будет именно этот парень.
So, we're gonna actually type out the priority number of 100 or 110, let's just type 110.|Итак, мы собираемся набрать приоритетное число 100 или 110, давайте просто наберем 110.
You can leave that the default, you really don't have to type it.|Вы можете оставить это значение по умолчанию, вам действительно не нужно его вводить.
You can just leave it at the default.|Вы можете просто оставить значение по умолчанию.
But just so you can see the command, let's just type it in.|Но чтобы вы могли видеть команду, давайте просто введем ее.
So let's go inside the interface,|Итак, зайдем внутрь интерфейса,
interface F0/0 right standby 1 IP 192.16 oops .168.1.100 okay.|интерфейс F0 / 0 правый резервный 1 IP 192.16 ой .168.1.100 хорошо.
And then we're going to do standby 1,|А затем мы перейдем в режим ожидания 1,
priority, 110.|Приоритет, 110.
Which is smaller.|Что меньше.
The WR Ctrl+Z shows standby and then it's going through it and typing faster than the actual router can.|WR Ctrl + Z показывает режим ожидания, а затем проходит его и набирает быстрее, чем это может сделать настоящий маршрутизатор.
Keep obviously I just changed it right there to standby right here all right.|Держите, очевидно, я просто изменил его прямо здесь на режим ожидания прямо здесь, хорошо.
So let's type in again so we can go ahead and see it alright so the state is standby this is a standby router this is the virtual|Итак, давайте введем еще раз, чтобы мы могли продолжить и все в порядке, так что состояние - резервный, это резервный маршрутизатор, это виртуальный
IP address the active virtual Mac address is still unknown hasn't Yet,|IP-адрес активный виртуальный Mac-адрес еще неизвестен.
you know, talking back and forth to recognize it, it will after a little bit.|вы знаете, разговаривая взад и вперед, чтобы распознать это, это произойдет через некоторое время.
And then, it's telling you a local virtual Mac address, there it is right there.|А затем он сообщает вам локальный виртуальный адрес Mac, вот и он.
And, then the next hello will be sent in 2.35 seconds.|И тогда следующее приветствие будет отправлено через 2,35 секунды.
We're going faster than the router can think, so, hey.|Мы едем быстрее, чем думает маршрутизатор, так что, привет.
All right, so all of this information will be filled out eventually.|Хорошо, значит, вся эта информация со временем будет заполнена.
All right, so, now, let's see what happens.|Хорошо, а теперь давайте посмотрим, что произойдет.
All right, now let's first see if we can ping this wall.|Хорошо, теперь давайте сначала посмотрим, сможем ли мы пропинговать эту стену.
First of all, I haven't changed the IP address of the client yet.|Во-первых, я еще не изменил IP-адрес клиента.
So, let's see if I can ping.|Итак, посмотрим, смогу ли я пинговать.
I still have connectivity.|У меня все еще есть связь.
Look at that.|Посмотри на это.
All right, cuz I am so going through there.|Хорошо, потому что я так переживаю.
But let's see if we can ping that that 1.100.|Но давайте посмотрим, сможем ли мы пинговать, что 1.100.
I sure can.|Я точно могу.
I sure can.|Я точно могу.
All right, so it exists.|Хорошо, так оно и есть.
It exists in there, so we can go ahead and use this.|Он существует там, поэтому мы можем использовать его.
So, we're gonna change, we have to tweak our client, and we're gonna,|Итак, мы собираемся измениться, нам нужно настроить нашего клиента, и мы собираемся,
instead of having the physical IP address,|вместо физического IP-адреса,
we're gonna give it this virtual,|мы дадим ему это виртуальное,
this ghost IP address, all right, as the gateway.|этот призрачный IP-адрес, ладно, как шлюз.
Now what I like to do it is.|Теперь мне нравится это делать.
Because if I were to ping again, I still won't get connectivity.|Потому что, если я снова запингуюсь, у меня все равно не будет подключения.
Well how do we really know that's the way we're going?|Хорошо, как мы действительно знаем, что мы идем по этому пути?
The easiest test to do, instead of going to simulation mode or anything like that.|Самый простой тест, вместо того, чтобы переходить в режим моделирования или что-то в этом роде.
I'm gonna go ahead and configure my telnet lines real quick.|Я собираюсь очень быстро настроить свои линии Telnet.
Line bty, zero space 15.|Строка bty, нулевой пробел 15.
Password Cisco.|Пароль Cisco.
Login.|Авторизоваться.
And I just put some enable password just to have it on there.|И я просто поставил пароль для включения, чтобы он был там.
ENABLE PASSWORD CISCO and yes, and that's it.|ВКЛЮЧИТЬ ПАРОЛЬ CISCO и да, вот и все.
Ctrl+Z.|Ctrl + Z.
And let's do the same thing on the other one.|И давайте сделаем то же самое с другим.
Config T, LINE V LINE VTY 0.15.|Конфиг T, LINE V LINE VTY 0.15.
Password.|Пароль.
So let's go, login,|Итак, пойдем, авторизуемся,
enable password, Cisco.|включить пароль, Cisco.
You [UNKNOWN], all right.|Вы [НЕИЗВЕСТНО], хорошо.
So what we're gonna do is, I'm actually gonna TelNet to that virtual IP address.|Итак, что мы собираемся сделать, я собираюсь использовать TelNet для этого виртуального IP-адреса.
And I'm gonna see which router I end up in.|И я посмотрю, в какой роутер я попаду.
Remember, this is router zero and this is router one on this side.|Помните, что это нулевой маршрутизатор, а это первый маршрутизатор с этой стороны.
So the active router is r0.|Итак, активный маршрутизатор - r0.
So let's go ahead and TELNET-|Итак, давайте продолжим и TELNET-
[BLANK_AUDIO]|[BLANK_AUDIO]
To 192.168.1.100.|Кому 192.168.1.100.
That is the virtual IP address, Cisco.|Это виртуальный IP-адрес Cisco.
[BLANK_AUDIO]|[BLANK_AUDIO]
I'm a router 0.|Я роутер 0.
This is where we're headed to.|Вот куда мы направляемся.
This is where we're going.|Вот куда мы идем.
Okay?|Ладно?
So that's the direction the packets are flowing.|Вот в каком направлении текут пакеты.
So now we know.|Итак, теперь мы знаем.
We've verified, hey, I'm actually going that way.|Мы проверили, эй, я действительно иду туда.
Cuz I'm, the virtual IP address is on both routers.|Потому что виртуальный IP-адрес есть на обоих маршрутизаторах.
But since router zero has a higher priority number, became the active router.|Но поскольку нулевой маршрутизатор имеет более высокий приоритетный номер, он стал активным маршрутизатором.
So packets are flowing that way.|Так что пакеты текут именно так.
So let's go ahead.|Так что вперед.
Raise exit out of here.|Поднимите выход отсюда.
[BLANK_AUDIO]|[BLANK_AUDIO]
All right.|Все в порядке.
Back at the PC.|Вернемся к ПК.
Let's do our PING minus T.|Давайте сделаем наш PING минус T.
[BLANK_AUDIO]|[BLANK_AUDIO]
Okay?|Ладно?
And it's enough space right there.|И места там достаточно.
So you can see what's going on, cuz after I ping here.|Так что вы можете видеть, что происходит, потому что после того, как я пингую здесь.
You have a couple of pings.|У вас есть пара пингов.
I'm going to shut down that interface again and let's see how long it takes it to throw over.|Я собираюсь снова закрыть этот интерфейс и посмотрим, сколько времени потребуется, чтобы его сбросить.
Remember, every three seconds says, hey,|Помните, каждые три секунды говорит, эй,
everything is still good.|все еще хорошо.
Hey, everything's still good.|Эй, все еще хорошо.
[BLANK_AUDIO]|[BLANK_AUDIO]
Wait a minute, ten seconds.|Подожди минутку, десять секунд.
Oh!|Ой!
Something happened.|Что-то произошло.
Quick!|Быстрый!
Switch it over.|Переключи это.
So let's see how long it takes.|Итак, посмотрим, сколько времени это займет.
So lets start the pinging.|Итак, приступим к пингу.
[BLANK_AUDIO]|[BLANK_AUDIO]
All right, the never ending ping.|Ладно, бесконечный пинг.
The ping minus t.|Пинг минус т. Д.
And now we're gonna go ahead, and I'm going to do it quickly,|И теперь мы пойдем вперед, и я сделаю это быстро,
enter, or I thought quicker, enter interface add 0,|введите, или я подумал быстрее, введите интерфейс добавить 0,
slash 0, shut, and let's go here.|косая черта 0, закройте и пойдем сюда.
Boom.|Бум.
And whoa, we lost connectivity.|И эй, мы потеряли связь.
We saw that.|Мы это видели.
Boom, request time out.|Бум, тайм-аут запроса.
Oh my god, what's happening?|Боже мой, что происходит?
All right?|Все в порядке?
The client's like, hey,|Клиент любит, эй,
I can't get to my email server, oh I can't send.|Я не могу попасть на свой почтовый сервер, о, я не могу отправить.
Oh, I'm back up again, never mind.|О, я снова вернулся, неважно.
It automatically switched over to the other router.|Он автоматически переключился на другой маршрутизатор.
That is cool.|Это круто.
You don't have to worry about it.|Вам не о чем беспокоиться.
And that's what HSRP is there for.|И для этого существует HSRP.
Obviously, you will, do have to worry about it.|Очевидно, вам придется об этом беспокоиться.
You will have third party monitoring software,|У вас будет стороннее программное обеспечение для мониторинга,
which we'll talk about in the next session, all right?|о чем мы поговорим на следующем занятии, хорошо?
That will alert you to like hey, on this router, this interface went down.|Это предупредит вас, что на этом маршрутизаторе этот интерфейс вышел из строя.
Traffic is now flowing this way.|Трафик сейчас идет по этой дороге.
So, you know, you'll see it pop up on the screen, or you'll get a beep, or you'll get a phone call, text, whatever the case may be, smoke signals.|Итак, вы знаете, вы увидите, как это всплывает на экране, или вы услышите звуковой сигнал, или вы получите телефонный звонок, текстовое сообщение, в любом случае, дымовые сигналы.
Something to let you know that, hey that router just went down,|Что-то, чтобы вы знали об этом, эй, роутер только что вышел из строя,
or that interface just went down, but packets are now flowing the other way, so you're gonna start investigating, saying hey, what's going on?|или этот интерфейс только что вышел из строя, но теперь пакеты идут в обратном направлении, так что вы собираетесь начать расследование, говоря: эй, что происходит?
But at least you still have connectivity.|Но, по крайней мере, у вас все еще есть возможность подключения.
People are gonna still route traffic through, to the destination.|Люди по-прежнему будут направлять трафик к месту назначения.
All right?|Все в порядке?
So let's take a look and see what happens over here.|Итак, давайте посмотрим, что здесь происходит.
Let's take a look at the, look, it says it changed the state.|Давайте посмотрим, смотри, там написано, что изменилось состояние.
Over here, and let's take a look at it.|Вот сюда, и давайте взглянем на это.
Let's go to privilege mode and do a show stand by.|Давайте перейдем в привилегированный режим и сделаем шоу в режиме ожидания.
And it says, is, state is initialization,|И он говорит, что состояние - это инициализация,
the virtual IP address is such.|виртуальный IP-адрес такой.
The active router is unknown, I guess we're, we're too quick for it.|Активный маршрутизатор неизвестен, я думаю, мы слишком быстрые для этого.
What it should say is that this is the standby router [LAUGH] and then the other one is the active router.|Он должен сказать, что это резервный маршрутизатор [СМЕЕТСЯ], а второй - активный маршрутизатор.
Let's take a look at the other one,|Давайте посмотрим на другой,
I guess the packet traders are just working too slow for us.|Я полагаю, что пакетные трейдеры работают для нас слишком медленно.
[BLANK_AUDIO]|[BLANK_AUDIO]
CSS standby just changed to active.|Режим ожидания CSS только что стал активным.
Let's do control Z, show standby, and the state is active.|Сделаем управление Z, покажем режим ожидания и состояние активно.
This state is active.|Это состояние активно.
So now package are flowing through this router,|Итак, теперь пакеты проходят через этот маршрутизатор,
even thought it has that lower priority,|даже думал, что у него более низкий приоритет,
but the other one is down.|но другой не работает.
So it's gotta go through this one.|Так что надо пройти через это.
Let's take, let's prove that.|Давайте, давайте это докажем.
Let's prove that by using our Telnet.|Давайте докажем это с помощью нашего Telnet.
All right, let's stop this ping real quick.|Хорошо, давайте поскорее остановим этот пинг.
[BLANK_AUDIO]|[BLANK_AUDIO]
>> And let's do that Telnet to the virtual, the virtual IP address.|>> А давайте сделаем Telnet виртуальным, виртуальным IP-адресом.
Hit Enter.|Нажмите Enter.
[BLANK_AUDIO]|[BLANK_AUDIO]
Now we're inside a router, which router are we in?|Теперь мы внутри маршрутизатора, в каком маршрутизаторе мы находимся?
[BLANK_AUDIO]|[BLANK_AUDIO]
We're inside router one.|Мы внутри первого роутера.
It switched over to the other router.|Он переключился на другой маршрутизатор.
This is so cool.|Это так круто.
And HSRP is used in today's environment.|И HSRP используется в сегодняшней среде.
And really, that's all you really, you know need to be aware of.|И действительно, это все, о чем вы действительно знаете, что вам нужно знать.
There's other things.|Есть еще кое-что.
Not to be aware of, but really need to concentrate on.|Не осознавать, но на самом деле нужно сосредоточиться.
Just that right there.|Просто прямо здесь.
Just doing that right there is good enough.|Достаточно просто сделать это прямо сейчас.
Or, well,|Или ну
I don't wanna say that because what happens if your WLAN goes down, right?|Я не хочу этого говорить, потому что что произойдет, если ваша WLAN выйдет из строя, верно?
So let's talk about that and also.|Так что давайте поговорим об этом и тоже.
So there's other commands, as you can see here, just for the basic configuration of HSRP, just by putting the virtual IP address,|Итак, есть и другие команды, как вы можете видеть здесь, только для базовой конфигурации HSRP, просто помещая виртуальный IP-адрес,
putting you know, giving a group virtual IP address and then actually giving a priority number, so one can be active, one can be standby, and|чтобы вы знали, давая групповой виртуальный IP-адрес, а затем фактически давая номер приоритета, чтобы один мог быть активным, другой мог быть резервным и
boom, it's up and running, it's working,|бум, он работает, он работает,
no big, no biggie.|не большой, не большой.
Now, can you tweak that?|Теперь вы можете это настроить?
Can you tweak that?|Вы можете это настроить?
Of course.|Конечно.
But what's gonna happen if I go back and turn on?|Но что произойдет, если я вернусь и включу?
I'd fix the issue.|Я бы исправил проблему.
And I'd go inside, config t,|И я бы пошел внутрь, конфиг т,
Interface F 0/0, and do a no shut.|Интерфейс F 0/0, и ничего не закрыто.
It was a mistake.|Это было ошибкой.
Somebody went in there for what ever reason and they decided to do a no shut.|Кто-то вошел туда по какой-либо причине, и они решили не закрывать глаза.
And let's see whats gonna happen.|И посмотрим, что произойдет.
Let's take a look, let's standby here.|Давайте посмотрим, давайте здесь подождем.
See if things are going to change, the states change.|Посмотрите, не изменится ли что-то, состояние изменится.
Oh, so you can see that that's gonna take a while.|О, чтобы вы понимали, это займет некоторое время.
[BLANK_AUDIO]|[BLANK_AUDIO]
And let's do that ping.|И давайте сделаем этот пинг.
[BLANK_AUDIO]|[BLANK_AUDIO]
You see?|Ты видишь?
We're, it's thinking about the ping now.|Мы сейчас думаем о пинге.
Oh, we're, we're, we're getting there,|О, мы, мы, мы приближаемся,
because it's still, woo,|потому что это все еще, у-у,
now we've got a full green light, I guess SCP decided.|теперь у нас есть полный зеленый свет, я думаю, SCP решил.
Everything is good to go.|Все хорошо.
We're in and out, in and out, in and out.|Мы входим и выходим, входили и выходили, входили и выходили.
Takes a little bit, I mean, oh, there we go.|Нужно немного, я имею в виду, ну вот и все.
We're once again, back in, back in action,|Мы снова, снова в действии,
and we take a look at our router, it says [UNKNOWN] says standby.|и мы смотрим на наш маршрутизатор, он говорит [НЕИЗВЕСТНО] говорит о режиме ожидания.
Really?|В самом деле?
Let's take a look at it.|Давайте посмотрим на это.
Show a standby.|Показать режим ожидания.
[BLANK_AUDIO]|[BLANK_AUDIO]
It says state is standby.|Он говорит, что состояние находится в режиме ожидания.
Oh, [INAUDIBLE] is going crazy.|О, [НЕРАЗБОРЧИВО] сходит с ума.
It should say active, obviously.|Очевидно, следует сказать, что активен.
It might take a while for it to do, but let's find out.|Это может занять некоторое время, но давайте выясним.
Let's see if it's actually going to be Standby or active.|Посмотрим, будет ли он на самом деле в режиме ожидания или активным.
What's going on there?|Что там происходит?
The other one says active, this one says standby, we're going crazy today.|Другой говорит, что активен, этот говорит в режиме ожидания, сегодня мы сходим с ума.
And let's see, let's telnet.|И посмотрим, давайте телнет.
Whoa.|Ого.
Let's telnet, Ctrl+C, let's telnet to the virtual IP,|Давайте telnet, Ctrl + C, давайте подключимся к виртуальному IP,
C-I-S-C-O, and we're still going to router one.|C-I-S-C-O, и мы все еще собираемся маршрутизировать один.
Why is that?|Почему это?
Because, there's a command called preempt.|Потому что есть команда preempt.
And I'll show it to you.|И я тебе это покажу.
[BLANK_AUDIO]|[BLANK_AUDIO]
Oh, config T.|Ой, конфиг T.
[BLANK_AUDIO]|[BLANK_AUDIO]
Standby.|Ожидать.
One.|Один.
[BLANK_AUDIO]|[BLANK_AUDIO]
My typing skills.|Мои навыки набора текста.
[BLANK_AUDIO]|[BLANK_AUDIO]
Oh, sorry.|Ой, извини.
[BLANK_AUDIO]|[BLANK_AUDIO]
Inside the interface there lies, inside the interface, add 0, slide 0.|Внутри интерфейса лежит, внутри интерфейса добавьте 0, слайд 0.
Standby.|Ожидать.
[BLANK_AUDIO]|[BLANK_AUDIO]
One.|Один.
All right preempt.|Ладно выгружай.
Look where it says, overthrow lower priority.|Посмотри, где написано, сбрось более низкий приоритет.
Active routers.|Активные роутеры.
So, that was acting as the active router,|Итак, это действовал как активный маршрутизатор,
but see I didn't put in preempts saying,|Но смотри, я не вставлял упущений, говоря,
hey, when I come back, you give me back my spot.|эй, когда я вернусь, ты вернешь мне место.
That's what that means.|Вот что это значит.
So, let's go ahead and do that.|Итак, давайте продолжим и сделаем это.
STANDBY 1 PREEMPT.|РЕЖИМ ОЖИДАНИЯ 1 ПРЕДВАРИТЕЛЬНЫЙ.
Boom!|Бум!
Look at that.|Посмотри на это.
[SOUND] I'm active now.|[ЗВУК] Сейчас я активен.
All right?|Все в порядке?
So, it overthrows, all right?|Итак, это свергает, хорошо?
It dominated the other one, it said, I'm active again.|Он доминировал над другим, он сказал: «Я снова активен».
All right?|Все в порядке?
That's the whole purpose of the preempt command.|В этом вся цель команды preempt.
You WR, Ctrl+Z, show STANDBY, and now, I'm active.|Вы WR, Ctrl + Z, показываете STANDBY, и теперь я активен.
Right?|Правильно?
I have the higher priority.|У меня высший приоритет.
I should be active.|Я должен быть активным.
The other one was still active because I didn't do the preemption command.|Другой все еще был активен, потому что я не выполнил команду приоритетного прерывания.
So, preempt is, it's, it's a double-edged sword really, because it is interface that went down, goes down again, then it's|Итак, упреждение - это, на самом деле, это палка о двух концах, потому что интерфейс вышел из строя, снова вышел из строя, а затем
gonna change back to the other one.|собираюсь вернуться к другому.
And then when it comes back up again, then you're gonna go back again over here.|А потом, когда он снова появится, ты снова вернешься сюда.
So, it could be a back and forth, so it depends on you.|Таким образом, это может быть вперед и назад, так что это зависит от вас.
If you know that,|Если ты это знаешь,
that's a troublesome, it could be the actual interface of the router.|это хлопотно, это может быть фактический интерфейс маршрутизатора.
You know, the [UNKNOWN] speed has messed up, then you need to swap it out, or it could be a bad cable, or whatever the case may be.|Вы знаете, скорость [НЕИЗВЕСТНО] испортилась, тогда вам нужно ее поменять, или это может быть плохой кабель, или в любом другом случае.
You know, you may not want that to be the active router, so,|Вы знаете, вы можете не захотеть, чтобы это был активный маршрутизатор, поэтому,
when choosing the active router, choose appropriately, correctly.|Выбирая активный роутер, выбирайте соответственно, правильно.
Make sure that those interfaces are good to go, and that the cables are good to go.|Убедитесь, что эти интерфейсы исправны, а кабели готовы к работе.
Cuz if it's constantly going up and down,|Потому что, если он постоянно поднимается и опускается,
it's gonna be an issue regardless.|в любом случае это будет проблемой.
Okay?|Ладно?
Now, one of the last commands that I wanna show you, with HSRP, is tracking.|Теперь одна из последних команд, которые я хочу показать вам с HSRP, - это отслеживание.
Right?|Правильно?
Because, now, and I, what tracking does,|Потому что теперь и я, что отслеживает,
and let's look at the actually topology,|и давайте посмотрим на собственно топологию,
so you can understand, I'm gonna track these links right here, right?|так что вы понимаете, я собираюсь отслеживать эти ссылки прямо здесь, верно?
And, you know, right now, we're going this way, going across.|И вы знаете, прямо сейчас мы идем сюда, переходим.
But if this goes down, then it, if you have the tracking,|Но если он выйдет из строя, то, если у вас есть отслеживание,
the tracking says, hey, wait a minute.|трекинг говорит: эй, подожди минутку.
This link went down.|Эта ссылка не работает.
We need to decrement the priority number,|Нам нужно уменьшить номер приоритета,
and make this one the active router, and send it this way, but unfortunately,|и сделайте его активным маршрутизатором и отправьте его таким образом, но, к сожалению,
the programming behind the package tracer we can do the tracking command, but it only decrements by ten.|Программируя трассировщик пакетов, мы можем выполнить команду отслеживания, но она уменьшается только на десять.
So, this 150 will always be higher than that one.|Итак, эти 150 всегда будут выше, чем эти.
And you'll still see connectivity, that'll be flowing this way, but you'll see that this will remain active because the higher priority,|И вы по-прежнему будете видеть возможность подключения, которая будет проходить таким образом, но вы увидите, что она останется активной, потому что более высокий приоритет,
and this all will be standby, but packets will be flowing this way.|и все это будет в режиме ожидания, но пакеты будут проходить таким образом.
All right?|Все в порядке?
Don't let it confuse you.|Пусть это вас не смущает.
All right, what it, what the tracking is,|Хорошо, что это такое, что такое отслеживание,
what it allows you to do,|что это позволяет вам делать,
is actually put in a number, so if this is 150, and this is 110,|фактически помещается в число, поэтому, если это 150, а это 110,
I wanna subtract, I don't know, I wanna subtract a 100 from it.|Я хочу вычесть, я не знаю, я хочу вычесть из него 100.
All right?|Все в порядке?
And then, it, they'll, this area, this goes down, and you're tracking this one up here, also track the 100 from it, and then|И затем, они будут, эта область, это идет вниз, и вы отслеживаете это здесь, также отслеживаете 100 из него, а затем
this will become ten.|это станет десять.
So, automatically, boom this is will be an active router, and this be a standby router, and that information will flow that way.|Таким образом, автоматически будет активный маршрутизатор, а это резервный маршрутизатор, и эта информация будет передаваться таким образом.
Unfortunately the package tracer doesn't allow you to put in whatever number you want to subtract.|К сожалению, трассировщик пакетов не позволяет ввести любое число, которое вы хотите вычесть.
It subtracts automatically by ten.|Он автоматически вычитает десять.
All right so, we're happy.|Хорошо, мы счастливы.
So, but it'll still do the correct job.|Итак, но он все равно будет делать правильную работу.
So, let's go ahead, and do the tracking first.|Итак, давайте продолжим и сначала займемся отслеживанием.
Let's do the tracking.|Сделаем отслеживание.
So, we're gonna track the [INAUDIBLE]|Итак, мы собираемся отслеживать [НЕРАЗБОРЧИВО]
zero, zero.|ноль, ноль.
We're gonna go config config T interface F0/0 STANDBY 1 TRACKING, and then you put the, okay, standby,|Мы собираемся настроить config T interface F0 / 0 STANDBY 1 TRACKING, а затем вы поместите, хорошо, режим ожидания,
oh sorry standby its one, it has to be standby one,|Ой, извините, в режиме ожидания, он должен быть в режиме ожидания,
okay, standby, this should be one.|хорошо, в режиме ожидания, это должно быть.
[INAUDIBLE] Okay, STANDBY TRACK F0/1.|[Неразборчиво] Хорошо, ДОРОЖКА F0 / 1.
All right?|Все в порядке?
We WR.|Мы WR.
Let's take a look at the commands,|Давайте посмотрим на команды,
let's make sure that it's all hunky dory.|давайте удостоверимся, что все это работяга дори.
Show standby.|Показать режим ожидания.
Wow, all right.|Вау, хорошо.
[SOUND] Here's our priority, expires,|[ЗВУК] Вот наш приоритет, истекает,
where's my tracking?|где мое отслеживание?
It should be in there somewhere.|Он должен быть где-то там.
Your name, priority 150, stand by, active router, preemption is enabled.|Ваше имя, приоритет 150, режим ожидания, активный маршрутизатор, приоритетное прерывание включено.
It should show you that it is tracking.|Он должен показать вам, что идет отслеживание.
It should have let me do a by a stand by,|Это должно было позволить мне сделать резерв,
and the group number, but, okay.|и номер группы, но ладно.
Hm.|Хм.
Hm, hm, hm, hm, hm.|Хм, хм, хм, хм, хм.
Okay, all right, so we're tracking that F0/1 interface.|Хорошо, хорошо, мы отслеживаем интерфейс F0 / 1.
All right, let's go to the other routers,|Хорошо, перейдем к другим роутерам,
do the same thing,|сделай то же самое,
let's try that interface in case it goes out.|давайте попробуем этот интерфейс на случай, если он погаснет.
Config T STANDBY, and it's funny,|Конфиг T STANDBY, и это забавно,
now this one says that,|теперь этот говорит,
cuz this isn't global configuration interface at 0/0 STANDBY TRACK.|потому что это не глобальный интерфейс конфигурации в 0/0 STANDBY TRACK.
Oh, all right, and then you put in the interface that you are tracking F 0/1,|Хорошо, а затем вы добавляете интерфейс, который отслеживаете, F 0/1,
let me see something before I do that.|позволь мне кое-что увидеть, прежде чем я это сделаю.
Before, because, now, you see, STANDBY 1,|Раньше, потому что теперь, как вы видите, STANDBY 1,
the only one's giving an error.|единственный выдает ошибку.
That's why you can't see it.|Вот почему вы этого не видите.
STANDBY 1, TRACK F0/1.|РЕЖИМ ОЖИДАНИЯ 1, ДОРОЖКА F0 / 1.
Hello, and there you go.|Привет, вот и все.
[UNKNOWN] Ctrl+Z, show STANBY,|[НЕИЗВЕСТНО] Ctrl + Z, показать STANBY,
and there it is right there.|и вот оно прямо там.
Track interface at F 0/1 decrement by ten.|Отслеживайте интерфейс при F 0/1 с уменьшением на десять.
So, lets go back to router zero, cuz it was acting silly.|Итак, давайте вернемся к нулевому маршрутизатору, потому что он вел себя глупо.
Not doing what it was supposed to do.|Не делал того, что должен был делать.
All right, and lets do that same command again.|Хорошо, давайте сделаем ту же команду снова.
Config T, or maybe it was just me.|Конфиг Т, а может это был только я.
Config T Interface F0/0 STANDBY 1 TRACK F0/1.|Конфиг Т Интерфейс F0 / 0 РЕЖИМ ОЖИДАНИЯ 1 ДОРОЖКА F0 / 1.
And here we are.|И вот мы здесь.
Ctrl+Z.|Ctrl + Z.
Show STANBY.|Показать STANBY.
All right, and there it is here.|Хорошо, и вот оно здесь.
Now you can actually see it.|Теперь вы действительно можете это увидеть.
[SOUND] And you can see it only let's you [UNKNOWN].|[ЗВУК] И вы можете это увидеть, только позвольте вам [НЕИЗВЕСТНО].
You should be able to put an actual number, that you wanna subtract,|Вы должны иметь возможность поставить действительное число, которое хотите вычесть,
from the priority number, if that interface going down.|от номера приоритета, если этот интерфейс выходит из строя.
All right, so let's see how this is gonna work.|Хорошо, давайте посмотрим, как это будет работать.
So, again, let's exit outta here.|Итак, снова давайте выйдем отсюда.
Okay, and we're going to ping, or ping minus t.|Хорошо, и мы собираемся пинговать или пинговать минус т.
All right, to our web server.|Хорошо, на наш веб-сервер.
Awesome, awesome.|Круто круто.
We're going through that router zero.|Мы проходим через нулевой маршрутизатор.
So, now we're going to change, well, we're gonna kill this F/01 right here.|Итак, теперь мы собираемся измениться, ну, мы убьем эту F / 01 прямо здесь.
So, Config T INTERFACE F0/1,|Итак, Config T INTERFACE F0 / 1,
shut.|закрыть.
Let's minimize.|Сведем к минимуму.
Get to the PC there it is right here.|Подойдите к ПК, вот и все.
We lost connectivity.|Мы потеряли связь.
Look at that.|Посмотри на это.
Destination unreachable.|Пункт назначения недоступен.
Destination unreachable.|Пункт назначения недоступен.
Request timeout.|Тайм-аут запроса.
It's thinking.|Это думает.
It's trying to change things over.|Он пытается все изменить.
Request timeout.|Тайм-аут запроса.
Boom!|Бум!
Now we're going again.|Теперь мы снова идем.
Now we're going again.|Теперь мы снова идем.
All right.|Все в порядке.
So, now we should be going the other way.|Итак, теперь мы должны пойти другим путем.
Now we're going the other way.|Теперь идем другим путем.
Let's, let's see if that's true.|Посмотрим, правда ли это.
Let's tell MET why did I close that.|Расскажем МЕТ, почему я это закрыл.
Let's tell MET to the virtual IP, Cisco.|Скажем МЕТ виртуальному IP, Cisco.
And it says, I'm going to router zero.|И там написано: собираюсь на нулевой роутер.
How in the world is that possible?|Как вообще такое возможно?
Cuz this is what it's doing.|Потому что это то, что он делает.
What's happening is, it's going up this way, then finding that it can't go that way, then it comes back down, and it goes|Что происходит, это то, что он идет вверх, затем обнаруживает, что он не может идти таким путем, затем он возвращается вниз и идет
this way.|сюда.
And I can show you that in simulation mode.|И я могу показать вам это в режиме моделирования.
In simulation mode.|В режиме моделирования.
So, let me show you, gonna click here.|Итак, позвольте мне показать вам, нажмите здесь.
PC zero, to destination.|Нулевой компьютер, по назначению.
Auto capture and play.|Автоматический захват и воспроизведение.
Let's sit back and watch the movie.|Давайте сядем и посмотрим фильм.
Here comes this ping.|Вот этот пинг.
This ICMP packet right?|Этот ICMP-пакет не так ли?
Goes out both interfaces.|Гаснет оба интерфейса.
Floods that out, right.|Вылезает наружу, верно.
Boom boom boom.|Бум бум бум.
You've got an X over here.|У вас здесь крестик.
Oh well, okay, got an X over here because that's the active router, and then it came back down.|Хорошо, хорошо, здесь X, потому что это активный маршрутизатор, а затем он снова отключился.
And then it sends it the right way,|И тогда он отправляет его в правильном направлении,
because it says hey you can't go through there.|потому что там написано: "Эй, ты не можешь пройти туда".
Can't get to that destination that way, go up and then come to the actual server.|Не можете добраться до места назначения таким образом, поднимитесь, а затем дойдите до фактического сервера.
So you can see that that's the way the packet is going.|Итак, вы можете видеть, что пакет идет именно так.
Alright.|Хорошо.
So in the fire trace it is a little bit funky in the way that it works but you get to understand what's going on alright you understand what's going on.|Так что в трассировке пожара это немного странно в том, как это работает, но вы понимаете, что происходит, хорошо понимаете, что происходит.
When you're tracking this interface okay,|Когда вы отслеживаете этот интерфейс,
your suppose to be able to bring back or bring down the priority number to something lower.|Вы предполагаете, что сможете вернуть или снизить число приоритета до чего-то более низкого.
Than this one, but we can't.|Чем этот, но мы не можем.
This, this priority number and that priority is 140, alright?|Это, этот номер приоритета и этот приоритет 140, хорошо?
This is 110.|Это 110.
So this is still the active router.|Итак, это все еще активный маршрутизатор.
So that's why it still wants to go that way.|Вот почему он все еще хочет идти этим путем.
But then when it sees that it can go that way, it brings it back down, and then comes this way.|Но затем, когда он видит, что может идти этим путем, он возвращает его обратно, а затем идет этим путем.
So even though, it's not working like we want it to work well, we can subtract it,|Таким образом, даже если он не работает так, как мы хотим, чтобы он работал хорошо, мы можем вычесть его,
make this a standby and it's inactive, is to say, hey, listen, that's down.|сделайте это резервным, и он неактивен, то есть, эй, послушайте, это не работает.
I can't send you that way, so let me send you over to the next router.|Я не могу отправить вас этим путем, поэтому позвольте мне отправить вас к следующему маршрутизатору.
It still sends it over to the next router regardless.|Он все равно отправляет его следующему маршрутизатору.
Alright.|Хорошо.
So, because these are,|Итак, потому что это
these guys are talking to each other with those three-second hellos.|эти парни разговаривают друг с другом этими трехсекундными приветствиями.
They're saying, hey, something's going on here.|Они говорят, эй, здесь что-то происходит.
I'm gonna send it to that way.|Я отправлю его туда.
It took a little bit.|Это заняло немного времени.
It took a little bit to do so but the reason is because the priority number.|На это потребовалось немного времени, но причина в том, что номер приоритета.
Because if you look at it, if you look at the priority number here,|Потому что если вы посмотрите на это, если вы посмотрите на номер приоритета здесь,
so control Z, show standby.|так что контролируйте Z, покажите режим ожидания.
Not tanby It still shows as active.|Не загар. Он все еще отображается как активный.
You see priority numbers 140.|Вы видите номера приоритета 140.
Because it's subtracted ten from it,|Потому что из него вычитается десять,
that's all.|вот и все.
Where the other one is still 110, so it still shows standby as the other one and we have the preemption saying hey,|Если у другого по-прежнему 110, поэтому он все еще показывает режим ожидания, как и другой, и у нас есть приоритетное сообщение: «Эй,
I'll throw anything that's lower priority number than mine.|Я выброшу все, что имеет более низкий приоритет, чем мой.
So I'm always gonna be active so they're,|Так что я всегда буду активен, так что они,
they're playing against each other, right,|они играют друг против друга, да,
because we can put the number we want it to.|потому что мы можем поставить желаемое число.
If I would have done the math correctly,|Если бы я правильно посчитал,
and I would have, you know, said,|и я бы сказал, знаете,
okay, this is, so this is 105, alright,|хорошо, это так, это 105, хорошо,
and,|а также,
I would have said 105 on this one, I would have 100, the other one.|Я бы сказал 105 на этом, я бы 100, другой.
Then if I also tried ten on that one, then it would have been okay cool.|Тогда, если бы я тоже попробовал десять на этом, то было бы нормально круто.
This would be 95, then this will be a 100|Это будет 95, тогда это будет 100
and this will be the active router, and this will be the standby router.|и это будет активный маршрутизатор, а это будет резервный маршрутизатор.
But we didn't do the math correctly,|Но мы неправильно посчитали,
that's why.|поэтому.
But still the point is these are redundant protocols.|Но все же дело в том, что это избыточные протоколы.
They talk to each other to allow traffic to be switched automatically to a router that is working properly to get to your|Они общаются друг с другом, чтобы разрешить автоматическое переключение трафика на маршрутизатор, который правильно работает, чтобы добраться до вашего
destination.|место назначения.
And that is so cool and again the other writing the other relation protocols the they do the same thing and we'll talk about those in this next lesson to come so|И это так здорово, и снова другой, пишущий другие протоколы отношений, они делают то же самое, и мы поговорим о них в следующем уроке, поэтому
I hope you understood it and you will be using this in the real world I guarantee you and you will be seeing this in your|Надеюсь, вы это поняли и будете использовать это в реальном мире, я гарантирую вам, и вы увидите это в своем
certification so read up on it.|сертификация, так что читайте об этом.
To get a lot more, you know, I guess, wet,|Чтобы получить больше, знаете, я думаю, мокрый,
as we would say.|как бы мы сказали.
I get more in, in-depth in it, all right.|Я вникаю в нее больше, все хорошо.
More than the, the video so you can really, you know, get a full, full,|Более того, видео, чтобы вы действительно могли получить полное, полное,
full understanding of it.|полное понимание этого.
I'll see you in the next one.|Увидимся в следующем.
[BLANK_AUDIO]|[BLANK_AUDIO]
  
