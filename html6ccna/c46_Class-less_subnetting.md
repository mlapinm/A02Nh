D:\mailCloud\prjother\tmp\1\c46_Class-less subnetting.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
Welcome back, everyone.|С возвращением, все.
We just finished doing what's called classful subnetting.|Мы только что закончили делать то, что называется классовой подсетью.
Meaning you have the same subnet mask or number of hosts in the same segments.|Это означает, что у вас одинаковая маска подсети или количество хостов в одних и тех же сегментах.
But that is not really the reality.|Но на самом деле это не так.
It used to be the reality.|Раньше это было реальностью.
Now the reality is that you have classless subnetting.|Теперь реальность такова, что у вас есть бесклассовые подсети.
It is called VLSM.|Это называется VLSM.
That is the, the birth of VLSM.|Это рождение VLSM.
It was a mechanism that was created to slow down the inevitable,|Это был механизм, который был создан, чтобы замедлить неизбежное,
that's how you say it, demise of IPv4,|так вы говорите, конец IPv4,
okay.|Ладно.
So what VLSM is, it stands for variable length subnet mask as the word says.|Итак, что такое VLSM, это означает маску подсети переменной длины, как говорится в этом слове.
It will vary throughout the,|Он будет варьироваться в зависимости от того,
the network segment based on the needs of the network, okay.|сегмент сети, основанный на потребностях сети, хорошо.
And you see this diagram that I have back here.|И вы видите эту диаграмму, которая у меня здесь.
Now I believe in my book I have this diagram, but for those of you who have the book, I'll give you a better explanation now, or an explanation.|Теперь я верю, что в своей книге у меня есть эта диаграмма, но для тех из вас, у кого есть эта книга, я дам вам лучшее объяснение или объяснение.
If you found this somewhat confusing, with the numbers and all that.|Если вас это несколько сбивает с толку, с числами и прочим.
All right, we have an infrastructure that you see here.|Хорошо, у нас есть инфраструктура, которую вы видите здесь.
This is one company, let's say an enterprise company.|Это одна компания, скажем, корпоративная компания.
That in one portion, one branch,|Что в одной части, в одной ветке,
headquarters or whatever,|штаб или что-то еще,
one branch office, you have a need for 3,500 IPs.|один филиал, вам необходимо 3500 IP.
On another one, you have 725 and another one you have 100.|На другом у вас 725, а на другом - 100.
And then of course you need two IPs per segment here to connect from router to router,|И тогда, конечно, вам понадобятся два IP-адреса на сегмент для подключения от маршрутизатора к маршрутизатору,
router to router.|маршрутизатор к маршрутизатору.
So the rule of VLSM, number one,|Итак, правило VLSM, номер один,
is that you need to always use the zero network.|в том, что вам нужно всегда использовать нулевую сеть.
Cuz the whole point of VLSM is not to waste IP addresses.|Потому что весь смысл VLSM - не тратить впустую IP-адреса.
So you wanna be able to use the whole spectrum.|Итак, вы хотите использовать весь спектр.
So you always use the zero network when working within VLSM,|Таким образом, вы всегда используете нулевую сеть при работе с VLSM,
variable length subnet mask.|маска подсети переменной длины.
Okay?|Ладно?
And then you would start from the highest number of IPs and work your way down to the lowest number of IPs.|А затем вы начнете с наибольшего количества IP-адресов и постепенно спуститесь к наименьшему количеству IP-адресов.
Okay.|Ладно.
So those are the rules,|Таковы правила,
the guidelines that you wanna follow.|руководящие принципы, которым вы хотите следовать.
All right.|Отлично.
Now, you have to start with the address that you've been given.|Теперь вы должны начать с адреса, который вам дали.
As far as the address that we've been given, and I'm gonna put these back to what they were.|Что касается адреса, который нам дали, и я верну их туда, где они были.
Let me do it here, cuz I don't wanna cause all sorts of craziness.|Позвольте мне сделать это здесь, потому что я не хочу вызывать всякое безумие.
Let me go here real quick.|Пусти меня сюда поскорее.
I say real quick, but.|Я говорю очень быстро, но.
[BLANK_AUDIO]|[BLANK_AUDIO]
Zero zero zero zero zero,|Ноль ноль ноль ноль ноль,
zero zero zero zero zero, zero, zero,|ноль ноль ноль ноль ноль, ноль, ноль,
zero.|нуль.
All right, so we're given a 172.20.0.0|Хорошо, мы получили 172.20.0.0
network.|сеть.
Obviously, this is.|Очевидно, это так.
[BLANK_AUDIO]|[BLANK_AUDIO]
This is one octet right here, correct?|Это один октет, верно?
One entire octet right here, all zeros,|Один целый октет, все нули,
all eight zeros.|все восемь нулей.
And this is another octet, fourth octet,|А это еще один октет, четвертый октет,
all eight zeros.|все восемь нулей.
I'll go ahead and move that back to where it was.|Я пойду и верну его на место.
There we go.|Вот и все.
I guess we can move a little bit more this way.|Я думаю, мы можем двигаться дальше в этом направлении.
All right.|Отлично.
And what the yellow numbers, as it explains here,|И что за желтые числа, как здесь объясняется,
all the numbers in yellow are the network increments.|все числа желтого цвета - это приращения сети.
Because, as we start drawing our lines, I put the numbers in yellow,|Потому что, когда мы начинаем рисовать линии, я выделяю числа желтым,
as your network increment.|по мере увеличения вашей сети.
And, we'll check as I go.|И мы проверим, как я пойду.
Make sure those no mistakes.|Убедитесь, что в них нет ошибок.
And the numbers up here in red,|И цифры здесь красные,
these numbers are used to calculate for broadcast.|эти числа используются для расчета трансляции.
It's the same scenario, when we do the diagram, when we explain the diagram,|Тот же сценарий, когда мы делаем диаграмму, когда мы объясняем диаграмму,
that the numbers to the right are used to calculate for broadcast.|что числа справа используются для расчета трансляции.
The, the sum of the numbers to the right.|, Сумма чисел справа.
That will equal the number that you calculate broadcast, all right?|Это будет равняться числу, которое вы рассчитали для трансляции, хорошо?
So, what do we have here?|Итак, что у нас здесь?
The first number of nodes, the largest number of nodes is 3,500.|Первое количество узлов, наибольшее количество узлов - 3500.
We have a starting point of sev,|У нас есть отправная точка сев,
172.20.0.0.|172.20.0.0.
That is our starting point.|Это наша отправная точка.
That is our starting address.|Это наш начальный адрес.
We must start from right there.|Мы должны начать прямо здесь.
So let's go ahead and bring this down a little bit here.|Итак, давайте продолжим и немного опустим это здесь.
All right.|Отлично.
There's another example down here,|Вот еще один пример,
so the green bar separates one example from the next.|таким образом, зеленая полоса отделяет один пример от другого.
So now, we have that.|Итак, теперь у нас это есть.
We need to count for 3,500 nodes or hosts.|Нам нужно насчитать 3500 узлов или хостов.
So we know when we count for hosts, we count from right to left, all right?|Итак, мы знаем, что когда мы считаем хостов, мы считаем справа налево, ясно?
And you start at the number two and double as you go.|И вы начинаете с числа два и удваиваете по мере продвижения.
So we got two, four, eight, 16, 32, 64,|Итак, у нас есть два, четыре, восемь, 16, 32, 64,
128,|128,
256, 512, 1024, 2048, 4096.|256, 512, 1024, 2048, 4096.
So there is where we stop, right?|Итак, на этом мы остановимся, верно?
Cuz we need 3,500.|Потому что нам нужно 3500.
So if we need 3,500, we're good to go right there.|Так что, если нам нужно 3500, мы можем приступить к делу.
So we draw our line between the 16 and the eight.|Итак, мы проводим линию между 16 и 8.
So the 16 becomes our network increment,|Таким образом, 16 становится приращением нашей сети,
now at this point, our network increment we're going to use as a cross reference to check to make sure that our next starting point is correct.|Теперь, на этом этапе, приращение нашей сети мы будем использовать в качестве перекрестной ссылки, чтобы убедиться, что наша следующая отправная точка верна.
So, we draw our line.|Итак, проводим нашу линию.
Then we went ahead and said okay.|Потом мы пошли дальше и сказали "хорошо".
From the number eight, and then, you know,|От числа восемь, а потом, знаете,
for some reason my finger just, you know,|почему-то мой палец просто, знаете ли,
doesn't like it.|не нравится.
All right, these right here, eight and two is ten, four is 14 and one is 15.|Хорошо, вот эти восемь, два - десять, четыре - 14, а один - 15.
That is why you see that red number 15 up there.|Вот почему вы видите там красное число 15.
So we take and then we we add up properly.|Итак, мы берем, а затем правильно складываем.
And this 255 that you see right here, is also the addition or the sum of all these bit values.|И этот 255, который вы видите здесь, также является сложением или суммой всех этих битовых значений.
That's what the 255 represents.|Вот что представляет собой 255.
So we have 15 in the third octet.|Итак, в третьем октете 15.
So we have zero here in the third octet.|Итак, в третьем октете у нас ноль.
So 172, zero plus 15, we have 172.15.|Итак, 172, ноль плюс 15, получаем 172,15.
Now in the fourth octet, it's 255.|Теперь в четвертом октете 255.
So we have 172.20.15, 0.255 and 255.|Итак, у нас есть 172.20.15, 0.255 и 255.
So that's how we get that.|Вот как мы это получаем.
So our line, our very first line that we drew,|Итак, наша линия, наша самая первая линия, которую мы нарисовали,
we drew it right here between the 16 and the eight.|мы нарисовали это прямо здесь между 16 и 8.
That means that those bit values to the left just turned odd.|Это означает, что значения битов слева стали нечетными.
[BLANK_AUDIO]|[BLANK_AUDIO]
So now your new mask for that particular network, for the 3,500 nodes, is a CIDR 20.|Итак, теперь ваша новая маска для этой конкретной сети для 3500 узлов - это CIDR 20.
And remember, what CIDR, C-I-D-R stands for, it's classless interdomain routing.|И помните, что означает CIDR, C-I-D-R, это бесклассовая междоменная маршрутизация.
Classless interdomain routing.|Бесклассовая междоменная маршрутизация.
Now the range and this is where it gets a little, some people get confused,|Теперь диапазон, и здесь он немного становится, некоторые люди путаются,
because we're working with two different octets.|потому что мы работаем с двумя разными октетами.
I think of it as a think of the analogy of a car, all right.|Я думаю об этом как об аналогии с автомобилем, хорошо.
What's after 0.0?|Что после 0.0?
0.1, right?|0,1, верно?
You have all zero miles, you have, you know, and the first number all the way to the right starts incrementing first before|У вас все ноль миль, вы знаете, и первое число вправо начинает увеличиваться, прежде чем
the second number.|второй номер.
So 0.1.|Итак, 0.1.
And then this is just the opposite.|А тут как раз наоборот.
Here you have 172, 20, 15, 255, the last available will be 15.254.|Здесь у вас 172, 20, 15, 255, последний доступный будет 15.254.
Not 14.254, but 15.254.|Не 14,254, а 15,254.
So, this will need to go all the way down,|Итак, это нужно будет полностью опустить,
let me get it out of the way.|позволь мне убрать это с дороги.
This 254 will need to go all the way down to zero before this can actually go down to 14.|Это 254 должно будет полностью опуститься до нуля, прежде чем оно действительно может снизиться до 14.
So you do have 3,500 addresses available for this particular network, which if you say,|Итак, у вас есть 3500 адресов, доступных для этой конкретной сети, которые, если вы скажете,
hey Mr.|эй, мистер
Administrator, here's your 3,500 nodes, or meaning here's your network ID with your mask,|Администратор, вот ваши 3500 узлов, то есть вот ваш сетевой идентификатор с вашей маской,
now you can resubnet that IP address.|теперь вы можете повторно подсеть этот IP-адрес.
That network ID with whate, whatever your needs may be.|Этот сетевой идентификатор с чем угодно, какими бы ни были ваши потребности.
Okay, whatever your needs may be.|Хорошо, какими бы ни были ваши потребности.
So, that's the first one.|Итак, это первое.
Now, another rule that I didn't mention,|А теперь еще одно правило, о котором я не упоминал,
once you get to the last IP,|как только вы дойдете до последнего IP,
cuz this is our IP, regardless, even though we can't use it on the network.|Потому что это наш IP-адрес, несмотря на то, что мы не можем использовать его в сети.
That is the last IP.|Это последний IP.
So, you say to yourself, okay, what after 15.255?|Итак, вы говорите себе, хорошо, что после 15.255?
We've reached the maximum value, and that octet 255.|Мы достигли максимального значения, и этот октет 255.
That means that it flips over the 15 by 1|Это означает, что он переворачивает 15 на 1
to 16, and then, it resets itself back to 0.|до 16, а затем сбрасывается обратно на 0.
Therefore, that's our next starting point,|Следовательно, это наша следующая отправная точка,
16.0.|16.0.
Okay?|Ладно?
16.0, which now, we can use that network increment,|16.0, теперь мы можем использовать это приращение сети,
that yellow number to verify, if that's indeed correct.|этот желтый номер, чтобы проверить, действительно ли это правильно.
And you see you got 0 and 16, 16.|И вы видите, что у вас 0 и 16, 16.
So, a cross check.|Итак, перекрестная проверка.
That's all it is.|Вот и все.
Is a cross check.|Это перекрестная проверка.
So now, we have our second starting point.|Итак, теперь у нас есть вторая отправная точка.
Now, our second point, we get the next highest number of IPs, Which is 725.|Теперь, наша вторая точка, мы получаем следующее по величине количество IP-адресов, которое составляет 725.
All right?|Отлично?
Perfect.|Отлично.
So now, that we have our new starting point.|Итак, теперь у нас есть новая отправная точка.
We know, what we need to do.|Мы знаем, что нам нужно делать.
We need to draw a new line.|Нам нужно провести новую линию.
So, we count again.|Итак, снова считаем.
Well, 2, 4, 8, 16, 32, 64, 128,|Ну, 2, 4, 8, 16, 32, 64, 128,
[INAUDIBLE] 1024, 2048.|[Неразборчиво] 1024, 2048.
One of the things that I counted too I'm sorry, 1024.|Одна из вещей, которые я тоже посчитал, извините, 1024.
That's where my line is at.|Вот где моя линия.
Sorry.|Сожалею.
1024.|1024.
If my total is too little, cuz I need 725.|Если моя сумма слишком мала, мне нужно 725.
So, the next one over 1024, will be the correct place to be.|Таким образом, следующий, более 1024, будет правильным местом.
So my line, would separate between 4, and 2.|Таким образом, моя линия будет разделяться между 4 и 2.
So 4 would be my network increment, and then, if I add 2, and 1, that's 3.|Итак, 4 будет моим приращением сети, а если я добавлю 2 и 1, то получится 3.
That's why you see that number 3 there, as the number that we're going to use,|Вот почему вы видите там цифру 3 как число, которое мы собираемся использовать,
to calculate for broadcast.|рассчитать для трансляции.
So, let's go on, and do so.|Итак, давайте продолжим и сделаем так.
And again, since we're in the third octet,|И снова, поскольку мы находимся в третьем октете,
we still have to add all these bid values on top, which will equal to 55.|нам все еще нужно добавить все эти значения ставок сверху, что будет равно 55.
Cuz we're still focusing on, the third octet.|Потому что мы все еще сосредоточены на третьем октете.
So, we have the 172, 20,16, 0.|Итак, у нас есть 172, 20, 16, 0.
So 16 in the third octet, plus 3 in the third octet, that gives me 19.|Итак, 16 в третьем октете плюс 3 в третьем октете, что дает мне 19.
And then, we go to the fourth octet, 0|Затем мы переходим к четвертому октету, 0
plus the 255, 255.|плюс 255, 255.
So, we have a 19.255 as a broadcast.|Итак, у нас есть трансляция 19.255.
But we did move the line over, two more bits, did we not?|Но мы переместили линию, еще два бита, не так ли?
So, oh, they're, so they're already in there.|Итак, о, они, так что они уже там.
I guess, I forgot to 0 them out,|Думаю, я забыл их выпустить,
[INAUDIBLE] but we already turned those two bits on.|[НЕДОСТАТОЧНО], но мы уже включили эти два бита.
So now, you went from a 20 at the beginning, to a 22.|Итак, вы перешли с 20 в начале на 22.
Now that you have that CIDR 22, you wanna find the range.|Теперь, когда у вас есть CIDR 22, вы хотите найти диапазон.
What's in between, 16.0, and 19.255?|Что находится между 16.0 и 19.255?
Well, what's after 16.0?|Ну что после 16.0?
16.1.|16.1.
That's your first available IP address.|Это ваш первый доступный IP-адрес.
Last available IP address, 1 before,|Последний доступный IP-адрес, 1 раньше,
whoops, 1 before 19.255 which is 19.254.|упс, 1 до 19,255, то есть 19,254.
There you go.|Вот так.
Now you have your, and you wanna verify,|Теперь у вас есть, и вы хотите проверить,
you wanna verify, because you say that you want, hey, okay, I reached the last one, what's my next starting point?|вы хотите подтвердить, потому что вы говорите, что хотите, эй, хорошо, я дошел до последнего, какова моя следующая отправная точка?
What's after 19.255?|Что после 19.255?
We've reached the maximum, in that last octet there, 255.|Мы достигли максимума в последнем октете 255.
So, it resets itself to 0, right?|Итак, он сбрасывается до 0, верно?
So that means it, incremented that 19.1,|Это означает, что увеличилось 19,1,
therefore you have 20.0.|поэтому у вас 20.0.
So, you see that the 4, and 16 is 20,|Итак, вы видите, что 4, а 16 - это 20,
therefore, we're still okay.|поэтому у нас все еще в порядке.
Cross check.|Перекрестная проверка.
Cross check.|Перекрестная проверка.
Just to keep us honest, right?|Просто чтобы мы были честны, правда?
So, we already got rid of that.|Итак, мы уже избавились от этого.
So, if you hand that to the administrator,|Итак, если вы передадите это администратору,
hey, here's your network ID,|эй, вот твой сетевой идентификатор,
here's your new mask.|вот твоя новая маска.
Do whatever it is that you need to do, to assign IP addresses,|Делайте то, что вам нужно, назначать IP-адреса,
to your particular part on the enterprise.|к вашей конкретной части на предприятии.
Now, we do one for 100 nodes.|Теперь мы делаем один для 100 узлов.
Now, with 100 nodes, you know, you're gonna be in the fourth octet.|Теперь, когда у вас 100 узлов, вы будете в четвертом октете.
You know that.|Ты это знаешь.
So, let's count.|Итак, давайте посчитаем.
How many do we need?|Сколько нам нужно?
100.|100.
So, 100, there it is, right there.|Итак, 100, вот оно, вот оно.
Between the 128th bit, and a 64.|Между 128-битным и 64-битным.
That will give us 128 minus 2, for those of you, that I think you know?|Это даст нам 128 минус 2 для тех из вас, кого, я думаю, вы знаете?
You have to subtract 2, from the host side.|Вы должны вычесть 2 со стороны хоста.
So, you have your 126 hosts, which is 2,400.|Итак, у вас есть 126 хостов, что составляет 2400.
You draw your line, right there.|Вы проводите свою линию прямо здесь.
Perfect.|Отлично.
Now, our focus has changed, from the third octet, to the fourth octet.|Теперь наш фокус сместился с третьего октета на четвертый октет.
Now, the first three octets, do not change.|Теперь первые три октета не меняются.
It is only the fourth octet, that we're focusing on.|Мы фокусируемся только на четвертом октете.
Everything else, stays the same.|Все остальное остается прежним.
Let's go ahead, and turn on the bit values now.|Давайте продолжим и теперь включим битовые значения.
1, 1, 1, okay, we turn on the three more,|1, 1, 1, ладно, включаем еще три,
three more bits.|еще три бита.
All right.|Отлично.
So, we have 170 172.20.20.0.|Итак, у нас 170 172.20.20.0.
20.0.|20.0.
So again, we're in the fourth octet.|Итак, мы снова находимся в четвертом октете.
We're in, am I in the right place?|Мы в нужном месте?
Yes, I am, okay?|Да, хорошо?
172.20.20.0, we're in the fourth octet,|172.20.20.0, мы находимся в четвертом октете,
therefore,|следовательно,
I need to add 127, because 128 is the increment.|Мне нужно добавить 127, потому что 128 - это приращение.
I add all the other ones, all the other bits, values, and they turn out to be 127, and really, I'm not adding them.|Я добавляю все остальные, все остальные биты, значения, и получается 127, и на самом деле я их не добавляю.
You could adding them in, if you want.|Вы можете добавить их, если хотите.
Just to verify.|Просто чтобы проверить.
It's always going to be one less the increment, the network increment number.|Это всегда будет на единицу меньше приращения, номера приращения сети.
So 127, and 0, is 127.|Итак, 127, а 0 - 127.
All right?|Отлично?
And then of course, we have our mask,|И, конечно же, у нас есть маска,
which is, this is all on, right?|это все включено, верно?
So, we've got one more, that's 25.|Итак, у нас есть еще один, это 25.
So, we set there, 25.|Итак, мы сидели там, 25.
And then, you say what's in between?|А потом вы говорите, что между ними?
Well, what's after 20.0?|Ну что после 20.0?
20.1.|20.1.
What's before 127?|Что до 127?
126.|126.
See, so the last octet is a lot easier to work with, cuz it's only that,|Видите ли, с последним октетом намного проще работать, потому что это только то,
that one octet you're working with.|тот один октет, с которым вы работаете.
So, you have your range, you have your 126|Итак, у вас есть свой диапазон, у вас есть 126
addresses.|адреса.
You give that network ID, that mask, you go on Mr Administrator,|Вы даете этот сетевой идентификатор, эту маску, вы переходите к господину Администратору,
do what you need to do.|делай то, что тебе нужно делать.
All right?|Отлично?
And then, we go to the next starting point.|А затем мы переходим к следующей отправной точке.
But now, our last address here was 20.127.|Но теперь наш последний адрес здесь был 20.127.
Our focus is the last octet.|Мы фокусируемся на последнем октете.
What's after 127?|Что после 127?
128.|128.
So, that's our new starting point, right there.|Итак, это наша новая отправная точка.
128.|128.
So, if you wanna cross reference again,|Итак, если вы снова хотите перекрестную ссылку,
cross check,|перекрестная проверка,
128, the network increment plus 0, that's 128.|128, приращение сети плюс 0, это 128.
Now, you have that 128 there.|Теперь у вас есть 128.
So, that is your new starting point.|Итак, это ваша новая отправная точка.
Now, we need to address,|Теперь нам нужно обратиться к
since we have every site, if you would.|так как у нас есть каждый сайт, если хотите.
We will find their network ID with their mask, giving it to the administrator.|Мы найдем их сетевой ID с их маской, передав администратору.
Now, we need to find IPs, for each particular router, all right?|Теперь нам нужно найти IP-адреса для каждого конкретного маршрутизатора, хорошо?
Cuz, you know, you had, you need IPs for each interface on that router.|Потому что, знаете, у вас были IP-адреса для каждого интерфейса на этом маршрутизаторе.
So, we need 2, and 2, and 2, and 2.|Итак, нам нужны 2, и 2, и 2, и 2.
So, our starting point is 128.|Итак, наша отправная точка - 128.
We need two IP's.|Нам нужно два IP-адреса.
We know, we need to move the line all the way over, to right there.|Мы знаем, что нам нужно переместить линию полностью, прямо здесь.
Cuz that's a typical number that we use in IT, for some reason.|Потому что это типичное число, которое мы почему-то используем в ИТ.
We're always using a /30, right?|Мы всегда используем / 30, верно?
Oops.|Ой.
[BLANK_AUDIO]|[BLANK_AUDIO]
Now, they wanna turn on.|Теперь они хотят включиться.
So now, we turn that on, and that turns into a CIDR 30.|Итак, теперь мы включаем это, и он превращается в CIDR 30.
CIDR 30.|CIDR 30.
So, that's our new mask.|Итак, это наша новая маска.
Now, you see that it's 2, 2, 2.|Теперь вы видите, что это 2, 2, 2.
So, we really don't need to move the line anymore.|Итак, нам больше не нужно перемещать линию.
We should need to go to the next starting point and then the next starting point and the next starting point.|Нам нужно перейти к следующей начальной точке, а затем к следующей начальной точке и следующей начальной точке.
And when you are working with CIDR 30,|А когда вы работаете с CIDR 30,
it's really, really very simple.|это действительно очень просто.
Now I'm gonna show you right now.|Сейчас я покажу тебе прямо сейчас.
Now our starting point was 128.|Теперь наша отправная точка была 128.
We need to find out the broadcast.|Нам нужно узнать трансляцию.
We need to add these two numbers, which is three.|Нам нужно сложить эти два числа, то есть три.
So 3 and 128, 131.|Итак, 3 и 128, 131.
What's in between?|Что между ними?
129 and 30.|129 и 30.
And we know it's already a CIDR 30.|И мы знаем, что это уже CIDR 30.
What's after 131?|Что после 131?
132.|132.
You add the 3, 132 and 3, 135.|Вы складываете 3, 132 и 3, 135.
What's in between?|Что между ними?
133 and 134, see that?|133 и 134, видите?
135, 136.|135, 136.
You add the 3, 139.|Вы добавляете 3, 139.
What's in between?|Что между ними?
137, 138.|137, 138.
And it's kind of cool because it goes in order, 128, 129, 130,|И это круто, потому что идет по порядку: 128, 129, 130,
131, 132, 33, 34, 35, 36, 37, 38, and 139.|131, 132, 33, 34, 35, 36, 37, 38 и 139.
So when I'm using a CIDR 30, it's extremely simple cuz it's like counting.|Когда я использую CIDR 30, это очень просто, потому что это похоже на счет.
The network, you know, you see the network in the broadcast, whatever's in between.|Сеть, вы знаете, вы видите сеть в трансляции, что бы там ни было.
But this is what VLSM is.|Но это то, что такое VLSM.
Are you going to be doing this in the examination?|Вы собираетесь делать это на экзамене?
By no means.|Ни в коем случае.
By no means are they going to sit down and tell you, hey, give you a scenario like this and then tell you to figure out what the networks are.|Ни в коем случае они не собираются сесть и сказать вам, эй, дать вам такой сценарий, а затем попросить вас выяснить, что это за сети.
They're gonna give you a very, very,|Они собираются дать вам очень, очень,
simplistic, three computers,|упрощенно, три компьютера,
four computers.|четыре компьютера.
Some of them are already gonna have assigned IP addresses,|Некоторым из них уже назначены IP-адреса,
and you need to find out what's the next subnet.|и вам нужно узнать, какая следующая подсеть.
And again, you say, okay, it's the same thing.|И снова вы говорите, хорошо, это то же самое.
If I end it on this one, what's next after that?|Если я закончу на этом, что будет дальше?
And then how many hosts do I need.|А потом сколько хостов мне нужно.
Then you give the right subnet mask.|Затем вы даете правильную маску подсети.
It's the concept of giving you a starting address,|Это концепция предоставления вам начального адреса,
knowing what the last address is,|зная, каков последний адрес,
following up.|последующие меры.
You know, doing, hey, 1555, then the next one, the starting one is 16.0.|Знаешь, делаю, эй, 1555, потом следующий, начальный - 16.0.
Then I move the line accordingly to find the right mask.|Затем я перемещаю линию соответствующим образом, чтобы найти правильную маску.
But now is you need to get used to, I mean VLSM is not, nothing difficult.|Но теперь к этому нужно привыкнуть, то есть VLSM нет, ничего сложного.
We use it more likely every day.|Мы пользуемся им чаще каждый день.
Not every department is gonna have the need for the same number of subnets.|Не каждому отделу потребуется одинаковое количество подсетей.
Now let me clarify something, and I've seen this in many schools that I've been at.|Теперь позвольте мне кое-что прояснить, и я видел это во многих школах, в которых учился.
You're not gonna really use VLSM internally.|Вы не собираетесь использовать VLSM для внутренних целей.
This is really something that's done externally with public IP addresses.|Это действительно то, что делается извне с помощью общедоступных IP-адресов.
The only reason that we use, as instructors, that we use private IP addressing, cuz it's something that we're used to seeing on a daily basis.|Единственная причина, по которой мы, как инструкторы, используем частную IP-адресацию, потому что это то, что мы привыкли видеть ежедневно.
So it's easier on the eyes to look at a private IP address than it would be a public IP address.|Таким образом, проще смотреть на частный IP-адрес, чем на общедоступный IP-адрес.
So, but, the reason, the birth,|Итак, но причина, рождение,
of VLSM was that, was to save public IP addresses.|VLSM было таково, было сохранять публичные IP-адреса.
So we don't, if somebody needed 1,000 IP addresses at one point,|Так что мы этого не делаем, если кому-то в какой-то момент понадобилось 1000 IP-адресов,
they would say okay, I wanna give you a CIDR 16.|они сказали бы хорошо, я хочу дать вам CIDR 16.
Now you have 65,000 plus addresses, way too much, way too much.|Теперь у вас есть 65 000 с лишним адресов, слишком много, слишком много.
So now we're allowed to move that line back and forth to meet the needs of the network.|Итак, теперь нам разрешено перемещать эту линию взад и вперед для удовлетворения потребностей сети.
And with the new routing protocols, such as RIP version two, EIGRP, or OSPF, or the version six, the IP version six, all those routing protocols.|И с новыми протоколами маршрутизации, такими как RIP версии два, EIGRP или OSPF, или версии шесть, IP версии шесть, все эти протоколы маршрутизации.
They all support VLSM.|Все они поддерживают VLSM.
The only ones that didn't support VLSM was RIP version one and EIGRP.|Единственные, которые не поддерживали VLSM, - это RIP версии 1 и EIGRP.
That's why we no longer use that, or teach that because it's not being used, period.|Вот почему мы больше не используем это или обучаем этому, потому что это не используется, точка.
So the newer routing protocols will support VLSM, which is great.|Так что новые протоколы маршрутизации будут поддерживать VLSM, и это здорово.
All right, because it's gonna save out networks, and it's gonna be a lot,|Хорошо, потому что это спасет сети, и это будет много,
a lot better on our routing tables.|намного лучше в наших таблицах маршрутизации.
And, we'll have a lot less waste of IP addresses on our network.|И у нас будет намного меньше ненужных IP-адресов в нашей сети.
So there you go.|Итак, поехали.
This is what VLSM is.|Вот что такое VLSM.
It's a little bit whatever, just gotta keep track of where you're at.|Это немного неважно, просто нужно отслеживать, где ты находишься.
Remember, you have a starting point.|Помните, у вас есть отправная точка.
You account for the number of hosts.|Вы учитываете количество хостов.
You find your broadcasts, what's in between, next starting point,|Вы находите свои трансляции, что между ними, следующую отправную точку,
same thing over and over and over again.|одно и то же снова и снова.
Again, something like this is not what you're gonna do.|Опять же, вы не собираетесь делать что-то подобное.
This is something you do to practice to get used to doing it.|Это то, что вы делаете, чтобы практиковаться, чтобы привыкнуть к этому.
In the exam it's gonna be a very, very simple, simple, or I'll give you this.|На экзамене это будет очень, очень просто, просто, или я дам вам это.
It'll be, let's say, two routers, and I say,|Это будет, скажем, два маршрутизатора, и я говорю:
what mask would you use between two routers?|какую маску вы бы использовали между двумя маршрутизаторами?
CIDR 30, right?|CIDR 30, верно?
You know, it has two IP addresses.|Вы знаете, у него два IP-адреса.
That's the type of questions that you probably confront in the test.|С такими вопросами вы, вероятно, столкнетесь в тесте.
All right.|Отлично.
There's your VLSM.|Вот и ваш VLSM.
Very simple, I'll see you in the next lecture.|Очень просто, увидимся на следующей лекции.
[BLANK_AUDIO]|[BLANK_AUDIO]