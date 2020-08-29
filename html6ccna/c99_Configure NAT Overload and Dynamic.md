D:\mailCloud\prjother\tmp\1\c99_Configure NAT Overload and Dynamic.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
All right, ladies and gents.|Хорошо, дамы и господа.
It's time to configure Nat overload.|Пришло время настроить перегруз Нат.
First of all, let's use the lab as an example.|Прежде всего, давайте возьмем лабораторную работу в качестве примера.
It's way down here.|Здесь очень далеко.
We'll need to change that and put it way up there, so I don't have to come all the way down here, and let's select all of this right here,|Нам нужно будет это изменить и поставить наверху, чтобы мне не приходилось проходить здесь весь путь, и давайте выберем все это прямо здесь,
bring it to the top, okay, [INAUDIBLE],|выведите его наверх, хорошо, [НЕРАЗБОРЧИВО],
okay.|Ладно.
[INAUDIBLE]|[НЕДОСТАТОЧНО]
Right there, cool.|Прямо там, круто.
Oh.|Ой.
[BLANK_AUDIO]|[BLANK_AUDIO]
All right.|Отлично.
All right.|Отлично.
So Nat overload.|Итак, Нэт перегрузка.
This is the most popular one because you have one public address with 65,000.|Это самый популярный, потому что у вас есть один публичный адрес с 65000.
Right?|Правильно?
So the first thing that I tell my students to do is you need to tell the Nat router, which is your inside and which is your outside.|Итак, первое, что я говорю своим ученикам, - это указать маршрутизатору Nat, что находится внутри вас, а какое снаружи.
Your inside, obviously, is your source,|Ваша внутренность, очевидно, ваш источник,
your private addresses.|ваши личные адреса.
Your outside are your public addresses.|Ваш внешний вид - это ваши публичные адреса.
You can't get them backwards.|Вы не можете вернуть их назад.
If you get them backwards, it's not gonna work.|Если вы перевернете их, это не сработает.
It won't translate, all right?|Не переводится, понятно?
So you gotta make sure that, and the way that they test you is through print screens.|Так что вы должны убедиться в этом, и они проверяют вас с помощью экранов печати.
I've only had a couple of individuals in the old exam, and really if I say a couple, I think I'm exaggerating, that actually had to finish|У меня было всего несколько человек на старом экзамене, и если я скажу пару, я думаю, что я преувеличиваю, они действительно должны были сдать
a dynamic Nat configuration.|динамическая конфигурация Nat.
Okay?|Ладно?
But other than that, it's just pretty much print screens.|Но в остальном это просто экраны для печати.
Why isn't it translating?|Почему не переводится?
And we'll discuss that in another lesson.|И мы обсудим это в другом уроке.
All right, so what you do is,|Хорошо, так что ты делаешь,
the first thing you should do is you would look right, to see if this is there.|Первое, что вам нужно сделать, это посмотреть прямо, чтобы увидеть, есть ли это.
But let's say you have to configure it from scratch.|Но допустим, вам нужно настроить его с нуля.
The first thing is go inside the interface.|Первым делом зайдите внутрь интерфейса.
I'm gonna go inside this interface right here, the add zero zero, and I'm gonna say ip nat inside.|Я собираюсь войти в этот интерфейс прямо здесь, добавить ноль ноль, и я скажу внутри ip nat.
That let's, and I'll put it in parentheses here,|Это давайте, и я заключу это здесь в скобки,
that this is the f0/0 just so you know that it's this interface.|что это f0 / 0, чтобы вы знали, что это интерфейс.
So I need to tell that interface, plus putting its IP address and all that, but I need to tell that interface that, hey,|Поэтому мне нужно указать этот интерфейс, а также указать его IP-адрес и все такое, но мне нужно сообщить этому интерфейсу, что, эй,
you're the inside for the nat.|ты внутри нац.
All right?|Отлично?
Nat needs to know that.|Нат должен это знать.
On the other one, you put ip nat outside.|На другом ставишь ip нат снаружи.
That lets nat know hey, okay, oh, this is the public side of the router.|Это дает знать, что это публичная сторона маршрутизатора.
So first, that's first things first.|Итак, во-первых, это по порядку.
You gotta do that.|Ты должен это сделать.
After you do that, then let's create the pool of one address.|После этого давайте создадим пул из одного адреса.
So we're gonna go and say ip nat pool.|Итак, мы пойдем и скажем ip nat pool.
We'll call it laz.|Назовем это лазом.
And then we'll say, 1.1.1.1.|И тогда мы скажем: 1.1.1.1.
Well, this will be 254.|Ну это будет 254.
And then 1.1.1.1.254.|А потом 1.1.1.1.254.
Net mask.|Сетевая маска.
And it's 255.255.255.0.|И это 255.255.255.0.
Now, questions that I usually get asked.|Теперь вопросы, которые мне обычно задают.
Laz, why do we have to type the same IP address twice?|Лаз, почему мы должны вводить один и тот же IP-адрес дважды?
Because it's a pool.|Потому что это бассейн.
It's a pool of one address.|Это пул из одного адреса.
The programmer before, it was used to, you know, before, I guess, it was first,|Программист раньше, вы знаете, раньше, я думаю, это был первый,
you know, you had an actual pool.|вы знаете, у вас был настоящий бассейн.
Well, they didn't wanna take that slot out, I guess, in the programming.|Ну, я думаю, они не хотели убирать этот слот при программировании.
So you create a pool of one addresses.|Итак, вы создаете пул из одних адресов.
That's the way it is.|Так оно и есть.
That's what you gotta do, okay?|Это то, что ты должен делать, хорошо?
Then, you write the access list to permit the networks that you want to allow through your nat.|Затем вы пишете список доступа, чтобы разрешить сети, которые вы хотите разрешить через свой nat.
So in this case we got the 192.168.1.0|Итак, в этом случае мы получили 192.168.1.0
network and it's a standard access list.|сеть, и это стандартный список доступа.
So you go access, list, permit, oh, I'm sorry, the number 1.|Итак, вы заходите, перечисляете, разрешаете, о, извините, номер 1.
Permit 192.168.1.0,|Разрешение 192.168.1.0,
0.00, 255.|0,00, 255.
You should be familiar with that, we've done access lists already.|Вы должны быть знакомы с этим, мы уже сделали списки доступа.
So we're permitting that network,|Итак, мы разрешаем эту сеть,
now we're not applying this access list to anything.|теперь мы ни к чему не применяем этот список доступа.
This is, access list is really just listening for interesting traffic,|То есть список доступа действительно просто прослушивает интересный трафик,
quote, unquote.|цитата, отменить цитату.
Now how does that know?|Откуда это знать?
Cuz the the third line is actually gonna bring these two lines together.|Потому что третья строка на самом деле объединяет эти две строки.
The last line is ip nat inside source list.|Последняя строка - ip nat внутри списка источников.
What list?|Какой список?
List one.|Список один.
Pool, what pool?|Бассейн, какой бассейн?
Laz.|Лаз.
And then the magical word overload.|А потом волшебное слово «перегрузка».
And then this is nat overload.|А то это нац перегруз.
Okay?|Ладно?
Let me see if I can bring it a little bit further to the top.|Дай мне посмотреть, смогу ли я поднять его немного дальше на вершину.
Okay, so you can see it a little better.|Хорошо, так что вы можете увидеть это немного лучше.
All right?|Отлично?
So you create your pool,|Итак, вы создаете свой бассейн,
you give it a name.|вы даете ему имя.
You put the range of IP addresses which is usually, just one address.|Вы указываете диапазон IP-адресов, который обычно составляет всего один адрес.
And then you can put the net mask.|А потом можно надеть сетчатую маску.
Now I've seen where they use the interface, the exit interface.|Теперь я видел, где они используют интерфейс, интерфейс выхода.
They'll put interface and then the exit interface so it can be either, or.|Они поместят интерфейс, а затем интерфейс выхода, так что это может быть либо, либо.
Usually it's netmask and then the mask that your ISP gave you.|Обычно это сетевая маска, а затем маска, которую вам дал ваш провайдер.
Then you put your access list, standard access list, whatever number it is.|Затем вы помещаете свой список доступа, стандартный список доступа, какой бы номер он ни был.
Permit the network that you're allowing to go through the net.|Разрешите сети, которой вы разрешаете выходить в сеть.
And then you put your IP nat inside source list.|И затем вы помещаете свой IP-адрес в список источников.
Bring these two lines together.|Соедините эти две строки вместе.
You point to the correct list, you point to the correct pool, and then our magical word overlord that allows 65,000|Вы указываете на правильный список, вы указываете на правильный пул, а затем на наш волшебный повелитель слова, который позволяет 65000
plus addresses to go through one public address.|плюс адреса для прохождения одного публичного адреса.
Now.|Сейчас.
How do we turn that, what's the difference between this and dynamic nat?|Как нам это повернуть, в чем разница между этим и динамическим нац?
Let me show you.|Позволь мне показать тебе.
[BLANK_AUDIO]|[BLANK_AUDIO]
There is no overload command.|Команды перегрузки нет.
And this would actually be.|И это действительно было бы.
[BLANK_AUDIO]|[BLANK_AUDIO]
A range, one through 254.|Диапазон от 1 до 254.
It would actually be a range, let's put,|На самом деле это будет диапазон, допустим,
let's put 200.|ставим 200.
Let's not exaggerate here.|Не будем здесь преувеличивать.
That's the difference between nat overload and dynamic nat.|В этом разница между nat overload и dynamic nat.
Where you actually have a real range down here in dynamic nat.|Там, где у вас действительно есть реальный диапазон здесь в динамическом физ.
Where in, nat overload, you only have one IP address.|Где, nat overload, у вас только один IP-адрес.
And obviously, you have the overload command, where here you do not.|И, очевидно, у вас есть команда перегрузки, а здесь ее нет.
You do not.|Ты не делай.
So definitely, this, I mean, it's the same exact thing.|Так что определенно, это то же самое.
Just one uses a real range.|Только один использует реальный диапазон.
One doesn't.|Один не делает.
And then one has overload and the other one does not.|И то у одного есть перегрузка, а у другого нет.
Okay, that is the difference between dynamic nat, or nat overload and dynamic nat.|Хорошо, в этом разница между динамическим натом или перегрузкой нат и динамическим нат.
Very simple configurations.|Очень простые конфигурации.
But again don't forget, first thing you do, you make sure you tell your interfaces, your interfaces, which is the inside, which is the outside.|Но опять же не забывайте, первое, что вы делаете, вы должны сказать своим интерфейсам, вашим интерфейсам, что находится внутри, а что снаружи.
And then you go into your pool creation,|А затем вы переходите к созданию своего пула,
your access list, and then your actual,|ваш список доступа, а затем ваш фактический,
last line telling it what access list and what pool to look at.|последняя строка сообщает ему, какой список доступа и какой пул смотреть.
And that's it, and you're done.|Вот и все, готово.
These are your configurations.|Это ваши конфигурации.
And we'll be putting these configurations when?|И когда мы будем ставить эти конфигурации?
In the next lesson, so you can see.|В следующем уроке, чтобы вы могли убедиться.
Cuz then we'll start talking about a couple of things you need to watch out for.|Потому что тогда мы начнем говорить о паре вещей, которых вам нужно остерегаться.
I'll see you then.|Увидимся тогда.
[BLANK_AUDIO]|[BLANK_AUDIO]