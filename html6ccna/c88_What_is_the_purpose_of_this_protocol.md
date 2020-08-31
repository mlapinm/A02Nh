D:\mailCloud\prjother\tmp\1\c88_What is the purpose of this protocol.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
All right, welcome back everyone.|Хорошо, с возвращением всех.
Now this particular session, we're gonna talk about a protocol called Virtual Trunking Protocol, VTP, that in the new exam really you'll, you'll see it, but|Теперь в этом конкретном сеансе мы поговорим о протоколе под названием Virtual Trunking Protocol, VTP, который вы действительно увидите на новом экзамене, вы его увидите, но
in the books they don't really talk much about it, and it didn't go away,|в книгах об этом особо не говорят, и это никуда не делось,
so you really need to know about VTP, and what is VTP?|так что вам действительно нужно знать о VTP, а что такое VTP?
VTP is the one that allows you to create.|VTP - это тот, который позволяет вам создавать.
Your VLANs that maintains naming consistency of your VLANs across your switch network,|Ваши VLAN, которые поддерживают согласованность именования ваших VLAN в сети коммутатора,
updates all your other switches.|обновляет все остальные переключатели.
So VTP does a lot of things.|Так что VTP делает много всего.
And we need to know, how to tweak VTP?|И нам нужно знать, как настроить VTP?
Let's take a, there's a lot from previous.|Возьмем, есть много из предыдущего.
Let's take a look at the VTP.|Давайте посмотрим на VTP.
[BLANK_AUDIO]|[BLANK_AUDIO]
And we'll go from there.|И мы пойдем оттуда.
Show VTP STAT or status.|Показать СТАТУС или статус VTP.
Stat for short.|Стат для краткости.
Now, what are we looking at here?|Итак, на что мы здесь смотрим?
The version of VTP, the very first thing,|Версия VTP, самое первое,
the version,|версия,
VTP version the first line, you're not really too concerned about it.|Версия VTP первая строка, вас это не особо беспокоит.
I believe I said this in an earlier lesson.|Кажется, я сказал это на предыдущем уроке.
The Configuration Revision,|Версия конфигурации,
that is something that you want to pay attention to.|это то, на что вы хотите обратить внимание.
Cuz the higher that number, the higher that number, okay.|Потому что чем выше это число, тем выше оно, хорошо.
It's the more current information.|Это более актуальная информация.
Now you can always reset it by changing the mode of the switch.|Теперь его всегда можно сбросить, изменив режим переключателя.
You can change that or by changing the domain name of the switch.|Вы можете изменить это или изменив доменное имя коммутатора.
As long as you do different things to the VLAN database it'll change that number and you can reset it back to zero.|Пока вы делаете разные вещи с базой данных VLAN, она изменяет это число, и вы можете сбросить его обратно на ноль.
All right.|Отлично.
But this is important, cuz the higher revision number, and I'll say it again.|Но это важно, потому что номер ревизии выше, и я повторю это еще раз.
The higher revision number means the more current information, so it will update all of the other switches,|Более высокий номер версии означает более актуальную информацию, поэтому он обновит все остальные переключатели,
all of the other switches with that information, even though it may not be information you want.|все другие переключатели с этой информацией, даже если она может быть вам не нужна.
[NOISE] Keep thinking about that.|[NOISE] Продолжай думать об этом.
Maximum VLANs supported locally, only 255|Максимальное количество VLAN, поддерживаемых локально, всего 255
even though you see,|хотя вы видите,
you have VLANs 2 to 2001 really that you can create.|у вас есть сети VLAN от 2 до 2001, которые вы действительно можете создать.
But if you do create,|Но если ты творишь,
try to create beyond that locally, it's gonna give you an error.|попробуйте создать что-то еще локально, это даст вам ошибку.
It's not gonna allow you to do it.|Это не позволит тебе сделать это.
All right, it shows you the number of existing VLANs.|Хорошо, он показывает количество существующих VLAN.
And the operating mode of the switch.|И режим работы переключателя.
All switches, all switches by default are operating by VTP Server.|Все коммутаторы, все коммутаторы по умолчанию работают под управлением VTP Server.
What does that mean?|Что это значит?
That means that allows you to create VLANs, to name VLANs,|Это означает, что вы можете создавать VLAN, называть VLAN,
to change VLANs, to delete VLANs.|для изменения VLAN, для удаления VLAN.
You can manipulate the VLAN database if you are a VTP Server.|Вы можете управлять базой данных VLAN, если вы являетесь VTP-сервером.
The other mode is Client mode, now also the server updates everybody obviously, all right but, and receives updates and sends updates.|Другой режим - это режим клиента, теперь сервер, очевидно, обновляет всех, но, и получает обновления, и отправляет обновления.
Client mode does the same exact thing,|Клиентский режим делает то же самое,
it just can't create Change, Rename,|он просто не может создавать изменения, переименовать,
Delete VLANs.|Удалите сети VLAN.
So, if you're in the Client mode, you can't do anything with the VLANs.|Итак, если вы находитесь в режиме клиента, вы ничего не можете сделать с виртуальными локальными сетями.
You just can send, eceive updates, but you can't change anything.|Вы просто можете отправлять, получать обновления, но вы не можете ничего изменить.
You can't manipulate the VLAN database.|Вы не можете управлять базой данных VLAN.
VTP domain name, this is something that you.|Доменное имя VTP, это то, что вы.
If now again, VTP the Virtual Trunking Protocol really just,|Если теперь еще раз, VTP Virtual Trunking Protocol действительно просто,
like STP doesn't come alive unless there's redundant links, well VTP,|как будто STP не оживает, если нет избыточных ссылок, ну VTP,
Virtual Trunking Protocol is really used when you have multiple VLANs.|Virtual Trunking Protocol действительно используется, когда у вас есть несколько VLAN.
If you're only using one VLAN you really don't,|Если вы используете только одну VLAN, на самом деле этого не делать,
you really don't need to be worried about VTP.|Вам действительно не нужно беспокоиться о VTP.
But if you have multiple VLANs, more than one VLAN, you have two VLANs,|Но если у вас несколько VLAN, более одной VLAN, у вас есть две VLAN,
then you need to go ahead, and start dealing with VTP.|тогда вам нужно пойти дальше и начать работать с VTP.
With VTP domain name, you can create a VTP domain name, and then your other switches must be in the same domain as you are, so|С доменным именем VTP вы можете создать доменное имя VTP, и тогда другие ваши коммутаторы должны быть в том же домене, что и вы, поэтому
they can receive updates.|они могут получать обновления.
If you have two switches, like or, or three switches, like we have in this lab.|Если у вас есть два переключателя, например или, или три переключателя, как у нас в этой лабораторной работе.
And they all have different VTP domain names, what's gonna happen is?|И все они имеют разные доменные имена VTP, что же произойдет?
You're gonna get a VTP domain mismatch,|Вы получите несоответствие домена VTP,
constantly.|постоянно.
But up, up, up, up it wont even allow you to type.|Но вверх, вверх, вверх, вверх он даже не позволит вам печатать.
Okay, so definitely, you want to make sure your in the same VTP domain name, and don't, it's not like a domain in DNS.|Итак, определенно, вы хотите убедиться, что вы используете одно и то же доменное имя VTP, и не делайте этого, это не похоже на домен в DNS.
Like you gotta say cisco.com, or anything like that.|Например, cisco.com или что-то в этом роде.
Just a name, you know, VTP domain Laz,|Просто имя, понимаете, VTP домен Laz,
VTP domain you know, whatever, whatever you want to call it.|Вы знаете домен VTP, как хотите, как хотите его называть.
But all those switches will operate in VTP domain.|Но все эти коммутаторы будут работать в домене VTP.
Now we always have that sneaky individual,|Теперь у нас всегда есть этот подлый человек,
we always have that sneaky individual,|у нас всегда есть этот подлый человек,
that sneaks in with their switch.|который пробирается с их выключателем.
Right, and plugs their switch in, and if you didn't set any passwords to your domain, it will update that switch with your information,|Правильно, и подключает их переключатель, и если вы не устанавливали пароли для своего домена, он обновит этот переключатель с вашей информацией,
that's something you don't want.|это то, чего ты не хочешь.
So definitely you will want to, you will like to or have to create VTP passwords as well for that particular domain.|Так что определенно вы захотите, захотите или должны будете создать пароли VTP для этого конкретного домена.
Now you do that, on a switch by switch basis, which as you can imagine the administrative headache that, that would be so, all right.|Теперь вы делаете это по принципу «переключение за переключателем», что, как вы понимаете, представляет собой головную боль администрирования, и все будет так, хорошо.
Now for us, we're just going to do VTP domain names,|Теперь для нас мы просто собираемся сделать доменные имена VTP,
we're not gonna be doing password, because again this is a simulator so it's more,|мы не собираемся вводить пароль, потому что это снова симулятор, так что это больше,
it's more of a pain, then try and take it out.|это больше похоже на боль, тогда попробуй избавиться от нее.
So you need to pay attention to that.|Так что вам нужно обратить на это внимание.
The, this right here the configuration revision one, the operating mode two,|Вот здесь первая редакция конфигурации, второй режим работы,
and the VTP domain name three, are key things that you need to look at when you're going through your examination through the switching portion of it.|и доменное имя VTP три, являются ключевыми вещами, на которые вам нужно обратить внимание, когда вы проходите экзамен через его переключающую часть.
It is important, and this print screen that you're looking at right here is extremely important.|Это важно, и этот экран печати, на который вы смотрите прямо здесь, чрезвычайно важен.
You need to know this command.|Вам нужно знать эту команду.
Show VTP status, so you can bring this up to be able to answer questions,|Показать статус VTP, чтобы вы могли поднять его, чтобы ответить на вопросы,
and down here, is how you get modified from other switches,|и вот как вы меняете другие переключатели,
all right, that send you their information.|ладно, что пришлют вам свою информацию.
So you need to make sure that you can,|Итак, вам нужно убедиться, что вы можете,
you're able to pull up this information,|вы можете получить эту информацию,
and take at look at that.|и посмотри на это.
Just remember, the commands within the switching you're using the, I, and we did in the beginning.|Просто помните, что команды в переключении, которые вы используете, I, и мы использовали в начале.
Show MAC Address Table, Show VTP Status,|Показать таблицу MAC-адресов, Показать статус VTP,
Show Spanning Tree Show CDP Neighbor, Show CDP Neighbor Detail, Showing Trunk.|Показать связующее дерево Показать соседа CDP, Показать детали соседа CDP, показать магистраль.
All of these different commands you need to be aware with,|Все эти разные команды, о которых вам нужно знать,
you need to be aware of, so when you look at information of the switch.|нужно знать, поэтому, когда вы смотрите на информацию о переключателе.
All right, so VTP though, is commonly confused with trunking or port.|Хорошо, но VTP обычно путают с транкингом или портом.
Ne, v, trunking or port, and VTP, in Windows called Virtual Trunking Protocol, that's two different things.|Ne, v, транкинг или порт, и VTP, в Windows называемый протоколом виртуального транкинга, это две разные вещи.
The Virtual Trunking Protocol, what it does?|Протокол виртуального транкинга, что он делает?
It sends information only through trunk ports, through trunk ports.|Он отправляет информацию только через магистральные порты, через магистральные порты.
Okay.|Ладно.
So if, again, if you're using more than VLAN then you should have this.|Так что, если, опять же, если вы используете больше, чем VLAN, у вас должно быть это.
Now, the operating mode there's, you know,|Итак, режим работы есть, вы знаете,
people say leave them all as servers.|люди говорят оставить их всех серверами.
Some people say have one server, and the rest of them Clients.|Некоторые говорят, что есть один сервер, а остальные - клиенты.
I'm one of them.|Я один из них.
You have one server machine there, or switch then the rest are all Clients.|У вас есть одна серверная машина, или переключитесь, тогда все остальные будут клиентами.
Now there's another operating mode that I didn't say, which was transparent.|Теперь есть еще один режим работы, о котором я не говорил, он прозрачный.
Transparent mode is exactly like Server mode,|Прозрачный режим аналогичен режиму сервера,
but it doesn't share its VLAN database information.|но он не передает информацию о своей базе данных VLAN.
It will not accept, well not accept.|Он не примет, не примет.
It won't copy the updates from other server switches into its own VLAN database.|Он не будет копировать обновления с других серверных коммутаторов в свою базу данных VLAN.
It will just forward the information across.|Он просто пересылает информацию.
And that's it.|И это все.
There usually used for remote switches,|Обычно используется для удаленных переключателей,
they have three modes that you need to be aware of Server, Client, and Transparent, but again,|у них есть три режима, о которых вам нужно знать: Сервер, Клиент и Прозрачный, но опять же,
this guy right here, this revision number your gonna see it on multiple questions.|вот этот парень, этот номер редакции, вы увидите его в нескольких вопросах.
Always remember the higher revision number is a more current information,|Всегда помните, что более высокий номер версии является более актуальной информацией,
therefore the other switches will accept its updates,|поэтому другие коммутаторы будут принимать его обновления,
but he will not accept anybody else's updates, because he's the most current.|но он не будет принимать чужие обновления, потому что он самый последний.
But he has to be in the same domain as the rest of you.|Но он должен быть в той же сфере, что и все вы.
If not that would be an issue so VTP is extremely important cuz if I were to change this right now to VTP,|Если бы не это было бы проблемой, поэтому VTP чрезвычайно важен, потому что если бы я прямо сейчас изменил это на VTP,
cuz I can create a VLAN,|потому что я могу создать VLAN,
just to show you as an example, CONFIG T VLAN10,|просто чтобы показать вам в качестве примера, CONFIG T VLAN10,
NAME LAZ, right that's a VLAN.|ИМЯ LAZ, верно, это VLAN.
When I look, what I'm gonna do?|Когда я посмотрю, что я буду делать?
I'm going to change the VTP mode to Client, and we can verify that by doing DO SHow VTP STAT, all right.|Я собираюсь изменить режим VTP на Client, и мы можем проверить это, выполнив DO SHow VTP STAT, хорошо.
Now we're a Client you see the change look at the revision number,|Теперь мы клиент, вы видите изменение, посмотрите на номер версии,
it changed to two right we created a VLAN,|он изменился на два, мы создали VLAN,
and now, I'm Client.|а теперь я клиент.
Now I'm going to try and create another VLAN.|Теперь я попробую создать еще одну VLAN.
VLAN 20, VTP VLAN configuration not allowed when device is in Client mode.|VLAN 20, VTP Конфигурация VLAN не разрешена, когда устройство находится в режиме клиента.
So really, what allows you, what allows you to create these VLANs,|Итак, действительно, что позволяет, что позволяет создавать эти VLAN,
is the mode that your switch is in.|это режим, в котором находится ваш коммутатор.
The operating mode, the VTP operating mode of the switch.|Режим работы, режим работы коммутатора VTP.
So in order to create VLANs, you must be in VTP server mode in order to do that, and you can see it right here.|Таким образом, чтобы создать VLAN, вы должны быть в режиме VTP-сервера, чтобы сделать это, и вы можете увидеть это прямо здесь.
All right, so VTP is extremely important,|Итак, VTP чрезвычайно важен,
and again, naming consistency which means,|и снова, называя последовательность, что означает,
which also means, if you have your native VLAN, that's VLAN 1 over here.|что также означает, что если у вас есть собственная VLAN, это VLAN 1 здесь.
But the switch over here, it's native VLAN is VLAN 20.|Но вот коммутатор, его собственная VLAN - это VLAN 20.
You're gonna have a mismatch of native VLANs, and you're gonna run into an issue.|У вас будет несоответствие собственных VLAN, и вы столкнетесь с проблемой.
That's why, you just can't get, you know,|Вот почему вы просто не можете понять,
all these switches that just came in, and you start throwing them out there, and you start plugging things in, and start configuring.|все эти переключатели, которые только что вошли, и вы начинаете их выбрасывать, и вы начинаете подключать вещи, и начинаете настраивать.
No.|Нет.
There's already got to be a blueprint designed from you on,|Уже должен быть план, разработанный вами,
how this infrastructure's gonna look like?|как эта инфраструктура будет выглядеть?
Down to the IP address, the VTP,|Вплоть до IP-адреса, VTP,
everything.|все.
What's gonna be configured?|Что собираетесь настраивать?
What is your idea and when it's gonna happen?|Какова ваша идея и когда это произойдет?
So you just can't put the things together.|Так что вы просто не можете сложить все вместе.
But for your certification ladies and gentlemen, this screen right here, very important with the revision number and and again the modes, and stuff like that.|Но для вашей сертификации, дамы и господа, вот этот экран, очень важный с номером версии, режимами и тому подобным.
So VTP should not be, may not be in the books that you see now, but it's most definitely, very much alive.|Так что VTP не должно быть, может и не быть в книгах, которые вы сейчас видите, но он определенно очень живой.
As you can see, you can't create a VLAN unless you are in VTP server.|Как видите, вы не можете создать VLAN, если не находитесь на сервере VTP.
And if you don't know about VTP, how would you know how to fix that?|А если вы не знаете о VTP, как бы вы узнали, как это исправить?
So, VTP is here to stay.|Итак, VTP здесь, чтобы остаться.
Okay, it's here to stay.|Хорошо, он здесь, чтобы остаться.
So again, that's VTP.|Опять же, это VTP.
This is how you look at it?|Это как ты на это смотришь?
Those are the key points you need to look at.|Это ключевые моменты, на которые вам нужно обратить внимание.
We will be configuring VTP,|Будем настраивать VTP,
we will be configuring VLANs, and your going to see how I do it?|мы будем настраивать VLAN, и вы увидите, как я это сделаю?
Not the way like in the, in the book,|Не так, как в книге,
I'm gonna show you the way I would do,|Я покажу тебе, как бы я поступил,
where I would create my VLANs?|где я бы создал свои VLAN?
And then I would have manipulate my spanning tree,|И тогда я бы манипулировал своим остовным деревом,
and then I will create a VTP domain.|а затем я создам домен VTP.
I won't put a password on it.|Я не буду ставить на него пароль.
But I will put a VTP domain, and I will change my others to Clients,|Но я поставлю домен VTP, а остальные поменяю на Клиентов,
and you'll see, how I'm going to do that?|и вы увидите, как я собираюсь это сделать?
In the next lesson.|В следующем уроке.
So I'll see you there.|Так что увидимся там.