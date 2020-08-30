D:\mailCloud\prjother\tmp\1\c96_Extended ACL's.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
Welcome back everyone, it is time now to do our extended access list.|С возвращением, пришло время сделать наш расширенный список доступа.
Now this lab obviously I took I took this from the book and is almost an exact replica,|Очевидно, что я взял эту лабораторную работу, я взял это из книги и представляет собой почти точную копию,
something that you may see in your certification, all right?|то, что вы можете увидеть в своем сертификате, хорошо?
The way that it was written, is m,|Как это было написано, это m,
trying to make you think, all right?|пытаюсь заставить вас думать, ладно?
So first, we're gonna talk about extended access lists.|Итак, сначала мы поговорим о расширенных списках доступа.
And then, we're actually gonna create it.|А потом мы его создадим.
All right?|Отлично?
Now, extended access lists,|Теперь расширенные списки доступа,
also numbered access lists, have a range.|также нумерованные списки доступа, имеют диапазон.
So, when you see an access list being written,|Итак, когда вы видите, что список доступа записывается,
if you see a number from 100 to 199, you know, that's an extended access list.|если вы видите число от 100 до 199, значит, это расширенный список доступа.
And at an extended access list you can place it nearest the source.|А в расширенном списке доступа вы можете разместить его ближе всего к источнику.
Why can you place it nearest the source?|Почему вы можете разместить его ближе всего к источнику?
And, I'll move out of the way so you can see it now, because I know I'm in your way.|И я отойду с дороги, чтобы вы могли это увидеть сейчас, потому что я знаю, что мешаю вам.
You can, because you can use source.|Вы можете, потому что вы можете использовать source.
Oh, let's do it correctly.|Ой, давайте сделаем это правильно.
You can use protocols.|Вы можете использовать протоколы.
You can use source and destination addresses,|Вы можете использовать адреса источника и назначения,
important numbers.|важные числа.
So you can be very specific as to what you wanna do.|Таким образом, вы можете очень четко указать, чем вы хотите заниматься.
Hey, I wanna block this guy using this protocol from this individual,|Эй, я хочу заблокировать этого парня, использующего этот протокол, от этого человека,
all right, using this port number.|хорошо, используя этот номер порта.
So you're very specific on what is it that you wanna block.|Итак, вы очень четко указываете, что именно вы хотите заблокировать.
Do you wanna block port 80, do you wanna block 23, 22.|Вы хотите заблокировать порт 80, вы хотите заблокировать 23, 22.
Basically Telnet, Ssh, WWW or whatever protocol it is that you want to block,|Обычно Telnet, Ssh, WWW или любой другой протокол, который вы хотите заблокировать,
you can use an extended access list to do so.|для этого вы можете использовать расширенный список доступа.
Okay?|Ладно?
So they're very very very flexible.|Так что они очень-очень-очень гибкие.
Now your book states you can do it nearest the source.|Теперь в вашей книге сказано, что вы можете сделать это ближе всего к источнику.
And it makes sense.|И это имеет смысл.
It makes sense because why would you want your router to process any packet if it's going to be denied anyway?|Это имеет смысл, потому что зачем вам нужно, чтобы ваш маршрутизатор обрабатывал любой пакет, если он все равно будет отклонен?
So I might as well just block it at the source if it's gonna get denied.|Так что я мог бы просто заблокировать его у источника, если он будет отклонен.
Boom, drop it right then and there.|Бум, брось это прямо сейчас.
Your router doesn't have to do any processing, no overhead on the router,|Ваш маршрутизатор не должен выполнять никакой обработки, никаких накладных расходов на маршрутизатор,
no bandwidth being taken up trying to go across, so it's a lot more feasible.|пропускная способность не используется, поэтому это намного более осуществимо.
Now, in the example in the background.|Теперь в примере на заднем плане.
And again, I've told you, I'm taking this example from the book.|И снова, как я уже говорил, я беру этот пример из книги.
We have a web server.|У нас есть веб-сервер.
Let's say this web server right there.|Скажем прямо здесь этот веб-сервер.
And, this is what I want or what's written.|И это то, что я хочу или что написано.
All right.|Отлично.
Let's say, let's pick PC0.|Допустим, возьмем PC0.
PC0 is the only PC that should have web access.|PC0 - единственный компьютер, на котором должен быть доступ в Интернет.
And, let's write that down.|И давайте это запишем.
So, we don't forget cuz you'll probably forget in five minutes.|Итак, мы не забываем, потому что вы, вероятно, забудете через пять минут.
I know, I would.|Я знаю, что хотел бы.
All right, so PC0.|Хорошо, так что PC0.
There's, there's some spaces here.|Здесь есть места.
PC0 is the only PC to have web access to the web server.|PC0 - единственный компьютер, имеющий веб-доступ к веб-серверу.
That's the only one.|Это единственное.
Everyone else should be denied web access to the web server.|Всем остальным должно быть отказано в доступе к веб-серверу.
All other traffic is allowed.|Весь остальной трафик разрешен.
Okay.|Ладно.
So we need to create an access list that states that, hey, only this guy right here should be able to use the browser to get|Итак, нам нужно создать список доступа, в котором указано, что, эй, только этот парень может использовать браузер для получения
to this particular web server.|на этот конкретный веб-сервер.
Nobody else should be allowed to use that browser to get to this web server.|Никому не должно быть разрешено использовать этот браузер для доступа к этому веб-серверу.
They can ping it.|Они могут это пинговать.
They can telnet it.|Они могут это сделать по телнету.
They can go through a share.|Они могут пройти через акцию.
They can remote desktop.|Они могут удаленный рабочий стол.
They can do anything else but they cannot use port 80.|Они могут делать что угодно, но не могут использовать порт 80.
That's what they can't use.|Вот что они не могут использовать.
That's what the, that's what the, that's saying.|Вот что, вот что, это говорит.
All right?|Отлично?
Cuz everything else is okay but not port 80.|Потому что все остальное в порядке, но не порт 80.
All right, we only have one router.|Хорошо, у нас только один роутер.
So we know we gotta create the access list there.|Итак, мы знаем, что нам нужно создать там список доступа.
Now according to your book, the access list,|Теперь, согласно вашей книге, список доступа,
extended access list is placed nearest the source.|расширенный список доступа располагается ближе всего к источнику.
So nearest the source would be the f0/0|Таким образом, ближайшим к источнику будет f0 / 0
interface right there.|интерфейс прямо здесь.
And the direction would be going in to the router.|И направление будет идти к маршрутизатору.
That's what we read in our chapters.|Об этом мы читаем в наших главах.
So according to the book, hey, that's the way it's supposed to be.|Итак, согласно книге, эй, так и должно быть.
But Cisco's warning you to think.|Но Cisco предупреждает вас подумать.
One of the statements says everybody else is denied web access to this guy.|В одном из заявлений говорится, что всем остальным отказано в доступе к этому парню.
Well, for whatever reason,|Ну по какой-то причине
whatever mental block we have, we always choose to ignore this.|какой бы ментальный блок мы ни имели, мы всегда предпочитаем игнорировать это.
we just think that's just a cloud sitting out there, it's nothing.|мы просто думаем, что это просто облако, это ничего.
We only pay attention to the PCs and things that we see like that well that's a mistake because if you were to do that and|Мы обращаем внимание только на компьютеры и вещи, которые мы так хорошо видим, это ошибка, потому что если бы вы сделали это и
you were to apply it to that interface going in You would be dead wrong.|вы должны были применить его к входящему в него интерфейсу. Вы были бы совершенно неправы.
Because you would definitely, it would affect everybody over here.|Потому что ты определенно повлиял бы на всех здесь.
It would definitely affect everybody there.|Это определенно коснется всех там.
But it wouldn't affect anybody that's sitting over here.|Но это не коснется никого, кто сидит здесь.
Because they're not going through that interface are they.|Потому что они не проходят через этот интерфейс.
They're coming through this interface, and then they'll be in the router, and then they'll go out this interface and do whatever it is that they wanna do.|Они проходят через этот интерфейс, а затем они будут в маршрутизаторе, а затем они выйдут из этого интерфейса и будут делать все, что хотят.
So they're making you think, all right.|Итак, они заставляют вас думать, хорошо.
I got other connections on this router, so I need to put, or I need to apply the access list to the funnel.|У меня есть другие подключения на этом роутере, поэтому мне нужно поставить, или мне нужно применить список доступа к воронке.
Where all these packets are coming through, where they gotta get through that interface right there, right, this f0/1|Где все эти пакеты проходят, где они должны пройти через этот интерфейс прямо здесь, верно, это f0 / 1
going out, right?|выходишь, да?
So we need to make sure that where all this information wherever it's coming from, that is, it's going down that interface.|Итак, нам нужно убедиться, что откуда вся эта информация, откуда бы она ни поступала, то есть она попадает в этот интерфейс.
That is where those packets need to confront that access list.|Вот где эти пакеты должны противостоять этому списку доступа.
So they can be either permitted or denied.|Так что их можно разрешить или запретить.
All right, so let's, let's give it a go.|Хорошо, давай, попробуем.
Shall we first?|Мы сначала?
Let's, let's check to make sure we have IPs.|Давайте, давайте проверим, есть ли у нас IP.
All right?|Отлично?
And there's an IP here.|И здесь IP.
Yeah, 100.1.|Ага, 100,1.
Gateway's 254, obviously.|Очевидно, у Gateway 254.
This is 100.2.|Это 100,2.
This is 100.3.|Это 100,3.
Okay?|Ладно?
The web server is 1.1.1.1.|Веб-сервер - 1.1.1.1.
Gateway is 1.1.1.254.|Шлюз - 1.1.1.254.
All right.|Отлично.
All right.|Отлично.
So let's see.|Так что посмотрим.
Let's see if we have connectivity to the web server through the browser.|Посмотрим, есть ли у нас подключение к веб-серверу через браузер.
All right?|Отлично?
1.1.1.1 Oh and I know with the,|1.1.1.1 Да, и я знаю, что
I know with this new packet tracer or am I using the NS?|Я знаю с этим новым трассировщиком пакетов или я использую NS?
I should be able to.|Я должен быть в состоянии.
I should be able to get it through the IP address 101.0.1.0.1.|Я должен получить его через IP-адрес 101.0.1.0.1.
Okay, he got there.|Хорошо, он туда попал.
Let's get over here.|Пойдем сюда.
I'm not really gonna configure DNS.|Я не собираюсь настраивать DNS.
It's basically, hey can I use the browser?|По сути, я могу использовать браузер?
HTTP right?|HTTP правильно?
Port 80.|Порт 80.
Come on now Mr. Arp.|Давай, мистер Арп.
Request timeout.|Тайм-аут запроса.
Okay.|Ладно.
I think I know the reason why to that.|Думаю, я знаю причину этого.
Maybe this is already pre-configured,|Возможно, это уже предварительно настроено,
and I didn't get rid of what I should have gotten rid of.|и я не избавился от того, от чего должен был избавиться.
So what I'll do is the following.|Итак, я сделаю следующее.
All right.|Отлично.
I'm just gonna erase it and reload it.|Я просто сотру и перезагружу.
To make sure because everybody should have web access.|Чтобы убедиться, потому что у всех должен быть доступ в Интернет.
I just put the IPs back on the interfaces.|Я просто вставил IP обратно в интерфейсы.
Once the router comes back up.|Как только роутер снова включится.
Everybody should have web access to it.|Каждый должен иметь к нему доступ в Интернете.
You won't actually put the accesses on there.|Вы фактически не будете помещать туда доступ.
But you really gotta be careful.|Но тебе действительно нужно быть осторожным.
Cuz, again, Cisco's now wanting not just hey.|Потому что, опять же, Cisco хочет не только «привет».
Well, the book said this.|Что ж, в книге это сказано.
I'm gonna do this.|Я сделаю это.
I'm gonna do that.|Я сделаю это.
Because when you get out there.|Потому что, когда ты выйдешь отсюда.
All right?|Отлично?
You're gonna have to start thinking.|Тебе придется начать думать.
You're gonna have to start applying these concepts to where your, your job is.|Вам придется начать применять эти концепции там, где ваша, ваша работа.
So okay, I know extended access is, gives me the flexibility to be able to block ports and use different protocols and destination addresses.|Хорошо, я знаю, что расширенный доступ дает мне возможность блокировать порты и использовать разные протоколы и адреса назначения.
So it gives me more flexibility to do things.|Так что это дает мне больше свободы действий.
The logic of it, okay, where could I apply it?|Логика этого, хорошо, где я могу это применить?
Where should I apply it?|Где мне это применить?
What should I block?|Что я должен заблокировать?
You know, how many lines is it gonna take?|Знаешь, сколько строк это займет?
So these are the things you need to think about.|Вот о чем вам нужно подумать.
So let's go ahead and go in the router.|Итак, давайте перейдем к роутеру.
Okay.|Ладно.
And enable interface f0/0.|И включите интерфейс f0 / 0.
FAT will help int f0/0.|FAT поможет int f0 / 0.
IP address, 192.168.1.254.|IP-адрес 192.168.1.254.
255, 255, 255.0.|255, 255, 255.0.
No shut.|Нет, заткнись.
And then, the other one is f01.|А потом еще один - f01.
The IP address there is 1.1.1.254,|Там IP-адрес 1.1.1.254,
255.255.255.0 Shut,|255.255.255.0 Закрыто,
do WR, Ctrll+Z.|сделать WR, Ctrl + Z.
Just putting IP address on the interfaces,|Просто поместив IP-адрес в интерфейсы,
no big deal.|ничего страшного.
Show IP Int Brief.|Показать IP Int Brief.
All right, okay, we're up, up.|Хорошо, хорошо, мы встали, встали.
All right.|Отлично.
So let's try our little test again.|Итак, давайте снова попробуем наш небольшой тест.
We know that the first one was able to make it.|Мы знаем, что это удалось первому.
So, 101010101.|Итак, 101010101.
Request time out.|Тайм-аут запроса.
Lovely.|Прекрасно.
[BLANK_AUDIO]|[BLANK_AUDIO]
[SOUND] Turn this on, just because, okay?|[ЗВУК] Включите это просто потому, что, хорошо?
[BLANK_AUDIO]|[BLANK_AUDIO]
Stop, let's try again 1.1.1.1 really okay ping 192.168.1.254|Стоп, попробуем еще раз 1.1.1.1 действительно хорошо пинг 192.168.1.254
[BLANK_AUDIO]|[BLANK_AUDIO]
Oh.|Ой.
Yes.|Да.
That would definitely.|Это определенно будет.
So, okay.|Так хорошо.
No problems.|Без проблем.
I see the problemo.|Я вижу проблему.
Okay.|Ладно.
I see the problem.|Я вижу проблему.
So let me go back to interface f0/0.|Итак, позвольте мне вернуться к интерфейсу f0 / 0.
It's not 1 but 100.|Не 1, а 100.
Interface f0/0 and you just put the IP address over it.|Интерфейс f0 / 0, и вы просто помещаете IP-адрес поверх него.
It will override it.|Это отменит это.
192.168.100.254, 255.255.255.0, do WR,|192.168.100.254, 255.255.255.0, делать WR,
Ctrl+Z.|Ctrl + Z.
Show IP in brief.|Покажите кратко IP.
Even though it told me up before, it will tell me up again.|Хотя он сказал мне раньше, он скажет мне снова.
All right, so let's try this one more time.|Хорошо, давай попробуем еще раз.
1.1.1.1.|1.1.1.1.
There it is.|Вот оно.
[BLANK_AUDIO]|[BLANK_AUDIO]
Let's close it, let's reopen it.|Давайте закроем, давайте снова откроем.
Clear that cache, right?|Очистить кеш, верно?
1.1.1.1.|1.1.1.1.
There it is.|Вот оно.
And then [BLANK_AUDIO]|А затем [BLANK_AUDIO]
1.1.1.1.|1.1.1.1.
So everybody has web access to that particular web server that shouldn't be, right?|Итак, у каждого есть веб-доступ к этому конкретному веб-серверу, которого не должно быть, верно?
So now we're going to develop an extended access list.|Итак, теперь мы собираемся разработать расширенный список доступа.
That actually does what is required.|Это действительно то, что требуется.
So, PC0, let's do it step by step.|Итак, PC0, давайте сделаем это шаг за шагом.
PC0 is the only PC to have web access to web server.|PC0 - единственный компьютер, имеющий веб-доступ к веб-серверу.
Okay.|Ладно.
And it's an extended access list.|И это расширенный список доступа.
Anytime you see something that states, you know, you must permit or deny SSH or Telnet or RDP or any particular port you know you're doing an extended|Каждый раз, когда вы видите что-то, что гласит, вы должны разрешить или запретить SSH, Telnet или RDP или любой конкретный порт, который, как вы знаете, вы делаете расширенный
access list, an extended access list.|список доступа, расширенный список доступа.
So, access list.|Итак, список доступа.
Again, you pick one from the range of numbers.|Опять же, вы выбираете один из диапазона чисел.
100, that's A.|100, это А.
Permit Host and that's 192.168.100.1|Разрешите хост и это 192.168.100.1
to host 1.1.1.1,|на хост 1.1.1.1,
that equals port 80.|что равно порту 80.
You're saying that, hey, PC 192.168.100.1,|Вы говорите, эй, ПК 192.168.100.1,
oh, I forgot something.|о, я кое-что забыл.
Permit the TCP because the, when you put port 80 and you look at your access it actually puts that EQ.|Разрешите TCP, потому что, когда вы устанавливаете порт 80 и смотрите на свой доступ, он фактически устанавливает этот EQ.
That 80 turns into a WWW.|Эти 80 превращаются в WWW.
So that port is part of the TCP protocol,|Итак, этот порт является частью протокола TCP,
so that's why you put TCP.|так вот почему вы ставите ПТС.
Access 100 permit TCP.|Доступ 100 разрешает TCP.
That protocol, from this source, this source address right here.|Этот протокол, из этого источника, этот адрес источника прямо здесь.
[BLANK_AUDIO]|[BLANK_AUDIO]
Okay, to this destination.|Хорошо, в это место.
[BLANK_AUDIO]|[BLANK_AUDIO]
Using that port number.|Используя этот номер порта.
So you are allowing that particular PC to do that.|Таким образом, вы позволяете это делать конкретному компьютеру.
Everybody else is denied that port.|Всем остальным этот порт не разрешен.
Access-list 100,|Список доступа 100,
denying TCP any source,|запретить TCP любой источник,
any source to host 1.1.1.1|любой источник для хоста 1.1.1.1
if they're using port 80.|если они используют порт 80.
By putting this any, you're saying anybody, any source.|Помещая это как угодно, вы говорите кому угодно, из любого источника.
Anybody from anywhere trying to get to it by using port 80 is gonna be denied if they're trying to get to that particular web server.|Кому-либо из любого места, пытающемуся получить к нему доступ через порт 80, будет отказано, если он попытается добраться до этого конкретного веб-сервера.
And the last one.|И последний.
It's just the most general.|Это просто самое общее.
Access-List.|Список доступа.
100 PERMIT IP,|100 РАЗРЕШЕНИЕ IP,
the rest of the IP suites.|остальные комплекты IP.
[COUGH] Any source, any destination.|[КАШЕ] Любой источник, любое место назначения.
That is your access list right there.|Вот ваш список доступа.
That is your access list right there.|Вот ваш список доступа.
Let me move this a little bit this way there, so ACCESS-LIST 100,|Позвольте мне переместить это немного сюда, поэтому ACCESS-LIST 100,
you gotta make sure, right?|ты должен убедиться, правда?
They're all within the same numbered access list,|Все они находятся в одном пронумерованном списке доступа,
most specific on top cuz you're permitting that particular host, to that particular host source destination, source destination, port number.|наиболее конкретный наверху, потому что вы разрешаете этот конкретный хост для этого конкретного назначения источника хоста, назначения источника, номера порта.
Here, we're denying TCP, any source,|Здесь мы отвергаем TCP, любой источник,
any source to that destination if they're using that port and then ACCESS-100 PERMIT the rest of the IP you can ping,|любой источник в этот пункт назначения, если они используют этот порт, а затем ACCESS-100 РАЗРЕШИТЬ остальной IP-адрес, который вы можете проверить,
telnet do whatever from any source any destination, that is what that means.|telnet делает что угодно из любого источника в любое место назначения, вот что это значит.
So let's go ahead and do so.|Так что давайте продолжим и сделаем это.
[BLANK AUDIO].|[ПУСТОЙ АУДИО].
Wanna copy that.|Хочу скопировать это.
I am gonna put it in the only router that I can,|Я вставлю его в единственный роутер, который смогу,
which is the only router that's there.|это единственный роутер, который там есть.
Let's maximize it,|Давайте максимизировать это,
config T and paste, all right.|config T и вставляем, все в порядке.
Do WR.|Сделайте WR.
As you know already just because I put that access list there, it does not matter.|Как вы уже знаете, это не имеет значения, если я поместил туда этот список доступа.
Access lists can sit on routers for years on end, nothing's gonna happen,|Списки доступа могут храниться на роутерах годами, ничего не случится,
all they're doing is taking up space until we apply it.|все, что они делают, занимают место, пока мы его не применим.
Now, where are we going to apply this?|Итак, где мы собираемся это применить?
We're going to apply it at the funnel.|Мы собираемся применить его на воронке.
At the interface that's facing towards those servers down there because we have other connections around this router that they're coming in.|В интерфейсе, который обращен к этим серверам там внизу, потому что у нас есть другие соединения вокруг этого маршрутизатора, к которым они приходят.
So we apply it at this interface right here,|Итак, мы применяем его в этом интерфейсе прямо здесь,
then anybody coming in through here will not get affected.|тогда никто, кто войдет сюда, не пострадает.
So we've got to apply it at the point where everything meets.|Так что мы должны применять это там, где все встречается.
They're trying to get to those servers,|Они пытаются добраться до этих серверов,
okay?|Ладно?
So we're going to go inside interface,|Итак, мы собираемся войти в интерфейс,
F0/1.|F0 / 1.
And then we're gonna go ahead and do IP ACCESS-GROUP and it's 100.|А потом мы продолжим и сделаем IP ACCESS-GROUP, и это будет 100.
And in which direction.|И в каком направлении.
Well, they're already in the router,|Ну они уже в роутере,
they're just trying to get out of that @01|они просто пытаются выбраться из этого @ 01
interface to get to where they need to go.|интерфейс, чтобы добраться туда, куда им нужно.
So, the direction would be out.|Итак, направление было бы вне.
Hit Enter, do WR.|Нажмите Enter, сделайте WR.
So, now we've actually created the access list.|Итак, теперь мы фактически создали список доступа.
And now we've applied the access list to the port right here.|А теперь мы применили список доступа к порту прямо здесь.
Let's see if we can see it, no.|Посмотрим, сможем ли мы это увидеть, нет.
I'm going to get over here.|Я пойду сюда.
I'm doing like, the cha cha cha over here.|Я делаю вот здесь, ча-ча-ча.
Okay.|Ладно.
Let's bring this a little bit,|Принесем это немного,
bring this a little bit more this way.|принеси это немного больше таким образом.
All right.|Отлично.
So apply to that port right there.|Так что обратитесь к этому порту прямо здесь.
All right.|Отлично.
So let's see, let's see if it works.|Так что посмотрим, посмотрим, работает ли это.
Let's go to PC 0.|Переходим к ПК 0.
Let's go to HTTP.|Перейдем к HTTP.
1.1.|1.1.
1.1.1.1.|1.1.1.1.
No problem.|Нет проблем.
PC 1 can get to it.|ПК 1 может до него добраться.
Okay, cool.|Хорошо.
That's what it should do.|Вот что он должен делать.
PC 1.|ПК 1.
I mean, or, PC 0.|То есть, или ПК 0.
But, PC 1 and PC 2 should not be able to get to it, should not.|Но ПК 1 и ПК 2 не должны иметь к нему доступ, не должны.
[BLANK_AUDIO]|[BLANK_AUDIO]
Good, we should get a request time out now.|Хорошо, мы должны получить время ожидания запроса.
[BLANK_AUDIO]|[BLANK_AUDIO]
But, we can still,|Но мы все еще можем,
not there,|не там,
we can still ping.|мы все еще можем пинговать.
We can still ping 1.1.1.1.|Мы все еще можем пинговать 1.1.1.1.
We just can't use the browser.|Мы просто не можем использовать браузер.
There we get a request timeout.|Получаем таймаут запроса.
Sooner or later.|Рано или поздно.
There you go.|Вот так.
So the access list seems to be working.|Значит, список доступа вроде работает.
Let's see if the last one will play nice as well.|Посмотрим, хорошо ли сыграет и последний.
Let's go to our browser first.|Давайте сначала зайдем в наш браузер.
1.1.1.1.|1.1.1.1.
Let's see what happens.|Давай посмотрим что происходит.
[SOUND] All right.|[ЗВУК] Хорошо.
That's good, that's a good thing, because that's what we want to happen.|Это хорошо, это хорошо, потому что мы этого хотим.
All right?|Отлично?
We've got a request time out, let me move it over here again.|Время ожидания запроса истекло, позвольте мне снова переместить его сюда.
Ping 1.1.1 1.|Пинг 1.1.1 1.
So, you still have connectivity, you're still able to get it's shares,|Итак, у вас все еще есть подключение, вы все еще можете получать его акции,
you're able to do whatever you need to do,|ты можешь делать все, что тебе нужно,
or access information from the web server,|или получить доступ к информации с веб-сервера,
just not through port 80.|просто не через порт 80.
And that's why extended access lists are very nice,|Вот почему расширенные списки доступа очень хороши,
because we can actually control,|потому что мы действительно можем контролировать,
what port people can ask you, access you through.|через какой порт люди могут спросить вас, получить к вам доступ.
All right because some ports are more vulnerable than others.|Хорошо, потому что одни порты более уязвимы, чем другие.
Maybe you don't want somebody doing a TFTP to you or an FTP to you.|Может быть, вы не хотите, чтобы кто-то выполнял для вас TFTP или FTP.
You can block FTP you know 21.|Вы можете заблокировать известный вам FTP 21.
All right you don't want people to telnet so you block port 23.|Хорошо, вы не хотите, чтобы люди использовали telnet, поэтому заблокируйте порт 23.
You only want certain emails or you permit just, you know,|Вам нужны только определенные электронные письма или вы разрешаете просто, знаете ли,
email 25 you don't want let's say IMAP or POP or anything like that.|электронное письмо 25, вы не хотите, скажем, IMAP или POP или что-то в этом роде.
So you can block or permit whatever number of ports to whatever destination, coming from whatever source.|Таким образом, вы можете заблокировать или разрешить любое количество портов в любой пункт назначения, из любого источника.
The flexibility is incredible.|Невероятная гибкость.
Again, you see that the syntax is not difficult.|Опять же, вы видите, что синтаксис несложный.
It's not difficult.|Это не трудно.
When you take your certification, when you take your certification,|Когда вы проходите сертификацию, когда вы получаете сертификат,
you need to read what they're telling you to do, okay,|тебе нужно прочитать, что они тебе говорят, хорошо,
and break it down in lay, lay terms.|и разбить его на простые, мирские термины.
All right, you want this guy to ask this guy?|Хорошо, вы хотите, чтобы этот парень спросил этого парня?
No problem.|Нет проблем.
Using port 80.|Используя порт 80.
Awesome.|Потрясающие.
Nobody else can access that through that port.|Никто другой не может получить к нему доступ через этот порт.
All right.|Отлично.
And then allow everything else.|А потом разрешите все остальное.
So, just break it down simple.|Итак, просто разбейте это на простые вещи.
And just, don't have a list of IP addresses and everything in there.|И просто не имейте там списка IP-адресов и всего остального.
And they like to use public IP addresses.|И им нравится использовать общедоступные IP-адреса.
I like to use easy public, like 1.1.1.1,|Мне нравится использовать простой паблик, например 1.1.1.1,
2.2.2.2.|2.2.2.2.
Just because it's teaching purposes.|Просто потому, что это учебные цели.
The whole point is not to drive you insane with IP's, but in an examination,|Все дело не в том, чтобы свести с ума IP, а в экзамене,
you know how it is.|Вы знаете, как это бывает.
They like to give you oh, you're more, oh my God, what IP was it?|Они любят давать тебе о, ты больше, о боже, какой это был IP?
169, 253, 1380?|169, 253, 1380?
What was that again?|Что это было снова?
So, write things down, write things down.|Итак, записывайте, записывайте.
Always before you commit to putting in the router, write it out.|Всегда, прежде чем вы решите установить маршрутизатор, запишите его.
Make sure it makes sense and then when you're sure,|Убедитесь, что это имеет смысл, а затем, когда вы уверены,
remember you've got ten minutes per simulation, then put it in there.|помните, что у вас есть десять минут на симуляцию, затем вставьте их туда.
And then test it.|А затем проверьте это.
Do not click next until you test it.|Не нажимайте "Далее", пока не протестируете.
But, regardless, extended access lists are very,|Но, несмотря на это, расширенные списки доступа очень,
very good, all right, because they're very flexible in what they do.|очень хорошо, хорошо, потому что они очень гибкие в том, что делают.
And, from my understanding,|И, как я понимаю,
this is something similar that, what you're gonna see, all right?|это что-то похожее на то, что ты увидишь, хорошо?
So this is one this extended access list here is something that you do need to look at, this lab right here, because.|Это один из расширенных списков доступа, на который вам действительно стоит обратить внимание, эта лаборатория прямо здесь, потому что.
And again, the trick was because this cloud was put here and that cloud wouldn't be there, then you can follow your book.|И снова уловка заключалась в том, что это облако было помещено сюда и этого облака там не было, тогда вы можете следить за своей книгой.
Your book says nearest the source, then we won't have an issue, but since there's another connection, well then we can't apply it to what the book says,|В вашей книге сказано, что ближайший к источнику, тогда у нас не будет проблем, но поскольку есть другая связь, мы не можем применить это к тому, что говорится в книге,
because then he won't be effected, that's it.|потому что тогда он не пострадает, вот и все.
So, again, extended access list, very simple, very simple to do.|Итак, снова расширенный список доступа, очень простой, очень простой в использовании.
You'll have maybe a couple of questions on there on extended access list,|У вас может быть пара вопросов в расширенном списке доступа,
you;ll have a simulation similar to this one on extended access list.|у вас будет симуляция, аналогичная этой, в расширенном списке доступа.
All it is is just read what is it that they're wanting you to do,|Просто прочтите, что они хотят от вас,
break it down in simple terms, write it out and then just apply it where you need to apply it.|Разбейте его простыми словами, запишите, а затем просто примените там, где вам нужно.
And look at the whole topology, not just you know, PC 0, PC 1.|И посмотрите на всю топологию, а не только на себя, ПК 0, ПК 1.
Look at the entire thing.|Посмотрите на все это.
But that's all there is to extended access list.|Но это все, что касается расширенного списка доступа.
Or a standard like we did before.|Или стандарт, как мы делали раньше.
There it is.|Вот оно.
You have you have the number, you have ACCESS-LIST 100,|У вас есть номер, у вас есть ACCESS-LIST 100,
you permit or deny, a protocol,|вы разрешаете или отрицаете протокол,
a source address, a destination address,|адрес источника, адрес назначения,
and a port number.|и номер порта.
All you gotta see is when read is what they're telling you to permit or deny.|Все, что вы должны видеть, это то, что вам говорят разрешить или запретить, когда читаете.
That's it.|Вот и все.
That's it, okay?|Все, ладно?
So that's it ladies and gentlemen.|Итак, дамы и господа.
This is your extended access list.|Это ваш расширенный список доступа.
There's really not much to it.|На самом деле в этом нет ничего особенного.
There's really not much to it.|На самом деле в этом нет ничего особенного.
Just practice, practice, practice.|Просто практика, практика, практика.
Definitely go over your chapter and do all the practices in there so you can go ahead and and be very familiar with the syntax of|Обязательно просмотрите свою главу и выполните все изложенные в ней практики, чтобы вы могли продолжить и хорошо ознакомиться с синтаксисом
writing out the access list so when you get to the day of certification you don't get blanked out or you forget to put, say, like I did, I|запишите список доступа, чтобы, когда вы дойдете до дня сертификации, вы не потерялись или не забыли поставить, скажем, как я, я
forgot to put TCP.|забыл поставить ПТС.
So, these are things that they could do,|Итак, вот что они могли сделать,
they can give you a multiple choice question, they leave out TCP, or they'll switch around, you know, the source and destination, because that's what it's|они могут задать вам вопрос с несколькими вариантами ответов, они не учитывают TCP или поменяют местами, знаете ли, источник и пункт назначения, потому что это то, что
supposed to be.|должно быть.
Source, destination, not destination and then source.|Источник, пункт назначения, а не пункт назначения, а затем источник.
So these are the little pitfalls that you may find when it comes to access lists.|Итак, это небольшие подводные камни, с которыми вы можете столкнуться, когда дело касается списков доступа.
They're not gonna go too insane with it,|Они не сойдут с ума,
but you will have a simulation like this,|но у вас будет такая симуляция,
all right?|отлично?
All right.|Отлично.
This is extended access list.|Это расширенный список доступа.
I'll see you guys in the next session.|Увидимся на следующем сеансе.