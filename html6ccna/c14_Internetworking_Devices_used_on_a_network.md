D:\mailCloud\prjother\tmp\1\c14_Internetworking Devices used on a network.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
And we're back in the game.|И мы снова в игре.
So, what do I have back here?|Итак, что у меня здесь?
Hey.|Привет.
These are the internetworking devices, or some of them,|Это межсетевые устройства или некоторые из них,
anyway more relevant to your CCNA and some relevant to what you're actually going to see when you get out there, all right.|в любом случае, это больше относится к вашей CCNA, а некоторые - к тому, что вы на самом деле увидите, когда выйдете оттуда, хорошо.
So there's four devices that you really need to be concentrating on.|Итак, есть четыре устройства, на которых вам действительно нужно сосредоточиться.
Well, really two devices but we'll learn all four.|Что ж, действительно два устройства, но мы изучим все четыре.
Two devices for the examination, but you see up, we have a router.|Два устройства для осмотра, но видите ли, у нас есть роутер.
Pretty simple.|Довольно просто.
A circle with a bunch of arrows pointing all over the place.|Круг с кучей стрелок, указывающих повсюду.
Right, because it goes all over, right?|Верно, потому что все кончено, верно?
Creates the path through the internetwork,|Создает путь через объединенную сеть,
you have a switch.|у вас есть переключатель.
All right?|Отлично?
Router layer three,|Третий уровень маршрутизатора,
when we talk about the USI, you'll see.|когда мы будем говорить о USI, вы увидите.
Switch layer two, hub which we just saw,|Переключатель второго уровня, концентратор, который мы только что видели,
bad, bad hub, we don't want hubs on our networks.|плохой, плохой концентратор, нам не нужны концентраторы в наших сетях.
And then we have a bridge, looks like a half-pipe,|А тут мост, похожий на хафпайп,
something a skateboarder would use, right?|что-то, что может использовать скейтбордист, верно?
So we have a bridge.|Итак, у нас есть мост.
So let's talk about this, let's talk about this.|Итак, давайте поговорим об этом, давайте поговорим об этом.
What devices do we use, or we would like to use?|Какие устройства мы используем или хотели бы использовать?
Well, we already know, and we're talking about Ethernet, Ethernet,|Что ж, мы уже знаем, и мы говорим об Ethernet, Ethernet,
remember Ethernet is a standard that was created, an IEEE standard,|помните, что Ethernet - это стандарт, который был создан, стандарт IEEE,
802.3, right, that has an access method that is CSMACD,|802.3, верно, у которого есть метод доступа CSMACD,
which really is, is just first come, first serve, all right.|что на самом деле, это просто первый пришел, первый подал, хорошо.
We're all listening, right?|Мы все слушаем, правда?
Carry your sense, we're listening for noise.|Имейте в виду, мы прислушиваемся к шуму.
You could have multiple access, then, but if you have the collision detection.|Тогда у вас может быть множественный доступ, но если у вас есть обнаружение столкновений.
Not two computers can actually be on the cable at the same time, all right.|На самом деле, два компьютера не могут быть подключены к кабелю одновременно.
So that's the problem with Ethernet.|Так вот проблема с Ethernet.
So our jobs as Cisco professionals, as network engineers,|Итак, наша работа как профессионалов Cisco, как сетевых инженеров,
we need to reduce the amount of broadcast,|нам нужно уменьшить объем трансляции,
reduce the amount of collisions that exist on a network,|уменьшить количество коллизий, существующих в сети,
and how, pray tell, do we do that?|и как, скажите, пожалуйста, мы это делаем?
Well, we do that by segmenting,|Что ж, мы делаем это путем сегментации,
segmenting, breaking up collision domains.|сегментирование, разбиение доменов коллизий.
Making more collision domains.|Создание дополнительных коллизионных доменов.
That sounds kind of like it's contradicting.|Это звучит как бы противоречиво.
Well, wait a minute Laz, you want more collision domains?|Ну, погоди, Лаз, ты хочешь больше доменов коллизий?
Yeah, I do.|Да, люблю.
I don't want one huge collision domain.|Мне не нужен один огромный домен коллизий.
It's like having one classroom with 200|Это как в одном классе с 200
students.|ученики.
I'd rather have five classrooms and break those up.|Я бы предпочел иметь пять классов и разбить их.
I don't know the math, I wanna break those up.|Я не знаю математики, я хочу разбить их.
Let's say 100 students, four, 25 students in each.|Допустим, 100 студентов, четверо, по 25 студентов.
I'll make it 100, I'll make it easy, or 50|Я сделаю 100, я сделаю это легко, или 50
students equals 200, right?|студентов равно 200, не так ли?
See I did the math, I did the math.|Видите, я посчитал, я посчитал.
But you wanna break that up.|Но ты хочешь разбить это.
You wanna break those collision domains.|Вы хотите разрушить эти области столкновения.
So the more collision domains you have,|Итак, чем больше у вас доменов коллизий,
collision domains, that's good.|домены столкновения, это хорошо.
The more broadcast domains you have,|Чем больше у вас широковещательных доменов,
that's even better, so that's what you wanna do, that's the whole point.|так даже лучше, вот что ты хочешь делать, в этом весь смысл.
But you need to understand the devices that you're using.|Но вам нужно понимать, какие устройства вы используете.
Let's talk about our little half-pipe buddy down here, the bridge.|Давайте поговорим о нашем маленьком приятеле по хаф-пайпу, мосту.
I hope you can see that, I think you can the bridge,|Надеюсь, вы это видите, я думаю, вы можете мост,
it's main purposes is to segment a network.|его основная цель - сегментировать сеть.
The bridge is software-based, so it's kind of slow.|Мост является программным, поэтому он довольно медленный.
It is limited on the amount of ports it can have.|Он ограничен количеством портов, которые он может иметь.
Now I'm going to throw a term at you.|Теперь я собираюсь бросить вам термин.
I'm going to throw a term, and I'll briefly or loosely define it.|Я собираюсь подбросить термин и дать ему краткое или вольное определение.
But once we get to that particular part of the course, I'll go deep into it.|Но как только мы перейдем к этой части курса, я углублюсь в нее.
I will.|Я буду.
I promise.|Обещаю.
The bridge can only have one spanning tree instance.|У моста может быть только один экземпляр связующего дерева.
Once span tree instance, and just, span tree, all it is is prevents loops,|Как только экземпляр связующего дерева и просто связующее дерево, все, что он есть, предотвращает петли,
switching loops, at layer two or bridging rules at layer two.|коммутационные петли на втором уровне или правила соединения на втором уровне.
So bridges, at the beginning, we use bridging.|Итак, вначале мы используем мосты.
That's why they say, you know, software bridging, things like that, so it's slow,|Вот почему они говорят, что программный мостик и тому подобное, так что это медленно,
it's limited on ports, so we got rid of the bridge slowly, and that's where, well,|он ограничен по портам, поэтому мы медленно избавились от моста, и вот где, ну,
we definitely got rid of hubs.|мы однозначно избавились от хабов.
We've done away with hubs, we don't want hubs.|Мы покончили с хабами, нам не нужны хабы.
That's your shared collision domain.|Это ваш общий домен конфликтов.
You only have half duplex, all right,|У вас только полудуплекс, ладно,
where you can only send or receive.|где вы можете только отправлять или получать.
Here, on a bridge, you have the full duplex, using two pairs of wires, meaning you can send and receive at the same time because you're using two pairs of wires.|Здесь, на мосту, у вас есть полный дуплекс с использованием двух пар проводов, что означает, что вы можете отправлять и получать одновременно, потому что вы используете две пары проводов.
That's a good thing.|Это хорошая вещь.
Where hubs, you're done.|Где хабы, все готово.
So hubs, you're pretty much, pretty much over.|Итак, хабы, вы в значительной степени закончили.
We don't use them in the real world.|Мы не используем их в реальном мире.
Nobody does.|Никто не делает.
Don't use them.|Не используйте их.
Bad thing.|Плохо.
Will they ask you something on the test about hubs?|Вас спросят на тесте о хабах?
If they do, just know it's bad anything it's, it's, it's bad about hubs,|Если они это сделают, просто знайте, что это плохо, что угодно, это плохо с концентраторами,
that's the answer for hubs, all right or shared collision domains.|это ответ для концентраторов, хорошо или общих коллизионных доменов.
Switches that's where you're gonna be tested on.|Переключатели, на которых вы собираетесь пройти испытания.
It's gonna be 20% of your grade and all the different things you can do on the switches.|Это будет 20% вашей оценки и все, что вы можете делать с переключателями.
What can you do?|Что ты можешь сделать?
You can break up well, each port on the switch, it's its own collision domain.|Можно хорошо разбить, каждый порт на коммутаторе, это свой домен коллизии.
So the more things you plug into it, so you have a 24 port switch or 48 port switch, you have 48 collision domains.|Таким образом, чем больше вещей вы подключаете к нему, то есть у вас есть коммутатор на 24 порта или коммутатор на 48 портов, у вас будет 48 доменов конфликтов.
You have that full bandwidth, if it's Cat 5e,|У вас есть полная пропускная способность, если это Cat 5e,
you have that 100 megabit per second, send and receive at the same time.|у вас есть эти 100 мегабит в секунду, отправляйте и получайте одновременно.
If you have a Cat 6, you got 1,000|Если у вас Cat 6, у вас 1000
megabits per second, send and receive at the same time.|мегабит в секунду, отправка и получение одновременно.
So you've broken up those collisions,|Итак, вы разбили эти столкновения,
that's awesome,|это потрясающе,
it's a private collision domain.|это частный домен коллизии.
The only thing, you have still only one broadcast domain,|Единственное, у вас остался только один широковещательный домен,
which means when people are talking back and forth,|это означает, что когда люди говорят взад и вперед,
regardless of what you hear out there, all right, they still hear that noise.|независимо от того, что вы там слышите, хорошо, они все равно слышат этот шум.
They still hear that noise.|Они все еще слышат этот шум.
So you still need to break up those broadcast domains.|Так что вам все равно нужно разделить эти широковещательные домены.
And guess what?|И угадайте, что?
That's what switches bring.|Вот что приносят переключатели.
Bridges bring in that segmentation when you wanna break things apart.|Мосты привносят эту сегментацию, когда вы хотите разбить вещи на части.
We have a group over here, we have a group over here.|У нас есть группа здесь, у нас есть группа здесь.
We use a layer three device, like a router,|Мы используем устройство третьего уровня, например маршрутизатор,
to intercommunicate with each other.|общаться друг с другом.
But with a switch, we can break up broadcast domains at layer two, how do we that?|Но с помощью коммутатора мы можем разбить широковещательные домены на втором уровне, как нам это сделать?
By creating VLANs, we create VLANs down here, virtual local area networks,|Создавая VLAN, мы создаем здесь VLAN, виртуальные локальные сети,
now we can have multiple broadcast on a switch, that is awesome.|теперь у нас может быть несколько трансляций на коммутаторе, и это здорово.
Because what happens in the broadcast,|Потому что то, что происходит в эфире,
stays in that broadcast.|остается в этой трансляции.
So imagine this.|Так что представьте себе это.
You have, let's say a school, makes thing simple.|У вас есть, скажем, школа, все упрощает.
Let's say on one side, you have medical students, and they're doing their labs,|Допустим, с одной стороны, у вас есть студенты-медики, и они делают свои лаборатории,
and they're doing their things on their computer, and then right next to them, you have a networking class.|и они делают свои дела на своем компьютере, а рядом с ними у вас класс по сетям.
And these guys, they're, you know, doing DHCP servers, they're doing all sorts of crazy stuff, security protocol, and they're trying to do hacking stuff.|И эти ребята, они, вы знаете, делают DHCP-серверы, они делают всякие сумасшедшие вещи, протоколы безопасности и пытаются взломать вещи.
What's gonna happen is if there are one particular,|Что произойдет, если будет один конкретный,
by default, and keep this in mind, this is something you should keep in mind.|по умолчанию, и имейте это в виду, это то, что вы должны иметь в виду.
So when we get into that, into that particular session, by default,|Итак, когда мы переходим к этому конкретному сеансу, по умолчанию
all switches are part of VLAN 1.|все коммутаторы являются частью VLAN 1.
All switches are part of VLAN 1, which means you are all in one broadcast domain,|Все коммутаторы являются частью VLAN 1, что означает, что вы все находитесь в одном широковещательном домене,
so whatever I do on my VLAN, guess what?|Итак, что бы я ни делал в своей VLAN, угадайте, что?
It's gonna affect you.|Это повлияет на тебя.
You're gonna hear that noise.|Вы услышите этот шум.
You're gonna get slowed down.|Ты замедлишься.
So if I have the DHCP, which what a DHCP serve, for those of you who may not know or don't remember, all right, it assigns|Итак, если у меня есть DHCP, который обслуживает DHCP, для тех из вас, кто не знает или не помнит, хорошо, он назначает
IP addresses.|IP-адреса.
Or, I'll say that correctly.|Или я правильно скажу.
It'll lease IP addresses, be careful with the terminology in the exam,|Он будет арендовать IP-адреса, будьте осторожны с терминологией на экзамене,
because in actuality, or I guess the reality of it is,|потому что на самом деле, или я предполагаю, что это так,
that's what a DHCP server does, it leases addresses, right?|это то, что делает DHCP-сервер, он сдает адреса в аренду, верно?
We'd normally say assign, everybody says assign, but the terminology that they play around with Is that it leases addresses.|Обычно мы говорим «назначить», все говорят «назначить», но терминология, с которой они экспериментируют, - это аренда адресов.
Okay?|Ладно?
Keep that open there.|Держите это открытым там.
So, if I have in that classroom a DACP server, and the school itself has a DACP server, we're not gonna clash with each other.|Итак, если у меня в классе есть сервер DACP, а в школе есть сервер DACP, мы не будем конфликтовать друг с другом.
I'll be assigning IP addresses to a classroom, the DACP server for the school will be assigning, so it'll be chaos.|Я буду назначать IP-адреса классу, сервер DACP для школы будет назначать, так что будет хаос.
It will be chaos because we didn't segment the broadcast domain.|Будет хаос, потому что мы не сегментировали широковещательный домен.
And we do that by creating [UNKNOWN], all right?|И мы делаем это, создавая [НЕИЗВЕСТНО], хорошо?
So that's what the switch brings in.|Вот что дает переключатель.
We can go ahead and have that extra functionality by creating those [UNKNOWN].|Мы можем продолжить и получить эту дополнительную функциональность, создав те [НЕИЗВЕСТНО].
Not only that, we can can set up port security.|Мало того, мы можем настроить безопасность порта.
We can create access lists.|Мы можем создавать списки доступа.
We can do what's call ether channel.|Мы можем делать то, что называется эфирным каналом.
There's a slew of things that you can do now with the switches that we didn't do before.|Теперь с переключателями можно делать множество вещей, которых мы раньше не делали.
So, definitely switches is what you're gonna have in your network.|Итак, коммутаторы - это то, что у вас будет в сети.
And if you're building a network in today's technology,|И если вы строите сеть с использованием современных технологий,
if you're building a network from the ground up, if you're that lucky or you get to upgrade and say hey, let's go with gigabit, right?|если вы строите сеть с нуля, если вам повезет или вы сможете обновить и сказать: «Эй, давайте перейдем к гигабитам, верно?
It was unheard of way back in the days of the bussed apology and coaxial cable and,|Это было неслыханно во времена извинений по автобусам, коаксиального кабеля и,
you know, we're running 10 megabits per second or less.|вы знаете, мы работаем со скоростью 10 мегабит в секунду или меньше.
Those days are gone.|Те дни прошли.
Now we want fast, fast,|Теперь мы хотим быстро, быстро,
when I send you something I want you to get it right then and there.|когда я посылаю вам что-то, я хочу, чтобы вы получили это прямо сейчас.
The minute I click on that button you should have it.|Как только я нажму на эту кнопку, она должна быть у вас.
What, where's that information I just sent you, you don't got it yet?|Что, где та информация, которую я вам только что отправил, а вы ее еще не получили?
So, definitely you want to get, if your gonna buy a switch and you're doing things, you wanna make sure if you're doing it on your own, right,|Итак, определенно вы хотите получить, если вы собираетесь купить коммутатор и что-то делаете, вы хотите убедиться, что делаете ли вы это самостоятельно, верно,
if you're a consultant, and this is your own business, or you're trying to convince your boss, [LAUGH] listen we have a lot of|если вы консультант и это ваше личное дело, или вы пытаетесь убедить своего босса, [СМЕХ] послушайте, у нас много
work, we need to be productive.|работать, нам нужно быть продуктивными.
In order for us to be productive, for the size of packets that we're sending on our network, let's say I always use the example of guys that do|Допустим, чтобы мы работали продуктивно, учитывая размер пакетов, которые мы отправляем в нашу сеть, я всегда использую пример парней, которые делают
surveying because I worked with surveyors.|геодезию, потому что я работал с геодезистами.
And they use these, what is it,|И они используют эти, что это такое,
auto cat, these auto cat files are huge,|auto cat, эти файлы auto cat огромны,
and they slow down the network a lot.|и они сильно замедляют работу сети.
So you want to use cat six.|Итак, вы хотите использовать кошку шесть.
So you gotta look at your situation and say hey, what type of device.|Итак, вы должны взглянуть на свою ситуацию и сказать, что за устройство.
Definitely, you're gonna want to use switches.|Определенно, вы захотите использовать переключатели.
You're going to want to use switches.|Вы захотите использовать переключатели.
And, key word here, you wanna use managed switches, managed.|И, ключевое слово здесь, вы хотите использовать управляемые переключатели, управляемые.
And what does that mean?|И что это значит?
Remember at the beginning that we were able to go inside a switch,|Помните, что вначале мы могли войти в переключатель,
put an IP address and a gateway and all that.|поставить IP-адрес и шлюз и все такое.
So you can go inside of the switch and then configure whatever it is you need to configure.|Таким образом, вы можете войти внутрь коммутатора, а затем настроить все, что вам нужно.
All right.|Отлично.
So, definitely switches, layer two,|Итак, определенно переключатели, второй уровень,
switches really only make a table,|переключатели действительно только составляют стол,
they create a table, what's called a MAC address table.|они создают таблицу, так называемую таблицу MAC-адресов.
We'll get deeper into that.|Мы углубимся в это.
So that's a layer two, and obviously the layer three.|Итак, это второй слой и, очевидно, третий слой.
This guy up here, the router, he breaks up broadcast domains by default.|Этот парень здесь, маршрутизатор, он по умолчанию разбивает широковещательные домены.
What does that mean?|Что это значит?
So if he has three interfaces, he's got three different broadcast domains.|Итак, если у него три интерфейса, у него есть три разных широковещательных домена.
Which means you have different networks.|Значит, у вас разные сети.
Different networks.|Разные сети.
Meaning you have the 10, 10, one zero, 10,|Это означает, что у вас есть 10, 10, один ноль, 10,
10, two zero, 10, 10, three zero.|10, два нуля, 10, 10, три нуля.
So you have three separate networks altogether.|Итак, у вас есть три отдельные сети.
They can't talk to each other unless you're trying to get to it,|Они не могут разговаривать друг с другом, если вы не пытаетесь понять это,
cuz their router creates a routing table saying, hey where do you want to go?|потому что их маршрутизатор создает таблицу маршрутизации, говоря: эй, куда вы хотите пойти?
Oh, you want to go somewhere in the three?|О, хочешь пойти куда-нибудь в тройку?
I'll send you right back down where you were before,|Я отправлю тебя обратно туда, где ты был раньше,
because that's the way that works and when we get to the routing process you'll understand what I'm talking about.|потому что именно так работает, и когда мы перейдем к процессу маршрутизации, вы поймете, о чем я говорю.
So, depending on what you're doing is the device that you're going to use,|Итак, в зависимости от того, что вы делаете, это устройство, которое вы собираетесь использовать,
but in today's world the router and the switch are the two devices that are,|но в современном мире маршрутизатор и коммутатор - это два устройства, которые
for sure, you're gonna have on your network.|наверняка у вас будет в вашей сети.
Now, I know these are symbols, these are symbols, so you need to understand these symbols, what they are, the bridge, the|Я знаю, что это символы, это символы, поэтому вам нужно понять эти символы, что они собой представляют, мост,
hub, the switch and the router.|концентратор, коммутатор и маршрутизатор.
But, when you get out there, you're gonna be working in racks.|Но когда вы выйдете отсюда, вы будете работать в стойках.
You know, the first time I went out there and I saw a rack, and I saw these patch panels.|Вы знаете, когда я впервые вышел туда, я увидел стойку и эти патч-панели.
Let me see if I can zoom in on the patch panel, so you can actually see it if you've never seen a patch panel,|Дайте мне посмотреть, смогу ли я увеличить масштаб патч-панели, чтобы вы могли его увидеть, если никогда не видели патч-панель,
because I know it freaked me out when I went out there.|потому что я знаю, что меня это испугало, когда я пошел туда.
I was like, what is this?|Я подумал, что это?
Cuz, I went out there, I was like, I learned on the fly.|Потому что я пошел туда и подумал, что научился на лету.
Okay?|Ладно?
I was, I was a, I er, I learned through fire, or something like that.|Я был ... я ... э ... я научился через огонь или что-то в этом роде.
All these are patch panels.|Все это патч-панели.
You want to have a centralized wiring system.|Вы хотите иметь централизованную систему электропроводки.
All your switches, all your servers, all these routers,|Все ваши коммутаторы, все ваши серверы, все эти маршрутизаторы,
everything is gonna be on this rack.|все будет на этой стойке.
Or it could be multiple racks.|Или это может быть несколько стоек.
And all your wiring is gonna come from your rooms into the,|И вся ваша проводка будет идти из ваших комнат в,
the back of these patch panels.|задняя часть этих патч-панелей.
And there's something called a, a crimper.|И есть что-то, называемое обжимом.
You have strippers that strip the jacket off the cable.|У вас есть стриптизерши, которые снимают куртку с кабеля.
When we talk about cables I'll show you those tools.|Когда мы говорим о кабелях, я покажу вам эти инструменты.
And then you actually crimp the cable into the back of each one of these ports.|И затем вы фактически обжимаете кабель на задней части каждого из этих портов.
And then you use a cable to patch it to whatever switch you're going to go ahead and plug it into.|А затем вы используете кабель, чтобы подключить его к любому переключателю, который вы собираетесь использовать, и подключить его.
And that's how you make it.|И вот как вы это делаете.
You're like a, remember in the old days those operators that would connect your calls, it would go from here to here, here|Вы как, помните, в старые времена те операторы, которые соединяли ваши звонки, шли отсюда сюда, сюда
to there, to connect those calls.|туда, чтобы соединить эти звонки.
Like, in the old days.|Как в былые времена.
That's what you're doing.|Вот что ты делаешь.
You're bringing in the cables.|Вы вводите кабели.
You're punching them in the back of these patch panels.|Вы пробиваете их сзади этих патч-панелей.
And then you're taking another cable,|А потом вы берете другой кабель,
which is called a patch cable, and then you take it from whatever port to whatever switch on whatever floor, or whatever department it is you're plugging|который называется патч-кабелем, и затем вы берете его с любого порта на любой коммутатор на любом этаже или в любой другой отдел, который вы подключаете
it into.|это в.
All right, and when we talk about cabling,|Хорошо, а когда мы говорим о кабелях,
I'm gonna go very deep into that,|Я собираюсь очень углубиться в это,
cuz you really need to understand because this is the reality.|Потому что вам действительно нужно понять, потому что это реальность.
This is what you're gonna see out there,|Это то, что ты увидишь там,
if you go do big networks.|если пойдешь делай большие сети.
If you do a small network, medium sized network,|Если вы делаете небольшую сеть, сеть среднего размера,
a lot of times it'll be in a closet somewhere, they'll have a switch in there,|часто это будет где-то в шкафу, там будет выключатель,
they won't even have a patch panel, and you just running the cables from the switch to the, to the computers, and that's it.|у них даже не будет патч-панели, и вы просто проложите кабели от коммутатора к компьютеру, и все.
I, I've seen that, in many real estate offices.|Я видел это во многих агентствах по недвижимости.
I've seen that in many medical offices,|Я видел это во многих медицинских кабинетах,
where all I have is just a switch sitting somewhere, and they run all the cables from there to wherever else that they need to.|где все, что у меня есть, это просто переключатель, который где-то сидит, и они прокладывают все кабели оттуда туда, где им нужно.
It's, it really shouldn't be that way.|Это действительно не должно быть так.
One, you don't want your inter-networking devices to be compromised.|Во-первых, вы не хотите, чтобы ваши межсетевые устройства были скомпрометированы.
Because one of the things that people ask me, hey [INAUDIBLE] can, you know,|Потому что одна из вещей, о которых меня спрашивают, "эй [НЕРАЗБОРЧИВО] может, вы знаете,
you have a router, let me move this over here.|у вас есть роутер, позвольте мне перенести его сюда.
So you can see that again, bring that back into the picture here.|Так что вы можете снова это увидеть, верните это на картинку здесь.
[INAUDIBLE] on this side, if you see, you don't have your router in your switch,|[НЕДОСТАТОЧНО] на этой стороне, если вы видите, у вас нет маршрутизатора в коммутаторе,
you don't have them sitting in the front desk where people can,|они не сидят на стойке регистрации, где люди могут,
you know, touch it, or, they're, they're somewhere hidden.|знаешь, потрогай его, или они где-то спрятаны.
You don't want it in the broom closet either with all the chemicals and,|Вы не хотите, чтобы он был в туалете для метел со всеми химикатами и,
you know, you got the people going in their mopping and stuff.|вы знаете, вы заставили людей мыть швабры и все такое.
You don't want that,|Вы этого не хотите,
you want your own little area where you're gonna set your things at, okay?|тебе нужна собственная маленькая площадка, где ты собираешься расставить свои вещи, хорошо?
So the reality of it, once you get out there, if you're not already out there,|Итак, реальность этого, как только вы выберетесь, если вы еще не там,
all right, is this.|хорошо, это.
A patch panel, a patch panel.|Патч-панель, патч-панель.
All right?|Отлично?
You can see it right there.|Вы можете увидеть это прямо здесь.
And you have your switch, you have routers.|И у вас есть коммутатор, у вас есть маршрутизаторы.
These are two different types routers that we have right there.|Это два разных типа маршрутизаторов, которые у нас есть.
All right?|Отлично?
And they all go interconnected to each other, all centralized, right there.|И все они связаны друг с другом, все централизованно, прямо здесь.
And you go down.|И вы спускаетесь.
I have a power strip.|У меня есть удлинитель.
You have a power strip they can put on the, on the rack.|У вас есть удлинитель, который они могут поставить на стойку.
You also have a UPS.|У вас также есть ИБП.
Important.|Важный.
Very importante.|Очень важно.
You need to have a UPS.|Вам нужен ИБП.
Lot of power outages,|Много отключений электроэнергии,
you don't want your things to go down, you need to get a UPS, make sure.|вы не хотите, чтобы ваши вещи вышли из строя, вам нужно получить UPS, убедитесь.
All right, so, but one thing we haven't talked about and really in the new CCNA they took that out,|Хорошо, но одна вещь, о которой мы не говорили, и на самом деле в новом CCNA они убрали это,
which is,|который,
you see here my little [LAUGH] wireless access point that Visio has.|вы видите здесь мою маленькую [СМЕХ] точку беспроводного доступа, которая есть в Visio.
All right.|Отлично.
Wireless is part of everybody's network nowadays.|В настоящее время беспроводная связь является частью сети каждого человека.
Everybody uses their wireless access point, as they call it, or wireless router, all right, to get out to the internet, you plug into your modem.|Все используют свою точку беспроводного доступа, как они это называют, или беспроводной маршрутизатор, хорошо, чтобы выйти в Интернет, вы подключаете свой модем.
It takes you out to the internet, and you're wireless.|Он выводит вас в Интернет, и вы получаете беспроводной доступ.
Just be careful, when you're using that,|Просто будьте осторожны, когда используете это,
especially the placement of it.|особенно его размещение.
I don't wanna get too deep, into that particular one,|Я не хочу слишком углубляться в этот конкретный вопрос,
but it is an internet working device.|но это устройство для работы в Интернете.
And I don't wanna get into a wireless.|И я не хочу подключаться к беспроводной сети.
Just be very careful when you're doing wireless.|Просто будьте очень осторожны при использовании беспроводной связи.
Because wireless is, you know,|Потому что беспроводная связь, знаете ли,
one of the biggest problems of wireless is that it's unsecure.|Одна из самых больших проблем беспроводной связи - ее небезопасность.
So, you gotta make sure, you gotta do your [UNKNOWN] and you gotta disable the SSID.|Итак, вы должны убедиться, что вам нужно сделать [НЕИЗВЕСТНО] и отключить SSID.
Now, I heard something, or read something the other day that somebody posted,|Я что-то слышал или читал на днях, что кто-то опубликовал,
I don't know where it was, I don't know where it was, or if it was read to me.|Я не знаю, где это было, я не знаю, где это было, и читали ли это мне.
That that disabling the SSID, all it does is just hide it from the users but it's still being broadcast.|Это отключение SSID, все, что он делает, просто скрывает его от пользователей, но он все еще транслируется.
And I think that individual's correct, the individual's correct.|И я думаю, что этот человек прав, человек прав.
Yes, when you disable your SSID, that is your security set identifier.|Да, когда вы отключаете свой SSID, это идентификатор вашего набора безопасности.
You know, when you call it, you know Spartacus,|Знаешь, когда ты это называешь, ты знаешь Спартак,
or you call it whatever, the name, FBI,|или вы называете это как угодно, имя, ФБР,
whatever you say you wanna call it,|что бы вы ни говорили, вы хотите называть это,
all right don't connect to this wireless access point.|хорошо, не подключайтесь к этой беспроводной точке доступа.
Whatever.|Без разницы.
That's what everybody needs in order to,|Это то, что нужно всем, чтобы,
you know, you find one and you connect to it.|вы знаете, вы находите его и подключаетесь к нему.
And then, if you secured it with some sort of you know, pre-shared key or whatever it is you're using then you put in the password and now you're in.|А затем, если вы защитили его с помощью какого-то известного вам предварительного общего ключа или того, что вы используете, вы вводите пароль, и теперь вы в системе.
[BLANK_AUDIO].|[BLANK_AUDIO].
The SS, the SS ID,|СС, идентификатор СС,
even if you disable it and nobody sees it,|даже если вы отключите его и его никто не увидит,
yes, it is still being broadcasted.|да, он все еще транслируется.
But if, in order for somebody to get it,|Но если, чтобы кто-нибудь это получил,
they need to run special software on there.|им нужно запускать там специальное программное обеспечение.
For homes, that's fine.|Для дома это нормально.
For businesses, there is many different ways in which I'm not gonna get into but there's many different ways to secure a wireless network.|Что касается бизнеса, есть много разных способов, которыми я не собираюсь вдаваться, но есть много разных способов защитить беспроводную сеть.
Just doing the mac filtering and disabling the SSID, and put in pre-sured keys on there and little policies and whatever within whatever the router has,|Просто выполняю фильтрацию Mac и отключение SSID, и вставляем туда заранее определенные ключи, небольшие политики и все, что есть в маршрутизаторе,
it's not enough.|этого не достаточно.
Even if you reduce the amount of power,|Даже если вы уменьшите количество энергии,
it's not enough.|этого не достаточно.
But just understand that wireless is a part of inter-networking.|Но просто поймите, что беспроводная связь - это часть межсетевого взаимодействия.
And the placement of it, which is what I was telling you originally,|И его размещение, о котором я говорил вам изначально,
the placement of it is very important.|его размещение очень важно.
Because remember, everything interferes with wireless.|Помните, что беспроводной сети все мешает.
So, wherever you put it, if you're putting it near fluorescent lighting,|Итак, куда бы вы его ни положили, если вы ставите его рядом с люминесцентным освещением,
if there's brick, or steel walls, or metal file cabinets, and all these different things, they could interfere.|если есть кирпич, или стальные стены, или металлические картотеки, и все эти разные вещи, они могут помешать.
Are there more access points there?|Есть еще точки доступа?
Are they gonna, are they running in the same channel that you are?|Собираются ли они, они работают в том же канале, что и вы?
So, all these things, you gotta take a look, you know,|Итак, все эти вещи, вы должны взглянуть, вы знаете,
take to the, take into consideration before you go ahead and put it.|примите во внимание, прежде чем приступить к делу.
The next thing I wanna show you is, not show you just, just point it out.|Следующее, что я хочу вам показать, это не показать вам, а просто указать на это.
Firewalls, obviously.|Брандмауэры, очевидно.
If you deal with firewalls,|Если вы имеете дело с межсетевыми экранами,
you're definitely gonna have to learn how to configure firewalls.|вам обязательно нужно научиться настраивать межсетевые экраны.
Whatever, there's a million and one different, you know, manufacturers of firewalls, depending who you're using.|Как бы то ни было, существует миллион и один разных производителей межсетевых экранов, в зависимости от того, кого вы используете.
So, you can configure your policies and then, we have this thing right here, the glooming cloud.|Итак, вы можете настроить свои политики, и тогда у нас есть эта вещь, мрачное облако.
Right?|Правильно?
When you see a cloud in a, in a book, all right,|Когда вы видите облако в книге, хорошо,
all it is, it's your provider, let's say.|все это, так сказать, ваш провайдер.
That's what I call it.|Так я это называю.
This is how you get from one side to the other.|Так вы переходите с одной стороны на другую.
So, inside this cloud, you have mainframes, you have servers,|Итак, внутри этого облака у вас есть мэйнфреймы, у вас есть серверы,
you have routers, you have switches.|у вас есть роутеры, у вас есть свитчи.
So, it all, you don't worry about what's in here, when you're creating an inter-network, and you're trying to get, let's say, from one location that's|Итак, вы не беспокоитесь о том, что здесь находится, когда вы создаете межсетевое взаимодействие и пытаетесь получить, скажем, из одного места, которое
across to another, a wide area network,|через другую, глобальную сеть,
and you've gotta go through a provider.|и вы должны пройти через провайдера.
Well, just worry about getting to, to the provider.|Ну, просто беспокойтесь о том, чтобы добраться до провайдера.
And then, the provider will do the rest to get you to the other side.|А затем провайдер сделает все остальное, чтобы вы перешли на другую сторону.
All right.|Отлично.
You just gotta make sure you can get to the provider.|Вы просто должны убедиться, что можете добраться до провайдера.
All right?|Отлично?
That's the thing.|Вот в чем дело.
So, these are internet working devices that we have, and we use on a daily basis.|Итак, это устройства для работы в Интернете, которые у нас есть, и мы используем их ежедневно.
Real world is that rack that I showed you.|Реальный мир - это та стойка, которую я вам показал.
Testing purposes.|Цели тестирования.
What you're gonna really be focused on is really just these two right here.|Вы действительно будете сосредоточены только на этих двоих прямо здесь.
The router and the switch.|Маршрутизатор и коммутатор.
We really need to focus and we will and learn the different parts.|Нам действительно нужно сосредоточиться, и мы будем изучать разные части.
This guy breaks up broadcasts domains by default.|Этот парень по умолчанию разбивает домены вещания.
Awesome.|Потрясающие.
This guy breaks up collision domains by default and if you create [UNKNOWN],|Этот парень по умолчанию разбивает домены коллизий, и если вы создадите [НЕИЗВЕСТНО],
It will break up broadcast domains as well.|Это также разделит широковещательные домены.
So, it brings in a lot of functionality.|Таким образом, он приносит много функциональности.
So, these are your inter-networking devices and these are the devices that we'll be working with and that you'll be learning|Итак, это ваши межсетевые устройства, и это устройства, с которыми мы будем работать и которые вы будете изучать.
on how to configure them, how to use them,|о том, как их настроить, как ими пользоваться,
and how to place them correctly.|и как их правильно разместить.
I'll see you in the next one.|Увидимся в следующем.
[BLANK_AUDIO]|[BLANK_AUDIO]
[BLANK_AUDIO]|[BLANK_AUDIO]
And we're back in the game.|И мы снова в игре.
So, what do I have back here?|Итак, что у меня здесь?
Hey, these are the internetworking devices, or some of them,|Эй, это устройства межсетевого взаимодействия или некоторые из них,
anyway more relevant to your CCNA.|в любом случае более актуален для вашего CCNA.
And some relevant to what you're actually going to see when you get out there.|И некоторые из них относятся к тому, что вы на самом деле увидите, когда выйдете оттуда.
All right?|Отлично?
So there's four devices that you really need to be concentrated on.|Итак, есть четыре устройства, на которых вам действительно нужно сосредоточиться.
Or really two devices but we'll learn all four.|Или действительно два устройства, но мы изучим все четыре.
Two devices for the examination but, as you see, up here we have our router.|Два устройства для осмотра, но, как видите, здесь наш роутер.
Pretty simple, a circle with a bunch of arrows pointing all over the place.|Довольно просто, круг с кучей стрелок, указывающих повсюду.
Right?|Правильно?
So it goes all over, right?|Так что все кончено, правда?
Creates the path to the internetwork.|Создает путь к объединенной сети.
You have a switch.|У вас есть переключатель.
All right?|Отлично?
Router layer 3.|Слой маршрутизатора 3.
When we talk about the OSI, you'll see.|Когда мы будем говорить об OSI, вы увидите.
Switch layer two.|Переключите второй уровень.
Hub, which we just saw.|Хаб, который мы только что видели.
Bad.|Плохой.
Bad hub.|Плохой хаб.
We don't want hubs on our networks.|Нам не нужны концентраторы в наших сетях.
And now we have a bridge, looks like a half pipe,|И вот у нас есть мост, похожий на полутрубку,
something a skateboarder would use, right?|что-то, что может использовать скейтбордист, верно?
So, we have a bridge.|Итак, у нас есть мост.
So, let's talk about this, let's talk about this.|Итак, поговорим об этом, поговорим об этом.
What devices do we use or we would like to use?|Какие устройства мы используем или хотели бы использовать?
Well, we already know and we're talking about Ethernet.|Что ж, мы уже знаем и говорим об Ethernet.
Ethernet, remember Ethernet is a standard that was created.|Ethernet, помните, что Ethernet - это стандарт, который был создан.
An IEEE standard 802.3.|Стандарт IEEE 802.3.
All right, that has an access method.|Хорошо, у этого есть метод доступа.
That is CSMA/CD.|Это CSMA / CD.
Which really is, is just first-come,|Что на самом деле, только в порядке очереди,
first-serve.|первая подача.
All right?|Отлично?
We're all listening, right?|Мы все слушаем, правда?
Carrier sets, we're listening for noise.|Наборы носителей, мы прислушиваемся к шуму.
You could have multiple axis then but you,|Тогда у вас может быть несколько осей, но вы,
you have the collision detection.|у вас есть обнаружение столкновений.
Not two computers can actually be on the cable at the same time.|На самом деле два компьютера не могут быть подключены к кабелю одновременно.
Alright, so that's the problem with Ethernet.|Хорошо, это проблема с Ethernet.
So our job as Cisco professionals as network engineers,|Итак, наша работа как профессионалов Cisco как сетевых инженеров,
we need to reduce the amount of broadcast,|нам нужно уменьшить объем трансляции,
reduce the amount of collisions that exist on a network.|уменьшить количество коллизий, существующих в сети.
And how pray tell do we do that?|И как нам это сделать?
Well, we do that by segmenting,|Что ж, мы делаем это путем сегментации,
segmenting.|сегментирование.
Break it up.|Разбить его.
Collision domains making more collision domains.|Домены столкновения создают больше доменов столкновения.
That sounds kinda like it's contradicting.|Это звучит как бы противоречиво.
Well wait a minute Laz, you want more collision domains?|Подожди минутку, Лаз, ты хочешь больше доменов столкновения?
Yeah, I do.|Да, люблю.
I don't want one huge collision domain.|Мне не нужен один огромный домен коллизий.
It's like having one classroom with 200|Это как в одном классе с 200
students.|ученики.
I'd rather have five classrooms and break those up.|Я бы предпочел иметь пять классов и разбить их.
I don't know the math.|Я не знаю математики.
You wanna break that up.|Ты хочешь разбить это.
Let's say 100 students, four [LAUGH] 25|Допустим, 100 студентов, четыре [СМЕХ] 25
students in each.|студенты в каждом.
That will make 100.|Получится 100.
That will make it easy.|Это облегчит задачу.
Or 50 students if it was 200, right?|Или 50 студентов, если было 200, верно?
See I did the math.|Смотрите, я посчитал.
I did the math.|Я посчитал.
But you want to break that up.|Но ты хочешь разбить это.
You want to break those collision domains.|Вы хотите разрушить эти области столкновения.
So the more collision domains you have collision domains.|Таким образом, чем больше коллизионных доменов, тем больше коллизионных доменов.
That's good.|Это хорошо.
The more broadcast domains you have,|Чем больше у вас широковещательных доменов,
that's even better.|это даже лучше.
So that's what you wanna do, that's the whole point.|Так вот что ты хочешь сделать, в этом весь смысл.
But you need to understand the devices that you're using.|Но вам нужно понимать, какие устройства вы используете.
So let's talk about our little half pipe buddy down here, the bridge.|Итак, давайте поговорим о нашем маленьком приятеле по хаф-пайпу, мосту.
I hope you can see that, I think you can.|Я надеюсь, вы это видите, я думаю, вы можете.
The bridge, its main purpose, is to segment a network.|Мост, его основная цель - сегментировать сеть.
The bridge is software-based.|Мост является программным.
So it's kinda slow.|Так что это довольно медленно.
It is limited on the amount of ports it can have.|Он ограничен количеством портов, которые он может иметь.
Now, I'll throw a term at ya.|А теперь я накину тебе срок.
I'm gonna throw a term.|Я выброшу срок.
And I'll briefly or loosely define it.|И я коротко или вольно определю это.
But once we get to that particular part of the course.|Но как только мы перейдем к этой конкретной части курса.
I'll go deep into it.|Я углублюсь в это.
I will, I promise.|Я буду я обещаю.
The bridge can only have one spanning tree instance.|У моста может быть только один экземпляр связующего дерева.
One spanning tree instance.|Один экземпляр остовного дерева.
And just, spanning tree all it is, it prevents loops.|И просто, остовное дерево все, что есть, предотвращает петли.
Add a layer to your bridging loops at layer two.|Добавьте слой к вашим соединительным петлям на втором слое.
So bridges are the beginning.|Итак, мосты - это начало.
We use bridging that's why they say, you know, software bridging things like that.|Мы используем мосты, вот почему они говорят, ну знаете, такие программные мосты.
So it's slow it's limited on ports.|Так что он медленный, ограничен портами.
So we got rid of the bridge slowly and that's where,|Итак, мы медленно избавились от моста, и вот где,
we definitely got rid of hub.|мы однозначно избавились от хаба.
We [SOUND] done away with hubs.|Мы [ЗВУК] покончили с хабами.
We don't want hubs.|Нам не нужны хабы.
That's your shared collision domain.|Это ваш общий домен конфликтов.
You only have half duplex, why, you can only send or receive.|У вас только полудуплекс, вы можете только отправлять или получать.
Here on a bridge you have the full duplex using two pairs of wires meaning you can send and receive at the same time because|Здесь, на мосту, у вас есть полный дуплекс с использованием двух пар проводов, что означает, что вы можете отправлять и получать одновременно, потому что
you're using two pairs of wires,|вы используете две пары проводов,
that's a good thing.|это хорошая вещь.
Where hubs you're done, so hubs you're pretty much, pretty much over.|Где хабы вы закончили, так хабы вы в значительной степени закончили.
We don't use them in the real world nobody does, don't use them, bad thing.|Мы не используем их в реальном мире, никто не использует их, плохо.
Will they ask you something on the test about hubs?|Вас спросят на тесте о хабах?
If they do, just know it's a bad anything.|Если они это сделают, просто знайте, что это плохо.
It's bad about hubs that's the answer for hubs.|Плохо то, что хабы - это ответ на хабы.
All right, or shared collision domains.|Ладно, или общие коллизионные домены.
Switches, now that's where you're gonna be tested on.|Переключатели, вот где вы собираетесь пройти испытания.
That's gonna be 20% of your grade on all the different things that you can do on the switches.|Это будет 20% вашей оценки за все, что вы можете делать с переключателями.
What can you do?|Что ты можешь сделать?
You can break up well, each port on the switch.|Можно хорошо разбить каждый порт на свитче.
It's its own collision domain.|Это его собственная область коллизий.
So the more things you plug in to it, so you have a 24 port switch or a 48 port switch yeah, 48 collision domains.|Чем больше вещей вы подключаете к нему, тем больше у вас коммутатор на 24 порта или коммутатор на 48 портов, да, 48 конфликтных доменов.
You have that full bandwidth if it's cat 5e.|У вас есть полная пропускная способность, если это cat 5e.
You have that 100 megabit per second, send and receive at the same time.|У вас есть эти 100 мегабит в секунду, отправляйте и получайте одновременно.
If you have a cat 6, you got 1000 megabits per second, send and receive at the same.|Если у вас есть cat 6, вы получаете 1000 мегабит в секунду, отправляйте и получайте одновременно.
So you've broken up those collisions.|Итак, вы разбили те столкновения.
That's awesome.|Это потрясающе.
It's a private collision domain.|Это частный домен коллизий.
The only thing, you have still only one broadcast domain.|Единственное, у вас еще один широковещательный домен.
Which means when people are talking back and forth, regardless of what you hear out there.|Это означает, что люди говорят взад и вперед, независимо от того, что вы слышите.
All right.|Отлично.
They still hear that noise.|Они все еще слышат этот шум.
They still hear that noise.|Они все еще слышат этот шум.
So you still need to break up those broadcast domains.|Так что вам все равно нужно разделить эти широковещательные домены.
And guess what?|И угадайте, что?
That's what switches bring.|Вот что приносят переключатели.
Bridges bring in that segmentation, we wanna break things apart.|Мосты привносят эту сегментацию, мы хотим разбить вещи на части.
We have a group over here, we have a group over here.|У нас есть группа здесь, у нас есть группа здесь.
We'll use a layer three device like a router to intercommunicate with each other.|Мы будем использовать устройство третьего уровня, например маршрутизатор, для взаимодействия друг с другом.
But with a switch, we can break up broadcast domain at layer two, how do we do that by creating VLANs.|Но с помощью коммутатора мы можем разбить широковещательный домен на втором уровне, как нам это сделать, создав VLAN.
We create VLANs down here, virtual local area networks.|Мы создаем здесь VLAN, виртуальные локальные сети.
Now we can have multiple broadcasts on a switch,|Теперь у нас может быть несколько трансляций на коммутаторе,
that is awesome because what happens on the broadcast stays on the broadcast.|Это здорово, потому что все, что происходит в трансляции, остается в трансляции.
So imagine this.|Так что представьте себе это.
You have let's say a school, make things simple.|У вас есть, скажем так, школа, упростите жизнь.
Let's say on one side you have medical students and they're doing their labs and they're doing their things on the computer.|Допустим, с одной стороны, у вас есть студенты-медики, они делают свои лаборатории и делают свои дела на компьютере.
And then right next to them you have a, a networking class.|А рядом с ними у вас класс по сетям.
And these guys, you know, they're doing DACT servers.|И эти ребята, вы знаете, они делают серверы DACT.
They're doing all sorts of crazy stuff,|Они делают разные безумные вещи,
security protocols,|протоколы безопасности,
and they're trying to do hacking stuff.|и они пытаются взломать вещи.
What's gonna happen is if there's one particular,|Что произойдет, если будет одна конкретная,
it goes by default, and keep this in mind.|он идет по умолчанию, и имейте это в виду.
This is something you should keep in mind.|Об этом следует помнить.
So when we get into that, into that particular session.|Итак, когда мы перейдем к этому, к той конкретной сессии.
By default, all switches are part of VLAN one.|По умолчанию все коммутаторы являются частью VLAN one.
All switches are part of VLAN one which means we're all on one broadcast domain.|Все коммутаторы являются частью VLAN one, что означает, что мы все находимся в одном широковещательном домене.
So whatever I do on my VLAN, guess what,|Итак, что бы я ни делал в своей VLAN, угадайте, что
it's gonna affect you.|это повлияет на тебя.
You're gonna hear that noise.|Вы услышите этот шум.
You're gonna get slowed down.|Ты замедлишься.
So if I have DHCP with what a DHCP server,|Итак, если у меня есть DHCP с каким DHCP-сервером,
for those you that may not know or don't remember all right, it assigns IP address.|для тех, кто не знает или не помнит, он назначает IP-адрес.
Or I'll say it correctly, it'll lease IP addresses.|Или я правильно скажу, он будет арендовать IP-адреса.
Be careful with the terminology in the exam.|Будьте осторожны с терминологией на экзамене.
Because in actuality, or I guess, what the reality of it is.|Потому что на самом деле, или я думаю, какова реальность.
That's what a DHCP server does.|Это то, что делает DHCP-сервер.
It leases addresses.|Сдает в аренду адреса.
Right?|Правильно?
We normally say assign.|Обычно мы говорим назначить.
Everybody says assign.|Все говорят: «Назначьте».
But the terminology that they play around with.|Но терминология, с которой они балуются.
Is that it leases addresses, okay?|Это сдает в аренду адреса, хорошо?
Keep, keep that open there.|Держите, держите это открытым там.
So if I have in that classroom a DHCP server and the school itself has a DHCP server, we're not going to clash with each other.|Так что если у меня в классе есть DHCP-сервер, а в самой школе есть DHCP-сервер, мы не собираемся конфликтовать друг с другом.
I'll be assigning IP addresses to a classroom, the DHCP server for the school will be assigning, so it will be chaos.|Я буду назначать IP-адреса классу, DHCP-сервер для школы будет назначать, так что это будет хаос.
It will be chaos, because we didn't segment the broadcast domain, and we do that by creating v-nets.|Будет хаос, потому что мы не сегментировали широковещательный домен, а делаем это, создавая виртуальные сети.
All right?|Отлично?
So that's what the switch brings in.|Вот что дает переключатель.
And we can go ahead, and have that extra functionality by creating those v-nets.|И мы можем продолжить и получить эту дополнительную функциональность, создав эти виртуальные сети.
Not only that, we can set up port security.|Мало того, мы можем настроить безопасность порта.
We can create access lists, we can do what's called EtherChannel.|Мы можем создавать списки доступа, мы можем делать то, что называется EtherChannel.
There's a slew of things that you can do now with the switches,|Теперь вы можете делать множество вещей с помощью переключателей,
that we didn't do before.|чего мы раньше не делали.
So definitely, switches is what you're gonna have in your network.|Таким образом, коммутаторы - это то, что вам нужно в вашей сети.
And if you're building a network, in today's technology,|И если вы строите сеть с использованием современных технологий,
if you're building a network from the ground up, if you're that lucky or you get to upgrade, you say hey, let's go with gigabyte, right?|если вы строите сеть с нуля, если вам так повезет или вам удастся обновить, вы говорите: «Эй, давайте перейдем к гигабайту, верно?
There's a harder way, back in the days of the bust apology and coaxial cable,|Есть более сложный путь, во времена извинений за бюст и коаксиального кабеля,
and, you know, we're running 10 megabytes per second or less, those days are gone.|и, знаете ли, мы работаем со скоростью 10 мегабайт в секунду или меньше, те времена прошли.
Now we want [SOUND] fast, fast,|Теперь мы хотим [ЗВУК] быстро, быстро,
when I send you something I want you to get it right then and there.|когда я посылаю вам что-то, я хочу, чтобы вы получили это прямо сейчас.
The minute I click on that button, you should have it.|Как только я нажму на эту кнопку, она у вас будет.
You go, where, where's that information I just sent you, you don't got it yet?|Вы идете, где, где та информация, которую я вам только что отправил, вы ее еще не получили?
So definitely, you wanna get, if you're gonna buy a switch or you're doing things, you wanna ma, make sure if you're doing it on your own,|Так что определенно, ты хочешь получить, если ты собираешься купить выключатель или делаешь что-то, ты хочешь мам, убедитесь, что ты делаешь это самостоятельно,
right, if you're a consultant and this is your own business, or you're trying to convince your boss, listen, we have a lot|правильно, если вы консультант и это ваше личное дело, или вы пытаетесь убедить своего начальника, послушайте, у нас много
of work, we need to be productive.|работы, нам нужно быть продуктивными.
In order for us to be productive for the size of packets that we're sending on our network, let's say, I always use the example of guys that do surveying,|Скажем, для того, чтобы мы могли продуктивно работать с такими размерами пакетов, которые мы отправляем в нашу сеть, я всегда использую пример парней, которые проводят опросы,
because I worked with surveyors.|потому что я работал с геодезистами.
And they use these, what is it, AutoCAD,|И они используют эти, что это такое, AutoCAD,
these AutoCAD files are huge,|эти файлы AutoCAD огромны,
and they slow down the network a lot, so,|и они сильно замедляют работу сети, поэтому,
you wanna use Cat 6.|вы хотите использовать Cat 6.
So you gotta look at your situation and say hey, what type of device?|Итак, вы должны взглянуть на свою ситуацию и сказать: "Эй, какое устройство?"
Definitely, you're gonna wanna use switches.|Определенно, ты захочешь использовать переключатели.
You're gonna wanna use switches.|Ты захочешь использовать переключатели.
And, keyword here, you want to use managed switches.|И, ключевое слово здесь, вы хотите использовать управляемые переключатели.
Managed, what does that mean?|Управляемый, что это значит?
Remember at the beginning,|Помните в начале,
they were able to go inside a switch, put an IP address and a gateway, and all that.|они могли войти в коммутатор, поставить IP-адрес, шлюз и все такое.
So you can go inside of the switch, and then configure whatever it is you need to configure.|Таким образом, вы можете войти внутрь коммутатора, а затем настроить все, что вам нужно.
All right?|Отлично?
So, definitely switches.|Так что однозначно переключается.
Layer 2 switches really only make a table,|Переключатели уровня 2 действительно составляют только таблицу,
they create a table, what's called the MAC Address Table.|они создают таблицу, которая называется таблицей MAC-адресов.
But we'll get deeper into that.|Но мы углубимся в это.
So that's a Layer 2.|Итак, это уровень 2.
And obviously the Layer 3.|И, очевидно, уровень 3.
This guy, up here, the router, he breaks up broadcast domains by default.|Этот парень здесь, маршрутизатор, он по умолчанию разбивает широковещательные домены.
What does that mean?|Что это значит?
So if he has three interfaces, he's got three different broadcast domains,|Итак, если у него три интерфейса, у него есть три разных широковещательных домена,
which means you have different networks.|это означает, что у вас разные сети.
Different networks.|Разные сети.
Meaning you have the 10, 10, 1, 0.|Это означает, что у вас есть 10, 10, 1, 0.
10, 10, 2, 0.|10, 10, 2, 0.
10, 10, 3, 0.|10, 10, 3, 0.
So you have three separate networks altogether, they can't talk to each other,|Итак, у вас есть три отдельные сети вместе, они не могут общаться друг с другом,
unless you're trying to get to it.|если вы не пытаетесь добраться до него.
Because your router creates a routing table.|Потому что ваш маршрутизатор создает таблицу маршрутизации.
Say hey, where do you want to go?|Скажи, эй, куда ты хочешь пойти?
Oh, you want to go somewhere in the three,|Ой, хочешь куда-нибудь в тройку,
I'll send you right back down where you were before.|Я отправлю тебя обратно туда, где ты был раньше.
Because that's the way that works.|Потому что так работает.
And when we get to the routing process,|И когда мы перейдем к процессу маршрутизации,
you'll understand what I'm talking about.|вы поймете, о чем я говорю.
So depending on what you're doing, is the device that you're gonna use.|Итак, в зависимости от того, что вы делаете, какое устройство вы собираетесь использовать.
But in today's world, the router and the switch are the two devices that are, for sure, you're gonna have on your network.|Но в современном мире маршрутизатор и коммутатор - это два устройства, которые наверняка будут в вашей сети.
Now, I know these are symbols.|Теперь я знаю, что это символы.
These are symbols, so you need to understand these symbols.|Это символы, поэтому вам необходимо понимать эти символы.
What they are, the bridge, the hub, the switch and the router.|Что они собой представляют: мост, концентратор, коммутатор и маршрутизатор.
But when you get out there, you're gonna be working in racks.|Но когда вы выйдете отсюда, вы будете работать в стойках.
You know I'm, first time I went out there and I saw a rack and I saw these patch panels, let me see if I can zoom in on the patch panel,|Вы знаете, я впервые пошел туда и увидел стойку и эти патч-панели, позвольте мне посмотреть, могу ли я увеличить патч-панель,
so you can actually see it, if you've never seen a patch panel.|так что вы действительно можете это увидеть, если никогда не видели патч-панель.
Cause I know it freaked me out when I went out there.|Потому что я знаю, что меня это испугало, когда я пошел туда.
It's like, what is this?|Это типа, что это?
Cuz, I went out there, I was like, I learned on the fly.|Потому что я пошел туда и подумал, что научился на лету.
Okay?|Ладно?
I, I was, how you say,|Я, я был, как вы говорите,
I I learned through fire, or something like that.|Я научился через огонь или что-то в этом роде.
All these are patch panels.|Все это патч-панели.
You wanna have a centralized wiring system.|Вы хотите иметь централизованную систему проводки.
All your switches, all your servers, all these co,|Все ваши коммутаторы, все ваши серверы, все это,
routers, everything is gonna be on this rack.|маршрутизаторы, все будет на этой стойке.
Or it could be multiple racks.|Или это может быть несколько стоек.
And all your wiring is gonna come from your rooms into the,|И вся ваша проводка будет идти из ваших комнат в,
the back of these patch panels.|задняя часть этих патч-панелей.
And there's something called a, a crimper.|И есть что-то, называемое обжимом.
They are strippers that strip the jacket of the cable.|Это стрипперы, снимающие оболочку кабеля.
When we talk about cables, I'll show you those tools.|Когда мы говорим о кабелях, я покажу вам эти инструменты.
And then you actually crimp the cable into the back of each one of these ports.|И затем вы фактически обжимаете кабель на задней части каждого из этих портов.
And then you use a cable to patch it to whatever switch you're gonna go ahead and plug it into.|И затем вы используете кабель, чтобы подключить его к любому переключателю, который вы собираетесь использовать, и подключите его.
And that's how you make it.|И вот как вы это делаете.
You're like a, remember in the old days those operators that will connect your calls that will go from here to here,|Вы как, помните, в старые времена тех операторов, которые будут соединять ваши звонки, которые будут идти отсюда сюда,
here, there,|здесь,
to connect those calls, like in the old days?|чтобы соединить эти звонки, как в старые времена?
That's what you're doing.|Вот что ты делаешь.
You're bringing in the cables, you punch them in the back of these patch panels,|Вы вводите кабели, вы втыкаете их сзади в эти патч-панели,
and then you're taking another cable,|а потом берете другой кабель,
which is called a patch cable, and then you take it from whatever port to whatever switch on whatever floor or whatever the department is you're plugging|который называется патч-кабелем, и затем вы берете его с любого порта на любой коммутатор на любом этаже или в другом отделе, который вы подключаете
into.|в.
All right, and we'll talking about cabling.|Хорошо, а мы поговорим о кабелях.
I'll go very deep into that, because you really need to understand,|Я углублюсь в это, потому что вам действительно нужно понять,
because this is the reality.|потому что это реальность.
This is what you're gonna see out there.|Вот что вы там увидите.
If you go do big networks.|Если вы идете делать большие сети.
If you do a small network, medium sized network, a lot of times, they'll,|Если вы используете небольшую сеть, сеть среднего размера, часто они,
it'll be in a closet somewhere.|это будет где-то в шкафу.
They'll have a switch in there.|Там будет переключатель.
They won't even have a patch panel, and you just run in the cables from the switch to the, to the computers and that's it.|У них даже не будет патч-панели, просто проложите кабели от коммутатора к компьютеру, и все.
I've, I've seen that In many real estate offices.|Я, я видел это во многих офисах недвижимости.
I've seen that in many medical offices,|Я видел это во многих медицинских кабинетах,
where all they have is just a switch sitting somewhere, and they run all the cables from there to wherever it is that they need to.|где все, что у них есть, - это просто переключатель, который где-то стоит, и они прокладывают все кабели оттуда туда, где им нужно.
It's, it really shouldn't be that way.|Это действительно не должно быть так.
One, you don't want your internetworking devices to be compromised.|Во-первых, вы не хотите, чтобы ваши межсетевые устройства были скомпрометированы.
Cuz one of the things that people ask me,|Потому что одна из вещей, о которых меня спрашивают,
hey Laz, can you know, you have a router.|Эй, Лаз, ты знаешь, у тебя есть роутер.
Let me move this over here, so you can see that again.|Позвольте мне переместить это сюда, чтобы вы снова это увидели.
Bring that back into the picture here.|Верните это на картинку.
All right.|Отлично.
Well, it'll be on this side.|Хорошо, это будет на этой стороне.
If you see a, you know, you don't have your router and your switch, you don't have them sitting in the front desk, where people can,|Если вы видите, вы знаете, что у вас нет маршрутизатора и коммутатора, у вас нет их на стойке регистрации, где люди могут,
you know, touch it or, there's somewhere hidden.|знаете, прикоснитесь к нему или там где-то спрятано.
You don't want it in the broom closet either, where all the chemicals and,|Вы также не хотите, чтобы это было в шкафу для метел, где все химикаты и,
you know, you've got the people going in there mopping.|вы знаете, у вас есть люди, идущие там мыть шваброй.
You don't want that,|Вы этого не хотите,
you want your own little area where you're gonna set your things at.|вам нужна собственная маленькая площадка, где вы собираетесь расставить свои вещи.
Okay?|Ладно?
So the reality of it once you get out there,|Итак, реальность этого, когда вы выйдете отсюда,
if you're not already out there, all right, is this.|если вы еще не там, хорошо, вот это.
A patch panel, a patch panel, all right?|Патч-панель, патч-панель, понятно?
You can see it right there and you have your switch.|Вы можете увидеть это прямо здесь, и у вас есть переключатель.
You have routers.|У вас есть роутеры.
These are two different type routers that we have right there, all right,|Это два роутера разных типов, которые у нас есть, хорошо,
and they all go interconnected to each other.|и все они связаны друг с другом.
All centralized right there.|Здесь все централизовано.
You go down, I have a power strip,|Вы идете вниз, у меня есть удлинитель,
you've got a power strip they can put on the on the rack.|у вас есть удлинитель, который они могут поставить на стойку.
You also have a UBS, important, very importante, you need to have a UBS.|У вас также есть UBS, важно, очень важно, вам нужно иметь UBS.
A lot of power outages,|Много отключений электроэнергии,
you don't want your things to go down, you need to get a UBS.|вы не хотите, чтобы ваши вещи падали, вам нужно получить UBS.
Make sure.|Удостовериться.
All right so, but one thing we haven't talked about, and really,|Хорошо, но одна вещь, о которой мы не говорили, и правда,
in the new CCNA, they took that out, which is,|в новом CCNA они убрали это, а именно:
you see here, my little wireless access point that Vizio has.|вы видите здесь мою маленькую точку беспроводного доступа, которая есть у Vizio.
All right?|Отлично?
Wireless is part of everybody's network nowadays.|В настоящее время беспроводная связь является частью сети каждого человека.
Everybody uses a wireless access point, as they call it, or wireless router,|Все используют точку беспроводного доступа, как они ее называют, или беспроводной маршрутизатор,
all right, to get out to the Internet, you plug into your modem,|хорошо, чтобы выйти в Интернет, вы подключаете свой модем,
it takes you out to the Internet, and you're wireless.|он выводит вас в Интернет, и вы получаете беспроводной доступ.
Just be careful when you're using that,|Просто будьте осторожны, когда используете это,
especially the placement of it.|особенно его размещение.
I don't wanna get too deep into that particular one, but it is an internet working device and I now wanna get into a wireless.|Я не хочу слишком углубляться в это конкретное, но это устройство для работы с Интернетом, и теперь я хочу использовать беспроводную связь.
Just be very careful when you're doing wireless because wireless is, you know,|Просто будьте очень осторожны, когда используете беспроводную связь, потому что беспроводная связь, знаете ли,
one of the biggest problems with wireless is that it's unsecure.|одна из самых больших проблем беспроводной связи - ее небезопасность.
So you gotta make sure,|Так что ты должен убедиться,
you gotta do your MAC filtering and you gotta disable the SSID.|вам нужно выполнить фильтрацию MAC-адресов и отключить SSID.
Now I heard something or read something the other day that somebody posted.|Теперь я что-то слышал или читал на днях, что кто-то опубликовал.
I don't know where it was.|Не знаю, где это было.
I don't know where it was or it was read to me, that that disabling the SSID all it does is just hides it from the users, but it's still being broadcast.|Я не знаю, где это было, или мне прочитали, что отключение SSID - все, что он делает, просто скрывает его от пользователей, но он все еще транслируется.
And I think the individual's correct.|И я думаю, что человек прав.
The individual's correct.|Человек правильный.
Yes, when you disable your SSID, that is your security set identifier.|Да, когда вы отключаете свой SSID, это идентификатор вашего набора безопасности.
You know, when you call it, you know Spartacus.|Вы знаете, когда вы называете это, вы знаете Спартак.
Or you call it whatever, the name, FBI,|Или вы называете это как угодно, имя, ФБР,
whatever it is that you wanna call it.|как бы вы это ни называли.
All right?|Отлично?
Don't connect to this wireless access point, whatever.|Ни в коем случае не подключайтесь к этой беспроводной точке доступа.
That's what everybody needs in order to,|Это то, что нужно всем, чтобы,
you know, you find one, and you connect to it.|вы знаете, вы находите его и подключаетесь к нему.
And then, if you secured it with some sort of you know pre-shared key or whatever it is you're using then you put in the password and now you're in.|А затем, если вы защитили его с помощью какого-то известного вам предварительного общего ключа или того, что вы используете, вы вводите пароль, и теперь вы в системе.
The SS, the SS ID, even if you disable it and nobody sees it, yes,|SS, SS ID, даже если вы отключите его и его никто не увидит, да,
it's still being broadcasted.|это все еще транслируется.
But if, in order for somebody to get it, they need to run special software on there.|Но если для того, чтобы кто-то это получил, им нужно запустить там специальное программное обеспечение.
For homes, that's fine.|Для дома это нормально.
For businesses there's many different ways, which I'm not gonna get into, but there's many different ways to secure a wireless network.|Для бизнеса есть много разных способов, в которые я не буду вдаваться, но есть много разных способов защитить беспроводную сеть.
Just doing the MAC filtering, and disabling the SSID.|Просто выполняю фильтрацию MAC и отключая SSID.
And putting pre-shared keys on there and little policies and whatever,|И помещать туда предварительно общие ключи и небольшие политики и все такое,
within whatever the router has, is not enough.|внутри того, что есть у маршрутизатора, этого недостаточно.
Even if you reduce the amount of power,|Даже если вы уменьшите количество энергии,
it's not enough.|этого не достаточно.
But just understand that wireless is a part of internet working.|Но просто поймите, что беспроводная связь - это часть работы Интернета.
And the placement of it, which is what I was telling you originally,|И его размещение, о котором я говорил вам изначально,
the placement of it is very important.|его размещение очень важно.
Because remember, everything interferes with wireless or wherever you put it.|Потому что помните, что все мешает работе беспроводной сети или где бы вы это ни поставили.
If you're putting it near for some lighting, if there's brick or steel walls or metal file cabinets and all these different things, it could interfere.|Если вы поставите его рядом для освещения, если есть кирпичные или стальные стены или металлические картотеки и все эти разные вещи, это может помешать.
Are there more access points there?|Есть еще точки доступа?
Are they gonna, are they running in the same channel that you are?|Собираются ли они, они работают в том же канале, что и вы?
So all these things, you gotta take a look.|Так что все это, ты должен взглянуть.
You know, take to, take into consideration before you go in and put it.|Вы знаете, примите во внимание, прежде чем вы войдете и положите это.
The next thing I wanna show you is, not show you, just, just point it out.|Следующее, что я хочу вам показать, это не показывать вам, а просто указать на это.
Firewalls, obviously.|Брандмауэры, очевидно.
If you deal with firewalls,|Если вы имеете дело с межсетевыми экранами,
you're definitely gonna have to learn how to configure firewalls.|вам обязательно нужно научиться настраивать межсетевые экраны.
Whatever.|Без разницы.
There's a million and one different, you know, manufacturers of firewalls, depending on who you're using.|Есть миллион и один производитель межсетевых экранов, в зависимости от того, кого вы используете.
So you can configure your policies.|Таким образом, вы можете настроить свои политики.
And then, we have this thing right here,|А потом у нас есть вот эта штука,
the glooming cloud, all right?|мрачное облако, хорошо?
When you see a cloud in a, in a book, all right,|Когда вы видите облако в книге, хорошо,
all it is, is your provider, let's say.|все это, скажем так, ваш провайдер.
That's how I call it.|Я так это называю.
This is how you get from one side to the other.|Так вы переходите с одной стороны на другую.
So inside this cloud you have mainframes,|Итак, внутри этого облака есть мэйнфреймы,
you have servers, you have routers,|у вас есть серверы, у вас есть маршрутизаторы,
you have switches.|у вас есть переключатели.
So it all, you don't worry about what's in here.|Так что не беспокойтесь о том, что здесь.
When you're creating an intra-network and you're trying to get,|Когда вы создаете внутреннюю сеть и пытаетесь получить,
let's say, from one location that's across to another, a wide area network,|скажем, из одного места в другое, в глобальную сеть,
and you gotta go through a provider, well just worry about getting to,|и вам нужно обратиться к провайдеру, просто беспокойтесь о том, чтобы добраться,
to the provider and then the provider will do the rest to get you to the other side.|к провайдеру, а затем провайдер сделает все остальное, чтобы вы перешли на другую сторону.
All right?|Отлично?
You just gotta make sure you can get to the provider.|Вы просто должны убедиться, что можете добраться до провайдера.
All right?|Отлично?
That's the thing.|Вот в чем дело.
So these are internet working devices that we have and we use on a daily basis.|Итак, это устройства для работы в Интернете, которые у нас есть и которые мы используем ежедневно.
Real world is that rack that I showed you.|Реальный мир - это та стойка, которую я вам показал.
Testing purposes, what you're gonna really be focused on is really just these two right here.|В целях тестирования вы действительно будете сосредоточены именно на этих двоих прямо здесь.
The router and the switch.|Маршрутизатор и коммутатор.
We really need to focus, and we will, and learn the different parts.|Нам действительно нужно сосредоточиться, и мы будем учиться на разных частях.
This guy breaks up broadcast domains by default.|Этот парень по умолчанию разбивает широковещательные домены.
Awesome.|Потрясающие.
This guy breaks up collision domains by default, and if you create VLANs,|Этот парень по умолчанию разбивает домены коллизий, и если вы создаете VLAN,
it will break up broadcast domains as well.|он также разбивает широковещательные домены.
So it brings in a lot of functionality.|Так что он приносит много функциональности.
So these are your internet working devices, and these are the devices that we'll be working with and that you'll be learning|Итак, это ваши рабочие устройства в Интернете, и это устройства, с которыми мы будем работать и которые вы будете изучать.
on how to configure them, how to use them,|о том, как их настроить, как ими пользоваться,
and how to place them correctly.|и как их правильно разместить.
I'll see you in the next one.|Увидимся в следующем.
[BLANK_AUDIO]|[BLANK_AUDIO]