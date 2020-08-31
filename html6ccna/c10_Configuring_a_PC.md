D:\mailCloud\prjother\tmp\1\c10_Configuring a PC.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
Okay, it is time to configure RPCs.|Хорошо, пора настроить RPC.
Now remember, we said that the last available P, available IP address was for the default gateway.|Теперь помните, мы сказали, что последний доступный P, доступный IP-адрес был для шлюза по умолчанию.
Then we use 253 for the switch, and switch's gateway is 254.|Затем мы используем 253 для коммутатора, а шлюз коммутатора - 254.
But, for the N devices we start by 1.|Но для N устройств мы начинаем с 1.
And that's just my own little Laz standard that I like to do.|И это просто мой собственный маленький стандарт Laz, который мне нравится делать.
All right, so we're gonna go to PC 0.|Хорошо, мы перейдем к ПК 0.
We click on it, and we go to the Desktop tab.|Щелкаем по нему, и переходим во вкладку Рабочий стол.
And then under IP Configuration, and I hope you can see that.|И затем в разделе «Конфигурация IP», и я надеюсь, вы это видите.
Let me put it this way, all right.|Позвольте мне сказать так, хорошо.
Whoa, what happened there?|Что там случилось?
A magic trick, there we go.|Волшебный трюк, вот и все.
I'm going to do 192.168.1.1|Собираюсь сделать 192.168.1.1
tab tab, default mask for a class C.|вкладка, маска по умолчанию для класса C.
And then the gateway cuz we have a router,|А затем шлюз, потому что у нас есть маршрутизатор,
192.168.1.254.|192.168.1.254.
Now, we are gonna have a DNS server.|Теперь у нас будет DNS-сервер.
That will be the last device we configure.|Это будет последнее устройство, которое мы настроим.
So, we're gonna put an IP address for DNS server.|Итак, мы собираемся указать IP-адрес для DNS-сервера.
So, our DNS server is gonna be 192.168.1.3.|Итак, наш DNS-сервер будет 192.168.1.3.
That's gonna be our DNS server.|Это будет наш DNS-сервер.
And I'm gonna configure some stuff there you'll see.|И я собираюсь настроить кое-что, что вы увидите.
Just a little basic stuff so you can see how that works.|Просто немного базовых вещей, чтобы вы могли увидеть, как это работает.
And then we close that, cuz the packet tracer automatically once you put in information, it memorizes it.|И затем мы закрываем это, потому что трассировщик пакетов автоматически, как только вы вводите информацию, запоминает ее.
So, go into the second PC,|Итак, заходим на второй компьютер,
Desktop tab, IP Configuration,|Вкладка Рабочий стол, Конфигурация IP,
192.168.1.2 tab, whoops, tab, tab.|192.168.1.2 вкладка, упс, вкладка, вкладка.
Default gateway, which is the same thing,|Шлюз по умолчанию, то же самое,
1.254, and then the same DNS server, which is 3 192,|1.254, а затем тот же DNS-сервер, то есть 3 192,
can you see that.|Вы можете видеть, что.
I'm sorry, let me put this, this way,|Извините, позвольте мне сказать вот так,
192.168.1.3.|192.168.1.3.
So we've got the 1.1 for the first PC, and a 1.3,|Итак, у нас есть 1.1 для первого ПК и 1.3,
a 1.254 for the gateway, and a 1.3 for the DNS server.|1,254 для шлюза и 1,3 для DNS-сервера.
The gateway's the same for both, which is 1.254.|Шлюз у обоих одинаковый, это 1,254.
So, let's check for connectivity, but we're gonna do it a special way, we're gonna do it a special way.|Итак, давайте проверим подключение, но мы будем делать это особым образом, мы будем делать это особым образом.
So, I'm gonna move this whole thing right here.|Итак, я перенесу все это прямо сюда.
I'm gonna do a lasso and loop, and I'm gonna move it this way.|Я сделаю лассо и петлю и переместу его сюда.
Well, you know what, I'm gonna leave it right here.|Ну, знаешь что, я оставлю это прямо здесь.
What I want to do is, remember when I told you about those special envelopes, and how you can see the packet flow information?|Что я хочу сделать, это вспомнить, когда я рассказывал вам об этих специальных конвертах, и как вы можете увидеть информацию о потоке пакетов?
I'm gonna go to simulation mode, and I'm going to select the simple PDU, which is the closed envelope.|Я перейду в режим моделирования и выберу простой PDU, который является закрытым конвертом.
I'm gonna click on it, and I'm gonna click on PC0.|Я нажму на него, и я нажму на PC0.
And then I'm going to click on PC1 if I can get my mouse over there.|И затем я собираюсь щелкнуть по ПК1, если я смогу навести туда указатель мыши.
There we go.|Вот и все.
Right, so what's going to happen, you see,|Хорошо, так что же произойдет, видите ли,
look, there's two envelopes there.|смотри, там два конверта.
And what are they?|А какие они?
If you look, if you expand this panel right here,|Если вы посмотрите, если вы развернете эту панель прямо здесь,
if you expand it, you can see it says,|если вы развернете его, вы увидите, что он говорит:
ICMP and ARP, ICMP and ARP.|ICMP и ARP, ICMP и ARP.
So, the first thing that happens will be an ARP and then the ICMP.|Итак, первым делом будет ARP, а затем ICMP.
So, let's take a look at what actually happens when you have a switch, a router.|Итак, давайте посмотрим, что на самом деле происходит, когда у вас есть коммутатор, маршрутизатор.
And really, what,|И действительно, что,
you're not gonna go all the way to the router cuz you're in the same network.|вы не собираетесь идти до маршрутизатора, потому что вы находитесь в той же сети.
So it should just go right here.|Так что он должен пойти прямо сюда.
So but, let's see what happens.|Но давайте посмотрим, что произойдет.
So you press right here.|Итак, вы нажимаете прямо здесь.
Let me go over here where it says Auto Capture and Play.|Позвольте мне пройти сюда, где написано «Автозахват и воспроизведение».
You click, boom.|Вы щелкаете, бум.
What coming down?|Что идет?
ARP, take a look at it, ARP.|ARP, взгляните на это, ARP.
Now, you see it went to both places because it floods the network both ways.|Теперь вы видите, что он попал в оба места, потому что он наводняет сеть в обоих направлениях.
But you see it x'ed out right there.|Но вы видите это прямо там.
And then the ARP comes back to the PC, and now, if you look here, the ping is next.|А затем ARP возвращается на ПК, и теперь, если вы посмотрите сюда, следующий пинг.
And there we have a ping.|А там пинг.
[BLANK_AUDIO]|[BLANK_AUDIO]
And it goes to the PC.|И это идет к ПК.
So isn't that great?|Так разве это не здорово?
You can see the packet flow as it goes,|Вы можете видеть поток пакетов, как он идет,
and then the ping goes back,|а затем пинг возвращается,
which is the reply.|что и есть ответ.
And then to delete it, you select here and then delete.|А затем, чтобы удалить его, вы выбираете здесь, а затем удаляете.
And then always remember, go back to real time mode and play with this.|И затем всегда помните, вернитесь в режим реального времени и поиграйте с этим.
This is something, it's a pretty neat tool to look at flow.|Это что-то, это довольно изящный инструмент для изучения потока.
Now, why did it x out here?|Итак, почему это x здесь?
Because we weren't going outside our network.|Потому что мы не выходили за пределы нашей сети.
But I'll switch, as you will learn in the switching section, it flows out all.|Но я переключаюсь, как вы узнаете в разделе переключения, все вытекает.
The ARP flows out all the the ports,|ARP исходит из всех портов,
except the one that it learned the source MAC address on.|кроме того, на котором он узнал MAC-адрес источника.
So that's why it went up to a router, but the router says, hey, that's not me.|Вот почему он подошел к маршрутизатору, но маршрутизатор говорит: эй, это не я.
And then that PC responded, hey, that's me.|А потом тот компьютер ответил: «Эй, это я».
Here's my MAC address, and then the ping went back.|Вот мой MAC-адрес, а затем пинг вернулся.
So that's pretty cool, so we have connectivity.|Так что это круто, у нас есть возможность подключения.
Now if you really want to verify if that,|Теперь, если вы действительно хотите проверить это,
you know, was, hey,|ты знаешь, был, эй,
I'm not used to seeing, you know, things like that.|Я не привык видеть такие вещи.
I'm used to seeing the ping, that's fine.|Я привык видеть пинг, ничего страшного.
You go to any PC.|Заходишь на любой ПК.
And you go to the command prompt, and you ping 192.168.1.3,|И вы переходите в командную строку, и вы ping 192.168.1.3,
I mean not 3, I'm sorry, 2.|То есть не 3, извините, 2.
And then you get your full replies.|И тогда вы получите полные ответы.
And there you have it, and you've pinged across.|Вот и все, и вы перешли.
We've created a very simple topology, all right.|Хорошо, мы создали очень простую топологию.
Now the last thing that we're going to do is,|Теперь последнее, что мы собираемся сделать, это
because we did put a DNS server address,|потому что мы указали адрес DNS-сервера,
we're actually going to add a server.|мы на самом деле собираемся добавить сервер.
And we'll do a little configuration in the server, make, turn it into a web server.|И мы сделаем небольшую настройку на сервере, сделаем, превратим его в веб-сервер.
Alright?|Хорошо?
And change some things so you can take a look at the configuration tab of the server.|И измените некоторые вещи, чтобы вы могли взглянуть на вкладку конфигурации сервера.
I'll see you in that one.|Увидимся в этом.
[BLANK_AUDIO]|[BLANK_AUDIO]
[BLANK_AUDIO]|[BLANK_AUDIO]
Okay.|Ладно.
It is time to configure our PCs.|Пришло время настроить наши ПК.
Now remember, we said that the last available P,|Теперь помните, мы сказали, что последний доступный P,
available IP address was for the default gateway.|доступный IP-адрес был для шлюза по умолчанию.
Then we used 253 for the switch and the switches gateway is 254.|Затем мы использовали 253 для коммутатора, а шлюз коммутатора - 254.
But, for the end devices, we start by one.|Но для конечных устройств мы начнем с одного.
And that's just my own little las standard that I like to do.|И это просто мой собственный маленький лас-стандарт, который мне нравится делать.
All right, so we're going to go to PC zero, we click on it and we go to the Desktop tab.|Итак, мы собираемся перейти на нулевой компьютер, щелкаем по нему и переходим на вкладку «Рабочий стол».
And then under IP configuration, and I hope you can see that,|Затем в разделе конфигурации IP, и я надеюсь, вы это видите,
let me put it this way, all right.|позвольте мне сказать так, хорошо.
Woah, we have an error.|Вау, у нас ошибка.
Magic trick.|Фокус.
There you go.|Вот так.
What I'm gonna do, 192.68.1.1., tab, tab.|Что я буду делать, 192.68.1.1., Вкладка, вкладка.
Default mass work for class C.|Массовая работа по умолчанию для класса C.
And then the gateway cuz we have a router,|А затем шлюз, потому что у нас есть маршрутизатор,
192.168.1.254.|192.168.1.254.
Now, we are gonna have a DNS server.|Теперь у нас будет DNS-сервер.
That'll be the last device we configure.|Это будет последнее устройство, которое мы настроим.
So, we're gonna put an IP address for DNS server.|Итак, мы собираемся указать IP-адрес для DNS-сервера.
So, our DNS server is gonna be 192.168.1.3, that's going to be our DNS server.|Итак, наш DNS-сервер будет 192.168.1.3, это будет наш DNS-сервер.
And I'm going to configure some stuff there you'll see.|И я собираюсь настроить кое-что, что вы увидите.
Just a little basic stuff so you can see how that works.|Просто немного базовых вещей, чтобы вы могли увидеть, как это работает.
And then we close that.|И затем мы закрываем это.
Cuz the package tracer automatically, once you put in information, it memorizes it.|Поскольку трассировщик пакетов автоматически, как только вы вводите информацию, он запоминает ее.
So going to the second PC, Desktop tab,|Итак, перейдем на второй компьютер, вкладку Desktop,
IP configuration, 192.168.1.2,|Конфигурация IP, 192.168.1.2,
tab, oops, tab, tab.|вкладка, упс, вкладка, вкладка.
Default gateway, which is the same thing 1.254.|Шлюз по умолчанию, это тоже самое 1.254.
And then the same DNS server, which is 3,|А потом тот же DNS-сервер, а это 3,
192.|192.
Can you see that?|Вы можете видеть, что?
I'm sorry.|Мне жаль.
Let me put this this way.|Позвольте мне сказать это так.
192.168.1.3.|192.168.1.3.
So we got the 1.1 for the first PC, and a 1.3,|Итак, мы получили 1.1 для первого ПК и 1.3,
a 1.254 is the gateway, and 1.3 for the DNS server.|1,254 - шлюз, а 1,3 - DNS-сервер.
The gate was the same for both, which is 1.254.|Ворота были одинаковы для обоих, это 1,254.
So let's check for connectivity, but we are going to do it a special way.|Итак, давайте проверим подключение, но мы будем делать это особым образом.
We are going to do it a special way, so I am going to move this whole thing right here, I am going to do the last one loop and|Мы собираемся сделать это особым образом, поэтому я собираюсь переместить все это прямо здесь, я собираюсь сделать последний цикл и
I want to move it this way, well you know what?|Я хочу сдвинуть его сюда, ну знаете что?
I am going to leave it right here.|Я собираюсь оставить это здесь.
What I want to do is, remember I told you about those special envelopes?|Я хочу, помните, я рассказывал вам об этих специальных конвертах?
And how you can see the packet flow information?|А как посмотреть информацию о потоке пакетов?
I'm gonna go to simulation mode and I'm gonna select the simple PDU which is the closed envelope and I'm gonna click on it and I'm gonna click|Я перейду в режим симуляции и выберу простой PDU, который является закрытым конвертом, я нажму на него, и я нажму
on PC zero.|на ПК ноль.
[BLANK_AUDIO]|[BLANK_AUDIO]
And then I'm gonna click on PC one.|А потом я нажму на ПК.
If I can get my mouse over there.|Если я смогу достать туда мышку.
There we go.|Вот и все.
Right.|Правильно.
So what's gonna happen?|Так что же произойдет?
You see, look, there's two envelopes there.|Понимаете, смотрите, там два конверта.
And what are they?|А какие они?
If you look, if you expand this panel right here,|Если вы посмотрите, если вы развернете эту панель прямо здесь,
If you expand it, you can see it says,|Если вы развернете его, вы увидите, что он говорит:
ICMP and ARP, ICMP and ARP.|ICMP и ARP, ICMP и ARP.
So the first thing that happens will be an ARP, and then the ICMP.|Итак, первым делом будет ARP, а затем ICMP.
So let's take a look at what actually happens when you have a switch, a router.|Итак, давайте посмотрим, что на самом деле происходит, когда у вас есть коммутатор, маршрутизатор.
And really, well, you're not gonna go all the way to the router.|И в самом деле, вы не дойдете до роутера.
Cuz you're in the same network, so you should just go right here.|Потому что вы находитесь в той же сети, поэтому вам нужно просто пойти сюда.
So, but, but, see what happens.|Итак, но, но посмотрим, что произойдет.
So you press right here.|Итак, вы нажимаете прямо здесь.
Let me go over here, where it says auto capture and play.|Позвольте мне перейти сюда, где написано, что автоматическая съемка и воспроизведение.
You click.|Вы щелкаете.
Boom!|Бум!
What's coming down, ARP.|Что будет дальше, ARP.
Take a look at it, ARP.|Посмотри на это, ARP.
Now you see it went to both places because it floods the network both ways.|Теперь вы видите, что он пошел в оба места, потому что он наводняет сеть в обоих направлениях.
But you see it X'd out right there.|Но вы видите это прямо там.
And then the ARP comes back to the PC.|А затем ARP возвращается на ПК.
And now if you look here, the ping is next.|А теперь, если вы посмотрите сюда, следующий пинг.
[BLANK_AUDIO]|[BLANK_AUDIO]
And there we have a ping.|А там пинг.
[BLANK_AUDIO]|[BLANK_AUDIO]
And it goes to the PC.|И это идет к ПК.
So wasn't that great?|Так разве это не здорово?
You can see the pack and flow as it goes.|Вы можете видеть стаю и поток, как он идет.
And then the ping goes back.|А затем пинг возвращается.
And which was the reply.|И что было ответом.
And then to delete it you select here.|А затем, чтобы удалить его, вы выбираете здесь.
And then Delete, and then always remember go back to real time mode.|А затем Удалить, а затем всегда помнить, что нужно вернуться в режим реального времени.
And play with this, this is something,|И поиграйте с этим, это что-то,
it's a pretty neat tool to look at flow.|это довольно удобный инструмент для изучения потока.
Now, why did it x out here, because we weren't going outside our network.|Итак, почему это произошло здесь, потому что мы не выходили за пределы нашей сети.
But our switch, as you will learn in the switching section, it floods out all,|Но наш коммутатор, как вы узнаете из раздела о переключении, вытесняет все,
the ARP floods out all the,|ARP затопляет все,
the ports except the one that it learned the source MAC address on.|порты, кроме того, на котором он узнал MAC-адрес источника.
So, that's why we went up to the router.|Итак, мы подошли к роутеру.
But the router says, hey, that's not me.|Но роутер говорит, эй, это не я.
And then that PC responded hey, that's me.|А потом тот ПК ответил: "Эй, это я".
Here's my MAC address, and then the ping went back.|Вот мой MAC-адрес, а затем пинг вернулся.
So that's pretty cool.|Так что это круто.
So we have connectivity.|Итак, у нас есть возможность подключения.
Now if you really want to verify that, you know, wasn't, hey, I'm not used to seeing,|Теперь, если вы действительно хотите проверить это, знаете, не было, эй, я не привык видеть,
you know, things like that, I'm just used to seeing the ping, that's fine.|знаете, такие вещи, я просто привык видеть пинг, это нормально.
You go to any PC and you go to the command prompt and you ping.|Вы заходите на любой компьютер, заходите в командную строку и пингуетесь.
192.168.1.3.|192.168.1.3.
I mean not three, I'm sorry.|То есть не трое, извини.
Two.|Два.
And then you get your four replies.|И тогда вы получите свои четыре ответа.
And there you have it, and you've pinged across.|Вот и все, и вы перешли.
We've created a very simply topology.|Мы создали очень простую топологию.
All right.|Отлично.
Now the last thing that we're going to do is, cuz we did put a DNS server address,|Последнее, что мы собираемся сделать, это, поскольку мы указали адрес DNS-сервера,
we're actually going to add a server and we'll do a little configuration in the server, turn it into a web server,|мы на самом деле собираемся добавить сервер, и мы сделаем небольшую настройку на сервере, превратим его в веб-сервер,
all right?|отлично?
And change some things, so you can take a look at the configuration tab of the server, I'll see you in that one.|И измените некоторые вещи, чтобы вы могли взглянуть на вкладку конфигурации сервера, увидимся на ней.