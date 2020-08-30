D:\mailCloud\prjother\tmp\1\c44_Diagram used to subnet & Using the diagram...PLEASE NOTE_ 2046 should be 2048.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
All right.|Отлично.
Here it is.|Вот.
Here's a diagram.|Вот диаграмма.
We're gonna break it down.|Мы сломаем это.
We're gonna break down the subnetting diagram, and we're gonna show you how to use it, okay?|Мы разберем диаграмму подсетей и покажем вам, как ее использовать, хорошо?
You know, more or less you looked at it,|Вы знаете, более-менее вы смотрели на это,
when I saw it,|когда я это увидел,
when I was doing the subnetting mask in the previous lecture.|когда я делал маску подсети на предыдущей лекции.
Now basically, as you can see, you have your bit values: 128,|Как видите, у вас есть битовые значения: 128,
64, 32, 16, 8, 4, 2, 1.|64, 32, 16, 8, 4, 2, 1.
Then this big black dot is a decimal, then 128, 64, 32, 16, 8, 4, 2, 1, okay?|Тогда эта большая черная точка является десятичной дробью, затем 128, 64, 32, 16, 8, 4, 2, 1, хорошо?
So if you have, let's say, the line is right there, so how many bits do you have on?|Итак, если у вас есть, скажем, линия прямо там, так сколько бит у вас есть?
Well eight, everything to the left of that line, those bit values are on,|Ну восемь, все слева от этой строки, эти битовые значения включены,
all right, so you have 8 and 8, right?|хорошо, так у вас 8 и 8, верно?
Then you have, okay, all right,|Тогда у тебя, ладно, ладно,
you have these eight, there are, okay, let me use the mouse.|у тебя есть эти восемь, есть, ладно, дай мне мышку.
I gotta mouse right here.|Мне нужна мышь прямо здесь.
Technology, technology.|Технологии, технологии.
[BLANK_AUDIO]|[BLANK_AUDIO]
Okay?|Ладно?
So you have all these eight, that are all right here.|Итак, у вас есть все эти восемь, и все в порядке.
And you have these three, that are all right here.|И у вас есть эти три, и все в порядке.
And this is where the line is.|И вот где линия.
So if you were to add this, the math would be what?|Итак, если бы вы добавили это, математика была бы какой?
255, 255, 255, 224 remember the bits a decimal three bits on on the last octet so that means that your focus,|255, 255, 255, 224 запоминают десятичные три бита в последнем октете, так что это означает, что ваш фокус,
you're focusing on the last octet altogether.|вы полностью фокусируетесь на последнем октете.
This is where your focus is at, on the fourth octet.|Здесь ваше внимание сосредоточено на четвертом октете.
So the line of separating this red line that you see right here, that's separating the network side, the subnet, from the|Итак, линия, разделяющая эту красную линию, которую вы видите прямо здесь, отделяет часть сети, подсеть, от
host side, okay?|сторона хозяина, хорошо?
This right here tells you, I put up here,|Это прямо здесь говорит вам, что я остановился здесь,
the bit value to the left of the line will always be your network increment.|значение бита слева от строки всегда будет приращением вашей сети.
So your network is incremented by 32.|Итак, ваша сеть увеличена на 32.
The sum of these bit values, well, that's wrong right there.|Сумма этих битовых значений, ну вот тут не так.
It's not 15, it's 32, I mean it's 31,|Это не 15, это 32, то есть 31,
sorry.|Прости.
The sum of the bit, and di, I did it again down here.|Сумма бит и ди, я сделал это снова здесь.
What's wrong with me?|Что со мной не так?
I'll fix it later.|Я исправлю позже.
Yeah, 31 here, because if you are to add all these, if you got to add 1,|Да, здесь 31, потому что если вы добавите все это, если вам нужно добавить 1,
2, 4 and 8, and 16, it comes out to 31 if you wanted to add,|2, 4 и 8 и 16, получается 31, если вы хотите добавить,
but it just do one less 32, that gives you a 31.|но он просто делает на один меньше 32, что дает вам 31.
All right, so you said, some of the bit values to the right of the line will give you the number of calculated the numbers|Хорошо, как вы сказали, некоторые значения битов справа от строки дадут вам количество вычисленных чисел
to calculate for broadcast.|рассчитать для трансляции.
So this number right here is what we call or what I call, the broadcast calculation number.|Итак, вот этот номер - это то, что мы называем, или то, что я называю, номер расчета трансляции.
It'll help you calculate for broadcast addresses.|Это поможет вам рассчитать широковещательные адреса.
And this would be your network increment and how many subnets can you have?|И это было бы приращением вашей сети и сколько подсетей у вас может быть?
Now this is where you say, well less, why you,|Вот где вы говорите, ну меньше, почему вы,
if your length is our focus is the fourth octet, right,|если ваша длина в центре нашего внимания, это четвертый октет, верно,
which is over here, why are you counting for subnets all the way up here?|что здесь, почему вы рассчитываете для подсетей полностью здесь?
Because this is a class B address.|Потому что это адрес класса B.
And the default mask for a class B is right here.|И маска по умолчанию для класса B прямо здесь.
Let me copy, paste this real quick.|Позвольте мне скопировать, вставить это очень быстро.
[BLANK_AUDIO]|[BLANK_AUDIO]
The default mask for class, the address is right there.|Маска по умолчанию для класса, адрес прямо там.
So I have to start counting for some that's there.|Так что я должен начать подсчитывать некоторые из них.
If it would have been a class C address,|Если бы это был адрес класса C,
then I would have started counting subnets from right here.|тогда я бы начал считать подсети отсюда.
It would have been two, four, eight.|Было бы два, четыре, восемь.
Now since this is a class B, I'll have more networks that are available to me.|Теперь, поскольку это класс B, у меня будет больше доступных сетей.
Keep that in mind.|Запомни.
There's a website that I think all of you should check out,|Есть веб-сайт, который, я думаю, всем вам стоит посетить,
which is called subnettingquestions.com.|который называется subnettingquestions.com.
Again, it's called subnettingquestions.com, and you're gonna get, it's not really on they give you explanations.|Опять же, это называется subnettingquestions.com, и вы поймете, что на самом деле это не так, они дают вам объяснения.
They just give you problems, problems and problems and problems.|Они просто создают вам проблемы, проблемы, проблемы и проблемы.
And they always use,|И они всегда используют,
which I'll explain, the zero network and they, they always use it.|что я объясню, нулевая сеть и они, они всегда ее используют.
And they'll give you questions with a class B address like this right here,|И они зададут вам вопросы с таким адресом класса B прямо здесь,
like this one right here.|как этот прямо здесь.
Where's my mouse?|Где моя мышь?
Like this one here, okay, where they ask how many subnets you have.|Как вот здесь, ладно, где спрашивают, сколько у вас подсетей.
And then since you're in the fourth octet,|А поскольку вы находитесь в четвертом октете,
you say,|ты говоришь,
well I'm just gonna count from right here.|ну, я просто отсюда буду считать.
Well, no.|Ну нет.
Because if you have a class B, you can count from all the way from the default,|Потому что если у вас есть класс B, вы можете отсчитывать от значения по умолчанию,
or what's called the classful boundary of the address,|или то, что называется классовой границей адреса,
the classful boundary of the address.|классовая граница адреса.
So you do have 2,046 subnets.|Итак, у вас есть 2046 подсетей.
Now how did I come up with that?|Как я это придумал?
I know there's a formula.|Я знаю, что есть формула.
I know that you do 2 to the n minus, 2 and all that good stuff.|Я знаю, что вы делаете 2 из n минус, 2 и все такое хорошее.
I don't do that.|Я этого не делаю.
You know, just to make an analogy, a lot of us play dominoes, right?|Вы знаете, чтобы провести аналогию, многие из нас играют в домино, верно?
We we all play dominoes, and when the chi,|Мы все играем в домино, и когда ци,
when the, you're left with too many,|когда у тебя осталось слишком много,
you know, I guess chips,|знаете, я думаю, фишки,
if you cu, if you will you have count to see how many you've got.|Если хотите, посчитайте, сколько у вас есть.
If you've seen these old guys that play dominoes, when they flip their chips over like [SOUND] and they're already, they count that thing in like three seconds.|Если вы видели этих старых парней, которые играют в домино, когда они переворачивают свои фишки, как [ЗВУК], а они уже это делают, они считают это примерно за три секунды.
I'm like, Jesus, well this is the same thing.|Я такой, Господи, ну, это то же самое.
So what I do is I know I'm counting by two and doubling as I go.|Так что я знаю, что считаю по два и удваиваю по ходу.
So two, four, eight, sixteen, thirty-two,|Итак, два, четыре, восемь, шестнадцать, тридцать два,
you double,|ты удваиваешься,
256, 512, 1024, 2046.|256, 512, 1024, 2046.
Just double as you go until you get to the line.|Просто удваивайте, пока не дойдете до линии.
You know what, there's been people out there that I've heard and I think that's cool that these people have done that.|Знаете что, были люди, которых я слышал, и я думаю, что это здорово, что эти люди сделали это.
They've actually memorized what, to the 13|Они действительно запомнили, что до 13
is, to the 16,|есть, до 16,
to the fif, they've memorized it.|для пятерки они это запомнили.
And that's fine, there's nothing wrong with that.|И это нормально, в этом нет ничего плохого.
Whatever helps you, when you go take that test.|Все, что вам поможет, когда вы пойдете, пройдите этот тест.
The goal of this course is for you to pass your CCNA,|Цель этого курса - сдать CCNA,
not to be a math genius, okay?|не быть математическим гением, ладно?
The goal is to pass the CCNA, but IP version four, you don't need to be a math genius, as long as you know how to count by two, you'll be good to go, all right?|Цель состоит в том, чтобы пройти CCNA, но IP версии четыре, вам не нужно быть математическим гением, пока вы умеете считать на два, вам будет хорошо, хорошо?
Now you see I got, okay, so I got 2,046|Теперь вы видите, что у меня, ладно, у меня 2046
subnets, and then for host, I count the same way, 2, 4, 8, 16,|подсети, а затем для хоста я считаю так же, 2, 4, 8, 16,
32, minus 2.|32, минус 2.
On the host side, on the host side, you always,|На стороне хозяина, на стороне хозяина, вы всегда,
always, always, always subtract 2, why?|всегда, всегда, всегда вычитайте 2, почему?
Because of your network ID and your broadcast address.|Из-за вашего сетевого идентификатора и вашего широковещательного адреса.
Those are two addresses that are not based on the math,|Это два адреса, которые не основаны на математике,
depending on what they come out to be, but you also try to,|в зависимости от того, какими они будут, но вы также пытаетесь,
because you have a subnet ID and you have broadcast address.|потому что у вас есть идентификатор подсети и широковещательный адрес.
You can't use those, you lose those two and you can only assign whatever's in between,|Вы не можете их использовать, вы теряете эти два и можете назначать только то, что находится между ними,
whatever's in between.|все, что между ними.
Now, here, you see that I did not subtract.|Вы видите, что я не вычитал.
I can control my mouse here, it's a little crazy mouse.|Я могу управлять своей мышкой здесь, это маленькая сумасшедшая мышка.
All right, I did not subtract 2 here,|Хорошо, я здесь 2 не вычитал,
because I'm using the zero network.|потому что я использую нулевую сеть.
Now for my mouse done now cuz I wanna get serious here now.|Теперь что касается моей мыши, потому что я хочу серьезно подумать.
Now it's really getting crazy anyway.|Теперь все равно действительно сходит с ума.
What is the zero network?|Что такое нулевая сеть?
The zero network is the very first network that's zero and the very last network, which in this case,|Нулевая сеть - это самая первая сеть, которая нулевая, и самая последняя сеть, которая в данном случае
will be 224.|будет 224.
How do I know that?|Откуда я это знаю?
Because your subnet mask, 225, 225, 225,|Поскольку ваша маска подсети, 225, 225, 225,
224, that number, 224, or 240, or 248 or 252, that is your last network.|224, это число, 224 или 240, или 248 или 252, это ваша последняя сеть.
That will always be your last network.|Это всегда будет ваша последняя сеть.
So when you're using the zero network,|Итак, когда вы используете нулевую сеть,
when you're using, when you're using the zero network, you will use the zero and use our very last network.|когда вы используете, когда вы используете нулевую сеть, вы будете использовать нулевую и использовать нашу самую последнюю сеть.
So in this case that your incrementing by 32, you have 0, 32,|Итак, в этом случае при увеличении на 32 у вас есть 0, 32,
64, 96, 128, 160,|64, 96, 128, 160,
192, 224, okay?|192, 224, ладно?
Well, if you really you have more, really,|Что ж, если у тебя действительно есть больше, правда,
cuz I just came up to here,|Потому что я только что подошел сюда,
you keep going, going, going, going, you keep, you can have the possibility of that many networks, but then it starts jumping|вы продолжаете идти, идти, идти, идти, вы продолжаете, у вас может быть возможность такого количества сетей, но затем он начинает прыгать
into another.|в другой.
This will definitely jump into a it starts getting a little bit more and more and more, okay?|Это определенно приведет к тому, что он начнет становиться все больше и больше, хорошо?
But, you would have, you know, normally,|Но вы бы, знаете, обычно
the 224 since that's where the mask is.|224, так как там маска.
That's what your last network would be.|Вот какой будет ваша последняя сеть.
If don't use the zero network, if you do not use the zero network,|Если не использовать нулевую сеть, если вы не используете нулевую сеть,
then I would have subtracted 2 right here,|тогда я бы вычитал 2 прямо здесь,
and would've had 2044, 2044.|и было бы 2044, 2044.
That's not the case with today's technology.|Это не относится к сегодняшним технологиям.
In today's IOS's, on the routers, there's a command that's called ip subnet-zero, it's on by default.|В сегодняшних IOS на маршрутизаторах есть команда ip subnet-zero, она по умолчанию включена.
That allows the router to use,|Это позволяет маршрутизатору использовать,
to understand the zero network, so you don't have to be worried about that.|чтобы понять нулевую сеть, поэтому вам не нужно об этом беспокоиться.
If you type it over again [SOUND] it might be sometimes zero, that's,|Если вы наберете еще раз [ЗВУК], иногда он может быть нулевым, то есть
that's just fine, nothing's gonna happen,|это нормально, ничего не произойдет,
okay?|Ладно?
But now you are allowed to use the zero network.|Но теперь вам разрешено использовать нулевую сеть.
Why am I explaining this?|Почему я это объясняю?
Because in your test they're gonna mess with your mind.|Потому что в вашем тесте они запутаются в вашем уме.
They're gonna ask you, if using the zero network, and you have this mask with this network, what is the eighth subnet's last IP address?|Они спросят вас, если вы используете нулевую сеть и у вас есть эта маска с этой сетью, какой последний IP-адрес восьмой подсети?
They'll ask, so there's key things in there, there's key things.|Они спросят, так что там есть ключевые вещи, есть ключевые вещи.
Are you using the zero network?|Вы используете нулевую сеть?
Yes.|Да.
Using the zero network with this class of address,|Используя нулевую сеть с этим классом адресов,
using the eightth subnet, what is the last available IP address?|используя восьмую подсеть, какой последний доступный IP-адрес?
So now you gotta count, starting from zero,|Итак, теперь вам нужно считать, начиная с нуля,
let's say it's 32, right, 0, 32, 64, 96,|допустим, 32, верно, 0, 32, 64, 96,
128.|128.
I said it was 224, didn't I?|Я сказал, что это 224, не так ли?
Yeah, I did.|Да, я сделал.
224 was the last network.|224 была последней сетью.
So 224 and 31 is 255.|Итак, 224 и 31 равно 255.
254 will be last available IP address,|254 будет последним доступным IP-адресом,
if you're using the zero network.|если вы используете нулевую сеть.
If you're not using the zero network,|Если вы не используете нулевую сеть,
then that whole world changes, then the whole world changes, okay?|тогда весь мир меняется, потом меняется весь мир, хорошо?
So be very careful when you're looking at one of those questions, if they tell you use the zero network or do not use the|Поэтому будьте очень осторожны, когда вы смотрите на один из этих вопросов, если вам говорят, что вы используете нулевую сеть или не используете
zero network, okay?|нулевая сеть, ладно?
But anyway, so here's your dividing line,|Но в любом случае, вот ваша разделительная линия,
remember this is the, I put this line here because I just wanted you to understand why I started counting all the way from back here.|помните, это то, я поставил эту строчку здесь, потому что я просто хотел, чтобы вы поняли, почему я начал отсчет отсюда.
And I just started counting from here down, all right, because this is how many subnets you're able to have, be able to have more networks.|И я просто начал отсчет отсюда, хорошо, потому что именно столько подсетей вы можете иметь, иметь больше сетей.
You can have more networks, but again,|У вас может быть больше сетей, но опять же,
your focus is the last octet that's why I counted those eight networks.|вы фокусируетесь на последнем октете, поэтому я насчитал эти восемь сетей.
And then and the whole side you always,|А потом и всю сторону ты всегда,
always subtract 2.|всегда вычитайте 2.
And then once you add this, which I had it wrong earlier, I put 30, it's 31, it's 31.|А затем, как только вы добавите это, что я ошибся ранее, я поставил 30, это 31, это 31.
That's it and guess what.|Вот и угадайте что.
And again, I'm giving this away before time.|И снова я раздаю это раньше времени.
But we'll have, I'll show you two different ways of getting this.|Но у нас есть, я покажу вам два разных способа получить это.
There's a wildcard mask right there, 31.|Там есть подстановочная маска, 31.
It's 0, 0,|Это 0, 0,
0, 31.|0, 31.
There's your wildcard mask.|Вот ваша маска с подстановочными знаками.
And once we get to that lecture I wanna prove to you that both of the methods work exactly the same, all right?|И как только мы перейдем к той лекции, я хочу доказать вам, что оба метода работают одинаково, ясно?
So once you draw that line, look at all the answers you've got.|Итак, как только вы проведете эту черту, посмотрите на все ответы, которые у вас есть.
Look at all the answers you've got.|Посмотрите на все ответы, которые у вас есть.
You've got your bit value, this is the diagram.|У вас есть битовое значение, это диаграмма.
This is what you need to do.|Это то, что вам нужно сделать.
This is your first step.|Это ваш первый шаг.
Once you find that mask and you know that bit table, all right, so if they give you a 224, or 240, or 248,|Как только вы найдете эту маску и узнаете эту таблицу битов, хорошо, поэтому, если они дадут вам 224, 240 или 248,
you know how many bits you need to go in,|вы знаете, сколько бит вам нужно вложить,
and whatever octet, you know where to draw that line, so you can find that number.|и какой бы октет вы не знали, вы знаете, где провести эту линию, чтобы найти это число.
Once you find that number, it's over, it's over.|Как только вы найдете этот номер, все кончено, все кончено.
Cuz you use increment either on the four,|Потому что вы используете приращение либо на четырех,
to the third, it doesn't matter.|к третьему не имеет значения.
You already got the answers to whatever it is you need, to whatever it is you need.|У вас уже есть ответы на все, что вам нужно, на все, что вам нужно.
Now the bottom example it's let me use the mouse, let me use the touchpad,|В нижнем примере я могу использовать мышь, позвольте мне использовать тачпад,
this is a crazy mouse, see,|это сумасшедшая мышь, видите ли,
look, look at this, it's moving by itself.|Посмотри, посмотри на это, оно движется само по себе.
Stop.|Стоп.
[BLANK_AUDIO]|[BLANK_AUDIO]
Runaway mouse.|Сбежавшая мышь.
And again here same question as above,|И снова здесь тот же вопрос, что и выше,
different class of address.|другой класс адреса.
Okay, obviously, but again, this is still is 32, made a mistake on it, I mean 31.|Ладно, очевидно, но опять же, это все еще 32, ошиблись, то есть 31.
Why do I keep staying that?|Почему я так и остаюсь?
All right, it is 31, sorry about that.|Хорошо, ему 31 год, извините за это.
And you can see the amount of subnets.|И вы можете увидеть количество подсетей.
Different class, though.|Хотя другого класса.
Different class, it's a class C.|Другой класс, это класс С.
So therefore I started counting just on the, that's the only,|Поэтому я начал рассчитывать только на то, что единственное,
that's the only way I can go because the,|это единственный путь, по которому я могу пойти, потому что
the boundary line is right here between the third and the fourth octet, I can't go beyond that.|граница проходит прямо здесь между третьим и четвертым октетами, я не могу выйти за пределы этого.
I can't go beyond that.|Я не могу пойти дальше этого.
So, 248.|Итак, 248.
I'm using the zero network cuz I didn't subtract 2 there,|Я использую нулевую сеть, потому что я не вычитал там 2,
I'm using the zero network.|Я использую нулевую сеть.
So I have eight networks that increment by 32, with 30 hosts on each network.|Итак, у меня есть восемь сетей, которые увеличиваются на 32, по 30 хостов в каждой сети.
So, you can see the difference, all right,|Итак, вы видите разницу, хорошо,
when you're using the diagram.|когда вы используете диаграмму.
If you're using a class B address, we have a lot more networks.|Если вы используете адрес класса B, у нас намного больше сетей.
Where if you have a class C address, you only have so many networks,|Если у вас есть адрес класса C, у вас будет только определенное количество сетей,
because you cannot more the line beyond the classful boundary yet, because if you do move the line beyond the classful boundary, now you're doing|потому что вы еще не можете вывести линию за границу класса, потому что, если вы переместите линию за границу класса, теперь вы делаете
route summarization.|Обобщение маршрута.
Now we're getting into a whole new other little world all together there, okay?|Теперь мы все вместе попадаем в совершенно новый, другой маленький мир, хорошо?
We're now just doing what's called this is just,|Сейчас мы просто делаем то, что называется, это просто,
I'm just showing you really how to use this diagram.|Я просто показываю вам, как использовать эту диаграмму.
And this is what you need to do, the different aspects of the diagram,|И это то, что вам нужно сделать, различные аспекты диаграммы,
that network incrementation, the broadcast calculation number,|приращение сети, номер вычисления широковещания,
how you're counting for host, okay,|как ты рассчитываешь на хозяина, ладно,
which is, let me use the arrow keys and the Shift key here.|то есть позвольте мне использовать здесь клавиши со стрелками и клавишу Shift.
How you count for not host I'm sorry,|Как ты считаешь не хозяином извини,
subnets or [BLANK_AUDIO]|подсети или [BLANK_AUDIO]
How you count for host, and you subtract 2.|Как вы считаете хозяина, и вы вычитаете 2.
It's showing you all this stuff that all that's there.|Он показывает вам все, что там есть.
And again, this is your wildcard mask, 0,|И снова это ваша маска подстановки, 0,
0, 0, 31.|0, 0, 31.
So again, learn this diagram.|Итак, еще раз изучите эту диаграмму.
Learn this diagram, read the things on it,|Выучите эту схему, прочтите на ней,
all right?|отлично?
I'm gonna save it that way when I,|Я сохраню его таким образом, когда я,
when you get it, the right answers are on there, okay?|когда вы его получите, там будут правильные ответы, хорошо?
But again, if there's mistakes just send an email say hey Laz, thank you.|Но опять же, если есть ошибки, просто отправьте электронное письмо, скажите привет, Лаз, спасибо.
[SOUND] Okay, yeah, you're right, it's this, no big deal.|[ЗВУК] Ладно, да, ты прав, это все, ничего страшного.
But again, learn this diagram.|Но опять же, изучите эту диаграмму.
You learn this, and really it's just learning the bit values, drawing the line,|Вы узнаете это, и на самом деле это просто изучение битовых значений, рисование линии,
there's your increment, done.|вот и ваше приращение, готово.
That's how fast you gotta be, and the only reason I tell you that you need to learn this, and be quick about it,|Вот как быстро вы должны быть, и единственная причина, по которой я говорю вам, что вам нужно научиться этому и действовать быстро,
because once you take,|потому что как только вы возьмете,
because again, I strongly urge you to take the CCNA 200-120.|потому что я снова настоятельно рекомендую вам взять CCNA 200-120.
If for some reason you can't do it,|Если по какой-то причине не получается,
whatever the case may be, I understand.|в любом случае я понимаю.
The only reason I tell you that, is because it's gonna be,|Единственная причина, по которой я говорю вам это, это потому, что это будет
it's gonna be a lot better for you.|для тебя будет намного лучше.
It's one exam, you're a full-blown associate.|Это один экзамен, ты полноценный помощник.
I know they have the CSAT now that you can take, and you can go on to other you can go beyond the CCNA.|Я знаю, что теперь у них есть CSAT, который вы можете пройти, и вы можете перейти к другому, вы можете выйти за рамки CCNA.
You can go CCNA wireless, CCNA security and all that good stuff.|Вы можете использовать беспроводную связь CCNA, систему безопасности CCNA и все такое хорошее.
But again, get that CCNA and with this,|Но снова получите этот CCNA и с этим,
when you start answering questions based on, you know, subnetting or what have you, you need to be quick about it.|когда вы начинаете отвечать на вопросы на основе, вы знаете, подсетей или чего-то еще, вам нужно действовать быстро.
That's why I always say 30 seconds, 30|Вот почему я всегда говорю 30 секунд, 30
seconds, less than 30 seconds, quick,|секунд, менее 30 секунд, быстро,
less than that, okay?|меньше, ладно?
Because there's a lot, quite a lot more questions out there with switching and routing that you need to pay close attention to.|Потому что существует очень много вопросов о коммутации и маршрутизации, на которые вам нужно обратить пристальное внимание.
Of course, when you start get into spanning tree and all these VLANs and split horizon, and all this, you need to take your time.|Конечно, когда вы начинаете входить в связующее дерево, все эти VLAN, разделять горизонт и все это, вам нужно не торопиться.
Not to mention you got three simulations to do.|Не говоря уже о том, что вам нужно сделать три симуляции.
So you wanna give yourself some extra time, right?|Так ты хочешь дать себе немного больше времени, верно?
So it's my, it's I believe it's a minute and 30 seconds per question, and they got ten minutes for simulation.|Так что это мой вопрос, я думаю, это минута и 30 секунд на вопрос, а у них есть десять минут на симуляцию.
When it comes to questions on the OSI,|Что касается вопросов по OSI,
standards, cabling and and IP's, anything with IP's whether it be summarization, VLSM,|стандарты, кабели и IP, все, что связано с IP, будь то резюмирование, VLSM,
class, full class list, subnetting and subnetting, period, you should be able to answer that boom, boom, boom, because the|класс, полный список классов, подсети и подсети, точка, вы должны быть в состоянии ответить на этот бум, бум, бум, потому что
questions are not complex, they are not,|вопросы не сложные, это не так,
they are not, and it's the same concept,|их нет, и это та же концепция,
it's the same concept, okay?|это та же концепция, хорошо?
All right, so here's your diagram.|Хорошо, вот ваша диаграмма.
Learn the diagram, learn the anatomy of it and what each part does.|Изучите схему, узнайте ее анатомию и то, что делает каждая часть.
And that's what I'm trying to or, or tried to explain in the particular lecture, okay?|И это то, что я пытаюсь или пытаюсь объяснить в конкретной лекции, хорошо?
Last time, increment number, broadcast calculation number, counting for hosts,|Последний раз, номер приращения, номер вычисления широковещательной рассылки, подсчет хостов,
I mean counting for subnets, left to right, counting for hosts, right to left.|Я имею в виду подсчет подсетей слева направо, подсчет хостов справа налево.
And then your wildcard mask is right there.|И тогда ваша маска подстановки прямо здесь.
And your broadcast count number becomes your wildcard mask.|И ваш номер счетчика трансляций становится вашей маской подстановки.
See you in the next lecture.|Увидимся на следующей лекции.
[BLANK_AUDIO]|[BLANK_AUDIO]