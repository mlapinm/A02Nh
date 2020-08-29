D:\mailCloud\prjother\tmp\1\c26_Distribution Layer.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
All right.|Отлично.
The distribution layer.|Слой распределения.
Now, this could be kind of confusing, the,|Это могло сбить с толку,
the drawing, because it looks like,|рисунок, потому что он выглядит так,
you know, all your networks are down, all your PCs are down here.|вы знаете, все ваши сети отключены, все ваши компьютеры здесь.
Then they go to this router and this router routes it over here.|Затем они переходят к этому маршрутизатору, и этот маршрутизатор направляет их сюда.
But really the distribution layer,|Но на самом деле слой распределения,
it's the go between the access layer and the core as you can see.|как видите, это переход между слоем доступа и ядром.
Not always is it gonna take it to a core because in the distribution layer that'll be your NAT, that'll be your firewall.|Не всегда он будет доводить его до ядра, потому что на уровне распространения, который будет вашим NAT, это будет ваш межсетевой экран.
That'll be your InterVLANs, that'll be your routing policies,|Это будут ваши InterVLAN, это будут ваши политики маршрутизации,
your quality of service, all these different things,|ваше качество обслуживания, все эти разные вещи,
your policy based routings, all that will be here, the distribution layer.|ваша маршрутизация на основе политик, все, что будет здесь, уровень распределения.
Obviously I didn't build an entire network and show different connections everywhere,|Очевидно, я не построил целую сеть и не показывал везде разные соединения,
just showing you the you know, there's three layers.|просто показываю вам, что есть три слоя.
But this is the one that's doing the majority of the work.|Но это тот, кто делает большую часть работы.
That's the one that the routing, the major routing,|Это та самая маршрутизация, основная маршрутизация,
the deciding hey, is this gonna go to the core layer cuz it has to go to the core layer, this is gonna go to another campus,|решающий, эй, это пойдет на основной уровень, потому что он должен перейти на основной уровень, это пойдет в другой кампус,
gonna go to another building, or is it just going somewhere else?|собираешься пойти в другое здание или просто куда-нибудь?
Is it going to this router?|Собирается ли он на этот роутер?
Right if I had a connection going here.|Хорошо, если бы у меня была связь здесь.
Or is it going to another VLAN because there's other VLANs coming down?|Или он переходит в другую VLAN, потому что другие VLAN отключаются?
So this distribution layer really is doing all that work, okay.|Итак, этот уровень распространения действительно делает всю эту работу, хорошо.
So DSP in any kind of router, but it's a beefy router all right.|Итак, DSP есть в любом маршрутизаторе, но это, конечно, мощный маршрутизатор.
Unlike the core, definitely is gonna be a beefy router and in the core one thing I didn't mention was, you don't want to expand the core, you try to avoid it.|В отличие от ядра, он определенно будет мощным маршрутизатором, а в ядре я не упомянул одну вещь: вы не хотите расширять ядро, вы пытаетесь этого избежать.
The one thing you want to do is upgrade it definitely.|Единственное, что вы хотите сделать, это определенно обновить его.
But as your distribution the one that's making the deciding factor,|Но поскольку ваше распределение является решающим фактором,
hey does this really need to go to the core or can I route it some other way.|эй, действительно ли это нужно, чтобы перейти к ядру, или я могу перенаправить его другим способом.
The only time, now remember,|Единственный раз, теперь помни,
that rule 80% of all traffic should be local to your segment.|это правило 80% всего трафика должно быть локальным для вашего сегмента.
This is, somewhat, applies here as well.|Это в некоторой степени применимо и здесь.
So, if you're gonna avoid trying to get outside because it's gotta go to the core,|Итак, если вы собираетесь избегать попыток выбраться наружу, потому что это должно идти в самое сердце,
because it's going somewhere else,|потому что он идет в другое место,
then the distribution router is the one that's gonna make that decision.|тогда это решение будет принимать распределительный маршрутизатор.
That's why you have your QoS, that's why you have your routing policies,|Вот почему у вас есть QoS, поэтому у вас есть свои политики маршрутизации,
that's why you have your access list,|вот почему у вас есть список доступа,
that's why you have your InterVLANs.|вот почему у вас есть свои InterVLAN.
Like I said before.|Как я говорил раньше.
So, this is gonna be doing a lot of the routing decisions.|Итак, это будет принимать многие решения по маршрутизации.
Whether it's gonna, if it's, is it necessary for grow,|Будет ли это, если это необходимо для роста,
to go to the core router, or can I just route it to the other router next door,|чтобы перейти на основной маршрутизатор, или я могу просто направить его на другой маршрутизатор по соседству,
or is it going back down, or what the case may be.|Или он снова упадет, или в чем дело.
So, that is your distribution layer.|Итак, это ваш уровень распределения.
That is your distribution layer.|Это ваш уровень распределения.
You, again, it'll make the decision, am I going to send it to the core router?|Вы, опять же, примете решение, я собираюсь отправить его на основной маршрутизатор?
That's the main thing you need to be concerned with.|Это главное, о чем вам нужно беспокоиться.
And as far as you know,|И насколько вы знаете,
what you shouldn't do is what the other two layers are doing, really.|на самом деле вам не следует делать то, что делают два других слоя.
But, other than that, it's going to have the majority of the work that that is doing, it's the distribution layer.|Но, кроме этого, большая часть работы, которую он выполняет, будет на уровне распределения.
That's where all the routing is going on.|Вот где и происходит вся маршрутизация.
And again in your test, they're not gonna ask you all those questions.|И снова в вашем тесте они не будут задавать вам все эти вопросы.
You may get asked one question.|Вам могут задать один вопрос.
They may ask you what are the three layers of the Cisco router,|Они могут спросить вас, каковы три уровня маршрутизатора Cisco,
of the Cisco three layer model.|трехуровневой модели Cisco.
They may ask you, you know, which is the most important layer, now, the core layer.|Они могут спросить вас, знаете ли, какой слой является наиболее важным, теперь это основной слой.
These are very basic questions, but understand that a lot, the chunk,|Это очень простые вопросы, но имейте в виду, что многое, кусок,
the main, the meat and potatoes, as I like to call it, is going on right here,|главное, мясо и картошка, как я люблю это называть, происходит прямо здесь,
because we don't want to bog down that core router, as I said previously.|потому что, как я сказал ранее, мы не хотим перегружать этот основной маршрутизатор.
We want just information passed back and forth.|Мы хотим, чтобы информация передавалась туда и обратно.
And it's the distribution layer that makes that decision, hey,|И это уровень распределения принимает это решение, эй,
am I going to send this packet to the core routers.|я собираюсь отправить этот пакет на основные маршрутизаторы.
So again, it's your distribution layer the one that's really doing all the routing, all the access lists,|Итак, опять же, именно ваш уровень распределения действительно выполняет всю маршрутизацию, все списки доступа,
everything that is required to actually route the packets in in the direction that they should be going.|все, что требуется для фактической маршрутизации пакетов в том направлении, в котором они должны идти.
Okay?|Ладно?
That's your distribution layer.|Это ваш уровень распределения.
See you in the next one.|Увидимся в следующем.
[BLANK_AUDIO]|[BLANK_AUDIO]