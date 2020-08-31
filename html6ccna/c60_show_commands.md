D:\mailCloud\prjother\tmp\1\c60_show commands.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
All right, welcome back everyone.|Хорошо, с возвращением всех.
We've configured our router fully.|Мы полностью настроили наш роутер.
IP addresses.|IP-адреса.
We verified that we can ping and that we can SSH and telnet to our routers.|Мы подтвердили, что можем пинговать и можем подключаться к маршрутизаторам по SSH и telnet.
Now, we're gonna go ahead, and as you can see, we're already in one of our routers,|Теперь мы продолжим, и, как видите, мы уже в одном из наших маршрутизаторов,
in router one.|в роутере один.
And there's a couple of SHOW commands that I want you to be very friendly with.|И есть пара команд SHOW, с которыми я хочу, чтобы вы были очень дружелюбны.
You need to know these SHOW commands.|Вам необходимо знать эти команды SHOW.
In your certification, it's basically, you know, in the router,|В вашей сертификации это в основном, как вы знаете, в маршрутизаторе,
anyway, it's SHOW SHOW RUN.|в любом случае, это SHOW SHOW RUN.
SHOW IP INT BRIEF.|ПОКАЗАТЬ КРАТКИЙ ОБЗОР IP.
But we wanna take a look at each one of these SHOW commands, and what is it you need to look at, okay, look at.|Но мы хотим взглянуть на каждую из этих команд SHOW, и на что вам нужно посмотреть, хорошо, посмотрите.
All right, so for the basic stuff,|Хорошо, так что по основам,
obviously in a certification,|очевидно, в сертификации,
you do SHOW RUN, and you take a look at your run and as you're looking at your run, you're taking a look at each and every thing that has been configured.|вы делаете SHOW RUN, и вы смотрите на свою пробежку, и когда вы смотрите на свою пробежку, вы смотрите на каждую вещь, которая была настроена.
Again, what you want to see is that service password-encryption,|Опять же, вы хотите видеть, что сервисное шифрование паролей,
host name, enable secret, but remember,|имя хоста, включить секрет, но помните,
whatever they tell you to do is what you need to look to see if it's configured or not configured.|все, что они вам говорят, это то, что вам нужно посмотреть, чтобы увидеть, настроено оно или нет.
And that's usually going to be either routing protocol and access list.|Обычно это либо протокол маршрутизации, либо список доступа.
You're not going to be doing anything like this.|Вы не собираетесь делать ничего подобного.
But at least you know what you're looking at.|Но по крайней мере вы знаете, на что смотрите.
I have the SSH.|У меня есть SSH.
You scroll down, you scroll down.|Вы прокручиваете вниз, вы прокручиваете вниз.
There's your interfaces.|Вот ваши интерфейсы.
Very important to make sure and verify that you have the right IP address and mask.|Очень важно убедиться, что у вас правильный IP-адрес и маска.
All right.|Отлично.
And the clock rate when it comes to the DCE portion of the router's interface.|И тактовая частота, когда речь идет о DCE-части интерфейса маршрутизатора.
Okay.|Ладно.
You keep scrolling down.|Вы продолжаете прокручивать вниз.
There's your banner, your consoles, your passwords, and all that.|Вот ваш баннер, ваши консоли, ваши пароли и все такое.
You see it's encrypted.|Вы видите, что это зашифровано.
Right, that's encrypted.|Верно, это зашифровано.
Because we did service password-encryption.|Потому что мы сделали сервис шифрования паролей.
Same thing with the vtys 0 through 15.|То же самое с vtys от 0 до 15.
And you see how it separates the default from the rest of the lines.|И вы видите, как он отделяет строку по умолчанию от остальных строк.
Now, the other one that you will be doing is SHOW IP INT BRIEF, SHOW IP INT BRIEF.|Теперь вы будете делать еще одно, это ПОКАЗАТЬ КРАТКИЙ ОБЗОР IP INT, ПОКАЗАТЬ КРАТКИЙ IP INT.
You will always do that, you'll always, or a lot of times, this command you will do,|Вы всегда будете делать это, вы всегда или много раз будете выполнять эту команду,
cuz you want to see, hey, the IP addresses are there, and now I know everything was up up, remember,|Потому что вы хотите увидеть, эй, IP-адреса есть, и теперь я знаю, что все было в порядке, помните,
before they said down down, and that was because the other side was not configured,|прежде, чем они сказали вниз, и это было потому, что другая сторона не была настроена,
therefore we had a layer one issue.|поэтому у нас была проблема первого уровня.
Remember, down down means layer one issue.|Помните, что вниз означает проблему первого уровня.
Up down means layer two issue,|Вверх вниз означает проблему второго уровня,
encapsulation issue, clock, clocking issue, okay?|проблема инкапсуляции, часы, проблема с синхронизацией, хорошо?
All right.|Отлично.
So SHOW IP INT BRIEF.|Итак, ПОКАЗАТЬ КРАТКИЙ ОБЗОР IP
There's a command that's similar to SHOW IP INT BRIEF which is called SHOW PROTOCOLS.|Есть команда, похожая на SHOW IP INT BRIEF, которая называется SHOW PROTOCOLS.
And I'm gonna tab over, and that's with an S,|И я перейду, и это с буквой S,
SHOW PROTOCOLS, and I'll show you what it says.|ПОКАЖИТЕ ПРОТОКОЛЫ, и я покажу вам, что там написано.
It's basically the same thing, just it looks different.|По сути, это то же самое, только выглядит иначе.
It is showing you that your FastEthernet is up, right?|Это показывает вам, что ваш FastEthernet работает, верно?
FastEthernet is up, line protocol is up,|FastEthernet включен, протокол линии работает,
just like the INT BRIEF showed you.|именно так, как вам показал INT BRIEF.
It is showing you the IP address, but at the same time, it shows you the mask.|Он показывает вам IP-адрес, но в то же время показывает вам маску.
So it gives you that one extra bit of information so you don't have to do a start, because in the start you see everything.|Таким образом, это дает вам один дополнительный бит информации, поэтому вам не нужно начинать, потому что в начале вы видите все.
On a production router, if you do a start,|На производственном маршрутизаторе, если вы начнете,
it'll tell you,|он скажет вам,
you'll get a warning probably in the banner that says, don't do a show start,|вы, вероятно, получите предупреждение в баннере, в котором говорится, не начинать шоу,
cuz you'll probably bog down the router,|потому что вы, вероятно, увязнете в маршрутизаторе,
looking at all those thousands and hundreds of thousands of information and lines are in there.|глядя на все эти тысячи и сотни тысяч информации и строк.
You'll learn something called the pipe command that you can actually tell it to look at specific things.|Вы узнаете что-то, что называется командой канала, которую вы можете сказать ей, чтобы посмотреть на конкретные вещи.
But here, we instead of doing SHOW IP INT BRIEF,|Но здесь мы вместо SHOW IP INT BRIEF,
another thing you can do is called SHOW PROTOCOLS, where you can see just the prot you will see the same thing, but now you|еще одна вещь, которую вы можете сделать, называется SHOW PROTOCOLS, где вы можете видеть только prot, вы увидите то же самое, но теперь вы
get to see the actual mask as well.|увидеть фактическую маску.
The next command that what we'll start doing later on will be SHOW FLASH.|Следующая команда, которую мы начнем делать позже, будет SHOW FLASH.
And I think I showed you this already, the SHOW FLASH, which you can actually see the IOS name right here that we would copy|И я думаю, что уже показал вам это, SHOW FLASH, вы можете увидеть имя IOS прямо здесь, которое мы скопируем
and paste when we're backing it up to a TFTP server, so a SHOW FLASH.|и вставьте, когда мы создадим резервную копию на сервере TFTP, поэтому SHOW FLASH.
SHOW VERSION, most definitely,|ПОКАЗАТЬ ВЕРСИЮ, безусловно,
SHOW VERSION is another command that you wanna do.|ПОКАЗАТЬ ВЕРСИЮ - еще одна команда, которую вы хотите выполнить.
It's gonna show you your IOS, another release of the the bootstrap, 12.3.|Он покажет вам вашу IOS, еще одну версию начальной загрузки, 12.3.
Okay, what this product contains, so the feature set, all right,|Хорошо, что содержит этот продукт, так что набор функций, хорошо,
it's gonna tell you right there, so sounds like a question to me.|он скажет вам прямо здесь, так что это звучит как вопрос для меня.
SHOW VERSION, all right, and then just copyright information.|ПОКАЖИТЕ ВЕРСИЮ, хорошо, а потом только информацию об авторских правах.
And then the amount of RAM, if you add these two numbers together,|А затем объем оперативной памяти, если сложить эти два числа вместе,
it'll tell you the amount of RAM.|он сообщит вам объем оперативной памяти.
What's being used versus what you have.|Что используется по сравнению с тем, что у вас есть.
So, add them both, you get a total number of RAM.|Итак, добавив их обоих, вы получите общее количество ОЗУ.
The Ethernet, the processor, how much NVRAM you have,|Ethernet, процессор, сколько у вас NVRAM,
okay, and how much flash you have.|ладно, а сколько у тебя вспышки.
Everything is in bytes and key, key, key,|Все в байтах и ​​ключ, ключ, ключ,
key, key.|ключ, ключ.
Registry.|Реестр.
This is the default setting, which is 0x2102.|Это значение по умолчанию - 0x2102.
All that is is a hexadecimal number.|Все это шестнадцатеричное число.
A hexadecimal number that tells it, hey,|Шестнадцатеричное число, которое говорит об этом, эй,
take a look at the NVRAM, so when I boot up, you could load any configurations, if there's any in there.|Взгляните на NVRAM, чтобы, когда я загрузился, вы могли загрузить любые конфигурации, если они там есть.
Now, there's still a lot more configurations that we'll need to do, and there's a lot more SHOW commands.|Теперь нам нужно сделать еще много настроек, и есть еще много команд SHOW.
But as we do more configurations, you will learn more SHOW commands.|Но по мере того, как мы делаем больше конфигураций, вы узнаете больше команд SHOW.
Like, let's say if you wanted to look at a show interface S0/0/0,|Например, если вы хотите посмотреть на интерфейс шоу S0 / 0/0,
that's one of the interfaces that exists here.|это один из существующих здесь интерфейсов.
It's looking at hardware information.|Он смотрит на информацию об оборудовании.
Hardware information, you see here, by the Internet address for that particular interface is 10.1.1.5.|Информация об оборудовании, которую вы видите здесь, по интернет-адресу для этого конкретного интерфейса - 10.1.1.5.
The protocol is up.|Протокол запущен.
Reliability.|Надежность.
The default encapsulation, HDLC.|Инкапсуляция по умолчанию, HDLC.
So, or you can do SHOW IP INTERFACE S 0/0.|Итак, или вы можете сделать SHOW IP INTERFACE S 0/0.
And when you do that, oops.|И когда вы это сделаете, ой.
I forgot one zero.|Я забыл один ноль.
When you do that, it'll show you, all right, IP information like, let's say, one of the things you want to look at, hey, is|Когда вы это сделаете, он покажет вам, хорошо, IP-информацию, например, скажем, одна из вещей, на которую вы хотите посмотреть, эй, это
there any access lists that are set?|есть ли списки доступа, которые установлены?
Okay?|Ладно?
That's another thing that you would look at on here.|Это еще одна вещь, на которую вы бы здесь посмотрели.
All right, so there are many show commands.|Хорошо, есть много команд шоу.
You can do show and a question mark and it will tell you exactly what is it that you're looking at.|Вы можете сделать показ и вопросительный знак, и он точно скажет вам, на что вы смотрите.
Show access list, show ARP, there's a million show commands that you can actually do, all right, just by going through this.|Показать список доступа, показать ARP, есть миллион команд шоу, которые вы действительно можете выполнить, хорошо, просто выполнив это.
All right.|Отлично.
And you can go, you know, show users to take a look if anybody's, you know,|И вы можете пойти, знаете, показать пользователям, чтобы они посмотрели, есть ли у кого-нибудь, знаете,
what users are telneted in, if you want to see your sessions, show sessions,|к каким пользователям подключены telneed, если вы хотите увидеть свои сеансы, показать сеансы,
any telnet sessions done over there.|любые сеансы telnet, сделанные там.
All right, so you can clear the telnet sessions.|Хорошо, так что вы можете очистить сеансы telnet.
So there's a lot of show commands that you would have to practice.|Так что есть много команд показа, которые вам придется практиковать.
Are you in all of them?|Вы во всех них?
No.|Нет.
You're gonna know the ones you do the most, show start, show run, show IP in brief,|Вы узнаете, какие вы делаете больше всего, показывать старт, показывать бег, вкратце показывать IP,
show protocols, show version, show flash.|показать протоколы, показать версию, показать flash.
So these are the ones that we mainly use to look at things, to look at things.|Так что это те, которые мы в основном используем, чтобы смотреть на вещи, чтобы смотреть на вещи.
I wanted to make a statement, I'm trying to think.|Я хотел сделать заявление, я пытаюсь думать.
Oh, what is the difference between show start and show run?|О, в чем разница между началом шоу и запуском шоу?
When you do a show start, you're looking at NVRAM.|Когда вы запускаете шоу, вы смотрите на NVRAM.
When you do a show run, you looking at RAM.|Когда вы делаете показ, вы смотрите на RAM.
They could be different.|Они могли быть разными.
Because if you didn't save, the run will tell you everything.|Потому что, если вы не экономили, бег вам все расскажет.
The start, you didn't copy what's in RAM to start.|Для начала вы не копировали то, что находится в ОЗУ.
So it's not going to tell you everything.|Так что это не расскажет вам всего.
So that's the reason I always do a show start, to make sure that I copy everything over to the start in case there's a power|Вот почему я всегда запускаю шоу, чтобы убедиться, что копирую все сначала, на случай, если есть сила.
outage.|отключение.
All right.|Отлично.
We are done with this lesson, so get ready for the next section for a lot more configurations to come.|Мы закончили этот урок, поэтому будьте готовы к следующему разделу, где будет гораздо больше конфигураций.
I'll see you there.|Увидимся там.
[BLANK_AUDIO]|[BLANK_AUDIO]