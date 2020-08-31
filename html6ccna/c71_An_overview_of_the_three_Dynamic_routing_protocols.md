D:\mailCloud\prjother\tmp\1\c71_An overview of the three Dynamic routing protocols.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
All right, everyone, welcome back.|Хорошо, все, добро пожаловать обратно.
You configured your static routes, you've configured your default routes.|Вы настроили свои статические маршруты, вы настроили маршруты по умолчанию.
You have connectivity going across.|У вас есть возможность подключения.
So we're doing things statically, but as a company we're going to grow.|Итак, мы делаем что-то статично, но как компания мы будем расти.
We're going to become a large enterprise.|Мы собираемся стать большим предприятием.
So we need to now say, okay,|Итак, теперь нам нужно сказать, хорошо,
we need to start thinking of which dynamic routing protocol to use.|нам нужно подумать о том, какой протокол динамической маршрутизации использовать.
That's what we're going to start learning about now, dynamic routing protocols.|Вот что мы собираемся начать изучать сейчас, протоколы динамической маршрутизации.
Now we're going to an overview first, of all three in this lesson.|Теперь мы собираемся сначала сделать обзор всех трех в этом уроке.
We're going do, we're going to talk about RIP version two.|Мы собираемся поговорить о второй версии RIP.
We're gonna talk about EIGRP, and then we're gonna talk about OSPF.|Мы поговорим о EIGRP, а затем поговорим об OSPF.
All right, we're gonna talk about the differences and, you know,|Хорошо, мы поговорим о различиях и, знаете,
which one would be better or not.|какой будет лучше или нет.
We're just gonna talk a little bit about all three of them.|Мы просто поговорим немного обо всех троих.
And then in the next lessons to come,|А потом в следующих уроках,
we're gonna get into details and configure each and every one.|мы собираемся вдаваться в подробности и настраивать каждого до единого.
So let's, let's take the first one.|Итак, давайте, возьмем первый.
This is our lab that we have.|Это наша лаборатория.
Remember, we have a default route on our stub routers and we have a static routes on our middle router, and we can get from|Помните, что у нас есть маршрут по умолчанию на наших тупиковых маршрутизаторах, и у нас есть статические маршруты на нашем среднем маршрутизаторе, и мы можем получить от
one point to the next.|одна точка к другой.
But now it comes time to do those dynamic routing protocols.|Но теперь пришло время создать протоколы динамической маршрутизации.
And I believe in the earlier lessons we talked about that when we started talking about what type of routing should I use?|И я верю в предыдущие уроки, о которых мы говорили, когда мы начали говорить о том, какой тип маршрутизации мне следует использовать?
Right?|Правильно?
Should it be static or dynamic?|Он должен быть статическим или динамическим?
Well, we've made the decision already that we're gonna go to dynamic because it's just gonna be too much to handle because we're gonna have a lot of routers.|Что ж, мы уже приняли решение, что мы перейдем к динамическому, потому что это будет слишком сложно, потому что у нас будет много маршрутизаторов.
So, the first routing protocol is RIP version 2.|Итак, первый протокол маршрутизации - это RIP версии 2.
Now there is a version for IPv6 which is RIPng.|Теперь есть версия для IPv6 - RIPng.
We'll discuss a little bit about that as well.|Об этом мы тоже немного поговорим.
So I'll put it in here.|Я положу это сюда.
All right, RIPng.|Хорошо, РИПнг.
Let me put that in lower case so it doesn't confuse, oops, so it doesn't confuse anyone.|Позвольте мне написать это в нижнем регистре, чтобы это не запутало, ой, чтобы никого не запутать.
Ripng, which is the IP version six.|Ripng ​​- шестая IP-версия.
Now it's RIP, regardless.|Теперь все равно RIP.
It's RIP regardless.|В любом случае это RIP.
Now the way you configure RIPng is different, but it still has the same limitations.|Теперь способ настройки RIPng изменился, но он по-прежнему имеет те же ограничения.
And yes, I am gonna say limitations.|И да, я скажу ограничения.
Because RIP, nonetheless, is a distance vector, a distance vector writing protocol, all right?|Потому что RIP, тем не менее, является вектором расстояния, протоколом записи вектора расстояния, понятно?
What does that mean?|Что это значит?
That it only cares about which direction and the distance,|Что его волнует только направление и расстояние,
right, distance and direction.|вправо, расстояние и направление.
Hop counts, that's what it means by distance.|Хмель считается, вот что значит расстояние.
Hop counts, we have a hop count of 15.|Подсчет переходов, у нас есть счетчик переходов 15.
So you have to go through, you can only go up to 15 routers.|Таким образом, вы должны пройти, вы можете пройти только до 15 маршрутизаторов.
Beyond that, it's unreachable.|Кроме того, это недостижимо.
It's unreachable.|Это недостижимо.
So you're limited, or you're limiting your growth, using RIP version 2.|Таким образом, вы ограничены, или вы ограничиваете свой рост, используя RIP версии 2.
Well, we have 15 routers, I consider that quite a pretty large network anyway.|Итак, у нас есть 15 роутеров, я считаю, что это довольно большая сеть.
Right, not a, maybe an enterprise network with hundreds and thousands of routers or hundreds of thousands of routers, but it's|Верно, не корпоративная сеть с сотнями и тысячами маршрутизаторов или сотнями тысяч маршрутизаторов, но это
still a pretty big network.|все еще довольно большая сеть.
Let's say these are schools, like I always talk about schools.|Допустим, это школы, как я всегда говорю о школах.
You have 15 campuses.|У вас 15 кампусов.
They're going across maybe counties, what have you.|Они, может быть, пересекают графства, что у вас есть.
So and you have multiple subnets underneath.|Итак, у вас есть несколько подсетей внизу.
So, you don't wanna keep track of that,|Итак, вы не хотите отслеживать это,
the routing protocol will do it.|протокол маршрутизации сделает это.
One of the disadvantages of distance vector routing protocols,|Один из недостатков протоколов дистанционно-векторной маршрутизации,
disadvantage of distance vector routing protocol,|недостаток протокола дистанционно-векторной маршрутизации,
is that they summarize automatically,|в том, что они суммируют автоматически,
auto-ma-ti-cally.|автоматически.
There you go.|Вот так.
Now, what does that mean.|Что это значит?
That means that it doesn't understand or,|Это означает, что он не понимает или,
and I'll say it different ways.|и я скажу это по-разному.
It doesn't understand that you have a Class A address with a /24.|Он не понимает, что у вас есть адрес класса A с / 24.
It only sees the classful boundary.|Он видит только классовую границу.
So in this example here, you see that in the serials,|В этом примере вы видите, что в сериалах
we have a 10.1.1.4 with a CIDR 30 and then 10.1.1.8 with a CIDR 30.|у нас есть 10.1.1.4 с CIDR 30, а затем 10.1.1.8 с CIDR 30.
Well, RIP doesn't see that.|Что ж, RIP этого не видит.
RIP sees 10.1, I mean sorry says 10.0.0.0.|RIP видит 10.1, то есть извините говорит 10.0.0.0.
So we have an entire network that's in a class A cuz that's how you build it.|Итак, у нас есть вся сеть, относящаяся к классу А, потому что именно так вы ее строите.
It's the whole network.|Это вся сеть.
It's, you know, hierarchical, or the way you want it to set up as a class A network.|Это, вы знаете, иерархическое, или то, как вы хотите его настроить как сеть класса А.
And you configure a distance vector routing protocol,|И вы настраиваете протокол маршрутизации вектора расстояния,
it's gonna summarize everything to the classful boundary.|он суммирует все до классовых границ.
Cuz the subnet mask is not gonna go out on the updates.|Потому что маска подсети не будет выходить из обновления.
It just sees, hey, it's a ten.|Он просто видит, эй, это десять.
That's a problem, and that's how they're gonna go ahead and test you in the certification exam with distance vector routing protocols.|Это проблема, и вот как они собираются протестировать вас на сертификационном экзамене с протоколами дистанционно-векторной маршрутизации.
That they're gonna give you let's say like a print screen, a scenario,|Что они дадут вам, скажем так, экран для печати, сценарий,
that this individual administrator has his entire network with a class A or a class B, but you have a distance vector routing protocol configured.|что этот индивидуальный администратор имеет всю свою сеть с классом A или классом B, но у вас настроен протокол маршрутизации вектора расстояния.
And you forgot the magical word.|И ты забыл волшебное слово.
In order to do this, you have to type, and I'll put it down here, so it doesn't go off the screen, no auto-summary.|Для этого вам нужно набрать текст, и я запишу его здесь, чтобы он не исчезал с экрана, без автоматического подведения итогов.
That's what makes RIP version 2 RIP version 2,|Вот что делает RIP версии 2 RIP версии 2,
that you have that no auto-summary command.|что у вас нет этой команды автоматического суммирования.
Forget about RIP version one, ignore version, RIP version one.|Забудьте о версии RIP один, игнорируйте версию, версию RIP один.
Nobody uses it anymore.|Больше этим никто не пользуется.
RIP version 2 and up, but with RIP version 2 or even EIGRP,|RIP версии 2 и выше, но с RIP версии 2 или даже EIGRP,
I didn't want to mention it just yet, but EIGRP.|Я пока не хотел об этом упоминать, но об EIGRP.
They're distance vectors.|Это векторы расстояния.
You must and I can't stress it.|Вы должны, и я не могу это подчеркнуть.
I'm going to stress it throughout the whole routing class.|Я буду подчеркивать это на всем уроке маршрутизации.
You need to type that no auto-summary when you're doing a distance vector routing protocol.|Вам нужно ввести это без автоматического суммирования, когда вы выполняете протокол векторной маршрутизации на расстоянии.
That way, what the no auto-summary command does when you're configuring these distance vectors, such as RIP version 2|Таким образом, то, что делает команда no auto-summary при настройке этих векторов расстояний, например, RIP версии 2
and EIGRP.|и EIGRP.
What I, when you talk about this guy right here,|Что я, когда вы говорите об этом парне прямо здесь,
totally different story, because the way you configure it.|Совершенно другая история, потому что так вы ее настраиваете.
With RIP version 2, I mean yeah, with RIP version 2, what you're actually doing when you're configuring it, you're creating network statements.|С RIP версии 2, я имею в виду, да, с RIP версии 2, что вы на самом деле делаете, когда настраиваете его, вы создаете сетевые операторы.
All right.|Отлично.
You're telling it, because with static routes, before remember, you told it, hey,|Вы рассказываете это, потому что со статическими маршрутами, прежде чем вспомнить, вы сказали это, эй,
there's a network beyond this point.|за этой точкой есть сеть.
You told this router, hey,|Вы сказали этому роутеру, эй,
there's networks that exist beyond that particular point right there.|есть сети, которые существуют за пределами этой конкретной точки прямо там.
You had to tell it.|Вы должны были это сказать.
Now, what's happening is that the routing protocol is saying,|Теперь происходит то, что протокол маршрутизации говорит:
hey guys, these are the networks that I am connected to.|Привет, ребята, это сети, к которым я подключен.
That's what the routing protocol does.|Вот что делает протокол маршрутизации.
It yells out to its neighbor router or neighbor routers and says, hey,|Он кричит своему соседнему маршрутизатору или соседним маршрутизаторам и говорит: "Эй,
these are the networks I am connected to.|это сети, к которым я подключен.
So it's snitching itself out.|Так что он выкарабкается.
That's what they call routing by rumor,|Это то, что по слухам называют маршрутизацией,
routing by rumor.|маршрутизация по слухам.
So you create these network statements.|Итак, вы создаете эти сетевые операторы.
I'm gonna tell you router RIP version 2,|Я расскажу вам роутер RIP версии 2,
and they go network.|и они идут по сети.
I'm attached to this particular network,|Я привязан к этой конкретной сети,
this particular network, this particular network.|эта конкретная сеть, эта конкретная сеть.
And then no auto-summary, and the no auto-summary is so crucial because once you tell it, that says, hey listen,|И тогда нет автоматического резюме, и оно так важно, потому что, как только вы это скажете, он говорит: эй, слушай,
do not summarize these networks when you send out the updates.|не суммируйте эти сети при рассылке обновлений.
Send a true subnet mask out.|Отправить истинную маску подсети.
That's one thing that it does,|Это то, что он делает,
that it's gonna send a subnet mask out on the updates.|что он будет отправлять маску подсети при обновлениях.
So the real network, it'll, everybody will know whoa,|Итак, настоящая сеть, все будут знать, эй,
they're attached to the 10.1.1.4, not the 10.0.0.0, right.|они прикреплены к 10.1.1.4, а не к 10.0.0.0, верно.
So there's no confusion.|Так что путаницы нет.
As well, as well, what it's gonna do is allow you to have discontiguous networks.|Кроме того, он позволит вам иметь разрозненные сети.
Not that you should have discontiguous networks,|Не то чтобы у вас были разрозненные сети,
but it will allow you to have that.|но это позволит вам иметь это.
Like me, I have discontiguous networks all the time when I had to do my labs.|Как и я, у меня всегда есть разрозненные сети, когда мне приходилось делать свои лаборатории.
I have a class C network here, have a class A.|У меня здесь сеть класса C, у меня класс A.
There's no continuity there.|Здесь нет преемственности.
There's, there's no order there.|Там нет никакого порядка.
I use this type because I do things for visualization purposes.|Я использую этот тип, потому что делаю вещи для визуализации.
So you know which is your LAN and which is your serial.|Итак, вы знаете, какая у вас локальная сеть, а какой у вас серийный номер.
But with the no auto-summary command, it would you allow you to do that.|Но без команды автоматического суммирования вы бы позволили это сделать.
It would allow you to do that.|Это позволит вам это сделать.
So when we talk about RIP, one of the things about RIP that makes it,|Итак, когда мы говорим о RIP, одной из составляющих RIP является
that everybody doesn't like about it, is the fact,|что всем это не нравится, это факт,
not only the fact that you only have 15|не только то, что у вас всего 15
routers.|маршрутизаторы.
You can't go beyond 15 routers.|Вы не можете выйти за пределы 15 маршрутизаторов.
But you have every 30 seconds by default,|Но по умолчанию каждые 30 секунд
which you can change, you can tweak this.|которые вы можете изменить, вы можете настроить это.
Is this is an update timer, which you can change.|Это таймер обновления, который можно изменить.
Every 30 seconds, you send the entire routing table out on the updates.|Каждые 30 секунд вы отправляете всю таблицу маршрутизации в обновлениях.
So you can see that okay,|Итак, вы можете видеть, что хорошо,
my neighbor router now knows about the networks that I'm connected to.|мой соседний маршрутизатор теперь знает о сетях, к которым я подключен.
And I know the, the network that my neighbor's connected to.|И я знаю сеть, к которой подключен мой сосед.
But since we're running RIP,|Но поскольку мы используем RIP,
every 30 seconds we're gonna tell each other the same thing, every 30 seconds.|каждые 30 секунд мы будем говорить друг другу одно и то же, каждые 30 секунд.
So, if you're worried about bandwidth,|Итак, если вас беспокоит пропускная способность,
that's an issue.|это проблема.
That's an issue, so you have to play around with timers.|Это проблема, поэтому вам придется поиграть с таймерами.
But we don't wanna get into that right now.|Но мы не хотим сейчас вдаваться в подробности.
So that's RIP version 2, RIP version 2, 15|Итак, это RIP версии 2, RIP версии 2, 15
routers,|роутеры
every 30 seconds you send an update, gotta use the no auto-summary.|каждые 30 секунд вы отправляете обновление, не используйте автоматическое резюме.
When it comes to RIPng,|Что касается RIPng,
there is no network statements that you have to create.|нет никаких сетевых операторов, которые вы должны создавать.
With RIPng, and now everything is multicast.|С RIPng, и теперь все многоадресно.
Everything is multicast, all right, with IPv6.|Все нормально, с IPv6 многоадресная рассылка.
But even in RIP version 2, when they send out updates, it's multicast as well.|Но даже в RIP версии 2, когда они рассылают обновления, они также многоадресны.
But with RIPng you configure it on the interface,|Но с RIPng вы настраиваете его на интерфейсе,
or an interface by interface basis.|или интерфейс на основе интерфейса.
So whatever interface that you want to participate in this particular RIP process, you go in there and enable that RIP process in that interface.|Итак, какой бы интерфейс вы ни хотели участвовать в этом конкретном процессе RIP, вы заходите туда и включаете этот процесс RIP в этом интерфейсе.
That's it, there's no network statements.|Все, сетевых заявлений нет.
So there's no need for no auto-summary in RIPng.|Таким образом, в RIPng нет необходимости в автоматическом суммировании.
See what the great things with IPv6 that we're getting,|Посмотрите, какие замечательные возможности IPv6 мы получаем,
when we're configuring these new routing protocols and everything.|когда мы настраиваем эти новые протоколы маршрутизации и все такое.
You don't have to worry about network statements.|Вам не нужно беспокоиться о сетевых операторах.
You don't have to worry about no auto-summary.|Вам не нужно беспокоиться об автоматическом подведении итогов.
That doesn't exist anymore with RIPng.|Этого больше не существует с RIPng.
But again, you're being tested for the CCNA certification.|Но опять же, вы проходите проверку на сертификат CCNA.
So do not, and I'm stressing it again, do not forget that no auto-summary command.|Так что не надо, и я еще раз подчеркиваю, не забывайте, что нет команды автосводки.
Okay?|Ладно?
But very little questions on the exam are about RIP version 2.|Но очень мало вопросов на экзамене касается RIP версии 2.
Even RIPng, they'll ask you things like multicast addresses and all that,|Даже RIPng они будут спрашивать вас о таких вещах, как адреса многоадресной рассылки и все такое,
and we'll get into that as we get into the details of each one.|и мы разберемся с этим по мере того, как будем разбираться в деталях каждого из них.
So that's RIP.|Так что RIP.
All right?|Отлично?
Man, I can go across any manufacturer.|Чувак, я могу найти любого производителя.
You can have a Juniper router, you can have a Cisco router,|У вас может быть маршрутизатор Juniper, вы можете иметь маршрутизатор Cisco,
whatever type of router you want, RIP will work on.|Какой бы тип маршрутизатора вы ни выбрали, RIP будет работать.
But what happens when you start growing?|Но что происходит, когда вы начинаете расти?
Well, the next protocol that we will be learning after RIP, will be E,|Что ж, следующий протокол, который мы будем изучать после RIP, будет E,
whoops, will be EIGRP.|упс, будет EIGRP.
Well, let's talk about the disadvantage first.|Что ж, сначала поговорим о минусе.
Let's, let's say the bad news first, which is not really bad news.|Давайте сначала скажем плохие новости, которые на самом деле не являются плохими новостями.
CISCO SPECIFIC, whoop,|КОНКРЕТНЫЙ CISCO, крик,
you can only use it on CISCO routers.|вы можете использовать его только на маршрутизаторах CISCO.
That's it.|Вот и все.
No other router supports this, at least not yet.|Ни один другой маршрутизатор не поддерживает это, по крайней мере, пока.
I've heard rumors, somewhere out there in the networking grapevine that they're working on an EIGRP that's going to work across all routers,|Я слышал слухи, где-то в сети, что они работают над EIGRP, который будет работать на всех маршрутизаторах,
all different types of vendors.|все разные типы продавцов.
But, as far as we're concerned right now,|Но, что касается нас сейчас,
EIGRP only works with Cisco routers,|EIGRP работает только с маршрутизаторами Cisco,
period.|период.
So, if you want to consider that a disadvantage, I don't.|Так что, если вы хотите считать это недостатком, я не считаю.
I'd rather use Cisco routers anyway.|Я все равно предпочитаю использовать маршрутизаторы Cisco.
All right, but, regardless, it's only Cisco specific.|Хорошо, но, тем не менее, это только для Cisco.
Now, with EIGRP, it's still considered,|Теперь, с EIGRP, все еще считается,
well it is considered,|хорошо это считается,
an advanced DV, I'll call it, distance vector.|продвинутый DV, я назову его вектором расстояния.
It used to be called the hybrid proto, all right, the hybrid routing protocol.|Раньше это называлось гибридным протоколом, да, протоколом гибридной маршрутизации.
Now they like to call it an advanced distance vector routing protocol.|Теперь они любят называть это протоколом расширенной векторной маршрутизации.
All that is, is that it acts like a link state, like OSPF.|Все, что есть, это то, что он действует как состояние ссылки, как OSPF.
And it has traits from OSPF and traits from a distance vector.|И у него есть черты OSPF и черты вектора расстояния.
What are the distance vector traits?|Каковы черты вектора расстояния?
Well, you've got to type in no auto-summary, cuz it summarizes,|Ну, вам не нужно вводить автоматическое резюме, потому что оно резюмирует,
summarize, summarizes auto, I'll look on top, matically.|резюмирую, резюмирую авто, посмотрю сверху, матово.
Whoa, some notes are in capital, others are in lowercase.|Ого, одни ноты написаны заглавными буквами, другие строчными.
Oh, that's all good.|О, это все хорошо.
All right.|Отлично.
Summarizes automatically.|Суммирует автоматически.
So that means, and from the last student that took the test the EIGRP was the one you're being tested on.|Это означает, что, начиная с последнего студента, который прошел тест, EIGRP был тем, на котором вы проходили тестирование.
So you know I'm gonna drill you on that.|Так что ты знаешь, я собираюсь подтолкнуть тебя к этому.
You must type the no auto-summary command.|Вы должны ввести команду no auto-summary.
Again, another distance vector routing protocol, advance or whatever.|Опять же, еще один протокол маршрутизации на основе вектора расстояния, заранее или что-то еще.
You, distance vector, you must type no auto-summary.|Вы, вектор расстояния, не должны вводить автоматическое резюме.
Or not, it will summarize everything to the classful boundary.|Или нет, он подведет все к классовой границе.
Do not forget that, all right?|Не забывай, ладно?
So Cisco specific is an advanced distance vector.|Таким образом, специфика Cisco - это продвинутый вектор расстояния.
We're summarizing automatically so we need to type the no auto-summary, all right?|Мы подводим итоги автоматически, поэтому нам нужно ввести автоматическое резюме, хорошо?
And the good thing about it is let's look at the link state portion of it.|И что хорошо в этом, давайте посмотрим на часть состояния ссылки.
That was the distance vector portion, all right, not to get too deep into it.|Это была часть вектора расстояния, хорошо, чтобы не углубляться в нее.
But let's look at the link state.|Но давайте посмотрим на состояние ссылки.
What's the advantage of it?|Какая от этого польза?
That it only sends the updates the first time.|Что он отправляет обновления только в первый раз.
So it only sends updates, or I'll say all updates, first time.|Таким образом, он отправляет только обновления, или я скажу все обновления, в первый раз.
Meaning when it's time to get its no, when it starts to get to know its neighbors,|Это означает, что когда пришло время отказаться, когда он начинает узнавать своих соседей,
then it sends hey, this is who I'm connected to.|затем он отправляет привет, это то, с кем я связан.
After that initial where everybody's learning about everybody and they converge finally, that's it.|После того, как все узнают обо всех и наконец сходятся, вот и все.
Only thing, only changes then, only changes, because EIGRP uses hellos to keep those adjacencies, all right,|Единственное, только тогда, только изменения, потому что EIGRP использует hellos для сохранения этих смежностей, хорошо,
between the same autonomous systems.|между одними и теми же автономными системами.
I'm, I'm just throwing things out there.|Я, я просто выбрасываю вещи туда.
Okay.|Ладно.
Because EIGRP is based on autonomous systems, all right?|Потому что EIGRP основан на автономных системах, понятно?
When we get into EIGRP, we'll go even further.|Когда мы перейдем к EIGRP, мы пойдем еще дальше.
But EIGRP, that's the that's the one.|Но EIGRP, вот и все.
Can you see that right there?|Вы видите это прямо здесь?
Autonomous systems, okay, autonomous systems.|Автономные системы, да, автономные системы.
Numbers, obviously.|Цифры, разумеется.
So for the CCNA because I know some of you are out there saying, well Laz,|Итак, что касается CCNA, потому что я знаю, что некоторые из вас говорят: ну, Лаз,
can we have multiple autonomous system numbers?|можем ли мы иметь несколько номеров автономных систем?
Of course.|Конечно.
Of course you can have multiple autonomous system numbers, but guess what,|Конечно, у вас может быть несколько номеров автономных систем, но угадайте, что,
you're taking a test.|вы проходите тест.
And this test says one autonomous system.|И этот тест говорит об одной автономной системе.
Everybody must be on the same autonomous system number.|У всех должен быть один и тот же номер автономной системы.
If you're not, you're not going to communicate.|Если нет, вы не собираетесь общаться.
All right, but anyway, we'll get into that later.|Хорошо, но в любом случае мы поговорим об этом позже.
Again, the update's only done the first time.|Опять же, обновление выполняется только в первый раз.
After that, after that it's just changes.|После этого просто меняется.
Anything that's, you know, changes or you added or you took out a subnet, then you'll send that.|Все, что, как вы понимаете, изменилось, или вы добавили или удалили подсеть, вы отправите это.
Other than that, it won't do it.|Кроме этого, он этого не сделает.
So that's good.|Так что хорошо.
That helps us out, right?|Это нам помогает, правда?
Plus it creates something called the topology table.|Кроме того, он создает так называемую таблицу топологии.
Again, a link state thing, right?|Опять же, состояние ссылки, верно?
That's what OSPF does as well, creates a typology table, well so does EIGRP.|OSPF также создает таблицу типологий, EIGRP - тоже.
So that's what they call an advanced,|Вот что они называют продвинутым,
an advanced, distance vector routing protocol.|усовершенствованный протокол векторной маршрутизации на расстоянии.
That's all.|Вот и все.
Now, the last one that we wanna talk about, to round off the lecture, is OSPF.|И последнее, о чем мы хотим поговорить, чтобы завершить лекцию, - это OSPF.
Now, this is a whopper of a routing protocol.|Итак, это гигантский протокол маршрутизации.
This is a huge routing protocol.|Это огромный протокол маршрутизации.
But for us, at the CCNA level, we don't have to worry about too many things.|Но нам, на уровне CCNA, не нужно беспокоиться о слишком многих вещах.
Now am I gonna give you a lot of information?|Теперь я дам вам много информации?
Yes I am.|Да, я.
But I'm gonna tell you, all right,|Но я скажу тебе, хорошо,
this is what you need to pay attention to at this moment for this test.|это то, на что вам нужно обратить внимание в данный момент для этого теста.
So as I'm telling you things about the details of OSPF, I'm gonna point out or highlight hey, this is what you need to know, for now.|Итак, когда я рассказываю вам кое-что о деталях OSPF, я собираюсь указать или выделить, эй, это то, что вам нужно знать на данный момент.
This is what you'll need to know for later.|Это то, что вам нужно знать позже.
Cuz OSPF is a huge routing protocol.|Потому что OSPF - это огромный протокол маршрутизации.
It is for huge networks.|Это для огромных сетей.
So this is what's called a link state routing protocol.|Это то, что называется протоколом маршрутизации состояния канала.
I'm not gonna say this.|Я не собираюсь этого говорить.
It's a link state, all right, ls.|Это состояние ссылки, хорошо, ls.
All right.|Отлично.
There is no limitation, meaning there is no hop counts.|Ограничений нет, то есть нет подсчета переходов.
EIGRP, which I have failed to mention, all right, is also based on hop counts.|EIGRP, о котором я, конечно, не упомянул, также основан на количестве переходов.
But OSPF is not based on hop counts.|Но OSPF не основан на подсчете переходов.
There is no limitations with OSPF.|OSPF не имеет ограничений.
Because OSPF is based like, EIGRP is based on autonomous systems but is limited to hops, meaning it's limited to 255 routers.|Поскольку OSPF основан на том же, EIGRP основан на автономных системах, но ограничен переходами, то есть ограничен 255 маршрутизаторами.
You say, well, wow, 255 routers, Laz,|Вы говорите ну вау, 255 роутеров, Лаз,
that's a pretty big network as it is.|это и так довольно большая сеть.
Yeah it is, 200, 200 some plus routers,|Да, 200, еще 200 плюс роутеры,
wow.|Вот это да.
But guess what?|Но знаете что?
OSPF is based on areas.|OSPF основан на областях.
OSPF can have over 4.2 billion areas.|OSPF может иметь более 4,2 миллиарда областей.
That's a pretty big network there.|Это довольно большая сеть.
So, OSPF can be huge, especially when you're doing multiple area OSPF.|Итак, OSPF может быть огромным, особенно когда вы делаете OSPF с несколькими областями.
That's why you can have so many areas.|Вот почему у вас может быть так много областей.
But guess what, for us at the CCNA, all we need to be concerned about is single area.|Но угадайте, что для нас в CCNA все, о чем нам нужно беспокоиться, - это одна область.
So when they give you those print screens and they tell you,|Поэтому, когда они дают вам эти печатные экраны и говорят вам:
hey Laz, they told me that this router is OSPF.|Привет, Лаз, мне сказали, что это маршрутизатор OSPF.
But one was on area one, one was on area two, one was on area three.|Но один был в зоне один, один был в зоне два, один был в зоне три.
They, they weren't talking.|Они, они не разговаривали.
Yeah, they're not gonna talk.|Да, они не будут разговаривать.
Because what they want you to, they, what they want you to understand is that for CCNA, a single area cuz there's criterias.|Потому что они хотят, чтобы вы поняли, что для CCNA - единственная область, потому что есть критерии.
I'm not getting into details yet.|Я пока не вдавался в подробности.
There's criterias in OSPF for it to become neighbors with its routers,|В OSPF есть критерии для того, чтобы он стал соседом со своими маршрутизаторами,
and the area is one of the criterias.|и площадь - один из критериев.
All right, so single area, single area is what you need to be concerned with.|Хорошо, одна область, одна область - это то, о чем вам нужно позаботиться.
And you can see that there, single area.|И вы можете видеть это там, единая область.
That's what we need to be concerned with,|Это то, о чем нам нужно беспокоиться,
with OSPF.|с OSPF.
OSPF, very, I'm gonna put it, I'm gonna put it in there, very processor,|OSPF, очень, я его вставлю, я вставлю туда, очень процессор,
processor, something like that, there's a two S, intensive, intense, for that.|процессор, что-то в этом роде, для этого есть два S, интенсивный, интенсивный.
Because it's a huge routing protocol.|Потому что это огромный протокол маршрутизации.
It's a huge routing protocol.|Это огромный протокол маршрутизации.
It does a lot of calculations, right, open shortest path first calculations.|Он делает много вычислений, правильно, сначала вычисляет кратчайший путь.
So it does do a lot of calculations.|Поэтому он делает много вычислений.
Each routing, each router that's running OSPF does a lot of calculations.|Каждая маршрутизация, каждый маршрутизатор, на котором работает OSPF, выполняет множество вычислений.
So it does, that's one of the I guess the disadvantages,|Так и есть, это один из недостатков,
if you would think of it that way, that it,|если бы вы подумали об этом так,
you have a have a very good router because if not OSPF will burn it, will burn it.|у вас есть очень хороший маршрутизатор, потому что если OSPF не сожжет его, то сожжет его.
It depends on how you build a network obviously but still, it does a lot of work.|Очевидно, это зависит от того, как вы строите сеть, но, тем не менее, он выполняет много работы.
It does a lot of work.|Делает много работы.
So those are the three routing protocols.|Итак, это три протокола маршрутизации.
Now, once we start getting into the details of it, we'll talk about the algorithms and exactly how you should configure and all these different things.|Теперь, когда мы начнем вдаваться в подробности, мы поговорим об алгоритмах, о том, как именно вы должны настраивать, и обо всех этих разных вещах.
But for now, know that hey, we're going to do dynamic routing.|Но пока знайте, что мы собираемся сделать динамическую маршрутизацию.
Now we need to choose in, on the three routing protocols that we have cuz we do have EIGRP for version six and we do have|Теперь нам нужно выбрать три протокола маршрутизации, которые у нас есть, потому что у нас есть EIGRP для версии шесть, и у нас есть
OSPF version three for versions of IPv6.|OSPF версии три для версий IPv6.
So it all depends what you wanna do,|Так что все зависит от того, что ты хочешь делать,
because all the IP version six for EIGRP and OSPF are configured in the interface.|потому что все IP версии шесть для EIGRP и OSPF настроены в интерфейсе.
That's great, no network statements.|Замечательно, никаких сетевых заявлений.
Makes things a lot easier on you.|Делает жизнь намного проще.
They configure a little bit different,|Настраивают немного иначе,
yeah.|Да.
But you know what?|Но вы знаете, что?
It is easier.|Легче.
But still, you need to make a decision,|Но все же нужно принять решение,
right.|право.
Cisco, EIGRP, RIP across whatever vendor but limited to 15 hops.|Cisco, EIGRP, RIP от любого поставщика, но с ограничением до 15 переходов.
OSPF, huge, processor intensive.|OSPF, огромный, ресурсоемкий.
What am I going to use?|Что я буду использовать?
What I am going to use?|Что я собираюсь использовать?
So now that you know a little bit about all three routing protocols,|Итак, теперь, когда вы знаете немного обо всех трех протоколах маршрутизации,
let's now go and start getting into the details of RIP.|А теперь давайте перейдем к подробностям RIP.
I'll see you in the next lesson.|Увидимся на следующем уроке.
[BLANK_AUDIO]|[BLANK_AUDIO]