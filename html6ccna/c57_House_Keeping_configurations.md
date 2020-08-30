D:\mailCloud\prjother\tmp\1\c57_House Keeping configurations.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
All right.|Отлично.
We're ready to configure.|Мы готовы к настройке.
Are you?|Ты?
Of course, you are.|Конечно же.
Now, we know [BLANK_AUDIO],|Теперь мы знаем [BLANK_AUDIO],
how to navigate through the iOS.|как ориентироваться в iOS.
So, the first thing that we're going to configure is what they call administrative configuration, or as I like to call it,|Итак, первое, что мы собираемся настроить, это то, что они называют административной конфигурацией, или, как я люблю это называть,
basic housekeeping,|базовая уборка,
which I wanna give you more than what you actually need, as usual.|что я хочу дать вам больше, чем то, что вам действительно нужно, как обычно.
So, we're gonna develop a little topology which you've learned earlier.|Итак, мы собираемся разработать небольшую топологию, которую вы узнали ранее.
How to connect routers and stuff,|Как подключить роутеры и прочее,
navigating through the Packet Tracer and all that.|навигация по Packet Tracer и все такое.
So, what we're gonna do is we'll make it simple.|Итак, что мы собираемся сделать, так это сделать это проще.
We'll do two routers.|Сделаем два роутера.
All right?|Отлично?
We'll put two switches.|Поставим два переключателя.
We're not going to configure the switches.|Мы не собираемся настраивать переключатели.
Well, will we?|Хорошо, а мы?
Will we?|Будем ли мы?
Yeah, yeah we probably will.|Да, возможно, мы будем.
We'll do the routers.|Сделаем роутеры.
We'll put two switches.|Поставим два переключателя.
Nah, we won't.|Нет, не будем.
We'll put two switches, and then, we'll go ahead and put two PCs.|Мы поставим два переключателя, а затем поставим два ПК.
And we're gonna do the administrator configurations of them only.|И мы собираемся делать настройки администратора только для них.
All right?|Отлично?
The administrative configurations of them only.|Только административные конфигурации из них.
And I will explain each command as I go through it.|И я объясню каждую команду по мере ее выполнения.
So, we're gonna go ahead and go through the 1841.|Итак, мы собираемся пройти через 1841 год.
And some of you, as we do this, they'll be saying man, we don't do this at work.|И некоторые из вас, когда мы это делаем, они будут говорить, чувак, мы не делаем этого на работе.
We don't have to do all this stuff.|Нам не нужно делать все это.
You're taking a certification.|Вы проходите сертификацию.
Guess what, you better know it.|Угадай, тебе лучше это знать.
[BLANK_AUDIO].|[BLANK_AUDIO].
When you go to your job, then you can go do whatever you want.|Когда вы идете на работу, вы можете делать все, что хотите.
Then, you'll be CCNA certified, then you'll get that extra raise.|Затем вы получите сертификат CCNA и получите дополнительное повышение.
Then, you'll be the man or the woman.|Тогда вы будете мужчиной или женщиной.
But if you don't get that certification,|Но если вы не получите этот сертификат,
you'll, you'll just be the tech.|ты будешь просто техником.
All right?|Отлично?
So, you need the certification.|Итак, вам нужна сертификация.
You want the certification.|Вам нужна сертификация.
So, pay attention to the certification.|Итак, обратите внимание на сертификацию.
All right.|Отлично.
We're gonna use straight-through cable from PC to switch.|Мы будем использовать прямой кабель от ПК для переключения.
And the reason, and how I plug things in,|И причина, и как я включаю вещи,
ladies and gentlemen, there is a method to the madness, please.|дамы и господа, есть метод безумия, пожалуйста.
I plug it in a certain way, but then sometimes, I get emails back people say,|Я подключаю его определенным образом, но иногда мне приходят письма, которые говорят:
look Las, I did exactly like you did, it's not working.|Послушай, Лас, я сделал в точности так же, как ты, не работает.
And then, I look at the lab, it's exactly,|А потом я смотрю на лабораторию, это точно,
it's not exactly like I did it.|это не совсем так, как я.
And that's why it's not working, okay?|И поэтому не работает, ладно?
So please, if you're gonna replicate these labs, do it exactly as I do it.|Так что, пожалуйста, если вы собираетесь воспроизвести эти лабораторные работы, делайте это точно так же, как я.
And plug it into the proper ports, all right?|И воткните его в соответствующие порты, хорошо?
Which when you send it back to me, will be easier to troubleshoot.|Когда вы отправите его мне, будет легче устранить неполадки.
All right?|Отлично?
That's the same thing I do in the classroom.|То же самое я делаю в классе.
Everybody plugs in everything to the exact same ports.|Все подключают все к одним и тем же портам.
So, if I have 30 students.|Итак, если у меня 30 учеников.
I don't have to look at 30 different configurations.|Мне не нужно рассматривать 30 различных конфигураций.
Just gonna go one topical configuration.|Пойду в одну актуальную конфигурацию.
Now, does it mean you always have to do it this way?|Значит ли это, что вы всегда должны так делать?
Of course not.|Конечно нет.
Once you get out there, you can do however you want to do it.|Как только вы выберетесь отсюда, вы сможете делать все, что хотите.
But in the classroom, this is how you do it.|Но в классе это то, как вы это делаете.
All right, to make it easier on me.|Хорошо, чтобы мне было легче.
Alright, and for you to understand the concept,|Хорошо, и чтобы вы поняли концепцию,
because that's what you're learning.|потому что это то, что вы изучаете.
Now, between routers we're gonna emulate,|Теперь между маршрутизаторами мы будем эмулировать,
we're gonna use a WIC-2T.|мы будем использовать WIC-2T.
And just so you know, the difference between a WIC-1T and a WIC-2T,|И чтобы вы знали, разница между WIC-1T и WIC-2T,
the WIC-2T they call it the smart serial,|WIC-2T они называют его умным серийником,
the author doesn't even know why the call it the smart serial but hey, it's called the smart serial.|автор даже не знает, почему его называют умным сериалом, но эй, он называется умным сериалом.
It has two more ports instead of having just one huge 60 pin port.|У него есть еще два порта вместо одного огромного 60-контактного порта.
It has two ports.|Имеет два порта.
Bandwidth is a lot more.|Пропускная способность намного больше.
Definitely, the connectors or the cable that goes to it,|Однозначно разъемы или кабель, который к нему идет,
is gonna be completely different.|будет совершенно другим.
So, in the real world, when you are purchasing WIC cards,|Итак, в реальном мире, когда вы покупаете карты WIC,
make sure you make the distinction between WIC-1T and WIC-2T.|убедитесь, что вы проводите различие между WIC-1T и WIC-2T.
Okay?|Ладно?
Because your serial cables, will be completely different.|Потому что ваши последовательные кабели будут совершенно другими.
All right?|Отлично?
So, we're gonna use WIC-2Ts and we're gonna put it on slot zero.|Итак, мы будем использовать WIC-2T и поместить его в нулевой слот.
Slot zero.|Слот нулевой.
They're not hot swappable.|Они не поддерживают горячую замену.
They're not hot swappable.|Они не поддерживают горячую замену.
So, make sure you turn off the router when you're putting in these cards.|Итак, не забудьте выключить маршрутизатор, когда вставляете эти карты.
Close.|Близко.
Laz, why are you using WIC-2Ts?|Лаз, зачем ты пользуешься WIC-2T?
Because I, I like to.|Потому что мне нравится.
That's all.|Вот и все.
[BLANK_AUDIO].|[BLANK_AUDIO].
Okay.|Ладно.
[BLANK_AUDIO].|[BLANK_AUDIO].
All righty, then.|Тогда ладно.
[BLANK_AUDIO].|[BLANK_AUDIO].
Now, I'm gonna go ahead and get the DCE cable,|А теперь я возьму кабель DCE,
and put it on the 000 and then, plug it into the here.|и поместите его на 000, а затем подключите его сюда.
Now, put the S01.|Теперь ставим S01.
All righty then, we're creating a little topology.|Хорошо, создадим небольшую топологию.
Look at that, how cool.|Посмотри, как круто.
All right.|Отлично.
We got a little topology there.|У нас есть небольшая топология.
Now, I'm gonna give you a little review.|Теперь я дам вам небольшой обзор.
How many broadcast domains and collision domains do we have?|Сколько у нас широковещательных доменов и коллизионных доменов?
Quickly.|Быстро.
Come on.|Давай.
I know you know.|Я знаю, что ты знаешь.
I know you know.|Я знаю, что ты знаешь.
I think I heard somebody say it.|Кажется, я слышал, как кто-то это сказал.
I think, I think you're right.|Думаю, ты прав.
I mean, if I heard you correctly.|Я имею в виду, если я правильно вас расслышал.
You have, one broadcast domain,|У вас есть один широковещательный домен,
two broadcast domains, three broadcast domains.|два широковещательных домена, три широковещательных домена.
Very good, very good.|Очень хорошо, очень хорошо.
How many collision domains do we have?|Сколько у нас коллизионных доменов?
One, two, three, four,|Один два три четыре,
five, cuz each port, each port on a router, right.|пять, потому что каждый порт, каждый порт на маршрутизаторе, верно.
Each port on a router is a collision domain.|Каждый порт на маршрутизаторе является доменом конфликтов.
You got one, two, you have three, four,|У тебя один, два, у тебя три, четыре,
five.|пять.
Broadcast domains, right?|Широковещательные домены, верно?
One, two, and then, three.|Раз, два, а потом, три.
And we move this.|И мы перемещаем это.
Think think it doesn't like my finger anymore, it's mad at me.|Думаю, мне больше не нравится мой палец, он злится на меня.
Move it over this way.|Переместите его сюда.
Okay?|Ладно?
So, now, we're gonna put the IP scheme oh,|Итак, теперь мы добавим схему IP, о,
oh no, yes, the dreaded IP.|о нет, да, ужасный IP.
[BLANK_AUDIO].|[BLANK_AUDIO].
All right.|Отлично.
So, we're going to use a ten, and zoom in all the way.|Итак, мы собираемся использовать десятку и полностью увеличивать масштаб.
There you go.|Вот так.
Cuz, you may be able to see it, but you know me.|Потому что ты можешь это видеть, но ты меня знаешь.
I can barely see it, and I'm standing,|Я едва вижу это, а я стою,
standing right in front of it.|стоя прямо перед ним.
[BLANK_AUDIO].|[BLANK_AUDIO].
All right.|Отлично.
Figure out a little basic network going on here, we got the sider 30,|Разберитесь с небольшой базовой сетью, которая здесь происходит, мы получили sider 30,
which gives us two IP addresses on the top, router to router.|что дает нам два IP-адреса сверху, от маршрутизатора к маршрутизатору.
Then, we're just gonna pick at random here, 192, 192.168.1.|Тогда мы просто выберем здесь наугад, 192, 192.168.1.
That's not 68,|Это не 68,
that's 38, 68.1.0/24.|это 38, 68.1.0 / 24.
Default class c mask, that's why we have our class c address.|Маска класса c по умолчанию, поэтому у нас есть адрес класса c.
[BLANK_AUDIO].|[BLANK_AUDIO].
Copy that.|Скопируй это.
And then, you just go in there and change that to a two.|А затем вы просто заходите и меняете это значение на два.
So, we have our basic setup, right?|Итак, у нас есть базовая настройка, верно?
The first things that I like to do,|Первое, что мне нравится делать,
because eventually,|потому что в конце концов,
we're gonna make this lab grow, grow, grow and grow, we're gonna go ahead and put the IP addresses on the computers.|мы собираемся заставить эту лабораторию расти, расти, расти и расти, мы продолжим и разместим IP-адреса на компьютерах.
Now, before we do, before we do.|Теперь, прежде чем мы это сделаем, прежде чем мы это сделаем.
I have my own little standard.|У меня есть свой маленький стандарт.
I know that everybody, that Microsoft has it's standard for assigning IPs.|Я знаю, что все, что у Microsoft есть стандарт для назначения IP-адресов.
And I'm sure Cisco has it's standard for assigning IPs.|И я уверен, что у Cisco есть стандарт назначения IP-адресов.
And I'm sure everybody in the world has their standard for assigning IPs.|И я уверен, что у каждого в мире есть свой стандарт назначения IP-адресов.
I like to use the first available IP address for the host, and the last available IP address for the gateway.|Мне нравится использовать первый доступный IP-адрес для хоста и последний доступный IP-адрес для шлюза.
So, please do it that way.|Так что, пожалуйста, сделайте это так.
Okay?|Ладно?
Why do I do it that way?|Почему я так делаю?
Visualization purposes, visualization.|Цели визуализации, визуализация.
Once I see a one [UNKNOWN], and I remember, oh,|Как только я вижу [НЕИЗВЕСТНО] и вспоминаю, о,
the last available was the gateway.|последним доступным был шлюз.
So, I already, I already know that, right off the bat.|Итак, я уже, я это уже знаю, сразу же.
Make it simple on my, on my brain.|Сделайте это просто для меня, для моего мозга.
Doesn't have to think that much.|Не нужно так много думать.
That I know what IP address is what.|Что я знаю, что такое IP-адрес.
Because you do need, not only documentation, but you need to be aware of the scheme that you're using for your particular topology.|Потому что вам нужна не только документация, но и нужно знать схему, которую вы используете для своей конкретной топологии.
All right.|Отлично.
So, we're gonna go to PC zero.|Итак, мы перейдем на нулевой ПК.
Alright.|Хорошо.
And we're not going into our routers yet.|И мы еще не входим в наши роутеры.
We're just getting things ready Right?|Мы просто готовим вещи, верно?
Go to IP configuration.|Перейдите к настройке IP.
We're gonna put the IP address.|Мы собираемся указать IP-адрес.
Can you see that?|Вы можете видеть, что?
Let me move that that way.|Позвольте мне сделать то же самое.
Oh, wrong way, ha ha.|Ой, неправильно, ха-ха.
[BLANK_AUDIO]|[BLANK_AUDIO]
There we go.|Вот и все.
And this is 1.00192.168.1.1.|А это 1.00192.168.1.1.
Tab.|Табл.
It's gonna put a default there, so tab again.|Там будет значение по умолчанию, так что снова вкладка.
192.168.1.2.|192.168.1.2.
254.|254.
So here we got 1.1 for the IP address of the host.|Итак, мы получили 1.1 для IP-адреса хоста.
We got a default 255.255.255.0, and we have a 1921681.254 40 gateway.|У нас есть 255.255.255.0 по умолчанию, и у нас есть шлюз 1921681.254 40.
So, we got that going.|Итак, мы получили это.
Let's go ahead and do that on the second PC.|Давайте продолжим и сделаем это на втором ПК.
Same thing, except there is going to be 2.1 and 2.254.|То же самое, только будет 2.1 и 2.254.
Pretty simple, pretty simple, nothing major.|Довольно просто, довольно просто, ничего особенного.
And make sure, am I moving in the right way?|И убедитесь, правильно ли я двигаюсь?
Ruh roh, that way, okay.|Рух-ро, туда, ладно.
Go to the IP configuration 192.168.1.1.|Заходим в конфигурацию IP 192.168.1.1.
Tab, tab, why tab, tab?|Вкладка, вкладка, почему вкладка, вкладка?
Because it puts in the default anyway,|Поскольку он все равно ставит значение по умолчанию,
that's what we're using.|вот что мы используем.
192.168.|192.168.
You see?|Ты видишь?
You guys didn't warn me.|Вы, ребята, меня не предупреждали.
You guys gotta tell me these things.|Вы, ребята, должны мне это рассказать.
It's 2.1.|Это 2.1.
See, you're not telling me.|Видишь, ты мне не говоришь.
You gotta let me know.|Дай мне знать.
192.168.2.254.|192.168.2.254.
All right.|Отлично.
So you got the IPs and the gateways for the PCs.|Итак, у вас есть IP-адреса и шлюзы для ПК.
That's wonderful.|Это прекрасно.
Now all we're gonna do is, like I said,|Теперь все, что мы собираемся сделать, как я уже сказал,
the basic housekeeping on the actual routers.|базовое обслуживание реальных маршрутизаторов.
Now, router one here the name, it's router one, and there's router two, so that's what we'll call it, so we don't have any confusions.|Итак, здесь имя маршрутизатора один, это маршрутизатор один, а есть маршрутизатор два, так что мы и будем его называть, чтобы не было путаницы.
Now pay attention with the packet tracer that you have,|Теперь обратите внимание на имеющийся у вас пакетный трассировщик,
you see you have a little clock right there?|Вы видите, что у вас тут есть маленькие часы?
That's your DCE portion of the once we get into the interfaces,|Это ваша часть DCE, как только мы перейдем к интерфейсам,
that's where you put your clock rate.|вот где вы ставите свою тактовую частоту.
You see the little clock?|Вы видите маленькие часы?
You put a little, you put the clock rates,|Ставишь немного, часы ставишь,
all right.|отлично.
No clock rate?|Нет тактовой частоты?
You're gonna get a layer 2 issue.|У вас будет проблема со вторым уровнем.
What's layer 2?|Что такое слой 2?
Right, the data link layer.|Правильно, уровень передачи данных.
Encapsulation, CRC frames, right?|Инкапсуляция, кадры CRC, верно?
You have you know if you've got CRC frames,|Вы знаете, есть ли у вас кадры CRC,
you have a mismatch in duplex speeds.|у вас несоответствие скоростей дуплексной печати.
All right, but you normally, they'll be asking you to have you know, clocking,|Хорошо, но обычно они будут просить вас знать, часы,
you're not receiving any clocking.|вы не получаете никаких часов.
All right, so if you have internal CSU/DSUs, or you're providing clocking for your particular routers, then you need to make sure you put in a clock rate.|Хорошо, поэтому, если у вас есть внутренние блоки CSU / DSU или вы обеспечиваете синхронизацию для своих конкретных маршрутизаторов, вам необходимо убедиться, что вы установили тактовую частоту.
And it's the cable that's going to decide,|И это решит кабель,
all right,|отлично,
which is the DC, if you're using serial cables.|то есть DC, если вы используете последовательные кабели.
This is our crossover serial cables.|Это наши кроссоверные последовательные кабели.
One side is DC, one side is DT.|Одна сторона - DC, другая - DT.
The pins will determine which is which.|Штифты определят, что есть что.
Okay, do we need to get into that granularity of it?|Хорошо, нужно ли нам углубляться в детализацию?
No.|Нет.
If you go into a real world,|Если вы попадете в реальный мир,
do you need to look at the pin?|тебе нужно посмотреть на булавку?
Okay, I think it's pin 20?|Хорошо, я думаю, это контакт 20?
No.|Нет.
All right?|Отлично?
Cause that would freak me out when I was in the A plus.|Потому что это меня напугало, когда я был на пятёрке.
You had this huge thing, and the pin is like 50 or 100 pins, and you have to know each one of those pins.|У вас была эта огромная штука, а булавка - это 50 или 100 булавок, и вы должны знать каждую из этих булавок.
It was crazy.|Это было безумно.
But here, you know, it says, hey, there's a DC sign.|Но здесь, вы знаете, там написано: «Эй, это знак постоянного тока».
There's a DT sign.|Есть знак DT.
And routers is, all routers by default are DT.|А роутеры есть, все роутеры по умолчанию DT.
It's really your provider that does the clocking for you.|Это действительно ваш провайдер, который выполняет синхронизацию за вас.
But anyway, I digress.|Но в любом случае я отвлекся.
Let's go inside router one.|Пойдем внутрь роутера один.
And I'll move it that way, so you guys can see.|И я переставлю его туда, чтобы вы, ребята, могли видеть.
[SOUND] All right, so we booted up the router.|[ЗВУК] Хорошо, мы загрузили роутер.
And obviously, I mean, let me get out your way a little bit more here, so you can see good.|И, очевидно, я имею в виду, позвольте мне немного больше уйти от вас, чтобы вы могли видеть хорошее.
All right, there we can always say no.|Хорошо, мы всегда можем сказать «нет».
We're always gonna say no.|Мы всегда говорим «нет».
Laz, why do we always say no?|Лаз, почему мы всегда говорим нет?
Because you don't wanna run through the wizard.|Потому что ты не хочешь бегать через волшебника.
You can do it yourself from scratch.|Можно сделать самому с нуля.
It really doesn't take that much longer.|Это действительно не займет много времени.
Okay?|Ладно?
Or if you wanna just ask questions,|Или, если вы хотите просто задать вопросы,
type setup again, and you get right back into setup mode.|введите setup еще раз, и вы вернетесь в режим настройки.
But we're not gonna do things in setup mode, we're gonna do things from scratch.|Но мы не будем делать что-то в режиме настройки, мы будем делать все с нуля.
Navigation, enable, now we're in prose mode.|Навигация, включи, теперь в режиме прозы.
Config T, now we're in global configuration mode.|Config T, теперь мы в режиме глобальной конфигурации.
Now we type host name, not hosf but host.|Теперь мы вводим имя хоста, не хост, а хост.
The hostname cannot have any spaces.|В имени хоста не должно быть пробелов.
No spaces whatsoever.|Никаких пробелов.
Okay?|Ладно?
You can use underscores, but you can't use spaces.|Вы можете использовать подчеркивания, но не можете использовать пробелы.
So we're gonna call this R1, very simple,|Так что мы назовем это R1, очень просто,
very straight to the point.|очень прямо к делу.
Now we're going to start securing.|Теперь приступим к закреплению.
As you can see when I typed enable, and I went, it took me directly to privilege mode.|Как вы можете видеть, когда я набрал enable и перешел, меня сразу перевели в привилегированный режим.
We don't want that, so we're gonna secure it.|Мы этого не хотим, поэтому мы это обезопасим.
We're gonna go enable, now be careful, if you're typing in capital or lowercase, or you're trying to use proper grammar, all|Мы собираемся включить, теперь будьте осторожны, если вы набираете заглавные или строчные буквы или пытаетесь использовать правильную грамматику, все
right,|право,
you better make sure you know what these passwords are, or if not,|вам лучше убедиться, что вы знаете, что это за пароли, а если нет,
you're gonna have a world of hurt on top of you, all right?|у тебя будет мир боли сверху, хорошо?
Enable password Cisco.|Включить пароль Cisco.
Enable secret, okay, I'm kind of cockeyed that's why I can't, secret students.|Включите секрет, ладно, я самоуверенный, поэтому не могу, секретные студенты.
Both of these, both of these passwords,|Оба эти, оба эти пароля,
and I'll bring them up so you can see that.|и я подниму их, чтобы вы это увидели.
Both of these passwords are both called privilege mode passwords.|Оба этих пароля называются паролями привилегированного режима.
What does that mean?|Что это значит?
That when you type enable, it takes to privilege mode, for the privilege mode passwords.|Когда вы вводите enable, он переходит в привилегированный режим для паролей привилегированного режима.
So a question should come to your head.|Так что в голову должен прийти вопрос.
It's like, Laz, why are you then typing two separate passwords?|Это как, Лаз, почему ты тогда вводишь два разных пароля?
And I've had, believe me, I've asked,|И у меня было, поверьте, я просил,
that question has been asked to me a million times.|этот вопрос задавали мне миллион раз.
And, I got the answer for that, there's two of 'em.|И я получил на это ответ, их двое.
One, you need to know it for your certification, they're going to ask you.|Во-первых, вам нужно знать это для сертификации, они вас спросят.
All right, so you need to know it.|Хорошо, тебе нужно это знать.
And two, as your book states, and you've read,|И два, как сказано в вашей книге, и вы читали,
that if you need to go to an older IOS I believe it's under 12, 11, something.|что, если вам нужно перейти на более старую IOS, я считаю, что она младше 12, 11, что-то в этом роде.
Okay?|Ладно?
I don't remember the exact number.|Я не помню точное число.
If you need to go into an older IOS that does not support the secret,|Если вам нужно перейти на более старую IOS, которая не поддерживает секрет,
the secret syntax, at least you have a plain text password.|секретный синтаксис, по крайней мере, у вас есть простой текстовый пароль.
Because secret means that it is encrypting, the actual password is student, there's encrypting the word student using an MD5 hash.|Поскольку секретность означает, что это шифрование, фактический пароль - student, есть шифрование слова student с использованием хеша MD5.
Well this one is just plain text CISCO.|Ну, это просто простой текст CISCO.
But again, if you have to go back to an older IOS, that's why you're typing both.|Но опять же, если вам нужно вернуться к более старой IOS, поэтому вы набираете оба.
Now, the reality of it, all right, when you're in the field, normally,|Итак, реальность, хорошо, когда вы в поле, обычно,
when you log in, it's gonna be prompting you for username and password.|когда вы входите в систему, вам будет предложено ввести имя пользователя и пароль.
And that username and password, it is being, it is being connected,|И это имя пользователя и пароль, он подключается,
or being grabbed, from an active directory, or domain controller.|или захвачены из активного каталога или контроллера домена.
So, your Windows username and password is what's actually going to give you that access.|Итак, ваше имя пользователя и пароль Windows - это то, что на самом деле даст вам этот доступ.
And normally, if you are working with routers, you'll have a higher, a very high privilege, where you're able to do whatever you need to do on the router.|И обычно, если вы работаете с маршрутизаторами, у вас будут более высокие, очень высокие привилегии, с помощью которых вы сможете делать с маршрутизатором все, что вам нужно.
Unless you work for certain companies, then you pretty much do nothing on the routers.|Если вы не работаете в определенных компаниях, вы практически ничего не делаете с маршрутизаторами.
Okay?|Ладно?
But it all depends, who you work for.|Но все зависит от того, на кого вы работаете.
But you need to know these two, and that these two are privilege mode passwords.|Но вам нужно знать эти два, и что это два пароля привилегированного режима.
And the secret password will always override the plain text.|И секретный пароль всегда будет иметь приоритет над обычным текстом.
Sounds kind of silly to type both, and it is, all right, but again, testing purposes, testing purposes.|Звучит глупо набирать и то и другое, и это нормально, но опять же, в целях тестирования, в целях тестирования.
You have to go, know the difference between one or the other.|Вы должны пойти, знать разницу между тем и другим.
All right?|Отлично?
And remember, the secret password will use MD5 hash.|И помните, секретный пароль будет использовать хеш MD5.
Very big.|Очень большой.
Uppercase, lowercase letters, numbers, and symbols.|Прописные, строчные буквы, цифры и символы.
Something about this big.|Что-то в этом большом.
Okay?|Ладно?
Cool.|Прохладно.
The next thing that we wanna do Service password,|Следующее, что мы хотим сделать с сервисным паролем,
I can't type today, password_encryption.|Сегодня я не могу печатать, password_encryption.
What does that do?|Что это значит?
Service k, service_password_encryption encrypts all plain,|Сервис k, service_password_encryption шифрует все,
or all plain text passwords, past, present and future.|или все пароли в виде обычного текста, прошлые, настоящие и будущие.
So any plain text password that I just typed,|Итак, любой простой текстовый пароль, который я только что набрал,
the Cisco password is in plain text.|пароль Cisco в виде обычного текста.
Once we do the show run or show start you will see that that is encrypted already because that command right there encrypts|Как только мы выполним запуск шоу или запуск шоу, вы увидите, что он уже зашифрован, потому что эта команда прямо здесь зашифровывает
it, so no big deal.|это, так что ничего страшного.
Now, we want to create user names.|Теперь мы хотим создать имена пользователей.
We want to create a username with a certain level of privilege.|Мы хотим создать имя пользователя с определенным уровнем привилегий.
Now I'm going to create a username for myself and I want to have administrative privileges.|Теперь я собираюсь создать себе имя пользователя и хочу иметь права администратора.
So the way you do that is through levels.|Таким образом, вы делаете это через уровни.
Are you gonna be asked this on a test, no.|Тебя спросят об этом на тесте, нет.
This is actually information that I'm giving you.|Это на самом деле информация, которую я вам даю.
All right,so, if you want to create a local user name for the router, username, in my case, LDIAZ.|Итак, если вы хотите создать локальное имя пользователя для маршрутизатора, имя пользователя, в моем случае, LDIAZ.
You can type whatever you want.|Вы можете вводить все, что хотите.
Bob Smith, all right?|Боб Смит, хорошо?
LDIAZ, privilege.|ЛДИАЗ, привилегия.
Now I'm going to tab because for whatever reason, I have forgotten, for the most part, my spelling.|Теперь я перейду на вкладку, потому что по какой-то причине я по большей части забыл свое правописание.
So I tab over.|Так что я перехожу.
Username_ldiaz_privilege.|Имя пользователя_ldiaz_privilege.
Now you're looking for level.|Теперь вы ищете уровень.
It's one through 15.|Это от 1 до 15.
One, you pretty much can't do anything.|Во-первых, вы практически ничего не можете сделать.
15, you are the administrator.|15, вы администратор.
So, 15.|Итак, 15.
And then you're gonna put in password.|А потом вы введете пароль.
Zero, which means the password that you're about to put It's gonna be in plain text.|Ноль, что означает пароль, который вы собираетесь ввести. Он будет в виде обычного текста.
But do you really care?|Но разве тебе все равно?
Because you have that service_password_encryption,|Поскольку у вас есть service_password_encryption,
because there you either put zero or seven.|потому что там ставится либо ноль, либо семь.
So it's going to use the same type of encryption, seven.|Таким образом, он будет использовать тот же тип шифрования, семь.
So, service_password_encryption uses seven as well.|Итак, service_password_encryption также использует семь.
So that will be encrypted also.|Так что это тоже будет зашифровано.
Now after that we're going to type a banner.|Теперь после этого мы собираемся набрать баннер.
Will you get tested on the banner?|Ты будешь тестироваться на баннере?
Yes and I will show you how they will test you on the banner.|Да, и я покажу вам, как вас будут проверять на баннере.
Alright?|Хорошо?
What banner will you be tested?|Какой баннер вы будете тестировать?
The message of the day banner.|Сообщение дня баннера.
And you need to pick a particular delimiting character.|И вам нужно выбрать определенный ограничивающий символ.
A symbol.|Символ.
And whatever symbol you start with, you must end with, and you can not use that symbol within the body of the message.|И какой бы символ вы ни начали, вы должны им заканчивать, и вы не можете использовать этот символ в теле сообщения.
So I usually put in welcome to R1, which is another reality or what you are going to see, all right, and then finish it with the pound sign.|Так что я обычно приветствую R1, который является другой реальностью или тем, что вы собираетесь увидеть, хорошо, а затем заканчиваю это знаком фунта.
Now, how would they test you?|Как бы они вас проверили?
They will tell you okay, instead of saying welcome to R1,|Они скажут вам хорошо, вместо того, чтобы приветствовать R1,
they'll say if you need help, you know,|они скажут, если вам понадобится помощь, вы знаете,
call the help desk number, pound sign 555.|позвоните в справочную службу по номеру решетки 555.
And then space, and then with a pound sign.|А затем пробел, а затем знак фунта.
Well, the message really ended, call number, pound sign.|Ну, сообщение действительно закончилось, номер звонка, знак фунта.
That ended the message.|На этом сообщение закончилось.
Nobody saw that it was 5555, because you ended it at that point.|Никто не видел, что это номер 5555, потому что вы закончили его на этом месте.
So you cannot,|Так что ты не можешь,
you cannot use the same symbol that you start with, and end with, within the body of the message.|вы не можете использовать тот же символ, которым вы начинаете и заканчиваете в теле сообщения.
So if you want to use an ampersand, you want to use the what's the other sign.|Итак, если вы хотите использовать амперсанд, вы хотите использовать другой знак.
Amper sign, dollar sign, that would be a pretty cool one, percent sign.|Знак Ампера, знак доллара, это было бы неплохо, знак процента.
So there are certain symbols you can't use and your, your router will let you know,|Итак, есть определенные символы, которые вы не можете использовать, и ваш маршрутизатор сообщит вам,
alright.|хорошо.
But for the symbols that for the most part I've used amper signs.|Но для символов, которые по большей части я использовал амперные знаки.
I've used the little carrot symbol.|Я использовал маленький символ моркови.
I've used the obviously the pound sign or the dollar sign.|Я использовал знак фунта или доллара.
Use one of those.|Воспользуйтесь одним из них.
If you start with those, you end with those, and the message goes in between.|Если вы начнете с них, вы закончите с ними, и сообщение будет между ними.
All right?|Отлично?
That's your message of the day and that is how they will try and trip you up.|Это ваше послание дня, и именно так они попытаются сбить вас с толку.
Okay?|Ладно?
So the next thing we're going to do,|Итак, следующее, что мы собираемся сделать,
now this is something that normally people turn off.|теперь это то, что обычно люди отключают.
Which is name resolution, name resolution.|Это разрешение имен, разрешение имен.
Okay?|Ладно?
We're gonna turn that on.|Мы это включим.
IP domain_lookup.|IP domain_lookup.
It's already on by default.|По умолчанию он уже включен.
I really didn't have to type that command.|Мне действительно не нужно было вводить эту команду.
But I'm just typing it so I can show you,|Но я просто печатаю его, чтобы показать тебе,
if it is off, how would you turn it on.|если он выключен, как бы вы его включили.
IP domain lookup.|Поиск IP-домена.
Then you will go, IP domain_name.|Затем вы перейдете, IP domain_name.
Right?|Правильно?
And obviously, we're gonna put cisco.com.|И, очевидно, мы разместим cisco.com.
I mean yeah, number one here.|Я имею в виду да, номер один здесь.
All right.|Отлично.
And then, you're gonna put the IP address,|А затем введите IP-адрес,
right?|право?
IP name.|IP-имя.
Which server are you gonna point it to?|На какой сервер вы его укажете?
And we'll use something in the one network 192 dot 168 dot one dot, one dot two.|И мы будем использовать что-то в одной сети: 192 точки, 168 точек, одна точка, одна точка, две.
Right?|Правильно?
So you're now pointing it to a particular DNS server.|Итак, теперь вы указываете на конкретный DNS-сервер.
And why do you want to do this.|И зачем тебе это нужно.
Let's say you want a ping or you want a tracer,.|Допустим, вам нужен пинг или трассировщик.
You want a telnet or SSH,|Вы хотите telnet или SSH,
whatever the case may be and you want to use names instead of IP addresses.|в любом случае вы хотите использовать имена вместо IP-адресов.
You can do that, but obviously you need to set up host A records,|Вы можете это сделать, но, очевидно, вам нужно настроить записи хоста A,
right, set up a domain on a DNS server.|правильно, настроить домен на DNS-сервере.
And then you create host records associated with that domain,|Затем вы создаете записи хоста, связанные с этим доменом,
which is the IP address and that name on the router.|который является IP-адресом и этим именем на маршрутизаторе.
Alright, and you can do up to eight IP addresses per router associated with that particular host name.|Хорошо, и вы можете сделать до восьми IP-адресов для каждого маршрутизатора, связанного с этим конкретным именем хоста.
Alright, so that's what that's for.|Хорошо, вот для чего это нужно.
So we created a host name, we created banners, we've created passwords.|Итак, мы создали имя хоста, мы создали баннеры, мы создали пароли.
We've turned up domain lookup.|Мы включили поиск домена.
Now, everybody telnets, everybody telnets.|Теперь все telnets, все telnets.
Telnet though, really, it's not secure,|Telnet, правда, небезопасен,
cause it's plain text.|потому что это простой текст.
So what we wanna do is set up SSH.|Итак, что мы хотим сделать, это настроить SSH.
So, when we set up SSH, that means we're using some encrypted connection, right?|Итак, когда мы настраиваем SSH, это означает, что мы используем какое-то зашифрованное соединение, верно?
So we set up some sort of keys.|Итак, мы установили какие-то ключи.
Now in order to set up these keys, there are requirements.|Теперь, чтобы настроить эти ключи, есть требования.
You have to have a host name, and you have to have a domain name.|У вас должно быть имя хоста и имя домена.
Those are the two key requirements in order to create these keys,|Это два ключевых требования для создания этих ключей:
these RSA keys.|эти ключи RSA.
And here is how you set that up.|И вот как вы это настроили.
Will they ask you about this?|Вас спросят об этом?
No, but now you know.|Нет, но теперь ты знаешь.
Crypto key generate.|Криптоключ сгенерировать.
[BLANK_AUDIO]|[BLANK_AUDIO]
RSA and you got to hit ENTER here.|RSA, и вы должны нажать здесь ENTER.
And it's going to ask you what size do you want.|И он спросит вас, какой размер вам нужен.
I just chose the default 512.|Я просто выбрал значение по умолчанию 512.
The bigger, the bigger you do it,|Чем больше, тем крупнее ты это делаешь,
the, the slower it will become because remember it's using a higher key to encrypt everything, so it's going to take a while to do it.|тем медленнее он станет, потому что помните, что он использует более высокий ключ для шифрования всего, поэтому на это потребуется время.
So just leave it at default 512, at least you know how to set this up.|Так что просто оставьте значение по умолчанию 512, по крайней мере, вы знаете, как это настроить.
Okay?|Ладно?
Am I missing something here?|Я что-то упустил?
Am I missing something?|Я что-то упускаю?
Did the user name, banners, servive, IP domain lookup,|Имя пользователя, баннеры, сервив, поиск IP-домена,
I don't think I'm missing anything, I don't think so, I don't think so.|Я не думаю, что что-то упускаю, не думаю, не думаю.
All right, now we're gonna go into the lines, the lines, okay.|Хорошо, теперь мы перейдем к строкам, строкам, хорошо.
And we're gonna go line column zero and you're gonna see what's happen.|И мы перейдем к нулевому столбцу строки, и вы увидите, что произойдет.
Boom, it's gonna tell me what version of SSH,|Бум, он скажет мне, какая версия SSH,
and it's telling me if you're using a different SSH.|и он говорит мне, используете ли вы другой SSH.
It would be at this, you know, this level of key, the 768.|Это, знаете ли, этот ключевой уровень, 768.
So we're to go ahead and do, as I say,|Итак, мы продолжим и сделаем, как я говорю,
each 1.5, and what have you.|каждые 1.5, а что у вас.
Just a little information, logging information.|Немного информации, запись информации.
[LAUGH] So when we get to the IP services chapter,|[СМЕХ] Итак, когда мы переходим к главе об IP-услугах,
we'll know what we'd be looking at.|мы будем знать, на что будем смотреть.
So we're gonna do password.|Итак, мы сделаем пароль.
[BLANK_AUDIO]|[BLANK_AUDIO]
Cisco, but instead of just doing login which is what the book asks you to do,|Cisco, но вместо того, чтобы просто войти в систему, о чем вас просит книга,
and when your certification their not going to ask you.|а при вашей сертификации их не спросят у вас.
It's just login, you're going to do login local.|Это просто вход в систему, вы собираетесь выполнить локальный вход.
Why?|Зачем?
Because you want to be able by typing in login local.|Потому что вы хотите иметь возможность, введя локальный логин.
You're telling the router, hey, prompt me not only for a password, but for a username.|Вы говорите маршрутизатору, эй, подскажите мне не только пароль, но и имя пользователя.
So now the person will be prompted for a username and password if they're going into the console line.|Итак, теперь человеку будет предложено ввести имя пользователя и пароль, если он войдет в консольную строку.
All right, and then we're gonna do.|Хорошо, а потом мы будем делать.
We're not done, we're not done there yet.|Мы еще не закончили, мы еще не закончили.
We're gonna do EXEC-,|Мы сделаем EXEC-,
oh, EXEC-TIMEOUT 0 0.|о, EXEC-TIMEOUT 0 0.
What does that mean?|Что это значит?
0 minutes, 0 seconds.|0 минут, 0 секунд.
So the first number is minutes.|Итак, первое число - минуты.
The second number is seconds.|Второе число - секунды.
Okay, so I put 0 0 because I never want to be timed out.|Хорошо, поэтому я поставил 0 0, потому что я никогда не хочу, чтобы время ожидания истекало.
You may want to do that in the real world.|Возможно, вы захотите сделать это в реальном мире.
You can put 10 minutes, 0 seconds, 15|Можно поставить 10 минут, 0 секунд, 15
minutes, 0 seconds,|минут, 0 секунд,
whatever it is that you want to do.|что бы вы ни делали.
Just remember if you're leaving the telecommunications closet,|Просто помните, если вы выходите из телекоммуникационного шкафа,
log out of your router, or at least lock the computer that goes into the router.|выйдите из роутера или хотя бы заблокируйте компьютер, подключенный к роутеру.
But you may want to log out of the router anyway.|Но вы все равно можете выйти из роутера.
Okay, and definitely don't leave the door open or what have you.|Ладно, и определенно не оставляй дверь открытой или что там у тебя.
Make sure these are secure doors.|Убедитесь, что это надежные двери.
So physical security is one of the first things, and definitely you don't leave your station with, you know, wide open.|Итак, физическая безопасность - одна из первых вещей, и вы определенно не покидаете свою станцию, знаете ли, нараспашку.
You log out or you lock it, okay.|Вы выходите из системы или блокируете ее, хорошо.
The next command, LOGGING, too many G's there, LOGGING SYNCHRONOUS, SYNCHRONOUS.|Следующая команда, LOGGING, слишком много G, LOGGING SYNCHRONOUS, SYNCHRONOUS.
Okay, what does that do?|Хорошо, что это значит?
I call that the nuisance command.|Я называю это неприятной командой.
Because your router, as you saw when I went to the line console,|Потому что ваш маршрутизатор, как вы видели, когда я подошел к линейной консоли,
that the SSH, I got some logging information from the console.|что SSH, я получил информацию о журнале с консоли.
It gave me some info, that will interrupt your typing.|Он дал мне некоторую информацию, которая помешает вам набирать текст.
So if I would have been typing, half of it would have been up here.|Так что, если бы я печатал, половина была бы здесь.
The other half would have been down here.|Другая половина была бы здесь.
If you don't have logging synchronous, the information is still going to come up, but your typing will stay in the same line.|Если у вас нет синхронного ведения журнала, информация все равно будет появляться, но ваш ввод останется в той же строке.
So that's a cool command to type because it'll do that.|Так что это классная команда для ввода, потому что она это сделает.
It'll keep your typing in one line.|Это сохранит ваш ввод в одну строку.
So we've done our console, but we're not done because we need to do our VTY lines,|Итак, мы сделали нашу консоль, но мы еще не закончили, потому что нам нужно сделать наши строки VTY,
all right, which is our virtual terminal lines, the line that we telnet or SSH.|хорошо, это наши виртуальные терминальные линии, линия, по которой мы проводим telnet или SSH.
We are setting up for SSH so we're going to tell it hey we wanna, we really wanna,|Мы настраиваемся на SSH, поэтому мы собираемся сказать ему, что мы хотим, мы действительно хотим,
I'm gonna show you how to do both, how to do both, okay?|Я покажу вам, как сделать и то и другое, как сделать и то, и другое, хорошо?
So, we're going to do LINE VTY 0 15.|Итак, сделаем LINE VTY 0 15.
If you didn't know, you type question mark after the 0.|Если вы не знали, введите вопросительный знак после 0.
It'll tell you how many lines you have.|Он скажет вам, сколько у вас строк.
But you can open as many lines as you want.|Но вы можете открыть столько строк, сколько захотите.
You can open up one line, you can open two lines.|Вы можете открыть одну строку, вы можете открыть две строки.
You can open default zero to four,|Вы можете открыть по умолчанию от нуля до четырех,
you can, you can open up as many lines as you want.|вы можете, вы можете открыть столько строк, сколько захотите.
This is just all the lines that this router has so I opened up all the lines.|Это только все линии, которые есть у этого маршрутизатора, поэтому я открыл все линии.
And now I put a PASSWORD CISCO.|А теперь ставлю ПАРОЛЬ CISCO.
Just to, and the only reason I use CISCO for everything so, my brain is so fried so I don't forget.|Просто для того, и единственная причина, по которой я использую CISCO для всего, так что мой мозг настолько перегорел, что я не забываю.
All right, now I do the same thing LOGIN LOCAL.|Хорошо, теперь я делаю то же самое ЛОКАЛЬНЫЙ ВХОД.
Right?|Правильно?
So I have to type in the username and password, EXEC-TIME out because it's a different line, all right.|Поэтому мне нужно ввести имя пользователя и пароль, EXEC-TIME out, потому что это другая строка, хорошо.
If I'm, if I create a session and you say,|Если я, если я создам сеанс, и вы скажете:
hey Laz, you didn't type time out, you typed time.|эй, Лаз, ты не вводил тайм-аут, ты вводил время.
Yeah, cuz the router knows.|Да, потому что роутер знает.
The router knows exactly what I wanted to type.|Маршрутизатор точно знает, что я хотел ввести.
So it understands that, really, that means time out because that's the only command that exists that's gonna have the time out.|Таким образом, он понимает, что на самом деле это означает тайм-аут, потому что это единственная существующая команда, у которой будет время ожидания.
So if we map just the abbreviated portion of it, it'll understand.|Поэтому, если мы нанесем на карту только сокращенную часть, он поймет.
And then LOGGING SYNCHRONOUS,|И затем ЛОГИН СИНХРОННЫЙ,
I'm gonna tab right here, and it'll finish it for me.|Я собираюсь поставить вкладку прямо здесь, и это закончится для меня.
So you're saying, Laz, you're typing the same command over and over again on different lines?|Итак, ты говоришь, Лаз, ты снова и снова набираешь одну и ту же команду в разных строках?
Yeah.|Да.
Cuz, you gonna be consoling in, or you can be SSHing in.|Потому что ты будешь утешаться, или можешь подключиться по SSH.
So you want those configurations there.|Итак, вам нужны эти конфигурации.
I'm not gonna do the auxiliary, you're just doing overkill.|Я не собираюсь делать вспомогательные вещи, ты просто убиваешь их.
But you would do the same thing there, the same commands.|Но вы бы там сделали то же самое, те же команды.
All right,|Отлично,
so, these are our administrative commands,|Итак, это наши административные команды,
let's test them out.|давайте проверим их.
All right, let's, first of all, let's copy them.|Хорошо, давайте, прежде всего, скопируем их.
EXIT, EXIT, copy, RUN START, Enter,|ВЫХОД, ВЫХОД, копирование, ЗАПУСК, ВВОД,
and it's gonna ask you, do you want to copy it to the startup configuration file?|и он спросит вас, хотите ли вы скопировать его в файл конфигурации запуска?
Yes, you do, and since it's in bracket,|Да, это так, и поскольку он заключен в скобки,
that's the only files there.|это единственные файлы.
You'd hit Enter.|Вы нажали Enter.
And then you wanna look at it, and, well,|А потом вы хотите посмотреть на это, и, ну,
these last lecture,|эта последняя лекция,
but, go, I'll show you a lot more short commands.|но, давай, я покажу тебе гораздо больше коротких команд.
This one show command that you look.|Это одна команда show, которую вы смотрите.
And you do a show start, and there you go.|И вы начинаете шоу, и вот оно.
There's the service password-encryption,|Есть сервисное шифрование паролей,
the hostname.|имя хоста.
Take a look at the enable secret, right?|Взгляните на секрет включения, верно?
That 5 right there.|Вот 5 прямо здесь.
That's the MD5.|Это MD5.
And you see here it's using 7.|Как видите, здесь используется 7.
This is Cisco that I put in plain text.|Это Cisco, которую я написал простым текстом.
But the service password-encryption is encrypting it.|Но служба шифрования паролей шифрует это.
And take a look, look at my password for the username, it's also encrypting it,|И посмотрите, посмотрите мой пароль для имени пользователя, он тоже его шифрует,
right?|право?
This wasn't encrypting it, this is a 7, I put 0.|Это не шифрование, это 7, я поставил 0.
Who encrypted it?|Кто его зашифровал?
The service password-encryption.|Сервис шифрования паролей.
So, if they ask you a question, who is stronger, who has stronger encryption,|Итак, если они зададут вам вопрос, кто сильнее, у кого более надежное шифрование,
is it the service password-encryption or is it the enable secret?|это сервисное шифрование паролей или секрет включения?
The enable secret, look at that, compared to that.|Секрет включения, посмотрите на это по сравнению с этим.
So the enable secret has a higher encryption than the service password-encryption,|Таким образом, ключ enable имеет более высокое шифрование, чем шифрование пароля службы,
remember that.|запомни это.
There's a username, there's the version of SSH that we're using.|Есть имя пользователя, есть версия SSH, которую мы используем.
Okay.|Ладно.
We haven't done the interfaces.|Мы еще не сделали интерфейсы.
That'll be in the next lesson.|Это будет на следующем уроке.
There's our banners, there's our line con,|Вот наши баннеры, вот наша линия против,
there's our VTYs, awesome.|вот и наши VTY, классные.
But let's test it out.|Но давайте проверим это.
Let's exit out our router, right.|Давайте выйдем из нашего роутера, верно.
I'm gonna hit Enter.|Я нажму Enter.
Boom.|Бум.
Username and there's, there's your banner.|Логин и вот там твой баннер.
Welcome to router one.|Добро пожаловать в первый роутер.
LDIAZ, Password, CISCO.|ЛДИАЗ, Пароль, CISCO.
And, now I'm in the router.|И теперь я в роутере.
And I'm going to do my show start, show run, do whatever I need to do.|И я собираюсь начать свое шоу, запустить шоу, сделать все, что мне нужно.
So, I gave you a little bit more than just the administrative commands.|Итак, я дал вам немного больше, чем просто административные команды.
But it's not that much, all right?|Но это не так уж и много, понятно?
You need to learn how to do this,|Тебе нужно научиться это делать,
especially setting up SSH.|особенно настройка SSH.
And we didn't really tweak SSH, cuz you can set up the authentication retries,|И мы действительно не настраивали SSH, потому что вы можете настроить повторные попытки аутентификации,
you can set up the timeouts, right.|вы можете настроить таймауты, верно.
You can tell, hey, I'll let you try three times to login through SSH, if not,|Вы можете сказать, эй, я позволю вам трижды попытаться войти через SSH, если нет,
you're gonna get kicked out.|тебя выгонят.
Or, if you're session time out, right, if you're, you know,|Или, если у вас тайм-аут сеанса, правильно, если вы, знаете,
idle, I'm gonna let you be idle for 120|Простаиваю, я позволю тебе бездействовать на 120
seconds.|секунд.
Then after that, boom, you're kicked out as well.|Потом, бум, тебя тоже выгнали.
So, we didn't do those two commands.|Итак, мы не выполняли эти две команды.
But at least you've done everything else administratively.|Но, по крайней мере, все остальное вы сделали административно.
Now in the next lesson, we'll learn to go into the interfaces.|Теперь в следующем уроке мы научимся разбираться в интерфейсах.
I'll see you there.|Увидимся там.
[BLANK_AUDIO]|[BLANK_AUDIO]