D:\mailCloud\prjother\tmp\1\c67_How does IP routing occur.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
Welcome back, everybody.|С возвращением, все.
All right, it's time.|Хорошо, пора.
It's time to start learning about the IP routing process.|Пришло время начать изучение процесса IP-маршрутизации.
We need to understand how we get from,|Нам нужно понять, как мы получаем,
from this PC to this PC, or from this PC to this PC.|с этого ПК на этот ПК или с этого ПК на этот ПК.
It really doesn't matter if it's two PC's or 2,000 PC's,|На самом деле не имеет значения, два это ПК или 2000 ПК,
the process is still the same.|процесс все тот же.
Obviously what makes the difference is the media that the information is being carried on.|Очевидно, что отличает СМИ, в которых передается информация.
Right?|Правильно?
If it's an ethernet media.|Если это носитель Ethernet.
If it's a serial media.|Если это серийный носитель.
If it's wireless media.|Если это беспроводной носитель.
But again, don't, don't burden your brain with all this.|Но опять же, не надо, не перегружайте свой мозг всем этим.
Remember, we're taking this.|Помните, мы берем это.
We're doing this for a CCNA certification.|Мы делаем это для сертификации CCNA.
So what we're about to explain, what I'm about to explain is the routing process.|Итак, что мы собираемся объяснить, то, что я собираюсь объяснить, - это процесс маршрутизации.
Which is the routing process, regardless of whether you do it on live routers or the Packet Tracer or wherever do it.|Каков процесс маршрутизации, независимо от того, выполняете ли вы его на активных маршрутизаторах, на Packet Tracer или где-то еще.
Routing is routing.|Маршрутизация - это маршрутизация.
Okay, and the process still remains the same.|Хорошо, и процесс остается прежним.
Okay, so what happens?|Итак, что происходит?
PC0 wants to ping PC1.|PC0 хочет проверить связь с PC1.
So the first thing PC0 has to do is say,|Итак, первое, что должен сделать PC0, это сказать:
hey,|Привет,
this packet is not part of my network.|этот пакет не является частью моей сети.
So I must then send it to the gateway, so it's gonna send it,|Поэтому я должен отправить его на шлюз, чтобы он отправил его,
if this is your first time, it's going to send an ARP request cuz it's ethernet and ethernet and IP version four, ARP still|если это ваш первый раз, он отправит запрос ARP, потому что это Ethernet и Ethernet, а также IP версии четыре, ARP все еще
exist.|существует.
So, it sends an ARP request to the default gateway meaning to to your F00.|Итак, он отправляет запрос ARP на шлюз по умолчанию, то есть на ваш F00.
The F00 gets that request and says, oh yes, this is me.|F00 получает этот запрос и говорит: о да, это я.
Here is my MAC address.|Вот мой MAC-адрес.
All right, so once he gets the MAC address,|Хорошо, так что как только он получит MAC-адрес,
it sends the information back down to complete that frame.|он отправляет информацию обратно, чтобы завершить этот кадр.
So now you have a source MAC address,|Итак, теперь у вас есть исходный MAC-адрес,
destination MAC address,|MAC-адрес назначения,
source IP address and destination IP address.|исходный IP-адрес и IP-адрес назначения.
Plus whatever port number ICMP is gonna be using, or whatever it is they're trying to get across.|Плюс к тому, какой номер порта будет использовать ICMP, или что бы там ни было, они пытаются передать.
And then it goes right back up to the router.|И затем он возвращается к маршрутизатору.
Once it gets up to the router, the router's gonna take a look.|Как только он подойдет к маршрутизатору, маршрутизатор осмотрит его.
First of all, the router's gonna take any Layer2 information and say [SOUND] throw it away.|Прежде всего, маршрутизатор возьмет любую информацию Layer2 и скажет [ЗВУК] выбросить.
Doesn't care.|Все равно.
It only cares about the network portion of the address and it's gonna say okay,|Он заботится только о сетевой части адреса, и он скажет: "Хорошо",
let me take a look at my routing table,|позвольте мне взглянуть на мою таблицу маршрутизации,
let me see where this destination network is going to.|позвольте мне увидеть, куда собирается эта сеть назначения.
Oh, yes, I see, you're going to the 2.0|О да, я вижу, вы собираетесь на 2.0
network.|сеть.
Okay, well the 2.0, according to my routing table,|Хорошо, ну, 2.0, согласно моей таблице маршрутизации,
I have to switch you over to that interface right there.|Я должен немедленно переключить вас на этот интерфейс.
And send you out to the next router.|И отправим вас к следующему роутеру.
So, there is no ARP in between here.|Итак, здесь нет никакого ARP.
So, the information gets sent to this middle router right over here.|Итак, информация отправляется на этот средний маршрутизатор прямо здесь.
The middle router sees that destination network.|Средний маршрутизатор видит эту сеть назначения.
Right?|Правильно?
Cuz in the packet, that's what it says,|Потому что в пакете, вот что написано,
hey, there's the destination network and this is where it came from, the source IP address.|эй, вот и сеть назначения, и вот откуда она пришла, исходный IP-адрес.
And this is where it wants to go to.|И это то, куда он хочет попасть.
Okay Layer3 information says oh, okay,|Хорошо, информация Layer3 говорит, что хорошо,
well, according to my routing table,|ну, согласно моей таблице маршрутизации,
I see that that 2.0 network or that 2.1|Я вижу, что та сеть 2.0 или та 2.1
address,|адрес,
it's in that, I gotta take you out at the F00.|это в том, я должен провести вас в F00.
So I'm gonna switch you over to the F00,|Итак, я переведу вас на F00,
to that doorway, if you will.|в этот дверной проем, если хотите.
And send you all that way.|И отправим вас туда.
But, I don't know the MAC address of the PC that that belongs to,|Но я не знаю MAC-адрес ПК, которому он принадлежит,
the end node that that belongs to.|конечный узел, которому он принадлежит.
So what do I need to do as a router?|Итак, что мне нужно делать маршрутизатору?
Or, I'm gonna go ahead and send an ARP request.|Или я отправлю ARP-запрос.
So I can go ahead and get, because now we're going back down to ethernet.|Так что я могу пойти дальше и начать, потому что теперь мы возвращаемся к Ethernet.
So we need that MAC address.|Итак, нам нужен этот MAC-адрес.
We have the source.|У нас есть источник.
The IP address where it came from, the source network,|IP-адрес, откуда он пришел, исходная сеть,
we know the destination network.|мы знаем сеть назначения.
We have our source MAC address which is our F00 on the router right there.|У нас есть исходный MAC-адрес, который является нашим F00 на маршрутизаторе прямо здесь.
But we need the destination MAC address or that particular end node that we're pinging so that ARP request needs to happen.|Но нам нужен MAC-адрес назначения или тот конкретный конечный узел, который мы проверяем, чтобы запрос ARP был выполнен.
So when that ARP request happens, it comes back up.|Поэтому, когда этот запрос ARP происходит, он возвращается.
Says, hey, that's me.|Говорит, эй, это я.
Completes a frame, then the information goes back down.|Завершает кадр, затем информация возвращается вниз.
Once that gets complete, then it goes right back up, and goes to the other side.|Как только это будет завершено, оно снова вернется наверх и перейдет на другую сторону.
Now your book, will explain it in extreme detail, all right?|Теперь ваша книга объяснит это очень подробно, хорошо?
I believe it's 26 or 36 steps, or something like that,|Я считаю, что это 26 или 36 шагов или что-то в этом роде,
which you should read.|которую вам следует прочитать.
You should read, but what you're gonna get on the test is questions about ARP.|Вам следует прочитать, но на тесте вы получите вопросы об ARP.
And what other type of questions that they're gonna ask you?|И какие еще вопросы они вам зададут?
Let's take this scenario, for example.|Возьмем, к примеру, такой сценарий.
Let's take these two routers so I don't have to move back and forth.|Давайте возьмем эти два роутера, чтобы мне не приходилось двигаться вперед и назад.
Let's take these two routers right here,|Возьмем эти два роутера прямо здесь,
with these two PCs right here.|с этими двумя ПК прямо здесь.
If I were to ask you a question.|Если бы я задала вам вопрос.
If PC1 was to ping PC2, what will be the destination Layer2 address?|Если ПК1 должен был проверить связь с ПК2, какой будет адрес назначения на уровне 2?
Well, the destination, if it's from PC1 to PC2,|Ну а пункт назначения, если он с ПК1 на ПК2,
the destination Layer2 address will be the gateway address of that particular router.|адрес уровня назначения Layer2 будет адресом шлюза этого конкретного маршрутизатора.
The F00 because Layer 2 or ARP stays within its own segment,|F00, потому что уровень 2 или ARP остается в своем собственном сегменте,
stays within its own segment.|остается в своем сегменте.
So, the source Layer2 address will be the PC.|Итак, адресом Layer2 источника будет ПК.
The destination Layer2 address will be the router's gateway.|Адрес назначения Layer2 будет шлюзом маршрутизатора.
The source IP address will be, or the source network,|Исходный IP-адрес или исходная сеть
lets say will be this network.|допустим будет эта сеть.
Or the source IP address would be the PC.|Или исходным IP-адресом будет ПК.
And the destination IP address is where it is you're pinging on this side.|И IP-адрес назначения - это то место, где вы пингуетесь с этой стороны.
So this is line of questioning that they're going to ask you when it comes to ARP.|Это вопрос, который они зададут вам, когда дело доходит до ARP.
They may show you, let's say a little figure,|Они могут показать вам, скажем, фигурку,
maybe with an envelope going that way or something like that.|может быть, с конвертом туда или что-то в этом роде.
Right, they'll say hey, there's a, and it's all ethernet.|Хорошо, они скажут: "Эй, вот и Ethernet".
It may not be serial.|Возможно, это не серийный номер.
If it's ethernet.|Если это Ethernet.
If it's ethernet, you have ARP, ARP, and ARP.|Если это Ethernet, у вас есть ARP, ARP и ARP.
Three ARP's.|Три ARP.
So we have three different frames being created.|Итак, у нас есть три разных фрейма.
So, if this, instead of being a serial media.|Итак, если это, а не серийный носитель.
It will be a twisted pair, or fiber.|Это будет витая пара или оптоволокно.
An ethernet.|Ethernet.
That means an ARP will have to go across,|Это означает, что ARP придется пройти,
will have to happen.|должно случиться.
So then they will tell you, well, if it's going from here to here, and it's ethernet, what will be your destination Layer2 address,|Тогда они скажут вам, ну, если он идет отсюда сюда, и это Ethernet, то какой будет ваш целевой адрес Layer2,
or destination MAC address, lets say?|или MAC-адрес назначения, скажем так?
It would be, that interface right there.|Было бы, вот этот интерфейс.
If its ethernet, and I keep saying that cuz I know I have a serial cable,|Если это Ethernet, и я все время говорю, потому что я знаю, что у меня есть последовательный кабель,
I'm saying this would be ethernet.|Я говорю, что это будет Ethernet.
Meaning you'll have a, cross over, UTP or whatever cable, ethernet.|Это означает, что у вас будет кроссовер, UTP или любой другой кабель Ethernet.
If this would be ethernet, all right, this would be the destination Layer2 address,|Если это будет Ethernet, хорошо, это будет адрес назначения Layer2,
this would be the source Layer2 hard drives.|это будут исходные жесткие диски Layer2.
So this is the kind of things you need to look out for in the test.|Вот на что вам нужно обратить внимание во время теста.
So the routing process is the same thing over and over and over again.|Таким образом, процесс маршрутизации повторяется снова и снова.
Once it knows, and you have your ARP cache, your computer has it if you do an ARP minus A, you know,|Как только он знает, и у вас есть кеш ARP, он будет у вашего компьютера, если вы выполните ARP минус A, вы знаете,
see your ARP cache, a router keeps an ARP cash in the RAM.|увидеть свой кэш ARP, маршрутизатор хранит кэш ARP в оперативной памяти.
So it already knows where it's been.|Значит, он уже знает, где он был.
The switch, has an ARP cache, everybody has an ARP cache.|Коммутатор имеет кеш ARP, у всех есть кеш ARP.
And it keeps it for a certain period of time.|И держит его в течение определенного периода времени.
As long as communication still occurs,|Пока происходит общение,
the ARP cache won't erase unless you erase it deliberately.|кэш ARP не будет удален, если вы не удалите его намеренно.
Now, even though it still has the ARP cache,|Теперь, несмотря на то, что у него все еще есть кеш ARP,
the process that at least will be one less.|процесс, который будет по крайней мере на один меньше.
There will be no ARP.|ARP не будет.
But, it's still got to look at it's routing table.|Но все равно нужно посмотреть на таблицу маршрутизации.
When the packet reaches that router, or the frame I should say,|Когда пакет достигает этого маршрутизатора или кадра, я бы сказал:
reaches that router.|достигает этого маршрутизатора.
That the router discards the Layer2|Маршрутизатор отбрасывает Layer2
address.|адрес.
Okay, because there is no ARP.|Ладно, потому что нет ARP.
It already knows, so no ARP happens.|Он уже знает, поэтому ARP не происходит.
So it goes to the router, the router, all it cares about is saying,|Итак, он переходит к маршрутизатору, маршрутизатору, все, о чем он заботится, говорит:
hey, you're coming from this network and you want to go to that network.|эй, вы пришли из этой сети и хотите перейти в эту сеть.
Which way do I need to send you?|Куда мне нужно отправить вас?
Do I need to send you this way, do I need to send you this way?|Мне нужно отправить вас этим путем, нужно ли мне отправить вас этим?
Apparently, it's not in your network cuz you wouldn't have gone to your router.|Очевидно, его нет в вашей сети, потому что вы бы не пошли к своему роутеру.
You would have gone to your gateway, you wouldn't have sent it, the protocol wouldn't have sent you, IP wouldn't have sent you to the gateway if it was local.|Вы бы пошли на свой шлюз, вы бы его не отправили, протокол не отправил бы вас, IP не отправил бы вас на шлюз, если бы он был локальным.
So, since it saw that it wasn't a local IP address,|Итак, поскольку он увидел, что это не локальный IP-адрес,
it sent you to the gateway so then it's up to the router to look at its routing table to make a decision which way to send you.|он отправил вас на шлюз, поэтому маршрутизатор должен посмотреть на свою таблицу маршрутизации, чтобы принять решение, каким путем вам отправить.
Okay?|Ладно?
That is the job of the router.|Это работа маршрутизатора.
And with that in mind, with that in mind,|И с учетом этого, с учетом этого,
these are the lessons to come next, right, in this particular session.|это уроки, которые будут следующими, верно, в этой конкретной сессии.
What type of routing am I gonna use?|Какой тип маршрутизации я собираюсь использовать?
Okay?|Ладно?
We shall talk next, so you need to make a decision, because this,|Мы поговорим дальше, поэтому вам нужно принять решение, потому что это,
in IP version four, you really need to pay attention to how things are getting sent from one point to the next.|в четвертой версии IP вам действительно нужно обращать внимание на то, как данные пересылаются от одной точки к другой.
And are we creating ARP and are, our routing, oh I'm sorry,|И мы создаем ARP, и наша маршрутизация, извините,
are, our routing tables are being efficient?|наши таблицы маршрутизации эффективны?
Are they efficient, are they too big?|Они эффективны, не слишком ли велики?
Do we need to do route summarization manually,|Нужно ли нам делать суммирование маршрута вручную,
which ever protocol that we're using?|какой протокол мы используем?
Are we building a hierarchy, so you don't need to know about everything?|Мы строим иерархию, чтобы вам не нужно было знать все?
So, when the path of the network gets created because that's what the routers do based on the routing protocols.|Итак, когда создается путь сети, потому что это то, что делают маршрутизаторы на основе протоколов маршрутизации.
They create the logical path.|Они создают логический путь.
Or are you gonna create that logical path.|Или вы собираетесь создать этот логический путь.
So, the routing process is gonna be the same regardless the size of your network.|Итак, процесс маршрутизации будет одинаковым независимо от размера вашей сети.
Regardless, if it doesn't have an ARP entry,|В любом случае, если у него нет записи ARP,
this is the first time you're sending information, or just, there was no communication being sent so the ARP table got erased.|это первый раз, когда вы отправляете информацию, или просто не было отправлено сообщение, поэтому таблица ARP была стерта.
And you send an ARP first, and it replies back with a MAC address of your gateway.|И вы сначала отправляете ARP, и он отвечает MAC-адресом вашего шлюза.
And then it sends the information, the router still needs to look at it's routing table to make a decision where to send you|И затем он отправляет информацию, маршрутизатору все еще нужно посмотреть свою таблицу маршрутизации, чтобы принять решение, куда вам отправить
and then the same thing happens on the other side.|а потом то же самое происходит на другой стороне.
It could be two computers, 2,000, 2|Это могут быть два компьютера, 2000, 2
million, 200 million, it doesn't matter.|миллион, 200 миллионов, это не важно.
That process repeats itself over, and over, and over again.|Этот процесс повторяется снова, и снова, и снова.
This is the reasons now we have neighbor discovery in IPv6.|По этой причине теперь у нас есть обнаружение соседей в IPv6.
It's making things a lot easier to network with a lot more nodes that we have now.|Это значительно упрощает работу в сети с гораздо большим количеством узлов, которые у нас есть сейчас.
but you need to understand this routing process.|но вы должны понимать этот процесс маршрутизации.
In order to network, we need to know the source MAC address, which is ours,|Чтобы подключиться к сети, нам нужно знать исходный MAC-адрес, который является нашим,
of course, the destination MAC address that's within our own segment which is our gateway, right?|конечно, MAC-адрес назначения, который находится в нашем собственном сегменте, который является нашим шлюзом, верно?
If we're going outside our network.|Если мы выходим за пределы нашей сети.
The destination IP address and the source IP address, and the port number.|IP-адрес назначения, IP-адрес источника и номер порта.
If you're FTPing, if you're telnetting, if you're SSHing,|Если вы используете FTP, если вы используете Telnet, если вы используете SSH,
if you're going on the internet.|если вы идете в Интернет.
Those destination port numbers.|Эти номера портов назначения.
That's what I'm talking about.|Это то, о чем я говорю.
And that's gonna be the line of questioning you're going to be asked on the test.|И это будет тот вопрос, который вам зададут на тесте.
So when you're going through this chapter in the book that I've always told you to look at for your certification.|Итак, когда вы читаете эту главу книги, я всегда просил вас взглянуть на нее для получения сертификата.
These exercises that they have in there,|Эти упражнения, которые у них есть,
is what you need to focus on.|это то, на чем вам нужно сосредоточиться.
The understanding of ARP.|Понимание ARP.
And they'll give you several examples like this.|И они приведут вам несколько таких примеров.
If this will be a server, let's say, and that's a web server.|Если это будет сервер, скажем, веб-сервер.
This PC, PC2 here, pretend it's a web server.|Этот ПК, здесь ПК2, представляет собой веб-сервер.
And I wanna ping this web server.|И я хочу пропинговать этот веб-сервер.
I wanna go to this website, let's say.|Скажем, я хочу зайти на этот сайт.
I'm going to go to a web page,|Я собираюсь перейти на веб-страницу,
it will still do the ARP, give me back the MAC address.|он по-прежнему будет выполнять ARP, верните мне MAC-адрес.
I will send that back up to you.|Я отправлю это вам обратно.
You make a decision which way I need to go,|Ты принимаешь решение, куда мне идти,
based on whatever type of routing I'm doing.|в зависимости от того, какой тип маршрутизации я использую.
Send it, cuz I looked at his routing pro,|Отправить, потому что я посмотрел на его профи маршрутизации,
routing table.|таблица маршрутизации.
Send it out the next router.|Отправьте его на следующий маршрутизатор.
That router will then switch it, look at it's routing table and say okay,|Затем этот маршрутизатор переключит его, посмотрит на его таблицу маршрутизации и скажет хорошо,
it's down my fast ethernet 00.|это мой быстрый Ethernet 00.
First time I know this, so I'm gonna send the ARP down, he's gonna reply back.|Я впервые это узнаю, поэтому я отправлю ARP, он ответит.
And then I'm gonna send it right back down to that particular one.|А потом я отправлю его обратно к тому конкретному.
So it doesn't really matter, the process stays the same and that's what you need to understand.|Так что на самом деле это не имеет значения, процесс остается прежним, и это то, что вам нужно понять.
So with this web server, destination MAC address,|Итак, с этим веб-сервером MAC-адрес назначения,
source MAC address destination IP address.|исходный MAC-адрес IP-адрес назначения.
Source IP address, and it's a web server,|Исходный IP-адрес, и это веб-сервер,
port 80.|порт 80.
That right there are the questions that you're going to get asked.|Вот и есть вопросы, которые вам зададут.
Or the line of questioning that you're going to get asked on your examination.|Или вопрос, который вам зададут на экзамене.
That is what you need to look at.|Вот на что нужно смотреть.
But not only in exams, when you're in a real world environment,|Но не только на экзаменах, когда вы находитесь в реальной среде,
and you're trying to get to a destination network.|и вы пытаетесь попасть в целевую сеть.
We do our trace routes, and see where the problem is, it's happening,|Мы проводим трассировку маршрутов и видим, где проблема, она происходит,
and why is it happening.|и почему это происходит.
Do we have an entry for that particular network?|Есть ли у нас запись для этой конкретной сети?
Why did it drop at that point?|Почему оно упало в тот момент?
Are we having a physical error issue?|У нас проблема с физической ошибкой?
So, all these things come into mind, but definitely,|Итак, все эти вещи приходят в голову, но определенно,
understanding this process will help us in the future to troubleshoot,|понимание этого процесса поможет нам в будущем устранять неполадки,
hey, where did their problem go wrong?|эй, где их проблема пошла не так?
Or, how is my packet being, you know, how is my packet traversing the network?|Или, как мой пакет, вы знаете, как мой пакет проходит по сети?
How did I get over there from point A to point B?|Как я перебрался из пункта А в пункт Б?
So that chapter on the routing process is important but I broke it down to very simple steps and that's what it is.|Так что эта глава о процессе маршрутизации важна, но я разбил ее на очень простые шаги, и вот что это такое.
If you want to read all 36 steps, you go for it, you go for it.|Если вы хотите прочитать все 36 шагов, сделайте это, сделайте это.
The more knowledge you know, the better.|Чем больше знаний вы знаете, тем лучше.
But, definitely, you want to go through the examples.|Но, безусловно, вы хотите просмотреть примеры.
Go through the examples because their examples in that book are the examples that you're going to see.|Просмотрите примеры, потому что их примеры в этой книге - это те примеры, которые вы собираетесь увидеть.
Not verbatim, obviously, but is the examples that has the same concept that you're gonna see in your exam.|Не дословно, очевидно, но это примеры, которые имеют ту же концепцию, которую вы увидите на своем экзамене.
All right, ladies and gentlemen.|Хорошо, дамы и господа.
That is your IP routing process.|Это ваш процесс IP-маршрутизации.
Now we start learning, hey, how are we gonna route?|Теперь мы начинаем учиться, эй, как мы будем двигаться?
Okay.|Ладно.
I'll see you in the next lesson.|Увидимся на следующем уроке.
[BLANK_AUDIO]|[BLANK_AUDIO]