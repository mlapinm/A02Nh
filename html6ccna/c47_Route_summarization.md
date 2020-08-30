D:\mailCloud\prjother\tmp\1\c47_Route summarization.md  


__|__
--|--
Welcome back, everyone.|С возвращением, все.
You just learned how to do classless sub-netting.|Вы только что научились делать бесклассовые подсети.
You know, DLSN, so,|Вы знаете, DLSN, так что,
this should be a cake walk for you.|это должна быть прогулка с тортом для вас.
Or it could be I'm throwing a screwdriver into so many because now we're going to opposite way.|Или, может быть, я бросаю отвертку во многих, потому что теперь мы идем по другому пути.
What is route summarization and there seems to be some sort of confusion between route summarization and when we get into the distance vector routing|Что такое суммирование маршрута? Кажется, есть некоторая путаница между суммированием маршрута и тем, когда мы переходим к векторной маршрутизации расстояния
protocols that I tell everybody to put no auto-summary.|протоколы, которые я говорю всем не ставить авто-сводку.
And I get hey Laz, but isn't it a good thing to summarize?|И я получаю привет, Лаз, но разве не стоит подвести итоги?
Most definitely it's a good thing to summarize when we're sending,|Определенно, это хорошо, когда мы отправляем
we're advertising the summary route that include all these networks in there.|мы рекламируем сводный маршрут, включающий все эти сети.
That way you're core router,|Таким образом, вы основной маршрутизатор,
right, has less to look at.|да, есть на что меньше смотреть.
Because all those networks are encompassed in there.|Потому что все эти сети заключены в нем.
Route summarization.|Обобщение маршрута.
When we're talking about our routing protocol, such as RIP version two or EIGRP, where they have the,|Когда мы говорим о нашем протоколе маршрутизации, таком как RIP версии два или EIGRP, где у них есть,
where you have to, where you have to put no auto hyphen summary,|где вам нужно, где вы не должны ставить краткое описание автоматического переноса,
it's different.|это другое.
Because the routing protocol will summarize automatically to the class full boundary.|Потому что протокол маршрутизации автоматически суммируется до полной границы класса.
Now I don't want to get too detailed in it cuz we're not talking about routing protocols.|Я не хочу вдаваться в подробности, потому что мы не говорим о протоколах маршрутизации.
But I want to make a distinction that the no auto summary command and route summarization are two separate entities.|Но я хочу отметить, что команда no auto summary и суммирование маршрута - это две разные сущности.
Because if you do not put no auto hyphen summary in EIGRP or RIP version two, and you're running an entire network with a class A or|Потому что, если вы не добавляете сводку автоматического переноса в EIGRP или RIP версии два, и вы используете всю сеть с классом A или
a class B, it will not know where to send the information.|класс B, он не будет знать, куда отправить информацию.
All right, so route summarization is completely different.|Хорошо, итоги маршрута совсем другие.
And I will actually show you the command that you will use to advertise that summary route to a core router.|И я на самом деле покажу вам команду, которую вы будете использовать для объявления этого сводного маршрута к базовому маршрутизатору.
And much later in the course you will have a summary lab to do,|И гораздо позже в ходе курса вам предстоит выполнить итоговую лабораторную работу,
in order f, to reduce the number of entries in that core router.|для того, чтобы уменьшить количество записей в этом основном маршрутизаторе.
Right, that Cisco three layer model,|Хорошо, эта трехуровневая модель Cisco,
that core router,|этот основной маршрутизатор,
we want to burn it with so many entries.|мы хотим сжечь его таким количеством записей.
So one of the ways we can do that is to do route summarization.|Таким образом, один из способов сделать это - обобщить маршрут.
Now, route summarization, just like VLSM,|Теперь суммирование маршрута, как и VLSM,
has its rules, all right, has its rules.|есть свои правила, хорошо, есть свои правила.
According to route summarization rules,|Согласно правилам суммирования маршрута,
you should, I'm not gonna say you must,|ты должен, я не скажу, что ты должен,
I'm gonna say you should you should.|Я скажу, что ты должен.
You should start with a even,|Вам следует начать с четного,
an even number network.|сеть с четными номерами.
That's not an even number network,|Это не сеть с четными числами,
that's an odd number network right, 1.0.|это нечетное число сети верно, 1.0.
And you should have an even number of networks which I don't.|И у вас должно быть четное количество сетей, чего у меня нет.
I have three networks, not two or four.|У меня три сети, а не две или четыре.
Now, in the certification exam,|Теперь на сертификационном экзамене
you do not care about that.|тебя это не волнует.
I'll say it again, just in case some of you say, he, he didn't say that, did he?|Я повторю это еще раз, на случай, если некоторые из вас скажут, он, он этого не говорил, не так ли?
Yes, I did.|Да, я сделал.
You don't care,|Тебе все равно,
because what they're gonna do in the exam,|потому что что они собираются делать на экзамене,
they're gonna give you a bunch of networks, and you need to summarize them.|они дадут вам кучу сетей, и вам нужно их обобщить.
Period.|Период.
Whether they're odd, even, or whatever it is, you need to know how to summarize networks.|Будь они нечетными, четными или чем-то еще, вам нужно уметь резюмировать сети.
That's it.|Вот и все.
Don't worry about that there contiguous,|Не беспокойтесь о том, что там смежные,
discontiguous or whatever it is because that's another rule.|несмежные или что-то еще, потому что это другое правило.
If you're going to summarize networks,|Если вы собираетесь резюмировать сети,
they should fall in a contiguous order.|они должны располагаться в непрерывном порядке.
But again ladies and gentlemen,|Но снова дамы и господа,
our focus is to take a certification exam.|наша цель - сдать сертификационный экзамен.
And if in the certification exam they tell you hey, I need you to summarize these networks, you will summarize those networks regardless.|И если на сертификационном экзамене вам скажут, эй, мне нужно, чтобы вы суммировали эти сети, вы все равно суммируете эти сети.
And they're usually gonna in a contiguous order anyway.|И в любом случае они обычно собираются в непрерывном порядке.
Now, I know on the internet there's many ways to go ahead and summarize, some of them using exponent values and what have you.|Теперь я знаю, что в Интернете есть много способов подвести итоги, некоторые из них используют значения экспоненты и то, что у вас есть.
And it's very simple and easy and quick to use, but it does not always work.|И это очень просто, легко и быстро в использовании, но не всегда работает.
And how can I dare say something like that?|И как я могу такое сказать?
Because I used to use that method, okay?|Потому что я использовал этот метод, хорошо?
And when I would put, at one point,|И когда я бы сказал, что однажды
I started putting in the advertised,|Я начал вставлять рекламируемые,
so bring the route in the router.|так что занесите маршрут в роутер.
And my router screamed at me and said, you are crazy.|И мой роутер наорал на меня и сказал, что ты сумасшедший.
I'm not going to accept that, that's the wrong math for what you're doing.|Я не собираюсь с этим соглашаться, это неправильная математика для того, что вы делаете.
I was like what?|Я был похож на что?
So Cisco states do it binary.|Таким образом, Cisco утверждает, что это двоичный код.
Binary.|Двоичный.
You will always get the same answer.|Вы всегда получите один и тот же ответ.
The, the right answer.|Правильный ответ.
The correct answer.|Правильный ответ.
Now some of you may be saying,|Некоторые из вас могут сказать:
my god, in binary, really?|Боже мой, в двоичном формате, правда?
You're not gonna get big numbers to turn these things into binary.|Вы не получите больших чисел, чтобы превратить эти вещи в двоичные.
And you're gonna see how easy it is.|И вы увидите, как это просто.
And after you get practice with it, you're going to be doing the first network,|И после того, как вы попрактикуетесь с этим, вы будете делать первую сеть,
the last network and then you'll know where the summary address will be.|последняя сеть, и тогда вы узнаете, где будет итоговый адрес.
Like I said, repetition breeds retention.|Как я уже сказал, повторение порождает удержание.
At first when we learned our time tables,|Сначала, когда мы изучили наши расписания,
you're like oh my God.|ты как боже мой.
What is nine times seven?|Сколько девять умножить на семь?
I knew it yesterday.|Я знал это вчера.
My God, I knew what seven times nine was but nine times seven it just confuses me.|Боже мой, я знал, что такое семь умножить на девять, но девять умножить на семь это меня просто сбивает с толку.
And we remember our times tables, and then we went on and on and on, calculus,|И мы вспоминаем наши таблицы умножения, а потом продолжали и продолжали, исчисление,
algebra, all this craziness, okay?|алгебра, все это безумие, хорошо?
And we went on and on, and we learned it.|И мы продолжали и продолжали, и мы узнали это.
So you'll learn this, okay?|Так ты научишься этому, хорошо?
So, we're gonna summarize these three networks.|Итак, мы суммируем эти три сети.
The interesting octet that we're gonna be looking at is the third octet.|Интересный октет, который мы собираемся рассмотреть, - это третий октет.
So we're going to go ahead.|Итак, мы продолжим.
Let me give me some space here.|Позвольте мне дать мне здесь немного места.
Okay, I thought I had space there.|Хорошо, я думал, у меня там есть место.
Okay.|Ладно.
There we go.|Вот и все.
All right, so we're going to go ahead.|Хорошо, мы продолжим.
We know that the interesting octet is the third so the first and second remain the same.|Мы знаем, что интересный октет - третий, поэтому первый и второй остаются неизменными.
Space, space x.x, right?|Пробел, пробел x.x, верно?
I'm going to copy that.|Я скопирую это.
Ctrl+C.|Ctrl + C.
Space space.|Космическое пространство.
Ctrl+V.|Ctrl + V.
Space Space Ctrl+V.|Пробел Пробел Ctrl + V.
All right?|Отлично?
This is called pure laziness right?|Это называется чистой ленью, верно?
No.|Нет.
Now I need visualization.|Теперь мне нужна визуализация.
So I'm going to put my bid values.|Итак, я выставлю свои ставки.
64, 32, 16, eight, four, two, and one,|64, 32, 16, восемь, четыре, два и один,
and that will put the octet later.|октет будет помещен позже.
All right, so you can have that visualization also.|Хорошо, так что вы тоже можете получить эту визуализацию.
So I put the first three octets.|Итак, я поставил первые три октета.
Now let's turn that third octet into binary,|Теперь давайте превратим этот третий октет в двоичный,
which as you can see is not that difficult.|что, как видите, не так уж и сложно.
0 0 0 0 0 0 0 1.|0 0 0 0 0 0 0 1.
Now, 0 0 0 0|Сейчас, 0 0 0 0
0 0 1 0.|0 0 1 0.
Zero.|Нуль.
Oops.|Ой.
0 0 0 0 0 0 1 1.|0 0 0 0 0 0 1 1.
Oops, one.|Ой, один.
All right, and then we have our fourth octet obviously.|Хорошо, а затем, очевидно, у нас есть четвертый октет.
And we'll put this really separate, one,|И мы поместим это отдельно, одно,
two, three, four, five, six, seven, eight,|два, три, четыре, пять, шесть, семь, восемь,
cuz it really doesn't take,|Потому что это действительно не нужно,
it doesn't do anything in this scenario.|в этом сценарии он ничего не делает.
All right, so again visualize the four octets.|Хорошо, снова визуализируйте четыре октета.
Now what you're actually doing is,|Теперь то, что вы на самом деле делаете,
the default line is right here, all right.|линия по умолчанию прямо здесь, хорошо.
Cuz you have three separate class C networks.|Потому что у вас есть три отдельные сети класса C.
They're, they're working, you know,|Они, они работают, понимаете,
the, you have the CIDR 24 so the line is actually right here.|у вас есть CIDR 24, так что линия на самом деле прямо здесь.
So what we're trying to do, we're making instead of subnetting, we're supernetting,|Итак, то, что мы пытаемся сделать, мы делаем вместо подсетей, мы создаем суперсети,
or we're summarizing,|или мы подводим итоги,
we're bringing the line to the left.|мы переносим линию влево.
Something that I always said you don't do.|То, что я всегда говорил, что ты не делаешь.
So any time you see a class C, right,|Итак, каждый раз, когда вы видите класс C, верно,
cuz I identify it by the first octet,|Потому что я идентифицирую его по первому октету,
class C network that has a mask that's less, that's smaller than a slash or a CIDR 24, you know or it's a pretty good hint that|сеть класса C, у которой маска меньше, меньше косой черты или CIDR 24, ну или это довольно хороший намек на то, что
that is a summarized address.|это краткий адрес.
All right, so how do we move that line over?|Хорошо, так как нам переместить эту линию?
Well, what we do is we go from left to right and we look for the uncommon bit values.|Что ж, мы идем слева направо и ищем необычные битовые значения.
And what does that mean, uncommon?|А что это значит, необычно?
Well in this column right here,|В этой колонке прямо здесь,
they're all common with each other, right?|все они общие, не так ли?
They're all zeroes.|Все они нули.
They're all zeroes.|Все они нули.
They're all zeroes.|Все они нули.
They're all zeroes.|Все они нули.
They're all zeroes.|Все они нули.
They're all zeroes.|Все они нули.
Aha, zeroes and ones,|Ага, нули и единицы,
well they're not common to each other.|ну они не общие друг для друга.
If they will be all ones,|Если они будут все едины,
they'll be good to go.|они будут в порядке.
If they'll be all zeroes,|Если они все будут нулями,
they'll be good to go.|они будут в порядке.
But they have a combination of zeroes and ones,|Но у них есть сочетание нулей и единиц,
therefore we draw our line, right there.|поэтому мы рисуем нашу линию прямо здесь.
Where, where's my line?|Где, где моя линия?
That's the wrong line.|Это неправильная линия.
Line right there,|Линия прямо там,
let's bring this over here.|давайте принесем это сюда.
Space I think.|Я думаю, космос.
No it's making a mess out of all this.|Нет, все это создает беспорядок.
Again I do it, okay?|Я снова делаю это, хорошо?
When you're here, line, moving down, line.|Когда вы здесь, линия, движение вниз, линия.
Let's make it look pretty.|Давайте сделаем это красивым.
Okay.|Ладно.
And here, all right, so we have our new line.|И вот, ладно, у нас есть новая линия.
Our original line was here.|Наша первоначальная линия была здесь.
That was our original line.|Это была наша оригинальная линия.
But now, our new line, or new mask,|Но теперь наша новая линия или новая маска,
I should say, is over here,|Я должен сказать, здесь,
which is a 22, right,|что 22, верно,
cuz we got eight bits on right there.|Потому что у нас тут восемь бит.
We got eight bits on right there.|У нас тут восемь битов.
That's 17, 18, 19, 20, 21, 22.|Это 17, 18, 19, 20, 21, 22.
So we have a slash or CIDR 22, that is our new mask that will encompass all those networks.|Итак, у нас есть косая черта или CIDR 22, это наша новая маска, которая будет охватывать все эти сети.
So now, what is the,|Итак, что это за
what's called the summary address?|как называется сводный адрес?
What numbers do I put in?|Какие числа я ввожу?
Well, first two octets are the same,|Ну, первые два октета одинаковые,
but what do I put in the third octet?|а что я вставляю в третий октет?
Well, you look between the line that you just drew,|Что ж, вы смотрите между линией, которую вы только что нарисовали,
up to the third octet,|до третьего октета,
they're all zeros, so it's all off.|они все нули, так что все выключено.
Zero.|Нуль.
And the fourth octet,|И четвертый октет,
obviously, is all zeros.|очевидно, все нули.
Therefore, zero.|Следовательно, ноль.
That is the summary address, and this is exactly what you would advertise,|Это сводный адрес, и это именно то, что вы бы рекламировали,
all right?|отлично?
And how would you advertise something like this?|А как бы вы такое рекламировали?
And I'll use EIGRP because your packet tracer only supports EIGRP.|И я буду использовать EIGRP, потому что ваш трассировщик пакетов поддерживает только EIGRP.
That does not mean that you can't do it with other protocols, you sure can,|Это не означает, что вы не можете сделать это с другими протоколами, вы точно можете,
all right?|отлично?
But for the packet tracer,|Но для трассировщика пакетов
EIGRP is the one that you will use.|EIGRP - это тот, который вы будете использовать.
So when you're advertising the summary address, you're advertising it more likely to a core router to reduce the amount of entries in that routing table.|Таким образом, когда вы объявляете сводный адрес, вы с большей вероятностью объявляете его базовому маршрутизатору, чтобы уменьшить количество записей в этой таблице маршрутизации.
Therefore you would say IP summary.|Следовательно, вы бы сказали «Резюме IP».
I think my spelling is correct.|Думаю, мое написание правильное.
I usually do a lotta tabbing.|Я обычно делаю много табуляции.
Address [LAUGH] IP summary address.|Адрес [LAUGH] Общий IP-адрес.
The routing protocol in use,|Используемый протокол маршрутизации,
the autonomous system, all right,|автономная система, хорошо,
let's just call it 100.|давайте просто назовем это 100.
And then the actual summary address.|А затем фактический сводный адрес.
192.168.0.0 with a 255.255.|192.168.0.0 с 255.255.255.
What's six bits on?|Что на шести битах?
252.0.|252,0.
That is how you would advertise, and it will go through an interface,|Это то, как вы бы рекламировали, и это будет проходить через интерфейс,
meaning, you actually do this in an interface configuration mode.|это означает, что вы фактически делаете это в режиме конфигурации интерфейса.
And advertise that summary route to that summary that to that core router.|И объявите этот сводный маршрут этому сводному маршрутизатору.
But that brings up a question, hey Laz well how does it know to use that and not the actual protocol that's,|Но тут возникает вопрос: привет, Лаз, откуда он знает, что использовать именно этот протокол, а не настоящий протокол,
that, you know,|это ты знаешь,
EIGRP because that's the protocol in use,|EIGRP, потому что это используемый протокол,
to use that protocol?|использовать этот протокол?
To use the main protocol cuz you did configure in global configuration EIGRP,|Чтобы использовать основной протокол, потому что вы настроили в глобальной конфигурации EIGRP,
why isn't it using that?|почему он этого не использует?
And now what,|И что теперь,
because you put it on the interface?|потому что вы ставили на интерфейс?
It's not the fact that I put it on the interface, because once you see once we do this lab, that you put this, and then you look at it again, let's say through|Не факт, что я поместил это в интерфейс, потому что, как только вы увидите, как только мы проведем эту лабораторную работу, вы поместите это, а затем посмотрите на это снова, скажем, через
the show start or show run, you're gonna see that's gonna add a five to it.|начало шоу или запуск шоу, вы увидите, это добавит к нему пять.
And what that five is is the administrative distance of a summary route.|И что это за пять - это административное расстояние суммарного маршрута.
And what that does is that oh, if you,|И что он делает, это то, о, если ты,
oh, you can't see that, I'm sorry.|о, ты этого не видишь, извини.
It adds a five to it.|К нему добавляется пять.
You didn't put it.|Вы не поставили.
I didn't put it.|Я не ставил.
But when you look at the start,|Но когда вы смотрите на начало,
it actually adds it because it is a summary route.|он фактически добавляет его, потому что это сводный маршрут.
And that summary route has an administrative distance of five.|И этот суммарный маршрут имеет административное расстояние пять.
EIGRP has an administrative distance of 90.|EIGRP имеет административное расстояние 90.
So who's more believable?|Так кто правдоподобнее?
The one with the lower administrative distance.|Тот, у которого административная удаленность меньше.
Therefore that core router will pay attention to that advertisement and not the other, okay?|Следовательно, основной маршрутизатор будет обращать внимание на эту рекламу, а не на другую, хорошо?
But you'll see when you do that line.|Но вы увидите, когда сделаете эту строчку.
So we'll do a couple more examples just so you get comfortable with it, all right?|Итак, мы сделаем еще пару примеров, чтобы вы освоились, хорошо?
There's just a first example and that, this syntax that I just wrote up there is an example how you would use that summary address because the reason|Есть только первый пример, и этот синтаксис, который я только что написал, является примером того, как вы могли бы использовать этот сводный адрес, потому что причина
you're using it is to advertise it, so you can have less entries in your routing tables, and that is your goal, all right?|вы используете его для рекламы, чтобы у вас было меньше записей в таблицах маршрутизации, и это ваша цель, хорошо?
It's easier to look at, let's say, a hundred routes versus a million routes, so you wanna reduce that because you wanna,|Проще рассматривать, скажем, сотню маршрутов по сравнению с миллионом маршрутов, поэтому вы хотите уменьшить это, потому что вы хотите,
you,|ты,
you don't wanna burden the router, all right, by looking and looking and looking.|Вы же не хотите перегружать маршрутизатор, глядя, глядя и глядя.
I mean, it's just, you know, not feasible.|Я имею в виду, это просто, понимаете, неосуществимо.
Not feasible.|Неосуществимо.
All right, let's do another example.|Хорошо, давайте сделаем еще один пример.
Where am I?|Где я?
Here I am.|А вот и я.
All right, so let's do it again, 192.168.|Хорошо, давайте сделаем это снова, 192.168.
We'll use bigger numbers.|Мы будем использовать большие числа.
Let's do let's do 100.|Давайте сделаем, давайте сделаем 100.
Let's start with an even number,|Начнем с четного числа,
all right,|отлично,
.0, 192.168.101.0.|.0, 192.168.101.0.
192.168.102.0 and 192.168.103.0, okay?|192.168.102.0 и 192.168.103.0, ладно?
So now we have an even number, right?|Итак, теперь у нас четное число, верно?
The rule, we have an even number network,|Правило, у нас четная сеть,
100 and let's bring this up,|100 и давайте поднимем это,
all right, so you guys can see that.|хорошо, так что вы, ребята, это видите.
So we have an even number network and we have an even number of networks.|Итак, у нас есть четная сеть, и у нас есть четное количество сетей.
So now that should be able to work perfectly, and let me explain that or elaborate on that because I didn't elaborate on the previous example,|Итак, теперь это должно работать идеально, и позвольте мне объяснить это или уточнить это, потому что я не уточнял предыдущий пример,
I do apologize for that.|Прошу прощения за это.
If you notice, that our original networks was one, two, and three,|Если вы заметили, что наши исходные сети были один, два и три,
all of a sudden, now we got zero.|внезапно мы получили ноль.
So we just added a network to it.|Итак, мы просто добавили к нему сеть.
So when you have these odd-numbered networks and so forth, and sometimes even numbered networks, that happens too.|Так что, когда у вас есть сети с нечетными номерами и так далее, а иногда и с четными номерами, такое тоже происходит.
The rule doesn't always work, okay?|Правило не всегда работает, хорошо?
You have the stray networks that all of a sudden appear in in the summary address.|У вас есть случайные сети, которые внезапно появляются в итоговом адресе.
There are additions to it.|К нему есть дополнения.
It's just the way it is, all right?|Так оно и есть, хорошо?
It's just the way the bit falls, okay?|Просто бит падает, хорошо?
It's just the way the bit falls.|Просто бит падает.
So it's up to you on how you wanna go ahead and do that, all right?|Так что тебе решать, как ты хочешь пойти дальше и сделать это, хорошо?
So let's go ahead and do this,|Итак, давайте продолжим и сделаем это,
this I'm sorry, where am I here?|это извините, где я здесь?
Okay, boom, boom, boom, boom, boom.|Ладно, бум, бум, бум, бум, бум.
All right, so let's set this up.|Хорошо, давайте настроим это.
So, x.|Итак, х.
How am I doing?|Как я поживаю?
X.x.|X.x.
Copy that.|Скопируй это.
X.x.|X.x.
Ok, what's going on?|Хорошо, что происходит?
It's almost the end, my friends.|Это почти конец, друзья мои.
All right, and then we, I need my visualization, I need my big values.|Хорошо, а потом нам, мне нужна моя визуализация, мне нужны мои большие ценности.
So I know what to put for the third octet.|Так что я знаю, что ставить для третьего октета.
128, 64, 32, 16, eight, four, two and one.|128, 64, 32, 16, восемь, четыре, два и один.
And we'll put the fourth octet when we're done.|А когда закончим, мы поместим четвертый октет.
All right?|Отлично?
So, let's go ahead and put a 100 in binary.|Итак, давайте продолжим и поместим 100 в двоичную систему.
So that's zero, 64 for sure,|Так что это ноль, 64 точно,
32 for sure, that's 96.|32 точно, это 96.
16 too much.|16 многовато.
Eight, too much.|Восемь - многовато.
Four, hey, that's 100.|Четыре, эй, это 100.
And then zero, zero.|А потом ноль, ноль.
So there's your 100 right there.|Так что вот ваша сотня.
Okay?|Ладно?
So all, already you know that 64 and 32 are always going to be on,|Итак, вы уже знаете, что 64 и 32 всегда будут включены,
because you have to get to 100,|потому что вам нужно дойти до 100,
so that's 96.|так что это 96.
And you need the four on, because,|И вам нужна четверка, потому что,
okay, how did that get up there?|хорошо, как это там попало?
You need this one here,|Вам нужен этот здесь,
cause that's 100, then you need 101.|потому что это 100, тогда вам нужно 101.
You see that?|Ты видишь это?
So zero, one, one,|Так что ноль, один, один,
didn't it go to zero, three?|не до нуля, до трех?
Cause I know I did.|Потому что я знаю, что сделал.
100 and two.|100 и два.
And then I know I did 103.|И тогда я знаю, что сделал 103.
Somehow it got erased.|Как-то стерлось.
So x.x, zero, one, one, zero, zero, one,|Итак, x.x, ноль, один, один, ноль, ноль, один,
that's 100, and now we need three.|это 100, а теперь нам нужно три.
All right?|Отлично?
Well let's put the fourth octet, right?|Ну что ж, четвертый октет поставим, да?
We want that visualization.|Мы хотим эту визуализацию.
One, two, three, four, five, six,|Один два три четыре пять шесть,
seven, eight, let's copy that.|семь, восемь, давайте скопируем это.
Control-C.|Ctrl-C.
[NOISE] All right,|[NOISE] Хорошо,
there's your four octet.|вот вам четыре октета.
So, again, left to right,|Итак, снова слева направо,
common bits, common bits.|общие биты, общие биты.
They're all common, all common,|Все они общие, все общие,
they're all the same,|они все одинаковые,
they're all the same, they're all the same, they're all the same.|все они одинаковые, все одинаковые, все одинаковые.
[SOUND] Different.|[ЗВУК] Разное.
We stop right there on the two column,|Останавливаемся тут же на двух колоннах,
right?|право?
We have zeros and ones, all again.|У нас снова есть нули и единицы.
So, we have a 22 again.|Итак, у нас снова 22.
Let me see something.|Дай мне кое-что посмотреть.
I think I no I did it right, okay.|Я думаю, что нет, я сделал это правильно, хорошо.
All right, so it falls in there again.|Хорошо, он снова попадает туда.
The line falls right there again.|Линия снова падает.
All right?|Отлично?
Just the way it is.|Просто так оно и есть.
I'm just making up numbers as I go,|Я просто придумываю числа, когда иду,
all right?|отлично?
So all right, so, we s, have again a /22.|Итак, хорошо, у нас снова есть / 22.
But what is our summary address?|Но каков наш сводный адрес?
192.168 dot what?|192.168 точка что?
Remember, our line is right there.|Помните, наша линия прямо там.
So anything beyond, that way of the line,|Так что все, что выходит за рамки этой линии,
if it's on, you got to add it.|если он включен, вы должны его добавить.
So, well, 64, 32, and four, they're all aligned.|Итак, 64, 32 и четыре, они все выровнены.
So, guess what?|Итак, угадайте, что?
It's 100.|Это 100.
Dot zero.|Нулевая точка.
That is your summary address.|Это ваш краткий адрес.
And that is our beginning address,|И это наш начальный адрес,
is it not?|это не?
My spelling is, wow.|Мое правописание - вау.
I have tabbed so much in the router that I have forgotten to spell.|Я столько закладок в роутере, что забыл записать.
Okay, summary address.|Хорошо, краткий адрес.
That is a summary address right there.|Вот краткий адрес.
All right, and you would advertise it the same way you did the previous one.|Хорошо, и вы бы его рекламировали так же, как и предыдущий.
But now, okay, so we summarize addresses, but sometimes in the test they don't give you for you to summarize addresses,|Но теперь, хорошо, поэтому мы суммируем адреса, но иногда в тесте они не дают вам суммировать адреса,
they actually give you a summary address.|они фактически дают вам краткий адрес.
And then they'll tell you hey,|А потом они скажут тебе, эй,
what networks, or what IPs will be forwarded if you're using this summary address?|какие сети или какие IP-адреса будут перенаправляться, если вы используете этот суммарный адрес?
So you need to know the range of addresses that exist within this summary address.|Итак, вам необходимо знать диапазон адресов, которые существуют в этом сводном адресе.
Well we, it should be 100, 101, 102, 103.|Ну мы, должно быть 100, 101, 102, 103.
But how will we find out?|Но как мы узнаем?
We would do out same procedures that we would always do.|Мы выполняли те же процедуры, что и всегда.
Our line is right here correct?|Наша линия прямо здесь, правильно?
That's the third octet.|Это третий октет.
Okay two plus one is three.|Хорошо, два плюс один - три.
Third octet three plus 100 is 103.|Третий третий октет плюс 100 равно 103.
[NOISE] 192 I got 168 dot 103.|[ШУМ] 192 Я получил 168 точек 103.
And then we had all these bit values over here.|И тут у нас были все эти битовые значения.
That's 255 plus the zero, that's 255.|Это 255 плюс ноль, это 255.
And guess what?|И угадайте, что?
It works out perfectly.|Получается отлично.
We do not introduce any new networks at all.|Мы вообще не вводим никаких новых сетей.
So the rule holds true in this case.|Так что в данном случае правило остается в силе.
You start with an even number network,|Вы начинаете с четной сети,
you finish,|ты заканчиваешь,
you have an even number of networks.|у вас четное количество сетей.
It works out perfectly.|Получается отлично.
All those networks follow each other.|Все эти сети следуют друг за другом.
There is no 99 network, or 104 network.|Нет сети 99 или сети 104.
It's just those networks right there.|Это просто те сети.
So that's what you would need to do.|Вот что вам нужно сделать.
That will give you a summary address like the sider 22 and the 192.168.100.0, and then they would ask you well, what net,|Это даст вам общий адрес, такой как sider 22 и 192.168.100.0, а затем они спросят вас, какая сеть,
what networks would be advertised or what IP addresses would be advertised that you need to choose three or choose two, what have you.|какие сети будут рекламироваться или какие IP-адреса будут рекламироваться, что вам нужно выбрать три или выбрать два, что у вас есть.
You will need to know the range of broadcast address will never be an IP address that's advertised.|Вам нужно будет знать, что диапазон широковещательных адресов никогда не будет объявленным IP-адресом.
A network address, yes.|Сетевой адрес, да.
An IP address or a a useable IP address, yes.|Да, IP-адрес или полезный IP-адрес.
Never a broadcast, never a broadcast.|Ни трансляции, ни трансляции.
So this is route summarization.|Итак, это обобщение маршрута.
The best method, the method that Cisco prefers, is to do it in binary.|Лучший метод, метод, который предпочитает Cisco, - это сделать это в двоичном формате.
Do it in binary.|Сделайте это в двоичном формате.
Turn whatever aug tech you're working in into binary.|Превратите любую технологию, над которой вы работаете, в двоичную систему.
Draw your line where the on prum and bit values are, that will be your new mask.|Нарисуйте линию там, где находятся значения prum и bit, это будет ваша новая маска.
And then if there's any on b,|А затем, если они есть на b,
any of the ones that are on,|любой из тех, что включены,
you just add those up and put it as your summary address.|вы просто складываете их и указываете как сводный адрес.
And that is it.|Вот и все.
That is it.|Вот и все.
So this is raw summarization.|Итак, это грубое обобщение.
Will you be asked questions on summarization?|Будут ли вам заданы вопросы по обобщению?
Yes you will.|Да, вы будете.
There will be at least, maybe three to five questions on your exam.|На экзамене будет не менее трех-пяти вопросов.
Well you will have to either summarize given addresses or you would have to find the addresses within that summary address.|Что ж, вам нужно будет либо суммировать данные адреса, либо вам нужно будет найти адреса в этом сводном адресе.
And that's where you would do this number right here.|И вот где вы бы сделали это число прямо здесь.
Our normal procedures that we would do for subnetting.|Наши обычные процедуры, которые мы выполняем для разделения на подсети.
All right?|Отлично?
So we've gone through classful subnetting,|Итак, мы прошли классовое разбиение на подсети,
we've gone through classless subnetting,|мы прошли через бесклассовое разбиение на подсети,
and now you've done route summarization.|и теперь вы сделали суммирование маршрута.
Okay?|Ладно?
Now you know the secrets.|Теперь вы знаете секреты.
I'll see you in the next lecture.|Увидимся на следующей лекции.