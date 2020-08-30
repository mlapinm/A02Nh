D:\mailCloud\prjother\tmp\1\c70_configuring static routes.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
All right.|Отлично.
Where are we?|Где мы?
What is this strange place that we're in?|Что это за странное место, в котором мы находимся?
Oh, we're in a live router.|О, мы в активном роутере.
Right?|Правильно?
No packet tracer.|Нет трассировщика пакетов.
Hooh, it must be different.|Ух, должно быть иначе.
No.|Нет.
Alright?|Хорошо?
Let's see our configuration.|Посмотрим нашу конфигурацию.
Show IP route.|Показать IP-маршрут.
Look, it's the same thing, it just takes slightly longer, okay?|Слушай, это то же самое, просто нужно немного больше времени, хорошо?
Depending on the RAM we have, but we can,|В зависимости от имеющейся у нас оперативной памяти, но мы можем,
we're not gonna discuss that at this moment.|мы не будем обсуждать это сейчас.
Now, in this router, we don't have any default routes set up, so we're gonna go ahead and actually do it.|В этом маршрутизаторе у нас нет установленных маршрутов по умолчанию, поэтому мы продолжим и фактически сделаем это.
Now, I can tell [UNKNOWN] routers but I'm not gonna do that.|Теперь я могу указать [НЕИЗВЕСТНО] маршрутизаторы, но я не буду этого делать.
I'm gonna show you, I'm gonna pull the console cable out,|Я покажу тебе, я вытащу консольный кабель,
put it back into the second router and I'm gonna hit Enter.|вставьте его обратно во второй роутер, и я нажму Enter.
Even though I do have,|Хотя у меня есть
[BLANK_AUDIO]|[BLANK_AUDIO]
space bar, space bar, my line DTY setup.|пробел, пробел, моя линия DTY setup.
But we're gonna go ahead and let's configure the fall route here.|Но мы продолжим и настроим здесь осенний маршрут.
Config T.|Конфиг T.
Same command.|Та же команда.
IP ROUTE 0.0.0.0 0.0.0.0 oops.|IP ROUTE 0.0.0.0 0.0.0.0 ой.
Right.|Правильно.
That's four 0s yes.|Это четыре 0, да.
Exit interface.|Выйти из интерфейса.
S0/0/0.|S0 / 0/0.
Same thing we just did.|То же, что и мы.
DO WR.|DO WR.
Same thing we just, see how it takes a little bit longer on a real router?|То же самое, что и мы, видим, как на реальном маршрутизаторе требуется немного больше времени?
That's the only difference.|Это единственная разница.
Why, that's why I look to use the packet tracer a lot of the time, all right?|Почему, именно поэтому я часто использую трассировщик пакетов, хорошо?
And let me exit out of here, do a show IP route.|И позвольте мне выйти отсюда, показать IP-маршрут.
And there you can see your gateway of last resorts set.|И там вы можете увидеть свой портал последней надежды.
Wow, it looks just like the packet tracer.|Вау, это похоже на трассировщик пакетов.
All right, now let me show you that I can telnet into the other one.|Хорошо, теперь позвольте мне показать вам, что я могу подключиться к другому через telnet.
So I'm gonna go on in telnet, and really,|Так что я пойду по телнету, и правда,
you don't even have to type telnet.|вам даже не нужно набирать telnet.
I can go 10.1.1.6 Cisco.|Я могу пойти на Cisco 10.1.1.6.
[BLANK_AUDIO]|[BLANK_AUDIO]
And I'm in.|И я в деле.
But I'm not gonna do it that way.|Но я не буду так поступать.
Whoa, Ctrl+Shift+6.|Ого, Ctrl + Shift + 6.
Yeah, see some commands, now you know I'm in the real router because some commands just don't work like that.|Да, посмотрите некоторые команды, теперь вы знаете, что я использую настоящий маршрутизатор, потому что некоторые команды просто так не работают.
Come on, oh sweet mother of.|Давай, милая мать.
Control [UNKNOWN], I'm trying every break command known to mankind.|Контроль [НЕИЗВЕСТНО], я пробую каждую команду прерывания, известную человечеству.
This is one of the reasons that why you type no IP domain lookup.|Это одна из причин, по которой вы не вводите поиск IP-домена.
Okay.|Ладно.
Ctrl+Shift+6|Ctrl + Shift + 6
should take you out of there but it's not doing it for some reason.|должен увести вас оттуда, но по какой-то причине он этого не делает.
Could be my laptop.|Может быть, мой ноутбук.
I don't have a pause break.|У меня нет перерыва на паузу.
Ctrl+C is not working.|Ctrl + C не работает.
Okay.|Ладно.
Well you can see what it's trying to do.|Что ж, вы видите, что он пытается сделать.
It's trying to broadcast out to a DNS server that we haven't configured so,|Он пытается транслировать на DNS-сервер, который мы так не настроили,
it's taking forever.|это займет вечность.
Okay, so I'm gonna exit.|Хорошо, я уйду.
Now I'm back in router one.|Теперь я снова в первом роутере.
Alright?|Хорошо?
But I'm not gonna do it that way.|Но я не буду так поступать.
I'm gonna unplug my console cable, and then I'm gonna plug it in [BLANK_AUDIO]|Я отключу консольный кабель, а потом воткну его [BLANK_AUDIO]
to router two.|к роутеру два.
And now I'm in router two.|И теперь я во втором роутере.
I'm gonna exit out of here.|Я выйду отсюда.
Now at router two, remember, this is where we did our statics routes, where we had it pointed to the 192.168.1.0, and the|Помните, что на втором маршрутизаторе мы выполняли наши статические маршруты, указывали на 192.168.1.0 и
192.168 3.0.|192.168 3.0.
So we gotta figure those routes, so IP ROUTE.|Итак, мы должны вычислить эти маршруты, так что IP ROUTE.
Now here, well, I'll, I'll say it when we start doing it.|Ну вот, я скажу это, когда мы начнем это делать.
IP ROUTE, I wanna go to 192.168.1.0, which is going to our network that's over here.|IP-МАРШРУТ, я хочу перейти на 192.168.1.0, который идет в нашу сеть, которая здесь.
That's a 255.255.255.0 through the exit interface S0/0/1 space,|Это 255.255.255.0 через пространство S0 / 0/1 интерфейса выхода,
not Enter, space, cause one of the things I wanna talk about right now Is the administrative distance.|не входить, пробел, потому что одна из вещей, о которой я хочу поговорить прямо сейчас, - это административная дистанция.
Now I said if you used the exit interface it should show up as a connected route.|Я сказал, что если вы использовали интерфейс выхода, он должен отображаться как связанный маршрут.
But, in later labs, right?|Но в более поздних лабораториях, верно?
Or in later co lectures we're going to talk about dynamic routing.|Или в последующих лекциях мы поговорим о динамической маршрутизации.
I'm going to use this same lab.|Я собираюсь использовать ту же лабораторию.
[BLANK_AUDIO]|[BLANK_AUDIO]
So I need to change the administrative distance.|Поэтому мне нужно изменить административное расстояние.
What is the administrative distance?|Какое административное расстояние?
The administrative distance is the believability of a route.|Административная удаленность - это надежность маршрута.
If it's directly connected,|Если он подключен напрямую,
like it would show up, here cause exit interface it would be zero.|как будто он появится, здесь интерфейс выхода будет нулевым.
If it's a next router's hop address it would be one.|Если это адрес перехода следующего маршрутизатора, это будет один.
Your, the lower the administrative distance the more believable the route.|Ваш, чем меньше административное расстояние, тем правдоподобнее маршрут.
So directly connected routes like the ones with Cs, they're the most believable.|Таким образом, маршруты с прямым подключением, такие как маршруты с буквой C, наиболее правдоподобны.
Then your next most believable are your static routes.|Затем ваши следующие наиболее правдоподобные - статические маршруты.
So when we get to configure RIP, which has an administrative distance of one twenty, it will never make it to the routing table, never.|Поэтому, когда мы настраиваем RIP, административное расстояние которого составляет сто двадцать, он никогда не попадет в таблицу маршрутизации, никогда.
Because its administrative distance is not as believable as the static route.|Потому что его административная удаленность не такая правдоподобная, как статический маршрут.
So, what do we do?|Так что же нам делать?
We Enter at the end of a static route, we enter a higher administrative distance then the routing protocol that we're gonna use.|Мы входим в конце статического маршрута, мы вводим большее административное расстояние, чем протокол маршрутизации, который мы собираемся использовать.
In this case RIP.|В этом случае RIP.
RIP usually is the one with the highest routing protocol unless you're using external eigrp, which I believe is one seventy which we're not using for|RIP обычно имеет самый высокий протокол маршрутизации, если вы не используете внешний eigrp, который, как мне кажется, составляет семьдесят, которые мы не используем для
the CCNA purposes.|целей CCNA.
Okay we're using eigrp internal eigrp which is ninety,|Хорошо, мы используем внутренний eigrp, равный девяносту,
and then we OSPF which is one ten.|а затем мы OSPF, который составляет один десяток.
So one fifty is just fine, for [UNKNOWN]|Так что один пятьдесят вполне достаточно для [НЕИЗВЕСТНО]
goes rip version two,|идет копировать версию два,
which would be the first routing protocol that we do is one twenty.|который будет первым протоколом маршрутизации, который мы сделаем, - это один двадцать.
But why do we do this?|Но зачем мы это делаем?
And let's go ahead and put in the next static route before I forget where gotta put it into.|И давайте продолжим и добавим следующий статический маршрут, пока я не забыл, куда его нужно поместить.
[BLANK_AUDIO]|[BLANK_AUDIO]
All right?|Отлично?
Destination network.|Сеть назначения.
Destination mass.|Назначение масса.
Exit interface.|Выйти из интерфейса.
Administrative distance.|Административная дистанция.
New one.|Новый.
New one.|Новый.
New administrative distance.|Новая административная дистанция.
One fifty.|Один пятьдесят.
And I'm going to go ahead and do It the correct way for the test.|И я собираюсь сделать это правильно для теста.
Copy.|Копировать.
Run.|Запустить.
Start.|Начало.
And we still gotta go to the last router,|И нам все равно нужно перейти на последний маршрутизатор,
router three, and put a default line on there.|маршрутизатор три, и поместите туда линию по умолчанию.
But why am I putting, why am I changing the administrative distance of these static entries, these static routes.|Но почему я ставлю, почему я меняю административное расстояние этих статических записей, этих статических маршрутов.
Because.|Так как.
We can have as you can see we have default routes at our stored routers.|Как видите, у нас есть маршруты по умолчанию на наших сохраненных маршрутизаторах.
In our middle routers we're using static routes but with a higher administrative distance because then we can go ahead and|В наших средних маршрутизаторах мы используем статические маршруты, но с более высоким административным расстоянием, потому что тогда мы можем продолжить и
use a routing protocol.|использовать протокол маршрутизации.
Have static routes as backups.|Используйте статические маршруты в качестве резервных копий.
In case the routing protocol goes haywire we have static routes they're waiting in the wings.|Если протокол маршрутизации выходит из строя, у нас есть статические маршруты, которые ждут своего часа.
In case something goes wrong with the writing protocol,|Если что-то пойдет не так с протоколом записи,
you have a backup aesthetic route, as a backup route.|у вас есть резервный эстетический маршрут, как резервный.
That's the reason I'm showing you this.|Вот почему я вам это показываю.
That you can do this.|Что вы можете это сделать.
All right?|Отлично?
So you can have a combination of routing configured within your routers.|Таким образом, вы можете настроить комбинацию маршрутизации в ваших маршрутизаторах.
And what, the majority of networks out there do this.|И что, большинство сетей делают это.
They have combinations of static routes with routing protocols, and a combination of different routing protocols depending|У них есть комбинации статических маршрутов с протоколами маршрутизации и комбинация различных протоколов маршрутизации в зависимости от
on which routers you're configuring.|на каких маршрутизаторах вы настраиваете.
All right?|Отлично?
So let's go to the last router,|Итак, перейдем к последнему роутеру,
when I get my console cable.|когда я получаю консольный кабель.
I'm going to pull it out, and I'm going to put it back in.|Я вытащу его и вставлю обратно.
To the other router and that is router three.|К другому маршрутизатору, и это третий маршрутизатор.
I want to do enable Cisco.|Я хочу включить Cisco.
Cool and then I'm gonna do let's take a look cause I,|Круто, а потом я сделаю, давайте посмотрим, потому что я,
I did I take that short draw?|Я сделал короткую ничью?
I'm pretty sure I did.|Я почти уверен, что знал.
Show IP route okay?|Показать IP-маршрут в порядке?
Yes, I don't have no LAN attached to it.|Да, у меня к нему нет локальной сети.
I didn't feel like putting it through a computer, okay?|Не хотелось пропускать через компьютер, понятно?
But we can always use a loopback address for that, but when to OSPF we'll do all that.|Но мы всегда можем использовать для этого адрес обратной связи, но в случае с OSPF мы все это сделаем.
Maybe earlier, I don't know.|Может, раньше, не знаю.
So let's go ahead and do our default out here.|Итак, давайте продолжим и сделаем здесь наше значение по умолчанию.
Config T.|Конфиг T.
Not that we need to, but ok, we're gonna do it anyway.|Не то чтобы нам это нужно, но ладно, мы все равно это сделаем.
[BLANK_AUDIO]|[BLANK_AUDIO]
IP route.|IP-маршрут.
I wanna go to the, no, no, it's the default route,|Я хочу пойти по маршруту, нет, нет, это маршрут по умолчанию,
its the other guy, destination network.|это другой парень, сеть назначения.
Destination mask.|Маска назначения.
Exit interface, 80.|Выходной интерфейс, 80.
/0/1.|/ 0/1.
That's a default out there.|Это по умолчанию.
DO WR.|DO WR.
Oh, sorry.|Ой, извини.
Some older IOS here, they didn't want to take my do, okay?|Некоторые старые IOS здесь, они не хотели меня подчинять, хорошо?
And then let's take a look the routing table.|А потом взглянем на таблицу маршрутизации.
Show IP route.|Показать IP-маршрут.
[BLANK_AUDIO]|[BLANK_AUDIO]
All right.|Отлично.
And you see your gateway of last resort is set.|И вы видите, что ваш шлюз последней инстанции настроен.
So I don't have an entry, because I do have a computer,|Так что у меня нет записи, потому что у меня есть компьютер,
that's in the 1.0 network.|это в сети 1.0.
I don't have an entry in this routing table for that, and I'm in router three.|У меня нет записи для этого в таблице маршрутизации, и я нахожусь на третьем маршрутизаторе.
So I should be able to ping 192.168.1.|Итак, я могу пинговать 192.168.1.
let's go for the gateway first.|пойдем сначала на шлюз.
I got there.|Я попал туда.
Let's go for the PC next.|Теперь займемся ПК.
[BLANK_AUDIO]|[BLANK_AUDIO]
And we got that infamous ARP [BLANK_AUDIO]|И у нас есть печально известный ARP [BLANK_AUDIO]
Obviously, it doesn't want to work.|Очевидно, работать не хочет.
Oh, well, well it got to the gateway.|Ну что ж, дошло до ворот.
So it's something going on with the PC, I didn't configure or something.|Так что что-то происходит с ПК, я не настраивал или что-то в этом роде.
But we did get to the gateway, which I'm happy with that.|Но мы добрались до шлюза, чему я доволен.
All right?|Отлично?
So you see that we can route back and forth.|Итак, вы видите, что мы можем двигаться вперед и назад.
We can route back and forth.|Мы можем двигаться вперед и назад.
Using a combination of default routes and static routes but now the only difference that we did from the packet tracer and|Использование комбинации маршрутов по умолчанию и статических маршрутов, но теперь единственное отличие, которое мы сделали от трассировщика пакетов и
to the live routers is that we went ahead and increased the administrative distance.|к живым маршрутизаторам - мы пошли дальше и увеличили административное расстояние.
That way once we get to dynamic routing and we configure a routing protocol all right?|Таким образом, как только мы перейдем к динамической маршрутизации и настроим протокол маршрутизации, все в порядке?
The routing protocol will take effect.|Протокол маршрутизации вступит в силу.
The routing protocol will make it to the routing table,|Протокол маршрутизации попадет в таблицу маршрутизации,
and the static routes will remain in the background waiting silently,|и статические маршруты останутся в фоновом режиме, ожидая беззвучно,
just in case the routing protocol fails,|на случай сбоя протокола маршрутизации,
for whatever reason.|для любой причины.
So there you go, static routes,|Итак, статические маршруты,
administrative distance,|административная удаленность,
default routes, using multiple ways to get to from point a to point b.|маршруты по умолчанию, с использованием нескольких способов добраться из точки a в точку b.
You can see that the live routers are, you know,|Вы можете видеть, что живые маршрутизаторы, знаете ли,
the same commands, than you would, same iOS, all right?|те же команды, что и вы, та же iOS, понятно?
One had, I think, this is a little bit older iOS that doesn't have the do command.|У одного, я думаю, была немного более старая iOS, в которой нет команды do.
But other than that, it's the same, same thing.|Но в остальном это то же самое, то же самое.
All right?|Отлично?
We, but the packets tracer obviously you're moving at lightening speed,|Мы, но трассировщик пакетов, очевидно, движется с молниеносной скоростью,
the packet tracer is meant for BCCNA.|трассировщик пакетов предназначен для BCCNA.
So, you can practice on that safely if you don't, so you feel confident just because you don't have live equipment.|Так что вы можете безопасно практиковаться в этом, если нет, так что вы чувствуете себя уверенно только потому, что у вас нет живого оборудования.
It's the same exact thing.|Это то же самое.
The only thing is that you'll be taking a little bit longer on the live router then you would on the packet tracer.|Единственное, что вам потребуется немного больше времени на активном маршрутизаторе, чем на трассировщике пакетов.
But there you have it.|Но вот оно.
Static and default routes.|Статические маршруты и маршруты по умолчанию.
I'll see you in the next section.|Увидимся в следующем разделе.
[BLANK_AUDIO]|[BLANK_AUDIO]