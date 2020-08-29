D:\mailCloud\prjother\tmp\1\c58_interface configurations.md  


__|__
--|--
All right welcome back everyone.|Хорошо, добро пожаловать снова.
This time we do the interfaces, but before we do we forgot one little thing in the line BTY 0 through 15.|На этот раз мы делаем интерфейсы, но перед этим мы забыли одну мелочь в строке BTY с 0 по 15.
So we are going to go back into the router that we were in.|Итак, мы собираемся вернуться к маршрутизатору, в котором мы были.
Let's I maximize it and your way over there so you can see that.|Давайте я максимизирую это и ваш путь туда, чтобы вы это увидели.
I think you can see that, lets make sure that you can see that.|Я думаю, вы это видите, давайте убедимся, что вы это видите.
So I'm just going to go do this instead.|Так что я просто сделаю это вместо этого.
I just wanna make sure that you can see it and we'll move it right there.|Я просто хочу убедиться, что вы это видите, и мы переместим его прямо сейчас.
Yeah, okay.|Да ладно.
So, we're gonna go to the line BTYs, which means we're gotta go to con,|Итак, мы собираемся перейти к линии BTY, что означает, что мы должны пойти на мошенничество,
go to config first.|сначала зайдите в config.
Line BTY zero.|Строка BTY нулевая.
And, like I said, you put a question mark after that,|И, как я уже сказал, после этого вы ставите вопросительный знак,
it'll tell you how many lines you have.|он скажет вам, сколько строк у вас есть.
You see?|Ты видишь?
It'll tell you right there.|Он скажет вам прямо здесь.
15.|15.
So, we put 15, and one of things that we forgot is to configure at SSH.|Итак, мы поставили 15, и одна из вещей, которые мы забыли, - это настроить на SSH.
So you're going to do: TRANSPORT INPUT,|Итак, вы собираетесь сделать: ВХОД ТРАНСПОРТА,
because you're going in, and this question mark.|потому что ты входишь, и этот вопросительный знак.
Oh, transport, what did I type wrong?|О, транспорт, что я напечатал не так?
What did I type wrong, you see?|Что я напечатал не так, понимаете?
TRANSPORT INPUT, okay.|ТРАНСПОРТНЫЙ ВВОД, хорошо.
We can do all.|Мы можем все.
We can do SSH.|Мы можем использовать SSH.
We can do Telnet.|Мы можем использовать Telnet.
We're going to do all and the only reason I'm doing all and then I'm going to exit.|Мы собираемся сделать все, и только по одной причине я делаю все, а затем я уйду.
Exit and do a copy, run, start.|Выйти и сделать копию, запустить, запустить.
Remember I say you can say whatever you want I just did a new command so I wanted to say that, because in the future in the lessons to come I gotta show|Помните, я говорю, что вы можете говорить все, что хотите. Я только что выполнил новую команду, поэтому я хотел сказать это, потому что в будущем на будущих уроках я должен показать
you how to Telnet into a router or how to SSH.|вы, как Telnet в маршрутизатор или как SSH.
So instead of going back and changing the configurations, I'm just gonna allow for both.|Поэтому вместо того, чтобы возвращаться и изменять конфигурации, я просто допущу оба варианта.
I can SSH or Telnet.|Я могу использовать SSH или Telnet.
But in the real world you would either,|Но в реальном мире вы бы тоже
you would really just do SSH.|вы бы действительно просто использовали SSH.
You really wouldn't do Telnet, Some people still use it, may, you know, internally,|Вы действительно не стали бы использовать Telnet, некоторые люди все еще используют его, вы знаете, внутри
or what have you.|или что у тебя.
But SSH is the way to go.|Но SSH - это правильный выбор.
So now let's go ahead and do the interfaces.|А теперь займемся интерфейсами.
Now the interfaces, what I like to do is to SHOW IP INT BRIEF.|Теперь об интерфейсах, что мне нравится делать, так это ПОКАЗАТЬ КРАТКИЙ ОБЗОР IP INT.
And that tells me the interfaces that I have.|И это говорит мне об имеющихся у меня интерфейсах.
So I know I'm using S0/0/0, cuz that's where I usually start with.|Итак, я знаю, что использую S0 / 0/0, потому что обычно я начинаю с него.
So I keep it consistent and I always use F0/0 for the router when it's connecting to the LAN.|Поэтому я придерживаюсь единообразия и всегда использую F0 / 0 для маршрутизатора, когда он подключается к локальной сети.
So, I know those are the two interfaces that I need to configure.|Итак, я знаю, что это два интерфейса, которые мне нужно настроить.
I'm first going to do that LAN interface.|Сначала я сделаю этот интерфейс LAN.
And we are using 192.168.100.1 I believe,|И мы используем 192.168.100.1, я считаю,
right?|право?
No 1.0, 1.0 okay?|Нет 1.0, 1.0 ладно?
So let's go ahead and do this more and more this way.|Так что давайте продолжим и будем делать это все чаще и чаще.
We are using the 1.0 and the 2.0 okay alright.|Мы используем 1.0 и 2.0, хорошо, хорошо.
So we're going to do config T.|Итак, мы собираемся выполнить конфигурацию T.
We're going to go inside the interface F0/0.|Мы собираемся зайти внутрь интерфейса F0 / 0.
We're going to put the IP address.|Мы собираемся указать IP-адрес.
This is your gateway, this is your gateway.|Это ваш шлюз, это ваш шлюз.
So IP ADDRESS 192.168.1.254|Итак, IP-АДРЕС 192.168.1.254
255.255.255.0.|255.255.255.0.
Now the next thing I wanna type is a description and it's nice,|Теперь следующее, что я хочу напечатать, - это описание, и оно приятно,
it's it's a courtesy to type a description.|это любезно набирать описание.
If you're going to test later on these lines, you know which is a circuit ID,|Если вы собираетесь позже протестировать эти строки, вы знаете, какой идентификатор цепи,
or which line is it that you are testing.|или какую строку вы тестируете.
So, I'm just going to put a simple description which says, connection to LAN.|Итак, я просто собираюсь поместить простое описание, которое говорит о подключении к локальной сети.
So, it's just so you know which line this is, all right.|Итак, просто чтобы вы знали, какая это строка, хорошо.
And if you're running some sort of test.|И если вы проводите какой-то тест.
And then all interfaces, all interfaces,|А потом все интерфейсы, все интерфейсы,
all routers by default are administratively down.|все маршрутизаторы по умолчанию отключены административно.
Administratively down means you need to turn them on.|Административно отключено означает, что вам нужно их включить.
So, clue, if you do, which we'll do li, in a little bit, show IPN brief, and you see that it's administratively down,|Итак, подскажите, если вы это сделаете, мы сделаем это чуть позже, покажем бриф IPN, и вы увидите, что он не работает административно,
that means you never turned it on.|это означает, что вы никогда его не включали.
Okay?|Ладно?
So I'll do a no shut.|Так что я ничего не сделаю.
Be careful what you type there.|Будьте осторожны с тем, что вы там набираете.
[LAUGH] So, no shut turns on the interface,|[СМЕХ] Итак, выключение не включает интерфейс,
where shut turns off the interface.|где выключение отключает интерфейс.
Okay?|Ладно?
And then we wanna do the S0/0, or S triple 0.|А затем мы хотим выполнить S0 / 0 или S тройной 0.
As I call it.|Как я это называю.
S0/0/0 interface.|Интерфейс S0 / 0/0.
IP our address.|IP наш адрес.
And then that's gonna be 10.1.15.|И тогда это будет 10.1.15.
255.255.255.255.|255.255.255.255.
Oops, my bad.|Ой, моя плохая.
.1.5 255.255.255.252 enter.|.1.5 255.255.255.252 введите.
Let's put a description,|Ставим описание,
connection to R2, connecting to R2.|подключение к R2, подключение к R2.
And then we put a clock-rate, now a clock-rate is the actual speed of the connection that you have going into the other one.|Затем мы устанавливаем тактовую частоту, теперь тактовая частота - это фактическая скорость соединения, которое вы используете для другого.
But since this is a simulator, I can use the maximum speed, which is 4,000,000.|Но поскольку это симулятор, я могу использовать максимальную скорость, которая составляет 4 000 000.
And then I turn on the interface.|А потом включаю интерфейс.
No shut.|Нет, заткнись.
So, I'm going to exit.|Итак, я собираюсь уйти.
Exit.|Выход.
And then I'm going to do a COPY RUN START.|А затем я сделаю ЗАПУСК КОПИРОВАНИЯ.
Enter, enter.|Входи, входи.
Now I could have done a control-Z.|Теперь я мог бы сделать Control-Z.
W-R.|W-R.
I could have done a do W-R from where I was at.|Я мог бы сделать W-R с того места, где был.
I didn't have to come back down to [UNKNOWN] mode to do that.|Для этого мне не нужно было возвращаться в режим [НЕИЗВЕСТНО].
That's the nice thing about the newer IOS's.|Это хорошая особенность новых IOS.
That you can do the do command right from where you're at, so you don't have to come back down.|Что вы можете выполнять команду do прямо с того места, где находитесь, поэтому вам не нужно возвращаться.
But for those of you that are taking or those of you that are taking this course,|Но для тех из вас, кто идет, или для тех, кто принимает этот курс,
obviously you're taking the CCNA 200-120|очевидно, вы берете CCNA 200-120
and you need to go ahead and know that you need to come back to privilege mode and do this.|и вам нужно идти вперед и знать, что вам нужно вернуться в привилегированный режим и сделать это.
So now let's check the interfaces.|Итак, теперь давайте проверим интерфейсы.
I'm gonna show you two commands.|Я покажу вам две команды.
Show IP int brief.|Показать краткий IP-адрес.
And let me open this up for you a little bit more.|И позвольте мне открыть это вам еще немного.
And what this is showing you right here,|И что это показывает вам прямо здесь,
I'll stand over here,|Я буду стоять здесь,
it's showing you the IP addresses, for each of the interfaces we've put in.|он показывает вам IP-адреса для каждого из встроенных интерфейсов.
And look there, this Serial0/0/0 is showing down, down.|И посмотрите, этот Serial0 / 0/0 показывает вниз, вниз.
Where my Fastethernet0/0 is showing up,|Где появляется мой Fastethernet0 / 0,
up.|вверх.
What does that mean?|Что это значит?
Well my fast ethernet is working without a problem.|Что ж, мой быстрый Ethernet работает без проблем.
My serial apparently has a problem, but this is a layer one issue.|У моего серийного номера явно проблема, но это проблема первого уровня.
Possible question.|Возможный вопрос.
This is a layer one issue.|Это проблема первого уровня.
I haven't done the other side of the router,|Я еще не делал другую сторону роутера,
that's why there's no connectivity to the other side of the router.|вот почему нет подключения к другой стороне маршрутизатора.
Therefore showing it's down, down.|Поэтому показывая это вниз, вниз.
And you can see since I've never turned on these other interfaces they're administratively down.|И вы можете видеть, поскольку я никогда не включал эти другие интерфейсы, они отключены административно.
Now, the other thing you could see is up down.|Теперь еще одна вещь, которую вы могли видеть, - это вверху вниз.
Line is up, protocol is down.|Линия активна, протокол не работает.
That's another thing, another way you can see this.|Это другое дело, это можно увидеть по-другому.
What that would mean is, a layer two encapsulation, clocking, CRCs,|Это будет означать, что инкапсуляция второго уровня, синхронизация, CRC,
there's where you can see an up down.|вот где вы можете увидеть вверх вниз.
But here you see is up, up, down, down So we're good but we have a layer one cuz we haven't done the other side.|Но здесь вы видите вверх, вверх, вниз, вниз. Итак, мы в порядке, но у нас есть первый слой, потому что мы еще не сделали другую сторону.
All right?|Отлично?
So, how do you configure, I'm gonna show you a different way of configuring, and this is why you need to know really how to|Итак, как вы настраиваете, я покажу вам другой способ настройки, и именно поэтому вам нужно действительно знать, как
navigate through your router.|перемещаться по маршрутизатору.
Okay?|Ладно?
I'm gonna go ahead and open up Notepad,|Я собираюсь открыть Блокнот,
which I have it right here already.|который у меня уже есть здесь.
If you know how you're navigating through your router all you really need to do is type the commands and everybody scripts everything.|Если вы знаете, как перемещаться по маршрутизатору, все, что вам действительно нужно, это вводить команды, и все пишут все сценарии.
Everybody out there has their scripts ready made up and all they do is copy paste into the router.|У всех уже есть готовые сценарии, и все, что они делают, это копируют и вставляют в маршрутизатор.
Can't do it in the, in the test but just to show you I'm gonna do router two.|Не могу сделать это в тесте, но просто чтобы показать вам, что собираюсь сделать второй маршрутизатор.
I'm gonna do router two but I'm gonna do it in Notepad.|Я собираюсь сделать второй роутер, но сделаю это в Блокноте.
And it's right there.|И это прямо там.
Okay.|Ладно.
So I'm gonna type enable.|Итак, я наберу enable.
No, that's not enable.|Нет, это не разрешено.
Enable.|Включить.
That's not enable either.|Это тоже не позволяет.
Wow, okay Laz, let's type here.|Вау, ладно, Лаз, давай напечатаем здесь.
ENABLE, then I type CONFIG T,|ВКЛЮЧИТЬ, затем я набираю CONFIG T,
then I'm gonna type HOSTNAME,|тогда я наберу HOSTNAME,
R2 then I'm gonna go ahead and start doing the passwords ENABLE PASSWORD CISCO,|R2, тогда я начну вводить пароли ENABLE PASSWORD CISCO,
ENABLE wow SECRET STUDENTS.|ВКЛЮЧИТЬ wow СЕКРЕТНЫХ СТУДЕНТОВ.
My fingers are not working today.|Мои пальцы сегодня не работают.
I need loosen them up.|Мне нужно их ослабить.
ENABLE SECRET STUDENT,|РАЗРЕШИТЬ СЕКРЕТНУЮ СТУДЕНТУ,
SERVICE PASSWORD-ENCRYPTION then the username.|СЕРВИСНЫЙ ПАРОЛЬ-ШИФРОВАНИЕ, затем имя пользователя.
Let me open this up.|Позвольте мне открыть это.
The font is big because I can't see.|Шрифт большой, потому что я не вижу.
All right, so I'm going to do username [BLANK_AUDIO]|Хорошо, я сделаю имя пользователя [BLANK_AUDIO]
LDIAZ PRIVILAGE, this is where spelling comes in, PRIVILEGE 15, no tabbing here.|LDIAZ PRIVILAGE, здесь на помощь приходит правописание, PRIVILEGE 15, здесь нет табуляции.
PRIVILIGE 15, password CISCO zero, there you go, look at that.|PRIVILIGE 15, пароль CISCO ноль, вот и посмотрите.
0 CISCO.|0 CISCO.
And then we're gonna do the banner.|А потом сделаем баннер.
Banner MOTD.|Баннер MOTD.
Start, we'll start this one with a, what happened?|Начнем, мы начнем с этого, что случилось?
Let's start this one with a $.|Начнем с символа $.
WELCOME TO R2.|ДОБРО ПОЖАЛОВАТЬ В R2.
And let's end it with a $.|И давайте закончим это символом $.
Okay.|Ладно.
Then we'll do IP DOMAIN-LOOKUP.|Затем мы проведем ПРОСМОТР IP-ДОМЕНА.
And again this one is already on.|И снова этот уже включен.
You don't have to type it but again just to show you the command.|Вам не нужно вводить его, но снова просто чтобы показать вам команду.
IP DOMAIN-NAME CISCO.COM.|IP ДОМЕННОЕ ИМЯ CISCO.COM.
We were pointing it to the same dns server, okay.|Мы указывали на тот же DNS-сервер, хорошо.
IP DOMAIN, nah, not domain, I'm sorry.|IP DOMAIN, нет, не домен, извините.
IP NAME-SERVER.|IP ИМЯ-СЕРВЕР.
And that was 192.168.1.2, I believe.|Думаю, это был 192.168.1.2.
All right.|Отлично.
And now, we're gonna go ahead and generate those crypto keys.|А теперь мы собираемся сгенерировать эти криптографические ключи.
CRYPTO KEY GENERATE RSA.|КРИПТО КЛЮЧ ГЕНЕРИРУЕТ RSA.
You're gonna hit enter.|Вы собираетесь нажать Enter.
All right.|Отлично.
Fi, you're gonna type 512, enter.|Фи, набери 512, входи.
Okay and because you have that's the way you gotta do it.|Хорошо, и потому что у вас есть такой способ, вы должны это делать.
Normally you'd just hit enter but just in case I type 512 and then I hit enter.|Обычно вы просто нажимаете Enter, но на всякий случай я набираю 512, а затем нажимаю Enter.
All right and then your gonna do LINE CON 0.|Хорошо, а потом ты сделаешь LINE CON 0.
PASSWORD CISCO,|ПАРОЛЬ CISCO,
LOGIN LOCAL to use the local user name.|LOGIN LOCAL для использования имени локального пользователя.
Then we're gonna go ahead and do EXEC-TIMEOUT 0 0,|Затем мы продолжим и сделаем EXEC-TIMEOUT 0 0,
meaning my session should never timeout.|это означает, что мой сеанс никогда не должен отключаться.
LOGGING SYNCHRONOUS all right?|ЛОГИН СИНХРОННЫЙ все в порядке?
So, the nuisance command.|Итак, неприятная команда.
Then we're gonna go to the line VTY 0 15, PASSWORD CISCO.|Затем мы перейдем к строке VTY 0 15, ПАРОЛЬ CISCO.
LOGIN LOCAL.|ВХОД ЛОКАЛЬНЫЙ.
[SOUND] exec, same commands exec I should've just copy paste it, EXEC-TIMEOUT 0 0.|[ЗВУК] exec, те же команды exec, я должен был просто скопировать и вставить, EXEC-TIMEOUT 0 0.
LOGGING SYNCHRONOUS.|ЛОГИНГ СИНХРОННЫЙ.
All right.|Отлично.
And then this is where we put TRANSPORT INPUT SS, oh, this is H, ALL.|А потом сюда мы помещаем ВХОД ТРАНСПОРТА SS, о, это H, ALL.
Okay?|Ладно?
Now let's do the interfaces.|Теперь займемся интерфейсами.
We've got the S0/11 And, we got the F 0 0.|У нас есть S0 / 11 И у нас есть F 0 0.
So, let's do the F 0 0 first.|Итак, давайте сначала сделаем F 0 0.
So, we're in line configuration mode.|Итак, мы находимся в режиме конфигурации линии.
Let's exit once.|Давай выйдем один раз.
That takes us to global.|Это переносит нас на глобальный уровень.
INT F0/0, enter.|INT F0 / 0, введите.
IP address.|Айпи адрес.
This is the 192.168.2.254.|Это 192.168.2.254.
That's the gateway.|Это шлюз.
255.255.255.0 enter.|255.255.255.0 введите.
We do a DESCRIPTION CONNECTION TO LAN, all right?|Делаем ОПИСАНИЕ ПОДКЛЮЧЕНИЕ К ЛВС, ладно?
The basic not LAZ, LAN, all right.|Базовый не ЛАЗ, ЛАН, да ладно.
And then NO SHUT.|А потом НЕ ЗАКРЫТЬ.
To turn that on.|Чтобы включить это.
This is the DT portion, and I just wanna verify that indeed it is the S001,|Это часть DT, и я просто хочу убедиться, что это действительно S001,
which I'm pretty sure it is.|в чем я почти уверен.
S001, yes.|S001, да.
Okay, so we go INT S0/0/1,|Хорошо, идем INT S0 / 0/1,
IP ADDRESS and 10.1.1.6|IP-АДРЕС и 10.1.1.6
255.255.255.252.|255.255.255.252.
Enter.|Войти.
No clock rate needed but let's put a description.|Тактовая частота не нужна, но давайте опишем.
Courtesy.|Вежливость.
CONNECTION TO R1.|ПОДКЛЮЧЕНИЕ К R1.
Now we do a NO SHUT.|Теперь делаем НЕ ВЫКЛЮЧЕНИЕ.
And then we're gonna type EXIT.|И затем мы наберем EXIT.
Which we were interface configuration mode.|Который мы были в режиме настройки интерфейса.
That took us to global.|Это привело нас к глобальному.
We EXIT again.|Мы ВЫХОДИМ снова.
That took us to privilege.|Это привело нас к привилегии.
And then we do it COPY RUN START.|И затем мы делаем это COPY RUN START.
Enter.|Войти.
Enter.|Войти.
So then we just paste and hopefully, I and do a Ctrl+Up and hopefully there should be no issues.|Итак, мы просто вставляем и, надеюсь, я нажимаю Ctrl + Up, и, надеюсь, проблем не должно быть.
And you wanna make sure you go all the way down so you can hit those enters as well.|И вы хотите убедиться, что вы прошли весь путь вниз, чтобы вы могли попасть и в эти входы.
On a Ctrl+C.|На Ctrl + C.
And if I didn't make any mistakes, it should configure the router fully,|И если я не ошибся, он должен полностью настроить роутер,
just like I did the other one.|точно так же, как я сделал другой.
But, again, you would need to be in enable, or not enable I'm sorry, in user mode in order to start.|Но, опять же, для запуска вам нужно будет включить или не включить, извините, в пользовательском режиме.
So you're right there.|Итак, вы правы.
All right?|Отлично?
You would say no at this point because this is telling you do you want to enter the initial configuration by logging in?|Вы бы сказали «нет» на данном этапе, потому что это говорит о том, что вы хотите войти в начальную конфигурацию, войдя в систему?
You say no.|Вы говорите нет.
And then you want to paste right into the router.|А потом вы хотите вставить прямо в роутер.
You can right click and paste where you just hit the button.|Вы можете щелкнуть правой кнопкой мыши и вставить туда, где вы только что нажали кнопку.
And let's see what happens.|И посмотрим, что получится.
And boom.|И бум.
No errors.|Ошибок нет.
It took everything, completely configured.|Снял все, полностью настроил.
Let's verify.|Давайте проверим.
Show start.|Показать начало.
There's my source password encryption,|Там мой исходный пароль шифрование,
host name.|имя хоста.
There are my secret and plain text passwords, username,|Это мой секретный пароль и пароль в виде обычного текста, имя пользователя,
SSH versions, my domain name, my ethernet,|Версии SSH, мое доменное имя, мой Ethernet,
my serial, okay?|мой серийник, ладно?
My banner, my line cons and my even my, is my SSH in there?|Мой баннер, мои строчные минусы и даже мой, мой SSH там?
Login, local.|Логин, местный.
I don't see that SSH.|Я не вижу этого SSH.
Took in the line DTI.|Брал в линейке DTI.
Okay, so let's go back in there to make sure that is configured.|Хорошо, давайте вернемся туда, чтобы убедиться, что все настроено.
So, line VTY 0 15|Итак, строка VTY 0 15
TRANSPORT INPUT ALL.|ТРАНСПОРТНЫЙ ВВОД ВСЕ.
Just to make that takes, because I didn't see it there.|Просто чтобы понять, потому что я этого там не видел.
Oh, what I was gonna do, I'm going to do a shortcut, control z, wr.|О, что я собирался сделать, я сделаю ярлык, control z, wr.
Copied it.|Скопировал.
Show START.|Показать СТАРТ.
I'm going to hit the space bar, or enter,|Я нажму пробел или войду,
then the space bar all the way to the bottom.|затем пробел до конца.
And is this supposed to show?|И это должно быть видно?
Well I guess not.|Думаю, нет.
We'll go ahead.|Пойдем дальше.
But now, you are fully configured, so two ways.|Но теперь вы полностью настроены, так что есть два пути.
In the first one, we did it step by step,|В первом мы делали это шаг за шагом,
we understood what each command did.|мы поняли, что делает каждая команда.
And we navigated through the IOS of the router putting in all the commands.|И мы прошли через IOS маршрутизатора, введя все команды.
We had forgotten one command, so we went back into the interface and put it in there.|Мы забыли одну команду, поэтому вернулись в интерфейс и поместили ее туда.
On the other router, router two, instead of doing it that way since you already knew where to go in the iOS, we actually just put in the actual|На другом маршрутизаторе, маршрутизаторе 2, вместо того, чтобы делать это таким образом, поскольку вы уже знали, куда идти в iOS, мы фактически просто вставили фактический
commands in Notepad and then just paste it down.|команды в Блокноте, а затем просто вставьте их.
Obviously some commands are gonna be the same.|Очевидно, что некоторые команды будут такими же.
The ones that are not gonna be the same is the IP addresses, and the host name,|Не будут совпадать IP-адреса и имя хоста,
those are not going to be the same.|они не будут прежними.
The passwords and all the other stuff will be the same.|Пароли и все остальное будут такими же.
Now, in the next lesson, we're going to go ahead and verify that everything is working, okay, and how we can Telnet for SSH Into our routers.|Теперь, в следующем уроке, мы продолжим и проверим, что все работает, хорошо, и как мы можем использовать Telnet для SSH в наших маршрутизаторах.
I'll see you then.|Увидимся тогда.
[BLANK_AUDIO]|[BLANK_AUDIO]