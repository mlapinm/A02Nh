D:\mailCloud\prjother\tmp\1\c19_The 4 Lower Layers of the OSI.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
All right, let's do the four lower layers.|Хорошо, давайте сделаем четыре нижних слоя.
Now we have the transport, network,|Теперь у нас есть транспорт, сеть,
data-link and physical.|канал передачи данных и физический.
So what happens at the transport layer?|Так что же происходит на транспортном уровне?
The transport layer now, it takes that chunk of data and starts segmenting it.|Теперь транспортный уровень берет этот кусок данных и начинает его сегментировать.
Now it starts breaking it apart.|Теперь он начинает разваливаться.
Now it starts putting some protocols, TCP,|Теперь он начинает ставить некоторые протоколы, TCP,
connection oriented, UDP, connection less.|ориентированный на соединение, UDP, без соединения.
Remember I told you in the previous lesson that DNS will use both?|Помните, я говорил вам на предыдущем уроке, что DNS будет использовать оба?
Well it all depends, it all depends, on what it's doing.|Ну, все зависит, все зависит от того, что он делает.
Now, the transport layer makes sure,|Теперь транспортный уровень гарантирует, что
because if you're using TCP,|потому что если вы используете TCP,
that's TCP's work in there, and has acknowledgements,|это работа TCP, и есть подтверждения,
negative acknowledgements, windowing,|отрицательные подтверждения, окна,
sequencing.|последовательность действий.
What does that mean?|Что это значит?
That means it makes sure that when it's going to talk to another computer,|Это означает, что когда он будет разговаривать с другим компьютером,
they say, hey listen, let's do this three way handshake.|они говорят, послушайте, давайте сделаем это трехстороннее рукопожатие.
Let's synchronize.|Синхронизируем.
Hey, are you ready to talk?|Эй, ты готов поговорить?
Hey, I am acknowledging you.|Эй, я тебя признаю.
I am ready to talk.|Я готов к разговору.
Okay, I acknowledge that you are ready to talk.|Хорошо, я подтверждаю, что вы готовы к разговору.
Let's go ahead and start sending data.|Давайте продолжим и начнем отправлять данные.
That's how that works.|Вот как это работает.
TCP, that's why we use TCP/IP.|TCP, поэтому мы используем TCP / IP.
That's the, that's the internet protocol.|Это интернет-протокол.
Imagine if that protocol, the sweeter protocol, that TCP/IP, even though they're in two separate layers, instead of using TCP, we'll use UDP.|Представьте, что этот протокол, более сладкий протокол, этот TCP / IP, даже если они находятся на двух разных уровнях, вместо использования TCP, мы будем использовать UDP.
Sometimes we may get to a web page,|Иногда мы можем попасть на веб-страницу,
sometime we, we wouldn't.|когда-нибудь мы бы не стали.
Because UDP does not do any acknowledgement or windowing or sequencing or anything like that.|Потому что UDP не выполняет никаких подтверждений, окон, упорядочивания или чего-то подобного.
That's why we use TCP.|Вот почему мы используем TCP.
Because TCP is connection oriented, all right?|Потому что TCP ориентирован на соединение, понятно?
So that's what happens at the transport layer and we do get these acknowledgements.|Вот что происходит на транспортном уровне, и мы действительно получаем эти подтверждения.
It makes sure, if it gets a negative acknowledgement because when it comes to the windowing and the flow control, when it sends,|Он гарантирует, что получит отрицательное подтверждение, потому что когда дело доходит до окон и управления потоком, когда он отправляет,
you know you have a window size of one or a window size of three.|вы знаете, что у вас размер окна один или размер окна три.
Your book explains that.|Ваша книга объясняет это.
It says, hey, I'm sending you one, two,|Он говорит: эй, я посылаю тебе один, два,
and three.|и три.
Hey, I got one, two, and three, send me four, five, and six, and so forth.|Эй, у меня есть один, два и три, пришлите мне четыре, пять, шесть и так далее.
Or send me four, and then I'll send your four, five and six,|Или пришлите мне четыре, а затем я пришлю ваши четыре, пять и шесть,
depending the size of your window.|в зависимости от размера вашего окна.
But if you say, hey, I'm sending you one,|Но если вы скажете, эй, я пришлю вам один,
two and three, and all of a sudden you reply, I'll send you,|два и три, и вдруг вы отвечаете, я пришлю вам,
hey I got a one and three.|эй, у меня есть один и три.
I didn't get two.|Я не получил двух.
That means you're gonna get resent number two before anything else.|Это означает, что вы получите возмущение номер два прежде всего.
So it will resend the information.|Таким образом, он повторно отправит информацию.
That's the flow control that it has.|Это управление потоком, которое у него есть.
It makes sure that everything,|Он следит за тем, чтобы все
not only do you get all the bytes that are supposed to be getting to you, but they are in the correct order, they're in the correct order.|Вы не только получаете все байты, которые должны быть вам доставлены, но они находятся в правильном порядке, они находятся в правильном порядке.
So your message is not corrupted.|Значит, ваше сообщение не повреждено.
And this is where all, you see all the different types of attacks, the syntax and all these different things that people attack.|И именно здесь вы видите различные типы атак, синтаксис и все эти разные вещи, которые атакуют люди.
They attack the TCP protocol.|Они атакуют протокол TCP.
So that's your seg, that's your transport layer.|Итак, это ваш сегмент, это ваш транспортный уровень.
The network layer, my favorite layer,|Сетевой уровень, мой любимый слой,
there we deal with packets now, packets.|вот с пакетами имеем дело, пакеты.
We deal with IP connection less, even though TCP/IP, IP is connection less.|Мы меньше занимаемся IP-соединением, хотя TCP / IP, IP-соединение меньше.
TCP make sure it gets there, IP is just a driver, right?|TCP убедитесь, что он попадает туда, IP - это просто драйвер, верно?
IPX, we rarely see it anymore, that is NetWare operating system.|IPX, мы его уже редко видим, это операционная система NetWare.
Hardly seen NetWare around much places.|Вряд ли видел NetWare во многих местах.
We got our route team protocol such as RIP, EIGRP, and OSPF,|У нас есть протокол группы маршрутизации, такой как RIP, EIGRP и OSPF,
right, depending on what type of routing protocol,|правильно, в зависимости от типа протокола маршрутизации,
depending on the types of hop counts,|в зависимости от типа количества хмеля,
metrics, or cost.|метрики или стоимость.
Then we have, and that is also considered the logical topology and obviously we have routers that are working at that layer.|Тогда у нас есть, и это также считается логической топологией, и, очевидно, у нас есть маршрутизаторы, которые работают на этом уровне.
So they, they were testing you, and they asked you a question about OSI,|Итак, они, они тестировали вас, и они задали вам вопрос об OSI,
it could be something similar to this.|это могло быть что-то подобное.
At what layer do routers work at, let's just say, to say a question.|На каком уровне работают роутеры, скажем так, вопрос.
Layer three, network layer, things like that.|Третий уровень, сетевой уровень и тому подобное.
IP addressing, that's when we talk about IP.|IP-адресация, вот когда мы говорим об IP.
IP ver, not only IP version 4 but IP version 6 also works at the network layer.|IP ver, не только IP версии 4, но IP версии 6 также работает на сетевом уровне.
Anything that deals with routing will deal,|Все, что связано с маршрутизацией, будет иметь дело,
will be at the network layer that deals with the packets.|будет на сетевом уровне, который имеет дело с пакетами.
Then we get to the data-link layer.|Затем мы переходим к уровню передачи данных.
Now data-link layer, you need to understand.|Теперь вам нужно понять уровень передачи данных.
That is sub-divided into two layers.|Это подразделено на два уровня.
You have your logical link control, and you have your media access control.|У вас есть контроль логических ссылок и контроль доступа к мультимедиа.
The data-link layer is called go-between layer,|Уровень канала передачи данных называется промежуточным уровнем,
the go between the network layer and the physical layer, because the logical link control knows how to talk to the upper layer network protocols.|переход между сетевым уровнем и физическим уровнем, потому что управление логическим каналом знает, как взаимодействовать с сетевыми протоколами верхнего уровня.
And the media access control will know how to go down to the physical layer into the zeros and ones.|А управление доступом к среде будет знать, как перейти на физический уровень в нули и единицы.
So it's a go between, but in today's technology,|Так что это промежуточный вариант, но в современных технологиях
depending on the application, it may just skip that layer altogether.|в зависимости от приложения, он может вообще пропустить этот слой.
All right, but in the, in data-link, what do we need to know?|Хорошо, но что нам нужно знать в канале передачи данных?
Frames, frames, that's what it deals with.|Рамки, рамки, вот этим и занимается.
Not packets, but frames.|Не пакеты, а кадры.
What is it?|Что это?
What type of address are we looking at?|Какой тип адреса мы ищем?
We're looking at MAC address.|Мы смотрим на MAC-адрес.
MAC addresses, physical addresses, burned in addresses.|MAC-адреса, физические адреса, записанные в адресах.
That's the kind of table it creates, it creates a MAC address table.|Он создает такую ​​таблицу, он создает таблицу MAC-адресов.
These switches, switches, bridges, WAN protocols, WAN, PPP,|Эти коммутаторы, коммутаторы, мосты, протоколы WAN, WAN, PPP,
FRAME-RELAY, X25, MPLS, all those are WAN protocols that work at layer two.|FRAME-RELAY, X25, MPLS, все это протоколы WAN, которые работают на втором уровне.
And that's all we need to know.|И это все, что нам нужно знать.
That's all we need to know.|Это все, что нам нужно знать.
I get excited about it, but it's just the fact that, hey,|Я в восторге от этого, но дело в том, что, эй,
we don't need to get too crazy with the OSI.|нам не нужно слишком сходить с ума с OSI.
And that's, that's why these are very quick lessons.|Вот почему это очень быстрые уроки.
Because all I want you to concentrate on is like, hey, I've got seven layers.|Потому что все, на чем я хочу, чтобы вы сконцентрировались, это типа, эй, у меня семь слоев.
These are the things that work on those layers, and these are my PDUs.|Это то, что работает на этих уровнях, и это мои PDU.
Okay, these are my PDUs.|Ладно, это мои PDU.
All right, and then the last layer, we have the physical layer, which we have BITS.|Хорошо, и затем последний уровень, у нас есть физический уровень, у нас есть БИТЫ.
We have BITS.|У нас есть БИТЫ.
What do we deal with there?|Что мы там делаем?
The voltage, the cabling, hubs,|Напряжение, кабели, концентраторы,
amplifiers, repeaters, again, WAN,|усилители, репитеры, опять же WAN,
wireless, physical, very unintelligent devices.|беспроводные, физические, очень неразумные устройства.
When we deal with, you see that's why the hub is there.|Когда мы имеем дело с, вы понимаете, почему существует хаб.
All right so, anything that's physical that deals with voltage you can touch,|Хорошо, все физическое, имеющее дело с напряжением, к которому можно прикоснуться,
that is your physical layer.|это ваш физический уровень.
Once it comes out through there, then it goes to the other side with all its,|Как только он выходит через него, он переходит на другую сторону со всеми своими
everything in this little sequence.|все в этой маленькой последовательности.
And then it goes up to the other computer,|Затем он переходит на другой компьютер,
and things get put back together.|и все снова складывается.
So those are your four lower layers.|Итак, это ваши четыре нижних уровня.
A lot of things that are happening here.|Здесь много чего происходит.
But, again, what do you need to remember?|Но, опять же, о чем нужно помнить?
You need to remember the Transport,|Транспорт нужно помнить,
Network, Data-Link, Physical.|Сеть, канал передачи данных, физический.
The Data-Link is subdivided into two layers, LLC and Mac.|Канал передачи данных разделен на два уровня: LLC и Mac.
And that we have the PDUs that are segments, packets, frames, and bits.|И что у нас есть PDU, которые представляют собой сегменты, пакеты, кадры и биты.
Okay, don't forget that.|Хорошо, не забывай об этом.
I'll see you in the next one.|Увидимся в следующем.
[BLANK_AUDIO]|[BLANK_AUDIO]