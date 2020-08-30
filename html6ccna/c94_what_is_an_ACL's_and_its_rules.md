D:\mailCloud\prjother\tmp\1\c94_what is an ACL's and its rules.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
Welcome back, ladies and gentlemen.|С возвращением, дамы и господа.
We have traveled far.|Мы далеко продвинулись.
We've gone through routing protocols.|Мы прошли протоколы маршрутизации.
We've gone through static routes.|Мы прошли статические маршруты.
We've learned how to configure our switches and spanning-tree in VLAN.|Мы узнали, как настроить коммутаторы и связующее дерево в VLAN.
It now comes time to secure our network.|Пришло время обезопасить нашу сеть.
Now obviously, there's many ways to secure a network.|Очевидно, что есть много способов защитить сеть.
The way that we need to secure a network,|Способ, которым нам нужно защитить сеть,
the,|то,
the way that we need to learn is really through the use of ACLs.|способ, которым нам нужно учиться, на самом деле заключается в использовании ACL.
I'm gonna use the lab that we used, in the previous session, or section.|Я собираюсь использовать лабораторию, которую мы использовали на предыдущем сеансе или в разделе.
That we have all these configurations, we got connective going back and forth between are VLANs and all that.|Поскольку у нас есть все эти конфигурации, у нас есть соединения, идущие туда и обратно между VLAN и всем остальным.
So we will be doing access lists in order to control the traffic.|Итак, мы будем делать списки доступа, чтобы контролировать трафик.
Right?|Правильно?
It's like a filter.|Это как фильтр.
An access list is like a filter that will permit or deny certain types of traffic.|Список доступа подобен фильтру, который разрешает или запрещает определенные типы трафика.
Now you'll see this in, internal or trusted networks, is where you usually will see these ACLs.|Теперь вы увидите это во внутренних или доверенных сетях, именно там вы обычно видите эти ACL.
Obviously, if you're talking about security,|Очевидно, если вы говорите о безопасности,
the first thing is physical security.|во-первых, физическая безопасность.
You will have firewalls, you will have group policies, you will have DMZs,|У вас будут брандмауэры, у вас будут групповые политики, у вас будут DMZ,
you have all sorts of types of security.|у вас есть всевозможные виды безопасности.
Security is just not one layer; it is a multitude of layers.|Безопасность - это не один уровень; это множество слоев.
So you can try and prevent somebody from trying to get in.|Так что вы можете попытаться помешать кому-то проникнуть внутрь.
Think of this, and, I mean, it goes beyond what we're gonna talk about with the ACL,|Подумайте об этом, и, я имею в виду, это выходит за рамки того, о чем мы будем говорить с ACL,
but just to give you an idea.|но просто чтобы дать вам представление.
If you're gonna secure your home, you have a gate.|Если вы собираетесь обезопасить свой дом, у вас есть ворота.
Let's say you customize that gate and now you have barbed wire around the gate.|Допустим, вы настраиваете эти ворота, и теперь у вас есть колючая проволока вокруг ворот.
Inside your yard, that's around your house the,|Внутри вашего двора, это вокруг вашего дома,
this gate is around you have dogs, right?|эти ворота вокруг вас есть собаки, верно?
Attack dogs and on top of that you have an alarm system.|Нападайте на собак и, кроме того, у вас есть сигнализация.
So it's different layers of security that somebody needs to circumvent in order to get inside your house.|Так что это разные уровни безопасности, которые нужно обойти, чтобы проникнуть в ваш дом.
So how bad does this individual or individuals want to get inside your home.|Итак, насколько сильно этот человек или люди хотят попасть в ваш дом.
So, security is about layering.|Итак, безопасность - это наслоение.
For the CCNA certification, all we need to understand is basically standard and extended access lists.|Для сертификации CCNA все, что нам нужно понимать, - это стандартные и расширенные списки доступа.
And that's what, that's what we're gonna talk about.|И вот что, вот о чем мы будем говорить.
And access lists, again, is a set of conditions, it's a filter.|И списки доступа, опять же, это набор условий, это фильтр.
Let's open up Notepad,|Откроем Блокнот,
[BLANK_AUDIO]|[BLANK_AUDIO]
All right?|Отлично?
So, as a set, ACLs,|Итак, как набор ACL,
small s is a set of conditions.|small s - это набор условий.
That's it.|Вот и все.
You either permit or deny.|Вы либо разрешаете, либо отрицаете.
And we're gonna do several types of access list.|И мы сделаем несколько типов списков доступа.
There's basically only two types, standard and extended.|В основном есть только два типа: стандартный и расширенный.
But yeah, okay, there's a third.|Но да, ладно, есть третий.
Because when you talk about standard,|Потому что когда вы говорите о стандарте,
standard,|стандарт
we're talking about numbered access lists.|мы говорим о нумерованных списках доступа.
But there's one called named, which is either an extended or a standard.|Но есть один, называемый named, который является либо расширенным, либо стандартным.
But instead of giving it a number,|Но вместо того, чтобы дать ему номер,
standard, but instead of giving it an actual number,|стандарт, но вместо того, чтобы дать ему действительный номер,
we're giving it a name.|мы даем ему имя.
Just to make it easier to identify.|Просто чтобы облегчить идентификацию.
So we'll be doing all of these.|Итак, мы будем делать все это.
Now, they're certain things you need to understand about access list.|Вот некоторые вещи, которые вам нужно знать о списке доступа.
There are rules to access list, there are rules to access list.|Есть правила для списка доступа, есть правила для списка доступа.
Now, when we talk about the rules and let me bring this up a little higher.|Теперь, когда мы говорим о правилах, позвольте мне поднять это немного выше.
You can see this right?|Вы это понимаете?
I want to make sure you can see that.|Я хочу убедиться, что вы это видите.
Let's maximize this.|Давайте максимизировать это.
Okay?|Ладно?
Rules of access list, basically is an,|Список правил доступа, в основном,
a, an ACL is read in order.|a, ACL читается по порядку.
Meaning, first line, second line,|Значение, первая строка, вторая строка,
third line and so forth.|третья строка и так далее.
All right, so if you're, you have an access list that's made up of you know,|Хорошо, так что, если у вас есть список доступа, состоящий из вы знаете,
100 lines.|100 строк.
It's going to keep reading each line in order, one, two, three, four, five, six,|Он будет продолжать читать каждую строку по порядку: один, два, три, четыре, пять, шесть,
seven, eight, nine, ten.|семь восемь девять десять.
We're talking about numbered access, any access list, actually.|Мы говорим о нумерованном доступе, фактически о любом списке доступа.
It's gonna go in sequential order until it makes a match.|Он будет идти в последовательном порядке, пока не найдется совпадение.
Once it makes a match, then it stops at that point and applies whatever condition is set at that point.|Как только он находит совпадение, он останавливается в этой точке и применяет любое условие, установленное в этой точке.
So that's one of the rules.|Так что это одно из правил.
Also, and not a,|Кроме того, а не
an ACL and this is extremely important,|ACL, и это очень важно,
has an implicit deny at the end.|имеет неявное отрицание в конце.
So if you write an access list statement,|Итак, если вы напишете оператор списка доступа,
let's say,|скажем,
standard access list one Deny, host,|стандартный список доступа один Запретить, хост,
1.1.1.1.|1.1.1.1.
And you leave it like that.|И вы оставите это так.
Right underneath that, it's invisible.|Прямо под ним это невидимо.
You don't see it, but there's an actual deny everything.|Вы этого не видите, но на самом деле все отрицать.
So, if you start an access list, with a deny statement,|Итак, если вы запустите список доступа с заявления deny,
you must end it with a permit any, or any any.|вы должны закончить это разрешением любого или любого другого.
Depending on the type of actions you are doing, but you must end it with a permit statement.|В зависимости от типа действий, которые вы выполняете, но вы должны закончить их разрешением.
Because if not, everything will be denied.|Потому что в противном случае будет отказано во всем.
And this is something that they'll ask questions about.|И об этом они будут задавать вопросы.
They'll give you, let's say an example of an access list.|Они дадут вам, скажем, пример списка доступа.
And all you'll see are a bunch of denies.|И все, что вы увидите, - это множество отрицаний.
You will never see a permit statement.|Вы никогда не увидите справку о разрешении.
So if it's going in sequential order and everything is denied,|Итак, если это происходит в последовательном порядке и все отклоняется,
and at the end it ends with a deny, well there's an implicit deny also.|и в конце это заканчивается отрицанием, ну, также есть неявное отрицание.
So there is no traffic that's gonna be allowed through that particular interface,|Таким образом, нет трафика, который будет разрешен через этот конкретный интерфейс,
period.|период.
Because it's denied.|Потому что это отрицается.
So that's an important rule right there,|Итак, это важное правило прямо здесь,
and ACL has an implicit deny at the end,|и в конце ACL есть неявное отклонение,
whether it's a standard, extended,|будь то стандартный, расширенный,
whatever it is.|что бы это ни было.
If you start an access list with an deny statement,|Если вы начинаете список доступа с заявления deny,
you must finish it with a permit.|вы должны закончить это с разрешением.
Always remember that.|Всегда помни об этом.
And the last one is, you can only have one acl per interface, comma,|И последнее: у вас может быть только один acl на интерфейс, запятая,
per protocol, per direction.|по протоколу, по направлению.
Meaning, when you,|Имея в виду, когда ты,
you first create an access list you can create as many access lists as you want.|вы сначала создаете список доступа, вы можете создать столько списков доступа, сколько захотите.
Nothing's gonna happen unless you apply it.|Ничего не произойдет, если вы его не примените.
It is a two step process.|Это двухэтапный процесс.
You must first create the access list and then you apply it to the interface of the router.|Сначала необходимо создать список доступа, а затем применить его к интерфейсу маршрутизатора.
Whether it's going into the router, or it's coming out of the router.|Идет ли он в маршрутизатор или выходит из маршрутизатора.
So you've got to make that decision, so basically you only have two,|Вы должны принять это решение, так что в основном у вас есть только два,
one going in, one coming out.|один входит, один выходит.
Those are your ACLs.|Это ваши ACL.
You will have to create an ACL from scratch.|Вам придется создать ACL с нуля.
So we must pay very close attention to this particular session, all right?|Итак, мы должны уделять очень пристальное внимание именно этой сессии, понятно?
So one ACL per interface, per protocol,|Итак, один ACL на интерфейс, на протокол,
per direction, that's another rule.|по направлению, это еще одно правило.
Also, I guess a rule, you can call it that.|Кроме того, я полагаю, что это правило можно так назвать.
You cannot,|Ты не можешь,
I'll put can't, but cannot remove a numbered ACL that lies within the group.|Я поставлю "не могу", но не могу удалить нумерованный ACL, который находится в группе.
What does that mean?|Что это значит?
So if I have ten lines.|Итак, если у меня есть десять строк.
If I have ten lines, okay?|Если у меня будет десять строк, хорошо?
If I have ten lines all in ACL, and I want to take off the eighth line, can't do it.|Если у меня десять строк всего в ACL, и я хочу убрать восьмую строку, я не могу этого сделать.
It'll remove the whole thing.|Он удалит все это.
You can't do that with a numbered ACL.|Вы не можете сделать это с пронумерованным списком ACL.
If you try to add something, it's just going to add it to the bottom.|Если вы попытаетесь что-то добавить, он просто добавит это внизу.
It's not going to add it to the very top or to the middle.|Он не собирается добавлять его в самый верх или в середину.
You have more flexibility with named access lists to do that than you do with number.|Для этого у вас больше гибкости с именованными списками доступа, чем с номерами.
It is recommended anyway, that you use a text editor or Notepad to create your ACL's and then just paste them onto your routers.|В любом случае рекомендуется использовать текстовый редактор или Блокнот для создания списков ACL, а затем просто вставлять их в свои маршрутизаторы.
Or switches, whatever the case may be, or Layer 3 switches,|Или переключатели, в любом случае, или переключатели уровня 3,
whatever the case may be.|в любом случае.
But again, for the CCNA certification,|Но опять же, для сертификации CCNA,
we're doing this on routers, on routers.|мы делаем это на маршрутизаторах, на маршрутизаторах.
Also, from top to bottom is most specific to most general.|Кроме того, «сверху вниз» относится к самому общему.
I guess you can consider that another rule.|Думаю, вы можете считать это еще одним правилом.
On top most specific.|Сверху самое конкретное.
And I'll move out of the way so you can see it.|И я отойду с дороги, чтобы вы это увидели.
On the bottom, ooh, most general.|Внизу, ох, самое общее.
So that's why, and let me bring this up,|Вот почему, и позвольте мне поднять это,
so you can see the rules right there.|так что вы можете увидеть правила прямо здесь.
Okay.|Ладно.
So on the very top, you're gonna be, I want you to deny this particular individual, to this, from this particular individual.|Итак, на самом верху вы будете, я хочу, чтобы вы отказали этому конкретному человеку, этому, этому конкретному человеку.
And the bottom, hey, hey, permit everything, so from very specific to most general.|И внизу, эй, эй, разрешите все, от очень конкретного до самого общего.
So you have got to organize,|Итак, вам нужно организовать,
the hardest thing about access lists is not really the configuration,|самое сложное в списках доступа на самом деле не конфигурация,
the syntax of it, but the logic of it, as to what is it you're doing.|синтаксис этого, но логика того, что вы делаете.
What, what am I denying?|Что, что я отрицаю?
How am I going to deny in this?|Как я буду отрицать это?
Where am I going to apply it?|Куда я буду его применять?
That is the most important part.|Это самая важная часть.
Now remember, and we'll, we'll get into more details.|Теперь запомните, и мы рассмотрим более подробную информацию.
We're going to separate standards from extended and we'll explain each one and do several labs for each one or several configurations for each one so|Мы собираемся отделить стандарты от расширенных, объясним каждый из них и проведем несколько лабораторных работ для каждой или нескольких конфигураций для каждой, так что
you can understand.|ты можешь понять.
But that is the most difficult part.|Но это самая сложная часть.
Because your book says one thing, which is correct, but now they're trying to make the test a little bit more real world.|Потому что ваша книга говорит одно, и это правильно, но теперь они пытаются сделать тест немного более реальным.
And when it comes to the access lists,|А что касается списков доступа,
they wanna make you think, because it's really going against what the book says.|они хотят заставить вас задуматься, потому что это действительно противоречит тому, что говорится в книге.
And once we get to extended access lists,|И как только мы дойдем до расширенных списков доступа,
I will explain that in further detail.|Я объясню это более подробно.
All right.|Отлично.
But again, what you need to know at this point, that access lists have rules.|Но опять же, что вам нужно знать на этом этапе, что списки доступа имеют правила.
Especially that implicit deny at the end,|Особенно это неявное отрицание в конце,
you can't forget that, you can't forget that.|Вы не можете забыть этого, вы не можете этого забыть.
Most general, I mean most specific to most general.|От самого общего, я имею в виду от самого конкретного до самого общего.
And you can only have one access list, per protocol, per interface, per direction.|И у вас может быть только один список доступа для каждого протокола, интерфейса и направления.
These are the type of rules.|Это своего рода правила.
And again, we'll be doing standard and extended access lists.|И снова мы будем делать стандартные и расширенные списки доступа.
And we're gonna go into each one, and talk about each one independently, so you can understand how to configure it,|И мы собираемся перейти к каждому из них и поговорить о каждом отдельно, чтобы вы могли понять, как его настроить,
and why it works the way it works.|и почему он работает именно так.
And now of course, with access list, ha ha,|А теперь, конечно, со списком доступа, ха-ха,
it's just like OSPF, we used wildcard masking.|это как OSPF, мы использовали маскировку с использованием подстановочных знаков.
So, I hope you remember how to do our wildcard masking, right?|Итак, я надеюсь, вы помните, как делать нашу маскировку с помощью подстановочных знаков, верно?
You gotta use your constant number or if you know how,|Вы должны использовать свой постоянный номер или, если знаете, как
you know the little diagram that I showed you.|вы знаете маленькую диаграмму, которую я вам показал.
You use that instead.|Вы используете это вместо этого.
ACLs are not really that difficult.|ACL не так уж и сложны.
They really are not.|На самом деле это не так.
Especially for what we're gonna be using them for, the CCNA, all right?|Специально для того, для чего мы собираемся их использовать, CCNA, хорошо?
They're very, very they're, they're simple.|Они очень, очень простые, они очень простые.
They're simple.|Они простые.
They're very straightforward,|Они очень простые,
they're not as difficult as you'd think.|они не такие сложные, как вы думаете.
But we'll go through it slowly but surely.|Но мы пройдем через это медленно, но верно.
But just remember, when we talk about security, I know in your mind,|Но помните, когда мы говорим о безопасности, я знаю, что вы думаете,
especially if you are IT professionals already.|особенно если вы уже являетесь ИТ-специалистами.
You're like hey, you know, we use policies and we use these firewalls and we use this, and that's what you do do,|Вы типа, эй, знаете, мы используем политики, и мы используем эти брандмауэры, и мы используем это, и это то, что вы делаете,
that's what you use.|вот что вы используете.
But again, for the certification,|Но опять же, для сертификации,
we need to learn these ACLs and know where to actually apply them.|нам нужно изучить эти ACL и знать, где их на самом деле применять.
And that's how they're going to test you.|И вот как они собираются тебя проверить.
Where are you going to apply this particular access list based on this scenario.|Куда вы собираетесь применить этот конкретный список доступа на основе этого сценария.
All right?|Отлично?
That's basically it.|Вот в основном это.
All right, so hope you are ready.|Хорошо, надеюсь, ты готов.
This is what access lists are.|Вот что такое списки доступа.
In our next session, we're gonna start talking about standard access lists.|На следующем занятии мы начнем говорить о стандартных списках доступа.
I will see you there.|Увидимся там.
[BLANK_AUDIO]|[BLANK_AUDIO]