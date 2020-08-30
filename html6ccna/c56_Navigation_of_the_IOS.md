D:\mailCloud\prjother\tmp\1\c56_Navigation of the IOS.md  


__|__
--|--
All right now that we know how de,|Хорошо, теперь, когда мы знаем, как
how to connect to a Cisco router.|как подключиться к маршрутизатору Cisco.
We're gonna go ahead and start navigating through the iOS.|Мы собираемся продолжить и начать навигацию по iOS.
All right in order to try navigating through the iOS obviously,|Хорошо, чтобы попробовать навигацию по iOS, очевидно,
we need to learn some commands.|нам нужно выучить некоторые команды.
So, let's say we're up to the router and your router says router con0.|Итак, допустим, мы подошли к маршрутизатору, и ваш маршрутизатор сообщает маршрутизатор con0.
Because you are connected to the console port of the router, is now available,|Поскольку вы подключены к консольному порту маршрутизатора, теперь доступен,
press press return to get started.|нажмите клавишу возврата, чтобы начать.
So we hit Enter and there we are and if you see a prompt you need to start learning your prompts if you see a prompt that has the greater than symbol|Итак, мы нажимаем Enter, и вот мы, и если вы видите подсказку, вам нужно начать изучение подсказок, если вы видите подсказку с символом больше, чем
that is called user mode,|это называется пользовательским режимом,
user mode, if you wanna know what commands are available under any prompt you type question mark.|пользовательский режим, если вы хотите знать, какие команды доступны в любом запросе, введите вопросительный знак.
And obviously there's gonna be a lot more commands on a real iOS, okay?|И очевидно, что на настоящей iOS будет намного больше команд, хорошо?
But, at least you know what commands are underneath here.|Но, по крайней мере, вы знаете, какие команды здесь.
All right?|Отлично?
So,|Так,
it'll give you an idea of what to type.|это даст вам представление о том, что набирать.
Can you type a question mark in the iOS?|Можете ли вы ввести вопросительный знак в iOS?
I have heard both.|Я слышал оба.
I have heard yes, I have heard no.|Я слышал да, я слышал нет.
So, if you forget, you know, and then you need that context sensitive help,|Итак, если вы забыли, вы знаете, и тогда вам понадобится контекстно-зависимая помощь,
then type the question mark.|затем введите вопросительный знак.
And if it, something comes up, hey great.|И если это, что-то всплывет, хорошо.
They're not gonna take points off for that.|Они не будут снимать за это очки.
But remember, the clock is ticking.|Но помните, время идет.
The clock is ticking.|Часы тикают.
So type question marks,|Так введите вопросительные знаки,
you can see all the commands are there.|вы можете видеть, что там есть все команды.
What we're interested in is getting into privilege mode,|Нас интересует переход в привилегированный режим,
because in user mode you really can only do very passive commands.|потому что в пользовательском режиме вы действительно можете выполнять только очень пассивные команды.
You can see disable, disconnect,|Вы можете увидеть отключение, отключение,
exit, log out, ping, ssh, telnet.|выход, выход, пинг, ssh, telnet.
Very, very passive command not going to hurt the router any kind a way.|Очень, очень пассивная команда, никак не повредит маршрутизатор.
So what we want to do is we want to turn on privileged mode.|Итак, мы хотим включить привилегированный режим.
So what do we do?|Так что же нам делать?
We type the word ENABLE.|Набираем слово ВКЛЮЧИТЬ.
And then once we type the word ENABLE,|А затем, когда мы введем слово ВКЛЮЧИТЬ,
we now are in privileged mode.|мы сейчас находимся в привилегированном режиме.
Now, privileged mode is dangerous.|Теперь привилегированный режим опасен.
Because in privileged mode we can erase the startup config.|Поскольку в привилегированном режиме мы можем стереть конфигурацию запуска.
We can delete the flash if we want to delete the iOS, get rid of it.|Мы можем удалить флешку, если хотим удалить iOS, избавьтесь от нее.
It could take us to other prompts.|Это может привести нас к другим подсказкам.
All right, such as global configuration,|Ладно, например глобальная конфигурация,
and then from there we can get to interface configuration, sub interface configuration, router configuration.|а затем оттуда мы можем перейти к конфигурации интерфейса, конфигурации субинтерфейса, конфигурации маршрутизатора.
So definitely, you want to secure when we start doing the administrative commands.|Так что определенно вы хотите обезопасить себя, когда мы начнем выполнять административные команды.
You will see how to secure,|Вы увидите, как обезопасить,
by using basic passwords and usernames.|с использованием основных паролей и имен пользователей.
To secure, to the privilege mode, area.|Для защиты, в привилегированный режим, область.
Okay, you just don't want anybody getting into privilege mode.|Хорошо, вы просто не хотите, чтобы кто-то попал в привилегированный режим.
And if you do, you can actually set some security parameters, where you can put them through level one through fifteen,|И если вы это сделаете, вы действительно можете установить некоторые параметры безопасности, где вы можете установить их с первого по пятнадцатый уровень,
and they can only do so many things.|и они могут только очень многое.
All right.|Отлично.
But when you type enable,|Но когда вы вводите enable,
that takes you to privilege mode.|что переводит вас в привилегированный режим.
So when you're in privilege mode,|Итак, когда вы находитесь в привилегированном режиме,
what can you do?|что ты можешь сделать?
Well let's type the question mark.|Что ж, давайте наберем вопросительный знак.
Well here, there's one command that your book shows you that you type clock.|Что ж, вот одна команда, которую ваша книга показывает вам, когда вы вводите часы.
All right.|Отлично.
Can set the clock.|Можно установить часы.
One of the ones that I like, which I don't see right now, right here, which is the.|Один из тех, которые мне нравятся, которых я не вижу прямо здесь, это файл.
Let me see.|Дайте-ка подумать.
Right down here somewhere.|Где-то прямо здесь.
Right now.|Сейчас.
I could have sworn that said.|Я мог бы поклясться, что так сказал.
It says undebug.|Там написано undebug.
I could have sworn that said underdog.|Я мог бы поклясться, что сказал неудачник.
Okay.|Ладно.
[LAUGH] All right.|[СМЕХ] Хорошо.
Wow, I don't see it.|Вау, я этого не вижу.
There's one that's the clock and one that, oh, terminal.|Один - часы, а другой - терминал.
And then terminal because one of the good commands is terminal history size because one of the things when you're configuring,|И затем терминал, потому что одна из хороших команд - это размер истории терминала, потому что одна из вещей, когда вы настраиваете,
especially in a real world scenario because obviously in the in the CCNA exam,|особенно в реальном мире, потому что, очевидно, на экзамене CCNA
you're not going to have to type that,|вам не придется это печатать,
but in a real world command,|но в реальном мире команда,
in a real world scenario, you want to type terminal history size, and then you can go from, you know,|в реальном сценарии вы хотите ввести размер истории терминала, а затем вы можете перейти, вы знаете,
I think it's zero to two fifty six.|Думаю, от нуля до двух пятьдесят шесть.
Let's just type it here real quick so you can see it.|Давайте просто напишем это здесь очень быстро, чтобы вы могли это увидеть.
"TERMINAL HISTORY SIZE".|"ИСТОРИЧЕСКИЙ РАЗМЕР ТЕРМИНАЛА".
And we'll put a question mark.|И поставим вопросительный знак.
0-256.|0-256.
Which means it will remember,|Это значит, что он будет помнить,
the last two hundred and fifty six commands that you typed.|последние двести пятьдесят шесть набранных вами команд.
You can type whatever it is that you want.|Вы можете вводить все, что хотите.
You can type 50, and then whatever prompt you're in, it'll remember the last fifty commands that you typed,|Вы можете ввести 50, и тогда в любой строке, в которой вы находитесь, он запомнит последние пятьдесят введенных вами команд,
and you can use the up arrow, up arrow.|и вы можете использовать стрелку вверх, стрелку вверх.
You can be a little bit more efficient with that.|С этим вы можете быть немного эффективнее.
So, that's one command that you can type there, but what we're interested in cause you can only do very passive commands.|Итак, это одна команда, которую вы можете ввести там, но то, что нас интересует, потому что вы можете выполнять только очень пассивные команды.
One of the commands that you'll do here a lot is show or ping or traceroute.|Одна из команд, которую вы здесь часто будете выполнять, - это show, ping или traceroute.
You can do telnet, you can SSH,|Вы можете использовать telnet, вы можете SSH,
you can go ahead and do a clear IP OSPF process, so there's many little passive commands.|вы можете продолжить и выполнить четкий процесс IP OSPF, поэтому есть много небольших пассивных команд.
Copy run start, okay?|Копирование запуска запуска, хорошо?
Copy flash TFTP.|Скопируйте flash TFTP.
So, again, your gonna be doing many commands from pros mode but in order to configure the router as a whole through the terminal that we're in|Итак, опять же, вы будете выполнять много команд из режима профи, но для настройки маршрутизатора в целом через терминал, в котором мы находимся
you have to type CONFIG T now you see how the prompt changed we type CONFIG T Now we're in global,|вам нужно ввести CONFIG T, теперь вы видите, как изменилось приглашение, которое мы набираем CONFIG T Теперь мы в глобальном,
global configuration mode.|режим глобальной конфигурации.
So, anything we do now affects the routers a whole.|Итак, все, что мы делаем сейчас, влияет на маршрутизаторы в целом.
One command, and especially that really holds to this would be CDP, CDP RUN.|Одна из команд, и особенно она действительно подходит для этого, - это CDP, CDP RUN.
If CDP and what is CDP,|Если CDP и что такое CDP,
just to give you a quick intro to it,|просто чтобы дать вам краткое введение,
is the Cisco discovery protocol.|это протокол обнаружения Cisco.
If it's not turned on, globally you will need to go to global configuration and do CDP run and it will turn on globally,|Если он не включен, вам нужно будет перейти в глобальную конфигурацию и запустить CDP, и он включится глобально,
but you can also go into an interface.|но вы также можете войти в интерфейс.
Now once you get to global configuration.|Теперь, когда вы перейдете к глобальной конфигурации.
It will allow you to go to other,|Это позволит вам перейти к другим,
other parts, of the router.|другие части маршрутизатора.
Like router configuration mode,|Как и в режиме настройки маршрутизатора,
interface configuration mode,|режим настройки интерфейса,
sub interface configuration mode.|режим настройки дополнительного интерфейса.
If you're doing access lists,|Если вы делаете списки доступа,
named access lists,|именованные списки доступа,
you'll go into different modes from global configuration.|вы перейдете в разные режимы из глобальной конфигурации.
You couldn't go into an interface if you're in privilege mode.|Вы не можете войти в интерфейс, если находитесь в привилегированном режиме.
You couldn't go into an interface if you're in user mode.|Вы не можете войти в интерфейс, если находитесь в пользовательском режиме.
You couldn't get to global configuration if you're in user mode.|Вы не можете получить глобальную конфигурацию, если находитесь в пользовательском режиме.
So, you've gotta, it's a stepping process.|Итак, вы должны, это пошаговый процесс.
Remember back in the DOS days, right?|Помните времена DOS, верно?
We had to go step by step to get to where we want to go.|Нам нужно было идти шаг за шагом, чтобы добраться туда, куда мы хотим.
And you cannot type the command on one line.|И вы не можете набрать команду в одной строке.
You gonna say well I want to go to this particular interface so I'm gonna type,|Ты скажешь, что я хочу перейти к этому конкретному интерфейсу, поэтому я напечатаю,
I'm in protus mode let's say.|Я в режиме протуса скажем так.
I'm gonna type config t backslash interface f zero one backslash and then type the command that you want.|Я собираюсь ввести config t backslash interface f zero one backslash, а затем набрать нужную команду.
That doesn't work, that doesn't work okay,|Это не работает, это не работает,
so CDP is one that holds true to this one.|так что CDP верен этому.
This one he just turned on CDP.|Этот он только что включил CDP.
Globally or I just turn LCP globally but lets say if you go to an interface INTERFACE lets say F0/0|Глобально, или я просто включаю LCP глобально, но скажем, если вы перейдете в интерфейс ИНТЕРФЕЙС, скажем, F0 / 0
which is one of the interfaces that's there invalid okay so huhuhuhm, so I'm going to do something that you can't do on the test|который является одним из недействительных интерфейсов, хорошо, так что я собираюсь сделать то, что вы не можете сделать в тесте
do you can't do the DO show interface INT BRIEF.|вы не можете сделать DO показать интерфейс INT BRIEF.
Do show int brief.|Показывать intrief.
Okay.|Ладно.
That didn't work,|Это не сработало,
let me go back to push mode,|позвольте мне вернуться в режим нажатия,
show INT BRIEF, oh,|показать INT BRIEF, oh,
I know why it didn't work.|Я знаю, почему это не сработало.
Show IP, how about that one.|Покажи IP, как насчет того.
Show IP INT BRIEF.|Показать краткий обзор IP INT.
All right.|Отлично.
So we have gigabit interfaces.|Итак, интерфейсы гигабитные.
All right.|Отлично.
So lets go back to global and I'm gonna go INT G0/0.|Итак, вернемся к глобальному, и я перейду к INT G0 / 0.
If I wanted to turn on,|Если бы я хотел включить,
now I'm in, I went from global to an interface configuration mode in this case I had to step back out because I forgot to put IP so|теперь я нахожусь, я перешел из глобального режима конфигурации в режим настройки интерфейса, в этом случае мне пришлось отступить, потому что я забыл указать IP, поэтому
its like okay what's going on but now I,|это вроде хорошо, что происходит, но теперь я,
I did a show IP in brief that allows me to see what is,|Я сделал краткое IP-шоу, которое позволяет мне увидеть, что есть,
what are I should say the interfaces that are that we'll be using so now I'm inside that particular interface,|что это за интерфейсы, которые мы будем использовать, так что теперь я внутри этого конкретного интерфейса,
so I can do CDP ENABLE.|так что я могу сделать CDP ENABLE.
Or CDP, or NO CDP ENABLE,|Или CDP, или НЕ ВКЛЮЧИТЬ CDP,
sorry, no CDP ENABLE.|извините, нет CDP ENABLE.
Any time that you want to take something out, whether it be an IP address,|Каждый раз, когда вы хотите что-то вытащить, будь то IP-адрес,
an access list,|список доступа,
anything that you want to negate,|все, что вы хотите отрицать,
that you want to take out you have to put no in front of that command.|то, что вы хотите удалить, вы должны поставить перед этой командой нет.
So if I turned that on in that interface,|Если бы я включил это в этом интерфейсе,
well, let's say that,|ну, скажем так,
that interface was really facing out to the internet I want to send any CDP advertisements out to the internet I can turn just on that particular interface.|этот интерфейс действительно был обращен к Интернету. Я хочу отправлять любую рекламу CDP в Интернет. Я могу включить только этот конкретный интерфейс.
I can turn that off.|Я могу выключить это.
But again,|Но опять же,
I don't want to give too much away,|Я не хочу слишком много отдавать,
because we'll have a section just on that one.|потому что у нас будет раздел только по этому поводу.
You can see the navigation.|Вы можете увидеть навигацию.
Sub interface, INT G0/0.1.|Вспомогательный интерфейс, INT G0 / 0.1.
That's how you create a sub interface.|Вот как вы создаете вспомогательный интерфейс.
We have a sub interface prompt that you need to be in, and you need to understand,|У нас есть подсказка субинтерфейса, в которой вам нужно быть, и вы должны понимать,
what can you type under those interfaces and it all depends on your configuration.|что вы можете вводить в этих интерфейсах, и все зависит от вашей конфигурации.
You see,|Ты видишь,
you have IPv6 that's already there.|у вас уже есть IPv6.
The encapsulation which you will be doing when we do inter VLAN communication with the dot one queue.|Инкапсуляция, которую вы будете выполнять, когда мы будем устанавливать связь между VLAN с очередью dot one.
Bandwidth.|Пропускная способность.
So all these different things.|Итак, все эти разные вещи.
There are all these different sub- interfaces.|Есть все эти разные суб-интерфейсы.
We need to know what to type.|Нам нужно знать, что набирать.
How will you be tested on things like this?|Как вас будут проверять в подобных вещах?
There will have a particular command,|Будет определенная команда,
let's say the CDP enable.|скажем, включение CDP.
And then we'll have user mode, privileged mode, global configuration mode and interface configuration mode and then you need to choose the correct one.|Затем у нас будет пользовательский режим, привилегированный режим, режим глобальной конфигурации и режим конфигурации интерфейса, и тогда вам нужно будет выбрать правильный.
Well, the CDP enable that will be under the config if, right, so you need to know that.|Что ж, включение CDP будет в конфигурации, если да, значит, вам нужно это знать.
You need to know that if you're running this particular command that you have to run it under the interface configuration mode.|Вы должны знать, что если вы запускаете эту конкретную команду, вы должны запускать ее в режиме конфигурации интерфейса.
Whether you're, if you're running CDP run,|Независимо от того, используете ли вы CDP run,
you're running it under global configuration mode, and if you're putting an IP address on a router,|вы запускаете его в режиме глобальной конфигурации, и если вы помещаете IP-адрес на маршрутизатор,
then you're doing it under interface configuration mode.|то вы делаете это в режиме настройки интерфейса.
So these, these are the way,|Так вот, вот путь,
or this is the way that they're going to test you when it comes to the CCNA certification.|или именно так они будут проверять вас, когда дело доходит до сертификации CCNA.
But, you're gonna have so much practice doing these labs that it's gonna become second nature to you.|Но у вас будет столько практики, когда вы будете выполнять эти лабораторные работы, что это станет для вас второй натурой.
But definitely the navigation throughout any operating system is key.|Но определенно навигация по любой операционной системе является ключевой.
Whether it be a Microsoft,|Будь то Microsoft,
in Linux, Mac or a Cisco iOS, you need to make sure that you know how to navigate and what commands you will be typing once you get there.|в Linux, Mac или Cisco iOS вам необходимо убедиться, что вы знаете, как перемещаться и какие команды вы будете вводить, когда попадете туда.
And if you want to back out, exit, takes you one out, exit, takes you back out.|И если вы хотите отступить, выход, вытаскивает вас, выход, возвращает вас обратно.
And now you're in privileged mode.|И теперь вы в привилегированном режиме.
Are they shortcuts?|Это ярлыки?
Sure, Ctrl+Z.|Конечно, Ctrl + Z.
Ctrl+Z takes you from wherever you're at right back to privileged mode, all right?|Ctrl + Z возвращает вас из любого места в привилегированный режим, хорошо?
And I'll,|И я,
as we go along through the course,|по мере прохождения курса,
I'll show you different shortcut commands,|Я покажу вам разные сочетания клавиш,
break commands like the do command,|команды break, такие как команда do,
like Ctrl+Shift+6 is a break command.|как Ctrl + Shift + 6 - это команда разрыва.
It'll break anything.|Это все сломает.
So, I will show the shortcuts, but I will give you my little disclaimer that you cannot do that on the exam.|Итак, я покажу ярлыки, но я дам вам небольшой отказ от ответственности, что вы не можете сделать это на экзамене.
On the exam there is no do,|На экзамене нет дела,
on the exam there are no Ctrl+Shift+6,|на экзамене нет Ctrl + Shift + 6,
there are no do, no up arrows or anything like that.|там нет до, стрелок вверх или чего-то подобного.
Mae sure that you know how to type everything the long way, the long way.|Мэй уверена, что ты умеешь печатать все долго и долго.
Now all these handouts will be made available to you, you will have all the commands for, that you would,|Теперь все эти раздаточные материалы будут доступны для вас, у вас будут все команды, для которых вы:
the commands that you would need.|команды, которые вам понадобятся.
So you don't have an issue.|Так что у вас нет проблем.
I mean, you have your book.|Я имею в виду, у тебя есть книга.
You're going to have these lessons.|Вы получите эти уроки.
And I'm going to give you the handouts so you won't have any confusion.|И я дам вам раздаточные материалы, чтобы вы не запутались.
All right, that is navigating,|Хорошо, это навигация,
as you can see, through the router.|как видите, через роутер.
It's just simply going either exit to back out one, or being in the right interface to get to the right point.|Просто нужно либо выйти, чтобы отказаться от одного, либо оказаться в правильном интерфейсе, чтобы добраться до нужной точки.
Cause look what happens just to end it real quick just before I end it real quick, if I type interface G0/0 its gonna give me an error, its gonna|Потому что посмотри, что происходит, чтобы закончить это очень быстро, как раз перед тем, как я закончу очень быстро, если я наберу интерфейс G0 / 0, он выдаст мне ошибку, это будет
give me an error its saying well sorry you made an error we that is the right command but I'm at the wrong place so I gotta make sure that I'm in config and|дайте мне ошибку, он говорит, что хорошо, что вы сделали ошибку, мы это правильная команда, но я не в том месте, поэтому я должен убедиться, что я в конфигурации и
then I can type, see I up-arrow.|тогда я могу печатать, вижу стрелку вверх.
And now it will give me the right things.|И теперь это даст мне то, что нужно.
So you need to be under the right prompt,|Итак, вы должны быть в правильном направлении,
to type the right command,|набрать правильную команду,
to get you where you need to go.|чтобы доставить вас туда, куда вам нужно.
All right.|Отлично.
So navigation through a router is extremely important.|Так что навигация через роутер чрезвычайно важна.
But don't worry,|Но не волнуйся,
you'll have plenty of practice.|у вас будет много практики.
I'll see you in the next one.|Увидимся в следующем.