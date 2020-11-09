D:\mailCloud\prjother\tmp\1\c114_SYSLOG and its Configuration.md  


__|__
--|--
Welcome back.|Добро пожаловать.
Alright, we did SNMP, now we know that we can get some management software and,|Хорошо, мы сделали SNMP, теперь мы знаем, что можем получить программное обеспечение для управления и,
have SNMP as the underlying protocol to manage our devices and get information from it.|использовать SNMP в качестве основного протокола для управления нашими устройствами и получения от них информации.
Another one that Cisco threw in the mix as well is Syslog.|Еще одна вещь, которую Cisco добавила в смесь, - это Syslog.
These are system messages.|Это системные сообщения.
You know how we do login synchronous?|Вы знаете, как мы выполняем синхронный вход в систему?
When we go to the console line so our typing doesn't get interrupted because the router gives us feedback every time something happens.|Когда мы переходим к строке консоли, чтобы не прерывать набор текста, потому что маршрутизатор дает нам обратную связь каждый раз, когда что-то происходит.
We're like, oh my god,|Мы такие, боже мой,
my typing gets interrupted.|мой набор текста прерывается.
Turn it off.|Выключи это.
No, don't turn it off, just put it where it won't interrupt your typing.|Нет, не выключайте его, просто положите туда, где он не будет мешать вам печатать.
You need those system messages to come up,|Вам нужно, чтобы эти системные сообщения появлялись,
and let's go on this router this time.|и давайте на этот раз перейдем к этому роутеру.
Okay, you want, let's say, do.|Ладно, хочешь, скажем, делаешь.
Okay.|Ладно.
I'll maximize this.|Я максимизирую это.
Let's do, do.|Давай, делаем.
Come on.|Давай.
Oh, not do.|О, не надо.
Show IP INT BRIEF.|Показать краткое изложение IP INT.
Okay.|Ладно.
CONFIG T.|КОНФИГ T.
You see how enter configuration, okay.|Вы видите, как войти в конфигурацию, ладно.
All that is system messages.|Все это системные сообщения.
Let's see if I can generate one here.|Посмотрим, смогу ли я создать его здесь.
[SOUND] let's go to INT G0/0.|[ЗВУК] переходим к INT G0 / 0.
I'll do SHUT.|Я сделаю ВЫКЛЮЧЕНИЕ.
All right.|Все в порядке.
That right there is,|Это прямо есть,
that's the message is giving you,|это сообщение дает вам,
hey something went down,|эй что-то упало,
something just happened.|что-то только что произошло.
Right?|Правильно?
Even when you're configuring,|Даже когда вы настраиваете,
if you turn it back on.|если снова включить.
You go, you know, NO SHUT.|Вы идете, знаете, НЕ ЗАКРЫТЬ.
All these things that keeps giving you back when you're putting in clock rates,|Все эти вещи, которые возвращают вас, когда вы устанавливаете тактовую частоту,
when you're putting in,|когда вы вставляете,
turning on interfaces.|включение интерфейсов.
Everything that comes up,|Все, что приходит,
it'll let you know that, you know,|это даст вам знать, вы знаете,
that you're configuring all these different things.|что вы настраиваете все эти разные вещи.
Exit, lets say like LINE CON 0.|Выход, скажем, как LINE CON 0.
PASSWORD, CISCO, LOGIN.|ПАРОЛЬ, CISCO, ВХОД.
All right?|Все в порядке?
Let's do a DO WR.|Сделаем DO WR.
When you start configuring your router as we have done, you've seen that as every time we've done something, a message will come up, a message will come up.|Когда вы начинаете настраивать свой маршрутизатор, как это сделали мы, вы видели, что каждый раз, когда мы что-то делаем, появляется сообщение, появляется сообщение.
Those are system messages.|Это системные сообщения.
That's what Syslog is for,|Вот для чего нужен Syslog,
to log all those system messages.|для регистрации всех этих системных сообщений.
Now, Syslog has different severity levels.|Теперь у Syslog разные уровни серьезности.
It's funny because on the package tracer,|Забавно, потому что на трассировщике упаковки
it only has seven.|их всего семь.
Okay?|Ладно?
You have really, zero through seven.|У вас действительно от нуля до семи.
Zero meaning that the device itself,|Ноль означает, что само устройство,
it's all unusable.|это все непригодно.
I mean,|Я имею в виду,
something's really bad just happened.|что-то действительно плохое только что случилось.
Seven is like debugging.|Семерка похожа на отладку.
And that's all the bad trenches report.|И это все отчеты о плохих окопах.
But we'll do it, so you can see the messages that keep popping up.|Но мы сделаем это, чтобы вы могли видеть сообщения, которые продолжают появляться.
Okay?|Ладно?
And I'll show you how to set that up.|И я покажу вам, как это настроить.
Now, you won't use on,|Теперь ты не будешь использовать,
at least in this case you will not use the PC, you'll actually use the server.|по крайней мере, в этом случае вы не будете использовать ПК, вы фактически будете использовать сервер.
Let me maximize it for you.|Позвольте мне максимизировать это для вас.
You go to the config tab, and you go to Syslog, all right, and you see that it's on, and right now nothing's happening,|Вы переходите на вкладку config, и вы заходите в Syslog, хорошо, и вы видите, что он включен, и прямо сейчас ничего не происходит,
nothing's happening at this moment.|в данный момент ничего не происходит.
But, something will happening shortly.|Но что-то скоро произойдет.
Okay, when we turn on logging, all right?|Хорошо, когда мы включим ведение журнала, хорошо?
So, you do wanna turn on logging, and if you do a question mark under global configuration.|Итак, вы хотите включить ведение журнала, и если вы поставите вопросительный знак в глобальной конфигурации.
I don't know what keeps going on with this thing.|Я не знаю, что происходит с этой штукой.
All right,|Все в порядке,
you go under global configuration.|заходишь под глобальную конфигурацию.
It says logging.|Там написано ведение журнала.
All right, you go LOGGING,|Ладно, иди ЛОГИНЬ,
you put a question mark, and I know I said incomplete command, but there's a reason I just wanted to bring up so you can see it.|вы поставили вопросительный знак, и я знаю, что сказал неполная команда, но есть причина, по которой я просто хотел поднять, чтобы вы ее увидели.
Logging in okay,|Вход в систему нормально,
what IP addresses do you want to log?|какие IP-адреса вы хотите регистрировать?
Meaning what devices do you want to log.|Это означает, какие устройства вы хотите регистрировать.
Buffered is pretty much on by default,|Буферизация включена по умолчанию,
cuz you can,|потому что ты можешь,
how much memory allocation you wanna have.|сколько памяти вы хотите выделить.
Console set to logging parameters.|Консоль настроена на параметры регистрации.
You can, that's on by default.|Можно, по умолчанию это включено.
Host on.|Хост на.
What you're most, worried about is trap.|Больше всего вас беспокоит ловушка.
Set the Syslog server logging level.|Установите уровень ведения журнала сервера системного журнала.
If, if you.|Если, если ты.
Turn on let's say,|Включите, скажем,
normally you would turn on five.|обычно вы включаете пять.
Because you gonna get information from zero to five.|Потому что вы получите информацию с нуля до пяти.
If you turn on seven,|Если включить семь,
it's going to give you all of them.|это даст вам их все.
So, it could be that maybe that work station or server that you're using to manage the Syslog, information it's gonna get|Так что, возможно, рабочая станция или сервер, который вы используете для управления системным журналом, информация, которую он получит
a bunch of information and may overwhelm it or just too much to keep track of.|куча информации, которая может подавлять ее или просто слишком много, чтобы отслеживать ее.
So, normally five is the middle ground.|Итак, обычно пять - это золотая середина.
So you need to know those severity levels four or five,|Итак, вам нужно знать четыре или пять уровней серьезности,
that's the pretty much everybody uses those to manage.|это почти все используют их для управления.
Okay.|Ладно.
It's like the halfway point.|Это похоже на полпути.
Okay?|Ладно?
So what we do is we'll say, we'll go LOGGING, and we'll log, let's say,|Итак, что мы делаем, мы говорим, мы пойдем в ЛОГИН, и мы войдем, скажем,
let's find some IP addresses to log.|давайте найдем несколько IP-адресов для регистрации.
Let's log our own server.|Давайте зарегистрируем наш собственный сервер.
What's the IP address of the server is 1.1, and this one is 3.1, okay?|Какой у сервера IP-адрес 1.1, а этот 3.1, хорошо?
So let's maximize this.|Так что давайте максимизировать это.
So, we're gonna go LOGGING,|Итак, мы собираемся ЛОГИНЬ,
192.168.1.1, all right?|192.168.1.1, ладно?
And then,|А потом,
you see that's there nothing else,|Вы видите, что больше ничего нет,
and now you see right here sys severity level 6.|и теперь вы видите здесь уровень серьезности sys 6.
This is a Syslog message.|Это сообщение системного журнала.
Let me bring it up, so you can see it better.|Позвольте мне поднять это, чтобы вам было лучше.
Okay, all right,|Ладно ладно,
this is your Syslog right here.|это ваш системный журнал прямо здесь.
The severity level of 6.|Уровень серьезности 6.
Sub component, logging host.|Подкомпонент, хост регистрации.
Logging to host 192.168.1.1 on port 514.|Вход на хост 192.168.1.1 через порт 514.
And that's started.|И вот началось.
Okay.|Ладно.
So we're going to do an up arrow again.|Итак, мы снова сделаем стрелку вверх.
And now we're going to do 3.1.|А теперь займемся 3.1.
Okay, now that's logging as well,|Хорошо, теперь это тоже ведение журнала,
okay, for us.|хорошо, для нас.
So, usually, you wanna use a remote server anyway, to do this, all right?|Итак, как правило, вы все равно хотите использовать удаленный сервер, хорошо?
To send the messages to.|Для отправки сообщений.
You don't wanna do it on the router.|Вы не хотите делать это на роутере.
All right, and then we're gonna set the trap, which is funny,|Хорошо, а потом мы поставим ловушку, что забавно,
because when we put TRAP, right?|ведь когда мы ставим ЛОВУШКУ, да?
There's what we get.|Вот что мы получаем.
You can apply, you really can put the number which is severity of seven as you can see right here.|Вы можете подать заявку, вы действительно можете указать степень серьезности семь, как вы можете видеть прямо здесь.
And If you can, I'll bring it up,|И если сможешь, я подниму это,
i'll bring it up.|я подниму это.
All right, severity is seven,|Ладно, тяжесть семь,
that's the high, the highest.|это высокий, самый высокий.
Lowest is zero but it's really kinda backwards, cause zero is like the worst.|Наименьшее значение равно нулю, но на самом деле это не так, потому что ноль - это худшее.
Okay?|Ладно?
So we'll put debugging.|Так что поставим отладку.
Oops.|Ой.
LOGGING TRAP DEBUGGING.|ЛОВУШКА РЕГИСТРАЦИИ ОТЛАДКА.
So now that's on.|Итак, вот и все.
DO WR, and it's gonna take these messages on both these servers.|DO WR, и он будет принимать эти сообщения на обоих серверах.
So what we're gonna do is, let's do it from right here on this router.|Итак, что мы собираемся сделать, давайте сделаем это прямо здесь, на этом маршрутизаторе.
And I believe that we're running is RIP,|И я считаю, что мы работаем, это RIP,
if I'm not mistaken.|если я не ошибаюсь.
Sure are.|Конечно.
So we're gonna debug IP RIP, and that's to make things work quickly.|Итак, мы собираемся отладить IP RIP, чтобы все работало быстро.
DEBUG IP RIP, all right, so now you know that RIP, every 30 seconds,|DEBUG IP RIP, хорошо, теперь вы знаете, что RIP, каждые 30 секунд,
it's actually sending information back and forth, back and forth, back and forth.|на самом деле он отправляет информацию туда и обратно, назад и вперед, назад и вперед.
So let's take a look at our,|Итак, давайте посмотрим на наши,
and you can see already that you're getting messages that say,|и вы уже видите, что получаете сообщения, в которых говорится:
hey, configured from console by console.|эй, настраивается с консоли на консоли.
When I started the sixth,|Когда я начал шестой,
the first one that I did, boom.|первый, который я сделал, бум.
Now I'm getting, you scared me.|Теперь я понимаю, ты меня напугал.
It, it gave me that, hey,|Это дало мне это, эй,
I'm getting updates from version two.|Я получаю обновления со второй версии.
All right?|Все в порядке?
From the other router, so you can see how you can keep track of what's going on.|С другого маршрутизатора, чтобы вы могли видеть, как вы можете отслеживать, что происходит.
So if RIP goes down, you take a look at your management workstation.|Поэтому, если RIP выйдет из строя, вы посмотрите на свою рабочую станцию ​​управления.
You say, oh.|Вы говорите, о.
Okay.|Ладно.
Let me read that.|Позвольте мне это прочитать.
Oh, yes.|О да.
The.|Файл.
I'm not getting any,|Я ничего не получаю,
any RIP updates from the other router.|любые обновления RIP от другого маршрутизатора.
Okay.|Ладно.
That's a problem.|Это проблема.
All right?|Все в порядке?
So this is what Syslog is all about.|Вот в чем суть Syslog.
What is it that you need to know?|Что вам нужно знать?
You need to know that, the severity levels, severity levels, not in detail.|Вы должны знать это, уровни серьезности, уровни серьезности, а не в деталях.
Just know that there's zero to seven,|Просто знай, что есть от нуля до семи,
and more or less what each one does.|и более или менее то, что делает каждый.
That's it.|Вот и все.
More or less what each one does,|Более или менее то, что делает каждый,
so find key words to learn those,|так что найдите ключевые слова, чтобы выучить их,
those severity levels.|эти уровни серьезности.
It's zero through seven.|С нуля до семи.
Know how to turn it on in the router.|Знайте, как включить его в роутере.
Now, all you really need to do is just do the login trap.|Теперь все, что вам действительно нужно сделать, это просто выполнить ловушку входа в систему.
And the, the login IP address,|И IP-адрес для входа,
and then the login trap.|а затем ловушка входа в систему.
Where are you going to trap,|Где ты собираешься заманить,
or capture, these messages coming back from your router?|или перехватить эти сообщения, приходящие с вашего роутера?
Those system messages that the router is sending you.|Те системные сообщения, которые отправляет вам маршрутизатор.
Because, we picked two servers.|Потому что мы выбрали два сервера.
So, I should be seeing it on this server as well.|Так что я тоже должен увидеть это на этом сервере.
On that other server.|На том другом сервере.
That 3.1 server.|Тот сервер 3.1.
Let's take a look at that.|Давайте посмотрим на это.
Oh, not there, config.|Ой, не там, конфиг.
Syslog.|Системный журнал.
And, I see it there as well,|И я тоже это вижу,
because I chose two servers to get that information in.|потому что я выбрал два сервера для получения этой информации.
Okay?|Ладно?
So that's where,|Так вот где,
that's where those IP addresses were.|вот где были эти IP-адреса.
Then I'm gonna be sending these Syslog messages to a particular server, or workstation, or whatever it is.|Затем я собираюсь отправить эти сообщения системного журнала на конкретный сервер, рабочую станцию ​​или что-то еще.
To go ahead and capture these particular system messages.|Чтобы продолжить и записать именно эти системные сообщения.
And you never, ever, wanna turn that off.|И ты никогда, никогда не захочешь это выключить.
But again, for your cert, for your cert, what is it you wanna do?|Но опять же, для вашего сертификата, для вашего сертификата, что вы хотите сделать?
You wanna go ahead and remember those traps, those,|Вы хотите идти вперед и помнить эти ловушки, те,
the severity levels, I'm sorry.|уровни серьезности, извините.
The severity levels, and that you wanna send things through a remote server, right.|Уровни серьезности и то, что вы хотите отправлять сообщения через удаленный сервер, верно.
The IP address of a remote server,|IP-адрес удаленного сервера,
and you do that by using,|и вы делаете это, используя,
you know putting the IP address.|вы знаете, ставя IP-адрес.
And then the severity levels you do it by saying, hey, login trap.|А затем уровни серьезности, которые вы делаете, говоря: эй, ловушка входа.
So that's pretty much it.|Вот и все.
But know that, hey,|Но знай, эй,
you're picking up system messages.|вы забираете системные сообщения.
And you saw it at the very beginning,|И ты видел это в самом начале,
I don't know that you can see it here cuz we've passed over too much.|Не знаю, можно ли здесь это увидеть, потому что мы слишком многое пропустили.
But was at SYS,|Но был в SYS,
telling you it's a Syslog, message.|говорю вам, что это системный журнал, сообщение.
The sever, the next one was a number that gives you the severity level, all right?|Следующий, следующий был числом, который дает вам уровень серьезности, хорошо?
And then it was a sub-component, and then an explanation of where it's going, so that's all Syslog is.|Затем это был подкомпонент, а затем объяснение того, куда он идет, так что это все, что есть Syslog.
But again, ladies and gentlemen,|Но опять же, дамы и господа,
you're not gonna be doing that.|ты не собираешься этого делать.
You're not gonna be doing that, on a real world scenario, something like this.|Вы не собираетесь делать это в реальном мире, что-то вроде этого.
It will be some sort of third party management software,|Это будет какое-то стороннее программное обеспечение для управления,
that's gonna be a lot easier to look at.|на это будет намного легче смотреть.
All this is, is so you understand what Syslog is, just like SNMP, which is the underlying protocol that you would configure on this management software, and|Все это для того, чтобы вы понимали, что такое Syslog, точно так же, как SNMP, который является основным протоколом, который вы должны настроить в этом программном обеспечении для управления, и
on the router, so they can talk back and forth, right?|на роутере, чтобы они могли разговаривать туда-сюда, верно?
They gotta be identical configs.|Конфиги должны быть идентичными.
They can talk back and forth.|Они могут разговаривать взад и вперед.
And then you gonna see what's going on your, on your network.|А потом вы увидите, что происходит в вашей сети.
Because one of the main things that you want to see what's going on is.|Потому что одна из главных вещей, которые вы хотите увидеть, - это.
Let's say they, Syslog is giving you,|Допустим, Syslog дает вам,
okay, you're monitoring the system and what have you.|ладно, вы следите за системой и при чем здесь.
The SNMP is like,|SNMP похож на
wait a minute, our bandwidth.|подождите, наша пропускная способность.
What's going on with our bandwidth?|Что происходит с нашей пропускной способностью?
We have hardly any.|У нас почти нет.
You go to your boss.|Вы идете к своему боссу.
You go whoever's in charge in IT.|Вы идете к тому, кто отвечает за ИТ.
You know, it goes, you get, obviously,|Вы знаете, это идет, вы, очевидно, получаете
you're getting help desk tickets.|вы получаете билеты в службу поддержки.
With SNMP, it's, like, hey,|С SNMP это вроде как, эй,
we got no more bandwidth.|у нас больше нет полосы пропускания.
Well, what do you mean?|Ну что ты имеешь в виду?
He goes, you know they're gonna ask you,|Он идет, ты знаешь, они тебя спросят,
well, why is the bandwidth so high?|ну почему пропускная способность такая высокая?
Nobody knows that Laz is playing Call of Duty on bandwi, on, on war time.|Никто не знает, что Лаз играет Call of Duty на бандви, в военное время.
Then that's a problem right?|Тогда это проблема?
But none of those two are going to tell you who this next one is.|Но никто из этих двоих не скажет вам, кто этот следующий.
Netflow.|Поток данных, передающихся по сети.
The next one is the one unfortunately doesn't have the configuration for it.|Следующий, к сожалению, не имеет соответствующей конфигурации.
But all it is is turning numbers.|Но все дело в цифрах.
I'll explain it to you next.|Я объясню вам это дальше.
All right so,|Ладно так,
I'll see you in the next lesson,|Увидимся на следующем уроке,
and we'll talk about net flow for a little bit.|и поговорим немного о чистом потоке.
See you then.|Тогда увидимся.
  
