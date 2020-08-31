D:\mailCloud\prjother\tmp\1\c80_Navigation on a switch and show commands.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
All right.|Отлично.
Welcome back, everyone.|С возвращением, все.
Now that we understand that we need switches in our network,|Теперь, когда мы понимаем, что нам нужны коммутаторы в нашей сети,
we need to learn how to navigate to our switches.|нам нужно научиться переходить к нашим переключателям.
We obviously, when we buy a switch, let's say, from Cisco,|Очевидно, что когда мы покупаем коммутатор, скажем, у Cisco,
where else are we gonna get them?|где еще мы их возьмем?
We, they, they may be blank, completely blank.|Мы, они, они могут быть пустыми, совершенно пустыми.
So you have to counsel in just like you would counsel in into a router.|Таким образом, вы должны консультироваться так же, как если бы вы консультировали маршрутизатор.
Or they can be preconfigured and they may have the ACP enable and you get an IP address and you connect to it, what have you.|Или они могут быть предварительно настроены, и у них может быть включен ACP, и вы получаете IP-адрес и подключаетесь к нему, что у вас есть.
But we're gonna pretend that we counseled in this switch is completely blank,|Но мы собираемся сделать вид, что мы советовали, что этот переключатель полностью пуст,
there's nothing in there.|там ничего нет.
So we've consoled into the switch right now using putty or whatever program that you use and then we're inside the switch.|Итак, мы успокоились в переключателе прямо сейчас, используя замазку или любую другую программу, которую вы используете, а затем мы внутри переключателя.
And as in the router, here we have user mode.|Как и в роутере, здесь есть пользовательский режим.
Same thing, we'll go ENABLE.|То же самое, пойдем ВКЛЮЧИТЬ.
That takes us to privileged mode and then we'll do CONFIG T.|Это переведет нас в привилегированный режим, а затем мы выполним CONFIG T.
That'll take us to global configuration.|Это приведет нас к глобальной конфигурации.
And that's where we start typing all the host themes and IP domain lookups, and the passwords and all that stuff.|И именно здесь мы начинаем вводить все темы хостов и поисковые запросы IP-домена, а также пароли и все такое.
We also have our LINE CON zeros.|У нас также есть нули LINE CON.
Right?|Правильно?
A line.|Линия.
Line VTYs.|Линия VTYs.
All that, same, same, same exact thing that we've done in the router,|Все то же самое, то же самое, что мы сделали в роутере,
we're probably going to do here as well.|мы, вероятно, собираемся поступить и здесь.
All those configurations, you can see the administrative commands.|Все эти конфигурации вы можете увидеть с помощью административных команд.
The, the housekeeping commands that I like to call.|Команды по ведению домашнего хозяйства, которые я люблю называть.
Now the things that were a little bit different is when we put an IP address on the switch,|Теперь немного по-другому, когда мы добавляем IP-адрес на коммутатор,
the IP address will be putting it Inside int VLAN one.|IP-адрес будет помещен внутрь int VLAN one.
It shows like, if it was an actual interface.|Это показывает, как если бы это был реальный интерфейс.
There, we will put the IP address and turn on VLAN one, so we can access.|Там мы поместим IP-адрес и включим VLAN one, чтобы мы могли получить доступ.
Because VLAN one by default is your native VLAN, so the native VLAN is meant for the IT people.|Поскольку VLAN один по умолчанию является вашей собственной VLAN, поэтому собственная VLAN предназначена для ИТ-специалистов.
The admin people that are going to manage this particular switch.|Администраторы, которые будут управлять этим переключателем.
So, if we leave VLAN1 as the native VLAN,|Итак, если мы оставим VLAN1 в качестве собственной VLAN,
we want to put an IP address on there.|мы хотим поместить туда IP-адрес.
Funny enough, the default gateway is outside VLAN one.|Как ни странно, шлюз по умолчанию находится за пределами VLAN one.
It's on global configuration.|Это глобальная конфигурация.
But again, we'll go through the configurations and you'll get to see all that.|Но опять же, мы рассмотрим конфигурации, и вы все это увидите.
All right?|Отлично?
But most importantly,|Но самое главное,
I mean, definitely, you need to know how to navigate through here.|Я имею в виду, что вам определенно нужно знать, как ориентироваться здесь.
You can go inside, in VLAN one, you can go inside interface F0/1.|Можно зайти внутрь, в VLAN one, можно зайти внутрь интерфейса F0 / 1.
Right?|Правильно?
Why would you wanna go inside an interface?|Зачем вам нужен интерфейс?
The, the reasons that we go inside interfaces are to put port security,|Причины, по которым мы заходим внутрь интерфейсов, - это обеспечение безопасности порта,
are to assign VLANs.|должны назначать VLAN.
All right?|Отлично?
To deal with spanning tree, okay?|Чтобы иметь дело с остовным деревом, хорошо?
So these are the things that we do within interfaces or, or a range of interfaces and we'll show you how to do range commands, you can do a lot|Итак, это то, что мы делаем в интерфейсах или, или в ряде интерфейсов, и мы покажем вам, как выполнять команды диапазона, вы можете многое
more than just one to trunk certain ports and we'll talk about trunking, as well.|больше, чем один для транкинга определенных портов, и мы также поговорим о транкинге.
All right.|Отлично.
But definitely, you need to know how to get inside there.|Но обязательно нужно знать, как туда попасть.
But more importantly, these show commands.|Но что более важно, эти команды show.
Obviously, when you get to the test it's either show run or show start and there's now start up right now.|Очевидно, что когда вы переходите к тесту, это либо шоу-запуск, либо шоу-запуск, а теперь запускается прямо сейчас.
If I were to do show start, it would say,|Если бы я начал шоу, он бы сказал:
start config is not present, because we,|start config отсутствует, потому что мы,
is a blank switch.|это пустой переключатель.
But I will do a show one and you can see what's there already,|Но я сделаю шоу, и вы уже увидите, что там,
you can see all of the interfaces that are there.|вы можете увидеть все интерфейсы, которые там есть.
All right.|Отлично.
Make sure you have 24 ports, all right?|Убедитесь, что у вас 24 порта, хорошо?
And then you have, you see that interface VLN one has no IP address and it shut down, so you need to turn it on.|А потом вы видите, что у интерфейса VLN one нет IP-адреса, и он отключился, поэтому вам нужно включить его.
There's our con, there's our VTY lines.|Вот и наш мошенник, вот и наши линии VTY.
So there's your are, and there's how you can look at everything in one shot.|Итак, вот ваша сущность, и вот как вы можете увидеть все в одном кадре.
You can also do a show VLAN, which we've done before,|Вы также можете сделать демонстрацию VLAN, которую мы делали раньше,
you can see how many VLANs are on there.|вы можете увидеть, сколько там VLAN.
All right?|Отлично?
And what port assignments those ports belong to.|И какому назначению портов принадлежат эти порты.
So you see your VLANs here, you see what ports are assigned to that particular VLAN, when they're active on that VLAN.|Итак, вы видите здесь свои VLAN, вы видите, какие порты назначены этой конкретной VLAN, когда они активны в этой VLAN.
And right now, all ports are active on VLAN one.|И прямо сейчас все порты в VLAN one активны.
So show VLAN is an important command to know.|Итак, show VLAN - важная команда, которую необходимо знать.
The other one is show VTP, virtual trunking protocol.|Другой - показать VTP, протокол виртуального транкинга.
Show VTP status, all right?|Показать статус VTP, хорошо?
Once we get to that particular section in the course, I will explain VTP and it's kind of interesting, cuz in the new,|Как только мы перейдем к этому конкретному разделу курса, я объясню VTP, и это будет интересно, потому что в новом
in the newer book,|в новой книге,
they rarely mention VTP, but it's it is a,|они редко упоминают VTP, но это,
a big part of your certification.|большая часть вашей сертификации.
So you need to understand about the revision number, all right?|Значит, вам нужно знать номер ревизии, понятно?
This is important.|Это важно.
This revision number right here.|Этот номер ревизии прямо здесь.
The operating mode by default.|Режим работы по умолчанию.
They're all servers.|Все они серверы.
You need to understand, hey, I was just modified by who?|Ты должен понять, эй, кто меня только что модифицировал?
All right.|Отлично.
The IP address.|IP-адрес.
So these are things that you'll be looking at, if you have a VTP domain name.|Вот на что вы будете обращать внимание, если у вас есть доменное имя VTP.
Right?|Правильно?
That will show up here.|Это будет здесь.
Right now, we do not, we will eventually.|Прямо сейчас мы этого не делаем, мы обязательно сделаем это.
All right.|Отлично.
So this is an extremely important command.|Так что это чрезвычайно важная команда.
We've seen the [UNKNOWN] command, which is show and then let me type it out for you.|Мы видели команду [UNKNOWN], которая отображается, и я могу напечатать ее для вас.
Show Mac-ADDRESS-TABLE.|Покажите Mac-ADDRESS-TABLE.
Now, one of the things that my students come back to me and they tell me,|Одна из вещей, которые мои ученики возвращаются ко мне и говорят мне,
hey, Laz, I tried typing MAC-ADDRESS-TABLE and it didn't work.|эй, Лаз, я попробовал набрать MAC-ADDRESS-TABLE, и это не сработало.
I say, and my response to that, did you try doing it without the hyphens?|Я говорю, и мой ответ на это, вы пробовали делать это без дефисов?
And they're like, well, no.|И они такие, ну нет.
Well, then, why?|Тогда почему?
It's a program.|Это программа.
Regardless of, you're not doing it on real live equipment,|Независимо от того, вы делаете это не на реальном живом оборудовании,
you're doing it on a simulator, just like you would in a packet tracer.|вы делаете это на симуляторе, точно так же, как в пакетном трассировщике.
So whoever programmed it, if you know that we're doing a show MAC-ADDRESS-TABLE and that's the way you would do it.|Итак, кто бы это ни программировал, если вы знаете, что мы делаем шоу MAC-ADDRESS-TABLE, и вы бы сделали это именно так.
That's the way you would do it on a real switch, but is not working in a similar do it without the hyphens.|Таким образом вы бы сделали это на реальном коммутаторе, но не работает в аналогичном режиме без дефисов.
Show MAC, space, address, space table,|Показать MAC, пространство, адрес, таблицу пространств,
Enter.|Войти.
Okay?|Ладно?
And that will show you the MAC-ADDRESS-TABLE and you need to know that, because you may get a question that says,|И это покажет вам MAC-ADDRESS-TABLE, и вам нужно это знать, потому что вы можете получить вопрос, который говорит:
hey this MAC address, what port is it assigned too?|эй, этот MAC-адрес, какой порт ему тоже назначен?
Show MAC-ADDRESS-TABLE and then you can see right there,|Покажите ТАБЛИЦУ MAC-АДРЕСОВ, и вы сразу увидите,
that MAC-ADDRESS-TABLE's assigned to whatever port.|что MAC-ADDRESS-TABLE назначен любому порту.
So that is an important command.|Так что это важная команда.
Again, you got show run, show start, show VLAN, show VTP status.|Опять же, у вас есть показывать запуск, показывать старт, показывать VLAN, показывать статус VTP.
All right?|Отлично?
And we did show MAC-ADDRESS-TABLE.|И мы показали MAC-ADDRESS-TABLE.
Show INT, short for interface, TRUNK.|Показать INT, сокращение от интерфейса, TRUNK.
Obviously, we have no trunk port that will show you all the ports that are trunked,|Очевидно, у нас нет транкового порта, который бы показал вам все транковые порты,
so you know what they are.|чтобы вы знали, что они из себя представляют.
Okay.|Ладно.
And let me see what else, what else, what else.|И позвольте мне посмотреть, что еще, что еще, что еще.
Well, you know, the show CDP neighbor.|Ну, знаете, по шоу CDP сосед.
Right?|Правильно?
There's no neighbors right now or show CDP neighbor detail.|Сейчас нет соседей или показать детали соседей CDP.
There's nothing to see, that's two very important commands.|Здесь не на что смотреть, это две очень важные команды.
These commands that I am showing you right now will recreate our infrastructure and we will, all right?|Эти команды, которые я вам сейчас показываю, воссоздают нашу инфраструктуру, и мы это сделаем, хорошо?
You need to know these commands, these commands I'm giving you right now.|Вам нужно знать эти команды, эти команды, которые я даю вам прямо сейчас.
Hint, hint, hint.|Подсказка, подсказка, подсказка.
Write them down, all right?|Запишите их, хорошо?
These are the commands that you are gonna be using, all right?|Это команды, которые вы собираетесь использовать, хорошо?
So you need to know what they do and how they are.|Поэтому вам нужно знать, что они делают и каковы они.
And again, as we go through the configurations,|И снова, когда мы проходим настройки,
I will show you how to do that.|Я покажу вам, как это сделать.
But again, the navigation of a switch is very simple and these are the basic commands that you will use.|Но опять же, навигация переключателя очень проста, и это основные команды, которые вы будете использовать.
When I go and let's say, I'm troubleshooting a switch to a student or anywhere.|Когда я иду и, скажем так, я устраняю проблемы с переключением на студента или где-нибудь еще.
One of the first things that I do is, you know, depending, obviously.|Одно из первых, что я делаю, это, знаете ли, очевидно.
Show start.|Показать начало.
Because if it's a huge switch,|Потому что если это огромный переключатель,
I wanna make sure that I don't bog down the switch.|Я хочу быть уверенным, что не переверну выключатель.
I can do a pipe command, whatever.|Я могу выполнить команду канала, что угодно.
But in the CCNA certification, you're gonna have thousands of interfaces.|Но в сертификации CCNA у вас будут тысячи интерфейсов.
Nothing like that.|Ничего подобного.
So you're gonna do a show start or a show run, alright?|Так ты собираешься начать шоу или провести шоу, хорошо?
Or I can do a show PORT, if they're doing PORT-security or their show PORT-security.|Или я могу сделать шоу PORT, если они занимаются PORT-security или их шоу PORT-security.
All right.|Отлично.
For any violations.|За любые нарушения.
I can do a show SPAnning-tree, show SPAnning-tree.|Я могу сделать шоу SPAnning-tree, показать SPAnning-tree.
All right?|Отлично?
You gonna start getting familiar with this screen big time, big time, big time.|Вы начнете знакомиться с этим экраном по-крупному, с большим разом, с большим разом.
All right.|Отлично.
So, I will show, I will break this screen down to you,|Итак, я покажу, я вам этот экран разобью,
just like I will break down the VTP string down to you.|точно так же, как я передам вам строку VTP.
So you understand what that's telling you and the VTP status, all those things.|Итак, вы понимаете, о чем это вам говорит, и о статусе VTP, и обо всем этом.
All those print screens, you need to be aware of.|Вы должны знать обо всех этих экранах печати.
All right?|Отлично?
The most difficult part in switching that I've seen the students it has,|Самая сложная часть переключения, которую я видел у студентов, - это
it has been with SPAnning-tree.|это было с SPAnning-tree.
Not because it's that difficult to understand,|Не потому, что это так сложно понять,
it's just the port assignments can be a little tricky.|просто назначение портов может быть немного сложным.
But I'll show you how to get to it in a very simple, simple method.|Но я покажу вам, как добраться до него очень простым и простым способом.
You know me.|Ты меня знаешь.
Me and math don't get along, even though I have a periodic table in front of me,|Я и математика не ладим, хотя передо мной таблица Менделеева,
you know, in front of you.|знаете, перед вами.
Me and math do not get along.|Я и математика не ладят.
So, I try and do things as easy as that way it's possible.|Итак, я стараюсь делать вещи настолько простыми, насколько это возможно.
So let's see, let's run down the commands.|Итак, давайте посмотрим, давайте запустим команды.
Let me open up a Notepad and let's run down the commands.|Позвольте мне открыть Блокнот и выполнить команды.
Okay?|Ладно?
So let's do a show run, let's say, or a show start, whichever one.|Итак, давайте устроим шоу-забег, скажем, или начало шоу, в зависимости от того, что.
Flash start, either or.|Флэш-старт, либо или.
We know the difference, right?|Мы знаем разницу, правда?
One's in RAM, one's in MV RAM.|Один в RAM, другой в MV RAM.
Then we do a show MAC-ADDRESS-TABLE,|Затем мы показываем MAC-ADDRESS-TABLE,
right?|право?
It shows you the ports that are assigned.|Он показывает вам назначенные порты.
The Mac addresses, they're assigned to what ports.|Адреса Mac, каким портам они назначены.
Okay?|Ладно?
Then you have show VLAN.|Тогда у вас есть показать VLAN.
It'll show you all the VLANs that exist within your switch.|Он покажет вам все VLAN, существующие в вашем коммутаторе.
You have the show VTP status, which is virtual trunking protocol not to be confused with trunk ports.|У вас есть статус показа VTP, который представляет собой протокол виртуального транкинга, который не следует путать с портами транка.
Trunking a port and the vi,|Транкинг порта и vi,
and the virtual trunking protocol are two separate things.|и протокол виртуального транкинга - это две разные вещи.
They are not the same, okay?|Они не такие, да?
Two separate things.|Две разные вещи.
You have show INT TRUNK, which is short for interface.|У вас есть показать INT TRUNK, что является сокращением от интерфейса.
I'll type it out, show INTERFACE TRUNK.|Я его напечатаю, покажу ИНТЕРФЕЙС БАГАЖНИК.
All right?|Отлично?
That lets you know, hey, which ports are trunk.|Это позволяет узнать, какие порты являются магистральными.
And when we get to that particular lesson,|И когда мы переходим к этому конкретному уроку,
when we start trunking ports,|когда мы начинаем транкинг портов,
I'll tell you the importance of trunking ports.|Я скажу вам важность транкинга портов.
Okay.|Ладно.
Because you have access ports and you have trunk ports.|Потому что у вас есть порты доступа и магистральные порты.
Okay?|Ладно?
What's the other one?|Что еще?
Oh, show spanning tree, definitely.|О, определенно покажите остовное дерево.
Show SPANNING-TREE.|Покажите ДЕРЕВО.
You need to be aware.|Вы должны быть в курсе.
All those all, these right here are very,|Все эти все, вот они, очень,
very important commands that you really need to be aware of.|очень важные команды, о которых вам действительно нужно знать.
Let me see, show MAC-ADDRESS-TABLE, show VLAN, show VTP status,|Позвольте мне посмотреть, показать MAC-ADDRESS-TABLE, показать VLAN, показать статус VTP,
show INTERFACE TRUNK, show SPANNING-TREE.|показать ИНТЕРФЕЙС БАГАЖНИК, показать SPANNING-TREE.
Obviously, the same things we did here on the,|Очевидно, то же самое, что и здесь, на
on the router, which was show CDP NEIGHBOR.|на роутере, на котором был показан CDP NEIGHBOR.
Oh, NEIGHBOR OR show CDP NEIGHBOR details.|О, СОСЕД ИЛИ покажите подробности о CDP NEIGHBOR.
Right?|Правильно?
Cuz you wanna look at who your neighbors are.|Потому что ты хочешь посмотреть, кто твои соседи.
Is it a switch?|Это переключатель?
Is it a router?|Это роутер?
What platform are they using?|Какую платформу они используют?
What IP address are they using?|Какой IP-адрес они используют?
Maybe by the IP address, you can, you know, conclude, hey, why do VTP neighbor?|Может быть, по IP-адресу вы можете сделать вывод, эй, а почему VTP соседствует?
I do show VTP status, right?|Я показываю статус VTP, верно?
I get who just updated me and then I say,|Я понимаю, кто только что обновил меня, и говорю:
okay, that's the IP address.|хорошо, это IP-адрес.
Okay.|Ладно.
That's show VTP status.|Это показывает статус VTP.
I see the IP address they just updated me.|Я вижу IP-адрес, который мне только что обновили.
Great.|Отлично.
Now, I'm gonna do show CDP NEIGHBOR DETAIL and I'm gonna match up those IP address,|А теперь я покажу ДЕТАЛИ СОСЕДА CDP и сопоставлю эти IP-адреса,
so I can get the name of the person that just updated me.|так что я могу узнать имя человека, который только что обновил меня.
So this is how you would use these commands and believe me ladies and gentlemen, you will be confronting these commands, all right?|Итак, вот как вы будете использовать эти команды и поверьте мне, дамы и господа, вы будете противостоять этим командам, хорошо?
When you do your layer two and another thing that I wanna drill on.|Когда вы делаете второй слой и еще одну вещь, которую я хочу продолжить.
This test, the CCNA,|Этот тест, CCNA,
deals with layer two switching.|имеет дело с переключением второго уровня.
A lot of students tell me, Laz, I have layer three and that's great,|Многие студенты говорят мне, Лаз, у меня третий слой, и это здорово,
great news for you guys.|отличные новости для вас, ребята.
Awesome.|Потрясающие.
But guess what?|Но знаете что?
This is not a layer three switch, this is layer two switching.|Это не переключатель третьего уровня, это переключение второго уровня.
Why?|Зачем?
I don't know.|Я не знаю.
There's a saying that goes, ours is not to question why, just to do or die.|Есть такая поговорка, наша не спрашивать почему, просто делать или умереть.
Right?|Правильно?
So we just need to, need to understand that when we take this test is a layer two switch.|Поэтому нам просто нужно, нужно понимать, что когда мы проводим этот тест, это переключатель второго уровня.
Period.|Период.
Focus on that.|Сосредоточьтесь на этом.
Once you get your CCNA certification, they can do whatever you want, but you need that piece of paper.|Как только вы получите сертификат CCNA, они смогут делать все, что захотите, но вам понадобится этот лист бумаги.
So learn the information that is required that I'm giving you and that you're researching out there, so you can pass the certification.|Так что изучите информацию, которая требуется, которую я вам даю и которую вы исследуете, чтобы вы могли пройти сертификацию.
All right?|Отлично?
If you're listening to what I'm telling you, if you follow these commands and you learn these commands and as we go through the configurations,|Если вы слушаете то, что я вам говорю, если вы будете следовать этим командам и выучите эти команды, и по мере того, как мы будем проходить через конфигурации,
you will get to understand them and use them, then you'll be all right for the switching part of the course and it's really not that bad.|вы научитесь их понимать и использовать, тогда вы будете в порядке для сменной части курса, и это действительно не так уж и плохо.
It really isn't.|На самом деле это не так.
I just takes practice, just like anything.|Я просто практикуюсь, как и все остальное.
You need to be practicing, practicing,|Вам нужно практиковаться, практиковаться,
practicing, practicing everyday.|практика, практика каждый день.
So, again, navigation through the switch,|Итак, снова навигация через переключатель,
pretty much the same as the router.|примерно так же, как маршрутизатор.
No big deal.|Ничего страшного.
Enable, config T, line column zero,|Включить, настроить T, нулевой столбец строки,
interface interface VLAN or interface F0 whatever.|interface interface VLAN или интерфейс F0 как угодно.
All right?|Отлично?
So not a big deal, all right?|Так что ничего страшного, понятно?
The show commands is what I'm more concerned about.|Меня больше беспокоят команды show.
The configuration, you guys got it.|Конфигурация, вы поняли.
That's no big deal.|В этом нет ничего страшного.
[SOUND] I got this.|[ЗВУК] Я понял.
You're gonna be bored after a while, cuz it's gonna be configuring, configuring,|Через некоторое время вам станет скучно, потому что это будет настройка, настройка,
configuring.|настройка.
It's like, my God, how many times are we gonna do this?|Боже мой, сколько раз мы будем это делать?
All right?|Отлично?
But it's, it's repetition breeds retention.|Но это повторение порождает удержание.
Repetition breeds retention.|Повторение порождает удержание.
All right?|Отлично?
These things need to become second nature to you.|Эти вещи должны стать для вас второй натурой.
Okay?|Ладно?
And the show commands are really, really important.|И команды show действительно очень важны.
Just like in the routing, when we did the show IP EIGRP topology to take a look at the topology table or did the show IP OSPF|Как и в случае с маршрутизацией, когда мы показывали топологию IP EIGRP, чтобы взглянуть на таблицу топологии, или показывали IP OSPF
interface and we looked at the interface to see the priority numbers and all that.|интерфейс, и мы посмотрели на интерфейс, чтобы увидеть номера приоритетов и все такое.
Well, the same thing goes for the switches.|То же самое и с переключателями.
We need to understand the show command, so we know what we're looking at.|Нам нужно понимать команду show, чтобы знать, на что мы смотрим.
Okay?|Ладно?
All right.|Отлично.
So navigation, you know it.|Итак, навигация, вы это знаете.
There's your commands right there.|Вот ваши команды прямо здесь.
Make sure you know it, okay?|Убедитесь, что вы это знаете, хорошо?
So, I guess, I'll be seeing you in the next lesson, so we can start doing some configurations.|Итак, я думаю, я увижу вас на следующем уроке, чтобы мы могли приступить к настройке.
[BLANK_AUDIO]|[BLANK_AUDIO]