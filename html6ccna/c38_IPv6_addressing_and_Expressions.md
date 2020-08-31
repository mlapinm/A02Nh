D:\mailCloud\prjother\tmp\1\c38_IPv6 addressing and Expressions.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
Okay, comes time to break down the IPV6|Хорошо, пришло время сломать IPV6
address.|адрес.
How do we even begin to break down an,|Как мы вообще начинаем ломать,
address that's a 120-bits long?|адрес длиной 120 бит?
Well we've taken into sections, IPv6|Ну мы разобрались по разделам, IPv6
address each section is separated by a colon instead of a decimal, where an IPv4 you had four octets each octet represented 8-bits|адрес, каждый раздел отделяется двоеточием вместо десятичного числа, где в IPv4 у вас было четыре октета, каждый октет представлял 8 бит
right?|право?
And they're separated by a decimal with IPv6 you have sections.|И они разделены десятичной дробью с IPv6 у вас есть разделы.
Each section is separated by a colon, and each section is 16-bits.|Каждая секция разделена двоеточием, и каждая секция состоит из 16 бит.
Now why is it 16 bits?|Теперь почему это 16 бит?
Because each hexadecimal number, the 2,|Поскольку каждое шестнадцатеричное число 2,
the 0, and I'm not using my arm, remember, I have an injury in my right arm.|0, и я не использую свою руку, помните, у меня травма правой руки.
The 2, the 0, the 0, the 1, all right.|2, 0, 0, 1, все в порядке.
Each one of those is a hexadecimal number that's 4-bits long.|Каждое из них представляет собой 4-битное шестнадцатеричное число.
Therefore, 4 times 4 is 16.|Следовательно, 4 умножить на 4 будет 16.
So if you have right here, I'm sorry you have my back to you right here.|Так что, если вы правы здесь, мне жаль, что вы стоите к вам спиной прямо здесь.
Is that, yeah, up to right there those,|Это, да, прямо там те,
these first four sections is considered the network portion of the address.|эти первые четыре раздела считаются сетевой частью адреса.
All right, that's 64-bits long, cuz again 16,|Хорошо, это 64-битная длина, потому что снова 16,
16, and 16, and 16, that's 64-bits.|16, и 16, и 16, это 64-битные.
So there's your 64-bit portion of the address.|Итак, вот ваша 64-битная часть адреса.
And this section over here, it's also the same 64-bits, but it is called the interface ID or you can think of it as the host portion of|И этот раздел здесь, он также тот же 64-битный, но он называется идентификатором интерфейса, или вы можете рассматривать его как часть хоста
the address.|адрес.
But it's called the interface ID.|Но это называется идентификатором интерфейса.
With IPv6 really the interface ID, we don't need to worry too much about,|Поскольку IPv6 действительно является идентификатором интерфейса, нам не нужно особо беспокоиться,
cuz remember I spoke before, that they have over 15 Quintilian or 18 Quintilian something, something,|Потому что помните, я говорил раньше, что у них есть более 15 квинтилийцев или 18 квинтилийцев, что-то, что-то,
something or other addresses,|какие-то адреса,
so it's really a lot of addresses that you don't need to be worried about.|так что это действительно много адресов, о которых вам не нужно беспокоиться.
Especially when we have features that can automatically assign that for us.|Особенно, когда у нас есть функции, которые могут автоматически назначать это за нас.
But since you can use all those numbers,|Но поскольку вы можете использовать все эти числа,
you can put whatever you want, you know,|вы можете положить все, что хотите, вы знаете,
you can try make it make sense.|вы можете попытаться понять это.
But you put whatever you want.|Но ставишь что хочешь.
So, it's broken down into two parts.|Итак, он разбит на две части.
Now this right here, is kinda hard even for myself to get use to saying, cuz I'm always saying CIDR CIDR CIDR or subnet,|Теперь это прямо здесь, даже мне довольно сложно привыкнуть к словам, потому что я всегда говорю CIDR CIDR CIDR или подсеть,
it's not a CIDR, it's not a subnet mask it is called the network prefix it is specifically used in routing purposes only.|это не CIDR, это не маска подсети, это называется префиксом сети, он специально используется только для целей маршрутизации.
The reason I put 64 here is because in your book it tells you,|Причина, по которой я поставил здесь 64, заключается в том, что в вашей книге говорится:
if you really don't know what to put, you can put just the default 64,|если вы действительно не знаете, что поставить, вы можете поставить только 64 по умолчанию,
and the rest will take care of itself,|а остальное позаботится само,
okay?|Ладно?
Do the feature that ic IP version 6 brings to us, okay.|Сделайте то же самое, что и ic IP версии 6, хорошо.
As you can see here, I don't do that.|Как видите, я этого не делаю.
You know, put 56 because when I do my labs,|Вы знаете, ставлю 56, потому что, когда я делаю свои лаборатории,
I have my students subnet as you will be subnetting, and IPv6 as well.|У меня есть подсеть моих учеников, так как вы будете разбивать ее на подсети, а также IPv6.
All right.|Отлично.
Which is, I used the same practice I do for IPv4 for the basics of subnetting in IPv6.|То есть я использовал ту же практику, что и для IPv4, для основ разделения на подсети в IPv6.
But that, that is your address right here,|Но это ваш адрес прямо здесь,
right here.|Прямо здесь.
This whole 128-bit address is your IPv6|Весь этот 128-битный адрес и есть ваш IPv6
address.|адрес.
Now, it's long, it's long, so they've come up with ways where we can shorten the address.|Это долго, это долго, поэтому они придумали способы сократить адрес.
Now I put some zeros there, not enough probably, but I did put some zeros in there because one of the rules with IPv6,|Теперь я поставил туда несколько нулей, вероятно, недостаточно, но я поставил несколько нулей, потому что одно из правил с IPv6,
and expressing an IPv6 address which are the things that you're gonna be tested on because they want you to come up to look at an IPv6 address and say hey,|и выражая адрес IPv6, на котором вы собираетесь тестироваться, потому что они хотят, чтобы вы подошли, взглянули на адрес IPv6 и сказали: "Эй,
that's a valid IPv6 address.|это действительный адрес IPv6.
Well in order to do that, one of the rules is you can take out the leading zeros.|Для этого одно из правил - вы можете убрать ведущие нули.
Any zero in the front of the address, you can remove it.|Любой ноль перед адресом можно убрать.
Okay.|Ладно.
So you came it look like this, all right.|Итак, вы пришли, это выглядит вот так, хорошо.
So that can shorten the address.|Так что это может сократить адрес.
And let's just say for example that, this section right here was all zeros, right?|И давайте просто скажем, например, что в этом разделе были все нули, верно?
We can even have a double colon, but you can only have one double colon in your address.|У нас может быть даже двойное двоеточие, но в адресе может быть только одно двойное двоеточие.
You cannot have two double colons, if for example this one here, this last portion here.|У вас не может быть двух двойных двоеточий, например, вот здесь, а вот последняя часть.
It was all zeros, and we did this, that would be an invalid address.|Это были все нули, и мы сделали это, это был бы недействительный адрес.
You would actually have to put a zero in there,|На самом деле вам нужно будет поставить ноль,
cuz if you do not, then it won't know!|Потому что, если вы этого не сделаете, он не узнает!
It won't know where to put the zero.|Он не знает, куда поставить ноль.
It's like I don't know.|Как будто я не знаю.
I don't know where to put the zero.|Не знаю, где поставить ноль.
So it gets confused.|Так что это сбивает с толку.
So it has those rules.|Итак, у него есть эти правила.
So we can take out leading zeros to make the address shorter, and we can use,|Таким образом, мы можем убрать ведущие нули, чтобы сделать адрес короче, и мы можем использовать,
if you have a consecutive set of zeros you can truncate it by using a double colon,|если у вас есть последовательный набор нулей, вы можете обрезать его, используя двойное двоеточие,
we should know that when we take a look,|мы должны знать, что когда мы посмотрим,
and I'll give you a sneak peek or not really a sneak peek is that one of the type of addresses, I guess looking for the enter, Enter key.|и я дам вам быстрый взгляд или не совсем быстрый взгляд, это один из типов адресов, я думаю, ищу ввод, вводить ключ.
Okay.|Ладно.
Double colon, right, the loop back, double colon 1.|Двойное двоеточие, право, петля назад, двойное двоеточие 1.
We do it already, cuz that is the loop back address in IPv6.|Мы уже это делаем, потому что это адрес обратной связи в IPv6.
The loop back address in IPv6,|Адрес обратной связи в IPv6,
cuz there is only one loop back address in IPv6 and that is it, unlike IPv4.|Потому что в IPv6 есть только один адрес обратной связи, и это все, в отличие от IPv4.
So, what that means, that's a whole bunch of zeroes in between there.|Итак, что это значит, это целая куча нулей между ними.
And then 1, right?|А потом 1, верно?
So, they've made it simpler for us to not to be like, so painful and actually, write out these long addresses.|Итак, они упростили для нас, чтобы мы не были такими болезненными и не выписывали эти длинные адреса.
So, when you take your test, which is the goal of the course.|Итак, когда вы сдаете тест, это и есть цель курса.
Is to prepare you to take the CCNA certification.|Подготовить вас к сертификации CCNA.
You need to be able to pick out a valid IPv6 address.|У вас должна быть возможность выбрать действительный адрес IPv6.
Ladies and gentleman, I'm here to tell you.|Дамы и господа, я здесь, чтобы сказать вам.
That in hexadecimal value, they don't go beyond f.|В шестнадцатеричном значении они не выходят за пределы f.
So if, if you see something that says [BLANK_AUDIO]|Если вы видите что-то с надписью [BLANK_AUDIO]
G, that is not a valid IPv6 address,|G, это недействительный IPv6-адрес,
because you cannot go beyond f.|потому что вы не можете выйти за рамки f.
And they'll throw things out there, out there like that for you, okay?|И они будут бросать тебе такие вещи, хорошо?
Or to you, they'll put x, y, z or they'll put like ridiculous numbers,|Или вам они поставят x, y, z или поставят как нелепые числа,
not enough sections, remember it's eight sections, four and four.|недостаточно разделов, помните, что это восемь разделов, четыре и четыре.
Each sec, each section being 16-bits.|Каждую секунду, каждый раздел состоит из 16 бит.
So be very careful when doing that.|Так что будьте очень осторожны при этом.
If you don't have enough sections, it's because like here.|Если вам не хватает разделов, это потому, что как здесь.
We have one, two, three, four, five, six,|У нас есть один, два, три, четыре, пять, шесть,
seven.|Семь.
Hm, but we have a double colon.|Хм, но у нас двойное двоеточие.
What does that mean?|Что это значит?
That means in that double colon right there, one, two, three, four.|Это означает, что в этом двойном двоеточии: один, два, три, четыре.
We have a set of four zeros.|У нас есть набор из четырех нулей.
So that will complete the one, two, three,|Так что это завершит один, два, три,
four, five, six, seven, eight.|четыре, пять, шесть, семь, восемь.
So we'll be looking out for that,|Так что мы будем следить за этим,
cuz just by looking at the maybe the font size not big enough.|Потому что просто взглянув на то, что размер шрифта может быть недостаточно большим.
I know for me it's never big enough, but when I look at it,|Я знаю, что он никогда не бывает достаточно большим, но когда я смотрю на него,
you look at the address, you kind of skip over maybe the double colon or you just,|вы смотрите на адрес, вы как бы пропускаете, может быть, двойное двоеточие или просто,
oh, my God, I only see five sections cuz the, the colons are too small.|Боже мой, я вижу только пять разделов, потому что двоеточия слишком маленькие.
Be very careful when you're picking that out, all right.|Будьте очень осторожны, выбирая это, хорошо.
So look for things that don't go over f.|Так что ищите вещи, которые не выходят за рамки f.
Look for double colons, cause they're not valid.|Ищите двойные двоеточия, потому что они недействительны.
Anything over f is not valid.|Все, что больше f, недопустимо.
You only can take out the leading zeros,|Вы можете вынести только ведущие нули,
the leading zeros.|ведущие нули.
And remember, this right here is called the network prefix.|И помните, вот это называется префиксом сети.
That is used for routing only.|Это используется только для маршрутизации.
What do I mean by that?|Что я имею в виду?
Let's go ahead, and remove the interface ID portion of the address.|Давайте продолжим и удалим часть адреса, содержащую идентификатор интерфейса.
So it wont that horrible to look at, and we just put I'll do another colon here.|Так что на это не так уж и ужасно смотреть, и мы просто помещаем сюда «Я сделаю еще одну двоеточие».
All right.|Отлично.
And that was just like, you see up there.|И это было похоже на то, как вы видите.
We have let me get rid of the loop back address over here.|Мы позволили мне избавиться от адреса обратной петли здесь.
Okay.|Ладно.
You're looking at the network portion of the address,|Вы смотрите на сетевую часть адреса,
but each section has its purpose.|но у каждого раздела есть свое предназначение.
Within the first section, this is the registry, the Arin.|В первом разделе это реестр Arin.
The people who, the Internet that assigns the wow,|Люди, которые, Интернет, который назначает "вау",
okay, really?|хорошо, правда?
This portion of the address, doesn't want to do the finger is the American Registry.|Эта часть адреса, которую не хотят трогать, - это американский реестр.
This tells us, hey, this a globally unique address, and that's what that is, a globally unique address.|Это говорит нам, что это глобально уникальный адрес, и вот что это такое, глобально уникальный адрес.
The next section, all right now I did it.|Следующий раздел, ладно сейчас я сделал.
The next section is your particular ISP.|Следующий раздел - это ваш конкретный интернет-провайдер.
So they got their address from the registry, and then this portion right here, the CADD right could be bad,|Итак, они получили свой адрес из реестра, а затем эта часть прямо здесь, право на CADD могло быть плохим,
it could be face like in Facebook.|это могло быть лицо, как в Facebook.
All right?|Отлично?
That is your company.|Это ваша компания.
That will represent your company.|Это будет представлять вашу компанию.
It's your company is using a particular ISP, that's using whatever registry.|Это ваша компания использует определенного интернет-провайдера, который использует любой реестр.
Okay?|Ладно?
And then the last portion of the address,|И затем последняя часть адреса,
this fourth section right there, that is for you to subnet.|этот четвертый раздел прямо здесь, он предназначен для подсети.
Yes, the wonderful world of subnetting.|Да, чудесный мир подсетей.
All right, so yes you will be subnetting in IPv6.|Хорошо, так что да, вы будете разбивать подсети в IPv6.
Just because you have Quintilian, and 18|Просто потому, что у вас есть Quintilian, а 18
Quintilian, and all sorts of Quintilian addresses, you still will subnet, because it's about networking, and building a hierarchy of those Quintilian|Quintilian и всевозможные Quintilian адреса, вы все равно будете использовать подсети, потому что речь идет о сети и построении иерархии этих Quintilian
addresses within your network.|адреса в вашей сети.
So you will be subnetting, and that is what this number is for?|Итак, вы будете разбивать на подсети, и для чего этот номер?
And just to break it down even further, so you can understand what I did up here.|И просто чтобы разбить это еще дальше, чтобы вы могли понять, что я здесь сделал.
This last portion and again,|Эта последняя порция и снова,
giving you a sneak peak into the subnetting portion of it.|давая вам возможность заглянуть в его подсети.
Okay remember, each one of these bits or bytes is 4-bits long.|Хорошо помните, каждый из этих битов или байтов имеет длину 4 бита.
So you have one, two, three, four.|Итак, у вас есть один, два, три, четыре.
One, two, three, four.|Один два три четыре.
One, two, three, four.|Один два три четыре.
One, two, three, four.|Один два три четыре.
Oh, and I got another space here.|О, и у меня здесь есть еще одно место.
There we go.|Вот и все.
So really,|Серьезно,
this portion right here is, means oh, here we go again.|вот эта часть, значит, вот и мы снова.
It means this right here.|Это значит прямо здесь.
Each one of those numbers is 4-bits long.|Каждое из этих чисел имеет длину 4 бита.
So where does that 56 come in?|Так что же тут 56?
How did you get that 56?|Как вы получили эти 56?
Well, you have 16 and 16, that's 32, and 16 more is 48.|У вас есть 16 и 16, это 32, а еще 16 - 48.
Then we have 49, 50, 51, fift, wait wa,|Тогда у нас есть 49, 50, 51, пять, подождите,
where am I?|Где я?
48, 49, okay I'm going to use, I'm going to move this over here.|48, 49, хорошо, я собираюсь использовать, я собираюсь переместить это сюда.
I'm going to use the mouse, because my finger's not working.|Я собираюсь использовать мышь, потому что у меня не работает палец.
I'll bring it over here so you guys can see.|Я принесу его сюда, чтобы вы, ребята, увидели.
All right, then I'll look at the laptop,|Хорошо, тогда я посмотрю на ноут,
so I know what I'm doing, here we have 16,|так что я знаю, что делаю, у нас их 16,
32, 48, 49, 50, 51, 52, 53, 54, 55, 56.|32, 48, 49, 50, 51, 52, 53, 54, 55, 56.
So that imaginary line that we always talk about is right there.|Итак, эта воображаемая линия, о которой мы всегда говорим, прямо здесь.
And when we get you subnetting you'll see.|И когда мы получим подсети, вы увидите.
So that slide come up in my lab, and I get a 56 cuz we actually take an actual network and we, we're given a network prefix of whatever.|Итак, этот слайд появился в моей лаборатории, и я получил 56, потому что мы на самом деле берем реальную сеть, и нам дают какой-либо сетевой префикс.
And then we look for the amount of subnets that we require, and then we put the appropriate number network prefix for our particular networks.|Затем мы ищем необходимое количество подсетей, а затем вводим соответствующий номерной сетевой префикс для наших конкретных сетей.
All right, so that's how we do it, when we are subnetting an IPv6,|Хорошо, вот как мы это делаем, когда мы разбиваем IPv6 на подсети,
but that is, what that portion is for.|но это то, для чего предназначена эта часть.
So it's not that difficult.|Так что это не так уж и сложно.
It's just again, like I said previously,|Это снова, как я уже сказал ранее,
it's getting used to looking at it,|он привыкает смотреть на это,
and understanding that you're not working with decimal numbers anymore.|и понимание того, что вы больше не работаете с десятичными числами.
You're working with hexadecimal numbers,|Вы работаете с шестнадцатеричными числами,
and each hexadecimal number is 4-bits long.|и каждое шестнадцатеричное число имеет длину 4 бита.
And then the bit values, all those hex numbers are now, you know, they're one,|А затем битовые значения, все эти шестнадцатеричные числа теперь, вы знаете, они одно,
two, four, eight, that's it.|два, четыре, восемь, вот и все.
And they don't go higher than f, right?|И они не поднимаются выше f, верно?
One, two, three, four, five, six, seven,|Один два три четыре пять шесть семь,
eight, nine, a, b, c, d, e, f.|восемь, девять, а, б, в, г, д, е.
Now we start again.|Теперь начнем снова.
So it's, again, it takes kind of getting used to, looking at that type of address.|Так что, опять же, нужно привыкнуть, глядя на этот тип адреса.
But once you do, and you start looking at it, and you start seeing how it's broken down which is really where you need to focus on, when you take|Но как только вы это сделаете, и вы начнете смотреть на него, и вы начнете видеть, как он разбит, и именно на этом вам действительно нужно сосредоточиться, когда вы берете
your test is how they break down?|ваш тест, как они ломаются?
Or when you're trying to find a valid IP address, you gotta make sure the rules that we talked about, no double colons, no|Или когда вы пытаетесь найти действующий IP-адрес, вы должны убедиться, что правила, о которых мы говорили, без двойных двоеточий, без
letters above f, make sure that it equals out to eight sections if they've truncated something, okay.|буквы над f, убедитесь, что оно равно восьми разделам, если они что-то урезали, хорошо.
So be on the lookout for something like that you should have no worries, no worries.|Так что будьте в поисках чего-то подобного, у вас не должно быть ни о каких заботах.
So there you go,|Итак, вы идете,
that's what an IPv6 address looks like that's the breakdown of it.|вот как выглядит IPv6-адрес, вот и все.
Now you've seen it, not that difficult,|Теперь вы это видели, не так уж и сложно,
just learn it, and work with it, and you'll be all right.|просто выучите это и работайте с этим, и все будет в порядке.
I'll see you in the next section.|Увидимся в следующем разделе.
[BLANK_AUDIO]|[BLANK_AUDIO]