D:\mailCloud\prjother\tmp\1\c112_VRRP and GLBP.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
All righty then, HSRP is, welcome back.|Итак, HSRP есть, с возвращением.
Let's just say it, cuz I always say that.|Скажем так, потому что я всегда так говорю.
All right, so, HSRP is the big one.|Итак, HSRP - самый большой.
All right.|Все в порядке.
It is the one that you need to be really,|Это тот, кем тебе нужно быть на самом деле,
really, really, really, really, really,|действительно, правда, правда, правда, правда,
really, really familiar with, all right?|действительно, действительно знакомы, хорошо?
You, like I said, you will be using it.|Вы, как я уже сказал, будете его использовать.
I've used it.|Я использовал это.
And I've been part of a trouble shooting process out there in the real world,|И я был частью процесса устранения неполадок в реальном мире,
all right?|все в порядке?
So, HSRP is a popular redundancy protocol,|Итак, HSRP - популярный протокол резервирования,
VRRP is basically the same thing.|VRRP - это в основном то же самое.
The same thing.|Тоже самое.
The only difference, like I, we said in the overview, it's, you know, any, any,|Единственная разница, как я, как мы сказали в обзоре, это, понимаете, любой, любой,
you can use any manufactural routers, an open standard.|можно использовать любые производственные роутеры открытого стандарта.
Right, so you're not bound to just one particular manufacturer.|Верно, значит, вы не привязаны к одному конкретному производителю.
But, the terminology changes a little bit Instead of active and standby like we did HSRP, it uses master and backup.|Но терминология немного меняется. Вместо активного и резервного, как мы делали HSRP, он использует главный и резервный.
Okay?|Ладно?
Standby group you can use a standby group as the vrrp group.|Резервная группа вы можете использовать резервную группу как группу vrrp.
That's what it's called.|Так это называется.
The master router can share the virtual ip address.|Главный маршрутизатор может совместно использовать виртуальный IP-адрес.
So, that's all it is, is just the terminology that it's using but it's basically the same thing.|Итак, это все, что он есть, это просто терминология, которую он использует, но в основном это то же самое.
Obviously, the timers are different.|Очевидно, что таймеры разные.
The timers are different.|Таймеры разные.
They're faster, but as like I told you in the overview,|Они быстрее, но, как я уже говорил вам в обзоре,
you can change the timers on HSRP to match VRRP.|вы можете изменить таймеры на HSRP в соответствии с VRRP.
All right?|Все в порядке?
Through down time.|Через время простоя.
And then the advertise and then the master and learns only.|А потом реклама, а потом мастер и только учится.
Basically, the, the master is the one that holds all the information.|По сути, хозяин - это тот, кто хранит всю информацию.
That would be the active, right?|Это было бы активным, правда?
And then just send out to everybody else,|А потом просто разошлите всем,
and everybody else is learning based off that.|и все остальные учатся на этом.
Obviously, the master goes down, the old ones take over.|Очевидно, хозяин уходит, старые берут верх.
Okay, that's, it's does vrrp.|Ладно, это действительно vrrp.
As far as the configuration, it would be the same exact thing.|Что касается конфигурации, то это будет то же самое.
But, this time you actually, when you go on the interface,|Но на этот раз вы на самом деле, когда заходите в интерфейс,
you actually would type vrrp.|вы бы фактически набрали vrrp.
And, as you saw it wasn't there in the CISCO packet tracer.|И, как вы видели, его не было в трассировщике пакетов CISCO.
And then you put the group number, the ip,|Затем вы вводите номер группы, ip,
and then, the virtual ip you're gonna use.|а затем виртуальный IP-адрес, который вы собираетесь использовать.
Then the preempt, right through overthrow,|Затем упреждение, прямо через свержение,
the lore, active, or master routers, or not master routers,|lore, активные или мастер-маршрутизаторы, или не мастер-маршрутизаторы,
backup routers.|резервные роутеры.
Or is it, was it backup?|Или это была резервная копия?
Yes.|Да.
Backup.|Резервное копирование.
Okay?|Ладно?
And then the and then you're gonna mess around with the timers to millisecond.|А потом ты будешь возиться с таймерами до миллисекунды.
And you can do the same thing, I mean, do you really wanna do milliseconds?|И вы можете делать то же самое, я имею в виду, вы действительно хотите делать миллисекунды?
I mean, it's completely up to you.|Я имею в виду, это полностью зависит от вас.
You know, depending on your bandwidth.|Вы знаете, в зависимости от вашей пропускной способности.
Remember, this is, they are going across wireless networks allow these routers,|Помните, что они проходят через беспроводные сети, позволяют этим маршрутизаторам,
if you have, you know, multiple routers,|если у вас есть несколько маршрутизаторов,
so you really gotta be careful how you're gonna go ahead and do this.|так что тебе действительно нужно быть осторожным, как ты собираешься делать это.
Do you really want every so, you know,|Вы действительно хотите, чтобы все так, знаете ли,
in less than a second, information is going back and forth?|менее чем за секунду информация передается туда и обратно?
I can understand why, so then the switchover happens a lot quicker,|Я могу понять почему, так что переключение происходит намного быстрее,
you know, cuz think about it.|вы знаете, потому что подумайте об этом.
If it's 3 seconds, 3, 1, 2, 3, 1, 2, 3.|Если это 3 секунды, 3, 1, 2, 3, 1, 2, 3.
You know, to say hey, I'm still here, I'm still good.|Знаешь, чтобы сказать: эй, я все еще здесь, я все еще в порядке.
But then it's 10 seconds to say I'm dead,|Но потом 10 секунд сказать, что я мертв,
I'm gone.|Меня нет.
Then it's 1, 2, 3, 4, 5, I mean really,|Тогда это 1, 2, 3, 4, 5, я действительно имею в виду,
seriously.|шутки в сторону.
So, and yeah, you can tweak it to milliseconds.|Итак, и да, вы можете настроить его до миллисекунд.
Just be careful on how quickly you want those milliseconds to be how fast.|Просто будьте осторожны с тем, насколько быстро должны быть эти миллисекунды.
Because, again, it all determines on your bandwidth.|Потому что, опять же, все зависит от вашей пропускной способности.
But HSRP can do the exact same thing.|Но HSRP может делать то же самое.
All right.|Все в порядке.
The only reason that the timers were at 3|Единственная причина, по которой таймеры были на 3
seconds, and at 10 seconds because it's 1994.|секунд и 10 секунд, потому что сейчас 1994 год.
You know?|Ты знаешь?
That's why we did, the, the speed wasn't there.|Вот почему мы это сделали, скорости не было.
But now the speed is there.|Но теперь скорость есть.
So you can actually tweak those timers the same way you can for vrrp.|Таким образом, вы можете настроить эти таймеры так же, как и для vrrp.
So it's basically the exact same thing.|Так что это в основном то же самое.
It's basically the exact same thing.|По сути, это то же самое.
Again, no low bounds, no low bounds.|Опять же, никаких нижних границ, никаких нижних границ.
And the way that you can play around,|И то, как вы можете поиграть,
with the low balancing to pretend that you're low balancing.|с низкой балансировкой, чтобы притвориться, что вы плохо балансируете.
Let's say you have three or four routers, you can separate them into different groups.|Допустим, у вас есть три или четыре маршрутизатора, вы можете разделить их на разные группы.
And then you can tell hey, if this group fails go to this one,|И тогда вы можете сказать, эй, если эта группа не справится, перейдите к этой,
if that group fails go to this one, if this group fail then go to this one.|если эта группа терпит неудачу, переходите к этой, если эта группа терпит неудачу, переходите к этой.
So you can use them that way but that's not real redundancy.|Таким образом, вы можете использовать их таким образом, но это не настоящая избыточность.
The one that has real redundancy is GLBP.|Тот, который имеет реальное резервирование, - это GLBP.
GLBP really has redundancy,|GLBP действительно имеет избыточность,
because it's active-active, meaning every router is active, and they work on a round robin type, where,|потому что он активен-активен, что означает, что каждый маршрутизатор активен, и они работают по циклическому типу, где,
hey, let's go ahead and take this traffic, and then let's send it all to this particular router.|Эй, давайте возьмем этот трафик, а затем отправим его на этот конкретный маршрутизатор.
Let's send part of it to this one, and part of it to that one.|Давайте отправим часть этому, а часть тому.
That's how GLBP works.|Вот как работает GLBP.
So, it's really truly doing some load-balancing.|Итак, он действительно выполняет некоторую балансировку нагрузки.
So, it uses a single, virtual IP address with multiple MAC, eh,|Таким образом, он использует один виртуальный IP-адрес с несколькими MAC-адресами.
it didn't highlight, with multiple MAC addresses.|он не выделялся с несколькими MAC-адресами.
That is really cool.|Это действительно круто.
So, I mean, think about it.|Я имею в виду, подумай об этом.
You're doing your arp, right?|Ты делаешь свой арп, верно?
So for every, you know, for every gateway that you're gonna using,|Итак, для каждого, вы знаете, для каждого шлюза, который вы собираетесь использовать,
it's gonna have it's own virtual MAC address too.|у него тоже будет собственный виртуальный MAC-адрес.
So that's pretty cool.|Так что это круто.
That's why they're active-active.|Вот почему они активны-активны.
So that they can do those low balancing.|Чтобы они могли выполнять эту низкую балансировку.
Right?|Правильно?
So everybody has an active virtual gateway, that's what they call AVGs.|Итак, у каждого есть активный виртуальный шлюз, это то, что они называют AVG.
All the routers are active-active.|Все роутеры активны-активны.
And they're virtual forwarders, they forward the information,|И они виртуальные экспедиторы, они пересылают информацию,
and there's different ways you can forward the information, and as you can see there,|и есть разные способы пересылки информации, и, как вы видите,
more than one router can be active.|может быть активным более одного маршрутизатора.
You're always gonna have one IP address.|У вас всегда будет один IP-адрес.
One IP address, one virtual IP address.|Один IP-адрес, один виртуальный IP-адрес.
That's what a VIP stands for, one virtual IP address.|Вот что означает VIP - один виртуальный IP-адрес.
But you will have virtual MAC addresses,|Но у вас будут виртуальные MAC-адреса,
and it makes sense, and it makes sense,|и это имеет смысл, и это имеет смысл,
because we're going the layer two, right?|потому что мы идем на второй слой, верно?
The layer two, do you want that MAC address to be different for every gateway.|Второй уровень, хотите ли вы, чтобы этот MAC-адрес был разным для каждого шлюза.
Okay.|Ладно.
Cuz you're again,|Потому что ты снова,
low balancing to different different routers.|низкая балансировка для разных роутеров.
And look that, that's an o, not a 0.|И посмотрите, это ноль, а не ноль.
What's up with that?|Что с этим?
Okay.|Ладно.
So GLBP, pretty much the same.|Итак, GLBP, почти то же самое.
GLBP 1, the virtual IP address.|GLBP 1, виртуальный IP-адрес.
GLBP 1, the priority.|ГЛБП 1, приоритет.
Again, the one with the highest priority is your active virtual gateway.|Опять же, активный виртуальный шлюз имеет самый высокий приоритет.
Where the other ones are your virtual forwarders, all right?|А где остальные ваши виртуальные экспедиторы, хорошо?
And then you can do the load-balancing,|А затем вы можете выполнить балансировку нагрузки,
and then you gonna do it host-dependent,|а затем вы сделаете это в зависимости от хоста,
you gonna do it round-robin, or weighted.|вы собираетесь делать это круговым или взвешенным.
The one that I put the asterisk on is the one that's the most popular one.|Я пометил звездочкой самый популярный.
Round-robin, meaning it takes turns.|Циклический, то есть по очереди.
Okay?|Ладно?
It's gonna see.|Это будет видно.
Okay, who's gonna be better, more available, less traffic?|Хорошо, кто будет лучше, доступнее, меньше трафика?
I'm gonna send it that way.|Я отправлю его туда.
Okay?|Ладно?
Round-robin type of effect.|Эффект циклического типа.
So this is the configuration for it.|Итак, это конфигурация для него.
This is the only one that's a little,|Это единственное, что немного,
well,|Что ж,
it's a lot different in the sense of that it does a little balancing commands.|он сильно отличается в том смысле, что выполняет небольшие команды балансировки.
And they have multiple MAC addresses and all, well,|И у них есть несколько MAC-адресов и все, ну,
you have one active virtual gateway and they're all forwarded, but they're all sending the information, which in the other ones are not,|у вас есть один активный виртуальный шлюз, и все они пересылаются, но все они отправляют информацию, которой нет в других,
they're either an active or standby, or they are a master and a backup.|они либо активны, либо резервны, либо они являются главным и резервным.
So they gotta wait until one does before the other one gets the info.|Поэтому им нужно подождать, пока один из них не сделает этого, прежде чем другой получит информацию.
Right?|Правильно?
The other one takes over.|Другой вступает во владение.
In here, you're low at,|Здесь у вас низкий уровень,
truly low balancing the information that's going to various routers.|действительно низкая балансировка информации, которая идет к различным маршрутизаторам.
And you almost keep forwarding that information.|И вы почти продолжаете пересылать эту информацию.
So when one dies the other one has that information already.|Итак, когда один умирает, у другого уже есть эта информация.
So and it keeps going and keeps going.|Так и продолжается, и продолжается.
So what you can see where GLBP, Cisco proprietary, all right.|Так что вы можете посмотреть, где GLBP, проприетарный Cisco, все в порядке.
Only Cisco routers only.|Только маршрутизаторы Cisco.
Which is not a bad thing.|Что неплохо.
All right.|Все в порядке.
GLBP is is very good to use.|GLBP очень удобен в использовании.
Okay.|Ладно.
And to be honest with you, I see it very little.|И, честно говоря, я этого очень мало вижу.
I seen more of HSRP than I have of GLBP.|Я видел больше HSRP, чем GLBP.
Why?|Зачем?
I really don't know a reason to,|Я действительно не знаю причины,
to tell you.|сказать тебе.
But again, every company, they gonna go out there.|Но опять же, каждая компания пойдет туда.
It's not gonna be the same.|Это не будет прежним.
So as far as for your certification, yeah definitely.|Итак, что касается вашей сертификации, да, безусловно.
What is it that you need to take from here is that you need a priority number,|Что вам нужно взять отсюда, так это то, что вам нужен номер приоритета,
that you have to have at least one router that's gonna be considered like here,|что у вас должен быть хотя бы один маршрутизатор, который будет рассматриваться как здесь,
active virtual gateway or a master or an active router.|активный виртуальный шлюз или мастер или активный маршрутизатор.
And then the, the other ones are waiting to see what happens.|А потом другие ждут, чтобы увидеть, что произойдет.
We're here with GLBP.|Мы здесь с GLBP.
You have all the routers constantly actively doing something.|У вас все роутеры постоянно что-то активно делают.
All right?|Все в порядке?
And with GLBP remember the round-robin.|А с GLBP помните о круговом.
That is the most popular way to send information.|Это самый популярный способ отправки информации.
All right.|Все в порядке.
It makes the decision.|Он принимает решение.
Okay, it's your turn, it's your turn, it's your turn, it's your turn,|Хорошо, теперь ваша очередь, это ваша очередь, это ваша очередь, это ваша очередь,
it's your turn, okay?|твоя очередь, ладно?
Obviously, it's making a smart decision based on the analysis of traffic.|Очевидно, что это разумное решение, основанное на анализе трафика.
But this is the, the way to go.|Но это путь.
All right?|Все в порядке?
Using the round-robin.|Используя круговой алгоритм.
But that's it, that's all there is to the redundancy protocols.|Но это все, это все, что касается протоколов резервирования.
That's all it is.|Вот и все.
And remember, when you're monitoring all this,|И помните, когда вы за всем этим следите,
which we're gonna talk about now in this next session.|о котором мы поговорим сейчас на следующей сессии.
When you're monitoring all this, you're not really looking, you,|Когда вы наблюдаете за всем этим, вы на самом деле не смотрите, вы,
you're only going to the router when you're third party software monitoring system tells you hey, there's a problem.|вы подходите к маршрутизатору только тогда, когда сторонняя система мониторинга программного обеспечения сообщает вам, что это проблема.
Oh, okay, let me go inside my router now and take a look.|О, ладно, позволь мне зайти в мой роутер и взглянуть.
You're not sitting there looking at your hundreds or thousands of interfaces to see if hey,|Вы не сидите и смотрите на свои сотни или тысячи интерфейсов, чтобы узнать, эй,
something is going on.|что-то происходит.
Okay?|Ладно?
So, in the next section now, we're gonna discuss about the monitoring,|Итак, в следующем разделе мы обсудим мониторинг,
the monitoring, the, the network using these different types of protocols.|мониторинг, сеть, использующая эти разные типы протоколов.
All right?|Все в порядке?
So, with this, again, don't sweat it too much.|Так что, опять же, не переживайте слишком сильно.
HSRP, VRRP, GLBP, just one of the new things that Cisco's putting in the test.|HSRP, VRRP, GLBP - лишь одно из нововведений, которые Cisco тестирует.
It's not as difficult as you think.|Это не так сложно, как вы думаете.
Again just read upon your chapters, and you'll be good to go.|Опять же, просто прочтите свои главы, и все будет хорошо.
I'll see you in the next session.|Увидимся на следующем сеансе.
[BLANK_AUDIO]|[BLANK_AUDIO]
  
  
