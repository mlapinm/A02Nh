D:\mailCloud\prjother\tmp\1\c87_Turning STP off and Guarding against BPDUs on ports not using STP.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
Welcome back.|Добро пожаловать.
Now that we know how to manipulate spanning tree by changing the priority number on the switch that we desire to be the root bridge,|Теперь, когда мы знаем, как управлять связующим деревом, изменяя номер приоритета на коммутаторе, который мы хотим быть корневым мостом,
spanning tree can be somewhat of a nuisance.|остовное дерево может быть в некоторой степени неприятным.
If we know where we're gonna plug in our end nodes.|Если мы знаем, куда мы будем подключать наши конечные узлы.
Because really, spanning tree is looking at ports, it's looking at all the ports.|Потому что на самом деле связующее дерево смотрит на порты, оно смотрит на все порты.
But the ports that we need to be concerned with as far as which interface to switch,|Но порты, которые нам нужно решить, чтобы переключить интерфейс,
switch to router, other internetworking devices.|переключиться на маршрутизатор, другие межсетевые устройства.
If you know that your gonna be plugging into these particular ports end nodes,|Если вы знаете, что собираетесь подключаться к этим конкретным конечным узлам портов,
like, you know, your PC, your printer, a phone, things of that nature,|например, ваш компьютер, принтер, телефон и тому подобное,
then we can safely turn off spanning tree in those ports, all right.|тогда мы можем безопасно отключить связующее дерево в этих портах, хорошо.
And they can turn into forwarding state almost immediately.|И они могут практически сразу перейти в состояние пересылки.
We don't have to wait that period of time while spanning tree's analyzing the port.|Нам не нужно ждать этот период времени, пока связующее дерево анализирует порт.
So we're gonna learn how to turn off spanning tree.|Итак, мы узнаем, как отключить остовное дерево.
But, and by the same token, you know, even though we're living in an,|Но, к тому же, вы знаете, хотя мы живем в
in an era, in the age of communication technology, right, we don't communicate.|в эпоху, в век коммуникационных технологий, мы не общаемся.
We don't communicate with the people who work with us, so.|Мы не общаемся с людьми, которые с нами работают, поэтому.
If by, if we do turn off spanning trees on certain ports and you don't tell people like your IT workers,|Если, если мы отключим связующие деревья на определенных портах, и вы не скажете об этом людям, подобным вашим ИТ-работникам,
and they plug in an internetworking device into that port,|и они подключают межсетевое устройство к этому порту,
it could create a switching loop, right?|он может создать петлю переключения, не так ли?
So, not only are we gonna learn how to turn off spanning tree,|Итак, мы не только научимся отключать связующее дерево,
we're gonna learn how to guard against things like that happening.|мы узнаем, как защититься от подобных вещей.
All right, you may get asked questions on this, in your examination.|Хорошо, вам могут задать вопросы по этому поводу на экзамене.
I honestly haven't heard that much about all of that, but you're gonna go ahead and learn it now.|Честно говоря, я не слышал так много обо всем этом, но вы собираетесь изучить это сейчас.
It's really not that difficult,|Это действительно не так уж и сложно,
but let's see what happens when you plug in a computer and you've seen it already the, on a port that spanning tree is working on.|но давайте посмотрим, что происходит, когда вы подключаете компьютер и уже видели это на порту, над которым работает связующее дерево.
So, let's get a PC out here.|Итак, давайте возьмем здесь ПК.
Let's just drag two PCs right off, right off the bat.|Давайте просто перетащим сразу два ПК, сразу же.
And I'm gonna plug it in to switch three.|И я подключу его, чтобы переключить три.
That's plenty of cable.|Кабеля много.
And just pick a cable here.|И просто выберите кабель здесь.
Let's plug it into cable number or port number three.|Давайте подключим его к кабелю номер или порт номер три.
You see that orange light, it's spanning tree, it's looking at that.|Вы видите этот оранжевый свет, это остовное дерево, он смотрит на него.
It's making that decision hey, in this port,|Он принимает это решение, эй, в этом порту,
can I turn it into a designated forwarding port?|могу я превратить его в назначенный порт пересылки?
So information can be forwarded out of that port?|Значит, информация может быть отправлена ​​из этого порта?
So it needs to know what to do with it.|Поэтому ему нужно знать, что с этим делать.
It's not an internetworking device,|Это не межсетевое устройство,
it will always turn that port to designated forwarding.|он всегда будет переключать этот порт на назначенную переадресацию.
But you see it takes time, it takes that 30 to 60, sometimes even longer, for that port to change.|Но, как видите, требуется время, от 30 до 60, а иногда и дольше, чтобы этот порт сменился.
Excuse me.|Прошу прощения.
For that port to even change, so unless,|Чтобы этот порт даже изменился, так что если,
just sit here, and just watch it.|просто сиди здесь и просто наблюдай.
Well it's never, they finally turn green.|Ну это никогда, они наконец позеленеют.
So now your able to forward information.|Итак, теперь вы можете пересылать информацию.
If you were to look at that particular port.|Если вы посмотрите на этот конкретный порт.
Let's look at it.|Посмотрим на это.
Oh, my God.|О Боже.
Was I in the way?|Я мешал?
Did you, were you able to see?|Вы могли видеть?
Let's, hold up.|Давай, подожди.
Yeah, you were able to see that.|Да, вы могли это видеть.
Okay.|Ладно.
All right, so, let's take a look at this.|Хорошо, давайте посмотрим на это.
Enable.|Включить.
So, we're gonna do show spanning tree.|Итак, мы собираемся показать остовное дерево.
You can see that port number three is designated forwarding, all right?|Вы видите, что порт номер три предназначен для пересылки, хорошо?
So, but it took spanning tree, you know,|Итак, но для этого потребовалось остовное дерево, знаете ли,
forever and a day, at least for today,|навсегда и день, по крайней мере, на сегодня,
right, cause, you know, we gotta, that hit that little bit of bug in every second tool, cause we want instant gratification.|правильно, потому что, вы знаете, нам нужно, чтобы эта маленькая ошибка обнаруживалась в каждом втором инструменте, потому что мы хотим мгновенного вознаграждения.
[COUGH] So,|[КАШЕ] Итак,
we can get that instant gratification by turning off spanning tree.|мы можем получить это мгновенное удовлетворение, отключив остовное дерево.
And I'll do it in this switch right here,|И я сделаю это в этом переключателе прямо здесь,
and I'll just do it at one port or you can do it at a range of ports.|и я просто сделаю это на одном порту, или вы можете сделать это на нескольких портах.
All right, so let's say, let's maximize this.|Хорошо, так что давайте максимизируем это.
[BLANK_AUDIO]|[BLANK_AUDIO]
Enable configt interface, let's do a range.|Включите интерфейс configt, давайте сделаем диапазон.
Range f0/3, let's say -10.|Диапазон f0 / 3, допустим -10.
So what we're gonna do is we're going to turn off spanning tree on these ports because we're gonna tell everybody that works with us in the IT right?|Итак, что мы собираемся сделать, так это отключить связующее дерево на этих портах, потому что мы собираемся сказать всем, кто работает с нами в ИТ?
There's probably only two guys anyway and cause we are, you know,|В любом случае, там, наверное, всего два парня, и потому что мы, знаете ли,
IT people are jack of all trades and we know everything.|ИТ-специалисты - мастера на все руки, и мы все знаем.
We're gonna turn on spanning tree in these particular ports.|Мы собираемся включить связующее дерево в этих конкретных портах.
So how do we do that?|Итак, как нам это сделать?
Spanning tree, I tab,|Связующее дерево, вкладка I,
spanning-tree port fast.|порт связующего дерева быстро.
Once you hit Enter, it's gonna give you a warning.|Как только вы нажмете Enter, появится предупреждение.
Are you sure you wanna do this?|Вы уверены, что хотите это сделать?
Are you sure that you wanna turn off spanning tree doing the port fast command?|Вы уверены, что хотите отключить связующее дерево, выполнив команду быстрого порта?
Caution, caution, caution.|Осторожно, осторожно, осторожно.
If someone plugs in some sort of internetworking device here,|Если кто-то подключит сюда какое-то межсетевое устройство,
you could cause switching loops.|вы можете вызвать петли переключения.
All right, so that's a problem when you turn that off.|Хорошо, это проблема, когда ты это выключаешь.
Well it's a program because you again, you don't tell old people, hey,|Что ж, это программа, потому что ты снова не говоришь старикам, эй,
I turn off the, you know, documentation,|Я отключаю документацию,
all that good stuff.|все это хорошее.
You need to do that, but let's guard against that.|Вам нужно это сделать, но давайте остерегаемся этого.
How do we do that?|Как мы это делаем?
We do spanning tree bpduguard enable.|Делаем связующее дерево bpduguard enable.
What does that mean?|Что это значит?
I am guarding against any bridge protocol data units that I may see coming my way.|Я защищаюсь от любых блоков данных протокола моста, которые могут встретиться на моем пути.
So, if somebody plugs in a switch there accidentally, that port's gonna see, hey,|Итак, если кто-то случайно включит там коммутатор, этот порт увидит, эй,
or those ports will see, hey I see a BPDU coming my way.|или эти порты увидят, эй, я вижу, что BPDU приближается.
You know, what am I gonna do, I'm gonna shut down the port.|Знаешь, что мне делать, я закрою порт.
It turns the port into something called error disable.|Это превращает порт в то, что называется отключением ошибки.
Error disable.|Ошибка отключения.
And it won't allow, you know, any traffic to come through there.|И это не позволит, знаете ли, никакому трафику туда пройти.
So that's you wanna put bpduguard enable.|Итак, вы хотите включить bpduguard.
That's its purpose.|Это его цель.
That its purpose.|Это его цель.
So let's see.|Так что посмотрим.
Let's see what happens.|Давай посмотрим что происходит.
Let's give this a try.|Давай попробуем.
Now, as pushed three through ten, so I'm just gonna plug it into port three,|Теперь, когда нажали с третьего по десять, я просто подключу его к третьему порту,
get a cable.|достаньте кабель.
[BLANK_AUDIO]|[BLANK_AUDIO]
Click on [UNKNOWN], click on port three.|Щелкните [НЕИЗВЕСТНО], щелкните порт три.
Boo.|Бу.
Right there.|Прямо там.
Immediately, designated 40.|Сразу обозначили 40.
And that's what we want.|И мы этого хотим.
We wanna tweak our network so as soon as we plug things in,|Мы хотим настроить нашу сеть так, чтобы, как только мы ее подключили,
things start working right away.|все сразу начинает работать.
But it takes planning.|Но это требует планирования.
It takes planning, it takes design,|Требуется планирование, требуется дизайн,
obviously.|очевидно.
You just don't start throwing things out there, and start doing, you know,|Вы просто не начинаете выбрасывать вещи, а начинаете делать, знаете ли,
you gotta run your cables, you know.|Знаешь, тебе нужно прокладывать кабели.
You gotta plan and design everything ahead of time.|Вы должны планировать и проектировать все заранее.
So, always in IT, the work is upfront.|Так что в IT всегда работа идет заранее.
Once the work is done right, then you can sit back and pretty much drink coffee all day, and just watch your network, as smooth as it is, all right.|Как только работа сделана правильно, вы можете сидеть сложа руки и пить кофе в течение всего дня и просто наблюдать за своей сетью, как бы гладко она ни была, хорошо.
But let's see what happens.|Но посмотрим, что получится.
Let's test the theory.|Давайте проверим теорию.
Let's test the theory.|Давайте проверим теорию.
Let's plug in a switch.|Давайте подключим выключатель.
All right, I'm the IT guy, that they, they didn't tell me anything.|Хорошо, я айтишник, они, они мне ничего не сказали.
They don't tell a lot of us anything.|Многим из нас они ничего не говорят.
They gonna screw it up.|Они собираются облажаться.
I'm the new guy on the block.|Я новый парень в районе.
You know how they like to mess around with new guys.|Вы знаете, как они любят возиться с новичками.
Let's plug it into port ten.|Подключим его к десятому порту.
All right.|Отлично.
Oh, look, it turned red.|Ой, посмотри, он стал красным.
It turned red.|Он стал красным.
Let's take a look at those ports.|Давайте посмотрим на эти порты.
Uh-oh.|Ой-ой.
Something happened.|Что-то произошло.
[BLANK_AUDIO]|[BLANK_AUDIO]
Let's take a look, I'll show start, see if we can see it through there.|Давайте посмотрим, я покажу начало, посмотрим, сможем ли мы его там увидеть.
Oh, come on.|Да ладно тебе.
Okay.|Ладно.
Show start.|Показать начало.
As you can see, spanning tree port files have been inpro, are enabled.|Как видите, файлы портов связующего дерева были включены в pro, включены.
We go to port 10.|Заходим в порт 10.
We cant see it through there, okay.|Мы не можем увидеть это там, хорошо.
So we go to, show interface f0/10,|Итак, мы переходим, показываем интерфейс f0 / 10,
and there it is right here.|и вот оно прямо здесь.
Error disabled, error disabled.|Ошибка отключена, ошибка отключена.
That port, it is now down.|Этот порт сейчас не работает.
So no information can go through there and that's the BPDU guard that did that.|Таким образом, никакая информация не может пройти через него, и это сделал охранник BPDU.
It turned that port into a err-disabled,|Это превратило этот порт в отключенный из-за ошибки,
err-disabled.|err-disabled.
All you really gotta do is, obviously,|Все, что вам действительно нужно, это, очевидно,
unplug the switch.|отключите выключатель.
All right, cause the switch doesn't belong there.|Ладно, потому что переключатель здесь не место.
Oh no, cancel.|О нет, отменить.
Unplug the switch.|Отключите выключатель.
It's still gonna stay in that error disabled state as you can see.|Как видите, он по-прежнему останется в отключенном состоянии из-за ошибки.
So we're gonna go inside there, configt,|Так что мы пойдем туда, конфиг,
and we'll do a no shut.|и мы сделаем не закрытие.
Oops, sorry.|Ой, извини.
Interface f0/10.|Интерфейс f0 / 10.
Let's do a shut.|Давай заткнемся.
No shuts.|Никаких затворов.
Oh, I'm in the wrong interface, wow.|О, я ошибся в интерфейсе, вау.
Interface f0/10.|Интерфейс f0 / 10.
There we go.|Вот и все.
We're gonna do a shut, no shut.|Мы собираемся закрыть, не закрывать.
All right, so we should be able to now,|Хорошо, теперь у нас должна быть возможность
should have gone to normal state.|должен был перейти в нормальное состояние.
Now, should have gotten out of that error disable state in a show interface f0/10.|Теперь нужно было выйти из состояния отключения при ошибке в интерфейсе шоу f0 / 10.
So it's not just disabled.|Так что дело не только в отключении.
It's just down.|Это просто вниз.
But, it's just no longer an error disabled.|Но это просто больше не ошибка отключена.
All right, so we can turn it on if we had to for whatever reason.|Хорошо, так что мы можем включить его, если потребуется по какой-либо причине.
But it takes it out of the changes.|Но он убирает его из изменений.
Kind of flip it.|Типа перевернуть.
Shut and no shut.|Заткнись и не закройся.
And it'll go ahead and go back to normal.|И он пойдет и вернется в норму.
Go back to normal.|Вернись к нормальной жизни.
But that's BPDU guard and turning off spanning tree.|Но это защита BPDU и отключение связующего дерева.
So will you do it?|Так ты сделаешь это?
Sure, why not.|Конечно, почему бы и нет.
You can do that safely.|Вы можете сделать это безопасно.
You know where you're gonna plug in your port, your end devices at.|Вы знаете, куда вы собираетесь подключить свой порт, ваши конечные устройства.
You can draw a spanning tree there.|Вы можете нарисовать там остовное дерево.
Just remember, really spanning tree is concerned about internetworking devices.|Просто помните, что на самом деле связующее дерево связано с устройствами межсетевого взаимодействия.
So if you're plugging in hubs,|Итак, если вы подключаете концентраторы,
concentrators,|концентраторы,
other bridges/switches routers, all that.|другие мосты / коммутаторы-роутеры и все такое.
You don't turn off spanning tree there.|Вы не отключаете там остовное дерево.
But if you're plugging in end devices like, again, computers,|Но если вы подключаете конечные устройства, например, компьютеры,
printers, phones, plotters, whatever,|принтеры, телефоны, плоттеры, что угодно,
scanners, things of that nature.|сканеры, подобные вещи.
End devices that don't send any BDPUs.|Конечные устройства, которые не отправляют BDPU.
It is safe to turn off spanning tree and those ports.|Можно безопасно отключить связующее дерево и эти порты.
But, just in case, you have that one individual or, you know,|Но на всякий случай у вас есть этот человек или, знаете,
that doesn't know any better, or somebody that's trying to do something malicious and plug in their own switch.|кто не знает ничего лучше, или кто-то, кто пытается сделать что-то вредоносное и подключить свой собственный переключатель.
I don't know why anybody'd be walking in with a switch unless you belong to the IT department and you bought a new switch or whatever the case may be.|Я не знаю, зачем кому-то приходить с коммутатором, если вы не принадлежите к ИТ-отделу и не купили новый коммутатор, или в любом другом случае.
But, either way, you don't wanna accidentally plug something in,|Но в любом случае вы не хотите случайно что-то подключить,
into a port that you've turned off spanning tree.|в порт, который вы отключили связующее дерево.
So, you definitely wanna guard yourself against that by doing the BPDU guard enable.|Итак, вы определенно хотите защитить себя от этого, включив защиту BPDU.
And again, spanning-tree bpdugauard enable and you do it within the ports.|И снова, включение связующего дерева bpdugauard, и вы делаете это внутри портов.
And then you turn off, oh, obviously cause you turn off spanning tree.|А затем вы выключаете, о, очевидно, потому что вы выключаете остовное дерево.
And that's it.|И это все.
That's all there is to that.|Вот и все.
All right.|Отлично.
So now you know all about spanning tree.|Итак, теперь вы знаете все о связующем дереве.
Pretty simple.|Довольно просто.
Not a big deal.|Не так уж и важно.
But again, get ready because towards the end of this switching ca the switching portion of this course, we gonna put all this stuff together.|Но опять же, будьте готовы, потому что ближе к концу этого переключения или части этого курса мы соберем все это вместе.
And we're gonna create a very nice big lab.|И мы собираемся создать очень хорошую большую лабораторию.
So be ready for that.|Так что будьте к этому готовы.
I'll see you in the next session.|Увидимся на следующем сеансе.
[BLANK_AUDIO]|[BLANK_AUDIO]