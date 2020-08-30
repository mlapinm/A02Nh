D:\mailCloud\prjother\tmp\1\c86_How to manipulate the election process.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
Welcome back, everyone.|С возвращением, все.
Now that we know the election process of STP, or familiar with it,|Теперь, когда мы знаем процесс выборов в STP или знакомы с ним,
we're gonna go ahead, and this is the same pyramid that we did in a previous lesson.|мы пойдем дальше, и это та же пирамида, что мы делали на предыдущем уроке.
I just deleted the two switches on top.|Я просто удалил два переключателя сверху.
All right.|Отлично.
So we know that this is the root bridge but we don't want that to be the root bridge.|Итак, мы знаем, что это корневой мост, но мы не хотим, чтобы он был корневым мостом.
Okay?|Ладно?
And when we do our labs,|И когда мы делаем наши лаборатории,
that's exactly what we're gonna be doing.|именно это мы и будем делать.
We're gonna be tweaking all these stuff.|Мы собираемся подправить все эти вещи.
Cuz we got a big lab towards the end of the switching portion of the course.|Потому что у нас есть большая лаборатория к концу переходной части курса.
We want this guy right here.|Мы хотим, чтобы этот парень был здесь.
The one that's actually being blocked.|Тот, который на самом деле заблокирован.
We want that particular switch to be the root bridge.|Мы хотим, чтобы этот конкретный коммутатор был корневым мостом.
Why?|Зачем?
Because in our labs, we're going to be connected to a router.|Потому что в наших лабораториях мы будем подключаться к маршрутизатору.
So I want that one to be the root bridge.|Итак, я хочу, чтобы он был корневым мостом.
So we need to go ahead and change the priority number to something lower than the other switches.|Поэтому нам нужно пойти дальше и изменить номер приоритета на что-то меньшее, чем у других переключателей.
But I want to make sure that you can't just introduce any other switch that has a lower number than mine and then that becomes the root bridge.|Но я хочу убедиться, что вы не можете просто ввести какой-либо другой коммутатор с меньшим номером, чем мой, и тогда он станет корневым мостом.
Right?|Правильно?
So I'm going to put it at the lowest number possible.|Поэтому я собираюсь поставить его как можно меньшее число.
So I'm going to go ahead, open up here.|Итак, я собираюсь открыть здесь.
Now, we only have one VLAN which is VLAN1,|Теперь у нас есть только одна VLAN - VLAN1,
all right, and we show VLAN, only on one VLAN.|ладно, а мы показываем VLAN, только на одном VLAN.
If we had multiple VLANs we can do one instance of spanning tree across all the VLANs.|Если бы у нас было несколько VLAN, мы могли бы создать один экземпляр связующего дерева для всех VLAN.
So we want this root bridge to be the root bridge across all the VLANs.|Итак, мы хотим, чтобы этот корневой мост был корневым мостом для всех VLAN.
All right, so we're gonna pretend we've created some VLANs.|Хорошо, мы сделаем вид, что создали несколько VLAN.
So we're gonna do this.|Итак, мы сделаем это.
We're gonna go to Global.|Мы пойдем в Global.
I'm gonna do Spanning tree, VLAN1.|Я собираюсь создать связующее дерево, VLAN1.
And normally, I would stop there, and then I would continue wit the syntax,|И обычно я останавливался на этом, а затем продолжал синтаксис,
priority number, blah, blah, blah, blah.|номер приоритета, бла, бла, бла, бла.
But we're gonna pretend that there's more VLANs, and there will be when we create our huge lab.|Но мы будем делать вид, что есть больше VLAN, и они будут, когда создадим нашу огромную лабораторию.
So across VLAN1, across VLAN10, across VLAN 20, priority.|Итак, по VLAN1, по VLAN10, по VLAN 20, приоритет.
Now, I'm going to put a number, and it's going to be a wrong number.|Теперь я поставлю число, и это будет неправильное число.
But I want you to see what comes out.|Но я хочу, чтобы вы увидели, что получится.
I'll put number nine, Enter.|Я поставлю номер девять, Enter.
And it said, hey, wait a minute.|И он сказал: «Эй, подожди минутку».
[BLANK_AUDIO]|[BLANK_AUDIO]
The allowed values, right?|Допустимые значения, верно?
I was putting hey, I put spanning tree VLAN1, 10,|Я ставил эй, я ставил связующее дерево VLAN1, 10,
20 because I want this to be the root bridge across all my VLANs.|20, потому что я хочу, чтобы это был корневой мост для всех моих VLAN.
I want one instance of spanning-tree across all my VLANs, and I was gonna give it a lower priority,|Мне нужен один экземпляр связующего дерева во всех моих VLAN, и я собирался дать ему более низкий приоритет,
nine.|девять.
But then it told me, hey listen these are the allowed values, 0,|Но потом он сказал мне, послушайте, это допустимые значения, 0,
4096, that's the incrementation.|4096, это приращение.
It increments by 4096, you just can't pick any number.|Он увеличивается на 4096, вы просто не можете выбрать любое число.
Now, I want you to pay attention to one number.|Теперь я хочу, чтобы вы обратили внимание на одно число.
What's the default number of all switches?|Какое количество всех переключателей установлено по умолчанию?
32769.|32769.
Do you see it in that range right there?|Вы видите это прямо здесь в этом диапазоне?
No, you do not.|Нет, ты не.
What you do see is this.|Вы видите вот что.
32768.|32768.
Because it will add VLAN1 to 32768 and it becomes 32769.|Потому что он добавит VLAN1 к 32768 и станет 32769.
So that lets you, leads you to believe that once you do create these VLAN 10 and 20, it's gonna add 10 to 0.|Это позволяет вам поверить, что как только вы создадите эти VLAN 10 и 20, они прибавят 10 к 0.
It's gonna add 20 to 0.|Он прибавит 20 к 0.
So that priority number will change per VLAN.|Таким образом, этот номер приоритета будет изменяться для каждой VLAN.
But it will, he will be the lowest of the lowest you'll have that one instance, okay?|Но это будет, он будет самым низким из самых низких, которые у вас будут в этом единственном экземпляре, хорошо?
So let's do another barrel.|Итак, займемся еще одной бочкой.
Let's take that nine away and let's put zero.|Уберем девять и поставим ноль.
And I'm gonna hit Enter, and as soon as I do that I'm gonna try and minimize quickly so you can see.|И я собираюсь нажать Enter, и как только я это сделаю, я попытаюсь быстро свернуть, чтобы вы могли видеть.
So the spanning tree is doing its thing.|Итак, остовное дерево делает свое дело.
This is amber that's amber, all right?|Это янтарь, это янтарь, понятно?
So we think okay, what do I block.|Итак, мы думаем, хорошо, что мне блокировать.
What do I block?|Что я блокирую?
I don't know.|Я не знаю.
All right?|Отлично?
It's doing it's calculation based on the lowest cost path to the root bridge,|Он выполняет расчет на основе самого дешевого пути к корневому мосту,
all right, which is going to be this one.|хорошо, это будет этот.
Now, based on the criteria of the priority number or the combination of the priority number and the MAC address which is the bridge ID.|Теперь на основе критериев номера приоритета или комбинации номера приоритета и MAC-адреса, который является идентификатором моста.
All right.|Отлично.
As you can see,|Как вы видете,
this is now the root bridge.|теперь это корневой мост.
This, pick this one to block a port because it has a,|Это, выберите этот, чтобы заблокировать порт, потому что у него есть,
it had a higher high res, remember this used to be the root bridge right here.|у него было более высокое разрешение, помните, что это был корневой мост прямо здесь.
Right?|Правильно?
So this MAC Address over here is gonna be higher than this one.|Итак, этот MAC-адрес здесь будет выше, чем этот.
So it chose this one to block and it blocked the higher port number because every port that faces the root bridge must be a root port.|Поэтому он выбрал этот для блокировки и заблокировал порт с более высоким номером, потому что каждый порт, обращенный к корневому мосту, должен быть корневым портом.
So let's take a look.|Итак, давайте посмотрим.
[BLANK_AUDIO]|[BLANK_AUDIO]
Let's open that up.|Давайте откроем это.
[SOUND] And let's exit out here.|[ЗВУК] И давайте выходим отсюда.
Let's do Show [COUGH] oh my god, Show Spanning Tree.|Давайте сделаем Show [COUGH] боже мой, Show Spanning Tree.
Show spanning tree,|Показать остовное дерево,
you can see I put a priority number of one because we have one VLAN, VLAN1.|Вы можете видеть, что я поставил приоритет номер один, потому что у нас одна VLAN, VLAN1.
Therefore, the priority number is one, and it tells you where, right here, you see?|Следовательно, число приоритета - единица, и оно говорит вам, где, прямо здесь, вы видите?
Priority is zero but the ID1 which is the VLAN1, it adds it to the priority number so that's why you see that that is a priority of one.|Приоритет равен нулю, но ID1, который является VLAN1, добавляет его к номеру приоритета, поэтому вы видите, что это приоритет, равный единице.
The VLAN 10and 20 would exist you would see 10 on under VLN 10 and 20 under VLAN 20.|Существуют VLAN 10 и 20, вы увидите 10 под VLN 10 и 20 под VLAN 20.
All right, if you do spanning tree, VLAN 10, it would show you.|Хорошо, если вы сделаете связующее дерево, VLAN 10, оно вам покажет.
All right, so this is the root bridge.|Хорошо, это корневой мост.
And my ports are designated forwarding.|А мои порты предназначены для переадресации.
And then we go down here, so now everything is based on priority numbers.|А потом мы спустимся сюда, так что теперь все основано на номерах приоритета.
Show Spanning Tree.|Показать связующее дерево.
[SOUND] All right, you're gonna see the alternating block right there.|[ЗВУК] Хорошо, вы увидите чередующийся блок прямо здесь.
You can see that the root bridge priority number is 1 but the non-root bridge priority number is 32769.|Вы можете видеть, что номер приоритета корневого моста равен 1, а номер приоритета некорневого моста - 32769.
So everything is based now on priority numbers.|Так что теперь все основано на приоритетных числах.
This is how you can go ahead and tweak,|Вот как вы можете пойти дальше и настроить,
all right, spanning trees.|хорошо, остовные деревья.
So you can decide who will be your root bridge, all right?|Итак, вы можете решить, кто будет вашим корневым мостом, хорошо?
And you can do it across VLANs, or you can do it just for that one VLAN.|И вы можете сделать это через VLAN, или вы можете сделать это только для этой одной VLAN.
That's all you have.|Это все, что у тебя есть.
You just, you don't want to do VLAN's.|Вы просто не хотите создавать VLAN.
You want to go against what I have told you.|Вы хотите пойти против того, что я вам сказал.
And you just want to have just one VLAN in your entire enterprise, okay.|И вы просто хотите иметь только одну VLAN на всем предприятии, хорошо.
You go ahead and it'll just be, just that one priority will always be one.|Вы идете вперед, и это будет просто, только один приоритет всегда будет одним.
You change it to zero, it will always be priority one.|Вы меняете его на ноль, приоритет всегда будет один.
All right.|Отлично.
That's it,|Это оно,
that's all there is to tweaking spanning tree, all right?|это все, что нужно для настройки связующего дерева, ясно?
To go head and, make the root bridge who you want to be the root bridge.|Чтобы пойти и сделать корневой мост, который вы хотите быть корневым мостом.
But again, you need to know what you're looking at.|Но опять же, вам нужно знать, на что вы смотрите.
You need to know what you're looking at.|Вам нужно знать, на что вы смотрите.
And always remember, so important,|И всегда помни, так важно,
remember the roles of those ports.|запомните роли этих портов.
Every port facing the root bridge R reports,|Каждый порт, обращенный к корневому мосту R, сообщает,
the root bridge will always have a designated forwarding.|у корневого моста всегда будет назначенная переадресация.
The one, the-|Тот, тот-
[BLANK_AUDIO]|[BLANK_AUDIO]
The switch with the highest MAC address,|Коммутатор с наивысшим MAC-адресом,
the highest port number,|наивысший номер порта,
will be the one that's blocked.|будет тот, который заблокирован.
Okay?|Ладно?
So always keep that in mind.|Так что всегда имейте это в виду.
Always keep that in mind because this is how they are going to test you for spanning tree.|Всегда имейте это в виду, потому что именно так они будут проверять вас на остовное дерево.
Lowest priority numbers, the, the port roles and status, all right?|Номера с самым низким приоритетом, роли и статус портов, хорошо?
[SOUND] and what else?|[ЗВУК] а что еще?
Role for that?|Роль для этого?
That's pretty much basically it.|В основном это все.
Just know the roles, know the status of the ports and know how to tweak spanning tree and the election process.|Просто знайте роли, знайте статус портов и знайте, как настроить связующее дерево и процесс выбора.
If you know that, you should have no issues.|Если вы это знаете, у вас не должно быть проблем.
But believe me, you're gonna get plenty of practice when we do our final lab on the the switching portion of the course.|Но поверьте мне, у вас будет много практики, когда мы проведем нашу последнюю лабораторную работу по переходной части курса.
All right, that is how you tweak spanning tree.|Хорошо, вот как вы настраиваете остовное дерево.
Very, very easy.|Очень и очень просто.
All you gotta do, spanning tree, VLAN,|Все, что вам нужно, связующее дерево, VLAN,
whatever VLANs you're using.|какие бы сети VLAN вы ни использовали.
If you're using one, just put one.|Если вы используете один, просто поставьте его.
Priority, and just make it to zero.|Приоритет, и просто довести его до нуля.
That will always be the root bridge.|Это всегда будет корневой мост.
See you in the next one.|Увидимся в следующем.
[BLANK_AUDIO]|[BLANK_AUDIO]