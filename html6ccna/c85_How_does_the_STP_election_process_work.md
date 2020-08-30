D:\mailCloud\prjother\tmp\1\c85_How does the STP election process work.md  


__|__
--|--
All righty.|Хорошо.
Let's learn about the election process.|Давайте узнаем об избирательном процессе.
And let's do certain comparisons.|И сделаем некоторые сравнения.
Let's do certain comparisons.|Сделаем некоторые сравнения.
Cuz there's a little bit of confusion out there, not confusion, just,|Потому что там немного путаницы, а не путаницы, просто
people like to learn the hard way,|люди любят учиться на собственном горьком опыте,
for whatever reason, all right.|по какой-то причине, хорошо.
This is the same example as before.|Это тот же пример, что и раньше.
Same switches,|Те же переключатели,
I didn't move it around, all right.|Я не стал его двигать, хорошо.
And we said that this was the root bridge.|И мы сказали, что это корневой мост.
Now, spanning tree has its criterias,|Теперь у остовного дерева есть свои критерии,
has its criterias to elect a root bridge.|имеет свои критерии выбора корневого моста.
Now let's bring out Notepad.|Теперь выпустим Блокнот.
Let's bring out Notepad.|Выпустим Блокнот.
There it is right there.|Вот оно прямо здесь.
We'll bring it down here, perfecto.|Мы принесем это сюда, перфекто.
Okay, so STP, all in caps,|Ладно, STP, заглавными буквами,
STP election of root bridge criteria.|Выбор STP критериев корневого моста.
First thing they look for,|Первое, что они ищут,
it is the bridge ID.|это идентификатор моста.
[SOUND] Oh, man.|[ЗВУК] Ой, чувак.
Change that, got ahead of myself.|Измени это, забегаю вперед.
Priority number.|Номер приоритета.
What is the de, what is the priority number of every switch by default?|Что такое de, каков номер приоритета каждого переключателя по умолчанию?
32769.|32769.
Every switch, every Cisco switch,|Каждый коммутатор, каждый коммутатор Cisco,
put it that way,|скажем так,
has a bridge priority number of 32769.|имеет номер приоритета моста 32769.
So, spanning tree takes a look at that,|Итак, остовное дерево смотрит на это,
says, well, wait a minute.|говорит, ну погоди.
If everybody is 32769,|Если всем 32769,
then I cannot use that because we're all have the same number.|то я не могу использовать это, потому что у всех нас одинаковый номер.
It's looking for the lowest.|Он ищет самого низкого.
Bridge priority number, okay?|Номер приоритета моста, хорошо?
So, if it can't use that,|Итак, если он не может этого использовать,
what does it default to next?|что по умолчанию будет дальше?
Mac address of switch.|Mac-адрес коммутатора.
Again, lowest.|Опять самый низкий.
So obviously,|Очевидно,
this must be the lowest mac address, or this switch here has a lower mac address than this one.|это должен быть самый низкий MAC-адрес, или этот переключатель здесь имеет меньший MAC-адрес, чем этот.
So it chose that one based on the mac address of the switch.|Таким образом, он выбрал тот, основанный на MAC-адресе коммутатора.
Now, the combination of these two,|Теперь комбинация этих двух,
the priority number and the mac address is called the combo of mac,|номер приоритета и MAC-адрес называется комбинацией Mac,
or I should say, priority, and mac is called bridge id, okay?|или я должен сказать приоритет, а Mac называется идентификатором моста, хорошо?
So that's for the election of the root bridge, and let's prove that,|Итак, это для выбора корневого моста, и давайте докажем это,
let's prove that.|давайте докажем это.
Let's open up this, this one right here.|Давайте откроем это, вот это прямо здесь.
And let's maximize the screen, okay.|И давайте увеличим экран, ладно.
Enable, and we know the command now,|Включите, и теперь мы знаем команду,
show spanning-tree, correct?|показать остовное дерево, правильно?
Show spanning-tree, I tab.|Показать остовное дерево, вкладка I.
All right, now, one thing that we didn't talk about in the previous lesson, right,|Хорошо, теперь одна вещь, о которой мы не говорили на предыдущем уроке, верно,
I didn't wanna get too much into detail.|Я не хотел вдаваться в подробности.
This portion over right here,|Эта часть прямо здесь,
this portion right here,|эта часть прямо здесь,
doesn't matter what switch you're in.|не имеет значения, в каком переключателе вы находитесь.
Does not matter what switch you're in.|Неважно, в каком переключателе вы находитесь.
This portion of, that you're looking at right here that's highlighted.|Эта часть, на которую вы смотрите прямо здесь, выделена.
That has to deal with the root bridge.|Это связано с корневым мостом.
That has to deal with the root bridge.|Это связано с корневым мостом.
And this portion down here has to deal with the switch itself, all right.|И эта часть здесь должна иметь дело с самим переключателем, хорошо.
So in this case,|Итак, в этом случае
the information is going to be the same because this is the root bridge.|информация будет такой же, потому что это корневой мост.
So, the mac address, obviously,|Итак, mac-адрес, очевидно,
is going to the be the same.|будет то же самое.
And you can see that we're using a default priority number.|И вы можете видеть, что мы используем номер приоритета по умолчанию.
We're using a default priority number.|Мы используем номер приоритета по умолчанию.
All right, and we have seen this before in a previous lesson.|Хорошо, и мы видели это раньше на предыдущем уроке.
But again, it chose it because it has a lower mac address, that was my statement.|Но опять же, он выбрал его, потому что у него меньший MAC-адрес, это было моим утверждением.
All right, so let's see.|Хорошо, так что посмотрим.
00, well you'll see this mac address on the other switch.|00, вы увидите этот MAC-адрес на другом переключателе.
Because remember, this information will go across all switches.|Помните, что эта информация будет передаваться по всем переключателям.
So let's go to the other switch.|Итак, перейдем к другому переключателю.
Let's maximize it, enable,|Давайте увеличим его, включим,
show spanning-tree.|показать остовное дерево.
So here's the mac address of the root bridge.|Итак, вот MAC-адрес корневого моста.
And here's the mac address of this switch that we're in.|А вот MAC-адрес этого переключателя, в котором мы находимся.
Well, now you see that E is greater than D.|Что ж, теперь вы видите, что E больше D.
So this is a higher mac address.|Итак, это более высокий MAC-адрес.
So indeed, since it could not use the criteria of the priority number,|Действительно, поскольку он не мог использовать критерии номера приоритета,
because they're all the same,|потому что они все одинаковые,
it chose to go to the second option.|он выбрал второй вариант.
And say, hey, I'm going to go ahead and choose the one with the lowest mac address.|И скажите: эй, я собираюсь выбрать тот, у которого самый низкий MAC-адрес.
And that one's going to become the root bridge.|И он станет корневым мостом.
Now, they'll mention it, I'm pretty sure.|Теперь они это упомянут, я уверен.
They'll try and say who's the one with the lowest bridge ID.|Они попытаются сказать, у кого самый низкий идентификатор моста.
All right, so again,|Хорошо, так что еще раз,
they'll give you, remember,|они тебе дадут, помни,
the combination of the priority number and the mac address creates that bridge ID.|комбинация номера приоритета и MAC-адреса создает этот идентификатор моста.
So just pick the lowest one.|Так что просто выберите самый низкий.
Okay, pick the lowest one, and that will be your lowest bridge ID.|Хорошо, выберите самый низкий, и это будет ваш самый низкий идентификатор моста.
But you can see that the mac address is bigger than the other one.|Но вы можете видеть, что MAC-адрес больше, чем другой.
But what ports, okay, so now okay, so we have other criteria that we need to think of.|Но какие порты, хорошо, теперь хорошо, у нас есть другие критерии, о которых нам нужно подумать.
So, let's draw a line here.|Итак, проведем здесь черту.
STP, let's put in caps,|STP, давайте в шапки,
STP Election to block a port,|Выбор STP для блокировки порта,
how does it decide?|как это решает?
Well first it picks the switch, t-c-h,|Ну сначала он выбирает переключатель, т-ц-ч,
with the highest, can't spell,|с высшим, не умею писать,
highest mac address, right?|старший MAC-адрес, верно?
We just saw that.|Мы только что это видели.
The second criteria, it says okay,|Второй критерий: хорошо,
which port do I block?|какой порт я заблокирую?
First thing it looked for is okay, let's look at bandwidth.|Первое, что он искал, это хорошо, давайте посмотрим на пропускную способность.
They're, they're all have the same bandwidth.|Они все имеют одинаковую пропускную способность.
These is fast eth, these are fast ethernet ports, so it's gonna be, can't use it.|Это быстрый eth, это быстрые порты Ethernet, так что он будет, не могу его использовать.
There's no tie breaker there,|Там нет разрешения на ничью,
same bandwidth.|та же пропускная способность.
So it would choose the slowest bandwidth to block.|Таким образом, для блокировки будет выбрана самая низкая пропускная способность.
So since it couldn't use bandwidth,|Так как он не мог использовать пропускную способность,
it will choose the highest port number to block.|он выберет самый высокий номер порта для блокировки.
Why the highest port number?|Почему самый высокий номер порта?
Higher mac address,|Высший MAC-адрес,
cuz that port number has a higher mac address than the lower port number.|Потому что этот номер порта имеет более высокий MAC-адрес, чем меньший номер порта.
Let's prove that.|Докажем это.
So, let's come back here.|Итак, вернемся сюда.
This is a switch with a higher mac address, so it chose to block a port.|Это коммутатор с более высоким MAC-адресом, поэтому он решил заблокировать порт.
As you can see, it blocked the highest port number, but let's take a look.|Как видите, он заблокировал самый высокий номер порта, но давайте посмотрим.
And let's maximize it.|И давайте максимизировать это.
Let's take a look at the ports.|Посмотрим на порты.
Show.|Шоу.
Okay, come on now.|Хорошо, давай.
[SOUND] Show interface F zero slash one.|[ЗВУК] Показать интерфейс F с нулевой косой чертой.
All right.|Отлично.
Here's the MAC address,|Вот MAC-адрес,
of port 1, okay.|порта 1, хорошо.
So let's look at the MAC address of port 2.|Итак, давайте посмотрим на MAC-адрес порта 2.
Port 2, okay, it looks similar, except,|Порт 2, хорошо, он похож, за исключением того,
except the last portion of the Mac address is 7202.|за исключением последней части Mac-адреса 7202.
Where the other one is 7201.|Где другой - 7201.
So this one is 7201, and the one for the others the other port,|Итак, это 7201, а одно для остальных - другой порт,
port 2, is 7202.|порт 2 - 7202.
So it has a higher MAC address and that's why I chose to block that port.|Таким образом, у него более высокий MAC-адрес, и поэтому я решил заблокировать этот порт.
So so let's, let's talk about this again.|Итак, давайте поговорим об этом еще раз.
We have two switches that are connected to each other.|У нас есть два переключателя, которые соединены друг с другом.
Since we wanna STP is on by default.|Поскольку мы хотим, чтобы протокол STP был включен по умолчанию.
The job of STP, as we said earlier,|Работа STP, как мы уже говорили ранее,
or and in a previous lesson,|или и на предыдущем уроке,
that it's purpose is prevent switching loops.|что его цель - предотвратить переключение петель.
The way that it does that,|То, как он это делает,
is by blocking a port.|заключается в блокировке порта.
Now how does this election take place?|Как проходят эти выборы?
First, it must elect a route bridge, and it elects the route bridge by choosing the, the switch with the lowest bridge priority number.|Во-первых, он должен выбрать маршрутный мост, и он выбирает маршрутный мост, выбирая коммутатор с наименьшим номером приоритета моста.
But since they're all the same, there 32-769 it has to go to a second criteria which is the lowest MAC address,|Но поскольку они все одинаковы, там 32-769 он должен перейти ко второму критерию, который является наименьшим MAC-адресом,
so this switch over here,|так что этот переключатель здесь,
since it had the lowest mac address, this became the root bridge therefore these ports became designated forwarding ports,|поскольку у него был наименьший MAC-адрес, он стал корневым мостом, поэтому эти порты стали назначенными портами пересылки,
okay, so, the only other switch here.|ладно, здесь есть еще один переключатель.
This must have had a higher MAC address and we verified that.|У него должен был быть более высокий MAC-адрес, и мы это проверили.
This had a higher MAC address,|У этого был более высокий MAC-адрес,
so it chose that.|поэтому он выбрал это.
To block a port on.|Чтобы заблокировать порт на.
So which port will it block?|Итак, какой порт он заблокирует?
Well, it needs to choose between one or the other.|Что ж, нужно выбирать между тем или другим.
The bandwidth is the same.|Пропускная способность такая же.
The cost, 19.|Стоимость, 19.
Fast ethernet.|Быстрый Ethernet.
So it can't use that.|Так что он не может этого использовать.
But, this 802, is a higher port number,|Но этот 802 - это более высокий номер порта,
that has a higher MAC address.|с более высоким MAC-адресом.
Therefore it will block that particular port right there, alright?|Следовательно, он заблокирует именно этот порт прямо здесь, хорошо?
So that's how it works.|Вот как это работает.
I mean, your certification,|Я имею в виду вашу сертификацию,
when you're asked on to pick,|когда вас просят выбрать,
you know, types of ports root bridge or what have you.|ну знаете, типы портов корневого моста или что там у вас.
The first thing you need to identify,|Первое, что вам нужно определить,
is who is the route bridge, and work your way from there,|Кто является путевым мостом, и проложите свой путь оттуда,
work your way from there.|работайте оттуда.
Now, I did say this,|Я сказал это,
then I want to cause any confusion.|тогда я хочу вызвать какое-то недоумение.
I said every port, the face is the root bridge must be a report.|Я сказал, что каждый порт, лицо - это корневой мост, должен быть отчет.
So, you must be thinking, well Laz,|Итак, вы, должно быть, думаете, хорошо, Лаз,
this isn't a root port, it's a block port?|это не корневой порт, это блочный порт?
Well, it has not choice,|Что ж, у него нет выбора,
it's gotta block it somewhere, right?|это нужно где-то заблокировать, верно?
So, it had to block this one, if not,|Итак, он должен был заблокировать этот, если нет,
you'll have a continuous loop and your network will go down.|у вас будет непрерывный цикл, и ваша сеть выйдет из строя.
If not,|Если не,
you're gonna do a test in your test lab.|ты собираешься сделать тест в своей лаборатории.
Not in your real life lab,|Не в твоей реальной лаборатории,
in your test lab.|в вашей тестовой лаборатории.
You take a straight through cable.|Вы берете прямой кабель.
You plug it into port 1 and port 2,|Вы подключаете его к порту 1 и порту 2,
whatever ports, in the same switch.|любые порты в том же коммутаторе.
And you're gonna create that loop.|И вы создадите этот цикл.
And you're gonna see how you're going to bring, boom, that's gonna go down ASAP.|И ты увидишь, как ты собираешься принести, бум, это будет как можно скорее.
All right, trust me on that one.|Хорошо, поверьте мне в этом.
Okay, all right, so now lets change the bandwidth,|Хорошо, хорошо, теперь давайте изменим пропускную способность,
lets take out that port right there that F02 port that link,|давайте вытащим этот порт прямо здесь, что порт F02, что ссылка,
lets take that link out, and lets put a gigabit link and see what happens.|Давайте уберем эту ссылку, давайте разместим гигабитную ссылку и посмотрим, что произойдет.
All right.|Отлично.
And remember our spanning tree only really comes alive,|И помните, что наше остовное дерево только оживает,
it only really comes alive and does what is has to do when it finds redundant links.|он действительно оживает и делает то, что должен делать, только когда находит избыточные ссылки.
So here there is no redundant link so really it doesn't matter.|Так что здесь нет избыточной ссылки, так что на самом деле это не имеет значения.
What did I say?|Что я говорил?
Oh, yeah, gigabit port, all right?|Ах да, гигабитный порт, хорошо?
So I'm actually choosing a port,|Так что я действительно выбираю порт,
I choose gigabit, I'll use the last port.|Выбираю гигабит, последний порт буду использовать.
Gigabit is one, two,|Гигабит - это один, два,
to gigabit one, two, okay?|на гигабит один, два, ладно?
And let's see which port it blocks now.|И посмотрим, какой порт он сейчас блокирует.
Spanning tree is doing it's magic,|Связывающее дерево творит чудеса,
it's working.|это работает.
It's, it's stinking oh,|Это вонючий ох,
my god, what's going on now?|Боже мой, что сейчас происходит?
Something changed.|Что-то изменилось.
I need to recalculate the costs have become difference.|Мне нужно пересчитать затраты, разница стала.
Now gigabit is 4.|Сейчас гигабит 4.
Where the ethernet is 19.|Где ethernet 19.
19.|19.
All right.|Отлично.
So, let's see what's gonna happen.|Итак, посмотрим, что произойдет.
It should happen any day now.|Это должно произойти со дня на день.
Really it will.|Действительно будет.
That's why we have rapid spanning trees so we can go faster.|Вот почему у нас есть деревья быстрого охвата, чтобы мы могли двигаться быстрее.
[LAUGH] Here we go.|[СМЕХ] Вот и мы.
As you can see now that the higher port is not blocked.|Теперь вы можете видеть, что порт более высокого уровня не заблокирован.
The higher port is going to be designated forwarding but the lower port is the one that's blocked.|Более высокий порт будет назначен для пересылки, но нижний порт будет заблокирован.
It makes sense, it makes sense,|Это имеет смысл, это имеет смысл,
let's take a look at it.|давайте посмотрим на это.
Why in the world would you wanna block a gigabit port?|Зачем вам блокировать гигабитный порт?
Show spanning tree.|Показать остовное дерево.
There it is.|Вот оно.
Right?|Правильно?
Your F zero, one, alternating block,|Ваш F ноль, один, чередующийся блок,
right?|право?
19 cost.|19 стоимость.
Gigabit part, route,|Гигабитная часть, маршрут,
forwarding, cause four.|пересылка, причина четыре.
So, that's why.|Итак, вот почему.
That's how that works.|Вот как это работает.
Based on bandwidth.|В зависимости от пропускной способности.
It's based on bandwidth when looking to see what block, or what portion, what block.|Он основан на пропускной способности, когда нужно посмотреть, какой блок, или какая часть, какой блок.
So, use bandwidth,|Итак, используйте пропускную способность,
it looks at the bandwidth, all right?|он смотрит на пропускную способность, ладно?
Some will say no, no, no, it doesn't.|Некоторые скажут: нет, нет, нет.
Yes, yes, yes, it does.|Да, да, да, это так.
All right, so it's gonna have it's calculation that you guys can go ahead and calculate across,|Хорошо, так что у него будет расчет, который вы, ребята, можете продолжить и вычислить,
19 plus 19 plus 4 plus 28 and all this stuff, you don't need to do all that.|19 плюс 19 плюс 4 плюс 28 и все такое, вам не нужно все это делать.
All right.|Отлично.
And those of you that say,|И те из вас, кто говорит:
well how about 3 switches, how about 4 switches, how about 10 switches,|ну как насчет 3 переключателей, как насчет 4 переключателей, как насчет 10 переключателей,
how, well, you, if you want to calculate that out, you go right ahead.|как, ну, если вы хотите это вычислить, идите вперед.
Normally you don't even mess around with that.|Обычно с этим даже не связываешься.
All right, you, our switches are in place.|Хорошо, вы, наши переключатели на месте.
Heck, people have a hard time creating VLAN, much less tweaking spanning tree.|Черт возьми, людям сложно создать VLAN, не говоря уже о настройке связующего дерева.
Okay.|Ладно.
But, you really don't tweak the spanning tree, you let it decide whose gonna be the root bridge unless you have a specific|Но вы действительно не настраиваете связующее дерево, вы позволяете ему решать, чей будет корневой мост, если у вас нет определенного
beefy switch that you want that one to be the main switch.|мощный выключатель, который вы хотите, чтобы он был главным выключателем.
And then things will propagate from there.|И оттуда все будет распространяться.
All right, but so you can see the election process.|Хорошо, но чтобы вы могли видеть процесс выборов.
Again you're taking a certification exam,|Вы снова сдаете сертификационный экзамен,
keep that in mind, alright?|имейте это в виду, хорошо?
So again, the election process, this is what happens, you see that now the higher port number actually didn't get blocked,|Итак, снова процесс выборов, вот что происходит, вы видите, что теперь более высокий номер порта фактически не был заблокирован,
because It had a faster bandwidth.|потому что у него была более высокая пропускная способность.
So if use that particular criteria,|Итак, если использовать этот конкретный критерий,
that we have written down here, all right,|что мы здесь записали, хорошо,
the second one, that's gonna block the slowest bandwidth to block, and it did, it blocked the fast Ethernet,|второй, который будет блокировать самую медленную полосу пропускания для блокировки, и он заблокировал быстрый Ethernet,
not the gigabit.|не гигабит.
So that is the election process of, of.|Итак, это процесс выборов оф.
[INAUDIBLE] But,|[НЕДОСТАТОЧНО] Но,
let's take it a step further.|давайте сделаем еще один шаг.
All right, because you are gonna be working when we do our, our labs.|Хорошо, потому что ты будешь работать, когда мы будем делать наши, наши лаборатории.
We are gonna be using three switches.|Мы собираемся использовать три переключателя.
So, I'm gonna,|Итак, я собираюсь,
I'm gonna get our switch out here.|Я достану наш выключатель.
I'm gonna put a switch out here.|Я поставлю здесь выключатель.
And I'm gonna put a switch out here.|И я поставлю здесь переключатель.
And again, I'm gonna cheat.|И снова я обманываю.
I'm just gonna let it plug in wherever.|Я просто позволю ему подключиться где угодно.
Portal once,|Портал однажды,
doesn't really matter to me at this point.|на данный момент для меня не имеет значения.
I'm just trying to show you, how this election process takes place for three switches, okay.|Я просто пытаюсь показать вам, как проходит процесс выборов для трех переключателей, хорошо.
You can say oh, we only did two switches.|Вы можете сказать, что мы сделали только два переключателя.
Here's three switches, all right.|Вот три переключателя, хорошо.
Lets put it over here.|Давай положим это сюда.
So spanning tree takes anywhere up to 90 seconds.|Таким образом, связующее дерево занимает до 90 секунд.
For it to do as I do.|Чтобы делать то же, что и я.
Like I said, there's different versions of a spanning tree, right?|Как я уже сказал, существуют разные версии остовного дерева, верно?
This is the original version of 8021D,|Это оригинальная версия 8021D,
you do have your rapid spanning tree.|у вас есть быстрое остовное дерево.
All right.|Отлично.
And there's also rapid spanning-tree with PVST and there's like four different types of spanning-tree.|Также есть быстрое связующее дерево с PVST и четыре разных типа связующего дерева.
Basically, all that does is how many spanning-tree per VLANs you can have or how quickly it can converge?|По сути, все, что для этого нужно, - это сколько связующего дерева на каждую VLAN вы можете иметь или как быстро оно может сойтись?
Okay?|Ладно?
So here, looking at this,|Итак, вот, глядя на это,
we know right off the bat that that's blocked.|мы сразу знаем, что это заблокировано.
All right?|Отлично?
Just like we know that that's blocked.|Также как мы знаем, что это заблокировано.
So, obviously, this is the one with the highest MAC address.|Итак, очевидно, что это тот, у которого самый высокий MAC-адрес.
I didn't change priority numbers,|Я не менял номера приоритета,
I didn't do anything.|Я ничего не делал.
So this is the one with the highest MAC address, this is the box.|Итак, это тот, у которого наивысший MAC-адрес, это коробка.
So this is definitely not the root bridge.|Так что это точно не корневой мост.
Okay.|Ладно.
And I said, [COUGH] excuse me,|И я сказал: [КАШЕ] извините,
I said that every port that faces the root bridge must be a root port.|Я сказал, что каждый порт, обращенный к корневому мосту, должен быть корневым портом.
Well, this is a blocked port.|Ну это заблокированный порт.
So if it's facing that switch,|Итак, если он стоит перед переключателем,
it's, this is not the root bridge.|это не корневой мост.
So this guy over here is the root bridge.|Итак, вот этот парень - корневой мост.
Let's see if that's true.|Посмотрим, правда ли это.
Let's open this guy up right here,|Давайте откроем этого парня прямо здесь,
switch number three.|переключатель номер три.
Let's maximize it.|Давайте максимизировать это.
And the command is very good,|И команда очень хорошая,
show spanning-tree.|показать остовное дерево.
And lo and behold.|И о чудо.
This is the root bridge, right?|Это корневой мост, верно?
So there's the MAC address, 0001.|Итак, есть MAC-адрес 0001.
Okay.|Ладно.
And all those ports are desg forwarding,|И все эти порты предназначены для переадресации,
we've got the same bandwidth as 19.|у нас такая же пропускная способность, как у 19.
This is something you really need,|Это то, что тебе действительно нужно,
a screen you need to pay attention to.|экран, на который нужно обратить внимание.
You need to know that this portion is for the root bridge, this portion is for the switch.|Вы должны знать, что эта часть предназначена для корневого моста, а эта часть - для коммутатора.
All right?|Отлично?
Take a look at the ports,|Взгляните на порты,
if they are designated or root ports or block ports.|если они назначены, либо корневые порты, либо порты блокировки.
You need to take a look at that.|Вам нужно взглянуть на это.
That's gonna be very important for your switching simulation.|Это будет очень важно для симуляции переключения.
Show spanning-tree.|Покажите остовное дерево.
All right.|Отлично.
So we see the other MAC address there.|Итак, мы видим там другой MAC-адрес.
Perfect.|Отлично.
We know that this is the root bridge.|Мы знаем, что это корневой мост.
We verified that, because it says it.|Мы это проверили, потому что там сказано.
This is a root bridge or just take a look at all the ports.|Это корневой мост или просто посмотрите на все порты.
They're designated forwarding ports.|Они назначены портами пересылки.
Designated forwarding ports,|Обозначенные порты пересылки,
so that is a root bridge.|так что это корневой мост.
All right.|Отлично.
Well, let's take a look at this,|Что ж, давайте посмотрим на это,
this switch over here.|этот переключатель здесь.
All right So, spanning-tree.|Хорошо Итак, остовное дерево.
Okay.|Ладно.
Now this is [COUGH] whoa,|Теперь это [КАШЕ] эй,
I'm growing up, I'm changing my voice.|Я взрослею, меняю голос.
All right.|Отлично.
This is the MAC address of the root bridge.|Это MAC-адрес корневого моста.
Okay.|Ладно.
This is a higher MAC address than this one.|Это более высокий MAC-адрес, чем этот.
Okay.|Ладно.
000, 0006 versus 0001.|000, 0006 против 0001.
So, okay.|Так хорошо.
That's why he did not become the root bridge, because see that they're using the same priority numbers.|Вот почему он не стал корневым мостом, потому что следите за тем, чтобы они использовали одинаковые номера приоритета.
So, it didn't choose that as a criteria and look at his ports,|Итак, он не выбирал это в качестве критерия и не смотрел на его порты,
one's designated 40, one is root.|один обозначен 40, один root.
Root, important root.|Корень, важен корень.
This is the one facing the root bridge.|Это тот, который обращен к корневому мосту.
What port is facing the root bridge?|Какой порт обращен к корневому мосту?
Port add 0/2.|Добавление порта 0/2.
Sounds like a test question to me.|Для меня это похоже на тестовый вопрос.
All right.|Отлично.
So show, show spanning-tree.|Так покажи, покажи остовное дерево.
You see that this port is a root port and that that root port is facing add 0/2.|Вы видите, что этот порт является корневым и что этот корневой порт стоит перед добавлением 0/2.
Hey, I may want to do show CDP neighbor.|Эй, может я хочу показать соседу по CDP.
Show CDP neighbor detail.|Показать детали соседа CDP.
Take a look at that name.|Взгляните на это имя.
Switching simulation, okay?|Имитация переключения, хорошо?
Anyway, all right.|Во всяком случае, хорошо.
So this has a high MAC address, 0006.|Итак, у него высокий MAC-адрес 0006.
So keep this in mind right here.|Так что имейте это в виду прямо здесь.
Keep this in mind.|Имейте это в виду.
Let's take a look at the switch that actually got blocked.|Давайте посмотрим на переключатель, который действительно заблокирован.
Enable, show spanning-tree and there's the root bridge.|Включите, покажите связующее дерево и корневой мост.
Oh, okay.|Ох, ну ладно.
Look at that, 005.|Посмотри на это, 005.
The other one was at least 0006,|Другой был не менее 0006,
this is 005.|это 005.
Definitely, this has the highest MAC address.|Определенно, у него самый высокий MAC-адрес.
Port one is the root port,|Первый порт - это корневой порт,
which is the root bridge.|который является корневым мостом.
The other one is just the one that decided, highest port to pick to block.|Другой - как раз тот, который решил, самый высокий порт, который нужно выбрать для блокировки.
So, information will now be forwarded out that port.|Таким образом, теперь информация будет отправляться через этот порт.
So there you go.|Итак, поехали.
Spanning-tree does it all on its own.|Spanning-tree делает все самостоятельно.
But in other lessons to come,|Но в других уроках впереди,
I will show you how to manipulate that.|Я покажу вам, как этим управлять.
But so you can get an understanding of how spanning-tree works and what command and what is it that you're looking at.|Но чтобы вы могли понять, как работает связующее дерево, какую команду и на что вы смотрите.
All right?|Отлично?
Because we will learn to manipulate spanning-tree,|Поскольку мы научимся манипулировать остовным деревом,
we will even learn to turn off spanning tree.|мы даже научимся отключать остовное дерево.
Okay?|Ладно?
But that's in lessons to come, so understand the election process.|Но это будут уроки впереди, так что разберитесь в избирательном процессе.
Because I know that sometimes it becomes difficult,|Потому что я знаю, что иногда бывает трудно,
because a lot of people like to use and Cisco does do this.|потому что многим людям нравится пользоваться, и Cisco это делает.
This they use the lowest cost path.|Для этого они используют самый дешевый путь.
Write that down, lowest cost path.|Запишите этот путь с наименьшей стоимостью.
If you ever run into a question in an examination at your school.|Если вы когда-нибудь столкнетесь с вопросом на экзамене в вашей школе.
Lowest cost path to the root bridge, okay?|Самый дешевый путь к корневому мосту, хорошо?
But again, we see now the trick, right?|Но опять же, теперь мы видим фокус, верно?
I find the root bridge,|Я нахожу корневой мост,
these are my designated forwarding.|это моя назначенная переадресация.
These are my root port, my block port and another designated forwarding port.|Это мой корневой порт, мой блочный порт и еще один назначенный порт пересылки.
Okay?|Ладно?
That's all there is to it.|Это все, что нужно сделать.
All right?|Отлично?
But you gotta practice that.|Но тебе нужно это практиковать.
You gotta practice.|Тебе нужно практиковаться.
You gotta look at this video over and over and over and over again.|Вы должны смотреть это видео снова и снова, снова и снова.
So you can get that spanning-tree and do the practice.|Так что вы можете получить это остовное дерево и практиковаться.
Hook, don't go crazy hooking up ten switches and try and figure out what they're doing.|Крюк, не сходи с ума, подключив десять переключателей и попытайся выяснить, что они делают.
The maximum you should go for is four switches.|Максимум, на что вы должны пойти, - это четыре переключателя.
Max.|Максимум.
Okay?|Ладно?
It is four switches.|Это четыре переключателя.
All I meant, get the idea of the criterias that spanning-tree is using to block ports and the whole purpose of it is just to avoid switching loops.|Все, что я имел в виду, - получить представление о критериях, которые Spanning-tree использует для блокировки портов, и вся его цель - просто избежать петель переключения.
And in a real world scenario, doubtful that you'll be tweaking spanning-tree.|И в реальном сценарии сомнительно, что вы будете настраивать связующее дерево.
All right?|Отлично?
But for the test you need to know these ports and they're,|Но для теста вам нужно знать эти порты, и они,
you know, how they become these ports.|вы знаете, как они становятся этими портами.
Okay?|Ладно?
All right.|Отлично.
[SOUND] I'll see you guys in the next session or lesson.|[ЗВУК] Увидимся на следующем занятии или уроке.