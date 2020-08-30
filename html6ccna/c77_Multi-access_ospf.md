D:\mailCloud\prjother\tmp\1\c77_Multi-access ospf.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
Okay, welcome back everyone.|Хорошо, с возвращением всех.
Now that we've configured point to point OSPF, and some of the differences between using a serial connection, or an ethernet connection were the priority|Теперь, когда мы настроили OSPF точка-точка, и некоторые различия между использованием последовательного соединения и подключения к сети Ethernet были приоритетными.
numbers change, and there is an election or no election.|числа меняются, выборы есть или нет.
So, now we're understanding what could happen if we're in an ethernet,|Итак, теперь мы понимаем, что может случиться, если мы находимся в сети Ethernet,
ethernet, whether its point to point or not, if it's an ethernet type network,|Ethernet, независимо от того, указывает ли он на точку или нет, если это сеть типа Ethernet,
you're gonna run into that broa broadcast nature type of network,|вы столкнетесь с этим типом сети вещания,
or type of network that will actually have to create an election for DR and BDR.|или тип сети, которая фактически должна будет создать выбор для DR и BDR.
But for your CCNA exam, and let me move the lab the other way, so you guys can see it better.|Но для вашего экзамена CCNA, и позвольте мне перенести лабораторию в другую сторону, чтобы вы, ребята, могли лучше видеть.
This is the multi-access lab.|Это лаборатория с множественным доступом.
This is something that you will see, more than likely,|Это то, что вы, скорее всего, увидите
a scenario like this, in your examination.|такой сценарий в вашем исследовании.
Now, what are we gonna do here?|Что мы будем здесь делать?
We know how to configure OSPF, we know how to advertise our networks using the wild card mask,|Мы знаем, как настроить OSPF, мы знаем, как рекламировать наши сети с помощью маски wild card,
creating a process ID number.|создание идентификационного номера процесса.
There are, and, other routers in the, the same area.|В том же районе есть и другие маршрутизаторы.
Easy enough, easy enough.|Достаточно легко, достаточно просто.
Now, understanding what's going on, it's the issue, right?|Теперь, понимая, что происходит, это проблема, верно?
Not the issue or the concern.|Не проблема или беспокойство.
Here we have a multi-access network, which obviously is a broadcast,|Здесь у нас есть сеть с множественным доступом, которая, очевидно, является широковещательной,
because we're dealing with ethernet.|потому что мы имеем дело с Ethernet.
We have four routers, connected to a switch.|У нас есть четыре маршрутизатора, подключенных к коммутатору.
Now you see there's only one IP address here, which is not one IP address.|Теперь вы видите, что здесь только один IP-адрес, а не один IP-адрес.
One network, which all the fast ethernets,|Одна сеть, в которой все быстрые Ethernet,
will be using.|будет использовать.
And so this will be, let's say, fast ethernet, 1.1, 1.2, 1.3, 1.4.|Итак, это будет, скажем, Fast Ethernet, 1.1, 1.2, 1.3, 1.4.
And when you create this lab, go in that order.|И при создании этой лаборатории действуйте в таком порядке.
At first, and then you can start playing around with it.|Сначала, а потом можно начинать с ней поиграться.
Then, we will configure all SPF,|Затем мы настроим все SPF,
advertising that one network that we're in, and then you're gonna, see what happens,|рекламируя ту сеть, в которой мы находимся, и тогда вы увидите, что произойдет,
because there's an, it's gonna create a new action, and it's gonna choose a particular IP address,|потому что есть, он создаст новое действие и выберет конкретный IP-адрес,
and it should choose, and listen to my words carefully,|и он должен выбирать и внимательно слушать мои слова,
it should choose the highest IP address on any physical interface,|он должен выбрать самый высокий IP-адрес на любом физическом интерфейсе,
to be the DR, and the second highest IP address, to be the BDR.|быть DR, а второй по величине IP-адрес - BDR.
All right?|Отлично?
Once we do this, and we figure out what's going on, who's the DR and the BDR, then we're gonna go ahead and create loopback addresses.|Как только мы это сделаем и выясним, что происходит, кто такие DR и BDR, мы продолжим и создадим адреса обратной связи.
That's why you see the loopback addresses here.|Вот почему вы видите здесь адреса обратной связи.
That will be the secondary portion of the lab,|Это будет второстепенная часть лаборатории,
where we create the loopback addresses,|где мы создаем адреса обратной связи,
and see, and then of course advertising an OSPF, and see, if it chooses that loopback.|и посмотреть, а затем, конечно, объявить OSPF, и посмотреть, выберет ли он эту петлю.
Now it won't do it automatically, there's a command that you're gonna learn here,|Теперь он не будет делать это автоматически, есть команда, которую вы собираетесь изучить здесь,
which is called clear IP OSPF.|который называется чистым IP OSPF.
Process.|Обработать.
Clear IP OSPF process.|Очистить процесс IP OSPF.
And what that does is, just that, it clears the process, so it can recalculate and let the, the new loopback addresses, take effect.|И что это делает, это просто очищает процесс, чтобы он мог пересчитать и позволить новым адресам обратной связи вступить в силу.
Cuz remember, that process ID number,|Потому что помните, этот идентификационный номер процесса,
deals with a links da, database.|занимается ссылками да, база данных.
So, we need to like kick-start that, cuz we add,|Итак, нам нужно понравиться толчком, потому что мы добавляем,
we added a new finding network, right?|мы добавили новую поисковую сеть, верно?
Well, our 11111 network.|Ну наша сеть 11111.
2223, and 444.|2223 и 444.
Sometimes, at work, and I think it's more of a packet tracer thing, that it takes effect.|Иногда на работе, и я думаю, что это больше похоже на трассировщик пакетов, это срабатывает.
Sometimes it doesn't.|Иногда это не так.
What I like to do is, go right into a switch sometimes,|Что мне нравится делать, так это иногда переходить прямо к выключателю,
because I'm not gonna keep trying to clear IP OSPF process.|потому что я не собираюсь продолжать попытки очистить процесс IP OSPF.
I'll do it on all the routers, I'll do it just on the, on two routers,|Я сделаю это на всех роутерах, сделаю только на двух роутерах,
and it still gets a little bit whatever,|и он все еще получает немного,
when I do it on the switch.|когда я делаю это на переключателе.
Nine out of ten times everything reboots,|В девяти из десяти раз все перезагружается,
obviously, the switch,|очевидно, переключатель,
central point of failure.|центральная точка отказа.
Everything reboots, and then, it decides to take place.|Все перезагружается, а затем принимает решение.
But again, I think that's more of a packet tracer thing.|Но опять же, я думаю, что это больше похоже на трассировщик пакетов.
Now, real world scenario, real world scenario,|Теперь сценарий реального мира, сценарий реального мира,
if you're planning to do a network like this we have this broadcast.|если вы планируете создать такую ​​сеть, у нас есть трансляция.
You do not, even though you do the clear IP OSPF process,|Вы этого не сделаете, даже если вы выполняете процесс очистки IP OSPF,
that will still take down the interfaces,|что по-прежнему отключит интерфейсы,
and then bring them back up.|а затем верните их обратно.
So, you will lose connectivity, your users will notice that,|Таким образом, вы потеряете соединение, ваши пользователи заметят, что,
you'll lose connectivity for a period of time, all right?|вы потеряете соединение на какое-то время, хорошо?
And then, but if you bring down the switch, that's another whole nother story right there.|А потом, но если вы нажмете выключатель, это уже совсем другая история.
That's even worse.|Это еще хуже.
So, if you are gonna do something like this, try to not to do it,|Итак, если вы собираетесь сделать что-то подобное, постарайтесь этого не делать,
anything that's gonna be damage, not damaging, but affecting the network.|все, что может повредить, не повредить, но повлиять на сеть.
Where people are like, hey what happened?|Где люди такие, эй, что случилось?
I was just emailing something, or, I was researching something on the internet and now it's gone, or I'm printing something|Я просто что-то отправлял по электронной почте, или, я что-то искал в Интернете, а теперь его нет, или я что-то печатаю
and it just stopped, or what have you.|и это просто прекратилось, что ли у вас.
If it's gonna affect the network, don't do it during, definitely during peak hours.|Если это повлияет на сеть, не делайте этого в часы пик.
So, I don't know, you wait til everybody goes to lunch, or the slow time in the network, or you do it after hours.|Итак, я не знаю, вы ждете, пока все пойдут на обед, или медленное время в сети, или вы делаете это в нерабочее время.
And normally there's things called maintenance windows,|И обычно есть окна обслуживания,
where you can change components, or you can, you know, clear the,|где вы можете изменить компоненты или, ну, знаете, очистить,
if you have no choice but to clear the process, during the day just, you know,|если у вас нет выбора, кроме как очистить процесс, просто в течение дня, вы знаете,
send an email out, first, and warn everyone.|сначала отправьте электронное письмо и предупредите всех.
Check with the higher ups before you do this.|Перед тем, как сделать это, посоветуйтесь с начальством.
They give you the go ahead, they give you the green light, take the burden off you.|Они дают вам добро, дают зеленый свет, снимают с вас бремя.
[LAUGH] All right.|[СМЕХ] Хорошо.
If they give you the green light, you go ahead and do it,|Если они дадут вам зеленый свет, вы сделаете это,
but make sure that everybody's aware, that they may lose connectivity, for a certain period of time.|но убедитесь, что все знают, что они могут потерять соединение на определенный период времени.
You wanna make sure that you warn everybody that, hey, this is gonna happen.|Вы хотите убедиться, что вы предупредили всех, что, эй, это произойдет.
All right?|Отлично?
If you have to do it during the day.|Если придется делать это днем.
If you can help it though, if you can do it after hours, or even at midnight,|Если вы можете помочь, если вы можете сделать это в нерабочее время или даже в полночь,
and IT, unfortunately, you know, our job is 24/7.|и IT, к сожалению, наша работа 24/7.
We do things normally when it's service affecting, or, you know,|Мы обычно делаем что-то, когда это влияет на обслуживание, или, вы знаете,
that's gonna affect the network, we do it between midnight and six in the morning.|это повлияет на сеть, мы делаем это с полуночи до шести утра.
Midnight and six in the morning.|Полночь и шесть утра.
Usually that's the time, we can do a whole bunch of these things.|Обычно в это время мы можем сделать целую кучу этих вещей.
But, anyway, we just wanna make sure that,|Но, в любом случае, мы просто хотим убедиться,
you know, hey well,|ты знаешь, привет хорошо,
we can do this in the world.|мы можем сделать это в мире.
No, no, no, no.|Нет нет Нет Нет.
Be careful before you, you know, you do this testing type thing.|Знаешь, будьте осторожны перед тем, как делать что-то вроде тестирования.
Or unless you have a separate network that you can, you know, play around with.|Или если у вас нет отдельной сети, с которой вы можете поиграться.
But if you actually have a working network, and you wanna add these loopbacks, and these loopbacks that are not taking effect,|Но если у вас действительно есть рабочая сеть, и вы хотите добавить эти петлевые проверки, и эти петлевые проверки, которые не действуют,
and you have to clear that process, you know that that's gonna happen.|и вы должны очистить этот процесс, вы знаете, что это произойдет.
All right?|Отлично?
Once we see what happens and we analyze,|Как только мы увидим, что происходит, и проанализируем,
right, cuz we analyze first with the IP addresses on the physical interfaces, and we see who becomes the DR and the BDR.|правильно, потому что сначала мы анализируем IP-адреса на физических интерфейсах и видим, кто становится DR и BDR.
And, we'll take a look at the states and all that, and then, we finally,|И мы посмотрим на состояния и все такое, а затем, наконец,
we understand that.|мы это понимаем.
And then we put our loopbacks, and then see if anything changed.|Затем мы помещаем петли и смотрим, изменилось ли что-нибудь.
And then, we're gonna play around with our priority numbers,|А потом мы поиграем с нашими приоритетными числами,
with the priority numbers.|с приоритетными номерами.
I personally, personally like to use the priority numbers.|Лично мне нравится использовать приоритетные числа.
Cuz the priority numbers will trump whatever IP address,|Потому что приоритетные числа будут важнее любого IP-адреса,
physically on the interface, or any loopback interface.|физически на интерфейсе или на любом интерфейсе обратной связи.
The priority number is above all that.|Номер приоритета превыше всего.
Now, the highest of all, the king on top of the hill, if, is the router ID.|Теперь, самый высокий из всех, король на вершине холма, если это идентификатор маршрутизатора.
If you hard code, which is something Cisco recommends, if you hard code the router ID, meaning you actually type in with a|Если вы жестко кодируете, что рекомендует Cisco, если вы жестко кодируете идентификатор маршрутизатора, то есть вы фактически вводите
router confi the OSPF router configuration mode, and you put in the router ID of that, of that particular router.|router конфигурирует режим конфигурации маршрутизатора OSPF, и вы вводите идентификатор этого маршрутизатора, этого конкретного маршрутизатора.
Remember the router ID is an IP address.|Помните, что идентификатор маршрутизатора - это IP-адрес.
An IP version 44 mat IP address, which is the name of the router.|IP-адрес версии 44, который является именем маршрутизатора.
That's the, how, that is how that router is identified.|Вот как, вот как идентифицируется этот маршрутизатор.
So, the one with the highest router ID,|Итак, тот, у кого самый высокий идентификатор маршрутизатора,
will always be the the designated router,|всегда будет назначенным маршрутизатором,
and then the second highest.|а затем второй по величине.
So, and that will trump everything, Cisco recommends to do that,|Таким образом, Cisco рекомендует это сделать,
well we're gonna go, we'll stop at a priority number, because again,|ну, мы пойдем, остановимся на приоритетном номере, потому что снова,
sometimes this lab can get a little flaky,|иногда эта лаборатория может немного пошатнуться,
and it could be due to the packet tracer,|и это могло быть связано с трассировщиком пакетов,
but we'll take it a step at a time, and we see that the whole purpose though of this,|но мы будем делать это шаг за шагом, и мы видим, что вся цель этого,
is to understand the election process, the election process.|заключается в понимании избирательного процесса, избирательного процесса.
Now there is no IP addresses configured,|Теперь IP-адреса не настроены,
we're gonna have to do it ourselves.|нам придется сделать это самим.
I'm sure by this point, we all know how to put IP addresses in interface and turn them on, and that's all we're gonna do.|Я уверен, что к этому моменту мы все знаем, как вводить IP-адреса в интерфейс и включать их, и это все, что мы собираемся сделать.
We're not gonna do any admin configs or anything like that.|Мы не собираемся делать никаких административных конфигов или чего-то подобного.
We're gonna go ahead and put IP addresses, but the way that I want you to do this lab.|Мы собираемся указать IP-адреса, но так, как я хочу, чтобы вы выполнили эту лабораторную работу.
And for whatever reason every time I say this, somebody goes off on a tangent and does it their way saying well mine doesn't|И по какой-то причине каждый раз, когда я это говорю, кто-то уходит в обход и поступает по-своему, говоря, что хорошо, что мой - нет.
look like it well did you do this,|похоже, это хорошо, ты сделал это,
no well okay then so if your going to do this at least the first time around okay,|нет ну ладно, тогда если ты собираешься сделать это хотя бы в первый раз, ладно,
do it how I'm gonna do, it I'm gonna configure it in this order this is why they have router 1, router 2, router 3, and router 4.|сделай так, как я собираюсь, я собираюсь настроить это в таком порядке, поэтому у них есть маршрутизатор 1, маршрутизатор 2, маршрутизатор 3 и маршрутизатор 4.
I want you to do it in that order.|Я хочу, чтобы вы сделали это в таком порядке.
I want you to put the IP addresses in that order, and when we configure OSPF,|Я хочу, чтобы вы разместили IP-адреса в этом порядке, и когда мы настраиваем OSPF,
I want you to do it in that order as well.|Я хочу, чтобы вы сделали это и в таком же порядке.
1,2,3,4.|1,2,3,4.
There a, there is a purpose.|Есть цель.
There's a method to the madness of why I want you to do it that way.|Есть метод безумия, почему я хочу, чтобы вы это сделали.
And you'll see it pretty soon.|И вы очень скоро это увидите.
So let's go ahead and configure the 192.168.1.0 which is gonna be all your LANs.|Итак, давайте продолжим и настроим 192.168.1.0, который будет всеми вашими локальными сетями.
All right?|Отлично?
And let's start by router number 1, and we're gonna go nice and easy, no hurry here.|И давайте начнем с маршрутизатора номер 1, и мы будем делать это легко и просто, здесь не нужно торопиться.
We need to understand the election process of the designated router.|Нам нужно понять процесс выбора назначенного маршрутизатора.
And the back up designated router, all right, how that happens.|И резервный назначенный маршрутизатор, хорошо, как это происходит.
Enable, config t.|Включить, настроить t.
Let's name this router one, hostname R1,|Назовем этот маршрутизатор один, имя хоста R1,
so I did, I didn't lie.|так я и сделал, я не лгал.
I didn't say everything, all right?|Я не все сказал, понятно?
We give it a name, hostname router 1.|Мы даем ему имя, hostname router 1.
Interface F0 slash 0 IP address.|Интерфейс F0 слэш 0 IP-адрес.
192.168.1.1.|192.168.1.1.
Right?|Правильно?
We're in the one.|Мы в одном.
Want to make sure of that.|Хочу в этом убедиться.
Yeah, we are in the one.|Да, мы в одном.
All right, and this open it up further.|Хорошо, и это откроет это дальше.
And then we put in the mask, 255.255.255,|Затем мы добавляем маску 255.255.255,
oops.|ой.
Dot 0.|Точка 0.
And we do a no shut.|И мы ничего не делаем.
And I'm going to do a do WR, all right?|И я собираюсь сделать WR, хорошо?
So we're done with router one for now.|Итак, мы закончили с первым маршрутизатором.
We just put the IP address on that particular interface.|Мы просто помещаем IP-адрес в этот конкретный интерфейс.
I'm going to do the same thing here, but this one will be one dot two,|Я собираюсь сделать то же самое здесь, но это будет одна точка два,
one dot three, and one dot four.|одна точка три и одна точка четыре.
So let's go ahead and do that [BLANK_AUDIO]|Так что давайте сделаем это [BLANK_AUDIO]
And, you know what?|И знаешь, что?
Let's just maximize it, cuz it's gonna be right there anyway.|Давайте просто максимизируем его, потому что он все равно будет здесь.
Not to waste time.|Не терять время зря.
Enable config t, hostname R2, interface F0/0,|Включите config t, имя хоста R2, интерфейс F0 / 0,
IP address 192.168.1.2,|IP-адрес 192.168.1.2,
255 255 255.0.|255 255 255,0.
Now shut DO WR.|Теперь закройте DO WR.
Done deal.|Сделка сделана.
Very simple.|Очень просто.
All we're doing is putting an IP address on the fast ethernet at zero zero.|Все, что мы делаем, это помещаем IP-адрес в Fast Ethernet на ноль.
Nothing major.|Ничего особенного.
All right.|Отлично.
Config t.|Конфиг t.
We'll put in the host name, hostname R3.|Мы введем имя хоста, имя хоста R3.
And then, interface, f0/0.|А затем интерфейс, f0 / 0.
IP address 192.168.1.3,|IP-адрес 192.168.1.3,
255.255.255.0.|255.255.255.0.
The purposes again, understanding what it is that we're doing, rather than just do a whole bunch of configurations,|И снова цели, понимание того, что мы делаем, а не просто целая куча конфигураций,
that things don't make sense.|что все не имеет смысла.
Now I did there, I did I fat fingered the key board so I tried to resolve using DNS,|Теперь я сделал это, я потрогал клавиатуру, поэтому я попытался разрешить с помощью DNS,
but since it's gonna have DNS configures,|но поскольку он будет иметь настройки DNS,
I did a CTRL+SHFT+6 and it went ahead and broke it and then did the correct command which is DO WR.|Я сделал CTRL + SHFT + 6, и он пошел дальше и сломал его, а затем выполнил правильную команду, которая называется DO WR.
[BLANK_AUDIO]|[BLANK_AUDIO]
And that was router three, so let's go to router four, which is our last router.|И это был третий маршрутизатор, так что давайте перейдем к четвертому маршрутизатору, который является нашим последним маршрутизатором.
[BLANK_AUDIO]|[BLANK_AUDIO]
And say no, enable config t.|И скажи нет, включи конфиг t.
Hostname R4 interface F0/0 IP address 192.168.1.4 255,|Имя хоста Интерфейс R4 F0 / 0 IP-адрес 192.168.1.4 255,
255, 255.0 enter and then no shut all right DO WR.|255, 255.0 введите, а затем не закрывайте все в порядке DO WR.
So we put the IP addresses, on these interfaces.|Итак, мы помещаем IP-адреса в эти интерфейсы.
Just as a side note, because see later on we will be you know after the routing we will be doing the switching.|Просто в качестве примечания, потому что позже мы узнаем, что после маршрутизации мы будем выполнять переключение.
Pay attention to these amber lights,|Обратите внимание на эти янтарные огни,
remember that's STP that's working on there, that's the reason those amber lights are there.|помните, что там работает STP, вот почему там янтарные огни.
So it takes time before it turns green turns reporting to for you.|Так что нужно время, прежде чем он станет зеленым, и вам нужно будет сообщить.
Give me a heads up on the switching.|Сообщите мне о переключении.
All right, so we'll wait until that turns green, la, la, la, there we go.|Хорошо, так что подождем, пока он не станет зеленым, ла, ла, ла, поехали.
All right, so now we've put in the IP addresses, obviously,|Хорошо, теперь мы ввели IP-адреса, очевидно,
we can probably ping each other.|мы, вероятно, сможем пинговать друг друга.
There's no need for routing protocol, but we are gonna use a routing protocol.|Протокол маршрутизации не нужен, но мы будем использовать протокол маршрутизации.
So now, we're gonna go in the same exact order, and we're gonna advertise that network, we're gonna advertise that 1.0 network.|Итак, теперь мы пойдем в том же точном порядке, и мы будем рекламировать эту сеть, мы собираемся рекламировать эту сеть 1.0.
Work, all right.|Работай, хорошо.
We're not going to do the loop backs yet.|Мы пока не собираемся делать петли.
We're actually gonna do just the 192.168.1.0 network.|На самом деле мы будем использовать только сеть 192.168.1.0.
Let's bring back router one.|Вернем маршрутизатор один.
All right, and let's maximize it, like we did the rest.|Хорошо, давайте увеличим его до максимума, как и все остальное.
And I can just exit from where I'm at.|И я могу просто уйти с того места, где нахожусь.
I'm gonna do router, OSPF 1|Я сделаю роутер, OSPF 1
network 192.168.1.0.|сеть 192.168.1.0.
It's a 24 mask therefore 255 walkover mask and we're gonna use area zero.|Это маска 24, поэтому маска перехода 255, и мы будем использовать нулевую область.
Right?|Правильно?
So nobody freaks out, that I'm using a completely different area.|Так что никого не волнует, что я использую совершенно другую область.
All right?|Отлично?
In practice, you can use whatever area you cho,|На практике вы можете использовать любую область, которую захотите,
choose, in a real world scenario meaning when you go out there and work.|выбирайте, в реальном мире, то есть когда вы выходите на работу.
Your first area must be zero.|Ваша первая область должна быть нулевой.
Remember your area zero is your backbone.|Помните, что нулевая зона - это ваша опора.
So just putting area zero there just, just stay along the lines of the certification.|Так что просто поставьте нулевую зону, просто оставайтесь в соответствии с требованиями сертификации.
But when you're doing practicing, you can put whatever area you please,|Но когда вы занимаетесь практикой, вы можете поместить любую область, которая вам нравится,
as long as they're all the same, as far as for single area OSPF.|пока они все одинаковы, что касается OSPF с одной областью.
All right.|Отлично.
So we're going to go router.|Итак, мы собираемся перейти на маршрутизатор.
OSPF 1 network 192.168.1.0|OSPF 1 сеть 192.168.1.0
0000255 area zero.|0000255 нулевая область.
DO WR and then that one gets done,|DO WR, и тогда это будет сделано,
let's go to the next one, which is router three,|перейдем к следующему, это третий маршрутизатор,
lets maximize that, we're gonna exit once.|давайте максимизировать это, мы выйдем один раз.
Router OSPF 1,|Маршрутизатор OSPF 1,
network 192.168.1|сеть 192.168.1
0.0.0.255, area 0.|0.0.0.255, область 0.
DO WR.|DO WR.
And then, whoops, oh, there you go, full loading done.|А потом, ох, вот и все, полная загрузка завершена.
I, did I ever tell you the correct network here?|Я, я когда-нибудь говорил вам здесь правильную сеть?
Yeah, yeah, I did, I did, I did, I did,|Да, да, я сделал, я сделал, я сделал, я сделал,
1.0, okay.|1.0, хорошо.
I was wondering why it took a while for it to say full loading done.|Мне было интересно, почему потребовалось время, чтобы он сказал, что полная загрузка завершена.
Oh, that is hefty protocol.|О, это здоровенный протокол.
All right, exit, [COUGH] router, OSPF 1.|Хорошо, выход, [КАШЕ] маршрутизатор, OSPF 1.
Network 192.68.1.0.000,255,00.|Сеть 192.68.1.0.000,255,00.
DO WR.|DO WR.
We, we do a Ctrl+Z.|Мы делаем Ctrl + Z.
Obviously, if we look at the routing table, we're not gonna see any Os, or anything like that, because we're directly connected.|Очевидно, что если мы посмотрим на таблицу маршрутизации, мы не увидим никаких ОС или чего-то подобного, потому что мы подключены напрямую.
We can see, we still say, it says full loading done, so OSPF is doing its thing.|Мы видим, мы по-прежнему говорим, что полная загрузка завершена, поэтому OSPF делает свое дело.
So what we wanna look at.F Now, I said that the highest IP address.|Итак, на что мы хотим взглянуть. F Теперь я сказал, что это самый старший IP-адрес.
The highest IP address is 1.4, is the fourth router.|Наивысший IP-адрес - 1,4, это четвертый маршрутизатор.
And the second highest is router number three, which is 1.3.|Вторым по величине является маршрутизатор номер три, то есть 1,3.
So, let's take a look at show IP OSPF interface F0/0.|Итак, давайте посмотрим на интерфейс IP OSPF F0 / 0.
And as we've seen in the previous labs,|И, как мы видели в предыдущих лабораторных работах,
when it's ethernet,|когда это Ethernet,
here we see the network type, broadcast,|здесь мы видим тип сети, широковещательную,
we have a priority of one.|у нас приоритет один.
All right?|Отлично?
But look how funny.|Но посмотрите, как смешно.
We're using the lowest IP address as the designated router,|Мы используем наименьший IP-адрес в качестве назначенного маршрутизатора,
and the second lowest as the backup designated router.|и второй самый низкий как резервный назначенный маршрутизатор.
And why is that?|И почему так?
The reason that is, because when you,|Причина в том, что когда ты,
in the order that we did it in when that first router came up, it said hey,|в том порядке, в котором мы это делали, когда появился тот первый маршрутизатор, он сказал: "Эй,
I'm the only OSPF process that's running in this infrastructure, so I'm the man.|Я единственный процесс OSPF, работающий в этой инфраструктуре, так что я мужчина.
And then the other router comes up, says well, I'm not the only one, he's the one.|А потом подходит другой роутер, говорит: ну, не я один, он один.
So he's gonna be the designated router,|Итак, он будет назначенным маршрутизатором,
I'll be the backup designated router.|Я буду резервным назначенным маршрутизатором.
And then the others are just what they call druthers.|А остальные просто те, кого они называют друтерами.
And how do we look at that?|И как мы на это смотрим?
Well if you look at show IP OSPF, there are several things you can look at.|Если вы посмотрите на show IP OSPF, вы увидите несколько вещей.
Border routers, database, interface, or neighbors.|Граничные маршрутизаторы, база данных, интерфейс или соседи.
All right.|Отлично.
Take a look at your neighbors.|Взгляните на своих соседей.
And these are your states that we talked about when you become relatio,n when your,|И это ваши состояния, о которых мы говорили, когда вы становитесь отношениями, когда вы,
trying to become neighbors with each other.|пытаясь стать соседями друг с другом.
1.2 is the backup designator router.|1.2 - резервный маршрутизатор с обозначением.
1.1 is a designator router.|1.1 - это маршрутизатор с обозначением.
And he has, done, a full relationship with all the routers.|И у него, по сути, полноценные отношения со всеми маршрутизаторами.
Full relationship with our routers, but look at 1.3.|Полное родство с нашими роутерами, но посмотрите на 1.3.
It stopped.|Это остановилось.
It stopped at the two way.|Он остановился у двух сторон.
And that's what I mean.|Вот что я имею в виду.
You need to understand what that means.|Вам нужно понять, что это значит.
That state is,|Это состояние,
it stops exchanging information with that particular router because it said hey,|он прекращает обмен информацией с этим конкретным маршрутизатором, потому что он сказал: "Эй,
we have DRs and BDRs, so I'm gonna make a full relationship with them, but not with you because all the updates from the designated router other or|у нас есть DR и BDR, поэтому я собираюсь установить с ними полные отношения, но не с вами, потому что все обновления с назначенного маршрутизатора другие или
drothers, again, well, like they came up with that name.|drothers, опять же, ну как будто они придумали это имя.
I don't know, they gonna name something else, but whatever.|Я не знаю, они назовут что-нибудь еще, но как угодно.
It is what it is.|Что есть, то есть.
The other routers that are not BDR or DR,|Остальные маршрутизаторы, не относящиеся к BDR или DR,
they're just standard old routers that say hey, I'm not gonna make a,a full relationship with a DR or,|это просто стандартные старые маршрутизаторы, которые говорят: «Эй, я не собираюсь устанавливать отношения с DR или,
I mean, any standard, any old router.|То есть любой стандартный, любой старый роутер.
I wanna make a full relationship with the BDR and the DR,|Я хочу установить полноценные отношения с BDR и DR,
cuz those is where, those routers is where I'm sending my updates to,|Потому что это те маршрутизаторы, на которые я отправляю свои обновления,
so it stopped the neighbor process at two-way.|поэтому он остановил соседний процесс в двустороннем режиме.
And if we were to look and this is from router four.|И если бы мы посмотрели, а это от четвертого роутера.
When we go to router three, we will see the same thing.|Когда мы перейдем к третьему маршрутизатору, мы увидим то же самое.
We will see the same thing.|Мы увидим то же самое.
We'll go to router three, Ctrl, Ctrl+C.|Мы перейдем к третьему маршрутизатору, Ctrl, Ctrl + C.
No?|Нет?
Maybe so.|Может быть, так.
Okay, show IP.|Ладно, покажи IP.
[BLANK_AUDIO]|[BLANK_AUDIO]
OSPF, interface at 0/0.|OSPF, интерфейс 0/0.
Again, we see that the designator router is 1.1 and then back up, is 1.2.|Снова мы видим, что маршрутизатор с указателем 1.1, а затем резервный - 1.2.
Broadcast, priority of one, one.|Трансляция, приоритет один, один.
Therefore, there is an election and don't forget, don't forget these bad boys right here.|Поэтому есть выборы и не забывайте, не забывайте этих плохих парней прямо здесь.
They, if they're different on your neighbor routers,|Они, если они разные на соседних маршрутизаторах,
you will not create relationship either.|вы тоже не создадите отношений.
That's the criteria, remember?|Это критерии, помните?
Same autonomous system, same subnet mask,|Та же автономная система, та же маска подсети,
security if configured,|безопасность, если настроена,
and authentication, and and the hellos and deads must be the same,|и аутентификация, и hellos и deads должны быть одинаковыми,
must be the same in order for that neighbor relationship to be created.|должен быть таким же, чтобы можно было создать отношения соседа.
So I'm going to do a show IP OSPF neighbor.|Итак, я собираюсь сделать шоу IP соседа OSPF.
And you see that with 1.4|И вы видите, что с 1.4
we did not create a full relationship, we created a two way relationship.|мы не создали полноценные отношения, мы создали двусторонние отношения.
We stopped at that point.|На этом мы остановились.
We stopped in the relationship process.|Мы остановились в процессе отношений.
We did not continue but we did create one with a BDR and a DR if you let, let's go to the DR and take a look at that.|Мы не продолжили, но мы создали один с BDR и DR, если позволите, давайте перейдем к DR и посмотрим на это.
[BLANK_AUDIO]|[BLANK_AUDIO]
So its important to understand that.|Так что это важно понимать.
[BLANK_AUDIO]|[BLANK_AUDIO]
Show IP OSPF, enter let's just look at the neighbor.|Покажи IP OSPF, войди давай просто посмотрим на соседа.
Closer to it, you can see that the DR has full relationships with everybody.|Ближе к этому вы можете видеть, что DR имеет полные отношения со всеми.
It has a full relationship with the BDR and with the other routers.|Он полностью связан с BDR и другими маршрутизаторами.
He, because everybody's updating him.|Он, потому что все его обновляют.
Let's take a look at the BDR now, which is this guy up here.|Давайте теперь посмотрим на BDR, это тот парень здесь.
See what he has.|Посмотри, что у него есть.
Show IP OSPF, neighbor same thing.|Покажи IP OSPF, сосед тоже самое.
Because they're the ones that need to have that full relationship.|Потому что именно им нужны полноценные отношения.
Because everybody's updating them.|Потому что все их обновляют.
And the DRs are updating everybody else.|А DR обновляют всех остальных.
All right, the VDRs erring case, the VR goes down, he takes over.|Хорошо, дело об ошибке VDR, VR выходит из строя, он берет верх.
But again the other routers do not need.|Но опять же другие роутеры не нужны.
So yeah, 50 routers, remember we gave that number.|Так что да, 50 маршрутизаторов, помните, мы дали это число.
You know, that magical number 50 per area.|Вы знаете, это магическое число 50 на область.
You don't want all those drouters, right?|Тебе же не нужны все эти дроутеры, верно?
Or designated router others updating to each other.|Или назначенный маршрутизатор другим обновляющимся друг к другу.
So they, you know how, however or how many DRs, well no.|Так что они, сами знаете, как, однако и сколько ДР, ну нет.
It can only be one DR and one BDR.|Это может быть только один DR и один BDR.
Per segment,|На сегмент,
per broadcast of the domain, one BDR and one DR.|на широковещательную рассылку домена - один BDR и один DR.
Let's say you have only one or you have two, so you have one DR over here,|Допустим, у вас есть только один или у вас два, поэтому у вас есть один DR,
one BDR, what would be an example of two?|один BDR, что было бы примером из двух?
Imagine that we're in the same area.|Представьте, что мы находимся в одном районе.
But in between, here there's a serial,|Но между ними есть сериал,
okay, point to point, serial connection,|хорошо, точка-точка, последовательное соединение,
and over here we have another star.|а здесь у нас есть еще одна звезда.
We have another one of these over here.|У нас есть еще один из них.
But, in between, we have a serial connection.|Но между ними у нас есть последовательное соединение.
Therefore, you have one multi-access network here one multiaxis network there.|Следовательно, у вас есть одна сеть с множественным доступом здесь, одна многоосная сеть там.
You will have one DR and one BDR per multiaxis network.|У вас будет один DR и один BDR на многоосевую сеть.
Sounds like a question to me.|Звучит как вопрос для меня.
Sounds like a question.|Похоже на вопрос.
All right, so be aware of that.|Хорошо, знай об этом.
We see that it really is not doing what it's supposed to do.|Мы видим, что он действительно не делает то, что должен.
What it's supposed to do is say hey, this should be the DR, and this should be the BDR.|Он должен сказать: «Эй, это должен быть DR, а это должен быть BDR».
So let's do that clear IP or OSPF,|Итак, давайте сделаем этот чистый IP или OSPF,
OSPF process, so I'm gonna come to router number one.|OSPF, так что я перейду к маршрутизатору номер один.
And I'm going to clear IP OSPF process,|И я собираюсь очистить процесс IP OSPF,
hit enter.|нажмите Enter.
And I'm gonna say yes, Y, yes.|И я скажу да, да, да.
Okay.|Ладно.
I gotta type in yes and it's gotta be exactly there.|Я должен ввести "да", и он должен быть именно там.
Boom.|Бум.
Done.|Готово.
Right?|Правильно?
And I'm gonna do it to the this guy right here I don't see if it clear IP OSPF OSPF process.|И я сделаю это с этим парнем прямо здесь, я не понимаю, ясно ли, что IP OSPF OSPF процесс.
Yes, all right, so let's see if that's good enough.|Да, хорошо, так что посмотрим, достаточно ли этого.
Let's wait for it to do everything it needs to do,|Подождем, пока он сделает все, что нужно,
all right, while the full loading had stopped, okay.|ладно, пока прекратилась полная загрузка, ладно.
And we see the four, the one, the three Towards itself, okay.|И мы видим четверку, одну, тройку В сторону самого себя, хорошо.
So let's take a look from router one, that was the original DR.|Итак, давайте посмотрим на первый маршрутизатор, это был оригинальный DR.
And Ctrl+Z here.|И Ctrl + Z здесь.
If it lets me.|Если это позволит мне.
Okay?|Ладно?
And I'm going to type in show IP OSPF.|И я собираюсь ввести показать IP OSPF.
No, I gotta type it here show IP OSPF interface f0/0,|Нет, я должен ввести его здесь, чтобы показать интерфейс IP OSPF f0 / 0,
show IP OSPF interface f0/0.|показать интерфейс IP OSPF f0 / 0.
All right, now what do we see?|Хорошо, теперь что мы видим?
Now we see that our designator router is 1.4 and our backup designator router is 1.3.|Теперь мы видим, что наш маршрутизатор с указателем - 1,4, а резервный маршрутизатор с указателем - 1,3.
Packet tracer wants to work with us today.|Packet Tracer хочет работать с нами сегодня.
Outstanding.|Выдающийся.
So now it chose the right ones.|Итак, теперь он выбрал правильные.
Now let's see, cuz this had full all the way down.|Теперь давайте посмотрим, потому что это было полностью заполнено.
Right?|Правильно?
The, the state was full.|Состояние было полным.
Lets take a look at actual IP OSPF neighbor command.|Давайте посмотрим на настоящую команду IP-соседа OSPF.
And now what do we see?|А теперь что мы видим?
Now 1.3 and 1.4.|Сейчас 1.3 и 1.4.
We have a full relationship with those routers.|У нас есть полноценные отношения с этими роутерами.
Because those are the designator and backup designator routers.|Потому что это маршрутизаторы с указателем и резервным указателем.
Where router two, we have a two way.|Где роутер два, у нас два пути.
We have a two way.|У нас есть два пути.
So see how the election process works sometimes?|Так посмотрите, как иногда работает избирательный процесс?
Because if it's, you know, and you can say, well, Laz,|Потому что, если это, вы знаете, и вы можете сказать, что ж, Лаз,
my God, if I'm creating a network, and I'm going across the entire globe, and,|Боже мой, если я создаю сеть и прохожу через весь земной шар, и,
well, this is a process that it takes.|ну, это процесс, который требуется.
That's why Cisco says sometimes it's better to hard code the router ID within the process I, within the OSPF process, let me show you what that means.|Вот почему Cisco говорит, что иногда лучше жестко закодировать идентификатор маршрутизатора в процессе. Я, в рамках процесса OSPF, позвольте мне показать вам, что это значит.
Router and we did router OSPF 1, so we're in router OSPF 1.|Маршрутизатор и мы сделали маршрутизатор OSPF 1, поэтому мы находимся в маршрутизаторе OSPF 1.
And if you type a question mark there is a command right down there, router-id.|И если вы наберете вопросительный знак, прямо там будет команда router-id.
So if you put the router ID, yourself,|Итак, если вы сами укажете идентификатор маршрутизатора,
in a IP version four format, then that's it, you won't have to worry about that.|в формате IP версии 4, вот и все, вам не о чем беспокоиться.
You don't have to worry about that particular election because you're fixing the election.|Вам не нужно беспокоиться об этих выборах, потому что вы проводите выборы.
You're fixing the election, or use priority numbers.|Вы фиксируете выборы или используете номера приоритета.
But I want you to understand that this is what really happens,|Но я хочу, чтобы вы поняли, что это действительно так,
is you let it up to OSPF to, hey, let's run an election and see what happens.|Вы позволите OSPF, эй, давайте проведем выборы и посмотрим, что произойдет.
So, as routers come up with their routing protocols, goes, you can't be like,|Итак, поскольку маршрутизаторы придумывают свои протоколы маршрутизации, вы не можете быть такими, как
all right guys, everybody together, on a conference call across the world.|хорошо, ребята, все вместе, на конференц-связи по всему миру.
All right, we're going to start typing now, okay?|Хорошо, сейчас мы начнем печатать, хорошо?
And then we got, we gotta be in sequence.|А потом мы получили, мы должны действовать последовательно.
So we can all try and come up together, so we can get the right.|Так что мы все можем попытаться прийти вместе, чтобы получить право.
It's not gonna happen.|Этого не случится.
So, everybody has a particular router ID.|Итак, у каждого есть определенный идентификатор маршрутизатора.
Everybody will have a maybe a priority number and that's why you have multiple areas.|У каждого, возможно, будет свой приоритетный номер, поэтому у вас несколько областей.
Everybody is in charge of that particular area, really well, okay?|Каждый отвечает за эту конкретную область, ну ладно?
But you're taking a sort of vacation.|Но у вас что-то вроде отпуска.
Single area, you're gonna go beyond three routers.|Единая зона, вы выйдете за пределы трех маршрутизаторов.
All you be, need to be concerned with,|Все, что вам нужно, нужно беспокоиться,
hey, the highest IP address, right?|эй, самый старший IP-адрес, верно?
The highest IP address, on any physical interface,|Самый высокий IP-адрес на любом физическом интерфейсе,
will be the DR and the second highest,|будет DR и вторым по величине,
will be the BDR.|будет BDR.
Unless, and what we're about to do, I create loopback addresses.|Если, и что мы собираемся делать, я создаю адреса обратной связи.
Then, if I create loopback addresses, it will use the highest loopback address as the DR, and the second highest as the BDR.|Затем, если я создам адреса обратной связи, он будет использовать наивысший адрес обратной связи в качестве DR, а второй по величине в качестве BDR.
And the reason why, they're virtual, they never go down,|И причина, по которой они виртуальные, они никогда не опускаются,
and that's one of the reasons that they like to use it.|и это одна из причин, по которой им нравится его использовать.
So let's go ahead and configure that now.|Итак, давайте продолжим и настроим это сейчас.
So we're in router one, which is great.|Итак, мы находимся в первом маршрутизаторе, и это здорово.
Let's exit.|Выходим.
Let's go and this is LO1, if I'm not mistaken.|Поехали, а это LO1, если не ошибаюсь.
Let's make sure that we have the naming convention down right.|Давайте удостоверимся, что у нас есть правильное соглашение об именах.
LO1, LO2, LO3, LO4.|LO1, LO2, LO3, LO4.
Pretty simple to follow.|Довольно просто следовать.
All right, and we're using a 32-bit mask.|Хорошо, мы используем 32-битную маску.
All right so we're gonna go interface LO1.|Хорошо, мы перейдем к интерфейсу LO1.
All right you don't need to go no shut, it turns on by itself.|Ладно, не закрывайся, он включается сам по себе.
IP address 1.111,|IP-адрес 1.111,
okay no block 1.1.1.1 255,|хорошо нет блока 1.1.1.1 255,
255, 255, 255 enter.|255, 255, 255 введите.
But we need to advertise that within OSPF so we go router OSPF one which is the process and then we go network 1.1.1.1 0.0.0.0, area|Но нам нужно объявить об этом внутри OSPF, поэтому мы переходим к маршрутизатору OSPF, который является процессом, а затем переходим к сети 1.1.1.1 0.0.0.0, области
zero.|нуль.
Remember, your wildcard masking, constant number on top, all 255s,|Помните, ваша подстановочная маска, постоянный номер сверху, все 255,
[INAUDIBLE] 255s as the mask, therefore they're all zeros.|[НЕДОСТАТОЧНО] 255 в качестве маски, поэтому все они нули.
Remember your wildcard masking now, very simple, okay?|Вспомните теперь маску подстановки, очень просто, хорошо?
Let's go to router 2.|Переходим к роутеру 2.
You do the same thing, but with a different loop back address.|Вы делаете то же самое, но с другим адресом обратной связи.
Okay?|Ладно?
Config t, interface, L02.|Конфиг t, интерфейс, L02.
IP address 2.2.2.2 255.255,|IP-адрес 2.2.2.2 255.255,
oops, 55.255.255.|упс, 55.255.255.
Better.|Лучше.
We're gonna exit once, router OSPF 1.|Мы собираемся выйти один раз, маршрутизатор OSPF 1.
Doesn't matter.|Неважно.
Process ID number.|Идентификационный номер процесса.
Network.|Сеть.
2.2.2.2, 0.0.0.0 area zero.|2.2.2.2, 0.0.0.0 нулевая зона.
Better.|Лучше.
DWR.|DWR.
We go to router three, same exact thing.|Идем к третьему роутеру, точно так же.
It's becoming kind of like whatever right?|Это похоже на все, правда?
Config t, interface,|Конфигурация, интерфейс,
LO 3 IP address, 3.3.3.3,|LO 3 IP-адрес, 3.3.3.3,
255.255.255.255.|255.255.255.255.
Enter.|Войти.
Exit once.|Выйти один раз.
Router OSPF1.|Маршрутизатор OSPF1.
Network 3, whoops, 3.3.3.3.|Сеть 3, упс, 3.3.3.3.
0.000, area 0, BWR.|0,000, площадь 0, BWR.
And remember, BWR, we do it here, but when you go take your certification,|И помните, BWR, мы делаем это здесь, но когда вы идете брать сертификат,
we have to exit back to purge mode and do a copy run start enter enter.|мы должны вернуться в режим очистки и выполнить копирование, запустить запуск, введите ввод.
Now remember, remember that, when you go take your examination okay?|Теперь помните, запомните это, когда вы пойдете сдавать экзамен, хорошо?
So you don't come back and say Laz, but you didn't BWR and we tried it and it didn't work.|Итак, вы не вернетесь и не скажете Laz, но вы не использовали BWR, и мы попробовали это, и это не сработало.
I think I've said this a million times through out the day, all right,|Думаю, я говорил это миллион раз в течение дня, хорошо,
throughout the course.|на протяжении всего курса.
All right, so lets do the last router int lo4.|Хорошо, давайте сделаем последний маршрутизатор int lo4.
IP address, oop one to many s's.|IP-адрес, от одного до многих.
4.4.4.4, 255, 255,|4.4.4.4, 255, 255,
255, 255, exit once.|255, 255, выход один раз.
Router OSPF 1, network 4.4.4.4,|Маршрутизатор OSPF 1, сеть 4.4.4.4,
0.0.0.0.|0.0.0.0.
Area 0.|Площадь 0.
BWR.|BWR.
Ctrl+Z.|Ctrl + Z.
And I haven't seen any full loading [INAUDIBLE].|И я не видел полной загрузки [НЕРАЗБОРЧИВО].
Have you?|А ты?
Show IP route.|Показать IP-маршрут.
We do have, you see I'm getting o's.|У нас есть, понимаете, у меня нет.
From the one, I'm getting o's from the two, I'm getting o's from the three.|От одного я получаю отрицательные результаты от двух, мне не нравится от трех.
Okay, so we should be able to ping.|Хорошо, значит, мы сможем пинговать.
Let's test for connectivity.|Давайте проверим возможность подключения.
Right?|Правильно?
So, we should be able to ping 3.3.3.3.|Итак, мы должны иметь возможность пинговать 3.3.3.3.
Awesome.|Потрясающие.
1.1.1.1.|1.1.1.1.
Awesome.|Потрясающие.
And then, 2.2.2.2.|А затем 2.2.2.2.
[BLANK_AUDIO]|[BLANK_AUDIO]
So, we are getting across to all the loopbacks.|Итак, мы переходим ко всем петлям.
Let's see who the designated router is now.|Посмотрим, кто теперь назначенный маршрутизатор.
Show IP, ospf, interface, f0/0.|Показать IP, ospf, интерфейс, f0 / 0.
[SOUND] It is still using the IP address on the physical interface.|[ЗВУК] Он по-прежнему использует IP-адрес на физическом интерфейсе.
That is not what we want.|Это не то, что мы хотим.
We want it to be the loop back address.|Мы хотим, чтобы это был обратный адрес.
So, lets do the same process as we did before.|Итак, давайте проделаем тот же процесс, что и раньше.
This is my DR.|Это мой ДР.
So, I'm gonna go clear.|Итак, я пойду прочь.
Ip ospf process.|Процесс ip ospf.
Let's tab that.|Давайте это сделаем.
Enter.|Войти.
Yes.|Да.
Okay.|Ладно.
And then we go to the BDR.|А потом переходим к БДР.
And lets clear that process their.|И давайте проясним, что обрабатывают их.
Hopefully it'll work, like it did before,|Надеюсь, это сработает, как и раньше,
nice and easy.|легко и приятно.
We don't have to get all crazy.|Нам не нужно сходить с ума.
All right, clear ip ospf process.|Хорошо, очистите процесс ip ospf.
Yes.|Да.
All right,|Отлично,
and we already see, it says, detach,|и мы уже видим, он говорит, отсоединяется,
detach, detach.|отсоединить, отсоединить.
Now, we're loading them with four.|Теперь мы загружаем их четырьмя.
Loading them with one.|Загружаю их одним.
We gotta see all the we gotta wait,|Мы должны увидеть все, что нам нужно подождать,
til everything starts populating, all right?|пока все не начнет заполняться, хорошо?
Should be, I'm just no patience.|Должно быть, у меня просто нет терпения.
I'm the guy that's always pressing the button on the elevator, I wanna go down.|Я тот парень, который всегда нажимает кнопку на лифте, я хочу спуститься.
I wanna go down.|Я хочу спуститься.
I wanna go down.|Я хочу спуститься.
So, let's do short IP route, let's take a look at the routing table.|Итак, давайте сделаем короткий IP-маршрут, посмотрим на таблицу маршрутизации.
See, it takes time, I only see the two,|Видишь, это требует времени, я вижу только двоих,
I'm only getting updates from the two now.|Я получаю только обновления от двух сейчас.
All right, so it's gonna take a little bit for it to learn everybody.|Хорошо, потребуется немного времени, чтобы узнать всех.
[BLANK_AUDIO]|[BLANK_AUDIO]
Just the way it is.|Просто так оно и есть.
Let's see what we see here.|Посмотрим, что мы здесь видим.
Yeah, same thing.|Да, тоже самое.
It's taking its time.|На это нужно время.
That is OSPF.|Это OSPF.
Trying to figure out.|Пытаться понять.
Now we're gonna see anything.|Теперь мы все увидим.
All right, so what I wanna do is, I wanna go in here because I really don't wanna wait, and definitely,|Хорошо, поэтому я хочу пойти сюда, потому что я действительно не хочу ждать, и определенно,
this is something,|это что-то,
you know, that you don't wanna do, is reload.|вы знаете, что вы не хотите делать, это перезагрузка.
[BLANK_AUDIO]|[BLANK_AUDIO]
All right, because once you reload a switch,|Хорошо, потому что как только вы перезагрузите переключатель,
it brings anything that's connected to it,|он приносит все, что с ним связано,
it brings it down.|это сбивает его.
So, now we gotta wait till everything,|Итак, теперь нам нужно дождаться всего,
everything just went down.|все просто рухнуло.
Your whole [UNKNOWN] [SOUND] went down,|Весь ваш [НЕИЗВЕСТНЫЙ] [ЗВУК] отключился,
and it's coming back up.|и он возвращается.
So, we just need to wait cuz now spanning tree's got to do its thing, and it's gonna look to see if this is a designator for|Итак, нам просто нужно подождать, потому что теперь связующее дерево должно сделать свое дело, и оно будет проверять, является ли это указателем для
import and all sorts of craziness.|импорт и всякое безумие.
All right, and then until that comes up,|Хорошо, а потом, пока это не произойдет,
then the routers can send their information through OSPF, so OSPF can do its calculations, well, so they can become neighbors, so|тогда маршрутизаторы могут отправлять свою информацию через OSPF, чтобы OSPF мог выполнять свои вычисления, ну, чтобы они могли стать соседями, поэтому
then they can do their calculations, and now all the updates get sent.|затем они могут произвести свои вычисления, и теперь все обновления будут отправлены.
So, clearing, the clear IP OSPF process,|Итак, очистка, чистый процесс IP OSPF,
definitely will be the best way to go,|определенно будет лучшим способом пойти,
but if, if it's acting up, especially the packet tracer, that's what I do.|но если, если он действует, особенно трассировщик пакетов, я так и делаю.
And if this doesn't kick-start it, then understand the concept, and we move on.|И если это не дает толку, тогда поймите концепцию, и мы двинемся дальше.
And we move on.|И мы идем дальше.
So, let me pick this router one over here.|Итак, позвольте мне выбрать вот этот роутер.
I think, I think we've got it now.|Я думаю, я думаю, что теперь у нас это есть.
You've just gotta be a little bit forceful!|Просто нужно быть немного настойчивым!
Slap it around a little bit.|Похлопайте его немного.
Show IP route.|Показать IP-маршрут.
Oh, you see, nice slapping me around.|Понимаешь, приятно шлепать меня.
All right.|Отлично.
Show ip route.|Показать IP-маршрут.
[SOUND] [LAUGH] Spoke too soon.|[ЗВУК] [СМЕХ] Слишком рано заговорил.
All right.|Отлично.
So, it's still loading now, what are you doing?|Итак, он все еще загружается, что вы делаете?
Show ip route, there it is, there is the four.|Покажи ip route, вот он, есть четверка.
Come on now, so while we have this time to wait,|Давай, пока у нас есть время подождать,
before OSPF decides to get all its networks back up and running, when, let's talk about the CCNA certification, if you will.|прежде, чем OSPF решит восстановить и запустить все свои сети, когда, если хотите, поговорим о сертификации CCNA.
Now, I've been asked a question that there is apparently a new CCNA I have never heard haven't heard yet, of a newer CCNA|Теперь мне задали вопрос, что, по-видимому, есть новый CCNA, о котором я никогда не слышал, но еще не слышал, о более новом CCNA.
version.|версия.
The 200-120 is the one that I know of.|200-120 - это тот, о котором я знаю.
Up to this point, the things that we've covered is the things you need to pay attention to for your certification.|До этого момента мы рассмотрели то, на что вам нужно обратить внимание при сертификации.
Especially here, with OSPF.|Особенно здесь, с OSPF.
Mult same area, same area.|Несколько одинаковых участков, одинаковых участков.
Hellos have to be the same.|Привет, должно быть так же.
And with the election here, the multi-access, okay?|А с выборами здесь и множественным доступом, понятно?
Now this thing doesn't wanna play, what's going on?|Теперь эта штука не хочет играть, что происходит?
[BLANK_AUDIO]|[BLANK_AUDIO]
Come on, come on, come on, come on, come on.|Давай, давай, давай, давай, давай.
Loopback.|Петля.
[BLANK_AUDIO]|[BLANK_AUDIO]
I advertised it, okay.|Я это рекламировала, ладно.
[BLANK_AUDIO]|[BLANK_AUDIO]
Is it really taking that long?|Неужели это так долго?
I should be able to see all the, show ip route.|Я должен видеть все, показать IP-маршрут.
There we go.|Вот и все.
Here's the two network, there's the oh, I mean the one network, I'm sorry.|Вот две сети, вот и одна сеть, извините.
The one network, the three network, and the four network.|Одна сеть, три сети и четыре сети.
So [UNKNOWN] router number two is seeing all the networks.|Итак, [НЕИЗВЕСТНО] маршрутизатор номер два видит все сети.
Lets see router number three, show ip route,|Давайте посмотрим маршрутизатор номер три, покажем IP-маршрут,
[BLANK_AUDIO]|[BLANK_AUDIO]
He's good to go, I see the one I see the two, and I see the four.|Он готов идти, я вижу одного, вижу двоих и вижу четверых.
Okay, okay, okay, lets see the four network only on router four, I'm sorry.|Хорошо, хорошо, хорошо, давайте посмотрим четыре сети только на четвертом маршрутизаторе, извините.
[BLANK_AUDIO]|[BLANK_AUDIO]
Okay, something going on between router four, and router one that, they just, are being who they wanna be.|Хорошо, что-то происходит между четвертым и первым маршрутизаторами, и они просто являются теми, кем хотят быть.
And [SOUND] let's go to router two,|И [ЗВУК] перейдем к маршрутизатору 2,
the Cs, everyone.|Cs, всем.
And let's do a show.|И давайте устроим шоу.
[BLANK_AUDIO]|[BLANK_AUDIO]
Oh, look at all those routers that are open.|О, посмотрите на все те маршрутизаторы, которые открыты.
[BLANK_AUDIO]|[BLANK_AUDIO]
Let's close that, close that, close that,|Давайте закроем это, закроем это, закроем это,
close that, close that,|закрой это, закрой это,
close that, okay, and, router two.|закройте это, хорошо, и маршрутизатор два.
Let's do a show ip ospf interface at f0/0.|Давайте сделаем show ip ospf interface на f0 / 0.
And [INAUDIBLE] there's A, and it's still not using.|И [НЕРАЗБОРЧИВО] есть A, и он все еще не используется.
It's still using designated router 1.2|Он все еще использует назначенный маршрутизатор 1.2
[UNKNOWN] 1.2,|[НЕИЗВЕСТНО] 1.2,
and 1.1, as a designated router and backup designated router, so, it's going a little crazy.|и 1.1, как назначенный маршрутизатор и резервный назначенный маршрутизатор, так что это немного сходит с ума.
All right, so we're not gonna really waste time.|Хорошо, мы не будем тратить время зря.
What should happen, what should happen,|Что должно случиться, что должно произойти,
what should happen, is that this one still should have been your designated router,|что должно произойти, это то, что этот маршрутизатор все еще должен был быть вашим назначенным маршрутизатором,
and this one should have been your backup,|и этот должен был быть твоей резервной копией,
because these are the two highest loopbacks.|потому что это две самые высокие петли.
And if you get questions, asked on your exam.|И если у вас есть вопросы, задаваемые на экзамене.
If you get questions asked on your exam,|Если на экзамене вам задают вопросы,
or you get a print screen, or what have you, and there are loopback addresses,|или у вас есть экран для печати, или что у вас, и есть адреса обратной связи,
the highest loopback addresses, will be chosen over the physical interfaces.|наивысшие адреса обратной связи будут выбраны по физическим интерфейсам.
Right, the IP addresses, on the physical interfaces.|Правильно, IP-адреса на физических интерфейсах.
And it will be the highest loopback addresses that would be the DRs,|И это будут самые высокие адреса обратной связи, которые будут DR,
all right?|отлично?
That's, that's what you need to understand, cuz it is just being silly right now, and I really don't have time, but if I could trace it to say, hey.|Вот что вам нужно понять, потому что сейчас это просто глупо, и у меня действительно нет времени, но если бы я мог проследить это, чтобы сказать, эй.
So, what we're going to do, all right,|Итак, что мы будем делать, хорошо,
we're gonna go to the next step, which is the priority numbers.|мы перейдем к следующему шагу, который является приоритетными числами.
The priority numbers.|Приоритетные числа.
The one with the highest priority number,|Номер с наивысшим приоритетом,
and the range is from zero to 255.|и диапазон от нуля до 255.
Zero, you saw it, if your priority number is zero,|Ноль, вы это видели, если ваш приоритет равен нулю,
you do not take part in any election.|вы не участвуете ни в каких выборах.
You are excluded from the election process.|Вы исключены из избирательного процесса.
All right?|Отлично?
If your are any other number than that, by default,|Если у вас любой другой номер, по умолчанию
all these guys priority numbers right now are one.|все эти парни приоритетные номера сейчас едины.
So, that's why it can not be the tie breaker.|Вот почему это не может быть решающим фактором.
The tie breaker, would be the loop bag addresses.|Прерыватель связи - это адреса петлевых мешков.
So, what we're gonna do is we're gonna configure Router2 as a desi,|Итак, что мы собираемся сделать, так это настроить Router2 как Desi,
as a matter of fact, let's take Router3.|собственно говоря, возьмем Router3.
Let's make Router3 the designator router,|Сделаем Router3 маршрутизатором с обозначением,
and let's make Router2 the backup designate a router,|и давайте сделаем Router2 резервным, обозначим маршрутизатор,
by giving them a higher priority than the ones 1 and 4.|отдавая им больший приоритет, чем 1 и 4.
All right?|Отлично?
And this is now on our, obviously I always go to the extreme so Router3,|И это сейчас у нас, очевидно, я всегда дохожу до крайности, поэтому Router3,
I don't wanna nobody to trump them.|Я не хочу, чтобы их кто-то превзошел.
So, his priority will be to be five.|Значит, его приоритетом будет пятеро.
And the priority for two will be 254,|И приоритет на двоих будет 254,
second highest.|второй по величине.
So let's go ahead and do that, very simple.|Так что давайте продолжим и сделаем это очень просто.
We go into the Interface, Config T,|Заходим в Интерфейс, Конфиг Т,
interface F0/0 IP OSPF priority right, you can see the range, 0 to 255.|интерфейс F0 / 0 IP OSPF Priority right, вы можете видеть диапазон от 0 до 255.
Let me bring that up, so you can see it better.|Позвольте мне поднять этот вопрос, чтобы вам было лучше.
You can see, the range is from 0 to 255|Как видите, диапазон от 0 до 255
for the priority number, and we're gonna choose, I did up arrow, we're gonna do 255 that's for Router3.|для номера приоритета, и мы будем выбирать, я сделал стрелку вверх, мы собираемся сделать 255 для Router3.
There's no advertising or anything like that with an OSPF.|В OSPF нет рекламы или чего-то подобного.
You're changing a priority number on the interface.|Вы меняете номер приоритета в интерфейсе.
You're already advertising, the networks that are on that interface.|Вы уже рекламируете сети, которые находятся на этом интерфейсе.
So, all this information gets sent out in the updates.|Итак, вся эта информация рассылается в обновлениях.
So, that's Router3, Router2 will have 254|Итак, это Router3, у Router2 будет 254
on the Fast E000.|на Fast E000.
So, Config T,|Итак, Config T,
IP OSPF process.|Процесс IP OSPF.
And there we'll make it 254 set.|А там сделаем 254 комплекта.
Oh, whoops.|Ой, ой.
I thought I was already on the interface.|Я думал, что уже на интерфейсе.
F00, IP OSPF, process.|F00, IP OSPF, процесс.
Going too fast for my own good.|Слишком быстро для моего же блага.
Priority is 254, wow, that's, that's not good aging.|Приоритет 254, ничего себе, это не хорошее старение.
The WR.|WR.
Now, for this to take effect, it's not gonna take effect right away, so what I'm gonna do is, I'm gonna restart my switch.|Теперь, чтобы это вступило в силу, это не вступит в силу сразу же, поэтому я собираюсь перезапустить свой коммутатор.
Lobby environment lov, gotta love it.|Люблю среду вестибюля, я должен любить его.
You can clear the process if you like.|Вы можете очистить процесс, если хотите.
In the real world, okay?|В реальном мире, ладно?
Or if you are gonna reboot the switch,|Или, если вы собираетесь перезагрузить коммутатор,
if you get the go ahead with the big wigs you can do it during the day.|Если вы решитесь на большие парики, вы сможете делать это днем.
You take not an email to your higher ups.|Вы не отправляете электронное письмо своему начальству.
Hey man, I need to do this, do you want me to do it?|Эй, чувак, мне нужно это сделать, ты хочешь, чтобы я это сделал?
Yay or nay?|Да или нет?
Yay!|Ура!
Cool, we have our [INAUDIBLE], black and white, you cover your butt.|Круто, у нас есть [НЕРАЗБОРЧИВО], черно-белое, ты прикрываешь задницу.
Or, as we used to say, your fourth port of contact, all right?|Или, как мы обычно говорили, ваш четвертый порт связи, хорошо?
Never just do things, acting on your own,|Никогда не делай ничего, действуя по своему усмотрению,
don't do that,|не делай этого,
especially something like this.|особенно что-то вроде этого.
Reload, usually things are done within minutes,|Перезагрузите, обычно все делается в течение нескольких минут,
but I can tell you from experience in the telecom industry.|но я могу сказать вам это по опыту работы в телекоммуникационной отрасли.
You do not, you do not, emails will save your life.|Вы не делаете, вы не делаете, электронные письма спасут вашу жизнь.
You do not wanna take down the network,|Вы не хотите отключать сеть,
during the day, you don't wanna do that.|днем ты не хочешь этого делать.
If you get permission from the higher ups,|Если вы получите разрешение от высшего руководства,
because once you tell your boss,|потому что как только вы скажете своему боссу,
your boss will tell his boss, and that boss will tell all the people on top,|ваш босс расскажет своему боссу, и этот босс расскажет всем людям наверху,
and how important this is.|и насколько это важно.
Do we really need to do it once they finally say okay go ahead, but we'll do it between this time, and this time send out an email, warn everybody.|Неужели нам действительно нужно это сделать, когда они наконец скажут, что ладно, давай, но мы сделаем это между этим временем и на этот раз отправим электронное письмо, предупредим всех.
Hey, here's what's gonna happen from this time to this time.|Эй, вот что произойдет с этого времени до этого времени.
You're not gonna have any internet, you're gonna not have this or email, whatever for a period that that 20 minutes, 30 minutes.|У вас не будет интернета, у вас не будет этого или электронной почты, что бы то ни было в течение этих 20 минут 30 минут.
So, just bear with it, you know, save all your work or all this other stuff.|Так что просто потерпите, знаете, сохраните всю свою работу или все это.
So, you wanna make sure that if you're gonna do something like this in a real world, that you let everybody know before you do it.|Итак, вы хотите убедиться, что если вы собираетесь сделать что-то подобное в реальном мире, вы должны сообщить всем, прежде чем это сделаете.
Well, more than likely, it was not that crucial at that moment,|Что ж, скорее всего, в тот момент это было не так важно,
because the network is working.|потому что сеть работает.
And you is doing it for, you know,|И вы делаете это, знаете ли,
you want this router to be the DER, the DR, and usually, it fix itself.|вы хотите, чтобы этот маршрутизатор был DER, DR и обычно сам исправлялся.
But, if you wanna manipulate it that way then do normally do another maintenance window or a time where there's nobody there after hours after hours, okay?|Но если вы хотите манипулировать этим таким образом, то обычно делайте еще одно окно обслуживания или время, когда никого нет после нескольких часов работы, хорошо?
So, lets see lets see if my boy over here,|Итак, давайте посмотрим, давайте посмотрим, здесь ли мой мальчик,
show IP OSPF neighbor and look at that.|покажите IP соседа OSPF и посмотрите на него.
1.2 254 is my BDR.|1.2 254 это мой БДР.
And then I got full relationships going all the way across, so that means that if, where am I?|И затем у меня были полноценные отношения, так что это означает, что если, где я?
I'm in Router3, Router2 is my BDR that's makes me the DR.|Я использую Router3, Router2 - это мой BDR, который делает меня DR.
So, we are gonna do show IP or SPF interface at 0/0.|Итак, мы собираемся показать интерфейс IP или SPF в 0/0.
And what do I have pray tell?|И что мне нужно, пожалуйста, скажите?
3.3.3 is my designator router and my backup designator router is 1.2.|3.3.3 - это мой маршрутизатор с указателем, а резервный маршрутизатор с указателем - 1.2.
I can care less about what IP address their using.|Меня не волнует, какой IP-адрес они используют.
Just the fact that Router2 is my BDR and Router3 is the DR, I'm happy with it.|Я доволен тем, что Router2 - это мой BDR, а Router3 - это DR.
Because, remember I'm basing it on priority numbers.|Потому что помните, я основываю это на числах приоритета.
This, you know, it the IP addresses,|Это, как вы знаете, IP-адреса,
whatever.|без разницы.
Doesn't matter.|Неважно.
What matters to me is who the DR?|Для меня важно, кто такой DR?
Again, and I based it off priority numbers.|Опять же, и я основывал это на числах приоритета.
It's working, let's go to the DR and, I mean, the BDR.|Работает, перейдем к DR и, я имею ввиду, BDR.
We'll take a look at that to verify.|Мы посмотрим на это, чтобы проверить.
[BLANK_AUDIO]|[BLANK_AUDIO]
Come on, now.|Давай же.
Show IP OSPF interface F0/0.|Показать интерфейс IP OSPF F0 / 0.
And here, you saw it, designated router is 3.3.3.|И вот, как вы это видели, назначенный маршрутизатор - 3.3.3.
Backup designated router is 192, which is myself, so it is working.|Резервный назначенный роутер 192, это я, так что он рабочий.
It is working.|Это работает.
The priority numbers works just fine.|Номера приоритета работают нормально.
My personal opinion, that's what I would do, I would choose priority numbers.|Мое личное мнение, я бы так поступил, я бы выбрал приоритетные номера.
But, if you're in I guess a large enough network where it goes over 285, and again you can only have one designated router and one backup designated router|Но, если вы находитесь, я предполагаю, что это достаточно большая сеть, где оно превышает 285, и снова у вас может быть только один назначенный маршрутизатор и один резервный назначенный маршрутизатор.
within each multi-access network, so that really doesn't even come into play.|в каждой сети с множественным доступом, так что это даже не играет роли.
But, a lot of people do like hard coding the router ID.|Но многим нравится жесткое кодирование идентификатора маршрутизатора.
That's another option.|Это еще один вариант.
That would be the highest option, all right?|Это был бы самый лучший вариант, хорошо?
What CISCO recommends.|Что рекомендует CISCO.
But again, this is what a multi access network is all about.|Но опять же, это и есть сеть с множественным доступом.
And this is how you're gonna get tested.|И вот как ты собираешься пройти тестирование.
Get very friendly with that particular screen.|Подружитесь с этим конкретным экраном.
And I think I told you this at the beginning when we did the point to point.|Думаю, я сказал вам это в начале, когда мы говорили по пунктам.
All right, let's hit return.|Хорошо, давай вернемся.
Show IP OSPF, interface add zero, so add zero.|Показать IP OSPF, интерфейс добавить ноль, поэтому добавьте ноль.
Get familiar with this screen.|Ознакомьтесь с этим экраном.
Understand the priority number.|Понять номер приоритета.
Understand what drother means, it's a designated router others,|Поймите, что означает drother, это другой маршрутизатор,
not a backup designate router, it's not a designated router.|не резервный назначенный маршрутизатор, это не назначенный маршрутизатор.
Router, okay?|Маршрутизатор, хорошо?
See who your designated router is, and who your backup designated router is, okay?|Посмотрите, кто ваш назначенный маршрутизатор, и кто ваш резервный назначенный маршрутизатор, хорошо?
And the type of broadcast you're in, and obviously your hellos and NEDs.|И тип трансляции, в которой вы участвуете, и, конечно же, ваши приветствия и NED.
This stream, I'm telling you again, get familiarized with it,|Этот поток, повторяю вам, ознакомьтесь с ним,
understand what it's doing, and always remember the comparison that we did.|понимать, что он делает, и всегда помнить то сравнение, которое мы сделали.
You will run an election in ethernet.|Вы будете проводить выборы в сети Ethernet.
You will not run an election, when there's serial cables involved, all right?|Вы не будете проводить выборы, когда задействованы последовательные кабели, понятно?
Testing purposes.|Цели тестирования.
Point-to-point, no election.|Точка-точка, без выборов.
Multi-access, election, okay?|Мультидоступ, выборы, хорошо?
I hope this helps.|Надеюсь, это поможет.
I'll see you in the next session.|Увидимся на следующем сеансе.
[BLANK_AUDIO]|[BLANK_AUDIO]