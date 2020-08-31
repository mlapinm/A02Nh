D:\mailCloud\prjother\tmp\1\c68_what type of routing should I use.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
All right, we're back.|Хорошо, мы вернулись.
And we're back for what?|И для чего мы вернулись?
It's time to make a decision.|Пора принимать решение.
What type of routing should we use?|Какой тип маршрутизации мы должны использовать?
Should we use static routing?|Стоит ли использовать статическую маршрутизацию?
Or should we use dynamic routing?|Или стоит использовать динамическую маршрутизацию?
What are the differences?|Какие отличия?
In this example, sounds like a real,|В этом примере звучит как настоящий,
right, like a real classroom.|да, как в настоящем классе.
In this example, right.|В этом примере верно.
And we're going to be back to use static routing.|И мы вернемся к использованию статической маршрутизации.
What are, what are the benefits of static routing?|Каковы преимущества статической маршрутизации?
Static routing puts no overhead on your router.|Статическая маршрутизация не увеличивает нагрузку на ваш маршрутизатор.
Your CPU is not being burdened with these algorithms and calculations and all that.|Ваш процессор не перегружен этими алгоритмами, вычислениями и прочим.
You're the one that's putting the static routes on there, right?|Вы же ставите там статические маршруты, верно?
So it doesn't have to think.|Так что не надо думать.
There's no updates being sent out on every so often, right?|Обновления не рассылаются так часто, верно?
So, security-wise, bandwidth-wise,|Итак, с точки зрения безопасности и пропускной способности,
it, it, it in, in, ma, makes it a lot better, okay?|это, это, это в, в, ма, делает это намного лучше, хорошо?
Security, bandwidth, overhead and processing.|Безопасность, пропускная способность, накладные расходы и обработка.
But as far as for yourself, but, I mean that would be the benefit, but as far as for yourself, you need to make sure that you keep track.|Но что касается вас самих, но, я имею в виду, что это было бы преимуществом, но что касается вас, вы должны следить за тем, чтобы отслеживать.
So that will be, I guess, maybe, if you want to call it a disadvantage, or job security, one or the others.|Так что это будет, я думаю, может быть, если вы хотите назвать это недостатком или безопасностью работы, одним или другим.
All right, because you need to maintain subnets that you put in, or subnets that you take out.|Хорошо, потому что вам нужно поддерживать подсети, которые вы вставляете, или подсети, которые вы удаляете.
Because you need to update every static routing table.|Потому что вам нужно обновить каждую статическую таблицу маршрутизации.
Small network like this, it wouldn't be a big deal.|Такая маленькая сеть, это не будет большим делом.
And what number did we decide?|А какое количество мы решили?
Is there a number?|Есть номер?
I've never seen a number.|Я никогда не видел числа.
So, I can tell you from my experience, my real world experience,|Итак, я могу сказать вам по своему опыту, моему опыту в реальном мире,
schools, campuses, seven campuses.|школы, кампусы, семь кампусов.
Each campus had two routers.|В каждом кампусе было по два маршрутизатора.
But the two routers were really,|Но два роутера действительно были
they were two different subnets, that weren't being routed internally.|это были две разные подсети, которые не маршрутизировались внутри.
It was just going somewhere else.|Он просто собирался куда-то еще.
Right, they had their own T1 connections.|Да, у них были свои собственные соединения T1.
Anyway, the routing tables were small.|Так или иначе, таблицы маршрутизации были небольшими.
They weren't that big.|Они не были такими уж большими.
So it was easy to maintain.|Так что было легко поддерживать.
You had an IT person on campus.|В кампусе у вас был ИТ-специалист.
It wasn't that difficult.|Это было не так уж сложно.
But, as that particular college grew, and grow it did.|Но по мере того, как этот конкретный колледж рос, он рос и рос.
All right.|Отлично.
Then definitely they have to change to something else.|Тогда определенно они должны перейти на что-то другое.
I don't know what they are doing now.|Я не знаю, что они сейчас делают.
But, I can assure you that it's not static routing.|Но могу вас уверить, что это не статическая маршрутизация.
But, again, being in telecommunications,|Но, опять же, в сфере телекоммуникаций,
where you have, you know, over 11,|где у вас, знаете ли, старше 11 лет,
12, 13, 15,000 sites that are point to point, you do static routes.|12, 13, 15 000 сайтов точка-точка, вы делаете статические маршруты.
So, backbone routers, but anyway I'm getting off, getting of the topic.|Итак, магистральные маршрутизаторы, но в любом случае я выхожу из темы.
Static routes are okay for small,|Статические маршруты подходят для небольших,
medium-sized networks.|сети среднего размера.
They're easier to configure.|Их проще настроить.
Something quick, hey, you know, [SOUND],|Что-нибудь быстрое, эй, [ЗВУК],
and get it done, all right.|и сделай это, хорошо.
But again, it's a burden on you,|Но опять же, это бремя для тебя,
depending on how many subnets your router doesn't know about.|в зависимости от того, сколько подсетей не знает ваш маршрутизатор.
Remember, when you do static routes, you gotta tell this router,|Помните, когда вы выполняете статические маршруты, вы должны сообщить этому маршрутизатору,
because routers only know who they're connected to directly so this router knows about the 10.1.1.4|потому что маршрутизаторы знают только, к кому они подключены напрямую, поэтому этот маршрутизатор знает о 10.1.1.4
network and knows about the 192.168.1.0.|сеть и знает о 192.168.1.0.
That's it.|Вот и все.
You gotta tell the router hey there's a 2.0 a, a, 10.1.1.8 and a 3.0, all right, so static routes, again,|Вы должны сказать маршрутизатору, что есть 2.0 a, a, 10.1.1.8 и 3.0, хорошо, так что статические маршруты, опять же,
I would say just to give it a number,|Я бы сказал просто дать ему номер,
no more than 10 routers, and depending on the amount of subnets you have in there.|не более 10 роутеров, и в зависимости от количества подсетей, которые у вас есть.
Okay?|Ладно?
And if you're suffering from bandwidth issues, definitely, maybe a static route will help you.|И если вы страдаете от проблем с пропускной способностью, возможно, вам поможет статический маршрут.
Okay, so static routes could be a good idea now.|Хорошо, статические маршруты теперь могут быть хорошей идеей.
But what about dynamic routing?|А как насчет динамической маршрутизации?
And then when you think about dynamic routing.|А потом, когда вы думаете о динамической маршрутизации.
Okay, so when you think about dynamic routing, you've got algorithms that are gonna calculate a certain path to the network, to the destinations, I'm sorry.|Итак, когда вы думаете о динамической маршрутизации, у вас есть алгоритмы, которые будут вычислять определенный путь к сети, к пунктам назначения, извините.
You have updates that get sent out, or triggered updates.|У вас есть рассылаемые обновления или запускаемые обновления.
It all depends on the routing protocol.|Все зависит от протокола маршрутизации.
So now you've got another decision.|Итак, теперь у вас есть другое решение.
Okay, I'm going to use dynamic routing gentle, ladies and gentleman.|Хорошо, дамы и господа, я собираюсь использовать динамическую маршрутизацию.
That's the way we're gonna go.|Вот так мы и пойдем.
Well, I have a question.|Что ж, у меня вопрос.
Which dynamic routing protocol are we going to use?|Какой протокол динамической маршрутизации мы будем использовать?
Are we going to use RIP version two, are we going to use EIDRP,|Собираемся ли мы использовать RIP версии два, собираемся ли мы использовать EIDRP,
are we going to us RSPF?|мы едем к нам в РФПФ?
Now why do I mention only those three?|Почему я упомянул только эти три?
Because those are the ones you're being tested on.|Потому что это те, на которых вы проходите испытания.
Are there more?|Есть еще?
Sure, there's ISIS, there's BGP.|Конечно, есть ISIS, есть BGP.
All right, we start getting into the other levels of certifications when to apply them, where to apply them, and how, but we|Хорошо, мы начинаем переходить на другие уровни сертификации, когда их применять, где применять и как, но мы
don't care about that right now.|не волнуйтесь об этом прямо сейчас.
We're trying to get the CCNA, so you need to make a decision which routing protocol obviously RIP here,|Мы пытаемся получить CCNA, поэтому вам нужно решить, какой протокол маршрутизации здесь явно RIP,
small network, but what would be the disadvantage of RIP version two?|небольшая сеть, но в чем будет недостаток второй версии RIP?
That every 30 seconds distance vector sends out the,|Каждые 30 секунд вектор расстояния отправляет
its updates even though you already know that you have fully converged.|его обновления, даже если вы уже знаете, что полностью сошлись.
We all know about each other's routing tables, but every 30 seconds RIP is still gonna send you the full routing table.|Все мы знаем о таблицах маршрутизации друг друга, но каждые 30 секунд RIP все равно будет отправлять вам полную таблицу маршрутизации.
Or the four, in the, in the updates.|Или четыре, в, в обновлениях.
So, it's taking up your bandwidth, and if you're, you know, even if you,|Итак, это занимает вашу полосу пропускания, и если вы, знаете, даже если вы,
you have a massive T1 line, you know, and you have a lot of traffic going through there, that could be a, a problem.|у вас есть огромная линия T1, и у вас много трафика, что может быть проблемой.
Can you tweak those timers?|Можете ли вы настроить эти таймеры?
Sure you can.|Что вы можете.
Sure.|Конечно.
You can tweak the timers to,|Вы можете настроить таймеры,
you know, be less, you know, take a little bit more time.|ну знаешь, будь меньше, знаешь, займи немного больше времени.
Maybe 30 seconds, maybe 90 seconds, or 120|Может быть 30 секунд, может быть 90 секунд или 120
seconds.|секунд.
Send the update.|Отправьте обновление.
So why not use EIGRP?|Так почему бы не использовать EIGRP?
Right?|Правильно?
Yet EIGRP only does it one time.|Однако EIGRP делает это только один раз.
When they fully converge, then it's based on changes.|Когда они полностью сходятся, значит, это основано на изменениях.
But EIGRP still distance vector.|Но EIGRP по-прежнему дистанция вектора.
It won't send the whole routing table, but we have to use what, only CISCO routers.|Он не отправит всю таблицу маршрутизации, но мы должны использовать только маршрутизаторы CISCO.
We have to only use CISCO routers.|Нам нужно использовать только маршрутизаторы CISCO.
It's proprietary.|Это проприетарно.
Still limited to hop count.|По-прежнему ограничено подсчетом хмеля.
Does calculate to find out what the metric is.|Вычисляет, чтобы узнать, что такое метрика.
All right.|Отлично.
Best metric, best path the network.|Лучшая метрика, лучший путь в сети.
But in this case really.|Но в данном случае действительно.
We have a straight forward network.|У нас прямая сеть.
There is no, you know, redundancy or anything.|Нет никакой избыточности или чего-то подобного.
We are going straight that way, or straight this way.|Мы идем прямо туда или прямо сюда.
So, if you wanted to EIGRP, you could.|Итак, если вы хотите использовать EIGRP, вы можете.
All right.|Отлично.
Are you going to grow, the growth of the company, all right.|Вы собираетесь расти, рост компании, все в порядке.
Are you gonna have multiple autonomous systems?|У вас будет несколько автономных систем?
That's something to consider, okay, or are you going just have just one?|Надо подумать, ладно, или ты просто возьмешь одну?
For the purpose of the CCNA, just one.|Для CCNA только один.
What about OSPF, now we can use any router we want.|Что касается OSPF, теперь мы можем использовать любой маршрутизатор, какой захотим.
All right?|Отлично?
Very complex.|Очень сложный.
Very processor-intensive.|Очень загружает процессор.
Lot of calculations for that shorter past firth, whew.|Множество вычислений для этого более короткого прошлого лимана, уф.
Shortest path first, tongue twister,|Кратчайший путь сначала, скороговорка,
algorithm.|алгоритм.
So it all depends what you wanna do.|Так что все зависит от того, что вы хотите делать.
So you gotta make a decision based on your network, based on the needs.|Итак, вы должны принять решение на основе вашей сети, исходя из потребностей.
As far as you know, hey, the bandwidth,|Насколько вы знаете, пропускная способность,
how big are we, how many sublets we have?|какие мы большие, сколько у нас субаренд?
So it's not a straight forward question.|Так что это непростой вопрос.
If anybody says, well, what are you gonna use, static or dynamic?|Если кто-нибудь скажет, что вы собираетесь использовать, статическое или динамическое?
Well, I haven't analyzed my network yet, I don't know what it is I'm gonna do.|Что ж, я еще не проанализировал свою сеть, я не знаю, что я собираюсь делать.
So you may just wanna use static.|Так что вы можете просто использовать static.
A lot of the questions you may run into when it comes to static or dynamic, is just that.|Многие вопросы, с которыми вы можете столкнуться, когда речь заходит о статике или динамике, являются именно такими.
That you may, well, if you see things like, what is the easiest way, what is the quickest way, what will be less overhead on our router, what will be less|Что вы можете, ну, если вы увидите такие вещи, как, какой самый простой способ, какой самый быстрый способ, что будет меньше накладных расходов на нашем маршрутизаторе, что будет меньше
intense on a router, static routes, static routes, static routes, static routes.|интенсивный на маршрутизаторе, статические маршруты, статические маршруты, статические маршруты, статические маршруты.
That will be the way to go especially on a network so small like this.|Это будет подходящим вариантом, особенно в такой маленькой сети, как эта.
Now when we get to the configuration part,|Теперь, когда мы переходим к настройке,
we will do it here.|мы сделаем это здесь.
But I'm also going to show you how to do it on the live routers.|Но я также собираюсь показать вам, как это сделать на живых маршрутизаторах.
I have 1841 routers.|У меня 1841 роутер.
And I got only two PCs, I've got my PC and another PC hooked up, so you can actually see the prompt, okay, of the live router.|И у меня есть только два ПК, мой компьютер и еще один подключены, так что вы действительно можете увидеть подсказку, хорошо, работающего маршрутизатора.
So, for those of you that think, oh, well it's a packet tracer, and it's, you know,|Итак, для тех из вас, кто думает, ну, это трассировщик пакетов, и это, вы знаете,
it's not the same.|это не одно и то же.
It's the same thing.|Это то же самое.
All right, it's the same exact thing.|Ладно, это то же самое.
Alright, now could you have more features on a real IOS?|Хорошо, теперь у вас может быть больше функций на настоящей IOS?
Yes, yes, you have more features.|Да, да, у вас есть больше возможностей.
You have more commands.|У вас есть больше команд.
But again, what is a packet tracer for?|Но опять же, для чего нужен трассировщик пакетов?
For CCNA purposes.|Для целей CCNA.
If you have a live lab, hey, good for you.|Если у вас есть живая лаборатория, хорошо для вас.
All right, but again, I'm gonna show you.|Хорошо, но я еще раз покажу тебе.
We'll do both.|Мы сделаем и то, и другое.
We'll do the packet tracer, and then I'll show you in the, in the live,|Мы сделаем трассировщик пакетов, а затем я покажу вам вживую,
the live router.|живой роутер.
Right?|Правильно?
So you can see how it goes back and forth.|Итак, вы можете увидеть, как он движется вперед и назад.
It's, it's still the same commands.|Это все те же команды.
Nothing changes.|Ничего не меняется.
Nothing changes.|Ничего не меняется.
A static route is a static route.|Статический маршрут - это статический маршрут.
A routing port is a routing port of call.|Порт маршрутизации - это порт маршрутизации вызова.
But you definitely need to make a decision, static versus dynamic.|Но вам определенно нужно принять решение, статическое или динамическое.
And just to break it down already, static routes, good for the router, bad for you.|И просто разбить его уже, статические маршруты, хорошо для роутера, плохо для вас.
All right, well, bad for you, or like I said, job security.|Ладно, ну, плохо для тебя, или, как я уже сказал, гарантия работы.
Because then, depending the size of it,|Потому что тогда, в зависимости от его размера,
you would be maintaining that,|вы бы поддерживали это,
that'll be an eight hour job, to maintain.|это будет восьмичасовая работа, чтобы поддерживать.
If not, if you guys,|Если нет, если вы, ребята,
if you gonna use, dynamic routing, then bad for the router, right?|если вы собираетесь использовать динамическую маршрутизацию, тогда плохо для роутера, верно?
The router is calculating all sorts of algorithms and math, trying to find out which way to go.|Маршрутизатор вычисляет всевозможные алгоритмы и математику, пытаясь выяснить, в каком направлении двигаться.
Especially if you a lot of redundancy, and all that.|Особенно, если у вас много избыточности и все такое.
But good for you, because all you gotta do is put the network that you're connected to, it's the opposite.|Но это хорошо для вас, потому что все, что вам нужно сделать, это подключить сеть, к которой вы подключены, все наоборот.
Right, because dynamic routing is routing my roomer.|Верно, потому что динамическая маршрутизация направляет мою комнату.
You kind of snitch yourself out.|Вы как бы изводите себя.
All right, and we'll be configuring all the routing protocols, all those three routing protocols, we will be configuring them both for IVP 4 and IVP 6.|Хорошо, и мы будем настраивать все протоколы маршрутизации, все эти три протокола маршрутизации, мы будем настраивать их как для IVP 4, так и для IVP 6.
You can see both.|Вы можете увидеть и то, и другое.
Okay, but again, you first got to make the decision, which one do I use?|Хорошо, но опять же, сначала вы должны решить, какой из них мне использовать?
But, and I haven't mentioned one yet, I haven't mentioned one yet.|Но, и я еще не упомянул ни одного, я еще не упомянул ни одного.
But definitely, the first configuration,|Но определенно первая конфигурация,
once we get to do the configurations.|как только мы займемся настройками.
We'll probably be doing a combination of something called default.|Вероятно, мы будем делать комбинацию чего-то, что называется по умолчанию.
Gave it away.|Отдал.
All right, but we'll talk about that in a little bit.|Хорошо, но мы поговорим об этом чуть позже.
Default and static routing.|Маршрутизация по умолчанию и статическая.
And then we'll implement the routing protocols as we progress into the course.|А затем мы реализуем протоколы маршрутизации по мере продвижения по курсу.
All right, so there you go.|Хорошо, так что поехали.
That's static versus dynamic.|Это статическое против динамического.
No big deal.|Ничего страшного.
You have to make the choice.|Вы должны сделать выбор.
Stay thirsty, my friends.|Сохраняйте жажду, друзья мои.
[BLANK_AUDIO]|[BLANK_AUDIO]