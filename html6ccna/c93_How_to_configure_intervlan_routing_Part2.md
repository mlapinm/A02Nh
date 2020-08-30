D:\mailCloud\prjother\tmp\1\c93_How to configure intervlan routing Part2.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
You see what I did here?|Вы видите, что я здесь сделал?
Yeah, I've trunked the pores, I thought I was in the client's switch, so.|Ага, я пробил поры, думал, что попал в коммутатор клиента, так что.
We can always get rid of that, not a big deal,|Мы всегда можем избавиться от этого, не беда,
we're not putting in at the end of those ports anyway.|в любом случае мы не устанавливаем в конце этих портов.
All right, all right, all right.|Хорошо, хорошо, хорошо.
Do WR, or WR, that was interesting that I didn't see that.|Сделайте WR или WR, это было интересно, что я этого не видел.
Show start, okay, there you go.|Покажи старт, ладно, поехали.
22, 23, and 24.|22, 23 и 24.
Good to go.|Хорошо пойти.
Let me verify here in the spanning tree.|Позвольте мне проверить здесь, в остовном дереве.
Show.|Шоу.
Yeah see, I did 40 and 50.|Да, видите, я сделал 40 и 50.
Okay.|Ладно.
Show spanning tree.|Показать остовное дерево.
And there's 40.|А их 40.
I didn't see 50.|Я не видел 50.
[BLANK_AUDIO]|[BLANK_AUDIO]
So we got for VLAN on one which is priority one.|Итак, мы получили для VLAN одну, которая является приоритетной.
And 40.|И 40.
And oh VLAN 50 there it is right there.|И ох, VLAN 50 вот он тут.
Okay cool.|Хорошо.
All right all right,|Хорошо, хорошо,
we're good to go there.|нам хорошо туда идти.
We're good to go there.|Мы готовы пойти туда.
All right let's go to the client.|Ладно переходим к клиенту.
And we have, let's verify, let's verify.|И у нас есть, давайте проверим, давайте проверим.
Let's make it first.|Сделаем это первым.
Before we give it a name.|Прежде чем дать ему имя.
I think this is Ctrl+Shift text.|Думаю, это текст Ctrl + Shift.
Okay.|Ладно.
Enable, we said registrar so we will make this registrar.|Включите, мы сказали регистратора, поэтому мы сделаем этого регистратора.
Config T host name registrar.|Настройте регистратор имени хоста T.
All right, so we'll go VTP domain, nope,|Хорошо, мы перейдем к домену VTP, нет,
VTP mode client.|Клиент режима VTP.
All right do show v lan.|Хорошо, покажи в лан.
Cool, cool, there it is.|Круто, круто, вот оно.
So int range.|Итак, int range.
F0/1-15#SWitchport MODE Access,|F0 / 1-15 # SWitchport MODE Доступ,
#SWitchport ACcess VLAN 30.|#SWitchport ACcess VLAN 30.
Then we do the SWitch, Port security.|Затем мы делаем SWitch, безопасность порта.
So it's port security, MAC sticky.|Так что это безопасность порта, MAC липкий.
So it's port security, max one.|Так что это безопасность порта, максимум один.
So it's port security, mile shut.|Так что это охрана порта, миля закрыта.
Then we do spanning tree.|Затем делаем остовное дерево.
Port fast all right, to turn it off on those ports, and then we already guessed it.|Port fast all right, отключить его на тех портах, а то мы уже догадались.
Span tree, new PGU guard, enable DWR.|Span tree, новая защита PGU, включить DWR.
So that's the registrar, PC right there,|Вот и регистратор, вот тут ПК,
or switch I should say.|или переключиться, я бы сказал.
And now the last switch, it's going to be the executive.|И теперь последний переключатель, это будет исполнительный директор.
The executive switch.|Исполнительный выключатель.
Enable.|Включить.
Config T.|Конфиг T.
Host name.|Имя хоста.
Exec.|Exec.
BTP mode.|Режим BTP.
Client.|Клиент.
Initial VLAN just to verify, there they are.|Начальный VLAN просто для проверки, вот они.
So int range F0/1-15.|Итак, int range F0 / 1-15.
Switch port mode access,|Доступ в режим порта коммутатора,
switch port access VLAN 60,|порт коммутатора доступа VLAN 60,
then switch port,|затем переключить порт,
port security MAC sticky match one.|безопасность порта MAC липкий соответствует одному.
Vio sharp.|Вио диез.
Spanning tree port fast.|Быстрый порт связующего дерева.
Spanning tree DWR enable.|Включение связующего дерева DWR.
DWR.|DWR.
So we've done everything.|Итак, мы все сделали.
The only one that was different from the rest of the configuration was the first pyramid, where we actually put an IP address for|Единственное, что отличалось от остальной конфигурации, была первая пирамида, где мы фактически поместили IP-адрес для
VLAN1 and the default gateway, for VLAN1.|VLAN1 и шлюз по умолчанию для VLAN1.
Now that we've got all our VLAN's assigned properly, all right?|Теперь, когда у нас есть все наши VLAN, правильно?
I had to switch around IPs, and we got the spanning tree and we got the trunking going on and we got the security going on.|Мне пришлось переключить IP-адреса, и мы получили связующее дерево, и мы получили транкинг, и мы включили безопасность.
Now it's gonna come time to do our inter VLAN routing, so again,|Теперь пришло время выполнить маршрутизацию между VLAN, так что снова,
we'll do it pyramid by pyramid by pyramid.|мы сделаем это пирамида за пирамидой за пирамидой.
We will check first to see we are connectivity within ourselves and then we'll do the routing to see if we can get across using EIGRP.|Сначала мы проверим, есть ли возможность подключения внутри себя, а затем проведем маршрутизацию, чтобы увидеть, сможем ли мы обойтись через EIGRP.
So let's start with this particular router right here.|Итак, давайте начнем с этого конкретного маршрутизатора прямо здесь.
Okay.|Ладно.
[BLANK_AUDIO]|[BLANK_AUDIO]
And we're gonna say null, obviously, here.|И, очевидно, здесь мы скажем null.
This is gonna be router one, generic name.|Это будет общее имя роутера.
Conf t host name R1.|Подтвердите имя хоста R1.
And again, int F0/0 Enter.|И снова int F0 / 0 Enter.
And here we have DNS 10 and 20 and we have VLAN1.|А здесь у нас есть DNS 10 и 20, и у нас есть VLAN1.
So, we gotta create the appropriate sub interfaces.|Итак, нам нужно создать соответствующие субинтерфейсы.
Well let's slow down, slow down so, 0.1,|Ну давай помедленнее, помедленнее так, 0,1
for VLAN1.|для VLAN1.
ENCAP, okay, 0.1q,|ENCAP, ладно, 0.1q,
one, must be one.|один, должен быть один.
And then the IP address would be 192.168|И тогда IP-адрес будет 192.168
IP address 192.168.1.254|IP-адрес 192.168.1.254
255.255.255.0, enter.|255.255.255.0, введите.
Then we go to the next subinterface should be ten.|Затем переходим к следующему подинтерфейсу, должно быть десять.
So I'm gonna up arrow, subinterface ten.|Итак, я собираюсь стрелкой вверх, субинтерфейс десять.
Encapsulation DOT1Q10.|Инкапсуляция DOT1Q10.
And then the IP address will be 10.254.|И тогда IP-адрес будет 10.254.
And the reason I do it that way is just to make life a whole lot easier.|И причина, по которой я это делаю, - просто чтобы сделать жизнь намного проще.
Now we got one more sub interface to do.|Теперь нам нужно сделать еще один вспомогательный интерфейс.
Sub interface 20 Endcap DOT1Q, 120.|Вспомогательный интерфейс 20 Заглушка DOT1Q, 120.
That must match.|Это должно совпадать.
That must match.|Это должно совпадать.
And then the IP address.|А потом IP-адрес.
20.|20.
Now I was asked this question only once.|Сейчас мне задали этот вопрос только один раз.
Last, does the IP need to match?|И наконец, должен ли IP совпадать?
Yeah, there, your gateway is your gateway.|Да, вот, ваш шлюз - это ваш шлюз.
Your gateway has to be within your own subnet.|Ваш шлюз должен находиться в вашей собственной подсети.
So the IP address that you put in your gateway must match the IP address on the gateway of your PC.|Таким образом, IP-адрес, который вы вводите в свой шлюз, должен совпадать с IP-адресом шлюза вашего ПК.
So it's an IP addressing thing.|Так что это вопрос IP-адресации.
All right, let's take a look at our routing table, so IP route.|Хорошо, давайте взглянем на нашу таблицу маршрутизации, так что IP-маршрут.
So as we're connected to the one, the ten,|Так как мы связаны с одним, с десятью,
and the 20.|и 20.
Cool, cool.|Классно классно.
Show IP in brief, get that summary to see if everything's up.|Покажите кратко IP, получите это резюме, чтобы увидеть, все ли в порядке.
Problem for the brief, oh, I said spell range, so IT in brief.|Проблема для краткости, о, я сказал диапазон заклинаний, так что вкратце.
All right, and it shows, up up, up up okay?|Хорошо, и это видно, вверх, вверх, ладно?
But one thing I wanna show you is the start, cuz you look at something cool,|Но одна вещь, которую я хочу показать вам, это начало, потому что вы смотрите на что-то крутое,
you can see how that encapsulation is very important.|вы можете видеть, насколько важна эта инкапсуляция.
I never put native, but I knew that when I put that 0.1Q 1,|Я никогда не ставил родной, но знал, что когда ставил ту 0.1Q 1,
that I'm talking about the native VLAN, so you can see how important that number is,|что я говорю о собственной VLAN, чтобы вы могли видеть, насколько важен этот номер,
after the 0.11Q, after the encapsulation type.|после 0.11Q, после типа инкапсуляции.
They are using, it is contacting that particular VLAN so it is imperative,|Они используют эту конкретную VLAN, поэтому это необходимо,
it is extremely important That you match up that number.|Чрезвычайно важно, чтобы вы совпали с этим числом.
That don't want your number with your D LAN ID.|Кому не нужен ваш номер с вашим D LAN ID.
Alright so we're seeing that we're good to go.|Хорошо, мы видим, что все готово.
We've seen.|Мы видели.
Let's ping within ourselves, obviously.|Разумеется, давайте пингуем внутри себя.
And let's bring this over here so you can see it so,|И давайте принесем это сюда, чтобы вы могли это увидеть,
we're gonna ping 192.168.20.1.|мы собираемся пинговать 192.168.20.1.
[BLANK_AUDIO]|[BLANK_AUDIO]
And we get our replies, our first time out.|И мы получаем ответы в первый раз.
Do it again, we get all four replies.|Сделайте это еще раз, мы получим все четыре ответа.
Beautiful.|Прекрасный.
So we are, everything is working in this particular pyramid right here.|Итак, мы, прямо здесь, в этой конкретной пирамиде все работает.
Now remember, here we got the 40 and the 50.|Теперь помните, у нас есть 40 и 50.
This is where I gotta, kind of went crazy,|Вот где я должен, вроде как сошел с ума,
so let's go ahead and 40 and 50.|так что вперед и 40 и 50.
40 and 50.|40 и 50.
We don't have to worry about VLAN 1 on this one, we're not gonna configure it.|Нам не нужно беспокоиться о VLAN 1 на этом, мы не собираемся его настраивать.
All right.|Отлично.
Enable, CONFIG T, this is host name.|Включите, CONFIG T, это имя хоста.
R2.|R2.
Now, we have interface of 0/0, no shot.|Теперь у нас интерфейс 0/0, без выстрела.
Alright.|Хорошо.
Interface .40 or now 40, end cap dot one q 40 and then the IP address is IP address 192.168.40.254.255.255 dot zero.|Интерфейс .40 или теперь 40, точка на торцевой крышке один q 40, а затем IP-адрес - IP-адрес 192.168.40.254.255.255 точка ноль.
Now I want to do one for 50.|Теперь я хочу сделать один за 50.
And I'm gonna make sure again because remember what I just said.|И я собираюсь убедиться еще раз, потому что помню, что я только что сказал.
Okay?|Ладно?
Yes it is 50 okay.|Да, 50, нормально.
Awesome.|Потрясающие.
So, so interface 50 not a requirement to name it the same.|Итак, интерфейс 50 не является обязательным для его названия.
Just makes a whole lot of sense.|В этом есть смысл.
50, and now the ip address will be 50,|50, и теперь ip-адрес будет 50,
[UNKNOWN].|[НЕИЗВЕСТНО].
Two WR.|Два WR.
Control Z, verification verification show IP in brief.|Control Z, верификация верификация кратко показать IP.
Everything is up up.|Все встало.
That's what you want to see.|Это то, что вы хотите увидеть.
Your elevator riding table.|Ваш стол для катания на лифте.
Show IP route.|Показать IP-маршрут.
Alright.|Хорошо.
It says that you're connected directly.|Он говорит, что вы подключены напрямую.
Great So let's try it in ping now, on 40|Отлично Итак, давайте попробуем это в пинге сейчас, на 40
to 50.|до 50.
[SOUND] So we're gonna ping 192.168.50.1.|[ЗВУК] Итак, мы собираемся пинговать 192.168.50.1.
And remember, you're always gonna get that first time out.|И помни, ты всегда получишь первый раз.
Because IPv4, we got that ARP.|Поскольку IPv4, мы получили этот ARP.
Boom, there we go 50.1, do it again,|Бум, мы идем 50.1, сделай это снова,
you'll get your four replies.|вы получите четыре ответа.
Awesome.|Потрясающие.
So, we're able to fix, our, my little craziness there.|Итак, мы можем исправить это мое маленькое безумие.
We'll go to the last one.|Пойдем к последнему.
We got 30 and 60.|У нас 30 и 60.
30 and 60, let's maximize this router.|30 и 60, давайте максимизируем этот роутер.
Say no, enable, config T, alright, host name R3,|Скажите нет, включите, настройте T, хорошо, имя хоста R3,
interface F zero slash zero, no shut on the physical interface, 30,|интерфейс F нулевая косая черта ноль, нет закрытия физического интерфейса, 30,
we will do our first interface of 30 our encapsulation,|мы сделаем наш первый интерфейс 30 нашей инкапсуляции,
right, that's what that's short for,|да, вот что это значит,
DOT1Q 30, that must be the same.|DOT1Q 30, это должно быть то же самое.
And then the IP address is 192.168.30.254,|И тогда IP-адрес 192.168.30.254,
255.255.255.0, enter.|255.255.255.0, введите.
Now we're gonna do the other sub interface which is 60.|Теперь мы займемся вторым субинтерфейсом - 60.
60 in cap 60 and the IP address 60|60 в шапке 60 и IP-адрес 60
okay so that should be it control z WR Verification.|хорошо, так что это должен быть контроль z WR Verification.
Show IP in brief.|Покажите кратко IP.
Everything's up, up.|Все встало, встало.
That's good.|Это хорошо.
Show IP route.|Показать IP-маршрут.
Shows that we're directly connected,|Показывает, что мы напрямую связаны,
perfect.|идеальный.
Everything is up, so let's see if we can ping across.|Все в порядке, давайте посмотрим, сможем ли мы пинговать.
260.1.|260.1.
And let me see if I change the IP address on that one.|И позвольте мне посмотреть, поменяю ли я на этом IP-адрес.
You see.|Ты видишь.
Hm hm hm.|Хм хм хм.
30 dial 1.|30 наберите 1.
I would've never left.|Я бы никогда не ушел.
Never gone anywhere.|Никуда не уходил.
Bring it up to the D4.|Поднесите это к D4.
Here we go.|Вот так.
Ping.|Пинг.
192.168.60.1.|192.168.60.1.
Remember when we had that, I made that, I put the original I P's out the way they should have been,|Помните, когда у нас это было, я сделал это, я выложил оригинальные ИП такими, какими они должны были быть,
until I made a little craziness.|пока я не сделал небольшое сумасшествие.
There we go.|Вот и все.
We get to the other side, do it again when we get to four pings.|Переходим на другую сторону, делаем это снова, когда дойдем до четырех пингов.
Perfect.|Отлично.
So, within our own pyramids,|Итак, внутри наших пирамид
we are communicating with each other,|мы общаемся друг с другом,
which is great.|что здорово.
Alright?|Хорошо?
We have communication.|У нас есть связь.
Remember that opens up a security hole you may not want for anybody to be able to ping your vlan or to access your other vlan.|Помните, что это открывает брешь в безопасности, которую вы, возможно, не хотите, чтобы никто не мог проверить связь с вашим vlan или получить доступ к вашему другому vlan.
But you do need to get out.|Но тебе нужно выбраться.
This is where your access list,|Вот где ваш список доступа,
come in we'll be talking about later on in this course.|войдите, о чем мы поговорим позже в этом курсе.
Now, it comes time to route a, a, across.|Теперь пришло время пересечь маршруты а, а.
Comes time to route across.|Приходит время пересечь дорогу.
So we're gonna be using EIGRP.|Итак, мы будем использовать EIGRP.
Now here in EIGRP we have to advertise the one network, the 10,|Теперь здесь, в EIGRP, мы должны объявить одну сеть, 10,
the 20, and the 10.114.|20 и 10.114.
Alright?|Хорошо?
So we're gonna go, config T > router >|Итак, мы идем, конфиг T> router>
EIGRP.|EIGRP.
And we'll use the autonomous system 100,|И мы будем использовать автономную систему 100,
alright?|хорошо?
And that means that everybody must be in the same autonomous system.|А это значит, что все должны быть в одной автономной системе.
And then we're gonna use network statements 192.168.1.0 about 10.0,|Затем мы будем использовать сетевые операторы 192.168.1.0 около 10.0,
20.0 and net times 10.0.0.0.|20.0 и чистое время 10.0.0.0.
Remember classful boundaries.|Помните классовые границы.
Since we are using a default subnet mass for the class c.|Поскольку мы используем массу подсети по умолчанию для класса c.
We can advertise it like that but with the class A address for the single connections we have a subnetted class A address since EGIRP still|Мы можем рекламировать это так, но с адресом класса A для отдельных подключений у нас есть адрес класса A с подсетями, поскольку EGIRP все еще
a distance vector writing protocol none the less it summarizes automatically so we need to put that and the most famous command of all no auto hyphen Summary.|протокол записи вектора расстояния, тем не менее, он суммируется автоматически, поэтому нам нужно ввести эту и самую известную команду из всех, без автоматического переноса.
You cannot forget to put that.|Вы не можете забыть поставить это.
I've stressed that throughout the routing protocols, for these inspected routing protocols, you cannot, cannot, cannot forget.|Я подчеркнул, что во всех протоколах маршрутизации для этих проверенных протоколов маршрутизации вы не можете, не можете и не можете забыть.
Alright.|Хорошо.
That's one.|Это один.
Here we need to advertise a 40, the 50,|Здесь нам нужно рекламировать 40, 50,
and the 10.|и 10.
So Config t.|Итак, Config t.
[BLANK_AUDIO]|[BLANK_AUDIO]
Config t.|Конфиг t.
Router, EIGRP 100, must be the same autonomous system.|Маршрутизатор, EIGRP 100, должен быть такой же автономной системой.
Network, 192.168.|Сеть, 192.168.
What is it again?|Что опять?
40 and 50.|40 и 50.
40.0, 50.0, and then net 10.0.0.0,|40.0, 50.0, а затем чистая 10.0.0.0,
we don't have e dot one here so we don't have to worry about it,|у нас нет здесь одной точки, поэтому нам не о чем беспокоиться,
no auto-summary must be put.|авто-сводку ставить не надо.
DO WR.|DO WR.
Oh yes, we are missing something very crucial that we haven't done,|О да, нам не хватает чего-то очень важного, чего мы еще не сделали,
for the right protocol, I got so excited.|за правильный протокол, я был так взволнован.
I want to do a writing protocol first without putting the IP address with all the interfaces so lets just keep going we'll put the IP addresses last.|Я хочу сначала создать протокол записи, не добавляя IP-адрес ко всем интерфейсам, поэтому давайте продолжим, мы поместим IP-адреса в последнюю очередь.
That's very interesting.|Это очень интересно.
Yeah, I'm very excited to see things go across.|Да, я очень рад видеть, как все происходит.
Router EIGRP 100.|Маршрутизатор EIGRP 100.
Here we got the 30, and the 60, that was,|Вот и 30, и 60, то есть
that's easy enough, and the 10.|это достаточно просто, и 10.
So network, we're gonna do this then,|Итак, сеть, мы сделаем это тогда,
cuz I know I have no IP addressing yet, so that's cool.|Потому что я знаю, что у меня еще нет IP-адреса, так что это круто.
Network 192.168.30.0.|Сеть 192.168.30.0.
And the r barrel 60.0 oh, I was wondering I see it you know adjacency and like what's going on, and I go oh, that's right I need IP addresses.|И r баррель 60.0 о, мне было интересно, я вижу это, вы знаете смежность и как то, что происходит, и я иду о, верно, мне нужны IP-адреса.
Move down the r.|Двигайтесь вниз по r.
So, what we need to do [LAUGH] now,|Итак, что нам нужно сделать [СМЕХ] сейчас,
obviously,|очевидно,
is put an IP address [UNKNOWN] serial interface.|ставится IP-адрес [UNKNOWN] последовательного интерфейса.
This one will be the 101110.|Это будет 101110.
So let's go with that one.|Так что давайте с этим.
Interface S0/0/1.|Интерфейс S0 / 0/1.
I believe that's correct.|Я считаю, что это правильно.
See this, you know,|Смотрите это, вы знаете,
what I'm doing, yeah?|что я делаю, да?
Okay.|Ладно.
IP address, 10.1.1.10 255, 255, 255, 252.|IP-адрес, 10.1.1.10 255, 255, 255, 252.
That's right, there you are and here we have the S triple zero, that's 10119.|Правильно, вот и вы, и вот у нас тройной ноль S, это 10119.
So, let's go here, now #EXIT,|Итак, пойдем сюда, а теперь #EXIT,
#INTERFACE S0/0/0, #IP ADDRESS 10.1.1.9|#INTERFACE S0 / 0/0, #IP-АДРЕС 10.1.1.9
255.255.255.252 clock rate,|255.255.255.252 тактовая частота,
you must put the clock rate on the DCE portion of the router.|вы должны установить тактовую частоту на DCE-части маршрутизатора.
Use their maximum, 123, 123.|Используйте их максимум, 123, 123.
And then we're gonna shut it.|А потом мы его закроем.
Be careful what you type there, okay?|Будьте осторожны с тем, что вы там набираете, хорошо?
And then we have an S001 which should be 6.|И затем у нас есть S001, который должен быть 6.
Oops, and there's your adjacencies coming up now, all right?|Ой, а теперь нас ждут ваши соседства, хорошо?
And then the IP address would be IP address 10.1.1.6.255.255.255.252|И тогда IP-адрес будет IP-адресом 10.1.1.6.255.255.255.252.
[BLANK_AUDIO]|[BLANK_AUDIO]
no, no shuts, BWR, and I just wanna check something here.|нет, никаких затворов, BWR, и я просто хочу кое-что здесь проверить.
Well, yes there's a green light, so there's a no shut there.|Ну да, есть зеленый свет, значит, там нет затвора.
And this'll be 10115.|А это будет 10115.
So Exit, Int as 0/0/0.|Итак, Exit, Int как 0/0/0.
IP address 10.1.1.5.255.255.255.252.|IP-адрес 10.1.1.5.255.255.255.252.
Clock rate again cannot forget that on the DC portion of it.|Тактовая частота снова не может забыть, что на части постоянного тока.
All right, and then we're doing more shorts.|Хорошо, а потом мы снимаем еще короткометражки.
Dwr.|Dwr.
Let's wait for adjacency to happen.|Подождем, пока произойдет смежность.
That shouldn't take too long.|Это не должно занять много времени.
There we go.|Вот и все.
I did it kind of backwards,|Я сделал это как бы наоборот,
I guess if you wanna look at it that way.|Я думаю, если ты хочешь посмотреть на это так.
And, let's take a look at the routing table, show IP routes.|И давайте взглянем на таблицу маршрутизации, покажем IP-маршруты.
And we see that we are learning, through the dual,|И мы видим, что мы учимся через дуальное,
we're learning about the 30, the 40, the 50, and the 60.|мы узнаем о 30, 40, 50 и 60.
So, we are learning about all those particular VLANs.|Итак, мы узнаем обо всех этих конкретных VLAN.
So are these be in router apparently,|Очевидно, они в роутере,
okay.|Ладно.
So let's go ahead and ping, always ping,|Так что давай пинг, всегда пинг,
that is how you're going to verify that everything is working.|вот как вы собираетесь проверить, что все работает.
So, I'm just gonna up arrow here.|Итак, я просто собираюсь здесь стрелкой вверх.
I wanna do let's say, 30.1.|Я хочу, скажем, 30.1.
I'm gonna ping.|Я буду пинговать.
40.1 I'm gonna ping.|40.1 Я пингую.
50.1, got a ping.|50.1, получил пинг.
And 60.1.|И 60,1.
Up, 60.1.|Вверх, 60,1.
And I got a ping.|И я получил пинг.
So you see again, one,|Итак, вы снова видите, один,
you're not gonna have to do all this,|тебе не придется делать все это,
right?|право?
When you go to your switching, you'll have a couple switches.|Когда вы перейдете к переключению, у вас будет пара переключателей.
You'll need to go in there, and do a bunch of show commands.|Вам нужно будет зайти туда и выполнить кучу команд show.
And, once you do your EIGRP, there'll be something wrong with it.|И как только вы выполните свой EIGRP, с ним что-то не так.
You have to fix it.|Вы должны это исправить.
The only thing you're actually gonna do from scratch, scratch,|Единственное, что ты собираешься делать с нуля, с нуля,
scratch, is the access list.|царапина, это список доступа.
And that's it.|И это все.
Everything else is, be fixing something.|Все остальное есть, поправляй что-нибудь.
Or you're being, or you're gonna be asked a question about the protocol,|Или вы, или вам зададут вопрос о протоколе,
about spanning tree, about VTP maybe?|о связующем дереве, может быть, о VTP?
I haven't seen much questions about VTP at all.|Я вообще не видел много вопросов о VTP.
And most students have come back, yeah,|И большинство студентов вернулись, да,
they asked me about the VTP.|они спросили меня о VTP.
No.|Нет.
Now as far as your switching simulations like, know your commands, like show DTP status.|Теперь что касается симуляции переключения, знайте свои команды, например, показать статус DTP.
Show MAC address table.|Показать таблицу MAC-адресов.
You know, show CDP neighbor.|Знаешь, покажи соседу ХДП.
Things like that, these are commands that you need to know, because I believe there's a switching simulation, these are commands that will be needed, okay?|Такие вещи, это команды, которые вам нужно знать, потому что я считаю, что есть имитация переключения, это команды, которые потребуются, хорошо?
And know what they mean.|И знайте, что они означают.
Because when they ask you a question about span tree like hey, based on this diagram,|Потому что, когда они задают вам вопрос о связующем дереве типа эй, основываясь на этой диаграмме,
who's gonna be the root bridge?|кто будет корневым мостом?
Well now, you know, the rule bridge is the one with the lowest bridge priority or bridge ID a combination of the bridge priority and|Итак, вы знаете, что мост правил - это мост с самым низким приоритетом моста или идентификатор моста, комбинация приоритета моста и
the MAC address the lowest wins.|MAC-адрес с наименьшим приоритетом.
This is the thing that you need to understand well,|Это то, что нужно хорошо понимать,
we did the EGIRP we're all on the same autonomous system so we're routing back and fourth, but again we did the same exact configurations and|мы сделали EGIRP, мы все находимся в одной автономной системе, поэтому мы выполняем маршрутизацию назад и четвертый, но снова мы сделали те же самые точные конфигурации и
besides the very first pyramid that [INAUDIBLE] on it.|кроме самой первой пирамиды, которая [НЕРАЗБОРЧИВО] на ней.
Other than that, it was the same thing over, and over, and over, and over, and over, and over again.|Кроме этого, одно и то же повторялось снова и снова, и снова, и снова, и снова, и снова.
Same thing with the routing protocols.|То же самое и с протоколами маршрутизации.
The same thing over, and over again repetition brings retention.|Одно и то же, и повторение снова приносит удержание.
This is gonna help you.|Это тебе поможет.
Learn these commands just by doing them over, and over again.|Изучите эти команды, просто повторяя их снова и снова.
And then, try understanding the concepts is what really the course is for,|А затем попытайтесь понять концепции, для чего на самом деле предназначен курс,
understanding.|понимание.
But, what I give you is keyed in,|Но то, что я вам даю, введено,
toned in, or tuned in, I should say, to the certification.|затонировал, или настроил, я бы сказал, на сертификацию.
So, when I say pay attention to this,|Итак, когда я говорю, обратите на это внимание,
there's a reason why I say that.|есть причина, по которой я говорю это.
All right, ladies and gentlemen, that is all.|Хорошо, дамы и господа, вот и все.
I'll see you in the next one.|Увидимся в следующем.
[BLANK_AUDIO]|[BLANK_AUDIO]