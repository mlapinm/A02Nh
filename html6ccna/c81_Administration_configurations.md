D:\mailCloud\prjother\tmp\1\c81_Administration configurations.md  


__|__
--|--
Welcome back.|Добро пожаловать.
It's time to configure.|Пора настраивать.
We're inside the Switch.|Мы внутри Switch.
There you go, Enter.|Вот и все, Enter.
So let's start doing some basic configurations.|Итак, приступим к выполнению основных настроек.
All right, so Enable,|Хорошо, так что включите,
of course I abbreviate, you can't.|конечно я сокращаю, вы не можете.
Enable CONFIG T,|Включите CONFIG T,
let's give the switch a name.|дадим переключателю имя.
HOSTNAME SW1, switch one,|HOSTNAME SW1, переключить один,
very simple, no spaces,|очень просто, без пробелов,
remember cannot have spaces in the hostname.|помните, что в имени хоста не может быть пробелов.
We'll do the same thing as we did in the router,|Сделаем то же самое, что и в роутере,
ENABLE PASSWORD CISCO,|РАЗРЕШИТЬ ПАРОЛЬ CISCO,
ENABLE SECRET STUDENT.|РАЗРЕШИТЬ СЕКРЕТНОГО СТУДЕНТА.
And again, just as a refresher,|И снова, как напоминание,
remember that these two passwords are the same thing.|помните, что эти два пароля - одно и то же.
They're to get to privilege mode, there,|Они должны перейти в привилегированный режим, вот,
these are your privilege mode passwords.|это ваши пароли привилегированного режима.
The secret is encrypted with an md5 hash,|Секрет зашифрован хешем md5,
it will override the plain text password of Cisco, all right?|он заменит простой текстовый пароль Cisco, хорошо?
So, that's what the these two passwords are.|Итак, вот что это за два пароля.
Why do we have these two passwords on there?|Почему у нас там эти два пароля?
In case we need to revert to an older iOS that does not understand the the secret syntax, so then we go SERVICE PASSWORD-ENCRYPTION,|В случае, если нам нужно вернуться к более старой iOS, которая не понимает секретный синтаксис, тогда мы идем ШИФРОВАНИЕ ПАРОЛЯ СЛУЖБЫ,
all right,|отлично,
same thing, BANNER MOTD,|то же самое, BANNER MOTD,
message of the day.|сообщение дня.
Money sign, WELCOME, which it won't be,|Знак денег, ДОБРО ПОЖАЛОВАТЬ, чего не будет,
WELCOME TO switch 1, SW1.|ДОБРО ПОЖАЛОВАТЬ К переключателю 1, SW1.
And end it with a money sign.|И закончите это денежным знаком.
Symbols must be the same.|Символы должны быть одинаковыми.
So same things apply USERNAME LDIAZ Privilege,|То же самое относится к привилегиям USERNAME LDIAZ,
I type that,|Я печатаю это,
don't want to make any spelling mistakes,|не хочу делать орфографические ошибки,
USERNAME LDIAZ Privilege 15 administrator privileges, PASSWORD 0Cisco.|ИМЯ ПОЛЬЗОВАТЕЛЯ LDIAZ Привилегия 15 прав администратора, ПАРОЛЬ 0 Cisco.
Okay.|Ладно.
I don't, I'm not worried about the zero,|Я не волнуюсь за ноль,
zero means plain text because I have my source password hyphen encryption that uses seven to encrypt all plain text,|ноль означает простой текст, потому что у меня есть шифрование дефиса исходного пароля, которое использует семь для шифрования всего простого текста,
all plain text passwords,|все пароли в виде обычного текста,
past present and future.|прошлое настоящее и будущее.
So I'm not worried about that.|Так что меня это не беспокоит.
All right, let's do the IP DOMAIN-LOOKUP,|Хорошо, давайте проведем ПРОСМОТР IP-ДОМЕНА,
IP DOMAIN CISCO, oop,|IP ДОМЕН CISCO, oop,
sorry, IP DOMAIN NAME, -NAME,|извините, IP DOMAIN NAME, -NAME,
sorry, CISCO, IP NAME-SERVER.|извините, CISCO, IP ИМЯ-СЕРВЕР.
We'll just make up an address.|Мы просто составим адрес.
192.168.100.|192.168.100.
I don't know, 100.|Не знаю, 100.
That will be the name server.|Это будет сервер имен.
Okay.|Ладно.
We can then [SOUND] do lines.|Затем мы можем [ЗВУК] строить строки.
LINE VTY 0 space 15.|LINE VTY 0 пробел 15.
PASSWORD CISCO.|ПАРОЛЬ CISCO.
LOGING LOCAL.|ЛОКАЛЬНЫЙ ВХОД.
Right.|Правильно.
LOGGING, only two Gs, synchronous.|РЕГИСТРАЦИЯ, только две Г, синхронные.
One n, yes, of course.|Один н, да, конечно.
Oh, LOGGING, look at that.|О, ЖУРНАЛ, посмотрите на это.
LOGGING Synchronous, okay.|ЛОГИН Синхронный, хорошо.
EXEC-timeout, 0 minutes, 0 seconds.|EXEC-timeout, 0 минут, 0 секунд.
You can put ten minutes, zero seconds.|Можно поставить десять минут, ноль секунд.
What you need to remember is that the first number is minutes,|Вам нужно помнить, что первое число - это минуты,
second number is seconds.|второе число - секунды.
All right?|Отлично?
And then we can do TRANSPORT INPUT ALL,|И тогда мы можем сделать ВСЕ ТРАНСПОРТ,
where it could be telnet or SSH,|где это может быть telnet или SSH,
I can to show you both, all right?|Я могу показать вам обоих, хорошо?
We have to be on another LINE CON 0,|Мы должны быть на другом LINE CON 0,
let's do LINE CON 0, PASSWORD CISCO,|сделаем LINE CON 0, ПАРОЛЬ CISCO,
LOGGIN LOCAL, and then we do,|ВХОД ЛОКАЛЬНЫЙ, а затем мы,
[SOUND] same thing.|[ЗВУК] то же самое.
EXEc-timeout, 0 space 0.|EXEc-тайм-аут, 0 пробел 0.
And then LOGGing Synchronous, all right?|А потом LOGGing Synchronous, хорошо?
We'll do a DO WR or we exit exit copy run start.|Мы выполним DO WR или выйдем из режима запуска копирования.
Right, let's do EXIT, EXIT and then we're gonna do a show START now that we have a start to look at.|Хорошо, давайте сделаем EXIT, EXIT, а затем мы сделаем шоу START, теперь у нас есть начало смотреть.
So now we see that we have the service-password encryption,|Итак, теперь мы видим, что у нас есть шифрование служебного пароля,
we have the that's the Shift key we have the enable secret,|у нас есть клавиша Shift, у нас есть секрет включения,
take a look at the encryption,|взгляните на шифрование,
you know this from the routers.|вы знаете это по роутерам.
Okay.|Ладно.
And there's the username with,|И есть имя пользователя с
see how it the s,|Посмотри, как это с,
the server's password-encryption,|шифрование пароля сервера,
encrypted.|зашифрованный.
All plain text passwords using 7,|Все пароли в виде обычного текста с использованием 7,
all right, 7.|хорошо, 7.
All right.|Отлично.
Ain't nothing on our interfaces,|На наших интерфейсах ничего нет,
nothing on our interfaces, we haven't done nothing with the interfaces yet.|ничего на наших интерфейсах, мы еще ничего не сделали с интерфейсами.
We don't need to.|Нам не нужно.
Okay.|Ладно.
And we have our banner,|И у нас есть знамя,
we have our line con, and our line VTY,|у нас есть линия con и наша линия VTY,
which we actually configured that we can't do both TELNET and SSH.|который мы на самом деле настроили так, что не можем использовать одновременно TELNET и SSH.
Now remember I said that it was very important.|Теперь помните, я сказал, что это очень важно.
That you will be putting an IP address in interface VLAN 1,|Что вы будете помещать IP-адрес в интерфейс VLAN 1,
because you want to be able, as the IT admin or the main guy that's gonna go in there and, do changes you gotta go inside the native VLAN.|потому что вы хотите иметь возможность, как ИТ-администратор или главный специалист, который собирается войти туда и внести изменения, вы должны войти в собственную VLAN.
So you go INT VLAN 1,|Итак, вы идете INT VLAN 1,
you go IP ADDRESS, and let's say,|вы вводите IP-АДРЕС, и скажем,
this would be, I guess an example,|это будет, я думаю, пример,
192.168, oops.|192.168, упс.
168.100.253.|168.100.253.
255.255.255.0.|255.255.255.0.
Enter, and then we need to turn on, no shut.|Вступаем, а потом надо включать, не закрывать.
Okay, save change state to all.|Хорошо, сохраните изменение состояния для всех.
All right, but we need to go back to privilege mode and put a default gateway.|Хорошо, но нам нужно вернуться в режим привилегий и установить шлюз по умолчанию.
Because if your remote to the switch,|Потому что, если ваш пульт к переключателю,
whether your in another broadcast domain,|находитесь ли вы в другом широковещательном домене,
think of it that way, your in another broadcast domain that means you are remote to the switch,|подумайте об этом так, вы находитесь в другом широковещательном домене, что означает, что вы удалены от коммутатора,
you need that IP DEfault-gateway.|вам нужен этот IP-шлюз DEfault.
You need that, and that's gonna be your router's LAN.|Вам это нужно, и это будет локальная сеть вашего маршрутизатора.
The one that's at zero zero or at zero one, whatever's pointed down,|Тот, что в ноль ноль или в ноль, в зависимости от того, что направлено вниз,
that's connected to the switch.|это связано с переключателем.
So, 192.168.100.254.|Итак, 192.168.100.254.
So, these are, I don't know if I missed any, I don't think so.|Итак, я не знаю, пропустил ли я что-нибудь, я так не думаю.
Didn't give you more then I should have.|Не дал тебе больше, чем должен был.
All right, because you won't really be doing all this.|Хорошо, потому что на самом деле ты не будешь делать все это.
You need to understand what these are,|Вам нужно понять, что это такое,
like the IP domain name Cisco.|вроде IP-имени домена Cisco.
All right,|Отлично,
you know that's forward name resolution,|вы знаете, что это прямое разрешение имен,
all right, the username is just so you can have a username for privileged mode.|хорошо, имя пользователя такое, чтобы вы могли иметь имя пользователя для привилегированного режима.
People need to log in using a username and password.|Людям необходимо войти в систему, используя имя пользователя и пароль.
Okay, go down through the interfaces here,|Ладно, пройдемся по интерфейсам здесь,
fairly quickly.|довольно быстро.
You see,|Ты видишь,
did I do a copy run start on this WR?|я сделал запуск копирования на этой WR?
let's do it again, show start,|давай сделаем это снова, покажи старт,
space, space, there you go,|космос, космос, вот и вы,
there's my IP address 192.168.100.253 for VLAN1, and there's my default gateway, and there's the rest of my configuration.|вот мой IP-адрес 192.168.100.253 для VLAN1, есть мой шлюз по умолчанию и остальная часть моей конфигурации.
So, you see, it's pretty similar.|Итак, видите, это очень похоже.
Slight changes because you're going inside a VLAN interface, all right,|Небольшие изменения, потому что вы входите в интерфейс VLAN, хорошо,
to put the IP address of the switch.|поставить IP-адрес коммутатора.
And in global configuration, you're putting the default gateway of the switch,|А в глобальной конфигурации вы устанавливаете шлюз коммутатора по умолчанию,
which is your router's LAN interface,|который является интерфейсом LAN вашего маршрутизатора,
the one that's facing the LAN.|тот, что стоит перед ЛВС.
That is the interface, that is the gateway for the switch, just like that would be the gateway for your PCs, it will be the gateway for your switch, all right?|Это интерфейс, это шлюз для коммутатора, точно так же, как он будет шлюзом для ваших ПК, он будет шлюзом для вашего коммутатора, хорошо?
So, we've assigned the IP address to that particular switch.|Итак, мы назначили IP-адрес именно этому коммутатору.
We gave it a gateway.|Мы дали ему шлюз.
We did all the admin commands we've done before in the router.|Мы выполнили все команды администратора, которые делали раньше, в маршрутизаторе.
So, now we're done, we're done with the administration commands.|Итак, теперь мы закончили, мы закончили с командами администрирования.
And now, we begin to start doing things like VLANs and VTP and STP.|А теперь мы начинаем делать такие вещи, как VLAN, VTP и STP.
And we start messing around with all those and we'll start explaining the,|И мы начинаем возиться со всем этим, и мы начнем объяснять,
you know, how to tweak all these different things and how to go about it, all right?|вы знаете, как настроить все эти разные вещи и как это сделать, хорошо?
I'll see you in the next session.|Увидимся на следующем сеансе.