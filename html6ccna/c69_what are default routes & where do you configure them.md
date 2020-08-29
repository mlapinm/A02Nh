D:\mailCloud\prjother\tmp\1\c69_what are default routes & where do you configure them.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
All right, we're gonna go ahead and talk about.|Хорошо, мы продолжим и поговорим об этом.
Yes we gonna right into the class no welcome back or anything.|Да, мы пойдем прямо в класс, без приветствия или чего-нибудь еще.
Default routes, but you, I mentioned it,|Маршруты по умолчанию, но вы, я уже упоминал,
right?|право?
In the previous lesson.|В предыдущем уроке.
But I wanna give a, we're gonna configure a default route in the packet tracer,|Но я хочу сказать, мы собираемся настроить маршрут по умолчанию в трассировщике пакетов,
and then, yes, in the live router, all right?|а то да, в живом роутере, ладно?
But, I'm gonna tell you what a default route is all about.|Но я расскажу вам, что такое маршрут по умолчанию.
I really want you, when you go take your exam,|Я действительно хочу тебя, когда ты пойдешь на экзамен,
I want you to have all this ammunition in your brain, so you can regurgitate it onto those laminates they give you so you can take your exam.|Я хочу, чтобы у вас в мозгу были все эти боеприпасы, чтобы вы могли извергнуть их на те ламинаты, которые вам дают, чтобы вы могли сдать экзамен.
Okay, we said that static routes, you know,|Хорошо, мы сказали, что статические маршруты, вы знаете,
was where you advertise the networks that you don't know about, right?|где вы рекламируете сети, о которых не знаете, верно?
And it's better on the router and so forth.|А лучше на роутере и тд.
Default routes, default routes are used on end routers, stub routers, okay?|Маршруты по умолчанию, маршруты по умолчанию используются на конечных маршрутизаторах, маршрутизаторах-заглушках, хорошо?
One way into a network and one way out.|Один выход в сеть и один выход.
Right?|Правильно?
It only can go one way in.|Он может войти только в одну сторону.
And there is no two ways.|И нет двух способов.
Like here.|Как здесь.
You can go this way or you can go that way.|Вы можете пойти этим путем или можете пойти тем путем.
Here?|Вот?
You can only go woop or woop.|Вы можете только пойти или пойти.
So stub routers, end routers.|Итак, маршрутизаторы-заглушки, конечные маршрутизаторы.
There's where you configures default routes.|Там вы настраиваете маршруты по умолчанию.
Cause you only give it one direction.|Потому что вы даете ему только одно направление.
What is the purpose of a default route.|Какова цель маршрута по умолчанию.
The purpose.|Цель.
The purpose of a default route is so the router, when it receives a destination network, that it doesn't have an entry for in the routing table.|Назначение маршрута по умолчанию состоит в том, чтобы маршрутизатор, когда он получает сеть назначения, не имел записи в таблице маршрутизации.
It does not drop it.|Не роняет.
Because the thing that the router looks at.|Потому что то, на что смотрит роутер.
The routing process that we talked about.|Процесс маршрутизации, о котором мы говорили.
Once the packet makes it inside the router,|Как только пакет попадает внутрь маршрутизатора,
the router will then look at it's routing table to make a match.|маршрутизатор затем посмотрит на свою таблицу маршрутизации, чтобы найти совпадение.
To see where it needs to switch that particular destination address, or that packet.|Чтобы увидеть, куда нужно переключить этот конкретный адрес назначения или этот пакет.
To whatever interface, outgoing interface it's sending it, where it needs to go.|К какому-либо интерфейсу, исходящему интерфейсу он его отправляет, куда ему нужно идти.
But, if in the routing table there isn't an entry for that particular destination network.|Но, если в таблице маршрутизации нет записи для этой конкретной сети назначения.
Normal circumstances, the router will drop it.|В обычных условиях маршрутизатор его уронит.
So the default route is also known as the gateway of last resort.|Таким образом, маршрут по умолчанию также известен как шлюз последней инстанции.
And what it does is, it will match the, it will match the IP address.|И что он делает, он будет соответствовать, он будет соответствовать IP-адресу.
It will match the the subnet mask and then you send it out either the exit interface or the next routers hop address.|Он будет соответствовать маске подсети, а затем вы отправите его либо выходной интерфейс, либо адрес следующего маршрутизатора.
And I'm going to show it to you first in notepad.|И я сначала покажу вам это в блокноте.
And we'll take our time with this.|И мы не торопимся с этим.
We're not in a hurry.|Мы никуда не торопимся.
All right, now a default route is a special kind of static routes,|Хорошо, теперь маршрут по умолчанию - это особый вид статических маршрутов,
and I believe you can see this.|и я думаю, вы это видите.
Let me, okay, I'll bring this up a little bit bigger,|Позвольте мне, хорошо, я подниму это немного больше,
make it a little bigger, put it right there.|сделай это немного больше, положи прямо здесь.
So, you started like you would a static route, IP route and then you go match destination network,|Итак, вы начали, как статический маршрут, IP-маршрут, а затем вы подходите к сети назначения,
match destination mask, and then you can use this is what's called using the exit interface,|сопоставить маску назначения, а затем вы можете использовать то, что вызывается с помощью интерфейса выхода,
what is the exit interface of the first router is the s00.|каков выходной интерфейс первого роутера - это s00.
So I'm telling it hey match whatever, it's not in the routing table, but just match whatever network and send it out, and send it out to the next router.|Итак, я говорю ему: «Эй, сопоставьте что угодно, это не в таблице маршрутизации, но просто сопоставьте любую сеть, отправьте ее и отправьте на следующий маршрутизатор».
Because it said just switch it to that interface and boop send it to the next router.|Потому что он сказал, просто переключите его на этот интерфейс и отправьте его на следующий маршрутизатор.
Or you can do it IP route 0.0.0.0|Или вы можете сделать это IP route 0.0.0.0
0.0.0.0 oops, or you can do 10.1.1.6 that will be using the next routers hop address we should be that right there what is the difference|0.0.0.0 ой, или вы можете сделать 10.1.1.6, который будет использовать адрес следующего маршрутизатора, мы должны быть там, в чем разница
now this is the same principal for using a default route or a static route.|теперь это тот же принцип для использования маршрута по умолчанию или статического маршрута.
A normal static route, versus this special type of static route.|Обычный статический маршрут по сравнению с этим специальным типом статического маршрута.
Remember these are, this is what you call a default route,|Помните, что это то, что вы называете маршрутом по умолчанию,
which equals your gateway of last resort.|что равносильно вашему шлюзу последней надежды.
Okay?|Ладно?
The difference is this if you use the exit interface, it,|Разница в том, что если вы используете интерфейс выхода, он,
the entry on the routing table for normal static routes, not for the gateway of last resort, but for normal static routes.|запись в таблице маршрутизации для обычных статических маршрутов, но не для шлюза последней инстанции, а для обычных статических маршрутов.
It will show up as it's directly connected.|Он будет отображаться, поскольку он напрямую подключен.
So the router only has to do one lookup.|Таким образом, маршрутизатору нужно выполнить только один поиск.
One lookup.|Один поиск.
Where is it you want to go.|Куда ты хочешь пойти?
Switch it to the interface, done.|Переключите его на интерфейс, готово.
If you use the, next router's hub address,|Если вы используете следующий адрес концентратора маршрутизатора,
then it'll, when you look at the routing table, you do show up your route,|тогда, когда вы посмотрите на таблицу маршрутизации, вы увидите свой маршрут,
you're going to have an administrative distance of one versus that it shows that it's directly connected.|у вас будет административное расстояние, равное единице, а не то, что оно показывает, что оно напрямую связано.
So now the router does two look ups.|Итак, теперь маршрутизатор выполняет два поиска.
Now it goes down, say okay, where you wanna go and where do I need to send you?|Теперь он идет вниз, скажите хорошо, куда вы хотите пойти и куда мне нужно вас отправить?
So, cause it's gotta look for that destination on the next router,|Итак, он должен искать этот пункт назначения на следующем маршрутизаторе,
next router's hop address.|адрес следующего маршрутизатора.
So, for point to point networks, for point to point networks, Cisco recommends exit interfaces, exit interfaces for static routes.|Итак, для сетей точка-точка, для сетей точка-точка Cisco рекомендует интерфейсы выхода, интерфейсы выхода для статических маршрутов.
That way the router does less look ups on the routing table.|Таким образом маршрутизатор будет меньше искать в таблице маршрутизации.
Well, let's configure this.|Что ж, давайте это настроим.
Let's configure this.|Давайте настроим это.
We're gonna first, we're gonna do everything.|Мы будем первыми, мы сделаем все.
On the, on the packet tracer and then we'll go ahead and do it on the live router.|На трассировщике пакетов, а затем мы продолжим и сделаем это на работающем маршрутизаторе.
Okay.|Ладно.
Let's go ahead and go to this router right here, that's the very first router.|Давайте перейдем к этому маршрутизатору прямо здесь, это самый первый маршрутизатор.
And we're gonna go over here so you guys can see it.|И мы пойдем сюда, чтобы вы, ребята, это увидели.
All right, let's open it up a little bit.|Хорошо, давай приоткроем его немного.
[BLANK_AUDIO]|[BLANK_AUDIO]
Let's go to the CLI.|Пойдем в CLI.
Use your name, everything in caps,|Используйте свое имя, все заглавными буквами,
LDIAZCISCO, alright we gotta go in global configuration and I want to show you something before I start so you can see.|LDIAZCISCO, хорошо, нам нужно перейти в глобальную конфигурацию, и я хочу показать вам кое-что, прежде чем я начну, чтобы вы могли видеть.
I want to look at the routing table right now.|Хочу прямо сейчас посмотреть таблицу маршрутизации.
I'm gonna do, which you can't do on your certification,|Я сделаю то, что вы не можете сделать в своей сертификации,
you have to be in privilege mode.|вы должны быть в привилегированном режиме.
So let's go ahead and go let's exit out.|Так что давай, давай выйдем.
Okay, okay, okay.|Хорошо, хорошо, хорошо.
Show IP route.|Показать IP-маршрут.
All right.|Отлично.
And you can see it says that your gateway of last resort is not set.|И вы можете видеть, что он говорит, что ваш шлюз последней инстанции не настроен.
And that you're directly connected to two networks,|И что вы напрямую подключены к двум сетям,
the 10.1.1.4 and the 192.168.1.0.|10.1.1.4 и 192.168.1.0.
All right.|Отлично.
So that's what our writing table looks like now.|Вот так теперь выглядит наш письменный стол.
Okay.|Ладно.
So, now let's go to global configuration.|Итак, теперь перейдем к глобальной настройке.
And let's do our default route.|И давайте сделаем наш маршрут по умолчанию.
IP Route, destination network.|IP-маршрут, сеть назначения.
Destination mask.|Маска назначения.
Exit interface.|Выйти из интерфейса.
[BLANK_AUDIO]|[BLANK_AUDIO]
I'm going to copy.|Я скопирую.
I'll exit.|Я выйду.
I'll do it the right way.|Я сделаю это правильно.
Another right way, the test way.|Другой правильный путь, испытательный путь.
copy run start.|копировать запуск запуска.
[SOUND] Not saying it's wrong, but just lengthy.|[ЗВУК] Не говорю, что это неправильно, но просто долго.
So now when we do a Show IP route.|Итак, теперь, когда мы делаем Показать IP-маршрут.
Now the gateway of last resort is set to all zeroes.|Теперь шлюз последней инстанции установлен на все нули.
And we have a default Static route entry that is directly connected to the 000.|И у нас есть запись статического маршрута по умолчанию, которая напрямую связана с 000.
Okay?|Ладно?
So it's a special type of static route,|Итак, это особый тип статического маршрута,
because if you look up here, let me,|потому что если вы посмотрите сюда, позвольте мне,
here so see, says e the [INAUDIBLE] means candidate default.|вот так видите, говорит е, [НЕРАЗБОРЧИВО] означает вариант по умолчанию.
The S I guess is a little bit higher,|S, я думаю, немного выше,
Maybe I went a little too far down with it.|Возможно, я зашел слишком далеко с этим.
And there you see it has an S, it's a static.|И там вы видите букву S, это статика.
So you have a static default route.|Итак, у вас есть статический маршрут по умолчанию.
That's what that S with the asterisk is telling you.|Это то, что вам говорит буква S со звездочкой.
So nothing gets dropped.|Так что ничего не упадет.
Nothing gets dropped.|Ничего не упадет.
So let's do it, and again, you can only do this on the end router.|Итак, давайте сделаем это, и снова вы можете сделать это только на конечном маршрутизаторе.
So let's go to the last router.|Итак, перейдем к последнему роутеру.
And let's to that.|И давайте к этому.
Let's do the same exact thing.|Сделаем то же самое.
But this time the exit interface will be the S0.0.1, cause we're going that way.|Но на этот раз интерфейсом выхода будет S0.0.1, потому что мы идем по этому пути.
We're going that way.|Мы идем туда.
Where here, we're coming this way.|Где здесь, мы идем сюда.
You see?|Ты видишь?
All right.|Отлично.
So let's move that more that way.|Так что давайте двигаться дальше в том же направлении.
Let's open that up.|Давайте откроем это.
[BLANK_AUDIO]|[BLANK_AUDIO]
All right, and,|Хорошо, и,
oh I didn't put no cis seal.|о, я не ставил цис печать.
Okay, config T, IP route 0.0.0.0.|Хорошо, конфиг T, IP-маршрут 0.0.0.0.
0.0.0.0 destination network match exactly.|0.0.0.0 сеть назначения точно соответствует.
Destination mask, matches exactly.|Маска назначения, точно совпадает.
Whatever number it is just match it match it match it.|Какой бы номер он ни был, просто сопоставьте его, сопоставьте его, сопоставьте ему.
Send it out the S0/0/1.|Отправьте ему S0 / 0/1.
Enter.|Войти.
Yes I'm going to cheat.|Да я обманываю.
Do show IP route, so we're looking at the same thing.|Показывать IP-маршрут, значит, мы смотрим на то же самое.
Cool.|Прохладно.
So now, I am going to oh why fr, why from right here oh let's get the PC.|Итак, теперь я собираюсь рассказать о том, почему, пожалуйста, отсюда, о, давайте возьмем ПК.
Let's get PC two.|Возьмем два ПК.
Let's go to the command prompt, and let's move it over here.|Перейдем в командную строку и переместим ее сюда.
So let's see, I do have my IP address, IP config.|Итак, давайте посмотрим, у меня есть свой IP-адрес, IP-конфигурация.
All right, of course you can't see it.|Хорошо, конечно, вы этого не видите.
I don't have no IP addresses on there?|У меня там нет IP-адресов?
Oh that's right, I added this to the network,|Ах да, я добавил это в сеть,
I guess I didn't put, forgot to put that 192.168.|Вроде не ставил, забыл поставить 192.168.
192.168.|192.168.
3.1 tab tab, 192.168.3.254.|Вкладка 3.1, 192.168.3.254.
So, lets try and ping our gateway first.|Итак, давайте сначала попробуем пинговать наш шлюз.
Make sure that we do have connectivity to the gateway.|Убедитесь, что у нас есть подключение к шлюзу.
192.168.3.254 and we do, awesome, awesome.|192.168.3.254 и мы делаем, здорово, здорово.
So, now we have a default out, no package should be dropped.|Итак, теперь у нас есть значение по умолчанию, ни один пакет не должен быть удален.
Well heck, I should be able to ping then the 192.168.1.1, I just gonna go for the gusco, let's see how far I get.|Ну, черт возьми, я смогу пинговать тогда 192.168.1.1, я просто пойду на гуско, посмотрим, как далеко я продвинусь.
Oh, it's taking long cause of our, that's,|О, это занимает много времени из-за нашей, вот,
that's the reason,|вот в чем причина,
that's the reason, that's the reason,|вот причина, вот причина,
let's see what happens.|Давай посмотрим что происходит.
Request timed out Request timed out.|Превышено время ожидания запроса. Истекло время ожидания запроса.
Why is that happening?|Почему так происходит?
Why is that happening?|Почему так происходит?
Not unreachable mind you.|Имейте в виду, что это не является недостижимым.
It says request timed out.|Он говорит, что истекло время ожидания запроса.
Well, this is what's going on.|Что ж, вот что происходит.
Remember.|Помните.
Oh ok.|Ну ладно.
I thought that, that, I saw that was closed, I was, I was minimizing it.|Я думал, что, я видел, что это закрыто, я был, я минимизировал это.
I said "Did this side reply?" Cause it wasn't supposed to.|Я сказал: "Эта сторона ответила?" Потому что этого не должно было быть.
Because whats happening is, okay the packet goes through the router, or the frame goes through the router, then the router looks,|Поскольку что происходит, хорошо, пакет проходит через маршрутизатор, или кадр проходит через маршрутизатор, затем маршрутизатор смотрит,
its matching up what ever destination it wants to go to, right.|это соответствует тому месту назначения, куда он хочет отправиться, верно.
So it sends it to this router, this router has no entry, it's not going beyond this point.|Таким образом, он отправляет его на этот маршрутизатор, у этого маршрутизатора нет входа, он не выходит за пределы этой точки.
Heck, it's not probably, it's not going beyond this point right here,|Черт возьми, это не вероятно, это не выходит за рамки этой точки прямо здесь,
because it doesn't know about the 1.0|потому что он не знает о 1.0
network.|сеть.
This router doesn't know about the 1.0|Этот маршрутизатор не знает о версии 1.0
network.|сеть.
And this router definitely doesn't know about the 3.0 network.|А про сеть 3.0 этот роутер точно не знает.
So, if I was pinging the two, somewhere in the two, it may work.|Итак, если я пинговал два, где-то два, это может сработать.
Let's, let's see.|Давай, посмотрим.
Let's see what happens using that default out.|Посмотрим, что произойдет при использовании этого значения по умолчанию.
And we wanna ping, the two dot one and see what happens.|И мы хотим пинговать, две точки, и посмотреть, что произойдет.
[BLANK_AUDIO]|[BLANK_AUDIO]
Still not getting where we need to go.|Все еще не добираемся туда, куда нам нужно идти.
Still not getting where we need to go.|Все еще не добираемся туда, куда нам нужно идти.
Okay, because we need to tell this router,|Хорошо, потому что нам нужно сообщить этому маршрутизатору,
all right you're getting there.|хорошо, вы добираетесь туда.
It's not unreachable, it's a timeout.|Это не недостижимо, это тайм-аут.
Because you're getting to where your destination is.|Потому что вы добираетесь до места назначения.
It just, when it goes back to the router,|Просто, когда он возвращается к маршрутизатору,
it doesn't know where to send you.|он не знает, куда вас послать.
Because the router has no entry.|Потому что в роутере нет входа.
That middle router has no entry for the 3.0.|Этот средний маршрутизатор не имеет записи для 3.0.
Or the 1.0.|Или 1.0.
So its not going to be able to send it back where it belongs.|Так что он не сможет отправить его туда, где он принадлежит.
That's where your getting those timeouts.|Вот откуда у вас таймауты.
That's why, when we're looking and we're trouble shooting and we're pinging and we trace route, and we do all these things.|Вот почему, когда мы ищем и устраняем проблемы, мы пингуем, отслеживаем маршрут и делаем все это.
We need to understand what those messages are telling us.|Нам нужно понимать, о чем нам говорят эти сообщения.
Unreachable, we never made it out our own gateway.|Недостижимые, мы так и не смогли выбраться через наши собственные ворота.
Or we didn't get to a certain point, okay,|Или мы не дошли до определенного момента, ладно,
out of our own network.|вне нашей собственной сети.
But when you say request time out, that means it did get there.|Но когда вы говорите, что время ожидания запроса истекло, это означает, что он действительно был доставлен.
It's just that that device, that remote device or one of the remote devices did not have an entry to send it back to me.|Просто это устройство, это удаленное устройство или одно из удаленных устройств не имело записи, чтобы отправить их мне.
That's what that means, so what do we need to do?|Вот что это значит, так что нам нужно делать?
We need to go ahead and configure, static routes, in the middle router,|Нам нужно продолжить и настроить статические маршруты в среднем маршрутизаторе,
in order for this network to work, all right.|для того, чтобы эта сеть работала, ладно.
So let's go ahead and do that.|Так что давайте продолжим и сделаем это.
Very simple, same, same type of syntax.|Очень простой, такой же синтаксис того же типа.
Okay.|Ладно.
Same type of syntax.|Одинаковый синтаксис.
But this time we're actually going to give it the networks that we don't know about.|Но на этот раз мы фактически предоставим ему сети, о которых мы не знаем.
Which is the 1.0 and the 3.0.|Это 1.0 и 3.0.
So we have default routes on either end.|Итак, у нас есть маршруты по умолчанию на обоих концах.
But we don't have it on the middle router.|Но у нас его нет на среднем роутере.
What is it.|Что это.
Cisco.|Cisco.
All right, Config T, so we're gonna go IP route, destination network,|Хорошо, Config T, мы идем по IP-маршруту, сети назначения,
192.168, it doesn't matter which one you do first.|192.168, неважно, что вы сделаете в первую очередь.
We have the mask of, out, my exit interface.|У нас есть маска моего выходного интерфейса.
This is to, this is going this way,|Это то, что происходит,
that's where the 1.0 is, so it's going out my S0/0/1.|вот где находится 1.0, так что он выходит из моего S0 / 0/1.
So my exit interface is S0/0/1.|Итак, мой интерфейс выхода - S0 / 0/1.
And now the other, and I'm gonna [UNKNOWN]|А теперь другой, и я собираюсь [НЕИЗВЕСТНО]
I'm gonna cheat big time, it's gonna be going this way, so it's triple zero.|Я собираюсь жульничать, так и будет, так что это три ноль.
And then I'm gonna.|А потом я собираюсь.
Put at the 3.0.|Ставить на 3.0.
So now I have two static entries to either network.|Итак, теперь у меня есть две статические записи в любую сеть.
Now I know about those networks.|Теперь я знаю об этих сетях.
So once they get to me I know how to send them back.|Так что, как только они доберутся до меня, я знаю, как их отправить.
So, let's copy this.|Итак, давайте скопируем это.
I'll cheat again.|Я снова обманываю.
Wow, really cheat do W.|Ух ты, действительно жульничаешь W.
That's the only command.|Это единственная команда.
Really you need to do exit then you do a copy and start.|На самом деле вам нужно выйти, затем вы сделаете копию и начнете.
Alright, let's take a look at the routing table.|Хорошо, давайте посмотрим на таблицу маршрутизации.
I did a Ctrl+Z in that moment.|В тот момент я нажал Ctrl + Z.
I'll do a show IP route.|Я покажу IP-маршрут.
So, now in your middle router and let's bring this up again.|Итак, теперь в вашем среднем маршрутизаторе, и давайте снова поднимем это.
We have two static entries.|У нас есть две статические записи.
We have three connected routes.|У нас есть три связанных маршрута.
Right?|Правильно?
The three connected networks that we know about.|Три связанные сети, о которых мы знаем.
The four the eight and the two.|Четыре, восемь и два.
But we now told it, that hey, there is a one dot zero network that's going to be, you know, you got to send it out this interface, and|Но теперь мы сказали ему, что есть сеть с одной точкой и нулем, которая будет, вы знаете, вы должны отправить ее через этот интерфейс, и
there's a three dot zero network that you got to send it out that interface.|есть сеть с тремя точками и нулем, которую вы должны отправить через этот интерфейс.
So now let's see what happens.|Итак, теперь посмотрим, что произойдет.
Alright which IP address.|Хорошо, какой IP-адрес.
Let's ping the 2.1.|Давайте пингуем 2.1.
We got a request timed out last time.|В прошлый раз истекло время ожидания запроса.
Let's see what happens.|Давай посмотрим что происходит.
Now we get a reply.|Теперь мы получаем ответ.
Why do we get a reply?|Почему мы получаем ответ?
Because it got there and when it went back up to the router.|Потому что он туда попал и когда вернулся к маршрутизатору.
It said okay, I know where that's at.|Там было сказано: хорошо, я знаю, где это.
It's this way and sends it to the other router.|Он отправляет его на другой маршрутизатор.
Lets do a, 1.1.|Давайте сделаем, 1.1.
It should, its ethernet,|Он должен, его локальная сеть,
that's why the first, request time outs going to happen.|вот почему произойдет первое время ожидания запроса.
Alright, but you see got a reply, you do it again.|Хорошо, но вы видите, что получил ответ, вы делаете это снова.
Now the ark cash is filled, we know how to get there.|Теперь наличные в ковчеге заполнены, мы знаем, как туда добраться.
Boom.|Бум.
we get four replies.|мы получаем четыре ответа.
So, here you have on the edge routers, you have two static entries.|Итак, у вас есть граничные маршрутизаторы, у вас есть две статические записи.
I mean, I'm sorry, you have two default routes.|Я имею в виду, извините, у вас есть два маршрута по умолчанию.
And in the middle, you have a static entries.|А в середине у вас есть статические записи.
One for either network.|Один для любой сети.
So use your combination of routing if you would.|Так что используйте вашу комбинацию маршрутизации, если хотите.
All right with static routes and default routes at the end.|Хорошо, со статическими маршрутами и маршрутами по умолчанию в конце.
All right, next lesson we're gonna go to the live routers and we're gonna repeat what we just did, but we're gonna do it slightly different,|Хорошо, на следующем уроке мы перейдем к живым роутерам и повторим то, что только что сделали, но мы сделаем это немного по-другому,
we're gonna go ahead and change the administrative distance.|мы собираемся изменить административное расстояние.
I'll see you there.|Увидимся там.