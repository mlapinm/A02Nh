D:\mailCloud\prjother\tmp\1\c78_OSPF multiple area details.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
All right everyone.|Все в порядке.
Welcome back.|Добро пожаловать.
This is multiple area OSPF.|Это многослойный OSPF.
Very basic multi area OSPF.|Очень простой OSPF с несколькими областями.
Most of you can understand that concept.|Большинство из вас может понять эту концепцию.
Are you gonna be tested on this?|Вы собираетесь пройти тестирование по этому поводу?
Not whatsoever.|Ни в коем случае.
Not whatsoever.|Ни в коем случае.
Do you need to understand that area zero is your backbone area?|Вам нужно понимать, что нулевая зона - это ваша магистраль?
Yes.|Да.
Need to understand that everyone sends their information to area zero?|Нужно понимать, что каждый отправляет свою информацию в нулевую зону?
Yes.|Да.
Does everybody need to connect to area zero directly or indirectly?|Всем ли нужно подключаться к нулевой зоне прямо или косвенно?
Yes.|Да.
That the router that connects you to area zero is called an area border router?|Что маршрутизатор, который соединяет вас с нулевой зоной, называется пограничным маршрутизатором области?
Yes.|Да.
Will they test you on it?|Будут ли они тебя проверять?
No.|Нет.
Do you need to know it?|Вам нужно это знать?
Yes.|Да.
Sounds kind of funny, right?|Звучит забавно, правда?
Well, that's just the way it is.|Ну, так оно и есть.
The book talks about it.|Об этом говорится в книге.
You need to know.|Ты должен знать.
You need to know about it.|Вы должны об этом знать.
You need to know about it when you go out there and you interview with these people that have no idea what they're interviewing you about.|Вам нужно знать об этом, когда вы идете туда и берете интервью у этих людей, которые понятия не имеют, о чем они вас берут.
All right?|Отлично?
So, you're gonna answer their questions which they still don't know the answer to but you, you know, you give it to them anyway.|Итак, вы ответите на их вопросы, на которые они все еще не знают ответа, но вы, знаете, все равно даете им это.
But, yeah, well, you, you will encounter,|Но, да, ну ты, ты встретишь,
multiple area OSP about this.|несколько областей OSP об этом.
I'll show you a little basic,|Я покажу вам немного основы,
configuration, multiple area OSPF.|конфигурация, OSPF с несколькими областями.
Not a big deal.|Не так уж и важно.
Nothing that you need to focus on heavily.|Ничего такого, на чем вам нужно сильно сосредоточиться.
At all, for your CCNA.|Вообще, для вашего CCNA.
Besides the fact that, hey, area zero is your backbone area.|Помимо того факта, что нулевая зона - это ваш позвоночник.
Okay?|Ладно?
So I know that it is possible.|Так что я знаю, что это возможно.
So what do we have here?|Итак, что у нас здесь?
You see some lube backs.|Вы видите смазку.
You see some ip addresses.|Вы видите несколько IP-адресов.
Right?|Правильно?
It's all ethernet.|Это все Ethernet.
So what does that mean?|Так что это значит?
DRs.|DRs.
All right, so here, oh no, here, sorry.|Хорошо, так что здесь, о нет, здесь, извините.
I, I just, I forget.|Я просто забыл.
My brain is going crazy.|Мой мозг сходит с ума.
All right so what you see in red if you see it in red.|Хорошо, так что вы видите красным, если видите это красным.
All right?|Отлично?
From the 2, loopback 2.2.2, loopback 3.3.3.|Из 2, шлейф 2.2.2, шлейф 3.3.3.
The 10.1.1.4 the 10.1.1.8 and the loopback 1.1.1, that is your area zero.|10.1.1.4, 10.1.1.8 и loopback 1.1.1, это нулевая область.
And then area then from the 10.1.1.12 and the loop backs, and the 10.1.1.6 and the loopback, that is,|И затем область, затем из 10.1.1.12 и обратной петли, и из 10.1.1.6 и обратной петли, то есть
you know, area one and area two.|вы знаете, область один и область два.
I want to make them all talk.|Я хочу заставить их всех поговорить.
Wanna make them all talk.|Хочу заставить их всех поговорить.
And there's really no special configuration that you have to do.|И нет никакой специальной настройки, которую вам нужно делать.
You just gotta make sure you put each interface in the right area.|Вам просто нужно убедиться, что вы поместили каждый интерфейс в нужную область.
And since they are connected, since this is directly connected to that one,|И поскольку они связаны, так как это напрямую связано с этим,
okay, and you'er the connected to him,|хорошо, и вы связаны с ним,
it will send the information on forward to area zero.|он отправит информацию о направлении в нулевую зону.
If there would have been another router in between, router four, right, there would be another router here with another network, then that router, we're not.|Если бы между ними был еще один маршрутизатор, четвертый маршрутизатор, верно, здесь был бы еще один маршрутизатор с другой сетью, тогда этот маршрутизатор, нас нет.
You have to do something called a virtual link at that point with the router ID,|В этот момент вам нужно сделать что-то, что называется виртуальной ссылкой с идентификатором маршрутизатора,
the area you need to traverse with that router four's ID.|область, которую вам нужно пройти с идентификатором четвертого маршрутизатора.
So it's a little bit different, but again, there' s no need to get into that detail, all right?|Так что это немного другое, но, опять же, нет необходимости вдаваться в подробности, понятно?
You don't, you're not gonna do anything like that.|Ты не будешь делать ничего подобного.
Know that you would, you could do it.|Знайте, что вы бы это сделали.
But, again, for the CCNA purposes, no.|Но, опять же, для целей CCNA нет.
So let's go ahead and have some fun with this.|Итак, давайте продолжим и повеселимся.
All right?|Отлично?
And basically the IP addresses are already on there, but we'll verify to make sure everything's copacetic.|И в основном IP-адреса уже есть, но мы проверим, чтобы убедиться, что все в порядке.
Okay.|Ладно.
And then we'll configure.|А потом настроим.
So let's verify, the IP addresses.|Итак, давайте проверим IP-адреса.
All right.|Отлично.
So, let's do a, let's do a show start.|Итак, давайте, давайте начнем шоу.
Just look at the whole thing.|Вы только посмотрите на все это.
Let's maximize the screen.|Давайте развернем экран.
Okay?|Ладно?
Let's take a look here.|Давайте посмотрим здесь.
Here's our loopback, 1.1.1.1.|Вот наш шлейф 1.1.1.1.
Here's a 10.1.1.5, which is in the 10.1.1.4 network.|Вот 10.1.1.5, который находится в сети 10.1.1.4.
10.1.1.9, which is the 10.1.1.8 network.|10.1.1.9, то есть сеть 10.1.1.8.
And cool, cool all right so we're good there.|И круто, круто, так что нам там хорошо.
IPs are there.|IP есть.
Let's do a do, oh not do.|Давай сделаем, о, не делай.
Let's just do a show IP INT BRIEF.|Давайте просто сделаем шоу IP INT BRIEF.
All right it shows everything as up, up.|Хорошо, он показывает все как вверх, вверх.
Very good, very good, very good.|Очень хорошо, очень хорошо, очень хорошо.
That's what we want to see.|Это то, что мы хотим видеть.
Well let's take a look at the running tables.|Что ж, давайте посмотрим на беговые столы.
Take a look at the running tables.|Взгляните на беговые столы.
What do we see in the running table?|Что мы видим в беговом столе?
Show, show IP route.|Показать, показать IP-маршрут.
All you see is just directly connected neighbors.|Все, что вы видите, это просто соседи с прямым подключением.
That's all you see.|Это все, что вы видите.
All right.|Отлично.
So that is the top router.|Итак, это верхний маршрутизатор.
Let's take a look at this one.|Давайте посмотрим на это.
So we'll enable, show start.|Так что включим, покажем старт.
Let's take a look at it.|Давайте посмотрим на это.
There's our loop back three our 10.1.1.10|Вот наш цикл на три, наш 10.1.1.10
which is in the eight network and then 10.1.1.17, and that's all she wrote right there.|который в сети восьмерка а потом 10.1.1.17, и это все, что она тут же написала.
All right, and then we come here.|Хорошо, а потом мы приходим сюда.
[BLANK_AUDIO]|[BLANK_AUDIO]
Enable.|Включить.
Show start.|Показать начало.
[SOUND] Well,|[ЗВУК] Ну,
we'll loop back.|мы вернемся назад.
All fives.|Все пятерки.
And the 10.1.1.8.|И версия 10.1.1.8.
All right?|Отлично?
So those IP addresses are already there.|Итак, эти IP-адреса уже есть.
Looks good.|Выглядит хорошо.
Cuz remember, this right here is gonna be area two.|Потому что помни, вот здесь будет вторая зона.
This section right there, that's area two.|Вот эта секция, вторая область.
And then over here, this section,|А потом здесь, в этом разделе,
gonna be area one, all right?|собираешься быть первой областью, хорошо?
Cool.|Прохладно.
So let's go ahead and configure area one.|Итак, давайте продолжим и настроим область один.
We'll leave area zero for last, all right?|Мы оставим нулевую зону напоследок, хорошо?
So let's go ahead and do that.|Так что давайте продолжим и сделаем это.
Doesn't even kind of make sense, why we're gonna do area zero first.|Даже не имеет смысла, почему мы сначала собираемся сделать нулевую зону.
That's the one you need to do first,|Это то, что вам нужно сделать в первую очередь,
right?|право?
Well, I wanna do area one first, all right?|Ну, я хочу сначала заняться первой областью, хорошо?
That's just the way I am, I like to go from left to right.|Просто я такой, мне нравится идти слева направо.
I'm always there if you need it.|Я всегда рядом, если тебе это нужно.
You guys know that.|Вы, ребята, это знаете.
I'm a rebel!|Я бунтарь!
[BLANK_AUDIO]|[BLANK_AUDIO]
Yeah, maximize, right?|Да, максимизировать, правда?
Why not?|Почему нет?
So if we maximize it we need to know what we're advertising, so show IP in brief.|Поэтому, если мы увеличиваем его, нам нужно знать, что мы рекламируем, поэтому кратко укажите IP.
And, of course, the loopback is gonna be using, well let's do short protocols to make sure, cause the short protocols give|И, конечно, будет использоваться шлейф, давайте сделаем короткие протоколы, чтобы убедиться, потому что короткие протоколы дают
us the actual mask.|нам настоящая маска.
Yeah, the, the 10.1.1.4 is using a sider 30 and, loopback is using a 32.|Да, 10.1.1.4 использует сайдер 30, а loopback использует 32.
So let's go ahead and do OSPF.|Итак, давайте продолжим и займемся OSPF.
Now this is area one.|Теперь это первая область.
Area one.|Первая зона.
So CONFIG T, ROUTER OSPF 1.|Итак, CONFIG T, ROUTER OSPF 1.
Again the process ID number doesn't matter, it's local to the router.|Опять же, идентификационный номер процесса не имеет значения, он является локальным для маршрутизатора.
Then we're going to do network, 4.4.4.4,|Затем займемся сетью, 4.4.4.4,
0.0.0.0.|0.0.0.0.
32 right?|32 верно?
Area one.|Первая зона.
[BLANK_AUDIO]|[BLANK_AUDIO]
>> Oh, one too many zeros.|>> Ой, нулей слишком много.
I mean, one too many periods.|Я имею ввиду, слишком много периодов.
Okay.|Ладно.
So yeah, I had a decimal up here.|Так что да, у меня здесь была десятичная дробь.
Where is it?|Где это находится?
Yeah.|Да.
I put a decimal right there.|Я тут же поставил десятичную дробь.
One too many.|Слишком много.
Okay.|Ладно.
[COUGH] And we advertised the other network which is 10.1.1.4 network.|[КАШЕ] И мы анонсировали другую сеть - сеть 10.1.1.4.
10.1.1.14.|10.1.1.14.
Sorry, 14.|Простите, 14.
And a 0.0.0.3, so 252 mask.|И 0.0.0.3, значит, 252 маска.
Area one.|Первая зона.
There we are.|Вот и мы.
Gonna show start.|Покажу старт.
And there's OSPF with both of those in area uno.|И есть OSPF с обоими из них в области uno.
Which is these two right here.|Вот эти двое прямо здесь.
All right?|Отлично?
That is area one.|Это первая область.
[BLANK_AUDIO]|[BLANK_AUDIO]
So, this router right here, this area border router,|Итак, вот этот маршрутизатор, этот пограничный маршрутизатор,
his interface, this particular interface,|его интерфейс, этот конкретный интерфейс,
so he's also part of area one, and then the loopback will be part of area zero plus the 10.1.1.5, the 10.1.1.4.|так что он также является частью области один, и тогда петля будет частью нулевой области плюс 10.1.1.5, 10.1.1.4.
So there's three networks here for this,|Итак, для этого есть три сети,
this ABR, this area border router.|этот ABR, этот пограничный маршрутизатор области.
That's going to go ahead.|Это будет продолжаться.
You need to advertise one interface that's gonna be the 10 112 network in area 1 and the other two interfaces will be, or, will|Вам необходимо объявить один интерфейс, который будет сетью 10 112 в области 1, а два других интерфейса будут или будут
be in area 0.|находиться в области 0.
So let's go ahead and do that.|Так что давайте продолжим и сделаем это.
And again we'll do the show protocols command so we can info right there in front of us.|И снова мы выполним команду show protocol, чтобы информация была прямо перед нами.
Show protocols.|Показать протоколы.
And, you know, one reason I like that is just to find back and see the mask.|И, знаете, одна причина, по которой мне это нравится, - это просто вернуться назад и увидеть маску.
All right, config t,|Хорошо, конфиг т,
router, OSPF 1.|маршрутизатор, OSPF 1.
All right.|Отлично.
So [COUGH].|Итак [КАШЕ].
[BLANK_AUDIO]|[BLANK_AUDIO]
The, [SOUND] 10.1.1.3 is area 1, which is going down.|[ЗВУК] 10.1.1.3 - это зона 1, которая идет вниз.
So, that's gonna be network.|Итак, это будет сеть.
Just gonna put net.|Поставлю чистую.
10.1.1.12, 0.0.0.3 Area 1.|10.1.1.12, 0.0.0.3 Область 1.
And then you have network 10.1.1.4 0.0.0.3 area 0.|И тогда у вас есть сеть 10.1.1.4 0.0.0.3 область 0.
And then network, 2.2.2.2|А потом сеть, 2.2.2.2
0.0.0.0 area 0.|0.0.0.0 область 0.
Enter.|Войти.
Do WR.|Сделайте WR.
Okay.|Ладно.
[BLANK_AUDIO]|[BLANK_AUDIO]
Oh, we got, yeah the 14 ones for 12, and then the 2 area 0.|О, у нас есть 14 из 12, а затем 2 области 0.
And the 6 which is the fourth network area 0.|И 6, что является четвертой областью сети 0.
All right so lets come over here, router number 5.|Хорошо, давай сюда, роутер номер 5.
We got the 5 and the 16 network for area 2.|У нас есть сети 5 и 16 для области 2.
Okay, and the good thing about separating things into multiple areas is the fact that you can maintain any kind of issues|Хорошо, и в разделении вещей на несколько областей хорошо то, что вы можете поддерживать любые проблемы.
within that area, within that area.|в этой области, в этой области.
The autonomous border router will not allow any,|Автономный пограничный маршрутизатор не позволит,
any problems to go across that that particular router.|какие-либо проблемы, связанные с этим конкретным маршрутизатором.
Any issues within that particular area will stay there.|Любые проблемы в этой конкретной области останутся там.
[SOUND] now while we looking here, do show protocols.|[ЗВУК] сейчас, пока мы здесь смотрим, покажем протоколы.
[BLANK_AUDIO]|[BLANK_AUDIO]
Okay?|Ладно?
All right, so we got router OSPF 1,|Итак, у нас есть роутер OSPF 1,
net 5.5.5.5.|нетто 5.5.5.5.
0.0.0.0, Area 2,|0.0.0.0, Область 2,
net 10.1.1.16, that's the network.|net 10.1.1.16, вот и сеть.
0.0.0 whoops,|0.0.0 упс,
0 3.|0 3.
Area 2, all right, DO WR.|Область 2, хорошо, DO WR.
So that takes care of this particular section right here.|Так что это касается именно этого раздела прямо здесь.
Now we need to advertise the 10.1.1.8 and the 3.3.3.3.3 for, you know, going that way, for area 0.|Теперь нам нужно прорекламировать 10.1.1.8 и 3.3.3.3.3 для того, чтобы идти этим путем, для области 0.
And of course the 10.1.1.6 for area 2.|И, конечно же, 10.1.1.6 для области 2.
Because it's in two different areas, this particular router.|Потому что этот конкретный маршрутизатор находится в двух разных областях.
That's why they call it area border router.|Вот почему они называют это пограничным маршрутизатором области.
So we're gonna [SOUND] show protocols again.|Итак, мы собираемся [ЗВУК] снова показывать протоколы.
[BLANK_AUDIO]|[BLANK_AUDIO]
All right, so you can see there, the 10.1.1.10,|Хорошо, вы можете увидеть там 10.1.1.10,
that's 8, and then 16 is going to the bottom.|это 8, а затем 16 идет вниз.
So, config t, ROUTER OSPF 1 NET 10.1.1.16|Итак, config t, ROUTER OSPF 1 NET 10.1.1.16
0.0.0.3, that is AREA 2.|0.0.0.3, то есть ОБЛАСТЬ 2.
It's going down, that will be the 17 that you see there in front of you.|Он идет вниз, это будут те 17 человек, которые вы увидите перед собой.
The next one will be oh, ooh, look at that.|Следующий будет о, о, посмотрите на это.
Okay?|Ладно?
The next one that you see would be the 10.1.1.10, that will be AREA 0,|Следующим, что вы увидите, будет 10.1.1.10, это будет ОБЛАСТЬ 0,
and that would be 8, the 8 network.|и это будет 8, сеть 8.
All right?|Отлично?
And then you have the loopback which is 32.|И тогда у вас есть шлейф 32.
Net 3.3.3.3 0.0.0.0, Area 0.|Нетто 3.3.3.3 0.0.0.0, Площадь 0.
DO WR.|DO WR.
Awesome.|Потрясающие.
So we got that done.|Итак, мы сделали это.
Let's make sure it's, I'm doing this correctly here.|Убедимся, что я здесь делаю правильно.
All right area 2 [SOUND] and then area, or area 2 going down, 0 coming up.|Хорошо, область 2 [ЗВУК] и затем область, или область 2 идет вниз, 0 поднимается.
All right.|Отлично.
All right, now 0.0 okay, this is 2.|Хорошо, теперь 0,0, хорошо, это 2.
All right, so now all we gotta do is configure the backbone,|Хорошо, теперь все, что нам нужно сделать, это настроить магистраль,
where we have the loopback, the 4 and the 8.|где у нас есть шлейф, 4 и 8.
That's what's in area 0.|Вот что находится в области 0.
So we go config, well let's do show protocols, just as usual.|Итак, мы переходим к настройке, ну давайте покажем протоколы, как обычно.
All right [SOUND].|Хорошо [ЗВУК].
All right, config T.|Хорошо, конфиг T.
So, let's do a loopback first Router or SPF 1.|Итак, давайте сделаем петлевой первый маршрутизатор или SPF 1.
Net 1.1.1.1 0.0.0.0.|Чистая 1.1.1.1 0.0.0.0.
Area 0, everything's in area 0.|Зона 0, все в зоне 0.
So we're going to go net,|Итак, мы идем в сеть,
10.1.1.4 0.0.0.0, area 0.|10.1.1.4 0.0.0.0, область 0.
And then you have the 8.|И тогда у вас есть 8.
Net 10.1.1.8.|Нетто 10.1.1.8.
Oops, made a mistake.|Ой, ошиблись.
Put the wrong wildcard match for the 1.1,|Поместите неправильное совпадение подстановочного знака для 1.1,
10.1.1.4.|10.1.1.4.
So I'm gonna say no.|Так что я скажу нет.
[BLANK_AUDIO]|[BLANK_AUDIO]
Copy.|Копировать.
Paste.|Вставить.
And I'll do it again.|И я сделаю это снова.
NET 10.1.1.4 0.0.0.3 AREA 0.|NET 10.1.1.4 0.0.0.3 ОБЛАСТЬ 0.
Then we'll go net, 10.1.1.8 0.0.0.3 Area 0.|Затем перейдем в сеть, 10.1.1.8 0.0.0.3 Area 0.
DO WR.|DO WR.
Let's take a look that everything is okay.|Посмотрим, все ли в порядке.
Show start.|Показать начало.
Let's take a look at the OSPF configurations.|Давайте посмотрим на конфигурации OSPF.
They're okay, we got the right networks,|Они в порядке, у нас правильные сети,
the 4 and the 8 using the 3.|4 и 8, используя 3.
And then the, all 0s for the loopback and area 0.|И затем все 0 для петли и области 0.
Okay, so what should we see?|Итак, что мы должны увидеть?
Let's see, SHOW IP ROUTE, let's look at our routing table.|Посмотрим, ПОКАЗАТЬ IP-МАРШРУТ, посмотрим на нашу таблицу маршрутизации.
All right, you can see here, we have our Os to the loopback addresses.|Хорошо, вы можете видеть здесь, у нас есть проблемы с адресами обратной связи.
All right, to the 2, to the 3, but if you notice that for the 10.1.1.16, all right, and for loopback 5.5.5.5, it's called an|Хорошо, для 2, для 3, но если вы заметили, что для 10.1.1.16 все в порядке, а для loopback 5.5.5.5 это называется
inter-area.|межрайонный.
What is an inter-area?|Что такое межрегиональный?
And inter-area is just, it's not in the same area, but it's part of the same OSPF domain.|И межобластная связь - это просто, она не находится в одной и той же области, но является частью того же домена OSPF.
It's part of the same OSPF domain,|Это часть того же домена OSPF,
it's just outside the area of area 0, or area 1 or area 2.|он находится за пределами области 0, 1 или 2.
If you were to look at, let's say, router 4.|Если вы посмотрите, скажем, на маршрутизатор 4.
[BLANK_AUDIO]|[BLANK_AUDIO]
And you would do a show IP route.|И вы бы сделали показ IP-маршрута.
[BLANK_AUDIO]|[BLANK_AUDIO]
And, it's taking its sweet time today.|И сегодня самое приятное время.
It has its issues today.|Сегодня у него есть проблемы.
All right.|Отлично.
This one's doing it.|Этот делает это.
[BLANK_AUDIO]|[BLANK_AUDIO]
All right, you can see that it is receiving inter error routes from the 1.1.1.1, from the 2.2.2,2,|Хорошо, вы можете видеть, что он получает маршруты с ошибками от 1.1.1.1, от 2.2.2,2,
3.3.3.3, the 10.1.1.4, and the 10.1.1.8.|3.3.3.3, 10.1.1.4 и 10.1.1.8.
These are routes, this is how you would see it.|Это маршруты, вот как вы это видите.
Now there's different types, obviously.|Очевидно, есть разные типы.
There's external routes as well that you would see an E1 or an E2 for external routes.|Также есть внешние маршруты, которые вы увидите E1 или E2 для внешних маршрутов.
Meaning it's going across what's called an ASBR, an autonomous system border router,|Это означает, что он проходит через так называемый ASBR, пограничный маршрутизатор автономной системы,
which is coming from an exterior routing protocol like BGP.|который исходит от внешнего протокола маршрутизации, такого как BGP.
Or another routing protocol together, it's coming from the internet.|Или другой протокол маршрутизации вместе, он исходит из Интернета.
All right, so that will be either an e,|Хорошо, так что это будет либо е,
type E1 or type E2, and there are differences between one or the other.|введите E1 или E2, и между ними есть различия.
But in this case, it is just a multiple area OSPF.|Но в данном случае это всего лишь многосекционный OSPF.
You're still within the OSPF domain, just in different areas.|Вы все еще находитесь в домене OSPF, только в разных областях.
That's why they're called inter-areas,|Вот почему их называют межрайонными,
inter-areas.|межрайоны.
And you can communicate back and forth.|И вы можете общаться туда и обратно.
Now I don't know what happened to this router.|Теперь я не знаю, что случилось с этим роутером.
It's being silly.|Это глупо.
Did I, well, maybe it's me.|Я, ну, может, это я.
Did I configure it?|Я это настраивал?
[BLANK_AUDIO]|[BLANK_AUDIO]
Say, it's the first one I configured.|Скажем, я настроил его первым.
[BLANK_AUDIO]|[BLANK_AUDIO]
Yeah, they're both in area 1.|Да, они оба в зоне 1.
Mm-hm, okay, well, all righty then because this one here, show start.|Мм, ладно, тогда ладно, потому что этот здесь, начало шоу.
As you can see, let's maximize it.|Как видите, давайте увеличим его до максимума.
Same, pretty much the same configuration.|Такая же, почти такая же конфигурация.
And let me make sure that I did put one interface in here.|И позвольте мне убедиться, что я поместил сюда один интерфейс.
And here's the configuration, is in area 0|А вот конфигурация, находится в области 0
which is the 10.|что 10.
Oh, okay, I see the problem.|Ладно, я вижу проблему.
You see what I did here?|Вы видите, что я здесь сделал?
I put that instead of 10.1.1.8 or 10.1.1.12 I should say, 10.1.1.12.|Я поставил это вместо 10.1.1.8 или 10.1.1.12, я бы сказал, 10.1.1.12.
So I put the actual IP address.|Я поставил настоящий IP-адрес.
So that's the problem right there.|Так вот в чем проблема.
Okay, it's not packet tracer, it's a user error.|Ладно, это не трассировщик пакетов, это ошибка пользователя.
All right, so let me go inside, ROUTER OSPF 1.|Хорошо, позвольте мне войти, МАРШРУТИЗАТОР OSPF 1.
NO, let's put this right here.|НЕТ, давайте поместим это прямо сюда.
[BLANK_AUDIO]|[BLANK_AUDIO]
Copy.|Копировать.
[BLANK_AUDIO]|[BLANK_AUDIO]
Paste.|Вставить.
And then I'm gonna say network 10.1.1.12,|И тогда я скажу сеть 10.1.1.12,
0.0.0.3, AREA 1.|0.0.0.3, ОБЛАСТЬ 1.
DO WR, show START.|DO WR, показать СТАРТ.
So now, that should be correct.|Итак, теперь это должно быть правильно.
There we go.|Вот и все.
Now we got the full Loading Done going on,|Теперь у нас есть полная загрузка Done,
awesome, awesome.|круто круто.
Let's see if now, show, show IP ROUTE.|Посмотрим, покажет ли сейчас IP ROUTE.
All right, there we go.|Хорошо, поехали.
Now, it was just my mistake there.|Так вот, это была просто моя ошибка.
Inter, now you're getting all the inter,|Интер, теперь ты получаешь все интер,
your OSPF routes and your inter area routes.|ваши маршруты OSPF и ваши межобластные маршруты.
So, that is multiple area OSPF.|Итак, это многослойный OSPF.
All you really gotta pay attention to is,|Все, на что вам действительно нужно обратить внимание, это
say okay, these are my ABRs,|скажи хорошо, это мои ABR,
and they're actually pointing to two different areas.|и они фактически указывают на две разные области.
In this case area 0 and then area 1, and then this router area 0 and area 2.|В этом случае область 0, затем область 1, а затем эта область маршрутизатора 0 и область 2.
Okay, so that all it is.|Ладно, так что все есть.
All areas, just so you know, all areas must connect back to area 0 because area 0|Все области, просто чтобы вы знали, все области должны соединяться с областью 0, потому что область 0
will update everybody else.|буду обновлять всех остальных.
It's the same kind of, same scenario as the DR and the BDR where the DR updates everybody else.|Это тот же самый сценарий, что и DR и BDR, когда DR обновляет всех остальных.
Same deal here, everybody updates area 0,|То же самое здесь, все обновляют область 0,
area 0 updates everybody else.|область 0 обновляет всех остальных.
Doesn't mean there's one router in area 0.|Это не значит, что в области 0 есть один маршрутизатор.
It means there, remember, you can have 50|Значит там, помните, у вас может быть 50
routers within an area.|маршрутизаторы в пределах области.
So it could be 50 routers in area 0, and they're pointing to different, you know,|Так что это может быть 50 маршрутизаторов в области 0, и они указывают на разные, вы знаете,
different areas are connecting to it,|к нему подключаются разные области,
handling those particular areas.|обработка этих конкретных областей.
Okay, so that's it.|Ладно, вот и все.
Pretty simple, all you gotta do is make sure hey, which interface, so I can advertise it correctly in that particular area.|Довольно просто, все, что вам нужно сделать, это убедиться, какой интерфейс, чтобы я мог правильно рекламировать его в этой конкретной области.
And that's it.|И это все.
It's not that's it, but for the basics of it, that is it.|Дело не в этом, но по сути, это так.
Again, in your examination you will not,|Опять же, на вашем экзамене вы не будете,
you will not have to ask,|тебе не придется спрашивать,
answer any question, multiple choice question, on multiple areas.|ответьте на любой вопрос, вопрос с несколькими вариантами ответов в нескольких областях.
You will not have to configure anything to deal with multiple area or OSPF for that matter.|Вам не нужно ничего настраивать для работы с несколькими областями или OSPF в этом отношении.
That they may ask you something wild like you have this network statement in OSPF.|Что они могут спросить вас что-то дикое, например, у вас есть этот сетевой оператор в OSPF.
And you see it on like a wildcard max like what we did.|И вы видите это как подстановочный знак, как то, что мы сделали.
What interfaces, you know, take part in this OSPF process?|Какие интерфейсы, вы знаете, участвуют в этом процессе OSPF?
And really that's not an OSPF question,|И это действительно не вопрос OSPF,
that's a subnetting question, all right.|это вопрос о подсети, хорошо.
So but that's it.|Так что это все.
That's as far as really I want to go with this because you're not going to go ahead and be doing it for your CCNA certification.|На самом деле я хочу остановиться на этом, потому что вы не собираетесь делать это для получения сертификата CCNA.
You'll be doing it for CCMP, definitely be doing it for CCIE, things of that nature.|Вы будете делать это для CCMP, определенно будете делать это для CCIE, и тому подобное.
But for CCNA, not yet anyway.|Но для CCNA пока нет.
You won't have to be doing that.|Тебе не нужно этого делать.
Be aware of it.|Знайте об этом.
Be aware of it, definitely.|Знайте об этом, определенно.
The terminology, as far as area border routers, all right,|Терминология, что касается пограничных маршрутизаторов, все в порядке,
that they bring different areas, within the OSPF domain, and autonomous system border routers which bring in external routes.|что они объединяют различные области внутри домена OSPF и пограничные маршрутизаторы автономных систем, которые вводят внешние маршруты.
Whether it be from RIP, or EIGRP, or BGP,|Будь то RIP, EIGRP или BGP,
or the internet, into OSPF.|или из Интернета в OSPF.
That's different.|Это другое.
That would be then like I said a type E1|Это было бы, как я сказал, тип E1
or type E2, external routes.|или введите E2, внешние маршруты.
These are internal routes because they're still a part of the OSPF routing protocol.|Это внутренние маршруты, потому что они все еще являются частью протокола маршрутизации OSPF.
That's all.|Вот и все.
That's all that is.|Это все, что есть.
So I hope you enjoyed the lab.|Надеюсь, вам понравилась лаборатория.
This comes to an end now.|Это подходит к концу.
As far as OSPF no, no big deal.|Насчет OSPF нет, ничего страшного.
I'll see you guys in the next section.|Увидимся в следующем разделе.
[BLANK_AUDIO]|[BLANK_AUDIO]