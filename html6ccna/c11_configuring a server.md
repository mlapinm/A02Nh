D:\mailCloud\prjother\tmp\1\c11_configuring a server.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
Okay, we're gonna have some fun now.|Хорошо, теперь мы повеселимся.
We're gonna get a server.|Мы собираемся получить сервер.
We're gonna bring it out and we're gonna configure.|Мы его выпустим и настроим.
We're gonna mess around with the HTTP settings and then we're gonna confi,|Мы собираемся возиться с настройками HTTP, а затем мы собираемся конфи,
we're gonna mess around with the DNS settings.|мы собираемся возиться с настройками DNS.
By no means is this anything near a real DNS.|Это ни в коем случае не похоже на настоящий DNS.
But hey, it works, you know, as a DNS so we can, we can play with it.|Но, знаете, он работает как DNS, поэтому мы можем играть с ним.
So we'll go ahead and go to our end devices, and [SOUND] and we're down here, right, end devices.|Итак, мы перейдем к нашим конечным устройствам, и [ЗВУК], и мы здесь, верно, конечные устройства.
And we'll pick a generic server.|И мы выберем общий сервер.
Let's put it way out here somewhere.|Давай поставим это где-нибудь здесь.
And let's go ahead and get a straight-through cable.|А давайте, возьмем прямой кабель.
We'll use port number 3.|Мы будем использовать порт номер 3.
We'll plug that in.|Мы подключим это.
[BLANK_AUDIO]|[BLANK_AUDIO]
And try to get a, see if we can get a straight line.|И попытайтесь получить, посмотрите, получится ли у нас прямая линия.
Whatever.|Без разницы.
Click on it.|Нажмите здесь.
First thing we're gonna do is put in the IP addresses of, or,|Первое, что мы сделаем, это введем IP-адреса, или,
or the IP address of the server which is 3.|или IP-адрес сервера 3.
So we put 192.168.1.3, Tab Tab.|Итак, ставим 192.168.1.3, Tab Tab.
192.168.1.254, same gateway.|192.168.1.254, тот же шлюз.
And I am the DNS server, so 192.16.8.3,|А я DNS-сервер, поэтому 192.16.8.3,
.1.3, sorry.|.1.3, извините.
So we put in the correct IP address as 1.3,|Итак, мы вводим правильный IP-адрес как 1.3,
which is the IP address.|который является IP-адресом.
Mask it with 24.|Замаскируйте его 24.
124 is the gateway and 1.3, because I have my own DNS server.|124 - это шлюз, а 1.3, потому что у меня свой DNS-сервер.
I can close that.|Я могу это закрыть.
Now, In the Config tab, first place I want to go to is the HTTP Settings.|Теперь, во вкладке «Конфигурация» я хочу в первую очередь перейти к настройкам HTTP.
Where it says Welcome to Cisco Packet Tracer, what I'm gonna do is.|Там, где написано «Добро пожаловать в Cisco Packet Tracer», я собираюсь сделать это.
Welcome to [BLANK_AUDIO]|Добро пожаловать в [BLANK_AUDIO]
THE NETWORKING DOCTORS.|СЕТЕВЫЕ ДОКТОРЫ.
All right.|Отлично.
I am just going to change that there so when we look at the web page when it comes up, you know, hey, you'll know we did it.|Я просто собираюсь изменить это там, поэтому, когда мы посмотрим на веб-страницу, когда она появится, вы знаете, эй, вы знаете, что мы это сделали.
And then we I want to go to DNS settings.|Затем я хочу перейти к настройкам DNS.
Now, in the name, now one this to look at,|Теперь, во имя, теперь одно это посмотреть,
and this almost gets me all the time, and it almost did already.|и это почти все время меня заводит, и почти уже получилось.
The DNS server in the pervious version was always on.|DNS-сервер в предыдущей версии всегда был включен.
In this version it's off.|В этой версии он выключен.
So make sure you turn the DNS on, okay?|Так что убедитесь, что вы включили DNS, хорошо?
And then as far as the name is concerned,|А потом, что касается названия,
the A record, right?|Рекорд, правда?
We're gonna go www, whoops, lower case,|Мы собираемся пойти www, упс, нижний регистр,
www.cisco.|www.cisco.
Uhh, no, let's just, not gonna do it that way.|Э-э, нет, давай, не будем так поступать.
We'll just do cisco.com.|Мы просто сделаем cisco.com.
Cisco.com.|Cisco.com.
And then the IP address, 192.168.1.3.|И затем IP-адрес 192.168.1.3.
And we click all right.|И щелкаем все нормально.
So now we got cisco.com as the A record and 192.168.1.3.|Итак, теперь у нас есть cisco.com как запись A и 192.168.1.3.
So how do we test this?|Так как же это проверить?
How do we test this?|Как это проверить?
All I did is put in a host record there.|Все, что я сделал, это поместил туда запись о хозяине.
I put cisco.com, which is domain name.|Я поставил cisco.com, то есть доменное имя.
And then I put in the IP address of, you know, to match it up to,|И затем я ввел IP-адрес, вы знаете, чтобы сопоставить его,
which is the DNS server.|который является DNS-сервером.
And then I go to my Desktop tab.|Затем я перехожу на вкладку «Рабочий стол».
I go to the Web Browser, and then I type cisco.com.|Я захожу в веб-браузер и набираю cisco.com.
[BLANK_AUDIO]|[BLANK_AUDIO]
And then it says the networking doctors right there.|И тут же говорится о сетевых врачах.
That's all.|Вот и все.
It did resolve that page, so DNS is working.|Эта страница действительно разрешила эту страницу, поэтому DNS работает.
Now let's see if through the other PCs we go to their web browsers and we go ahead and put cisco.com.|Теперь посмотрим, перейдем ли мы через другие ПК к их веб-браузерам, и поместим cisco.com.
There it is.|Вот оно.
Networking doctors right there.|Сетевые врачи прямо здесь.
Right?|Правильно?
There we are right there.|Вот и мы.
And then we go to the last one here.|А затем мы переходим к последнему.
Very simple, very simple operation.|Очень простая, очень простая операция.
Just getting you used to working with the packet tracer and the different aspects that it has.|Просто приучаю вас к работе с трассировщиком пакетов и различными аспектами, которые он имеет.
All right.|Отлично.
Cisco packet tra, no, cisco.com, sorry.|Пакетный канал Cisco, нет, cisco.com, извините.
And there it is, so our DNS is working just fine.|И вот он, так что наш DNS работает нормально.
Now normally you use the DNS server when you're doing name resolution on the router.|Теперь вы обычно используете DNS-сервер, когда выполняете разрешение имен на маршрутизаторе.
There's one of the things that we will be doing, okay, but you can see we got a simple topology.|Хорошо, но вы можете видеть, что у нас простая топология.
We did add now a third collision domain,|Мы добавили третий домен столкновения,
so now we have four collision domains, right?|Итак, теперь у нас есть четыре домена столкновения, верно?
Still one broadcast.|Еще одна трансляция.
We haven't created VLANs, but once we get there, we'll talk about that.|Мы не создавали VLAN, но как только мы доберемся до них, мы поговорим об этом.
So this is your packet tracer.|Итак, это ваш трассировщик пакетов.
The navigation, the creation, the configurations of it, is not that bad.|Навигация, создание, настройки не так уж и плохи.
Its just repetition, repetition,|Это просто повторение, повторение,
repetition, repetition.|повторение, повторение.
Now, as of the next section, we begin with the internet working basics and the models and so forth.|Теперь, в следующем разделе, мы начнем с основ работы в Интернете, моделей и так далее.
So I hope you if you're used to the packet tracer,|Надеюсь, если вы привыкли к трассировщику пакетов,
then this section you can pretty much don't worry about it.|то в этом разделе вы можете не беспокоиться об этом.
If you're brand new to the packet tracer,|Если вы новичок в системе трассировки пакетов,
I urge you to look at it and practice with it and play with it and connect it and stuff like that.|Я призываю вас взглянуть на это и попрактиковаться с этим, поиграть с этим, соединить и все в таком роде.
All right?|Отлично?
But if not,|Но если нет,
as we go through the course, you'll see how we'll connect things.|по мере прохождения курса вы увидите, как мы соединяем вещи.
So I will definitely see you guys in the next section.|Так что я обязательно увижу вас, ребята, в следующем разделе.
[BLANK_AUDIO]|[BLANK_AUDIO]
[BLANK_AUDIO]|[BLANK_AUDIO]
Okay we're gonna have some fun now.|Хорошо, теперь мы повеселимся.
We're gonna get a server.|Мы собираемся получить сервер.
We're gonna bring it out.|Мы собираемся выпустить это.
And we're gonna configure.|И мы собираемся настроить.
And we're gonna mess around with the HTTP settings.|И мы собираемся возиться с настройками HTTP.
And then we're gonna config, and we're gonna mess around with the DNS settings.|А затем мы собираемся настроить и возиться с настройками DNS.
By no means is this anything near a real DNS but hey,|Это ни в коем случае не похоже на настоящий DNS, но эй,
it works, you know, as a DNS so we can, we can play with it.|он работает, знаете ли, как DNS, поэтому мы можем играть с ним.
So we'll go ahead, and go to our end devices.|Итак, мы продолжим и перейдем к нашим конечным устройствам.
And, and we're down here, right, end devices.|И вот мы здесь, да, конечные устройства.
And we'll pick a generic server.|И мы выберем общий сервер.
Let's put it way out here somewhere.|Давай поставим это где-нибудь здесь.
And let's go ahead and get a straight through cable.|И давайте продолжим и возьмем прямой кабель.
We'll use port number three.|Мы будем использовать порт номер три.
We'll plug that in and try to see if I can get a straight line.|Мы подключим его и попробуем посмотреть, смогу ли я провести прямую линию.
Whatever.|Без разницы.
Click on it, first thing we're going to do is put in the IP addresses, of, or,|Нажмите на нее, первое, что мы сделаем, это введем IP-адреса, или,
or the IP address of the server, which is three.|или IP-адрес сервера, то есть три.
So we put 192.168.1.3 tab,|Так ставим вкладку 192.168.1.3,
tab, 192.168.1.254 same gateway.|tab, 192.168.1.254 тот же шлюз.
And I am the DNS server so 192.168.3.1.3|И я DNS-сервер, поэтому 192.168.3.1.3
sorry.|Прости.
So we put in the correct IP address 1.3.|Итак, мы ввели правильный IP-адрес 1.3.
Which is the IP Address.|Какой IP-адрес.
Mask it with 24.|Замаскируйте его 24.
124 is the gateway.|124 - это шлюз.
And 1.3 because I have my own DNS server.|И 1.3, потому что у меня есть собственный DNS-сервер.
You can close that.|Вы можете закрыть это.
Now, in the Config tab, first place I wanna go to is the HTTP setting,|Теперь, во вкладке Config, в первую очередь я хочу перейти к настройке HTTP,
where it says welcome to Cisco packet tracer.|где написано: "Добро пожаловать в трассировщик пакетов Cisco".
What I want to do is Welcome to.|Я хочу добро пожаловать.
[BLANK_AUDIO]|[BLANK_AUDIO]
The networking doctors.|Сетевые врачи.
[BLANK_AUDIO]|[BLANK_AUDIO]
All right, I'm just going to change that there.|Хорошо, я просто собираюсь это изменить.
So when we look at the webpage when it comes out you know, hey we know we did it.|Итак, когда мы смотрим на веб-страницу, когда она появляется, вы знаете, эй, мы знаем, что сделали это.
And then I'm gonna go into DNS setting.|А затем я перейду к настройке DNS.
Now, in the name.|Теперь по имени.
Now one thing to look at, and this always gets me, all the time and it almost did already.|Теперь одна вещь, на которую стоит взглянуть, и это всегда меня заводит, все время, и это почти уже произошло.
The DNS server in the previous version was always on, in this version it's off.|DNS-сервер в предыдущей версии был всегда включен, в этой - выключен.
So make sure you turn the DNS on, okay.|Так что убедитесь, что вы включили DNS, хорошо.
And then as far as the name is concerned,|А потом, что касается названия,
the A record.|Рекорд.
Right, we wanna go www, whoops, lowercase.|Хорошо, мы хотим использовать www, упс, в нижнем регистре.
www.Cisco.|www.Cisco.
Nah let's just.|Нет, давай просто.
[INAUDIBLE]|[НЕДОСТАТОЧНО]
Just do Cisco.com.|Просто сделайте Cisco.com.
Cisco.com.|Cisco.com.
And then the IP 192.168.1.3.|А потом IP 192.168.1.3.
And we click on it.|И нажимаем на нее.
So now we got cisco.com as the A record and 1921681.3.|Итак, теперь у нас есть cisco.com как запись A и 1921681.3.
So how do we test this?|Так как же это проверить?
How do we test this?|Как это проверить?
All I did was put in a host record there put cisco.com which is the domain name and then I put in the IP address of, you know,|Все, что я сделал, это поместил в запись хоста, там поместил cisco.com, которое является доменным именем, а затем я ввел IP-адрес, вы знаете,
to match it up to which is the DNS server.|чтобы сопоставить его с DNS-сервером.
And then I go to my desktop tab, I go to the web browser,|Затем я перехожу на вкладку рабочего стола, захожу в веб-браузер,
and then I type cisco.com.|а затем набираю cisco.com.
And then it says,|И тогда он говорит:
the networking doctors right there.|сетевые врачи прямо здесь.
It did resolve that page.|Это разрешило эту страницу.
So DNS is working.|Значит DNS работает.
Now let's see if through the other PC's we go to their web browsers, and we go ahead and put Cisco.com, there it is networking doctors right there right.|Теперь давайте посмотрим, перейдем ли мы через другие ПК к их веб-браузерам, и мы поместим Cisco.com, вот и сетевые врачи прямо здесь.
Then we go right there.|Тогда идем прямо туда.
And then we go to the last one here.|А затем мы переходим к последнему.
Very simple very simple operation.|Очень простая очень простая операция.
Just getting you used to working with the [UNKNOWN].|Просто привыкаю к ​​работе с [НЕИЗВЕСТНО].
The different aspects that it has.|Различные аспекты, которые у него есть.
All right.|Отлично.
Cisco packet, oh, Cisco.com, sorry, and there it is.|Пакет Cisco, о, Cisco.com, извините, и вот он.
So our DNS is working just fine.|Итак, наш DNS работает нормально.
Now normally you use the DNS server when you're doing name resolution on the router.|Теперь вы обычно используете DNS-сервер, когда выполняете разрешение имен на маршрутизаторе.
This is one of the things that we will be doing, okay, but you can see we have a simple topology.|Это одна из вещей, которые мы будем делать, но вы можете видеть, что у нас простая топология.
We did add now a third collision domain,|Мы добавили третий домен столкновения,
so now we have four collision domains.|Итак, теперь у нас есть четыре домена столкновения.
Right?|Правильно?
Still one broadcast.|Еще одна трансляция.
We haven't created B-LANs but once we get there we'll talk about that.|Мы не создавали B-LAN, но как только мы доберемся до них, мы поговорим об этом.
So this is your packet tracer.|Итак, это ваш трассировщик пакетов.
The navigation, the creation,|Навигация, создание,
the configuration's of it is really not that bad.|конфигурация этого действительно не так уж и плоха.
It's just repetition, repetition,|Это просто повторение, повторение,
repetition, repetition.|повторение, повторение.
Now as of the next section, we begin with the internet working basics and the models and so forth.|Теперь, что касается следующего раздела, мы начнем с основ работы в Интернете, моделей и так далее.
So I hope you if you're used to the packet tracer,|Надеюсь, если вы привыкли к трассировщику пакетов,
then this section, you can pretty much don't worry about it.|тогда в этом разделе вы можете не беспокоиться об этом.
If you're brand new to the packet tracer,|Если вы новичок в системе трассировки пакетов,
I urge you to look at it and practice with it and play with it.|Я призываю вас посмотреть на это, попрактиковаться и поиграть с этим.
And connect it and stuff like that.|И подключить его и все такое.
All right?|Отлично?
But if not as we go through the course,|Но если не так, как мы проходим курс,
you'll see how we'll connect things.|вы увидите, как мы соединим вещи.
So I'll definitely see you guys in the next section.|Так что я обязательно увижу вас, ребята, в следующем разделе.
[BLANK_AUDIO]|[BLANK_AUDIO]