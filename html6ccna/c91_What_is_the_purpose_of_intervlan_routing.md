D:\mailCloud\prjother\tmp\1\c91_What is the purpose of intervlan routing.md  


__|__
--|--
All right, are we ready to make these two PCs talk?|Хорошо, мы готовы заставить эти два компьютера разговаривать?
They're in different VLANs, how do we do that?|Они находятся в разных VLAN, как нам это сделать?
You have one physical interface on that router.|У вас есть один физический интерфейс на этом маршрутизаторе.
That router is your gateway, so how in the world are you gonna make these two computers talk?|Этот маршрутизатор - ваш шлюз, так как же вы собираетесь заставить эти два компьютера разговаривать?
It's very simple, all right?|Все очень просто, понятно?
Enter VLAN routing, you are gonna get this scenario over and over and over and over again in your examinations.|Войдите в маршрутизацию VLAN, и вы будете получать этот сценарий снова и снова, снова и снова в своих экзаменах.
This is called router on a stick, where you're gonna create sub interfaces,|Это называется роутером на флешке, где вы собираетесь создавать вспомогательные интерфейсы
all right?|отлично?
And then you'll use the encapsulation 8021q which is the newest version of encapsulation that we use for InterVLAN routing.|И затем вы будете использовать инкапсуляцию 8021q, которая является новейшей версией инкапсуляции, которую мы используем для маршрутизации InterVLAN.
In previous, it was ISL.|Раньше это был ISL.
We no longer use ISL, just know that we did.|Мы больше не используем ISL, просто знаем, что мы это сделали.
Inner switch link that's what we used to use, not anymore.|Внутренняя ссылка переключателя - это то, что мы использовали раньше, а не сейчас.
I say that again, not anymore we use 8021q.|Я повторяю это снова, мы больше не используем 8021q.
Now I'm gonna show you how to do it here,|Теперь я покажу вам, как это сделать здесь,
in a very small lab because in the next lesson, [SOUND] I got a big one for you, okay?|в очень маленькой лаборатории, потому что на следующем уроке [ЗВУК] у меня есть для тебя большой, хорошо?
So your gonna see a big ol' lab we're gonna do combining everything we've done in switching and we're gonna, yes its gonna be big lab.|Итак, вы увидите большую старую лабораторию, мы собираемся объединить все, что мы сделали при переключении, и мы собираемся, да, это будет большая лаборатория.
Anyway, it is important to do InterVLAN routing, right?|В любом случае, важно сделать маршрутизацию InterVLAN, не так ли?
Because like remember the school example that I talked about, you have all these different VLANs, all these different classrooms and their own VLAN.|Потому что, как вспомните пример школы, о котором я говорил, у вас есть все эти разные VLAN, все эти разные классы и их собственная VLAN.
They all need a gateway to get outside.|Всем им нужен выход на улицу.
Once you do this, I want you to consider this, once you create this InterVLAN connectivity because they need to get to the internet.|Как только вы это сделаете, я хочу, чтобы вы обдумали это, как только вы создадите это соединение InterVLAN, потому что им необходимо подключиться к Интернету.
They need to get outside, right?|Им нужно выбраться наружу, верно?
They're not gonna stay within their own VLAN.|Они не собираются оставаться в своей собственной VLAN.
Then somehow they need to get to the outside world or maybe access something outside their own VLAN.|Затем им нужно каким-то образом попасть во внешний мир или, возможно, получить доступ к чему-то за пределами их собственной VLAN.
Remember, 80% of traffic should be local to your VLAN.|Помните, что 80% трафика должно быть локальным для вашей VLAN.
But let's say, they need to get outside so you need to do InterVLAN connectivity.|Но, скажем, им нужно выбраться наружу, поэтому вам необходимо установить соединение InterVLAN.
Once you do that, once you do that and we'll be learning this later on.|Как только вы это сделаете, как только вы это сделаете, мы узнаем об этом позже.
But once you create this InterVLAN connectivity,|Но как только вы создадите это соединение InterVLAN,
you are actually creating like a security hold.|вы фактически создаете что-то вроде блокировки безопасности.
Because anybody can go back and forth,|Потому что каждый может ходить туда-сюда,
back and forth.|взад и вперед.
And then this is where obviously in the CCNA certification level that we need to understand for Cisco.|И вот здесь, очевидно, находится уровень сертификации CCNA, который нам необходимо понять для Cisco.
We create then our access lists,|Затем мы создаем наши списки доступа,
can you create an access list at the layer two level?|вы можете создать список доступа на уровне второго уровня?
Yes.|Да.
Will you be doing that?|Вы будете это делать?
No.|Нет.
Will you be doing that access list at layer three?|Будете ли вы делать этот список доступа на третьем уровне?
Yes.|Да.
So that's what you need to know because we're all here.|Вот что вам нужно знать, потому что мы все здесь.
Why are you here?|Почему ты здесь?
Why did you get this course?|Почему вы прошли этот курс?
You got this course to pass the CCNA certification.|Вы прошли этот курс, чтобы пройти сертификацию CCNA.
Once you guys and gals go back out to your jobs or whatever it was that you were doing.|Как только вы, ребята, и девушки вернетесь на свою работу или чем бы вы там ни занимались.
Now you need to see what they do and then just apply the concepts to your particular infrastructure by now you understand.|Теперь вам нужно посмотреть, что они делают, а затем просто применить концепции к вашей конкретной инфраструктуре, и теперь вы понимаете.
So what we're gonna do is oh, before I,|Итак, что мы собираемся сделать, это о, прежде чем я,
before I say that InterVLAN?|прежде чем я скажу, что InterVLAN?
Yes, it's a must, it's a necessity especially, specially for your certification.|Да, это обязательно, особенно необходимо, особенно для вашей сертификации.
Because you're not gonna be configuring through VLAN connectivity but guess what, you're gonna have maybe a multiple choice question.|Поскольку вы не собираетесь настраивать подключение через VLAN, но угадайте, у вас может возникнуть вопрос с несколькими вариантами ответов.
That's gonna say, hey, this guy needs to talk to this guy.|Это скажет, эй, этому парню нужно поговорить с этим парнем.
How do we get that done?|Как это сделать?
A, b, c, d, e, f, g, h, you need to know the steps.|A, b, c, d, e, f, g, h, вам нужно знать шаги.
So let's show you fairly quickly in this very small app cuz you better be ready for the next, lesson that's to come because|Итак, давайте довольно быстро покажем вам это очень маленькое приложение, потому что вам лучше быть готовым к следующему уроку, который будет, потому что
it's gonna be a bigger lab than this.|это будет лаборатория побольше, чем эта.
So, we have all very important, very important.|Итак, у нас все очень важно, очень важно.
We trunked these ports and let's verify that we did.|Мы объединили эти порты, и давайте проверим, что мы сделали.
If you remember, this was our root bridge you can see that there, perfect.|Если вы помните, это был наш корневой мост, вы можете это увидеть, отлично.
So the command is show in trunk.|Итак, команда отображается в багажнике.
Now remember, we have ports 22 and 23|Теперь помните, у нас есть порты 22 и 23
there.|там.
We don't see port 24, why?|Мы не видим порт 24, почему?
Because part 24 is plugged in to the routers F00 interface.|Потому что часть 24 подключена к интерфейсу маршрутизатора F00.
Where what happens?|Где что происходит?
It's off, so that's why you don't see it there.|Он выключен, поэтому вы его там не видите.
So we know that that port is trunked and if you look, if you do a show start.|Итак, мы знаем, что этот порт транкинговый, и если вы посмотрите, если вы начнете шоу.
[SOUND] And you look at port 24 right there.|[ЗВУК] И вы смотрите на порт 24 прямо там.
Switchport mode trunk.|Транк в режиме Switchport.
So we know that our port is trumped.|Итак, мы знаем, что наш порт превзошел.
It doesn't show up there because that port is connected to the router,|Он не отображается там, потому что этот порт подключен к маршрутизатору,
router is not on.|роутер не включен.
So therefore,|Так что,
we not gonna be able to see it so that's the first thing I wanted to check.|мы не сможем его увидеть, так что это первое, что я хотел проверить.
I wanted to make sure that these three were trumped.|Я хотел убедиться, что этих троих превзойдут.
Why is that, why is that, because only the native VLAN, admin VLAN, management VLAN.|Почему это так, потому что только собственная VLAN, административная VLAN, управляющая VLAN.
Whatever you want to call it is the only one that can go across access ports or trunk ports and we proved that already in|Как бы вы ни называли, это единственный, который может проходить через порты доступа или транковые порты, и мы уже доказали, что
lab that we did.|лаборатория, которую мы сделали.
So, since we have VLAN, what is this VLAN 10 and VLAN 20 right here, they must go across trunk ports that are trunked, in|Итак, поскольку у нас есть VLAN, что это за VLAN 10 и VLAN 20, они должны проходить через транковые порты, в
order to get from one side to the next.|чтобы попасть с одной стороны на другую.
So we need to go into our router, all right?|Итак, нам нужно войти в наш роутер, хорошо?
So we gonna click on our router there and let's maximize it.|Итак, мы нажмем на наш роутер и увеличим его.
Let's maximize it, very good.|Давайте увеличим его, очень хорошо.
Now we just give them over, we're not gonna configure too many things on here.|Теперь мы просто передадим их, мы не собираемся настраивать здесь слишком много вещей.
Let's just give it a name.|Давай просто дадим ему имя.
HOSTNAME, very generic R1, lets capitalize that.|HOSTNAME, очень общий R1, позволяет использовать это с большой буквы.
Now, we'll have to go into the physical interface.|Теперь нам нужно перейти к физическому интерфейсу.
INT F0/1, oops 0, sorry, Enter.|INT F0 / 1, ой 0, извините, Enter.
We don't need to put an IP address.|Нам не нужно указывать IP-адрес.
We do not need to know how to put in an IP address on this F0/0 because you can't.|Нам не нужно знать, как ввести IP-адрес в этот F0 / 0, потому что вы не можете.
You can't put 2 or 3, or 4, or 100 that's why we create sub interfaces.|Вы не можете поставить 2 или 3, или 4, или 100, поэтому мы создаем субинтерфейсы.
So all we need to do here is no shut it.|Так что все, что нам нужно сделать, это не закрывать глаза.
Turn it on and now I'm gonna up arrow and create my first sub interface.|Включите его, и теперь я собираюсь стрелкой вверх и создавать свой первый вспомогательный интерфейс.
I'm gonna do .10 for VLAN10, is that a requirement?|Я сделаю .10 для VLAN10, это требование?
Do you have to name the sub interface the same as your VLAN ID?|Нужно ли называть подчиненный интерфейс таким же, как ваш идентификатор VLAN?
No, you do not but does it make sense?|Нет, нет, но есть ли в этом смысл?
If you have VLAN10 to put VLAN, I don't know, 113 or sub interface 113?|Если у вас есть VLAN10, чтобы поставить VLAN, я не знаю, 113 или субинтерфейс 113?
That makes no sense.|Это не имеет смысла.
So visualization, so when you look a sub interface, you know what VLAN it belongs to.|Итак, визуализация, когда вы смотрите на субинтерфейс, вы знаете, к какой VLAN он принадлежит.
So just a little common sense boys and girls, all right?|Так что немного здравого смысла, мальчики и девочки, хорошо?
Now we do the encapsulation.|Теперь делаем инкапсуляцию.
ENCAP DOT1Q 10, this must match,|ENCAP DOT1Q 10, это должно совпадать,
this number right here must, must,|этот номер здесь должен, должен,
requirement, must match the VLAN that you wanna talk to.|требование, должно соответствовать VLAN, с которой вы хотите поговорить.
So the, the both size, the VLAN ID.|Итак, оба размера, идентификатор VLAN.
The VLAN do you wanna talk to?|VLAN, с которой вы хотите поговорить?
So if you want to talk, if this is gonna be for VLAN10 then that encapsulation must be 10 if not, it's not gonna work.|Итак, если вы хотите поговорить, если это будет для VLAN10, тогда эта инкапсуляция должна быть 10, если нет, это не сработает.
That is required, the subnet of it's not,|Это необходимо, подсеть в нем нет,
as far as the numbering but when it comes to encapsulation, yes, it does.|что касается нумерации, но когда дело доходит до инкапсуляции, да, это так.
So now what do we do?|Итак, что нам теперь делать?
We put the IP scheme for the IP address for that particular VLAN.|Мы помещаем схему IP для IP-адреса для этой конкретной VLAN.
IP address, you know what I just I forgot the oh, 192.168, okay.|IP-адрес, вы знаете, я просто забыл о 192.168, хорошо.
[BLANK_AUDIO]|[BLANK_AUDIO]
Where am I?|Где я?
Okay, 192.168.10.254.|Хорошо, 192.168.10.254.
255.255.255.0, Enter.|255.255.255.0, введите.
No need to do a no shut.|Нет необходимости делать закрытие.
Subinterfaces are already on.|Подинтерфейсы уже включены.
You saw that it did turn on once you go ahead and create it.|Вы видели, что он действительно включился, когда вы его создали.
Now let's go to the next subinterface.|Теперь перейдем к следующему подинтерфейсу.
I want to opt out, just to make things speedy, go to the sub interface and now the next VLAN is 20, so hey,|Я хочу отказаться, просто чтобы ускорить процесс, перейдите во вспомогательный интерфейс, и теперь следующая VLAN - 20, так что привет,
interface, sub interface 20.|интерфейс, подчиненный интерфейс 20.
All right, you see it goes up, the encapsulation must mach the VLAN ID, 20 and now the IP address.|Хорошо, вы видите, что он идет вверх, инкапсуляция должна соответствовать идентификатору VLAN 20, а теперь и IP-адресу.
Yes, I am getting very lazy, [INAUDIBLE]|Да, я становлюсь очень ленивым, [НЕРАЗБОРЧИВО]
for everything.|За все.
You cannot do that in this replication,|Вы не можете этого сделать в этой репликации,
okay?|Ладно?
20, Ctrl+Z, WR or exit, exit, copy around start, enter, enter.|20, Ctrl + Z, WR или выход, выход, копирование с начала, ввод, ввод.
I'm gonna do a show IP INT BRIEF.|Я собираюсь устроить шоу IP INT BRIEF.
Please remember these commands, all right?|Пожалуйста, запомните эти команды, хорошо?
So you come here, you got your sub interfaces 10 and 20,|Итак, вы пришли сюда, у вас есть субинтерфейсы 10 и 20,
for VLAN's 10 and 20.|для VLAN 10 и 20.
You see you have the different gateways and it shows up, up.|Вы видите, что у вас разные шлюзы, и он появляется.
Outstanding, you look at your routing tables, show IP ROUTE.|Отлично, вы смотрите в свои таблицы маршрутизации, показываете IP ROUTE.
To look at your routing table and you see that you're connected to those particular networks.|Взглянуть на свою таблицу маршрутизации и увидеть, что вы подключены к этим конкретным сетям.
Oops, three is not oh, okay.|Ой, три - это не так.
All right, there you go.|Хорошо, вот так.
So it should work at this point, so let's see if we do have IPs on all our PCs.|Так что на данном этапе это должно работать, поэтому давайте посмотрим, есть ли у нас IP-адреса на всех наших компьютерах.
I don't want to click on, just wanna, no,|Я не хочу нажимать, просто хочу, нет,
we do not and that's like me.|у нас нет и это похоже на меня.
[LAUGH] All right, let's go to the desktop.|[СМЕХ] Хорошо, перейдем к рабочему столу.
Put some IPs on here.|Поместите сюда несколько IP-адресов.
This is for the 20, so 192.168.20.1, tab,|Это для 20, поэтому 192.168.20.1, вкладка,
tab using default here.|здесь используется вкладка по умолчанию.
192.168.20.254, close,|192.168.20.254, закрыть,
close, let's do for the 10, same thing.|близко, давайте сделаем на 10, тоже самое.
All right, got you over there.|Хорошо, ты там.
You guys can see that 192.168.10.1 tab,|Ребята, вы видите вкладку 192.168.10.1,
tab.|таб.
192.168.10.254, all right.|192.168.10.254, хорошо.
Now let's take a look back at that switch,|Теперь давайте посмотрим на этот переключатель,
the core switch that we did the show in trunk and nothing came up.|основной переключатель, который мы показывали в багажнике, и ничего не подошло.
Oh, only the two ports came up, actually.|О, на самом деле подошли только два порта.
Let's do it again, up arrow shown in trunk there it is.|Давайте сделаем это снова, стрелка вверх, показанная в багажнике, вот она.
Now you can see 24 but it's using the 8021q.|Теперь вы видите 24, но он использует 8021q.
Cool, all right.|Круто, хорошо.
So we know that that's okay, so we should be able to route.|Итак, мы знаем, что это нормально, поэтому у нас должна быть возможность маршрутизировать.
I should go to ping PC2 or student PC and so forth.|Я должен пойти на ping PC2 или ученический компьютер и так далее.
All right so, oops, oh that's very interesting.|Ладно, ой, это очень интересно.
Okay,|Ладно,
[BLANK_AUDIO]|[BLANK_AUDIO]
Let's put this over here so you guys can see it.|Давайте поместим это сюда, чтобы вы, ребята, это увидели.
Let's ping 192.168.20.1 and let's see what happens.|Пингуем 192.168.20.1 и посмотрим, что получится.
Remember your ARP is always gonna be the first thing.|Помните, что ваш ARP всегда будет первым.
Remember what's going on it's not going through the switch.|Помните, что происходит, он не проходит через переключатель.
It's going up the switch, through the router and then back down again and we did it again, let's do it again so we get the full replies.|Он идет вверх по коммутатору, через маршрутизатор, а затем снова вниз, и мы сделали это снова, давайте сделаем это снова, чтобы получить полные ответы.
So now we have InterVLAN connectivity.|Итак, теперь у нас есть возможность подключения к InterVLAN.
Now, VLAN10 can talk to VLAN20 and that is the kind of, the kind of configuration that they want you to know.|Теперь VLAN10 может взаимодействовать с VLAN20, и они хотят, чтобы вы знали именно такую ​​конфигурацию.
They want you to know the encapsulation type which is gonna be 8021q.|Они хотят, чтобы вы знали тип инкапсуляции, которым будет 8021q.
They want you to know that the encapsulation must match.|Они хотят, чтобы вы знали, что инкапсуляция должна совпадать.
The DOT 1q must match the VLAN ID.|DOT 1q должен соответствовать идентификатору VLAN.
The ID is created under sub interfaces and what else, yeah,|Идентификатор создается под подчиненными интерфейсами и что еще, да,
sub interfaces and you put the IP address for that particular gateway that's it.|sub интерфейсы, и вы вводите IP-адрес для этого конкретного шлюза.
That's it but trust me in the next lesson,|Вот и все, но поверьте мне на следующем уроке,
you're gonna get a big review of everything we've done with the spanning tree, with the trunking, with VTP.|вы получите подробный обзор всего, что мы сделали с остовным деревом, с транкингом, с VTP.
All that creating the VLAN's, all that stuff, all over again in a much bigger lab with more, a lot more subnets, so repetition breeds retention.|Все это создание виртуальных локальных сетей, все это снова и снова в гораздо более крупной лаборатории с большим количеством подсетей, поэтому повторение порождает удержание.
Now, you can do the same thing if you have the packet tracer,|Теперь вы можете сделать то же самое, если у вас есть трассировщик пакетов,
you can create your own labs.|вы можете создавать свои собственные лаборатории.
It doesn't necessarily have to be exactly like mine.|Он не обязательно должен быть таким же, как у меня.
Start putting switches out there, start putting routers out there.|Начните ставить переключатели там, начните ставить там маршрутизаторы.
Start creating VLANs and then do your sub interfaces, all right?|Начните создавать сети VLAN, а затем займитесь своими подчиненными интерфейсами, хорошо?
You can do that as well.|Вы тоже можете это сделать.
All right guys and gals, I'll see you in the next lesson.|Хорошо, парни и девушки, увидимся на следующем уроке.
[BLANK_AUDIO]|[BLANK_AUDIO]