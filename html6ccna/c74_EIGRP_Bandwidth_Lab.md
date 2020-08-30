D:\mailCloud\prjother\tmp\1\c74_EIGRP Bandwidth Lab.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
All right, I did promise you in the previous lesson, which was EIGRP bo,|Хорошо, я обещал вам на предыдущем уроке, который был EIGRP bo,
both version four and version six, that we're gonna do another type lab,|как версия четыре, так и версия шесть, что мы собираемся провести еще одну лабораторию типов,
where you're gonna have several pathways that the packing can get to.|где у вас будет несколько путей, по которым может добраться упаковка.
So I wanna show you, how we're gonna manipulate those two key or really, just one key value of the k values?|Итак, я хочу показать вам, как мы собираемся манипулировать этими двумя ключевыми или действительно только одним ключевым значением из k значений?
All right, which is the bandwidth.|Хорошо, это пропускная способность.
All right, so let me show you exactly what's going on the topology table,|Хорошо, позвольте мне показать вам, что именно происходит в таблице топологии,
cuz now, there will be a feasible successor.|Потому что теперь будет возможный преемник.
All right, you have two different ways it can go, so we maybe better understand what you're looking at because the other one|Хорошо, у вас есть два разных пути, так что мы, возможно, лучше понимаем, на что вы смотрите, потому что другой
was straight across, there was no feasible successor and, you know, everything had the pretty much the same metric.|было прямым, не было подходящего преемника, и, знаете, все имело почти одинаковые метрики.
So, let's take a look, cuz remember we got two destinations that works.|Итак, давайте посмотрим, потому что помните, у нас есть два работающих пункта назначения.
We got the 100.0 or got the 200.0.|Мы получили 100.0 или получили 200.0.
As you notice down here, you have three routers versus two routers up here.|Как вы заметили здесь внизу, у вас есть три маршрутизатора против двух маршрутизаторов здесь.
All right, so let's take a look at router zeros.|Хорошо, давайте посмотрим на нули маршрутизатора.
One click, and again, if I'm in the way,|Один щелчок, и снова, если я мешаю,
I'll get out of the way after I do the command.|Я уйду с дороги после того, как выполню команду.
It's Enabled, you know that, CONFIG T, and we'll do a show IP route,|Он включен, вы знаете, CONFIG T, и мы сделаем показ IP-маршрута,
SH IP now ROUE, that's in French by the way, no.|СХ ИП теперь РУЭ, это по-французски кстати, нет.
I'm in the wrong place.|Я не в том месте.
Show IP ROUTE.|Показать IP-МАРШРУТ.
Okay, as you can see here, show IP route,|Хорошо, как вы можете видеть здесь, покажите IP-маршрут,
and the routing table that we have to get to the 200 network, we're going via the 10.1.1.6, which is up through the 0000.|и таблица маршрутизации, которую мы должны получить в сети 200, мы проходим через 10.1.1.6, то есть через 0000.
That's what the routing table is saying.|Это то, что говорит таблица маршрутизации.
Take a look at this number right here.|Взгляните на этот номер прямо здесь.
This is the feasible distance, this is the successor route.|Это допустимое расстояние, это следующий маршрут.
All right, the 2686976.|Хорошо, 2686976.
So, let's, but there's two ways that it could go.|Итак, давайте, но есть два варианта развития событий.
Let's take a look at the topology table.|Взглянем на таблицу топологии.
Remember we only got one way to get there according to our routing table.|Помните, что у нас есть только один способ попасть туда согласно нашей таблице маршрутизации.
But let's take a look at the topology table.|Но давайте посмотрим на таблицу топологии.
Show IP, EIGRP TOPALO, oh, TOPOLOGY.|Покажи IP, EIGRP TOPALO, ой, ТОПОЛОГИЯ.
And if you're looking for that same destination network, let's move it up a little bit here, right here, everything was passive remember, we said it was good.|И если вы ищете ту же самую целевую сеть, давайте немного переместим ее сюда, прямо здесь, все было пассивным, помните, мы сказали, что это хорошо.
But we have two ways.|Но у нас есть два пути.
We have the 6, and we have 29, 29's coming down.|У нас есть 6, и у нас 29, идет 29.
But if you take a look, this is the number that we saw up there.|Но если вы посмотрите, это то число, которое мы видели там.
Well this number is lower, than this number right here.|Ну, это число ниже, чем это число прямо здесь.
Therefore, it will use the feasible distance, which is the 2686976.|Следовательно, будет использоваться допустимое расстояние, равное 2686976.
That is the fastest route, that is the best route to get to that point.|Это самый быстрый маршрут, лучший путь к этой точке.
Why is that the best route?|Почему это лучший маршрут?
Think about this.|Думать об этом.
Just to do a little math in our heads,|Просто чтобы посчитать в голове,
nothing big, nothing major,|ничего большого, ничего серьезного,
don't freak out, all right?|не волнуйтесь, хорошо?
Let's take a look.|Давайте взглянем.
Well, you know already cause I've shown you, right?|Ну, ты уже знаешь, потому что я тебе показал, верно?
These are WIC-2T, both of these are one point,|Это WIC-2T, это одна точка,
they are 1544 megabits per second, the fast,|они 1544 мегабита в секунду, быстрые,
Ethernet though let's take a look up here,|Ethernet, хотя давайте посмотрим здесь,
and I'll show you those Enable how interface F0/0 right, and we look at it's bandwidth let's just maximize the screen.|и я покажу вам, как включить интерфейс F0 / 0 правильно, и мы посмотрим на его пропускную способность, давайте просто развернем экран.
If you take a look at it's bandwidth is 100000 kilobits per second,|Если вы посмотрите на его пропускную способность, это 100000 килобит в секунду,
which is 100 megabits per second.|что составляет 100 мегабит в секунду.
So, think about just that bandwidth right there, and the delay is 100.|Итак, подумайте об этой полосе пропускания прямо сейчас, и задержка составляет 100.
But, when you're doing the calculations not you but EIGRP.|Но когда вы делаете вычисления, не вы, а EIGRP.
It's looking they have two routers, so you have a delay it won't be the delay over here,|Похоже, у них два маршрутизатора, так что у вас задержка, это не задержка здесь,
I think its 20,000 which turns out to be to the is it two the,|Я думаю, что это 20000, которые, как оказалось, связаны с двумя,
20,000 let's take a look at it, I forget just wanna make sure that I'm telling you the right stuff, show [NOISE] show IP in,|20,000, давайте посмотрим на это, я забыл, просто хочу убедиться, что я говорю вам правильные вещи, покажите [NOISE], покажите IP,
not show IP Int, show interface not ubt,|не показывать IP Int, показывать интерфейс не ubt,
SH INT S0/0/0 0.|SH ИНТ S0 / 0/0 0.
It's a delay of 20,000 okay, which really turns into 2000 but 20,000, and we have 100.|Это задержка в 20 000, что действительно превращается в 2000, но в 20 000, а у нас 100.
But here, you only have two.|Но здесь у вас их всего два.
Right here you have three, so you're have a bigger delay going this way than you would going this way, because it is cumulative delay.|Прямо здесь у вас их три, так что у вас будет большая задержка в этом направлении, чем в этом, потому что это кумулятивная задержка.
So, you have more delay coming this way,|Итак, у вас еще больше задержки,
than you would going this way.|чем вы бы пошли по этому пути.
That's why EIGRP choose to sent the packet that way.|Вот почему EIGRP решил отправить пакет именно таким образом.
And let's verify that the packet does go that way.|И давайте проверим, что пакет действительно идет по этому пути.
So what we're gonna do is we're gonna go to simulation mode,|Итак, что мы собираемся сделать, мы перейдем в режим симуляции,
simulation mode, that's ru, okay.|режим симуляции, вот ру, ладно.
And we're going to choose a, the close envelope which is a simple PDU or PNG.|И мы собираемся выбрать закрытый конверт, который представляет собой простой PDU или PNG.
We're gonna click on it, we're gonna click on PC0,|Мы нажимаем на него, мы нажимаем на PC0,
and then we're going to click on PC1.|а затем мы собираемся нажать на ПК1.
Yes, you're not gonna see an arc, because I you know I did this lab,|Да, вы не увидите дуги, потому что я, вы знаете, делал эту лабораторию,
I pinged across to make sure we had connectivity.|Я пробежался, чтобы убедиться, что у нас есть связь.
That's why you only see the PNG now.|Вот почему сейчас вы видите только PNG.
So if I were to auto-capture and play, you see that it's gonna go up.|Так что, если бы я включил автоматический захват и воспроизведение, вы увидите, что он будет расти.
And we'll wait for the little envelope,|А мы будем ждать конвертик,
there you go, it goes up.|вот так, он идет вверх.
Because it's chosen, the routing table says it chooses to go that way, cuz again,|Поскольку он выбран, таблица маршрутизации говорит, что он выбирает этот путь, потому что опять же,
the delay this way is a lot more than it would be going this way.|задержка в этом направлении намного больше, чем в этом случае.
So, we're going to actually mani tweak that,|Итак, мы собираемся изменить это,
manipulate by changing the bandwidth of the path.|манипулировать, изменяя полосу пропускания пути.
I'm actually gonna change the bandwidth,|Я на самом деле собираюсь изменить пропускную способность,
we're going to change the bandwidth.|мы собираемся изменить пропускную способность.
Going across each side because we want it to go that way, and come back this way.|Пересекая каждую сторону, потому что мы хотим, чтобы все шло по тому пути, и возвращались сюда.
That's exactly what we wanted, I mean, I'm sorry, we want to do opposite.|Это именно то, что мы хотели, я имею в виду, извините, мы хотим сделать наоборот.
Since it's coming this way, and coming back this way we want to send it down this ways.|Поскольку он идет этим путем и возвращается этим путем, мы хотим отправить его этим путем.
So we're going to increase to the maximum amount of bandwidth which is like 10|Итак, мы собираемся увеличить пропускную способность до максимального значения, равного 10
million.|миллион.
All right, we're gonna, yes I do exaggerate.|Хорошо, мы собираемся, да, я преувеличиваю.
But that's just, that's just me, you should know me by now, all right.|Но это просто, это только я, ты должен знать меня сейчас, хорошо.
We're gonna go ahead, and do that.|Мы пойдем дальше и сделаем это.
We're gonna go ahead, and increase the bandwidth here to all,|Мы собираемся пойти дальше и увеличить пропускную способность для всех,
all, every point along here.|все, каждая точка здесь.
We're going to increase it to 10 million,|Мы собираемся увеличить его до 10 миллионов,
all right.|отлично.
And this way, we're going to reduce it,|И таким образом мы уменьшим его,
I'm gonna put 100 or I'm going to put 64, 64, 64, 64, 64, 64.|Я поставлю 100 или 64, 64, 64, 64, 64, 64.
I'm just gonna go too extremes.|Я просто пойду слишком далеко.
And you're going to see how EIGRP is going to recalculate.|И вы увидите, как EIGRP будет пересчитывать.
And then what it should happen is that the packet now, the routing tables will change, and er, and it should tell you that it's gonna go this way.|И тогда должно произойти следующее: теперь пакет, таблицы маршрутизации изменятся, и э-э, и он должен сказать вам, что он пойдет этим путем.
So let's get that done.|Итак, давайте сделаем это.
So I want to go to the first router.|Итак, я хочу перейти на первый роутер.
And this is pretty simple.|А это довольно просто.
All you gotta do, let's bring it this way so you can.|Все, что вам нужно сделать, давайте сделаем это так, чтобы вы могли.
All you do is, you go into the interface,|Все, что вам нужно сделать, это войти в интерфейс,
and you change the bandwidth.|а вы меняете пропускную способность.
Now we're gonna change the bandwidth first going down.|Теперь мы сначала изменим пропускную способность.
So that's my, at zero zero one, and then,|Итак, это мой, в ноль ноль один, а затем,
s zero,|с ноль,
zero, and we, we'll, we'll look at the routers as we do them.|ноль, и мы, мы, мы будем смотреть на маршрутизаторы, как мы их делаем.
Okay, so first my S zero, zero, one.|Итак, сначала мои S ноль, ноль, один.
Let's do the bottom first, cuz I get very easily confused.|Давайте сначала сделаем нижнюю часть, потому что меня очень легко запутать.
CONFIG T INTerface, S0/0/1, and let me open it up a little bit.|CONFIG T INTerface, S0 / 0/1, и позвольте мне немного его открыть.
So we can see one more.|Итак, мы можем увидеть еще один.
And we're going to do bandwidth, and we're going to say 64 no, that's 10|И мы собираемся сделать пропускную способность, и мы собираемся сказать 64 нет, это 10
million this way.|миллион таким образом.
Ten, one two three, one two three.|Десять, один два три, один два три.
So, we're changing the bandwidth to 10|Итак, мы меняем пропускную способность на 10
million.|миллион.
Boom.|Бум.
And you see it starts now,|И вы видите, что это начинается сейчас,
the bounds are changing, your IP's going hey, what's going on?|границы меняются, ваш IP выходит. Эй, что происходит?
Right, and going up well, I said first we were going to do the ones going down okay,|Хорошо, и поднимаясь хорошо, я сказал сначала, что мы собираемся сделать те, которые идут вниз, хорошо,
then we'll do the ones going up.|тогда мы сделаем те, которые поднимаются.
So we did that add 001 here, we changed the bandwidth to 10 million,|Итак, мы добавили 001 здесь, мы изменили пропускную способность до 10 миллионов,
now we gonna do these two right here,|Теперь мы сделаем эти двое прямо здесь,
we're going to put it to 10 million.|мы собираемся довести его до 10 миллионов.
[BLANK_AUDIO]|[BLANK_AUDIO]
CuzI wanna make sure that it chooses that route.|Потому что я хочу убедиться, что он выбрал этот маршрут.
So S triple zero and F01, okay?|Итак, S тройной ноль и F01, хорошо?
And, make sure you guys can see that.|И убедитесь, что вы, ребята, это видите.
So Enable config, CONFIG T.|Итак, включите config, CONFIG T.
Was that S000?|Это была S000?
Yes, it was.|Да, было.
INTerface S0/0/0.|INTerface S0 / 0/0.
Bandwidth one, two, three.|Пропускная способность один, два, три.
One, two, no not, no, ten, one, two,|Один, два, нет, нет, десять, один, два,
three, one, two, three.|три, один, два, три.
Cool, and then the F01, Int F0/1.|Cool, а затем F01, Int F0 / 1.
Bandwidth 10, 123, 123.|Пропускная способность 10, 123, 123.
So we'll do WR, all right, let's minimize that.|Итак, мы сделаем WR, хорошо, давайте минимизируем это.
Close these two.|Закройте эти два.
Okay, now we're going to do F00 and F01.|Хорошо, теперь займемся F00 и F01.
10 million both, down here.|По 10 миллионов оба здесь.
Cuz remember, we're going to manipulate the bandwidth in order for it to make it go the way we wanna go,|Потому что помните, мы собираемся манипулировать пропускной способностью, чтобы заставить ее работать так, как мы хотим,
because bandwidth is a variable.|потому что пропускная способность - переменная.
It's a logical variable that we can manipulate.|Это логическая переменная, которой мы можем управлять.
We can't manipulate the delay.|Мы не можем управлять задержкой.
We can manipulate the, the bandwidth.|Мы можем управлять пропускной способностью.
CONFIGT INT f0/0, bandwidth 10 million, 10, 123123.|CONFIGT INT f0 / 0, пропускная способность 10 миллионов, 10, 123123.
[UNKNOWN] 01 [UNKNOWN] boom.|[НЕИЗВЕСТНО] 01 [НЕИЗВЕСТНО] бум.
Done deal with that one, DWR.|Готово с этим, DWR.
Now, I'm gonna go to this router right here, which is the F00, and the S00.|Теперь я перейду к этому маршрутизатору прямо здесь, это F00 и S00.
You're gonna see right here.|Вы увидите прямо здесь.
These two right here.|Эти двое прямо здесь.
10 million here, 10 million here.|10 миллионов здесь, 10 миллионов здесь.
And then the last one will be 10 million right there.|И тут последняя будет 10 миллионов.
That will finish everything off, so all zeros here.|Это все прикончит, поэтому здесь все нули.
So let's go ahead and change that.|Так что давайте изменим это.
[BLANK_AUDIO]|[BLANK_AUDIO]
And let's move it this way so you guys can see it.|И давайте переместим его сюда, чтобы вы, ребята, это увидели.
Okay, right there.|Хорошо, прямо здесь.
Enable CONFIG T, INTerface F0/0 Bandwidth 10 million.|Включите CONFIG T, INTerface F0 / 0 Пропускная способность 10 миллионов.
Oops, 10, 123, 123, okay, and then the Int S tripple zero and tap it again just in case,|Упс, 10, 123, 123, хорошо, а затем Int S сбрасывает ноль и снова нажимает на него на всякий случай,
cuz I hate when I'm interrupts the typing,|Потому что я ненавижу, когда я прерываю набор текста,
and I'd do it again.|и я сделаю это снова.
And then I will put the bandwidth of 10|А потом поставлю полосу 10
million, awesome, do WR.|миллион, офигенно, делай WR.
And then in this last router, we just gonna do that S001,|И затем в этом последнем маршрутизаторе мы просто сделаем S001,
that's it, that'll be the last one we do as far as 10 million, okay?|вот и все, это будет последнее, что мы сделаем до 10 миллионов, хорошо?
[BLANK_AUDIO]|[BLANK_AUDIO]
Enable, confi, CONFIG T, INT let me move it this way,|Enable, confi, CONFIG T, INT, позвольте мне переместить его сюда,
so you can see what I'm doing.|чтобы вы могли видеть, что я делаю.
INT S 001, 0/0/1,|INT S 001, 0/0/1,
Bandwidth 10, 123, 123.|Пропускная способность 10, 123, 123.
[SOUND] Do WR.|[ЗВУК] Сделайте WR.
All right and remember, you guys can do,|Хорошо и помните, вы, ребята, можете,
do WR.|делать WR.
You guys gotta go back to privilege mode and do Copy, Run, Start, Enter, Enter.|Вам, ребята, нужно вернуться в режим привилегий и выполнить Копирование, Выполнить, Пуск, Ввод, Ввод.
To do your stuff on the test, you can do,|Чтобы сделать свое дело на тесте, вы можете:
do and all tabs and stuff there, and do just, do it for the sake of time.|do и все вкладки и прочее там, и делай просто, делай это ради экономии времени.
Now what we're gonna do now we got from this point all the way around to that point, the bandwidth for each of these interfaces has changed to 10 million.|Теперь, что мы собираемся делать, мы получили от этого момента до этого момента, полоса пропускания для каждого из этих интерфейсов изменилась до 10 миллионов.
Now it should now pick, I mean we could really let's see if it or,|Теперь он должен выбрать, я имею в виду, мы действительно могли бы посмотрим, если это или,
and we don't have to even bother with the top,|и нам даже не нужно возиться с верхом,
we can just leave it alone, so we don't have to go around again.|мы можем просто оставить его в покое, чтобы не приходилось снова ходить.
Show IP route, it should have changed already, and it sure, you see that it did.|Покажите IP-маршрут, он уже должен был измениться, и вы наверняка видите, что это изменилось.
So good, we don't have to change the top,|Так хорошо, нам не нужно менять верх,
I mean cuz the top is one point 544 or 100.|Я имею в виду, потому что вершина составляет 544 или 100 баллов.
So we've really increased the, the bandwidth on the bottom quite a bit.|Так что мы действительно немного увеличили пропускную способность внизу.
So you can see it's already pointing before, okay, before it wasn't pointing to 29, it was pointing to 6, so now it's pointing to 29 meaning it's going down.|Итак, вы можете видеть, что он уже указывал раньше, хорошо, раньше он не указывал на 29, он указывал на 6, а теперь он указывает на 29, что означает, что он падает.
Take a look at the metric.|Взгляните на метрику.
It has changed, it has changed,|Он изменился, он изменился,
completely.|полностью.
It recalculated everything.|Он все пересчитал.
Let's take a look at the routing table.|Взглянем на таблицу маршрутизации.
Show all the topology table.|Показать всю таблицу топологии.
I'm sorry.|Мне жаль.
The topology table.|Таблица топологии.
For the 200.|Для 200.
Oh, look at that.|Ой, посмотрите на это.
The 200 only has one way to go.|У 200 есть только один путь.
One way to go, which is that way.|Один путь, и это тот путь.
It doesn't, you don't see any other way to go to the 200 but that 1, 10.1.1.29.|Нет, вы не видите другого способа перейти к 200, кроме этого 1, 10.1.1.29.
Since the bandwidth is so spread apart the, the remember I said that the feasible successor has to qualify, has to qualify.|Поскольку полоса пропускания так сильно разнесена, помните, я сказал, что возможный преемник должен соответствовать требованиям, должен соответствовать требованиям.
In this one, it couldn't qualify because I used to much of an extreme.|В этом он не мог пройти квалификацию, потому что я привык к крайностям.
There's no way that the advertised distance of one of the routers can compare to the feasible successors, feasible distance.|Невозможно сравнить заявленное расстояние одного из маршрутизаторов с возможными преемниками, допустимым расстоянием.
So there is no feasible successors.|Так что реальных преемников нет.
So let's take a look, and see what happens.|Итак, давайте посмотрим, что произойдет.
Well cool.|Ну круто.
We don't have to, and if we take a look at this writing table which we never have.|Нам не нужно, и если мы взглянем на этот письменный стол, которого у нас никогда не было.
We haven't done that yet.|Мы еще этого не сделали.
Let's see what this guy says.|Посмотрим, что говорит этот парень.
Ctrl+Z.|Ctrl + Z.
Let's take a look at the routing table,|Взглянем на таблицу маршрутизации,
Show IP ROUTE.|Показать IP-МАРШРУТ.
All right, and we got a 200.|Хорошо, и у нас есть 200.
I mean though, we need, we're trying to go to the 100,|Я имею в виду, что нам нужно, мы пытаемся выйти на 100,
and it says it's going via the 1.1.18, the 1.1.18.|и он говорит, что идет через 1.1.18, 1.1.18.
And where's the 1.1.18?|А где 1.1.18?
It's going down this way.|Это происходит вот так.
So once it hits this, it's going to come back down that way.|Итак, как только он попадет в это, он вернется туда.
All right.|Отлично.
Let's take a look at the topology table.|Взглянем на таблицу топологии.
Show.|Шоу.
Okay.|Ладно.
Show IP EIGRP TOPOLOGY.|Показать ТОПОЛОГИЮ IP EIGRP.
And we're looking for the 100 network, and there it is right here.|И мы ищем сеть 100, и вот она прямо здесь.
The 100 network, let's raise it up a little bit more so you guys can see that.|Сеть 100, давайте поднимем ее еще немного, чтобы вы, ребята, это увидели.
Here's the 100 network.|Вот сеть 100.
There's only one way to go, there's no feasible successor.|Есть только один путь, возможного преемника нет.
There is no, there it, it didn't qualify.|Нет, вот оно, не подходило.
So, you have no back-up route, so what,|Итак, у вас нет запасного маршрута, ну и что,
what's gonna happen?|что будет?
What will be, will there be a problem?|Что будет, будет проблема?
The only problem in this case is, since there is no feasible successor, so it can't query the topology table to just choose another route to get to,|Единственная проблема в этом случае заключается в том, что нет подходящего преемника, поэтому он не может запросить таблицу топологии, чтобы просто выбрать другой маршрут для доступа,
what it's gonna do, it's gonna have to do an update all the way across, gonna have to recalculate the whole thing, and then|что он будет делать, он должен будет полностью обновить его, пересчитать все, а затем
find how to get to the 100 network.|найти как попасть в сеть 100.
That will be the bad thing.|Это будет плохо.
Other than, other than that, that's it.|Кроме всего прочего, это все.
And the calculations is really quick, it's not as bad as OSPF.|И вычисления действительно быстрые, это не так плохо, как OSPF.
Only those routers will calculate that particular route and say,|Только эти маршрутизаторы рассчитают этот конкретный маршрут и скажут:
okay this is how you get to this particular area.|хорошо, вот как вы попадаете в эту конкретную область.
Only that one router, not every router.|Только этот маршрутизатор, а не каждый маршрутизатор.
So you can see there's only one way to get to that 100 network or one way to get to a 200 network, right?|Итак, вы видите, что есть только один способ добраться до этой сети 100 или один способ добраться до сети 200, верно?
Which is going down, not coming up, it's not going through a top route.|Которая идет вниз, не поднимается, не проходит по верхнему маршруту.
It's going through a bottom route, because we manipulated the bandwidth.|Он проходит по нижнему маршруту, потому что мы манипулировали пропускной способностью.
Now, since I took it to an extreme,|Теперь, когда я довел это до крайности,
I took it to a point where the feasible successor could not qualify.|Я довел дело до того, что возможный преемник не смог пройти квалификацию.
All right, so let's, let's see what's gonna happen.|Хорошо, давай, посмотрим, что произойдет.
Let's see if our calculations are correct.|Посмотрим, верны ли наши расчеты.
All right, so we go to simulation mode,|Хорошо, переходим в режим симуляции,
once again we take our simple PDU, we click on the PC0.|еще раз берем наш простой PDU, нажимаем на PC0.
Now remember last time we took up, it went up,|Теперь помните, когда мы в прошлый раз поднялись, он поднялся,
now it's gonna go down let's do auto capture and play.|Теперь он собирается упасть, давайте сделаем автоматический захват и сыграем.
Sit back and enjoy the fun.|Устройтесь поудобнее и наслаждайтесь весельем.
Let's see the moving, there's your PNG,|Посмотрим на движение, вот и ваш PNG,
[NOISE] straight down, okay.|[NOISE] прямо вниз, хорошо.
Slow and it's 10 million, and it's still going slow, all right.|Медленно, и это 10 миллионов, и он все еще идет медленно, хорошо.
Either channel, right?|Любой канал, верно?
No, no, it's going across the area network here, supposedly.|Нет-нет, якобы здесь идет по локальной сети.
All right come on.|Хорошо, давай.
Now it goes there, goes to the PC, and it should come back the same way.|Теперь он идет туда, идет на ПК и должен возвращаться таким же образом.
It should come back the same way.|Он должен вернуться таким же образом.
This is just showing you,|Это просто показывает вам,
that's, that bandwidth is actually something that we can manipulate.|То есть, эта пропускная способность - это то, чем мы можем управлять.
So when you're doing EIGRP these are ways that you can tweak it to.|Итак, когда вы выполняете EIGRP, это способы, которые вы можете настроить.
Make the packet go the way you want it to go and it is, it is.|Сделайте так, чтобы пакет пошел так, как вы хотите, и он есть.
We changed it, so now it's going the way that we actually told it to based on bandwidth.|Мы изменили его, так что теперь все идет так, как мы на самом деле сказали, в зависимости от пропускной способности.
So there you go, that's what I wanted to show you not only did I show you that you can tweak it, by changing the bandwidth, and|Итак, вот что я хотел показать вам, я не только показал вам, что вы можете настроить его, изменив пропускную способность, и
I changed it just on one side to a obviously an extreme, but I changed it.|Я изменил его только с одной стороны до явно крайнего, но я изменил его.
But as well that hey,|Но как хорошо, что эй,
there was no feasible successor cuz it couldn't qualify, it couldn't qualify.|не было подходящего преемника, потому что он не мог пройти квалификацию, он не мог пройти квалификацию.
And now, if one of these links goes down,|А теперь, если одна из этих ссылок перестанет работать,
then it would actually have to recalculate those routers, and I go oh, my God.|тогда он действительно должен был бы пересчитать эти маршрутизаторы, и я иду, боже мой.
Let me send out again, updates, to find out, it goes active and say, hey, I need to find where is a way to get 200.|Позвольте мне снова разослать обновления, чтобы узнать, он становится активным и говорю: «Эй, мне нужно найти способ получить 200».
So a lot of math needs to happen at that point, to find the whole thing.|Так что на этом этапе нужно провести много математики, чтобы найти все.
If there was a feasible successor,|Если бы был возможный преемник,
all they had to do was query this topology table, and then we choose from there.|все, что им нужно было сделать, это запросить эту таблицу топологии, а затем мы сделаем выбор.
So again, it's all based on how you set up your network?|Опять же, все зависит от того, как вы настраиваете свою сеть?
And if you are gonna mess around with the bandwidth, how far do you go?|И если вы собираетесь возиться с пропускной способностью, как далеко вы зайдете?
But again, that is beyond the CCNA, all you need to be concerned about is hey,|Но опять же, это выходит за рамки CCNA, все, о чем вам нужно беспокоиться, это эй,
bandwidth is what we can change.|пропускная способность - это то, что мы можем изменить.
There you go, now you're really seeing every part of EIGRP that you need to know to pass that cert.|Итак, теперь вы действительно видите каждую часть EIGRP, которую вам нужно знать, чтобы пройти этот сертификат.
I'll see you in the next lecture.|Увидимся на следующей лекции.
[BLANK_AUDIO]|[BLANK_AUDIO]