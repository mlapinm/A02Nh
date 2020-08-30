D:\mailCloud\prjother\tmp\1\c83_How to create and assign a vlan Trunking appropriate ports.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
All right, welcome back.|Хорошо, добро пожаловать обратно.
So we got this little app going on back here.|Итак, у нас есть это маленькое приложение.
All right, and just like we, I said previously, I'm gonna, I'm gonna have two different VLANs on one switch, and the same two VLANs on the other switch.|Хорошо, и, как мы, я сказал ранее, у меня будет две разные VLAN на одном коммутаторе и те же две VLAN на другом коммутаторе.
And they're gonna be part of two different networks.|И они будут частью двух разных сетей.
Then we see how they're gonna communicate going across these particular ports right here.|Затем мы увидим, как они собираются общаться через эти конкретные порты прямо здесь.
So let's ahead to this switch over here.|Итак, давайте перейдем к этому переключению здесь.
And let's create [COUGH] our VLANs.|И давайте создадим [КАШЕ] наши VLAN.
So, let's say, there's gonna be VLAN 100|Итак, допустим, будет VLAN 100
and VLAN 101, obviously.|и VLAN 101, очевидно.
We're gonna create them on both switches,|Мы собираемся создать их на обоих переключателях,
all right?|отлично?
So, we're gonna come here.|Итак, мы собираемся прийти сюда.
Let's maximize.|Давайте максимизировать.
Let's go to the CLI.|Пойдем в CLI.
Let's give this switch a name.|Дадим этому переключателю имя.
Config T, and we'll call this, switch one.|Config T, и мы назовем это, переключите один.
Let's keep the thing simple, SW1.|Давайте будем проще, SW1.
Now, let's first take a look at the VLANs that exist by default.|Теперь давайте сначала посмотрим на VLAN, которые существуют по умолчанию.
Do show VLAN, and you see everything is part of VLAN 1.|Покажите VLAN, и вы увидите, что все является частью VLAN 1.
All the ports are active on VLAN 1.|Все порты активны в VLAN 1.
We're attached to port I believe three and four, if I'm not mistaken.|Мы привязаны к порту, кажется, третьему и четвертому, если я не ошибаюсь.
Yes we are, three and four.|Да, трое и четверо.
Okay.|Ладно.
So, but they're both different VLANs.|Итак, но это разные VLAN.
So let's go ahead and create the VLANs first.|Итак, давайте сначала создадим сети VLAN.
So we're going to go VLAN 100.|Итак, мы собираемся перейти на VLAN 100.
Wow, you just created a VLAN.|Вау, вы только что создали VLAN.
Hold on to your pants, okay?|Держись за штаны, хорошо?
That's just creating a VLAN right there.|Это просто создание VLAN прямо здесь.
VLAN 100.|VLAN 100.
You created a VLAN.|Вы создали VLAN.
But, you should give your VLAN a name.|Но вы должны дать своей VLAN имя.
If you don't give it a name.|Если вы не дадите ему имя.
It's gonna assign itself its own name, but it's gonna be a number,|Он присвоит себе собственное имя, но это будет номер,
it's gonna be like 00100, or 0100.|это будет как 00100 или 0100.
Something like that.|Что-то такое.
You don't want that.|Вы этого не хотите.
We're not computers yet, so we identify things by name.|Мы еще не компьютеры, поэтому мы идентифицируем вещи по именам.
So give VLAN 100 name, let's call VLAN 100, let's call it name faculty.|Итак, дайте VLAN 100 имя, давайте назовем VLAN 100, назовем его факультетом.
Boom.|Бум.
And let's, and let's create the other one.|И давайте, и давайте создадим еще один.
VLAN 101, Enter.|VLAN 101, введите.
Name, and let's call this students.|Назовите и назовем это студентами.
All right?|Отлично?
So, let's exit.|Итак, выходим.
Exit, like you would in the exam, and do a show VLAN.|Выйдите, как на экзамене, и сделайте шоу VLAN.
So now, we have two VLANs that we created.|Итак, у нас есть две сети VLAN, которые мы создали.
But we yet have to assign to any ports.|Но нам еще нужно назначить какие-либо порты.
We haven't assigned the VLANs to any ports, ok?|Мы не назначали VLAN ни одному порту, хорошо?
So let's go ahead and go to the other particular the other switch,|Итак, давайте перейдем к другому переключателю,
and let's do the same thing.|и давайте сделаем то же самое.
All right, because you've got both VLANs over there.|Хорошо, потому что у вас есть обе VLAN.
We got enable, config T, and then we're going to do VLAN 100, name faculty,|У нас есть enable, config T, а затем мы собираемся сделать VLAN 100, назовите факультет,
VLAN 101, name students.|VLAN 101, назовите студентов.
Do WR, do show VLAN.|Сделай WR, покажи VLAN.
If not you can during the test.|В противном случае вы можете во время теста.
There they are, faculty students, and you make sure that it says students on this side as well, not just student.|Вот они, студенты факультета, и вы убедитесь, что на этой стороне написано и студенты, а не только студенты.
Okay, students as well, and faculty.|Ладно, студенты и преподаватели.
All right, so we have both VLANs.|Хорошо, у нас есть обе VLAN.
Now, that's all it is to creating and naming a VLAN, that's all it is.|Вот и все, что нужно для создания и присвоения имени VLAN, вот и все.
So all we we'll go, what we're gonna do now is we're going to assign the VLANs to their particular ports.|Итак, все, что мы собираемся сделать, сейчас мы собираемся назначить VLAN их конкретным портам.
So in this case, VLAN 100 will be assigned to port three on switch one.|Таким образом, в этом случае VLAN 100 будет назначен на порт три на первом коммутаторе.
And VLAN 100 will be assigned to port three on switch two,|И VLAN 100 будет назначен порту три на коммутаторе два,
so, and then four one and so forth, okay?|итак, а потом четыре и так далее, ладно?
So let's go ahead and do that.|Так что давайте продолжим и сделаем это.
So VLAN 100 on port three, so we gotta go config T.|Итак, VLAN 100 на третьем порту, поэтому нам нужно настроить T.
We go inside that port interface F0/3|Заходим внутрь интерфейса этого порта F0 / 3
ENTER.|ВОЙТИ.
Now.|Сейчас.
[BLANK_AUDIO]|[BLANK_AUDIO]
When, when you assign VLANs you must assign them the ports,|Когда при назначении VLAN необходимо назначить им порты,
by default, they're set to dynamic auto.|по умолчанию они настроены на динамический автоматический режим.
You need to put them as an access port.|Ставить их нужно как порт доступа.
Access port.|Порт доступа.
To assign the VLAN.|Назначить VLAN.
[INAUDIBLE] Tracers [UNKNOWN] forgiven.|[Неразборчиво] Трассеры [НЕИЗВЕСТНО] прощены.
So you go switch, tch, port mode access,|Итак, вы идете switch, tch, доступ в режим порта,
and then you tell it switch port access VLAN.|а затем вы говорите ему переключить порт доступа к VLAN.
This is 100.|Это 100.
So now, VLAN 100 is assigned to port F 03,|Итак, теперь VLAN 100 назначен на порт F 03,
so I'm just gonna [INAUDIBLE] now.|так что я просто собираюсь [НЕРАЗБОРЧИВО] сейчас.
I'm gonna go to a port.|Я пойду в порт.
I'm gonna go to four.|Я пойду в четыре.
I'm gonna hit ENTER.|Я нажму ENTER.
I'm gonna go to switch port mode access,|Я собираюсь переключить режим доступа к порту,
turning the mode of that port as an access port.|переключение режима этого порта как порта доступа.
And then I'm going to go ahead and tell it which VLAN is that gonna be a part of, which is VLAN 101.|А затем я собираюсь сказать ему, частью какой VLAN будет эта сеть, а именно VLAN 101.
That's exit, let's do it the proper way for the exam.|Это выход, давайте сделаем это как следует на экзамене.
Exit.|Выход.
Do.|Делать.
Not do.|Не делать.
Copy, run, start, ENTER ENTER, show VLAN.|Копировать, запустить, запустить, ENTER, ENTER, показать VLAN.
Now you have faculty, which is in port three, and students, which is in port four.|Теперь у вас есть преподаватели, которые находятся в третьем порту, и студенты, которые находятся в четвертом порту.
Awesome.|Потрясающие.
[BLANK_AUDIO]|[BLANK_AUDIO]
Right?|Правильно?
And we're gonna the some thing over here,|И мы собираемся кое-что здесь,
in the other VLAN.|в другой VLAN.
[BLANK_AUDIO]|[BLANK_AUDIO]
Exit.|Выход.
And then we're gonna go [NOISE]|А потом мы пойдем [NOISE]
VLAN 100, main faculty,|VLAN 100, главный факультет,
VLAN 101, name students.|VLAN 101, назовите студентов.
No, we just did that, sorry.|Нет, мы только что сделали это, извините.
Sorry, sorry, sorry, sorry.|Простите, прости, прости, прости.
I don't know why I'm doing that, okay.|Я не знаю, зачем я это делаю, ладно.
I'm assigning it now, so sorry.|Сейчас назначаю, извините.
Now back to the interface.|Теперь вернемся к интерфейсу.
F0/3.|F0 / 3.
We just, well, we just created it, so never mind.|Мы просто, ну, мы только что создали это, так что неважно.
In that's row three.|В этом ряду три.
So we go switch, tch, port mode access and then switch port,|Итак, мы переходим к переключению, tch, доступу в режим порта, а затем к переключению порта,
too many p's, access VLAN 100.|слишком много p, доступ к VLAN 100.
Another [INAUDIBLE], port four.|Другой [НЕРАЗБОРЧИВО], порт четыре.
Mode Access, and then, VLAN 101.|Mode Access, а затем VLAN 101.
Ctrl+Z WR.|Ctrl + Z WR.
Show VLAN.|Показать VLAN.
And now we have the same thing.|И теперь у нас то же самое.
100 VLAN on port three.|100 VLAN на третьем порту.
101 on port four.|101 на четвертом порту.
Not that it really matter, I just want to stay consistent.|Не то чтобы это действительно имело значение, я просто хочу оставаться последовательным.
It doesn't matter which port I assigned on the other switch, the faculty one, but just to be the same.|Не имеет значения, какой порт я назначил на другом коммутаторе, факультетском, просто чтобы он был таким же.
So, what should happen, should happen, is that now host one should be able to ping host three, cuz they're on the same network.|Итак, что должно произойти, должно произойти, так это то, что теперь хост 1 должен иметь возможность пинговать хост 3, потому что они находятся в одной сети.
This is 100.1, this is 100.2.|Это 100,1, это 100,2.
Let's see, what happens pray tell.|Посмотрим, что будет, молитесь.
Ping, and you can't see that cause I'm in your way.|Пинг, и ты не видишь этого, потому что я на твоем пути.
Bring that over here.|Принеси это сюда.
Pinging 192.168.100.2.|Пинг 192.168.100.2.
I want to try the first time out is because we're going though an ethernet network.|Я хочу попробовать в первый раз, потому что мы идем через сеть Ethernet.
Request timed out.|Истекло время запроса.
Mm-hm.|Мм-хм.
[BLANK_AUDIO]|[BLANK_AUDIO]
Uh-oh, what's going on?|Ой, что происходит?
[BLANK_AUDIO]|[BLANK_AUDIO]
It's not able to, ping across, what's the problem?|Не может пинговать, в чем проблема?
Let's try the other one.|Попробуем другой.
Let's try, VLAN101.|Попробуем, VLAN101.
[BLANK_AUDIO]|[BLANK_AUDIO]
And again let's bring it this way so you guys can see.|И снова давайте представим это так, чтобы вы, ребята, могли видеть.
[BLANK_AUDIO]|[BLANK_AUDIO]
Ping 192.168.101.2.|Пинг 192.168.101.2.
[BLANK_AUDIO]|[BLANK_AUDIO]
And again, the first time out, I always say cuz it's ethernet,|И снова, в первый раз, я всегда говорю, потому что это Ethernet,
but it looks like it's gonna continue to time out.|но похоже, что тайм-аут будет и дальше.
That's not a go through, let's see what happens.|Это не пройти, посмотрим, что будет.
What is the problem?|В чем проблема?
Must be the IP addressing, right?|Должен быть IP-адрес, верно?
Am I IP addressing wrong?|Я неправильно ввожу IP-адрес?
No, the IP addressing is correct.|Нет, IP-адрес правильный.
I'm pretty sure it's 101, I was pinging 102, 101.2.|Я почти уверен, что это 101, пинговал 102, 101.2.
So, it's not that.|Значит, дело не в этом.
See, this is the problem.|Видите, это проблема.
And this looks like a very similar example that you're,|И это похоже на очень похожий пример, что вы,
may run into in your examination.|может наткнуться на ваш экзамен.
The only VLAN, the only VLAN that can go across, because ports one and two that you see here, ports one and two,|Единственная VLAN, единственная VLAN, которая может проходить, потому что порты один и два, которые вы видите здесь, порты один и два,
ports one and two, those are access ports.|порты один и два, это порты доступа.
But they should be trunk ports.|Но они должны быть магистральными портами.
From switch to switch or switch to router, those ports should be trunk when dealing with VLANs.|От коммутатора к коммутатору или от коммутатора к маршрутизатору эти порты должны быть магистральными при работе с VLAN.
Only the native VLAN is allowed to go across access ports, or trunk ports.|Только собственная VLAN может проходить через порты доступа или транковые порты.
So, let's prove that theory.|Итак, давайте докажем эту теорию.
Let's go ahead and grab, a PC.|Давайте, возьмем компьютер.
Onto this side.|На эту сторону.
Let's put one on this side over here.|Давай положим сюда вот эту сторону.
[BLANK_AUDIO]|[BLANK_AUDIO]
I'm just going to connect it to any random port.|Я просто подключу его к любому случайному порту.
[BLANK_AUDIO]|[BLANK_AUDIO]
Let's pick Let's pick port 20 here,|Давайте выберем Давайте выберем здесь порт 20,
just to be completely different, than everybody else.|просто быть совершенно другим, чем все остальные.
All right.|Отлично.
[BLANK_AUDIO]|[BLANK_AUDIO]
And then let's use, let's use an easy IP address.|А затем давайте использовать простой IP-адрес.
Let's just use 1.1.1.1.|Давайте просто воспользуемся 1.1.1.1.
Yes I know that's a public IP address.|Да, я знаю, что это публичный IP-адрес.
Well this will be too, obviously.|Ну, это тоже будет очевидно.
And then, yeah, we'll leave it at the default, forget about the gateway,|А потом, да, оставим по умолчанию, про шлюз забудем,
we're not worried about a gateway anyway.|нас все равно не беспокоит шлюз.
This is just to prove a point.|Это просто чтобы доказать свою точку зрения.
All right, and this will be 1.1.1.1|Хорошо, а это будет 1.1.1.1
default mask, 1.1.1.1 default mask.|маска по умолчанию, маска по умолчанию 1.1.1.1.
So, everything is green.|Итак, все зеленое.
That's awesome.|Это потрясающе.
And let's see we can ping those, ping 1.1.1.2.|И давайте посмотрим, мы можем пинговать их, пинговать 1.1.1.2.
And we can.|А мы можем.
Why is that?|Это почему?
Because particular port, port 20, and let me go ahead and go inside switch two, it'll be the same thing on switch one, CTRL+C.|Поскольку конкретный порт, порт 20, и позвольте мне пойти дальше и войти внутрь коммутатора 2, на первом коммутаторе будет то же самое, CTRL + C.
I'm gonna to do a show VLAN.|Я собираюсь устроить шоу VLAN.
Well, port 20, ladies and gentlemen, is part of VLAN 1.|Итак, порт 20, дамы и господа, является частью VLAN 1.
So VLAN 1 at this point is the native VLAN, the admin VLAN,|Итак, VLAN 1 на данный момент является собственной VLAN, административной VLAN,
the management VLAN, the admin VLAN,|VLAN управления, VLAN администратора,
whatever you wanna call it.|как бы вы это ни называли.
That native VLAN is the only one allowed to go across access ports or trunk ports.|Эта собственная VLAN - единственная, которой разрешено проходить через порты доступа или транковые порты.
Because the, in the header of the native VLAN there's something called a PVID, a Personal VLAN Identifier.|Потому что в заголовке собственной VLAN есть что-то, называемое PVID, персональный идентификатор VLAN.
That when they see it come across, hey,|Что, когда они видят это, эй,
that's the nativeVLAN, let it through,|вот и роднойVLAN, пропустите,
let it through, let it through.|пропустите это, позвольте этому пройти.
But every other VLAN, 2, right,|Но все остальные VLAN, 2, верно,
2 through all the way to 1001 must go across trunk ports.|2 до 1001 должны проходить через транковые порты.
Must go across trunk ports.|Должен проходить через порты магистрали.
Which means that you need to trunk your port.|Это означает, что вам нужно связать свой порт.
Let's see, I'll come over here and do it on this one, switch one.|Посмотрим, я приду сюда и сделаю это на этом, поменяю.
[BLANK_AUDIO]|[BLANK_AUDIO]
All right?|Отлично?
There's two.|Их двое.
And I'm gonna go,|И я пойду,
I wanna do a range command, and start getting used to this.|Я хочу выполнить команду диапазона и начать к этому привыкать.
INT RANGE F0/1-2, simple enough.|INT RANGE F0 / 1-2, достаточно просто.
Now you're in config if range.|Теперь вы находитесь в конфигурации, если диапазон.
So whatever you do now is going to take affect in those two particular ports.|Итак, что бы вы ни делали сейчас, это повлияет на эти два конкретных порта.
And you can go switch port mode trunk, okay?|И вы можете переключить режим порта на транк, хорошо?
And if you were to do now show int trunk,|И если бы вы теперь показывали int trunk,
now you see that F01 and F02, the trunking mode is on.|теперь вы видите, что F01 и F02, транкинговый режим включен.
802, 802.1q encapsulation is on for the, those, those ports.|Инкапсуляция 802, 802.1q включена для этих портов.
And if you come over here you see how it's changing, it's changing,|И если вы подойдете сюда, вы увидите, как это меняется, это меняется,
something just happened.|что-то только что произошло.
Span tree's going hello, what's going on here?|Привет, Span tree, что здесь происходит?
So, span tree did its thing.|Итак, Span Tree сделал свое дело.
Not really, span tree didn't do anything.|Не совсем, Span Tree ничего не сделал.
It's, it's actually that it's changing modes from, from,|На самом деле он меняет режимы с, с,
dynamic auto to now a trunking port.|динамический авто теперь транкинговый порт.
And if you look at these ports over here,|И если вы посмотрите на эти порты вот здесь,
do a CTRL+C,|сделать CTRL + C,
and do the same command showing trunk.|и выполните ту же команду, показывающую ствол.
You see that automatically these ports down here got trunked as well.|Вы видите, что автоматически эти порты здесь тоже были соединены.
You don't have to go down there and manually trunk those ports.|Вам не нужно спускаться туда и вручную соединять эти порты.
Once you trunk them on one side, since they're connected together,|Как только вы соедините их с одной стороны, поскольку они соединены вместе,
it's gonna go ahead and trunk the ones on the other switch.|он пойдет дальше и соединит те, что на другом переключателе.
So, based on the theory, now VLAN, or host one on VLAN 100 should be able to ping 100.2.|Итак, исходя из теории, теперь VLAN или хост в VLAN 100 должны иметь возможность пинговать 100.2.
Now we can, because it's going across a trunk port.|Теперь мы можем, потому что он проходит через магистральный порт.
So that's important to remember.|Так что это важно помнить.
Let's test the other one,|Давайте протестируем другой,
[BLANK_AUDIO]|[BLANK_AUDIO]
101.2.|101.2.
And now you get a reply.|И теперь вы получите ответ.
So that lets you know right there.|Так что вы сразу узнаете.
Cuz you will see a very similar scenario okay?|Потому что вы увидите очень похожий сценарий, хорошо?
On your examination.|На вашем осмотре.
Where you're gonna have one particular VLAN that's able to go back and forth without an issue.|Где у вас будет одна конкретная VLAN, которая может без проблем перемещаться вперед и назад.
But the others cannot go across without the issue.|Но другие не могут обойтись без проблем.
It cannot go across because we have an issue.|Это невозможно, потому что у нас есть проблема.
What is that problem?|Что это за проблема?
The problem is that the port's going from switch to switch are not trunked because,|Проблема в том, что порт, переходящий от коммутатора к коммутатору, не транкинговый, потому что:
again, the only VLAN that can go across a,|опять же, единственная VLAN, которая может проходить через
an access port is the native VLAN.|порт доступа - это собственная VLAN.
All other VLANs must go across trunk ports.|Все остальные сети VLAN должны проходить через транковые порты.
And the reason that is is because those other VLANs get tagged.|Причина в том, что эти другие сети VLAN помечаются.
That's where the f, the, the phrase tagged VLANs and untagged VLANs.|Вот где f, the, фраза VLAN с тегами и без тегов.
When we talk about untagged VLANs, we're talking about VLAN 1.|Когда мы говорим о немаркированных VLAN, мы говорим о VLAN 1.
When we're talking about tagged VLANs we're talking about everything else.|Когда мы говорим о тегированных VLAN, мы говорим обо всем остальном.
Because tagged VLANs are the ones that have to go across those trunked ports.|Потому что тегированные VLAN - это те, которые должны проходить через эти транковые порты.
So that's very, very important to know.|Это очень, очень важно знать.
So that's it, that's all there is to creating a VLAN, assigning a VLAN,|Вот и все, что нужно для создания VLAN, назначения VLAN,
well creating the VLAN, giving the VLAN a name, assigning the VLAN to a port.|хорошо создать VLAN, дать VLAN имя, назначить VLAN порту.
And then making sure that, if you're going from switch to switch,|А затем убедитесь, что если вы собираетесь с переключателя на переключатель,
that those ports that are going from switch to switch are trunked.|что те порты, которые переходят от коммутатора к коммутатору, являются транковыми.
So all the VLANs, other than the native VLAN can also go across those ports.|Таким образом, все сети VLAN, кроме собственной VLAN, также могут проходить через эти порты.
All right, simple as that, not a problem.|Ладно, все просто, не проблема.
I will see you In the next lesson.|Увидимся на следующем уроке.
[BLANK_AUDIO]|[BLANK_AUDIO]