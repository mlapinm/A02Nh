D:\mailCloud\prjother\tmp\1\c75_OSPF Terminology.md  


__|__
--|--
Welcome everyone,|Добро пожаловать,
I wanna welcome you to the final frontier of the routing protocols, the OSPF.|Я хочу поприветствовать вас на последнем рубеже протоколов маршрутизации - OSPF.
Now OSPF was introduced a while back ago.|Теперь OSPF был представлен некоторое время назад.
As a matter of fact,|Собственно говоря,
when I took my first CCNA, or my CCNA, well it will be my first CCNA because you renamed our [INAUDIBLE].|когда я взял свой первый CCNA, или мой CCNA, ну, это будет мой первый CCNA, потому что вы переименовали наш [INAUDIBLE].
But anyway, the first time I took the CCNA that was my routing protocol that I had to configure, was OSPF.|Но в любом случае, когда я впервые использовал CCNA, который был моим протоколом маршрутизации, который мне нужно было настроить, был OSPF.
OSPF is a very large protocol,|OSPF - это очень большой протокол,
we talked about in the previous section.|мы говорили в предыдущем разделе.
I actually dedicated a section just to OSPF because of its immense size.|На самом деле я посвятил раздел только OSPF из-за его огромного размера.
Now, I will point out the things that you need to know for your certification.|Теперь я выделю то, что вам нужно знать для получения сертификата.
I will tell you, hey, this is good to know information when you get out there,|Я скажу вам, эй, это полезно знать информацию, когда вы выйдете оттуда,
when you take another certification.|когда вы берете еще один сертификат.
So let's say CCMP, if you're going to go that route, you need to know these things.|Итак, скажем, CCMP, если вы собираетесь пойти по этому пути, вам нужно знать эти вещи.
And when you're out there,|И когда ты там,
you will be configuring the things that I'll be telling you about.|вы будете настраивать то, о чем я вам расскажу.
It's a huge routing protocol.|Это огромный протокол маршрутизации.
It's a huge routing protocol.|Это огромный протокол маршрутизации.
Now we said it was a link state routing protocol, which means it's,|Мы сказали, что это протокол маршрутизации состояния канала, что означает,
really, there is no limitations on OSPF.|на самом деле ограничений на OSPF нет.
There's no limitations on OSPF,|Для OSPF нет ограничений,
except for areas.|кроме областей.
And we'll get into the terminology in a little bit.|И мы немного углубимся в терминологию.
We just want to do a little comparison first, as you can see back here,|Мы просто хотим сначала провести небольшое сравнение, как вы можете видеть здесь,
I don't know if you can or not.|Не знаю, сможешь ты или нет.
We'll do a little bit of co a little comparison between OSPF and RIP.|Мы сделаем небольшое сравнение между OSPF и RIP.
Why RIP, why not EIGRP?|Почему RIP, а не EIGRP?
Well, remember, OSPF and RIP are open standard, they can go across different vendors, different manufacturers,|Помните, OSPF и RIP - это открытый стандарт, они могут использоваться разными поставщиками, разными производителями,
where EIGRP is purely for Cisco.|где EIGRP предназначен исключительно для Cisco.
So I usually like compare OSPF to RIP.|Поэтому мне обычно нравится сравнивать OSPF с RIP.
It's not fair, really.|На самом деле это нечестно.
Poor little RIP is being beat up,|Бедный маленький РИП бьют,
cuz OSPF will be a bully, I guess,|Потому что OSPF будет хулиганом, я думаю,
if you compare it to RIP, on just the immense size, and things that it can do.|если вы сравните его с RIP, просто по огромному размеру и возможностям.
It's a link state ready protocol,|Это протокол готовности канала,
it does create many different things.|он действительно создает много разных вещей.
We talked about it a little bit previous,|Мы говорили об этом немного раньше,
in the previous section.|в предыдущем разделе.
Neighbor tablesm creates apology tables,|Neighbor tablesm создает таблицы извинений,
creates routing tables, all right?|создает таблицы маршрутизации, хорошо?
Has its own algorithm, just like every routing protocol, called the Dijkstra.|Имеет собственный алгоритм, как и каждый протокол маршрутизации, называемый Dijkstra.
Don't ask me to spell it,|Не проси меня произносить это по буквам,
you'll see it here when we start actually,|вы увидите это здесь, когда мы начнем,
when I typed up all these different notes for you.|когда я напечатал для вас все эти разные заметки.
All right, all these things here,|Хорошо, все эти вещи здесь,
I always misspell it.|Я всегда ошибаюсь в написании.
I can't, never, for the life of me spell Dijkstra, okay?|Я не могу, никогда, хоть убей, заклинать Дейкстра, хорошо?
So that is the routing,|Итак, это маршрутизация,
that is the algorithm.|это алгоритм.
Now that algorithm is pretty much linked up or is used,|Теперь этот алгоритм в значительной степени связан или используется,
it uses the topology table a lot to make that shortest path first calculation.|он часто использует таблицу топологии, чтобы сначала вычислить кратчайший путь.
And that's another thing, OSPF is very heavy when it comes to the calculations of where to send the information.|И еще одна вещь, OSPF очень сложен, когда дело доходит до вычислений, куда отправлять информацию.
So it really puts a burden on the router.|Так что это действительно создает нагрузку на роутер.
It is extremely processor intensive.|Это чрезвычайно интенсивно использует процессор.
Sounds like a question to me, okay.|Для меня это вопрос, ладно.
Processor intensive, so keep that in mind.|Имейте это в виду.
But, well, one more thing,|Но, ну, еще кое-что,
one more thing before I continue, as far as the administrative distance, just to throw that out there, is 110, is 110.|Еще одна вещь, прежде чем я продолжу, что касается административного расстояния, просто скажем, 110, это 110.
I do have different labs for this.|Для этого у меня есть разные лаборатории.
I'm not gonna use the same labs that we used before.|Я не собираюсь использовать те же лаборатории, которые мы использовали раньше.
We're gonna use OSPF.|Мы будем использовать OSPF.
It has its own IPv6 lab,|У него есть собственная лаборатория IPv6,
it has its own everything.|в нем все свое.
So we'll be using the labs just for OSPF in itself,|Поэтому мы будем использовать лаборатории только для OSPF,
just to keep everything separate,|просто чтобы все было отдельно,
just to keep everything separate.|просто чтобы все было отдельно.
Now let's compare couple things.|А теперь сравним пару вещей.
Now you see here, OSPF is a link state,|Теперь вы видите, что OSPF - это состояние связи,
while RIP version 2 is a distance vector.|в то время как RIP версии 2 - это вектор расстояния.
And now we know we already know that a distance vector routing protocol,|И теперь мы знаем, что мы уже знаем, что протокол векторной маршрутизации на расстоянии,
all right, distance vector,|хорошо, вектор расстояния,
all it does is based on hey, direction,|все, что он делает, основано на эй, направление,
which way am I going,|куда я иду,
and how far is it away?|и как далеко это далеко?
All right, that's RIP.|Хорошо, это RIP.
So we're not talking about EIGRP.|Так что мы не говорим об EIGRP.
We know how EIGRP works.|Мы знаем, как работает EIGRP.
But RIP, that's all it's worried about,|Но RIP, это все, о чем он беспокоится,
hop count, hop count, hop count.|количество прыжков, количество прыжков, количество прыжков.
There is no hop count,|Нет подсчета хмеля,
when we come to OSPF.|когда мы подходим к OSPF.
With OSPF, remember, you have,|Помните, что с OSPF у вас есть
you have a process ID number,|у вас есть идентификационный номер процесса,
and you have an area number.|и у вас есть номер города.
The process ID number, for our purposes,|Идентификационный номер процесса, для наших целей,
for our purposes in the CCNA,|для наших целей в CCNA,
it is locally significant.|это имеет местное значение.
It is used for the stability of the database and keep track of the database that it creates.|Он используется для обеспечения стабильности базы данных и отслеживания создаваемой базы данных.
Link state database, that's the database I'm talking about, all right?|База данных состояний ссылок, это база данных, о которой я говорю, хорошо?
So that process ID number,|Итак, этот идентификационный номер процесса,
that's what that does.|вот что это делает.
All right?|Отлично?
The next number is the area number.|Следующее число - это номер области.
The area number,|Номер участка,
has to be the same for the CCNA.|должно быть таким же для CCNA.
Again, I can't stress that enough.|Опять же, я не могу этого особо подчеркнуть.
You have 4.2 billion areas.|У вас 4,2 миллиарда площадей.
Laz, you have 4.2 billion areas.|Лаз, у вас 4,2 миллиарда областей.
You mean to tell me we can only use one?|Вы хотите сказать, что мы можем использовать только один?
You can use one for the CCNA.|Вы можете использовать один для CCNA.
When you get there, if you do work for a company that is huge,|Когда вы доберетесь туда, если вы работаете в огромной компании,
then you will more likely use multiple area OSPF.|тогда вы, скорее всего, будете использовать OSPF с несколькими областями.
And you probably won't be putting area 51,|И вы, вероятно, не поставите область 51,
and you won't be putting area 0.|и вы не будете помещать область 0.
Well, you will be using area zero, sorry.|Ну, извините, вы будете использовать нулевую область.
You will be using area zero.|Вы будете использовать нулевую область.
But what I've ran into, especially in the telecommunications industry,|Но то, с чем я столкнулся, особенно в телекоммуникационной отрасли,
is that they use the IP format for the area, instead of the actual decimal for the area.|заключается в том, что они используют IP-формат для области вместо фактического десятичного числа для области.
They use a dotted decimal IP format instead of just a decimal number.|Они используют десятичный IP-формат с точками, а не просто десятичное число.
Like I, I'm in area 65,233,|Как и я, я нахожусь в районе 65 233,
they get that number and they convert it into an IP,|они получают это число и конвертируют его в IP,
and there's a method for that.|и для этого есть способ.
But again, you do not need to know that.|Но опять же, вам не нужно этого знать.
Can you do it?|Ты можешь сделать это?
Yes.|Да.
Will you do it?|Вы сделаете это?
Yes.|Да.
All right.|Отлично.
But again, if you're lucky enough to get,|Но опять же, если вам повезет получить,
to land the job or to be in that position,|получить работу или занять эту должность,
awesome, you'll se it.|круто, вы это увидите.
If you don't, you'll never see it.|Если вы этого не сделаете, вы никогда этого не увидите.
All right, so it all depends,|Хорошо, все зависит от того,
it all depends.|Все это зависит.
But for the CCNA,|Но для CCNA,
all we need to be concerned with is hey,|все, что нам нужно, это эй,
make sure the routers are all in the same area.|убедитесь, что все маршрутизаторы находятся в одной области.
And they don't go, the numbers don't go crazy to 1000 or nothing like that.|И они не идут, цифры не сходят с ума до 1000 или чего-то такого.
There are numbers in testing,|Есть числа в тестировании,
you know, you know, 300, you know,|знаете, знаете, 300, знаете,
area zero or area one.|нулевая зона или зона один.
That's the kinda things that they do.|Вот что они делают.
Just make sure that we're in the same area.|Просто убедитесь, что мы находимся в одном районе.
So, the limitation of OSPF,|Итак, ограничение OSPF,
as far as areas, 4.2 billion.|что касается площадей, то 4,2 млрд.
Is that really a limitation?|Это действительно ограничение?
If you wanna call it one, okay.|Если вы хотите назвать это одним, хорошо.
Everything has its limits.|У всего есть свои пределы.
All right, but we can give it a limitation.|Хорошо, но мы можем дать этому ограничение.
If you are using multiple area OSPF, you really don't want to that huge of an area.|Если вы используете OSPF с несколькими областями, вам действительно не нужна такая огромная область.
Just like you don't wanna have that huge of a VLAN, because then you, you know,|Точно так же, как вы не хотите иметь такую ​​огромную VLAN, потому что тогда вы, знаете ли,
are defeating the purpose of segmenting the broadcast.|побеждают цель сегментирования трансляции.
Well, the same thing goes here.|Что ж, здесь то же самое.
You rule of thumb, 50 routers,|Правило большого пальца, 50 маршрутизаторов,
let's say, per area.|скажем, на площадь.
But again, that's a number that I'm throwing out there.|Но опять же, это число, которое я выбрасываю.
So it all depends on your infrastructure and what you do.|Так что все зависит от вашей инфраструктуры и от того, чем вы занимаетесь.
And this isn't enough and I want to get off topic, because, you know,|И этого недостаточно, и я хочу уйти от темы, потому что, знаете,
I get calls just like everybody else,|Мне звонят, как и всем остальным,
cuz my resume is out there, right?|ведь мое резюме есть, верно?
Just for the heck of it.|Просто черт возьми.
Just for the heck of it.|Просто черт возьми.
And I was looking up today cuz they keep asking the definition for enterprise networks.|И я искал сегодня, потому что они продолжают спрашивать определение корпоративных сетей.
And it was funny,|И это было забавно,
cuz there's no real definition for it.|Потому что для этого нет настоящего определения.
There's a,|Есть,
there's a very general definition for it.|есть очень общее определение для этого.
So the next time somebody calls you,|Так что в следующий раз, когда тебе позвонят,
test them on it.|протестируйте их на нем.
Ask them, what do you mean by enterprise?|Спросите их, что вы подразумеваете под предприятием?
Is it a size they're looking at,|Это размер, на который они смотрят,
because it's not a size.|потому что это не размер.
It is the, not the amount of devices, but,|Дело не в количестве устройств, а в
well you can say the amount of different devices that is being used, the amount of different protocols that is being used.|ну, вы можете сказать количество различных устройств, которые используются, количество различных протоколов, которые используются.
Cuz really those people out there that are calling you,|Потому что действительно те люди, которые тебе звонят,
they themselves don't know what's going on, all right.|они сами не знают, что происходит, хорошо.
So hey, do not feel intimidate by all these people.|Так что, не пугайтесь всех этих людей.
You guys know what you're going.|Вы, ребята, знаете, что собираетесь.
And gals, you know what you're doing.|И девочки, вы знаете, что делаете.
All right?|Отлично?
So, be confident in what you're doing,|Так что будьте уверены в том, что делаете,
your knowledge, and you'll see that you'll do just fine, okay?|ваши знания, и вы увидите, что у вас все будет хорошо, хорошо?
Anyway, Supports, they both support classless routing, right?|В любом случае, Supports, они оба поддерживают бесклассовую маршрутизацию, верно?
BLSM, so there goes that.|BLSM, так вот.
Auto summarization,|Автоматическое суммирование,
auto summarization, sorry.|авто резюме, извините.
OSPF does not auto summarize.|OSPF не суммирует автоматически.
OSPF does not auto summarize,|OSPF не суммирует автоматически,
so we don't have to.|так что нам не нужно.
In OSPF, we don't have to worry about no auto summary command.|В OSPF нам не нужно беспокоиться об отсутствии команды автоматического суммирования.
We don't have to worry about it.|Нам не о чем беспокоиться.
We actually are going to use wild card masks.|На самом деле мы собираемся использовать маски подстановки.
We will put the exact network we belong to, so that's cool.|Мы укажем точную сеть, к которой принадлежим, так что это круто.
We can do that with OSPF.|Мы можем сделать это с помощью OSPF.
Now, remember with IPv6, or OSPF version 3, we don't do that.|Помните, что с IPv6 или OSPF версии 3 мы этого не делаем.
We do it on an interface by interface basis,|Мы делаем это от каждого интерфейса к другому,
just like we did RIP version 2 and EIGRP, okay?|точно так же, как мы сделали RIP версии 2 и EIGRP, хорошо?
But, if we're doing IPv4, which we will,|Но если мы используем IPv4, что мы и сделаем,
that's the first one we're gonna do.|это первое, что мы сделаем.
You're going to see that it's based on network statements.|Вы увидите, что он основан на сетевых утверждениях.
And again it's using wildcards,|И снова используются подстановочные знаки,
and then of course the area.|а потом конечно район.
Okay there's some support and manual summarization if you wanted to.|Хорошо, есть некоторая поддержка и ручное резюмирование, если хотите.
Wall propagation based on multicast or change.|Распространение стены на основе многоадресной передачи или изменения.
Everything is Multicast,|Все многоадресно,
but it's based on change.|но это основано на изменении.
It's based on triggered updates,|Он основан на запускаемых обновлениях,
triggered updates.|запускаемые обновления.
Now the thing with OSPF though.|Теперь о OSPF.
Yes it creates a topology table,|Да, он создает таблицу топологии,
but it does not work like EIGRP.|но он не работает как EIGRP.
Where EIGRP would query the topology table and bring out the next successor,|Если EIGRP запросит таблицу топологии и вызовет следующего преемника,
the feasible successor and everything keeps going.|возможный преемник, и все продолжается.
If a link goes down,|Если ссылка не работает,
if a link goes down in OSPF,|если ссылка в OSPF не работает,
every single router in that area is gonna recalculate a new path.|каждый маршрутизатор в этой области будет пересчитывать новый путь.
So that shortest path first calculation is just not that routers that lost that link.|Таким образом, первый расчет кратчайшего пути не относится к маршрутизаторам, которые потеряли эту ссылку.
Each and every router,|Каждый маршрутизатор,
all 50 routers, let's say,|все 50 роутеров, скажем так,
in that area, just to throw that number,|в этой области, просто чтобы бросить это число,
all 50 routers will recalculate again.|все 50 роутеров пересчитаются заново.
So, that's the problem with OSPF.|Итак, в этом проблема OSPF.
Now, are they gonna ask you something like that on the examination?|Теперь они собираются у вас спросить что-то подобное на экзамене?
No, they're not.|Нет, они не.
No, they're not.|Нет, они не.
No, they use shortest path first?|Нет, они сначала используют кратчайший путь?
Sure, all right?|Конечно, хорошо?
No, they're in the same area?|Нет, они в одном районе?
Sure.|Конечно.
But know that it calculates using the dicer, sure, and it creates a topology table?|Но знаете ли, что он, конечно, рассчитывает с помощью dicer и создает таблицу топологии?
Yes.|Да.
But as far as what I just said that all routers will calculate again?|Но насколько то, что я только что сказал, что все роутеры будут рассчитывать заново?
No.|Нет.
Know that it's processor intensive,|Знайте, что это интенсивно использует процессор,
but this is one of the reasons.|но это одна из причин.
Imagine.|Представить.
And it's not as quick as EIGRP,|И это не так быстро, как EIGRP,
or even RIP.|или даже RIP.
Because of the fact that every router has to recalculate.|Из-за того, что каждый роутер должен пересчитывать.
So if they recalculate,|Итак, если они пересчитают,
that means that link state advertisements.|это означает, что ссылка на государственную рекламу.
What is that?|Что это такое?
They got to sign all these link state updates, link state request.|Они должны были подписать все эти обновления состояния ссылок, запросы состояния ссылок.
All right?|Отлично?
All these different things need to be sent in order for the, the router to make the path again, to recreate everything again.|Все эти разные вещи необходимо отправить, чтобы маршрутизатор снова проложил путь, чтобы заново все воссоздать.
So that is one the things that with OSPF it takes,|Это одна из тех вещей, которые требуются для OSPF,
it was a little slower than EIGRP.|он был немного медленнее, чем EIGRP.
A little slower than EIGRP.|Немного медленнее, чем EIGRP.
Edit.|Редактировать.
Here is based on bandwidth just like EIGRP, bandwidth.|Здесь используется пропускная способность, как и EIGRP, пропускная способность.
Where we know that RIP is based on hob counts.|Мы знаем, что RIP основан на количестве плит.
We have, there is no limits,|У нас нет предела,
like I said, all right?|как я уже сказал, хорошо?
It is faster than RIP,|Это быстрее, чем RIP,
okay, if, if you say so.|хорошо, если, если ты так скажешь.
Does support authentication,|Поддерживает аутентификацию,
peer-to-peer, obviously.|одноранговый, очевидно.
Hierarchical networks, again,|И снова иерархические сети
if you're using multiple areas.|если вы используете несколько областей.
Will you use multiple areas to create a hierarchy of networks?|Будете ли вы использовать несколько областей для создания иерархии сетей?
Of course.|Конечно.
If your network is big enough,|Если ваша сеть достаточно большая,
when you get out there,|когда ты выйдешь оттуда,
you will create a multiple area OSPF.|вы создадите OSPF с несколькими областями.
A multiple area OSPF, you will do that.|OSPF с несколькими областями, вы это сделаете.
Now I will show you at the end of this session,|Сейчас я покажу вам в конце этого сеанса,
how to create a simple,|как создать простой,
a basic multi-area OSPF.|базовый многозонный OSPF.
Though you will understand the concept of it.|Хотя вы поймете концепцию этого.
We will do it.|Мы сделаем это.
But yes, definitely,|Но да, определенно,
when you get onto it you will see that.|когда вы войдете в него, вы увидите это.
You will not see that on your certification, and remember, this is your goal.|Вы не увидите этого в своем сертификате и помните, что это ваша цель.
This is what you need to focus on.|Это то, на чем вам нужно сосредоточиться.
All right?|Отлично?
And again we talked event triggered, oh,|И снова мы поговорили о событии, о
and there's Dijkstra,|и есть Дейкстра,
that's how you spell it.|вот как вы это пишете.
No matter how much I look at it,|Как бы я ни смотрел на это,
there it is.|вот оно.
Where RIP uses the Belman-Ford.|Где RIP использует файл Belman-Ford.
So again, a little bit of a comparison,|Итак, еще раз небольшое сравнение,
one routing protocol to the other.|один протокол маршрутизации к другому.
It's okay to compare but I mean that's like a little bully, really because,|Сравнивать можно, но я имею в виду, что это как маленький хулиган, потому что
my god, OSPF is huge, all right?|Боже мой, OSPF огромен, понятно?
Or OSPF is not very small, all right?|Или OSPF не очень маленький, да?
So that's a little comparison table.|Это небольшая сравнительная таблица.
What I'd like to show you next,|Что я хотел бы тебе показать дальше,
is the actual terminology that you need to be aware of, you need to be aware of.|- это фактическая терминология, которую вам нужно знать, вам нужно знать.
You need to understand what a link is.|Вы должны понимать, что такое ссылка.
Two routers connected to each other,|Два маршрутизатора, подключенных друг к другу,
that's a link.|это ссылка.
Two are routers that,|Два маршрутизатора,
their interfaces are joined,|их интерфейсы соединены,
that they've built that adjacency, right?|что они построили эту смежность, верно?
That is their foreman-neighbor relationship.|Это их отношения между мастером и соседом.
That is a link.|Это ссылка.
That is a link, all right?|Это ссылка, понятно?
Our router ID,|ID нашего роутера,
that's the name of the router.|это название роутера.
It's an IP address, the RID is an IP address used to identify the router.|Это IP-адрес, RID - это IP-адрес, используемый для идентификации маршрутизатора.
It's the name!|Это имя!
That's what it is,|Это и есть,
that's how they identify each other,|вот как они идентифицируют друг друга,
through the router ID.|через идентификатор маршрутизатора.
So it's essentially their name,|Так что по сути это их имя,
but in an IP format.|но в формате IP.
Neighbors.|Соседи.
This is important.|Это важно.
In order to qualify to be a neighbor,|Чтобы иметь право быть соседом,
you mu,|ты му,
remember we're talking about single area OSPF.|помните, что мы говорим об OSPF с одной областью.
The area must be the same.|Площадь должна быть такой же.
The subnet mask must be the same.|Маска подсети должна быть такой же.
Authentication is optional if you wanna configure it.|Аутентификация необязательна, если вы хотите ее настроить.
And the hello and deads are, are crucial.|И привет, и мертвые очень важны.
This right here, ladies and gentlemen, this one, and this one.|Это прямо здесь, дамы и господа, это и это.
The Area and the Hellos.|Район и привет.
This is something that you really need to pay attention to,|Это то, на что вам действительно нужно обратить внимание,
because I would test you on that.|потому что я хотел бы проверить вас на этом.
I would definitely create a test,|Я бы обязательно создал тест,
let's say like a print screen,|скажем, как экран для печати,
that I would have one router with a different area or I would show you a print screen with the default values of, of the hellos,|что у меня будет один роутер с другой областью, или я покажу вам экран печати со значениями по умолчанию hellos,
and then the other one on the bottom doesn't have the default values.|а другой внизу не имеет значений по умолчанию.
So you would say oh, the hellos are different because OSPF is extremely picky.|Итак, вы бы сказали, что привет разные, потому что OSPF очень разборчив.
If you do not have these the same,|Если у вас их нет,
and again, this is optional.|и опять же, это необязательно.
This is optional.|Это необязательно.
You don't have to have that.|Вам не обязательно это иметь.
You do not have to have that.|Вам не обязательно это иметь.
But, if you do,|Но если вы это сделаете,
it's gotta be identical on both sides.|он должен быть одинаковым с обеих сторон.
And you'll see that when we do PVP later on in the course.|И вы убедитесь в этом позже, когда мы будем проводить PVP.
But the hellos and the area are key,|Но привет и территория являются ключевыми,
and those are things you need home in,|и это то, в чем ты нуждаешься дома,
because if you have a question that deals with OSPF, nine out of ten, I guarantee you it's gonna have to deal with the area|потому что если у вас есть вопрос, связанный с OSPF, девять из десяти, я гарантирую вам, что это будет связано с областью
or the hello intervals are not the same.|или интервалы приветствия не совпадают.
And OSPF, its criteria, in order to become neighbors, that must be the same.|И OSPF, его критерии, чтобы стать соседями, должны быть такими же.
That must be the same, again,|Это должно быть то же самое, снова,
I stress, in a single area OSPF.|Подчеркиваю, в единой области OSPF.
All right, Adjacency is, again,|Хорошо, Смежность, опять же,
a relationship between two routers.|связь между двумя маршрутизаторами.
A DR, a DR, a DR's a designated router.|DR, DR, DR - это назначенный маршрутизатор.
Now a designated router only comes when there's an election.|Теперь назначенный маршрутизатор приходит только во время выборов.
It has to be in a broadcast environment,|Это должно быть в среде вещания,
such as ethernet.|например Ethernet.
So what is a job of a DR?|Так в чем же работа DR?
Of a designated router.|Назначенного маршрутизатора.
Because you have designated routers and you have back-up designated routers.|Потому что вы назначили маршрутизаторы и у вас есть резервные назначенные маршрутизаторы.
A designated router, what it does,|Назначенный маршрутизатор, что он делает,
it creates a full relationship, and we'll talk about that in a second,|это создает полноценные отношения, и мы поговорим об этом через секунду,
a full relationship with the rest,|полные отношения с остальными,
with everybody else.|со всеми остальными.
Think about a multi-access network, and we will, we have all, here let me show you.|Подумайте о сети с множественным доступом, и у нас есть все, позвольте мне показать вам.
It's no big deal.|Это ничего важного.
Here you go.|Ну вот.
Think about this network right here.|Подумайте об этой сети прямо здесь.
Imagine if everybody here had to talk to everybody here, and update everybody,|Представьте, если бы всем здесь пришлось поговорить со всеми здесь и сообщить всем,
it will be chaos.|это будет хаос.
This is ethernet, broadcast domain, right?|Это Ethernet, широковещательный домен, верно?
They're all touching each other,|Все они касаются друг друга,
multi-access network.|сеть с множественным доступом.
So, now they're all updating each other,|Итак, теперь они все обновляют друг друга,
they all have full relationships with each other.|все они имеют полные отношения друг с другом.
My god, that's a mess.|Боже мой, это беспорядок.
So what, what does OSPF do when they find themselves in this scenario?|Так что, что делает OSPF, когда они попадают в этот сценарий?
Well, let's say we're going to run an election.|Что ж, допустим, мы будем проводить выборы.
And they designate a designator router or a backup design- and, and a backup designator router.|И они обозначают маршрутизатор с указателем или резервный маршрутизатор, и резервный маршрутизатор с указателем.
All right?|Отлично?
But when we get into that we'll get a little bit deeper.|Но когда мы углубимся в это, мы немного углубимся.
All right?|Отлично?
But that's what a DR, and and only happens in this type of scenario,|Но это то, что DR, и происходит только в этом типе сценария,
multi-access network.|сеть с множественным доступом.
But again, this is what I mean by that.|Но опять же, я имею в виду именно это.
All right, so and the,|Хорошо, так и то,
the whole purpose is that,|вся цель в том,
so the DR sends the updates to everybody else and everybody else updates the DR.|поэтому DR отправляет обновления всем остальным, и все остальные обновляют DR.
That is the, the main deal.|Это главное.
All right.|Отлично.
And like it says here you can control it,|И, как здесь говорится, вы можете контролировать это,
and again I wanna talk about when we get to it, but you can control it many ways.|И снова я хочу поговорить о том, когда мы доберемся до этого, но вы можете контролировать это многими способами.
On of the ways it talks about here is using priority numbers.|Один из способов, о котором здесь говорится, - это использование номеров приоритета.
And they range from zero to 255.|И они варьируются от нуля до 255.
The higher the priority,|Чем выше приоритет,
you're the, you're the man!|ты, ты мужчина!
You are the DR.|Вы ДР.
For here to infinity.|Ибо здесь до бесконечности.
And beyond!|И не только!
No, from here to infinity, right?|Нет, отсюда до бесконечности, верно?
You are the designator router.|Вы - маршрутизатор с обозначением.
One less than that would be the backup designator router.|На единицу меньше этого будет резервным маршрутизатором с указателем.
Everybody else would be what they call a drother, designator router other.|Все остальные будут тем, что они называют друфером, другим маршрутизатором с обозначением.
Who made up that name?|Кто придумал это имя?
I have no idea, okay,|Понятия не имею, ладно,
but that's what it is.|но вот что это такое.
All right?|Отлично?
But anyway, so that's what these two things are and we'll run into them when we do the lab for that.|Но в любом случае, вот что это за две вещи, и мы столкнемся с ними, когда сделаем для этого лабораторию.
Hello!|Здравствуйте!
That is, and look, multicast, multicast,|То есть и посмотрите, мультикаст, мультикаст,
multicast that's how it maintains the relationship between these routers.|многоадресная рассылка - вот как он поддерживает отношения между этими маршрутизаторами.
Between their neighbor, cuz remember, it's the neighbors that talk to each other, and it does it based on multicast addresses.|Между своими соседями, помните, это соседи, которые общаются друг с другом, и это происходит на основе адресов многоадресной рассылки.
So now, OSPF uses two addresses.|Итак, теперь OSPF использует два адреса.
If you're forming a full relationship with standard OSPF routers, let's say,|Если вы формируете полноценные отношения со стандартными маршрутизаторами OSPF, скажем,
you have a point-to-point connection,|у вас есть соединение точка-точка,
you're gonna use the 224.0.0.5.|вы собираетесь использовать 224.0.0.5.
But in a multi-access network you're gonna use 224.0.0.5 and, 224.0.0.6.|Но в сети с множественным доступом вы будете использовать 224.0.0.5 и 224.0.0.6.
The six is for the DR and the BDR so,|Шесть для DR и BDR, так что
that's why there's two multi-access IP addresses used in OSPF.|вот почему в OSPF используются два IP-адреса с множественным доступом.
One for just standard routers.|Один только для стандартных роутеров.
One just for DR and BDR purposes.|Один только для DR и BDR.
All right.|Отлично.
Know that.|Знай это.
Neighbor database.|База данных соседей.
Again a list of all the neighbors that,|Снова список всех соседей, которые,
you know, their hellos.|вы знаете, их привет.
The topology database.|База данных топологии.
Contains the LSA packets that have been received.|Содержит полученные пакеты LSA.
These your link-state advertisements that.|Эти ваши ссылки-государственные рекламные объявления.
Within those Link State Advertisements are the Link State Updates.|В этих объявлениях о состоянии канала содержатся обновления состояния канала.
All right?|Отлично?
And Link State Requests and all that.|И запросы состояния ссылки и все такое.
All these Link State Advertisements,|Все эти объявления о состоянии ссылок,
even though they're,|хотя они,
they're small there there's a lot of information in there.|там они маленькие, там много информации.
[SOUND] All right?|[ЗВУК] Хорошо?
And when we get to how to become a neighbor,|И когда мы дойдем до того, как стать соседом,
you'll see that.|вы увидите это.
All right, then you have, I just showed you a broadcast multi-access network,|Хорошо, тогда у вас есть, я только что показал вам широковещательную сеть с множественным доступом,
which is a network with multiple devices connected to one,|это сеть с несколькими устройствами, подключенными к одному,
just sort of like ethernet.|просто вроде как Ethernet.
OSPF areas, contiguous areas.|Области OSPF, прилегающие территории.
In our por, in our scenario,|В нашем пор, в нашем сценарии,
we'll have one one area that we have to be concerned with.|у нас будет одна область, о которой мы должны позаботиться.
And then, you have point-to-point.|Кроме того, у вас есть точка-точка.
Or point to multipoint, okay, topologies.|Или указать на многоточечные, ладно, топологии.
So again, but, non-broadcast can also be frame relay, all right?|И снова, но нешироковещательная передача также может быть ретрансляцией кадров, хорошо?
And, we won't do a frame relay,|И мы не будем использовать Frame Relay,
network for OSPF cuz the whole point for you is to learn what frame relay is,|сеть для OSPF, потому что все дело в том, чтобы узнать, что такое Frame Relay,
but, it does exist.|но он существует.
Now the,|Сейчас,
the problem with this is non-broadcast.|проблема с этим не в трансляции.
Well, so is Frame relay.|Ну, и Frame Relay тоже.
So that's why when you get to do frame relay, non-broadcast multi-access you run into the same situation of designator routers and backup designator routers.|Вот почему, когда вы выполняете ретрансляцию кадров, нешироковещательный множественный доступ, вы попадаете в ту же ситуацию, что и маршрутизаторы с указателем и резервные маршрутизаторы с указателем.
So you need to be aware of these things.|Так что вам нужно знать об этих вещах.
So when you get into this typical scenario.|Итак, когда вы попадаете в этот типичный сценарий.
So there's our terminology and this will be a ma, made available to you but again,|Итак, вот наша терминология, и это будет ма, доступная вам, но, опять же,
not, no, be familiarized with everything obviously but there's certain things that you will see on test like these criterias,|нет, нет, ознакомьтесь со всем, очевидно, но есть определенные вещи, которые вы увидите на тесте, например эти критерии,
the area and the hellos.|область и привет.
All right?|Отлично?
The Router ID.|Идентификатор маршрутизатора.
That you need to know.|Это вам нужно знать.
The BR, I mean the DR and BDR,|BR, я имею в виду DR и BDR,
you need to know about these.|вам нужно знать об этом.
Okay?|Ладно?
All right.|Отлично.
So this is the terminology about OSPF that you need to be aware of.|Итак, это терминология OSPF, о которой вам нужно знать.
Remember, it's a link state routing protocol.|Помните, что это протокол маршрутизации состояния канала.
There is no, no auto-summary command,|Нет, нет команды автосводки,
because it doesn't summarise automatically.|потому что он не резюмирует автоматически.
All right?|Отлично?
We'll be putting in a wild card mask.|Мы будем использовать маску подстановки.
It is based on areas.|Он основан на площадях.
Areas.|Области.
Areas can go from zero to 4.2 billion,|Площади могут быть от нуля до 4,2 миллиарда,
whatever the whole number is.|каким бы ни было целое число.
Whether it's 4.2 billion,|Будь то 4,2 миллиарда,
we're concerned with just one single area,|нас интересует только одна область,
and it's using bandwidth.|и он использует полосу пропускания.
It's using bandwidth that the [INAUDIBLE]|Это использование пропускной способности, которое [НЕВНЯТНО]
uses to calculate the shortest path.|используется для вычисления кратчайшего пути.
First algorithm in order to find all these different, networks and pathways.|Первый алгоритм для поиска всех этих различных сетей и путей.
So we can get to our destinations, and thus it keeps that in the dipositator.|Таким образом, мы можем добраться до места назначения и, таким образом, удерживать его в дипозитаторе.
Obviously, the best path, as usual,|Очевидно, лучший путь, как обычно,
go up to the routing table and that's how it goes.|подойти к таблице маршрутизации и вот как это происходит.
The only problem is if one link goes,|Проблема только в том, что если идет одна ссылка,
they all calculate again.|все они снова рассчитывают.
They all calculated again.|Все пересчитали.
And, once we get to the,|И как только мы доберемся до
the, the DR and BDR,|, DR и BDR,
the multi-access, labs that we'll be doing and we'll be discussing more and more detail with the multi-access OSPF,|лабораторные работы с множественным доступом, которые мы будем делать, и мы будем обсуждать все больше и больше деталей с OSPF с множественным доступом,
then we'll get, we'll talk about that.|потом доберемся, об этом и поговорим.
All right?|Отлично?
I'll see you guys in the next lesson.|Увидимся на следующем уроке.