D:\mailCloud\prjother\tmp\1\c50_How to setup the diagram for subnetting..md  


__|__
--|--
All right, here we are.|Хорошо, вот и мы.
The diagram for subnetting in IPv6.|Схема подсетей в IPv6.
Well a little review first, a little review, all right?|Ну, сначала небольшой обзор, небольшой обзор, хорошо?
Remember, we have two, separate different sides.|Помните, что у нас есть две разные стороны.
We have the interface ID and the network prefix side,|У нас есть идентификатор интерфейса и сторона префикса сети,
which we really don't work with.|с которыми мы действительно не работаем.
I mean, I'm sorry, we don't work with the interface ID.|То есть, извините, мы не работаем с идентификатором интерфейса.
Autoconfiguration feature, right?|Функция автоконфигурации, правда?
EUI64, the triple [UNKNOWN] that it does.|EUI64, тройное [НЕИЗВЕСТНО], что он делает.
All right so, we really don't work with that side.|Хорошо, мы действительно не работаем с этой стороной.
We're focused on this side.|Мы сосредоточены на этой стороне.
And really, we are assigned 2001, 4800 and whatever company.|И действительно, нам приписывают 2001, 4800 и любую другую компанию.
So this is the octet that we are interested in.|Итак, это октет, который нас интересует.
Right?|Правильно?
That not oh, I said octet.|Это не ох, я сказал октет.
Bad Laz.|Бад-Лаз.
Bad Laz.|Бад-Лаз.
That's not an octet, that's a section.|Это не октет, это раздел.
Because each one of these sections is 16|Поскольку в каждом из этих разделов по 16
bits.|биты.
Now you do see here that I say first,|Теперь вы видите, что я говорю первым:
second, third, and fourth.|второй, третий и четвертый.
Just to let you know that there is four sections per side,|Просто чтобы вы знали, что на каждой стороне четыре секции,
if you would, all right?|если да, хорошо?
So that's what makes up the 128 bit address.|Вот что составляет 128-битный адрес.
So what do you do?|Ну так что ты делаешь?
When I'm working with this diagram, what I like to do is, I take,|Когда я работаю с этой диаграммой, мне нравится, что я
well you have to do that.|ну, ты должен это сделать.
You take this last section.|Вы берете этот последний раздел.
Remember these are hex numbers.|Помните, что это шестнадцатеричные числа.
Hex numbers.|Шестнадцатеричные числа.
So you need to make sure that this last section,|Поэтому вам нужно убедиться, что этот последний раздел,
you break it up into their binary bits.|вы разбиваете его на двоичные биты.
I know I'm always working in binary, I know that.|Я знаю, что всегда работаю с двоичным кодом, я это знаю.
Okay, so what do I do?|Хорошо, так что мне делать?
I put, now even though I just put everything in binary the way it is,|Я поставил, теперь, хотя я просто поместил все в двоичном формате, как есть,
really I put the zeros.|правда я ставлю нули.
Zeros zeros and zeros.|Нули нули и нули.
So now these zeros though If you look at them,|Итак, теперь эти нули, хотя если вы посмотрите на них,
I call them first position, second position, third position, fourth position.|Я называю их первой позицией, второй позицией, третьей позицией, четвертой позицией.
This last section right here that first number,|Этот последний раздел прямо здесь, первый номер,
that number one that's the first position.|тот номер один, это первая позиция.
Then you have the second position which is the second zero, third zero,|Затем у вас есть вторая позиция, которая является вторым нулем, третьим нулем,
third position and fourth position.|третья позиция и четвертая позиция.
I, Lazaro J Diaz, okay was the one that came up with that naming convention,|Я, Лазаро Дж. Диас, хорошо, был тем, кто придумал это соглашение об именах,
all right, giving them a position so you know where you're at.|хорошо, давая им позицию, чтобы вы знали, где вы находитесь.
Cuz with IPv4 we knew that we're in this bit value,|Потому что с IPv4 мы знали, что находимся в этом битовом значении,
that bit value whatever, here we're in a position.|это битовое значение независимо от того, здесь мы находимся в позиции.
Okay?|Ладно?
And then once you put them in a position and then remember,|А затем, как только вы поставите их в положение, а затем вспомните,
you are given like VLSM or whatever it is.|вам дано как VLSM или как там.
You're given a mask to start off with.|Вам дается маска для начала.
So this is the mask right here.|Вот и маска.
Because you have, what?|Потому что у вас есть что?
16, 16 and 16.|16, 16 и 16.
That's 48.|Это 48.
49, 50, 51, 52.|49, 50, 51, 52.
That's why you see that blue line right here cuz you'll have the 52 right there.|Вот почему вы видите эту синюю линию прямо здесь, потому что у вас есть 52 прямо здесь.
So this diagram is what you need to actually do.|Итак, эта диаграмма - это то, что вам нужно сделать.
You need to make the last, the last,|Тебе нужно сделать последнее, последнее,
section,|раздел,
turn it into four different, into their bit values, right.|превратить его в четыре разных, в их битовые значения, верно.
Four bits, four bits, four bits, and four bits.|Четыре бита, четыре бита, четыре бита и четыре бита.
Give them there hexidecimal values.|Дайте им там шестнадцатеричные значения.
Give them their hexidecimal values.|Дайте им их шестнадцатеричные значения.
And then you'll see that you'll have to start accounting for your subnets, find your increments and all that okay?|И тогда вы увидите, что вам нужно начать учет своих подсетей, найти свои приращения и все такое, хорошо?
But definitely you need to break everything down into that diagram and draw your, your starting point which is whatever the whatever preface they give you, that|Но определенно вам нужно разбить все на эту диаграмму и нарисовать вашу, вашу отправную точку, независимо от того, какое предисловие они вам дают, что
would be your starting point.|будет вашей отправной точкой.
And then remember you're only counting for subnets.|И помните, что вы учитываете только подсети.
Forget about hosts in IPv6.|Забудьте о хостах в IPv6.
You, and I do that confusion all the time okay?|Мы с тобой все время путаемся, хорошо?
You only count for subnets.|Вы учитываете только подсети.
We don't deal with host addresses anymore.|Мы больше не занимаемся адресами хостов.
We only worry about the subnet side of the address.|Мы беспокоимся только о подсети адреса.
Okay, we'll only deal with subnets from now on.|Хорошо, теперь мы будем заниматься только подсетями.
Because remember, either you use the out of configuration, oh my God,|Потому что помните, либо вы используете вне конфигурации, о мой Бог,
you have a quintillion of addresses, zero zero, you know, colon, colon one,|у вас есть квинтиллион адресов, ноль ноль, ну знаете, двоеточие, двоеточие,
colon colon two, colon colon three, colon zero one, colon zero zero.|двоеточие два, двоеточие три, двоеточие ноль один, двоеточие ноль.
Whatever it is that you want to do, you can make up whatever number you want.|Что бы вы ни хотели сделать, вы можете придумать любое число, какое захотите.
You have enough addresses not to, you know,|У вас достаточно адресов, чтобы, знаете ли,
as long as you have some sort of an order so you don't have that duplicate address.|при условии, что у вас есть какой-то заказ, чтобы у вас не было повторяющегося адреса.
Cuz remember ICMPV6, what is it do?|Потому что помните ICMPV6, что он делает?
It sends out a DAD, a duplicate address detection,|Он отправляет DAD, обнаружение повторяющегося адреса,
to see if there's any duplicate address on the network.|чтобы узнать, есть ли в сети повторяющийся адрес.
But anyway, this is the diagram that we're going to be using to actually count for subnets and find the increment, and then layout the subnets that we're going|Но в любом случае это диаграмма, которую мы собираемся использовать для фактического подсчета подсетей и нахождения приращения, а затем компоновки подсетей, которые мы собираемся использовать.
to be using.|использовать.
This is what I do on a daily basis in the classroom, recreate our own subnets.|Это то, что я делаю ежедневно в классе, воссоздаю наши собственные подсети.
All right, and we implement them then in a, in a natural light.|Хорошо, и мы реализуем их тогда в a, при естественном освещении.
See you in the next section.|Увидимся в следующем разделе.