D:\mailCloud\prjother\tmp\1\c107_show commands for frame-relay.md  


__|__
--|--
Welcome back everybody.|С возвращением всем.
All right.|Все в порядке.
This is the last lesson for this session in frame relay.|Это последний урок данного сеанса по Frame Relay.
And basically what I'm gonna do is show you some show commands that you should familiarize yourself with.|И в основном то, что я собираюсь сделать, это показать вам некоторые команды show, с которыми вам следует ознакомиться.
That will help you on your certification.|Это поможет вам в сертификации.
So, let's hit Enter here, we're in router two, doesn't really matter, same thing for all the routers.|Итак, давайте нажмем Enter здесь, мы находимся во втором маршрутизаторе, не имеет значения, то же самое для всех маршрутизаторов.
Show frame relay, and remember, packet tracer is there for,|Покажите Frame Relay и помните, что пакетный трассировщик предназначен для,
to help you pass certification, so these three right there,|чтобы помочь вам пройти сертификацию, вот эти трое,
is what you need to know.|это то, что вам нужно знать.
So, show frame relay.|Итак, покажите Frame Relay.
LMI, let's do the first one.|LMI, давайте сделаем первый.
All right, this one, if they run into a question, if you run into a question,|Хорошо, этот, если у них возникнет вопрос, если у вас возникнет вопрос,
that says, hey, what command will show you the signaling method that the router is using to communicate with the others in the frame relay?|в котором говорится: эй, какая команда покажет вам метод сигнализации, который маршрутизатор использует для связи с другими в ретрансляции кадров?
Right?|Правильно?
The LMI type that is what you're looking for.|Тип LMI - это то, что вы ищете.
Signalling method LMI type.|Метод сигнализации Тип LMI.
I didn't tell you LMI cause then you just type in show frame-relay LMI.|Я не сказал вам LMI, потому что тогда вы просто набираете show frame-relay LMI.
So today, what, what command can you type to see the signalling method?|Итак, что, какую команду вы можете набрать сегодня, чтобы увидеть метод сигнализации?
Show frame-relay LMI that will show you the signaling method.|Покажите LMI Frame Relay, который покажет вам метод сигнализации.
There it is right there.|Вот оно прямо здесь.
All right?|Все в порядке?
And this is really the,|И это действительно
all this information that you see here is between the router and the frame relay cloud.|вся эта информация, которую вы видите здесь, находится между маршрутизатором и облаком Frame Relay.
Obviously, there's nothing going on.|Очевидно, ничего не происходит.
[LAUGH] There's no information going back and forth.|[СМЕХ] Информации нет.
So that's why you see all the zeroes and things like that.|Вот почему вы видите все нули и тому подобное.
But that command show frame-relay LMI,|Но эта команда показывает LMI Frame Relay,
that's what it's showing you, the signalling method.|это то, что он вам показывает, метод сигнализации.
That's what do you wanna see.|Вот что ты хочешь увидеть.
Now of course you only show the errors and things like that, and how many links sent and received and,|Теперь, конечно, вы показываете только ошибки и тому подобное, а также количество отправленных и полученных ссылок и
between you and the friend and the cloud but your thing to remember is the signalling method.|между вами и вашим другом и облаком, но вам следует помнить о методе передачи сигналов.
What type is it using?|Какой тип он использует?
All right.|Все в порядке.
So that's for the frame-relay LMI.|Итак, это для LMI с ретрансляцией кадров.
The next one is show frame-relay PVC.|Следующий - показать PVC с ретрансляцией кадров.
A little bit, a little bit more and I'm telling you right now,|Еще немного, еще немного, и я говорю вам прямо сейчас,
in your book, this is, this, this print screen is right there.|в твоей книге вот это, вот этот экран для печати.
All right, so what do you want, what are things you look for here?|Хорошо, так что вы хотите, что вы здесь ищете?
One, this'll show you your local DLCI,|Во-первых, это покажет вам ваш местный DLCI,
those DLCIs are local to your router,|эти DLCI являются локальными для вашего маршрутизатора,
okay?|Ладно?
It will show you the status, that is active, which is good.|Он покажет вам статус, который активен, что хорошо.
Cause it will be, if it would say delete it, that means there's something going on,|Потому что, если он скажет удалить его, это означает, что что-то происходит,
on the far end.|на дальнем конце.
There's something going on, on the far end.|Что-то происходит на дальнем конце.
So the status of this DLCI is active which is a good thing.|Так что статус этого DLCI активен, и это хорошо.
That's how you wanna see.|Вот как ты хочешь видеть.
You see delete it here, there's a problem across on the other side.|Вы видите, удалите это здесь, на другой стороне проблема.
The next thing that you wanna look at here are these in BECNs, all right.|Следующее, на что вы хотите посмотреть, это эти в BECN, хорошо.
Your DE, look at your DE bits right there.|Ваш DE, посмотрите здесь свои биты DE.
All right, and you have out FECNs.|Хорошо, и у вас есть FECN.
All right?|Все в порядке?
So BECN and FECN.|Итак, BECN и FECN.
What in the world is that?|Что это вообще такое?
Backward explicit congestion and forward explicit congestion.|Явная перегрузка в обратном направлении и явная перегрузка вперед.
BECN really your routers don't act upon it unless you tell them to.|BECN на самом деле ваши маршрутизаторы не действуют на него, пока вы им не скажете.
BECN says, hey, I am experiencing traffic towards the destination,|BECN сообщает: "Эй, я вижу движение к месту назначения,
meaning where I just came from okay, cause they went back there and we came back.|То есть откуда я только что приехал, хорошо, потому что они вернулись туда, а мы вернулись.
Where I came from, I'm experiencing congestion.|Там, откуда я приехал, у меня заторы.
Forward explicit congestion, right?|Прямая явная перегрузка, верно?
FECNs is telling the destination router,|FECN сообщает маршрутизатору назначения,
say hey, I'm experiencing traffic.|скажи привет, у меня пробки.
So, if these numbers start going up,|Итак, если эти цифры начнут расти,
because usually they'll tell you how people in the corporate or people in your company are whining about that they're experiencing congestion going|потому что обычно они расскажут вам, как люди в компании или люди в вашей компании жалуются на то, что они испытывают перегрузку
to their corporate office.|в их корпоративный офис.
So the number you're looking for it's like okay so I'm experiencing going to over there.|Так что номер, который вы ищете, в порядке, поэтому я собираюсь туда.
That means as I'm traversing this network,|Это означает, что пока я прохожу через эту сеть,
right?|верно?
Cause the information is coming back to me is the BECN.|Потому что информация возвращается ко мне - это BECN.
All right.|Все в порядке.
BECN, so these two right here are things you should look at,|BECN, вот эти две вещи, на которые вы должны обратить внимание,
all right, for congestion avoidance.|хорошо, во избежание перегрузки.
These are your DE.|Это ваши ДЭ.
Obviously, we're not going over CIR,|Очевидно, мы не переходим CIR,
right?|верно?
Cause we're not transmitting anything but these are your discard eligible bits.|Потому что мы ничего не передаем, но это ваши подходящие биты для сброса.
Discard that means if they are marked with DE bit,|Отбросить это означает, что если они помечены битом DE,
that means that they're eligible to be dropped, eligible to be dropped.|это означает, что они могут быть исключены, имеют право быть исключенными.
Remember you purchase an access rate.|Помните, что вы покупаете скорость доступа.
If the toggle has the bandwidth available,|Если у переключателя есть доступная пропускная способность,
it will send out your information but if it doesn't, [SOUND] that traffic is gone.|он отправит вашу информацию, но если этого не произойдет, [ЗВУК] этот трафик пропал.
Definitely, if you go above your access rate, all right?|Определенно, если вы превысите свою скорость доступа, хорошо?
If you're doing the maximum burst rate,|Если вы используете максимальную скорость серийной съемки,
your packets are not going anywhere,|ваши пакеты никуда не денутся,
period.|период.
So, you need to pay attention to these numbers right here, because if those numbers, on a weekly basis, keeps going, keep going up, that's an issue.|Итак, вам нужно обратить внимание на эти цифры прямо здесь, потому что если эти цифры на еженедельной основе продолжают расти, продолжать расти, это проблема.
You need to analyze the network better,|Вам нужно лучше анализировать сеть,
and find out,|и узнай,
hey why are we having this bandwidth issue?|эй, почему у нас проблема с пропускной способностью?
Why am I getting all these help desk tickets to you know, that I,|Почему я получаю все эти билеты в службу поддержки, знаете ли, что я,
you know, getting to the destinations, or sending email, or what have you.|вы знаете, добраться до места назначения, или отправить электронное письмо, или что у вас есть.
It's, it's, it takes forever.|Это займет вечность.
So, you need to keep an eye on this.|Итак, вам нужно следить за этим.
Now, obviously, you're not gonna be sitting in your router doing show frame-relay PVC to take a look to see if there's congestion.|Теперь, очевидно, вы не собираетесь сидеть в своем маршрутизаторе и показывать PVC Frame Relay, чтобы посмотреть, нет ли перегрузки.
You will know there's congestion.|Вы будете знать, что есть пробка.
One, you'll be getting a lot of calls at the help desk.|Во-первых, вам будут часто звонить в службу поддержки.
And two, you're gonna be using a third party software.|И, во-вторых, вы будете использовать стороннее программное обеспечение.
Whatever it is to monitor, and which we'll be talking about in lessons to come, all right.|Что бы это ни было, и о чем мы будем говорить на следующих уроках, хорошо.
You'll be monitoring your network through these third party softwares that will send you an email.|Вы будете контролировать свою сеть с помощью этого стороннего программного обеспечения, которое отправит вам электронное письмо.
Right?|Правильно?
That will send you if you have a beeper,|Это отправит вам, если у вас есть пейджер,
if you're from the 80s and you have a beeper still.|если вы из 80-х и у вас есть пищалка.
All right.|Все в порядке.
You will, you will get a beep.|Вы услышите звуковой сигнал.
All right?|Все в порядке?
I don't know.|Я не знаю.
I mean you might get strike by lightning to let you know that, hey, go take a look at your router,|Я имею в виду, что вас может поразить молния, чтобы вы знали, что, эй, иди взгляни на свой маршрутизатор,
there's something going on or whatever the case may be, all right?|там что-то происходит или что там такое, хорошо?
You'll be using third party software.|Вы будете использовать стороннее программное обеспечение.
You're not gonna sit there and type show frame-relay PVC console.|Ты же не будешь сидеть там и типа показывать консоль PVC frame-relay.
You're not gonna be staring at your router.|Ты не будешь пялиться на свой роутер.
Okay, I'm looking at it, I'm looking at it, yeah, okay, I.|Хорошо, я смотрю на это, я смотрю на это, да, хорошо, я.
No, that doesn't happen that way, okay?|Нет, так не бывает, хорошо?
But again, for your test, if you get asked, these are the things you look at.|Но опять же, для вашего теста, если вас спросят, это то, на что вы смотрите.
BECN and FECN, and DE.|BECN и FECN, а также DE.
Backward explicit congestion, forward explicit congestion.|Явная перегрузка в обратном направлении, явная перегрузка вперед.
I'm experiencing traffic where I just came from,|У меня пробки там, откуда я только что пришел,
I'm experiencing traffic where I'm going to.|Я собираюсь попасть в пробку.
All right, and then the discart eligible,|Хорошо, а затем отбрасывать право,
it can go beyond your CIR.|он может выходить за рамки вашего CIR.
So that's what the show, show frame-relay PVC does show you a lot of things.|Это то, что показывает PVC Frame Relay, и многое другое.
All the congestion information, plus your local DLCI and if the PVC is actually active, so it does show you a lot of things.|Вся информация о перегрузке, плюс ваш локальный DLCI и активен ли PVC, так что он действительно многое вам показывает.
Now as well,|Теперь тоже,
the sub-interface, but again that's not a big deal, you can see that in the start.|субинтерфейс, но опять же, это не имеет большого значения, вы можете видеть это в начале.
But the FECN, the BECN, the DE bit, all that is crucial,|Но FECN, BECN, бит DE, все, что имеет решающее значение,
this screen right here is in your book.|вот этот экран в вашей книге.
That should tell you something, all right,|Это должно тебе кое-что сказать, хорошо,
so be looking for that.|так что ищите это.
So that's show frame-relay PVC, and that's your show frame-relay LMI.|Итак, это show frame-relay PVC, и это ваш show frame-relay LMI.
And the last one, a show frame-relay map,|И последний, показать карту ретрансляции кадров,
we haven't done any map statements,|мы не делали никаких операторов карты,
all right?|все в порядке?
But again, here it's telling you, oops.|Но опять же, здесь он говорит вам, упс.
Ctrl+Shift+6 by finger on the keyboard.|Ctrl + Shift + 6 пальцем по клавиатуре.
[BLANK_AUDIO]|[BLANK_AUDIO]
All right.|Все в порядке.
Show frame-relay MAP.|Покажите КАРТУ Frame Relay.
They're showing you your local DLCI and it's broadcing,|Они показывают вам ваш местный DLCI, и он транслируется,
broadcasting out the information.|распространение информации.
It's on a point-to-point.|Это точка-точка.
If they show you a print screen of a frame-relay map statement,|Если они покажут вам экран печати оператора карты Frame Relay,
always remember it has to be the destination IP address, and the local DLCI.|всегда помните, что это должен быть IP-адрес назначения и локальный DLCI.
If it's the other way around, it's wrong.|Если наоборот, то это неправильно.
Period.|Период.
It is not the destination DLCI.|Это не целевой DLCI.
It is not the source IP address.|Это не исходный IP-адрес.
The correct way, I'm gonna say it again,|Правильно, я скажу это еще раз,
would be the destination IP address and the local DLCI.|будет IP-адресом назначения и локальным DLCI.
Okay?|Ладно?
So if they were to show a frame-relay map statement.|Так что, если бы они показали оператор карты Frame Relay.
If they do, then you know.|Если они это сделают, тогда вы знаете.
If they don't, then don't worry about it.|Если нет, не беспокойтесь об этом.
But definitely, be familiarized with the show frame-relay PVC for those congestions.|Но обязательно ознакомьтесь с показом PVC Frame Relay для этих перегрузок.
And with a show frame-relay LMI so you know what type of signaling method the routers are using.|И с показом LMI с ретрансляцией кадров, чтобы вы знали, какой тип метода сигнализации используют маршрутизаторы.
All right, this is frame relay everyone.|Хорошо, это все, кто использует Frame Relay.
Next session, we get into PBP which is really easy to do.|На следующем занятии мы перейдем к PBP, что действительно легко сделать.
I'll see you then.|Увидимся тогда.
[BLANK_AUDIO]|[BLANK_AUDIO]
