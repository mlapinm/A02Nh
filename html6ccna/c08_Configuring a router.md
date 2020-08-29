D:\mailCloud\prjother\tmp\1\c08_Configuring a router.md  


__|__
--|--
Okay, we got our simple Topology.|Хорошо, у нас есть простая топология.
We got our IP address, first thing that we're gonna configure.|Мы получили наш IP-адрес, и это первое, что мы собираемся настроить.
I know it's kind of backwards.|Я знаю, что это отчасти наоборот.
We usually start from the bottom up,|Обычно мы начинаем снизу вверх,
we're going to start this time from the top down.|в этот раз мы начнем сверху вниз.
The router is our gateway.|Маршрутизатор - это наш шлюз.
The router is our layer three device, so what we're going to configure, I'll do a little basic configuration.|Маршрутизатор - это наше устройство третьего уровня, поэтому что мы собираемся настроить, я сделаю небольшую базовую настройку.
We'll give the router a name,|Мы дадим роутеру имя,
and then we're gonna go straight into the interface.|а затем мы перейдем прямо к интерфейсу.
At least we know, what router we're working in?|По крайней мере, мы знаем, в каком роутере мы работаем?
Okay?|Ладно?
So we're going to click on the router.|Итак, мы собираемся щелкнуть по маршрутизатору.
I'm going to move it over here, so you guys can see it.|Я собираюсь переместить его сюда, чтобы вы, ребята, могли это увидеть.
And we're using the IP schema of 192.168.1.0.|И мы используем схему IP 192.168.1.0.
So I'm going to come over here.|Так что я пойду сюда.
I'm gonna go on the CLI tab.|Я перейду на вкладку CLI.
Please don't cheat, and go into the Config tab, and do everything through there.|Пожалуйста, не обманывайте, перейдите на вкладку Config и проделайте все там же.
Don't do that.|Не делай этого.
And I'll explain once we get to the iOS portion and administration portions of the class, of the course, what all this stuff means?|И я объясню, как только мы перейдем к части iOS и части администрирования класса, конечно, что все это означает?
But for right now, if you find yourself,|Но прямо сейчас, если ты найдешь себя,
and something is asking you yes or no?|и что-то спрашивает вас да или нет?
You will always say no,|Ты всегда будешь говорить нет,
because we don't wanna be wizard driven through the whole time.|потому что мы не хотим быть волшебниками все время.
So, you hit Enter a couple times there.|Итак, вы нажимаете Enter там пару раз.
We're in user mode.|Мы в пользовательском режиме.
I'm gonna type Enable, and yes, I abbreviate quite a bit, CONFIG T.|Я наберу Enable, и да, я немного сокращу CONFIG T.
You cannot abbreviate in the exam.|На экзамене нельзя сокращать.
You can abbreviate to a certain degree,|Вы можете сокращать до определенной степени,
all right?|отлично?
I'm gonna give it a host name.|Я дам ему имя хоста.
[BLANK_AUDIO]|[BLANK_AUDIO]
Let's call it R1.|Назовем его R1.
I have caps lock on, okay.|У меня заглавные буквы включены, хорошо.
Go into the interface F0/0, IP ADDRESS,|Заходим в интерфейс F0 / 0, IP-АДРЕС,
you actually have to put that,|вы действительно должны поставить это,
192.168.1.254, remember.|192.168.1.254, помните.
I said the last available IP address within that network is 254, not 24.|Я сказал, что последний доступный IP-адрес в этой сети - 254, а не 24.
255.255.255.0.|255.255.255.0.
We're using a default mask for a Class C,|Мы используем маску по умолчанию для класса C,
CIDR 24.|CIDR 24.
Converts to a dotted decimal 255.255.255|Преобразует в десятичное число с точками 255.255.255
0, right?|0 да?
32550, all right?|32550, хорошо?
Now, remember what I said.|Теперь вспомни, что я сказал.
I also said that by default,|Я также сказал, что по умолчанию
all routers' interfaces are shut down, so we need to turn them on.|все интерфейсы роутеров выключены, поэтому нам нужно их включить.
So, what do we do?|Так что же нам делать?
NO SHUT, and that's it.|НЕТ ЗАКРЫТИЯ, и все.
That's how simple that is?|Вот как это просто?
I'm gonna do a keyboard combination.|Я сделаю комбинацию клавиш.
Ctrl+Z, that takes me directly into privileged mode.|Ctrl + Z, что переводит меня прямо в привилегированный режим.
And we will learn all these commands later on.|И все эти команды мы узнаем позже.
We'll, and I'm gonna type a SHOW IP INT BRIEF, and what that shows me?|Мы напечатаем, и я напечатаю SHOW IP INT BRIEF, и что это мне показывает?
And I'll open this up, all right that shows me hey, this is my interface that I just did.|И я открою это, хорошо, что показывает мне, эй, это мой интерфейс, который я только что сделал.
This is the IP address I put on it, and everything is up, up.|Это IP-адрес, который я ему поставил, и все в порядке.
So we're good.|Так что у нас все хорошо.
We gave our router a name, we gave the router an IP address.|Мы дали нашему роутеру имя, мы дали роутеру IP-адрес.
We're turned on, we're good.|Мы заводимся, мы в порядке.
We're good to go.|Мы в порядке.
We're done with the router, we're off to the next lesson, and we'll configure the next device.|С маршрутизатором мы закончили, переходим к следующему уроку и настраиваем следующее устройство.
I'll see you there.|Увидимся там.
[BLANK_AUDIO]|[BLANK_AUDIO]
Okay, we got our simple topology.|Хорошо, у нас есть простая топология.
We've got our IP address.|У нас есть IP-адрес.
First thing that we're gonna configure, I know it's kind of backwards,|Первое, что мы собираемся настроить, я знаю, это как бы наоборот,
since we usually start from the bottom up,|поскольку мы обычно начинаем снизу вверх,
but we're gonna start this time from the top down.|но на этот раз мы начнем сверху вниз.
The router is our gateway.|Маршрутизатор - это наш шлюз.
The router is our layered three device, so what we're gonna configure.|Маршрутизатор - это наше трехуровневое устройство, так что мы собираемся его настроить.
We'll do a little basic configuration,|Сделаем небольшую базовую настройку,
we'll give the router a name and then we're gonna go straight into the interface.|мы дадим маршрутизатору имя, а затем перейдем прямо к интерфейсу.
At least we know what router we're working in, okay?|По крайней мере, мы знаем, с каким роутером работаем, хорошо?
So we're gonna click on the router.|Итак, мы щелкнем по маршрутизатору.
I'm gonna move it over here, so you guys can see it.|Я перенесу его сюда, чтобы вы, ребята, это увидели.
And we're using the IP scheme of 192.168.1.0.|И мы используем IP-схему 192.168.1.0.
So I'm gonna come over here.|Так что я пойду сюда.
I'm gonna go on the CLI tab.|Я перейду на вкладку CLI.
Please don't cheat and go into the config tab and do everything through there.|Пожалуйста, не обманывайте, перейдите на вкладку конфигурации и проделайте все там же.
Don't do that.|Не делай этого.
And I'll explain once we get to the iOS portion and administration portions of the class, of the course, what all this stuff means.|И я объясню, как только мы перейдем к части iOS и части администрирования класса, конечно, что все это означает.
But for right now, if you find yourself in something that's asking you yes or no, you will always say no because we don't wanna|Но прямо сейчас, если вы обнаружите, что вас спрашивают да или нет, вы всегда будете говорить нет, потому что мы не хотим
be wizard-driven through the whole time.|быть управляемым волшебником все время.
So you hit Enter a couple of times there.|Итак, вы нажали там пару раз Enter.
We're in user mode.|Мы в пользовательском режиме.
I'm gonna type enable and yes I abbreviate quite a bit.|Я напечатаю enable и да, я немного сокращу.
Config T.|Конфиг T.
You cannot abbreviate in the exam.|На экзамене нельзя сокращать.
You can abbreviate to a certain degree.|Вы можете сокращать до определенной степени.
All right, I'm gonna give it a host name.|Хорошо, я дам ему имя хоста.
[BLANK_AUDIO]|[BLANK_AUDIO]
Let's call it R1, I have caps lock on,|Назовем его R1, у меня заглавные буквы включены,
okay.|Ладно.
Going to the interface F0/0, IP R address you actually have to put that, 192.168.1.254.|Переходя к интерфейсу F0 / 0, IP-адрес R, который вам нужно указать, 192.168.1.254.
Remember I said the last available IP address within that network is 254.|Помните, я сказал, что последний доступный IP-адрес в этой сети - 254.
Not 24.|Не 24.
255.255.255.0.|255.255.255.0.
We're using a default mask for a class C,|Мы используем маску по умолчанию для класса C,
CIDR 24 converts to a dotted decimal, 255.255.255.0, right?|CIDR 24 преобразуется в десятичное число с точками, 255.255.255.0, верно?
Three 255 zeroes.|Три 255 нулей.
All right?|Отлично?
Now remember what I said,|Теперь помните, что я сказал,
I also said that by default all routers interfaces are shut down.|Я также сказал, что по умолчанию все интерфейсы маршрутизаторов отключены.
So we need to turn them on.|Значит, нам нужно их включить.
So what do we do?|Так что же нам делать?
No shut.|Нет, заткнись.
And that's it, that's how simple that is.|И все, вот как это просто.
IвЂ™m gonna do a keyboard combination Ctrl+Z, that takes me directly into privileged mode, and we'll learn all these commands later on.|Я собираюсь ввести комбинацию клавиш Ctrl + Z, которая переведет меня прямо в привилегированный режим, и мы изучим все эти команды позже.
We, and I'm gonna type a show IP int brief.|Мы, и я напечатаем краткое описание IP-адреса шоу.
And what that shows me, and I'll open this up.|И то, что это показывает мне, и я открою это.
[BLANK_AUDIO]|[BLANK_AUDIO]
All right, and that shows me hey this is my interface that I just did.|Хорошо, и это показывает мне, что это мой интерфейс, который я только что сделал.
This is the IP address I put on it and everything is up, up.|Это IP-адрес, который я наделил, и все в порядке.
So we're good.|Так что у нас все хорошо.
We gave our router a name.|Мы дали нашему роутеру имя.
We gave the router an IP address.|Мы дали роутеру IP-адрес.
We turned it on.|Мы его включили.
We're good.|Были хороши.
We're good to go.|Мы в порядке.
We're done with our router.|Мы закончили с нашим маршрутизатором.
We're off to the next lesson and we'll configure the next device.|Мы переходим к следующему уроку, и мы настроим следующее устройство.
I'll see you there.|Увидимся там.
[BLANK_AUDIO]|[BLANK_AUDIO]