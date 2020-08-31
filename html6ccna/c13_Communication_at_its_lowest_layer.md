D:\mailCloud\prjother\tmp\1\c13_Communication at its lowest layer.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
Welcome back.|Добро пожаловать.
Now that we know the need for networks is here,|Теперь, когда мы знаем, что потребность в сетях существует,
we're to gain an understanding of how computers communicate at their lowest level, their most functional level.|мы должны понять, как компьютеры общаются на самом низком, наиболее функциональном уровне.
Excuse me for a second, I have to take my glasses off for this one.|Простите меня на секунду, мне нужно снять очки для этого.
Not really.|На самом деле, нет.
It's very, very simple the way they communicate.|Они общаются очень и очень просто.
Now obviously we'll be talking about IPv4,|Теперь, очевидно, мы будем говорить об IPv4,
because we will be discussing a little bit about ARP, all right?|потому что мы немного поговорим об ARP, хорошо?
We'll get more into ARP when we get into the routing process, but you have two computers, as you can see back here, and I'm going to move out of your way, all|Мы подробнее рассмотрим ARP, когда перейдем к процессу маршрутизации, но у вас есть два компьютера, как вы можете видеть здесь, и я собираюсь уйти с вашего пути, все
right, and move this to one side.|вправо, и переместите это в сторону.
And you guys can see there we got Juan and you have Maria, right?|И вы, ребята, видите, что у нас есть Хуан, а у вас Мария, верно?
Two computers, those are their computer names, but obviously these computers in order to communicate with each other have to have an IP address.|Два компьютера, это их имена компьютеров, но очевидно, что эти компьютеры для связи друг с другом должны иметь IP-адрес.
Not only do they have, and that will be considered a layer three address, right?|Мало того, что у них есть, и это будет считаться адресом третьего уровня, верно?
We'll talk about layers later on when we talk about the OSI model, but this is a layer three.|Мы поговорим об уровнях позже, когда будем говорить о модели OSI, но это третий уровень.
This is the IP address.|Это IP-адрес.
So that will be then we need to have IP addresses and they also have, whoops.|Так что тогда нам понадобятся IP-адреса, и они тоже, упс.
They also have MAC addresses, MAC which are.|У них также есть MAC-адреса, которые есть.
okay.|Ладно.
I guess my finger's not on the on the money there.|Я полагаю, что мой палец не на деньгах.
So this is 192.168.1.1, this will be 192.168.1.2.|Это 192.168.1.1, это будет 192.168.1.2.
So, but we have a layer one device right here, which is a hub.|Итак, но у нас прямо здесь есть устройство первого уровня, которое является концентратором.
Now hubs are not used in today's technology, and let me explain just a tad bit about hubs,|Сейчас концентраторы не используются в сегодняшних технологиях, и позвольте мне немного рассказать о концентраторах,
because when Juan wants to talk to Maria,|потому что, когда Хуан хочет поговорить с Марией,
he only knows the name.|он знает только имя.
He doesn't know Maria's IP address.|Он не знает IP-адрес Марии.
Right, we're talking about users.|Да, мы говорим о пользователях.
Users don't know each other's IP addresses.|Пользователи не знают IP-адреса друг друга.
So you go searching for Juan, right, or Maria in this case, you look, searching for Maria's computer.|Итак, вы идете искать Хуана, верно, или Марию, в данном случае, смотрите, ищите компьютер Марии.
So if this is the first time you're doing it, what's gonna happen is there's gonna be an ARP request that's gonna be sent out|Итак, если вы делаете это в первый раз, что произойдет, это будет запрос ARP, который будет отправлен
through this particular layer one device.|через это конкретное устройство уровня один.
And it's going to flood out as many ports as this hub may have.|И он захлестнет столько портов, сколько может иметь этот концентратор.
You could have a four port hub, you can have a 24 port hub.|Вы можете иметь концентратор с четырьмя портами, вы можете иметь концентратор с 24 портами.
All right.|Отлично.
And, this ARP request, this ARP, broadcast Which actually does a layer two and layer three broadcast, looking, hey, who's|И этот запрос ARP, этот ARP, широковещательная передача, которая на самом деле выполняет широковещательную передачу второго и третьего уровня, глядя, эй, кто
Maria?|Мария?
Well, I'm Maria, that's my NetBIOS name,|Что ж, я Мария, это мое имя в NetBIOS,
which is my computer name,|это имя моего компьютера,
and she will reply and she'll say hey,|и она ответит, и она скажет эй,
this is, that's, that's me.|это, это я.
This is my MAC address.|Это мой MAC-адрес.
Right, this is my IP address.|Хорошо, это мой IP-адрес.
So now Juan knows the IP address and knows the MAC address.|Итак, теперь Хуан знает IP-адрес и знает MAC-адрес.
So he's able to communicate with Maria at that point once they make,|Таким образом, он может общаться с Марией в тот момент, когда они
once he finds that information.|как только он найдет эту информацию.
Cuz in order for computers to communicate to each other they need a couple of things.|Потому что для того, чтобы компьютеры могли общаться друг с другом, им нужно кое-что.
They need their source IP address.|Им нужен их исходный IP-адрес.
They need their source MAC address.|Им нужен их исходный MAC-адрес.
They need the destination IP address, and they need the destination MAC address,|Им нужен IP-адрес назначения и MAC-адрес назначения,
plus they need a port number.|плюс им нужен номер порта.
Right?|Правильно?
You're going to a destination somehow,|Вы как-то собираетесь в пункт назначения,
you're doing a remote desktop,|вы делаете удаленный рабочий стол,
are you telneting in, are you sending an email?|вы используете telnet, отправляете ли вы электронное письмо?
So the way you reach the destination,|Итак, как вы доберетесь до места назначения,
whatever path you choose,|какой бы путь вы ни выбрали,
what application you're choosing to use,|какое приложение вы решите использовать,
whether it's the browser,|будь то браузер,
whether it's these telnet sessions, or remote desktop sessions, however it is,|будь то сеансы telnet или сеансы удаленного рабочего стола, как бы то ни было,
FTP sessions, TFTP sessions, however it is you're trying to access that particular destination a port number gets assigned to that.|Сеансы FTP, сеансы TFTP, однако вы пытаетесь получить доступ к этому конкретному месту назначения, которому назначается номер порта.
So all that information needs to be there.|Так что вся эта информация должна быть там.
Well, at first, they don't know that.|Ну, сначала они этого не знают.
So that ARP broadcast will give you that MAC address and IP address of the destination computer.|Таким образом, широковещательная передача ARP предоставит вам MAC-адрес и IP-адрес конечного компьютера.
Now the problem is this,|Теперь проблема в том,
because if you look at it the ARP means Address Resolution Protocol.|потому что если вы посмотрите на это, ARP означает протокол разрешения адресов.
First you had to resolve her name, her NetBIOS name.|Сначала вам нужно было разрешить ее имя, ее имя NetBIOS.
Once he resolves the NetBIOS name,|Как только он разрешит имя NetBIOS,
to get the IP name he needs to resolve the the MAC address.|чтобы получить IP-имя, ему необходимо разрешить MAC-адрес.
Once he gets the MAC address, boom, now we can go ahead and go across.|Как только он получит MAC-адрес, бум, теперь мы можем идти дальше.
But the problem lies in the hub.|Но проблема в хабе.
It's a problem with the hub that we're going to get into definitely, and I just want to mention this right now,|Это проблема с хабом, в которую мы обязательно войдем, и я просто хочу упомянуть об этом прямо сейчас,
just a little bit.|только немного.
A hub is what's called a shared collision domain.|Хаб - это то, что называется общим доменом коллизий.
It's what they call a multi-port repeater.|Это то, что они называют многопортовым повторителем.
Remember that repeaters really only have two ports,|Помните, что ретрансляторы действительно имеют только два порта,
one coming in, and one going out.|один входит и один выходит.
All they do is they bring in a signal,|Все, что они делают, - это сигнал,
they regenerate or or they clean it up, and they send it out the other side, so we can extend a network,|они регенерируют или очищают его и отправляют на другую сторону, чтобы мы могли расширить сеть,
all right, or whatever it is that you're extending.|ладно, или что там вы расширяете.
Hubs are just, just that.|Хабы просто такие.
They just have more ports, and the problem with that is that you have only one collision domain, and I know I'm putting a term at you.|У них просто больше портов, и проблема в том, что у вас только один домен коллизий, и я знаю, что ставлю вам термин.
One collision domain, one broadcast domain.|Один домен коллизии, один домен широковещания.
What that really means is chaos, chaos.|На самом деле это означает хаос, хаос.
Because the more you, more computers that you plug in to this particular hub.|Потому что чем больше вы, тем больше компьютеров вы подключаете к этому конкретному концентратору.
Since it's a shared collision domain,|Поскольку это общий домен конфликтов,
what's gonna happen is,|что произойдет,
it's gonna divide that bandwidth.|это разделит эту полосу пропускания.
Now, we haven't talked about cables, but this is a Cat5 twisted pair cable that can have the capability of going 100|Мы не говорили о кабелях, но это витая пара Cat5, способная выдерживать 100
megabits per second,|мегабит в секунду,
the more, let's say you had that 24 ports.|Более того, допустим, у вас было 24 порта.
And all those 24 ports are now plugged in with nodes or computers.|И все эти 24 порта теперь подключены к узлам или компьютерам.
So you gotta divide those 24 ports into those computers,|Итак, вам нужно разделить эти 24 порта на эти компьютеры,
you have five megabits per port.|у вас есть пять мегабит на порт.
You just reduced that bandwidth that you're capable of having,|Вы только что уменьшили пропускную способность, на которую способны,
because you can only have one set of wires,|потому что у вас может быть только один комплект проводов,
one pair of wires, to send and receive.|одна пара проводов для отправки и получения.
So what is that called?|Так как это называется?
It's called half duplex.|Это называется полудуплекс.
So definitely, just to give you an idea.|Так что определенно, просто чтобы дать вам представление.
Very simple network, just two computers trying to talk to each other.|Очень простая сеть, всего два компьютера пытаются общаться друг с другом.
But you know what, I'm going to take this opportunity to show you.|Но знаете что, я воспользуюсь этой возможностью, чтобы показать вам.
I know we've seen it before.|Я знаю, что мы видели это раньше.
Now I'm gonna, I'm gonna show you again,|Теперь я собираюсь, я покажу тебе снова,
all right?|отлично?
So you don't forget.|Так что не забывай.
I'm going to go to our simulation mode right there.|Я собираюсь перейти в наш режим моделирования прямо здесь.
I'm going to get that simple PDU,|Я собираюсь получить этот простой PDU,
remember?|Помните?
That we did in the packet tracer.|Это мы сделали в трассировщике пакетов.
I am going to put it in to Juan's PC and then I am going to hit Maria's PC again and we get that ARP.|Я собираюсь поместить его на компьютер Хуана, а затем снова зайти на компьютер Марии, и мы получим этот ARP.
And I am going to hit that auto capture and play and we see what happens.|И я собираюсь включить этот автоматический захват и воспроизвести, и мы посмотрим, что произойдет.
There is your ARP.|Вот и ваш ARP.
Now that ARP will go out all existing ports if anything was connected on there.|Теперь, когда ARP отключит все существующие порты, если к ним что-то было подключено.
Maria says, hey that's me.|Мария говорит, эй, это я.
Here's my MAC address.|Вот мой MAC-адрес.
I'm going to send that right back at ya,|Я отправлю это тебе обратно,
so you can communicate with me.|так что вы можете общаться со мной.
Once it goes back over there, any day now.|Однажды он вернется туда, в любой день.
Well, it is a shared collision domain, so it slows down.|Ну, это общий домен коллизий, поэтому он тормозит.
And now the ping can go across.|И теперь пинг может пройти.
And you've seen this before.|И вы видели это раньше.
And you can, you can see it right there,|И вы можете, вы можете увидеть это прямо здесь,
that now the ICMP, that is the protocol.|что теперь ICMP, это протокол.
Let's go ahead and delete that.|Давайте удалим это.
All right.|Отлично.
So, it does the same thing.|Итак, он делает то же самое.
The problem is, and we'll always remember to go back to real-time.|Проблема в том, что мы всегда будем помнить о том, чтобы вернуться в режим реального времени.
The problem is this device right here.|Проблема вот в этом устройстве.
You do not wanna have hubs in your networks.|Вы не хотите иметь концентраторы в своих сетях.
Now when we start talking about internetworking devices, and we are, that exist on a network.|Теперь, когда мы начинаем говорить об устройствах межсетевого взаимодействия, которые существуют в сети.
You're gonna start, I'm gonna start explaining to you why you want to use these different devices in your network.|Вы собираетесь начать, я начну объяснять вам, почему вы хотите использовать эти различные устройства в своей сети.
One of which is because this is considered an ethernet network,|Одно из них связано с тем, что это сеть Ethernet,
which is an 802.3 standard, which the access method is CSMACD which means,|который является стандартом 802.3, метод доступа - CSMACD, что означает,
hey, there's noise in the wire.|эй, в проводе шум.
I can't transmit, first come first serve.|Я не могу передавать, первым пришел - первым подал.
Think about it.|Подумай об этом.
You're sharing the bandwidth across all ports.|Вы разделяете полосу пропускания по всем портам.
You have to wait to see if there is anybody transmitting in order for you to transmit, and you can only send or receive,|Вам нужно подождать, чтобы увидеть, есть ли кто-нибудь передающий, чтобы вы могли передавать, и вы можете только отправлять или получать,
because you're using one pair of wires.|потому что вы используете одну пару проводов.
So definitely this would be a chaos.|Так что это определенно будет хаос.
I always use the example of a hub as imagine the busiest intersection in the world.|Я всегда использую пример хаба, представляя самый оживленный перекресток в мире.
Imagine the busiest intersection.|Представьте себе самый оживленный перекресток.
Everybody's going 100 miles an hour.|Все едут со скоростью 100 миль в час.
No stop signs, no traffic lights,|Ни стоп-сигналов, ни светофоров,
no police officers directing traffic,|нет полицейских, управляющих движением,
nothing.|ничего.
Just everybody just running, [SOUND]|Просто все просто бегут, [ЗВУК]
non-stop.|без остановки.
There's bound to be a crash somewhere along the line, and this is exactly what happens when we deal with ethernet.|Где-то на линии обязательно произойдет сбой, и именно это происходит, когда мы имеем дело с Ethernet.
This is one of the issues that we have to face.|Это одна из проблем, с которыми нам приходится сталкиваться.
That's the just the way ethernet is.|Таков и Ethernet.
So one of the things that, as networks developed as you'll see,|Итак, по мере развития сетей, как вы увидите,
definitely, the hub got replaced.|однозначно заменили ступицу.
Because of that one collision domain,|Из-за этого домена столкновения
one broadcast domain that all it does, it causes chaos.|один широковещательный домен, который все, что он делает, вызывает хаос.
But once we start learning about the different devices that exist on a network,|Но как только мы начнем узнавать о различных устройствах, существующих в сети,
then you'll start getting an idea on, hey,|тогда вы начнете понимать, эй,
this will be a better device.|это будет лучшее устройство.
This is how we are going to segment it.|Вот как мы собираемся его сегментировать.
This is how we create those VLANs later,|Вот как мы создадим эти VLAN позже,
too, so we can tweak our network and make it more functional.|тоже, чтобы мы могли настроить нашу сеть и сделать ее более функциональной.
So I'll see you in the next lecture.|Увидимся на следующей лекции.
[BLANK_AUDIO]|[BLANK_AUDIO]
[BLANK_AUDIO]|[BLANK_AUDIO]
Welcome back.|Добро пожаловать.
Now that we know the need for networks is here,|Теперь, когда мы знаем, что потребность в сетях существует,
we're to gain an understanding of how computers communicate at their lowest level.|мы должны понять, как компьютеры общаются на самом низком уровне.
Their most functional level.|Самый функциональный их уровень.
Excuse me for a second.|Простите меня на секунду.
I have to take my glasses off for this one.|Для этого мне нужно снять очки.
Not really.|На самом деле, нет.
It's very, very simple, the way they communicate.|Они общаются очень и очень просто.
Now obviously, we'll be talking about IPv4|Теперь, очевидно, мы будем говорить об IPv4.
because we're gonna be discussing a little bit about ARP, all right?|потому что мы собираемся немного обсудить ARP, хорошо?
We'll get more into ARP when we get into the routing process.|Мы подробнее рассмотрим ARP, когда перейдем к процессу маршрутизации.
But, you have two computers, and you can see back here, and I'm gonna move out of your way, all right,|Но у вас есть два компьютера, и вы можете видеть здесь, и я собираюсь уйти с вашего пути, хорошо,
and move this to one side.|и переместите это в сторону.
And, you guys can see there, we got Juan,|И вы, ребята, видите, у нас есть Хуан,
and you have Maria, right?|а у тебя есть Мария, да?
Two computers there.|Там два компьютера.
Those are their computer names, but obviously, these computers,|Это имена их компьютеров, но очевидно, что эти компьютеры,
in order to communicate with each other,|чтобы общаться друг с другом,
have to have an IP address.|должен иметь IP-адрес.
Not only do they have and that would be considered a layer three address right?|Мало того, что у них есть, и это будет считаться адресом третьего уровня, верно?
And we'll talk about layers later on when we talk about the OSI model.|А о слоях мы поговорим позже, когда будем говорить о модели OSI.
But, this is a layer three, this would be IP address.|Но это третий уровень, это будет IP-адрес.
So there will be then we need to have IP addresses.|Значит, тогда нам понадобятся IP-адреса.
And they also have, whoops, they also have MAC addresses, MAC which are, okay?|И у них также есть MAC-адреса, MAC-адреса, которые есть, хорошо?
I guess my finger's not on the on the money there.|Я полагаю, что мой палец не на деньгах.
So this is 192.168.1.1.|Итак, это 192.168.1.1.
This would be 192.168.1.2.|Это будет 192.168.1.2.
So, but, we have a layer one device right here, which is a hub.|Итак, но у нас прямо здесь есть устройство первого уровня, которое является концентратором.
Now hubs are not used in today's technology.|Сейчас хабы не используются в сегодняшней технике.
And let me explain just a tad bit about hubs,|И позвольте мне немного рассказать о хабах,
because when Juan wants to talk to Maria,|потому что, когда Хуан хочет поговорить с Марией,
he only know the name,|он знает только имя,
he doesn't know Maria's IP address, right,|он не знает IP-адрес Марии, верно,
we're talking about users.|мы говорим о пользователях.
Users don't know each other's IP addresses.|Пользователи не знают IP-адреса друг друга.
So, you go searching for Juan, right?|Итак, вы идете искать Хуана, верно?
Or Maria, in this case, you go searching for Maria's computer.|Или Мария, в этом случае вы идете искать компьютер Марии.
So, if this is the first time you're doing it,|Итак, если вы делаете это впервые,
what's gonna happen is, there's going to be an ARP request that's gonna be sent out through this particular layer one device.|Что произойдет, так это то, что будет ARP-запрос, который будет отправлен через это конкретное устройство первого уровня.
And it's gonna flood out as many ports as this hub may have.|И он захлестнет столько портов, сколько может иметь этот концентратор.
You can have a four port hub, you can have a 24 port hub.|Вы можете иметь концентратор с четырьмя портами, вы можете иметь концентратор с 24 портами.
All right?|Отлично?
And this ARP request, this ARP broadcast,|И этот запрос ARP, эта трансляция ARP,
which actually does a layer two and layer three broadcast.|который фактически транслирует уровень два и уровень три.
Looking, hey, who's Maria?|Смотри, эй, кто такая Мария?
Well, I'm Maria.|Что ж, я Мария.
That's my NetBIOS name, which is my computer name.|Это мое имя NetBIOS, имя моего компьютера.
And she will reply and she'll say, hey,|И она ответит, и она скажет, эй,
this is, that's, that's me.|это, это я.
This is my MAC address.|Это мой MAC-адрес.
Right, this is my IP address.|Хорошо, это мой IP-адрес.
So now, Juan knows the IP address and knows the MAC address, so he's able to communicate with Maria at that point, once they make, once he finds that information.|Итак, теперь Хуан знает IP-адрес и MAC-адрес, поэтому он может общаться с Марией в этот момент, как только они это сделают, как только он найдет эту информацию.
Cuz in order for computers to communicate to each other,|Потому что для того, чтобы компьютеры могли общаться друг с другом,
they need a couple of things.|им нужна пара вещей.
They need their source IP address.|Им нужен их исходный IP-адрес.
They need their source, MAC address,|Им нужен их источник, MAC-адрес,
they need the destination IP address, and they need the destination MAC address,|им нужен IP-адрес назначения, и им нужен MAC-адрес назначения,
plus, they need a port number.|плюс им нужен номер порта.
Right?|Правильно?
You're going to a destination some how,|Каким-то образом вы собираетесь в пункт назначения,
you're doing a remote desktop, are you telnetting it, are you sending an email?|вы делаете удаленный рабочий стол, подключаете ли вы его через telnet, отправляете ли вы электронное письмо?
So, the way you reach the destination,|Итак, как вы доберетесь до места назначения,
whatever path you choose, or application you're choosing to use.|какой бы путь вы ни выбрали или какое приложение вы выбрали для использования.
Whether it's the browser.|Будь то браузер.
Whether it's these telnets sessions, or remote desktop session.|Будь то сеансы Telnet или сеанс удаленного рабочего стола.
However it is.|Однако это так.
FTP sessions, TFTP sessions.|FTP-сеансы, TFTP-сеансы.
However it is you're trying to access that particular destination,|Однако вы пытаетесь получить доступ к этому конкретному месту назначения,
a port number gets assigned to that.|ему назначается номер порта.
So, all that information needs to be there.|Итак, вся эта информация должна быть там.
Well, at first, they don't know that.|Ну, сначала они этого не знают.
So, that ARP broadcast will give you that MAC address and IP address of the destination computer.|Таким образом, эта широковещательная передача ARP даст вам MAC-адрес и IP-адрес конечного компьютера.
Now the problem is this.|Теперь проблема вот в чем.
Because, if you look at it, the ARP means Address Resolution Protocol.|Потому что, если вы посмотрите на это, ARP означает протокол разрешения адресов.
First, you had to resolve her name, her NetBIOS name.|Во-первых, вам нужно было разрешить ее имя, ее имя NetBIOS.
Once she resolves the NetBIOS name, she gets the IP name,|Как только она разрешает имя NetBIOS, она получает IP-имя,
then she needs to resolve the the MAC address.|тогда ей нужно разрешить MAC-адрес.
Once it gets the MAC address, boom.|Как только он получит MAC-адрес, бум.
Now we can go ahead and go across, but the problem lies in the hub.|Теперь мы можем пойти дальше, но проблема в ступице.
It's a problem with the hub that we're gonna get into, definitely, and I just want to mention this right now,|Это проблема с хабом, в который мы обязательно войдем, и я просто хочу упомянуть об этом прямо сейчас,
just a little bit.|только немного.
A hub is what's called a shared collision domain.|Хаб - это то, что называется общим доменом коллизий.
It's what they call a multi-port repeater.|Это то, что они называют многопортовым повторителем.
Remember that repeaters really only have two ports, one coming in, one going out.|Помните, что у повторителей на самом деле только два порта: один входящий, другой выходной.
All they do is they bring in a signal,|Все, что они делают, - это сигнал,
they regenerate it, they clean it up and they send it out the other side.|они регенерируют его, очищают и отправляют на другую сторону.
So we can extend a network.|Таким образом, мы можем расширить сеть.
All right?|Отлично?
Or whatever it is that you're extending.|Или что-то еще, что вы расширяете.
Hubs are just, just that, they just have more ports.|Хабы просто, просто у них больше портов.
And the problem with that is that you have only one collision domain, and I know I'm throwing a term at you, one collision domain, one broadcast domain.|И проблема в том, что у вас только один домен коллизии, и я знаю, что бросаю вам термин: один домен коллизии, один домен широковещания.
What that really means is, chaos.|На самом деле это означает хаос.
Chaos.|Хаос.
Because the more you, more computers that you plug into this particular hub,|Потому что чем больше вы, тем больше компьютеров вы подключаете к этому конкретному концентратору,
since this is a shared collision domain,|поскольку это общий домен коллизий,
what's gonna happen is,|что произойдет,
it's gonna divide that bandwidth.|это разделит эту полосу пропускания.
Now, we haven't talked about cables but this is a cat 5 twisted pair cable that can have the capability of going 100|Мы не говорили о кабелях, но это витая пара категории 5, которая может выдерживать 100
megabits per second.|мегабит в секунду.
The more, let's say you had that 24 ports,|Более того, допустим, у вас было 24 порта,
and all those 24 ports are now plugged in with nodes, or computers, so you gotta divide those 24|и все эти 24 порта теперь подключены к узлам или компьютерам, поэтому вам нужно разделить эти 24
ports into those computers.|порты в эти компьютеры.
You have five megabits, per port.|У вас есть пять мегабит на порт.
You just reduced that bandwidth that you're capable of having,|Вы только что уменьшили пропускную способность, на которую способны,
cuz you can only have one set of wires,|Потому что у вас может быть только один комплект проводов,
one pair of wires, to send and receive, so what is that called?|одна пара проводов для отправки и получения, так как это называется?
It's called half duplex.|Это называется полудуплекс.
So, definitely, just to give you an idea.|Так что, определенно, просто чтобы дать вам представление.
Very simple network, just two computers trying to talk to each another.|Очень простая сеть, всего два компьютера пытаются общаться друг с другом.
But you know what, I'm going to take this opportunity to show you,|Но знаешь что, я воспользуюсь этой возможностью, чтобы показать тебе,
I know we've seen it before.|Я знаю, что мы видели это раньше.
But I'm going, I'm going to show you again, all right, so you don't forget.|Но я пойду, я покажу тебе еще раз, хорошо, так что не забывай.
I'm going to go to our simulation mode,|Я собираюсь перейти в наш режим симуляции,
right there.|прямо там.
I'm going to get that simple PDU,|Я собираюсь получить этот простой PDU,
remember,|Помните,
that we did in the packet tracer.|что мы сделали в трассировщике пакетов.
I'm gonna put it in Juan's PC and then I'm gonna hit Maria's PC.|Я собираюсь поместить его в компьютер Хуана, а затем я найду компьютер Марии.
Again, we get that ARP.|Опять же, мы получаем тот ARP.
And I'm gonna hit that Auto Capture and Play and we see what happens.|И я нажму на кнопку Auto Capture and Play, и мы посмотрим, что произойдет.
There's your ARP.|Вот ваш ARP.
Now that ARP will go out all existing ports of anything it was connected on there.|Теперь, когда ARP отключит все существующие порты всего, к чему он был подключен.
Maria says hey, that's me.|Мария говорит, эй, это я.
Here's my MAC address.|Вот мой MAC-адрес.
I'm going to send it right back at you, so you can communicate with me.|Я отправлю его вам обратно, чтобы вы могли связаться со мной.
Once it goes back over there, any day now,|Однажды он вернется туда, в любой день,
well it is a shared collision domain so it slows down, and now the ping can go across.|ну, это общий домен коллизий, поэтому он замедляется, и теперь пинг может проходить.
And you've seen this before.|И вы видели это раньше.
And you can, you can see it right there that now the ICMP, that is the protocol,|И вы можете, вы можете видеть это прямо здесь, что теперь ICMP, это протокол,
let's go ahead and delete that.|давайте продолжим и удалим это.
All right.|Отлично.
So it does the same thing, the problem is,|То же самое, проблема в том,
and always remember to go back to Real Time,|и всегда не забывайте возвращаться в реальное время,
the problem is, this device right here.|проблема в том, что это устройство прямо здесь.
You do not want to have hubs in your networks.|Вы не хотите, чтобы в ваших сетях были концентраторы.
Now, when we start talking about internetworking devices, and we are, that exist on our network.|Теперь, когда мы начинаем говорить об устройствах межсетевого взаимодействия, которые существуют в нашей сети.
You're going to start, I'm going to start explaining to you why you want to use these different devices in your network.|Вы собираетесь начать, я собираюсь начать объяснять вам, почему вы хотите использовать эти разные устройства в своей сети.
One of which, is because this is considered an Ethernet network,|Один из них, потому что это считается сетью Ethernet,
which is an 802.3 standard.|который является стандартом 802.3.
Which the access method is CSMACD, which means hey,|Какой метод доступа - CSMACD, что означает эй,
there's noise in the wire, I can't transmit, first come first serve.|в проводе шум, я не могу передать, первым пришел, первым подал.
Think about it, you're sharing the bandwidth across all ports.|Подумайте об этом, вы разделяете полосу пропускания по всем портам.
You have to wait to see if there's anybody transmitting in order for you to transmit and you can only send or receive, because|Вам нужно подождать, чтобы увидеть, есть ли кто-нибудь передающий, чтобы вы могли передавать, и вы можете только отправлять или получать, потому что
you're using one pair of wires.|вы используете одну пару проводов.
So, definitely, this would be a chaos.|Так что определенно будет хаос.
I always use the example of a hub, as,|Я всегда использую пример хаба, так как,
imagine the busiest intersection in the world.|представьте себе самый оживленный перекресток в мире.
Imagine the busiest intersection,|Представьте себе самый оживленный перекресток,
everybody's going 100 miles an hour.|все едут со скоростью 100 миль в час.
No stop signs,|Знаков остановки нет,
no traffic lights, no police officers directing traffic, nothing.|ни светофоров, ни полицейских, управляющих движением, ничего.
Just everybody just running, [NOISE],|Просто все просто бегут, [NOISE],
nonstop.|без остановки.
There's bound to be a crash somewhere along the line, and this is exactly what happens, when we deal with Ethernet.|Где-то на линии обязательно произойдет сбой, и именно это происходит, когда мы имеем дело с Ethernet.
This is one of the issues that we have to face, that's just the way Ethernet is.|Это одна из проблем, с которыми мы должны столкнуться, таков и Ethernet.
So one of the things that, as networks developed, as you'll see.|Это одна из вещей, которые развиваются по мере развития сетей, как вы увидите.
Definitely, the hub got replaced.|Однозначно заменили ступицу.
Because of that one collision domain, one broadcast domain that,|Из-за этого одного домена коллизий, одного домена широковещательной передачи,
all it does, it causes chaos.|все, что он делает, вызывает хаос.
But once we start learning about the different devices that exist on the network, then you'll start getting an idea of,|Но как только мы начнем изучать различные устройства, существующие в сети, вы начнете понимать,
hey, this would be a better device.|эй, это было бы лучшее устройство.
This is how we're gonna segment it.|Вот как мы будем его сегментировать.
This is how we create those VLANs at layer two, so we can tweak our network and make it more functional.|Вот как мы создаем эти VLAN на втором уровне, чтобы мы могли настроить нашу сеть и сделать ее более функциональной.
So, I'll see you in the next lecture.|Итак, увидимся на следующей лекции.
[BLANK_AUDIO]|[BLANK_AUDIO]