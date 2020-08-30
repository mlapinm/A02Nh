D:\mailCloud\prjother\tmp\1\c09_Configuring a switch.md  


__|__
--|--
Okay, next device on the list, what is it?|Хорошо, следующее устройство в списке, что это?
The switch.|Выключатель.
Remember it went from top to bottom.|Помните, что все шло сверху вниз.
A little different than how I do it, but that's okay.|Немного отличается от того, как я это делаю, но это нормально.
Now, switches, you really don't need to configure, you really don't,|Теперь переключатели, вам действительно не нужно настраивать, вам действительно не нужно,
they they work all by themselves, but the only reason you would configure it is because you want to manage them, and you do want to manage them.|они работают сами по себе, но вы бы настроили их только потому, что вы хотите управлять ими, и вы действительно хотите управлять ими.
You do not want buy unmanaged switches.|Вы не хотите покупать неуправляемые коммутаторы.
You want to be able to go in there so you can create VLANs,|Вы хотите иметь возможность войти туда, чтобы вы могли создавать VLAN,
VTP domains, you can tweak the estimated STP.|VTP домены, вы можете настроить предполагаемый STP.
You can do a whole bunch of different things on switches,|На переключателях можно делать кучу разных вещей,
access lists, port security, all these different things.|списки доступа, безопасность портов, все эти разные вещи.
So what we're gonna do is, we're gonna go inside the switch.|Итак, что мы собираемся сделать, мы войдем в выключатель.
We're gonna assign, obviously we're gonna give it a host name.|Мы собираемся назначить, очевидно, мы дадим ему имя хоста.
We're gonna assign two, two major important things.|Мы назначим две, две важные вещи.
One, we're gonna give it an IP address,|Во-первых, мы дадим ему IP-адрес,
and two,|и два,
we're gonna give it a default gateway.|мы дадим ему шлюз по умолчанию.
Those items right there are extremely important because in order to get into the switch, you do an IP address, and in order to remotely get into the switch,|Эти элементы чрезвычайно важны, потому что для доступа к коммутатору вы используете IP-адрес, а для удаленного доступа к коммутатору,
you need a default gateway.|вам нужен шлюз по умолчанию.
So let's go ahead and do that now.|Так что давайте продолжим и сделаем это сейчас.
Let's go into the switch, and I'll bring it where you guys can see that.|Пойдем к переключателю, и я отнесу его туда, где вы, ребята, это увидите.
Not that way.|Не так.
[SOUND] Right there.|[ЗВУК] Прямо здесь.
And let's wind this out.|И давайте закончим это.
[BLANK_AUDIO]|[BLANK_AUDIO]
There we go.|Вот и все.
So we got the CLI.|Итак, мы получили CLI.
All right, so the first one we gonna do,|Хорошо, так что первым, что мы сделаем,
is we gonna give it a name.|мы дадим ему имя.
Enable config T.|Включите config T.
Host name will get a very generic name.|Имя хоста получит очень общее имя.
Switch 1.|Переключатель 1.
All right, now we're going to give it an IP address.|Хорошо, теперь мы дадим ему IP-адрес.
All right, so we give the IP address to the VLAN.|Хорошо, поэтому мы даем IP-адрес VLAN.
All switches by default, or all, they all have VLAN 1.|Все коммутаторы по умолчанию или все они имеют VLAN 1.
So you're going to INT VLAN 1, it acts as an interface,|Итак, вы идете к INT VLAN 1, он действует как интерфейс,
and we'll go IP ADDRESS 192.168.|и мы пойдем IP-АДРЕС 192.168.
Whoa.|Ого.
Forgot the dot there.|Забыл точку там.
Going too fast for my own good.|Слишком быстро для моего же блага.
.1.253, [SOUND] space 255.255.255.0.|.1.253, [ЗВУК] пробел 255.255.255.0.
All right, so now we've assigned VLAN 1 an IP address,|Хорошо, теперь мы назначили VLAN 1 IP-адрес,
which is the IP address of the switch.|который является IP-адресом коммутатора.
That's how we would access the switch.|Вот как мы получим доступ к переключателю.
If we were within that same network.|Если бы мы были в той же сети.
Now what if we're in a different network?|Что, если мы находимся в другой сети?
What if we remote to the switch?|Что, если мы подключимся к коммутатору?
As per Cisco, we need to have a default gateway.|Согласно Cisco, нам нужен шлюз по умолчанию.
Well, what's our default gateway for this particular switch?|А какой у нас шлюз по умолчанию для этого коммутатора?
Our router.|Наш роутер.
But in order to put the gateway, we have to be in global configuration.|Но чтобы поставить шлюз, мы должны быть в глобальной конфигурации.
Don't fret.|Не волнуйся.
Don't fret.|Не волнуйся.
Once we start doing the configurations,|Как только мы приступим к настройке,
all these different modes will come easily.|все эти различные режимы будут легко доступны.
I'm gonna exit one time, go back to global configuration, and I'm gonna put IP address, and as the address of the actual F00, that's the gateway.|Я выйду один раз, вернусь к глобальной конфигурации, и я поставлю IP-адрес, и в качестве адреса фактического F00 это шлюз.
192.168.1.254.|192.168.1.254.
At, what?|Что?
[BLANK_AUDIO]|[BLANK_AUDIO]
I made a mistake here.|Я ошибся здесь.
Oh, I may have forgot IP?|О, может я IP забыл?
Hm.|Хм.
Address?|Адрес?
Oh.|Ой.
When in doubt, question mark.|В случае сомнений - вопросительный знак.
There is the word IP, so IP,|Есть слово IP, значит IP,
and, and this switch, I don't see the address.|и этот переключатель, я не вижу адреса.
Because you don't need it.|Потому что тебе это не нужно.
It's IP default gateway.|Это IP-шлюз по умолчанию.
Excuse me, IP default gateway.|Простите, шлюз по умолчанию IP.
That's what we said we're going to assign [LAUGH].|Это то, что мы сказали, что собираемся назначить [СМЕХ].
IP default gateway, 192.168.1.254.|Шлюз по умолчанию IP, 192.168.1.254.
There we go.|Вот и все.
So when in doubt, when you're, hey,|Поэтому, когда сомневаешься, когда ты, эй,
confused,|смущенный,
a question mark will always save you.|вопросительный знак всегда спасет вас.
Now, I have heard that in the test you can type a question mark and you can actually see the commands that are there.|Я слышал, что в тесте вы можете ввести вопросительный знак, и вы действительно можете увидеть команды, которые там есть.
But, again, I'm thinking IP address, and that's why that happens.|Но, опять же, я думаю об IP-адресе, и вот почему это происходит.
So, now we've actually assigned, and I did Ctrl-Z just now.|Итак, теперь мы фактически назначили, и я только что нажал Ctrl-Z.
And, I wanna do, just a show show run.|И, я хочу, просто шоу-шоу.
Okay?|Ладно?
Just to take a look at what I have, and now, I really haven't done much, but there's my IP address for the VLAN, and there's my default gateway.|Просто чтобы взглянуть на то, что у меня есть, и теперь я действительно мало что сделал, но есть мой IP-адрес для VLAN и мой шлюз по умолчанию.
I haven't done any other configuration besides the host name of switch one.|Я не выполнял никаких других настроек, кроме имени хоста первого переключателя.
So there's a lot more configurations to be done.|Так что предстоит еще многое сделать.
We're just doing something very simple,|Мы просто делаем что-то очень простое,
very easy.|очень просто.
But those two right there, the default gateway and the IP address for VLAN 1,|Но вот эти два, шлюз по умолчанию и IP-адрес для VLAN 1,
are extremely important because you need to access your switches, so you can manage your switches and you can tweak your switches the way you want them to work.|чрезвычайно важны, потому что вам нужен доступ к своим коммутаторам, поэтому вы можете управлять своими коммутаторами и настраивать коммутаторы так, как вы хотите, чтобы они работали.
And in order for you to remotely get to your switches, you need that gateway,|И для того, чтобы вы могли удаленно добраться до своих коммутаторов, вам нужен этот шлюз,
you need that gateway, all right?|вам нужен этот шлюз, хорошо?
Well, that's it, oh, one last thing I forgot, I forgot.|Ну вот и все, последнее, что я забыл, я забыл.
Remember how I said that the router's interfaces by default were turned off?|Помните, я говорил, что интерфейсы роутера по умолчанию отключены?
Well guess what, the VLAN 1 by default is turned off,|Ну угадайте, VLAN 1 по умолчанию выключен,
so you need to do a no shut within VLAN 1.|поэтому вам нужно не закрывать сеть VLAN 1.
So if you always forget a command, you can always go back into where you were, and just do whatever command you forgot to do|Итак, если вы всегда забываете команду, вы всегда можете вернуться туда, где вы были, и просто выполнить ту команду, которую вы забыли сделать.
and it'll take it.|и это займет.
So now we're good to go.|Итак, теперь мы в порядке.
Now we're okay.|Теперь все в порядке.
So we got an IP address for the switch, we got a default gateway for the switch, and we got a name for the switch.|Итак, у нас есть IP-адрес для коммутатора, у нас есть шлюз по умолчанию для коммутатора и мы получили имя для коммутатора.
Very simple, very easy.|Очень просто, очень просто.
Not much to do there.|Делать там особо нечего.
It's a lot to do later on, but for right now, this is it.|Позже предстоит еще много работы, но сейчас это все.
So, next lesson, guess what we're gonna do.|Итак, следующий урок, угадайте, что мы будем делать.
We're gonna do the PC's.|Мы собираемся делать компьютеры.
That's gonna be the next, lesson that we're gonna do.|Это будет следующий урок, который мы собираемся сделать.
We're gonna configure the PCs, and we're gonna verify connectivity.|Мы собираемся настроить компьютеры и проверить подключение.
I'll see you there.|Увидимся там.
[BLANK_AUDIO]|[BLANK_AUDIO]
[BLANK_AUDIO]|[BLANK_AUDIO]
Okay, next device on the list, what is it?|Хорошо, следующее устройство в списке, что это?
The switch, cuz remember, we're going from top to bottom.|Выключатель, помните, мы идем сверху вниз.
Little different than how I do it, but that's okay.|Немного отличается от того, как я это делаю, но это нормально.
Now, switches you really don't need to configure.|Теперь переключатели, которые вам действительно не нужно настраивать.
You really don't.|Вы действительно этого не делаете.
They they work all by themselves, but the only reason you would configure it is because you want to manage them.|Они работают сами по себе, но вы бы их настраивали только потому, что вы хотите ими управлять.
And you do want to manage them.|И вы хотите ими управлять.
You do not want to buy unmanaged switches.|Вы не хотите покупать неуправляемые коммутаторы.
You want to be able to go in there so you can create VLANs, VTP Domains,|Вы хотите иметь возможность войти туда, чтобы вы могли создавать VLAN, домены VTP,
you can tweak the STP.|вы можете настроить STP.
You can do a whole bunch of different things on switches,|На переключателях можно делать кучу разных вещей,
access lists, port security, all these different things.|списки доступа, безопасность портов, все эти разные вещи.
So what we're gonna do is we're gonna go inside the switch,|Итак, что мы собираемся сделать, мы войдем в переключатель,
we're gonna assign obviously, we're gonna give it a host name.|мы собираемся назначить, очевидно, мы дадим ему имя хоста.
There's, like, two, two major, important things.|Есть две, две важные вещи.
One, we're gonna give it an IP address,|Во-первых, мы дадим ему IP-адрес,
and two,|и два,
we're gonna give it a default gateway.|мы дадим ему шлюз по умолчанию.
Those items right there are extremely important,|Эти предметы очень важны,
because in order to get into the switch,|потому что для того, чтобы попасть в переключатель,
you need an IP address.|вам нужен IP-адрес.
And in order to remotely get into the switch, you need a default gateway.|А чтобы удаленно попасть в коммутатор, нужен шлюз по умолчанию.
So let's go ahead and do that now.|Так что давайте продолжим и сделаем это сейчас.
Let's go into the switch, and I'll bring it where you guys can see that.|Пойдем к переключателю, и я отнесу его туда, где вы, ребята, это увидите.
Not that way.|Не так.
[NOISE] Right there.|[ШУМ] Прямо здесь.
And let's wind this out.|И давайте закончим это.
[BLANK_AUDIO].|[BLANK_AUDIO].
There we go.|Вот и все.
So we got the CLI.|Итак, мы получили CLI.
All right so the first thing we're going to do is give it a name.|Хорошо, поэтому первое, что мы сделаем, это дадим ему имя.
Enable config T.|Включите config T.
Host name, we'll get a very generic name,|Имя хоста, мы получим очень общее имя,
switch one.|переключить один.
All right.|Отлично.
Now we're gonna give it an IP address.|Теперь мы дадим ему IP-адрес.
All right, so, we give the IP address to the VLAN.|Итак, мы даем IP-адрес VLAN.
All switches by default were all, they all have VLAN 1.|Все свитчи по умолчанию были у всех, у всех VLAN 1.
So you go into Int VLAN1.|Итак, вы заходите в Int VLAN1.
It acts as an interface and we go IP address 192 then 168 wow forgot the dot there.|Он действует как интерфейс, и мы идем по IP-адресу 192, затем 168, ничего себе забыл там точку.
I'm going to fast for my own good.|Я буду поститься ради собственного блага.
Then 1.253.|Тогда 1.253.
[BLANK_AUDIO]|[BLANK_AUDIO]
Space 255.255.255.0 all right?|Пробел 255.255.255.0 все в порядке?
So now we've assigned vLAN 1 an IP address,|Итак, теперь мы назначили vLAN 1 IP-адрес,
which is the IP address of the switch.|который является IP-адресом коммутатора.
That's how we would access the switch.|Вот как мы получим доступ к переключателю.
If we were within that same network.|Если бы мы были в той же сети.
Now, what if we're in a different network?|А что, если мы находимся в другой сети?
What if we're remote to the switch?|Что, если мы удалены от коммутатора?
As per Cisco, we need to have a default gateway.|Согласно Cisco, нам нужен шлюз по умолчанию.
What's our default gateway for this particular switch?|Какой у нас шлюз по умолчанию для этого конкретного коммутатора?
Our router.|Наш роутер.
But in order to put the gateway we have to be in global configuration.|Но чтобы поставить шлюз, мы должны быть в глобальной конфигурации.
Don't fret, don't fret.|Не волнуйся, не волнуйся.
Once we start doing the configurations,|Как только мы приступим к настройке,
all these modes will come easily.|все эти режимы придутся легко.
I'm going to exit one time, and go back to global configurations.|Я собираюсь выйти один раз и вернуться к глобальным настройкам.
And I'm going to put IP address, and as the address of the actual f:0:0.|И я собираюсь поставить IP-адрес, а в качестве адреса фактического f: 0: 0.
That's the gateway.|Это шлюз.
192.168.1.254.|192.168.1.254.
Et, what?|Эт, что?
I have made a mistake here.|Я ошибся здесь.
Oh, I may have forgot IP mm, address no?|Ой, возможно я забыл IP мм, адрес нет?
When in doubt, here is the word IP,|Если вы сомневаетесь, вот слово IP,
so IP and, and this switch,|так что IP и этот переключатель,
I don't see the address.|Я не вижу адреса.
Because you don't need it.|Потому что тебе это не нужно.
It's IP default gateway.|Это IP-шлюз по умолчанию.
Excuse me.|Прошу прощения.
IP default gateway.|Шлюз по умолчанию IP.
That's what we said we were gonna assign.|Это то, что мы обещали назначить.
[LAUGH] IP default gateway 192, then 168.|[СМЕХ] IP-шлюз по умолчанию 192, затем 168.
You got 1.254.|У вас 1,254.
There we go.|Вот и все.
So when in doubt, when you're confused, a question mark will always save you.|Так что, если вы сомневаетесь, когда вы запутались, вопросительный знак всегда спасет вас.
Now, I have heard that in the test you can type a question mark and you can actually see the commands that are there.|Я слышал, что в тесте вы можете ввести вопросительный знак, и вы действительно можете увидеть команды, которые там есть.
But, again I'm thinking IP address and that's what I have.|Но, опять же, я думаю об IP-адресе, и это то, что у меня есть.
So now we've actually assigned a control Z just now.|Итак, мы только что назначили элемент управления Z.
And I wanna do just a show show run,|И я хочу устроить шоу-шоу,
okay, just to take a look at what I have.|хорошо, просто чтобы взглянуть на то, что у меня есть.
And now I really haven't done much, but there's my IP address for the VLAN and there's my default gateway.|И теперь я действительно мало что сделал, но есть мой IP-адрес для VLAN и мой шлюз по умолчанию.
Haven't done any other configuration besides the host name.|Никаких других настроек, кроме имени хоста, не выполнялось.
I'll switch one.|Я поменяю одну.
So there's a lot more configurations to be done.|Так что предстоит еще многое сделать.
We're just doing something very simple.|Мы просто делаем что-то очень простое.
Very easy.|Очень просто.
But those two right there, the default gateway and the IP address for b.1, are extremely important.|Но эти два, шлюз по умолчанию и IP-адрес для b.1, чрезвычайно важны.
Because you need to access your switches,|Потому что вам нужен доступ к своим переключателям,
so you can manage your switches.|так что вы можете управлять своими переключателями.
So you can tweak your switches the way you want them to work.|Таким образом, вы можете настроить свои переключатели так, как вы хотите, чтобы они работали.
And in order for you to remotely get to your switches you need that gateway.|И чтобы вы могли удаленно подключаться к коммутаторам, вам нужен этот шлюз.
You need that gateway.|Вам нужен этот шлюз.
All right?|Отлично?
Well that's it.|Ну вот и все.
Oh, one last thing I forgot.|О, последнее, что я забыл.
I forgot,|Я забыл
remember how I said that the routers interfaces by default were turned off?|помните, как я говорил, что интерфейсы роутеров по умолчанию отключены?
Well guess what?|Ну что ж?
The VLAN 1 by default is turned off.|Сеть VLAN 1 по умолчанию отключена.
So you need to do a no shut within [SOUND]|Поэтому вам нужно не закрывать [ЗВУК]
VLAN 1.|VLAN 1.
So if you always forget a command, you can always go back in to where you were, and just do whatever command you forgot to do,|Поэтому, если вы всегда забываете команду, вы всегда можете вернуться туда, где вы были, и просто выполнить ту команду, которую вы забыли сделать,
and it will take it.|и это займет.
[SOUND] So now we're good to go.|[ЗВУК] Итак, мы в порядке.
Now we're okay.|Теперь все в порядке.
So we got an IP address.|Итак, мы получили IP-адрес.
We got a default gate for the switch, and we got a name for the switch.|У нас есть шлюз по умолчанию для переключателя, и у нас есть имя для переключателя.
Very simple, very easy, not much to do there,|Очень просто, очень легко, там особо нечего делать,
it's a lot to do later on, but for right now this is it.|это еще много нужно сделать позже, но сейчас это все.
So next lesson guess what we're gonna do,|Итак, на следующем уроке угадайте, что мы будем делать,
we're gonna do the PC's.|мы собираемся делать компьютеры.
That's gonna be the next r lesson that we're gonna do,|Это будет следующий урок, который мы сделаем,
we're gonna configure a PC's I wanna verify connectivity.|мы собираемся настроить ПК. Я хочу проверить подключение.
I'll see you there.|Увидимся там.
[BLANK_AUDIO]|[BLANK_AUDIO]