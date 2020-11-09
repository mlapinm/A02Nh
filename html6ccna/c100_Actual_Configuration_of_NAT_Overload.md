D:\mailCloud\prjother\tmp\1\c100_Actual Configuration of NAT Overload.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
Alright, so let's go ahead and take these configurations that we did in Notepad,|Хорошо, давайте продолжим и возьмем те конфигурации, которые мы сделали в Блокноте,
and we're going to go ahead and do it from scratch on the actual router.|и мы собираемся сделать это с нуля на самом роутере.
Alright, now you see that we have no IP addresses or anything,|Хорошо, теперь вы видите, что у нас нет IP-адресов или чего-то еще,
cause they're, that, oops.|потому что они, это, ой.
The lines are, you see we have red dots there.|Линии такие, видите, у нас там красные точки.
I'll put this over here.|Я положу это сюда.
So, we are going to need to put an IP address here.|Итак, нам нужно будет указать здесь IP-адрес.
It'll be 1.254.|Будет 1,254.
This'll be 1.254.|Это будет 1,254.
All right.|Все в порядке.
Then we'll start with our NAT configurations.|Затем мы начнем с наших конфигураций NAT.
So why don't I just maximize the router right there.|Так почему бы мне просто не развернуть роутер прямо сейчас.
I want to say nope.|Я хочу сказать нет.
Enable, config T,|Включить, настроить T,
host name, NAT.|имя хоста, NAT.
Okay.|Ладно.
So now we're going to go into interface.|Итак, теперь мы переходим к интерфейсу.
F0/0.|F0 / 0.
IP address.|Айпи адрес.
192.168.100.254.|192.168.100.254.
Is it 100254, you see how my brain is all messed up?|Это 100254, вы видите, как у меня в голове все запуталось?
It's 1.254.|Это 1,254.
[BLANK_AUDIO]|[BLANK_AUDIO]
1.254 255, 255, 255 now zero.|1.254 255, 255, 255 теперь ноль.
Okay we'll do a no shut on that.|Хорошо, мы не будем закрывать глаза на это.
And since we're here already let's tell it hey, your the inside part of the NAT.|И раз уж мы здесь, давайте скажем, эй, ваша внутренняя часть NAT.
So, i p NAT, inside.|Итак, внутри NAT.
Boom, now we're gonna go to the other side.|Бум, теперь мы перейдем на другую сторону.
Interface add zero slash one, IP address,|Интерфейс добавить нулевую косую черту, IP-адрес,
not that many of these.|не так много их.
1.1.1.254, 255,|1.1.1.254, 255,
255, 255.0, no shots.|255, 255.0, выстрелов нет.
And then we're gonna go ahead and tell it,|И тогда мы продолжим и расскажем это,
hey you're the outside IP NAT, outside.|эй, ты внешний IP NAT, снаружи.
DWR.|DWR.
All right..|Все в порядке..
And that's pretty much it for that.|Вот и все.
Let's take a look to see show IP in brief.|Давайте посмотрим, чтобы вкратце увидеть IP.
We are up, up.|Мы встали, встали.
Probably have connectivity already going across.|Вероятно, уже есть возможность подключения.
Now what we're gonna do.|Теперь что мы будем делать.
We're gonna routing table.|Мы собираемся таблицу маршрутизации.
Show IP route.|Показать IP-маршрут.
We're connected to both sides, so no issues there.|Мы связаны с обеими сторонами, поэтому проблем нет.
So, what we're gonna do now is, we're gonna create our pool of addresses,|Итак, теперь мы собираемся создать пул адресов,
since now we know which is inside and which is outside.|теперь мы знаем, что внутри, а что снаружи.
So, config t, IP NAT pool, laz.|Итак, config t, IP NAT pool, laz.
The pool is gonna be 1.1.1.254.|Пул будет 1.1.1.254.
1.1.1.254.|1.1.1.254.
We don't have real addresses.|У нас нет реальных адресов.
I'm gonna use that one.|Я воспользуюсь этим.
All right.|Все в порядке.
And net mask.|И чистая маска.
It's going to be 255.255.255.0.|Это будет 255.255.255.0.
Standard access list.|Стандартный список доступа.
Access hyphen list.|Доступ к списку дефисов.
I'm gonna use 10.|Я собираюсь использовать 10.
Permit the 192 168.1.0,|Разрешить 192 168.1.0,
0.00 255 network.|0,00 255 сеть.
Again that access lives by itself, doesn't do anything,|Опять же, доступ существует сам по себе, ничего не делает,
we're not applying it to any lines, we're not applying it to any interfaces.|мы не применяем его ни к каким линиям, мы не применяем его ни к каким интерфейсам.
It's listening for interesting traffic.|Он ищет интересный трафик.
How does it do that?|Как оно это делает?
By this third line.|По этой третьей строке.
IP NAT inside source list, what list?|IP NAT внутри списка источников, какой список?
Ten.|10.
What pool?|Какой пул?
Laz.|Лаз.
Magical word?|Волшебное слово?
Overload.|Перегрузка.
DO WR and you're done.|DO WR, и все готово.
That is it.|Вот и все.
Easy peasey Japanesey, very simple, very simple.|Легкая легкая японская, очень простая, очень простая.
Okay?|Ладно?
So let's see if we're actually translating.|Итак, давайте посмотрим, действительно ли мы переводим.
In order to translate, we have to go through the NAT router.|Для перевода нам нужно пройти через маршрутизатор NAT.
So what we're going to do.|Итак, что мы будем делать.
We're going to get one of these PCs that say PC zero.|Мы собираемся получить один из этих компьютеров с надписью «PC zero».
And we'll ping.|И мы пингуем.
Let's see if this server has an IP address.|Посмотрим, есть ли у этого сервера IP-адрес.
Sure does.|Конечно, делает.
Awesome, awesome.|Круто круто.
So, look at that.|Итак, посмотри на это.
Still recovering from that accident.|Все еще восстанавливаюсь после той аварии.
And though the humerus is on this side,|И хотя плечевая кость с этой стороны,
it's really this side.|это действительно с этой стороны.
I should have a plate showing nine screws.|У меня должна быть табличка с девятью винтами.
Not fun.|Не смешно.
So, let's ping.|Итак, пингуем.
Ping, 1.1.1.1.|Пинг, 1.1.1.1.
Come on, IPv4.|Давай, IPv4.
All right, we have connectivity.|Хорошо, у нас есть связь.
We would have had connectivity with or without the net, we just want to make sure that we're translating.|У нас было бы соединение с сетью или без нее, мы просто хотим убедиться, что мы переводим.
All right.|Все в порядке.
So, supposedly we are.|Итак, якобы мы.
Let's see.|Посмотрим.
How do we check to see if we're translating?|Как мы проверяем, переводим ли мы?
Do a control Z here.|Сделайте контрольную Z здесь.
Come on.|Давай.
Show IP NAT trans, short for translation.|Показать IP NAT trans, сокращение от перевода.
And we are.|И мы.
There is your, the protocol that you're using, obviously, is PNG.|Вот ваш протокол, который вы используете, очевидно, PNG.
Here is your inside global.|Вот ваш внутренний мир.
This is the IP address that got translated, right?|Это IP-адрес, который был переведен, верно?
Well after a translation, this is the IP address that got translated,|После перевода это IP-адрес, который был переведен,
to the global or public IP address.|на глобальный или общедоступный IP-адрес.
You can see the port numbers that it's using cuz really paint doesn't have a port number.|Вы можете видеть номера портов, которые он использует, потому что на самом деле у paint нет номера порта.
But if you take a look at the outside local or global they're both the same cuz this is the destination.|Но если вы посмотрите на внешнее, локальное или глобальное, они оба одинаковы, потому что это пункт назначения.
So it's gonna be the same.|Так что все будет так же.
Let's try and go through the browser and see if we see anything different.|Давайте попробуем пройтись по браузеру и посмотреть, увидим ли мы что-нибудь другое.
Let's go back to the PC, let's use the browser and we'll go one dot one dot one dot one.|Вернемся к ПК, воспользуемся браузером и перейдем одна точка, одна точка, одна точка.
Oops.|Ой.
Alright so we went to the server.|Итак, мы пошли на сервер.
But this time we went through the browser.|Но на этот раз мы пошли через браузер.
So now the protocol should have changed.|Итак, теперь протокол должен был измениться.
So I.|Так что я.
[BLANK_AUDIO]|[BLANK_AUDIO]
Okay, now we're using the tcp protocol.|Хорошо, теперь мы используем протокол tcp.
You can see you have an actual now port number.|Вы можете видеть, что у вас есть текущий номер порта.
Remember the first 1024 are known ports.|Помните, что первые 1024 порта являются известными.
So it starts on the very first port 1025|Итак, он запускается на самом первом порту 1025
and it goes up.|и он идет вверх.
Again, this is the IP address of your PC that got translated to this inside global and you can see that your outside local destination port is 80.|Опять же, это IP-адрес вашего ПК, который был преобразован в этот внутренний глобальный, и вы можете видеть, что ваш внешний локальный порт назначения - 80.
It is 80 but the IP addresses do not change.|Это 80, но IP-адреса не меняются.
The IP addresses do not change.|IP-адреса не меняются.
So that's all there is to configuring NAT,|Вот и все, что нужно для настройки NAT,
as long as you remember because you'll see a screen it will give you maybe like a show start or a show run and you'll be right there.|пока вы помните, потому что вы увидите экран, он может показаться вам как начало шоу или запуск шоу, и вы будете прямо там.
Be sure that you look for this IP NAT inside.|Убедитесь, что вы ищете IP NAT внутри.
I've been at outside.|Я был снаружи.
And there is your, you know, your NAT configuration.|И есть ваша, знаете ли, ваша конфигурация NAT.
All right.|Все в порядке.
Next lesson, that we're gonna get into,|Следующий урок, которым мы займемся,
which will be your final lesson for NAT will be the pitfalls, what to look for in your certification exam.|который станет вашим последним уроком по NAT, будет подводным камнем, на что следует обратить внимание на сертификационном экзамене.
I'll see you there.|Увидимся там.
[BLAN|[BLAN
  
