D:\mailCloud\prjother\tmp\1\c89_Commands and Configurations of the VTP protocol.md  


__|__
--|--
All right, in this lesson,|Хорошо, в этом уроке
[SOUND] we're gonna configure VTP, yes.|[ЗВУК] мы собираемся настроить VTP, да.
But we're gonna encompass a couple of things that we've done already.|Но мы собираемся охватить пару вещей, которые уже сделали.
We're gonna create some VLANs,|Мы собираемся создать несколько VLAN,
we're gonna tweak spanning tree.|мы собираемся настроить остовное дерево.
And then we'll get into the VTP, and then we're actually gonna trunk some ports as well.|А затем мы перейдем к VTP, а затем на самом деле собираемся соединить некоторые порты.
So there's a couple of things that we're gonna do here.|Итак, есть пара вещей, которые мы здесь сделаем.
All right, so it's gonna be a nice little lab,|Хорошо, так что это будет хорошая маленькая лаборатория,
that encompasses some of the things we've already learned to do.|это включает в себя некоторые вещи, которым мы уже научились.
But it's not the big,|Но это не большое,
big lab that we're going to do towards the end of the switching course.|большая лаборатория, которую мы собираемся проделать ближе к концу курса переключения.
It just so happens, cuz when I pulled this out here, it just so happens that that is the route bridge.|Так уж получилось, потому что, когда я вытащил это здесь, так получилось, что это маршрутный мост.
As you can see,|Как вы видете,
this is the block port right here.|это блок-порт прямо здесь.
Okay?|Ладно?
And decided to disappear there, Ctrl+Z,|И решил там пропасть, Ctrl + Z,
no Ctrl+Z, Ctrl+Z, Ctrl+Z, Ctrl+Z.|нет Ctrl + Z, Ctrl + Z, Ctrl + Z, Ctrl + Z.
All right, let me, oh, there it is.|Хорошо, позволь мне, о, вот оно.
How'd that happen?|Как это случилось?
Port 21, I believe.|Кажется, порт 21.
Okay, it just so happens that hey,|Ладно, так получилось, что эй,
that's the route bridge, but we're gonna make it the route bridge anyway.|это маршрутный мост, но мы все равно сделаем его маршрутным мостом.
We're gonna tweak that.|Мы собираемся это исправить.
And you'll see as we go along what we're going to do.|И по мере продвижения вы увидите, что мы собираемся делать.
Let me move it this way,|Позвольте мне сдвинуть его сюда,
so you can see it.|так что вы можете это увидеть.
Now, I have a router here because this is the ones that we're gonna use, this same lab is the one that we're gonna use for, to practice our inter-VLAN routing.|Теперь у меня есть маршрутизатор, потому что это тот, который мы собираемся использовать, эта же лаборатория - та, которую мы собираемся использовать, чтобы практиковать нашу маршрутизацию между VLAN.
But this is gonna very basic.|Но это будет очень просто.
Once we get to the bigger lab,|Как только мы доберемся до большой лаборатории,
you'll see what I'm talking about.|вы увидите, о чем я говорю.
All right, so let's go to the top switch,|Хорошо, давайте перейдем к верхнему переключателю,
let's make that switch the route bridge.|давайте сделаем это переключить маршрутный мост.
Well, first let's name it.|Ну сначала назовем это.
All right.|Отлично.
So let's maximize the screen.|Итак, давайте развернем экран.
Enable, config, conf t, host name,|Enable, config, conf t, имя хоста,
let's just call it CORE1.|назовем его просто CORE1.
All right, so I'm gonna manipulate spanning tree.|Хорошо, я собираюсь манипулировать остовным деревом.
As you can see,|Как вы видете,
I have VLAN 10 and VLAN 20.|У меня VLAN 10 и VLAN 20.
It was there before, now it's not.|Это было раньше, а теперь нет.
Okay, so let me go ahead and just let me copy this real quick.|Хорошо, позвольте мне продолжить и просто позвольте мне скопировать это очень быстро.
That's when I did that whole, magic finger trick that everything disappeared.|Вот когда я проделал весь фокус с волшебным пальцем, и все исчезло.
Okay.|Ладно.
Not a problem.|Не проблема.
20.|20.
20.|20.
All right, so we have VLAN 10 and VLAN 20.|Хорошо, у нас есть VLAN 10 и VLAN 20.
So when we do the span tree,|Итак, когда мы делаем остовное дерево,
we gotta include that,|мы должны включить это,
we gotta include VLANs 1, 10, and 20.|мы должны включить VLAN 1, 10 и 20.
If you don't do that, you run in the arr,|Если вы этого не сделаете, вы бежите в обр.
the issue that hey all your ports might turn green and you're gonna have a switching loop, remember that.|проблема в том, что все ваши порты могут стать зелеными, и у вас будет петля переключения, помните об этом.
So, we're gonna go here,|Итак, мы пойдем сюда,
and maximize again.|и снова максимизировать.
Let's do the spanning tree that we did before.|Давайте сделаем остовное дерево, которое мы делали раньше.
So we do it, spanning tree.|Итак, мы делаем это, покрывая дерево.
VLAN 1, comma, 10,|VLAN 1, запятая, 10,
comma, 20, priority 0.|запятая, 20, приоритет 0.
Now that's not gonna do anything.|Теперь это ничего не даст.
This has always been the route bridge,|Это всегда был путевой мост,
regardless.|несмотря на.
But we're making sure that this is the route bridge.|Но мы убеждаемся, что это путевой мост.
All right.|Отлично.
So now what I'm gonna do, is I'm going to create the VLAN's on the core switch.|Итак, что я собираюсь сделать, это создать VLAN на основном коммутаторе.
I wanna create VLAN's on the core switch.|Я хочу создать VLAN на основном коммутаторе.
Because what I want to happen,|Потому что то, что я хочу,
is for those VLANs to propagate down to all the other switches to make life a whole lot easier.|чтобы эти VLAN распространялись на все другие коммутаторы, чтобы сделать жизнь намного проще.
So let's do VLAN 10 and we'll use the same name, faculty.|Итак, давайте сделаем VLAN 10, и мы будем использовать то же имя, факультет.
VLAN 20, name student.|VLAN 20, имя ученика.
But we're not going to assign them.|Но мы не собираемся их назначать.
We're just creating them on there.|Мы просто создаем их там.
So let's verify.|Итак, давайте проверим.
Let's exit, exit.|Выходи, выходи.
Let's do a copy run start.|Давайте начнем копирование.
Look at me doing the proper commands.|Посмотри, как я делаю правильные команды.
Look at that.|Посмотри на это.
All right, we're gonna do show VLAN.|Хорошо, мы покажем VLAN.
All right, and we have our faculty and we have our students.|Хорошо, у нас есть преподаватели и студенты.
Let's take a look at our spanning tree,|Давайте посмотрим на наше остовное дерево,
show spanning tree.|показать остовное дерево.
And there is our spanning tree right there.|И прямо там есть наше остовное дерево.
Priority one, all right,|Приоритет один, хорошо,
because we put zero,|потому что мы ставим ноль,
remember, this is the route bridge,|помните, это путевой мост,
all right, all designated ports.|хорошо, все обозначенные порты.
Now, what we're gonna do is,|Теперь, что мы собираемся сделать,
we're gonna play around with the VTP.|мы поиграемся с VTP.
So we're gonna make,|Итак, мы собираемся сделать,
this is already VTP server.|это уже VTP-сервер.
It wouldn't allow me to create these VLANs if it wouldn't have been.|Это не позволило бы мне создать эти VLAN, если бы этого не было.
So I'm going to give it a VTP domain name of CISCO.|Я собираюсь дать ему доменное имя VTP CISCO.
So let's go to global configuration,|Итак, перейдем к глобальной настройке,
and I'll go VTP domain, CISCO.|и я пойду в домен VTP, CISCO.
So it's telling you, hey, we changed the domain name from nothing to CISCO.|Итак, это говорит вам, эй, мы изменили доменное имя с ничего на CISCO.
How do we verify that?|Как мы можем это проверить?
Well, we exit once.|Что ж, выходим один раз.
We do show.|Мы показываем.
Okay?|Ладно?
Show VTP stat.|Показать статистику VTP.
All right.|Отлично.
And we see here, that the domain now is CISCO.|И здесь мы видим, что домен теперь CISCO.
There's two, there,|Там двое, там
our default VLANs were 5, now they're 7.|у нас по умолчанию было 5 VLAN, теперь их 7.
All right, so we've manipulated things on there.|Ладно, мы там кое-чем манипулировали.
So we created VLANs.|Итак, мы создали сети VLAN.
Well, we manipulated spanning tree.|Ну, мы манипулировали остовным деревом.
We created VLANs and named them.|Мы создали сети VLAN и дали им имена.
Now we change the VTP, name to CISCO.|Теперь мы меняем имя VTP на CISCO.
Now, what we need to do is trunk ports.|Теперь нам нужно сделать магистральные порты.
And this is the reason why I picked these specific ports, 22, 23, and 24.|По этой причине я выбрал именно эти порты: 22, 23 и 24.
So I can use a range command,|Итак, я могу использовать команду диапазона,
make it very simple.|сделать это очень просто.
So those three ports, I need to trunk.|Итак, эти три порта мне нужно соединить.
Because remember, VLANs two through 1,001 can only go through trunk ports.|Помните, что сети VLAN со второго по 1001 могут проходить только через магистральные порты.
And VTP is the one that's looking or sending information on those trunked ports.|И VTP - это тот, который ищет или отправляет информацию по этим транкинговым портам.
So you must trunk the ports going from switch to switch or switch to router.|Таким образом, вы должны соединить порты, идущие от коммутатора к коммутатору или от коммутатора к маршрутизатору.
All right, so let's go ahead and trunk those ports, using the range command.|Хорошо, давайте продолжим и соединим эти порты с помощью команды range.
So we're gonna go to config t int range, F0/22-24.|Итак, мы перейдем к настройке диапазона int, F0 / 22-24.
And then we go switch port mode trunk.|И затем мы переходим к переключению режима порта в транк.
Right and we do a Ctrl+Z,|Вправо и делаем Ctrl + Z,
gonna do a WR and look at show int trunk,|собираюсь сделать WR и посмотреть на show int trunk,
you can only see 22 and 23.|вы можете видеть только 22 и 23.
You don't see 24 because 24|Вы не видите 24, потому что 24
is plugged into the router's interface which is administratively down.|подключен к интерфейсу маршрутизатора, который не работает административно.
That's why you see the red dots.|Вот почему вы видите красные точки.
So you're not gonna see that until that turns on on the router, but you still need to trunk 24 anyway.|Так что вы не увидите этого, пока он не включится на маршрутизаторе, но вам все равно потребуется транк 24.
So once you match the encapsulation on the router, everything will work just fine.|Поэтому, как только вы установите соответствие инкапсуляции на маршрутизаторе, все будет работать нормально.
So remember you gotta trunk those ports.|Так что помните, что вам нужно соединить эти порты.
Cool, so we have our VLANs.|Круто, у нас есть свои VLAN.
All right.|Отлично.
We did the spanning tree.|Мы сделали остовное дерево.
We did the VTP.|Мы сделали VTP.
Now we're gonna come down here.|Теперь мы спустимся сюда.
Now I'll change this from PC0,|Сейчас поменяю с PC0,
I'm gonna name this faculty over here, so we know this is the faculty switch.|Я назову этот факультет вот здесь, чтобы мы знали, что это переключение факультетов.
And this will be the student.|И это будет студент.
Or the student side right.|Или со стороны студента справа.
The student's side, all right.|Со студенческой стороны, все в порядке.
So let's go to the switch, let's name it.|Итак, перейдем к переключателю, назовем его.
Config t, host name, faculty.|Конфигурация, имя хоста, факультет.
Now what I wanna do here, remember I said one server operating mode for only one server, the rest clients.|Теперь, что я хочу здесь сделать, помните, что я сказал один режим работы сервера только для одного сервера, остальных клиентов.
So I wanna go VTP, mode client.|Итак, я хочу перейти на VTP в режиме клиента.
Now what I wanna verify, hey did those switch, did those VLANs come down?|Теперь, что я хочу проверить, эй, эти переключатели, эти VLAN вышли из строя?
Do show VLAN.|Показать VLAN.
Awesome, they did.|Потрясающе, они сделали.
They came down.|Они спустились.
I trunked the ports,|Я подключил порты,
we're in the same VTP domain, right,|мы находимся в одном домене VTP, верно,
because that came down right along with it.|потому что это произошло вместе с ним.
Do show VTP stat.|Показывать статистику VTP.
There it is, CISCO.|Вот она, CISCO.
Okay, so we do that, so hey,|Хорошо, так что мы делаем это, эй,
it cuts our work in half.|это вдвое сокращает нашу работу.
All we really need to do is just assign the VLANs, assign the VLANs.|Все, что нам действительно нужно сделать, это просто назначить VLAN, назначить VLAN.
So let's go ahead and do that.|Так что давайте продолжим и сделаем это.
So we name the switch,|Итак, мы называем переключатель,
we change it to client, mode.|меняем его на клиентский, режим.
Client mode.|Клиентский режим.
Which means we can create them, but we don't need to cuz they came down.|Это означает, что мы можем их создавать, но нам не нужно, потому что они спустились.
All right, so this is the faculty so it's in VLAN 10.|Хорошо, это факультет, поэтому он находится в VLAN 10.
So we're gonna go to ports,|Итак, мы пойдем в порты,
we'll do a range.|сделаем ряд.
We'll do int F0/1-15.|Мы сделаем int F0 / 1-15.
Oops, I forgot the range command.|Ой, я забыл команду дальности.
Int range F0/1-15 and then we're gonna do,|Интервал F0 / 1-15 и тогда мы будем делать,
remember has to be access, access ports,|помните, что должен быть доступ, порты доступа,
cuz they're by default dynamic.|потому что они по умолчанию динамические.
So we'll switch port TCH, mode access.|Так что переключим порт ТСН, режим доступа.
Now you're gonna assign the VLAN.|Теперь вам нужно назначить VLAN.
Switch port, TCH.|Порт коммутатора, ТКП.
Bridge port, access,|Порт моста, доступ,
VLAN, 10.|VLAN, 10.
All righty.|Хорошо.
And while we're here,|И пока мы здесь,
since we know we're only gonna plug in end devices, why not turn off spanning tree?|Поскольку мы знаем, что будем подключать только конечные устройства, почему бы не отключить связующее дерево?
Spanning tree port fast.|Быстрый порт связующего дерева.
And, we guard against it.|И мы остерегаемся от этого.
Spanning tree, BPDU guard, enable.|Связующее дерево, защита BPDU, включить.
So you can see, you combine a whole bunch of things together.|Как видите, вы объединяете множество вещей вместе.
So we're gonna do a Ctrl+Z, WR.|Итак, мы сделаем Ctrl + Z, WR.
Let's take at show VLAN and there we have our faculty VLAN that is active on ports one through fifteen.|Давайте возьмем на показе VLAN, и там у нас есть наша факультетская VLAN, которая активна на портах с первого по пятнадцать.
And if we we're to take a look at the show start and take a look at the interfaces,|И если мы посмотрим на начало шоу и взглянем на интерфейсы,
you see that we have portfast, bpduguard enable, all those things are on there.|вы видите, что у нас есть portfast, bpduguard enable, все это там.
Now we haven't done no IP addresses or anything like that.|Сейчас мы не делали никаких IP-адресов или чего-то подобного.
That'll be left for the big lab.|Это останется для большой лаборатории.
But, we're essentially done with this particular switch.|Но мы, по сути, закончили с этим конкретным переключателем.
Now we're gonna go to the student switch.|Теперь мы перейдем к студенческому переключателю.
And we'll do the same exact thing.|И мы сделаем то же самое.
So you see how VTP helps us?|Итак, вы видите, как VTP нам помогает?
By being in the same domain.|Находясь в одном домене.
Right, by changing the modes from server to client and receiving updates.|Правильно, изменяя режимы с сервера на клиент и получая обновления.
All these things are important because it can cut your work in half.|Все это важно, потому что это может сократить вашу работу вдвое.
Enable, config t, host name,|Включить, настроить, имя хоста,
what's this, students.|что это, студенты.
All right.|Отлично.
Now we go VTP, mode, client.|Теперь идем VTP, режим, клиент.
Let's verify that the VLANs did come down,|Давайте проверим, что VLAN действительно вышли из строя,
do show VLAN.|показывать VLAN.
And they sure do.|И они точно так и делают.
I'll do a Ctrl+Z.|Я сделаю Ctrl + Z.
So now we do the range command again.|Итак, теперь мы снова выполняем команду диапазона.
Int range, F0/1-15,|Интервал, F0 / 1-15,
just a number that I always pick.|просто число, которое я всегда выбираю.
So now we assign the VLANs, but before we gotta change it to access mode.|Итак, теперь мы назначаем сети VLAN, но прежде, чем мы должны переключить их в режим доступа.
Switch, I'm gonna tab, switch port mode,|Переключить, я собираюсь перейти, переключить режим порта,
access, switch port access, VLAN 20.|доступ, доступ к порту коммутатора, VLAN 20.
Right.|Правильно.
Now we do a spanning tree.|Теперь делаем остовное дерево.
Port fast.|Порт быстро.
And then we do the spanning tree.|А затем делаем остовное дерево.
BPDU guard enable.|Включена защита BPDU.
Done deal.|Сделка сделана.
Done deal.|Сделка сделана.
That is how cool VTP is.|Вот насколько крутой VTP.
Cuz the virtual trunking protocol.|Потому что протокол виртуального транкинга.
Show VTP stat.|Показать статистику VTP.
The virtual trunking protocol,|Протокол виртуального транкинга,
we're all in the same domain.|мы все в одном домене.
Right.|Правильно.
We're the client switches.|Мы - переключатели клиентов.
We'll be receiving updates.|Мы будем получать обновления.
If our revision number however,|Однако если номер нашей ревизии
for whatever reason,|для любой причины,
changes to a higher number, cuz you took it out and you configured something,|изменяется на большее число, потому что вы вынули его и что-то настроили,
you put it back in and now the revision number is higher than the rest.|вы вставляете его обратно, и теперь номер ревизии выше, чем у остальных.
That could wipe all your other VLANs,|Это может стереть все ваши другие VLAN,
so you gotta be careful.|так что будьте осторожны.
You gotta be careful when doing that.|При этом нужно быть осторожным.
But you see how easy that was.|Но вы видите, как это было легко.
You see how easy that was.|Вы видите, как это было легко.
We created the VLANs up here on our core switch by trunking the ports using a VTP domain name and changing the mode to client on the bottom switches,|Мы создали VLAN здесь, на нашем основном коммутаторе, путем объединения портов с использованием доменного имени VTP и изменения режима на клиентский на нижних коммутаторах,
it actually propagated everything down.|он фактически распространил все вниз.
So it cut our work in half, and then we just did our normal stuff that we would do with turning off spanning tree and then guarding against it.|Таким образом, это сократило нашу работу вдвое, а затем мы просто сделали свои обычные вещи, которые мы сделали бы, отключив остовное дерево, а затем защитившись от него.
And again this is just part of it.|И снова это только часть.
This is just the beginning.|Это только начало.
But you see that VTP is extremely important because it will watch these VLANs as it goes across and tag them correctly.|Но вы видите, что VTP чрезвычайно важен, потому что он будет отслеживать эти VLAN по мере их прохождения и правильно маркировать их.
If there's a mismatch somewhere then,|Если где-то есть несоответствие, тогда
believe me, VTP will let you know.|поверьте, VTP сообщит вам об этом.
VTP will let you know,|VTP сообщит вам,
because if I were to change,|потому что если бы я изменился,
let's say manually, I would change the VTP domain name on one of those client switches by changing it to server and changing the name, then you will have,|скажем вручную, я бы изменил доменное имя VTP на одном из этих клиентских коммутаторов, изменив его на сервер и изменив имя, тогда у вас будет,
immediately you'll see a VTP domain name mismatch.|сразу вы увидите несоответствие доменного имени VTP.
And you don't wanna do that.|И ты не хочешь этого делать.
But that's what VTP is, so again,|Но это то, что такое VTP, поэтому снова
just to show you one last time,|просто чтобы показать тебе в последний раз,
one last time, well its not really the last time, but be very familiar.|в последний раз, ну, на самом деле, не в последний раз, но будьте очень знакомы.
Know that command.|Знайте эту команду.
Show VTP status.|Показать статус VTP.
Show VTP status.|Показать статус VTP.
And again, the revision number,|И снова номер ревизии,
the operating mode, the domain name.|режим работы, доменное имя.
And then this number down here.|А потом вот этот номер.
Who was the last switch that modified you?|Кто был последним переключателем, который изменил вас?
All right.|Отлично.
Because don't forget, your handy dandy,|Потому что не забывай, твой удобный денди,
show CDP neighbor detail.|показать детали соседа CDP.
All right, or let's do,|Хорошо, или давай,
let's do a simple one.|давайте сделаем простой.
Show CDP neighbor, well the detail will give you the IP address,|Покажите соседа CDP, подробности предоставят вам IP-адрес,
we have the IP addresses.|у нас есть IP-адреса.
But you can see that, hey,|Но ты видишь это, эй,
here's my core 1 and here's my faculty.|вот мое ядро ​​1 и вот мой факультет.
Those are the two switches that I'm directly connected to.|Это два переключателя, к которым я напрямую подключен.
All right, so that's important.|Хорошо, это важно.
That's important to be very aware of that VTP status and using it in combination with the show CDP neighbor or show CDP neighbor detail if you're|Важно знать этот статус VTP и использовать его в сочетании с показом соседа CDP или показывать подробности соседа CDP, если вы
looking for a particular IP address.|ищет конкретный IP-адрес.
There is your VTP.|Вот и ваш ВТП.
I'll see you in the next one.|Увидимся в следующем.