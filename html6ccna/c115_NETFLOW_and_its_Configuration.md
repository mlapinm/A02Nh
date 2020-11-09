D:\mailCloud\prjother\tmp\1\c115_NETFLOW and its Configuration.md  


__|__
--|--
All right.|Все в порядке.
We've made it to the very last lesson in the CCNA course.|Мы дошли до самого последнего урока курса CCNA.
All right, this it NetFlow.|Хорошо, это NetFlow.
All right?|Все в порядке?
This is one of the last IP services that we need to talk about and NetFlow really, what it is.|Это одна из последних IP-служб, о которой нам нужно поговорить, и NetFlow действительно, что это такое.
It actually shows you who is doing the naughty things on our network that they shouldn't be doing.|Это на самом деле показывает вам, кто делает в нашей сети непослушные вещи, которых им делать не следует.
Right?|Правильно?
That's why we have to do all these group policies, and all these access lists, and all these switchport security stuff.|Вот почему мы должны выполнять все эти групповые политики, все эти списки доступа и все эти вещи, связанные с безопасностью портов коммутатора.
Right?|Правильно?
On our network to make sure that people don't go or plug in where they don't need to be plugging in.|В нашей сети, чтобы люди не заходили и не подключались туда, где им не нужно подключаться.
Or going where they don't need to be going.|Или идти туда, куда им не нужно.
Or sending email back and forth within a network.|Или отправка электронной почты туда и обратно внутри сети.
Or because you just came back from a cruise and you want to show your family pictures,|Или потому, что вы только что вернулись из круиза и хотите показать семейные фотографии,
which is very nice.|что очень приятно.
But it's not supposed to be done within the network, or across the water, or water and network, right?|Но это не должно происходить в сети, или по воде, или по воде и сети, верно?
It's taking up bandwidth.|Это занимает полосу пропускания.
I mean, we have bandwidth issues as enough.|Я имею в виду, что у нас достаточно проблем с пропускной способностью.
SNMP just told us we're peaking, we're peaking at our bandwidth right?|SNMP только что сказал нам, что мы достигли пика пропускной способности, верно?
Because we're really typing [INAUDIBLE]|Потому что мы действительно набираем [НЕРАЗБОРЧИВО]
right?|верно?
We're looking at those feckin and beckin bits yeah, no, only for the test.|Мы смотрим на эти долбанные и соблазнительные кусочки, да, нет, только для теста.
After that, you've got monitoring software, trust me.|После этого у вас есть программное обеспечение для мониторинга, поверьте мне.
Using SNMP, sys log, and now NetFlow.|Использование SNMP, системного журнала, а теперь и NetFlow.
Who, what does NetFlow do?|Кто, чем занимается NetFlow?
NetFlow actually tells us, hey, Laz is sending email pictures of all his big,|NetFlow на самом деле сообщает нам, что Лаз отправляет по электронной почте фотографии всех своих больших,
his vacations for the past year that has been going on.|его отпуск за последний год, который продолжается.
Okay, Susie is showing us her photo shoot that she did for,|Хорошо, Сьюзи показывает нам свою фотосессию, для которой она работала,
I don't know, some modeling agency.|Не знаю, какое-то модельное агентство.
You know, and that's where this actually takes you down to the IP address,|Вы знаете, и именно здесь это приводит вас к IP-адресу,
the MAC level.|уровень MAC.
Whoa, the user, what is it they're doing?|Ого, пользователь, что они делают?
All right?|Все в порядке?
But again, if you're using a third party software,|Но опять же, если вы используете стороннее программное обеспечение,
like the ones we've mentioned before.|как те, которые мы упоминали ранее.
Says, says look PRTG, Cisco Works, or Solar Winds.|Говорит, говорит посмотрите PRTG, Cisco Works или Solar Winds.
It's going to build that histogram.|Он построит эту гистограмму.
It's going to build that graph.|Он построит этот график.
It's going to show you in red.|Он будет отображаться красным цветом.
[SOUND] Right?|[ЗВУК] Верно?
It's like whoa, wait a minute, what's going on there?|Это похоже на стойку, подожди, что там происходит?
Then you start drilling down, and finding out down to the MAC address,|Затем вы начинаете детализировать и выяснять MAC-адрес,
down to the driver, right?|вплоть до водителя, верно?
Who is the cause of, of our bandwidth slowing down.|Кто является причиной замедления нашей пропускной способности?
Who is the cause of all these problems that's happening?|Кто является причиной всех этих проблем?
So, NetFlow will tell you why things are happening, which is great, which is great.|Итак, NetFlow расскажет вам, почему что-то происходит, и это здорово, и это здорово.
Unfortunately, packet tracer cannot.|К сожалению, трассировщик пакетов не может.
Doesn't support it as of yet, as of yet.|Пока не поддерживает его.
I'm sure they are working on it.|Я уверен, что они над этим работают.
But this is how you would do it.|Но вот как бы вы это сделали.
This is how you would do it.|Вот как бы вы это сделали.
You go into the interface.|Заходишь в интерфейс.
Whatever it is.|Что бы это ни было.
Whatever interface you are going to do.|Какой бы интерфейс вы ни собирались делать.
And you are going to look at what's coming in,|И вы посмотрите, что входит,
the ingress, the flow of packets in or the flow of packets coming out, egress.|входящий, входящий или исходящий поток пакетов, исходящий.
In global configuration,|В глобальной конфигурации
you're going to export that information to whoever's monitoring it right?|вы собираетесь экспортировать эту информацию тому, кто ее отслеживает, верно?
Then you're going to export the version.|Затем вы собираетесь экспортировать версию.
There's only three versions, one, five and nine.|Есть только три версии: первая, пятая и девять.
So you pick nine.|Итак, вы выбираете девять.
That's the latest version.|Это последняя версия.
Okay?|Ладно?
But whatever you put on the router,|Но что бы вы ни поставили на роутер,
you gotta put it on your monitoring software okay?|Вы должны поставить это на свое программное обеспечение для мониторинга, хорошо?
And that's it.|Вот и все.
That's all you do.|Это все, что ты делаешь.
And then you just make sure that on monitoring software you put the same thing.|А потом вы просто убедитесь, что на программное обеспечение для мониторинга вы поставили то же самое.
That's it.|Вот и все.
And then, you want to look at the show IP flow export.|А затем вы хотите посмотреть на экспорт IP-потока show.
But again, you rarely do this.|Но опять же, вы делаете это редко.
You look at your monitoring software.|Вы смотрите на свое программное обеспечение для мониторинга.
You'll get, you know, alarms, calls,|Вы получите, знаете ли, будильники, звонки,
whatever the case may be.|в любом случае.
How it tells you.|Как он вам говорит.
Because you may be sitting down there,|Потому что ты можешь сидеть там,
you're that guy or gal that works overnight, so you got nothing better to do than to look at all these 20 screens.|Вы тот парень или девушка, которые работают всю ночь, поэтому вам нечего делать лучше, чем смотреть на все эти 20 экранов.
And the same things are going to pop up.|И то же самое будет всплывать.
You're like, oh, wait a minute, that's red.|Ты такой, подожди, это красный.
Let me take a look at that.|Позвольте мне взглянуть на это.
You take a look at it then you go into the router and you can find out what happened.|Вы смотрите на него, затем заходите в маршрутизатор и можете узнать, что произошло.
But a lot of these third party applications,|Но многие из этих сторонних приложений,
you can stop people right from there.|вы можете останавливать людей прямо там.
Oh, you can't go to that website.|О, вы не можете зайти на этот сайт.
[NOISE] and you deny right from right there.|[NOISE], и вы сразу же отрицаете.
So, so sometimes people get slick and they know how to circumvent the security of, that you configured.|Итак, иногда люди становятся хитрыми и знают, как обойти безопасность, которую вы настроили.
So you that's why you really need to you know,|Так ты вот почему тебе действительно нужно знать,
people say man, that's a that administrator is harsh.|люди говорят, мужик, вот и такой администратор резкий.
We can't use anything on here.|Здесь мы ничего не можем использовать.
We can't bring in our USB.|Мы не можем ввести наш USB.
Right, you can't.|Правильно, ты не можешь.
Because if this is your network and it should be up and running 100% of the time.|Потому что, если это ваша сеть, и она должна быть в рабочем состоянии 100% времени.
That may not be a realistic number, but it's a goal that we want to have.|Это может быть нереалистичное число, но это цель, которую мы хотим достичь.
All right, but NetFlow again, really.|Хорошо, но опять же NetFlow.
This is the configuration right here.|Это конфигурация прямо здесь.
If you want to look inside the router, you can use these show,|Если вы хотите заглянуть внутрь маршрутизатора, вы можете использовать это шоу,
these three show command.|эти три команды show.
So look at, hey, where is that exporting to?|Итак, посмотрите, куда это идет?
You wanna look at the interface and see how much information is going through there.|Вы хотите посмотреть на интерфейс и увидеть, сколько информации там проходит.
What interface is it actually using.|Какой интерфейс он на самом деле использует.
And the size of the packets that are going through.|И размер пакетов, которые проходят.
That's it.|Вот и все.
That's it.|Вот и все.
But again,|Но опять же,
you're not gonna be really looking into it through the router.|вы не собираетесь действительно смотреть на это через маршрутизатор.
You're not even gonna to be doing it on the certification.|Ты даже не будешь делать это на сертификации.
They'll ask you questions, maybe, on what NetFlow is and, what would, how would,|Они, может быть, зададут вам вопросы о том, что такое NetFlow и что бы, как бы
what would be the command, a, b, c, d or e.|какая будет команда: a, b, c, d или e.
That you want to monitor things going in,|Что вы хотите следить за происходящим,
or things going out.|или что-то выходит.
But this is it right here.|Но это прямо здесь.
These, this, whoa, whoa, whoa, wait a minute.|Эти, это, стой, стой, стой, подожди минутку.
Okay.|Ладно.
I can fix that.|Я могу это исправить.
Right there.|Прямо там.
That, that's it.|Вот и все.
This is how you configure NetFlow.|Вот как вы настраиваете NetFlow.
It's no big deal.|Это ничего важного.
It's a big deal when, in a network, when you actually are monitoring and because there's something going on.|Это большая проблема, когда в сети вы на самом деле контролируете и потому что что-то происходит.
And you need to take back to the higher ups and let them know, hey,|И вам нужно вернуться к руководству и сообщить им, эй,
listen these are the reports that I can pull.|послушайте, это отчеты, которые я могу вытащить.
Because that's what's important.|Потому что это важно.
You're pulling all of these reports you know, weekly, monthly,|Вы составляете все эти отчеты: еженедельно, ежемесячно,
whatever the case may be.|в любом случае.
Hey, and this is what's going on.|Эй, вот что происходит.
All right?|Все в порядке?
You know, like, I want to see,|Знаешь, я хочу увидеть,
I want to go to a certain website of some bodybuilding.|Я хочу зайти на определенный сайт, посвященный бодибилдингу.
I'm not supposed to be doing that during the work day.|Я не должен делать этого в течение рабочего дня.
All right, so all these different things that's why,|Хорошо, так что все эти разные вещи, поэтому,
when we're doing our logging or when we're doing our SNMP.|когда мы ведем наш журнал или когда мы делаем наш SNMP.
We tweak it to see what is it that we want to manage and they'll tell you.|Мы настраиваем его, чтобы увидеть, чем мы хотим управлять, и они вам расскажут.
Okay and that's why we have our firewalls.|Хорошо, и поэтому у нас есть брандмауэры.
All these different things, the third party softwares, the firewalls, all,|Все эти разные вещи, стороннее программное обеспечение, брандмауэры, все,
that's what they do.|вот что они делают.
To make sure and maintain, you know, that,|Чтобы убедиться и поддерживать, вы знаете, что,
hey,|Привет,
control over our network, because bandwidth is an issue.|контроль над нашей сетью, потому что пропускная способность является проблемой.
And security, there may be certain websites,|И безопасность, могут быть определенные веб-сайты,
that could be a bodybuilding website or it could be supplementation website,|это может быть сайт о бодибилдинге или сайт о добавках,
or it could be, you know, vacation website that you're going to.|или это может быть сайт для отпуска, на который вы собираетесь.
But they've been hacked, or it's, whatever re-, they may have something on there.|Но они были взломаны, или, что бы там ни было, у них там что-то есть.
Then they might have a virus, and then you get infected.|Тогда у них может быть вирус, и тогда вы заразитесь.
So, you gotta protect the network as much as possible.|Итак, вы должны максимально защитить сеть.
So, monitoring your network is extremely important.|Итак, мониторинг вашей сети чрезвычайно важен.
Don't think that I'm saying, I'm just,|Не думайте, что я говорю, я просто
whatever,|без разницы,
I'll set SNMP, no, no, no, no, no or syslog.|Я установлю SNMP, нет, нет, нет, нет, нет или системный журнал.
No, no, the configuration of it is, it's simple, it's easy to use.|Нет-нет, конфигурация у него такая, простая, удобная в использовании.
And with these monitoring software's that exist it really makes life a whole lot easier.|И с этим существующим программным обеспечением для мониторинга оно действительно делает жизнь намного проще.
But again, there's three things that we need to at least be monitoring for.|Но опять же, есть три вещи, за которыми нам нужно хотя бы следить.
SNMP is telling you, hey, this is what's going on with the system.|SNMP сообщает вам: «Эй, вот что происходит с системой».
Okay?|Ладно?
Or, this is what's, this is what's going on with this particular device.|Или вот что, вот что происходит с этим конкретным устройством.
I'm sorry, this is what's going on with this particular device.|Извините, вот что происходит с этим конкретным устройством.
The other one, the syslog.|Другой, syslog.
Hey, this is what's going on with the actual system.|Эй, вот что происходит с реальной системой.
We're getting system messages now.|Сейчас мы получаем системные сообщения.
Right?|Правильно?
Like that debug that we saw.|Как та отладка, которую мы видели.
Or, hey, who's messing up the network?|Или, эй, кто портит сеть?
Why is our bandwidth messed up?|Почему наша пропускная способность испорчена?
Why is the processor on that particular device going crazy?|Почему процессор на этом конкретном устройстве сходит с ума?
So now we get to know exactly what's going on.|Итак, теперь мы точно знаем, что происходит.
So when we take these reports and we take them to the higher ups.|Итак, когда мы берем эти отчеты и передаем их руководству.
They get a better understanding as to why you want newer computers,|Они лучше понимают, зачем вам нужны новые компьютеры,
as to why you want to go gigabit, as to why we to, we need more bandwidth.|Что касается того, почему вы хотите перейти на гигабит, насчет того, почему нам нужно больше пропускной способности.
That's the whole point of NetFlow.|В этом весь смысл NetFlow.
Very simple to configure, very important.|Очень просто настроить, очень важно.
All three of them are very important,|Все трое очень важны,
okay?|Ладно?
And they will be in your certification.|И они будут в вашей аттестации.
Again, from what I gather, gather from my students that have taken the test,|Опять же, из того, что я собираю, у моих учеников, прошедших тест,
they do have a couple questions on all three, all right?|у них есть пара вопросов по всем трем, понятно?
But they're not as much as you would think.|Но их не так много, как вы думаете.
It's a brand new, brand new thing that they have on there, which is good.|У них там совершенно новая, совершенно новая вещь, и это хорошо.
It's good.|Это хорошо.
It gives you more ammunition so when you get out there you're like okay I'm ready I understand what you're telling me.|Это дает вам больше боеприпасов, поэтому, когда вы выйдете оттуда, все в порядке, я готов, я понимаю, что вы мне говорите.
So it's gonna be good for you when you get to your interviews.|Так что тебе будет хорошо, когда ты придешь на интервью.
So as long as you understand the concepts of what SNMP does,|Итак, если вы понимаете концепции того, что делает SNMP,
syslog and NetFlow, you should be good to go.|syslog и NetFlow, все готово.
All right?|Все в порядке?
You should be good to go.|Тебе должно быть хорошо.
But always keep this in mind.|Но всегда имейте это в виду.
It is monitoring software, what you use.|Это программное обеспечение для мониторинга, которым вы пользуетесь.
I'll see you in the next.|Увидимся в ближайшее время.
[BLANK_AUDIO]|[BLANK_AUDIO]
  
