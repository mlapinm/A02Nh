D:\mailCloud\prjother\tmp\1\c79_Purpose of Using Switches & Specific functions at Layer2.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
Welcome back, everyone.|С возвращением, все.
Well, we made it through the dynamic writing protocols read version two,|Что ж, мы сделали это через протоколы динамической записи, читаем версию два,
EIGRP and OSPF.|EIGRP и OSPF.
As you can see behind me, I do have a little switch lab here.|Как вы можете видеть позади меня, у меня здесь есть небольшая лаборатория переключателей.
But basically we're gonna talk about switching.|Но в основном мы поговорим о переключении.
And do we need switching?|А нужно ли переключение?
Of course we need switching.|Конечно, нам нужно переключение.
Everything within our networks are switches.|Все в наших сетях - переключатели.
We come from a world of hubs where,|Мы приехали из мира хабов, где,
where we explain early in the course hubs are just a complete disaster.|где мы объясняем в начале курса, хабы - это просто катастрофа.
Because they have one collision domain,|Поскольку у них один домен коллизии,
one broadcast domain.|один широковещательный домен.
You can only have half duplex.|У вас может быть только полудуплекс.
So, not a good idea.|Итак, не лучшая идея.
We did have bridges, but again,|У нас были мосты, но опять же,
we're limited with bridges, as far as the number of ports are concerned.|мы ограничены мостами, что касается количества портов.
They're software based, so they're a little bit slower than the actual switches, plus they can only do one spanning tree per one spanning tree|Они основаны на программном обеспечении, поэтому они немного медленнее, чем фактические коммутаторы, плюс они могут выполнять только одно связующее дерево на одно связующее дерево.
period for all VLAN.|период для всех VLAN.
Where now cuz the person of bridges was through segment,|Где теперь, потому что человек мостов был через сегмент,
were switches bringing this functionality into the network.|были коммутаторы, обеспечивающие эту функциональность в сети.
Not only are they faster, cuz they're a,|Они не только быстрее, потому что они,
the firmware ASICs everything's within the firmware, so things run a lot faster.|прошивки ASIC все внутри прошивки, так что все работает намного быстрее.
We don't, I mean a small switch 24 ports,|Мы нет, я имею в виду небольшой коммутатор на 24 порта,
12 ports, 48 ports, and they, and the number keeps going up, up,|12 портов, 48 портов, и они, и число продолжает расти, расти,
up and up.|вверх и вверх.
The higher switches you get to.|Чем выше переключатели вы доберетесь.
Also you have full duplex coming out of each ports.|Также у вас есть полный дуплекс, выходящий из каждого порта.
Okay, that means we can send and receive at the same time.|Хорошо, это означает, что мы можем отправлять и получать одновременно.
So that increased that as well.|Так что это тоже увеличило.
Obviously, we do have the possibility of creating VLANs, and VLANs when we get into it, but just an overview.|Очевидно, что у нас есть возможность создавать VLAN и VLAN, когда мы входим в это, но это только обзор.
VLANs layer is logical segmentation of a local area network.|Уровень VLAN - это логическая сегментация локальной сети.
Okay?|Ладно?
So that's where VLANs are.|Вот где находятся VLAN.
Not only to mention it, it brings the spanning tree as well, for that switching loop not to happen.|Не только упомянуть об этом, но и получить связующее дерево, чтобы этот цикл переключения не происходил.
But you can create a spanning tree sessions per VLAN,|Но вы можете создать сеансы связующего дерева для каждой VLAN,
where before you couldn't do that.|где раньше вы не могли этого сделать.
And we also have switch port security plus another a lot of other things,|И у нас также есть защита порта коммутатора плюс еще много других вещей,
but switch port security will be the last place we will stop, okay.|но безопасность порта коммутатора будет последним местом, на котором мы остановимся, хорошо.
Because there's only so many things that you need to know.|Потому что вам нужно знать очень много всего.
We'll talk about VTP, and trunking, and all these different things, once we get to the appropriate lesson.|Мы поговорим о VTP, транкинге и всех этих разных вещах, когда перейдем к соответствующему уроку.
But definitely you do need switches.|Но вам определенно нужны переключатели.
You do need switches in your infrastructure.|Вам действительно нужны коммутаторы в вашей инфраструктуре.
Whether it's upper classroom, whatever it is.|Будь то старшая школа, что бы это ни было.
You need switches in your internetwork.|Вам нужны коммутаторы в вашей объединенной сети.
Now, what switches do, they learn MACaddresses.|Теперь, что делают коммутаторы, они изучают MAC-адреса.
Remember, switches are layer two.|Помните, что переключатели - это второй уровень.
They deal MAC addresses, which are the physical address of each node.|Они имеют дело с MAC-адресами, которые являются физическим адресом каждого узла.
So they create this table called a MAC address table.|Поэтому они создают эту таблицу, которая называется таблицей MAC-адресов.
Now I have three computers here, they already have an IP address.|Теперь у меня здесь три компьютера, у них уже есть IP-адрес.
If I go into the switch, and type enable,|Если я перейду к переключателю и наберу enable,
and I do a show MAC hyphen address table, I see that it's not populated.|и я показываю таблицу MAC-адресов с дефисами, я вижу, что она не заполнена.
Let me maximize this.|Позвольте мне максимизировать это.
All right, it's not populated.|Хорошо, это не заселено.
There's no information going back, and forth at this point.|На данный момент нет никакой информации, возвращающейся туда и обратно.
So it has not learned of any MAC addresses on the network as of yet.|Таким образом, он еще не узнал о каких-либо MAC-адресах в сети.
When communication starts going back and forth, switches learn s,|Когда связь начинает идти туда-сюда, переключатели изучают s,
this is key, source addresses.|это ключевые, исходные адреса.
Source addresses.|Исходные адреса.
In the IP version four world, once a switch sees a Mac address coming towards it, let's say on port one, for example.|В мире IP версии четыре, как только коммутатор видит, что к нему приближается Mac-адрес, например, на порт один.
All right, let me minimize this.|Хорошо, позволь мне минимизировать это.
Let's say PC 0 wanted to talk to PC 1.|Допустим, ПК 0 хотел поговорить с ПК 1.
Once he sends, he sends out what?|Когда он отправляет, он что отправляет?
An ARP request.|Запрос ARP.
IP Version 4, right?|IP версии 4, верно?
So, once that ARP request gets to the switch,|Итак, как только запрос ARP попадает на коммутатор,
the switch will learn that source MAC address on that particular PC,|коммутатор узнает этот исходный MAC-адрес на этом конкретном ПК,
and assign it to that particular port, in this case, F01.|и назначьте его этому конкретному порту, в данном случае F01.
And then out of every other port, and again this is a key word that you need to look for within your testing,|А затем из любого другого порта, и снова это ключевое слово, которое вам нужно искать при тестировании,
it will flood, it will flood, all the other ports with this ARP looking for this, hey whose the owner of this IP address?|он будет заливать, он будет заливать, все остальные порты с этим ARP ищут это, эй, чей владелец этого IP-адреса?
I need to make a MAC address.|Мне нужно сделать MAC-адрес.
The appropriate computer or node would reply,|Соответствующий компьютер или узел ответит:
and then it would map that particular MAC address to that port.|и затем он сопоставит этот конкретный MAC-адрес с этим портом.
Now you have a mapping of ports of MAC addresses per port.|Теперь у вас есть сопоставление портов MAC-адресов на порт.
Does that mean, that now that our Mac address table is populated,|Означает ли это, что теперь, когда наша таблица адресов Mac заполнена,
that there is no more broadcasts?|что трансляций больше нет?
Yes, there is.|Да, есть.
Yes, there is.|Да, есть.
Yes, there is.|Да, есть.
Just because it learned all these MAC addresses, are these computer's great,|Просто потому, что он узнал все эти MAC-адреса, хорош ли этот компьютер,
no more ARP.|больше нет ARP.
But they're still broadcast, because whatever he's doing here, they're gonna hear noise over here, cuz you have multiple collision domain, which is great.|Но они все еще транслируются, потому что что бы он ни делал здесь, они будут слышать здесь шум, потому что у вас есть несколько доменов коллизий, и это здорово.
We should get that full bandwidth coming out of there,|Мы должны получить оттуда полную пропускную способность,
you're not sharing your bandwidth.|вы не делитесь своей пропускной способностью.
This is what's called a Private Collision Domain, but you still have only one broadcast domain.|Это то, что называется частным доменом конфликта, но у вас по-прежнему есть только один домен широковещательной рассылки.
And certain IT individuals still do not understand that.|И некоторые ИТ-специалисты этого до сих пор не понимают.
Give you an example, real world example.|Приведу пример, пример из реального мира.
Schools.|Школы.
I have, all of you know me for saying the same thing, cuz I've done a lot of schools.|Все вы знаете, что я говорю то же самое, потому что я учился во многих школах.
In schools, they for whatever reason,|В школах они по какой-то причине,
maybe they're catching up now, I don't know they don't use VLANs.|возможно, они сейчас догоняют, я не знаю, что они не используют VLAN.
They separate, physically segment the network between, let's say,|Они разделяют, физически сегментируют сеть между, скажем,
administration where the the registrars the ad what do you call those people?|администрация где регистраторы объявление как вы называете этих людей?
The the people that get you into school.|Люди, которые приводят вас в школу.
The admissions, the counselors, wha,|Прием, вожатые, ага,
account executives,|руководители счетов,
whatever they wanna be called.|как бы они ни назывались.
The executive director, the ED, admin people, okay?|Исполнительный директор, ED, администраторы, хорошо?
The people that run the school.|Люди, которые управляют школой.
That, they physically have their own routers, and switches, and firewalls and stuff like that.|То есть, у них физически есть свои собственные маршрутизаторы, коммутаторы, межсетевые экраны и тому подобное.
The students have their own routers, and switches, and firewalls, and all that.|У студентов есть свои маршрутизаторы, коммутаторы, межсетевые экраны и все такое.
So they physically segment, but you have,|Итак, они физически сегментируют, но у вас есть
let's say, 50 classrooms.|скажем, 50 аудиторий.
And your IT school, part IT, part I don't know medical whatever's hot nowadays,|И ваша ИТ-школа, отчасти ИТ, отчасти я не знаю медицины, что бы сейчас ни крутилось,
all right so, you're running on the same VLAN because by default all switches are part of VLAN 1, VLAN 1,|хорошо, значит, вы работаете в одной и той же VLAN, потому что по умолчанию все коммутаторы являются частью VLAN 1, VLAN 1,
and I'm gonna show you this real quick,|и я покажу тебе это очень быстро,
just, you know, what I'm talking about,|просто, вы знаете, о чем я говорю,
just so, you know, what I'm talking about.|просто так, понимаете, о чем я говорю.
Okay.|Ладно.
Do, do, do.|Делай, делай, делай.
Show VLAN.|Показать VLAN.
See?|Видеть?
We're all part of VLAN 1.|Мы все являемся частью VLAN 1.
All ports are part of the same VLAN.|Все порты являются частью одной VLAN.
So if you, you can have 50 switches, a switch per classroom,|Итак, если у вас может быть 50 переключателей, переключатель на класс,
we're all part, of that VLAN1.|мы все являемся частью этой VLAN1.
So, no mater where you are in your campus,|Итак, не важно, где вы находитесь в своем кампусе,
if you're not physically segmented from that VLAN1,|если вы физически не отделены от этой VLAN1,
anything you do, it will create noise.|что бы вы ни делали, это создаст шум.
And the example is the following.|И пример такой.
I was in a school at one point we're again,|Я был в школе, когда мы снова,
over 400 students no, no that's not such a big number, but it's okay 400 people,|более 400 студентов нет-нет это не такая уж и большая цифра, но это нормально 400 человек,
right 400 computers actually, you know,|на самом деле 400 компьютеров, вы знаете,
people doing things to it and it's IT, partial IT, partial, you know,|люди что-то делают с этим, и это ИТ, частичное ИТ, частичное, понимаете,
nursing whatever.|уход за кем угодно.
But what happens, when the IT students start configuring DHCP?|Но что происходит, когда ИТ-студенты начинают настраивать DHCP?
And we're all part of the same VLAN.|И мы все являемся частью одной VLAN.
Now, you have two DHCP servers with the same VLAN assigning IP addresses to a school.|Теперь у вас есть два DHCP-сервера с одной и той же VLAN, назначающие IP-адреса школе.
Problem number, that's a that's a problem.|Номер проблемы, вот и проблема.
cuz they, somebody's doing a test, and they're based on going out to the internet,|потому что они, кто-то делает тест, и они основаны на выходе в Интернет,
and now they just received an IP address from you, now they're no longer gonna be going to the internet, because you're not|и теперь они только что получили от вас IP-адрес, теперь они больше не собираются выходить в Интернет, потому что вы не
hooked up to the internet.|подключен к Интернету.
You're not running NAD or anything like that, you're not hooked up to the router that goes to the internet.|Вы не используете NAD или что-то в этом роде, вы не подключены к маршрутизатору, который выходит в Интернет.
So that's problem number one, problem number two, let's say the IT individual decides to run an image using whatever,|Итак, это проблема номер один, проблема номер два, допустим, ИТ-специалист решает запустить образ, используя что угодно,
Copernicus, Ghost, whatever software.|Коперник, Призрак, любой софт.
I, I think it's called Copernicus, but I know Ghost is popular that I,|Мне кажется, его зовут Коперник, но я знаю, что Призрак популярен, что я,
at least back then everybody used.|по крайней мере, тогда все использовали.
If you're running an image, and the image is kind of big,|Если вы запускаете изображение, и оно довольно большое,
you're going to bring an hour down to a crawl.|вы собираетесь довести час до ползания.
So you're gonna have students that are suffering they won't be able to take tests, because the tests are on the network or they're very slow to do that.|Итак, у вас будут ученики, которые страдают от того, что они не смогут пройти тесты, потому что тесты находятся в сети или они очень медленно это делают.
You're gonna have instructors that are going to suffer, because let's say they need to put in grades, but in order to get to the grade book,|У вас будут преподаватели, которые будут страдать, потому что, скажем, им нужно ставить оценки, но чтобы добраться до журнала,
which is in our centralized server outside of their own local area network,|который находится на нашем централизованном сервере за пределами их собственной локальной сети,
outside their particular location, that's a problem.|за пределами их конкретного местоположения, это проблема.
So, some web-based application, let's say,|Итак, какое-нибудь веб-приложение, скажем,
we gotta get to the internet.|нам нужно добраться до интернета.
Now, that image is causing a problem, so we can see, where creating VLANs is something that you must do.|Теперь это изображение вызывает проблему, поэтому мы можем видеть, где создание VLAN - это то, что вы должны сделать.
So, that's why we're gonna learn how to create VLANs?|Итак, почему мы узнаем, как создавать сети VLAN?
But broadcast, that was a whole point of this analogy.|Но трансляция - вот и весь смысл этой аналогии.
Broadcasts still exist.|Трансляции все еще существуют.
Whoever thinks that just because the MAC address table is full,|Тот, кто думает, что только потому, что таблица MAC-адресов заполнена,
the CAM table, it's full and the MAC addresses of all nodes are there,|таблица CAM, она заполнена и есть MAC-адреса всех узлов,
but that's it, there's no more broadcast.|но все, трансляции больше нет.
Well, you're mistaken.|Вы ошибаетесь.
There is broadcast.|Есть трансляция.
It is your job to segment properly, and to include those VLANs.|Ваша задача - правильно сегментировать и включать эти VLAN.
Use the VLANs, because you can physically segment, but how about logically segmenting?|Используйте VLAN, потому что вы можете сегментировать физически, но как насчет логической сегментации?
All right, and when we get to it, we'll look at the advantages of doing VLANs, but this is what switches bring to us, this|Хорошо, и когда мы дойдем до этого, мы рассмотрим преимущества создания VLAN, но это то, что нам дают коммутаторы, это
functionality.|функциональность.
So I'm gonna go ahead and PNG back and forth, so now you can see,|Итак, я собираюсь перейти к PNG назад и вперед, так что теперь вы можете видеть,
how it's gonna populate that particular MAC address table?|как он будет заполнять эту конкретную таблицу MAC-адресов?
All right, so I'm gonna go ahead.|Хорошо, я пойду вперед.
And I already know the IP address, so this is PNG 192.168.100.2, and then 3, all right?|И я уже знаю IP-адрес, так что это PNG 192.168.100.2, а потом 3, хорошо?
So now, once you PNG that, remember it learns source IP addresses.|Итак, теперь, как только вы это сделаете PNG, помните, что он изучает исходные IP-адреса.
So, the MAC addre, MAC address table should be full now.|Итак, MAC-адрес, таблица MAC-адресов теперь должны быть заполнены.
Let me maximize this window.|Позвольте мне увеличить это окно.
[BLANK_AUDIO]|[BLANK_AUDIO]
If it allows me to?|Если это позволяет мне?
Okay, here we go.|Хорошо, поехали.
And now we see, because once we send that ARP, right?|И теперь мы видим, потому что как только мы отправим этот ARP, верно?
It mapped my MAC address, it saw my source, and then it went out looking for that destination.|Он сопоставил мой MAC-адрес, увидел мой источник, а затем отправился искать этот пункт назначения.
But when that source computer came back,|Но когда тот исходный компьютер вернулся,
it gave it, its source MAC address.|он дал ему свой исходный MAC-адрес.
And that's how I learned for now, we know exactly where these three computers were at based on their MAC addresses.|И вот как я сейчас узнал, мы точно знаем, где были эти три компьютера, на основе их MAC-адресов.
It learned it dynamically.|Он узнал это динамически.
So this is what switches do, and as long as there's communication sure, the ARP broadcast one exists.|Вот что делают коммутаторы, и пока существует связь, существует широковещательная передача ARP.
There, it holds it for a certain period of time, off the top of my head,|Вот оно какое-то время держит его над моей головой,
I don't remember the number, okay?|Я не помню номер, хорошо?
But as long as there's communication going back and forth, and in a network there's always communication back and forth.|Но пока есть связь, идущая туда и обратно, а в сети всегда есть коммуникация туда и обратно.
And you have third party software to be monitoring just in case there's a broken milk cart or something that's constantly|И у вас есть стороннее программное обеспечение, которое нужно отслеживать на случай поломки молочной тележки или чего-то, что постоянно
sending out broadcasts cuz that could be an issue as well.|отправка трансляций, потому что это тоже может быть проблемой.
But that's why the segmentation of your,|Но именно поэтому сегментация вашего,
of your school, of your business, is extremely important.|вашей школы, вашего бизнеса, чрезвычайно важно.
And the best way to make use of that, not only physically, but logically as well.|И лучший способ использовать это не только физически, но и логически.
So, switches, there you go.|Итак, переключатели, поехали.
MAC address tables.|Таблицы MAC-адресов.
All right.|Отлично.
But that's not the only thing.|Но это не единственное.
I mean, we talked about that it brings spanning tree.|Я имею в виду, мы говорили о том, что он приносит остовное дерево.
It can do a pers, spanning tree turbulent.|Это может сделать людей, охвативших дерево, турбулентными.
It can do switch port security.|Он может обеспечивать безопасность порта коммутатора.
So now you can, you're able to control how many and which computer you're going or which nodes, you're going to allow to that|Итак, теперь вы можете, вы можете контролировать, сколько и на каком компьютере вы собираетесь или какие узлы вы собираетесь разрешить этому
particular switch, all right?|конкретный переключатель, хорошо?
So you can create what's called VTP domains.|Таким образом, вы можете создавать так называемые домены VTP.
Where all the switches within that VTP domain will talk to each other.|Где все коммутаторы в этом домене VTP будут общаться друг с другом.
Again, when we get to the lesson we'll,|Опять же, когда мы дойдем до урока, мы,
we'll talk about VTP domains.|поговорим о доменах VTP.
All right, and does the switch need an IP address?|Хорошо, а нужен ли коммутатору IP-адрес?
I didn't need an IP address to get in it because I consoled in, right?|Мне не нужен был IP-адрес, потому что я утешился, верно?
Consoled in.|Утешил.
But, of course, of course, if you have switches in your network,|Но, конечно, если в вашей сети есть свитчи,
and they're not manageable switches,|и это неуправляемые переключатели,
what's the purpose?|какая цель?
What's the purpose of having a switch that brings all this functionality, and not taking advantage of it by have non-managed switches?|Какая цель иметь коммутатор, который обеспечивает всю эту функциональность, и не использовать его преимущества неуправляемых коммутаторов?
So yes, if you're gonna get a switch, get a managed switch.|Так что да, если вы собираетесь получить переключатель, возьмите управляемый переключатель.
That way you put an IP address on the switch.|Таким образом вы установите IP-адрес на коммутаторе.
Now we're going learn, shortly, how to navigate through the switch?|Вскоре мы узнаем, как перемещаться по переключателю?
How to configure put it, its administrative configurations?|Как его настроить, его административные настройки?
But yes, not only does it need an IP address, so you can access that switch,|Но да, ему нужен не только IP-адрес, чтобы вы могли получить доступ к этому коммутатору,
so you can go in there, and tweak the switch, and what I mean by you?|так что ты можешь пойти туда и настроить переключатель, и что я имею в виду под тобой?
I mean the IT administrator or the IT individuals that are allowed to do that.|Я имею в виду ИТ-администратора или ИТ-специалистов, которым это разрешено.
Because you can do it just like the router based on user name and passwords.|Потому что вы можете сделать это так же, как маршрутизатор, на основе имени пользователя и паролей.
But you also put a default gateway on the switch.|Но вы также ставите на коммутатор шлюз по умолчанию.
Cisco recommends, not recommends, Cisco requires that you put a default gateway on your switch, because if you're remote,|Cisco рекомендует, а не рекомендует, Cisco требует, чтобы вы установили шлюз по умолчанию на коммутаторе, потому что, если вы находитесь удаленно,
to your switch and let me make a little clarification on what remote is?|к вашему коммутатору и позвольте мне немного пояснить, что такое пульт?
These are not remote.|Это не удаленные.
They're connected right there.|Они связаны прямо здесь.
But if this is VLAN1, and VLAN2, VLAN3,|Но если это VLAN1, а VLAN2, VLAN3,
VLAN2, and VLAN3 are now remote to the switch,|VLAN2 и VLAN3 теперь удалены от коммутатора,
because they need to go through the router to get back or to get anywhere.|потому что им нужно пройти через маршрутизатор, чтобы вернуться или добраться куда-нибудь.
So they're like remote.|Так что они как бы отдаленные.
But if you're actually, physically or with in a different broadcast domain,|Но если вы на самом деле, физически или находитесь в другом широковещательном домене,
in order to access, in order to access,|чтобы получить доступ, чтобы получить доступ,
the switch.|выключатель.
To go in the switch.|Идти в выключатель.
You need to put a default gateway, as per Cisco.|Вам нужно поставить шлюз по умолчанию согласно Cisco.
So you need to remember that, and we'll do it when we do the configurations.|Так что вам нужно помнить об этом, и мы сделаем это при настройке.
All right so, you need an IP address so you can get into your switch.|Итак, вам нужен IP-адрес, чтобы вы могли подключиться к коммутатору.
If you're local, all you need is really an IP address.|Если вы местный, вам действительно нужен IP-адрес.
But if you're remote, to your switch in a different broadcast domain, you do need a default gateway.|Но если вы находитесь удаленно, к коммутатору в другом широковещательном домене вам понадобится шлюз по умолчанию.
So all these things are what switches are doing?|Итак, все эти вещи делают переключатели?
They're doing a lot of work, but we definitely need them.|Они много работают, но они нам точно нужны.
Definitely I, I remember working for another school where they had routers perform.|Определенно я, я помню, как работал в другой школе, где работали маршрутизаторы.
Not feasible, very nice.|Не возможно, очень красиво.
Thank you very much, I appreciate that.|Большое спасибо, я ценю это.
But you're shooting yourself in the foot definitely financially.|Но вы стреляете себе в ногу определенно в финансовом отношении.
It's a switch per floor, if you want.|Если хотите, это переключатель на каждом этаже.
And just one router by the POP, right,|И только один роутер у точки доступа, верно,
the Point of Presence, where the internet's gonna be.|Точка присутствия, где будет Интернет.
Switch per floor, switch per classroom.|Переключатель на этаже, переключатель на класс.
However it is, that you are gonna do it but,|Как бы то ни было, вы собираетесь это сделать, но,
definitely switches, switches, switches are what you need,|определенно переключатели, переключатели, переключатели - это то, что вам нужно,
because you can create access lists on switches as well.|потому что вы также можете создавать списки доступа на коммутаторах.
Now I know there's a question out there,|Теперь я знаю, что есть вопрос,
and nobody's asked me it.|и меня об этом никто не спрашивал.
But they say, hey Laz, how come?|Но они говорят: эй, Лаз, как получилось?
Because at my company we use layer three switches and that's very good for you, but in the CCNA certification we use layer two switches.|Потому что в моей компании мы используем коммутаторы третьего уровня, и это очень хорошо для вас, но в сертификации CCNA мы используем коммутаторы второго уровня.
You need to know about layer two switching not layer three.|Вам нужно знать о переключении второго уровня, а не третьего.
A layer three switch just has routing capabilities.|Коммутатор третьего уровня просто имеет возможности маршрутизации.
For the CCNA you don't need to be concerned about layer three switches.|Для CCNA вам не нужно беспокоиться о переключателях третьего уровня.
All you need to be concerned about is,|Все, о чем вам нужно беспокоиться, это
layer two switches.|переключатели второго уровня.
How to create VLANs?|Как создать VLAN?
How to assign VLANs?|Как назначить VLAN?
How to manipulate spanning tree?|Как управлять остовным деревом?
What is a VTP domain?|Что такое домен VTP?
What is a trunk?|Что такое ствол?
These are the things, interim VN routing,|Вот такие вещи, временная маршрутизация VN,
these are the things that you need to be concerned with, because switching is another 20% part of your grade.|это то, о чем вам нужно позаботиться, потому что переключение - это еще 20% вашей оценки.
And guess what, ladies and gentlemen?|И знаете что, дамы и господа?
When you go take your test, switching will be a simulation.|Когда вы пойдете на тест, переключение будет имитацией.
I believe, from what I hear, all right?|Я полагаю, из того, что я слышу, хорошо?
Again, I get feedback from all my students that go take their test.|Опять же, я получаю отзывы от всех своих учеников, которые проходят тест.
It is just a bunch of show commands.|Это просто набор команд для показа.
But, you need to know the show commands,|Но вам нужно знать команды шоу,
which I will show you what you need to type, to look at the information that you need to look at.|который я покажу вам, что вам нужно напечатать, чтобы увидеть информацию, которую вам нужно просмотреть.
All right, so I'll show you the main show commands that you to know.|Хорошо, я покажу вам основные команды show, которые вам следует знать.
So again, do we need switches in our network?|Итак, опять же, нужны ли нам коммутаторы в нашей сети?
Yes.|Да.
Do we need to put IP addresses and default gateways on there?|Нужно ли нам указывать там IP-адреса и шлюзы по умолчанию?
Yes.|Да.
Why?|Зачем?
Because we need to access our switches so we can configure them appropriately, so our network will be efficient.|Потому что нам нужен доступ к нашим коммутаторам, чтобы мы могли их правильно настроить, чтобы наша сеть была эффективной.
And always remember the golden rule,|И всегда помни золотое правило,
80% of all your traffic should be local to your segment.|80% всего вашего трафика должно быть локальным для вашего сегмента.
All right?|Отлично?
I'll see you in the next session.|Увидимся на следующем сеансе.
[BLANK_AUDIO]|[BLANK_AUDIO]