D:\mailCloud\prjother\tmp\1\c51_Counting for subnets and finding increment value.md  


__|__
--|--
All right, our little diagram here that we were looking at before.|Хорошо, вот наша маленькая диаграмма, на которую мы смотрели раньше.
Let's see if I can, well,|Посмотрим, смогу ли я, ну
that's as far as it goes.|это все, что нужно.
All right, let me get on this side.|Хорошо, позволь мне встать на эту сторону.
[SOUND] All right, so, we know now that this last section here is for subnetting, subnetting purposes only.|[ЗВУК] Хорошо, теперь мы знаем, что этот последний раздел здесь предназначен только для разделения на подсети.
We break it up into its four bit values for each position, all right?|Мы разбиваем его на четыре битовых значения для каждой позиции, хорошо?
We've been given a network presix,|Нам дали префикс сети,
prefix, I'm sorry, network prefix of 52.|префикс, извините, префикс сети 52.
Therefore, that blue line you see right here, that is our starting point.|Таким образом, эта синяя линия, которую вы видите здесь, является нашей отправной точкой.
And we count for subnets like we normally do.|И мы считаем подсети, как обычно.
We count for subnets like we normally do starting at here.|Мы считаем подсети, как обычно, начиная с этого места.
So we count for subnets two,|Итак, мы считаем подсети два,
what do we mean?|что мы имеем в виду?
What are we looking for?|Что мы ищем?
I think we have a need for 10 subnets.|Думаю, нам нужно 10 подсетей.
So we go 2, 4, 8, to little, 16 so that's where my line then stops.|Итак, мы идем 2, 4, 8, к маленькому, 16, так что моя линия заканчивается.
So what is the increment value?|Итак, каково значение приращения?
And that is the most important part in IPv6.|И это самая важная часть IPv6.
We need to understand what is our increment value.|Нам нужно понять, какова наша ценность приращения.
Our increment value is one.|Наше значение приращения равно единице.
We stopped at what position, though?|Но на какой позиции мы остановились?
That is key.|Это ключ.
Cuz we need to know what position we're incrementing by.|Потому что нам нужно знать, на какую позицию мы увеличиваем.
In this case,|В таком случае,
we're in the second position,|мы на второй позиции,
meaning that second 0 right there.|это означает, что второй 0 прямо здесь.
Right, right here,|Прямо здесь,
we're at the second position.|мы на второй позиции.
So we're incrementing right there,|Итак, мы увеличиваем прямо здесь,
by what number?|по какому номеру?
One.|Один.
Remember, in IPv4 the bit values on top was, 1, 2, 4, 8, 16, 32, 64, 128.|Помните, что в IPv4 значения битов сверху были 1, 2, 4, 8, 16, 32, 64, 128.
But this is hex now.|Но теперь это проклятие.
The bit values are just 1, 2, 4, 8.|Битовые значения равны 1, 2, 4, 8.
So therefore, if I stop counting for subnets right there,|Поэтому, если я сразу перестану считать подсети,
cuz all I needed were 10,|Потому что все, что мне нужно, было 10,
I had to go to 16.|Пришлось перейти на 16.
My increment is one.|Мой прирост - один.
So I am incrementing by one in the second position.|Итак, я увеличиваю на единицу во второй позиции.
That's how you find it.|Вот как вы это находите.
You first put the line where the sub,|Вы сначала помещаете строку, где саб,
where the network prefix that was given.|где был указан сетевой префикс.
And it was getting here,|И это было здесь,
remember how we got that, 16 and 16 is 32 and 16 is 48,|помните, как мы это получили, 16 и 16 равно 32, а 16 - 48,
49, 50, 51, 52, line.|49, 50, 51, 52, стр.
That is our starting point.|Это наша отправная точка.
That line is our starting point.|Эта линия - наша отправная точка.
Now we'll need 10 subnets.|Теперь нам понадобится 10 подсетей.
So we count like we normally do for IPv4, from left to right, 2, 4, 8, 16.|Итак, мы считаем, как обычно делаем для IPv4, слева направо, 2, 4, 8, 16.
16, therefore, our increment is 1.|16, следовательно, наше приращение равно 1.
1 because that bit value right there,|1, потому что это битовое значение прямо здесь,
is 1.|равно 1.
What position?|Какая позиция?
Position 2, position 2, all right?|Позиция 2, позиция 2, хорошо?
And then, we can go ahead and start incrementing by one.|А затем мы можем продолжить и начать увеличивать на единицу.
This right here, finding the,|Это прямо здесь, найдя,
this increment value is the most important part of the subnetting.|это значение приращения является наиболее важной частью подсети.
That's the hardest part that people have when they're starting IPv6 is finding the increment value.|Это самая сложная часть, с которой люди запускают IPv6, - это найти значение приращения.
Are there calculators out there?|Есть ли калькуляторы?
Yes.|Да.
Do you want to check your work?|Хотите проверить свою работу?
Most definitely.|Определенно.
I do it.|Я делаю это.
I want to make sure that I'm doing it right.|Я хочу убедиться, что делаю все правильно.
Do you go to what's that website,|Вы заходите на сайт,
subnettingonline.com,|subnettingonline.com,
subnettingonline.com.|subnettingonline.com.
They have IPv6 calculators.|У них есть калькуляторы IPv6.
They have IPv4 calculators.|У них есть калькуляторы IPv4.
They've got all sorts of tools.|У них есть всевозможные инструменты.
So you want to verify your work,|Итак, вы хотите проверить свою работу,
all right.|отлично.
Me as an instructor, definitely I wanna make sure I'm doing things correctly, so I verify my work.|Я, как инструктор, определенно хочу убедиться, что все делаю правильно, поэтому проверяю свою работу.
You, as an IT individual out in the field,|Вы, как ИТ-специалист в этой области,
as well, okay, you wanna verify your work.|а также, хорошо, вы хотите подтвердить свою работу.
You always wanna verify that what you're doing is correct.|Вы всегда хотите убедиться, что то, что вы делаете, правильно.
So using calculators,|Итак, используя калькуляторы,
there's nothing wrong.|нет ничего плохого.
You just can't use it when you go take your certification.|Вы просто не можете использовать его, когда идете брать сертификат.
And, don't worry.|И не волнуйтесь.
Do not worry.|Не волнуйтесь.
Do not worry.|Не волнуйтесь.
For this course, for the CCNA 200-120|Для этого курса, для CCNA 200-120
test, or if you're taking ICND1 or ICND2,|тест, или если вы принимаете ICND1 или ICND2,
or you're taking the CCNT,|или вы берете CCNT,
whatever it is that you're taking,|что бы вы ни брали,
all right, you are not going to be subnetting in IPv6.|хорошо, вы не собираетесь использовать подсети в IPv6.
Nowhere near in the future is that gonna happen.|Это произойдет не в ближайшем будущем.
Okay, so but I want you to start embracing it.|Хорошо, но я хочу, чтобы вы начали это понимать.
Because you can see it's not that difficult.|Как видите, это не так уж и сложно.
All you gotta do is take that subnet section,|Все, что вам нужно сделать, это взять этот раздел подсети,
break it up into its binary bit form.|разбить его на двоичную битовую форму.
All right,|Отлично,
cuz each one of these is 4 bits long.|потому что каждый из них имеет длину 4 бита.
Put it in the increment values on top.|Поместите его в значения приращения вверху.
You have a starting point that you've been given.|У вас есть отправная точка, которую вам дали.
Count your subnets like you normally would, 2, 4, 8, whatever it is.|Подсчитайте свои подсети, как обычно, 2, 4, 8, что угодно.
Then, the bit value that it lands on,|Затем значение бита, на которое он попадает,
that is your increment.|это ваш прирост.
And once you find the increment,|И как только вы найдете приращение,
and once you find the position that you're incrementing in,|и как только вы найдете позицию, в которой вы увеличиваете,
then you can begin to layout the network,|затем можно приступить к разводке сети,
and that's what we're gonna do next.|и это то, что мы будем делать дальше.
I'll see you in the next lecture.|Увидимся на следующей лекции.