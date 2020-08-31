D:\mailCloud\prjother\tmp\1\c54_Components we need to know about.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
Welcome back young Jedis.|С возвращением, молодые джедаи.
It is now time to learn the components that you will see in your certifications.|Пришло время изучить компоненты, которые вы увидите в своих сертификатах.
ROM, RAM, NVRAM, and Flash.|ROM, RAM, NVRAM и Flash.
Those are the four that you need to know.|Это четыре, которые вам нужно знать.
Okay?|Ладно?
That said, don't go crazy on it.|Тем не менее, не сходите с ума по этому поводу.
Those are the four that you need to know.|Это четыре, которые вам нужно знать.
What you need to know is what works on those four different components, and obviously, the boot process.|Что вам нужно знать, так это то, что работает с этими четырьмя различными компонентами и, разумеется, с процессом загрузки.
But far as we're gonna learn these four components, and what's on them.|Но мы собираемся изучить эти четыре компонента и что на них есть.
ROM, what is normally on there?|ROM, что там обычно есть?
First, I'm gonna say it in order, POST,|Во-первых, я скажу это по порядку, POST,
then you have a Bootstrap,|тогда у вас есть Bootstrap,
then you have, a, mini-IOS, and then you have a dark dirty place call ROMmon.|затем у вас есть мини-IOS, а затем у вас есть темное грязное место с вызовом ROMmon.
Okay?|Ладно?
ROM, this is where everything starts,|ROM, здесь все начинается,
right?|право?
We all know this from, you know, desktop computers, what have you.|Мы все знаем это по настольным компьютерам, что у вас есть.
The first thing that happens is the POST.|Первое, что происходит, - это POST.
All right?|Отлично?
From the POST, then goes to Bootstrap, the Bootstrap looks to the Flash,|Из POST, затем переходит в Bootstrap, Bootstrap смотрит на Flash,
Flash looks for NVRAM, finds whatever's in there, and there's any configs, boom,|Flash ищет NVRAM, находит все, что там есть, и есть какие-то конфиги, бум,
loads the config, you see the pound signs,|загружает конфиг, вы видите знаки решетки,
whala, everything's up in RAM.|whala, все в ОЗУ.
All right?|Отлично?
But the first thing that happens is POST.|Но первое, что происходит, - это POST.
Then we go to the Bootstrap.|Затем заходим в Bootstrap.
The mini -IOS, think of it as a troubleshooting,|Мини-iOS, считайте это средством устранения неполадок,
like F5 in Windows, where you go to a safe mode type of,|как F5 в Windows, где вы переходите в безопасный режим типа,
type of thing, where you can have just the minimal amount of information, so you can do what you need to do.|тип вещей, в которых у вас может быть минимальное количество информации, чтобы вы могли делать то, что вам нужно.
And you can actually have a to-boot to that, if you wanted to,|И вы действительно можете добавить к этому, если хотите,
using boot system commands.|с помощью команд загрузочной системы.
And deliberately boot, and I believe it is 200X201O1, or,|И намеренно загрузился, и я считаю, что это 200X201O1, или,
if I remember correctly to boot into that deliberately.|если я правильно помню, чтобы загрузиться в это намеренно.
And then ROMmon, ROMmon stands for ROM monitor mode.|А затем ROMmon, ROMmon означает режим монитора ROM.
Now, if you find yourself,|Теперь, если вы окажетесь,
and you didn't do anything to be in ROMmon,|и ты ничего не делал, чтобы быть в ROMmon,
and all of a sudden you are in ROMmon,|и вдруг ты в ROMmon,
that's a problem.|это проблема.
All right?|Отлично?
And the way ROMmon will look like, it will look just like that, it will say ROMmon,|И то, как ROMmon будет выглядеть, это будет выглядеть так, он скажет ROMmon,
and then you see number one, let's say,|а затем вы видите номер один, скажем,
and then, no, and then that.|а потом нет, а потом то.
If you find yourself in that prompt in your router, that's a problem.|Если вы обнаружите, что это приглашение на вашем маршрутизаторе, это проблема.
If you didn't do it deliberately.|Если вы не сделали это намеренно.
Because that will give you an indication that,|Потому что это укажет вам, что
hey, your IOS meaning your Flash, your well, your operating system, I'm sorry,|эй, ваш IOS означает ваш Flash, ваш колодец, вашу операционную систему, извините,
which exists in your Flash, is missing, or corrupted.|который существует в вашем Flash, отсутствует или поврежден.
Missing or corrupted.|Отсутствует или поврежден.
And we'll learn how to change setting and I'll show you the why,|Мы узнаем, как изменить настройку, и я покажу вам, почему,
I'll just show you now.|Я вам сейчас просто покажу.
I mean I'm already here.|То есть я уже здесь.
TFTP oh, case sensitive.|TFTP ой, с учетом регистра.
When you're in here, tftpdnld, this is something that's above the CCNA,|Когда вы здесь, tftpdnld, это что-то выше CCNA,
so I'm not going to get too deep in it.|так что я не собираюсь углубляться в это.
But just so you know, if you do find yourself in ROMmon, and it is because your, your operating system is missing or corrupted,|Но просто чтобы вы знали, если вы обнаружите себя в ROMmon, и это потому, что ваша, ваша операционная система отсутствует или повреждена,
and you need to put a new one, you need to type tftpdnld and do this whole set of instructions, and I'll show it to you.|и вам нужно поставить новый, вам нужно набрать tftpdnld и выполнить весь этот набор инструкций, и я вам его покажу.
This whole set of instructions will go ahead and come out, and you've got to type it verbatim.|Весь этот набор инструкций будет продолжаться и выходить, и вы должны ввести его дословно.
It is a royal pain, okay?|Это королевская боль, понятно?
If you don't type it, if you mistype it,|Если вы его не наберете, если вы его опечатаете,
it's case sensitive, the whole nine yards,|это чувствительно к регистру, все девять ярдов,
okay?|Ладно?
And then from a TFTP server, that's what that means,|А затем с TFTP-сервера, вот что это значит,
TFTP download, you actually upload, so I don't know why I said download, but anyway, you upload a new IOS into the router.|Загрузка по TFTP, вы фактически загружаете, поэтому я не знаю, почему я сказал загрузить, но в любом случае вы загружаете новую IOS в маршрутизатор.
Okay?|Ладно?
So, you definitely don't want to find yourself in ROMmon, but ROMmon does exist, and you can boot into it deliberately as well.|Итак, вы определенно не хотите попадать в ROMmon, но ROMmon существует, и вы также можете загрузиться в него намеренно.
But you do not want to find yourself there.|Но вы не хотите там оказаться.
The next thing I have here is RAM.|Следующее, что у меня есть, это оперативная память.
RAM as we know, ROM, before I move on ROM is read only memory.|RAM, как мы знаем, ROM, прежде чем я перейду к ROM, является постоянным запоминающим устройством.
All right?|Отлично?
It's always going to be there,|Он всегда будет там,
it's not going anywhere.|это никуда не денется.
RAM is random access memory and that we know is volatile, we know this.|ОЗУ - это оперативная память, и мы знаем, что она энергозависима.
So when you're there configuring your heart out and you're typing this and you're typing that, and there's a power outage, [NOISE] and|Итак, когда вы там настраиваете свое сердце, и вы печатаете это, и вы набираете это, и происходит отключение электроэнергии, [NOISE] и
you didn't save your information, guess what?|вы не сохранили свою информацию, знаете что?
Now it's gone.|Теперь его нет.
All right?|Отлично?
So definitely, RAM.|Так что определенно RAM.
What do we have in RAM?|Что у нас в ОЗУ?
Running, and its, I'm just going to put run.|Бегу, а ее поставлю бежать.
Run, you have your run, which is your running config.|Беги, у вас есть пробег, который является вашей текущей конфигурацией.
Okay?|Ладно?
You have your ARP, cache,|У вас есть свой ARP, кеш,
you'll have your routing table, and you'll have your packet buffers.|у вас будет таблица маршрутизации и буферы пакетов.
All right?|Отлично?
All these things are things that are changeable,|Все эти вещи изменчивы,
they are volatile, that can change on a constant moment.|они непостоянны, могут меняться в постоянный момент.
Your routing table is ever changing.|Ваша таблица маршрутизации постоянно меняется.
If you're putting in new networks, or taking out networks.|Если вы вводите новые сети или удаляете сети.
So this is every changing.|Так что это каждое изменение.
So is your archives.|Как и ваши архивы.
So that's going to be ever changing when you see things come in and out.|Так что это будет когда-либо меняться, когда вы увидите, как вещи приходят и уходят.
And definitely the run.|И обязательно бег.
Remember in the CCNA you have to do a copy, run, start.|Помните, что в CCNA вам нужно сделать копию, запустить, запустить.
What does that mean?|Что это значит?
You want to copy your run, what's in RAM,|Вы хотите скопировать свой пробег, что находится в ОЗУ,
into your start, which is?|в ваш старт, что есть?
NVRAM.|NVRAM.
All right?|Отлично?
So, that's what that means.|Вот что это значит.
That's what that means.|Вот что это значит.
Can you do copy run start in the exam?|Можете ли вы запустить запуск копирования на экзамене?
I am pretty sure you can.|Я почти уверен, что ты сможешь.
Some people say, no, you got to type the whole thing,|Некоторые люди говорят: нет, ты должен все это напечатать,
copy running hyphen config start up hyphen config.|копировать текущую конфигурацию дефиса запускать конфигурацию дефиса.
This is what I, this is my opinion, this is my, why my advice to you.|Это то, что я, это мое мнение, это мое, поэтому мой вам совет.
If you're taking the test, type copy, run,|Если вы проходите тест, введите копировать, запустить,
start.|Начало.
If it works, beautiful.|Если работает - красиво.
If it gives you an error, then type the whole thing.|Если выдает ошибку, наберите все.
Okay?|Ладно?
Cause you're not going to be configuring routers from scratch.|Потому что вы не собираетесь настраивать роутеры с нуля.
You will be here in this course, but you won't be doing it in the examination.|Вы будете здесь на этом курсе, но не будете делать этого на экзамене.
So that is what works in, or that's what RAM handles.|Так вот что работает, или это то, что обрабатывает RAM.
All right?|Отлично?
The, the run, the ARP cache, the routing tables, most specifically, and packet buffers.|The, run, кэш ARP, таблицы маршрутизации, в частности, и буферы пакетов.
NVRAM, that's like your hard drive, your hard drive or your router.|NVRAM, это как ваш жесткий диск, жесткий диск или маршрутизатор.
So that's going to hold your start, your start up config.|Итак, это будет вашим стартом, ваша конфигурация запуска.
Think of it as your HDD, right?|Думайте об этом как о своем жестком диске, верно?
Your hard disk drive.|Ваш жесткий диск.
That's where, that's your start.|Вот где, это ваше начало.
That's where you're going to copy, run,|Вот куда вы собираетесь копировать, бегать,
start.|Начало.
So when you're, that's why people tell me Laz, why do you always do show start?|Так когда ты, вот почему люди говорят мне, Лаз, почему ты всегда начинаешь шоу?
Because I want to make sure that my students copy their information.|Потому что я хочу убедиться, что мои ученики копируют свою информацию.
Because I do things deliberately.|Потому что я все делаю сознательно.
I know they don't do it, so I tell them reload your routers.|Я знаю, что они этого не делают, поэтому я говорю им перезагрузить ваши маршрутизаторы.
And then when they reload, they come back to an empty configuration.|А затем при перезагрузке они возвращаются к пустой конфигурации.
And I say, why did you, I told you to copy as you go.|И я говорю, почему вы, я сказал вам копировать на ходу.
That's another question that people ask me.|Это еще один вопрос, который мне задают.
Laz, when should we copy our configurations?|Лаз, когда мы должны скопировать наши конфигурации?
Whenever you want, there is no rule that states after five lines,|Когда бы вы ни захотели, не существует правила, которое гласит после пяти строк,
copy your configuration.|скопируйте вашу конфигурацию.
It's like when you're doing a resume or you're doing a letter to your loved one,|Это как когда ты составляешь резюме или пишешь письмо любимому человеку,
are you going to wait until the very end of this beautiful,|ты собираешься подождать до самого конца этого прекрасного,
heartfelt letter that you wrote?|сердечное письмо, которое ты написал?
Shakespeare couldn't have done better himself, are you going to go ahead and save or are you gonna save as you go?|Шекспир и сам не мог бы сделать лучше, собираетесь ли вы продолжать экономить или собираетесь сохранять на ходу?
It's the same thing here.|Здесь то же самое.
You save as you go.|Вы сохраняете на ходу.
So any time you do,|Поэтому в любое время, когда вы это сделаете,
let's say the administrative configurations, copy, run start.|допустим административные настройки, копировать, запускать, запускать.
And then we do the interfaces, copy, run,|А потом делаем интерфейсы, копируем, запускаем,
start.|Начало.
We added an IP address on interface, copy,|Мы добавили IP-адрес в интерфейс, скопируйте,
run, start.|беги, старт.
We config the running protocol, copy, run,|Настраиваем запущенный протокол, копируем, запускаем,
start.|Начало.
You get my meaning, right?|Вы понимаете, что я имею в виду, верно?
That's just the way it is.|Просто так оно и есть.
After you do your configuration, copy,|После настройки скопируйте,
run, start.|беги, старт.
I'm not saying to do it every line, but every so often, just in case,|Я не говорю делать это каждую строчку, но время от времени, на всякий случай,
you never know what may happen.|никогда не знаешь, что может случиться.
You know, your dog, your little brother,|Знаешь, твоя собака, твой младший брат,
your little sister, your grandma,|твоя младшая сестра, твоя бабушка,
she's in a happy, gullible mood and she wants to come by and unplug your, unplug your router, just for the heck of it.|она в счастливом, легковерном настроении, и она хочет зайти и отключить ваш роутер, просто так.
You know what I mean?|Если вы понимаете, о чем я?
It's like, you don't, that's not good.|Как будто ты не знаешь, это нехорошо.
So make sure you copy your configurations,|Поэтому убедитесь, что вы скопировали свои конфигурации,
copy, run, start.|копировать, запускать, запускать.
Now, I will admit, I create bad habits for my students.|Теперь, признаюсь, я прививаю своим ученикам вредные привычки.
And I'll tell you what I mean.|И я вам скажу, что имею в виду.
Oops, not there.|Ой, не там.
And, freaking Notepad.|И, черт возьми, Блокнот.
You guys must be, and you'll learn all this,|Вы, ребята, должны быть, и вы все это узнаете,
you'll be in privileged mode in your test,|вы будете в привилегированном режиме в тесте,
and you have to do copy, run, start,|и вам нужно скопировать, запустить, запустить,
enter, and then it's going to ask you to confirm, and you hit enter again, right?|Enter, а затем он попросит вас подтвердить, и вы снова нажмете Enter, верно?
So, I, since I'm so used to it, but I always tell people don't do this,|Итак, я, поскольку я так привык к этому, но я всегда говорю людям, что этого не делают,
you can't do it on the test, I always do this, wr.|вы не можете сделать это на тесте, я всегда так делаю, wr.
Or do wr, depending on where I am in the router.|Или пиши, в зависимости от того, где я нахожусь в роутере.
But if I'm in Prisma, I just do wr, or even sometimes even just w.|Но если я использую Prisma, я просто пишу, а иногда даже просто пишу.
All right?|Отлично?
That's to write.|Вот писать.
That's just something, you, you know you're in the field you do this,|Это просто что-то, вы, вы знаете, что вы делаете это в той области,
[SOUND] just to do it quick.|[ЗВУК] просто чтобы сделать это быстро.
But in the test, in the test you have to do copy, run, start.|Но в тесте, в тесте вы должны сделать копирование, запуск, запуск.
I mean I'll, I'll tab, I'll, I'll barrel,|Я имею в виду, я, я закажу, я, я буду бочку,
I'll do wr,|Я сделаю письмо,
all right guys, do a Control+Z wr, boom,|хорошо, ребята, сделайте Control + Z wr, бум,
we're done.|были сделаны.
That's fine for the lab, so we can move forward in what we're doing, especially when we're in the classroom with the live|Это нормально для лаборатории, поэтому мы можем двигаться дальше в том, что делаем, особенно когда мы находимся в классе с живым
routers, but that's a different story.|роутеры, но это отдельная история.
Because, you know, the real routers are not like the Packet Tracer,|Потому что, как вы знаете, настоящие маршрутизаторы не похожи на Packet Tracer,
[NOISE] they just boot up, you know,|[NOISE] они просто загружаются, понимаете,
lightening speed or nothing like that.|скорость молнии или что-то в этом роде.
So they take their time.|Так что они не торопятся.
So we try to do things as fast as possible.|Поэтому мы стараемся делать все как можно быстрее.
But for certification purposes, for the CCNA,|Но в целях сертификации для CCNA,
you got to do things in sort of orders.|вы должны делать что-то по порядку.
You got to go back to privilege mode.|Вам нужно вернуться в привилегированный режим.
You going to do a copy, run, start.|Вы собираетесь сделать копию, запустить, начать.
You got to do the whole command.|Вы должны выполнить всю команду.
They don't allow you to do keyboard shortcuts like Control+Z or anything like that.|Они не позволяют вам использовать сочетания клавиш, такие как Control + Z или что-то в этом роде.
So remember that.|Так что помни об этом.
So try to learn the whole spelling of the commands.|Так что постарайтесь выучить написание команд целиком.
Especially I really get bad when I go to layer two.|Особенно мне становится плохо, когда я перехожу на второй слой.
Eh, cause for whatever reason in my brain,|Эх, причина по какой-то причине в моем мозгу,
when I type switch port and so doing TCH, I do THC, and I've gotta keep thinking TCH, TCH.|когда я набираю порт коммутатора и, таким образом, делаю TCH, я использую THC, и я должен продолжать думать TCH, TCH.
So that's how you save time.|Так вы экономите время.
You know what I mean?|Если вы понимаете, о чем я?
So learn, learn these spelling,|Так что учись, учи это написание,
the full spelling of the command, in case you can't do the shortcut.|полное написание команды, если вы не можете использовать ярлык.
All right?|Отлично?
Cause I do, I will be giving you bad habits, but I will be warning you of the bad habits as well.|Потому что я даю вам вредные привычки, но я также буду предупреждать вас о вредных привычках.
Okay, now, the last component that we're going to talk about is the Flash.|Хорошо, теперь последний компонент, о котором мы собираемся поговорить, - это Flash.
And that's where your IOS sits, that's where your IOS sits.|Вот где находится ваша IOS, вот где находится ваша IOS.
And that's the most important one.|И это самый важный.
And if you, I don't have the Packet Tracer open, there you go.|А если у вас, у меня Packet Tracer не открыт, вот и все.
Let's open it up real quick.|Давайте откроем это очень быстро.
[BLANK_AUDIO]|[BLANK_AUDIO]
Cause to look at these different things,|Потому что посмотреть на эти разные вещи,
[BLANK_AUDIO]|[BLANK_AUDIO]
that stood out.|что выделялось.
I always use 1841s, cause that's the router that I have here in the classroom.|Я всегда использую 1841, потому что это роутер, который у меня есть здесь, в классе.
[BLANK_AUDIO]|[BLANK_AUDIO]
All right.|Отлично.
The Flash card goes right there.|Флэшка идет тут же.
Where are you?|Где ты?
Right there.|Прямо там.
All right?|Отлично?
It's a compact Flash card.|Это компактная флеш-карта.
You put it right there.|Вы положили это прямо здесь.
Let me see if I can take it out.|Дай мне посмотреть, смогу ли я его вынуть.
I got a router down here.|У меня здесь роутер.
I'm gonna go down here real quick.|Я пойду сюда очень быстро.
I'm gonna pop it out.|Я выскочу.
Okay, that's what it looks like right there.|Хорошо, вот как это выглядит прямо здесь.
A little compact Flash card.|Маленькая компактная флешка.
I hope you can see that.|Надеюсь, вы это видите.
And make it closer, all right?|И сделай ближе, ладно?
There you go.|Вот так.
So, this is obviously physical security is one of your main concerns.|Итак, очевидно, что физическая безопасность - одна из ваших главных забот.
All right, nobody's, you know, should be walking around where they can just press that button and take your flash card.|Ладно, знаете, никто не должен ходить туда, где они могут просто нажать эту кнопку и взять вашу флеш-карту.
All right, so this 64 megabytes, that's important to know.|Итак, это 64 мегабайта, это важно знать.
That's important to know, all right?|Это важно знать, хорошо?
How much Flash you have.|Сколько у вас Flash.
One of the questions that you may encounter on your test, like any test,|Один из вопросов, с которыми вы можете столкнуться на своем тесте, как и в любом другом тесте,
I guess, that deals with hey, if you're gonna upgrade an operating system,|Я думаю, это касается того, что если вы собираетесь обновить операционную систему,
how much RAM, how much hard drive space,|сколько оперативной памяти, сколько места на жестком диске,
how,|как,
in this case how much Flash you need to have.|в этом случае, сколько Flash вам нужно иметь.
That is important, because these IOs's are decompressed into RAM,|Это важно, потому что эти операции ввода-вывода распаковываются в ОЗУ,
so that means they're compressed in here.|так что это означает, что они здесь сжаты.
So it could be a 64 megabyte size Flash IOS, right?|Значит, это может быть Flash IOS размером 64 мегабайта, верно?
The operating system.|Операционная система.
But you only have 32 RAM.|Но у вас всего 32 RAM.
Now they can't decompress into RAM and I found that out the hard way.|Теперь они не могут распаковать в ОЗУ, и я обнаружил это на собственном горьком опыте.
I didn't pay attention to what I was supposed to.|Я не обращал внимания на то, что должен был.
I'm going to go put this back, okay?|Я собираюсь положить это обратно, хорошо?
Let me put it back down here.|Позвольте мне положить его сюда.
Give me a second.|Погоди.
I'm sure it goes in, whoa, wait a minute.|Я уверен, что он войдет, подожди минутку.
All right.|Отлично.
All right, so I'll put that back in there.|Хорошо, я верну это туда.
So, now you know what the Flash card looks like.|Итак, теперь вы знаете, как выглядит флэш-карта.
Make sure nobody takes it out, okay?|Убедитесь, что его никто не вынимает, хорошо?
Especially if the router's on.|Особенно если включен роутер.
So, definitely, but the good thing about that is, if that IOS goes batty and have an extra 1841, cause these are specific.|Итак, определенно, но хорошо в том, что если эта IOS выходит из строя и имеет дополнительный 1841, потому что они специфичны.
These are specific to the series of routers.|Они относятся к серии маршрутизаторов.
You just can't get a 2600 router,|Вы просто не можете получить роутер 2600,
take the Flash card out and put it in an 1800 series.|выньте флеш-карту и вставьте ее в серию 1800.
You can't do that.|Вы не можете этого сделать.
It's got to be series specific.|Это должно быть для серии.
Series specific.|В зависимости от серии.
And the way you would look at that, and we'll do it several times, I'm going to say no here,|И то, как вы посмотрите на это, и мы сделаем это несколько раз, я скажу здесь нет,
and you'll learn soon enough if you don't already, why you would say no there.|и вы скоро узнаете, если вы еще этого не сделали, почему вы бы сказали «нет».
Show ver.|Показать вер.
Let me go, go down.|Отпусти меня, спустись.
And this gives you a whole bunch of information.|И это дает вам массу информации.
Right here, it's telling you the RAM.|Прямо здесь он сообщает вам оперативную память.
You add these two numbers, and it'll tell you the RAM that you have.|Вы складываете эти два числа, и он сообщит вам объем оперативной памяти, который у вас есть.
Okay?|Ладно?
It's telling you the Fast Ethernet cards.|Это говорит вам о картах Fast Ethernet.
How much kilobytes you have of NVRAM.|Сколько у вас килобайт NVRAM.
You don't need that many.|Вам не нужно так много.
And then of course you have how much in kilobytes you have for your Flash.|И, конечно же, у вас есть количество килобайт для вашего Flash.
So that's important and this is also, as we get into the registry,|Это важно, и это также, когда мы попадаем в реестр,
this is later on, this is important to know as well.|это позже, это тоже важно знать.
So the show version command,|Итак, команда show version,
the show version command, shows you a lot of different things.|команда show version показывает много разных вещей.
One of which is obviously the size that I just showed you of your RAM,|Один из которых, очевидно, - это размер вашей оперативной памяти, который я вам только что показал,
your NVRAM, and your FLASH, but also this guy right here.|ваш NVRAM и ваша FLASH, но также и этот парень прямо здесь.
All right?|Отлично?
Your Flash, okay?|Твой Флэш, хорошо?
You see that name?|Вы видите это имя?
It used to be very cryptic.|Раньше это было очень загадочно.
Now it's not so cryptic, not so cryptic.|Теперь все не так загадочно, не так загадочно.
All right, but at least we know that this says hey, it's advanced IP services.|Хорошо, но, по крайней мере, мы знаем, что это говорит о том, что это расширенные IP-услуги.
So we know more or less what it's dealing with.|Итак, мы более или менее знаем, с чем он имеет дело.
All right?|Отлично?
So it, it gives us actually a 15 T1 IOS.|Итак, это дает нам IOS 15 T1.
So now there, that is your IOS.|Итак, вот и ваша IOS.
Now, I always tell my students, when we're actually going to copy this to a TFTP server, the best command to type is show|Я всегда говорю своим ученикам, что когда мы действительно собираемся скопировать это на TFTP-сервер, лучше всего ввести команду show
Flash.|Вспышка.
There's your Flash right there, I'll bring this up a little bit higher.|Вот и ваша вспышка, я подниму это немного выше.
Okay, there's your, there's your Flash file right there.|Хорошо, вот и ваш, вот и ваш Flash-файл.
You can, you're going to copy paste.|Вы можете скопировать пасту.
Because to write that down, very easy to make a mistake.|Потому что, если это записать, очень легко ошибиться.
So you copy, and then you paste that when you're supposed to.|Итак, вы копируете, а затем вставляете это, когда вам нужно.
So, those are your four components.|Итак, это ваши четыре компонента.
Will you be asked questions on those four components?|Будут ли вам заданы вопросы по этим четырем компонентам?
Yes, you will.|Да, вы будете.
You'll be asked questions on the boot process.|Вам будут заданы вопросы о процессе загрузки.
You'll be asked questions, what runs on those components.|Вам будут заданы вопросы, что работает на этих компонентах.
Okay?|Ладно?
So you need to know, need to know what happens if something's missing or if you find yourself in this prompt, what does that mean?|Итак, вам нужно знать, нужно знать, что произойдет, если чего-то не хватает или вы окажетесь в этом приглашении, что это означает?
So you need to know exactly these different components.|Итак, вам нужно точно знать эти разные компоненты.
Okay?|Ладно?
So run is the first thing, right?|Так что бежать - это первое, что надо?
That has to POST, the first thing that happens.|Это первое, что происходит в POST.
Then the Bootstrap.|Затем файл Bootstrap.
Bootstrap takes over, looks for the IOS,|Начинает Bootstrap, ищет IOS,
once the IOS is found,|как только IOS будет найден,
which by default is in Flash, then the Flash looks for the NVRAM.|который по умолчанию находится во Flash, тогда Flash ищет NVRAM.
Important, Flash looks for the NVRAM to see what configuration is in there.|Важно: Flash ищет NVRAM, чтобы узнать, какая там конфигурация.
Configuration registry.|Реестр конфигурации.
Okay?|Ладно?
Getting a little ahead of myself,|Забегая немного вперед,
but that's okay.|но это нормально.
And then if there is some sort of, it says, hey, look at it, look at it,|А затем, если есть какой-то, он говорит: эй, посмотри на это, посмотри на это,
see if it's there.|посмотреть, есть ли оно там.
And then it says, oh,|А потом он говорит: о,
okay, there's configurations in this start up config file.|хорошо, в этом файле конфигурации запуска есть настройки.
Well, let me load 'em.|Что ж, позволь мне их загрузить.
And then great.|А потом отлично.
Then you see all these pound signs,|Затем вы видите все эти знаки фунта,
which is decompressing the operating system into RAM and boom,|который распаковывает операционную систему в RAM и бум,
and then you can go ahead and log in and start working and doing your thing.|а затем вы можете войти в систему и начать работать и заниматься своим делом.
All right, so these are your four components and a very brief introduction to the boot up process of the router.|Хорошо, это ваши четыре компонента и очень краткое введение в процесс загрузки маршрутизатора.
All right, so this is it.|Хорошо, вот и все.
I'll see you in the next section.|Увидимся в следующем разделе.
[BLANK_AUDIO]|[BLANK_AUDIO]