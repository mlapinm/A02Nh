D:\mailCloud\prjother\tmp\1\c95_Standard ACL's.md  


__|__
--|--
All right, everyone, welcome back.|Хорошо, все, добро пожаловать обратно.
It's time now to get into the standard access list.|Пришло время попасть в стандартный список доступа.
As you can see, I've added a laptop to the core switch, because we gonna,|Как видите, я добавил ноутбук к коммутатору ядра, потому что мы
we gonna be doing a couple standard access, actually we'll be doing two,|мы собираемся сделать пару стандартных вариантов доступа, на самом деле мы сделаем два,
all right, where we're gonna block these VLAN's, ten and 20 from actually accessing the VLAN one.|хорошо, где мы собираемся заблокировать эти VLAN, 10 и 20 от фактического доступа к VLAN one.
Because VLAN one is your management VLAN,|Поскольку VLAN one - это ваша управляющая VLAN,
no other VLAN should be able to access your management VLAN.|никакая другая VLAN не должна иметь доступ к вашей VLAN управления.
So, this is where ACLs come in.|Итак, здесь на помощь приходят ACL.
There'll be one of the labs that we're gonna do.|Мы займемся одной из лабораторий.
Then the other lab that we're gonna do is,|Тогда другая лаборатория, которую мы собираемся сделать, это,
because standard access lists are limited,|поскольку стандартные списки доступа ограничены,
now, let's talk a little bit about that.|теперь давайте поговорим об этом немного.
Let me go ahead and open the,|Позвольте мне пойти дальше и открыть,
there's the standard right here.|вот стандарт прямо здесь.
All right, this is the actual access list that we're gonna do.|Хорошо, это фактический список доступа, который мы собираемся сделать.
All right,|Отлично,
I've already prepared it for you.|Я уже приготовил это для вас.
Standard access lists, the way that you're doing it you can see a syntax already.|Стандартные списки доступа, то, как вы это делаете, вы уже можете увидеть синтаксис.
The numbers you can use are from one through 99.|Вы можете использовать числа от одного до 99.
But the,|Но,
the problem with standard access list is that they're limited to only source addresses.|проблема со стандартными списками доступа в том, что они ограничены только исходными адресами.
You can't use port numbers.|Вы не можете использовать номера портов.
You can't use protocols.|Вы не можете использовать протоколы.
You can't use destination addresses.|Вы не можете использовать адреса назначения.
So you're limited to only using the source address.|Таким образом, вы ограничены использованием только исходного адреса.
So you can either block the entire network or just a host or a couple hosts at a time.|Таким образом, вы можете заблокировать либо всю сеть, либо только один или несколько хостов одновременно.
And you can play around with the wildcard mask to see how many hosts you can block and what have you.|И вы можете поиграть с подстановочной маской, чтобы узнать, сколько хостов вы можете заблокировать и какие у вас есть.
You wanna be getting creative.|Вы хотите проявить творческий подход.
So, it's limited.|Итак, это ограничено.
So what we're gonna do right now, since it is limited, you can see what it says here,|Итак, что мы будем делать прямо сейчас, поскольку он ограничен, вы можете увидеть, что здесь написано,
you must apply it nearest the destination.|вы должны применить его к месту назначения.
Meaning, and just to give you a visual,|Это означает, и просто чтобы дать вам визуальное представление,
just to give you a visual because,|просто чтобы дать вам наглядное представление, потому что,
being on the same router, may not give you that visual that you, you know,|находясь на одном и том же маршрутизаторе, может не дать вам такого изображения, которое вы знаете,
you can understand.|ты можешь понять.
But remember we have VLAN, so that's a different broadcast domains,|Но помните, что у нас есть VLAN, так что это разные широковещательные домены,
that's a different destination.|это другое место назначения.
So imagine that I'm trying to block this PC from accessing this network over here.|Итак, представьте, что я пытаюсь заблокировать доступ этого ПК к этой сети вот здесь.
I would literally have to create the access list on this router and apply it to the subinterface that's nearest this particular network.|Мне буквально пришлось бы создать список доступа на этом маршрутизаторе и применить его к подинтерфейсу, ближайшему к этой конкретной сети.
So that means that the packet has to travel all the way across getting inside the router.|Это означает, что пакет должен пройти через маршрутизатор.
The router has to process that information and finally end up at the router interface going out to be blocked anyway.|Маршрутизатор должен обработать эту информацию и в конечном итоге оказаться на интерфейсе маршрутизатора, который все равно будет заблокирован.
So that's one of the bad things about standard access list is that they need to travel to their destination and then be denied.|Так что одна из плохих сторон стандартного списка доступа заключается в том, что им нужно добраться до места назначения, а затем им будет отказано.
So that's not, you know,|Так что это не так, вы знаете,
that's not a good thing.|это нехорошо.
But the other lab you'll see that we're,|Но в другой лаборатории вы увидите, что мы,
I don't wanna give it away too much,|Я не хочу слишком много отдавать,
but you do wanna tell me.|но ты хочешь сказать мне.
Even though I just told you you can't use protocols or port numbers in order to create a standard access list, you're not|Хотя я только что сказал вам, что вы не можете использовать протоколы или номера портов для создания стандартного списка доступа, вы не
allowed, the syntax doesn't let you do it.|разрешено, синтаксис не позволяет это сделать.
But there's a way of applying the access list, because that's the whole thing.|Но есть способ применить список доступа, потому что это все.
You first create the access list,|Сначала вы создаете список доступа,
and then you apply it.|а затем вы применяете его.
And that, that that, you know,|И то, что то, знаете,
hit something in my memory.|ударил что-то в моей памяти.
I've had students in the past asked me,|В прошлом студенты спрашивали меня,
hey Laz, can't we just apply the access list first and then create it.|Эй, Лаз, не можем ли мы сначала применить список доступа, а затем создать его.
Now I know shouldn't say what I'm about to say, but I'm gonna say it anyway.|Теперь я знаю, что не следует говорить то, что я собираюсь сказать, но я все равно это скажу.
You know me by now.|Вы меня уже знаете.
Why in the world, would you apply something that doesn't exist?|Почему бы вам применить то, чего не существует?
Okay, I can see, you know,|Хорошо, я вижу, ты знаешь,
the chicken before the egg thing, okay,|курица перед яйцом, хорошо,
that's a conundrum, I understand that,|это загадка, я это понимаю,
but here, that's not the case.|но здесь это не так.
You first apply the access list and then you, I mean, I'm sorry,|Сначала вы применяете список доступа, а затем вы, я имею в виду, извините,
you first create the access list,|вы сначала создаете список доступа,
excuse me, you first create the access list, and then you apply it.|извините, вы сначала создаете список доступа, а потом применяете его.
Firewall, the movie, Firewall, the movie.|Брандмауэр, фильм, Брандмауэр, фильм.
There, they have access lists already created.|Там у них уже созданы списки доступа.
And then Harrison Ford saves the day by applying it.|И тогда Харрисон Форд спасает положение, применяя его.
That's all he did.|Это все, что он сделал.
He comes in at the beginning of the movie and does that.|Он появляется в начале фильма и делает это.
So, please, create them, apply them.|Так что, пожалуйста, создавайте их, применяйте.
Just like VLANs, create them, then apply them, even though yes the VLAN you can't apply the VLAN that doesn't exist, the switch will create it for you, but it will|Как и в случае с виртуальными локальными сетями, создайте их, а затем примените их, даже если да, виртуальная локальная сеть, которую вы не можете применить, виртуальная локальная сеть, которая не существует, коммутатор создаст ее для вас, но он будет
create it using an unnatural number,|создать его с помощью неестественного числа,
and then you have to rename it anyway.|а потом все равно придется его переименовать.
Just doesn't make sense.|Просто не имеет смысла.
Create them, then apply them.|Создайте их, а затем примените.
That's the order.|Таков порядок.
Don't get creative,|Не проявляй творчества,
when you're doing your CCNA certification.|когда вы проходите сертификацию CCNA.
If you need,|Если тебе надо,
cuz you will be doing an access list, and I believe it's an extended access list.|Потому что вы будете делать список доступа, и я считаю, что это расширенный список доступа.
So create it.|Так что создайте это.
Make sure that it makes sense what there's, they're asking you to do.|Убедитесь, что это имеет смысл, они просят вас сделать.
And then apply it to the appropriate interface.|А затем примените его к соответствующему интерфейсу.
Because when you create an access list it's just gonna sit there until you apply it.|Потому что, когда вы создаете список доступа, он просто остается там, пока вы его не примените.
So, our goal right now,|Итак, наша цель прямо сейчас,
is to deny these two networks,|отрицать эти две сети,
the 10.0, the 20.0 because the 10 VLAN,|10.0, 20.0, потому что 10 VLAN,
20 VLAN access to the VLAN one,|20 VLAN доступ к VLAN один,
to VLAN one.|к VLAN один.
So I shouldn't be able to get to VLAN one.|Так что я не смогу попасть в VLAN one.
But before we create anything, cuz as you can see, as your book tells you,|Но прежде чем мы что-нибудь создадим, как вы видите, как сказано в вашей книге,
you should use a notepad, right,|тебе следует использовать блокнот, верно,
a text editor, to create your VLANs.|текстовый редактор для создания ваших VLAN.
And we're looking at this one first,|И мы сначала смотрим на это,
right here.|Прямо здесь.
All right, this access list, the number of the access list, are you denying or permitting?|Хорошо, этот список доступа, номер списка доступа, вы отказываетесь или разрешаете?
And the network, right,|И сеть, верно,
that you're denying, deny.|что вы отрицаете, отрицаете.
As you can see, based on the rules since I started with a deny,|Как видите, исходя из правил, которые я начал с отрицания,
I end it with a permit.|Я заканчиваю разрешением.
Because if I don't end it with a permit that means everything else is denied as well.|Потому что, если я не закрою это разрешением, это означает, что все остальное также будет отказано.
And that's not what we want.|А мы этого не хотим.
All right, so that's the goal.|Хорошо, вот и цель.
Okay, so let's go ahead and copy that.|Хорошо, давайте продолжим и скопируем это.
Let's go into the router.|Заходим в роутер.
[COUGH] Let's maximize it.|[Кашляет] Давайте максимизировать это.
Enable.|Включить.
Cisco.|Cisco.
Cisco, config t.|Cisco, конфиг t.
And the reason I put passwords is because since we're gonna be doing another lab,|Причина, по которой я ввожу пароли, заключается в том, что поскольку мы собираемся провести еще одну лабораторию
it requires me to put a password so you can see that I can get inside the router.|он требует, чтобы я ввел пароль, чтобы вы могли видеть, что я могу попасть внутрь маршрутизатора.
It's, it's a method to the madness,|Это метод безумия,
trust me.|Доверьтесь мне.
So, let's paste this.|Итак, давайте вставим это.
All right, so now we have that VLAN there.|Хорошо, теперь у нас есть эта VLAN.
And let's do a do wr.|И давайте сделаем запись.
Let's do a Ctrl+Z,|Сделаем Ctrl + Z,
go back to privileged mode.|вернуться в привилегированный режим.
Show access list, all right?|Покажи список доступа, хорошо?
And then he sees that hey, we have an access list there that states we're denying these two networks but, but we're permitting everything else.|А потом он видит, что у нас есть список доступа, в котором говорится, что мы запрещаем эти две сети, но, но мы разрешаем все остальное.
All right, so let's see if that's the case.|Хорошо, давайте посмотрим, так ли это.
I'm going to ping Laptop number one.|Я собираюсь пинговать ноутбук номер один.
And we bring this over here,|И мы приносим это сюда,
which is ping 192.168.1.1.|который пингует 192.168.1.1.
And I can ping it without a problem.|И я могу пинговать его без проблем.
But I created an access list.|Но я создал список доступа.
Let's see if this guy can ping as well.|Посмотрим, умеет ли этот парень пинговать.
Ping 192.168.1.1.|Пинг 192.168.1.1.
I, I can ping it as well.|Я тоже могу пинговать.
Of course, cuz it's just like I just said,|Конечно, потому что я только что сказал,
just because you created an access list doesn't mean anything.|то, что вы создали список доступа, ничего не значит.
It's there, it's just sitting taking space on your router.|Он там, он просто сидит, занимая место на вашем роутере.
Now we must apply it.|Теперь мы должны применить это.
Now we need to apply it nearest the destination,|Теперь нам нужно применить его к месту назначения,
according to the rules of the book.|по правилам книги.
Show, show ip int brief.|Показать, показать ip intrief.
And you see that ten to 20 sit on these subinterfaces right here, so we need to apply it to this subinterface because that's where VLAN one is.|И вы видите, что на этих субинтерфейсах прямо здесь находится от десяти до двадцати, поэтому нам нужно применить это к этому субинтерфейсу, потому что именно там находится VLAN один.
So, we need to go inside that interface and apply it.|Итак, нам нужно зайти внутрь этого интерфейса и применить его.
Now remember, the packet's already in,|Теперь помните, пакет уже отправлен,
it's in the router,|это в роутере,
it's being processed, hey,|это обрабатывается, эй,
where do you wanna go?|Куда ты хочешь пойти?
Oh, you wanna go to this network.|О, ты хочешь пойти в эту сеть.
So there it's trying to get out of the router,|Так вот пытается выйти из роутера,
so the direction will be going out of the router.|так что направление будет выходить из маршрутизатора.
It's not coming in,|Это не входит,
it's already in the router.|это уже в роутере.
It's coming from its 20 network, it's inside the router, the routers now making a decision based on the routing table,|Он поступает из его сети 20, он находится внутри маршрутизатора, маршрутизаторы теперь принимают решение на основе таблицы маршрутизации,
where you trying to get to.|куда вы пытаетесь добраться.
Or your trying to get to the,|Или вы пытаетесь добраться до
1.0 network its out the F0.0.1 interface.|1.0 выходит из интерфейса F0.0.1.
But once it gets there,|Но как только он попадает туда,
it's confronted, with in, with a,|он сталкивается, с, с,
with an access list that says no, no,|со списком доступа, который говорит нет, нет,
no, 10 and 20, you're not allowed.|нет, 10 и 20, вам нельзя.
Right?|Правильно?
It'll read it line by line and sequential order.|Он будет читать его построчно и в последовательном порядке.
You're not allowed to get out.|Тебе не разрешено выходить.
You're denied.|Тебе отказано.
So, you shouldn't be able to.|Итак, у вас не должно быть возможности.
So let's go inside that interface.|Итак, давайте войдем в этот интерфейс.
Config T interface F 0/0.1,|Config T interface F 0 / 0.1,
and the way we apply it is,|и то, как мы его применяем,
to an interface, is IP access-group.|к интерфейсу, это IP-группа доступа.
The number, which is one,|Число, которое равно единице,
and then the direction.|а затем направление.
In this case, it will be out.|В этом случае его не будет.
We'll copy that.|Мы скопируем это.
Obviously in your exam, if you need to do something like this you'll go back to privileged mode, and do a copy run start.|Очевидно, что на экзамене, если вам нужно сделать что-то подобное, вы вернетесь в привилегированный режим и выполните запуск копирования.
Under Ctrl+Z and you see that already.|Под Ctrl + Z, и вы это уже видите.
We're gonna look at it now where in which direction it is applied,|Сейчас мы посмотрим, в каком направлении он применяется,
we see how we going to look at access list by saying show access list, and I'll show you a list of all the access lists that exist on your router.|мы увидим, как мы будем смотреть на список доступа, сказав показать список доступа, и я покажу вам список всех списков доступа, которые существуют на вашем маршрутизаторе.
Easy to do a little show,|Легко устроить небольшое шоу,
IP interface F0/0.1, you see that you have an outgoing access list,|IP-интерфейс F0 / 0.1, вы видите, что у вас есть список исходящего доступа,
all right, under that interface.|хорошо, под этим интерфейсом.
So that's, that's the command that will show you in which direction.|Это команда, которая покажет вам, в каком направлении.
You can see you can only have one outgoing and one inbound.|Вы можете видеть, что у вас может быть только один исходящий и один входящий.
That was usually acts as multiple lines.|Обычно это было несколько строк.
All right.|Отлично.
So we have now we assigned it now.|Итак, мы назначили это сейчас.
We applied to that interface.|Мы обратились к этому интерфейсу.
Now it access list should work.|Теперь список доступа должен работать.
When before we were able to ping as you can see.|Когда раньше мы могли пинговать, как видите.
And I'll bring this over here so you can see it better.|И я принесу это сюда, чтобы вам было лучше.
Let me open it up a little bit more.|Позвольте мне открыть его еще немного.
And it's just up arrow.|И это просто стрелка вверх.
And now I'm getting a destination host unreachable, right.|И теперь я получаю, что целевой хост недоступен, верно.
That's what it says on the other side.|Так написано на другой стороне.
But I'm getting a reply back from my gateway.|Но я получаю ответ от своего шлюза.
That's as far as I can go.|Это все, что я могу.
I can't get anywhere else.|Больше никуда не денусь.
And then the same that,|А потом то же самое,
I'm sure the same thing's gonna happen.|Я уверен, что произойдет то же самое.
To this particular one.|К этому конкретному.
We're able to ping it before with no issues.|Мы можем пинговать его раньше без проблем.
We can open up a little bit bigger ,so you can see that it's still TTL's and everything, and now you see host unreachable.|Мы можем открыть немного больше, чтобы вы могли видеть, что TTL все еще и все такое, и теперь вы видите, что хост недоступен.
So indeed, all right, now, we're working,|Итак, действительно, хорошо, сейчас мы работаем,
it doesn't mean that we can't get anywhere else.|это не значит, что мы больше никуда не денемся.
If I up hour and I pay, say 30.1,|Если я работаю час и плачу, скажем, 30,1,
obviously it's gonna take a little bit.|очевидно, это займет немного времени.
It's gonna be routed to somewhere else,|Он будет направлен куда-то еще,
and of course we have our getting out of my own network,|и, конечно же, у нас есть выход из моей сети,
I just can't get to B line one.|Я просто не могу добраться до первой линии B.
And that's one of the things you should do.|И это одна из вещей, которую вы должны сделать.
You should block.|Вам следует заблокировать.
Any other VLANs from accessing your management VLAN.|Любые другие сети VLAN от доступа к вашей управляющей VLAN.
Whether it be VLAN1 or VLAN,|Будь то VLAN1 или VLAN,
you know, 99 doesn't matter.|знаете, 99 не имеет значения.
Or 100.|Или 100.
You can change, it is recommended that you change the default VLAN, or VLAN1.|Вы можете изменить, рекомендуется изменить VLAN по умолчанию или VLAN1.
And make it into something else.|И превратить это во что-нибудь другое.
Take it, change the native VLAN into another number.|Возьми, поменяй родной VLAN на другой номер.
Just like in Microsoft,|Как и в Microsoft,
you want to rename your administrator account to Bob, let's say.|вы хотите переименовать свою учетную запись администратора в Bob, скажем.
And then create an administrator account,|А затем создайте учетную запись администратора,
that's a regular user.|это обычный пользователь.
So, when people try to hack you,|Итак, когда люди пытаются вас взломать,
they look for administrator account,|они ищут учетную запись администратора,
it's just a regular user,|это просто обычный пользователь,
things like that.|такие вещи.
Things like that.|Такие вещи.
All right, so that's one way that we use numbered access lists.|Хорошо, это один из способов использования нумерованных списков доступа.
Right, to block a particular network from getting to another network.|Правильно, чтобы заблокировать доступ одной сети к другой.
Now again, we can only use source IP addresses, so we're limited.|Опять же, мы можем использовать только исходные IP-адреса, поэтому мы ограничены.
So what about, because your book shows you a real world scenario.|Так что насчет того, потому что ваша книга показывает вам сценарий реального мира.
On actually using a standard access list to block or to permit or deny telnet access.|При фактическом использовании стандартного списка доступа для блокировки, разрешения или запрета доступа через Telnet.
I just said that you couldn't do that.|Я просто сказал, что ты не можешь этого сделать.
But your book says,|Но ваша книга говорит:
hey there is a way around it.|эй, есть способ обойти это.
Let's see what that way is.|Посмотрим, что это за способ.
If we look,|Если мы посмотрим,
we have two ways cuz we want our permit.|у нас есть два пути, потому что мы хотим получить разрешение.
I want to allow somebody to be able to into my router,|Я хочу, чтобы кто-нибудь мог войти в мой роутер,
this is my you know,|это мой ты знаешь,
second IT individual or whoever.|второй ИТ-специалист или кто-то еще.
All right, to telnet or somebody is working remotely,|Хорошо, телнет или кто-то работает удаленно,
that makes it telnet into a router.|это превращает telnet в маршрутизатор.
Obviously they'll be doing SSH or through a BPN or something like that.|Очевидно, они будут использовать SSH или BPN или что-то в этом роде.
What, we'll just say telnet into the router.|Что, просто скажем телнет в роутер.
So, I make an access list to permit that individual, or maybe a group of individuals,|Итак, я составляю список доступа, чтобы позволить этому человеку или, возможно, группе людей,
all right, to go into the router.|ладно, зайти в роутер.
So, I can create an access list just to permit, let's say,|Итак, я могу создать список доступа, чтобы разрешить, скажем,
I want to permit this individual only.|Я хочу разрешить только этого человека.
And like I said earlier,|И, как я сказал ранее,
there's 2 ways of writing this,|есть два способа написать это,
you can use the wildcard mask of all zeroes and the IP address.|вы можете использовать подстановочную маску всех нулей и IP-адреса.
Or you can write host, and then put the IP address.|Или вы можете написать host, а затем поставить IP-адрес.
So there's two ways of writing it.|Так что есть два способа написать это.
They both mean the same thing.|Оба они означают одно и то же.
It all depends on your preference.|Все зависит от ваших предпочтений.
Would you like to light, would you like to write the wildcard mask, or would you like to just put host and then the IP address of the host.|Хотели бы вы зажечь, хотите ли вы написать маску подстановки, или вы хотите просто указать хост, а затем IP-адрес хоста.
So, let's first test to see if we can actually telnet.|Итак, давайте сначала проверим, можем ли мы на самом деле telnet.
Since there is an access list,|Поскольку есть список доступа,
let's see if we can actually telnet into these routers.|посмотрим, сможем ли мы подключиться к этим маршрутизаторам через Telnet.
Let's test that theory.|Давайте проверим эту теорию.
Telnet 192.168.20|Telnet 192.168.20
.254 Cisco, enable Cisco,|.254 Cisco, включить Cisco,
and [INAUDIBLE] right?|и [НЕРАЗБОРЧИВО] верно?
Show IP in brief, not a problem,|Кратко показать IP, не проблема,
okay, exit it out, and out, okay.|хорошо, выходи из этого и выходи, хорошо.
Let's try and do it this one.|Давай попробуем сделать это.
And, Telnet.|И Telnet.
Let's move it this way.|Давайте переместим его сюда.
Telnet 192.168.10.254 Cisco.|Telnet 192.168.10.254 Cisco.
Enable.|Включить.
Cisco and I'm in the route, right?|Cisco и я в пути, верно?
Show IP route.|Показать IP-маршрут.
So let's do a different command.|Итак, давайте выполним другую команду.
You'll see I'm routing back and forth.|Вы увидите, что я иду туда и обратно.
That's cool.|Это классно.
Exit.|Выход.
So we are able to telnet and I'm sure the admin person is also able to telnet but just test him anyway.|Таким образом, мы можем использовать telnet, и я уверен, что администратор также может использовать telnet, но все равно просто протестируйте его.
Let's not forget the lonely admin IT individuals,|Давайте не будем забывать об одиноких администраторах ИТ-специалистов,
telnet 192.168.1.254,|телнет 192.168.1.254,
cisco, enable, cisco.|cisco, включить, cisco.
Then you're in.|Тогда ты в игре.
Show protocols.|Показать протоколы.
Get a different one.|Купи другой.
And when it's showing you, your,|И когда он показывает вам, ваш,
you know, your masks, your IP's,|вы знаете, ваши маски, ваш IP,
your LAN's, your stuff.|ваша локальная сеть, ваши вещи.
Perfect.|Отлично.
Ctrl+C.|Ctrl + C.
Amazing.|Удивительный.
So we're all able to telnet into a router.|Итак, мы все можем подключиться к маршрутизатору через Telnet.
So, I'm going to create,|Итак, я собираюсь создать,
or I have created already.|или я уже создал.
An actual, and I'm gonna use this one down here.|Настоящая, и я собираюсь использовать ее здесь.
An actual access list that's only going to permit the VLAN 10,|Фактический список доступа, который разрешит только VLAN 10,
the host on VLAN 10 to be able to telnet into that specific router.|хост в VLAN 10, чтобы иметь возможность подключиться к этому конкретному маршрутизатору через Telnet.
I'm gonna come here let me maximize our router.|Я пойду сюда, позволь мне максимизировать наш роутер.
Okay, Ctrl+C.|Хорошо, Ctrl + C.
Okay.|Ладно.
Config t, I'm gonna paste.|Config t, я вставлю.
Now if you look at that access list,|Теперь, если вы посмотрите на этот список доступа,
it's not saying much.|это мало что говорит.
It's saying,|Это говорит,
hey ACCESS-LIST 2 permits this host.|Привет ACCESS-LIST 2 разрешает этот хост.
But we're not being specific as to what we're permitting.|Но мы не уточняем, что мы разрешаем.
And since I started with a permit,|И так как я начал с разрешения,
I'm not going to put another permit.|Другого разрешения ставить не буду.
I want to let that invisible,|Я хочу, чтобы это было невидимым,
that implicit deny to take effect.|это неявное отрицание вступления в силу.
Because this is the only person I want to be able to permit.|Потому что это единственный человек, которого я хочу позволить.
So what I do since I cannot put a port number or protocol or destination.|Итак, что я делаю, поскольку я не могу указать номер порта, протокол или пункт назначения.
What I'm actually going to do is,|На самом деле я собираюсь сделать следующее:
I'm actually going to go into the telnet lines and I'm going to apply that access list into the telnet lines.|Я собираюсь перейти к линиям telnet и применить этот список доступа к линиям telnet.
So I'm going to go line vty 0 15|Так что я пойду на линию vty 0 15
with the access class, access-class.|с классом доступа, класс доступа.
The access list is 2 and in which direction in,|Список доступа 2 и в каком направлении,
because you're trying to get,|потому что вы пытаетесь получить,
you're trying to telnet into the router.|вы пытаетесь подключиться к маршрутизатору через Telnet.
Before, we were trying to get out of an interface, so we used the IP access group,|Раньше мы пытались выйти за пределы интерфейса, поэтому использовали группу доступа IP,
all right, the belmer and then out.|хорошо, бельмер, а потом вон.
But now we're talking about lines.|Но сейчас мы говорим о линиях.
A line vty, now however many vty lines you open, how many terminal lines you open,|Строка vty, сколько бы строк vty вы ни открывали, сколько терминальных линий вы открываете,
whether it's 181 or 1,081, you need to apply the access-list to all those lines.|будь то 181 или 1081, вам нужно применить список доступа ко всем этим строкам.
So while I'm applying it all the lines,|Итак, пока я наношу все линии,
saying hey, access-class 2 in, so class 2 is pointing to this ACCESS-LIST saying, PERMIT only that HOST.|говоря: «Эй, класс доступа 2», значит класс 2 указывает на этот СПИСОК ДОСТУПА, говоря: РАЗРЕШИТЬ только этот ХОЗЯИН.
And then because we have an implicit deny at the end, it will deny everybody else.|А затем, поскольку в конце у нас есть неявное отрицание, это отрицает всех остальных.
Let's see if that works.|Посмотрим, работает ли это.
Let's copy this.|Давайте скопируем это.
All right.|Отлично.
So, I'm gonna try and telnet again,|Итак, я собираюсь снова попробовать телнет,
I was able to telnet before.|Раньше я мог пользоваться телнетом.
Refused by remote host,|Отказано удаленным хостом,
interesting, interesting.|интересно, интересно.
Let's do it again.|Давай сделаем это снова.
Let's do it through the admin.|Сделаем это через админку.
Surely, the admin is able to get in.|Наверняка админ может войти.
Nope.|Нет.
Not the admin, is not able to get in.|Не админ, не может войти.
Let's try now the last one.|Попробуем теперь последний.
And, able to get in.|И может попасть внутрь.
Because he's the only one that's being permitted by that particular access list in order to do what he needs to do.|Потому что он единственный, кому этот конкретный список доступа позволяет делать то, что ему нужно.
But I know what you're thinking.|Но я знаю, о чем вы думаете.
Oh, well, that's in the,|О, ну это в,
in the same pyramid.|в той же пирамиде.
It's not the same LAN, because it's a broad, each one is a different broadcast.|Это не та же ЛВС, потому что она широкая, каждая - отдельная трансляция.
But it's in the same enterprise.|Но это на том же предприятии.
The other, the other PCs should be able to because they have nothing to do with that.|Другой, другие ПК должны иметь возможность, потому что они не имеют к этому никакого отношения.
They're in a different world all together.|Все вместе они в другом мире.
It could be another county or across.|Это может быть другой округ или другой округ.
Well, let's, let's test that out.|Что ж, давайте, давайте это проверим.
Telnet 192.|Telnet 192.
No not 192, telnet to take 10.1.1.5.|Нет не 192, телнет взять 10.1.1.5.
Refused!|Отказалась!
So it doesn't really matter if, if you're routing and you're going across whoever.|Так что на самом деле не имеет значения, если вы маршрутизируете и встречаетесь с кем бы то ни было.
You didn't apply this to an interface,|Вы не применили это к интерфейсу,
you applied it to a line,|вы применили это к строке,
to the actual telnet lines.|к фактическим линиям telnet.
And it's recommended that you do that.|И вам рекомендуется это сделать.
If you want, cuz, because an extended access list will give you more flexibility to put protocols, important numbers.|Если хотите, потому что расширенный список доступа даст вам больше гибкости для ввода протоколов, важных чисел.
But why waste a line just to deny or permit telnet when you can use a standard access list and actually apply it on the lines?|Но зачем тратить линию только на то, чтобы запретить или разрешить Telnet, если вы можете использовать стандартный список доступа и фактически применить его к линиям?
We're limited already to one in and one out.|Мы уже ограничены одним входом и одним выходом.
So you can use a standard access-list to actually permit or deny the telnet protocol.|Таким образом, вы можете использовать стандартный список доступа, чтобы фактически разрешить или запретить протокол telnet.
And that's, I think is very, very cool.|И это, я думаю, очень и очень круто.
Two ways that we used this standard access-list,|Мы использовали этот стандартный список доступа двумя способами:
even though we are limited,|хотя мы ограничены,
to block access to your native VLAN.|чтобы заблокировать доступ к вашей собственной VLAN.
Which is definitely something you need to do and to permit or deny telnet access.|Это определенно то, что вам нужно сделать, а также разрешить или запретить доступ по telnet.
Now there is a third way but when we get to NAT.|Теперь есть третий способ, но когда мы переходим к NAT.
You don't have to apply it, but you do create a standard access list and it just serves a different purpose than the two ways that we showed here.|Вам не обязательно применять его, но вы создаете стандартный список доступа, и он просто служит другой цели, чем два способа, которые мы показали здесь.
But, that's it.|Но это все.
That is your standard access list.|Это ваш стандартный список доступа.
I'll see you in the next one.|Увидимся в следующем.