D:\mailCloud\prjother\tmp\1\c45_Class-full subnetting.md  


__|__
--|--
Hello, everybody.|Привет всем.
Now that we've learned how to use that diagram,|Теперь, когда мы узнали, как использовать эту диаграмму,
all right and we're getting into the subnetting portion of it.|хорошо, и мы переходим к разделению на подсети.
All right, the subnet mask and all that.|Хорошо, маска подсети и все такое.
And we've seen a little bit of it already.|И мы уже видели немного этого.
We have some problems to figure out, okay?|Нам нужно решить некоторые проблемы, хорошо?
And get on this side,|И встань на эту сторону,
I really don't know which side to get on where you can see it, all right?|Я правда не знаю, с какой стороны перейти, где вы это увидите, хорошо?
All right, so here we have the first question.|Итак, у нас есть первый вопрос.
We'll do a couple of questions, not many,|Мы ответим на пару вопросов, не много,
just for you,|для тебя,
you to get the idea of what classful subnetting is, which is usually,|вы, чтобы получить представление о том, что такое классовое разбиение на подсети, что обычно,
classful subnetting means that you have the same number of hosts per network.|Классовое разбиение на подсети означает, что у вас одинаковое количество хостов в сети.
That's classful subnetting, all right,|Это классное разбиение на подсети, хорошо,
same number of hosts, same mask per network, okay?|такое же количество хостов, та же маска на сеть, хорошо?
So here says, what valid host range is the IP address,|Итак, здесь говорится, какой допустимый диапазон хостов является IP-адресом,
172.16.10.22, with that particular mask,|172.16.10.22, с этой конкретной маской,
255.255.255.240 a part of?|255.255.255.240 в составе?
Now, when I'm asked a question like this,|Теперь, когда мне задают такой вопрос,
how do you attack a question like this?|как ответить на такой вопрос?
Well, you look at the subnet mask, the key, right?|Ну вы посмотрите на маску подсети, ключ, да?
So, it's 240.|Итак, это 240.
So you get this 240.|Итак, у вас есть 240.
You say, okay, so I'm focused on the last octet.|Вы говорите, хорошо, поэтому я сосредоточился на последнем октете.
So let me draw my diagram.|Итак, позвольте мне нарисовать схему.
X.X, not Z what is that?|X.X, а не Z, что это?
X.X.X., one, two, three, four line, one,|X.X.X., один, два, три, четыре строки, один,
two, three, four.|два, три, четыре.
How did I know?|Как я узнал?
How did I know that it was going to be that right there,|Откуда я знал, что это будет именно здесь,
because 240 is four bits on, that's where the bits of decimal table helps you.|Поскольку 240 - это четыре бита, здесь вам помогут биты десятичной таблицы.
So, it's 240.|Итак, это 240.
I'm on the last octet.|Я на последнем октете.
This bit value right here, is 16, is 16.|Это битовое значение 16, 16.
All right, because one, two, eight one,|Хорошо, потому что раз, два, восемь один,
two, four, eight, 16.|два, четыре, восемь, 16.
That's our increment so our focus is that 22, so how many times do we need to increment by 16 to get to 22 in the last octet?|Это наше приращение, поэтому мы фокусируемся на 22, так сколько раз нам нужно увеличить на 16, чтобы добраться до 22 в последнем октете?
I know that it's only gonna be ones but let's see how you would do that so you would say, okay, X.X.X, nope 16, no,|Я знаю, что это будут только единицы, но давайте посмотрим, как вы это сделаете, чтобы вы сказали, хорошо, X.X.X, нет 16, нет,
it is the last octet, I'm sorry.|это последний октет, извините.
X, last octet, right?|X, последний октет, верно?
Yeah, 16, and then, okay, and if I increment again, is X.X.X.32.|Да, 16, а потом, хорошо, и если я снова увеличу, будет X.X.X.32.
Well, the number I'm looking for is 22,|Ну, номер, который я ищу, 22,
which is in the last octet.|который находится в последнем октете.
So I know it's not gonna be in the 32|Так что я знаю, что этого не будет в 32
network.|сеть.
It's gonna be in the 16 network and they're asking for the valid host range.|Он будет в сети 16, и они запрашивают допустимый диапазон хостов.
So what do I do?|Так что же мне делать?
I sum up these vid, these bits right there which is only one less the increment,|Я суммирую эти видео, эти биты прямо там, что всего на единицу меньше приращения,
than our increment, so it's 15.|чем наше приращение, поэтому оно равно 15.
That summation, that addition, 15 plus 16|Это суммирование, это добавление, 15 плюс 16
is 31.|31 год.
[BLANK_AUDIO]|[BLANK_AUDIO]
X.X.X.31, so what's in between 16 and 31?|X.X.X.31, а что между 16 и 31?
17 and 30, right?|17 и 30, верно?
After 16 we have 17.|После 16 у нас 17.
Before 31, we have 30.|До 31 года у нас 30.
There you go.|Вот так.
Even easier since I incremented twice,|Еще проще, так как я увеличил вдвое,
what's one less 32?|что на один меньше 32?
31.|31.
And it always works out that way.|И всегда так получается.
So there's many ways of doing it to make it quick, make it easy for you.|Так что есть много способов сделать это быстро, упростить для вас.
So you can do less work and get your answers that you need.|Так вы сможете меньше работать и получать нужные ответы.
But anyway, for this our first answer, the range is 17 to 30.|Но в любом случае для этого нашего первого ответа диапазон от 17 до 30.
So the answer would be 17 to 30.|Итак, ответ будет 17 к 30.
So the answer will be e.|Так что ответ будет e.
That is how you do that.|Вот как вы это делаете.
Again, what did I focus on?|Опять же, на чем я сосредоточился?
I focused on the mask.|Я сосредоточился на маске.
Cuz the mask told me where to draw that line.|Потому что маска сказала мне, где провести эту линию.
Sounds like a spirit I hear voices, right?|Похоже на дух, я слышу голоса, верно?
The [LAUGH] mask told me where to draw the line.|Маска [СМЕХ] подсказала мне, где провести черту.
So once I draw the line, I know what I increment by.|Итак, когда я рисую линию, я знаю, на что я увеличиваю.
So I increment till I get close to the number that I'm focusing on,|Поэтому я увеличиваю, пока не приблизлюсь к числу, на котором я сосредотачиваюсь,
which is in the fourth octet.|который находится в четвертом октете.
In this case it was 16, 22.|В данном случае это было 16, 22.
So obviously, I wasn't gonna go beyond 16.|Очевидно, я не собирался выходить за рамки 16.
I just did it so you can see a visualization.|Я просто сделал это, чтобы вы могли увидеть визуализацию.
So, 22 will not fall in the 32 network,|Значит, 22 не попадет в сеть 32,
okay?|Ладно?
So, that's the first problem.|Итак, это первая проблема.
That's the first problem.|Это первая проблема.
That's how we got the answer to get the range.|Вот как мы получили ответ, чтобы получить диапазон.
Let's go to the question number two.|Перейдем к вопросу номер два.
Question number two states what is the broadcast address of the subnet address,|Во втором вопросе указывается широковещательный адрес подсети.
172.16.8.9, I lost my notepad, all right,|172.16.8.9, потерял блокнот, ладно,
172.16.8.159.|172.16.8.159.
So that's an address, 159/26.|Это адрес 159/26.
Again, what am I focusing on?|Опять же, на чем я сосредоточен?
I don't care about anything else then,|Тогда меня больше ни о чем не волнует,
hey the first thing I need to do is draw that line.|эй, первое, что мне нужно сделать, это нарисовать эту линию.
Draw that line.|Проведите эту линию.
It's a 26, so there you go.|Это 26, так что поехали.
That was easy enough.|Это было достаточно просто.
26 bits on.|26 бит на.
Eight, eight, and eight is 24.|Восемь, восемь и восемь - 24.
25, 26 then one, one, two, three, four,|25, 26, затем один, один, два, три, четыре,
five, six.|пять шесть.
That's eight bits, right?|Это восемь бит, правда?
And what is the address?|А какой адрес?
What did it say, what is the broadcast address of 159, okay, so we increment by what?|Что там написано, каков широковещательный адрес 159, хорошо, так на что увеличиваем?
This number right here, we're incrementing by 64.|Это число прямо здесь, мы увеличиваем на 64.
So therefore,|Так что,
X.X.X, 64.|Х.Х.Х, 64.
X.X.X, 64 again.|X.X.X, снова 64.
That's 128.|Это 128.
And we increment again, X.X.X and 64.|И мы снова увеличиваем, X.X.X и 64.
That's 192.|Это 192.
So, 159 is less than 192.|Итак, 159 меньше 192.
So there's no way that 159 will fall in there.|Так что 159 ни за что не попадут туда.
Now, in our previous example,|Теперь в нашем предыдущем примере
I said that one less this network is this guy's broadcast.|Я сказал, что на одну сеть меньше, чем на трансляцию этого парня.
So, the broadcast here is X.X.X, 191.|Итак, трансляция здесь - X.X.X, 191.
But let's prove that.|Но давайте это докажем.
If we add these bit values which is 63,|Если мы сложим эти битовые значения, то есть 63,
because it's always one less the increment 63, 128, 191.|потому что оно всегда на единицу меньше приращения 63, 128, 191.
So the answer is, 191.|Итак, ответ - 191.
And that would be C.|И это будет C.
Again, the, pray, that these are the type of questions that you're gonna get asked when it comes to IP's.|Опять же, молитесь, чтобы это были вопросы, которые вам зададут, когда дело доходит до IP.
I'm gonna tell you, right off the bat,|Я скажу тебе сразу,
that they're not.|что это не так.
But let's do one more question, let's do one more question.|Но давайте зададим еще один вопрос, давайте еще один вопрос.
Just so you can get the hang of it, let's move this up a little bit.|Чтобы вы могли освоиться, давайте немного продвинемся.
I'm gonna use the tools of the trade.|Я собираюсь использовать инструменты торговли.
Let's go here, here we go.|Пойдем сюда, поехали.
Let's use this one, question number four.|Давайте воспользуемся этим, вопросом номер четыре.
Let's get the notepad, okay, up here.|Давайте возьмем блокнот, ладно, сюда.
Question number four.|Вопрос номер четыре.
That's the one we're gonna do, question number four, and let me erase all this all right,|Это то, что мы собираемся сделать, вопрос номер четыре, и позвольте мне стереть все это хорошо,
so now in question number four, they don't really give you any,|Итак, теперь в вопросе номер четыре, они действительно не дают вам ничего,
any numbers or masks, they're looking for masks.|любые числа или маски, они ищут маски.
But look at the question.|Но посмотрите на вопрос.
If you wanted to have 12 subnets with a class C,|Если вы хотите иметь 12 подсетей с классом C,
key, class C network ID, what subnet mask would you use?|ключ, идентификатор сети класса C, какую маску подсети вы бы использовали?
Okay, a class C network ID, right?|Хорошо, идентификатор сети класса C, верно?
That would mean X.X.X because class C classful boundary that means the first three octets, so what mask would you use for 12 subnets?|Это будет означать X.X.X, потому что классовая граница класса C означает первые три октета, так какую маску вы бы использовали для 12 подсетей?
Well we don't know, we know we have one,|Ну, мы не знаем, мы знаем, что у нас есть один,
two, three,|два три,
four, five, six, seven, eight bits to work with, and when you count for subnets, you're counting from left to right.|четыре, пять, шесть, семь, восемь бит для работы, и когда вы считаете для подсетей, вы считаете слева направо.
So, let's go ahead and count from left to right now.|Итак, давайте продолжим и посчитаем слева направо.
All right, let me get over here.|Хорошо, позволь мне пройти сюда.
And, I'll use the Shift, there you go.|Я воспользуюсь Shift, вот и все.
Two, four, eight, can't stop there, 16, so you have those four bits that aren't, so your line will be right there.|Два, четыре, восемь, нельзя останавливаться на достигнутом, 16, так что у вас есть те четыре бита, которых нет, так что ваша строка будет прямо там.
That means you turn on these four bits right here.|Это означает, что вы включаете эти четыре бита прямо здесь.
So that would be your mass.|Так что это будет твоя масса.
So what's four bits?|Так что четыре бита?
240.|240.
Again, this is why you need to know that bit to decimal table, you see?|Опять же, вот почему вам нужно знать этот бит в десятичной таблице, понимаете?
All right, so this is classful subnetting.|Хорошо, это классовое разбиение на подсети.
When they're asking you, think number of hosts, you can use the same math.|Когда вас спрашивают, подумайте о количестве хостов, вы можете использовать ту же математику.
This is what this deals with, in this line of questioning, all right, where they're gonna ask you things, they're not gonna|Это то, с чем это связано, в этой очереди вопросов, хорошо, когда они будут спрашивать вас о вещах, они не собираются
ask you things like this, but if they do, very straight forward questions, be happy about it.|спрашивать вас о таких вещах, но если они задают очень простые вопросы, будьте счастливы.
But again, what classful subnetting is,|Но опять же, что такое классовое разбиение на подсети,
which we don't use anymore, all right,|которые мы больше не используем, хорошо,
very few of us use, is having the same number of hosts or the same masks per network segment, which is not a reality anymore and|очень немногие из нас используют одинаковое количество хостов или одинаковые маски для каждого сегмента сети, что больше не является реальностью и
that is the reason that we ran out of IPv4|это причина того, что у нас закончился IPv4
addresses.|адреса.
Eventually we would have ran out anyway.|В конце концов, мы бы все равно выбежали.
We just ran out a lot quicker because we just gave away so many addresses, all right?|Просто мы закончили намного быстрее, потому что раздали так много адресов, понятно?
But classful subnetting is a thing of the past.|Но классовое разбиение на подсети осталось в прошлом.
Now we do what's called classless subnetting, and that's your next lecture.|Теперь мы займемся тем, что называется бесклассовым распределением подсетей, и это ваша следующая лекция.
I'll see you there.|Увидимся там.
[BLANK_AUDIO]|[BLANK_AUDIO]