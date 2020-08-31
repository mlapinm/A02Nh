D:\mailCloud\prjother\tmp\1\c64_using the CDP command.md  


__|__
--|--
Welcome back.|Добро пожаловать.
No, I'm not going to sing.|Нет, я не буду петь.
I want you, I want you watching the course.|Я хочу, чтобы ты смотрел курс.
Very short lesson, very important lesson.|Очень короткий урок, очень важный урок.
This is gonna deal with the Cisco discovery protocol, all right.|Это будет иметь дело с протоколом обнаружения Cisco, хорошо.
You need, you will be using the Cisco discovery protocol in I believe in your switch simulation, according to my students that have taken the examination.|Вам нужно, вы будете использовать протокол обнаружения Cisco в моделировании коммутатора, как утверждают мои студенты, сдавшие экзамен.
That's one of the commands that they had to, to type.|Это одна из команд, которую они должны были ввести.
All right, are the two commands that you're gonna learn today.|Хорошо, это две команды, которые вы выучите сегодня.
So you need to understand if they give you a print screen of the show CDP neighbor or show CDP neighbor detail or if you need to type it, what exactly is it|Итак, вам нужно понять, дают ли они вам экран печати соседа шоу CDP или показывают детали соседа CDP, или если вам нужно его ввести, что именно
that you're looking at.|что вы смотрите.
Now, obviously the name itself tells you it is a Cisco invented protocol, right, cuz it's called discovery protocol.|Очевидно, само название говорит вам, что это протокол, изобретенный Cisco, потому что он называется протоколом обнаружения.
And what it does, it goes out, sends out little hellos.|И то, что он делает, гаснет, передает небольшие приветы.
And it it finds its neighbors.|И он находит своих соседей.
It sees who is directly connected to.|Он видит, с кем напрямую связан.
That's what it does.|Вот что он делает.
That's it.|Вот и все.
That's what it does.|Вот что он делает.
To see who is connected to, your book makes a real world scenario where if you had to actually create a map of your network, you can actually.|Чтобы увидеть, с кем связан, ваша книга представляет собой сценарий реального мира, в котором, если бы вам действительно пришлось создать карту своей сети, вы действительно могли бы это сделать.
I'm saying actually one too many times.|Я говорю на самом деле слишком много раз.
You can see, you can create the the map of your network.|Как видите, вы можете создать карту своей сети.
If you had to do that and it's a large enterprise, I'm sorry for you.|Если вам пришлось это сделать, а это большое предприятие, мне вас жаль.
All right, please get some third-party software.|Хорошо, пожалуйста, установите стороннее программное обеспечение.
But for your testing purposes,|Но для целей тестирования
you can use the show CDP neighbor or show CDP more detail.|вы можете использовать команду show CDP neighbour или показать CDP более подробно.
So let's go to router one, and we'll maximize that.|Итак, давайте перейдем к маршрутизатору один, и мы его максимально увеличим.
And let's log in again.|И давайте снова авторизуемся.
Cisco.|Cisco.
And we do show CDP neighbor.|И мы показываем соседа по CDP.
Yes, I put nei.|Да ставил неи.
I don't put neighbor.|Я не ставлю соседа.
I'll tab it out so you can see exactly what the whole command is just in case, well, not just in case.|Я отложу его, чтобы вы могли точно увидеть, что представляет собой вся команда, на всякий случай, ну, а не на всякий случай.
You will be typing that command in if you have the switch simulation, all right.|Вы будете вводить эту команду, если у вас есть имитация переключения, хорошо.
And what am I looking at?|И что я смотрю?
I'm looking at my directly connected neighbors.|Я смотрю на своих напрямую связанных соседей.
I'm looking at the switch that's just underneath me and the router too that's just to the right of me, right, left, however you're standing.|Я смотрю на переключатель, который находится прямо подо мной, и на маршрутизатор, который находится справа от меня, справа, слева, как бы вы ни стояли.
So Router 2, this is my local interface.|Итак, Маршрутизатор 2, это мой локальный интерфейс.
So on my F 0/0 and all my Serial 0/0/0, I am learning,|Итак, на моем F 0/0 и на всех моих серийных 0/0/0 я учусь,
I am receiving information about my neighbor, right?|Я получаю информацию о своем соседе, верно?
It's telling me, well, we'll contain this information for this period of time.|Он говорит мне, что мы будем содержать эту информацию в течение этого периода времени.
It's telling me the capabilities that hey,|Это говорит мне о возможностях, которые эй,
this is a switch.|это переключатель.
This is a router.|Это роутер.
Well, what type of switch is it?|Ну что это за переключатель?
It's a 2960, and it's a 1841.|Это 2960, а это 1841 год.
And I'm sending it to you.|И я отправляю его вам.
And this is important when you're doing the show CDP neighbor.|И это важно, когда вы делаете шоу соседа CDP.
I am sending it to you through the F 0/24|Отправляю вам через F 0/24
on the switch, or through the S 0/0/1 of your neighbor router.|на коммутаторе или через S 0/0/1 вашего соседнего маршрутизатора.
This is why you see that in my labs, I always put F 0/24|Вот почему вы видите, что в моих лабораториях я всегда ставлю F 0/24.
connected to the router F 0/0.|подключил к роутеру F 0/0.
So, visually I know that that's the switch.|Итак, визуально я знаю, что это переключатель.
I don't even need to look at this.|Мне даже не нужно на это смотреть.
I, I know that's my switch.|Я знаю, что это мой переключатель.
This is the reason why, be, so you can understand this particular protocol.|Это причина, по которой вы можете понять этот конкретный протокол.
So you, your switch is sending CDP information through its F 0/24,|Итак, ваш коммутатор отправляет информацию CDP через F 0/24,
and you are receiving that information on the F 0/0 of your local interface, of your local interface.|и вы получаете эту информацию в F 0/0 вашего локального интерфейса, вашего локального интерфейса.
Oh, and here in the router side,|О, и здесь, на стороне маршрутизатора,
you are sending the S 0/0/1 CDP information, you're sending it.|вы отправляете информацию CDP S 0/0/1, вы ее отправляете.
And you're receiving it on your local interface, very basic information,|И вы получаете его на свой локальный интерфейс, очень базовую информацию,
layer two information.|информация о втором уровне.
But what if you wanted to see more information than just that?|Но что, если вы хотите увидеть больше информации?
What would you type?|Что бы вы напечатали?
Well, you would type detail.|Ну вы бы подробно набрали.
And now you see a lot more information.|А теперь вы видите намного больше информации.
Let's scroll up, all right, show CDP neighbor detail.|Давайте прокрутим вверх, хорошо, покажем детали соседа CDP.
Now if the switch itself were to have an IP address,|Теперь, если бы у коммутатора был IP-адрес,
right, here's the, that's what it means by entry address.|да, вот что значит адрес входа.
It means IP address, you would see it right there.|Это означает IP-адрес, вы бы его тут же увидели.
It still tells you the platform, the capabilities of, which is the switch.|Он по-прежнему сообщает вам платформу, возможности которой находится переключатель.
The FastEthernet0/0 is the local port, and the outgoing port F 0/24|FastEthernet0 / 0 - это локальный порт, а исходящий порт F 0/24.
is where the information is coming from,|откуда исходит информация,
coming from, all right?|идет откуда, хорошо?
Take a look at the router, let's keep going down a little bit.|Взгляните на роутер, давайте еще немного спустимся.
You see this right here?|Вы видите это прямо здесь?
Router 2, there is the IP address of router 2, so you can see the IP address.|Маршрутизатор 2, есть IP-адрес маршрутизатора 2, поэтому вы можете видеть IP-адрес.
But look at also, not only can you see it's a router, the type of router, the,|Но посмотрите также, вы не только увидите, что это маршрутизатор, тип маршрутизатора,
your local interface, the other router's interface.|ваш локальный интерфейс, интерфейс другого маршрутизатора.
But you're also looking at proprietary information like the iOS,|Но вы также смотрите на конфиденциальную информацию, такую ​​как iOS,
okay, that that particular router has.|хорошо, что у этого конкретного роутера есть.
So you see a lot more information.|Итак, вы видите намного больше информации.
This one right here, show CDP neighbor detail, is extremely, something's like,|Вот этот вот, показать детали соседа CDP, очень, что-то вроде,
it's got me back here, is pinching me.|он вернул меня сюда, щиплет меня.
This information here is extremely important.|Эта информация здесь чрезвычайно важна.
You will be getting print screens like this.|Вы будете получать такие экраны печати.
And you will have to type the show CDP neighbor detail so you can get information.|И вам нужно будет ввести подробную информацию о соседе по CDP, чтобы получить информацию.
Like what?|Как что?
Let's say somebody or in the test or what have you asks you, hey,|Скажем, кто-нибудь или в тесте или что у вас спрашивает, эй,
I wanna know who was the last person that sent you information or something to that effect, all right?|Я хочу знать, кто последним прислал вам информацию или что-то в этом роде, хорошо?
Oh, well, no, no.|Ой, ну нет, нет.
Let's see, I'll be, gave a bad example.|Посмотрим, я буду, привел плохой пример.
Let's see [SOUND], let's say you're stuck like I am.|Посмотрим [ЗВУК], допустим, ты застрял, как и я.
I'm here, I'm on a router.|Я здесь, у меня роутер.
And you want to know the other router's IP address and name and what have you.|И вы хотите знать IP-адрес и имя другого маршрутизатора и что у вас есть.
This would be what you can type, show CDP neighbor detail.|Это то, что вы можете ввести, показать детали соседа CDP.
You get the IP address, you get the name,|Вы получаете IP-адрес, вы получаете имя,
all right?|отлично?
But in your switch when you're inside a switch, they're going to ask you, and when we get to a switching part I'll show you exactly what I'm talking about.|Но в вашем коммутаторе, когда вы находитесь внутри коммутатора, вас спросят, и когда мы перейдем к коммутатору, я покажу вам именно то, о чем я говорю.
We'll do the same command, all right, with other commands combined.|Хорошо, мы выполним ту же команду с другими командами вместе.
So it will help you for the certification.|Так что это поможет вам в сертификации.
But this show CDP neighbor detail is important,|Но эта деталь показа соседа CDP важна,
especially when it comes to knowing the IP address, the IP address.|особенно когда дело доходит до знания IP-адреса, IP-адреса.
Because you're gonna have to match up that IP address with another screen to go ahead and get the name of the device,|Потому что вам нужно будет сопоставить этот IP-адрес с другим экраном, чтобы получить имя устройства,
to get the name of the device.|чтобы получить имя устройства.
So that's extremely important.|Так что это очень важно.
Show CDP neighbor and show CDP neighbor detail, it's a Cisco discovery protocol,|Показать соседа CDP и показать детали соседа CDP, это протокол обнаружения Cisco,
and it's used to find its locally attached neighbors.|и он используется для поиска своих локально прикрепленных соседей.
If there's another router beyond or another, you know, another switch connected to the, like a core switch,|Если есть другой маршрутизатор помимо другого, вы знаете, другой коммутатор, подключенный к, например, основной коммутатор,
you're not gonna see the other switch.|ты не увидишь другого переключателя.
Only what you are directly connected to is what you see.|Вы видите только то, с чем вы напрямую связаны.
That's what Cisco discovery protocol.|Вот что такое протокол обнаружения Cisco.
Now, let's say you type a command and nothing came out.|Теперь предположим, что вы набираете команду и ничего не выходит.
That means Cisco discovery protocol wasn't on.|Это означает, что протокол обнаружения Cisco не был включен.
Now there's two ways, there's in global configuration you can.|Теперь есть два способа, это можно сделать в глобальной конфигурации.
Now this obviously was on so if I want to turn off, I will say, NO CDP RUN.|Теперь это, очевидно, было включено, поэтому, если я хочу выключить, я скажу: NO CDP RUN.
And I just turned off CDP globally.|И я просто отключил CDP глобально.
Or I can say CDP RUN and turn it back on.|Или я могу сказать CDP RUN и снова включить его.
But let's say you have an interface.|Но допустим, у вас есть интерфейс.
Let's say you have an interface that's going out towards the internet or towards a network that you don't wanna send your CDP|Допустим, у вас есть интерфейс, который выходит в Интернет или в сеть, в которую вы не хотите отправлять свой CDP.
information cuz you don't want them to know, you know, your information,|информация, потому что вы не хотите, чтобы они знали, вы знаете, вашу информацию,
your IP address, your host name, what kind of iOS or capabilities you are.|ваш IP-адрес, ваше имя хоста, какая у вас iOS или возможности.
You don't want to send that information out.|Вы не хотите рассылать эту информацию.
So, you will go to that particular interface and let's take a look at,|Итак, вы перейдете к этому конкретному интерфейсу, и давайте взглянем на
let's just pick an interface.|давайте просто выберем интерфейс.
Do show IP INT BRIEF, just to look at my interfaces.|Покажите IP INT BRIEF, просто чтобы посмотреть на мои интерфейсы.
All right, let's use the 0/1, INT F0/1.|Хорошо, давайте использовать 0/1, INT F0 / 1.
And I'm just gonna do NO CDP ENABLE.|И я просто сделаю NO CDP ENABLE.
That's the difference.|Вот в чем разница.
Globally you do either CDP run to turn it on or no CDP run to turn it off, globally.|В глобальном масштабе вы либо выполняете CDP, чтобы включить его, либо не запускаете CDP, чтобы выключить его, глобально.
If you want to do it on an interface by interface basis,|Если вы хотите сделать это на основе интерфейса за интерфейсом,
it's CDP enable.|это включение CDP.
Or, if you want to turn it off, no CDP enable.|Или, если вы хотите отключить его, не включайте CDP.
So, and that's it.|Итак, вот и все.
That's as far as you need to go with this command for the CCNA certification, very simple.|Это все, что вам нужно с этой командой для сертификации CCNA, очень просто.
Just again, and I'm gonna type it again so you don't forget,|Еще раз, и я напечатаю еще раз, чтобы ты не забыл,
show CDP neighbor, tab, detail, all right.|показать соседа CDP, вкладку, деталь, все в порядке.
This one right here, this is the one that I'm more concerned with with this particular screen right here where it says router 2 and the IP address.|Вот этот прямо здесь, это тот, который меня больше беспокоит именно здесь, на этом экране, где написано маршрутизатор 2 и IP-адрес.
This right here, be aware of the screen.|Это прямо здесь, обратите внимание на экран.
Remember, this is your local interface.|Помните, что это ваш локальный интерфейс.
This is your neighbor's interface, okay?|Это интерфейс вашего соседа, хорошо?
This is the IP address of your neighbor,|Это IP-адрес вашего соседа,
the name of your neighbor cuz you're looking at your neighbor, all right?|имя твоего соседа, потому что ты смотришь на своего соседа, хорошо?
Don't forget that, extremely important.|Не забывай об этом, очень важно.
You will be using this.|Вы будете использовать это.
And you will see this command again, once we get to switching.|И вы снова увидите эту команду, как только мы перейдем к переключению.
I'll see you in the next lesson.|Увидимся на следующем уроке.
[BLANK_AUDIO]|[BLANK_AUDIO]