D:\mailCloud\prjother\tmp\1\c39_IPv6 address types.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
Okay.|Ладно.
Just like in IP before, that we have unicast, multicast, addresses, broadcast.|Как и раньше в IP, у нас есть одноадресная, многоадресная рассылка, адреса, широковещательная рассылка.
Oh, no that's right, there is no broadcast in IPv6, another wonderful feature.|О, нет, верно, в IPv6 нет трансляции, еще одна замечательная функция.
All right?|Отлично?
So no broadcast in IPv6,|Так что никакой трансляции в IPv6,
but we do have multicast addresses, we have unicast addresses.|но у нас есть многоадресные адреса, у нас есть одноадресные адреса.
We have something called global unicast,|У нас есть так называемая глобальная одноадресная передача,
which is, there's your range right here.|то есть вот ваш диапазон прямо здесь.
That's why you always see me 2001, cuz the range of global unicast,|Вот почему вы всегда видите меня 2001, из-за диапазона глобальной одноадресной передачи,
which are the equivalent to publicly routable addresses, okay.|которые эквивалентны публично маршрутизируемым адресам, хорошо.
Okay, what happened to my notepad?|Хорошо, что случилось с моим блокнотом?
Magic.|Магия.
Okay, I guess my hand touched the board.|Ладно, думаю, моя рука коснулась доски.
All right global unicast, publicly routable addresses.|Хорошо, глобальные одноадресные, публично маршрутизируемые адреса.
That's what their range is right there.|Вот какой у них диапазон.
It starts with 2,000 and 2,001.|Он начинается с 2000 и 2001.
2,002, really starts using for 6to4|2002, действительно начинает использоваться для 6to4
tunneling.|туннелирование.
Well, transition mechanism, right, we don't wanna talk about that yet.|Что ж, механизм перехода, да, мы пока не хотим об этом говорить.
But we have that type.|Но у нас есть такой тип.
And we also have this new one here this anycast address, right?|И у нас также есть этот новый адрес, не так ли?
This anycast address which is very, very interesting.|Это произвольный адрес, который очень и очень интересен.
It is also called the one to nearest.|Его еще называют ближайшим.
One to nearest, what does that mean?|От одного до ближайшего, что это значит?
Well, it comes from the range of the unicast addresses.|Ну, это исходит из диапазона одноадресных адресов.
You have to put, it's normally configured on a router, not on a host or source address or anything like that.|Вы должны поставить, это обычно настраивается на маршрутизаторе, а не на хосте или исходном адресе или что-то в этом роде.
It's usually on a router where you configure these anycast addresses.|Обычно это на маршрутизаторе, где вы настраиваете эти произвольные адреса.
And you can put the same address on different interfaces, all right.|И вы можете поместить один и тот же адрес на разные интерфейсы, хорошо.
What it does is, if you're looking for a service of a particular, whatever it is,|Что он делает: если вы ищете какую-либо услугу, какой бы она ни была,
based on the routing protocol, it becomes the nearest.|на основе протокола маршрутизации он становится ближайшим.
Now let me explain.|Теперь позвольте мне объяснить.
If you're running RIP, if it takes you,|Если вы используете RIP, если вам потребуется
one hop versus three hops to get to that particular service, then that one hub is the nearest, okay.|один переход по сравнению с тремя переходами, чтобы добраться до этой конкретной службы, тогда этот один концентратор является ближайшим, хорошо.
If you're running EIGRP and you're calculating the metric,|Если вы используете EIGRP и вычисляете метрику,
well the lowest metric, it could be three routers away, it could be two routers away, depending on the bandwidth, right,|ну, самая низкая метрика, это может быть три маршрутизатора, это может быть два маршрутизатора, в зависимости от пропускной способности, верно,
the k-values, that EIGRP uses.|k-значения, которые использует EIGRP.
How they're configured.|Как они настроены.
So the, the nearest address could be three routers away or two routers away.|Таким образом, ближайший адрес может быть через три или два маршрутизатора.
If we're using OSPF, which is based on cost, the lowest cost, right, that router may be just one router away, could be your|Если мы используем OSPF, который основан на стоимости, самая низкая стоимость, верно, этот маршрутизатор может быть всего на расстоянии одного маршрутизатора, может быть вашим
neighbor router, that is the nearest.|соседний маршрутизатор, то есть ближайший.
So depending on the type of routing that you're doing,|Итак, в зависимости от типа маршрутизации, которую вы выполняете,
the metrics of the router is what nearest means.|Ближайшие средства - это метрики роутера.
Right, the one to nearest, means you have one address that you can place all,|Правильно, от одного до ближайшего означает, что у вас есть один адрес, по которому вы можете разместить все,
in all these routers the identical address on all these routers or on these interfaces, and you would end it,|во всех этих маршрутизаторах одинаковый адрес на всех этих маршрутизаторах или на этих интерфейсах, и вы бы его закончили,
you'd put the actual IP address and then you say anycast, all right.|вы указываете реальный IP-адрес и говорите «anycast», хорошо.
It would be based on the routing so that's one of the newest addresses that has come into play in IPv6.|Он будет основан на маршрутизации, так что это один из новейших адресов, который вошел в игру в IPv6.
Very nice feature.|Очень приятная особенность.
Very nice feature.|Очень приятная особенность.
The next one is the link local.|Следующая ссылка - локальная.
We've all seen the link lo, link local.|Мы все видели ссылку вот, ссылка местная.
And if you haven't, go to your computers right now, go in the command prompt, and type IPconfig all.|А если нет, перейдите к своим компьютерам прямо сейчас, войдите в командную строку и введите IPconfig all.
Regardless if you, I'm sure you DACP enabled, but whether you're DACP enabled or not that FE80 address will be there.|Независимо от того, включен ли вы, я уверен, что у вас включен DACP, но независимо от того, включен ли у вас DACP или нет, адрес FE80 будет там.
That link local address is really the replacement of the APIPA, all right,|Этот локальный адрес ссылки действительно является заменой APIPA, хорошо,
the automatic private IP address, that 169.254 address that we used to see,|автоматический частный IP-адрес, тот адрес 169.254, который мы видели,
only if we were DHCP enabled and we never received and IP address.|только если у нас был включен DHCP и мы никогда не получали IP-адрес.
Well with a linked local address, it will always be there.|Что ж, со связанным локальным адресом он всегда будет там.
It will always be there.|Он всегда будет там.
The FE80.|Модель FE80.
Now one of the things that the book doesn't talk much about, and really you're not tested on, as long as you know FE80,|Одна из вещей, о которой в книге мало говорится, и на самом деле вы не тестировали, пока знаете FE80,
that's your linked local address, you're good to go for the examination.|это ваш связанный местный адрес, вы можете пойти на экзамен.
But, the link local address, if you have a multi-home computer,|Но локальный адрес ссылки, если у вас есть несколько домашних компьютеров,
if you have multiple nic cards on your computer, and you have, and you're running IPv6 or an operating system that, that supports IPv6,|если у вас есть несколько карт nic на вашем компьютере, и у вас есть, и вы используете IPv6 или операционную систему, которая поддерживает IPv6,
and, you'll have an FE80 on each one of those NIC cards.|и у вас будет FE80 на каждой из этих сетевых карт.
So, how does it know where to send the information, or when you're pinging how do you know which link local you wanna ping?|Итак, как он узнает, куда отправить информацию, или когда вы пингуетесь, как узнать, по какой локальной ссылке вы хотите пинговать?
Well there is, at the end of the link local address,|Ну, в конце ссылки локальный адрес,
cuz remember there's 128 bits just any IPv6 address.|Потому что помните, что любой IPv6-адрес 128 бит.
At the end of it is something, a percent and a number.|В конце будет что-то, процент и число.
Percent 10, percent 15, percent 20,|Процентов 10, процентов 15, процентов 20,
whatever it is, right.|что бы это ни было, верно.
And you would, it's called, that percent and the number is called the zone ID.|И вы бы, это называется, этот процент и число называется идентификатором зоны.
So in order to ping out of that particular NIC card, through that FE80 address,|Итак, чтобы выполнить эхо-запрос этой конкретной сетевой карты через этот адрес FE80,
you would need to use that zone ID so it knows where it needs to go, okay.|вам нужно будет использовать этот идентификатор зоны, чтобы он знал, куда ему нужно идти, хорошо.
And also that percent, just a little extra info,|А также этот процент, небольшая дополнительная информация,
if you didn't know, that's what it's called, zone ID.|если вы не знали, это так называется идентификатор зоны.
But as far as for the CCNA exam, as long as you know your FE80 is your link local address is a replacement for your IP PO,|Но что касается экзамена CCNA, если вы знаете, что FE80 - это ваш локальный адрес ссылки, он заменяет ваш IP PO,
[SOUND] you're good to go, no worries.|[ЗВУК] Тебе хорошо, не беспокойся.
The next one doesn't even look like an address,|Следующий даже не похож на адрес,
all you have are two double colons, right,|все, что у вас есть, это два двойных двоеточия, верно,
well why is that?|ну почему это?
Because they are all zeroes.|Потому что все они нули.
So you truncated it to two double colons,|Итак, вы усекли его до двух двойных двоеточий,
and that's perfectly valid.|и это совершенно верно.
That is a valid IPv6 address.|Это действительный адрес IPv6.
Two double colons.|Два двойных двоеточия.
One though right, you don't see two,|Один, хотя и прав, двух не видишь,
that's only one double colon.|это всего лишь одно двойное двоеточие.
And that's the same thing as using 0.0.0.0|И это то же самое, что использовать 0.0.0.0
in IPv4, like a default route, right?|в IPv4, как маршрут по умолчанию, верно?
All zeros, all zeros.|Все нули, все нули.
Then we have a loopback, we've already talked about the loopback address,|Затем у нас есть шлейф, про шлейфовый адрес мы уже говорили,
there's only one loopback, one loopback in IPv6.|в IPv6 только один шлейф, один шлейф.
And the good thing with IPv6,|И что хорошо с IPv6,
you see all these different type of addresses that we were just mentioning?|вы видите все эти разные типы адресов, которые мы только что упомянули?
You can put each and every one of them on the same interface.|Вы можете разместить каждый из них в одном интерфейсе.
You can put a multicast address with FF on an interface.|Вы можете поместить многоадресный адрес с помощью FF на интерфейс.
Lets say the F00, lets do the fast ethernet 00, you can put a multicast,|Допустим, F00, давайте сделаем быстрый Ethernet 00, вы можете поставить многоадресную рассылку,
a unicast, a global, an anycast, a link local,|одноадресная, глобальная, произвольная, локальная ссылка,
well the link local's already there.|ну местная ссылка уже там.
You can put any one of those types of addresses on there,|Вы можете поместить туда любой из этих типов адресов,
you can put multiple addresses on an interface with IPv6,|вы можете разместить несколько адресов на интерфейсе с IPv6,
something that we weren't able to do with IPv4.|то, что мы не могли сделать с IPv4.
I don't know if you recall with IPv4, they tried,|Не знаю, помните, с IPv4 они пытались,
what's called, that secondary IP address.|как называется, этот вторичный IP-адрес.
They didn't work too well on that.|Они не очень хорошо с этим работали.
They didn't advise it, so that's why we never used it.|Они этого не посоветовали, поэтому мы им и не воспользовались.
Rarely.|Редко.
All right, but with IPv6 that story changes.|Хорошо, но с IPv6 эта история меняется.
If need be, you can put all those addresses in one interface.|При необходимости вы можете поместить все эти адреса в один интерфейс.
Now there's a reason though, at the bottom,|Но теперь есть причина, внизу,
you see the three running protocols that you need to be aware of as well.|вы видите три работающих протокола, о которых вам также нужно знать.
Those are the IPv6 versions of RIP, EIGRP and OSPF.|Это версии протокола RIP, EIGRP и OSPF для IPv6.
You need to, and if you see FF, what does that mean?|Вам нужно, и если вы видите FF, что это значит?
It's a multicast address.|Это многоадресный адрес.
There is no more broadcast.|Трансляции больше нет.
Broadcast does not exist in IPv6.|В IPv6 широковещательной рассылки нет.
There's no art broadcast, there's no broadcast whatsoever.|Нет художественной трансляции, нет никакой трансляции.
Period.|Период.
So, even though, in IP version four the routing protocols used multicast addresses to send their updates to their neighboring routers, but they|Таким образом, несмотря на то, что в IP версии 4 протоколы маршрутизации использовали многоадресные адреса для отправки своих обновлений на соседние маршрутизаторы, но они
were in, not in decimal format.|были в, а не в десятичном формате.
You need to know, you need to know the IPv6 version of those addresses.|Вам нужно знать, вам нужно знать версию IPv6 этих адресов.
Wherein IPv4 RIP version 2 was 224009 and IPv6 is ff02::9, all right.|При этом IPv4 RIP версии 2 был 224009, а IPv6 - ff02 :: 9, хорошо.
With EIGRP, it was 224 0010.|С EIGRP это было 224 0010.
In IPv6, it's ff02::a,|В IPv6 это ff02 :: a,
because 10 is equivalent to a in hexadecimal.|потому что 10 эквивалентно шестнадцатеричной системе счисления.
And then OSPF version three 224 005 or 006 and IPv6 is ff02 5 and 6.|И затем OSPF версии три 224005 или 006, а IPv6 - это ff02 5 и 6.
And remember, again not giving stuff away for, for future lessons but something that needs to be said.|И помните, опять же, не раздача вещей для будущих уроков, а то, что нужно сказать.
OSPF does use two address.|OSPF использует два адреса.
The only time there's using the six is when they're sending information towards a designated router or a backup designated|Единственный раз, когда они используют шесть, - это когда они отправляют информацию на назначенный маршрутизатор или резервный резервный сервер.
router.|роутер.
Plus when we get to those lessons,|К тому же, когда мы дойдем до этих уроков,
you will, you'll understand what we're talking about.|вы поймете, вы поймете, о чем мы говорим.
So these are the types of addresses that we use.|Итак, это типы адресов, которые мы используем.
Anycast really being one of the newest,|Anycast действительно один из самых новых,
the most interesting out of all the address because it's the one to nearest.|самый интересный из всех адресов, потому что он ближайший.
And again it's looking based, the nearest based on the metric of whatever routing protocol you're using, okay.|И снова он выглядит основанным, ближайшим к метрике любого протокола маршрутизации, который вы используете, хорошо.
So that's one of the newest ones and it comes from the unicast address,|Так что это один из самых новых, и он исходит из одноадресного адреса,
the top 128 addresses, okay.|верхние 128 адресов, хорошо.
So there they are in all their glory.|Вот и они во всей красе.
Pretty much the same, just again looking at hexadecimal numbers, all right.|Практически то же самое, просто снова посмотрим на шестнадцатеричные числа, хорошо.
And, the other special one, I guess, would be the FE80, that replaced the link local.|И, я полагаю, другим специальным устройством будет FE80, который заменил локальную ссылку.
You can route, somewhat, with this,|Вы можете отчасти прокладывать маршрут с помощью этого,
something goes beyond the scope of the book, but again you need to know, really,|что-то выходит за рамки книги, но опять же вам нужно знать, правда,
you don't need to know the prefix of it,|вам не нужно знать его префикс,
if you do its wonderful.|если вы сделаете это замечательно.
What you need to really know is this right here, the FE80,|Что вам действительно нужно знать, так это вот этот FE80,
the F00, the 2000, 2001 and the FF, that is a multicast.|F00, 2000, 2001 и FF, то есть многоадресная передача.
Because when you get tested and you're looking for, hey,|Потому что, когда вы проходите тестирование и ищете, эй,
which of the following are multicast or which of the following is something local,|какие из следующего являются многоадресными или какие из следующих являются локальными,
they'll throw in multicast, or unicast,|они добавят многоадресную или одноадресную рассылку,
and they'll throw the link local or they'll throw something else in there.|и они бросят ссылку локально или добавят туда что-нибудь еще.
And you need to know how to pick it.|И нужно знать, как его забрать.
So be careful with that.|Так что будьте осторожны с этим.
As long as you know, this portion of the address and what that does, what it is, you should be fine, okay.|Если вы знаете эту часть адреса и то, что она делает, что это такое, с вами все будет в порядке, хорошо.
All right guys, this is it, I'll see you in the next session.|Хорошо, ребята, это все, увидимся на следующем сеансе.
[BLANK_AUDIO]|[BLANK_AUDIO]