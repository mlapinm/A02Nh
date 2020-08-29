D:\mailCloud\prjother\tmp\1\c84_what is STP used for.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
Welcome back, everyone.|С возвращением, все.
See, that wasn't too bad, creating VLANs,|Видите, это было не так уж плохо, создавать VLAN,
assigning VLANs.|назначение VLAN.
Very simple, very simple,|Очень просто, очень просто,
just always remember to trunk those ports between switches.|просто всегда не забывайте соединять эти порты между коммутаторами.
But when you do, something happens.|Но когда вы это делаете, что-то происходит.
And this is where it leads us to the spanning tree protocol.|И здесь это приводит нас к протоколу связующего дерева.
What is spanning tree?|Что такое остовное дерево?
The purpose of spanning tree is to avoid switching loops.|Задача связующего дерева - избежать петель переключения.
A switch, by nature, since nature created it,|Выключатель по своей природе, поскольку природа создала его,
it will continue to forward and forward and forward nonstop.|он будет продолжать движение вперед, вперед и назад без остановок.
And as network techs or engineers,|И как сетевые специалисты или инженеры,
whatever title you want to give yourself,|какой бы титул вы себе ни дали,
all right the forwarding of these bridge protocol data units going around all these switches, it's not a good thing.|Хорошо, пересылка этих блоков данных протокола моста через все эти коммутаторы, это нехорошо.
Because it will cause a broadcast storm.|Потому что это вызовет широковещательный шторм.
And we all know that, what that means, a broadcast storm means that your network will fall down to its knees,|И все мы знаем, что это означает, что широковещательный шторм означает, что ваша сеть упадет на колени,
it will die, literally on you.|он умрет, буквально на тебе.
But let's take a look at the packet tracer.|Но давайте посмотрим на трассировщик пакетов.
So take a look at spanning tree in action.|Итак, взгляните на остовное дерево в действии.
All right.|Отлично.
So we don't really need crossover cables,|Так что перекрестные кабели нам не нужны,
I'm gonna be lazy,|Я буду ленив,
I'm just gonna use that lightning bolt.|Я просто использую эту молнию.
So you're gonna pick, it usually picks the first ports anyway.|Так что вы собираетесь выбирать, обычно он все равно выбирает первые порты.
Gotta hit around the blue.|Должен ударить по синему.
All right, when you see these lights that are turning amber, there we got, we got two switches, I know it was right behind|Хорошо, когда вы видите эти огни, которые загораются желтым, у нас есть два переключателя, я знаю, что это было прямо позади
me, so you couldn't probably see it.|меня, так что вы, вероятно, не могли этого увидеть.
All right, we've got two switches, you see that spanning tree is thinking about it,|Хорошо, у нас есть два переключателя, вы видите, что остовное дерево думает об этом,
saying, hm, what's going on here, we got redundant links.|говоря, хм, что здесь происходит, у нас есть избыточные ссылки.
That's when spanning tree becomes alive,|Вот когда остовное дерево оживает,
when you have redundant links.|когда у вас есть избыточные ссылки.
And it takes about 30 all the way up to maybe 90 seconds for it to make a decision.|И для принятия решения требуется от 30 до 90 секунд.
And we'll talk about that in a future lesson.|И мы поговорим об этом на следующем уроке.
But for right now, you can see that these two lights are green,|Но сейчас вы можете видеть, что эти два огонька зеленые,
that third light up there is green, but one light, it's amber, it is amber.|тот третий свет там зеленый, но один свет, он янтарный, он янтарный.
So I can tell you right now for the terminology that you need to understand about spanning trees.|Так что прямо сейчас я могу рассказать вам о терминологии, которую вам нужно понять в отношении остовных деревьев.
So, now you know spanning tree,|Итак, теперь вы знаете остовное дерево,
its purpose is to block switching loops,|его цель - блокировать шлейфы переключения,
right?|право?
Stop switching loops.|Прекратите переключение шлейфов.
How do they do that?|Как они это делают?
Block support.|Блокировка поддержки.
There it is, that's your blocked port.|Вот он, ваш заблокированный порт.
It stayed amber.|Он остался янтарным.
Doesn't mean it's not listening, it still receives, but it will not forward,|Это не значит, что он не слушает, он все равно принимает, но не пересылает,
all right.|отлично.
But let's take a look at this first switch right here.|Но давайте посмотрим на этот первый переключатель прямо здесь.
All right, let's put this over here.|Хорошо, положим это сюда.
You know what, let's just maximize it.|Знаете что, давайте просто максимизируем это.
And the way you look at it, you go to privileged mode, obviously.|И если посмотреть на это, очевидно, что вы попадаете в привилегированный режим.
Show spanning-tree, and you take a look at it.|Покажите остовное дерево, и вы посмотрите на него.
Now, one of the things that you want to pay attention to is, hey,|Итак, одна из вещей, на которую вы хотите обратить внимание, это, эй,
this is telling us the root bridge.|это говорит нам корневой мост.
And we'll go into the election process later.|И мы поговорим об избирательном процессе позже.
But this is the root bridge.|Но это корневой мост.
That means that on the root bridge,|Это означает, что на корневом мосту
on the root bridge, all ports are designated forwarding ports.|на корневом мосту все порты назначены портами пересылки.
Designated forwarding ports.|Назначенные порты пересылки.
And you see, since we're using fast Ethernet, the cost of that is 19.|Видите ли, поскольку мы используем Fast Ethernet, стоимость этого составляет 19.
The cost of it is 19.|Стоимость 19.
If we're using gigabit, it would be 4.|Если мы используем гигабит, это будет 4.
All right?|Отлично?
So these, any port on the root bridge will be a designated forwarding port.|Таким образом, любой порт на корневом мосту будет назначенным портом пересылки.
All right, that's what you need to keep drilled in your head.|Хорошо, это то, что вам нужно держать в голове.
Meaning, it will forward out information,|Это означает, что он будет пересылать информацию,
okay.|Ладно.
Designated forwarding.|Специальная пересылка.
This is the root bridge.|Это корневой мост.
Okay?|Ладно?
So I guess we're going to go to the non-root bridge,|Думаю, мы перейдем к некорневому мосту,
which is the bridge that's not the root.|это мост, а не корень.
[LAUGH] Pretty simple, right?|[СМЕХ] Довольно просто, правда?
Don't, don't gotta get complicated with it.|Не надо, не надо усложнять это.
[BLANK_AUDIO]|[BLANK_AUDIO]
Show spanning tree, and here, hey, this is not the root bridge, okay.|Покажи остовное дерево, а здесь, эй, это не корневой мост, хорошо.
So, but what are we looking at?|Итак, но на что мы смотрим?
Hey, there's the port that it blocked.|Эй, это порт, который он заблокировал.
See?|Видеть?
Alternating block.|Переменный блок.
And then there's a port that says root.|А еще есть порт с надписью root.
All ports that face the root bridge are root ports.|Все порты, обращенные к корневому мосту, являются корневыми портами.
They will forward, obviously.|Очевидно, они будут вперед.
You can see the status of it is forwarding.|Вы можете видеть статус пересылки.
But it is a root port, because it's facing the root bridge.|Но это корневой порт, потому что он обращен к корневому мосту.
Now, this is a very simple example.|Это очень простой пример.
This is just so you are aware of the command to look at spanning tree,|Это просто для того, чтобы вы знали о команде для просмотра связующего дерева,
which is show spanning-tree, all right.|который является остовным деревом, хорошо.
Or show spanning-tree VLAN 1.|Или покажите связующее дерево VLAN 1.
Because it's the only VLAN we have for now.|Потому что это единственная VLAN, которая у нас есть на данный момент.
All right?|Отлично?
But, once you see the amber light, and what they'll do on your test they'll ask you to pick the the root bridge.|Но как только вы увидите желтый свет и то, что они будут делать в вашем тесте, они попросят вас выбрать корневой мост.
They'll ask you to pick which port is designated forwarding,|Вас попросят выбрать порт для пересылки,
or which port is block port, or which port is a root port.|или какой порт является заблокированным портом, или какой порт является корневым портом.
So these are the things you need to be aware of.|Итак, это то, о чем вам нужно знать.
So remember, on the root bridge, on the root bridge, all ports,|Итак, помните, что на корневом мосту, на корневом мосту, все порты,
all ports are designated forwarding, they will forward information.|все порты предназначены для пересылки, они будут пересылать информацию.
On the non-root bridges, all right, like in this scenario anyway you'll have one block port and the other one will be a designated forwarding port, it will|На некорневых мостах все в порядке, как и в этом сценарии, в любом случае у вас будет один блочный порт, а другой будет назначенным портом пересылки, он будет
forward information.|пересылать информацию.
Always remember, the block port will just block from PDUs being forwarded,|Всегда помните, что блокирующий порт просто блокируется от перенаправляемых PDU,
bridge protocol data units from being forwarded.|блоки данных протокола моста от пересылки.
But, it will receive, it will receive.|Но он получит, он получит.
But it just won't send.|Но его просто не отправят.
All right, that, ladies and gentlemen, is what STP is.|Хорошо, дамы и господа, это и есть STP.
In our next lesson, though, we are going to break it down, and make several comparisons and take a look at the election process of spanning-tree.|Однако в нашем следующем уроке мы разберем его, проведем несколько сравнений и взглянем на процесс выбора остовного дерева.
I'll see you there.|Увидимся там.
[BLANK_AUDIO]|[BLANK_AUDIO]