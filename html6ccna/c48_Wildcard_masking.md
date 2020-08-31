D:\mailCloud\prjother\tmp\1\c48_Wildcard masking.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
All right, welcome back everybody!|Хорошо, с возвращением всех!
Now, we've done all the subnetting, all the summarization, class less,|Итак, мы сделали все подсети, все суммирование, без класса,
class full, now comes time to do the final lesson, which is wildcard masking.|class full, теперь пришло время сделать последний урок - маскировку подстановочных знаков.
Now, a lot of people have problems with wildcard masking and it really is not as difficult as it seems.|Сейчас у многих людей возникают проблемы с маскировкой подстановочных знаков, и это действительно не так сложно, как кажется.
And I want to show you.|И я хочу вам показать.
You've been doing wildcard masking all along.|Вы все время использовали подстановочную маску.
I showed you early on in the course when we did the diagram that once you do your line, your broadcast calculation number is your wildcard mask.|Я показал вам на раннем этапе курса, когда мы сделали диаграмму, что после того, как вы сделаете свою строку, ваш расчетный номер широковещательной передачи будет вашей маской подстановки.
But we'll get back into that, and you'll see that, and I'll show you now a different way of doing it.|Но мы вернемся к этому, и вы увидите это, и я покажу вам другой способ сделать это.
Now when you see, you can say, are you serious?|Теперь, когда вы видите, вы можете сказать, вы серьезно?
Is that it?|Это оно?
That is it.|Вот и все.
And now when I actually show you how you would use these wildcard masks,|А теперь, когда я на самом деле покажу вам, как использовать эти маски,
where would you use these wildcard masks,|где бы вы использовали эти маски,
okay?|Ладно?
So let's go ahead and get started.|Итак, давайте приступим.
The first way that we're gonna do it is by using a constant number which is 255.255.255.255.|Первый способ сделать это - использовать постоянное число 255.255.255.255.
Right?|Правильно?
And then I'm going to subtract whatever mask I'm using.|А потом я вычту любую маску, которую использую.
So if I'm using a 255.255.255.252 which is a mask that we normally use between routers.|Итак, если я использую 255.255.255.252, это маска, которую мы обычно используем между маршрутизаторами.
We subtract that from that constant number and what do we get?|Мы вычитаем это из постоянного числа и что получаем?
0 0 0 3.|0 0 0 3.
There's your wildcard mask.|Вот ваша маска с подстановочными знаками.
0's mean match exactly, so you're gonna match exactly to the first three octets and then any number that falls in that range.|0 означает точное точное совпадение, поэтому вы будете точно соответствовать первым трем октетам, а затем любому числу, попадающему в этот диапазон.
Because remember the IP address is already set on the interface and the mask.|Потому что помните, что IP-адрес уже установлен на интерфейсе и маске.
So when you put in a wildcard mask because, let's say, you're advertising it,|Итак, когда вы добавляете подстановочную маску, скажем, рекламируете ее,
it's gonna know the range of IPs that it's looking for.|он будет знать диапазон IP-адресов, которые он ищет.
All right?|Отлично?
So that is how you get the wildcard mask.|Вот как вы получаете маску подстановки.
But let's make another example.|Но приведем другой пример.
Let's make another example let's use this right here.|Давайте сделаем еще один пример, давайте воспользуемся этим прямо здесь.
Let's use a 240.|Давайте использовать 240.
So if you subtract that what do you got?|Итак, если вычесть это, что у вас есть?
15.|15.
There's your wildcard mask.|Вот ваша маска с подстановочными знаками.
And let's use a different example let's use 224.|И давайте использовать другой пример, давайте использовать 224.
What do you have?|Что у тебя есть?
31.|31.
Now, very simple, right?|Теперь очень просто, правда?
We're in the last octet.|Мы на последнем октете.
Come on Laz, you're in the last octet.|Давай, Лаз, ты в последнем октете.
Let's move it around, let's change it up a bit.|Давайте переместим его, давайте немного изменим.
Right?|Правильно?
Let's do that.|Давайте сделаем это.
Okay?|Ладно?
So let's go ahead and go to the third octet, let's get dangerous, right,|Итак, давайте перейдем к третьему октету, давайте опасно, верно,
and let's do a 192 subnet mask.|и давайте сделаем маску подсети 192.
Uh-oh!|Ой-ой!
Now we're really getting, we got, we're really getting dangerous with a 192.|Теперь мы действительно получаем, мы действительно становимся опасными с 192.
What is the increment there?|Какой там прирост?
64, one less 63, we subtract there that's what you get 63, right?|64, на один меньше 63, мы вычитаем вот что получается 63, верно?
So, 63.255, there is your wildcard mask.|Итак, 63.255, это ваша маска с подстановочными знаками.
It doesn't matter what octet you're in.|Неважно, в каком октете вы находитесь.
You have a constant number and then you subtract from your mask that you're using.|У вас есть постоянное число, а затем вы вычитаете из маски, которую используете.
That's it.|Вот и все.
If you were to [UNKNOWN], I'll give you one, one last example using this.|Если бы вы были [НЕИЗВЕСТНО], я дам вам один, последний пример, использующий это.
The masked that we normally also are very accustomed to,|В масках, к которым мы обычно тоже очень привыкли,
the CIDR 24 map, well then there you go.|карта CIDR 24, ну что ж, поехали.
That's it right there.|Вот и все.
That's as hard as it gets.|Это настолько сложно, насколько это возможно.
But you've been doing it all ready, you been doing it all ready and because you've been doing the diagram.|Но вы делали все готово, вы делали все готово и потому, что вы делали диаграмму.
So let's use that same examples that we used above for the diagram.|Итак, давайте использовать те же примеры, которые мы использовали выше для диаграммы.
Let's go x.x.x.1111|0000.|Поехали x.x.x.1111 | 0000.
That's a 240 mask, because I know you know that,|Это маска 240, потому что я знаю, что ты это знаешь,
because you've already memorized your bit to decimal table.|потому что вы уже запомнили свой бит в десятичной таблице.
Four bits on, that's 240.|Включены четыре бита, это 240.
So what is the incrementation right here?|Так что же здесь за приращение?
That's 32.|Это 32.
So that means that this guy right here, if you add all these up it's 31,|Это означает, что этот парень прямо здесь, если сложить все это, это 31 год,
I mean I'm sorry, it's 16.|Я имею ввиду, что мне очень жаль, это 16.
My apologies.|Мои извинения.
This is 16.|Это 16.
If you add all these guys right there,|Если вы добавите всех этих ребят прямо здесь,
that is, 15.|то есть 15.
So your wildcard mask the x's.|Итак, ваш подстановочный знак маскирует x.
You match, and then, in the last octet,|Вы сопоставляете, а затем в последнем октете
you have 15.|у вас 15.
And, let's say in the second octet, x.x.x.|И, скажем, во втором октете x.x.x.
No, in the third octet, I'm sorry.|Нет, извините, в третьем октете.
And, let's say 1, 2, 3.|И, скажем, 1, 2, 3.
One, two, three, four, five.|Раз, два, три, четыре, пять.
One, two, three, four, five, six, seven,|Один два три четыре пять шесть семь,
eight.|восемь.
So x's match.|Итак, совпадение x.
Then three bits in, that means you're incrementing by 32.|Затем вводятся три бита, это означает, что вы увеличиваете на 32.
So that means that these boys right here,|Значит, эти мальчики прямо здесь,
they add up to 31 and, and when we're talking about what are we adding, we're adding bit values.|они в сумме составляют 31 и, когда мы говорим о том, что мы добавляем, мы добавляем битовые значения.
We're adding bit values that are on top.|Мы добавляем битовые значения сверху.
One, two, four, six, eight, 16, and so forth.|Один, два, четыре, шесть, восемь, 16 и так далее.
Okay, and then we add these bit values here, that comes out to 255.|Хорошо, а затем мы добавляем эти битовые значения сюда, и получается 255.
There you go, that's it, and remember.|Вот и все, и запомните.
This is geared to our certification exam.|Это связано с нашим сертификационным экзаменом.
Okay?|Ладно?
Geared to a certification exam, so this is as hard as it gets to calculate the wildcard mask.|Приспособлен к сертификационному экзамену, поэтому вычислить маску подстановки очень сложно.
Now, where in the world do you use a wildcard mask?|Итак, где в мире вы используете подстановочную маску?
Very easy, and this is how they're gonna hide ip address in question.|Очень просто, и вот как они собираются скрыть рассматриваемый IP-адрес.
So let's move this up to the top a little bit,|Итак, давайте немного переместим это наверх,
it gives us a little bit more room to write.|это дает нам немного больше места для написания.
So let's go ahead and do an access list.|Итак, давайте сделаем список доступа.
ACCESS-LIST.|ДОСТУП-СПИСОК.
Right, and we'll do a standard access list.|Хорошо, а мы сделаем стандартный список доступа.
And we're going to deny, let's deny a network.|И мы будем отрицать, давайте откажемся от сети.
192.168.1.0.|192.168.1.0.
We're using a sider 24, a slash 24, a default class C mask.|Мы используем sider 24, косую черту 24, маску класса C по умолчанию.
So we go 0.0.0.|Итак, мы идем 0.0.0.
We want to block the entire network.|Мы хотим заблокировать всю сеть.
There you go.|Вот так.
There's your wildcard mask, by doing the message that I showed you on top.|Вот ваша маска с подстановочными знаками, выполняя сообщение, которое я вам показал сверху.
255 255 255, you know, the constant number?|255 255 255, вы знаете, постоянное число?
And then the master we're using, which is a 24 and we get a 255.|И затем мастер, который мы используем, это 24, и мы получаем 255.
That means, that we're going to match the first to three octets and then whatever number comes after that it will be blocked|Это означает, что мы собираемся сопоставить первые три октета, а затем любое число, которое появится после этого, будет заблокировано.
within that range of 1 through to 254.|в пределах этого диапазона от 1 до 254.
Because remember, the IPs and the mask are sitting on the interface.|Помните, что IP-адреса и маска находятся в интерфейсе.
The mask as I said.|Маска, как я уже сказал.
Now the same thing goes for if you wanna do a host let's say,|То же самое происходит, если вы хотите сделать хост, скажем,
ACCESS-LIST.|ДОСТУП-СПИСОК.
Oh.|Ой.
Typing all sorts of letters.|Печатать всевозможные буквы.
ACCESS-LIST 10.|СПИСОК ДОСТУПА 10.
Deny let's say 10.1.1.1,|Запретить, скажем, 10.1.1.1,
an actual IP address, 0.0.0.0.|фактический IP-адрес 0.0.0.0.
Yeah, cuz each 0 means match exactly what's on that octet, so I am denying each and every, or matching each and every octet but it's a deny.|Да, потому что каждый 0 означает точное совпадение с тем, что находится в этом октете, поэтому я отрицаю каждый октет или сопоставляю каждый октет, но это отрицание.
So whatever it matches up with that IP,|Итак, что бы он ни совпадал с этим IP,
that one will be denied.|этому будет отказано.
So you can use an actual all 0's to match exactly each and every octet, okay?|Итак, вы можете использовать фактические все 0 для точного соответствия каждому октету, хорошо?
So you can use a combination of wildcard masks with access lists,|Таким образом, вы можете использовать комбинацию подстановочных масок со списками доступа,
because this access list, really, if you look at it,|потому что этот список доступа, на самом деле, если вы посмотрите на него,
which you will, when we get to that particular part in the course.|что вы и сделаете, когда мы перейдем к этой конкретной части курса.
It's the same thing if you were saying deny host 192 dot no, 10.1.1.1.|То же самое, если бы вы говорили deny host 192 dot no, 10.1.1.1.
It's the same thing, but using a wildcard mask to use it.|Это то же самое, но с использованием маски подстановки.
So you're saying the same thing but using a wildcard mask.|Итак, вы говорите то же самое, но используете подстановочную маску.
Now the other way, the other way that you can use an access list is when you're advertising a route using OSPF.|С другой стороны, еще один способ использования списка доступа - это объявление маршрута с помощью OSPF.
That is the only time and I'm going to clarify this now before actually do it.|Это единственный раз, и я собираюсь прояснить это сейчас, прежде чем это делать.
When you're using RIP version 2 and EIGRP for your certification exam, the CCNA 200-120,|Когда вы используете RIP версии 2 и EIGRP для своего сертификационного экзамена, CCNA 200-120,
you will advertise the classful boundaries of the address.|вы будете рекламировать классные границы адреса.
You will not use wildcard masks in EIGRP,|Вы не будете использовать маски подстановки в EIGRP,
what you're required to do is advertise the class full boundary, okay?|что вам нужно сделать, это объявить полную границу класса, хорошо?
Because I've seen problems with that before,|Потому что я видел проблемы с этим раньше,
the only time you use wildcard masks is,|единственный раз, когда вы используете маски с подстановочными знаками,
with a routing protocol,|с протоколом маршрутизации,
it is when you're using OSPF, again, for the CCNA certification.|это когда вы снова используете OSPF для сертификации CCNA.
So, let's go ahead and do an OSPF statement.|Итак, давайте продолжим и сделаем заявление OSPF.
ROUTER OSPF 1, which is the process ID number,|МАРШРУТИЗАТОР OSPF 1, который является идентификационным номером процесса,
and we'll learn all about that later on.|и мы узнаем об этом позже.
NETWORK, I'm going to advertise the network 192.168.1.0.|СЕТЬ, я собираюсь анонсировать сеть 192.168.1.0.
Wildcard mask 0.0.0.255.|Маска подстановки 0.0.0.255.
And then the AREA, 0 let's say.|И затем ОБЛАСТЬ, скажем, 0.
All right.|Отлично.
And then we're going to advertise the next network.|А потом мы будем рекламировать следующую сеть.
NETWORK 10.1.1.4.|СЕТЬ 10.1.1.4.
0.0.0.3 because it's a 252 mask at the end.|0.0.0.3, потому что это маска 252 в конце.
AREA 0.|ПЛОЩАДЬ 0.
And network, let's say at the other side would be 10.1.1.8.|А сеть, скажем, на другой стороне, будет 10.1.1.8.
Same wildcard mask.|Та же маска подстановки.
Cuz using a 252 AREA 0 and then one of the things that you will be doing in OSPF is creating loop back interfaces.|Потому что вы используете 252 ОБЛАСТЬ 0, а затем одна из вещей, которые вы будете делать в OSPF, - это создание интерфейсов обратной связи.
And we'll, we'll learn all of that once we get there so don't worry network.|И мы, мы узнаем все это, как только мы туда доберемся, так что не беспокойтесь о сети.
Now, what I like to use for loop back addresses is what's called the host address.|Теперь, что мне нравится использовать для адресов обратной связи, так это то, что называется адресом хоста.
So I'll use a 1.1.1.1 and then, I want to match that exactly.|Так что я буду использовать 1.1.1.1, а затем я хочу точно соответствовать этому.
So therefore 0.0.0.0 AREA 0.|Таким образом, 0.0.0.0 ОБЛАСТЬ 0.
So you see, they, this is where you will use wildcard masking.|Итак, вы видите, они, именно здесь вы будете использовать маскировку с использованием подстановочных знаков.
It's not hard to calculate, as you saw here above,|Нетрудно подсчитать, как вы видели здесь выше,
very, very simple to calculate, but this is where they hide IP addressing questions.|очень и очень просто вычислить, но именно здесь они скрывают вопросы IP-адресации.
Especially when it comes to this gentleman right here,|Особенно когда речь идет об этом джентльмене прямо здесь,
OSPF cuz you may get a question that states, based on,|OSPF, потому что вы можете получить вопрос, в котором говорится:
let's say this above network statement 192.168.1.0, well that's kinda easy.|скажем, этот сетевой оператор 192.168.1.0, что ж, это довольно просто.
Let's say this second network statement,|Скажем, это второе сетевое утверждение,
10.1.1.4.0.0.0.3 what are they, the IPs that follow them at range?|10.1.1.4.0.0.0.3 что это такое, IP-адреса, следующие за ними на расстоянии?
Well it, it would be five and six.|Ну, было бы пять и шесть.
That would be the range.|Это будет диапазон.
Because this is your broadcast calc,|Поскольку это ваша трансляция,
right?|право?
What's 3 and 4?|Что 3 и 4?
7.|7.
What's in between 7 and 4?|Что между 7 и 4?
5 and 6.|5 и 6.
There you go.|Вот так.
That's how simple this is.|Вот как это просто.
So embrace the wildcard mask, embrace learning how to do all these things,|Так что примите маску подстановки, научитесь делать все эти вещи,
because you already know everything about IPv4.|потому что вы уже все знаете об IPv4.
Now it comes time to subnet and IPv6.|Теперь пришло время подсети и IPv6.
So be ready for that.|Так что будьте к этому готовы.
[BLANK_AUDIO]|[BLANK_AUDIO]