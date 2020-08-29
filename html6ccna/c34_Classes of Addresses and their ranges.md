D:\mailCloud\prjother\tmp\1\c34_Classes of Addresses and their ranges.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
All right.|Отлично.
Welcome back.|Добро пожаловать.
Now that we know what an IPv4 address is,|Теперь, когда мы знаем, что такое IPv4-адрес,
what it looks like,|На что это похоже,
what it's used for, and you saw how we assigned it to an IP an IP address,|для чего он используется, и вы видели, как мы присвоили ему IP-адрес,
we saw how we assigned it to a PC.|мы видели, как закрепили его за ПК.
We need to know what type of IP address we're looking at,|Нам нужно знать, на какой тип IP-адреса мы смотрим,
meaning we need to learn how to classify an IP address.|Это означает, что нам нужно научиться классифицировать IP-адрес.
Okay?|Ладно?
Now, and I get this all the time.|Теперь, и я получаю это все время.
Yes we still use class-full and class-less routing,|Да, мы по-прежнему используем классовую и бесклассовую маршрутизацию,
cuz we're still in IPv4, we're not fully in IPv6 yet.|Потому что мы все еще находимся на IPv4, мы еще не полностью на IPv6.
In IPv6, there are no classes, they're designations of IP addresses,|В IPv6 нет классов, это обозначения IP-адресов,
which we will be talking about later on in the course.|о чем мы поговорим позже в этом курсе.
But since we still use IPv4, you need to understand the classification of an IP address, or an IPv4 address.|Но поскольку мы все еще используем IPv4, вам необходимо понимать классификацию IP-адреса или IPv4-адреса.
The way you classify an IPv4 addresses, is by looking at the first object.|Вы классифицируете IPv4-адреса, глядя на первый объект.
So first, let's put the type of classes that we have.|Итак, сначала давайте укажем тип классов, которые у нас есть.
We have A, B, C, D and E.|У нас есть A, B, C, D и E.
And even though we don't really use the C,|И хотя мы действительно не используем C,
I mean the C and E, but you still need to know their ranges.|Я имею в виду C и E, но вам все равно нужно знать их диапазоны.
And when I say their range, I mean the range within the first octet,|И когда я говорю их диапазон, я имею в виду диапазон в пределах первого октета,
all the way to the left.|полностью налево.
Right?|Правильно?
Those are the four octets.|Это четыре октета.
From left to right, first, second, third,|Слева направо, первый, второй, третий,
and fourth.|и четвертый.
So the range for class A is 1 through 126.|Таким образом, диапазон для класса A составляет от 1 до 126.
What happened to 0?|Что случилось с 0?
0 is a default route.|0 - маршрут по умолчанию.
0 is a reserved IP address, so it's not part of the range.|0 - это зарезервированный IP-адрес, поэтому он не входит в диапазон.
What happened to 127?|Что случилось с 127?
Well, we know that the whole 127 address is reserved for loopback.|Что ж, мы знаем, что весь адрес 127 зарезервирован для обратной связи.
For loopback purposes.|Для целей обратной связи.
So the actual address is 127.0.0.1, but you can ping 127.232.250.1 and you'll still get a reply back from that particular IP address|Таким образом, фактический адрес 127.0.0.1, но вы можете пропинговать 127.232.250.1, и вы все равно получите ответ с этого конкретного IP-адреса.
because it is all reserved for loopbacks.|потому что все это зарезервировано для петель.
So that's why those two are not in the range of a class A, but now since we're on the subject of the loopback, the loopback address.|Вот почему эти два не входят в диапазон класса A, но теперь, когда мы говорим о петле, адрес петли.
Or if you ping the loopback address or you ping loop back, what you're doing is,|Или, если вы пингуетесь по адресу обратной связи или возвращаете петлю, то что вы делаете,
you're testing the TCP/IP stack.|вы тестируете стек TCP / IP.
You're not testing your NIC card.|Вы не тестируете свою сетевую карту.
If you ping your NIC card's IP address,|Если вы пропингуете IP-адрес своей сетевой карты,
then you're testing your NIC card.|затем вы тестируете свою сетевую карту.
And if you ping the loopback, you're testing the protocol suite, okay?|И если вы пингуетесь по петле, вы тестируете набор протоколов, хорошо?
So keep that embedded in your head.|Так что держите это в своей голове.
The next range is for the B.|Следующий диапазон - для B.
We go there, we go for 128 to 191.|Идем туда, идем с 128 на 191.
That's right, no surprises there.|Правильно, никаких сюрпризов.
C, 192 to 223.|С, 192-223.
D, 224 to 239, and let's stop here real quick.|D, с 224 по 239, и давайте быстро остановимся на этом.
Now, maybe I'm getting a little bit ahead of myself cuz we haven't used a default mask or anything like that yet, but the|Теперь, возможно, я забегаю вперед, потому что мы еще не использовали маску по умолчанию или что-то подобное, но
class D range is used for multicasting,|диапазон класса D используется для мультикастинга,
and I'll write that in there in a little bit, all right, is used for multicasting.|и я напишу, что там немного, хорошо, используется для многоадресной рассылки.
Now every example in your books that they give you, let's say oh video conferencing on your group, a range of people can actually participate in|Теперь каждый пример в ваших книгах, который они дают вам, допустим, видеоконференцсвязь в вашей группе, в которой действительно могут участвовать разные люди.
a video conference cuz they have one of these addresses and what have you.|видеоконференция, потому что у них есть один из этих адресов и что у вас есть.
But these addresses, what's more important to you is, in your routers,|Но эти адреса, что для вас более важно, в ваших маршрутизаторах,
your routing protocols and I wanna write this down here.|ваши протоколы маршрутизации, и я хочу записать это здесь.
And I'll put RIP, and put EIGRP and then I'll put OSPF.|И я поставлю RIP, и поставлю EIGRP, а потом я поставлю OSPF.
RIP uses a multipass address of 224.0.0.9.|RIP использует многопроходный адрес 224.0.0.9.
EHRP uses 224.0.0.10.|EHRP использует 224.0.0.10.
OSPF uses 224.|OSPF использует 224.
Oops.|Ой.
.0.0.|.0.0.
5 and 224.0.0.6,|5 и 224.0.0.6,
it uses two different IP addresses.|он использует два разных IP-адреса.
It all depends if it's sending it to a standard router or is it sending it to a designated router or a backup designated router.|Все зависит от того, отправляет ли он его на стандартный маршрутизатор или отправляет его на назначенный маршрутизатор или резервный назначенный маршрутизатор.
Then we'll use the 6.|Затем мы воспользуемся 6.
So if you were to do a debug IP RIP or IP EIGRP or debug OSPF, you would see these updates being sent back and forth and this is a troubleshooting|Таким образом, если вам нужно выполнить отладку IP RIP или IP EIGRP или отладить OSPF, вы увидите, что эти обновления отправляются туда и обратно, и это устранение неполадок.
technique that you would use.|техника, которую вы бы использовали.
If you're not receiving information from a dynamic routing protocol, a network.|Если вы не получаете информацию от протокола динамической маршрутизации, network.
You would go and do a debug IP for whatever running protocol you're using and you would see if you're getting these updates or not.|Вы должны пойти и выполнить отладку IP для любого используемого протокола, и вы увидите, получаете ли вы эти обновления или нет.
You would see these particular multicast addresses that are specifically for these writing protocols.|Вы увидите эти конкретные адреса многоадресной рассылки, которые предназначены специально для этих протоколов записи.
And they also have their version six address which is ff02 and then the 9.|И у них также есть адрес шестой версии: ff02, а затем номер 9.
FF02 and then A for 10 and then FF02 and then the 5 and the 6.|FF02, затем A для 10, затем FF02, а затем 5 и 6.
So anything that starts with an FF in IPv6|Итак, все, что начинается с FF в IPv6
is a multicast address.|это многоадресный адрес.
So, multicast addresses, you will be seeing them because when you're in the router and you're looking to see if updates are being sent back and|Итак, адреса многоадресной рассылки вы будете видеть их, потому что, когда вы находитесь в маршрутизаторе, и вы хотите увидеть, отправляются ли обновления и
forth using the debug command, you will see these addresses.|далее, используя команду отладки, вы увидите эти адреса.
Okay?|Ладно?
So it's important that you know,|Поэтому важно, чтобы вы знали,
these addresses because you will be asked questions on these particular addresses right here.|эти адреса, потому что именно по этим адресам вам будут заданы вопросы прямо здесь.
Follow me on the screen for a little bit.|Следуйте за мной по экрану немного.
And then the last one, which is E is 240|И последний, E - 240
through 255, and that is in the first octet.|через 255, и это в первом октете.
Remember, what we're looking at here,|Помните, на что мы здесь смотрим,
these ranges,|эти диапазоны,
is because we're classifying, we're classifying an IP address to see if it's an A or B, a C, and it's important why?|потому что мы классифицируем, мы классифицируем IP-адрес, чтобы узнать, является ли он A или B или C, и это важно, почему?
Because each one of these has a default mask and a default host.|Потому что у каждого из них есть маска по умолчанию и хост по умолчанию.
The default mask that got a decimal version of it of an A, is 255.0.0.0.|Маска по умолчанию, которая получила десятичную версию буквы A, - 255.0.0.0.
For B, it is 255.255.0.0.|Для B это 255.255.0.0.
For C, it is 255.255.255.0.|Для C это 255.255.255.0.
[NOISE] And for D, it is not applicable because,|[NOISE] А для D это неприменимо, потому что,
since it is a specialized address, it doesn't have a default mask, and E.|поскольку это специализированный адрес, у него нет маски по умолчанию, и E.
I call that one black ops because you're not allowed to use these addresses.|Я называю это темной операцией, потому что вам не разрешено использовать эти адреса.
Even D, if you're to put something other than from A through C, your computer, your router, will scream at you and say hey,|Даже D, если вы поставите что-то другое, кроме от A до C, ваш компьютер, ваш маршрутизатор будет кричать на вас и говорить эй,
outside the normal range of addresses.|вне нормального диапазона адресов.
It will not allow you to do it.|Это не позволит вам этого сделать.
All right, and definitely E, you are not allowed to use that one at all.|Хорошо, и определенно E, вам вообще не разрешено использовать его.
But the first a, b, and c, they have a default member host.|Но первые a, b и c имеют хост-член по умолчанию.
Now I don't expect you to remember the the exact number as long as you know it's millions.|Я не думаю, что вы запомните точное число, если знаете, что оно миллионы.
That's fine.|Это хорошо.
Unless you're taking a certification exam.|Если вы не сдаете сертификационный экзамен.
Like I know with plus, that requires you to know the exact number of addresses.|Как я знаю, с плюсом, это требует, чтобы вы знали точное количество адресов.
That in A holes, it's a good trivia to know.|Что в дырках, это хорошая мелочь.
All right?|Отлично?
B, 65,536.|В, 65 536.
A comma will be nice.|Запятая будет хорошо.
All right, and then 254 for the C.|Хорошо, а затем 254 для C.
So, you need to know this.|Итак, вам нужно это знать.
When you're creating a network and you're decide, well, we want you use a classy address.|Когда вы создаете сеть и решаете, что ж, мы хотим, чтобы вы использовали стильный адрес.
Everybody wants to use a classy C addresses easy to work with.|Все хотят использовать классные адреса C, с которыми легко работать.
It's only in the last octet.|Это только последний октет.
But you don't consider the type of company you're working for, and you run out of IP class C addresses, private class C addresses, that is.|Но вы не учитываете тип компании, в которой работаете, и у вас заканчиваются IP-адреса класса C, то есть частные адреса класса C.
You'll be like, oh-oh, what now?|Вы будете типа, о-о, что теперь?
And I, I saw it.|И я, я это видел.
Not saw it happen, but a, a student of mine who is a consultant,|Не видел, чтобы это произошло, но мой студент, который работает консультантом,
he came to me with this, that particular scenario.|он пришел ко мне с этим конкретным сценарием.
One of the companies that he was working for, the previous person that set up their network didn't take into consideration the|Одна из компаний, на которую он работал, предыдущий человек, создававший их сеть, не принял во внимание
growth,|рост
the exponential growth of that company which was tremendous and they ran out of IPv4 class C IPv4 address.|экспоненциальный рост этой компании, который был огромным, и у них закончились IPv4-адреса класса C IPv4.
Now what?|Что теперь?
Now what?|Что теперь?
So that's why you need to understand when you're creating a network, always leave yourself room to grow.|Вот почему вам нужно понимать, что когда вы создаете сеть, всегда оставляйте себе место для роста.
And in a certification exam is a totally different story.|А на сертификационном экзамене - совсем другая история.
When we're doing subnetting and what have you.|Когда мы делаем подсети и что у вас.
Don't worry about room to grow.|Не беспокойтесь о пространстве для роста.
They ask you a particular question, and you answer it to what they need.|Они задают вам конкретный вопрос, а вы отвечаете на него тем, что им нужно.
But in a real world scenario, most definitely,|Но в реальном мире, безусловно,
you give yourself room to grow.|вы даете себе возможность расти.
I can tell you right now.|Я могу сказать вам прямо сейчас.
The majority of schools that I've been at.|Большинство школ, в которых я учился.
They only use class Bs or class As for their networks, because, you know,|Они используют только классы B или As для своих сетей, потому что, как вы знаете,
you have, hundreds, maybe thousand of students.|у вас есть сотни, может быть, тысячи студентов.
All right?|Отлично?
And the same thing goes for faculty.|То же самое и с преподавателями.
You have hundreds of faculties that are coming around.|У вас есть сотни новых факультетов.
So, you need to make sure.|Итак, вам нужно убедиться.
And you may have different campuses and what have you.|А у вас могут быть разные кампусы и какие есть.
You wanna make sure that you don't run out of IP, especially private IPv4 address.|Вы хотите убедиться, что у вас не закончился IP, особенно частный IPv4-адрес.
All right, so this right here, what we are looking at, we'll in another section we'll talk about the private IP address range|Хорошо, вот что мы смотрим, мы в другом разделе поговорим о диапазоне частных IP-адресов.
because there's a lot to say about that on that particular subject but here, it's just the basics.|потому что по этому поводу можно много сказать, но здесь это только основы.
We are looking at the first octet when we see an IP address.|Мы смотрим на первый октет, когда видим IP-адрес.
And let me go ahead and take this out of the screen so I can write in there.|И позвольте мне вынуть это с экрана, чтобы я мог писать там.
If we look at an IP address and we see that it says, 131.|Если мы посмотрим на IP-адрес и увидим, что он говорит: 131.
[NOISE] Let's see this, okay.|[NOISE] Давай посмотрим, хорошо.
131.1.2.6.|131.1.2.6.
What class of address is that?|Что это за класс адреса?
Well, it falls within the B range in the first octet, so you could use the default mask of a 255.255.0.0.|Что ж, он попадает в диапазон B в первом октете, поэтому вы можете использовать маску по умолчанию 255.255.0.0.
It has the capacity of holding 65,000 plus IP addresses.|Он может содержать более 65 000 IP-адресов.
This is the reason why we need to know that, so when we're creating our networks we know hey, if we're using a class A that means we can have millions|Это причина, по которой нам нужно это знать, поэтому, когда мы создаем наши сети, мы знаем, эй, если мы используем класс A, это означает, что у нас могут быть миллионы
of addresses on our network which we need to subnet appropriately.|адресов в нашей сети, которые нам нужно правильно подсеть.
All right, based on departments or what have you.|Хорошо, исходя из отделов или того, что у вас есть.
But we have the capacity for millions of addresses.|Но у нас есть возможности для миллионов адресов.
That's why we need to know how to classify an IP address,|Вот почему нам нужно знать, как классифицировать IP-адрес,
version 4 by looking at its first octet and knowing their default mask.|версии 4, посмотрев на свой первый октет и зная их маску по умолчанию.
And just to give you a little extra, and it's not really extra.|И просто чтобы дать вам немного больше, и на самом деле это не лишнее.
I'm sure all of you know this.|Я уверен, что все вы это знаете.
CIDR, all right, which is Classless Inter-Domain Routing,|CIDR, хорошо, это бесклассовая междоменная маршрутизация,
the CIDR, that would be [SOUND] 8 slash 8.|CIDR, это будет [ЗВУК] 8 косая черта 8.
Okay, I didn't mean to do that.|Ладно, я не хотел этого делать.
Do, do, do, do, do, slash 8.|Делай, делай, делай, делай, делай, косая черта 8.
Slash 16,|Слэш 16,
[NOISE] [NOISE] and then slash 24.|[NOISE] [NOISE], а затем косая черта 24.
Okay, all that means is that there is 8|Хорошо, все это означает, что есть 8
bits on consecutively from left to right and that's where you get your 255 and the next one you have 16 bits consecutively|биты последовательно слева направо, и именно здесь вы получаете свои 255, а следующий у вас 16 бит последовательно
there on that's why you have your 255, 255|вот почему у вас есть 255, 255
and the last one class C you have 24|и последний класс C у вас 24
bits consec consecutively from left to right 255, 255, 255 and then 0.|биты последовательно слева направо 255, 255, 255 и затем 0.
So now you know when you look at an address,|Итак, теперь вы знаете, когда смотрите на адрес,
what type of address you're looking at.|какой тип адреса вы смотрите.
Now, remember, there are certain addresses that we don't use that are reserved.|Теперь помните, что есть определенные адреса, которые мы не используем, которые зарезервированы.
The ones you need to know about.|Те, о которых вам нужно знать.
The 0, it's a default route.|0 - это маршрут по умолчанию.
The 127.0.0.1, which is your loopback.|127.0.0.1, который является вашей обратной связью.
And the other one, 169.254, and really it could be whatever number back here, is your APIPA.|А другой, 169,254, и на самом деле это может быть любое другое число, это ваш APIPA.
Your automatic private IP address.|Ваш автоматический частный IP-адрес.
Your automatic private IP address.|Ваш автоматический частный IP-адрес.
Right there, your APIPA address.|Вот ваш адрес APIPA.
Let me get out of the way, so you guys can see that.|Позвольте мне уйти с дороги, чтобы вы, ребята, это видели.
Right?|Правильно?
Your default route, your loopback address,|Ваш маршрут по умолчанию, ваш адрес обратной связи,
and your APIPA.|и ваш APIPA.
The APIPA, we know that we get it when we're,|APIPA, мы знаем, что получаем это, когда мы,
let's say we're, we're plugged into a network and we're DACP enabled.|допустим, мы подключены к сети и у нас включен DACP.
We're supposed to be getting an IP address from a DACP server, and when we do an IP config and we see this address, right off the bat you know that,|Предполагается, что мы получаем IP-адрес от сервера DACP, и когда мы делаем IP-конфигурацию и видим этот адрес, вы сразу же знаете, что
okay, something is wrong.|ладно, что-то не так.
We're not getting an IP address, so it, it assigned itself an APIPA address.|Мы не получаем IP-адрес, поэтому он присвоил себе адрес APIPA.
All right, that, that's when we see IPv4,|Хорошо, вот тогда мы видим IPv4,
that's what that means.|вот что это значит.
An automatic private IP address.|Автоматический частный IP-адрес.
Now you could change that within the TCP/IP properties and if you're JCP enabled you will get another tab that would allow you.|Теперь вы можете изменить это в свойствах TCP / IP, и если у вас включен JCP, вы получите другую вкладку, которая позволит вам.
Let me see if cuz I'm not really connected right now.|Дай мне посмотреть, если я сейчас не на связи.
I'm connected to, I'm not really connected to a network, so.|Я подключен, я не совсем подключен к сети, так что.
If I were to be connected to a network,|Если бы я был подключен к сети,
you can go to the properties of your TCP/IP.|вы можете перейти к свойствам вашего TCP / IP.
And if you're DACP enabled, there's there's two tabs.|И если у вас включен DACP, есть две вкладки.
The one to the right will show you advanced settings.|Тот, что справа, покажет вам расширенные настройки.
You go in there.|Иди туда.
And there you will see that by default it chooses to give you an APIPA.|И там вы увидите, что по умолчанию он выбирает APIPA.
But you can put manually configured.|Но можно поставить вручную настроенный.
And you can put, if you're part of another network, if you leave that location.|И вы можете поставить, если вы являетесь частью другой сети, если вы покинете это место.
You can put the information for that particular networks or if you don't get a, because they're statically assigned.|Вы можете поместить информацию для этих конкретных сетей или, если вы не получите, потому что они статически назначены.
So if you don't receive an IP address from this particular location,|Поэтому, если вы не получаете IP-адрес из этого конкретного места,
you don't get enough people, you get what you manually configured.|у вас недостаточно людей, вы получаете то, что настроили вручную.
So you can tweak it to have two sets of networks, all right?|Итак, вы можете настроить его так, чтобы у него было два набора сетей, хорошо?
One on the main screen and one on the tab that allows you to go ahead.|Один на главном экране и один на вкладке, позволяющей продолжить.
One is DHCP enabled because you have to have DHCP enabled in order to get that tab.|Один из них - DHCP включен, потому что у вас должен быть включен DHCP, чтобы получить эту вкладку.
So on one, you go, you go to your main job, let's say.|Итак, на первом этапе вы идете, вы идете, скажем, на свою основную работу.
You're DACP enabled.|У вас включен DACP.
Burp.|Отрыжка.
You get your IP address, what have you.|Вы получаете свой IP-адрес, что у вас есть.
And in your, in your, let's say your house.|И в вашем, в вашем, скажем, вашем доме.
You have wireless, and then you're not DACP enabled or everything's static because of security purposes.|У вас есть беспроводная связь, но вы не включили DACP или все статично из соображений безопасности.
You manually configure your settings and then you're still a part of a network and you won't be left out.|Вы вручную настраиваете свои параметры, и тогда вы по-прежнему являетесь частью сети, и вы не останетесь в стороне.
So you can do many things to help out but know that these, and by no means are these all the addresses that are reserved.|Таким образом, вы можете сделать многое, чтобы помочь, но знайте, что это, а ни в коем случае не все адреса, которые зарезервированы.
These are the main three that you need to remember.|Это основные три, которые вам нужно запомнить.
Okay.|Ладно.
For let's say, you know, classification or questions that they may arise on, hey,|Например, классификация или вопросы, по которым они могут возникнуть, эй,
what's an APIPA or what have you?|что такое APIPA или что у вас?
That folder though, asks you about the people possibly as far as these two addresses right here, the default route and the loop back.|Однако эта папка спрашивает вас о людях, возможно, до этих двух адресов прямо здесь, маршрута по умолчанию и обратной петли.
For sure they may ask questions to you on those two types of addresses.|Конечно, они могут задать вам вопросы по этим двум типам адресов.
All right?|Отлично?
We'll be creating default routes, so you'll see that address and definitely you already know what the loopback is.|Мы будем создавать маршруты по умолчанию, поэтому вы увидите этот адрес и определенно уже знаете, что такое петля.
So there you go.|Итак, поехали.
Those are your classes of IP addresses.|Это ваши классы IP-адресов.
Their range within the first octet, their default mask and dotted decimal and CIDR notation.|Их диапазон в первом октете, их маска по умолчанию, десятичная дробь с точками и нотация CIDR.
And the default number of hosts.|И количество хостов по умолчанию.
All right, ladies and gentlemen, that's it for this session.|Хорошо, дамы и господа, на этом сеанс закончился.
I will see you in the next one.|Увидимся в следующем.
[BLANK_AUDIO]|[BLANK_AUDIO]