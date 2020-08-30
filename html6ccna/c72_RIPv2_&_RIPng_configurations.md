D:\mailCloud\prjother\tmp\1\c72_RIPv2 & RIPng configurations.md  


__|__
--|--
Well I'm back ladies and gentleman.|Что ж, я вернулся, дамы и господа.
Here we are.|Мы здесь.
We're gonna start talking about RIP version 2 and RIPNG.|Мы собираемся поговорить о RIP версии 2 и RIPNG.
Now we spoke on it before,|Мы говорили об этом раньше,
but it was very brief.|но это было очень кратко.
We're gonna get into the details of these routing protocols.|Мы собираемся более подробно остановиться на этих протоколах маршрутизации.
Now again, the basics of these routing protocols, RIP version 2 and RIPNG are the same.|Опять же, основы этих протоколов маршрутизации, RIP версии 2 и RIPNG одинаковы.
The only thing that changes is the configuration of the routing protocol.|Единственное, что меняется - это конфигурация протокола маршрутизации.
So now we talked about something that is a RIP, is a distance.|Итак, теперь мы поговорили о том, что такое RIP, это расстояние.
And I'm just gonna abbreviate,|И я просто сокращу,
distance vector routing protocol,|протокол дистанционно-векторной маршрутизации,
which means again that it's looking at the distance,|что снова означает, что он смотрит вдаль,
meaning the hop count, how far away is it,|имеется в виду количество хмеля, как далеко это,
and the direction that it's gonna take.|и направление, в котором он пойдет.
And the direction it's gonna take,|И направление, в котором он пойдет,
so that's what a distance vector is.|так вот что такое вектор расстояния.
That the RIP uses the BELLMAN-FORD algorithm,|Что RIP использует алгоритм BELLMAN-FORD,
and again I'm going to,|и снова я собираюсь,
I'm gonna put ALGO, not 0.|Я поставлю ALGO, а не 0.
So you understand what I'm talking about.|Итак, вы понимаете, о чем я говорю.
The algorithm, that's what does the calculation, the math and all of it.|Алгоритм, вот что делает расчет, математика и все такое.
Now what we need to understand is that RIP itself,|Теперь нам нужно понять, что сам RIP,
just like RIPNG, has a MAX HOP COUNT.|так же, как RIPNG, имеет МАКСИМАЛЬНОЕ СЧЕТЧИКА HOP.
And we talked about it already,|И мы об этом уже говорили,
hop count of 15, not 025, 15.|количество переходов 15, а не 025, 15.
Which means if you see within your routing table, or you won't see, if it's 16 away,|Это означает, что если вы видите в своей таблице маршрутизации или не видите, если она находится на расстоянии 16,
that means that network is unreachable,|это означает, что сеть недоступна,
it's unreachable.|это недостижимо.
Now one thing in the new test,|Теперь одно в новом тесте,
what I've seen in the, the newer books.|что я видел в новых книгах.
They don't really get that deep into RIP.|Они не особо разбираются в RIP.
They really do not.|На самом деле нет.
They really just want you to know how to configure it.|Они просто хотят, чтобы вы знали, как это настроить.
But there's certain things that I'm gonna tell you anyway,|Но есть кое-что, что я все равно тебе скажу,
because you need to understand, all right?|потому что нужно понимать, хорошо?
Now definitely you need to know the administrative distance,|Теперь обязательно нужно знать административную дистанцию,
ADMIN DISTANCE over it,|ADMIN DISTANCE над ним,
which is 120, right?|что 120, не так ли?
And you learned that in the previous lesson that I showed you.|И вы узнали это на предыдущем уроке, который я вам показал.
The ADMIN DISTANCE is 120|АДМИНИСТРАТОРНОЕ РАССТОЯНИЕ - 120.
because it is important.|потому что это важно.
Because depending on the administrative distance of any of the routing protocols,|Потому что в зависимости от административного расстояния любого из протоколов маршрутизации,
that's the way it's gonna decide who's gonna make it to the routing table.|таким образом он решит, кто попадет в таблицу маршрутизации.
On the administrative distance,|На административной дистанции,
when you're talking about, you know,|когда ты говоришь о, знаешь,
hey RIP, EIGRP, or OSPF, or static routes, depending on the AD,|эй RIP, EIGRP или OSPF, или статические маршруты, в зависимости от AD,
administrative distance.|административная удаленность.
So for RIP, or RIPNG is 120, so that still remains the same.|Так что для RIP или RIPNG это 120, так что это остается прежним.
Now, we talked about timers.|Теперь мы поговорили о таймерах.
We talked about an update timer,|Мы говорили о таймере обновления,
which is 30 seconds, right?|это 30 секунд, правда?
Which was that a distance vector routing protocol like RIP is going to send the entire routing table out every 30 seconds.|А именно, протокол маршрутизации с вектором расстояния, такой как RIP, будет отправлять всю таблицу маршрутизации каждые 30 секунд.
The next timer, whoops,|Следующий таймер, упс,
the next timer that I believe I said was the HOLDOWN TIMER,|следующий таймер, который, кажется, я сказал, был ТАЙМЕР УДЕРЖАНИЯ,
HOLDOWN, spell it right,|ДЕРЖАТЬ, пиши правильно,
HOLDOWN TIMER, which is 180 seconds.|ТАЙМЕР УДЕРЖАНИЯ, который составляет 180 секунд.
All right, which means it's gonna hold that information of the update for 180 seconds.|Хорошо, это означает, что он будет хранить эту информацию об обновлении в течение 180 секунд.
The next one is that INVALID TIMER.|Следующий - НЕВЕРНЫЙ ТАЙМЕР.
Which is the same as a hold down,|Это то же самое, что и удержание,
180 seconds,|180 секунд,
means that if I don't receive an update at 30 seconds, that timer starts ticking in.|означает, что если я не получаю обновления через 30 секунд, этот таймер начинает отсчитывать время.
All right, I don't care,|Хорошо, мне все равно,
I'm gonna hold this information for 180.|Я собираюсь хранить эту информацию на 180.
Okay, I'm at 180,|Хорошо, я на 180,
I still don't have the information.|У меня до сих пор нет информации.
You haven't gotten any updates still,|У вас еще нет обновлений,
then that route becomes invalid.|тогда этот маршрут становится недействительным.
It's still in the routing table,|Он все еще в таблице маршрутизации,
it's just invalid.|это просто недействительно.
And then the last timer, which by the way in the previous lesson I said to be 60,|А затем последний таймер, который, кстати, на предыдущем уроке я сказал, 60,
that was incorrect.|это было неправильно.
The the FLUSH TIMER is 240,|ТАЙМЕР ПРОМЫВКИ - 240,
so forgive me, okay?|так что прости меня, ладно?
I try to keep all this in my head,|Я стараюсь все это держать в голове,
but it's 240 seconds.|но это 240 секунд.
So if it gets to 180 and it doesn't receive that update,|Поэтому, если он достигает 180 и не получает это обновление,
it's gonna go ahead and count up to 240, all right.|это будет продолжаться и сосчитать до 240, хорошо.
And that's okay.|И это нормально.
Once I reach 240, if I don't re, if I don't get an update from my neighbor, that particular route will be flush, will be taken out of the routing table altogether.|Как только я достигну 240, если я не вернусь, если я не получу обновления от моего соседа, этот конкретный маршрут будет очищен, будет полностью удален из таблицы маршрутизации.
So these timers, you can tweak.|Так что эти таймеры вы можете настроить.
Why would you want tweak these timers?|Зачем вам настраивать эти таймеры?
Because of bandwidth issues.|Из-за проблем с пропускной способностью.
That's one of the things that, you know,|Это одна из вещей, которые, как вы знаете,
you would take into consideration.|вы бы приняли во внимание.
You would say hey,|Вы бы сказали эй,
across a wide area network,|через глобальную сеть,
we really didn't purchase a lot of bandwidth.|мы действительно не покупали много пропускной способности.
So, you know, we're using RIP,|Итак, вы знаете, мы используем RIP,
which is not the most popular routing protocol to use, all right?|какой протокол маршрутизации не самый популярный, понятно?
Because it's for very small networks.|Потому что это для очень маленьких сетей.
So if you're sending it out across a wired network that's less than a T1 and you're using RIP, every 30 seconds.|Так что, если вы отправляете его по проводной сети, длина которой меньше T1, и вы используете RIP, каждые 30 секунд.
And you, let's say you do have a lot of subnets underneath each particular router.|Допустим, у вас есть много подсетей под каждым конкретным маршрутизатором.
And you have, let's say,|А у вас, скажем так,
seven or ten routers.|семь или десять роутеров.
And under each router you have 10,|И под каждым роутером у вас по 10,
15, 20 different subnets.|15, 20 разных подсетей.
All those subnets need to be advertised through RIP.|Все эти подсети необходимо объявлять через RIP.
So it will send that every 30 seconds that entire routing table, so you can play with a holdown timer.|Таким образом, он будет посылать это каждые 30 секунд всю таблицу маршрутизации, чтобы вы могли играть с таймером задержки.
Say hey let's, let's, or,|Сказать, давай, давай, или
and the, all these timers.|и все эти таймеры.
The update timer, definitely, you don't want that to go out every 30 seconds so you can increase each one.|Таймер обновления, безусловно, вы не хотите, чтобы он срабатывал каждые 30 секунд, поэтому вы можете увеличивать каждое из них.
Just remember that your holdown and your invalid have to be the same.|Просто помните, что ваша собственность и инвалид должны быть одинаковыми.
They have to be the same, and then you can increase your force timer after that.|Они должны быть такими же, и после этого вы можете увеличить таймер силы.
Now, the reason the flush timer,|Теперь причина таймера промывки,
and invalid timers also, you, and the holdown timer.|а также недействительные таймеры, вы и таймер задержки.
One of the reasons that you want to increase that, is so is due to something called a flapping interface.|Одна из причин, по которой вы хотите это увеличить, связана с чем-то, что называется изменяющимся интерфейсом.
The update timer you do it because you don't want every 30 seconds, right?|Таймер обновления вы делаете потому, что не хотите каждые 30 секунд, правда?
You're bound with being diminished every 30 seconds.|Вы будете уменьшаться каждые 30 секунд.
But the other timers are really because,|Но другие таймеры действительно потому, что
let's say you have a problem with that interface that's going up and down.|Допустим, у вас проблема с тем интерфейсом, который постоянно меняется.
Whether it be the cable or it be the actual interface itself that you have something going up and down, up and down,|Будь то кабель или сам интерфейс, в котором что-то движется вверх и вниз, вверх и вниз,
which is called a flopping interface.|который называется гибким интерфейсом.
You can play with these timers so it doesn't release, you know,|Вы можете поиграть с этими таймерами, чтобы он не срабатывал, понимаете,
that information.|эта информация.
It doesn't get rid of that information as fast as you see here.|Он не избавляется от этой информации так быстро, как вы видите здесь.
So you can increase those timers.|Так что вы можете увеличить эти таймеры.
Again, the new task doesn't really,|Опять же, новая задача не совсем
the new,|новый,
even the new book doesn't really get into the timers, just know that they do exist.|даже новая книга не особо попадает в таймеры, просто знайте, что они существуют.
And you can play with it.|И с этим можно поиграть.
Now, one of the things with RIP that you can use, obviously, again,|Теперь одна из вещей с RIP, которую вы, очевидно, снова можете использовать,
to prevent routing loops and all these different things is,|чтобы предотвратить петли маршрутизации и все эти разные вещи,
one of them is your holdown timer.|один из них - ваш таймер удержания.
The other one is something called SPLIT,|Другой называется SPLIT,
not SPLITE, SPLIT HORIZON, all right?|НЕ РАЗДЕЛЕНИЕ, РАЗДЕЛЕНИЕ ГОРИЗОНТА, хорошо?
Which really means, hey,|Что на самом деле означает, эй,
don't, symbol DON'T SEND BACK.|нет, символ НЕ ОТПРАВЛЯЙТЕ НАЗАД.
UPDATES, [SOUND] ON,|ОБНОВЛЕНИЯ, [ЗВУК] ВКЛ,
ON THE SAME INTERFACE.|НА ОДНОМ ИНТЕРФЕЙСЕ.
Oh, wow.|Ух ты.
All right, so here let's say for example, this network goes down.|Хорошо, так вот, например, эта сеть выходит из строя.
I think I've explained it before.|Думаю, я уже объяснял это раньше.
This router is going to update this router, right, through that interface.|Этот маршрутизатор будет обновлять этот маршрутизатор, верно, через этот интерфейс.
Say hey, this network is down, you can't reach me anymore the way you used to.|Слушай, эта сеть не работает, ты больше не можешь связаться со мной, как раньше.
And this router goes cool, but this router didn't advertise this one.|И этот роутер идет круто, но этот роутер не афишировал.
Then this router,|Тогда этот роутер,
his turn to update that neighbor router.|его очередь обновить этот соседний маршрутизатор.
So he updates this router before he gets a chance to tell him that network is down.|Поэтому он обновляет этот маршрутизатор до того, как получит возможность сказать ему, что сеть не работает.
So he thinks, oh, I just got a new update that says this network up and I can reach it through this interface.|Поэтому он думает: о, у меня только что получилось новое обновление, в котором говорится, что эта сеть работает, и я могу связаться с ней через этот интерфейс.
Okay, so I'm gonna update that router,|Хорошо, я собираюсь обновить этот маршрутизатор,
and that router's gonna say, no.|и этот роутер скажет "нет".
I told you this interfa,|Я тебе это интерфа сказал,
this network is down, and sends it back.|эта сеть не работает и отправляет ее обратно.
So that creates a routing loop.|Это создает петлю маршрутизации.
So split horizon is on by default,|Таким образом, разделение горизонта включено по умолчанию,
to let, you know, for that not to happen.|чтобы этого не случилось.
And again, that causes an issue in our frame relay network, but I'm not gonna get into that, all right?|И снова это вызывает проблему в нашей сети Frame Relay, но я не собираюсь вдаваться в подробности, понятно?
When we get to frame relay, or get into it again, cuz I think I explained it in the previous,|Когда мы дойдем до Frame Relay или вернемся к нему снова, я думаю, что объяснил это в предыдущем,
that causes an issue in frame relay.|это вызывает проблему в Frame Relay.
And there's a certain way you configure frame relay to circumvent that particular issue on split horizon.|И есть определенный способ настроить ретрансляцию кадров, чтобы обойти эту конкретную проблему на разделенном горизонте.
But, that's what split horizon is.|Но вот что такое разделенный горизонт.
The next thing that you can do to prevent routing loops is POISON REVERSE.|Следующее, что вы можете сделать для предотвращения петель маршрутизации, - это ОБРАТНЫЙ ОТКАЗ.
And, basically,|И, в основном,
you're putting a MAX HOP COUNT of 16.|вы ставите MAX HOP COUNT равным 16.
The maximum hop count of RIP is 15.|Максимальное количество переходов RIP - 15.
It's 15, you're giving it 16, so you're telling it, hey, listen,|Это 15, вы даете ему 16, так что вы говорите это, эй, слушайте,
this network is unreachable, period.|эта сеть недоступна, точка.
So everybody gets that update saying,|Итак, все получают это обновление, в котором говорится:
oh, okay, that network's unreachable, so you're poisoning the route.|о, хорошо, эта сеть недоступна, так что вы отравляете маршрут.
Understand it, you don't have to configure poison reverse,|Поймите, ядовитый реверс настраивать не нужно,
you don't have to configure split horizon.|вам не нужно настраивать разделение горизонта.
Understand what this is for.|Разберитесь, для чего это нужно.
That's it.|Вот и все.
Understand what this is for.|Разберитесь, для чего это нужно.
Even if they don't ask you a question on split horizon.|Даже если они не зададут вам вопрос на расколотом горизонте.
Which I believe in the frame, frame relay,|Я верю в фрейм, ретрансляцию кадров,
in the wired area network portion.|в проводной сети.
They'll mention oh, due to split horizon,|Они будут упоминать о, из-за раскола горизонта,
and you're running this routing protocol,|и вы используете этот протокол маршрутизации,
how can you, circumvent that?|как вы можете это обойти?
And that's how they're gonna test you on split horizon.|И вот как они собираются проверить вас на расколотом горизонте.
But, no,|Но нет,
since RIP has a maximum hop count of 15,|поскольку RIP имеет максимальное количество переходов 15,
that if you poison the route deliberately,|что если вы намеренно отравите маршрут,
now that you have to configure it,|теперь, когда вам нужно его настроить,
if you poison the route deliberately,|если вы намеренно отравляете маршрут,
you set a maximum HOP COUNT of 16.|вы устанавливаете максимальное количество HOP, равное 16.
So if you telling everybody, hey to get to this network of 16, and we know we're running RIP, all the routers are gonna say okay, that network is unreachable.|Итак, если вы скажете всем, привет, чтобы добраться до этой сети из 16, и мы знаем, что используем RIP, все маршрутизаторы скажут хорошо, эта сеть недоступна.
It's unreachable, so it won't even,|Это недостижимо, так что даже не будет
it won't even look at it.|он даже не смотрит на это.
All right.|Отлично.
The next one they can use I said,|Следующий, который они могут использовать, я сказал:
again, was a hold down timer.|опять же, был таймер удержания.
Hold down timer.|Удерживайте таймер.
So you can use those three.|Так что вы можете использовать эти три.
Those three are the ones really you look at it, you update the hold down timer,|Это те три, на которые вы действительно смотрите, вы обновляете таймер удержания,
hold the information for a certain amount of time,|удерживать информацию определенное время,
split horizon, and poison reverse.|расколоть горизонт и отравить обратный.
Now, with rip also and this is, and this next command I'm gonna give you,|Теперь, с рипом, и вот эта следующая команда, которую я вам дам,
you will see in one of your simulations I believe.|я думаю, вы увидите это в одном из ваших симуляций.
All right and again this information that I get,|Хорошо, и снова эта информация, которую я получаю,
I get from students that just taken the CCNA.|Я получаю от студентов, которые только что прошли CCNA.
So I'm just letting you know what could possibly you can run into.|Так что я просто даю вам знать, с чем вы можете столкнуться.
It's called the, passive Hyphen interface,|Это называется пассивным интерфейсом дефиса,
and then whatever interface you're gonna use.|а затем любой интерфейс, который вы собираетесь использовать.
That command,|Эта команда,
holds updates from being, woo hoo.|держит обновления от быть, у-у-у.
Sent out, okay?|Отправлено, хорошо?
That's what it basically does.|Это то, что он в основном делает.
When do you wanna use something like this?|Когда вы хотите использовать что-то подобное?
I mean, RIP a, in itself already,|Я имею в виду, RIP уже сам по себе,
is every 30 seconds sending out an update.|каждые 30 секунд рассылает обновление.
But let's say you have a wide area network, or a LAN, or whatever it is,|Но допустим, у вас есть глобальная сеть, или локальная сеть, или что-то еще,
that you don't want, you do not want to send out updates out that interface.|что вы не хотите, вы не хотите отправлять обновления через этот интерфейс.
You use a passive-interface command.|Вы используете команду пассивного интерфейса.
And the way you configure that is within the routing pr,|И способ, которым вы настраиваете, находится в маршруте pr,
route, config router, or router configuration mode, alright?|маршрут, конфигурация маршрутизатора или режим конфигурации маршрутизатора, хорошо?
Within RIP.|Внутри RIP.
You configure this.|Вы настраиваете это.
You set a passive of that interface, and then the interface that you don't want to send out these updates.|Вы устанавливаете пассив для этого интерфейса, а затем интерфейс, который вы не хотите отправлять эти обновления.
So no updates will be sent out about the networks that you know about.|Таким образом, обновления о сетях, о которых вы знаете, рассылаться не будут.
You can receive updates, but you will not send out updates.|Вы можете получать обновления, но не будете их рассылать.
So that's what it does within RIP.|Вот что он делает в RIP.
And again,|И опять,
this remains the same with RIPng.|то же самое и с RIPng.
Nothing I've said so far is different between either or.|Ничего из того, что я сказал до сих пор, не отличается между или.
They're both the same.|Они оба одинаковые.
They're both exactly the same.|Они оба абсолютно одинаковые.
It's just a configuration, ladies and gentlemen, just a configuration.|Это просто конфигурация, дамы и господа, просто конфигурация.
All right?|Отлично?
So passive interface, F00.|Итак, пассивный интерфейс, F00.
All right?|Отлично?
And then the last thing you can do also.|И последнее, что вы можете сделать.
Let's say, and, right here, let's say,|Скажем, и вот, скажем,
let's take a look at our lab.|давайте взглянем на нашу лабораторию.
And let's say I will add, let's say that this, I will put a web server right here.|И, скажем, я добавлю, скажем, это, я поставлю веб-сервер прямо здесь.
As a matter of fact, let's take one out,|Собственно говоря, возьмем одну,
just so you can have a better visual,|просто чтобы вы могли лучше видеть,
all right?|отлично?
Let's say I have a web server here.|Допустим, у меня здесь есть веб-сервер.
And that web server is connected to a particular interface.|И этот веб-сервер подключен к определенному интерфейсу.
And obviously we'll use a crossover cable,|И, очевидно, мы будем использовать кроссовый кабель,
right?|право?
F00, and then we'll put it on the F01.|F00, а потом поставим на F01.
So let's say this is a public web server.|Допустим, это общедоступный веб-сервер.
Let's put here www.|Положим сюда www.
So there's a command that's called default Information originate, or default, yeah,|Итак, есть команда, которая называется источником информации по умолчанию или по умолчанию, да,
default hyphen information originate.|информация о дефисах по умолчанию.
Which you do within, RIP.|Что вы делаете внутри, RIP.
That will actually send out,|Это на самом деле отправит,
if anybody here,|если кто-нибудь здесь,
anybody other than this router, everybody here wants to get to that one Instead of advertising the network itself, you can do|кто угодно, кроме этого маршрутизатора, все здесь хотят добраться до него Вместо того, чтобы рекламировать саму сеть, вы можете сделать
the default information originate command.|команда создания информации по умолчанию.
All right, and what's going to happen is,|Хорошо, и вот что произойдет,
they're all going to get it.|они все получат это.
And what's cool about it, that they're all going to have the same HOP count.|И что круто, у них у всех будет одинаковое количество HOP.
That's cool.|Это классно.
It won't increase the HOP count,|Это не увеличит количество HOP,
it'll remain the same.|он останется прежним.
So that's one thing with RIP that you can do.|Так что это единственное, что вы можете сделать с RIP.
So you have the default information originate,|Итак, у вас есть информация по умолчанию,
you have the, passive, now where is it.|у вас есть пассив, теперь где он.
The passive, there you go,|Пассивный, вот и все,
passive interface that goes down.|пассивный интерфейс, который выходит из строя.
That holds, the updates for being sent out.|Это касается обновлений для рассылки.
So all things are going on in RIP.|Итак, все происходит в RIP.
One last thing, one last thing I want to mention, is the multicast [INAUDIBLE],|И последнее, последнее, о чем я хочу упомянуть, - это многоадресная рассылка [НЕРАЗБОРЧИВАЕТСЯ],
the multicast addresses,|адреса многоадресной рассылки,
this you need need to know.|это вам нужно знать.
This you need to know.|Это вам нужно знать.
For sure you're probably going to get questions on this.|Наверняка у вас наверняка возникнут вопросы по этому поводу.
224 dot zero dot zero dot,|224 точки нулевая точка нулевая точка,
nine, all right.|девять, хорошо.
That is when the updates,|Вот когда обновления,
when RIP version two talk to it,|когда с ним разговаривает вторая версия RIP,
is talking to its neighbors,|разговаривает со своими соседями,
it's going to use.|это будет использовать.
That information, that,|Эта информация, что,
IP address, 224009,|IP-адрес, 224009,
that's how it sends updates in IP version four.|вот как он отправляет обновления в четвертой версии IP.
In IP version six, and you should see a distinction, FF02::2, I mean 9, sorry.|В шестой версии IP, и вы должны увидеть различие, FF02 :: 2, я имею в виду 9, извините.
Say anything in IPv6 that starts with an FF, it's a multicast address.|Скажите все, что в IPv6 начинается с FF, это многоадресный адрес.
So you see they're still using the 9.|Итак, вы видите, что они все еще используют 9.
I believe you can see that.|Я думаю, вы это видите.
They're still using the 9, but now it's FF02 colon, colon 9, versus 224.0.0.9.|Они все еще используют 9, но теперь это двоеточие FF02, двоеточие 9, а не 224.0.0.9.
It is still the same multicast address,|Это все тот же адрес многоадресной рассылки,
just in a different method, right?|просто другим способом, правда?
IPv6.|IPv6.
So multicast nonetheless, and that is the multicast address that refuses.|Тем не менее, многоадресная рассылка, а этот многоадресный адрес отказывает.
How can you see that?|Как вы это видите?
How can you see that?|Как вы это видите?
You can type debug IP RIP.|Вы можете ввести отладочный IP RIP.
Debug IP rip, and you can see the updates going back and forth.|Отладьте копирование IP-адреса, и вы увидите, как обновления идут туда и обратно.
All right, so that is RIP, that is RIP.|Хорошо, это RIP, то есть RIP.
What we're gonna do now is, we're gonna configure rip on all the routers.|Теперь мы собираемся настроить рип на всех роутерах.
Will you have to configure a RIP in your certification?|Придется ли вам настраивать RIP в вашей сертификации?
As of yet, no.|Пока нет.
Do you need to?|Вам это нужно?
Of course.|Конечно.
If you're going out on an interview and this is not such a large, enterprise.|Если вы идете на собеседование, а это не такое уж большое предприятие.
It's a medium size or small network You need to know or they may just ask you, okay how would you configure a rip on this network?|Это сеть среднего или небольшого размера. Вам нужно знать, или они могут просто спросить вас, хорошо, как бы вы настроили рип в этой сети?
So if you're like A is the answer,|Итак, если вам нравится A, это ответ,
then that's a problem.|тогда это проблема.
All right?|Отлично?
So we're going to go ahead and configure RIP, and we'll start with this router right here.|Итак, мы собираемся продолжить настройку RIP, и мы начнем с этого маршрутизатора прямо здесь.
Let's move it over here.|Давай переместим это сюда.
Eh, my finger is getting better,|Эх, мой палец поправляется,
it likes it.|ему это нравится.
Alright, let's go to the CLI.|Хорошо, перейдем к интерфейсу командной строки.
Let's just open it up a little bit more.|Давайте просто откроем его еще немного.
Now remember, let's take a look,|Теперь помните, давайте посмотрим,
anytime I get into a router,|каждый раз, когда я попадаю в роутер,
one of the first things I look,|одна из первых вещей, на которую я смотрю,
I make it a habit, all right,|Я делаю это привычкой, хорошо,
if it's a small, right,|если маленький, верно,
configuration like we do here.|конфигурация, как здесь.
What is that Cisco?|Что это за Cisco?
Cisco, yes.|Cisco, да.
I always do a show start.|Я всегда начинаю шоу.
Not starat, start.|Не старь, начни.
All right, I take a look at this and say, okay, all these configurations, but I'm more interested in.|Хорошо, я смотрю на это и говорю, хорошо, все эти конфигурации, но меня больше интересует.
The IP addressing that's there,|Этот IP-адрес,
the networks that are, that are there.|сети, которые есть, которые есть.
All right?|Отлично?
And this one,|И этот,
you can see that it has a default route.|вы можете видеть, что у него есть маршрут по умолчанию.
You wanna leave that gateway of last resort.|Вы хотите покинуть этот портал в крайнем случае.
Why do I wanna leave that gateway of last resort there?|Почему я хочу оставить там последний выход?
Because it's a stub router.|Потому что это роутер-заглушка.
There's nothing else going out this way.|Больше ничего не выходит из этого пути.
So, you know what?|Знаете что?
Let's just leave it there.|Давай просто оставим это здесь.
Let's just leave the default gateway so in case there's a network that I add, okay?|Давайте просто оставим шлюз по умолчанию, так что на случай, если я добавлю сеть, хорошо?
It doesn't really matter because what's gonna, that default,|На самом деле это не имеет значения, потому что, что по умолчанию,
remember what that default route is.|запомните, что это за маршрут по умолчанию.
Default route.|Маршрут по умолчанию.
A default static route.|Статический маршрут по умолчанию.
What does that one do?|Что он делает?
That says hey Match exactly the mask.|Это говорит: «Эй, подбери именно маску».
Match exactly,|Точно совпадать,
I mean match exactly the IP.|Я имею в виду точное соответствие IP.
Match exactly the mask, and just send it out the exit interface.|Точно сопоставьте маску и просто отправьте ее через интерфейс выхода.
So that's your gateway of last resort.|Так что это ваш крайний выход.
If you were to look, again, at the just,|Если бы вы снова посмотрели на справедливое,
and this is reviewing, show IP route,|и это проверка, покажите IP-маршрут,
the routing table, you see that your gateway of last resort is set to whatever.|таблица маршрутизации, вы видите, что ваш шлюз последней инстанции настроен на что угодно.
And then here you see that static default route.|И тут вы видите статический маршрут по умолчанию.
So what we're gonna do now is configure RIP.|Итак, что мы собираемся сделать сейчас, это настроить RIP.
Okay?|Ладно?
So let's do that.|Итак, давайте сделаем это.
We need to be in global configuration.|Нам нужно быть в глобальной конфигурации.
#CONFIG T, not IT.|#CONFIG T, а не IT.
#CONFIG T, #ROUTER RIP.|# КОНФИГ Т, # РОЙТЕР РИП.
Do not forget, which I'm sure you're not gonna have to do it,|Не забывай, я уверен, тебе не придется этого делать,
but just in case, #VERSION 2..|но на всякий случай # ВЕРСИЯ 2 ..
We don't use version one anymore.|Мы больше не используем первую версию.
Forget about reading about version one.|Забудьте о первой версии.
Once you're done with the test, if you wanna read about version one, great.|Когда вы закончите тест, если вы захотите прочитать о первой версии, отлично.
We don't use version one anymore.|Мы больше не используем первую версию.
It doesn't support class list routing,|Он не поддерживает маршрутизацию списка классов,
right, DLSM.|верно, ДЛСМ.
Well, RIP version 2 does.|Что ж, RIP версии 2 делает.
RIP version 2 supports authentication,|RIP версии 2 поддерживает аутентификацию,
all right?|отлично?
And so there's a lot of things that RIP version 2 does that RIP version 1 didn't,|RIP версии 2 делает многое, чего не делает RIP версии 1,
doesn't, or never did, or never will,|нет, или никогда не делал, или никогда не будет,
cuz we don't use it any more, so forget about that.|потому что мы больше не используем его, так что забудьте об этом.
Because if you forget to put version 2,|Потому что если вы забудете поставить 2 версию,
again, I don't know why I'm saying this,|Опять же, я не знаю, почему я говорю это,
but I'm gonna say it anyway.|но я все равно это скажу.
This is what happens.|Вот что происходит.
If you have a router that has version two,|Если у вас есть маршрутизатор второй версии,
and you have a router that has version one, the version one router will accept the version two updates, but the version two router will not|и у вас есть маршрутизатор с версией один, маршрутизатор версии 1 будет принимать обновления версии 2, но маршрутизатор версии 2 не будет
accept the version one updates.|принять обновления первой версии.
That's what happens.|Вот что происходит.
Now, you could, you could go inside router configuration and say, accept both.|Теперь вы могли бы, вы могли бы войти в конфигурацию маршрутизатора и сказать, принять оба.
Why would you wanna do that?|Зачем тебе это нужно?
Well, one is just a class full routing protocol that you have to have the same subnet mask to route the entire network.|Ну, это просто протокол полной маршрутизации класса, у вас должна быть одна и та же маска подсети для маршрутизации всей сети.
And the other one doesn't.|А другой нет.
One doesn't support authentication,|Один не поддерживает аутентификацию,
the other one does.|другой делает.
Why would you want to go back in time?|Зачем вам возвращаться во времени?
That's like saying, hey, you know what?|Это как сказать: эй, знаешь что?
I think everybody in the company should have, one side of the company will be Windows 8, the other side of the company will be Windows 98, let's try that!|Я думаю, что все в компании должны иметь, одна сторона компании будет Windows 8, другая сторона - Windows 98, давайте попробуем!
That's the same thing here.|Здесь то же самое.
You don't go, you're not gonna do that.|Не уходи, ты не собираешься этого делать.
So if you run RIP version two,|Итак, если вы запустите RIP версии два,
you run RIP version two.|вы запускаете RIP версии два.
Forget about RIP version one.|Забудьте о первой версии RIP.
I, I think I made that clear, all right?|Я думаю, что ясно дал понять, хорошо?
So now,|А сейчас,
when we're advertising these networks,|когда мы рекламируем эти сети,
this is where everybody goes, what?|сюда все идут, что?
You see that we're in the 10.1.1.4,|Вы видите, что мы в 10.1.1.4,
correct?|верный?
And we have the, let me bring it a little lower, the 192.168.1.0.|И у нас есть, позвольте мне немного понизить его, 192.168.1.0.
Distance vector routing protocols.|Протоколы дистанционно-векторной маршрутизации.
They summarize automatically to the class full boundary.|Они автоматически суммируются до полной границы класса.
This is a class C address, right, 192.|Это адрес класса C, верно, 192.
And it's using a default mask.|И он использует маску по умолчанию.
So, the class full boundary is a third octave.|Итак, полная граница класса - третья октава.
This is a class A address.|Это адрес класса А.
It's using a slash 30 mask, but the class full boundary is at the eight,|Он использует маску косой черты 30, но полная граница класса находится на восьмерке,
the slash A, right, the ten.|косая черта A, верно, десять.
So I wanna do something on purpose,|Так что я хочу что-то сделать специально,
so you can see what happens.|чтобы вы могли видеть, что происходит.
Cuz this is the way I,|Потому что так я,
I wouldn't configure it.|Я бы не стал его настраивать.
Not because it's wrong or whatever.|Не потому, что это неправильно или что-то в этом роде.
Just, I'm not gonna waste my time typing things that are not gonna happen anyway.|Просто я не собираюсь тратить свое время на то, чтобы печатать вещи, которых в любом случае не произойдет.
So I wanna go NET for short, 10.1.1.4.|Итак, я хочу для краткости использовать NET, 10.1.1.4.
All right?|Отлично?
And that's all you put, and then NET 192.168., oh, wow.|И это все, что вы ставите, а затем NET 192.168., О, вау.
Finger memory.|Память пальцев.
192.168.|192.168.
Oh, the num lock key.|О, ключ от num lock.
Silly man.|Глупый человек.
192.168.1.0.|192.168.1.0.
Enter.|Войти.
And what command can we not forget?|А какую команду нельзя забыть?
What is a command that we have to know for this inspector running protocols?|Какую команду мы должны знать, чтобы этот инспектор запускал протоколы?
No auto hyphen summary.|Сводка без автоматического переноса.
Very good there, Charles.|Очень хорошо, Чарльз.
Very good.|Очень хорошо.
#NO AUTO-SUMMARY.|# НЕТ АВТО-РЕЗЮМЕ.
All right?|Отлично?
That's it.|Вот и все.
That's all you do.|Это все, что ты делаешь.
But let me show you,|Но позвольте мне показать вам,
I'm going to cheat because I can.|Я собираюсь обмануть, потому что могу.
You can't.|Вы не можете.
You gotta go back to publish mode and type copy run start enter enter.|Вам нужно вернуться в режим публикации и набрать, скопировать, запустить, ввести, ввести.
But I wanna show you something.|Но я хочу тебе кое-что показать.
You saw that I put 10.1.1.4.|Вы видели, что я поставил 10.1.1.4.
I put the entire network that I'm connected to.|Ставлю всю сеть, к которой подключен.
All right, show start.|Хорошо, начало шоу.
Come on.|Давай.
Do you see that I put 10 triple 0?|Вы видите, что я поставил 10 тройных 0?
Cuz RIP doesn't see that mask,|Потому что RIP не видит эту маску,
it only sees the class full boundary.|он видит только полную границу класса.
That is why it's essential to type that command.|Вот почему так важно набрать эту команду.
That command did not exist in RIP version one.|Эта команда не существовала в первой версии RIP.
It exists now in RIP version two and EIGRP, all right?|Сейчас он существует во второй версии RIP и EIGRP, понятно?
So you must type it.|Так что вы должны это ввести.
That command right there, you will see it in print screens, ladies and gentlemen.|Эта команда прямо здесь, вы увидите ее на экранах печати, дамы и господа.
All right, we're, hey, the administrator can't get their labs to talk to each other, but the routers connected to each other can, what's the problem?|Хорошо, мы, эй, администратор не может заставить их лаборатории разговаривать друг с другом, но маршрутизаторы, подключенные друг к другу, могут, в чем проблема?
And then they show you like a routing table.|А потом вам покажут как таблицу маршрутизации.
Because he forgot to put that.|Потому что он забыл это поставить.
Because everything is being summarized.|Потому что все резюмируется.
Imagine everything being a class A or a class B, I think I said it in the,|Представьте, что все это класс A или класс B, я думаю, что сказал это в,
in the, previous lesson.|в предыдущем уроке.
Where do I send the packet if all I see is a big ten triple zero network but I wanna go specifically to this network?|Куда мне отправить пакет, если все, что я вижу, - это сеть большой десятки и тройного нуля, но я хочу перейти именно в эту сеть?
Your router's like, I don't know where to send you, I'll just send you out this way.|Ваш роутер такой: я не знаю, куда вас отправить, я просто отправлю вас сюда.
So you may get lucky, you may not.|Так что тебе может повезти, а может и нет.
So you must put the no auto summary when using distance vector routing protocol.|Таким образом, при использовании протокола векторной маршрутизации расстояния вы должны указывать автоматическую сводку.
Let's take a look at the routing table.|Взглянем на таблицу маршрутизации.
Show IP route.|Показать IP-маршрут.
Hey, there's nothing there.|Эй, там ничего нет.
I just configured RIP,|Я только что настроил RIP,
but there's nothing there.|но там ничего нет.
Of course not.|Конечно нет.
There's not gonna be anything there because RIP doesn't talk to itself.|Там ничего не будет, потому что RIP не разговаривает сам с собой.
RIP has gotta have somebody to snitch to.|У RIP есть к кому стучать.
So you gotta configure RIP in the other router.|Поэтому вам нужно настроить RIP на другом маршрутизаторе.
In the other router.|В другом роутере.
Because remember, they only talk,|Потому что помните, они только говорят,
they only talk to neighbors, and router two is the neighbor.|они разговаривают только с соседями, а второй маршрутизатор является соседом.
So the neighbor doesn't have RIP version two, but what does the neighbor have?|Итак, у соседа нет второй версии RIP, но что есть у соседа?
This where we looked at it previously,|Здесь мы уже рассматривали это ранее,
or we configured it previously.|или мы настроили его ранее.
We did a static route, but what did I forget to do?|Мы сделали статический маршрут, но что я забыл сделать?
Did I do it on purpose,|Я сделал это специально,
or did I just forget?|или я просто забыл?
I think I just forgot.|Думаю, я просто забыл.
We didn't change the administrative distance and.|Мы не меняли административную дистанцию ​​и.
[SOUND] LDIAZ, Cisco.|[ЗВУК] ЛДИАЗ, Cisco.
Let's do a show start, all right?|Давай начнем шоу, хорошо?
So let's go down,|Так что пойдем вниз,
let's go down, let's go down.|пойдем вниз, пойдем вниз.
Blah blah blah blah,|Бла-бла-бла-бла,
basic avs and configs.|основные авы и конфиги.
Lovely, lovely, lovely.|Прекрасно, мило, мило.
Ha, we have a static actual static route.|Ха, у нас есть статический фактический статический маршрут.
Not our default route,|Не наш маршрут по умолчанию,
because default routes can only configure on, stub routers.|потому что маршруты по умолчанию можно настроить только на тупиковых маршрутизаторах.
Here we have a static route, but we didn't change the administrative distance.|Здесь у нас есть статический маршрут, но мы не меняли административное расстояние.
So if I can figure RIP here,|Итак, если я могу понять RIP здесь,
and I will, all right?|и я буду, хорошо?
I'm gonna show you that RIP is not gonna go on the routing table.|Я покажу вам, что RIP не попадет в таблицу маршрутизации.
Why?|Зачем?
Because we have a static route.|Потому что у нас есть статический маршрут.
So let's take a look at it.|Итак, давайте посмотрим на это.
So let's, let's do that so you can believe me.|Итак, давайте, давайте сделаем это, чтобы вы мне поверили.
ROUTER [COUGH]|МАРШРУТИЗАТОР [КАШЕ]
RIP version two.|RIP версия вторая.
I also get this question.|Мне тоже задают этот вопрос.
A lot from students,|Много от студентов,
especially in the classroom.|особенно в классе.
Hey, Laz,|Привет, Лаз,
do we always have to do it in that order?|всегда ли мы должны делать это в таком порядке?
Router RIP version two, network,|Маршрутизатор RIP версии 2, сетевой,
network on auto summary?|сеть на авто сводке?
Say no, no, you don't have to.|Скажи нет-нет, тебе не обязательно.
You can do Router RIP network, network.|Можно сделать маршрутизатор RIP сеть, сеть.
Or network version two, then network.|Или сетевая версия два, потом сетевая.
I mean, whatever makes you happy.|Я имею в виду то, что делает тебя счастливым.
But just don't for, and then auto summary.|Но только не для, а потом автоматическое резюме.
Don't forget to put the commands.|Не забудьте поставить команды.
So this is the way that I did it,|Вот как я это сделал,
that I'm accustomed to doing it.|что я привык это делать.
Because my brain, you know,|Потому что мой мозг, ты знаешь,
as I grow in years Yet,|как я расту с годами,
so I will put version two,|так что поставлю вторую версию,
right off the bat.|с места в карьер.
Because, it's easy to forget to put version two, and then I have version one.|Потому что легко забыть поставить вторую версию, а потом у меня будет первая.
So, router RIP, version two, then advertise the networks, and then the very last thing put model summary, is that a rule in blood in the stone, of course not.|Итак, маршрутизатор RIP, версия два, затем рекламирует сети, а затем последнее, что помещает резюме модели, это то, что правило кровью в камне, конечно же, нет.
But that's just a guideline that I'm giving you.|Но это всего лишь рекомендация, которую я вам даю.
If you wanna do it, you know, the opposite way, I mean, it's completely up to you.|Если вы хотите сделать это, знаете, наоборот, я имею в виду, это полностью зависит от вас.
I'm just giving you a guideline of what to do.|Я просто даю вам руководство, что делать.
As long as you type all the commands in,|Пока вы вводите все команды,
I'm a happy camper, and so will you when you pass your CCNA.|Я счастливый турист, и вы тоже, когда сдадите экзамен CCNA.
All right, now I'm gonna go on network,|Хорошо, теперь я пойду в сеть,
so I'm attached to the 10.0.0.0.|поэтому я привязан к 10.0.0.0.
You're not attached to 10.0.0.0 you're attached to the 10114 and the 10118.|Вы не привязаны к 10.0.0.0, вы подключены к 10114 и 10118.
I know I am, but did it not put it back to a 10 triple 0?|Я знаю, что да, но разве это не вернуло его к 10 тройным 0?
So why am I going to type both networks when it's only going to summarize it to the 10 triple 0?|Итак, почему я собираюсь набрать обе сети, если я собираюсь суммировать это только до 10 тройных 0?
All right?|Отлично?
So, and now I'm in the network, 192.168.|Итак, теперь я в сети 192.168.0.1.
1.2, right?|1.2, правда?
Oh, 2.0, 2.0.1.2.|Ой, 2.0, 2.0.1.2.
2.0, and then what can you not forget?|2.0, а чего тут не забыть?
No auto, on a hi, tab that.|Нет авто, привет, вкладка.
No auto summary which you can in the test,|Нет автоматического резюме, которое вы можете в тесте,
I don't know if you can or not.|Не знаю, сможешь ты или нет.
People are telling me that you can't so if you can, perfect it.|Люди говорят мне, что вы не можете, поэтому, если можете, усовершенствуйте это.
If you, if you cannot, make sure that you type out the whole thing in auto summary.|Если вы, если не можете, убедитесь, что вы напечатали все это в автоматическом сводке.
First learn how to type out the whole command, you know, the spelling and all that,|Сначала научитесь печатать всю команду, понимаете, орфографию и все такое,
cause after you get into the real world,|Потому что после того, как вы попадете в реальный мир,
if you're already in the real world, using the certification for, you know, credit,|если вы уже находитесь в реальном мире, используя сертификацию, вы знаете, кредит,
props, more money,|реквизит, больше денег,
whatever the case may be.|в любом случае.
You know, you forget to,|Знаешь, ты забываешь,
you forgot how to spell, honestly.|ты разучился писать, честно.
Tab this, tab that,|Вкладка, вкладка,
abbreviate this, abbreviate that.|сократите это, сократите это.
But for testing purposes, for the CCNA,|Но в целях тестирования для CCNA,
you gotta type out the whole thing.|вы должны напечатать все это.
All right, so be very careful.|Хорошо, так что будьте очень осторожны.
So no auto summary.|Так что никакого автоматического резюме.
And download do WR, not ER, do WR.|И загрузите WR, а не ER, сделайте WR.
And I'll do a do show IP route,|И я покажу IP-маршрут,
do show IP route.|показывать IP-маршрут.
And low and behold, no RIP.|И низко и вот, никакого RIP.
But hey, you, hey Laz you said that if two routers are neighbors with each other,|Но эй, ты, эй, Лаз, ты сказал, что если два маршрутизатора соседствуют друг с другом,
they're going to talk, yes I did.|они собираются поговорить, да, я говорил.
But I also just said that hey,|Но я также просто сказал, что эй,
we configured static routes with a lower administrative distance then RIP cause RIP is administrative distance is what?|мы настроили статические маршруты с меньшим административным расстоянием, чем RIP, потому что RIP - это административное расстояние, что?
It's 120, the static routes we configured have 0 because we're using the exit interface.|Это 120, статические маршруты, которые мы настроили, имеют 0, потому что мы используем интерфейс выхода.
So how do we fix that?|Так как же это исправить?
Well, we got two options.|Что ж, у нас есть два варианта.
We can get rid of the static routes all together,|Мы можем полностью избавиться от статических маршрутов,
or, we can change the administrative distance at of the static routes and have them there as backup.|или мы можем изменить административное расстояние статических маршрутов и использовать их в качестве резервных.
If RIP goes insane, for you know in IT,|Если RIP сойдет с ума, как вы знаете в ИТ,
things go insane because they want to.|вещи сходят с ума, потому что они хотят.
And RIP goes bad,|И RIP выходит из строя,
you still have static routes to back,|у вас все еще есть статические маршруты назад,
oh you're changing routing protocol I'd say, you want to get rid of RIP without losing connectivity and put another routing protocol?|ой вы меняете протокол маршрутизации, я бы сказал, вы хотите избавиться от RIP без потери связи и поставить другой протокол маршрутизации?
You have your static routes that will take over for you right away.|У вас есть статические маршруты, которые сразу же возьмут на себя вас.
So what we're going to is we're going to change the administrive distance of the static routes to 150.|Итак, мы собираемся изменить административное расстояние статических маршрутов на 150.
So they can remain in the background and RIP will get into the routing table.|Таким образом, они могут оставаться в фоновом режиме, а RIP попадет в таблицу маршрутизации.
Let's see how we do that.|Посмотрим, как мы это сделаем.
So we have configure RIP already,|Итак, мы уже настроили RIP,
it's there.|Это здесь.
The static routes are there but we need to change them, so how do we do that?|Статические маршруты есть, но нам нужно их изменить, так как же нам это сделать?
Let's exit one time.|Давай выйдем один раз.
We need to be in global configuration.|Нам нужно быть в глобальной конфигурации.
All right.|Отлично.
I'm gonna open this a little bit more.|Я открою это еще немного.
Make sure that I'm not in the way,|Убедитесь, что я не мешаю,
all right.|отлично.
I'm gonna do a, a do show start,|Я собираюсь начать шоу,
and why am I gonna do that?|и зачем мне это делать?
Cause I wanna see the static routes.|Потому что я хочу увидеть статические маршруты.
Cause I wanna copy paste, big time.|Потому что я хочу скопировать пасту, большое время.
Cause I'm not gonna rewrite all this.|Потому что я не собираюсь все это переписывать.
So I'm gonna do a Ctrl+C at this moment,|Так что сейчас я сделаю Ctrl + C,
control Charlie.|контролировать Чарли.
And there's my static routes right there.|И вот тут мои статические маршруты.
So what I'm gonna do is,|Итак, что я собираюсь сделать,
I'm gonna type NO, so I can get rid of,|Я наберу НЕТ, чтобы избавиться от
I'll do the first one first.|Сначала я сделаю первый.
I'm gonna copy.|Я скопирую.
And then I'm gonna paste.|А потом я вставлю.
That static route is gone,|Этот статический маршрут исчез,
but I'm gonna put it back.|но я верну его обратно.
I'm gonna paste it again.|Я вставлю это снова.
But this time I'm gonna space and go 150.|Но на этот раз я выхожу в космос и иду 150.
I just made, I redid the static route but now I changed the administrative distance,|Я только что сделал, переделал статический маршрут, но теперь изменил административное расстояние,
and I'll bring it up so you can see it.|и я подниму это, чтобы вы это увидели.
The administrative distance to 150.|Административное расстояние до 150.
Now there,|Сейчас,
you see that the routing protocol is got to make it to the routing table.|вы видите, что протокол маршрутизации должен попасть в таблицу маршрутизации.
Yes indeed.|Да, в самом деле.
So let's do the second one.|Итак, займемся вторым.
Let's copy that bad boy right there.|Давайте прямо сейчас скопируем этого плохого парня.
And you can see that?|И вы это видите?
Yes, perfect.|Да, идеально.
I'm gonna type NO, and then I'm going to paste.|Я наберу НЕТ, а затем вставлю.
That's the rid,|Это избавление,
that gets rid of that second static route.|это избавляет от этого второго статического маршрута.
I'm gonna repaste it again.|Я собираюсь снова его отшить.
But, this time, space 150.|Но на этот раз пробел 150.
I'm gonna do it the right way.|Я сделаю это правильно.
Not the right way, the test way.|Не правильный путь, тестовый путь.
And do a COPY RUN START,|И сделайте ЗАПУСК КОПИРОВАНИЯ,
that's how you got to do it.|вот как вы должны это делать.
Enter.|Войти.
Do you wanna copy to the start and config?|Хотите скопировать в начало и конфиг?
Obviously.|Очевидно.
So just henter, Enter, again.|Так что просто введите, Enter, еще раз.
And then as we'll show,|А потом, как мы покажем,
start, and I see what we see.|старт, и я вижу то, что мы видим.
Let's see if those static routes did change.|Посмотрим, изменились ли эти статические маршруты.
Sure, indeed.|Конечно, конечно.
There is now, they have a 150.|Есть сейчас у них 150.
So it,|Так что,
now when I look at the routing table,|теперь, когда я смотрю на таблицу маршрутизации,
what needs to happen is the following.|должно произойти следующее.
We should not see any Ss,|Мы не должны видеть никаких Ss,
all we should see are Rs and connected routes because we change the administrative distance.|все, что мы должны увидеть, это Rs и связанные маршруты, потому что мы меняем административное расстояние.
Let's see if this makes me a liar.|Посмотрим, делает ли это меня лжецом.
Show IP ROUTE.|Показать IP-МАРШРУТ.
Bada bing, bada boom.|Bada bing, bada boom.
There it is, all right?|Вот оно, понятно?
Now we are learning and that's what this means.|Сейчас мы учимся и вот что это значит.
We are learning about the 1.0 network from RIP.|Мы узнаем о сети 1.0 от RIP.
You know it's RIP because there's your AD right there,|Вы знаете, что это RIP, потому что прямо там ваша реклама,
your administrative distance of 120.|ваше административное расстояние 120.
We are one router away, one hot count.|Мы на расстоянии одного роутера, один горячий счет.
How are we learning this?|Как мы этому учимся?
Through 10.1.1.5.|Через 10.1.1.5.
On what interface?|На каком интерфейсе?
Let me open this.|Позвольте мне открыть это.
On my S 0 0 1.|На моем S 0 0 1.
That's how you read this.|Вот как вы это читаете.
Okay?|Ладно?
And the same thing holds true,|И то же самое,
well that's the only one, okay,|ну это единственный, ладно,
that's the only one that's there.|это единственный, что есть.
Hm, that one didn't update yet.|Хм, тот еще не обновился.
Oh this, look, look at this.|О, это, посмотри, посмотри на это.
Since router three, since router three,|Начиная с третьего маршрутизатора, начиная с третьего маршрутизатора,
I haven't configured RIP on it yet.|Я еще не настроил на нем RIP.
You see that my static route is still there to get to that network.|Вы видите, что мой статический маршрут все еще существует, чтобы добраться до этой сети.
Because RIP is not configured on the last router, but I can still get to that network because there's a static route for it.|Поскольку RIP не настроен на последнем маршрутизаторе, я все еще могу добраться до этой сети, потому что для нее существует статический маршрут.
You see the importance?|Вы понимаете важность?
So I have a combination of connected RIP and static routes.|Итак, у меня есть комбинация подключенных RIP и статических маршрутов.
Amazing.|Удивительный.
So now what is that telling you?|Итак, что это вам говорит?
You can use a different combination of things.|Вы можете использовать разные комбинации вещей.
That's why I don't want to get into design of a network,|Поэтому я не хочу вдаваться в дизайн сети,
that's a whole another class,|это совсем другой класс,
you know, course.|знаете, конечно.
Completely, but, so you can start opening your mind to say,|Полностью, но, чтобы вы могли начать открывать свой разум, чтобы сказать:
okay, how can I use a combination of different things,|хорошо, как я могу использовать комбинацию разных вещей,
depending on what type of network I'm working with.|в зависимости от того, с какой сетью я работаю.
All right?|Отлично?
And, especially, dealing with the bandwidth, with the bandwidth.|И особенно, имея дело с пропускной способностью, с пропускной способностью.
All right.|Отлично.
So see the R made it to the routing table for that particular one.|Итак, посмотрите, как R попал в таблицу маршрутизации для этого конкретного.
Now we're gonna go to the last router.|Теперь перейдем к последнему роутеру.
Now, remember, router two still had one S.|Помните, что на втором маршрутизаторе все еще был один S.
Because it had that network that,|Потому что у него была сеть,
you know, that's on router three and we haven't configured anything on router three, yet.|вы знаете, это на третьем маршрутизаторе, а на третьем маршрутизаторе мы еще ничего не настроили.
So let's go ahead and do router three, the last router.|Итак, давайте продолжим и займемся третьим маршрутизатором, последним маршрутизатором.
Okay.|Ладно.
And let's again, let's open this up.|И давайте еще раз, давайте откроем это.
All right, let's go to the C align Here we have default routes so we don't have to worry about changing anything like that.|Хорошо, перейдем к C align. Здесь у нас есть маршруты по умолчанию, поэтому нам не нужно беспокоиться об изменении чего-либо в этом роде.
C I S C O.|C I S C O.
Cool.|Прохладно.
Config T.|Конфиг T.
Router rip.|Маршрутизатор рип.
Ver two, version two.|Версия вторая, версия два.
Network ten triple zero.|Сеть десять, тройной ноль.
Network one nine two dot one six eight dot three dot zero.|Сеть один девять две точки один шесть восемь точек три точки ноль.
And, well, we can't, what we cannot forget, no auto hyphen summary.|И, что ж, мы не можем, то, что мы не можем забыть, - никакого резюме с автоматическим дефисом.
Do WR.|Сделайте WR.
Control z.|Control z.
Show IP route.|Показать IP-маршрут.
And there we go.|И вот так.
Now we got full bars right here.|Теперь у нас есть полные бары.
We have our default route,|У нас есть маршрут по умолчанию,
there's your gateway of last resort.|вот вам выход на крайний случай.
But here's a one network, right?|Но ведь здесь одна сеть, верно?
That router two also learned about.|Об этом роутере 2 тоже узнал.
But router two is one hop away,|Но второй маршрутизатор находится на расстоянии одного прыжка,
we are two hops away.|мы на расстоянии двух прыжков.
All right?|Отлично?
And here is the second network,|А вот и вторая сеть,
which is, or the second LAN,|который есть, или второй LAN,
which is only one hop away.|который находится всего в одном прыжке.
But we're learning it via the same interfaces, all right,|Но мы учимся через те же интерфейсы, ладно,
because they're sending it through the 10119, and we're learning it on the 0001.|потому что они отправляют его через 10119, а мы изучаем его через 0001.
Okay?|Ладно?
And then you're connected to your directly connected networks.|И тогда вы подключены к своим напрямую подключенным сетям.
And you have your default route.|И у вас есть маршрут по умолчанию.
Let's go back to router two.|Вернемся ко второму маршрутизатору.
Let's see if that S changed for us.|Посмотрим, изменилось ли это S для нас.
See that?|Видеть, что?
Remember?|Помните?
That was previous.|Это было раньше.
We had an S.|У нас был S.
So let's go ahead and do a show IP ROUTE again.|Итак, давайте продолжим и снова проведем шоу IP ROUTE.
Did that S go away?|Это S ушло?
It sure did.|Да, конечно.
No more S.|Больше нет С.
Now we have the one,|Теперь у нас есть тот,
that we had there before, and now we're learning about the three.|что у нас было там раньше, а теперь мы узнаем о трех.
No longer it's a static route.|Это больше не статический маршрут.
No longer.|Больше никогда.
All right?|Отлично?
So you can see how that works cuz we changed the administrative distances and routing protocol took over.|Итак, вы можете увидеть, как это работает, потому что мы изменили административные расстояния, и протокол маршрутизации вступил во владение.
But we have backup routes, and we have those default routes on the stub routers in case,|Но у нас есть резервные маршруты, и у нас есть маршруты по умолчанию на тупиковых маршрутизаторах на случай, если
in case somebody wants to come through,|на случай, если кто-то захочет пройти,
that we don't have a network in there.|что у нас там нет сети.
Because if you look at the last routers,|Потому что если вы посмотрите на последние роутеры,
there's really no networks,|действительно нет сетей,
now we are because we are doing a rip, but if someone were to add another network,|сейчас мы делаем рип, но если кто-то добавит еще одну сеть,
we really don't need to advertise it.|нам действительно не нужно его рекламировать.
So let's say, you know, let's say we add another subnet here to router two.|Допустим, мы добавляем еще одну подсеть к маршрутизатору 2.
And we want to get, we,|И мы хотим получить, мы,
we put that within the routing protocol.|мы помещаем это в протокол маршрутизации.
But, when he tries to get over there,|Но когда он пытается добраться туда,
this one won't have any entries.|у этого не будет никаких записей.
So, you go ahead.|Итак, вперед.
It will still get through because that's the purpose of the default routes.|Он все равно пройдет, потому что это назначение маршрутов по умолчанию.
If the routing table has no entry for the destination network,|Если в таблице маршрутизации нет записи для сети назначения,
it will use the gateway of last resort to get out.|он воспользуется последней возможностью, чтобы выбраться отсюда.
That's the whole purpose of those default routes, or those default static routes,|В этом вся цель этих маршрутов по умолчанию или статических маршрутов по умолчанию,
at the end, all right?|в конце концов, хорошо?
But now we in the world of dynamic routing.|Но теперь мы в мире динамической маршрутизации.
Now, that's RIP version 2.|Теперь это RIP версии 2.
Well, what about RIPng?|Ну что насчет RIPng?
Well, we have to configure IPV6.|Что ж, нам нужно настроить IPV6.
So we're gonna turn this into a dual-stack type scenario, all right?|Итак, мы собираемся превратить это в сценарий типа двойного стека, хорошо?
So what are we gonna do?|Итак, что мы будем делать?
All right, I'm gonna go ahead and just come up with an IPv6 network,|Хорошо, я собираюсь создать сеть IPv6,
we're not gonna subnet right now.|мы не собираемся подсеть прямо сейчас.
So, or do we even have a lab for IPv6?|Итак, или у нас вообще есть лаборатория для IPv6?
Well, we'll just, make one up.|Ну, мы просто придумаем.
Ok, 2001, colon 3200, colon.|Хорошо, 2001, двоеточие 3200, двоеточие.
Face.|Лицо.
Colon, Facebook.|Колон, Facebook.
Facebook.|Facebook.
Okay?|Ладно?
And then 1,000.|А потом 1000.
All right?|Отлично?
Colon, colon, and let's use a 56.|Двоеточие, двоеточие и давайте использовать 56.
All right.|Отлично.
And we'll increment on the second position.|И мы увеличим на второй позиции.
We'll Ctrl+C, Ctrl+V,|Мы будем Ctrl + C, Ctrl + V,
Ctrl+V, Ctrl+V, Ctrl+V.|Ctrl + V, Ctrl + V, Ctrl + V.
I'm just gonna,|Я просто собираюсь
just lay these out right here, All right.|просто выложи это прямо здесь, хорошо.
Hey, come back.|Эй, вернись.
I'll put them down here, give ourselves a little bit more room, all right?|Я положу их сюда, дадим себе немного больше места, хорошо?
I'll change the numbers in a second.|Я поменяю цифры через секунду.
I'm just pasting them up there.|Я просто наклеиваю их туда.
So you're going to be quick about it.|Так что поспешите с этим.
Cool, I made enough.|Круто, я сделал достаточно.
All right, so we're going incrementing in the second position, all right,|Хорошо, теперь мы будем увеличивать вторую позицию, хорошо,
on that first zero on the subnet portion of it.|на этом первом нуле в подсети.
And then this one's going to be 1100.|А потом будет 1100.
This one's going to be 1200.|Это будет 1200.
This one's gonna be up here at 1300.|Этот будет здесь в 13:00.
And this is, I mean, I'm not, I didn't just configure this out of the blue.|И это, я имею в виду, я не так, я не просто настроил это на ровном месте.
I don't want you to think, oh my God,|Я не хочу, чтобы ты думала, боже мой,
Laz is like he thinks in IPv6.|Лаз похож на IPv6.
No, no.|Нет нет.
This is from previous labs that I've done before,|Это из предыдущих лабораторных работ, которые я делал раньше,
all right, I remember these numbers.|хорошо, я помню эти числа.
Yeah, I know,|Да, я знаю,
I got some things in my brain that I don't know how they stay there.|У меня в голове есть кое-что, что я не знаю, как они там остаются.
Can't remember a phone number,|Не могу вспомнить номер телефона,
but I, I'll remember this.|но я запомню это.
F 1400.|Ф 1400.
So we got these four networks running.|Итак, мы запустили эти четыре сети.
Now it's important, and this is going to be the, the foundation,|Теперь это важно, и это будет основой,
the groundwork for any IPv6 lab that you're gonna do.|фундамент для любой лаборатории IPv6, которую вы собираетесь делать.
So in actuality we're doing a dual stack scenario here.|Так что на самом деле мы здесь реализуем сценарий с двойным стеком.
A dual stack.|Двойной стек.
So let's go to the very first router.|Итак, перейдем к самому первому роутеру.
Now if you are going to do routing,|Теперь, если вы собираетесь выполнять маршрутизацию,
and I don't know if I said this before,|и я не знаю, говорил ли я это раньше,
and if I didn't, I wanna say it now.|и если бы я этого не сделал, я хочу сказать это сейчас.
And if you're gonna be routing an IPv6,|И если вы собираетесь маршрутизировать IPv6,
one of the first things you need to do is turn on IPv6 unicast routing,|одно из первых, что вам нужно сделать, это включить одноадресную маршрутизацию IPv6,
or you will not route anywhere.|или никуда не поедешь.
Or you will not route anywhere.|Или никуда не поедешь.
So, well, we actually need to put the IP addresses, don't we?|Итак, нам действительно нужно указать IP-адреса, не так ли?
Well, I'm gonna go ahead and just do that IPv6.|Что ж, я просто сделаю IPv6.
Unicast routing,|Одноадресная маршрутизация,
that needs to be turned on.|что нужно включить.
This command is important.|Эта команда важна.
If you don't turn that on,|Если вы не включите это,
you're not gonna route anywhere.|ты никуда не поедешь.
But we have to go into the interfaces and put the IP addresses, all right?|Но мы должны войти в интерфейсы и указать IP-адреса, хорошо?
So, we have the 1,000 for the LAN and we have the 1300|Итак, у нас есть 1000 для локальной сети и у нас есть 1300
between the WANs up here, right?|между WAN здесь, верно?
So, we're going to go inside interface.|Итак, мы идем внутрь интерфейса.
F0, slash 0.|F0, косая черта 0.
Enter.|Войти.
Now, we need to put an IPv6 address.|Теперь нам нужно указать IPv6-адрес.
IPv6 address, and this is where copy paste comes in really handy, but that's okay.|IPv6-адрес, и именно здесь копипаст очень пригодится, но это нормально.
2001:3200:FACE Colon,|2001: 3200: Колонна ЛИЦА,
1000, colon, colon, f.|1000, двоеточие, двоеточие, f.
Slash, this is cool.|Слэш, это круто.
Fif, oops, 56.|Fif, ой, 56.
That is so cool,|Это так круто,
that we can go ahead and use the actual.|что мы можем пойти дальше и использовать фактическое.
Remember, that's not a sider.|Помните, это не сторонник.
That is not a sider,|Это не сторонник,
this is a network prefix.|это сетевой префикс.
All right, we can't call it a sider no more because this deals with the routing portion of it.|Хорошо, мы не можем больше называть это сайдером, потому что здесь речь идет о его маршрутизации.
It has nothing to do with the host.|Это не имеет ничего общего с хозяином.
Okay?|Ладно?
So we put in the IP address for that, let's put in for the serial.|Итак, мы вводим для этого IP-адрес, давайте вставим серийный номер.
So we're going to go int S zero slash zero slash zero, enter.|Итак, мы собираемся пойти int S нулевая косая черта нулевая косая черта ноль, введите.
IPv6 address,|IPv6-адрес,
2001 colon 3200 colon f a c e colon,|2001 двоеточие 3200 двоеточие f a c e двоеточие,
and then that's, 1300.|а потом это 1300.
Colon, colon, and we can just use one, slash 56.|Двоеточие, двоеточие, и мы можем просто использовать одну косую черту 56.
Now, I don't need to turn it on or anything.|Теперь мне не нужно его включать или что-то в этом роде.
Everything's on,|Все включено,
the interface is already on.|интерфейс уже включен.
The interface already has the clock rate.|Тактовая частота интерфейса уже есть.
I'm just putting an i,|Я просто ставлю i,
an IPv6 version address on there.|адрес версии IPv6 там.
Now, how in the world Do we actually configure RIPing?|Итак, как же мы на самом деле настраиваем RIPing?
Remember I said that all you really need to do is go into the interfaces that you wanted?|Помните, я сказал, что все, что вам действительно нужно, это войти в те интерфейсы, которые вам нужны?
For this particular routing protocol to participate in.|Для участия в этом конкретном протоколе маршрутизации.
So all, I could do, I could do it.|Так что все, что я мог сделать, я мог это сделать.
I'll do it the long way first and then on the second router I'll do it the other way, okay?|Я сначала сделаю длинный путь, а потом на втором роутере сделаю по-другому, хорошо?
So Im gonna go IPV6 ROUTER RIP 1.|Итак, я собираюсь использовать IPV6 ROUTER RIP 1.
What is that one?|Что это?
It's a process.|Это процесс.
It's a process.|Это процесс.
And if you put the question mark, really there's nothing else you can do here.|А если поставить вопросительный знак, действительно, тут больше ничего не поделаешь.
Okay?|Ладно?
You're not gonna change the administrative distance,|Вы не собираетесь менять административное расстояние,
you're not gonna do anything, okay?|ты не собираешься ничего делать, хорошо?
You can only redistribute.|Можно только распространять.
So that router, IPV6 ROUTER RIP 1,|Итак, этот маршрутизатор, IPV6 ROUTER RIP 1,
that's a routing process.|это процесс маршрутизации.
it's a routing process.|это процесс маршрутизации.
Now I need to go into each interface.|Теперь мне нужно перейти к каждому интерфейсу.
Interface F0/0 and enable IPV6 RIP 1 ENABLE.|Интерфейс F0 / 0 и включить IPV6 RIP 1 ВКЛЮЧИТЬ.
That's it.|Вот и все.
No network statements.|Нет сетевых заявлений.
I just enabled that routing process on that particular interface.|Я только что включил этот процесс маршрутизации на этом конкретном интерфейсе.
How simple can it get?|Насколько просто это может быть?
That's great.|Замечательно.
All right, interface S0/0/0.|Хорошо, интерфейс S0 / 0/0.
Same thing, up arrow, done.|То же самое, стрелка вверх, сделано.
CTRL+Z, SWR.|CTRL + Z, КСВ.
And if you look at the start,|И если вы посмотрите на начало,
you have your IPV6 unicast routing that's on, you must have it on, okay?|у вас включена одноадресная маршрутизация IPV6, она должна быть включена, хорошо?
But when you look at the interfaces now,|Но когда вы посмотрите на интерфейсы сейчас,
now you have IPV6 rip 1 enabled,|теперь у вас включен IPV6 rip 1,
IPV6 address 2001,3200, [NOISE].|IPV6-адрес 2001,3200, [NOISE].
So, you have two IP addresses,|Итак, у вас есть два IP-адреса,
right, on each interface.|правильно, на каждом интерфейсе.
If you look at the serial down here,|Если вы посмотрите здесь сериал,
same thing goes, same thing goes.|то же самое, то же самое.
So let's go ahead and continue.|Итак, давайте продолжим.
Now, in second [INAUDIBLE] I was gonna do the short way.|Теперь, через секунду [НЕРАЗБОРЧИВО] я собирался пройти короткий путь.
So we have three interfaces,|Итак, у нас есть три интерфейса,
the S001, S000, and S00.|S001, S000 и S00.
And again it's just enabling a process on the interface, right?|И опять же, это просто включение процесса в интерфейсе, верно?
So, okay.|Так хорошо.
CONFIG T.|КОНФИГ T.
Interface, let's go S0/0/1.|Интерфейс, поехали S0 / 0/1.
Wanting to put an IP address.|Желание поставить IP-адрес.
Okay, this is, this is what it is,|Хорошо, это то, что есть,
the 1,300 side right, yes.|1300 правых сторон, да.
So we go IPV6 [SOUND]|Итак, мы переходим к IPV6 [ЗВУК]
2001:3200 :FACE 1300::2 cuz we used one previously, 56.|2001: 3200: FACE 1300 :: 2, потому что раньше мы использовали 56.
Oops, I forget a colon.|Ой, я забыл двоеточие.
Colon.|Двоеточие.
There we go.|Вот и все.
All right, let's do it again.|Хорошо, давай сделаем это снова.
IPV6.|IPV6.
How about putting an address there, Laz?|Как насчет того, чтобы указать там адрес, Лаз?
IPV6 address 2001 colon 3200 colon FACE colon 1300 colon,|IPV6-адрес 2001 двоеточие 3200 двоеточие FACE двоеточие 1300 двоеточие,
colon, 2 slash 56.|двоеточие, 2 слэш 56.
Ta da.|Да да.
Alright, and then let's go to the adj,|Хорошо, а потом перейдем к прил.
well I'll just enable RIP right now.|ну, я просто включу RIP прямо сейчас.
IPV6, RIP 1 ENABLE.|IPV6, RIP 1 ВКЛЮЧИТЬ.
What is that first thing I said that needed to be done,|Что я сказал в первую очередь, что нужно сделать?
if you wanted to do IPV6?|если вы хотели сделать IPV6?
That's correct.|Это правильно.
IPV6 unicast routing.|Одноадресная маршрутизация IPV6.
Let's go back into the interface.|Вернемся в интерфейс.
Which interface was I in, S00.|В каком интерфейсе я был, S00.
S0/0/1.|S0 / 0/1.
And, [NOISE], there we go.|И, [NOISE], поехали.
So we now enabled the routing process.|Итак, мы включили процесс маршрутизации.
We never went into IPV6 router configuration, all right?|Мы никогда не занимались настройкой маршрутизатора IPV6, понятно?
I just went straight to the interface and enabled it.|Я просто перешел к интерфейсу и включил его.
I'm going to show you something in a second.|Я собираюсь показать вам кое-что через секунду.
Let's go to the F00, INT F0/0, IP address.|Переходим к F00, INT F0 / 0, IP-адресу.
IPV6 address, I'm sorry.|Адрес IPV6, извините.
IPV6 ADDRESS.|АДРЕС IPV6.
And this is going to be 2001 colon 3200,|И это будет 2001 двоеточие 3200,
colon, FACE, colon, and then this is,|двоеточие, ЛИЦО, двоеточие, а затем это,
we started with 1000, 1100, colon, colon,|мы начали с 1000, 1100, двоеточие, двоеточие,
and that's going to be F slash 56.|и это будет F слэш 56.
And then, we gonna do the same thing.|А потом мы сделаем то же самое.
IPV6 RIP 1 ENABLE.|IPV6 RIP 1 ВКЛЮЧИТЬ.
We got one more interface.|У нас появился еще один интерфейс.
We got one more interface.|У нас появился еще один интерфейс.
Which is the serial zero zero zero.|Это серийный ноль ноль ноль.
So we go INT S0/0/0, and that's gonna be the 1400, the 1400.|Итак, мы идем INT S0 / 0/0, и это будет 1400, 1400.
So IPV6 ADDRESS 2001|Итак, АДРЕС IPV6 2001
colon 3200 colon FACE colon, and that's 1400 colon colon 1 slash 56.|двоеточие 3200 двоеточие FACE двоеточие, а это 1400 двоеточие 1 косая черта 56.
And then IPV6 RIP 1 ENABLE.|И затем IPV6 RIP 1 ВКЛЮЧИТЬ.
I'm going to do a DO WR.|Я собираюсь сделать DO WR.
And now let's take a look at the start,|А теперь давайте посмотрим на начало,
so you can see how cool this is.|так что вы можете увидеть, насколько это круто.
IPV6 unicast routing, which I forgot to do, I have to go back and do it before allowing each of the routing protocol.|Одноадресная маршрутизация IPV6, которую я забыл сделать, мне нужно вернуться и сделать это, прежде чем разрешить каждый из протоколов маршрутизации.
And you can see here, I got my LAN,|И вы можете видеть здесь, у меня есть свой LAN,
which we just did, LAN.|что мы только что сделали, LAN.
And here's my serials, right, they're IPV6, and you see RIP 1 is enabled.|А вот и мои серийные номера, правильно, они IPV6, и вы видите, что RIP 1 включен.
But look what it did automatically,|Но посмотрите, что он сделал автоматически,
I didn't do this on this router,|Я не делал этого на этом роутере,
on the other one I did.|на другом я сделал.
But it didn't do it on this one and it puts there all for you.|Но он не сделал этого на этом, и он помещает все для вас.
Can't get any easier than that.|Нет ничего проще.
That's what I wanted to show you.|Это то, что я хотел вам показать.
All right?|Отлично?
And let's do the last router.|И займемся последним роутером.
Let's do the last router.|Сделаем последний роутер.
And that was 1400, okay, this is 1200.|И это было 1400, хорошо, это 1200.
All right.|Отлично.
So going into here.|Итак, зайдем сюда.
All right, so enable, Cisco,|Хорошо, включите, Cisco,
CONFIG T IPV6, Unicast-routing.|CONFIG T IPV6, Unicast-маршрутизация.
Ha-ha, wasn't gonna get me again.|Ха-ха, больше не поймаешь.
So we're gonna do interface S0/0/1 ENTER.|Итак, сделаем интерфейс S0 / 0/1 ENTER.
And we're gonna to put an IPV6 address on there.|И мы собираемся поместить туда адрес IPV6.
IPV6 address that;s going to be 2001|IPV6-адрес, который будет 2001 г.
colon 3200 colon FACE colon,|двоеточие 3200 двоеточие ЛИЦО двоеточие,
that is 1400 colon colon 2 slash 56,|это 1400 двоеточие двоеточие 2 косая черта 56,
and then we're going to enable RIP.|а затем мы собираемся включить RIP.
IPV6 RIP 1 ENABLE.|IPV6 RIP 1 ВКЛЮЧИТЬ.
All right, just to do it and get it out the way, and we go into the fast ethernet.|Хорошо, просто чтобы сделать это и избавиться от этого, и мы перейдем в быстрый Ethernet.
INT F0/0 ENTER, and then we'll put an IP address on there, IPV6 address.|INT F0 / 0 ENTER, а затем мы поместим туда IP-адрес, IPV6-адрес.
And we're gonna do 2001 colon 3200 colon FACE colon, 1200.|И мы сделаем 2001 двоеточие 3200 двоеточие FACE двоеточие 1200.
Oh, what did I do here?|Ой, что я здесь делал?
I hit enter by mistake?|Я нажал "Enter" по ошибке?
Okay.|Ладно.
Colon 1200 colon, colon, and that's going to be F slash 56.|Двоеточие 1200, двоеточие, двоеточие, и это будет F слэш 56.
Alright, and we're gonna enable RIP.|Хорошо, мы включим RIP.
IPV6 RIP 1 ENABLE.|IPV6 RIP 1 ВКЛЮЧИТЬ.
Alright, guess we'll DO WR.|Хорошо, думаю, мы сделаем WR.
Let's verify that everything's hunky-dory.|Проверим, все ли в порядке.
Show start.|Показать начало.
Alright, there's our unicast routing,|Хорошо, вот наша одноадресная маршрутизация,
[SOUND].|[ЗВУК].
There's IPV6.|Есть IPV6.
[SOUND] Show the FastEthernet F,|[ЗВУК] Покажите FastEthernet F,
cool, cool, cool.|круто, круто, круто.
Then we have the 1400, with the two.|Затем у нас есть 1400 с двумя.
All right, all right,|Хорошо, хорошо,
all right, all right.|хорошо, хорошо.
And then we have,|И тогда у нас есть
again automatically it does that for you.|опять же автоматически он делает это за вас.
So let's take a look now at that routing table.|Итак, давайте теперь посмотрим на эту таблицу маршрутизации.
Show IP ROUTE.|Показать IP-МАРШРУТ.
Hey that's that IPV4 routing table.|Эй, это та таблица маршрутизации IPV4.
That's correct,|Это правильно,
because we didnt show IP route.|потому что мы не показали IP-маршрут.
In order to look at the IPV6 routing table we gotta show IPV6 route.|Чтобы посмотреть таблицу маршрутизации IPV6, мы должны показать маршрут IPV6.
And now you are routing in RIPng.|И теперь вы выполняете маршрутизацию в RIPng.
There is your 1000, right?|Вот твоя 1000, да?
There is your 1100.|Вот и ваш 1100.
There is your 1300 network, right?|Есть ваша сеть 1300, да?
We just hit ENTER, keep hitting ENTER.|Мы просто нажимаем ENTER, продолжаем нажимать ENTER.
So, now, you're routing not only with RIP version two.|Итак, теперь вы маршрутизируете не только с помощью RIP версии 2.
You're routing with RIPng.|Вы выполняете маршрутизацию с помощью RIPng.
You're doing static routes in the background.|Вы выполняете статические маршруты в фоновом режиме.
You have default routes on the side.|У вас есть маршруты по умолчанию на стороне.
So you're doing all sorts of routing.|Итак, вы делаете всякие роутинги.
That's all there is to that.|Вот и все.
That's all there is to that.|Вот и все.
So you, dual stack scenario.|Итак, сценарий двойного стека.
And you're using multiple types of routing going on.|И вы используете несколько типов маршрутизации.
This is RIP.|Это RIP.
Very simple, straight to the point.|Очень просто, прямо по делу.
Again when it comes to your certification,|Опять же, когда дело доходит до вашей сертификации,
very minimal questions.|очень минимальные вопросы.
Do know your administrative distances for these routing protocols, all right?|Вы знаете свои административные расстояния для этих протоколов маршрутизации, хорошо?
And understand the differences between using RIP static routes, all right?|И понимаете разницу между использованием статических маршрутов RIP, хорошо?
And the difference, obviously,|И разница, очевидно,
of configuration between RIP version two and RIPng.|конфигурации между RIP версии 2 и RIPng.
I'll see you in the next lesson.|Увидимся на следующем уроке.
We'll start EIGRP.|Запустим EIGRP.