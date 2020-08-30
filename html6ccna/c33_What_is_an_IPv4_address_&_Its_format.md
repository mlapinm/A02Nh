D:\mailCloud\prjother\tmp\1\c33_What is an IPv4 address & Its format.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
All right everybody.|Все в порядке.
Now we get into the fun stuff.|Теперь перейдем к интересным вещам.
IP's.|IP-адреса.
What we need to understand what an IPv4|Что нам нужно, чтобы понять, что такое IPv4
address is?|адрес?
IPv4 it's a logical address, all right.|IPv4, это логический адрес, хорошо.
There's many types of of classes, and we'll get into the classes and all that later on, but we need to understand that I an IPv4 address is something that we|Существует много типов классов, и мы рассмотрим классы и все такое позже, но мы должны понимать, что IPv4-адрес - это то, что мы
choose, that we put into the notes so we can go ahead, and network and they can talk to each other.|выбрать, что мы помещаем в заметки, чтобы мы могли продолжить, и пообщаться, и они могли поговорить друг с другом.
And if, it's a hierarchy of IP addresses.|А если, то это иерархия IP-адресов.
It's not a flat design, it's a hierarchical.|Это не плоский дизайн, это иерархический.
I was trying to avoid using that word because it's very difficult, hierarchical,|Я пытался избежать использования этого слова, потому что оно очень сложное, иерархическое,
forget it word scheme they use, right,|забудь схему слов, которую они используют, верно,
instead of a flat scheme.|вместо плоской схемы.
So IP four addressing we know that it's 32-bits long address.|Итак, IP-адресация четыре, и мы знаем, что это 32-битный адрес.
And that is separated by it's separated into four different octets,|И это разделено на четыре разных октета,
separated by decimals.|разделенные десятичными знаками.
We all know this, but we need to go ahead,|Мы все это знаем, но нам нужно идти вперед,
and put these addresses into our PCs so we can go ahead, and communicate with each other.|и помещаем эти адреса в наши ПК, чтобы мы могли продолжать общаться друг с другом.
Now we know for networking, we saw it at the very beginning of the course.|Теперь мы знаем, что такое нетворкинг, мы видели это в самом начале курса.
In order to communicate with another computer we need to know the source and destination IP, source and destination MAC address, and you need a port number,|Для связи с другим компьютером нам необходимо знать IP-адрес источника и назначения, MAC-адрес источника и назначения, а также номер порта,
obviously, which port you're using to get from one location whether you're emailing FTPing or whatever it is you're going from|очевидно, какой порт вы используете для получения из одного места, отправляете ли вы электронную почту по FTP или что-то еще, из чего вы собираетесь
one side to the next.|с одной стороны на другую.
So you need those five things.|Итак, вам нужны эти пять вещей.
But we need to understand IP's.|Но нам нужно понимать IP.
We really, really, really do.|Мы действительно, действительно, действительно делаем.
We need to understand the difference between public and private IP addressing.|Нам нужно понимать разницу между публичной и частной IP-адресацией.
When to use them, how to subnet them?|Когда их использовать, как их разбить на подсети?
Cuz we're gonna be segmenting later on,|Потому что мы собираемся сегментировать позже,
and why should we do this?|и зачем нам это делать?
Okay, so IP, when somebody comes up to you, goes hey, what's an IP address?|Итак, IP, когда кто-то подходит к вам, спрашивает, а что такое IP-адрес?
An IP address is a logical address, that is used on a network that's assigned to every node on the network.|IP-адрес - это логический адрес, который используется в сети и назначается каждому узлу в сети.
If it's a node that's directly attached to a network.|Если это узел, который напрямую подключен к сети.
I know that some of you are saying that not every printer has an IP address,|Я знаю, что некоторые из вас говорят, что не у каждого принтера есть IP-адрес,
your right, not every printer does have an IP address.|ваше право, не у каждого принтера есть IP-адрес.
If it's plugged in to a particular machine, and then as that machine does shares the printer that has the IP that everybody gets to.|Если он подключен к определенной машине, а затем, когда эта машина действительно использует принтер, у которого есть IP-адрес, доступный всем.
But there are printers that have, there are IP printers.|Но есть принтеры, которые есть, есть IP-принтеры.
And you can go ahead and search them, and map them to your computer whether you search them through active directory,|И вы можете продолжить поиск и сопоставить их со своим компьютером, независимо от того, ищете ли вы их в активном каталоге,
whether you search them throughout the network, however it is.|ищите ли вы их по всей сети, как бы там ни было.
All right.|Отлично.
But we need to understand, and we're gonna start understanding what is this IPv4 address?|Но нам нужно понять, и мы начнем понимать, что это за адрес IPv4?
And let's go, and take a look at it right now.|И пошли, посмотрим на это прямо сейчас.
I just decided to create this little small network, and you probably saw it at the very beginning.|Я просто решил создать эту маленькую сеть, и вы, наверное, видели это в самом начале.
It's the same thing.|Это то же самое.
We've got two computers that are plugged in to a switch.|У нас есть два компьютера, подключенных к коммутатору.
And in the Desktop tab, and if you saw the earlier lessons,|На вкладке "Рабочий стол", если вы видели предыдущие уроки,
you should know, how to get in here?|ты должен знать, как сюда попасть?
And put in an IP address 192.168.1.1.|И введите IP-адрес 192.168.1.1.
And you see I just tabbed, and it put in the default mask for a class c address,|И вы видите, что я просто добавил вкладку, и он вставил маску по умолчанию для адреса класса c,
cuz it already TCP/IP suite classified it as a class c address.|Потому что пакет TCP / IP уже классифицировал его как адрес класса c.
And this would be 192.168.1.2,|И это будет 192.168.1.2,
Desktop tab, IP 192.168.1.2 Tab.|Вкладка Desktop, IP 192.168.1.2 Tab.
We don't need a gateway, we don't need a DNS.|Нам не нужен шлюз, нам не нужен DNS.
I'm just showing you what an IP address looks like, all right?|Я просто показываю вам, как выглядит IP-адрес, хорошо?
And I'm sure you, you've seen them before,|И я уверен, что вы видели их раньше,
but just in case, there you go.|но на всякий случай поехали.
Go back to the Command Prompt.|Вернитесь в командную строку.
You can do an IP config.|Вы можете настроить IP-адрес.
IP config forward slash, whoops, forward slash all,|Косая черта в конфигурации IP, упс, косая черта все,
and then you would see, let me open this up for you a little bit more.|и тогда вы увидите, позвольте мне открыть вам еще немного.
And you will see the IP address, and subnet mask of the particular computer,|И вы увидите IP-адрес и маску подсети конкретного компьютера,
and then you PNG the other computer, which is 1.2,192.68.1.2.|а затем вы PNG на другой компьютер, то есть 1.2,192.68.1.2.
And low and behold, we have connectivity.|И вот, у нас есть возможность подключения.
Not such a big deal, very small network,|Ничего особенного, очень маленькая сеть,
obviously.|очевидно.
Nothing really to think about, it's pretty simple, but hey, there's a lot of things that are,|На самом деле не о чем думать, это довольно просто, но, эй, есть много вещей, которые
that is going on here.|что здесь происходит.
We have a full duplex because we have a switch,|У нас есть полный дуплекс, потому что у нас есть переключатель,
we have two collision domains, which is a good thing, right?|у нас есть две области столкновения, что хорошо, правда?
We increase the number of collision domains from a hub to a switch.|Увеличиваем количество конфликтных доменов от концентратора до коммутатора.
Instead of one we have two, so we have that full duplex going on, back and forth, and we'll probably running if we looked at the switch at the actual|Вместо одного у нас есть два, поэтому у нас есть этот полный дуплекс, вперед и назад, и мы, вероятно, будем работать, если посмотрим на переключатель на фактическом
interface that we're running 100 megabits per second, category five cabling.|интерфейс, что мы работаем со скоростью 100 мегабит в секунду, кабели пятой категории.
Right.|Правильно.
So, again.|Итак, еще раз.
An IP address is the logical address.|IP-адрес - это логический адрес.
It works at layer three of the OSI model.|Он работает на третьем уровне модели OSI.
That we actually design, and we implement in all our nodes that are directly attached to our network.|Это мы на самом деле проектируем и реализуем во всех наших узлах, которые напрямую подключены к нашей сети.
In the next video, what we're gonna do.|Что мы будем делать в следующем видео.
Or in the next lesson, what we're gonna do is,|Или на следующем уроке мы сделаем следующее:
break down the different classes of IP address.|разбить различные классы IP-адресов.
All right.|Отлично.
But the format of the address you need to understand, very well.|Но формат обращения нужно понимать, очень хорошо.
Now one of the things, I, I do, I do wanna do, I know, I did it in other videos, and I wanna make sure, I do it in this one,|Теперь одна из вещей, я, я, я действительно хочу сделать, я знаю, я делал это в других видео, и я хочу убедиться, что я делаю это в этом,
you know in this lesson, same video.|вы знаете, в этом уроке такое же видео.
When you're looking at an IP address, and you say 192.168,|Когда вы смотрите на IP-адрес и говорите 192.168,
whoops not 268, 168.1.1, it's very simple just to look at that there,|упс, не 268, 168.1.1, это очень просто посмотреть там,
okay, so there's decimal numbers separated by a, a decimal right, and we have home the numbers started by a decimal but what you're really looking at?|хорошо, есть десятичные числа, разделенные знаком, десятичное справа, и у нас есть числа, начинающиеся с десятичного числа, но что вы на самом деле смотрите?
Is one, two, three, four, five, six,|Один, два, три, четыре, пять, шесть,
seven, eight.|семь восемь.
One, two, three, four, five, six, seven,|Один два три четыре пять шесть семь,
eight.|восемь.
One, two, three, four, five, six, seven,|Один два три четыре пять шесть семь,
eight.|восемь.
One, two, three, four, five, six, seven,|Один два три четыре пять шесть семь,
eight.|восемь.
The computer is not looking at the number 192 the computer is, sees 192 as that.|Компьютер не смотрит на номер 192, который у него есть, он видит 192 как это.
[BLANK_AUDIO]|[BLANK_AUDIO]
It sees it in its binary format.|Он видит его в двоичном формате.
You need to really understand that this is what you're looking at?|Вы действительно должны понимать, что это то, на что вы смотрите?
Right here.|Прямо здесь.
All right, because in each one of these octets 128,|Хорошо, потому что в каждом из этих октетов 128,
64, 32, oops, 32, 16, 8,|64, 32, ой, 32, 16, 8,
4, 2, and 1, you have bit values.|4, 2 и 1 у вас есть битовые значения.
Those bit values that you see up there,|Те битовые значения, которые вы видите там,
and if you can't see them cuz they're too far off over there, I'm gonna put them closer to the middle so you can see it.|и если вы их не видите, потому что они слишком далеко, я помещу их ближе к середине, чтобы вы могли это увидеть.
Those bit values right there, are the same bit values on every single octet, they do not change, they do not change.|Эти битовые значения прямо здесь, это те же самые битовые значения в каждом октете, они не меняются, они не меняются.
When I write those bit values, I use those bit values on the top.|Когда я записываю эти битовые значения, я использую эти битовые значения вверху.
So I will put 1, 2, 4, 8, 16, 32, 64, 128,|Я поставлю 1, 2, 4, 8, 16, 32, 64, 128,
and boom,|и бум,
boom, boom, boom all the way across.|бум, бум, бум полностью.
Those are your bit values.|Это ваши битовые значения.
As we get later on into our course,|Когда мы продолжим наш курс,
you'll understand the importance of those bit values when we comes to subnetting.|вы поймете важность этих битовых значений, когда мы перейдем к разделению на подсети.
All right, so those bit values do not change,|Хорошо, эти битовые значения не меняются,
but the IP address is 8-bits long in each octet.|но IP-адрес имеет длину 8 бит в каждом октете.
That's why it's called an octet, all right.|Вот почему это называется октетом.
Eight bits creates a byte, creates a number, a character.|Восемь бит создают байт, создают число, символ.
All right, and that's why we see, as humans, we see those numbers, but behind the scenes, what you're really looking at, what the computer is really|Хорошо, вот почему мы, люди, видим эти числа, но за кулисами, то, на что вы действительно смотрите, что на самом деле представляет собой компьютер.
looking at, is those binary, the binary format of that particular number.|глядя на, это двоичный, двоичный формат этого конкретного числа.
It used to be.|Это было.
And I'm gonna pick some easy numbers because I just don't wanna do any math.|И я выберу несколько простых чисел, потому что я просто не хочу заниматься математикой.
All right, 224.240.252.|Хорошо, 224.240.252.
Let's put that as an address.|Давайте представим это как адрес.
All right, so another reason why I'm doing that?|Хорошо, еще одна причина, почему я это делаю?
Because that's the table that I know, and I don't want to do any math.|Потому что это таблица, которую я знаю, и я не хочу заниматься математикой.
All right come here, one, two, three.|Хорошо, иди сюда, раз, два, три.
[BLANK_AUDIO]|[BLANK_AUDIO]
One, two, three, four.|Один два три четыре.
And then 252.|А потом 252.
One, two, three, four, five, six.|Один два три четыре пять шесть.
That is those, that IP address looks like that in binary.|То есть тот IP-адрес выглядит так в двоичном формате.
Obviously, I picked the, the table,|Очевидно, я выбрал стол,
that bit to decimal table, so will make it easy.|этот бит в десятичную таблицу, так что это упростит.
But that's what I'm trying to get at,|Но это то, что я пытаюсь понять,
that's what is looking at,|вот на что смотришь,
it's not looking at the decimal that we see, it's looking at the bina,|мы видим не десятичную дробь, а бина,
the binary bits that are on.|включенные двоичные биты.
So that's why turning things into binary is very important.|Вот почему очень важно преобразовывать вещи в двоичные файлы.
So you can never go wrong, cuz once we get into summarization or do it in binary format, you'll never go wrong, you'll always get the right answer.|Так что вы никогда не ошибетесь, потому что как только мы перейдем к обобщению или сделаем это в двоичном формате, вы никогда не ошибетесь, вы всегда получите правильный ответ.
So this, you need to understand.|Итак, вам нужно понять.
The format of this particular IP address.|Формат этого конкретного IP-адреса.
That it is 32-bits, but each one of these octets is separated in to 8-bits,|Что это 32 бита, но каждый из этих октетов разделен на 8 бит,
and that the bit values that it has on top by turning them on or off will create that particular number.|и что битовые значения, которые он имеет наверху, путем их включения или выключения создают это конкретное число.
Okay?|Ладно?
So this ladies and gentlemen, is your IPv4|Итак, дамы и господа, ваш IPv4
addresses or address.|адреса или адрес.
This is what it looks like, this is the format of it.|Вот как это выглядит, это его формат.
And we use it, so we can assign it to devices, so we can communicate with each other.|И мы используем его, чтобы назначать его устройствам, чтобы мы могли общаться друг с другом.
I'll see you in the next video.|Увидимся в следующем видео.