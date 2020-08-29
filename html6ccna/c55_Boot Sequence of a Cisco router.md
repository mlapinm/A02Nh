D:\mailCloud\prjother\tmp\1\c55_Boot Sequence of a Cisco router.md  


__|__
--|--
All right everyone, now we're gonna talk about the boot sequence.|Хорошо, теперь мы поговорим о последовательности загрузки.
I know I mentioned that in the previous lesson.|Я знаю, что упоминал об этом на предыдущем уроке.
I did it kinda quickly.|Я сделал это довольно быстро.
So we're gonna slow down the process a little bit, cuz you really, really,|Так что мы собираемся немного замедлить процесс, потому что ты правда, правда,
really, really, really,|действительно, правда, правда,
really need to know the boot sequence.|действительно нужно знать последовательность загрузки.
They will mess with you with these questions in the main, for the IOS portion of the router,|Они будут связываться с вами с этими вопросами в основном для части маршрутизатора IOS,
you know, the basic stuff.|знаете, основные вещи.
All right, so remember, all right,|Хорошо, так что помни, хорошо,
we said it in the last video, but we're going to say it again.|мы сказали это в последнем видео, но мы собираемся повторить это снова.
And down at the bottom I've got something special, all right,|И внизу у меня есть что-то особенное, хорошо,
that they might throw at you, okay?|что они могут бросить в тебя, хорошо?
First thing that gets looked at when you turn on your router,|Первое, на что обращают внимание при включении роутера,
the first thing that happens,|первое, что происходит,
come on finger, do your job.|давай на палец, делай свою работу.
All right,|Отлично,
lets see if this thing will do its job.|Посмотрим, будет ли эта штука делать свою работу.
No, all right, no problem,|Нет, хорошо, без проблем,
we can circumvent that.|мы можем обойти это.
POST, POST is going to do all the preoperative check, system checks, okay?|POST, POST выполнит всю предоперационную проверку, проверку системы, хорошо?
To make sure everything's running smooth,|Чтобы убедиться, что все идет гладко,
everything's fine.|все в порядке.
All the hardware, what have you.|Все железо, что у вас есть.
Just like in a computer,|Как в компьютере,
it's the same type of post.|это тот же тип сообщения.
It's the very first thing that happens.|Это происходит в первую очередь.
Then the next thing is the Bootstrap.|Затем следует Bootstrap.
The Bootstrap, its job is to look for the IOS, in the default location.|Bootstrap, его задача - искать IOS в местоположении по умолчанию.
Which is what?|Который является то, что?
Exactly.|Именно.
FLASH.|ВСПЫШКА.
So, for troubleshooting purposes,|Итак, в целях устранения неполадок,
if you know that at that point in the boot up process, when the Bootstrap is looking for the FLASH and all of a sudden you find|если вы знаете, что в тот момент процесса загрузки, когда Bootstrap ищет флэш-память, вы внезапно обнаруживаете
yourself in ROMMON, okay.|себя в ROMMON, хорошо.
That means that hey,|Это означает, что эй,
my IOS is missing or corrupted.|моя IOS отсутствует или повреждена.
All right, so that's a good hint for that.|Хорошо, это хороший намек на это.
But let's say it found your FLASH,|Но допустим, он нашел вашу ВСПЫШКУ,
it found it, it, or it found your IOS in FLASH.|он нашел его, или он нашел ваш IOS во FLASH.
So once the bootstrap locates the IOS in FLASH,|Итак, как только начальная загрузка обнаружит IOS во FLASH,
then the IOS looks at NVRAM.|затем IOS смотрит на NVRAM.
And really what it's doing,|И действительно, что он делает,
how is it looking at NVRAM?|как там смотрит NVRAM?
Cuz it's looking at the registry.|Потому что он смотрит в реестр.
And I'm going to be briefly through this.|И я кратко расскажу об этом.
It's looking to see, at the registry.|Это нужно увидеть в реестре.
Cuz that's a question that you may get asked.|Потому что это вопрос, который вам могут задать.
What's the next step that it's gonna do once it finds the IOS and it's gonna load that image?|Какой следующий шаг он сделает, когда найдет IOS и загрузит этот образ?
Well, it's gonna look towards the register settings.|Что ж, это будет смотреть в сторону настроек реестра.
Is it 2102 or 2142?|Это 2102 или 2142?
2102, looking at NVRAM and tell me the configurations are there, and if they're there, load them.|2102, смотрит на NVRAM и говорит мне, что конфигурации есть, и если они есть, загрузите их.
If it's 2142, ignore it.|Если это 2142, не обращайте на него внимания.
Okay?|Ладно?
So that's what the IOS does, it looks at the registry, depending on what it's set to, it will either load the configurations|Итак, что делает IOS, он смотрит на реестр, в зависимости от того, что он установлен, он либо загружает конфигурации
or not load the configurations.|или не загружать конфигурации.
And then once it, it,|А потом однажды это,
let's say it's at default and it loads,|допустим, он по умолчанию и загружается,
it looks at NVRAM and there's configs there.|смотрит на NVRAM и там конфиги.
It loads the configs,|Загружает конфиги,
you see the decompression, and boom,|вы видите декомпрессию и бум,
you're up in the in RAM, right?|ты в оперативной памяти, верно?
Everything gets loaded into RAM.|Все загружается в оперативную память.
And then you're prompted for your username and password.|Затем вам будет предложено ввести имя пользователя и пароль.
Or just hit Enter and then you're asking for a you're in user mode,|Или просто нажмите Enter, а затем вы просите, чтобы вы в пользовательском режиме,
you type enable, and then you may be asked for a password at that point.|вы вводите enable, и тогда вас могут попросить ввести пароль.
It all depends on the configurations that were configured in the startup config file.|Все зависит от конфигураций, которые были настроены в файле конфигурации запуска.
So that is the, the order, okay,|Таков порядок, ладно,
the order, post Bootstrap.|заказ, выложите Bootstrap.
Then it goes from the Bootstrap to the IOS, from the IOS,|Затем он переходит от Bootstrap к IOS, от IOS,
it looks towards the registry to see if it looks at NVRAM.|он смотрит в реестр, чтобы увидеть, смотрит ли он на NVRAM.
And that's important.|И это важно.
It goes,|Это идет,
the FLASH will look at the registry to see if it should look at the IOS,|FLASH просмотрит реестр, чтобы узнать, следует ли искать IOS,
or not look at the IOS.|или не смотреть на IOS.
Okay?|Ладно?
Depending if it's 2102 or 2142.|В зависимости от того, 2102 это или 2142.
And then if it is the default which is 2102, it will look at NVRAM,|А затем, если по умолчанию 2102, он будет смотреть на NVRAM,
load any configurations, if any, and then it goes on to load everything into RAM.|загружает любые конфигурации, если они есть, а затем загружает все в ОЗУ.
So that's the default.|Так что по умолчанию.
Now here at the bottom, they may ask you what if it doesn't find the IOS in FLASH?|Теперь здесь, внизу, они могут спросить вас, а что, если он не найдет IOS во FLASH?
What's the next step that it will look for an IOS?|Каким следующим шагом будет поиск IOS?
It will look for a TFTP server.|Он будет искать сервер TFTP.
Now, if you're running ISR router,|Теперь, если вы используете маршрутизатор ISR,
meaning integrated service routers,|имеется в виду интегрированные сервисные маршрутизаторы,
if they're connected to a LAN or a WAN environment already, and they can sense, they can detect that there's a co-connection, they will|если они уже подключены к локальной или глобальной сети, и они могут почувствовать, они могут обнаружить, что есть совместное подключение, они будут
broadcast out looking for configurations.|транслировать в поисках конфигураций.
All right?|Отлично?
Now if it's an ISR router,|Теперь, если это ISR-маршрутизатор,
if it doesn't find it, you will quickly see that either you will load it and you will be in RAM, or you'll be in ROMMON, which would be a problem.|если он не найдет его, вы быстро увидите, что либо вы загрузите его, и вы будете в ОЗУ, либо вы будете в ROMMON, что будет проблемой.
With a non-ISR router, this is where you see the broadcast of 255,|На маршрутизаторе без ISR вы видите широковещательную передачу 255,
255, 255, layer three broadcast,|255, 255, трансляция третьего уровня,
looking for a TFTP server.|ищу TFTP сервер.
And that sounds like a question to me,|И это звучит для меня как вопрос,
boys and girls.|мальчики и девочки.
All right?|Отлично?
That when you see that,|Что, когда вы это видите,
that it's looking for a TFTP server,|что он ищет сервер TFTP,
it could be that hey, it's not find,|может быть, эй, это не найти,
it didn't find it in the default location.|он не нашел его в местоположении по умолчанию.
It could be that somebody used a boot system command that told it hey,|Возможно, кто-то использовал команду системы загрузки, которая сообщила ему: «Эй,
boot system, look for the FLASH in this particular TFTP server with this file name.|загрузочной системы, найдите флэш-память на этом конкретном сервере TFTP с этим именем файла.
So you couldn't force it to boot.|Так что вы не могли заставить его загрузиться.
But if it doesn't find one in FLASH,|Но если он не найдет его во FLASH,
it could back up to a TFTP server, and if it doesn't find one in a TFTP server,|он может выполнить резервное копирование на TFTP-сервер, и если он не найдет его на TFTP-сервере,
the last option is ROM, ROM.|последний вариант - ROM, ROM.
And if it goes into ROM to look for an IOS, what IOS is it gonna find?|И если он войдет в ПЗУ в поисках IOS, какой IOS он найдет?
It's gonna find that MINI-IOS.|Он найдет МИНИ-IOS.
All right?|Отлично?
Which is basically, you're in ROMMON.|По сути, вы в ROMMON.
That's what's really gonna happen, you're gonna be in ROMMON, and then you're like,|Вот что действительно произойдет, ты будешь в ROMMON, а потом ты такой:
oh wow, you know,|о, вау, знаешь,
you're gonna be in, not trouble, but you're gonna have some work ahead of you.|у тебя будут проблемы, не беда, но впереди у тебя будет работа.
All right?|Отлично?
But again, to drill this down remember,|Но опять же, чтобы понять это, помните,
pulse comes first,|пульс на первом месте,
there's always checking.|всегда есть проверка.
Then it kicks the Bootstrap, it kicks off.|Затем он запускает Bootstrap, он запускается.
Bootstrap's looking for FLASH,|Bootstrap ищет FLASH,
it's looking for IOS in FLASH, by default.|по умолчанию он ищет IOS во FLASH.
And if it finds it,|И если найдет,
FLASH looks towards the registry to see if it looks, if it looks or doesn't look at NVRAM.|FLASH смотрит на реестр, чтобы узнать, смотрит ли он, смотрит или не смотрит на NVRAM.
And if it does look at NVRAM, if there's any configurations, then you're in RAM.|И если он смотрит на NVRAM, если есть какие-то конфигурации, то вы в ОЗУ.
But what if there's no configs?|А что делать, если конфигов нет?
What if everything's default settings,|Что, если все настройки по умолчанию,
right?|право?
Found my FLASH, everything is 2102,|Нашел свою FLASH, все 2102,
that's the default.|это по умолчанию.
It looked at NVRAM and it saw that NVRAM was empty.|Он посмотрел на NVRAM и увидел, что NVRAM пуста.
You say, hey, there's no configs,|Вы говорите, эй, конфигов нет,
there's no configs in NVRAM.|в NVRAM конфигов нет.
Fine.|Хорошо.
Then we are in, setup mode,|Затем мы находимся в режиме настройки,
the initial configuration dialogs, right?|диалоги начальной настройки, верно?
Setup mode.|Режим настройки.
This is where we get the question,|Здесь возникает вопрос:
yes or no.|да или нет.
So this process right here, you will be asked questions on this process.|Итак, этот процесс прямо здесь, вам будут заданы вопросы по этому процессу.
So this is something that you really need to understand.|Так что это то, что вам действительно нужно понять.
It's not going to be tricky questions.|Это не будет сложными вопросами.
The trickiest question is this.|Самый сложный вопрос вот в чем.
Or it could be this,|Или это могло быть так,
some fashion of it, all right?|какая-то мода, хорошо?
I don't know it verbatim or nothing like that.|Я не знаю это дословно или что-то в этом роде.
But if it's about to load,|Но если он вот-вот загрузится,
it found the IOS and it's about to load the image,|он нашел IOS и собирается загрузить изображение,
what does it do next?|что он делает дальше?
Well it's going to look at the registry,|Ну вот реестр посмотрю,
because yes, it's going to look at NVRAM,|потому что да, он будет смотреть на NVRAM,
it's gonna, it has to go to NVRAM, but in order to go to NVRAM, who tells it to go?|он должен идти в NVRAM, но чтобы перейти в NVRAM, кто велит ему идти?
The registry.|Реестр.
The registry tells it to go, all right?|Реестр говорит, что надо идти, хорошо?
So it all depends.|Так что все зависит от обстоятельств.
So it will look at the registry depending,|Таким образом, он будет смотреть в реестр в зависимости,
2102, look at it.|2102, посмотрите на это.
2142, ignore it.|2142, не обращайте на это внимания.
And then if it's ignoring it,|И если он это игнорирует,
it just boots you up into the router, and doesn't load any configs.|он просто загружает вас в маршрутизатор и не загружает никаких конфигураций.
If it's 2102 and there's configs,|Если это 2102 и есть конфиги,
it loads whatever configs were there.|он загружает любые конфиги.
All right?|Отлично?
If there's no configs, and you're 2102, what happens?|Если конфигов нет, а ты 2102, что будет?
You're in setup mode.|Вы находитесь в режиме настройки.
Let me show you real quick a router with no configs.|Позвольте мне быстро показать вам роутер без конфигов.
All right?|Отлично?
Oh, not that right there.|О, не то, что прямо здесь.
Minimize that and open up the Packet Tracer.|Сверните это и откройте Packet Tracer.
All right, let's put that, any router,|Хорошо, допустим, любой роутер,
it doesn't matter which router.|не имеет значения, какой роутер.
Let's maximize it.|Давайте максимизировать это.
You see, it's already, I mean,|Понимаете, это уже, я имею в виду,
the simulator goes so quickly, but you saw the pound signs.|симулятор идет так быстро, но вы видели знаки фунта.
You see that now we're in setup mode.|Вы видите, что теперь мы находимся в режиме настройки.
The configuration dialog box, right?|Диалоговое окно конфигурации, верно?
If you click Yes, it's just gonna, I mean not if you click Yes, if you type in yes,|Если вы нажмете Да, это будет просто, я имею в виду, что нет, если вы нажмете Да, если вы введете Да,
it's gonna give you a bunch of questions.|это даст вам кучу вопросов.
Cuz you can configure the router,|Потому что вы можете настроить маршрутизатор,
the basic configurations of the router,|основные конфигурации роутера,
through this.|сквозь это.
Here we normally, I tell you about it,|Вот мы обычно, я вам об этом говорю,
you type no, because we're gonna be doing things from scratch, we're going to be doing things from scratch, okay?|вы набираете «нет», потому что мы будем делать что-то с нуля, мы собираемся делать что-то с нуля, хорошо?
So there you go.|Итак, поехали.
That is your complete boot up process.|Это ваш полный процесс загрузки.
Know it, love it, embrace it, remember it.|Знайте это, любите, принимайте это, помните.
All right,|Отлично,
cuz you will be asked questions on it.|Потому что вам будут задавать вопросы по этому поводу.
So you need to understand that boot up order.|Итак, вам нужно понимать этот порядок загрузки.
All right ladies and gentlemen,|Хорошо, дамы и господа,
I'll see you in the next lecture.|Увидимся на следующей лекции.