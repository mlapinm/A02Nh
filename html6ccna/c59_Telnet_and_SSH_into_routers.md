D:\mailCloud\prjother\tmp\1\c59_Telnet and SSH into routers.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
Okay, welcome back everyone.|Хорошо, с возвращением всех.
Now that we fully configured our routers,|Теперь, когда мы полностью настроили наши маршрутизаторы,
we did the administrative configurations or the basic housekeeping, right.|мы сделали административную настройку или базовое обслуживание, верно.
And then we did the interfaces, now we did configure it differently on both routers.|Затем мы сделали интерфейсы, теперь мы настроили его по-разному на обоих маршрутизаторах.
And did we do it?|И мы это сделали?
Yeah, we did the interfaces on this one and then, on this one,|Да, мы сделали интерфейсы на этом, а потом на этом
we actually did it in notepad.|мы действительно сделали это в блокноте.
We did both the administrator and the interfaces right on notepad and paste it in.|Мы сделали и администратора, и интерфейсы прямо в блокноте и вставили его.
So, two ways that you can configure routers.|Итак, два способа настройки роутеров.
But, now that they're configured, you'll be able from you're computer, all right,|Но теперь, когда они настроены, вы сможете со своего компьютера, хорошо,
to either, through the command prompt to telnet or SSH into your router.|либо через командную строку, чтобы подключиться к маршрутизатору по telnet или SSH.
Cuz that's the reality of it.|Потому что это реальность.
The reality is that you're gonna be sitting in your office,|Реальность такова, что ты будешь сидеть в своем офисе,
your nice captain's chair, drink your coffee.|ваше милое капитанское кресло, пейте кофе.
You'll get a call, hey, can you please telnet?|Тебе позвонят. Эй, можешь телнет?
You'll telnet in right?|Ты будешь использовать телнет?
Or your ssh in into your router.|Или подключите ssh к маршрутизатору.
You're not gonna be sitting inside the telecommunications closet you know,|Знаешь, ты не будешь сидеть в телекоммуникационном шкафу,
doing it like that.|делать это вот так.
You're gonna be somewhere else in the ssh in.|Ты будешь где-нибудь еще в ssh.
So I'll show you how to do that.|Итак, я покажу вам, как это сделать.
First let's see if we have connectivity with our own gateway.|Сначала посмотрим, есть ли у нас подключение к нашему собственному шлюзу.
So let's take a look with IP config.|Итак, давайте посмотрим на конфигурацию IP.
Let's take it step by step.|Давайте рассмотрим это шаг за шагом.
IPCONFIG.|IPCONFIG.
Space.|Космос.
ALL.|ВСЕ.
Cuz you really know you don't have to.|Потому что ты действительно знаешь, что тебе не нужно.
Right?|Правильно?
But here, being the packet tracer,|Но здесь, будучи трассировщиком пакетов,
it wants you to do that space.|он хочет, чтобы вы занимали это место.
You really don't have to.|Вам действительно не нужно.
All right?|Отлично?
And you see that you have your IPs.|И вы видите, что у вас есть свои IP.
[BLANK_AUDIO]|[BLANK_AUDIO]
It likes my finger now.|Теперь ему нравится мой палец.
So you have the IPs and the gateways.|Итак, у вас есть IP-адреса и шлюзы.
So let's go ahead and PING the gateway.|Итак, давайте продолжим и отправим PING на шлюз.
192.168.1.254.|192.168.1.254.
And we have gone through the gateway, so we should be able to Telnet.|И мы прошли через шлюз, так что мы можем подключиться к Telnet.
So let's Telnet space 192.168.1.254,|Итак, давайте займемся Telnet 192.168.1.254,
user name, why is it asking us for a user name?|имя пользователя, почему он запрашивает у нас имя пользователя?
Because we created a user name.|Потому что мы создали имя пользователя.
If we wouldn't have done that log in local, it would have not prompted us for a user name.|Если бы мы не делали этот вход локально, он не запрашивал бы у нас имя пользователя.
So, l Diaz, enter, Cisco, C-I-S-C-O,|Итак, Диас, входи, Cisco, C-I-S-C-O,
enter.|войти.
Now we're in privileged mode.|Теперь мы в привилегированном режиме.
You see that we went straight to privileged mode.|Как видите, мы сразу перешли в привилегированный режим.
We didn't go to user mode, we went straight into privileged mode.|Мы не перешли в пользовательский режим, мы сразу перешли в привилегированный режим.
Why is that?|Это почему?
Because since we're using the local username and password, that username has level 15 privilege, administrative privilege, that way we can bypass that.|Поскольку, поскольку мы используем локальное имя пользователя и пароль, это имя пользователя имеет привилегию 15 уровня, административную привилегию, таким образом мы можем обойти это.
So that is telnetting, but that is basi,|Итак, это телнетинг, но это в основном,
that is plain text that we went is not, it's not as secure as SSH.|это обычный текст, который мы пошли не так, он не так безопасен, как SSH.
So, let's exit out,|Итак, выходим,
cuz we did do the command transport input as all, so we're able to SSH as well.|потому что мы сделали ввод команды транспорта как все, поэтому мы также можем использовать SSH.
So, we're gonna type SSH minus L to log in.|Итак, мы собираемся ввести SSH минус L, чтобы войти в систему.
Username, L diaz and then the I-P address 192.168.1.254.|Имя пользователя, L diaz, а затем IP-адрес 192.168.1.254.
Password, cisco.|Пароль, cisco.
And now again, I am in router one.|И вот снова я на первом роутере.
So that is tail natting and SSHing, if that's even a word.|Так что это хвостовая натяжка и SSHing, если это хоть слово.
All right well how we SSH into the router,|Хорошо, как мы SSH в маршрутизатор,
and this is something that you do want to set up, and you will set it up on a user name basis, so you will do login local.|и это то, что вы действительно хотите настроить, и вы настроите его на основе имени пользователя, поэтому вы будете входить в систему локально.
For your test, for your CCNA certification,|Для вашего теста, для вашей сертификации CCNA,
they don't go that far, they'll ask you questions, you know, icon zero,|они не заходят так далеко, они будут задавать вам вопросы, ну, ну значок,
password assist, go to login, that's fine.|помощь с паролем, войдите в систему, все в порядке.
Now what is exec hyphen timeout zero minutes zero seconds.|Теперь что такое время ожидания выполнения дефиса ноль минут ноль секунд.
That is what you need to know.|Это то, что вам нужно знать.
What is log in synchronous?|Что такое синхронный вход?
Again, so your typing will stay on the same line it won't be interrupted.|Опять же, так что ваш набор текста останется на той же строке, он не будет прерван.
And when you're telnetting in, one of the things that they ask you is,|И когда вы подключаетесь через telnet, вас спрашивают,
when you telnet.|когда вы телнет.
If you didn't configure telnet, you get an error message that states password required but none set.|Если вы не настраивали telnet, вы получите сообщение об ошибке, в котором указано, что пароль требуется, но не установлен.
So, if you're trying to telnet or SSH,|Итак, если вы пытаетесь использовать telnet или SSH,
into a certain location it will probably [INAUDIBLE] into a refused by remote host.|в определенное место он, вероятно, [НЕИЗБЕЖНО] будет отклонен удаленным хостом.
But if you, if you try to telnet it in,|Но если вы попытаетесь подключиться через telnet,
you will get that error back.|вы получите эту ошибку обратно.
So, basically hey, you call, hey you need to configure your telnet it's giving me this error, meaning the other side has not|Итак, в основном эй, вы звоните, эй, вам нужно настроить свой телнет, он выдает мне эту ошибку, что означает, что другая сторона не
configured there telnet lines.|настроил там линии telnet.
So, that is the line of questioning that you're going to get on your examination.|Итак, это вопрос, который вам предстоит задать на экзамене.
For this particular, you know, type of configuration.|Для этого конкретного типа конфигурации.
You're not going to have to configure SSH,|Вам не нужно настраивать SSH,
you're not going to have to configure telnet, you're going to need to know that in order to configure telnet,|вам не нужно настраивать telnet, вам нужно знать, что для настройки telnet,
you need to do you [INAUDIBLE] and if you want to open one or two [INAUDIBLE].|вам нужно сделать [НЕРАЗБОРЧИВО] и, если вы хотите открыть один или два [НЕРАЗБОРЧИВО].
You don't have to do space, 0 space 15.|Вам не нужно делать пробел, 0 пробел 15.
You're going to do just 1 line bty 1, and you'll open 1.|Вы собираетесь сделать только 1 строку bty 1, и вы откроете 1.
If you want the passwords to be encrypted,|Если вы хотите, чтобы пароли были зашифрованы,
all those passwords at the bottom.|все эти пароли внизу.
Like the user name password, or the passwords for the console,|Например, пароль от имени пользователя или пароли для консоли,
the line, the aux.|линия, доп.
You use that service password-encryption.|Вы используете эту службу шифрования паролей.
So things like that is what they're gonna ask you on the examination, but at least for real world, you'll know now how to, telnet into a router, or|Такие вещи - вот что они будут спрашивать у вас на экзамене, но, по крайней мере, в реальном мире вы теперь знаете, как подключиться к маршрутизатору через telnet или
SSH into a router, cuz there is your syntax right there, okay?|SSH в маршрутизатор, потому что там есть ваш синтаксис, хорошо?
Next lesson, what we are going to get into is a bunch of show commands that you really need to understand and use that's going to help you look at your router and|В следующем уроке мы рассмотрим набор команд show, которые вам действительно нужно понять и использовать, которые помогут вам взглянуть на свой маршрутизатор и
how to troubleshoot it.|как это исправить.
I'll see you then.|Увидимся тогда.
[BLANK_AUDIO]|[BLANK_AUDIO]