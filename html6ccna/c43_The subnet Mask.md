D:\mailCloud\prjother\tmp\1\c43_The subnet Mask.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
All right, we've come into the realm of subnetting.|Хорошо, мы подошли к разделу подсетей.
This section is going to be long and painful.|Этот раздел будет длинным и болезненным.
No, it's not.|Нет, это не так.
It's not painful at all.|Это совсем не больно.
It's not, I want to shed light, get it?|Это не так, я хочу пролить свет, понятно?
Shed light on the subject.|Пролить свет на предмет.
It is not physics.|Это не физика.
It is not three different or four different differential equations.|Это не три или четыре разных дифференциальных уравнения.
So you don't have to worry about that,|Так что тебе не о чем беспокоиться,
okay?|Ладно?
It's simple, it's easy.|Это просто, это просто.
Like it says right there, the subnet mask is the key.|Как тут же сказано, ключом является маска подсети.
That's the first thing we want to talk about, the subnet mask.|Это первое, о чем мы хотим поговорить, - маска подсети.
In your examination, pray,|На экзамене молитесь,
hope, whatever it is that they ask you,|надеюсь, что бы они ни просили,
direct questions like, if you have this IP address or this mask, what network,|прямые вопросы, например, есть ли у вас этот IP-адрес или эта маска, в какой сети,
what's the network ID, what's the range and what's the broadcast?|какой идентификатор сети, какой диапазон и какая трансляция?
That would be excellent.|Это было бы отлично.
But they're not gonna ask you that.|Но они не будут спрашивать тебя об этом.
Everything's gonna be hidden within an, I told you, within a NAT question or within an access list or an OSPS statement.|Все будет спрятано в, как я вам сказал, в вопросе NAT, в списке доступа или в заявлении OSPS.
And then you'll have to figure it out by doing reverse engineering, you know.|А потом вам придется разобраться в этом с помощью обратного проектирования.
Oh, okay, has this wall card mask, so this is this.|О, хорошо, у тебя есть маска на стене, так вот это.
And we're gonna talk about all those different things here in this particular section, okay?|И мы собираемся поговорить обо всех этих разных вещах здесь, в этом конкретном разделе, хорошо?
But the first thing is the subnet mask.|Но в первую очередь это маска подсети.
If you're given a subnet mask,|Если вам дана маска подсети,
automatically you need to understand where that line, which people have been calling now the magical line.|автоматически вам нужно понять, где та линия, которую люди теперь называют волшебной линией.
Which it is a magical line because once you draw that line, you know what's up.|Это волшебная линия, потому что как только вы ее проведете, вы поймете, в чем дело.
You know your break, once you draw the line you know how many holes you have,|Вы знаете свой разрыв, когда вы проводите линию, вы знаете, сколько у вас отверстий,
you know how many subnets you have, you know what your broadcast add,|вы знаете, сколько у вас подсетей, вы знаете, что добавляет ваша трансляция,
not your broadcast address, what your wildcard mask is going to be,|не ваш широковещательный адрес, какова будет ваша подстановочная маска,
you know how your network is gonna increment.|вы знаете, как будет расти ваша сеть.
It gives you all that information right there at your fingertips.|Он дает вам всю эту информацию прямо у вас под рукой.
All right?|Отлично?
I'm telling you, the subnet mask is the key to everything, but this is the problem.|Я говорю вам, маска подсети - это ключ ко всему, но в этом проблема.
If they give you a 255.255.255.0, okay,|Если они дадут вам 255.255.255.0, хорошо,
that's easy enough.|это достаточно просто.
We know, that that means that eight bits are on, eight bits are on,|Мы знаем, что это означает, что восемь бит включены, восемь бит включены,
eight bits are on, and then one, two,|восемь бит включены, а затем один, два,
three, four, five, six, seven, eight.|три, четыре, пять, шесть, семь, восемь.
That means our line is right here, we understand that, and that means that when your, your network id,|Это означает, что наша линия находится прямо здесь, мы это понимаем, и это означает, что когда ваш идентификатор сети,
will be X dot X dot X dot zero then you add all these bit values right here,|будет X точка X точка X точка ноль, тогда вы добавляете все эти битовые значения прямо здесь,
and that's 255, and then that will come over here.|и это 255, а потом это придет сюда.
It will be x.x.x.255, and then whatever's in between, which is one through 254.|Это будет x.x.x.255, а затем все, что находится между ними, от 1 до 254.
Pretty simple.|Довольно просто.
That's a pretty simple, it doesn't matter if it's a class A, B or C.|Это довольно просто, неважно, класс это A, B или C.
And let me clarify something right now cuz apparently,|И позвольте мне кое-что уточнить прямо сейчас, очевидно,
there's some rogue professor, instructor,|там какой-то мошенник профессор, инструктор,
teacher, whatever you want to call it,|учитель, как бы вы это ни называли,
that's telling people that the subnet mask determines the class of address.|это говорит людям, что маска подсети определяет класс адреса.
No, it does not.|Нет.
If you have a class A address, and I'll put it down here,|Если у вас есть адрес класса A, и я запишу его здесь,
just to show you an example, let me make a little bit more room,|просто чтобы показать вам пример, позвольте мне освободить немного больше места,
put it in the middle where you guys can see that.|поместите его посередине, чтобы вы, ребята, это могли видеть.
If you have 10.1.1 zero, a network, and you have slash 24 what?|Если у вас 10.1.1 ноль, сеть, а у вас слэш 24 какой?
That 24 mask all of a sudden, that 255,|Эта 24 маска внезапно, эта 255,
255, 255 dot zero magically turned that ten into a class a range.|255, 255 нулевых точек волшебным образом превратили эту десятку в диапазон класса А.
No, that's why we learned to classify IP addresses by looking at the first octet and seeing the range that it falls in.|Нет, поэтому мы научились классифицировать IP-адреса, глядя на первый октет и видя диапазон, в который он попадает.
What you're looking at is a subnetted class A address, and then you are allowed to have more networks, all right, and we'll talk about class full boundaries and|То, что вы видите, - это адрес класса A с подсетями, и тогда вам разрешено иметь больше сетей, хорошо, и мы поговорим о полных границах класса и
all that good stuff, especially when we get into the routing protocols.|все это хорошее, особенно когда мы переходим к протоколам маршрутизации.
But please, keep that in mind.|Но, пожалуйста, имейте это в виду.
The mask has nothing to do with the class of address.|Маска не имеет ничего общего с классом адреса.
That we have default mask for each class is one thing, but you can take a class A and subnet it, you know, with a 24 or a 28 or 20 or whatever you want,|То, что у нас есть маска по умолчанию для каждого класса, - это одно, но вы можете взять класс A и подсеть его, вы знаете, с 24, 28 или 20 или как хотите,
completely up to you, that mask is not gonna change the classification of that particular IP address.|полностью зависит от вас, эта маска не изменит классификацию этого конкретного IP-адреса.
All right?|Отлично?
We classify the IP address so we know,|Мы классифицируем IP-адрес, чтобы знать,
hey, this IP address can hold 16 million.|эй, этот IP-адрес может содержать 16 миллионов.
This IP address, or this class of address can hold 16 million.|Этот IP-адрес или этот класс адресов может содержать 16 миллионов.
This class of address can hold thousands,|Этот класс адресов может содержать тысячи,
and this class can only hold hundreds, so depending on the infrastructure that you're setting up,|и этот класс может содержать только сотни, поэтому в зависимости от инфраструктуры, которую вы настраиваете,
you decide accordingly what class of address you want to use.|вы соответственно решаете, какой класс адреса вы хотите использовать.
That's what that's there for, but the subnet mask is so you can do something that I just did, just like here, no numbers, right?|Это то, для чего это там, но маска подсети предназначена для того, чтобы вы могли делать то, что я только что сделал, прямо как здесь, без цифр, верно?
I know that a slider 24, slash 24 means,|Я знаю, что слайдер 24, косая черта 24 означает,
hey, my line,|эй, моя линия,
this magical line, is right here that's it, and you saw how quick I did that.|вот эта волшебная линия, вот она, и вы видели, как быстро я это сделал.
You saw how quick I did that.|Вы видели, как быстро я это сделал.
It is that simple.|Это так просто.
Well, the problem begins that not only is it working,|Что ж, проблема начинается с того, что он не только работает,
not working the last octet, cuz that's simple enough, but when you're working in the third octet, and then if they give you|не работает последний октет, потому что это достаточно просто, но когда вы работаете в третьем октете, а затем, если они дают вам
a mask like this, 255.255.240,|такая маска, 255.255.240,
cuz a lot of people like, oh, well, how many bits run?|Потому что многим людям нравится, ну, сколько битов работает?
I, I know if they would've given me a sider 20,|Я, я знаю, дали бы мне сидера 20,
I knew how to count 20 bits over.|Я умел считать на 20 бит больше.
But guess what, they didn't give you a side of 20, they gave you a 240.|Но знаете что, они не дали вам сторону 20, они дали вам 240.
What does that mean?|Что это значит?
That means x.x.x, whoops, sorry, one, two,|Это означает x.x.x, упс, извините, один, два,
three,|три,
four, line, one, two, three four, dot one,|четыре, линия, один, два, три четыре, точка один,
two, three four, one, two, three, four.|два, три, четыре, один, два, три, четыре.
Now how did I know four bits?|Как я узнал четыре бита?
We know that we have bit values, ladies and gentlemen, bit values that go on top,|Мы знаем, что у нас есть битовые значения, дамы и господа, битовые значения, которые идут сверху,
on top, 128.|сверху, 128.
Let me bring this down a little bit more.|Позвольте мне еще немного об этом рассказать.
Sorry.|Сожалею.
Put that there, oops, there, there we go.|Положи это туда, ой, вот так.
Now obviously, this is not going to line up perfectly,|Очевидно, это не будет идеально совпадать,
[SOUND] but those are your bit values.|[ЗВУК] но это ваши битовые значения.
All right?|Отлично?
If you add these first four bit values right there,|Если вы добавите эти первые четыре битовых значения прямо здесь,
which are these four bit values, that's going to come out to 240.|которые представляют собой эти четырехбитные значения, получается 240.
You need to know.|Ты должен знать.
You need to know my, this little, not mine, this is not mine.|Тебе нужно знать мое, это маленькое, не мое, это не мое.
But this little table, this little bit to decimal table right here.|Но вот эта маленькая таблица, вот эта маленькая десятичная таблица.
One bit on, 128.|Один бит включен, 128.
Consecutive bits, all right?|Последовательные биты, хорошо?
One bit on, 128, two bits on, 192, three bits on, 224, four bits on, 240.|Один бит включен, 128, два бита включены, 192, три бита включены, 224, четыре бита включены, 240.
You need to know that.|Вы должны это знать.
So you, so you know whatever.|Итак, вы, так что вы все знаете.
They give you a sa, slash 20, where it's easy, just count 20 bits, right?|Они дают вам са, косую черту 20, где это легко, просто посчитайте 20 бит, верно?
That's what the number is for.|Вот для чего нужен номер.
Or they give you a 240, you know exactly where you need to be.|Или они дают вам 240, вы точно знаете, где вам нужно быть.
Cuz once you draw that line, It's over.|Потому что, как только вы проведете эту линию, все кончено.
It's over.|Все окончено.
You've already got the answers to whatever you need.|У вас уже есть ответы на все, что вам нужно.
You know that if your line is right here,|Вы знаете, что если ваша линия прямо здесь,
hey, your increment is sixteen.|эй, твоя прибавка шестнадцать.
It's incrementing on the third octet, but you're incrementing by sixteen.|Он увеличивается на третьем октете, но вы увеличиваете на шестнадцать.
You know your wildcard mask, well, if you add these it's well,|Вы знаете свою маску подстановки, ну, если вы добавите их, это хорошо,
really one less increment, that's fifteen,|действительно на один шаг меньше, это пятнадцать,
this is 255, so it's,|это 255, так что это,
your wildcard mask is 0.0.15.255.|ваша маска подстановки - 0.0.15.255.
No physics.|Никакой физики.
How many holes do we have?|Сколько у нас дырок?
Two, four, eight, 16, 32, 64, 128, 256,|Два, четыре, восемь, 16, 32, 64, 128, 256,
512, 1024, 2048, 4906 minus two 40, 4094.|512, 1024, 2048, 4906 минус два 40, 4094.
How many holes?|Сколько дырок?
I mean subnets, sorry.|Я имею ввиду подсети, извините.
2, 4, 8, 16.|2, 4, 8, 16.
If I'm using the 0 network it's 16.|Если я использую сеть 0, это 16.
If I'm not using the 0 network I take away 2, 14.|Если я не использую сеть 0, я убираю 2, 14.
That line gives you everything, so knowing how to convert from a dotted decimal notation, all right?|Эта строка дает вам все, так что вы знаете, как преобразовать десятичную систему с разделительными точками, хорошо?
To know exactly where that line is at, you need to know that table.|Чтобы точно знать, где находится эта линия, вам нужно знать эту таблицу.
You need to know that table.|Вам нужно знать эту таблицу.
Now people tell me, hey Laz, there's just way too many things to remember.|Теперь люди говорят мне: «Эй, Лаз, мне нужно запомнить слишком много вещей».
This table, that line, if you add this number,|Эта таблица, эта строка, если вы добавите это число,
then you count by two at the bottom and you count by one.|затем вы считаете на два внизу и считаете на один.
I ask you this question, ladies and gentlemen.|Я задаю вам этот вопрос, дамы и господа.
Did we not have to learn all these different,|Разве нам не пришлось учиться всему этому разному,
memorize all these different things as far as, time table, how to divide, you know,|запомнить все эти разные вещи, например, расписание, как делить, знаете,
some of us that took physics, we're not even using numbers for God sakes.|некоторые из нас, которые занимались физикой, ради бога, мы даже не используем числа.
They're symbols, all right, and we figure out all these different things.|Это символы, и мы понимаем все эти разные вещи.
So there's certain things that you need to memorize.|Итак, есть определенные вещи, которые вам нужно запомнить.
There's certain things that you need to know.|Есть определенные вещи, которые вам нужно знать.
That's just the way it is.|Просто так оно и есть.
Especially in IT, that hey, this works like this, and that's it.|Особенно в IT, вот так работает, вот и все.
And this is the con, syntax for this, and that's it.|И это минус, синтаксис для этого, и все.
Those of you that went, that, learned JavaScript, or HTML, or Flash,|Те из вас, кто учился, изучили JavaScript, HTML или Flash,
or any kind of programming language, you had to understand the syntax and the columns, and the apostrophes, and the brackets,|или любой другой язык программирования, вам нужно было понимать синтаксис, столбцы, апострофы и скобки,
and you gotta point to this one and then point to the back, you know, all these,|и вы должны указать на это, а затем указать на спину, вы знаете, все эти,
memorization, memorization and repetition breeds retention.|запоминание, запоминание и повторение порождают запоминание.
The more you do something, the more it becomes second nature to you.|Чем больше вы что-то делаете, тем больше это становится для вас второй натурой.
Okay?|Ладно?
So with this, you need to practice every single day.|Итак, вам нужно практиковаться каждый божий день.
You need to understand what the subnet mask is.|Вам нужно понять, что такое маска подсети.
That is the key to everything.|Это ключ ко всему.
Cuz the subnet mask in IPv4, there is no subnet mask in IPv6.|Потому что маска подсети в IPv4, в IPv6 нет маски подсети.
Just to tell you that right now.|Просто чтобы сказать вам это прямо сейчас.
There is no subnet mask in IPv6.|В IPv6 нет маски подсети.
There is a subnet mask, in IPv4.|В IPv4 есть маска подсети.
You need to understand that part, that subnet mask is the key,|Вы должны понимать эту часть, что маска подсети является ключом,
it tells you what network you're in, and how many holes exist on that network.|он сообщает вам, в какой сети вы находитесь и сколько в ней дыр.
So, that's the key.|Итак, это ключ.
Because if I tell you, hey, my IP is 172|Потому что, если я скажу вам, эй, мой IP 172
16 10.33, okay, so what?|16 10.33, ну и что?
Well, what network am I in?|Ну а в какой я сети?
Well, what's your masks?|Ну какие у тебя маски?
Well, you tell me.|Ну ты мне скажи.
Well, how am I gonna tell you?|Ну как я тебе скажу?
Okay, sa, slash 16.|Хорошо, са, слэш 16.
You're in a default class B.|Вы находитесь в классе по умолчанию B.
I don't know.|Я не знаю.
The IP address by itself is nothing.|Сам по себе IP-адрес ничего не значит.
It's just a number.|Это просто число.
It is the subnet mask that actually tells you what part is the host and what part is the network, so this right here, ladies|Это маска подсети, которая на самом деле сообщает вам, какая часть является хостом, а какая - сетью, так что вот здесь, дамы
and gentlemen, is the key to everything,|и господа, это ключ ко всему,
and you can see where this bit right here,|и вы можете увидеть, где этот бит прямо здесь,
this last bit right there,|этот последний бит прямо здесь,
is this guy right here, the 16.|это парень прямо здесь, 16.
That you're incrementing by 16, so your network's incrementing by 16.|То, что вы увеличиваете на 16, значит, ваша сеть увеличивается на 16.
And guess what?|И угадайте, что?
In the test, if you are asked an IP addressing question straight out like that, CISCO loves to use the incrementation of 16.|В тесте, если вам прямо задают вопрос об IP-адресации, CISCO любит использовать увеличение на 16.
Why?|Зачем?
Because it's the hardest one, and it's the easiest one to make a math mistake.|Потому что это самый сложный и самый простой способ ошибиться в математике.
So what did Laz do when he was going through school?|Так что же делал Лаз, когда учился в школе?
I made it a point, not even to add any more, I added at first, but then I said,|Я сделал это, даже не добавляя больше, сначала добавил, но потом сказал:
you know what, I'm gonna memorize the heck out of this one.|знаете что, я собираюсь выучить чертовски из этого.
Where it's oh, it's incrementing by 16?|Где это ах, увеличивается на 16?
No problem, zero, 16, 32, 48, 64, 80, 96,|Нет проблем, ноль, 16, 32, 48, 64, 80, 96,
112, 128.|112, 128.
144, 160, 176, 192, 208 and then, 16 more, is 224, and then 240.|144, 160, 176, 192, 208, а затем еще 16, это 224, а затем 240.
So I remembered all those.|Так что я все это вспомнил.
So if I were to take a test right now,|Итак, если бы я сдал тест прямо сейчас,
that was just pure.|это было просто чисто.
Let's say that back in the, back in the days,|Скажем так, в те времена,
the year 2000, right, that there was an actual exam called TCPIP, and the majority of the exam was subnetting,|2000 год, верно, был настоящий экзамен под названием TCPIP, и большая часть экзамена была разбита на подсети,
so,|так,
I would literally write everything down before I actually took the test.|Я буквально все записывал перед тем, как сдавать экзамен.
Okay?|Ладно?
That way you underst, that way you don't have to make a math mistake.|Так вы поймете, и вам не придется делать математические ошибки.
Because if you're like me, and I am the worst, I think, test taker in the world.|Потому что, если ты такой же, как я, и я считаю себя худшим экзаменуемым в мире.
I mean, I don't know, because I haven't been around the world, but I'm pretty bad.|То есть, я не знаю, потому что я не был по всему миру, но я очень плохой.
I get the shakes, I go pale, I've told you this story before.|Меня трясет, я бледнею, я уже рассказывала вам эту историю раньше.
And, so, I make sure that when I go take a certification exam that will some sort of IP questions, I write out the incrementation of 16.|Итак, я удостоверяюсь, что, когда я иду на сертификационный экзамен, который будет содержать какие-то вопросы по IP, я выписываю увеличение на 16.
Because once you write out that incrementation,|Потому что, как только вы напишете это приращение,
it doesn't matter if your in the third,|неважно, если ты в третьем,
fourth, third,|четвертый, третий,
second, first, you already know that incrementation.|во-вторых, во-первых, вы уже знаете это приращение.
Just be careful so you know which octet you're in.|Просто будьте осторожны, чтобы знать, в каком октете вы находитесь.
So again, like here, this, this one right here,|Итак, снова, как здесь, это, вот здесь,
the two five five two five five two two four, I know two two four's three bits, so if it's three bits I'm incrementing in by|два, пять, пять, два, пять, пять, два, два, четыре, я знаю два, два, четыре, три бита, поэтому, если это три бита, я увеличиваю их на
32.|32.
There it is right here three bits, there's my 32, I already know that.|Вот тут вот три бита, вот и мои 32, я это уже знаю.
Yeah, but Laz you been teaching this for 200 years.|Да, но, Лаз, ты учишь этому 200 лет.
You're right, but that's what, how I want you to get.|Ты прав, но это то, что я хочу, чтобы ты получил.
I want you to get to the point where you know, you,|Я хочу, чтобы вы дошли до того момента, когда вы знаете, что
how you see in those movies where the guys take apart weapons and all these things blindfolded, they drive blindfolded and all this stuff.|как вы видите в тех фильмах, где ребята разбирают оружие и все это с завязанными глазами, водят с завязанными глазами и все такое.
Well instead of you know, doing that,|Что ж, вместо того, чтобы делать это,
blindfolded, you should be able to know oh, I know the IP address that you're using and the subnet map.|с завязанными глазами вы должны знать, о, я знаю IP-адрес, который вы используете, и карту подсети.
You should be able to figure it out like this.|Вы должны понять это вот так.
There's no need to have six board coming up and down doing all this crazy formulas to figure out, you know, what network you're in or|Нет необходимости иметь шесть плат, которые поднимаются и опускаются, выполняя все эти сумасшедшие формулы, чтобы выяснить, знаете ли, в какой сети вы находитесь или
how many holes you have or, I've seen,|сколько у тебя дыр или, я видел,
[LAUGH] I've seen people do some crazy stuff with Excel to figure out I mean, I was like, my God.|[СМЕХ] Я видел, как люди делали сумасшедшие вещи с Excel, чтобы понять, что я имею в виду, я подумал, боже мой.
What is this?|Что это?
This is more confusing than anything else.|Это сбивает с толку больше, чем что-либо другое.
This is all it is.|Это все, что есть.
This subnet mask, that's it.|Эта маска подсети, вот и все.
I mean, here, let me, let me write it out for you.|Я имею в виду, вот, позвольте мне, позвольте мне написать это для вас.
It's X eight bytes on, X eight bits on,|Это X восемь байт, X восемь бит,
224, one, two, three, line one,|224, один, два, три, первая строка,
two, three, four, five, one, two, three,|два, три, четыре, пять, один, два, три,
four, five, one, two, three.|четыре, пять, один, два, три.
I increment by 32, so X X 32 0, X X 64 0,|Я увеличиваю на 32, поэтому X X 32 0, X X 64 0,
X X 96 0, those are your networks.|X X 96 0, это ваши сети.
That's it, and then you add accordingly,|Вот и все, и затем вы соответственно добавляете
if that's a 32, guess what these add up to?|если это 32, угадайте, что они в сумме?
One less is 31, third octet.|На единицу меньше 31, третий октет.
So you add that 31 to 32, that's 63.|Итак, вы добавляете 31 к 32, получается 63.
Right, so let's, let's, let's just write out the first one, and I know I'm not supposed to be subnetting in this particular lecture, but|Хорошо, давайте, давайте, давайте просто выпишем первую, и я знаю, что я не должен разбивать подсети в этой конкретной лекции, но
just to show you how simple this is once I got the line.|просто чтобы показать вам, насколько это просто, как только я получу строку.
Yes, I'm excited.|Да, я взволнован.
That's why I wrote a book on it.|Вот почему я написал об этом книгу.
Right?|Правильно?
And it's going extremely well in Amazon.|И это очень хорошо на Amazon.
And a lot of people are getting into it,|И многие люди попадают в это,
okay, because it gives them a very straightforward, simple explanation on all about IPs because it is straightforward.|хорошо, потому что он дает им очень прямое, простое объяснение всего об IP, потому что это просто.
So, here x.x, right?|Итак, здесь x.x, верно?
What's the incrementation?|Что за приращение?
32.|32.
So let's start with 32,|Итак, начнем с 32,
let's say dot zero.|скажем точка ноль.
That's your network ID.|Это ваш сетевой идентификатор.
So what do you do?|Ну так что ты делаешь?
You get this right here, you add those bit values that are on.|Вы получаете это прямо здесь, вы добавляете те битовые значения, которые включены.
Well, you add the bit values, which are these right here.|Ну, вы добавляете битовые значения, которые находятся прямо здесь.
Guess what that adds up to?|Угадайте, к чему это сводится?
One less 32.|На один меньше 32.
So you add that 31, which is in the third octet,|Итак, вы добавляете 31, который находится в третьем октете,
to that 32 on the third octet, gives you what?|к тому 32 на третьем октете, что дает?
X.x.x, oops, 63.|X.x.x, ой, 63.
And then the last one which was all zeroes, right,|А потом последний, в котором все были нули, верно,
you take all those bit values and you add them up.|вы берете все эти битовые значения и складываете их.
What does that come up to?|К чему это приходит?
25!|25!
There you go!|Вот так!
You got your network ID, and you got your broadcast address.|У вас есть идентификатор сети и широковещательный адрес.
So what's in-between?|Так что между ними?
So what's after 32.0?|Так что после 32.0?
32.1.|32.1.
What's before 63 255?|Что до 63 255?
63.254.|63,254.
Now, when we get to subnetting,|Теперь, когда мы переходим к разделению на подсети,
I'll get a little bit deeper because a lot of people say, well, 62.|Я пойду немного глубже, потому что многие люди говорят: ну, 62.
No, no.|Нет нет.
Always remember.|Всегда помни.
Always remember in the last octet.|Всегда помните в последнем октете.
In the last octet, is, you,|В последнем октете вы,
this has gotta go all the way down to zero before you can change this to 62.|это должно быть полностью уменьшено до нуля, прежде чем вы сможете изменить это на 62.
Remember that little analogy with the turning in the leaves,|Вспомните эту небольшую аналогию с переворачиванием листьев,
you gotta roll back the miles?|ты должен отбросить мили?
Same thing.|То же самое.
Okay?|Ладно?
Same thing.|То же самое.
This has gotta go all the way back to zero before this turns to 62.|Это должно полностью вернуться к нулю, прежде чем оно превратится в 62.
All right?|Отлично?
Look at this, this is easy.|Посмотри на это, это легко.
I didn't even give you any numbers, any class, or anything.|Я даже не дал вам ни номеров, ни класса, ни чего-то еще.
I just gave you a mask, and I came up with networks.|Я только что дал тебе маску и придумал сети.
Because I knew where to draw a line, and the bit values tell you everything, okay?|Потому что я знал, где провести линию, а битовые значения говорят вам все, хорошо?
So definitely your subnet mask is the key,|Так что определенно ваша маска подсети является ключом,
and I'm telling you right now, [SOUND] you need to memorize that table.|и я говорю вам прямо сейчас, [ЗВУК] вам нужно запомнить эту таблицу.
You need to memorize the bit table.|Вам необходимо запомнить битовую таблицу.
If you already know it, great.|Если вы это уже знаете, отлично.
Awesome.|Потрясающие.
All right.|Отлично.
Awesome.|Потрясающие.
If you know this, life will be easy on you when you go out there and start doing IP questions.|Если вы это знаете, жизнь будет легкой для вас, когда вы выйдете и начнете задавать вопросы по интеллектуальной собственности.
But again, the subnet mask is the most important part of an IP version 4 address cuz that is the key to everything.|Но опять же, маска подсети - самая важная часть адреса IP версии 4, потому что это ключ ко всему.
That is the one that is gonna tell you what's what,|Это тот, который расскажет вам, что к чему,
where that dividing line is at.|где эта разделительная линия.
All right?|Отлично?
All right, I'll see you in the next lecture, so be ready.|Хорошо, увидимся на следующей лекции, так что будь готов.
[BLANK_AUDIO]|[BLANK_AUDIO]