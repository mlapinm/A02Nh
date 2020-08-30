D:\mailCloud\prjother\tmp\1\c82_What are vlans and the importance of using vlans in our network.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
All right everyone welcome to the world of VLANs.|Итак, добро пожаловать в мир виртуальных локальных сетей.
We discussed VLANs in the past and we,|Мы обсуждали VLAN в прошлом, и мы,
I've told you that VLANs are extremely important, all right, in a real world scenario.|Я уже говорил вам, что VLAN чрезвычайно важны в реальном мире.
We tend to procrastinate in creating VLANs.|Мы склонны откладывать создание сетей VLAN.
Because, I don't know, all right.|Потому что, я не знаю, хорошо.
We have certain companies that buy unmanaged switches.|У нас есть определенные компании, которые покупают неуправляемые коммутаторы.
Bad companies, bad companies.|Плохие компании, плохие компании.
Why?|Зачем?
Don't do that, slap on the hand.|Не делай этого, хлопни по руке.
All right, you want to buy managed switches so you can create these VLANs.|Хорошо, вы хотите купить управляемые коммутаторы, чтобы создавать эти VLAN.
Now what exactly, right?|Что именно, правильно?
What exactly is a VLAN?|Что такое VLAN?
All it is, is just a logical portion of your network.|Это всего лишь логическая часть вашей сети.
You, you're, you're segmenting logically,|Вы, вы, вы логически сегментируете,
meaning,|смысл,
like this drawing back here, all right?|как этот рисунок здесь, хорошо?
Let's say this, this switch over here will be the HR department.|Скажем так, это будет отдел кадров.
And then this switch over here will be the finance department and this will be, I like to match up my IPs with my VLANs,|И затем этот переключатель здесь будет финансовым отделом, и это будет, я хотел бы сопоставить мои IP-адреса с моими VLAN,
so this will be VLAN 20 and this will be VLAN 10.|так что это будет VLAN 20, а это будет VLAN 10.
What happens here, you know how they say what happens in Vegas stays in Vegas?|Что здесь происходит, знаете, как говорят, что происходит в Вегасе, остается в Вегасе?
Well what happens in the VLAN, stays in the VLAN.|То, что происходит в VLAN, остается в VLAN.
All right.|Отлично.
Nothing's gonna go outside.|Ничего не выйдет наружу.
So if you have a printer within that department,|Итак, если у вас есть принтер в этом отделе,
if you're doing things in that department,|если вы делаете что-то в этом отделе,
remember cuz we're using, excuse me.|помните, потому что мы используем, извините.
We're doing CSMACD, right?|Мы делаем CSMACD, верно?
We're using ethernet.|Мы используем Ethernet.
So that noise, we still have broadcast.|Так что этот шум мы все еще транслируем.
But since we're breaking up broadcast domains at layer two,|Но поскольку мы разделяем широковещательные домены на втором уровне,
they are not going to, no, they are not going to hear that noise that's going on in this department right here, you're not going to hear it.|они не собираются, нет, они не услышат того шума, который происходит прямо здесь в этом отделе, вы его не услышите.
Whatever happens in here and let me move this a little bit more,|Что бы здесь ни происходило, позвольте мне немного переместить это,
let's see if I can move it more this way.|давай посмотрим, смогу ли я переместить его так.
Sorry to give you my back here.|Извините, что вернул вам мою поддержку.
All right, but whatever happens in this particular VLAN here is not gonna bother this VLAN over here.|Хорошо, но все, что происходит в этой конкретной VLAN, не будет беспокоить эту VLAN здесь.
You can have two DACP servers, different VLANs,|У вас может быть два сервера DACP, разные VLAN,
it's just gonna be for that particular broadcast domain.|это будет только для этого конкретного широковещательного домена.
If you wanna go outside your VLAN, now this router comes into effect, right.|Если вы хотите выйти за пределы своей VLAN, теперь вступает в силу этот маршрутизатор, верно.
Now the router comes into effect because that's where your inter-VLAN communications comes in.|Теперь вступает в силу маршрутизатор, потому что именно здесь вступает в силу ваша связь между VLAN.
Okay.?|Ладно.?
But for, for now, yes, create your VLANs,|Но пока что да, создайте свои VLAN,
you logically segment your VLANs.|вы логически сегментируете свои VLAN.
Of course you're going to get asked quite often, he'll ask do we break up the switch into different VLANs or is it a VLAN per switch.|Конечно, вас будут спрашивать довольно часто, он спросит, разбиваем ли мы коммутатор на разные VLAN или это VLAN для каждого коммутатора.
It's completely up to you on the size of your network.|Это полностью зависит от размера вашей сети.
If it's a small company you may want to have,|Если вы хотите создать небольшую компанию,
you know, they have ports one through,|знаете, у них порты один сквозной,
what is it, one through eight and nine,|что это, от одного до восьми и девяти,
10, 11, 12 then there's then, oh my God,|10, 11, 12, тогда есть тогда, о мой Бог,
then eight, nine through 16.|потом восемь, с девяти до 16.
Then 17 through 24, whatever, you can break them up however you want.|Затем с 17 по 24, как угодно, вы можете разбить их, как хотите.
Okay, and you know this is VLAN whatever.|Хорошо, и вы знаете, что это какая-то VLAN.
Just always leave room for VLAN one and that you're going to maintain.|Просто всегда оставляйте место для первой VLAN, которую вы собираетесь поддерживать.
That has your native VLAN.|Это ваш собственный VLAN.
Remember that.|Помни это.
Maintain, VLAN one exists on all switches,|Поддерживайте, VLAN один существует на всех коммутаторах,
and VLAN one is your native VLAN,|а VLAN one - это ваша собственная VLAN,
your admin VLAN, your management VLAN,|ваша административная VLAN, ваша управляющая VLAN,
goes by many names, all right.|хорошо известен под разными именами.
But that's the one that the IT personnel actually accesses to do whatever it is that they need to do.|Но именно к нему на самом деле обращается ИТ-персонал, чтобы делать все, что им нужно.
Nobody else should have access to that particular VLAN.|Никто другой не должен иметь доступа к этой конкретной VLAN.
And that's where your access lists come in.|И здесь на помощь приходят ваши списки доступа.
Future lesson.|Будущий урок.
Right?|Правильно?
In this course.|В этом курсе.
But no, you create your VLANs however you,|Но нет, вы создаете свои VLAN так, как вы,
you want to.|ты хочешь.
Like, in a school, it would be a VLAN per classroom.|Например, в школе это будет VLAN на класс.
Right, it could be a VLAN per department,|Верно, это может быть VLAN на отдел,
it doesn't really,|на самом деле это не так,
I mean it matters, it all that matters, it depends on the size of your company.|Я имею в виду, что это имеет значение, все, что имеет значение, все зависит от размера вашей компании.
Like I said, a small company, you have five people in your company, really?|Как я уже сказал, небольшая компания, в вашей компании пять человек, правда?
It's not that big of a deal,|Это не так уж важно,
then you may not want to do VLANs, or maybe you have a graphic arts company.|тогда вы, возможно, не захотите создавать VLAN, или, может быть, у вас есть компания, занимающаяся полиграфией.
Or you're using a surveying company that your, CAD, AutoCAD drawings.|Или вы пользуетесь услугами геодезической компании, которая предоставляет свои чертежи в САПР, AutoCAD.
Maybe the people that do the AutoCAD can be in their own VLAN and everybody else on another VLAN because the AutoCAD,|Возможно, люди, которые работают с AutoCAD, могут быть в своей собственной VLAN, а все остальные - в другой VLAN, потому что AutoCAD,
those drawings going through the network,|эти рисунки проходят по сети,
will take up a lot of band, bandwidth.|займет много полосы пропускания.
Right, they're very huge, huge packets,|Да, это очень большие, огромные пакеты,
right.|право.
Those, those file sizes are huge, so you may want to separate it that way.|Размер этих файлов огромен, поэтому вы можете захотеть разделить их таким образом.
So it's completely up to you.|Так что это полностью зависит от вас.
The great things about VLANs is, let's say okay, we've got HR and we've got finance, right?|Отличные особенности VLAN в том, что, допустим, у нас есть кадры и есть финансы, верно?
We've got these two different VLANs here but the great thing about that is,|У нас есть эти две разные VLAN, но самое главное в этом то, что
let's say we run out of room in the accounting department.|допустим, нам не хватает места в бухгалтерии.
But it's only like three or four people in HR.|Но это примерно три-четыре человека в HR.
But there's so many people in accounting,|Но в бухгалтерии так много людей,
we have nowhere to put you in this particular department.|нам некуда поместить вас в этот конкретный отдел.
We gotta fit you somewhere else until we make room for you, and unfortunately,|Мы должны разместить вас в другом месте, пока не освободим место для вас, и, к сожалению,
sometimes that's because we're downsizing,|иногда это потому, что мы сокращаемся,
but let's hope that's not the case.|но будем надеяться, что это не так.
Let's hope that the company is flourishing and growing,|Будем надеяться, что компания процветает и растет,
that we need to knock down a wall and put more cubicles and what have you.|что нам нужно снести стену и поставить побольше кабин и что там у вас.
But let's say you have so many accountants over here that they don't fit, so we can sit you on another switch, in another department.|Но допустим, у вас здесь так много бухгалтеров, что они не подходят, поэтому мы можем посадить вас на другой переключатель, в другой отдел.
We can put you in the frickin basement if we had to, okay, but as long as you're part of that particular VLAN, you have access to that information.|Мы можем поместить вас в чертов подвал, если потребуется, хорошо, но пока вы являетесь частью этой конкретной VLAN, у вас есть доступ к этой информации.
You're a part of the accounting VLAN, so you'll see what the accounting VLAN sees.|Вы являетесь частью учетной VLAN, поэтому вы будете видеть то, что видит учетная VLAN.
And that's what's great about it, you don't have the limitation,|И вот что в этом хорошего, у тебя нет ограничений,
the physical limitation, of hey, you have to be within that department.|физическое ограничение, эй, вы должны быть в этом отделе.
You could be anywhere as long as your part of that VLAN hey,|Вы можете быть где угодно, пока входите в эту VLAN. Эй,
you can access that information.|вы можете получить доступ к этой информации.
So it is extremely important for security purposes, for,|Поэтому это чрезвычайно важно в целях безопасности, поскольку
you know, bandwidth okay, conserving bandwidth.|ну, с пропускной способностью все в порядке, с сохранением пропускной способности.
Main, keeping information within or problems within your particular VLAN.|Главное, хранение информации в вашей конкретной VLAN или проблемы с ней.
It is just organization, keeping track of everything.|Это просто организация, отслеживающая все.
Administratively, VLANs are great.|С административной точки зрения VLAN великолепны.
For your certifications they will ask you things like this.|Что касается сертификатов, они будут спрашивать вас о таких вещах.
You know, what are the benefits of using VLANs?|Вы знаете, каковы преимущества использования VLAN?
Hey, security would be one.|Эй, безопасность будет одним из них.
Organization would be another.|Организация была бы другой.
Administration would be another.|Администрация была бы другой.
These are three key points that, you're gonna say,|Это три ключевых момента, о которых вы скажете:
hey this is the reason why we wanna do VLANs.|эй, это причина, по которой мы хотим создавать VLAN.
And not to have the physical limitation because VLANs are logical segmentations.|И не иметь физических ограничений, потому что VLAN представляют собой логические сегменты.
Key, key, key, key.|Ключ, ключ, ключ, ключ.
Logical segmentations of local area networks.|Логические сегменты локальных сетей.
So each switch can be a, a different VLAN and, or you can do,|Таким образом, каждый коммутатор может быть отдельной VLAN и, или вы можете,
you know, a, we have a lab here that once we know how to do this we'll do for,|вы знаете, у нас здесь есть лаборатория, и как только мы узнаем, как это сделать, мы сделаем для нее,
it's called the summary lab.|это называется итоговой лабораторией.
We learn how to summarize and actually use that summary address to reduce the routing tables.|Мы узнаем, как суммировать и фактически использовать этот итоговый адрес для сокращения таблиц маршрутизации.
You also use how to use the VLANs.|Вы также узнаете, как использовать VLAN.
When you you can create each port, make it a different VLAN.|Когда вы можете создать каждый порт, сделайте его отдельной VLAN.
I mean, I don't know why would you, but you could if you wanted to.|Я имею в виду, я не знаю, зачем вам это, но вы могли бы, если бы захотели.
And you can reuse the same IP address in every port.|И вы можете повторно использовать один и тот же IP-адрес в каждом порту.
They wouldn't conflict with each other because you are breaking a broadcast of layer two, you're breaking a broadcast on layer two.|Они не будут конфликтовать друг с другом, потому что вы нарушаете трансляцию на втором уровне, вы нарушаете трансляцию на втором уровне.
Now this is a question obviously that comes to everybody's mind, or it should come to your mind.|Очевидно, это вопрос, который приходит в голову каждому, или он должен прийти в голову.
You have two different networks, you have the ten network over there,|У вас есть две разные сети, у вас есть десять сетей,
you have the 20 network over here but you only have one,|у вас есть 20 сетей здесь, но у вас только одна,
one physical interface on that router.|один физический интерфейс на этом маршрутизаторе.
How are people supposed to get out?|Как люди должны выйти?
Let's say you have the internet somewhere over here, right.|Допустим, у вас где-то здесь есть интернет, верно.
How are people supposed to get out to the internet?|Как люди должны выходить в Интернет?
Everybody has to have their individual gateway within their own subnet.|У каждого должен быть свой индивидуальный шлюз в собственной подсети.
And you're absolutely correct, you're absolutely correct.|И вы абсолютно правы, вы абсолютно правы.
Well, this is an, this is something called a router on a stick,|Ну, это то, что называется роутером на флешке,
which you'll learn when we do the inter-VLANs, all right?|что вы узнаете, когда мы сделаем меж-VLAN, хорошо?
Because you would do inter-VLAN routing,|Поскольку вы выполняете маршрутизацию между VLAN,
and you would do that based on sub-interfaces.|и вы бы сделали это на основе суб-интерфейсов.
That's where we start creating sub-interfaces on the router.|Здесь мы начинаем создавать субинтерфейсы на маршрутизаторе.
Will you see this in your exam?|Вы увидите это на экзамене?
Yes you will.|Да, вы будете.
Will they ask you questions,|Будут ли они задавать вам вопросы,
what does it take to create something like this to make it work?|что нужно, чтобы создать что-то подобное, чтобы оно заработало?
Yes you will.|Да, вы будете.
It will probably be in the form of a multiple choice question.|Вероятно, это будет вопрос с несколькими вариантами ответов.
You won't actually have to do it yourself.|На самом деле вам не придется делать это самому.
But we'll give you the commands and the prompts,|Но мы дадим вам команды и подсказки,
that's why it's very important to know the navigation of the switch, which we did.|вот почему очень важно знать, как работает переключатель, что мы и сделали.
All right?|Отлично?
And putting in administration commands and all that stuff.|И вводить административные команды и все такое.
All right?|Отлично?
But now it comes time to start learning how to create the VLANs,|Но теперь пришло время научиться создавать сети VLAN,
how to assign the VLANs.|как назначить VLAN.
All right?|Отлично?
And again,|И опять,
you can make the whole switch one particular VLAN.|вы можете сделать весь коммутатор одной конкретной VLAN.
Or you can make, you know, a report of different VLAN,|Или вы можете сделать, знаете ли, отчет о различных VLAN,
however you do it is completely up to your network.|как бы вы это ни делали, это полностью зависит от вашей сети.
Again, school environments that I'm most familiar with, every classroom is a VLAN.|Опять же, школьная среда, с которой я наиболее знаком, каждый класс - это VLAN.
And then for the student sides and for the administration side,|А затем для студенческой и административной стороны,
if the departments are really that big, or that intense,|если отделы действительно такие большие или интенсивные,
where data is flowing back and forth, then you can separate through VLANs.|там, где данные передаются туда и обратно, вы можете разделить их через VLAN.
I mean, you could, cuz each department will have their own switch.|Я имею в виду, что вы могли бы, потому что в каждом отделе будет свой переключатель.
So you can actually put them in different VLANs if you wanted to.|Таким образом, вы можете разместить их в разных VLAN, если хотите.
Just remember, a lot of these locations,|Просто помните, многие из этих мест,
right, these schools or businesses, like to share printers.|да, эти школы или предприятия любят делиться принтерами.
So, if you are going to be using a shared printer and you have to go across multiple VLANs.|Итак, если вы собираетесь использовать общий принтер, и вам нужно пройти через несколько VLAN.
Then the problem, not a problem, but the thing is,|Тогда проблема, не проблема, но дело в том,
if this computer on VLAN 10 wants to talk to a computer on VLAN 20.|если этот компьютер в VLAN 10 хочет поговорить с компьютером в VLAN 20.
Remember the information will not flow straight across.|Помните, что информация не будет передаваться прямо.
The inflammation, the inflammation, the information will go to the router.|Воспаление, воспаление, информация уйдет на роутер.
The router will make the routing decision and then come back down.|Маршрутизатор примет решение о маршрутизации и затем отключится.
That's what you need to consider as well.|Это тоже нужно учитывать.
So these are VLANs.|Итак, это сети VLAN.
And yes they are important.|И да, они важны.
They should be required.|Они должны быть обязательными.
Okay, in major infrastructures.|Хорошо, в основной инфраструктуре.
Telecommunications uses VLANs, all right,|Телекоммуникации используют VLAN, хорошо,
major, major companies use VLANs.|крупные, крупные компании используют сети VLAN.
Certain schools have come to the conclusion, light bulb turned on and said, hey, it's best if we use VLANs.|Некоторые школы пришли к такому выводу, загорелась лампочка и сказала: «Эй, лучше, если мы будем использовать VLAN».
And why is that?|И почему так?
Because again, the same analogy we used in the previous lesson.|Потому что снова та же аналогия, которую мы использовали в предыдущем уроке.
If I create a DACP server on the same VLAN that you're in,|Если я создам сервер DACP в той же VLAN, что и вы,
then I'm gonna be assigning you IP addresses.|тогда я назначу вам IP-адреса.
And then there's gonna be an issue with a DACP server from the school.|И тогда будет проблема с сервером DACP в школе.
The most simplest example I can give you.|Самый простой пример, который я могу вам привести.
So you definitely wanna break up those segments, all right, logically.|Итак, вы определенно хотите разбить эти сегменты, хорошо, логично.
For that better organization, better security,|Для этой лучшей организации, лучшей безопасности,
better administration, all of these things, all right?|лучшее администрирование, все это, понятно?
So VLANs, yes are truly important and we're going to start learning how to configure the VLANs and the type of ports that VLANs sit on and|Итак, VLAN, да, действительно важны, и мы собираемся начать изучать, как настроить VLAN и тип портов, на которых находятся VLAN, и
the type of ports that the other VLANs,|тип портов других VLAN,
other than the main VLAN, must go through.|кроме основной VLAN, должны проходить.
I'll see you in the next lesson.|Увидимся на следующем уроке.
[BLANK_AUDIO]|[BLANK_AUDIO]