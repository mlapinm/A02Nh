D:\mailCloud\prjother\tmp\1\c63_Configuring static host tables.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
All right everyone, we got the ACP, we got admins,|Хорошо, у нас есть ACP, у нас есть админы,
we got a whole bunch of stuff, right?|у нас есть куча всего, не так ли?
One last thing here we're gonna talk about is name resolution.|И последнее, о чем мы собираемся поговорить, - это разрешение имен.
Now when we did our ad- admin configs, I mean.|Я имею в виду, когда мы сделали наши настройки админа.
Whoops.|Упс.
And we open up our router here.|И здесь мы открываем наш роутер.
Let's maximize it.|Давайте максимизировать это.
Okay.|Ладно.
And we see that there, user name, LDiaz.|И мы видим, что там имя пользователя LDiaz.
And then Cisco.|А потом Cisco.
[BLANK_AUDIO]|[BLANK_AUDIO]
Show start.|Показать начало.
You see we did some DNS, we set up the router.|Вы видите, мы сделали DNS, мы настроили маршрутизатор.
So actually look for DNS when we want to resolve a name or have you.|Так что на самом деле ищите DNS, когда мы хотим разрешить имя или вас.
But obviously that means you'll need to configure a DNS server with hostnames in order for it to, let's say you want to ping your router by name.|Но, очевидно, это означает, что вам нужно настроить DNS-сервер с именами хостов, чтобы он мог, скажем, пинговать свой маршрутизатор по имени.
You configure the main in call cisco.com.|Главное настраиваете в вызове cisco.com.
And then within that cisco.com you create a hostrecord R1.cisco.com will be the fully qualified domain name.|Затем в этом cisco.com вы создаете запись хоста R1.cisco.com будет полным доменным именем.
And you associate that host A record with the IP address on the router.|И вы связываете эту запись хоста A с IP-адресом на маршрутизаторе.
So you're gonna do it through DNS.|Итак, вы собираетесь делать это через DNS.
What we're gonna do is, we're gonna go IP host tables.|Мы собираемся перейти к таблицам IP-хостов.
Now IP host tables are statically assigned.|Теперь таблицы IP-хостов назначаются статически.
I mean, meaning you actually do static mappings of a name to an IP address,|Я имею в виду, что вы действительно делаете статическое сопоставление имени с IP-адресом,
a name to an IP address.|имя в IP-адрес.
That will work just fine in a very small medium size network, but in a very large enterprise DNS definitely would be the way to go.|Это будет прекрасно работать в очень маленькой сети среднего размера, но в очень большом предприятии DNS определенно будет подходящим вариантом.
But again, I'm gonna show you how to go ahead and, do host tables.|Но опять же, я собираюсь показать вам, как действовать дальше и делать таблицы хостов.
Very simple.|Очень просто.
All right.|Отлично.
We're gonna go to global configuration.|Мы собираемся перейти к глобальной настройке.
We only got two routers but there's not that much we gotta type in anyway.|У нас только два маршрутизатора, но в любом случае нам не так уж много нужно вводить.
So IP host and then we do let's say R1,|Итак, IP-хост, а затем, скажем, R1,
ourselves,|мы сами,
and the IP addresses that are associated with us.|и связанные с нами IP-адреса.
In this case, it would be 192.168.1.254,|В этом случае это будет 192.168.1.254,
and believe version 10.1.1.5.|и верю версии 10.1.1.5.
I'll check in a second.|Я проверю через секунду.
IP host, R2 and then it would be 192.168.2.254 and then 10.1.1.1.6.|IP-хост, R2, затем будет 192.168.2.254, а затем 10.1.1.1.6.
That's all you really DWR, yes I'm doing shortcuts again.|Это все, что вы действительно DWR, да, я снова делаю ярлыки.
That's really all you need to do.|Это действительно все, что вам нужно сделать.
You can do the same exact thing on the other router.|Вы можете сделать то же самое на другом маршрутизаторе.
I'm going to go and verified the IP addresses.|Я пойду и проверим IP-адреса.
Do exactly, yeah okay.|Делай точно, да ладно.
So using 192.1.254, 204,|Итак, используя 192.1.254, 204,
and we got a 5 and then we got a 6 over here, and that's where I put yes.|и у нас есть 5, а затем у нас здесь 6, и вот где я поставил да.
[BLANK_AUDIO]|[BLANK_AUDIO]
Five for me, six for them.|Пять для меня, шесть для них.
Okay, that's cool.|Хорошо, это круто.
Let's go ahead and go to the other router.|Давайте перейдем к другому маршрутизатору.
Let's do the same thing, Ctrl + C, all right?|Давайте сделаем то же самое, Ctrl + C, хорошо?
We're gonna do config T, IP host, and then the host thing,|Мы собираемся настроить T, IP-хост, а затем хост,
duh, R2, IP associated with it, 10, match it up right.|да, R2, связанный с ним IP, 10, совпадите правильно.
192.168.1.254 10.1.1.6, okay?|192.168.1.254 10.1.1.6, ладно?
And that's the other three is 02, and we're gonna go IP host,|Остальные три - 02, и мы собираемся перейти на IP-хост,
R1 192.168.1, oh, [NOISE] look what I did.|R1 192.168.1, ох, [ШУМ] посмотри, что я сделал.
So it should have been 2.254 So I'll say no because you can't overwrite it.|Значит, должно было быть 2.254. Я скажу нет, потому что вы не можете его перезаписать.
If I were to write something different it will amend it.|Если я напишу что-то другое, это исправит.
So you really have to get rid of it.|Так что от этого действительно нужно избавиться.
So I get rid of that entry by putting no in front of it and redoing it.|Поэтому я избавляюсь от этой записи, ставя перед ней «нет» и переделывая ее.
Then I'm just gonna edit it and change that one to a two.|Тогда я просто отредактирую его и поменяю одно на два.
And then gonna go IP host R1,|И затем перейду на IP-хост R1,
192.168.1.254 10.1.1.5.|192.168.1.254 10.1.1.5.
Okay?|Ладно?
DWR, let's do a Ctrl + Z.|DWR, давайте сделаем Ctrl + Z.
Let's take a look at our start.|Давайте посмотрим на наше начало.
And you see your host tables are right there.|И вы видите, что ваши хост-таблицы прямо здесь.
So, we got our host, R1, 1, 1.254, 1.5 and R2, 254, 10.1.1.6.|Итак, у нас есть хост, R1, 1, 1.254, 1.5 и R2, 254, 10.1.1.6.
So instead of actually pinging it, I won't be able,|Поэтому вместо того, чтобы пинговать его, я не смогу,
because we have no routing protocol.|потому что у нас нет протокола маршрутизации.
All right, so we won't be able to get,|Хорошо, мы не сможем получить,
you know, anywhere else beyond where we're connected to.|знаете, где угодно, кроме того, с чем мы связаны.
So if I just ping R1, I should be able to ping my neighbor address.|Так что, если я просто пингую R1, я смогу пинговать адрес моего соседа.
Now what happens sometimes with this,|Что с этим иногда случается,
since the first IP address that I chose was VLAN.|поскольку первый IP-адрес, который я выбрал, был VLAN.
Because since we are not routing,|Поскольку, поскольку мы не маршрутизируем,
it's not going to work so this is what I am going to do.|это не сработает, поэтому я собираюсь это сделать.
And again, the only reason I was doing this cuz I'm not going to get rid of the host table and put it back in.|И снова, единственная причина, по которой я делал это, потому что я не собираюсь избавляться от таблицы хостов и вставлять ее обратно.
I'm just going to do a really quick default route IP default no not network IP route 0.0.0.0 cuz it's just pretty simple.|Я просто собираюсь сделать действительно быстрый IP-маршрут по умолчанию, а не сетевой IP-маршрут 0.0.0.0, потому что это довольно просто.
And then, my exit interface on router two should be as 0.0.0.1.|И тогда мой выходной интерфейс на втором маршрутизаторе должен быть 0.0.0.1.
And when we get to routing, you'll understand what I'm doing.|И когда мы перейдем к маршрутизации, вы поймете, что я делаю.
Because I will explain it obviously.|Потому что я объясню это явно.
That's 0/0/1 DWR I'm gonna do the same thing for the other one.|Это 0/0/1 DWR. Я сделаю то же самое для другого.
So since there was no routing, since there was no routing and the first address that I put for him to resolve was the LAN|Итак, поскольку не было маршрутизации, поскольку не было маршрутизации, и первым адресом, который я поставил ему для разрешения, был LAN
address, that's why it couldn't.|адрес, поэтому не мог.
So I should have put the, if I would have put the WAN address,|Так что я должен был поставить, если бы я поставил адрес WAN,
the one that they're connected to, it would've been okay.|тот, с которым они связаны, было бы хорошо.
I wasn't about to do that again.|Я не собирался делать это снова.
So, IP route 000000, whoops,|Итак, IP-маршрут 000000, упс,
0000 and the interface as 0/00.|0000 и интерфейс как 0/00.
When we get to this, when we get to routing, I'll explain that command.|Когда мы дойдем до этого, когда мы перейдем к маршрутизации, я объясню эту команду.
And again, let's try and ping.|И снова попробуем пинговать.
Well, le's go back to Router 2 and that was the original router that we did it on [COUGH].|Что ж, давайте вернемся к маршрутизатору 2, и это был оригинальный маршрутизатор, на котором мы это сделали [COUGH].
Let's maximize it, Control + Z.|Давайте развернем его, Control + Z.
Control + Z.|Ctrl + Z.
Ping R1.|Пинг R1.
And now we can ping it.|И теперь мы можем пинговать его.
Now we can ping it.|Теперь мы можем пинговать его.
And the only reason we can ping it is because we added a default route.|И единственная причина, по которой мы можем пинговать его, - это то, что мы добавили маршрут по умолчанию.
If I have this again In the order that I did it,|Если у меня это снова будет в том порядке, в котором я это сделал,
we just elaborate a little bit more on that if I didn't make myself clear.|мы просто немного подробнее остановимся на этом, если я не буду ясно выражаться.
Since the first IP address that I told the router to look for this particular host was the LAN interface.|Поскольку первым IP-адресом, который я сказал маршрутизатору искать этот конкретный хост, был интерфейс LAN.
Was the LAN interface.|Был интерфейс LAN.
Okay?|Ладно?
Well, it can't find the LAN interface cuz it's not routing.|Ну, он не может найти интерфейс LAN, потому что он не маршрутизирует.
It doesn't see it.|Он этого не видит.
And it should've defaulted to the second IP address, but it didn't.|И он должен был по умолчанию использовать второй IP-адрес, но этого не произошло.
It's again, it's a simulator.|Это снова симулятор.
That's why you put more than one address,|Вот почему вы указываете более одного адреса,
so that if one fails, it'll go to the next one, the next one, the next one.|так что, если один выйдет из строя, он перейдет к следующему, следующему, следующему.
But, if I were to turn this around, and were to put 10.1.1.5 first and then 1.2.5.4 then we wouldn't have an issue.|Но если бы я перевернул это и поставил сначала 10.1.1.5, а затем 1.2.5.4, у нас не было бы проблем.
It would've pinged right away.|Сразу бы пинговали.
But that's okay cuz we just did our quick default route.|Но это нормально, потому что мы просто проложили наш быстрый маршрут по умолчанию.
And then now it knows where to go back and forth.|И теперь он знает, куда идти вперед и назад.
Cuz really, if you want it to now since we have that default route,|На самом деле, если вы хотите это сейчас, поскольку у нас есть этот маршрут по умолчанию,
I can actually ping,|Я действительно могу пинговать,
[BLANK_AUDIO]|[BLANK_AUDIO]
And let me move this this way.|И позвольте мне двигаться вот так.
I can actually ping, from one computer to the other.|Я действительно могу пинговать с одного компьютера на другой.
Ping 192.168.2.1.|Пинг 192.168.2.1.
Come on, don't make me look bad.|Давай, не заставляй меня плохо выглядеть.
There you go.|Вот так.
All right?|Отлично?
And but once again, that's default routing.|И опять же, это маршрутизация по умолчанию.
Once we get to routing you'll learn all the secrets.|Как только мы перейдем к маршрутизации, вы узнаете все секреты.
All right?|Отлично?
So that is what a host table is.|Вот что такое хост-таблица.
All right, and again, if you want to look and see your connections and all that, you can, there is a show host I believe command.|Хорошо, и еще раз, если вы хотите посмотреть и увидеть свои соединения и все такое, вы можете, я верю, что есть команда show host.
Yeah, there it is right there.|Да, вот оно и есть.
Show hosts.|Показать хозяев.
And you can see that it will show you the permanent resolutions for router one to the IP addresses,|И вы можете видеть, что он покажет вам постоянные разрешения для IP-адресов первого маршрутизатора,
the mappings of the host name to the IP addresses.|сопоставления имени хоста с IP-адресами.
And if DNS would have actual entries to it, it would show you the DNS,|И если в DNS будут фактические записи, он покажет вам DNS,
temporary DNS entries in there as well,|временные записи DNS также там,
the show host command.|команда show host.
All right?|Отлично?
That's it.|Вот и все.
That's all static tables static host tables are.|Это все статические таблицы, статические хост-таблицы.
They just are another form of name resolution.|Они просто еще одна форма разрешения имен.
But remember, static holds tables fit for small companies, medium-sized companies.|Но помните, что статические таблицы подходят для малых и средних компаний.
All right, and remember, all this stuff you can do on a notepad,|Хорошо, и помните, все это можно делать в блокноте,
copy paste it into a router and you're done.|скопируйте и вставьте его в маршрутизатор, и все готово.
All right.|Отлично.
If it's a very large enterprise with complex subnets, obviously,|Если это очень большое предприятие со сложными подсетями, очевидно,
you may wanna, you're gonna do DNS name resolution.|вы можете захотеть, вы сделаете разрешение имен DNS.
Which we configured in the admin config with IP domain-lookup, IP domain name cisco.com, IP name server and that is pointing to a DNS server, okay?|Что мы настроили в конфигурации администратора с поиском IP-домена, IP-именем домена cisco.com, сервером IP-имен, который указывает на DNS-сервер, хорошо?
Those are the two main forms of name resolution.|Это две основные формы разрешения имен.
With the DNS, though, you would have to,|Однако с DNS вам придется,
have to,|должен,
you would actually have to set up a Microsoft DNS.|вам действительно нужно будет настроить Microsoft DNS.
Well, I not just Microsoft, but a DNS server, nonetheless.|Ну, я не просто Microsoft, но тем не менее DNS-сервер.
All right.|Отлично.
That's it.|Вот и все.
That's your host tables.|Это ваши хост-таблицы.
Pretty simple.|Довольно просто.
Easy peasy.|Очень просто.
See you in the next lecture.|Увидимся на следующей лекции.
>> [BLANK_AUDIO]|>> [BLANK_AUDIO]