D:\mailCloud\prjother\tmp\1\c31_The access method of ethernet (CSMACD).md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
Welcome back everybody.|С возвращением всем.
All right, now we can go on and start talking more about the actual standard that Ethernet uses and the access method that Ethernet uses.|Хорошо, теперь мы можем продолжить и начать больше говорить о фактическом стандарте, который использует Ethernet, и о методе доступа, который использует Ethernet.
Let's get the little handy dandy pencil back.|Давай вернем маленький удобный денди-карандаш.
Let's put the thickness a little bit, that was a kind of,|Давайте немного увеличим толщину, это было своего рода,
I didn't like the fact that was kind of,|Мне не нравился тот факт, что это было
wasn't that thick.|не такой уж толстый.
All right, so ethernet the standard that the IEEE actually came up with was 802.3.|Итак, стандарт Ethernet, который фактически предложил IEEE, был 802.3.
The access method is CSMA/CD.|Метод доступа - CSMA / CD.
And again, in all that, this whole time I've had an injury and it's really hurting me, so that's why I'm holding my hand.|И опять же, все это время у меня была травма, и мне очень больно, поэтому я держу себя за руку.
Okay?|Ладно?
Just so you know.|Просто чтобы вы знали.
802.3, it's the axis method.|802.3, это осевой метод.
Now we have variations available 802.3,|Теперь у нас есть варианты 802.3,
because we went from 10|потому что мы пошли с 10
megabits per second to 100 megabits per second to 1,000 megabits per second.|мегабит в секунду до 100 мегабит в секунду до 1000 мегабит в секунду.
And then we get in to fiber optics.|Затем мы переходим к волоконной оптике.
Well is, the faster you go, obviously this will be, you know tx, cx,|Ну, чем быстрее вы пойдете, очевидно, что это будет, вы знаете tx, cx,
ox, all these different cabling standards that they have.|ох, все эти разные стандарты кабельной разводки, которые у них есть.
But 802.3 is the Ethernet standard,|Но 802.3 - это стандарт Ethernet,
if ever asked what IEEE standard you use,|если когда-нибудь спросят, какой стандарт IEEE вы используете,
it is 802.3.|это 802.3.
Doubtful they'll ask you that on the CCNA,|Сомневаюсь, что они спросят вас об этом на CCNA,
but you need to understand CSMA/CD.|но вам нужно понимать CSMA / CD.
Carrier sends multiple access collision detection.|Оператор передает данные об обнаружении конфликтов множественного доступа.
And basically all that does, is remember the, what I just drew, the bus apology or the, or the star, whatever it is, hybrid|И в основном все, что он делает, это запоминает то, что я только что нарисовал, автобусное извинение или звезду, что бы это ни было, гибрид.
star, extended star.|звезда, расширенная звезда.
All these things that these drawings have.|Все это есть на этих рисунках.
In today's technology if you have a switch and you're running a hundred megabits per second, that is Ethernet.|В современных технологиях, если у вас есть коммутатор, и вы используете 100 мегабит в секунду, это Ethernet.
You're going to run into this situation,|Вы попадете в эту ситуацию,
which means first-come-first-serve.|что означает - первым пришел - первым подал.
The first one who gets to the wire, is the one who gets to transmit.|Первый, кто подключается к проводу, тот и получает возможность передавать.
If you hear a noise on your wire, no information's going to be sent out on it.|Если вы слышите шум на своем проводе, никакой информации по нему не будет.
So if it's clear, then it will send.|Так что если понятно, то пошлёт.
But there will be times where your network is so bogged down that there's so many people transmitting, that you may have collisions.|Но будут моменты, когда ваша сеть настолько зависнет, что будет передавать столько людей, что у вас могут возникнуть коллизии.
And when you do have collisions, what happens is the standard right,|А когда возникают коллизии, происходит стандартное право,
shoots out a jamming signal.|издает глухой сигнал.
Everybody gets, you know nobody is allowed to actually send information,|Все понимают, что никому не разрешено отправлять информацию,
back off algorithm is, starts ticking.|алгоритм отката есть, начинает тикать.
Pretend like there's a clock going there.|Представьте, что там идут часы.
Once that timer is over, then people can try and transmit again.|Как только этот таймер закончится, люди могут попытаться передать снова.
And this is something that's really transparent to the user,|И это действительно прозрачно для пользователя,
the user says man the network is slow.|пользователь говорит человеку, что сеть медленная.
Man it's taking forever to print.|Человек, печать которого занимает вечность.
My God what's wrong with this internet?|Боже мой, что не так с этим интернетом?
That's all we hear in IT because they don't know and that's, that's perfectly okay.|Это все, что мы слышим в ИТ, потому что они не знают, и это нормально.
So it's our, that's why it's our job as Cisco professionals,|Так что это наша, поэтому наша работа как профессионалов Cisco,
networking professionals, that we need to break up collision domains.|сетевым специалистам, что нам нужно разбивать домены коллизий.
This is the reason,|Это причина,
this is the reason that we need to break up collision domains, broadcast domains.|это причина того, что нам нужно разбить домены коллизии, широковещательные домены.
If we can break up broadcast domains [UNKNOWN] logically using VLANs,|Если мы сможем логически разбить широковещательные домены [НЕИЗВЕСТНО], используя VLAN,
segmentation's extremely important,|сегментация чрезвычайно важна,
because of the type of access method that we have, which is Ethernet.|из-за типа метода доступа, который у нас есть, а именно Ethernet.
Because of this.|Из-за этого.
Because everybody's trying to transmit at the same time.|Потому что все пытаются передавать одновременно.
And if you have everybody on the same VLAN, because by default we have one VLAN.|И если у вас все в одной VLAN, потому что по умолчанию у нас одна VLAN.
Right?|Правильно?
VLAN 1, on all the switches.|VLAN 1 на всех коммутаторах.
So we need to segment.|Итак, нам нужно сегментировать.
And it's, this is the reason right here.|И это причина прямо здесь.
That's why we don't use hubs.|Вот почему мы не используем хабы.
Hubs are a thing of the past, well,|Хабы ушли в прошлое, ну
multiport repeaters, right?|многопортовые повторители, да?
We don't use those anymore.|Мы их больше не используем.
We use switches.|Используем переключатели.
And the faster you go, the better it is.|И чем быстрее ты пойдешь, тем лучше.
So if you had the opportunity,|Итак, если бы у вас была возможность,
instead of doing 100 megabits per second,|вместо 100 мегабит в секунду,
you're doing 1,000 megabits per second,|вы делаете 1000 мегабит в секунду,
go ahead and do so, if it's feasible for the company.|действуйте и сделайте это, если это возможно для компании.
And it should be feasible, because you want productivity in your company.|И это должно быть осуществимо, потому что вы хотите продуктивности в своей компании.
All right?|Отлично?
But that's how this access method is,|Но вот каков этот метод доступа,
it's first come, first serve.|это первым пришел, первым подал.
All right?|Отлично?
Now this was put in place in case, so hey,|Теперь это было на всякий случай, так что, эй,
if more than one person, all right, is on the wire,|если более одного человека, хорошо, на проводе,
then it sends out that jamming signal,|затем он посылает сигнал глушения,
people got to wait for a period of time.|люди должны ждать какое-то время.
Run before they can transmit again.|Беги, прежде чем они снова смогут передавать.
But you don't want that to happen on a constant basis.|Но вы не хотите, чтобы это происходило постоянно.
Now how do you prevent that?|Как теперь предотвратить это?
This is where we talked about previously with the OSI and all these models,|Об этом мы говорили ранее с OSI и всеми этими моделями,
when you're building a network from the ground up.|когда вы строите сеть с нуля.
All right?|Отлично?
You keep the standards in mind.|Помните о стандартах.
Because, hey okay, this is a surveying company.|Потому что, ладно, это геодезическая компания.
We're using AutoCAD.|Мы используем AutoCAD.
We're doing all sorts of drawings.|Рисуем всевозможные.
Or, you know, heavy computations or big packets are going across constantly,|Или вы знаете, что тяжелые вычисления или большие пакеты проходят постоянно,
the network.|сеть.
And even, whatever, in there is a whole another story, but if we're doing within the local LAN,|И даже, что бы там ни было, это совсем другая история, но если мы делаем это в локальной сети,
definitely.|определенно.
You know, your boss wants to see your drawings, or you need to have a shared folder, or whatever the case may be, you want things to be quick.|Вы знаете, ваш босс хочет увидеть ваши рисунки, или вам нужна общая папка, или, в любом случае, вы хотите, чтобы все было быстро.
Because you know, you know, if you're in IT or going into IT and you work help desk, and I've worked help desk,|Потому что вы знаете, знаете, если вы занимаетесь ИТ или собираетесь в ИТ, и вы работаете в службе поддержки, а я работал в службе поддержки,
that those trouble tickets don't stop.|что эти билеты не прекращаются.
Don't stop, and the biggest complaint is my network is slow, my network is slow,|Не останавливайтесь, и самая большая жалоба - моя сеть медленная, моя сеть медленная,
my network is slow.|моя сеть медленная.
Why is your network slow?|Почему ваша сеть медленная?
How did you build it from the ground up?|Как вы построили его с нуля?
Did you segment properly?|Вы правильно сегментировали?
Did you take in consideration the standard that Ethernet is running, so people when they are sending information in their big packets, it's like hey,|Вы приняли во внимание стандарт, в котором работает Ethernet, поэтому люди, когда они отправляют информацию своими большими пакетами, это как эй,
you're running 10 megabits per second,|вы используете 10 мегабит в секунду,
what are you doing?|что вы делаете?
Or you're running 100 megabits per second,|Или вы используете 100 мегабит в секунду,
but everybody, you have, you know,|но все, вы знаете,
200 people underneath one one segment.|200 человек под одним сегментом.
You don't want to do it.|Вы не хотите этого делать.
They're all trying to go online, print,|Они все пытаются выйти в Интернет, распечатать,
access shared folders constantly, and these are big files.|доступ к общим папкам постоянно, а это большие файлы.
So these are things to take in consideration in understanding what this,|Вот что нужно учитывать, чтобы понять, что это,
how Ethernet works, and is based on that access method type.|как работает Ethernet, и на основе этого типа метода доступа.
I mentioned token ring.|Я упомянул токен-ринг.
See token ring never had their problem,|Смотрите, у токен-ринга никогда не было проблем,
because they had oh, oh, they had that free flowing token that will go around either counterclockwise or clockwise,|потому что у них был ой ой, у них был этот свободно текущий токен, который будет вращаться либо против часовой стрелки, либо по часовой стрелке,
depending on if you're using the IBM,|в зависимости от того, используете ли вы IBM,
original standard, or the IEEE 802.5.|исходный стандарт, или IEEE 802.5.
Whoever had that token, was the one that can talk, that can transmit information.|Тот, у кого был этот жетон, был тем, кто мог говорить, мог передавать информацию.
Once that token was obtained by the destination and it was released back on to the network, then the next person that gets it, can talk.|Как только этот токен был получен адресатом и передан обратно в сеть, следующий человек, который его получит, может говорить.
It was all on an orderly basis, but it was very slow, 16 megabits per second.|Все было организовано, но очень медленно, 16 мегабит в секунду.
Reliable, but slow.|Надежно, но медленно.
So that's why token ring didn't make it too, well it made it far enough, but it really, not say died off, but it's not as popular as Ethernet.|Вот почему Token Ring не добрался до него, ну, он прошел достаточно далеко, но на самом деле, не сказать, умер, но он не так популярен, как Ethernet.
Ethernet is the king, and that's the way we're, all networks are being turned to, is the Ethernet network.|Ethernet - это король, и именно так мы, все сети, обращаемся к сети Ethernet.
So the way we compensate for that access method, is having big pipes.|Таким образом, мы компенсируем этот метод доступа с помощью больших труб.
Having those 1,000 megabits per second,|Имея эти 1000 мегабит в секунду,
having across what are your networks,|в ваших сетях,
10 gigabits, or 100 gigabits, whatever it is, if you're sending information across.|10 гигабит или 100 гигабит, что бы это ни было, если вы пересылаете информацию.
Having the connection types would be least connection types,|Наличие типов подключения будет наименьшим количеством типов подключения,
using PPP, things like that so you have that full bandwidth all the time.|используя PPP и тому подобное, чтобы у вас всегда была полная пропускная способность.
But again, you need to justify that, you need to analyze.|Но опять же, это нужно обосновать, нужно проанализировать.
And I don't want to get into the design part, which I usually find myself going.|И я не хочу вдаваться в детали дизайна, чем я обычно занимаюсь.
But it's so important, because even though we don't like to talk about the USI and standards and all that, they're there for|Но это так важно, потому что, хотя мы не любим говорить о USI, стандартах и ​​прочем, они существуют для
a reason.|причина.
For us to understand, say hey,|Чтобы мы поняли, скажите эй,
we're creating an Ethernet network from the ground up, this company is XYZ.|мы создаем сеть Ethernet с нуля, эта компания - XYZ.
XYZ company sends big packets within their LAN across their WAN,|Компания XYZ отправляет большие пакеты внутри своей LAN через WAN,
so we need to make sure that there is no delay.|поэтому нам нужно убедиться, что нет задержек.
We need to, they're a big company, we need to segment them properly,|Нам нужно, это большая компания, нам нужно правильно их сегментировать,
we need to create VLANs, not only for bandwidth, but for security purposes.|нам нужно создавать сети VLAN не только для увеличения пропускной способности, но и в целях безопасности.
And you tweak things, and you go along and you do these things, and you create the gigabit Ethernet in the LAN.|И вы настраиваете вещи, и вы продолжаете, и делаете эти вещи, и вы создаете гигабитный Ethernet в локальной сети.
And you create, you know, ten gig you know, metro Ethernet.|И вы создаете, знаете, десять гигабайт, метро Ethernet.
Whatever it is that you want, across the wide area network.|Независимо от того, что вы хотите, по глобальной сети.
But again, you have to justify it.|Но опять же, вы должны это оправдать.
But that's get around the the 802.3|Но это обойти 802.3
contention based access method, where it's first come,|метод доступа на основе конкуренции, где он первый,
first serve.|первая подача.
So if you have ban enough bandwidth that it's not gonna matter,|Итак, если у вас достаточно полосы пропускания, это не имеет значения,
it's not gonna matter, then okay.|это не имеет значения, тогда ладно.
But if you're struggling in your LAN,|Но если у вас проблемы в локальной сети,
because you're running 100 megabits per second, and let me tell you, I've been in many, many,|потому что вы используете скорость 100 мегабит в секунду, и позвольте мне сказать вам, я был во многих, многих,
many, many, many, many, many, many, LANs.|много-много-много-много-много-много локальных сетей.
Where you're running 100 megabits per second, and you think that's the best thing in the world, and you have everybody,|Когда вы используете 100 мегабит в секунду и думаете, что это лучшее в мире, и у вас есть все,
all of a sudden, just you know, imaging,|внезапно, просто вы знаете, воображение,
and going online, and doing all these things, and you're in the same VLAN, your network comes to a crawl.|и выходя в интернет, и делая все это, и вы находитесь в одной и той же VLAN, ваша сеть начинает сканировать.
And we're just talking about 400 users,|И мы говорим о 400 пользователях,
400 users.|400 пользователей.
That's it, now imagine a large enterprise network.|Вот и все, теперь представьте себе большую корпоративную сеть.
A whole building 12, 14, 20 floors, that they're all part of the same company.|Целое здание 12, 14, 20 этажей, все они принадлежат одной компании.
And they all have to be inter-networked together at some point.|И все они в какой-то момент должны быть объединены в сеть.
Are you not going to separate those with VLANs?|Вы не собираетесь разделять их с помощью VLAN?
Are you not going to use gigabit?|Вы не собираетесь использовать гигабит?
What's going to be your backbone as you go across?|Что станет вашей опорой при переходе?
All these things is what you need to consider when you're creating these Ethernet networks.|Все это необходимо учитывать при создании сетей Ethernet.
You need to have that bandwidth available to a, avoid,|Вы должны иметь эту полосу пропускания, чтобы избежать,
not avoid, but to at least, since it is a first-come-first-serve,|не избегать, но по крайней мере, поскольку это - первый пришел - первый обслуживает,
that you have less and less collisions,|что у вас все меньше и меньше столкновений,
and that is our complete goal.|и это наша полная цель.
And have as much or as least I should say,|И иметь столько или по крайней мере я должен сказать,
downtime on your network.|время простоя в вашей сети.
And the least number of trouble tickets as possible.|И как можно меньше аварийных билетов.
Okay?|Ладно?
Because imagine if you get calls every day, I can't print, or not that I can't print printing's taking forever.|Потому что представьте, что если вам звонят каждый день, я не могу печатать или не могу печатать, печать занимает вечность.
It takes me you know, 15 minutes, I'm exaggerating,|Это занимает у меня 15 минут, я преувеличиваю,
15 minutes to print one Word document.|15 минут на печать одного документа Word.
Well that's a problem, you know, if it's telling, you know,|Ну, это проблема, знаете, если это говорит, знаете,
a small Word document is taking that long to print, something's going on.|небольшой документ Word так долго печатается, что-то происходит.
All right?|Отлично?
So all these things you need to take in consideration when you work with Ethernet,|Итак, все эти вещи необходимо учитывать при работе с Ethernet,
because of this access matter.|из-за этого вопрос доступа.
All right?|Отлично?
All right.|Отлично.
That's it for Ethernet.|Вот и все, что касается Ethernet.
I hope you understand how Ethernet works.|Надеюсь, вы понимаете, как работает Ethernet.
All right, and when you are creating your networks, keep that in mind.|Хорошо, и когда вы создаете свои сети, имейте это в виду.
So when you are going to these consulting jobs,|Итак, когда вы собираетесь работать консультантом,
you consult the company correctly based on what they do.|вы правильно консультируетесь с компанией, исходя из того, что они делают.
I'll see you in the next lesson.|Увидимся на следующем уроке.
[BLANK_AUDIO]|[BLANK_AUDIO]