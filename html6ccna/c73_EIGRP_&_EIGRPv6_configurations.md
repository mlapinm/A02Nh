D:\mailCloud\prjother\tmp\1\c73_EIGRP & EIGRPv6 configurations.md  


__|__
--|--
All right.|Отлично.
Welcome back.|Добро пожаловать.
We finished RIP version two, and RIPng.|Мы закончили RIP версии 2 и RIPng.
That was one of the dynamic routing protocols.|Это был один из протоколов динамической маршрутизации.
And we talked about its limitations and how to configure.|И мы поговорили о его ограничениях и способах настройки.
So now we're getting into EIGRP.|Итак, теперь мы переходим к EIGRP.
Now all these routing protocols that we're talking about, they're considered IGPs.|Все эти протоколы маршрутизации, о которых мы говорим, считаются IGP.
What is that?|Что это такое?
Interior Gateway Protocols, which means that they share the same routing table.|Протоколы внутреннего шлюза, что означает, что они используют одну и ту же таблицу маршрутизации.
And this holds even truer when it comes to EIGRP, and we start doing OSPF.|И это еще более верно, когда дело доходит до EIGRP, и мы начинаем делать OSPF.
Because EIGRP is based on something called autonomous systems and I think we talked about it previously.|Потому что EIGRP основан на том, что называется автономными системами, и я думаю, мы уже говорили об этом ранее.
An autonomous system number,|Номер автономной системы,
let me put autonomous system number.|позвольте мне поставить номер автономной системы.
Now this autonomous system number can be in the range between 1 through 65,500,|Теперь этот номер автономной системы может находиться в диапазоне от 1 до 65 500,
and I believe it's 35.|и я считаю, что это 35.
That number keeps popping up all over the place.|Это число постоянно появляется повсюду.
All right, that is how many autonomous systems you can have.|Хорошо, вот сколько у вас может быть автономных систем.
For the CCNA, and I know I've said this a million times, and I'm going to say it a million more times until I engrave it in your heads.|Что касается CCNA, и я знаю, что говорил это миллион раз, и я скажу это еще миллион раз, пока я не запечатлел это в ваших головах.
For the CCNA certification, which is what you are studying for ladies and gentlemen, you only need a single autonomous system.|Для сертификации CCNA, которую вы изучаете для дам и джентльменов, вам понадобится только одна автономная система.
So, EIGRP is the favorite.|Итак, EIGRP - фаворит.
I mean, you're taking a Cisco certification, guess what?|Я имею в виду, вы проходите сертификацию Cisco, знаете что?
They're gonna ask you a lot of questions on EIGRP.|Они зададут вам много вопросов по EIGRP.
So, I think they're still doing the simulation in EIGRP.|Итак, я думаю, что они все еще проводят моделирование в EIGRP.
So, one of the main things you need to remember, or focus on is that,|Итак, одна из главных вещей, которые вам нужно запомнить или сосредоточить внимание, - это то, что
that autonomous system must be the same on all the routers.|эта автономная система должна быть одинаковой на всех маршрутизаторах.
Okay, because the test is based on a single autonomous system number.|Хорошо, потому что тест основан на одном номере автономной системы.
So when you're doing your simulations,|Итак, когда вы занимаетесь симуляцией,
or your print screens, or whatever it is that they ask you,|или ваши печатные экраны, или что-то еще, о чем вас спрашивают,
or whatever questions.|или какие-то вопросы.
You got to make sure that that autonomous system number is the same on all the routers.|Вы должны убедиться, что этот номер автономной системы одинаков на всех маршрутизаторах.
That is crucial.|Это очень важно.
That is crucial.|Это очень важно.
That is one of the main things they're going to test you on.|Это одна из главных вещей, на которой они собираются вас проверить.
Okay?|Ладно?
Now EIGRP, they called it the hybrid.|Теперь EIGRP, они назвали это гибридом.
Some people still call it the hybrid protocol.|Некоторые до сих пор называют это гибридным протоколом.
We talked about that as well.|Об этом мы тоже говорили.
But now it's considered an ADVANCED DV or distance vector.|Но теперь это считается ADVANCED DV или вектором расстояния.
Right?|Правильно?
An ADVANCED DV, let me bring this up here a little bit, let me put my finger on it,|ADVANCED DV, позвольте мне немного поднять это здесь, позвольте мне указать пальцем на это,
put it up.|положить его.
All right, well,|Хорошо, хорошо,
let's maximize it why not?|давайте максимизируем почему бы и нет?
Okay, an advanced distance vector routing protocol which means it has both the link state and distance vector.|Хорошо, расширенный протокол маршрутизации вектора расстояния, что означает, что он имеет как состояние соединения, так и вектор расстояния.
Distance vector, we discussed it already,|Вектор расстояния, мы это уже обсуждали,
it does have a max.|у него есть макс.
Hop count of 255.|Количество переходов 255.
Okay, MAX HOP COUNT of 255.|Хорошо, MAX HOP COUNT из 255.
But it is set by default to 100, to 100.|Но по умолчанию он установлен на 100, на 100.
By default you, you know,|По умолчанию вы знаете,
you'd be running 100 routers at a time or you can change it, within the EIGRP or router EIGRP configuration, and change the MAX HOP COUNT to 255.|у вас будет 100 маршрутизаторов одновременно, или вы можете изменить это в конфигурации EIGRP или маршрутизатора EIGRP и изменить MAX HOP COUNT на 255.
You can do that.|Вы можете сделать это.
So you still wanna limit it as far as how many routers you can have in your network,|Так что вы все еще хотите ограничить количество маршрутизаторов в вашей сети,
not to mention that it can only be,|не говоря уже о том, что это может быть только
only Cisco routers.|только роутеры Cisco.
Only Cisco routers.|Только роутеры Cisco.
You can only use Cisco routers.|Вы можете использовать только маршрутизаторы Cisco.
Up to this point only EIGRP both,|До этого момента только EIGRP,
EIGRP for version 4 or or for IPv6.|EIGRP для версии 4 или IPv6.
Only Ciscor outers.|Только снаружи Ciscor.
Now, the algorithm is DUAL,|Теперь алгоритм ДВОЙНОЙ,
DUAL ALGO, all right, to abbreviate.|ДВОЙНОЙ АЛГОРИТМ, хорошо, для сокращения.
The dual algorithm.|Двойственный алгоритм.
Now because of the dual algorithm,|Теперь из-за двойного алгоритма
there's, it does do a lot of calculations unlike RIP, that didn't pay attention.|там он выполняет много вычислений, в отличие от RIP, на который не обращал внимания.
They only had, cared about is hey, how many hop count, how far away are you and which direction I should go?|Они только позаботились о том, эй, сколько прыжков сосчитать, как далеко вы и в каком направлении мне нужно идти?
Boom.|Бум.
That's it.|Вот и все.
It won't load balance.|Это не будет загружать баланс.
It won't load balance if there's nothing in between.|Он не будет загружать баланс, если между ними нет ничего.
Cuz remember, what's the shortest point,|Потому что помни, какая самая короткая точка,
from a certain destination?|из определенного пункта назначения?
A straight line.|Прямая линия.
So if he sees a straight line,|Итак, если он видит прямую линию,
oh, one hop away?|о, один прыжок?
Well, I'm going that way.|Что ж, я иду туда.
Does it matter if it's, you know,|Имеет ли значение, если это, знаете ли,
a 56k line or what it is.|линия 56k или что это такое.
So, it's not really paying attention to different things you know, it's, it's,|Итак, он не обращает внимания на разные вещи, вы знаете, это, это,
it's heavy traffic this way,|здесь интенсивное движение,
slower this way, whatever the case may be.|так медленнее, в любом случае.
Doesn't pay attention to what's going on on the network, it just sees hey,|Не обращает внимания на то, что происходит в сети, просто видит, эй,
this is the shortest route from point A to point B,|это кратчайший путь из точки А в точку Б,
based on how many routers I got to go through.|в зависимости от того, через сколько маршрутизаторов мне пришлось пройти.
That's not the case with EIGRP,|Это не относится к EIGRP,
which is great.|что здорово.
EIGRP is based on metrics.|EIGRP основан на показателях.
Based in the sense of which way it's going to send the information.|Основываясь на том, каким образом он будет отправлять информацию.
Now these metrics,|Теперь эти метрики,
are calculated yes by a dual but there's something called K-VALUES.|рассчитываются да по двойному, но есть нечто, называемое К-ЗНАЧЕНИЯ.
Now your book tells you there's only four.|Теперь в вашей книге сказано, что их всего четыре.
There's controversy cuz there's,|Есть споры, потому что есть
some say four, some say five.|некоторые говорят четыре, некоторые говорят пять.
You have BANDWIDTH,|У вас есть BANDWIDTH,
DELAY, RELIABILITY.|ЗАДЕРЖКА, НАДЕЖНОСТЬ.
Really?|В самом деле?
BANDWIDTH, DELAY, RELIABILITY, LOAD.|ПОЛОСА, ЗАДЕРЖКА, НАДЕЖНОСТЬ, НАГРУЗКА.
MTU.|MTU.
Now I've put the older test book,|Сейчас положил старую зачетную книжку,
all right, with the newer test book.|хорошо, с новой тестовой тетрадью.
And there are certain things they really don't talk about.|И есть некоторые вещи, о которых они действительно не говорят.
And they've taken things out, whatever but, I'm gonna tell you everything.|И они все убрали, что угодно, но я вам все расскажу.
Because this one right here, this MTU.|Потому что вот этот MTU.
This MTU right there,|Вот этот MTU,
is what the controversy is.|вот в чем спор.
Some people says that it does use the maximum transmission unit.|Некоторые говорят, что он использует максимальную передачу.
There are questions in the exam that may ask you, what's the maximum transmission unit, which is 1500 by default,|В экзамене есть вопросы, которые могут спросить вас, какова максимальная единица передачи, которая по умолчанию составляет 1500,
all right, bytes per second.|хорошо, байт в секунду.
But what's on,|Но что происходит,
what's on is BANDWIDTH and DELAY.|что идет, это BANDWIDTH и DELAY.
Those are the defaults that it uses,|Это значения по умолчанию, которые он использует,
all right?|отлично?
Bandwidth, if you're using,|Пропускная способность, если вы используете,
let's say in our serials, and we'll take a look at the interfaces when we configure EIGRP.|скажем, в наших сериалах, и мы посмотрим на интерфейсы при настройке EIGRP.
We'll take a look at those interfaces.|Мы посмотрим на эти интерфейсы.
And we may even create a new line item, so you can see how you can manipulate the bandwidth, all right?|И мы можем даже создать новую позицию, чтобы вы увидели, как вы можете управлять пропускной способностью, хорошо?
Where you can go ahead and send it one way instead of another.|Где вы можете пойти дальше и отправить в одну сторону, а не в другую.
So EIGRP based on these K-VALUES,|Итак, EIGRP на основе этих K-VALUES,
it will choose the faster route.|он выберет более быстрый маршрут.
So if you do have a straight line,|Итак, если у вас есть прямая линия,
you know, one hop kinda way.|вы знаете, одним прыжком.
But that straight line is,|Но эта прямая линия,
you know, a dial-up.|вы знаете, набор.
And you have, you know, T1s on the side,|И у вас есть Т1 на стороне,
it'll choose to load balance across,|он выберет балансировку нагрузки,
you know, the the outsides.|вы знаете, внешние стороны.
So, EIGRP definitely does,|Итак, EIGRP определенно делает,
is a very good routing protocol.|это очень хороший протокол маршрутизации.
It is scalable because you, in the real world you will have multiple autonomous systems, and why would you have multiple autonomous systems?|Он масштабируемый, потому что в реальном мире у вас будет несколько автономных систем, и зачем вам несколько автономных систем?
Because you can maintain inconsistencies within that autonomous system.|Потому что вы можете поддерживать несогласованность в этой автономной системе.
That's why you would use, not only for organizational hierarchy, hierarchical,|Вот почему вы должны использовать не только для организационной иерархии, иерархические,
right a very hard word.|правильно очень жесткое слово.
Purposes but, because,|Цели, но, потому что,
organization, all right?|организация, хорошо?
But for the CCNA we're lucky.|Но с CCNA нам повезло.
We don't have to worry about that.|Нам не о чем беспокоиться.
Not that it's that difficult, but definitely we don't have to be concerned with it.|Не то чтобы это так сложно, но определенно нам не о чем беспокоиться.
We need to be concerned that hey,|Мы должны быть обеспокоены этим, эй,
is one autonomous system, and these are the K-VALUES that we use.|это одна автономная система, и это те К-ЗНАЧЕНИЯ, которые мы используем.
Speaking of when EIGRP creates what's called an adjacency with its neighbor or neighbors, right.|Говоря о том, когда EIGRP создает так называемую смежность со своим соседом или соседями, верно.
Remember, routers only talk with who they're directly connected to,|Помните, роутеры общаются только с теми, к кому они напрямую подключены,
regardless of whatever routing protocol you're gonna have.|независимо от того, какой протокол маршрутизации у вас будет.
They only talk who they're connected to.|Они говорят только о том, с кем связаны.
So in order for EIGRP to create that adjacency,|Итак, чтобы EIGRP создал эту смежность,
with it's neighbor router, it must have,|со своим соседним маршрутизатором, он должен иметь,
there's a couple criteria,|есть пара критериев,
couple criterias.|пара критериев.
I'm going to hit enter one more time.|Я собираюсь нажать Enter еще раз.
So, criteria's For adjacencies.|Итак, критерии смежности.
Adjacen, j, j no.|Adjacen, j, j no.
I think, it's like that, adjacencies.|Я думаю, что это так, смежности.
All right.|Отлично.
You must have, first and foremost, same autonomous system.|У вас должна быть, прежде всего, такая же автономная система.
Second, k-values.|Во-вторых, k-значения.
Same.|Тем же.
You must have,|Вы должны иметь,
I should have put identical.|Я должен был поставить идентичный.
You must have the same k-values,|У вас должны быть одинаковые k-значения,
if your k-value, if your meaning, if on one router using bandwidth and delay and the other router using reliability and load, then boom.|Если ваше k-значение, если вы имеете в виду, если на одном маршрутизаторе используется пропускная способность и задержка, а на другом маршрутизаторе используются надежность и нагрузка, тогда бум.
It's not gonna create that neighbor,|Это не создаст этого соседа,
that adjacency,|эта смежность,
you're not gonna become neighbors, okay.|ты не собираешься стать соседями, ладно.
And the last thing.|И последнее.
And this is really hello.|И это действительно привет.
Is you ping supposedly,|Ты якобы пингуешься,
you can have different hellos.|у вас могут быть разные приветы.
And those hellos is what makes it a link state,|И эти приветы делают это состояние ссылки,
or one of the things that makes it a link state, where it sends the updates.|или одна из вещей, которая делает его состоянием ссылки, куда он отправляет обновления.
Hey, I'm still here,|Эй, я все еще здесь,
I'm still here, I'm still here.|Я все еще здесь, я все еще здесь.
It doesn't, it's, according to you book,|Это не так, это, согласно вашей книге,
these are the three criterias that it looks at.|это три критерия, на которые он смотрит.
But really, the hellos are not as important for EIGRP than it is for OSPF.|Но на самом деле приветствия не так важны для EIGRP, как для OSPF.
OSPF very strict when it comes to hellos,|OSPF очень строг, когда дело касается приветствий,
they must be the same.|они должны быть одинаковыми.
EIGRP is very flexible, I think,|Я думаю, что EIGRP очень гибкий,
but for EIGRP, the default hello,|но для EIGRP привет по умолчанию,
we'll look at it.|мы посмотрим на это.
I, I think it's five seconds.|Я думаю, это пять секунд.
But, again,|Но, опять же,
you really don't mess around with that.|вы действительно не возитесь с этим.
They aren't going to test you on the hello's when it comes to EIGRP.|Они не собираются проверять вас на приветствии, когда дело касается EIGRP.
That's why I tell you it really,|Вот почему я говорю вам это на самом деле,
as far as the criteria's to become neighbors, your book says it.|Что касается критериев для того, чтобы стать соседями, ваша книга говорит об этом.
But, reality,|Но, на самом деле,
EIGRP doesn't really pay attention.|EIGRP на самом деле не обращает внимания.
It's not that finicky.|Это не так уж и разборчиво.
Definitely the autonomous system,|Определенно автономная система,
the K-values, do need to be the same.|K-значения должны быть одинаковыми.
Do need to be the same.|Неужели нужно быть таким же.
And these two criterias,|И эти два критерия,
the first two that I put on here.|первые два, которые я здесь надел.
These two right here, is something that for your examination, whether you're in college, or, you know, whatever school you're in, or you're taking the test.|Эти двое прямо здесь, это то, что нужно для вашего экзамена, учитесь ли вы в колледже или, знаете, в какой бы школе вы ни учились, или когда вы проходите тест.
There's something you need to home in.|Есть кое-что, что вам нужно сделать.
Okay, you need to home in on that.|Хорошо, тебе нужно сосредоточиться на этом.
So yes, EIGRP does have these criteria.|Так что да, у EIGRP есть эти критерии.
This is something good that it does that it looks at these different things,|Это то, что он делает, что он смотрит на эти разные вещи,
in order to make a decision.|чтобы принять решение.
Because EIGRP creates something, right.|Потому что EIGRP что-то создает, верно.
It's not like hop counts.|Это не похоже на счет хмеля.
You're gonna see something that looks like this.|Вы увидите что-то похожее на это.
In RIP, when you did RIP, you saw this.|В RIP, когда вы выполняли RIP, вы видели это.
Alright.|Хорошо.
It brackets when you look at the routing table.|Это скобки, когда вы смотрите на таблицу маршрутизации.
Where is that thing?|Где это?
Alright.|Хорошо.
You know you're using RIP because it's the administrative distance and it's one hop away, cool.|Вы знаете, что используете RIP, потому что это административное расстояние, и это на расстоянии одного прыжка, здорово.
With EIGRP, it's not like that.|С EIGRP все не так.
With EIGRP you have the administrative distance of 90, and then you'll have a number, lets say one,|С EIGRP у вас есть административное расстояние 90, а затем у вас будет число, скажем, один,
two, three, four, five, six.|два, три, четыре, пять, шесть.
Something like this.|Что-то вроде этого.
Right.|Правильно.
That's called a metric.|Это называется метрикой.
This is the feasible distance.|Это допустимое расстояние.
The feasible distance.|Возможное расстояние.
Which became, which is the b,|Который стал, который является б,
which became the successor route,|который стал преемником маршрута,
but now it's in the routing table.|но теперь это в таблице маршрутизации.
So EIGRP uses things, and this is more terminology that you need to be aware of.|Итак, EIGRP использует разные вещи, и это дополнительная терминология, о которой вам нужно знать.
Because EIGRP uses something called feasible, FS,|Поскольку EIGRP использует то, что называется выполнимым, FS,
which stands for feasible successor.|что означает возможного преемника.
Which means a backup route.|Что означает резервный маршрут.
Alright, you have also something called a feasible distance.|Хорошо, у вас также есть допустимое расстояние.
The feasible distance is a calculation of the advertised distance of a router.|Возможное расстояние - это расчет объявленного расстояния до маршрутизатора.
To the destination.|К месту назначения.
Okay?|Ладно?
Then you have the advertised distance.|Тогда у вас есть объявленное расстояние.
Alright, this is what the router considers,|Хорошо, это то, что считает маршрутизатор,
hey this is how much it takes to get to,|эй, это сколько нужно, чтобы добраться,
from point a to point b.|из точки а в точку б.
You also have a successor,|У тебя тоже есть преемник,
and you can put s, all right.|и вы можете поставить s, хорошо.
But this is what's called the successor.|Но это то, что называют преемником.
Route, let's say.|Маршрут, допустим.
Successor route meaning it has the lowest feasible distance which makes it to the routing table.|Последующий маршрут означает, что он имеет наименьшее возможное расстояние до таблицы маршрутизации.
All right?|Отлично?
Feasible successors, which is the backup route, let me put it up here,|Возможные преемники, что является резервным путем, позвольте мне указать здесь,
remain, in the topology table.|остаются в таблице топологии.
All right, so you have feasible successors, feasible systems,|Хорошо, у вас есть возможные преемники, возможные системы,
advertiser systems and successor.|системы рекламодателя и преемник.
I'll put SR, successor routes.|Ставлю SR, преемник маршрутов.
All right, let's, let's do that.|Хорошо, давай, давай сделаем это.
Successor routes, SR.|Преемник маршрутов, SR.
Successor routes.|Последующие маршруты.
The successor routes, successor I won,|Маршруты преемника, преемник я победил,
I go to the routing table.|Захожу в таблицу маршрутизации.
Lower, lower successor.|Нижний, нижний преемник.
So let's say between these two, let's say.|Итак, скажем, между этими двумя, скажем так.
Let's say they're going to the same place and you have the administrative distance.|Допустим, они едут в одно и то же место, а у вас административное расстояние.
And this one is, I don't know,|А это, я не знаю,
one, two, three, four, five, six.|один два три четыре пять шесть.
So out of these two, this has a lower feasible distance than this one.|Таким образом, из этих двух, это имеет меньшее возможное расстояние, чем это.
Therefore this metric, right?|Значит, это метрика, правда?
This one will make it to the routing table while this one will stay in the topology.|Он попадет в таблицу маршрутизации, а этот останется в топологии.
Cause your topology table within EIGRP will hold all routes.|Потому что ваша таблица топологии в EIGRP будет содержать все маршруты.
All routes to all destinations.|Все маршруты по всем направлениям.
They will be there.|Они будут там.
Cuz there is one good thing.|Потому что есть одна хорошая вещь.
EIGRP creates these table for,|EIGRP создает эти таблицы для
these tables for a reason.|эти таблицы не зря.
It creates a topology table.|Создает таблицу топологии.
Well, let's put it in order.|Что ж, давайте по порядку.
It creates a neighbor table.|Создает соседнюю таблицу.
It creates, gonna do another again, it creates a, I should have done that right.|Он создает, собираюсь сделать еще один, он создает, я должен был сделать это правильно.
Creates a topology table and obviously it creates a routing table.|Создает таблицу топологии и, очевидно, создает таблицу маршрутизации.
The neighbor table is information, okay?|Таблица соседей - это информация, хорошо?
I'm sorry, I'm looking down, but it's information,|Извините, я смотрю вниз, но это информация,
info about the neighbors.|информация о соседях.
I'll put it, I'll abbreviate.|Поставлю, сокращу.
The neighbors it found.|Соседи его нашли.
Topology table Has all known routes.|Таблица топологии Имеет все известные маршруты.
So all the routes that it finds the first time it converges, okay.|Итак, все маршруты, которые он находит при первом схождении, хорошо.
Let's see if I can bring this up a little bit here, so you guys can see that.|Давайте посмотрим, смогу ли я немного поднять это здесь, чтобы вы, ребята, это увидели.
Okay, so it has all known routes.|Итак, у него есть все известные маршруты.
In the topology table all known routes good or bad, they're in there.|В таблице топологии все известные маршруты хороши или плохи, они там.
They're in there, in your topology table.|Они там, в вашей таблице топологии.
The neighbor is about hey, my neighbor router, right, information about it.|Сосед насчет эй, мой соседский роутер, да, информация об этом.
The routing table has the best routes to destination.|В таблице маршрутизации указаны лучшие маршруты к месту назначения.
And what is it based on again?|И опять же на чем он основан?
Based on lowest metric.|На основе самого низкого показателя.
It does its calculations.|Он делает свои расчеты.
It looks at the interfaces.|Смотрит на интерфейсы.
It looks at its bandwidth.|Смотрит на его пропускную способность.
And it does look at the delay.|И это действительно смотрит на задержку.
Now, the delay will be a cumulative delay.|Теперь задержка будет кумулятивной.
Now in the.|Теперь в.
This is a lab we did from previous.|Это лабораторная работа, которую мы сделали из предыдущей.
And we're gonna use it again.|И мы будем использовать его снова.
From previous in this lab, there's not gonna be any feasible successor or anything like that.|Судя по предыдущему в этой лаборатории, не будет подходящего преемника или чего-то подобного.
It's the fact that, it's gonna go ahead and it's only got one way to go.|Дело в том, что это будет продолжаться, и у него есть только один путь.
It's only got one way to go.|Есть только один путь.
So, this way and that way.|Итак, так и так.
But, when you're looking at these,|Но когда вы смотрите на них,
what can I say the,|что я могу сказать
let's look at the interface.|посмотрим на интерфейс.
Let's say, let's pick this router,|Допустим, возьмем этот роутер,
right here.|Прямо здесь.
Let me move it this way right here.|Позвольте мне переместить его сюда прямо сюда.
Okay.|Ладно.
Lets open this up a little bit.|Давайте немного откроем это.
Just to show you the interface.|Просто чтобы показать вам интерфейс.
C-I-S-C-O and let's look at that serial,|C-I-S-C-O и давайте посмотрим на этот сериал,
show interface S0/0/0 or one, sorry.|показать интерфейс S0 / 0/0 или один, извините.
All right, there's your bandwidth for that particular one,|Хорошо, вот ваша пропускная способность для этого конкретного,
for that, that's a, that's a WIC-2T.|для этого, это WIC-2T.
The WIC-2T has that type of bandwidth on there.|WIC-2T имеет такую ​​полосу пропускания.
If there was a WIC-1T, you'll be lower,|Если бы был WIC-1T, у вас будет меньше,
I mean it'll be, it's be greater, sorry.|Я имею в виду, что будет, это будет больше, извините.
No yeah, lower, lower, less bandwidth.|Нет да, ниже, ниже, с меньшей пропускной способностью.
Less bandwidth.|Меньшая пропускная способность.
And here's your delay.|А вот и ваша задержка.
Here's your delay.|Вот твоя задержка.
Now your book shows you how to calculate that.|Теперь ваша книга показывает вам, как это вычислить.
Do you need to know how to calculate that?|Вам нужно знать, как это рассчитать?
If you wanted to you can,|Если хочешь, можешь,
all right, you don't have to,|хорошо, тебе не обязательно,
it's not that it's that difficult,|не то чтобы это так сложно,
you can do it manually.|вы можете сделать это вручную.
But again, your not, your concern is,|Но опять же, это не ваше дело,
hey the faster the router means the best bandwidth.|эй, чем быстрее маршрутизатор, тем лучше пропускная способность.
So if you have a T1 going this way and you have a T3 going that way,|Итак, если у вас есть T1, идущий по этой дороге, и у вас есть T3, идущий по этой дороге,
and, you know, and depending on the connectors that you have and the cables that you have If it's fiber or if it's whatever it is.|и, знаете ли, и в зависимости от разъемов, которые у вас есть, и кабелей, которые у вас есть, если это оптоволокно или что-то еще.
It's gonna say, okay, I want to choose based on this information.|Он скажет, хорошо, я хочу сделать выбор на основе этой информации.
The delay is gonna be different.|Задержка будет другой.
So, and the bandwidth is gonna be different so I'm gonna make my calculations based on that and send you this way.|Итак, и пропускная способность будет другой, поэтому я сделаю свои расчеты на основе этого и отправлю вас сюда.
That's all.|Вот и все.
That's all it is.|Вот и все.
That's all it is.|Вот и все.
But this is where you would see it.|Но вот где вы это увидите.
You can see you have your MTUs which is 1500 bytes like I said earlier.|Вы можете видеть, что у вас есть MTU, равный 1500 байтам, как я сказал ранее.
So, keep that in mind.|Так что имейте это в виду.
For some reason or another,|По той или иной причине
I don't know which student it was,|Я не знаю, какой это был студент,
it was a while back ago.|это было некоторое время назад.
During the old examination that they asked a question on, hey, what, you know,|Во время старого экзамена они задали вопрос, эй, что, знаете,
what is the default MTU,|какой MTU по умолчанию,
or something like that.|или что-то вроде того.
For some reason it's in the back of my mind.|По какой-то причине это в глубине души.
So, there's your, your five k-values.|Итак, вот ваши пять k-значений.
Even though the book now tells you there's only four.|Хотя теперь в книге сказано, что их всего четыре.
There's five, your MTU's, your bandwidth,|Их пять, ваш MTU, ваша пропускная способность,
your delay, your reliability and your load, okay?|Ваша задержка, ваша надежность и ваш груз, хорошо?
Transmit and receive,|Передавать и получать,
all right, and your load.|ладно, а твоя нагрузка.
So, all these things come into play or could come into play when dual is making it's calculations.|Итак, все эти вещи вступают в игру или могут вступить в игру, когда dual выполняет свои вычисления.
Remember, these k-values need to be the same, need to be the same.|Помните, что эти k-значения должны быть одинаковыми, должны быть одинаковыми.
So EIGRP does do a lot of things.|Так что EIGRP действительно много чего делает.
Does do a lot of things.|Много чего делает.
It keeps track of a lot of things.|Он отслеживает множество вещей.
Especially the topology table.|Особенно таблица топологии.
Once we configure EIGRP,|После настройки EIGRP,
we'll go in there and how you look at the topology table is SHOW, and we're abbreviating, SHOW EIGRP TOPOLOGY.|мы зайдем туда, и то, как вы посмотрите на таблицу топологии, будет SHOW, а мы сокращаем - SHOW EIGRP TOPOLOGY.
Or SHOW IP EIGRP TOPOLGY, sorry.|Или ПОКАЖИТЕ ТОПОЛГИЮ IP EIGRP, простите
SHOW IP EIGRP TOPOLOGY, all right?|ПОКАЗАТЬ ТОПОЛОГИЮ IP EIGRP, хорошо?
That command right there will show you the topology table.|Эта команда сразу же покажет вам таблицу топологии.
One of the things when you're looking at the topology table that you need to be aware of, is you see a letter in front of all the routes.|Когда вы смотрите на таблицу топологии, вам необходимо знать, что вы видите букву перед всеми маршрутами.
This equals passive.|Это равносильно пассивному.
That's a good thing.|Это хорошая вещь.
All right.|Отлично.
You wanna see a passive.|Вы хотите увидеть пассив.
If you don't see a passive if you see,|Если вы не видите пассив, если видите,
let's say, active.|скажем так, активный.
Instead of a P you see an A,|Вместо P вы видите A,
that's active.|это активно.
That's a, that's not that it's a bad thing, but being active means.|Это не значит, что это плохо, но быть активным - значит.
That it's still looking.|Что он все еще ищет.
For routes, and you don't want that because it hasn't found that route.|Для маршрутов, а вы этого не хотите, потому что он не нашел этот маршрут.
There is a problem.|Существует проблема.
There is a problem if it's still active.|Есть проблема, если он все еще активен.
That it's still looking for that particular router.|Что он все еще ищет именно этот роутер.
You haven't fully converged yet.|Вы еще не сошлись полностью.
So, one of the things you want to see is passive, that P.|Итак, одна из вещей, которую вы хотите видеть, является пассивной, что П.
That is a good thing.|Это хорошая вещь.
You want to make sure that it is passive,|Вы хотите убедиться, что он пассивен,
because if not then there is a problem.|потому что если нет, тогда возникает проблема.
There could be, if I were to create a,|Если бы я создал
an exam, right,|экзамен, да,
I would definitely put a print screen on there, all right for my students.|Я бы обязательно поставил там экран для печати, хорошо для моих студентов.
And I would put one that says active or make one up obviously.|И я бы поставил один, который говорит активный, или явно придуманный.
And I will say okay, what,|И я скажу хорошо, что,
why can I get to this network?|почему я могу попасть в эту сеть?
And I will put A.|И я поставлю А.
Oh, because it's actively looking for it and that's the problem, right?|Ох, потому что он активно его ищет, и в этом проблема, верно?
So if everything is passive then we need to look for other things that could be going on.|Так что, если все пассивно, нам нужно искать другие вещи, которые могут происходить.
All right, cuz the topology table,|Хорошо, потому что таблица топологии,
one of the things that EIGRP does,|одна из функций EIGRP,
feasible successors.|возможные преемники.
You can have up to eight feasible successors.|У вас может быть до восьми возможных преемников.
Wow.|Вот это да.
And let's go back up into the notes,|И давайте вернемся к заметкам,
and lets put that in there.|и давайте поместим это туда.
You can have up to eight feasible successors.|У вас может быть до восьми возможных преемников.
That is awesome.|Это замечательно.
All right.|Отлично.
Now as you get into your other certifications, right,|Теперь, когда вы перейдете к другим сертификатам, верно,
like CCNP, it'll tell you, hey,|как CCNP, он скажет вам, эй,
you wanna feasible successor because if a route were to go down,|вы хотите возможного преемника, потому что, если маршрут пойдет вниз,
you successor route, the one that's in the routing table, that link goes down.|у следующего маршрута, указанного в таблице маршрутизации, эта ссылка отключается.
It will actually look at the topology table looking for a backup route through actually put it in the routing table and then send it that way.|Он фактически просматривает таблицу топологии в поисках резервного маршрута, фактически помещает его в таблицу маршрутизации и затем отправляет по этому пути.
Alright?|Хорошо?
So, it is,|Так что, это,
it is good to have feasible successors,|хорошо иметь реальных преемников,
but again, not too many feasible successors depending on how your design is, they could actually maybe cause loops.|но опять же, не так много возможных преемников, в зависимости от вашего дизайна, они могут действительно вызвать циклы.
So you've got to be very careful when you're, you know, you're designing your network that you don't want to have these feasible successor going on.|Итак, вы должны быть очень осторожны, когда вы, вы знаете, проектируете свою сеть, чтобы не допустить существования этого возможного преемника.
Sometimes it's good, sometimes it's bad.|Иногда это хорошо, иногда плохо.
But again, you can have eight feasible successor in your particular network.|Но опять же, у вас может быть восемь возможных преемников в вашей конкретной сети.
In our network we're not gonna have any feasible successors.|В нашей сети у нас не будет реальных преемников.
We may do another lab so I can show you,|Мы можем сделать еще одну лабораторию, чтобы я мог показать вам,
or I can show you on this one how you can change the bandwidth of a particular interface and make it go in one direction or|или я могу показать вам, как вы можете изменить полосу пропускания определенного интерфейса и заставить его работать в одном направлении или
the other, okay?|другой, ладно?
So you can see that EIGRP has a lot of things that it's doing.|Итак, вы можете видеть, что EIGRP выполняет множество функций.
And it converges Very quickly.|И очень быстро сходится.
It's one of the faster ones that immediately it converges and creates these adjacencies with its neighbor routers.|Это один из самых быстрых, который сразу же сходится и создает смежности со своими соседними маршрутизаторами.
If it meets those criterias, and it's going to meet those criterias,|Если он соответствует этим критериям, и он будет соответствовать этим критериям,
because you're not going to create anything different.|потому что вы не собираетесь создавать ничего другого.
Now, just like RIP version two and RIPng, EIGRP for version four and version six, all this that I talked about,|Теперь, точно так же, как RIP версии два и RIPng, EIGRP для версии четыре и версии шесть, все, о чем я говорил,
is exactly the same.|точно так же.
What's not the same is the configuration.|Что не то конфигурация.
You actually do it on the interface by interface basis.|Фактически вы делаете это на основе интерфейса за интерфейсом.
Instead of doing network statements,|Вместо того, чтобы делать сетевые операторы,
like we're gonna do.|как мы собираемся делать.
And that's another thing.|А это другое дело.
It's still a distance vector ladies and gentlemen.|Это все еще вектор дамы и господа.
It's still a distance vector end protocol.|Это все еще протокол конца вектора расстояния.
I'll get out the way so you can see it.|Я уйду, чтобы ты это увидел.
But, I'm going to write it first.|Но сначала я напишу это.
Because I don't have it full screen.|Потому что у меня нет полноэкранного режима.
I'm, I know I'm so huge that you cant see it.|Я, я знаю, я такой огромный, что ты этого не видишь.
Since it's still a distance vector.|Поскольку это все еще вектор расстояния.
I don't care if it's a hybrid,|Мне все равно, гибрид это ли,
or an advanced distance vector.|или продвинутый вектор расстояния.
It's a distance vector none the less.|Тем не менее, это вектор расстояния.
Cannot forget, and I'll put it in quotes,|Не могу забыть, заключу в кавычки,
no auto-item summary.|нет автозапуска.
You cannot forget that command.|Вы не можете забыть эту команду.
You can't forget that auto-summary command.|Вы не можете забыть эту команду автоматического суммирования.
It's still gonna summarize by default.|По умолчанию он все равно будет подводить итоги.
It's gonna send it to the classful boundary.|Это отправит его к классовой границе.
So you must type no auto-summary in order for it to work, in order for it to work, okay?|Итак, вы не должны вводить автоматическое резюме, чтобы оно работало, чтобы оно работало, хорошо?
You must do that,|Вы должны это сделать,
know you're doing for IP version four.|знаю, что вы делаете для IP версии четыре.
Now, in your examination,|Теперь, на вашем экзамене,
one of the things, and this is more of a test-taking skill or advice that I'm giving you,|одна из вещей, и это скорее навык сдачи теста или совет, который я вам даю,
again based on all the feedback that I get from students that are taking their test.|опять же на основе всех отзывов, которые я получаю от студентов, сдающих тест.
And I've had several students lately,|И в последнее время у меня было несколько учеников,
they have been going out there taking their test.|они ходили туда, чтобы пройти свой тест.
And they, you know,|А они, знаете ли,
send me an email, call me back.|напишите мне, перезвоните мне.
Apparently this is again the routing protocol that Cisco allows.|Судя по всему, это снова тот протокол маршрутизации, который разрешает Cisco.
So apparently this is the simulation that they're running into.|Очевидно, это симуляция, с которой они столкнулись.
It could be different for you, it could be OSPF, it could be RIP version two.|Для вас он может быть другим, это может быть OSPF, это может быть RIP версии два.
But up to now, it's still EIGRP.|Но до сих пор это все еще EIGRP.
Remember, it must be on the same autonomous system number.|Помните, что он должен быть на том же номере автономной системы.
That's number one.|Это номер один.
Number two,|Номер два,
make sure you advertise the networks that are connected to that particular router or routers.|убедитесь, что вы рекламируете сети, которые подключены к этому конкретному маршрутизатору или маршрутизаторам.
You can have a simulation that maybe you have to go into two routers, I don't know.|Вы можете смоделировать, что, возможно, вам придется использовать два маршрутизатора, я не знаю.
So you have to make sure that in each router,|Поэтому вы должны убедиться, что в каждом маршрутизаторе
right, whatever, you read the scenario.|да ладно, вы читаете сценарий.
You have ten minutes per simulation.|У вас есть десять минут на симуляцию.
Read the scenario and make sure that the routers are getting the network that was introduced, or whatever the case may be.|Прочтите сценарий и убедитесь, что маршрутизаторы получают доступ к той сети, которая была представлена, или в любом другом случае.
But it's advertising the correct networks.|Но это реклама правильных сетей.
And then there again,|А потом снова
same autonomous system number.|тот же номер автономной системы.
And it's a classful boundary.|И это классовая граница.
Just like I did the 10.0.0.0 here,|Так же, как я сделал здесь 10.0.0.0,
the same thing you gotta do,|то же самое, что и ты,
if they give you whatever IP scheme.|если они дадут вам любую схему IP.
If it's a class A or a class B, you put in the classful boundary of the address.|Если это класс A или класс B, вы указываете классовую границу адреса.
There's no need to put in the exact network.|Нет необходимости ставить точную сеть.
You put in the classful boundary.|Вы ставите классовую границу.
And this goes out to certain individuals out there that love,|И это касается некоторых людей, которые любят,
or can't you put wildcard mask?|или маску подстановки поставить нельзя?
Yeah, you could.|Да, ты мог бы.
But guess what?|Но знаете что?
You're not.|Ты не.
This is for the CCNA.|Это для CCNA.
Not the CCMP, not the CCIE.|Ни CCMP, ни CCIE.
This is for the CCNA.|Это для CCNA.
They wanna know that you understand that EIGRP will go back to the classful boundaries so that's what you're going to advertise.|Они хотят знать, что вы понимаете, что EIGRP вернется к классовым границам, так что это то, что вы собираетесь рекламировать.
And do not forget the no auto-summary command.|И не забудьте команду no auto-summary.
I cannot stress this enough, because I see a lotta people are making mistakes,|Я не могу это подчеркнуть, потому что вижу, что многие люди делают ошибки,
not only in the classroom,|не только в классе,
because they wanna do something else.|потому что они хотят заняться чем-то другим.
Don't do it.|Не делай этого.
You're gonna advertise the classful boundaries.|Вы собираетесь рекламировать классовые границы.
So the way that I configure it here,|Итак, как я это настроил здесь,
is the way that you need to configure it on your certification.|это способ, которым вам нужно настроить его в вашей сертификации.
All right, once you get to the real world,|Хорошо, как только вы попадете в реальный мир,
once you get to real routers,|как только вы доберетесь до настоящих маршрутизаторов,
depending whatever that company does,|в зависимости от того, что делает эта компания,
that's what you're gonna do.|вот что ты собираешься делать.
Okay, but for now, you're taking this course because you wanna pass the CCNA.|Хорошо, но пока вы идете на этот курс, потому что хотите сдать CCNA.
So you need to do it this way.|Значит, вам нужно сделать это так.
I'm very serious on this.|Я очень серьезно отношусь к этому.
It's very important.|Это очень важно.
I've seen things that it's like,|Я видел такие вещи, как
oh, wow, okay,|о, вау, хорошо,
because again, CCNA specific,|потому что опять же, специфичный для CCNA,
all right, anyway.|ладно, по крайней мере.
So don't forget about the auto-summary command because it is a distance vector.|Так что не забывайте о команде автоматического суммирования, потому что это вектор расстояния.
So administrative distance of EIGRP is what?|Итак, какая административная удаленность EIGRP?
What's the ad?|Что за реклама?
All right I'll write a,|Хорошо, я напишу,
administrative distance, cuz you do have an advertised distance, don't get them confused, administrative distance.|административное расстояние, потому что у вас есть объявленное расстояние, не путайте их, административное расстояние.
And I think I already said a,|И я думаю, что уже сказал,
it a little bit of, it's 90 right,|это немного, это 90 правильно,
the administrative distance of EIGRP is 90.|административное расстояние EIGRP - 90.
Since it's 90, it's gonna override those static routes that we have on there.|Поскольку сейчас 90, он переопределит те статические маршруты, которые у нас есть.
And it's gonna override the RIP routing protocol version 2 or NG cuz that uses 120.|И он переопределит протокол маршрутизации RIP версии 2 или NG, потому что использует 120.
So, EIGRP should take over.|Итак, EIGRP должен взять верх.
All right, so let's go ahead and configure for version four, and see how that looks like.|Хорошо, давайте продолжим настройку для версии четыре и посмотрим, как это будет выглядеть.
All right, we're gonna go ahead and start.|Хорошо, мы продолжим и начнем.
And we're gonna just say network.|И мы просто скажем сеть.
Why and, you know, reinvent the wheel?|Зачем и, знаете ли, велосипед изобретать?
We have IPs already on there for both version six and version four.|У нас уже есть IP-адреса для шестой и четвертой версий.
So, all it is is just configuring the routing protocol.|Итак, все, что вам нужно - это просто настроить протокол маршрутизации.
So let's go to router one,|Итак, перейдем к маршрутизатору один,
right here, okay?|прямо здесь, ладно?
Let's hit Enter a couple of times.|Давайте нажмем Enter пару раз.
[SOUND] So we're gonna go CONFIG T.|[ЗВУК] Итак, мы перейдем к КОНФИГУРАЦИИ T.
And we're gonna go ROUTER.|И мы пойдем на МАРШРУТИЗАТОР.
This is for version four.|Это для версии четыре.
ROUTER EIGRP.|МАРШРУТИЗАТОР EIGRP.
Now we need to pick an autonomous system.|Теперь нам нужно выбрать автономную систему.
Let's leave a question mark just to verify what I said earlier.|Оставим вопросительный знак, чтобы подтвердить то, что я сказал ранее.
So there yeah go, so I'm not wrong.|Итак, да, я не ошибаюсь.
We do have from one to 65,535|У нас есть от одного до 65 535
autonomous system numbers, all right?|номера автономной системы, хорошо?
So we're gonna choose one.|Итак, мы выберем одно.
Let's choose 300, why 300?|Выберем 300, почему 300?
Cuz I like the movie 300, all right?|Потому что мне нравится фильм 300, хорошо?
That's why I chose that.|Вот почему я выбрал это.
So you can choose whatever autonomous system.|Так что вы можете выбрать любую автономную систему.
Obviously, if you're out there in a real world scenario,|Очевидно, что если вы находитесь в реальном мире,
you wanna organize it a certain way.|вы хотите организовать это определенным образом.
You pick your numbering scheme,|Вы выбираете свою схему нумерации,
it's up to you, all right?|решать тебе, хорошо?
So ROUTER EIGRP 300.|Итак, ROUTER EIGRP 300.
Network, not NEY, network 10.0.0.0.|Сеть, а не НЕЙ, сеть 10.0.0.0.
Same thing.|То же самое.
Network 192.168.1.0 and the famous no auto-summary.|Сеть 192.168.1.0 и знаменитая без автосводки.
DO WR.|DO WR.
Let's go ahead and do that here now for the second router.|Давайте продолжим и сделаем это сейчас для второго маршрутизатора.
Spread this bad boy right up here.|Распространите этого плохого парня прямо здесь.
Now, you can see that.|Теперь вы это видите.
CONFIG T, ROUTER EIGRP 300,|КОНФИГ Т, МАРШРУТИЗАТОР EIGRP 300,
same autonomous system.|та же автономная система.
Network 10.0.0.0.|Сеть 10.0.0.0.
Well, look at that, we found the neighbor.|Что ж, посмотри, мы нашли соседа.
Automa, look at how quick it converts.|Автома, посмотрите, как быстро конвертирует.
Right there in there say,|Прямо там говорят,
hey I know, I know you, okay?|эй, я знаю, я знаю тебя, хорошо?
And now we're gonna go ahead and do the next one.|А теперь мы продолжим и сделаем следующий.
Network 192.168.2.0 and then no auto-item summary.|Сеть 192.168.2.0, а затем без сводки автоматических элементов.
Once we do that, guess what?|Как только мы это сделаем, угадайте, что?
Again, because we recalculate, because we're operating on auto-summary, it says,|Опять же, потому что мы пересчитываем, потому что мы работаем с автоматическим суммированием, он говорит:
okay, well I have neighbors.|хорошо, у меня есть соседи.
That are in the ten but we actually now with an no auto-summary, boom,|Это входит в десятку, но на самом деле у нас сейчас нет автосводки, бум,
it faces a certain way, all right?|он смотрит в определенную сторону, хорошо?
We'll do the WR cuz those are the only two networks there, right?|Мы сделаем WR, потому что это единственные две сети, верно?
It really is three but again, classful boundary.|Это действительно три, но опять же классовая граница.
And then we do the last one.|А потом делаем последнее.
You may be enable Cisco,|Вы можете включить Cisco,
and then we do CONFIG T and then we're gonna do ROUTER EIGRP 300.|Затем мы выполняем CONFIG T, а затем выполняем ROUTER EIGRP 300.
Network 10.0.0.0.|Сеть 10.0.0.0.
Oh, look at that, found that already.|О, посмотрите на это, это уже обнаружено.
Network 192.168.3.0.|Сеть 192.168.3.0.
Ooh, that's not 30, 3.0.|Ох, это не 30, 3.0.
No auto-summary, do WR.|Нет автосводки, сделай WR.
From right here let's take a look at the show IP route.|Отсюда давайте взглянем на показанный IP-маршрут.
Let's take a look at the routing table.|Взглянем на таблицу маршрутизации.
Hey look at that, now we got these.|Эй, посмотри на это, теперь у нас есть это.
We got D's for the 10.1.1.4.|У нас есть D для 10.1.1.4.
We got a D for 1.0 network.|Мы получили D за сеть 1.0.
We got D for the 1, for the 2.0 network.|Мы получили D для 1 для сети 2.0.
Outstanding, there's the administrative distance.|Замечательно, есть административное расстояние.
There's my metric, right here.|Вот моя метрика, вот здесь.
Okay, and I'm learning it again via the 10.1.1.9,|Хорошо, я снова изучаю это через 10.1.1.9,
which is the neighbor over here on my 0.0.1.|который является соседом по моей версии 0.0.1.
So you read it the same, but now it's D.|Итак, вы читаете то же самое, но теперь это Д.
What does D stand for?|Что означает D?
Dual.|Двойной.
If you don't know,|Если ты не знаешь,
take a look at this right here.|взгляните на это прямо здесь.
It'll tell you D, EIGRP.|Он скажет вам D, EIGRP.
Why not E?|Почему не Е?
Because D means dual, they decided on D.|Поскольку D означает двойное, они выбрали D.
That's, hey, that's, you gotta know.|Это, эй, это ты должен знать.
D is E I G R P because of the algorithm.|D - это E I G R P из-за алгоритма.
So there you go, we have connectivity now.|Итак, теперь у нас есть возможность подключения.
And it took over because of the administrative distance.|И это произошло из-за административной удаленности.
You see how important that administrative distance is?|Вы видите, насколько важна эта административная дистанция?
Because again, when I do my task list,|Потому что снова, когда я делаю свой список задач,
one of the things I put on there, it'll run in these three routing protocols.|одна из вещей, которые я поставил там, это будет работать в этих трех протоколах маршрутизации.
You know, and I'll throw in some metrics,|Знаешь, я добавлю несколько показателей,
and I'll throw in some hop counts and things like that and cost values,|и я добавлю количество прыжков и тому подобное, а также значения стоимости,
just to throw it off.|просто скинуть.
Who will make it to the routing table?|Кто попадет в таблицу маршрутизации?
Well, the metrics or the hop counts or the costs for OSPF have nothing to do,|Что ж, ни метрики, ни количество переходов, ни затраты на OSPF не имеют никакого отношения,
or has nothing to do with who's gonna make it to the routing table based on the routing protocol.|или не имеет никакого отношения к тому, кто попадет в таблицу маршрутизации на основе протокола маршрутизации.
It is the administrative distance of the routing protocol that says you're going to the routing table.|Это административное расстояние протокола маршрутизации, которое говорит о том, что вы переходите к таблице маршрутизации.
And you could control that,|И ты мог это контролировать,
you can change the administrative distance of a particular routing protocol.|вы можете изменить административное расстояние определенного протокола маршрутизации.
Again, it's completely up to you.|Опять же, это полностью зависит от вас.
So you see that configuration's very,|Итак, вы видите, что эта конфигурация очень,
very simple.|очень просто.
Now, what's, we need to understand and get familiarized with is show IP,|Теперь, что нам нужно понять и изучить, это показать IP,
EIGRP TOPOLOGY.|ТОПОЛОГИЯ EIGRP.
This is what we need to know.|Это то, что нам нужно знать.
All the networks are there, okay?|Все сети есть, хорошо?
There is your feasible distance to each particular network, all right?|Есть ваше допустимое расстояние до каждой конкретной сети, хорошо?
You see right there the 856,|Вы видите здесь 856,
and they're the same.|и они такие же.
You see that there's no,|Вы видите, что нет,
not one network that's two routes,|не одна сеть, а два маршрута,
because there's only one way to get across.|потому что есть только один способ перейти.
There's only one way to get across.|Есть только один способ перебраться.
So you're not gonna have two.|Так что двоих у тебя не будет.
In order to have that,|Для этого
we would have to have,|мы должны были бы иметь
let's say, a redundant link coming back.|скажем, возвращается избыточная ссылка.
But you can, you know, if you have those redundant links, you could then go inside the interface and change the bandwidth and|Но вы можете, знаете ли, если у вас есть эти избыточные ссылки, вы могли бы затем войти в интерфейс и изменить пропускную способность и
force it to where you want it to go.|заставьте его туда, куда вы хотите.
All right, okay?|Ладно ладно?
So there's EIGRP for version four.|Итак, для четвертой версии есть протокол EIGRP.
Can we ping across?|Мы можем пинговать?
Let's bring up a PC, and let's find out.|Давайте возьмем компьютер, и давайте узнаем.
Come on PC, come over here, there you go.|Заходи на ПК, иди сюда, поехали.
Good PC, all right?|Хороший компьютер, понятно?
And lets, lets ping, again,|И давай, давай снова пингуем,
the version four address.|адрес версии четыре.
192.168.3.254, that is the default gateway right here, the, 00.|192.168.3.254, это шлюз по умолчанию прямо здесь, 00.
Let's pi, let's see if we can ping the actual IP version four address.|Давай пи, посмотрим, сможем ли мы пропинговать фактический IP-адрес четвертой версии.
Now of course, ARP, right?|Теперь, конечно, ARP, правда?
We missed that one time.|Мы пропустили это однажды.
Boop, now we got it.|Буп, теперь мы его получили.
We can ping all the way across.|Мы можем пинговать всю дорогу.
Let's do it again,|Давай сделаем это снова,
just to get the four replies.|просто чтобы получить четыре ответа.
Awesome, and we're doing it via,|Отлично, и мы делаем это через
okay, EIGRP.|хорошо, EIGRP.
Let's take a look at here.|Давайте посмотрим здесь.
We can see that the neighbors that it starts the end there, Ctrl+Z.|Мы видим, что у соседей, что она начинается, конец там Ctrl + Z.
Show IP ROUTE, and you see that this one also has all these.|Покажите IP-МАРШРУТ, и вы увидите, что у этого тоже есть все это.
Learning about the two, learning about the three, learning about the eight.|Узнавать о двух, узнавать о трех, узнавать о восьми.
And again, the administrative distance,|И снова административная дистанция,
the 90, the metric that it's using.|90, метрика, которую он использует.
And you see it's the same, because we have a straight line going across.|И вы видите, что это то же самое, потому что у нас проходит прямая линия.
That's not gonna change.|Это не изменится.
Now let's configure EIGRP for version six.|Теперь давайте настроим EIGRP для шестой версии.
Now we have everything in place.|Теперь у нас все на месте.
Now one of the first things I said for version six that we need to do is turn on IPv6, unicast routing.|Теперь одно из первых вещей, которые я сказал для версии 6, что нам нужно сделать, это включить IPv6, одноадресную маршрутизацию.
That's already there, so we don't need do it because we did it earlier when we did RIP.|Это уже есть, поэтому нам не нужно этого делать, потому что мы сделали это раньше, когда делали RIP.
So all we really need to do is go inside the interface.|Так что все, что нам действительно нужно сделать, это зайти внутрь интерфейса.
But wait, the first one,|Но подождите, первый,
let's do it the long way.|давай сделаем это долгим путем.
Because with EIGRP, there's a couple things that you do need to do,|Потому что с EIGRP вам нужно сделать несколько вещей,
and I'll show you.|и я вам покажу.
CONFIG T, again,|CONFIG T, опять же,
we have to do IPV6 ROUTER EIGRP.|мы должны сделать IPV6 ROUTER EIGRP.
And let's use something different.|А давайте воспользуемся чем-нибудь другим.
Let's use [COUGH] 100, All right?|Давайте использовать [КАШЕ] 100, хорошо?
Now if I did a question mark,|Если бы я поставил вопросительный знак,
there's two things.|есть две вещи.
All right, so, we,|Хорошо, так что мы,
we did the IPV6 ROUTER EIGRP 100.|мы сделали IPV6 ROUTER EIGRP 100.
We know we're gonna use the autonomous system 100.|Мы знаем, что будем использовать автономную систему 100.
But now we have these two commands down here, router-id and shutdown.|Но теперь у нас есть две команды: router-id и shutdown.
You see that the router-id is for this EIGRP process.|Вы видите, что идентификатор маршрутизатора предназначен для этого процесса EIGRP.
This is something new.|Это что-то новенькое.
This is, this router-id,|Это идентификатор маршрутизатора,
which is based on IPv4 addresses,|который основан на адресах IPv4,
you have to use the IPv4 address format,|вы должны использовать формат адреса IPv4,
is for the protocol instance.|для экземпляра протокола.
That's what it's called.|Так это называется.
All right?|Отлично?
A protocol instance, a process for this particular EIGRP.|Экземпляр протокола, процесс для этого конкретного EIGRP.
You must put it in there.|Вы должны положить это туда.
You must put it in there.|Вы должны положить это туда.
And then you must turn on the protocol.|И тогда вы должны включить протокол.
You must turn on the protocol.|Вы должны включить протокол.
So, we'll go ahead and do, Router-id.|Итак, мы продолжим и сделаем, Router-id.
This is router 1, so I'll use that router-id.|Это маршрутизатор 1, поэтому я буду использовать этот идентификатор маршрутизатора.
And then I will do a NO SHUT.|И тогда я НЕ ЗАКЛЮЧАЮСЬ.
Done, all right, at least there.|Готово, хорошо, по крайней мере, есть.
But now, I need to go into the interface,|Но теперь мне нужно войти в интерфейс,
interface F0/0 and then enable that.|интерфейс F0 / 0, а затем включите его.
IPV6 EIGRP, what is it?|IPV6 EIGRP, что это?
100.|100.
And then go to INT S0/0/0.|Затем перейдите к INT S0 / 0/0.
IPV6, I'm just going to up arrow, 100.|IPV6, я просто на стрелку вверх, 100.
So I enabled that autonomous system,|Итак, я включил эту автономную систему,
on those two interfaces.|на этих двух интерфейсах.
And we're gonna do the same thing on the other routers.|И мы сделаем то же самое с другими маршрутизаторами.
Let me save this, DO WR.|Позвольте мне сохранить это, DO WR.
All right, let's exit one time.|Хорошо, давайте выйдем один раз.
ROUTER, oh, I'm sorry,|МАРШРУТИЗАТОР, извини,
IPV6 ROUTER EIGRP, E-I-G-R-P 100.|IPV6 МАРШРУТИЗАТОР EIGRP, E-I-G-R-P 100.
Router-id, I'm just gonna do everything the same just for quickness sake.|Идентификатор роутера, я просто сделаю все то же самое, просто для быстроты.
And then NO SHUT.|А потом НЕ ЗАКРЫТЬ.
Now I'm gonna go into the interface S0/0/1, Enter.|Теперь зайду в интерфейс S0 / 0/1, Enter.
I'm gonna do IPV6 EIGRP 100,|Я сделаю IPV6 EIGRP 100,
build a new adjacency.|построить новую смежность.
So, and then F0/0.|Итак, а затем F0 / 0.
All right, so if you look at it,|Хорошо, так что если вы посмотрите на это,
let's take a look at the start.|давайте посмотрим на начало.
Show START.|Показать СТАРТ.
And let me do a DO WR, I'm sorry, do a DO WR, or WR, so you can look at the start.|И позвольте мне сделать DO WR, извините, сделать DO WR или WR, чтобы вы могли посмотреть в начале.
And now to do a show run, but we know the difference, right?|А теперь поехать на показ, но мы знаем разницу, правда?
You should know the difference.|Вы должны знать разницу.
All right,|Отлично,
let's take a look at the routing protocol.|давайте посмотрим на протокол маршрутизации.
You see the interfaces.|Вы видите интерфейсы.
You have ipv6, rip 1 enable, but you also have ipv6 eigrp 100.|У вас есть ipv6, rip 1 enable, но у вас также есть ipv6 eigrp 100.
So, who is going to take over?|Итак, кто возьмется за дело?
You saw that recreated when you saw it came up, right?|Вы видели это воссозданным, когда видели, как оно появилось, верно?
Before, so okay, so that's in there, awesome, awesome.|Раньше, так хорошо, так что это там, круто, круто.
And there's router EIGRP.|И есть роутер EIGRP.
For version four, and then there's IPv6 router EIGRP 100,|Для версии четыре, а также есть маршрутизатор IPv6 EIGRP 100,
with a router ID and no shut down,|с идентификатором маршрутизатора и без выключения,
meaning it's turned on.|это означает, что он включен.
All right, and that was,|Хорошо, и это было,
what router is this?|что это за роутер?
Router 2.|Маршрутизатор 2.
Let's go to the last router,|Переходим к последнему роутеру,
and, we do the same thing.|и мы делаем то же самое.
CONFIG T, IPV6 ROUTER,|КОНФИГ Т, МАРШРУТИЗАТОР IPV6,
EIGRP 100.|EIGRP 100.
Router ID 1.1.1.1 and then NO SHUT.|Идентификатор маршрутизатора 1.1.1.1, а затем NO SHUT.
All right, to turn on the routing protocol interface, let's do the LAN first F0/0.|Хорошо, чтобы включить интерфейс протокола маршрутизации, давайте сначала сделаем LAN F0 / 0.
Why?|Зачем?
Cuz I want to get that adjacency to pop up.|Потому что я хочу, чтобы эта смежность всплыла.
[NOISE] IPv6, EIGRP 100, and then interface, 0/0/1.|[NOISE] IPv6, EIGRP 100, а затем интерфейс, 0/0/1.
IPv6 HRP 100, boom.|IPv6 HRP 100, бум.
Adjacency, Ctrl+Z, WR and if I wanted to take a look at the routing protocol, I meant the routing table.|Смежность, Ctrl + Z, WR, и если я хотел взглянуть на протокол маршрутизации, я имел в виду таблицу маршрутизации.
SH IPV6 ROUTE.|SH МАРШРУТ IPV6.
Now who do we have?|Теперь кто у нас есть?
Now we have D.|Теперь у нас есть Д.
Just like same thing that happened in IPv4.|Точно так же, как и в IPv4.
We have the D in there, okay, for IPv6.|Хорошо, у нас есть буква D для IPv6.
Right, we're learning about the 1000,|Правильно, мы узнаем о 1000,
the 1100,|1100,
we're learning about the 1300, and that should be it right there.|мы узнаем о 1300, и это должно быть прямо здесь.
All right, so, there you go, we have three routers running static routes as backup,|Хорошо, итак, у нас есть три маршрутизатора, использующие статические маршруты в качестве резервных,
a RIP running protocol, so if EIGRP goes bad, RIP will take over.|протокол выполнения RIP, поэтому, если EIGRP выходит из строя, RIP берет на себя.
All right, and if that goes bad, we have static routes that are gonna take over with the default routes and the stubs.|Хорошо, и если что-то пойдет не так, у нас есть статические маршруты, которые заменят маршруты по умолчанию и заглушки.
You see that, now obviously you're not gonna do this in the real world.|Вы видите это, теперь очевидно, что вы не собираетесь делать это в реальном мире.
You're not gonna create three routing protocols or two routing protocols as backups because you have those algorithms that are calculating and|Вы не собираетесь создавать три протокола маршрутизации или два протокола маршрутизации в качестве резервных копий, потому что у вас есть те алгоритмы, которые рассчитывают и
you don't want that to happen because you're burn the router too much,|вы не хотите, чтобы это произошло, потому что вы слишком сильно сжигаете роутер,
the processing of the router, right.|обработка роутера, верно.
Not that RIP really does a lot of processing in there, but EIGRP is making a lot of calculations.|Не то чтобы RIP действительно много там обрабатывает, но EIGRP выполняет много вычислений.
Not as much as OSPF, but it is doing it's calculations.|Не так много, как OSPF, но он выполняет свои вычисления.
Looking at the topology table.|Смотрим на таблицу топологии.
Creating that topology table.|Создание этой таблицы топологии.
Creating SH IP EIGRP NEI,|Создание SH IP EIGRP NEI,
for the neighbor.|для соседа.
Hey, there's my IP version four neighbor,|Эй, это мой сосед по IP версии четыре,
right?|право?
Now, don't worry too much about, like,|Теперь не беспокойтесь слишком сильно о, например,
this, like this right here,|вот так вот здесь,
the return trip timer, right?|таймер обратного пути, верно?
How long it took, or the smooth, round, trip timer.|Сколько времени это заняло, или плавный таймер туда и обратно.
How long did it take it to get around the network.|Сколько времени понадобилось, чтобы обойти сеть.
And you can see it's milliseconds right here, it didn't take that long.|И вы можете видеть миллисекунды прямо здесь, это не заняло так много времени.
It's a very small network.|Это очень маленькая сеть.
So, but know that it's, hey, it's learning about your neighbors right here.|Так что, но знайте, что это, эй, это изучение ваших соседей прямо здесь.
Okay, learning about your neighbors.|Хорошо, узнаю о своих соседях.
So this is important things.|Так что это важные вещи.
Do you need to know these commands?|Вам нужно знать эти команды?
Sure, sure.|Конечно конечно.
Show IP EIGRP neighbors, show IP EIGRP topology even more important.|Показать IP EIGRP соседей, еще более важно показать топологию IP EIGRP.
Because guarantee you,|Потому что гарантирую вам,
guarantee you you're gonna end up here.|гарантирую, что вы окажетесь здесь.
And just do topology.|И вобще топологию.
I guarantee you, cuz I would do it on my exam, you will get a print,|Я гарантирую вам, потому что я сделаю это на экзамене, вы получите распечатку,
print screen that looks something like this on the topology table.|напечатайте экран, который выглядит примерно так в таблице топологии.
You need to make sure that, hey,|Вы должны убедиться, что, эй,
passive, good to go, all right.|пассивный, хорошо, хорошо.
Found all the routes.|Нашел все маршруты.
I'm not actively looking for anything.|Я ничего активно не ищу.
If I were to change this,|Если бы я изменил это,
let's say I were to put it in word,|скажем, я должен был выразить это словами,
change it to active, do some different metrics, whatever change it around,|измените его на активный, сделайте несколько других показателей, что бы это ни изменилось,
means it's still actively looking,|означает, что он все еще активно ищет,
we still haven't fully converged.|мы еще не полностью сошлись.
Okay.|Ладно.
So that's the problem is that it's active,|Так вот проблема в том, что он активен,
okay.|Ладно.
And again, it will cuz it will query,|И снова, он будет запрашивать,
if our line goes down.|если наша линия выйдет из строя.
And this will have redundant links to it.|И это будет иметь избыточные ссылки на него.
It will query the topology table looking for feasible successor.|Он запросит таблицу топологии в поисках возможного преемника.
If a feasible successor even exists,|Если возможный преемник вообще существует,
because feasible successors have to qualify, have to qualify to be a feasible successor.|потому что возможные преемники должны соответствовать критериям, должны соответствовать требованиям, чтобы стать возможным преемником.
All right?|Отлично?
So that's the EIGRP.|Итак, это EIGRP.
That's the EIGRP.|Это EIGRP.
What do you need to remember?|Что нужно помнить?
Hey, the terminology on what a feasible successor, feasible distance,|Эй, терминология о том, какой возможный преемник, допустимое расстояние,
advertise distance and the,|рекламировать расстояние и
successor, routes are.|преемник, маршруты есть.
Know that the feasible successors are backup routes.|Знайте, что возможные преемники - это резервные пути.
Know that your successor routes are the ones in the routing table.|Знайте, что ваши последующие маршруты - это те, которые указаны в таблице маршрутизации.
Know your K-values.|Знайте свои K-ценности.
Know the fact that you have to have the same autonomous system number across each and every router for the certification.|Помните, что для сертификации у вас должен быть один и тот же номер автономной системы на каждом маршрутизаторе.
Real world, different story.|Реальный мир, другая история.
We're not talking about real world.|Мы не говорим о реальном мире.
We're talking about in a certification.|Мы говорим о сертификации.
If you have a small network in a real world scenario,|Если у вас небольшая сеть в реальном мире,
yeah you can have the same autonomous system.|да, у вас может быть такая же автономная система.
Not a big deal.|Не так уж и важно.
But as you grow and you expand and you're, you know,|Но по мере того, как вы растете и расширяетесь, вы знаете,
you're branching out to different counties, different states.|вы переходите в разные округа, разные штаты.
Then you may want to start doing multiple autonomous systems.|Тогда вы можете захотеть создать несколько автономных систем.
But other than that using, you know,|Но кроме этого, вы знаете,
small networks with a single autonomous system, you're not going to kill anything.|небольшие сети с единственной автономной системой, вы ничего не убьете.
All right, but these are things that you need to be concerned with.|Хорошо, но это вещи, о которых вам нужно позаботиться.
All right, these are the things.|Ладно, вот такие вещи.
The range of the autonomous listings.|Диапазон автономных объявлений.
The summary that you're going to type,|Резюме, которое вы собираетесь напечатать,
that you're going to advertise the class full boundary.|что вы собираетесь рекламировать полную границу класса.
And one last thought,|И последняя мысль,
one last thing, okay?|последнее, хорошо?
Just in case.|На всякий случай.
Just in case, and if you can't see it because as I'm typing it,|На всякий случай, и если вы его не видите, потому что, когда я его печатаю,
I'll move out of the way.|Я уйду с дороги.
The PASSIVE-INTERFACE,|ПАССИВНЫЙ ИНТЕРФЕЙС,
and then the INTERFACE, I'm just gonna put whatever, that one right there.|а затем ИНТЕРФЕЙС, я просто положу что угодно, вот это прямо здесь.
If for whatever reason on an examination,|Если по какой-либо причине на экзамене
school, wherever, okay.|школа, где угодно, ладно.
You see this but it's pointing to an interface let's say that's going out to the internet.|Вы видите это, но он указывает на интерфейс, допустим, выходящий в Интернет.
Don't worry about it.|Не беспокойся об этом.
You don't want EIGRP to send out updates out to the internet.|Вы не хотите, чтобы EIGRP рассылал обновления в Интернет.
Now if this PASSIVE-INTERFACE,|Теперь, если этот ПАССИВНЫЙ ИНТЕРФЕЙС,
it's pointing to an interface that's two networks within,|он указывает на интерфейс, внутри которого находятся две сети,
internally, all right?|внутренне все в порядке?
That you want these routers to know about these networks.|Что вы хотите, чтобы маршрутизаторы знали об этих сетях.
Then that's a problem, then you will need to go inside the router EIGRP or IPv6 router, EIGRP,|Тогда это проблема, тогда вам нужно будет зайти внутрь маршрутизатора EIGRP или маршрутизатора IPv6, EIGRP,
whatever autonomous system it is, and put no PASSIVE-INTERFACE,|какая бы автономная система ни была, и не ставьте ПАССИВНЫЙ ИНТЕРФЕЙС,
whatever interface that they're using.|какой бы интерфейс они ни использовали.
But if it's pointing to an ISP,|Но если он указывает на интернет-провайдера,
if it's pointing outside the network,|если он указывает за пределы сети,
don't worry about it.|не беспокойтесь об этом.
One of the things in your certification or your exams that you do in your schools,|Одна из вещей в вашей сертификации или экзаменах, которые вы делаете в своих школах,
when it's a hands on thing and you're dealing with routing,|когда дело касается рук, и вы имеете дело с маршрутизацией,
make sure you can ping.|убедитесь, что вы можете пинговать.
You sit on one router and you start trying to ping the others.|Вы садитесь на один роутер и начинаете пытаться пинговать остальные.
If you can ping every router, from where you're at, then you don't have a problem.|Если вы можете пинговать каждый маршрутизатор, где бы вы ни находились, у вас нет проблем.
If you can't, then you better fix it.|Если не можете, то лучше исправьте.
Now remember in your certification,|Теперь помните в своей сертификации,
you got ten minutes for simulation.|у тебя есть десять минут на симуляцию.
But once you hit that Next button,|Но как только вы нажмете кнопку "Далее",
you're done.|все готово.
You're not coming back to that question again.|Вы больше не вернетесь к этому вопросу.
So you gotta make sure that you can ping.|Так что вы должны убедиться, что можете пинговать.
And now, what I'm telling you now is, make sure you're in the same autonomous system,|А теперь я говорю вам: убедитесь, что вы находитесь в той же автономной системе,
make you sure you advertise the class full boundaries, all right?|Убедитесь, что вы рекламируете полные границы класса, хорошо?
Remember, when you're doing dynamic routing,|Помните, когда вы выполняете динамическую маршрутизацию,
you advertise the networks that you are connected to.|вы рекламируете сети, к которым вы подключены.
The advertising networks that you are connected to.|Рекламные сети, к которым вы подключены.
And it's the classful boundary network.|И это классовая пограничная сеть.
Just like we do with the class A,|Как и в случае с классом A,
tangible zero,|осязаемый ноль,
the things we put in individual networks.|вещи, которые мы помещаем в отдельные сети.
That's the same thing you would do.|Вы поступили бы так же.
All right.|Отлично.
So make sure you do that.|Так что убедитесь, что вы это делаете.
Same autonomous system and advertising classful boundary.|Та же автономная система и классовая граница рекламы.
And please, again, once again.|И, пожалуйста, еще раз.
Do not forget the no auto summary.|Не забывайте об автореферате.
Okay, all right.|Ладно, ладно.
There's EIGRP,|Есть EIGRP,
it's not difficult to configure.|настроить не сложно.
Just remember those three things that I just told you about.|Просто запомните те три вещи, о которых я вам только что рассказал.
All right, oh, and yes, PASSIVE-INTERFACE.|Ладно, да, ПАССИВНЫЙ ИНТЕРФЕЙС.
If it's going out to the internet,|Если он выходит в Интернет,
forget about it.|забудь об этом.
If it's facing internally then you take it out, you go inside the EIGRP process,|Если он обращен внутрь, вы вынимаете его, вы входите в процесс EIGRP,
or router EIGRP, whichever version six or four, you just put a no.|или маршрутизатора EIGRP, в зависимости от версии шесть или четыре, вы просто указываете нет.
No passive interface or whatever it is,|Нет пассивного интерфейса или чего-то еще,
and you'll be just fine, okay?|и с тобой все будет хорошо, ладно?
All right, ladies and gentleman,|Хорошо, дамы и господа,
that's the end of this lesson.|это конец этого урока.
I'll see you in the next one.|Увидимся в следующем.