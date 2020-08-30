D:\mailCloud\prjother\tmp\1\c76_Point-to-Point ospf.md  


__|__
--|--
All right, welcome back everyone.|Хорошо, с возвращением всех.
This is, I know it looks the same as previous, but it's not the same.|Это, я знаю, выглядит так же, как и предыдущее, но это не то же самое.
I just did this lab.|Я только что сделал эту лабораторию.
What I did is, trying to save you time.|Я пытался сэкономить ваше время.
We did, this is, let's consider a point to point connection,|Мы сделали это, давайте рассмотрим соединение точка-точка,
you know that when you did your static routes and and RIP and EIGRP.|вы знаете это, когда создавали свои статические маршруты, а также RIP и EIGRP.
All right, so point to point connection.|Хорошо, так что соединение точка-точка.
We have serial connections over here and we have Ethernet down here.|Здесь у нас есть последовательные соединения, а здесь - Ethernet.
All right.|Отлично.
We have the IP addresses that we're using between the, between the routers.|У нас есть IP-адреса, которые мы используем между маршрутизаторами.
And we have the or the networks that we're using between the routers, and the networks that we're using for our LANs.|И у нас есть сети, которые мы используем между маршрутизаторами, и сети, которые мы используем для наших локальных сетей.
So all that's already configured,|Итак, все, что уже настроено,
so we can take a look at that,|так что мы можем взглянуть на это,
let's go to router 1.|переходим к роутеру 1.
Which is right there.|Что прямо здесь.
Let me move this over here.|Позвольте мне перенести это сюда.
All right.|Отлично.
And let's open it up a little bit.|И давайте немного приоткроем.
[NOISE]|[ШУМ]
All right.|Отлично.
And you can see that you're connected directly to the 10.1.1.4,|И вы можете видеть, что вы подключены напрямую к 10.1.1.4,
to 172.31.1.0, and the 192.168.1.0.|до 172.31.1.0 и 192.168.1.0.
And that's, there is no routing protocol because or else you would see it on here.|И здесь нет протокола маршрутизации, потому что иначе вы бы его здесь не увидели.
And or you're not learning anything,|И или ты ничего не узнаешь,
everything is connected to the route.|все связано с маршрутом.
And you see the interfaces that you're using.|И вы видите интерфейсы, которые используете.
Now let's talk about this interface before we begin.|А теперь давайте поговорим об этом интерфейсе, прежде чем мы начнем.
So one of the things that I failed to mention in the terminology portion of it,|Одна из вещей, о которых я не упомянул в терминологической части,
it's the loopback, the loopback address.|это петля, адрес петли.
The loopback address is used in OSPF when you're doing the designator router and backup designator router.|Адрес обратной связи используется в OSPF, когда вы делаете маршрутизатор с указателем и резервный маршрутизатор с указателем.
You use it because you could use loopbacks as a virtual interface.|Вы используете его, потому что вы можете использовать петли в качестве виртуального интерфейса.
It's not real.|Это нереально.
All right?|Отлично?
And that's one of the things that you can use to trump,|И это одна из вещей, которую вы можете использовать, чтобы превзойти,
if you would the elections.|если бы выборы.
You can fix the elections by using loopback addresses, okay?|Вы можете исправить выборы, используя адреса обратной связи, хорошо?
But you can use the loopback addresses as you would any other interface, so you can ping back and forth, so testing purposes, things of that nature.|Но вы можете использовать адреса обратной петли, как и любой другой интерфейс, так что вы можете пинговать туда и обратно, для целей тестирования и тому подобного.
So I create it.|Итак, я его создаю.
And you can have a different loopback interface per, per router.|И у вас может быть другой интерфейс обратной петли для каждого маршрутизатора.
What is the limitation on loopback addresses?|Какое ограничение на адреса обратной связи?
I really have not found a book that has told me,|Я действительно не нашел книги, в которой бы мне сказали,
hey, this is how many loopbacks you can create.|эй, вот сколько петель вы можете создать.
And I really haven't sat there to find out how many loopbacks you can create.|И я действительно не сидел там, чтобы узнать, сколько петель вы можете создать.
All right?|Отлично?
So if you have to create more than what,|Итак, если вам нужно создать больше, чем что,
you know, now let's say,|вы знаете, теперь давайте скажем,
let's give it a number.|дадим ему номер.
999,000.|999 000.
You have to create more than that.|Вы должны создать нечто большее.
Wow, I hope you're getting paid a lot of money.|Вау, я надеюсь, тебе платят много денег.
All right, but as regards the matter what you need to understand is that loopbacks can be used as just testing purposes.|Хорошо, но что касается того, что вам нужно понять, так это то, что петли могут использоваться только в целях тестирования.
But they still need to be advertised within OSPF.|Но их все еще нужно рекламировать в OSPF.
Now, the type of OSPF that we're doing is considered point-to-point.|Теперь тип OSPF, который мы делаем, считается двухточечным.
When you do a point-to-point OSPF,|Когда вы выполняете двухточечный OSPF,
there is no election.|нет выборов.
Now that's a loaded question with a loaded answer,|Это загруженный вопрос с загруженным ответом,
because the only reason,|потому что единственная причина,
the only reason that there is no election is because you have this serial that's going across.|единственная причина, по которой нет выборов, состоит в том, что у вас есть повторяющийся сериал.
That's the only reason.|Это единственная причина.
I wanna show you another lab,|Я хочу показать тебе другую лабораторию,
before we end this lesson.|прежде, чем мы закончим этот урок.
It's gonna be a comparison between point-to-point and multi-access.|Это будет сравнение между точка-точка и множественным доступом.
All right?|Отлично?
But I'm gonna show you several things that we're gonna be looking at.|Но я покажу вам несколько вещей, на которые мы будем смотреть.
We'll actually only comparing these two interfaces, the serial interface and the fast Ethernet interface.|На самом деле мы будем сравнивать только эти два интерфейса, последовательный интерфейс и интерфейс Fast Ethernet.
So you could notice the difference, and things I'm gonna point out to you,|Чтобы вы могли заметить разницу, и то, что я вам скажу,
that you need to look at.|что вам нужно посмотреть.
The configuration of OSPF is simple.|Конфигурация OSPF проста.
It is simple.|Это просто.
There's nothing to it.|Ничего особенного.
Understand what you're looking at,|Поймите, на что вы смотрите,
that's a different story.|это другая история.
All right?|Отлично?
And then you need to understand what you're looking at and that's what I want to point out to you.|И тогда вам нужно понять, на что вы смотрите, и это то, что я хочу вам указать.
So, what we're going to do is now is configure OSPF for IP version 4,|Итак, что мы собираемся сделать, это настроить OSPF для IP версии 4,
and we're going to go ahead and advertise using network statements.|и мы собираемся продвигаться вперед и рекламировать с помощью сетевых операторов.
So here we will use the actual network that we are connected to.|Итак, здесь мы будем использовать реальную сеть, к которой мы подключены.
So we are connected to the 10.114 and we are connected 192.168.1.0.|Итак, мы подключены к 10.114, и мы подключены к 192.168.1.0.
But don't forget, you have that loopback,|Но не забывайте, что у вас есть петля,
so you're also connected.|так что вы тоже связаны.
And let's use our handy dandy show commands.|И давайте воспользуемся нашими удобными командами dandy show.
#SH PROTOCOLS.|#SH ПРОТОКОЛЫ.
You can see that I'm using a loopback 0.|Как видите, я использую шлейф 0.
And let's bring it up further.|И давайте поднимем это дальше.
You can see that your fast Ethernet is a /24.|Вы можете видеть, что ваш быстрый Ethernet - это / 24.
You can see that you're using a /30,|Вы видите, что используете / 30,
obviously, for the ones on the serial.|очевидно, для тех, что указаны в сериале.
And your loopback is using also a /24.|И ваша петля также использует / 24.
Okay?|Ладно?
And, normally, I like to use a /30 for the loopbacks, and I will, or a /32, I should say.|И, как правило, мне нравится использовать / 30 для петлевых проверок, и я так и буду, или, я бы сказал, / 32.
When I use loopbacks for the election process which should be in the next lesson I believe, all right?|Когда я использую петли для процесса выборов, которые должны быть на следующем уроке, я думаю, хорошо?
But let's go ahead and configure OSPF now that we know the networks that we belong to, right?|Но давайте продолжим и настроим OSPF теперь, когда мы знаем сети, к которым мы принадлежим, верно?
We belong to the 192.168.1.0,|Мы принадлежим к 192.168.1.0,
the 10.1.1.4 and the 172.31.1.0.|10.1.1.4 и 172.31.1.0.
So, let's go ahead and configure OSPF.|Итак, приступим к настройке OSPF.
Config t on router 1.|Настроить на роутере 1.
Router OSPF.|Маршрутизатор OSPF.
Now you need,|Теперь тебе нужно,
you need to pick a process id number.|вам нужно выбрать идентификационный номер процесса.
You have from 1 through 65,535.|У вас от 1 до 65 535.
Do you need to know the range?|Вам нужно знать диапазон?
Yes, you need to know the range.|Да, вам нужно знать диапазон.
Will they try and trick you with the range?|Попытаются ли они обмануть вас дальностью?
Yes, they'll try and trick you with the range.|Да, они попытаются обмануть вас диапазоном.
Know that your process ID number is from 1 through 65,535.|Знайте, что ваш идентификатор процесса - от 1 до 65 535.
Remember that the process ID number,|Помните, что идентификационный номер процесса,
all it does,|все это делает,
it keeps track of that database,|он отслеживает эту базу данных,
that link state database that it creates.|эту базу данных состояний ссылок, которую он создает.
Gives it the stability of it.|Придает ему стабильность.
All right.|Отлично.
So, that's what that number is for,|Итак, вот для чего этот номер,
that is it.|вот оно что.
So you can pick an, it's local, it's local so I can pick whatever number I want.|Так что вы можете выбрать, он местный, он местный, поэтому я могу выбрать любой номер, который захочу.
So, we usually just pick one, all right.|Итак, мы обычно просто выбираем один, хорошо.
Now, we advertise using network statements,|Теперь мы рекламируем с помощью сетевых операторов,
network, we said what was it, 192.168.1.0.|сеть, мы сказали, что это было, 192.168.1.0.
0.0.0.255 and we'll pick area 0 just to keep it real world.|0.0.0.255, и мы выберем область 0, чтобы сохранить ее в реальном мире.
All right?|Отлично?
Area 0.|Площадь 0.
Remember your wildcard masking.|Помните о маскировке подстановочного знака.
You can use your constant 255, 255, 255,|Вы можете использовать свою константу 255, 255, 255,
255 and then subtract your mask from it and that'll give you your wildcard mask.|255, а затем вычтите из него маску, и вы получите маску подстановки.
Or if you just drew the line between the third and the fourth octet, and add the bit values to the right,|Или, если вы просто нарисовали линию между третьим и четвертым октетами и добавили битовые значения справа,
you know that it would be 255.|вы знаете, что это будет 255.
0's mean match exactly, and the 1's in the fourth octet mean any,|Среднее точное совпадение 0, а единицы в четвертом октете означают любое,
any numbers within that range from 1 to 255.|любые числа в этом диапазоне от 1 до 255.
All right, or from 0 to 255.|Хорошо, или от 0 до 255.
Now the next network we're gonna advertise Is the serial,|Теперь следующая сеть, которую мы собираемся рекламировать, - это сериал,
which is 10.1.1.4,|что 10.1.1.4,
0.0.0.3, so start at 30.|0.0.0.3, поэтому начните с 30.
Again, do your subtraction.|Снова сделайте вычитание.
AREA 0.|ПЛОЩАДЬ 0.
Must be in the same area.|Должен быть в том же районе.
Must be in the same area.|Должен быть в том же районе.
And then the last one,|А потом последний,
which is your loopback,|какая у вас петля,
you need to advertise that as well.|это тоже нужно рекламировать.
It is extremely important.|Это очень важно.
172.31.1.0.|172.31.1.0.
Using a 24, 0.0.0.255 AREA 0.|Используя 24, 0.0.0.255 AREA 0.
All right and that's it, you're done.|Хорошо, и все, готово.
There's, there's nothing else to that.|В этом нет ничего другого.
I'm gonna do a DO WR.|Я сделаю DO WR.
You would exit all the way out to privilege mode and do a Copy > Run > Start.|Вы должны полностью выйти в режим привилегий и выполнить Копировать> Выполнить> Пуск.
Enter, Enter.|Enter, Enter.
Now, if you forget to advertise a network,|Теперь, если вы забыли прорекламировать сеть,
OSPF is finicky, big time.|OSPF привередлив, большое время.
It will take its sweet time before it decides that,|Пройдет время, прежде чем он решит,
hey I'm gonna go ahead and I'll start to say, okay, you put in a new network.|эй, я пойду вперед и начну говорить, хорошо, ты подключил новую сеть.
I'm gonna start recalculating,|Начну пересчитывать,
I'm gonna start saying, hey,|Я собираюсь сказать, эй,
there's a new network involved, and it's gotta send to its neighbor,|задействована новая сеть, и она должна послать своему соседу,
because it has to create the neighbor relationship.|потому что он должен создать отношения соседа.
And while we're on the subject,|И пока мы говорим об этом,
let me show you.|позволь мне показать тебе.
In order, it has to go through this process right here,|Для этого он должен пройти этот процесс прямо здесь,
Do you need to know the states?|Вам нужно знать штаты?
More or less.|Более или менее.
They're not gonna ask you questions about the state, but I want to understand them because we're gonna look at it once we do|Они не будут задавать вам вопросы о состоянии, но я хочу их понять, потому что мы рассмотрим это, как только мы это сделаем.
the multi-access, okay, even here,|мультидоступ, ладно, даже здесь,
when we start looking at the information.|когда мы начинаем смотреть на информацию.
One router,|Один роутер,
let's say here we got three routers.|допустим, у нас есть три роутера.
We're now gonna connect router 1 and router 2.|Теперь мы подключим маршрутизатор 1 и маршрутизатор 2.
Router 1 and router 2 start sending information to each other.|Маршрутизатор 1 и маршрутизатор 2 начинают отправлять информацию друг другу.
When they start to send information,|Когда они начинают посылать информацию,
they're considered in a down state, okay?|они считаются в неработающем состоянии, хорошо?
Once they receive the information, now they change from down to initialization,|Как только они получат информацию, теперь они переходят от состояния к инициализации,
they start looking at things.|они начинают смотреть на вещи.
When they reply to each other, meaning hey, I got information from you, okay?|Когда они отвечают друг другу, имея в виду, что я получил информацию от вас, хорошо?
I got information from you, so now we're gonna have a two-way state,|Я получил информацию от вас, так что теперь у нас будет двустороннее состояние,
that we may start sharing information.|что мы можем начать делиться информацией.
And what happens, the routers begin to exchange their link state database,|И что происходит, маршрутизаторы начинают обмениваться своей базой данных состояний каналов,
their link state database.|их база данных состояний ссылок.
I forgot what this abbreviation, it's the same as this, it's just DBD, database,|Я забыл, что это за аббревиатура, она такая же, просто DBD, база данных,
whatever, I forgot what it stands for.|что бы там ни было, я забыл, что это означает.
Link state database,|База данных состояний ссылок,
that's when they go to exchange start.|вот когда они идут, чтобы начать обмен.
Now they start exchanging information.|Теперь они начинают обмениваться информацией.
It's like the Cliff Notes of what they have and what you have.|Это как в Cliff Notes, что у них есть и что есть у вас.
You know, one goes first,|Знаешь, один идет первым,
then the other one sends, all right?|тогда другой отправляет, хорошо?
When the databases are acknowledged,|Когда базы данных подтверждены,
now they're in the loading state.|теперь они в состоянии загрузки.
And then, they say, hey, wait a minute,|А потом они говорят, эй, погоди,
router 1, I received information from you.|роутер 1, я получил от вас информацию.
I got this database information,|Я получил эту информацию из базы данных,
but I don't have this network.|но у меня нет этой сети.
I don't know about this network, and that's where it sends the link state request.|Я не знаю об этой сети, и именно туда она отправляет запрос состояния ссылки.
Says hey,|Говорит привет,
I need to you to send me an update about that network because I don't know about it.|Мне нужно, чтобы вы прислали мне обновленную информацию об этой сети, потому что я не знаю об этом.
So one of the routers again they take their turns.|Итак, один из маршрутизаторов снова по очереди.
They take their turn.|Они по очереди.
They'll say, okay, router 2 says to router 1, hey listen, I got your database.|Они скажут, хорошо, маршрутизатор 2 говорит маршрутизатору 1, послушайте, я получил вашу базу данных.
I've, I, I know about these networks,|Я, я, я знаю об этих сетях,
and I know about that one.|и я знаю об этом.
So can you please send me an update?|Не могли бы вы прислать мне обновленную информацию?
He sends them a link state request to send him an update about that,|Он отправляет им запрос состояния ссылки, чтобы сообщить ему об этом,
that network that he didn't know about.|та сеть, о которой он не знал.
And router 1 says why,|И маршрутизатор 1 говорит, почему,
of course, my pleasure.|конечно, с удовольствием.
And then router 1 does the same thing.|Затем маршрутизатор 1 делает то же самое.
Router 1 says hey, wait a minute, you send me something that I don't know about.|Маршрутизатор 1 говорит: «Эй, подождите, вы отправили мне что-то, о чем я не знаю».
Can you please send, sends him a request to send him a link state update.|Не могли бы вы отправить, отправляет ему запрос на отправку ему обновления состояния ссылки.
So they're going back and forth during the loading state.|Итак, они ходят туда-сюда во время загрузки.
That's when you start creating the neighbors, you see full loading done.|Вот когда вы начинаете создавать соседей, вы видите полную загрузку.
When full loading done, bam!|Когда полная загрузка завершена, бац!
We're in a full state.|Мы в полном состоянии.
We've changed information.|Мы изменили информацию.
We now know about each other's networks.|Теперь мы знаем о сетях друг друга.
We're fully, we know everything.|Мы полностью, мы все знаем.
At that time.|В это время.
Is when shortest path first starts calculating.|Когда начинается вычисление кратчайшего пути.
Why?|Зачем?
Because that's,|Потому что это,
now that I know about all the networks,|теперь, когда я знаю обо всех сетях,
now the topology table gets created.|теперь создается таблица топологии.
That's where the shortest path starts getting its calculations from.|Отсюда и начинается расчет кратчайшего пути.
So you can see that there's a lot of work,|Итак, вы видите, что работы много,
especially if it's a huge network.|особенно если это огромная сеть.
It's got to go though this process right here.|Это должно пройти через этот процесс прямо здесь.
And right in here, listen, if you're not in the same autonomous system, and if you don't have the same hellos, you're not|И прямо здесь, слушайте, если вы не в той же автономной системе, и если у вас нет таких же приветствий, вы не
going to get past this state right here.|собираюсь пройти это состояние прямо здесь.
You'll never make it to 2way.|Вы никогда не доберетесь до 2way.
Do you have the same autonomous system number that I do?|У вас такой же номер автономной системы, как у меня?
Let me see.|Дайте-ка подумать.
Do you have the same subnet mask that I do?|У вас такая же маска подсети, что и у меня?
Do you have the same hellos that I do?|У вас такие же приветы, как у меня?
We're not using security, so I'm not gonna worry about that.|Мы не используем охрану, поэтому я не буду об этом беспокоиться.
But it does worry about the other three.|Но это действительно беспокоит остальных трех.
And if it doesn't pass this, you won't make it past the initialization state.|И если это не пройдет, вы не сможете пройти дальше состояния инициализации.
That's all I'm trying to say.|Это все, что я пытаюсь сказать.
So when you're looking,|Итак, когда вы смотрите,
you're doing these show commands.|вы выполняете эти команды шоу.
And you,|А ты,
you will be doing show IP OSPF topology.|вы будете показывать топологию IP OSPF.
Oh, I'm sorry, show IP OSPF interface whatever interface that we're gonna look at.|Ой, извините, покажите интерфейс IP OSPF, какой бы интерфейс мы ни рассматривали.
You're gonna see, especially in the multi-access network, you're gonna see if it's in the two-way state, is it in a full state, or is it in a drother state.|Вы увидите, особенно в сети с множественным доступом, вы увидите, находится ли она в двустороннем состоянии, в полном состоянии или в другом состоянии.
And you need to understand what the heck that means, okay?|И вам нужно понять, что это значит, ладно?
So, but this is the process.|Итак, но это процесс.
How just two routers are becoming neighbors.|Как сразу два роутера становятся соседями.
So now imagine if you have 50 routers in one area and each one of those routers are connected to each other, they need to become neighbors.|Итак, теперь представьте, что если у вас есть 50 маршрутизаторов в одной области и каждый из этих маршрутизаторов подключен друг к другу, они должны стать соседями.
All this information is being sent back and forth and then the calculation begins.|Вся эта информация пересылается туда и обратно, а затем начинается расчет.
And then people can start sending information.|И тогда люди могут начать присылать информацию.
So, I mean,|Итак, я имею в виду,
obviously it's transparent to the user.|очевидно, это прозрачно для пользователя.
And you, all you see is full loading,|А ты, все, что видишь, это полная загрузка,
now you're like, yes, it's working.|теперь ты такой, да, он работает.
But then when you start doing your show commands, you need to understand, hey,|Но затем, когда вы начнете выполнять свои команды show, вам нужно понять, эй,
this stopped here,|это остановилось здесь,
this stopped here, what's going on.|это остановилось здесь, что происходит.
So, you need to understand those.|Итак, вам нужно это понять.
But just wanted to show you that because that is important.|Но просто хотел показать вам это, потому что это важно.
So we did our OSPF for router 1, perfect.|Итак, мы сделали наш OSPF для маршрутизатора 1, идеально.
Obviously we're not gonna get an update from anybody else,|Очевидно, мы не получим обновлений ни от кого,
because there is no other OSPF on the network.|потому что в сети нет другого OSPF.
So let's go ahead and open up router 2.|Итак, давайте продолжим и откроем маршрутизатор 2.
Now with router 2, what I'm gonna do is,|Теперь с маршрутизатором 2 я собираюсь сделать следующее:
I'm gonna do this side.|Я сделаю эту сторону.
I'm gonna go this way when I'm doing the second router cuz I don't wanna get interrupted.|Я пойду этим путем, когда буду делать второй роутер, потому что не хочу, чтобы меня отвлекали.
Cuz if not, I will.|Если нет, то сделаю.
All right, and I believe we also have loopbacks on this one, show [SOUND] IP INT BRIEF.|Хорошо, и я считаю, что у нас также есть петли на этом, покажите [ЗВУК] IP INT BRIEF.
And we do, and it's a 24,|И мы делаем, и это 24,
so we gonna go CONFIG T.|Итак, мы перейдем к CONFIG T.
Router, let me open it up a little bit more.|Маршрутизатор, позвольте мне открыть его еще немного.
Okay?|Ладно?
ROUTER OSPF 1, again.|МАРШРУТИЗАТОР OSPF 1, снова.
Doesn't really matter, it's local.|Неважно, это местное.
NETWORK, we're gonna use the one going that way, which is the 10.1.1.8.|NETWORK, мы будем использовать тот, который идет по этому пути, а именно 10.1.1.8.
And it's a 30, 0.0.0.3, and we're using AREA 0, same area.|И это 30, 0.0.0.3, и мы используем ОБЛАСТЬ 0, ту же область.
NETWORK 192.168.2.0|СЕТЬ 192.168.2.0
0.0.0.255, oops.|0.0.0.255, упс.
AREA 0, there you go.|AREA 0, вот и все.
NETWORK 172.31.1, oop, .2.0.|СЕТЬ 172.31.1, уп, .2.0.
And we're using a also a 24 mask, AREA 0.|И мы также используем маску 24, AREA 0.
And now, let's do the serial to the left,|А теперь займемся сериалом слева,
which is,|который,
I'm just gonna up arrow through here.|Я просто пойду сюда стрелкой вверх.
And I'm just gonna put 4, okay.|И я просто поставлю 4, хорошо.
I'll do a DO WR, all right?|Я сделаю DO WR, хорошо?
We should be getting OSPF again.|Мы должны снова получить OSPF.
It's not as fast EIGRP, but we should start getting, you see there,|Это не такой быстрый EIGRP, но мы должны начать получать, видите ли,
it says FULL, Loading Done.|он говорит ПОЛНАЯ, загрузка завершена.
See that, FULL, Loading.|Смотрите, ПОЛНЫЙ, Загрузка.
That's the meant, it already exchanged,|Это значит, он уже обменялся,
it links the database.|он связывает базу данных.
Every knows about the networks.|Все знают о сетях.
So it created that neighbor relationship,|Таким образом, это создало отношения соседства,
all right.|отлично.
Let's do the last router.|Сделаем последний роутер.
I will do the LAN, the the loop back address, and then I'll do the WAN.|Я сделаю LAN, обратный адрес, а затем WAN.
It's just funny that I say WAN when we're not using any WAN protocols.|Просто забавно, что я говорю WAN, когда мы не используем никаких протоколов WAN.
But in actually we are, when I can, cuz this HDLC is considered a WAN protocol.|Но на самом деле это так, когда я могу, потому что этот HDLC считается протоколом WAN.
When anytime you see a,|Когда в любое время вы видите,
a line like this, you consider that to,|такую ​​строку вы считаете,
you consider it, right,|ты считаешь это, правда,
in a drawing, let's say.|в чертеже, скажем так.
That's a WAN.|Это WAN.
Let's do a show PROTOCOLS,|Сделаем шоу ПРОТОКОЛЫ,
let's use that command.|давайте воспользуемся этой командой.
All right, so you can see the,|Хорошо, так что вы можете видеть,
there you go.|вот так.
All right, so CONFIG T.|Хорошо, так что CONFIG T.
ROUTER OSPF 1.|МАРШРУТИЗАТОР OSPF 1.
Let's open it up more.|Давайте раскроем его подробнее.
NETWORK.|СЕТЬ.
Let us use this for the LAN.|Давайте использовать это для LAN.
192.168.3.0000.255 area 0,|192.168.3.0000.255 область 0,
let's put the loop back,|давайте вернем петлю,
Network 172.31.3.0 000.255 area 0.|Сеть 172.31.3.0 000.255 область 0.
And then the WAN,|А потом WAN,
network 10.1.1.8 which is the 30.|сеть 10.1.1.8, которая является 30.
AREA 0. Okay? And there we are.|ОБЛАСТЬ 0. Хорошо? И вот мы здесь.
Let's wait for it to do the full loading.|Подождем, пока он загрузится полностью.
All right.|Отлично.
That's one of the things you say hey,|Это одна из вещей, которые вы говорите, эй,
I am getting updates.|Я получаю обновления.
That's a good thing.|Это хорошая вещь.
Boom.|Бум.
Awesome.|Потрясающие.
I'm gonna do a Ctrl+Z, and right from router, the last router,|Я сделаю Ctrl + Z, и прямо с маршрутизатора, последнего маршрутизатора,
I'm gonna do a show IP route.|Я собираюсь показать IP-маршрут.
Awesome.|Потрясающие.
I see Os.|Я вижу Ос.
I see Os.|Я вижу Ос.
All right, which is good.|Хорошо, и это хорошо.
You see that this is not the same LAN, we don't have the gateway of last resort, or anything like that.|Вы видите, что это не та же LAN, у нас нет шлюза последней инстанции или чего-то подобного.
There is no other routing protocol on here but OSPF.|Здесь нет другого протокола маршрутизации, кроме OSPF.
We are learning about the 10.1.1.4 network from OSPF.|Мы узнаем о сети 10.1.1.4 от OSPF.
We know that it's OSPF,|Мы знаем, что это OSPF,
not only because you see an O there, but we have an administrative distance of 110.|не только потому, что вы видите там букву O, а у нас административное расстояние 110.
This number right next to that,|Этот номер рядом с этим,
that is the cost.|это стоимость.
That is the cost that the shortest path first algorithm actually calculated.|Это стоимость, которую фактически рассчитал алгоритм поиска кратчайшего пути.
You're learning it via the 10.1.1.9,|Вы изучаете его через 10.1.1.9,
and on your, zero, one, zero.|и по вашему, ноль, один, ноль.
That's how you read that.|Вот как вы это читаете.
The same thing for the rest.|То же самое и в остальном.
There are your loopbacks right here,|Вот ваши петли прямо здесь,
that you're learning.|что вы изучаете.
The one, the two, okay.|Один, два, хорошо.
You are connected directly to the three,|Вы напрямую связаны с тремя,
and you're learning about the LANs right here,|и вы узнаете о локальных сетях прямо здесь,
and you're connected about the three.|и вы связаны насчет трех.
And each one you see has a different cause of who you're connected to.|И у каждого из них есть своя причина того, с кем вы связаны.
But, and that's great, you need to learn how to read the routing table,|Но, и это здорово, вам нужно научиться читать таблицу маршрутизации,
and who's updating you, and what their admin is, and the cost and all that.|и кто вас обновляет, и каков их администратор, и стоимость и все такое.
And where it's coming from,|И откуда это,
what interface and all.|какой интерфейс и все.
But with OSPF,|Но с OSPF
one of the things that you wanna look at,|одна из вещей, на которую вы хотите посмотреть,
one of the print screens that you need to be looking at, is show IP OSPF,|один из экранов печати, на который вы должны смотреть, - это показать IP OSPF,
interface, I wanna look at the serial interface, S zero slash one slash zero.|интерфейс, я хочу посмотреть на последовательный интерфейс, S ноль косая черта одна косая черта ноль.
I'm gonna hit enter.|Я нажму Enter.
I'll bring that up.|Я подниму это.
Let's take a look at our key things here.|Давайте посмотрим на наши ключевые моменты здесь.
Great, hey, our serial one is up, up.|Отлично, эй, наш серийный номер готов.
We know that.|Мы знаем это.
We know that our address is ten one one ten.|Мы знаем, что наш адрес десять один один десять.
The process ID number is one.|Идентификационный номер процесса - один.
But the router ID,|Но идентификатор роутера,
which is the router's number, okay,|это номер роутера, ладно,
it shows the loop back address.|он показывает обратный адрес петли.
Now, I'm supposed to explain this in,|Теперь я должен объяснить это,
in multi-access, but I'm gonna explain it now.|в мультидоступе, но сейчас я объясню это.
Because it shows the highest loop back address, for it to be the router ID.|Потому что он показывает наивысший адрес обратной связи, чтобы быть идентификатором маршрутизатора.
If that loop back address wouldn't be there,|Если этого обратного адреса не было бы,
it would have chosen the 192 168 3 dot network.|он выбрал бы сеть 192 168 3 точки.
Cause that would be the highest IP address.|Причина в том, что это будет наивысший IP-адрес.
That's one of the things that it does.|Это одна из вещей, которые он делает.
All right, but it shows the loop back because the loop back was configured.|Хорошо, но он показывает обратный цикл, потому что он был настроен.
One of the things that you need to pay attention to is the network type,|Одна из вещей, на которую нужно обратить внимание, - это тип сети,
it is a point-to-point.|это точка-точка.
All right?|Отлично?
It gives you the cost value.|Это дает вам стоимость.
The importance is that it is a point-to-point,|Важно то, что это точка-точка,
the type of it is a point-to-point.|Тип этого - точка-точка.
The priority is zero.|Приоритет равен нулю.
If there's a zero priority that means there is no election.|Если есть нулевой приоритет, это означает, что выборов нет.
Therefore, you will have no designated router, no backup designated router, okay?|Следовательно, у вас не будет ни назначенного маршрутизатора, ни резервного назначенного маршрутизатора, хорошо?
And there you see your hellos,|И вот вы видите свои приветы,
your default values, all right,|ваши значения по умолчанию, хорошо,
they all must be the same in order for them to become, become neighbors.|все они должны быть одинаковыми, чтобы стать соседями.
But things you need to look at.|Но на вещи нужно смотреть.
The router ID, the network type,|Идентификатор маршрутизатора, тип сети,
the priority,|приоритет,
that if you have backup or designated routers and your hello indent.|что, если у вас есть резервные или назначенные маршрутизаторы и приветственный отступ.
This is where your focus needs to be.|Это то, на чем вы должны сосредоточиться.
When you're taking your examination,|Когда ты сдаешь экзамен,
all right.|отлично.
But you can see on a point-to-point that there is no election.|Но вы можете сразу увидеть, что выборов нет.
And like I said,|И, как я уже сказал,
that's a full loaded question.|это полностью загруженный вопрос.
And I'm not trying to confuse you,|И я не пытаюсь запутать тебя,
I'm trying to make you think.|Я пытаюсь заставить тебя задуматься.
Let's take a look at the LAN interface.|Давайте посмотрим на интерфейс LAN.
The F zero zero.|F ноль ноль.
Show IP OSPF Interface F0/0.|Показать интерфейс IP OSPF F0 / 0.
Same router ID, right,|Тот же идентификатор роутера, верно,
different address, obviously.|другой адрес, очевидно.
But, now the type of network is broadcast.|Но теперь тип сети - широковещательный.
So now we have a cost of one,|Итак, теперь у нас есть стоимость одного,
therefore, we're now a priority of one,|Таким образом, мы теперь приоритетом один,
now we have a designated router which is the router ID.|теперь у нас есть назначенный маршрутизатор, который является идентификатором маршрутизатора.
So it actually created an election.|Так что это фактически привело к выборам.
It created an election.|Это привело к выборам.
The D\designated router ID is 172.31.3.1 because it's the loop back.|Идентификатор маршрутизатора, назначенный D \, - 172.31.3.1, потому что это обратный цикл.
But there is no backup designator router,|Но нет резервного маршрутизатора с указателем,
because there's nothing else that it's talking to.|потому что больше не с чем он разговаривает.
So he thinks he's the only designated router on that particular broadcast domain.|Поэтому он думает, что он единственный назначенный маршрутизатор в этом конкретном широковещательном домене.
But you're saying Laz you well that makes sense Laz because it's not a point-to-point network then that's going to happen because it's a broadcast like|Но вы хорошо говорите Laz, что имеет смысл Laz, потому что это не сеть точка-точка, тогда это произойдет, потому что это широковещательная передача, например
you said previously.|вы сказали ранее.
And you would be right.|И ты был бы прав.
But let me show you something else, and it will be the same throughout each route.|Но позвольте мне показать вам кое-что еще, и оно будет одинаковым на каждом маршруте.
Will be the same throughout each router and I'll show you.|Будет одинаково для всех маршрутизаторов, и я вам покажу.
Let's look at the middle router.|Посмотрим на средний роутер.
Let's open that up.|Давайте откроем это.
Let's do first show IP Route.|Давайте сначала покажем IP Route.
That we are routing correctly,|Что мы правильно проложим маршрут,
we have all the different routes that we need to know about right there.|у нас есть все разные маршруты, о которых нам нужно знать прямо здесь.
We're gonna do a show IP OSPF, S0/0/0,|Мы собираемся сделать шоу IP OSPF, S0 / 0/0,
I believe we're using S0/0/0, yeah.|Я считаю, что мы используем S0 / 0/0, да.
Okay, might as well full-screen it, okay.|Ладно, можно было бы развернуть его на весь экран, ладно.
Oops.|Ой.
Show IP OSPF.|Покажи IP OSPF.
Oh, Show IP OSPF interface S zero slash zero slash zero.|О, Показать интерфейс IP OSPF S нулевая косая черта ноль косая черта ноль.
All right.|Отлично.
Point-to-point, now we're type point-to-point.|Точка-точка, теперь мы набираем точка-точка.
Zero priority.|Нулевой приоритет.
All right?|Отлично?
And no designated router, no backup.|И ни назначенного маршрутизатора, ни резервного копирования.
Again the loop back is the Router ID,|И снова петля - это идентификатор маршрутизатора,
the name of the router,|название роутера,
how you identify the router,|как вы идентифицируете роутер,
and the hellos are the same.|и привет такие же.
They work to do the same thing for the S1,|Они работают, чтобы сделать то же самое для S1,
I believe that's the interface that we're using.|Я считаю, что это тот интерфейс, который мы используем.
Now SH says again, Priority zero.|Теперь SH снова говорит: приоритет нулевой.
All right, that means that there's no designated router, no back up, and those are the same.|Хорошо, это означает, что нет назначенного маршрутизатора, нет резервной копии, и это то же самое.
But, if we do the LAN, F0/0,|Но, если мы делаем LAN, F0 / 0,
now things change again.|теперь все снова меняется.
From broadcast environment we have a priority of one,|Из среды вещания у нас есть приоритет один,
then we have a designated router.|тогда у нас есть назначенный маршрутизатор.
And he thinks he is the only,|И он думает, что он единственный,
well he is really, that interface,|ну он действительно, этот интерфейс,
the only designated router within that broadcasted lane.|единственный назначенный маршрутизатор в пределах этой полосы вещания.
So again, you see the differences between point-to-point, and broadcast.|Итак, вы снова видите разницу между двухточечной и широковещательной передачей.
But let me show you a little lab,|Но позвольте мне показать вам небольшую лабораторию,
a comparison lab.|лаборатория сравнения.
[BLANK AUDIO].|[ПУСТОЙ АУДИО].
These are point-to-point.|Это точка-точка.
These are point-to-point connections.|Это соединения точка-точка.
And, I will come down here.|И я приду сюда.
I believe I already did OSPF, yes,|Я считаю, что уже сделал OSPF, да,
there's your full loading done.|вот ваша полная загрузка сделана.
All right lets maximize this.|Хорошо, давайте максимизируем это.
Enable.|Включить.
Show IP Route.|Показать IP-маршрут.
We're connected directly to it but if we do a show IPOSPF and what interface are we using?|Мы подключены напрямую к нему, но если мы проводим шоу IPOSPF, и какой интерфейс мы используем?
S triple zero,|S тройной ноль,
Show IPOSPF interface S0/0/0.|Показать интерфейс IPOSPF S0 / 0/0.
[SOUND] Oh, hey, still holds true right?|[ЗВУК] Эй, все еще верно?
Point-to-point, zero priority,|Точка-точка, нулевой приоритет,
no designated router,|нет назначенного маршрутизатора,
no backup designated router.|нет резервного назначенного маршрутизатора.
All those are the same.|Все они одинаковы.
All those will never change unless you actually go into the interface.|Все это никогда не изменится, если вы не войдете в интерфейс.
And do a IP OSPF hello, and then change the hello timer.|И сделайте приветствие IP OSPF, а затем измените таймер приветствия.
You're not gonna mess with timers, you just gotta make sure they're all the same.|Вы не будете связываться с таймерами, просто убедитесь, что они все одинаковые.
All right.|Отлично.
But it's a serial interface,|Но это последовательный интерфейс,
it's a serial interface.|это последовательный интерфейс.
What happens in,|Что происходит в
if we do a point to point with ethernet?|если мы сделаем точку-точку с Ethernet?
Let's bring that up.|Давайте поднимем это.
[COUGH] Excuse me.|[Кашляет] Извините.
Show IP OSPF interface F0/0.|Показать интерфейс IP OSPF F0 / 0.
Look how interesting.|Посмотри как интересно.
We have a designated router and a backup designated router.|У нас есть назначенный маршрутизатор и резервный назначенный маршрутизатор.
We have our priority of one,|У нас есть приоритет один,
network type is broadcast.|тип сети - широковещательный.
So what does that tell you?|Так что это вам говорит?
That tells you that if you're in an ethernet network,|Это говорит вам, что если вы находитесь в сети Ethernet,
you will have broadcast,|у вас будет трансляция,
you will have IPV4 obviously,|очевидно, у вас будет IPV4,
broadcast, and you will have elections being run, right?|транслируют, и у вас будут выборы, верно?
Because their priority, the only priority that's the zero priority,|Поскольку их приоритет, единственный приоритет, это нулевой приоритет,
that's the only one that doesn't run the election.|это единственный, кто не участвует в выборах.
Anything else will run the election.|Все остальное будет управлять выборами.
So he has a priority of one,|Значит, у него приоритет один,
there's your designated router,|вот ваш назначенный маршрутизатор,
there's your backup designated router.|вот ваш резервный назначенный маршрутизатор.
You can see the hellos are still the same.|Вы можете видеть, что приветствия остались прежними.
But it ran an election.|Но прошли выборы.
Let's take a look at the other router,|Давайте посмотрим на другой роутер,
see what he says.|посмотрите, что он говорит.
Let's minimize this,|Давайте минимизировать это,
let's go to the next router.|перейдем к следующему роутеру.
Maximize it.|Максимизируйте это.
Go to the CLI.|Зайдите в CLI.
Enable.|Включить.
Show IP OSPF INT F0/0.|Показать IP OSPF INT F0 / 0.
So we have a designated router six.|Итак, у нас есть назначенный роутер шесть.
And now, and the backup is generator five.|А теперь и резервный генератор пятый.
So it's using the highest IP address as the designated router, and the lowest IP address, or the second highest IP address if you|Таким образом, он использует самый высокий IP-адрес в качестве назначенного маршрутизатора и самый низкий IP-адрес или второй по величине IP-адрес, если вы
would, as a backup designated router.|будет в качестве резервного маршрутизатора.
So it's not just that it's point to point,|Так что дело не только в том, чтобы указать,
it's the fact that it's a point to point serial connection.|Дело в том, что это последовательное соединение точка-точка.
If it would be a point to point like this one is that is ethernet,|Если бы это было похоже на то, что это Ethernet,
then you do run, an election,|тогда вы бежите, выборы,
because ethernet has broadcast.|потому что Ethernet транслирует.
Point to point.|Точка-точка.
But now we have an ethernet cable.|Но теперь у нас есть кабель Ethernet.
No longer is it a serial cable.|Это больше не последовательный кабель.
So now we run an election at that point.|Итак, сейчас мы проводим выборы на этом этапе.
How interesting.|Как интересно.
So, food for thought.|Итак, пища для размышлений.
Will you get this?|Вы получите это?
No.|Нет.
They're not going to be like that on the test, but this is something for you to be aware of.|Они не будут такими на тесте, но вам стоит знать об этом.
When you get out there, or if you already are out there, they say hey, okay, so now I know why this is going on on my network.|Когда вы выходите, или если вы уже там, они говорят: «Эй, хорошо, теперь я знаю, почему это происходит в моей сети».
Because controlling the DR and the BDR is extremely important.|Потому что контроль DR и BDR чрезвычайно важен.
And I mean I don't wanna get too whatever,|И я имею в виду, что я не хочу слишком ничего,
but if you're introducing external routes into a multi-access or not multi-access,|но если вы вводите внешние маршруты в множественный доступ или без множественного доступа,
I'm sorry, multiple area OSPF, that could be an issue with your DR and BDR.|Извините, OSPF с несколькими областями, это может быть проблема с вашим DR и BDR.
All right, so now you know.|Хорошо, теперь ты знаешь.
It's not just that it's point to point,|Дело не только в том, что это точка в точку,
it's the fact that it's point to point with a serial.|Дело в том, что это точка-точка с серийным номером.
And that's how you'll see it on your test.|И вот как вы это увидите на своем тесте.
That's how you'll see it, more likely.|Скорее всего, так вы это увидите.
They're not gonna be this tricky,|Они не собираются быть такими сложными,
maybe in the next version of the test,|может быть в следующей версии теста,
if one ever, ever exists,|если он когда-либо существует,
I'm sure it will.|Я уверен, что так и будет.
They'll do something like this, maybe.|Может быть, они сделают что-то подобное.
All right, so keep an eye out on that.|Хорошо, так что следи за этим.
Do your own labs.|Сделайте свои собственные лаборатории.
Try this lab, okay, and see, and create your OSPF.|Попробуйте эту лабораторную работу, хорошо, и посмотрите, и создайте свой OSPF.
Because you have ethernet,|Поскольку у вас есть Ethernet,
you have that different priority.|у вас другой приоритет.
Now remember, you can control a priority.|Теперь помните, вы можете контролировать приоритет.
I can go in here and change this priority to a zero, change that priority to a zero.|Я могу войти сюда и изменить этот приоритет на ноль, изменить этот приоритет на ноль.
And there will be no election.|И выборов не будет.
They will not participate in any election.|Они не будут участвовать ни в каких выборах.
So I can control that,|Так что я могу это контролировать,
by changing the priority number to zero.|изменив номер приоритета на ноль.
So, if this is what you want,|Итак, если это то, что вы хотите,
you can do it, but you have to change the priority number to zero.|вы можете это сделать, но вы должны изменить номер приоритета на ноль.
Just wanted to give you that food for thought.|Просто хотел дать вам пищу для размышлений.
So this is point to point OSPF.|Итак, это точка-точка OSPF.
That's all you really need to know.|Это все, что вам действительно нужно знать.
The configuration of OSPF is pretty straightforward.|Конфигурация OSPF довольно проста.
You go route OSPF, the process ID number,|Вы идете по маршруту OSPF, ID процесса,
you got from one to 65,135,|вы получили от одного до 65 135,
you do your network statement,|вы делаете заявление в сети,
the exact network that it connected to,|точная сеть, к которой он подключен,
with a wildcard mask, and the area.|с подстановочной маской и областью.
And you must advertise also your loop back, if you have any.|И вы должны также рекламировать свой шлейф, если он у вас есть.
You must advertise it in OSPF at that time.|Вы должны рекламировать это в OSPF в то время.
If you do it later, OSPF is gonna take its sweet time to put it in there.|Если вы сделаете это позже, OSPF найдет время, чтобы вставить его туда.
So make sure you put everything in there in the same area.|Поэтому убедитесь, что вы поместили все в одну и ту же область.
Make sure your wildcard masks are correct.|Убедитесь, что маски подстановки правильные.
Remember, you can use that constant 255s all the way across on top.|Помните, что вы можете использовать константу 255 сверху вниз.
And just put your subnet mask on the bottom and subtract.|И просто поместите свою маску подсети внизу и вычтите.
And that's the way you get your subnet mask.|Таким образом вы получаете маску подсети.
So as you can see,|Как видите,
OSPF is not something difficult.|OSPF - это не что-то сложное.
It's understanding when you're you're looking at the show commands,|Это понимание, когда вы смотрите на команды show,
what it is that you're looking at.|на что вы смотрите.
I'll see you guys in the next session.|Увидимся на следующем сеансе.