D:\mailCloud\prjother\tmp\1\c104_Understanding the CIR and Burst Rate.md  


__|__
--|--
Welcome, everyone.|Добро пожаловать.
I have traveled through time,|Я путешествовал во времени,
as you can see, so I can explain to you in bite-sized morsels, frame relay.|Как видите, я могу объяснить вам в небольших количествах, Frame Relay.
Frame relay is the most confusing one to understand.|Frame Relay - самый непонятный для понимания.
Not that it's confusing to configure,|Не то чтобы это сбивало с толку,
it just has a little different I guess you want to say, components to it.|у него просто немного другие, я думаю, вы хотите сказать, компоненты к нему.
And there's a lot of different ways of configuring frame relay, okay?|И есть много разных способов настройки Frame Relay, хорошо?
The first two things that we need to be aware of in frame relay is these two terms,|Первые две вещи, о которых нам нужно знать в Frame Relay, - это эти два термина,
your CIR and your access rate.|ваш CIR и скорость доступа.
Your CIR is your committed,|Ваш CIR - это ваша приверженность,
I don't know about the spelling here,|Я не знаю, как здесь написано,
committed information rate.|фиксированная скорость передачи информации.
This is what's guaranteed.|Это то, что гарантировано.
Guaranteed.|Гарантированно.
Wow, I can't spell today.|Вау, сегодня я не умею писать.
I don't know.|Я не знаю.
All right.|Все в порядке.
Meaning that this is what, if you,|Это значит, что если вы,
let's say you call your provider.|допустим, вы звоните своему провайдеру.
Let's say, for example,|Скажем, например,
it's AT&T, or whoever.|это AT&T или кто-то еще.
And you say, listen,|И вы говорите, слушайте,
I wanna run a frame relay and I only need 256 kilobits per second.|Я хочу запустить Frame Relay, и мне нужно всего 256 килобит в секунду.
So 256K, all right, that's all,|Так что 256К, ладно, и все,
that's all you require.|это все, что вам нужно.
So that's what they're gonna guarantee you, that is what that CIR is.|Вот что они вам гарантируют, вот что такое CIR.
So from zero, or let's say 33 kilobits per second,|Итак, с нуля, или, скажем, 33 килобита в секунду,
up to 256 kilobits per second,|до 256 килобит в секунду,
they will guarantee you that traffic.|они гарантируют вам этот трафик.
Now, you can, you'll,|Теперь ты можешь, ты,
you can purchase an access rate.|вы можете приобрести скорость доступа.
Of, lets say T1, all right,|Ну, скажем, Т1, хорошо,
a whopping, mega, megabits per second,|колоссальные, мега, мегабиты в секунду,
all right, that's not guaranteed.|хорошо, это не гарантировано.
Anything above 256, it's not guaranteed.|Все, что выше 256, не гарантируется.
If the telco has it available for you, then it will send it.|Если у телефонной компании он есть в наличии, он его отправит.
But if you go beyond that, and I'll give you a sneak peak into the future since I, I can travel through time.|Но если вы выйдете за рамки этого, и я дам вам заглянуть в будущее, так как я, я могу путешествовать во времени.
It will mark those bits that go beyond your CIR with something called a DE.|Он пометит те биты, которые выходят за пределы вашего CIR, с помощью так называемого DE.
I'll put that there.|Я положу это туда.
And I, I'll put a little statement here.|И я, я сделаю здесь небольшое заявление.
If you surpass, the CIR,|Если вы превзойдете, CIR,
the bits will be marked.|биты будут отмечены.
I'll get out of the way so you can see it.|Я уйду с дороги, чтобы ты это увидел.
With D.|Вместе с Д.
I'll put it in quotes.|Я заключу это в кавычки.
Quotes DE.|Котировки DE.
Okay?|Ладно?
So if you go beyond your 256,|Итак, если вы выйдете за пределы своих 256,
which is what they're guaranteeing you,|что они вам гарантируют,
because this is what you said you,|потому что это то, что вы сказали вам,
hey, I need 256.|эй, мне нужно 256.
This is my, you know, that's my analysis.|Это мой, вы знаете, это мой анализ.
This is what I found out that I require.|Это то, что я выяснил, что мне нужно.
So they can guarantee you up to,|Таким образом, они могут гарантировать вам до,
key word, up to 256.|ключевое слово, до 256.
All right, but since you purchased an access rate of a T1,|Хорошо, но поскольку вы приобрели скорость доступа T1,
so, you're saying, hey telco,|Итак, вы говорите, привет, телеком,
if you have the bandwidth available,|если у вас есть доступная пропускная способность,
I would like to go up to that T1 speed,|Я бы хотел разогнаться до скорости Т1,
if it's available.|если он доступен.
Sure, why not, all right?|Конечно, а почему бы и нет, хорошо?
It could be at 1 in the morning,|Это могло быть в час ночи,
it could be you know, 1 in the afternoon.|это может быть вы знаете, час дня.
And you may be sending data, or you may be backing up things or,|И вы можете отправлять данные, или вы можете делать резервные копии, или,
what do you call this synchronizing your domain controllers, what have you.|как вы это называете синхронизацией контроллеров домена, что у вас есть.
Right, DNS servers.|Верно, DNS-серверы.
It could possibly get to 1.544 megabits per second if the telco provide, has the capability.|Он мог бы достичь 1,544 мегабит в секунду, если бы у оператора связи была такая возможность.
Meaning, that they have that bandwidth available for you because you're actually sharing that bandwidth with other people.|Это означает, что у них есть доступная пропускная способность для вас, потому что вы фактически делитесь этой пропускной способностью с другими людьми.
Remember earlier, I said that it was,|Помните, раньше я сказал, что это было,
things you call frctional T1s,|вещи, которые вы называете фракционными Т1,
people share T1 lines.|люди используют линии T1.
So they sell them in 64 kilobit chunks.|Поэтому они продают их кусками по 64 килобита.
So you're sharing this line, that's why you're getting this frame relay.|Итак, вы разделяете эту строку, вот почему вы получаете это Frame Relay.
So, that's why they tell you,|Итак, вот почему они говорят вам,
all right, we can guarantee you up to.|хорошо, мы можем гарантировать вам до.
Doesn't mean you have 256|Это не значит, что у вас 256
kilobits per second at all times,|килобит в секунду постоянно,
it means you can go up to 256 and they'll guarantee it.|это означает, что вы можете увеличить количество до 256, и они это гарантируют.
Beyond that,|За гранью этого,
since you got an access rate, of,|поскольку у вас есть скорость доступа,
of T1, if it's available,|Т1, если есть,
they will send it.|они пришлют это.
But again, those bits will be marked and later on, when we do show commands,|Но опять же, эти биты будут отмечены, и позже, когда мы покажем команды,
these are some of the things that you want to look at.|это некоторые вещи, на которые вы хотите взглянуть.
Cuz if you're constantly getting bits that are being marked DE, and they start growing, growing, growing,|Потому что, если вы постоянно получаете биты с пометкой DE, и они начинают расти, расти, расти,
growing and growing,|растет и растет,
then you need to purchase more bandwidth.|тогда вам нужно приобрести дополнительную пропускную способность.
Now that's just one of the ways that we monitor our network.|Это лишь один из способов мониторинга нашей сети.
You'll see when we get into the monitoring of our devices and when we get to that particular session.|Вы увидите, когда мы перейдем к мониторингу наших устройств и когда перейдем к конкретному сеансу.
We'll talk about other types of things that we can do to monitor our network.|Мы поговорим о других вещах, которые мы можем делать для мониторинга нашей сети.
Our bandwidth and stuff like that, utilization.|Наша пропускная способность и тому подобное, использование.
But, when using frame relay, definitely,|Но при использовании Frame Relay, безусловно,
one of the things we wanna pay attention to, is that DE, right?|одна из вещей, на которую мы хотим обратить внимание, это DE, верно?
Those DE bits.|Эти биты DE.
That, if they're marked,|Что, если они отмечены,
that means that hey,|это означает, что эй,
I'm going beyond my CIR,|Я выхожу за пределы своего CIR,
my committed information rate.|моя преданная скорость передачи информации.
So that means my analysis wasn't as good,|Значит, мой анализ был не таким хорошим,
or hey, we're doing a lot more business.|или эй, у нас гораздо больше бизнеса.
We're transferring a lot more information out the, you know,|Мы передаем намного больше информации из, вы знаете,
throughout the internet.|по всему Интернету.
Hopefully that's the case.|Надеюсь, это так.
It's not somebody watching movies on YouTube.|Это не кто-то смотрит фильмы на YouTube.
Then that's why it's causing your bandwidth.|Тогда вот почему это вызывает вашу пропускную способность.
But again,|Но опять же,
we'll get into that in the other session.|мы займемся этим на другом сеансе.
How you can find out that Joe's been watching YouTube movies throughout the day instead of doing what he's supposed to do.|Как узнать, что Джо весь день смотрел фильмы на YouTube вместо того, чтобы делать то, что ему положено.
Right?|Правильно?
So definitely, if you have a frame relay connection, these are the two,|Итак, определенно, если у вас есть соединение с ретрансляцией кадров, это два,
first two things that you need to be concerned with.|Первые две вещи, о которых вам нужно позаботиться.
All right, because your, you need to,|Хорошо, потому что тебе нужно,
when you call your provider,|когда вы звоните своему провайдеру,
they're gonna ask you, well, what's your bandwidth, how much bandwidth do you want?|они спросят вас: ну, какая у вас пропускная способность, какая пропускная способность вам нужна?
Because you can actually pay less money using a frame relay,|Поскольку вы можете платить меньше денег, используя Frame Relay,
and you can still make it look like a T1.|и вы все еще можете сделать его похожим на T1.
Now remember, you're not using eight you can make it, I'm sorry,|Теперь помните, вы не используете восемь, вы можете сделать это, извините,
you can make it look like an lease connection, right?|вы можете сделать так, чтобы это выглядело как договор аренды, не так ли?
Remember a lease, we're using HDLC, PPP yeah you need that bandwidth at all times.|Помните об аренде, мы используем HDLC, PPP. Да, вам всегда нужна эта полоса пропускания.
Well you can make frame relay look like a leased line, but pay like if it was a circuit switch.|Что ж, вы можете сделать Frame Relay похожим на выделенную линию, но заплатите, как если бы это был коммутатор цепи.
Very cheap, very inexpensive, all right,|Очень дешево, очень недорого, хорошо,
based on your CIR and your access rate.|на основе вашего CIR и вашей скорости доступа.
Because when those two numbers become the same, you know, you can actually,|Потому что, когда эти два числа становятся одинаковыми, вы знаете, что на самом деле вы можете
what they call burst, or maximum burst,|то, что они называют взрывом или максимальной скоростью,
or MBR, you can go up to.|или MBR, вы можете подняться до.
If it goes beyond the T1 obvi,|Если он выходит за пределы T1 obvi,
if it goes beyond that T1,|если он выходит за пределы этого T1,
you can kiss that those bits goodbye.|Вы можете поцеловать эти кусочки на прощание.
But anything up to the access rate,|Но все, что угодно, вплоть до скорости доступа,
if the telco has the capabilities of it,|если у телекоммуникационной компании есть возможности,
definitely they'll, they'll, you know,|определенно они будут, они, вы знаете,
it'll go through, but again,|это пройдет, но опять же,
they will be marked with the DEs.|они будут отмечены DE.
Now, I was gonna say something, oh, when we're using frame relay, you're not gonna use PPP or ACLC, when you do frame relay,|Я собирался кое-что сказать, о, когда мы используем Frame Relay, вы не будете использовать PPP или ACLC, когда вы используете Frame Relay,
your encapsulation is frame relay.|ваша инкапсуляция - это Frame Relay.
When you do the end cap,|Когда вы делаете заглушку,
you do end cap frame relay.|вы делаете оконечное реле кадра.
Now there's something called signaling methods, all right, within frame relay,|Теперь есть что-то, называемое методами сигнализации, внутри Frame Relay,
which is, you have Cisco, where you look for the default for Cisco devices.|то есть у вас есть Cisco, где вы ищите устройства Cisco по умолчанию.
All right, that's your LMIs.|Хорошо, это ваши LMI.
And you also have ANSI.|А еще у вас есть ANSI.
And, I always forget this last one,|И я всегда забываю это последнее,
which is Q933.A, or Q.933A, or something of that nature.|это Q933.A, или Q.933A, или что-то в этом роде.
I never can remember where that dot is or Q9333A, something like that.|Я никогда не могу вспомнить, где эта точка или Q9333A, что-то в этом роде.
But, normally it's,|Но обычно это
it's either Cisco or IETF.|это либо Cisco, либо IETF.
I mean Cisco, ANSI or that last one I just mentioned the Q9333, or 933A, okay?|Я имею в виду Cisco, ANSI или тот последний, о котором я только что упомянул Q9333 или 933A, хорошо?
But normally, when we configure this,|Но обычно, когда мы настраиваем это,
it's going to be Cisco router so we're gonna have it DLMI default at Cisco.|это будет маршрутизатор Cisco, так что у нас будет DLMI по умолчанию в Cisco.
Now, you yourself,|Теперь ты сам,
now I'll show you the lab back here this is the basic,|Сейчас я покажу вам лабораторию, это основная,
one that we're gonna start with.|тот, с которого мы собираемся начать.
Cuz remember, you got that huge lab,|Потому что помни, у тебя огромная лаборатория,
which has a frame relay connection in the middle.|который имеет соединение Frame Relay посередине.
Your devices, normally, I say remember the S00's have the clock rates.|Обычно я говорю, что ваши устройства помнят, что у S00 есть тактовая частота.
Remember, that's not the case.|Помните, что это не так.
Your provider,|Ваш провайдер,
is where the clock rate goes.|вот где идет тактовая частота.
You're provider is the DCE.|Ваш провайдер - это DCE.
Routers, test question,|Маршрутизаторы, тестовый вопрос,
sounds like it, at least on my exams.|звучит так, по крайней мере, на моих экзаменах.
Test questions.|Контрольные вопросы.
Your routers, by default, are DTE.|По умолчанию ваши маршрутизаторы DTE.
Data terminating equipment.|Оборудование для завершения передачи данных.
It is your provider that gives you the clocking,|Это ваш провайдер, который дает вам синхронизацию,
the synchronization for information to go across, okay?|синхронизация для передачи информации, хорошо?
But, as far as the test is concerned,|Но что касается теста,
one of the things that you need to be aware of, as far as this, right now.|одна из вещей, о которых вам нужно знать прямо сейчас.
Cuz again, I'm breaking this down into little pieces so you can understand frame relay and then we can actually do the lab.|Опять же, я разбиваю это на мелкие части, чтобы вы могли понять Frame Relay, а затем мы могли бы провести лабораторную работу.
The first two things, the first two terminology terms is the CIR,|Первые две вещи, первые два терминологических термина - это CIR,
which is the committed information rate,|что является подтвержденной скоростью передачи информации,
that's what's guaranteed.|это то, что гарантировано.
And the access rate, where you would like to go at if the bandwidth is available at your provider, okay?|И скорость доступа, которую вы хотели бы получить, если пропускная способность доступна у вашего провайдера, хорошо?
Again, and again, you will not,|Снова и снова ты не будешь,
you will not be using PPP or HDLC.|вы не будете использовать PPP или HDLC.
Also, I wanna repeat this again.|Кроме того, я хочу повторить это еще раз.
You can make frame relay look like a leased connection, all right?|Вы можете сделать Frame Relay похожим на выделенное соединение, хорошо?
If you can match these two numbers, right?|Если вы можете сопоставить эти два числа, верно?
You can make then, you know you can be going at 1.544 megabits per second.|Тогда вы можете работать со скоростью 1,544 мегабит в секунду.
But, making it paying for,|Но, заставив платить за
like if you were paying for a circuit switch, like an ISDN line.|как если бы вы платили за коммутатор цепи, например, за линию ISDN.
So you can make it look like a leased line.|Таким образом, вы можете сделать его похожим на выделенную линию.
All right, frame relay.|Хорошо, Frame Relay.
Just remember that anything above your access rate,|Просто помните, что все, что выше вашей скорости доступа,
anything above your access rate.|все, что выше вашей скорости доступа.
Those bits will be, or anything above,|Эти биты будут или что-то выше,
I'm sorry, anything above your CIR,|Извините, что-либо выше вашего CIR,
anything above your CIR,|все, что выше вашего CIR,
will be marked with DE which means discard eligible,|будут отмечены DE, что означает отказ от участия,
that those are eligible to be discarded.|что от них можно отказаться.
Because if the bandwidth is not there,|Потому что, если пропускной способности нет,
boom.|бум.
And that is a trigger for you to,|И это спусковой крючок для вас,
when you're monitoring your network,|когда вы контролируете свою сеть,
to say hey, these DE bits keep growing,|чтобы сказать эй, эти биты DE продолжают расти,
growing, growing and growing.|растет, растет и растет.
I'm probably gonna have to call back my provider and increase the number of bandwidth, my number of my CIR to something greater than what I have.|Мне, вероятно, придется перезвонить моему провайдеру и увеличить пропускную способность, мой номер CIR до чего-то большего, чем у меня.
It could be the case that you may have to switch over to a lease connection.|Возможно, вам придется переключиться на подключение по аренде.
But again,|Но опять же,
you have to create that documentation for the justification to your boss, okay?|вы должны создать эту документацию для оправдания вашего босса, хорошо?
Because if not, there's you know,|Потому что если нет, ты знаешь,
people are not just going to dish out money just like that.|люди не собираются просто так тратить деньги.
If you're the boss, then hey,|Если ты босс, то эй,
it's your money that you're gonna spend.|это ваши деньги, которые вы собираетесь потратить.
Make sure that,|Убедись, что,
this is just not a one time thing.|это просто не разовая вещь.
That happened one week and then doesn't happen again until,|Это случилось одну неделю и не повторится, пока
you know, the following month.|знаете, в следующем месяце.
If it's happening on an ongoing basis and you're monitoring this.|Если это происходит на постоянной основе, и вы за этим следите.
And you should be monitoring this,|И вы должны следить за этим,
and creating you know, charts and what have you.|и создание вы знаете, диаграммы и что у вас есть.
Obviously through third party software,|Очевидно, через стороннее программное обеспечение,
okay?|Ладно?
That you can see hey,|Что вы можете видеть, эй,
my balance is usually at a peak already.|мой баланс обычно уже на пике.
So, you need to manage that,|Итак, вам нужно управлять этим,
you need to manage that.|вам нужно управлять этим.
All right, so for this particular part of frame relay, we're done.|Итак, с этой конкретной частью Frame Relay мы закончили.
Just keep these two terms in your mind,|Просто запомните эти два термина,
especially for your certification purposes.|особенно для целей сертификации.
I'll see you in the next one.|Увидимся в следующем.
[BLANK AUDIO].|[ПУСТОЙ АУДИО].
