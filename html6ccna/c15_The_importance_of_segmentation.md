D:\mailCloud\prjother\tmp\1\c15_The importance of segmentation.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
All righty then.|Тогда ладно.
In our previous lesson, we touched upon collision domains and broadcast domains.|В нашем предыдущем уроке мы коснулись коллизионных доменов и широковещательных доменов.
The importance of segmenting a network.|Важность сегментации сети.
And as Cisco professionals, networking professionals,|И как профессионалы Cisco, сетевые профессионалы,
network engineers, that we all are striving for.|сетевых инженеров, к которым мы все стремимся.
We must learn how to segment.|Мы должны научиться сегментировать.
We must segment.|Мы должны сегментировать.
Now here, we have a little simple lab that we usually do and what we have,|Теперь у нас есть небольшая простая лаборатория, которую мы обычно делаем и что у нас есть,
we have three switches here.|у нас здесь три переключателя.
Three switches here and we're going between two routers.|Здесь три коммутатора, и мы идем между двумя маршрутизаторами.
Now you can see here, I don't know if you can or not, let me zoom in a little bit.|Теперь вы можете видеть здесь, я не знаю, можете вы или нет, позвольте мне немного увеличить.
If my finger is on point here.|Если мой палец попал в точку.
I think it doesn't matter that this side disappears,|Думаю, не имеет значения, что эта сторона исчезает,
at least you can see this one right here.|по крайней мере, вы можете увидеть это прямо здесь.
Let me scroll up a little bit though.|Но позвольте мне прокрутить немного вверх.
I know my finger's not gonna do that, I'm gonna get right there.|Я знаю, что мой палец этого не сделает, я сейчас пойду.
All right.|Отлично.
So you see that VLAN one and we said that VLAN one was what?|Итак, вы видите тот VLAN один, и мы сказали, что это VLAN один?
Was what?|Что было?
Was what?|Что было?
Was the default VLAN.|Была VLAN по умолчанию.
All right.|Отлично.
Now we have VLAN one and VLAN 100.|Теперь у нас есть VLAN 1 и VLAN 100.
So right there, we have three separate networks.|Итак, у нас есть три отдельные сети.
Three separate networks that really could not talk to each other.|Три отдельные сети, которые действительно не могли общаться друг с другом.
So whatever happens in this particular network right here, stays in here.|Итак, что бы ни происходило в этой конкретной сети прямо здесь, остается здесь.
Because when PC3, let's say wants to talk to PC0, they're in the same network,|Потому что, когда ПК3, скажем, хочет поговорить с ПК0, они находятся в одной сети,
they're in the 100 network.|они в сети 100.
So if, lets say this is IP address is coincides this computer here, desktop, what is, what is this?|Итак, если, допустим, это IP-адрес, он совпадает с этим компьютером, настольным компьютером, что это такое, что это?
Just hold on there, desktop, password,|Просто держись там, рабочий стол, пароль,
okay.|Ладно.
100.1, so the other computer must be 102.|100.1, поэтому другой компьютер должен быть 102.
So, if computer one wants to talk to computer two, it's no need for it to go to the gateway.|Итак, если первый компьютер хочет поговорить с вторым компьютером, ему не нужно обращаться к шлюзу.
It's gonna go hide in stay right in here,|Он собирается спрятаться, оставаясь здесь,
cuz it has a list.|потому что у него есть список.
So they'll talk to each other and ma, that is gonna stop right at the switch.|Так что они будут говорить друг с другом, и мама остановится прямо у переключателя.
No need to get out.|Не нужно выходить.
The only time that it will go out to a gateway, if we wanted to talk to the 100.|Единственный раз, когда он выйдет на шлюз, если мы хотим поговорить с сотней.
So you can do whatever you want here.|Так что вы можете делать здесь все, что хотите.
This could be one classroom, this could be another classroom what have you and you're doing all your networks.|Это может быть один класс, это может быть другой класс, который у вас есть, и вы делаете все свои сети.
This could be one floor, this could be another floor.|Это может быть один этаж, это может быть другой этаж.
However, is that you wanna do it.|Однако вы хотите это сделать.
But you see that VLAN are really a crucial,|Но вы видите, что VLAN действительно важны,
vital instrument in our arsenal for networking that we want to go ahead and use.|жизненно важный инструмент в нашем арсенале для создания сетей, который мы хотим использовать.
All right?|Отлично?
And I'll create these VLANs.|И я создам эти VLAN.
And normally, we leave VLAN one alone, you know, technically, even though they say,|И обычно мы оставляем VLAN one в покое, понимаете, технически, даже если они говорят:
you should change VLAN one.|вам следует изменить VLAN один.
Rename VLAN one into something else for security purposes.|В целях безопасности переименуйте VLAN one во что-нибудь другое.
But I left VLAN one alone and I put a laptop up there like, you know,|Но я оставил одну VLAN в покое и поставил туда ноутбук, как вы знаете,
the IT guy.|айтишник.
So he's on VLAN one, but you have two different VLANs down here.|Итак, он находится в VLAN один, но у вас здесь две разные VLAN.
Now you only see, now, think about this, I want you to think about this good,|Теперь вы только видите, теперь подумайте об этом, я хочу, чтобы вы думали об этом добре,
cuz this is something that will come up or may come up on your examination.|Потому что это то, что придет или может появиться на вашем экзамене.
You have only one connection, going from your switch to your router.|У вас есть только одно соединение, идущее от коммутатора к маршрутизатору.
How is that possible?|Как такое возможно?
You have three different networks.|У вас есть три разные сети.
So that means each network, it has to have a different gateway.|Это означает, что каждая сеть должна иметь свой шлюз.
Well, as I'll show you in a little bit.|Ну, как я вам немного покажу.
We create some interfaces for that.|Мы создаем для этого несколько интерфейсов.
All right?|Отлично?
But again, what I'm trying to show you here is that now we have one, two, three.|Но опять же, я пытаюсь показать вам, что теперь у нас есть один, два, три.
Okay.|Ладно.
One, two, three, four.|Один два три четыре.
Right there, you wanted to count that,|Прямо здесь вы хотели это посчитать,
that other connection.|та другая связь.
You have four broadcast domain or you have one, two, three broadcast domains.|У вас четыре широковещательных домена или один, два, три широковещательных домена.
All right.|Отлично.
If you wanna exclude that that serial connection there.|Если вы хотите исключить это последовательное соединение.
One, two, three.|Раз два три.
Each network, get its own broadcast domain.|Каждая сеть получает свой собственный широковещательный домен.
That will be another network over there,|Там будет другая сеть,
as well.|также.
So let's say, right here in this pyramid,|Итак, скажем, прямо здесь, в этой пирамиде,
we have three broadcast domains.|у нас есть три широковещательных домена.
How many collision, how many collision domains do we have?|Сколько коллизий, сколько у нас доменов коллизий?
We have one, cuz remember, everything connected to a switch,|У нас есть один, потому что помните, все подключено к переключателю,
if it's all collision domains.|если это все домены коллизии.
We have one, two, three, four, five, six,|У нас есть один, два, три, четыре, пять, шесть,
seven, eight.|семь восемь.
Cuz everything connected to the switch,|Потому что все, что связано с переключателем,
it's, its own collision domain.|это его собственная область коллизий.
We have eight collision domains.|У нас есть восемь коллизионных областей.
We have three different broadcast domains right here.|У нас есть три разных широковещательных домена.
We segmented the network.|Мы сегментировали сеть.
So now whatever happens in that particular VLAN, stays there.|Итак, теперь все, что происходит в этой конкретной VLAN, остается там.
And one of the most important things is that I've come across in schools let's say, the IT department.|И одна из самых важных вещей - это то, что я встречал в школах, скажем, в ИТ-отделе.
Let's say, these are classrooms and let's say, there's 24 PCs here and we're in different VLAN's.|Допустим, это классы и, допустим, здесь 24 компьютера, и мы находимся в разных VLAN.
Well, that's okay.|Ну ничего страшного.
If you wanted to image, all the computers that exist in this VLAN, that's okay.|Если вы хотите создать образ всех компьютеров в этой VLAN, ничего страшного.
Cuz you won't bother these VLANs.|Потому что вы не будете беспокоить эти VLAN.
You simply are going to send them to this VLAN and they'll never the wiser, they'll never the wiser.|Вы просто собираетесь отправить их в эту VLAN, и они никогда не станут мудрее, они никогда не станут мудрее.
Before when, and people don't take advantage of this and I've seen it.|Раньше когда, и люди этим не пользовались, и я это видел.
That they don't create the VLAN, we're all part of the default VLAN,|Что они не создают VLAN, мы все являемся частью VLAN по умолчанию,
whichever that may be.|что бы это ни было.
Management VLAN, administrative VLAN,|Management VLAN, административная VLAN,
native VLAN,|собственный VLAN,
which is usually the VLAN one.|обычно это VLAN.
Well, [UNKNOWN], the IT guy decides.|Что ж, [НЕИЗВЕСТНО], решает айтишник.
Hey, I'm gonna go ahead and image these 24|Эй, я собираюсь представить эти 24
computers.|компьютеры.
There goes your network.|Вот и ваша сеть.
All bandwidth goes [NOISE] down to a crawl,|Вся полоса пропускания снижается [NOISE] до сканирования,
cuz you've got students that are doing research online.|Потому что у вас есть студенты, которые проводят исследования в Интернете.
You have other students in networking that are creating,|У вас есть другие ученики в сети, которые создают,
you know, [UNKNOWN] servers or what have you.|ну знаете, [НЕИЗВЕСТНЫЕ] серверы или что там у вас.
All right.|Отлично.
So you've got a lot of things going on in that network and now on top of that,|Итак, у вас много чего происходит в этой сети, и теперь, помимо этого,
maybe you have faculty that are putting in grades or sending reports.|возможно, у вас есть преподаватели, которые выставляют оценки или отправляют отчеты.
Or students taking tests online or throughout the network.|Или студенты, сдающие тесты онлайн или по сети.
So, all that traffic just now went to a crawl.|Итак, весь этот трафик только что пропал.
So this is why we want to segment.|Вот почему мы хотим сегментировать.
And this is how you, one of the ways, all right?|А это как у вас, один из способов, ладно?
That you would segment.|Это вы бы сегментировали.
And this is the kind of topology, if you would,|И вот такая топология, если хотите,
that you're going to see when you get to your examination.|что вы увидите, когда придете на экзамен.
This is what's called, because you have one router and you have multiple networks and each one needs a gateway.|Это так и называется, потому что у вас есть один маршрутизатор, несколько сетей, и каждой из них нужен шлюз.
It's a router on a stick, but more importantly than that is that you segment your network at layer two by creating more broadcast domains and|Это маршрутизатор на палке, но что более важно, вы сегментируете свою сеть на втором уровне, создавая больше широковещательных доменов и
that's what you want you want to create more broadcast domains.|это то, что вы хотите, вы хотите создать больше широковещательных доменов.
Now people tell me, hey Laz, are you gonna, can I make,|Теперь люди говорят мне, Эй, Лаз, ты собираешься, я могу сделать,
let's say VLAN two and VLAN three on the same switch?|скажем, VLAN два и VLAN три на одном коммутаторе?
My response to that is hey, how big is your network?|Я отвечаю на это: "Эй, насколько велика ваша сеть?"
And that's all you got?|И это все, что у тебя есть?
All you got is two departments?|У тебя всего два отдела?
You got one switch, you got maybe 60|У тебя есть один переключатель, у тебя может быть 60
employees.|сотрудники.
Okay.|Ладно.
That's fine.|Это хорошо.
Not gonna overkill it, you know, make a switch per department,|Знаете, не переборщите, переключитесь на отдел,
you could go ahead and do that.|вы можете пойти дальше и сделать это.
But if you have a medium size to, you know, large network,|Но если у вас средняя или большая сеть,
you wanna make sure that each department has their own switch and that switch every port on that switch should be part of that particular VLAN.|вы хотите убедиться, что у каждого отдела есть собственный коммутатор, и каждый порт этого коммутатора должен быть частью этой конкретной VLAN.
That's the way it should be on a larger scale.|Так и должно быть в большем масштабе.
On a very small scale, like we saw earlier.|В очень маленьком масштабе, как мы видели ранее.
Like that office that I drew in Visio that had only three offices.|Как тот офис, который я нарисовал в Visio, в котором было всего три офиса.
You had the receptionist and the little conference area.|У вас был администратор и небольшая конференц-зона.
Yeah, that's fine.|Да ладно.
You can have, you know, 1, 24 port, even 48 port switch.|Вы можете иметь коммутатор на 1, 24 или даже 48 портов.
And you can segment each, you know,|И вы можете сегментировать каждый, знаете,
section for, you know,|раздел для, вы знаете,
four ports or six ports per office.|четыре порта или шесть портов на офис.
However, you want to do it.|Однако вы хотите это сделать.
You can do that on a small network.|Вы можете сделать это в небольшой сети.
Just remember, in a real world scenario,|Просто помните, что в реальном мире
you're looking,|ты смотришь,
what is it I keep thinking of growth,|что это я все время думаю о росте,
growth, growth.|рост, рост.
You don't want to get caught.|Вы не хотите, чтобы вас поймали.
All of a sudden, you run out of ports.|Внезапно у вас заканчиваются порты.
Now you got to buy another switch and you need an IP scheme and another [INAUDIBLE], so don't want to catch yourself that way.|Теперь вам нужно купить еще один коммутатор, и вам нужна IP-схема и еще один [НЕРАЗБОРЧИВО], так что не хотите ловить себя на этом.
So, always think of growth.|Так что всегда думайте о росте.
You'd rather have more than less, all right?|Вы бы предпочли больше, чем меньше, хорошо?
More than less.|Более чем меньше.
Then you need to explain that.|Тогда вам нужно это объяснить.
But definitely, one of the things you need to explain that your network is going to work more efficient by you creating more broadcast domains.|Но определенно одна из вещей, которые вам нужно объяснить, что ваша сеть будет работать более эффективно, если вы создадите больше широковещательных доменов.
Increasing the amount of broadcast domains.|Увеличение количества широковещательных доменов.
Increasing the amount of collisional maintenance by using switches,|Увеличение объема обслуживания при столкновении с помощью переключателей,
cuz now you have the full duplicates that we talked about before.|Потому что теперь у вас есть полные дубликаты, о которых мы говорили раньше.
Now what ever happens in that VLAN, stays in that VLAN.|Теперь все, что происходит в этой VLAN, остается в этой VLAN.
But do not fall into the pit into the,|Но не упади в яму в,
the pitfall or the trap that your VLAN.|ловушка или ловушка в вашей VLAN.
Now you have 200 machines in that B-line.|Теперь у вас есть 200 машин в этой B-линии.
Well, now you're defeating the purpose,|Что ж, теперь ты побеждаешь цель,
you're shooting yourself in the foot.|вы стреляете себе в ногу.
You don't want that, you want your VLANs to get big.|Вы не хотите этого, вы хотите, чтобы ваши VLAN становились большими.
Is there a, a particular number?|Есть какое-то конкретное число?
To be quite honest with you, I don't know off the top of my head, but I wouldn't go any further than 48.|Честно говоря, я не знаю, в голове ли, но я бы не пошел дальше 48.
All right?|Отлично?
48 for switches.|48 для переключателей.
[LAUGH] You don't wanna have a whole bunch of people crammed into one VLAN,|[LAUGH] Вы же не хотите, чтобы целая группа людей была втиснута в одну VLAN,
cuz then you are gonna run into the same problem.|Потому что тогда вы столкнетесь с той же проблемой.
All right?|Отлично?
Broadcast, everybody's in there.|Трансляция, все там.
But definitely, they're very versatile.|Но определенно они очень универсальны.
So segmentation is really, really important.|Так что сегментация действительно очень важна.
And you can see, let's say, between these two routers and we have the same thing on the other side.|И вы можете видеть, скажем, между этими двумя маршрутизаторами, и у нас есть то же самое на другой стороне.
Same thing on the other side.|То же самое и с другой стороны.
We're going across campuses lets say.|Скажем так, мы проходим через кампусы.
This is a wide area network and that's usually what this represents,|Это глобальная сеть, и обычно это означает,
even though we're really not using our cloud or anything like that.|хотя мы действительно не используем наше облако или что-то в этом роде.
We're connecting that directly.|Мы подключаем это напрямую.
We'll pretend it's a wide area network.|Представим, что это глобальная сеть.
You know, these routers are gonna send the information across.|Вы знаете, эти маршрутизаторы будут пересылать информацию.
And again, you have your VLANs are segmented down here.|И снова, здесь ваши VLAN сегментированы.
VLAN 102 and you have I forgot to change here.|VLAN 102 а у вас я забыл поменять здесь.
There's 103, I'm sorry.|Там 103, извини.
This should be VLAN 103, I forgot to change it down here.|Это должен быть VLAN 103, я забыл изменить его здесь.
This is VLAN 102 and then you've got your 101 over there.|Это VLAN 102, а потом у вас есть 101.
All right?|Отлично?
So definitely, segmentation, segmentation,|Итак, определенно, сегментация, сегментация,
segmentation.|сегментация.
That needs to happen.|Это должно произойти.
One of the best ways,|Один из лучших способов,
one of the best ways that you could do that is by using that tool, that VLAN.|один из лучших способов сделать это - использовать этот инструмент, эту VLAN.
All right?|Отлично?
And it's gonna increase your bandwidth.|И это увеличит вашу пропускную способность.
It's going to increase your security.|Это повысит вашу безопасность.
It's going to increase your flexibility and scalability of your network.|Это повысит вашу гибкость и масштабируемость вашей сети.
So make use of that tool that you already have in that arsenal.|Так что используйте тот инструмент, который у вас уже есть в арсенале.
So segment your network.|Так что сегментируйте свою сеть.
I'll see you in the next session.|Увидимся на следующем сеансе.
[BLANK_AUDIO]|[BLANK_AUDIO]
[BLANK_AUDIO]|[BLANK_AUDIO]
All righty then.|Тогда ладно.
In our previous lesson, we touched upon collision domains and broadcast domains, the importance of segmenting a network.|В нашем предыдущем уроке мы коснулись коллизионных доменов и широковещательных доменов, а также важности сегментации сети.
And as Cisco professionals, networking professionals, network engineers,|И как профессионалы Cisco, сетевые специалисты, сетевые инженеры,
that we all are striving for, we must learn how to segment, we must segment.|к чему мы все стремимся, мы должны научиться сегментировать, мы должны сегментировать.
Now here, we have a little simple lab that we usually do and what we have, we have three switches here, three switches here,|Итак, у нас есть небольшая простая лаборатория, которую мы обычно делаем, и то, что у нас есть, у нас есть три переключателя здесь, три переключателя здесь,
and we're going between two routers.|и мы идем между двумя маршрутизаторами.
Now you can see here, I don't know if you can or not, let me zoom in a little bit and my finger is on point here.|Теперь вы можете видеть здесь, я не знаю, можете вы или нет, позвольте мне немного увеличить масштаб, и мой палец здесь находится на точке.
I think it doesn't matter if the other side disappears,|Я думаю, неважно, исчезнет ли другая сторона,
at least you can see this one right here.|по крайней мере, вы можете увидеть это прямо здесь.
Let me scroll up a little bit though, I know my finger's not gonna do that,|Позвольте мне прокрутить немного вверх, я знаю, что мой палец этого не сделает,
so I'm gonna, yeah, right there.|так что я собираюсь, да, прямо здесь.
All right, so see, you have v-line one and we said that v-line one was what?|Хорошо, так что видите, у вас есть v-line one, и мы сказали, что v-line one было что?
Was what?|Что было?
Was what?|Что было?
Was the default VLAN.|Была VLAN по умолчанию.
All right, and we have VLAN 101, and VLAN 100.|Хорошо, и у нас есть VLAN 101 и VLAN 100.
So right there, we have three separate networks.|Итак, у нас есть три отдельные сети.
Three separate networks that really can now talk to each other.|Три отдельные сети, которые теперь действительно могут общаться друг с другом.
So whatever happens in this particular network right here, stays in here.|Итак, что бы ни происходило в этой конкретной сети прямо здесь, остается здесь.
Because when PC3, let's say, wants to talk to PC0, they're in the same network,|Потому что, когда ПК3, скажем, хочет поговорить с ПК0, они находятся в одной сети,
they're in the 100 network.|они в сети 100.
So if, let's say this is, let me see what P address this is.|Итак, если, допустим, это так, позвольте мне посмотреть, что это за адрес P.
Go inside this computer here, desktop,|Зайди в этот компьютер, настольный компьютер,
what's, what's, what is this.|что, что, что это.
Just hold on there, desktop, that's okay 100.1 so the other computer must be 102.|Просто подождите, настольный компьютер, это нормально, 100.1, поэтому другой компьютер должен быть 102.
So if computer one wants to talk to computer two there's no need for it to go to the gateway, it's gonna go ahead and stay right in here.|Так что, если первый компьютер хочет поговорить с вторым компьютером, ему не нужно идти к шлюзу, он пойдет дальше и останется здесь.
Because it has a list, so they'll talk to each other that is gonna stop right at the switch and that means to get out.|Потому что у него есть список, поэтому они будут разговаривать друг с другом, что остановится прямо у переключателя, а это значит, что нужно уйти.
The only time that it will go out to the gateway if it wanted to talk to the 100.|Единственный раз, когда он выйдет на шлюз, если он захочет поговорить со 100.
So you can do whatever you want here, this can be one classroom,|Так что вы можете делать здесь все, что хотите, это может быть один класс,
this can be another classroom or what have you.|это может быть другой класс или что у вас есть.
And you're doing all your networks, this could be one floor,|И вы делаете все свои сети, это может быть один этаж,
this could be another floor.|это мог быть другой этаж.
However it is that you wanna do it but you see that VLANs are really a crucial,|Однако вы хотите это сделать, но видите, что VLAN действительно имеют решающее значение,
vital, instrument in our arsenal for networking that we want to go ahead and use, all right?|жизненно важный инструмент в нашем арсенале для создания сетей, который мы хотим использовать и дальше, хорошо?
And I'll create these VLANs and normally we'll leave VLAN 1 alone, you know,|И я создам эти VLAN, и обычно мы оставляем VLAN 1 в покое, понимаете,
technically even though they say you should change VLAN 1,|технически даже если они говорят, что вам следует изменить VLAN 1,
rename VLAN 1 into something else for security purposes.|переименуйте VLAN 1 во что-нибудь другое в целях безопасности.
But I left VLAN 1 alone, and I put a laptop up there, like, you know,|Но я оставил VLAN 1 в покое и поставил туда ноутбук, ну, знаете,
the IT guy.|айтишник.
So, he's on VLAN 1 but you have two different VLANs down here.|Итак, он находится в VLAN 1, но у вас здесь две разные VLAN.
Now, you only see, now, think about this,|Теперь вы только видите, теперь подумайте об этом,
I want you to think about this good,|Я хочу, чтобы ты подумал об этом добре,
cuz this is something that will come up or may come up on your examination.|Потому что это то, что придет или может появиться на вашем экзамене.
You have only one connection going from your switch to your router,|У вас есть только одно соединение от коммутатора к маршрутизатору,
how is that possible?|как это возможно?
You have three different networks, so it means each network has to be, it has to have a different gateway.|У вас есть три разные сети, поэтому это означает, что каждая сеть должна быть, у нее должен быть свой шлюз.
Well, as I'll show you in a little bit, we create some interfaces for that,|Что ж, как я покажу вам немного позже, мы создаем для этого несколько интерфейсов,
all right?|отлично?
But again, what I'm trying to show you is that now we have one, two, three, okay?|Но опять же, я пытаюсь показать вам, что теперь у нас есть один, два, три, хорошо?
One, two, three, four, right there you want it to count that, that other connection.|Один, два, три, четыре, прямо здесь вы хотите, чтобы он посчитал это, это другое соединение.
We have four broadcast domains or you have one, two, three broadcast domains.|У нас есть четыре широковещательных домена или у вас один, два, три широковещательных домена.
All right, if you wanna exclude that, that serial connection there.|Хорошо, если вы хотите исключить это, то последовательное соединение там.
One, two, three, each network is its own broadcast domain,|Один, два, три, каждая сеть - это собственный домен вещания,
now will be another network over there as well.|теперь там будет и другая сеть.
So let's say right here in this permit, we have 3 broadcast domains,|Итак, допустим, прямо здесь, в этом разрешении, у нас есть 3 широковещательных домена,
how many collision?|сколько столкновений?
How many collision domains do we have?|Сколько у нас коллизионных доменов?
We have one, because remember,|У нас есть один, потому что помните,
everything connected to a switch is it's own collision domains,|все, что связано с коммутатором, - это его собственные домены столкновения,
we have one, two, three, four, five, six,|у нас есть один, два, три, четыре, пять, шесть,
seven,|Семь,
eight because everything connected to the switch is its own collision domain.|восемь, потому что все, что связано с коммутатором, является его собственной областью конфликтов.
We have eight collision domains, we have three different broadcast domains.|У нас восемь коллизионных доменов, у нас есть три разных широковещательных домена.
Right here we segmented the network, so now whatever happens in that particular VLAN stays there.|Прямо здесь мы сегментировали сеть, так что теперь все, что происходит в этой конкретной VLAN, остается там.
And one of the most important things is,|И одна из самых важных вещей -
that I've come across,|что я встретил,
in schools let's say the IT department.|в школах скажем ИТ-отдел.
Let's say these are classrooms and let's say there's 24 PCs here.|Допустим, это классы, и допустим, здесь 24 компьютера.
And we're in different VLANs, well, that's okay.|И мы находимся в разных VLAN, ну это нормально.
If you wanted to image all the computers that exist in this VLAN,|Если вы хотите создать образ всех компьютеров, которые существуют в этой VLAN,
that's okay, cuz you won't bother this VLAN.|это нормально, потому что вы не будете беспокоить эту VLAN.
You simply are gonna send them to this VLAN and they'll never be the wiser, they'll never be the wiser.|Вы просто отправите их в эту VLAN, и они никогда не станут мудрее, они никогда не станут мудрее.
Before, when and people don't take advantage of this, and I've seen it, that they don't create the VLAN.|Раньше, когда и люди не использовали это в своих интересах, и я видел это, они не создают VLAN.
We're all part of the default VLAN,|Мы все являемся частью VLAN по умолчанию,
whichever that may be.|что бы это ни было.
Management VLAN, administrative VLAN,|Management VLAN, административная VLAN,
native VLAN which is usually VLAN 1.|собственный VLAN, обычно это VLAN 1.
We're all fall in the same one, the IT guy decides, hey,|Мы все попадаем в одну точку, айтишник решает, эй,
I'm going to go add an image these 24|Я собираюсь добавить изображение этих 24
computers.|компьютеры.
There goes your network, all band width goes [NOISE].|Вот и ваша сеть, вся полоса пропускания [ШУМ].
Down to a crawl cuz you got students that are doing research online.|Вплоть до ползания, потому что у вас есть студенты, которые проводят исследования в Интернете.
You have other students in networking that are creating the ICP servers or what have you, all right?|У вас есть другие студенты, изучающие сети, которые создают серверы ICP, или что у вас, хорошо?
So you got a lot of things going on right now we're gonna add on top of that.|Итак, у вас сейчас много чего происходит, мы добавим к этому.
Maybe you have faculty there are putting in grades, or sending reports, or students taking tests online, or throughout their network.|Возможно, у вас есть преподаватели, которые выставляют оценки или отправляют отчеты, или студенты сдают тесты в Интернете или по всей своей сети.
So all that traffic just now went to a crawl.|Так что весь этот трафик только что пропал.
So this is why we want to segment and this is how you, one of the ways, all right?|Так вот почему мы хотим сегментировать, и вот как вы, один из способов, хорошо?
That you would segment and this is the kind of topology,|Что вы будете сегментировать, и это такая топология,
if you would, that you're going to see when you get to your examination.|если да, то это вы увидите, когда придете на экзамен.
This is what's called, because you have one router and you have multiple networks and each one needs a gateway, it's a router on a stake.|Это так и называется, потому что у вас есть один маршрутизатор, и у вас несколько сетей, и каждой из них нужен шлюз, это маршрутизатор на ставке.
But more importantly than that, is that you segment your network at layer two by creating more broadcast domains.|Но что более важно, вы сегментируете свою сеть на втором уровне, создавая больше широковещательных доменов.
And that's what you want, you want to create more broadcast domains.|И это то, что вы хотите, вы хотите создать больше широковещательных доменов.
Now people tell me, hey, [UNKNOWN].|Теперь люди говорят мне, эй, [НЕИЗВЕСТНО].
Are you gonna, can I make, like, say, VLAN 2 and VLAN 3 on the same switch?|Вы собираетесь, я могу сделать, например, VLAN 2 и VLAN 3 на одном коммутаторе?
My response to that is, hey, how big is your network?|Мой ответ: эй, насколько велика ваша сеть?
And that's all you got, all you got is two departments.|И это все, что у вас есть, это два отдела.
You got one switch, you got maybe 60|У тебя есть один переключатель, у тебя может быть 60
employees.|сотрудники.
Okay, that's fine, not gonna overkill it,|Хорошо, это нормально, не переборщить,
you know,|знаешь,
make a switch per department you can go ahead and do that.|сделайте переключение в каждом отделе, вы можете пойти дальше и сделать это.
But if you have medium size to, you know,|Но если у вас средний размер, вы знаете,
large network, you wanna make sure that each department has their own switch.|большая сеть, вы хотите, чтобы у каждого отдела был свой коммутатор.
And that switch, every port on that switch should be part of that particular VLAN, that's the way it should be on a larger scale.|И этот коммутатор, каждый порт на этом коммутаторе должен быть частью этой конкретной VLAN, так и должно быть в большем масштабе.
On a very small scale like we saw earlier,|В очень маленьком масштабе, как мы видели ранее,
like that office that I drew in Visio,|как тот офис, который я нарисовал в Visio,
that had only three offices.|в котором было всего три отделения.
You had the receptionist and the little conference area, you know,|У вас была регистратор и небольшая конференц-зона, знаете ли,
that's fine you can have, you know, one 24|это нормально, ты знаешь, один 24
port even 48 port switch.|порт даже коммутатор 48 портов.
And you can segment each, you know,|И вы можете сегментировать каждый, знаете,
section for you know, 4 ports or 6 ports per office, however it is that you want to do it.|раздел, как вы знаете, 4 порта или 6 портов на офис, но это то, что вы хотите сделать.
You can't do that on a small network, just remember, in a real world scenario,|Вы не можете сделать это в небольшой сети, просто помните, что в реальном мире
you're looking, you always got to keep thinking of growth, growth, growth.|вы смотрите, вы всегда должны думать о росте, росте, росте.
You don't want to get caught, now assign,|Вы не хотите, чтобы вас поймали, теперь назначьте,
now you run out of ports,|Теперь у вас закончились порты,
now you gotta buy another switch and, you know, IP scheme and now I've gotta create another VLAN.|Теперь вам нужно купить еще один коммутатор и, вы знаете, схему IP, и теперь мне нужно создать еще одну VLAN.
So you want kinda catch yourself that way.|Так что ты хочешь поймать себя на этом.
So always think of growth.|Так что всегда думайте о росте.
You'd rather have more than less, all right?|Вы бы предпочли больше, чем меньше, хорошо?
More than less and you need to explain that.|Более чем меньше, и вам нужно это объяснить.
But definitely one of the things that you need to explain is that your network is going to work more efficient while you're|Но, безусловно, одна из вещей, которую вам нужно объяснить, - это то, что ваша сеть будет работать более эффективно, пока вы
creating more broadcast domains.|создание большего количества широковещательных доменов.
Increasing the amount of broadcast domains.|Увеличение количества широковещательных доменов.
Increasing the amount of collision domains by using switches.|Увеличение количества конфликтных доменов с помощью переключателей.
Because now you have the four duplex that we talked about before.|Потому что теперь у вас есть четыре дуплекса, о которых мы говорили раньше.
Now, whatever happens in that VLAN, stays in that VLAN but do not fall into the pit into the pitfall or the trap that your VLAN, now you have 200|Теперь, что бы ни происходило в этой VLAN, остается в этой VLAN, но не попадет в яму, в ловушку или ловушку, в которую ваша VLAN, теперь у вас 200
machines in that VLAN.|машины в этой VLAN.
Well now you, you're defeating the purpose,|Ну, теперь ты побеждаешь цель,
you're shooting yourself in the foot.|вы стреляете себе в ногу.
You don't want that, you don't want your VLANs to get big.|Вы не хотите этого, вы не хотите, чтобы ваши VLAN становились большими.
Is there a particular number?|Есть конкретный номер?
To be quite honest with you, I don't know off the top of my head but we're not going to go any further than 48.|Честно говоря, я не знаю в голове, но мы не собираемся идти дальше 48.
All right, [LAUGH] 48, 4 switches.|Хорошо, [СМЕХ] 48, 4 переключателя.
You don't wanna have a whole bunch of people crammed in to one VLAN cuz then you are going to run into the same problem, right?|Вы же не хотите, чтобы целая группа людей была втиснута в одну VLAN, потому что тогда вы столкнетесь с той же проблемой, верно?
Broadcast, everybody's in there but definitely they're very versatile.|Вещание, все присутствуют, но определенно они очень разносторонние.
So segmentation is really, really important and can see let's say between these two routers and we have the same thing on the other side.|Так что сегментация действительно очень важна, и мы можем видеть, скажем, между этими двумя маршрутизаторами, и у нас есть то же самое на другой стороне.
Same thing on the other side, we're going across campuses let's say.|То же самое с другой стороны, скажем, мы проходим через кампусы.
This is a wide area network and that's what usually this represents even though we're not really using a cloud or anything|Это глобальная сеть, и это то, что обычно она представляет, хотя мы на самом деле не используем облако или что-то еще.
like that we're connecting it directly.|вот так мы подключаем его напрямую.
We'll pretend it's a wide area network,|Представим, что это глобальная сеть,
you know,|знаешь,
these routers are gonna send the information across.|эти маршрутизаторы будут отправлять информацию.
And again, you have your VLANs are segmented down here,|И снова, здесь ваши VLAN сегментированы,
VLAN 102 and you can have, I forgot to change here, this is 103.|VLAN 102 и можно, забыл поменять здесь, это 103.
I'm sorry, this should be VLAN 103, we have to change it down here.|Извините, это должен быть VLAN 103, мы должны изменить его здесь.
This is VLAN 102 and then you got your VLAN 101 over there.|Это VLAN 102, и у вас там есть VLAN 101.
All right, so definitely segmentation,|Хорошо, определенно сегментация,
segmentation,|сегментация,
segmentation, that needs to happen.|сегментация, которая должна произойти.
One of the best ways, one of the best ways that you could do that is by using that tool, that VLAN, all right?|Один из лучших способов, один из лучших способов сделать это - использовать этот инструмент, эту VLAN, хорошо?
And It's gonna increase your bandwidth,|И это увеличит вашу пропускную способность,
it's gonna increase your security,|это повысит вашу безопасность,
it's gonna increase your flexibility and scalability of your network.|это повысит вашу гибкость и масштабируемость вашей сети.
So make use of that tool that you already have in that arsenal.|Так что используйте тот инструмент, который у вас уже есть в арсенале.
So segment your network, I'll see you in the next section.|Так что сегментируйте свою сеть, увидимся в следующем разделе.
[BLANK_AUDIO]|[BLANK_AUDIO]