D:\mailCloud\prjother\tmp\1\c62_Configuring DHCP Relay Agent.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
Welcome back.|Добро пожаловать.
All right, in the previous lesson we did a DHCP server lab, right?|Хорошо, на предыдущем уроке мы провели лабораторную работу с DHCP-сервером, верно?
We were all in part of the same broadcast domain.|Мы все были частью одного широковещательного домена.
It's important to know because why look what we got here.|Это важно знать, потому что зачем смотреть, что у нас здесь есть.
Okay?|Ладно?
I don't think you can see that because it's like on right behind me.|Я не думаю, что вы это видите, потому что это как будто прямо позади меня.
And I believe I have this lab, when I created this lab I created it somewhere.|И я считаю, что у меня есть эта лаборатория, когда я создавал эту лабораторию, я где-то ее создавал.
I don't remember where, or when I did it.|Я не помню, где и когда я это сделал.
But this was really There was a question based on how DACP worked.|Но это было действительно. Был вопрос, основанный на том, как работает DACP.
This is an actual, well not actual.|Это актуально, а не актуально.
But this is a DACP server right here,|Но вот здесь DACP-сервер,
right.|право.
And you can do this in your packet tracer very very simple.|И вы можете сделать это в вашем пакетном трассировщике очень-очень просто.
All right.|Отлично.
Let's maximize it so you can really see it.|Давайте максимизируем это, чтобы вы действительно могли это увидеть.
And you go to config tab and you go to DACP.|И вы переходите на вкладку config, и вы переходите в DACP.
And you can create your pools.|И вы можете создавать свои бассейны.
You can create actual pool addresses.|Вы можете создавать фактические адреса пула.
Alright.|Хорошо.
And you see my pool names are VLAN 10, 20,|И вы видите, что имена моих пулов - VLAN 10, 20,
40, 50, and we had the default gateway based on the subnet that they're in.|40, 50, и у нас был шлюз по умолчанию, основанный на подсети, в которой они находятся.
Everybody has the same DNS server address.|У всех одинаковый адрес DNS-сервера.
The start IP address would be different based on the subnet you're in.|Начальный IP-адрес будет отличаться в зависимости от подсети, в которой вы находитесь.
And obviously, the subnet mask is two two four,|И, очевидно, маска подсети - два, два, четыре,
because we're using a thirty two increment.|потому что мы используем приращение тридцать два.
Okay, and I have a TITP server address there.|Хорошо, и у меня там есть адрес сервера TITP.
Why, whatever, I don't know why I did that, but I did.|Почему, как бы то ни было, я не знаю, зачем я это сделал, но я сделал.
Okay, but the cool, the thing that you need to understand here,|Ладно, но круто, вот что вам нужно понять,
is what a relay agent is.|что такое агент ретрансляции.
In a Microsoft environment,|В среде Microsoft
you will actually have to go into routing remote access.|вам фактически придется перейти к удаленному доступу с маршрутизацией.
And install that protocol, the ACP relay agent and then configure it to look for, give it the IP address of the DACP server.|И установите этот протокол, агент ретрансляции ACP, а затем настройте его для поиска, дайте ему IP-адрес сервера DACP.
So it can intercept a node.|Таким образом, он может перехватить узел.
It can go on your behalf to assigned IP address and why is that?|Он может перейти от вашего имени к назначенному IP-адресу, и почему?
If you take a look at this configuration,|Если вы посмотрите на эту конфигурацию,
you figure,|вы полагаете,
hey isn't everybody on the same network?|эй, не все ли в одной сети?
No they're not.|Нет, они не.
Because here this v-lan 2, right?|Потому что здесь это v-lan 2, верно?
We have a TITP server, and a DACP server,|У нас есть сервер TITP и сервер DACP,
obviously, statically assigned all right?|очевидно, статически назначено все в порядке?
And he, these switches here are all different.|А он, эти переключатели здесь все разные.
VLANS, we got VLANS 10, 20, 30, 40, and 50,|VLANS, мы получили VLANS 10, 20, 30, 40 и 50,
which means they're in a different broadcast domain.|что означает, что они находятся в другом широковещательном домене.
So the ACP server, or routers for that matter, do not accept,|Таким образом, сервер ACP или маршрутизаторы, если на то пошло, не принимают,
by default, broadcast addresses.|по умолчанию широковещательные адреса.
So if it sees a broadcast address coming at it, it will just dump it.|Поэтому, если он увидит приходящий широковещательный адрес, он просто сбросит его.
It won't accept it.|Он этого не примет.
So if you have an ICP server on another broadcast domain and trying to assign IP addresses within another broadcast domain, it will fail.|Поэтому, если у вас есть сервер ICP в другом широковещательном домене и вы пытаетесь назначить IP-адреса в другом широковещательном домене, это не удастся.
It will actually fail.|Это действительно не удастся.
Now I'll show you when we configure the router,|Сейчас я покажу вам, когда мы настраиваем роутер,
like we normally would for inter VLAN connectivity, but these computers,|как мы обычно делали бы подключение между VLAN, но эти компьютеры,
all right, they're DACP enabled and you see, well let's go let's do static.|хорошо, у них включен DACP, и, видите ли, давайте сделаем статику.
It's, that's like okay, failed.|Это вроде нормально, не удалось.
Because normally I just go static, DACP.|Потому что обычно я просто статичен, DACP.
It's like an IP config release and then renew.|Это похоже на выпуск конфигурации IP с последующим обновлением.
I just go back and forth.|Я просто хожу туда-сюда.
Okay?|Ладно?
But.|Но.
Ugh.|Тьфу.
That, the [UNKNOWN] is off today.|Что, [НЕИЗВЕСТНО] сегодня выключено.
It's been off for quite a bit.|Это было не так давно.
All right anyway, so what we're gonna do is we're gonna configure the DHCP relay agent but, the way we're gonna do it is within the router.|В любом случае, хорошо, так что мы собираемся настроить агент ретрансляции DHCP, но мы будем делать это внутри маршрутизатора.
And in the router is called an IP helper address.|И в маршрутизаторе это называется вспомогательным IP-адресом.
IP helper address.|IP-адрес помощника.
Do you use this in the real world?|Вы используете это в реальном мире?
Most definitely.|Определенно.
Most definitely you will be using IP helper addresses.|Скорее всего, вы будете использовать вспомогательные IP-адреса.
Especially if you work for very large organizations.|Особенно, если вы работаете в очень крупных организациях.
They do use this particular, service.|Они действительно пользуются именно этой услугой.
Okay?|Ладно?
Instead of actually, deploying, other servers or what have you.|Вместо фактического развертывания других серверов или чего-то еще.
So we will go ahead and do the IP helper address, now in each switch already,|Итак, мы продолжим и сделаем вспомогательный IP-адрес, теперь уже в каждом коммутаторе,
the v lengths are already created, and I'll show you, I'll show you so you can see, okay, actually, I need to stop using my finger, I'll just use the mouse.|длины v уже созданы, и я покажу вам, я покажу вам, чтобы вы могли видеть, хорошо, на самом деле мне нужно перестать использовать свой палец, я просто буду использовать мышь.
Now the mouse is going crazy, that way,|Теперь мышь сходит с ума, вот так,
okay.|Ладно.
You see that it's already named and everything.|Вы видите, что он уже назван и все такое.
Now use the show VLAN and then scroll up and you can see that VLAN 10 and CLS 10 is assigned to those ports.|Теперь используйте show VLAN, а затем прокрутите вверх, и вы увидите, что этим портам назначены VLAN 10 и CLS 10.
So all switches already have their VLANs assigned.|Таким образом, всем коммутаторам уже назначены свои VLAN.
Also show int trunk.|Также покажите int trunk.
All right?|Отлично?
Port 24 is being dynamically trunked which means,|Порт 24 динамически транкинговый, что означает:
you see what it says there, automatic mode, n-802.1q, right.|вы видите, что там написано, автоматический режим, n-802.1q, верно.
So, all these VLANs are already set up that way, or the VLANs have been created,|Итак, все эти VLAN уже настроены таким образом, или VLAN были созданы,
you've assigned the VLAN to a port, and then the ports are trunked.|вы назначили VLAN порту, а затем порты объединены в транкинг.
And really what we did on this core switch.|И действительно, что мы сделали с этим переключателем ядра.
Alright?|Хорошо?
And again, we take it that way,|И снова мы так понимаем,
right there, and then we go ahead and open it up.|прямо здесь, а затем мы открываем его.
Let's take it to the top.|Давайте возьмем его наверх.
And you can do this for verification.|И вы можете сделать это для проверки.
There's your core and you can do show VNS there is VLAN 2 because VLAN 2 is the admin VLAN thus the worthy DACP server and TFCP server exist Ctrl+C and|Вот ваше ядро, и вы можете показать, что VNS есть VLAN 2, потому что VLAN 2 является административной VLAN, поэтому достойный сервер DACP и сервер TFCP существуют Ctrl + C и
then we do our show int trunk and there you see that we actually trunk the ports there and then it dynamically trunk the ports that|затем мы делаем наш show int trunk, и вы видите, что мы фактически транслируем порты туда, а затем он динамически транслирует порты,
they were directly connected to.|они были напрямую связаны с.
So trunking's important.|Так что транкинг важен.
Now, the only reason you see port 24|Теперь единственная причина, по которой вы видите порт 24
trunked right there, which is that port right, let me zoom in a little bit so you can see a little bit better.|прямо там, это тот порт, позвольте мне немного увеличить, чтобы вы могли видеть немного лучше.
Alright?|Хорошо?
The only reason that you don't see this port in there, which it is trunk is because the F zero zero is turned off.|Единственная причина, по которой вы не видите этот порт там, который является транком, заключается в том, что нулевой нулевой уровень F отключен.
So now what we need to do because the router is not configured,|Итак, что нам нужно сделать, потому что маршрутизатор не настроен,
we need to create the subinterfaces per VLAN.|нам нужно создать подынтерфейсы для каждой VLAN.
All right.|Отлично.
I'm gonna create one also for VLAN 2.|Я собираюсь создать его также для VLAN 2.
All right.|Отлично.
It's not the native VLAN.|Это не родной VLAN.
So I need to create a VLAN, VLAN 2 So I'm going to create a sub interface of VLAN 2,|Итак, мне нужно создать VLAN, VLAN 2. Итак, я собираюсь создать субинтерфейс VLAN 2,
10, 20, 30, 40, and 50, with the proper encapsulation which is dot 1Q and remember, remember, and again, we haven't gotten to the switch part yet, but again,|10, 20, 30, 40 и 50, с правильной инкапсуляцией, которая представляет собой точку 1Q, и помните, помните, и снова, мы еще не дошли до части переключателя, но опять же,
heads up, heads up, heads up, the encapsulation ID number, when you say eight o two, [UNKNOWN] dot 1Q, that number that come next, that comes next.|хедз-ап, хедз-ап, хедз-ап, номер идентификатора инкапсуляции, когда вы говорите восемь или два, [НЕИЗВЕСТНО] точка 1Q, то число, которое будет следующим, оно будет следующим.
Must match the VLAN ID.|Должен соответствовать идентификатору VLAN.
So if it's ten, it's ten.|Так что если десять, то десять.
If it's twenty, it's twenty.|Если двадцать, то двадцать.
If it's thirty, thirty, and so forth.|Если тридцать, тридцать и так далее.
All right?|Отлично?
And then we put in the IP addresses for each one.|И затем мы вводим IP-адреса для каждого из них.
So let's set this up where we can see the IP scheme for it.|Итак, давайте настроим это так, чтобы мы могли видеть схему IP для него.
Cause, and we'll take our time with it, because we don't want to make silly mistakes.|Потому что, и мы не торопимся, потому что не хотим делать глупых ошибок.
Now, what is it you need to know?|Что вам нужно знать?
They may ask you what a, what is IP helper address?|Они могут спросить вас, что такое вспомогательный IP-адрес?
What is it used for?|Для чего его используют?
And really that would be about it.|И действительно об этом.
Okay.|Ладно.
That would be about it.|Вот бы об этом.
You will now be configuring the ACP like we did in the previous,|Теперь вы будете настраивать ACP, как мы делали в предыдущем,
lab that we just did.|лабораторию, которую мы только что сделали.
Previous lecture.|Предыдущая лекция.
And you're not gonna be configuring IP helper but you may be asked a question on what the IP helper address does.|И вы не собираетесь настраивать вспомогательный IP-адрес, но вам может быть задан вопрос о том, что делает вспомогательный IP-адрес.
So now you'll see what it does.|Итак, теперь вы увидите, что он делает.
Right now you saw they're, they're not being assigned an address and we'll take it a step at a time so you can see even though the ports were up|Прямо сейчас вы видели, что им не назначается адрес, и мы будем делать это постепенно, чтобы вы могли видеть, даже если порты были задействованы.
it reconfigured inter VLAN routing.|он перенастроил маршрутизацию между VLAN.
Now I'm gonna go through it quickly because again,|Теперь я быстро пройду через это, потому что снова,
we are not into switching yet.|мы еще не перешли.
When we get to switching you will learn how to do all of that.|Когда мы перейдем к переключению, вы научитесь все это делать.
But, to show you that they're still not going to get assigned an IP address.|Но, чтобы показать вам, что им все еще не назначат IP-адрес.
Until you put this IP helper address,|Пока вы не укажете этот вспомогательный IP-адрес,
okay?|Ладно?
I'm gonna go enable, config T Interface F0/0.|Я собираюсь включить, настроить T Interface F0 / 0.
Just gonna do a no shut on the physical interface.|Просто отключу физический интерфейс.
Create my first subinterface which is .2,|Создайте свой первый подинтерфейс .2,
is because, it's the admin VLAN.|потому что это административная VLAN.
I just did dot two, just to match that,|Я просто поставил точку два, просто чтобы соответствовать этому,
that's all.|вот и все.
dot one, sorry.|поставьте точку один, извините.
ENCAP, DOT1Q 2.|ENCAP, DOT1Q 2.
That's the match.|Это совпадение.
And then the IP address for that is, what?|И тогда какой IP-адрес?
[BLANK_AUDIO]|[BLANK_AUDIO]
It's 10.100.0.254.|Это 10.100.0.254.
10.0.100.0.254.|10.0.100.0.254.
And then 255.255.255.|А потом 255.255.255.
We're using a twenty seven so that's a two two four.|Мы используем двадцать семь, так что это два два четыре.
Be careful.|Быть осторожен.
Alright?|Хорошо?
Now that we did [UNKNOWN]|Теперь, когда мы сделали [НЕИЗВЕСТНО]
zero two the rest pretty are.|ноль два остальные довольно хороши.
Pretty easy.|Очень легко.
All you gotta do is up arrow.|Все, что вам нужно сделать, это стрелка вверх.
All right.|Отлично.
So what we're gonna do now for VLAN 10 and VLAN 10, which is the top one right there.|Итак, что мы собираемся делать сейчас для VLAN 10 и VLAN 10, которые сейчас являются верхними.
Let me move this up a little bit here so you can see all of them right there.|Позвольте мне немного поднять это здесь, чтобы вы могли увидеть их все прямо здесь.
Let's get the router back in the picture here.|Вернемся к маршрутизатору, изображенному на картинке.
So you're gonna do up arrow, up arrow, up arrow til I get to the sub interface.|Итак, вы будете использовать стрелку вверх, стрелку вверх, стрелку вверх, пока я не доберусь до вспомогательного интерфейса.
I'm gonna sub interface 10.|Я собираюсь подинтерфейс 10.
Go to the encapsulation, change it to ten.|Переходим в инкапсуляцию, меняем на десять.
The IP address is the gateway right?|IP-адрес - это шлюз, верно?
So we are subnetting.|Итак, мы разбиваем на подсети.
Sixty four is the next network.|Шестьдесят четыре - это следующая сеть.
One less, sixty three.|На один меньше, шестьдесят три.
Sixty two is the, gateway, alright?|Шестьдесят два, шлюз, хорошо?
You see how quickly we can do that?|Вы видите, как быстро мы можем это сделать?
So I'm just gonna up, IP, there we go.|Так что я просто пойду, IP, поехали.
So, it's going to be, what did I say?|Итак, это будет, что я сказал?
Oh.|Ой.
I made a mistake in the first one.|Я ошибся в первом.
Okay.|Ладно.
It's zero.|Это ноль.
All last.|Все последнее.
Did I?|Я?
Did I?|Я?
No, I did not.|Нет, я не.
Hold on.|Оставайтесь на линии.
Let me check before I continue.|Позвольте мне проверить, прежде чем я продолжу.
You see Ok zero zeros [INAUDIBLE] zero an hour so we're fine we're fine yeah zero zero fifty four okay, we're good.|Вы видите: Хорошо, ноль, нули [НЕРАЗБОРЧИВО], ноль в час, так что все в порядке, мы в порядке, да, ноль, ноль, пятьдесят четыре, хорошо, все в порядке.
So we're in the last octet so.|Итак, мы находимся в последнем октете.
So it can be two fifty four.|Так что может быть два пятьдесят четыре.
So it can not be two fifty four.|Так что не может быть два пятьдесят четыре.
It has to be thirty, for VLAN 2 so what we're going to do, we're going to erase all of this.|Для VLAN 2 должно быть тридцать, так что то, что мы собираемся сделать, мы собираемся стереть.
Ctrl+E and go to the end.|Ctrl + E и идти до конца.
I'm going to go to sub interface 2 and I'm going to put the change the IP address.|Я собираюсь перейти к субинтерфейсу 2, и я собираюсь изменить IP-адрес.
Sorry 10.100.0.30.|Извините 10.100.0.30.
255.255.255.224,|255.255.255.224,
there.|там.
What I did was, again, for some reason, I see the zero in the third octet,|Я снова по какой-то причине вижу ноль в третьем октете,
I don't know why I decided to do that.|Не знаю, почему я решил это сделать.
It's not a two fifty four.|Это не два пятьдесят четыре.
It's in the zero network but we have a twenty seven.|Он находится в нулевой сети, но у нас есть двадцать семь.
Right?|Правильно?
If the next network's thirty two,|Если в следующей сети тридцать два,
one less is thirty one, the gateway's thirty, not two fifty four.|На один меньше тридцать один, у ворот тридцать, а не два пятьдесят четыре.
So be very careful.|Так что будьте очень осторожны.
Be very, very careful.|Будьте очень-очень осторожны.
And then learn all about it again to the sub interface which is already created, really.|А затем узнайте все об этом снова в субинтерфейсе, который на самом деле уже создан.
F 0.10 then we're gonna do the end cap,|F 0.10, тогда мы сделаем заглушку,
which is ten.|что десять.
Oops.|Ой.
Not there.|Не там.
End cap, end cap, there it is.|Заглушка, заглушка, вот она.
End cap ten.|Заглушка десять.
All right.|Отлично.
For VLAN 10.|Для VLAN 10.
And then the IP address would be sixty two.|И тогда IP-адрес будет шестьдесят два.
And just so you know where I'm getting these numbers from okay?|И ты просто знаешь, откуда я беру эти цифры, ладно?
You see that the network here is 32 for VLAN 10.|Вы видите, что сеть здесь 32 для VLAN 10.
The next network, 64.|Следующая сеть, 64.
One less 64 is 63 which is the broadcast.|На одно меньше 64 - это 63, что является трансляцией.
One less that is 62 which is 32's network gateways.|На один меньше, это 62, что составляет 32 сетевых шлюза.
Alright?|Хорошо?
Last available IP address.|Последний доступный IP-адрес.
That's what I like to use always for the gateways.|Это то, что я всегда использую для шлюзов.
So that's done with ten, so we go to b line twenty so the sub interface.|Итак, с десятью сделано, поэтому мы переходим к двадцатой строке b, то есть к вспомогательному интерфейсу.
20.|20.
dot 1 Q.|точка 1 Q.
20.|20.
And then what IP address am I gonna use?|И тогда какой IP-адрес я собираюсь использовать?
Well, the next network is 96.|Ну следующая сеть 96.
One less is 95, which is the broadcast,|На один меньше - 95, это трансляция,
one less than that is 94, so therefore,|на один меньше - 94, поэтому
it's 94.|это 94.
[BLANK_AUDIO]|[BLANK_AUDIO]
Done deal.|Сделка сделана.
Then we're going to go up there and do 30.|Затем мы собираемся пойти туда и сделать 30.
Sub interface 30.|Дополнительный интерфейс 30.
And then we're going to go ahead and do the dot one Q 30 and then the IP address.|И затем мы продолжим и сделаем точку один Q 30, а затем IP-адрес.
What is the IP address?|Какой IP-адрес?
Well we're in the 96th network one after that is 120,|Что ж, мы в 96-й сети, после 120,
one is 126, so that will be 126.|один - 126, значит, будет 126.
Enter.|Войти.
Okay?|Ладно?
We good?|Мы хороши?
All right.|Отлично.
And then we do 40.|А потом делаем 40.
So, sub interface 40.|Итак, субинтерфейс 40.
And O pairing dot one Q.|И O соединяет точку один Q.
40.|40.
And then what IP address am I going to use?|И тогда какой IP-адрес я собираюсь использовать?
Well 40 is the 128, the next one below is 160.|Скважина 40 - это 128, следующая ниже - 160.
One less is 159 so 158 would be the IP address that's available.|На единицу меньше - 159, поэтому доступным IP-адресом будет 158.
Alright, and now we go to the fifties of interface.|Хорошо, а теперь мы переходим к интерфейсу пятидесятых годов.
And then we blue the one Q 50 and then the IP address would be, well let's see,|И затем мы синий Q 50, а затем IP-адрес будет, ну, давайте посмотрим,
if we're incrementing by 32,|если мы увеличиваем на 32,
the next one would be 192, one less 192 is 191 which is the broadcast, one less that,|следующий будет 192, на один меньше 192 это 191, который является трансляцией, на один меньше,
is 190 I sound like a guy who's, what do you call those guys, auctioneers?|190 Я звучу как парень, который, как вы называете этих парней, аукционисты?
190, 190, 190, 190.|190, 190, 190, 190.
Okay, 190.|Хорошо, 190.
All right, so I'll do a control-z, and let's bring the router this way.|Хорошо, я сделаю control-z, и давайте перенесем маршрутизатор сюда.
A little bit more okay, you guys can see that.|Еще немного, ладно, вы, ребята, это видите.
Good, good, good.|Хорошо, хорошо, хорошо.
I'll do a show IP, well, let's copy first.|Сделаю шоу IP, ну давайте сначала скопируем.
Shortcut WR, instead of copy on the start.|Ярлык WR вместо копирования на старте.
I'm gonna do a show IP INT BRIEF.|Я собираюсь устроить шоу IP INT BRIEF.
All right, what I wanna do is one of the things I'm looking at It's obviously that all my interfaces are up, up, which they are.|Хорошо, то, что я хочу сделать, это одна из вещей, на которую я смотрю. Очевидно, что все мои интерфейсы работают, работают, что и есть.
I'm also looking to make sure that the gateways are correct.|Я также хочу убедиться, что шлюзы правильные.
So, I do have 30, 62, 94, 126, 158, 190.|Итак, у меня есть 30, 62, 94, 126, 158, 190.
I just verify from what I have right there.|Я просто проверяю то, что у меня есть прямо сейчас.
You see, VLAN 10 is 32,|Видите ли, VLAN 10 - это 32,
VLAN two, is zero, so,|VLAN два, равно нулю, поэтому
one less 32 is 31.|на один меньше 32 - это 31.
One less that is 30, that's VLAN two and so forth.|На один меньше 30, это два VLAN и так далее.
Alright, so we're, we're good to go we're following the correct order.|Хорошо, мы в порядке, мы следуем правильному порядку.
Now we should have.|Теперь у нас должно быть.
Inter VLAN connectivity.|Связь между VLAN.
Alright, we do show IP route.|Хорошо, мы показываем IP-маршрут.
Shows that we're connected directly right through our routing table to all these particular interfaces.|Показывает, что мы напрямую подключены через нашу таблицу маршрутизации ко всем этим конкретным интерфейсам.
But when we go over here we're still not getting an IP address assigned to us.|Но когда мы идем сюда, мы все еще не получаем назначенный нам IP-адрес.
From the DACP server.|С сервера DACP.
We're still not gonna get a sign because again by default the DACP server will deny broadcast.|Мы по-прежнему не получим сигнала, потому что снова по умолчанию сервер DACP отклоняет трансляцию.
So what do you do?|Ну так что ты делаешь?
You go inside each one of those sub-interfaces, and you're gonna put the IP helper address,|Вы заходите внутрь каждого из этих субинтерфейсов и помещаете вспомогательный IP-адрес,
all right.|отлично.
Which is the IP address of the DACP server, so the IP address or the DACP server is 10.100 0.1, okay?|Какой IP-адрес сервера DACP, значит, IP-адрес или сервер DACP - 10.100 0,1, хорошо?
So we're gonna go to config T,|Итак, мы переходим к настройке T,
we're gonna go to the first sub interface,|мы перейдем к первому подчиненному интерфейсу,
which is F 0 10.|что F 0 10.
INT F 0/0 Not ten.|INT F 0/0 Не десять.
And we're gonna go IP, helper, hyphen,|И мы пойдем IP, помощник, дефис,
address, 10.100.0.1.|адрес, 10.100.0.1.
Almost there, right?|Почти готово, правда?
Now everybody saw.|Теперь все увидели.
And then hit Enter.|А затем нажмите Enter.
And then you're gonna up arrow.|И тогда ты пойдешь стрелкой вверх.
Make life easy.|Сделайте жизнь проще.
20.|20.
Enter all barrel IP helper address same one your pointing to the DACP server and then your going to go 30 for the sub interface and|Введите весь вспомогательный IP-адрес ствола, совпадающий с тем, который вы указываете на сервер DACP, а затем вы собираетесь пойти 30 для вспомогательного интерфейса и
then the same helper address 40 helper address and then 50 And then helper address, all right?|затем тот же адрес помощника 40 адрес помощника, а затем 50 И затем адрес помощника, хорошо?
DO WR Ctrl+Z know all these commands DO WR,|DO WR Ctrl + Z знаю все эти команды DO WR,
Ctrl+Z might not work on your exam, okay?|Ctrl + Z может не работать на вашем экзамене, понятно?
So you have to exit, exit, copy, run,|Итак, вам нужно выйти, выйти, скопировать, запустить,
start and then what I'm going to do is I'm going to do a show start, cause I want to see exactly what I have inside each of my|начать, а затем я собираюсь начать шоу, потому что я хочу точно увидеть, что у меня внутри каждого из моих
sub inter faces.|суб интерфейсы.
So, I didn't put an IP helper address under the admin VLAN,|Итак, я не помещал вспомогательный IP-адрес в VLAN администратора,
because they're statically assigned.|потому что они назначены статически.
But and they're within the same VLAN, so they don't need one.|Но они находятся в одной VLAN, поэтому они не нужны.
But definitely under the other VLANs, the IP helper address needs to be in there,|Но определенно в других VLAN должен быть вспомогательный IP-адрес,
and you can see that it is.|и вы можете видеть, что это так.
So let's take a look now and see if we are receiving an IP address from the DACP server, a correct IP address for the scope that I'm in.|Итак, давайте посмотрим, получаем ли мы IP-адрес от сервера DACP, правильный IP-адрес для области, в которой я нахожусь.
Boom, there it is.|Бум, вот оно.
10.100.0.33.|10.100.0.33.
I'm in the 32 network, outstanding.|Я в сети 32, выдающийся.
We have that going there, we're gonna go now to the 64, should be 65.|У нас это есть, мы собираемся перейти на 64, должно быть 65.
And I am getting a 65 let me just put that over there it says 65|И я получаю 65, позвольте мне просто поставить это там, где написано 65
with a 224 alright the right gateway assigned outstanding and then we got 96 should be 97 and that's what we got 97,|с 224 хорошо, правильный шлюз назначен выдающимся, а затем мы получили 96, должно быть 97, и это то, что мы получили 97,
224 mask 126 gateway and then the 128.|224 маска 126 шлюз, а затем 128.
You see that?|Ты видишь это?
129, first available mask.|129, первая доступная маска.
Gateway address.|Адрес шлюза.
[BLANK_AUDIO]|[BLANK_AUDIO]
And then the last one should be 161 and then again we have 190.|И тогда последним должно быть 161, а потом снова 190.
So IP helper-address to the rescue.|Так что на помощь приходит IP-адрес-помощник.
When we're actually using a Microsoft server, let's say.|Скажем, когда мы на самом деле используем сервер Microsoft.
This is mimicking a Microsoft server.|Это имитирует сервер Microsoft.
And we're going across VLANs which means we're going across broadcast domains.|И мы проходим через VLAN, что означает, что мы проходим через широковещательные домены.
It could be within the same building.|Это могло быть в том же здании.
So you could use that IP helper address to allow you,|Таким образом, вы можете использовать этот вспомогательный IP-адрес, чтобы позволить вам,
to assign all these VLAN, all these IP addresses dynamically per VLAN, per VLAN.|чтобы назначить все эти VLAN, все эти IP-адреса динамически для каждой VLAN, для каждой VLAN.
So there we go.|Итак, поехали.
Previous lesson very basic DACP.|Предыдущий урок очень простой DACP.
Now you have an actual DACP server but you're using the relay agent of Cisco which is the IP helper address.|Теперь у вас есть реальный сервер DACP, но вы используете агент ретрансляции Cisco, который является вспомогательным IP-адресом.
To allow you or to help you assign our cross broadcast domain.|Чтобы позволить вам или помочь вам назначить наш домен перекрестной трансляции.
We'll see you in the next lecture.|Увидимся на следующей лекции.
[BLANK_AUDIO]|[BLANK_AUDIO]