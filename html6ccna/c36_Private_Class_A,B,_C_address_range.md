D:\mailCloud\prjother\tmp\1\c36_Private Class A,B, C address range.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
And we're back.|И мы вернулись.
All right, so now we need to know the ranges.|Хорошо, теперь нам нужно знать диапазоны.
Right?|Правильно?
We've classified IP addresses,|Мы классифицировали IP-адреса,
done all these different things.|делал все эти разные вещи.
Now we need to know the private range of addresses.|Теперь нам нужно знать частный диапазон адресов.
Now remember I told you in previous lessons that it's very important to understand which class of address you're going to use, privately in your network,|Теперь помните, что я говорил вам в предыдущих уроках, что очень важно понимать, какой класс адресов вы собираетесь использовать в частной сети,
or publicly, but privately in your network as well, because you don't wanna run out.|или публично, но также и в частном порядке в вашей сети, потому что вы не хотите выбегать.
So the range for a class A, meaning the entire range,|Таким образом, диапазон для класса A, то есть весь диапазон,
10.0.0.1 through 10.255.255.254.|С 10.0.0.1 по 10.255.255.254.
And we need to widen that.|И нам нужно это расширить.
There we go.|Вот и все.
All right, so that is the in, so basically, the whole entire ten,|Хорошо, так что это вход, в общем, все десять,
you see an IP address that starts with a ten, it is a private IP address, private.|вы видите IP-адрес, который начинается с десяти, это частный IP-адрес, частный.
The broadcast input the network ID.|Широковещательный ввод идентификатора сети.
Network ID would be all zeros, obviously.|Очевидно, что в идентификаторе сети будут нули.
Now the broadcast address would be 10.255.255.255.|Теперь широковещательный адрес будет 10.255.255.255.
Okay, I didn't put the network ID, whether you all will, you, you'll know.|Ладно, я не указывал идентификатор сети, вы все это сделаете, вы знаете.
It's 10.0.0.0, all right, one before one.|Это 10.0.0.0, хорошо, по порядку.
So that's good there, and then, what's CIDR?|Так что это хорошо, а что же CIDR?
For our classless inter-domain routing,|Для нашей бесклассовой междоменной маршрутизации
correct?|верный?
So it's going to be a /8,|Так что это будет / 8,
and we need to bold that, because I can barely see it myself.|и нам нужно выделить это жирным шрифтом, потому что я сам едва это вижу.
Let's go ahead and use format painter here, and we'll,|Давайте продолжим и воспользуемся форматом рисования здесь, и мы,
all right, well the rest is right there so let's not do that.|хорошо, остальное здесь, так что не будем этого делать.
Thank God for Format Painter, very easy.|Слава богу за Format Painter, очень просто.
There you go.|Вот так.
Poof, okay, we'll do it that way.|Пуф, хорошо, мы так и сделаем.
No, I don't like that either.|Нет, мне это тоже не нравится.
You want to change this.|Вы хотите это изменить.
You know, there was an instructor in my previous life that he would write his name on the board until it was perfect,|Вы знаете, в моей прошлой жизни был инструктор, который писал свое имя на доске, пока оно не стало идеальным,
and then he would begin the class.|а затем он начинал занятия.
But I just, didn't take that long, CIDR 8,|Но я просто, не так много времени, CIDR 8,
CIDR 8.|CIDR 8.
All right, so that's your class A range.|Хорошо, это ваш диапазон класса А.
So, if you were to do an IP config on any computer, and you see that they're having ten.|Итак, если вы настроите IP-конфигурацию на любом компьютере, и вы увидите, что их десять.
You can, you know, you can say, oh, okay,|Вы можете, вы знаете, вы можете сказать, о, хорошо,
well,|хорошо,
they're using a private class A range.|они используют частный диапазон класса А.
They must have a lot of nodes to use that part of the class A.|У них должно быть много узлов, чтобы использовать эту часть класса A.
And not necessarily so.|И не обязательно так.
I've seen a lot of companies that have maybe a couple hundred, 20 computers,|Я видел много компаний, у которых может быть пара сотен, 20 компьютеров,
and they decided to use a class A, cuz privately you can do whatever you want.|и они решили использовать класс A, потому что в частном порядке вы можете делать все, что хотите.
But always think towards the future,|Но всегда думай о будущем,
always think and growth.|всегда думать и расти.
That if you are going to grow that you have the room to do so.|Что, если вы собираетесь расти, у вас есть для этого место.
All right, now, everything's normal there,|Хорошо, теперь там все нормально,
CIDR 8.|CIDR 8.
So that means that the, the 8 on that side, whoa,|Это означает, что восьмерка с той стороны, эй,
I moved it with my shoulder, I'm so big.|Перевела плечом, такая большая.
Okay, I moved that with the shoulder.|Хорошо, я сдвинул это плечом.
So, the ten, that's where the, the line is, always remains ten.|Итак, десять, вот где линия, всегда остается десять.
And there's a reason why I'm saying this,|И есть причина, по которой я говорю это,
and then the rest change.|а потом все остальное поменять.
Therefore, it is a CIDR 8.|Следовательно, это CIDR 8.
So now we're do a B,|Итак, теперь мы делаем B,
172.16.0.1 to 172.31,|172.16.0.1 к 172.31,
uh-oh, .255.254.|ох, 0,255,254.
Interesting, let's do the broadcast,|Интересно, давайте сделаем трансляцию,
172.31.255.255.|172.31.255.255.
And as we all know, by default, a class B has a CIDR 16.|И, как все мы знаем, по умолчанию класс B имеет CIDR 16.
But we'll make another little thing right here.|Но мы сделаем еще одну мелочь прямо здесь.
We'll say Cisco.|Мы скажем Cisco.
Let's go ahead, nope.|Давай, нет.
Let's go ahead and format that if I can actually get the mouse to do what I want it to do.|Давайте продолжим и отформатируем это, если я действительно могу заставить мышь делать то, что я хочу.
[BLANK_AUDIO]|[BLANK_AUDIO]
Format here, format there, and we can get rid of that format painter.|Отформатируйте здесь, отформатируйте там, и мы сможем избавиться от этого средства рисования форматов.
Now this is true, by default.|Теперь это правда, по умолчанию.
If you were to put any one of these private IP addresses in the properties of your TCP/IP, you're gonna say put 172.16.0.1 and you hit the tab key,|Если вы поместите любой из этих частных IP-адресов в свойствах вашего TCP / IP, вы скажете, что поместите 172.16.0.1, и нажмете клавишу табуляции,
it's gonna recognize 172 that is part of the B range.|он распознает 172, которые являются частью диапазона B.
Therefore, it will automatically populate your subnet mask as 255.255.0.0.|Следовательно, он автоматически заполнит вашу маску подсети как 255.255.0.0.
But why does it go from 1, from 16 to 31.|Но почему он идет с 1, с 16 на 31.
And let me zoom in a little bit.|И позвольте мне немного увеличить масштаб.
Wonder if you guys can see that?|Интересно, видите ли вы это?
Make sure you can see that well.|Убедитесь, что вы хорошо это видите.
All right, see it goes from 16 to 31.|Хорошо, смотри, идет от 16 до 31.
So, is the line really between the second and third octet?|Итак, действительно ли линия между вторым и третьим октетами?
I think not.|Думаю, нет.
I think the line is in between somewhere in the second octet.|Я думаю, что строка находится где-то посередине во втором октете.
Let's take a look at, see how that all works out using our subnetting techniques,|Давайте посмотрим, как это все работает, используя наши методы разделения на подсети,
which all of you have done and practiced constantly, since you've known me, okay?|что все вы делали и практиковали постоянно, с тех пор как знаете меня, хорошо?
So, 172 we'll do it here.|Итак, 172 мы сделаем это здесь.
172.16 doesn't change.|172,16 не меняется.
That stays the same, all right.|Это остается неизменным, хорошо.
Then we have one, two, three, four, five,|Тогда у нас есть один, два, три, четыре, пять,
six, seven, eight, one, two, three,|шесть, семь, восемь, один, два, три,
four, five, six, seven, eight, correct?|четыре, пять, шесть, семь, восемь, верно?
16 is our first number.|16 - наше первое число.
Hm, so that means that my line is right there,|Хм, значит, моя линия прямо там,
because that fourth bit, that bit next to that line,|потому что этот четвертый бит, этот бит рядом с этой строкой,
the value of that bit is 16.|значение этого бита - 16.
And then if you were to add, not those.|А потом, если добавить, не те.
If you were to add these bit values here,|Если бы вы добавили сюда эти битовые значения,
it's 15.|это 15.
So you take the 15 and, am I in the right place?|Итак, вы берете 15, и я в нужном месте?
I'm not in the right place, I apologize.|Я не в том месте, прошу прощения.
[BLANK_AUDIO]|[BLANK_AUDIO]
One, two, three, four, five, six, seven,|Один два три четыре пять шесть семь,
eight, and let's make this bigger here.|восемь, и давайте сделаем это больше здесь.
There we go, I don't want to confuse anybody.|Итак, я не хочу никого путать.
I almost did.|Я почти сделал.
Let's put our line where it belongs in the second octet,|Поместим нашу строку на место во втором октете,
all right, cuz that bit value's 16.|хорошо, потому что это битовое значение 16.
Then as I was saying, if you were to add those bits at 15, so 15 plus 16 is 31.|Затем, как я уже говорил, если вы добавите эти биты к 15, то 15 плюс 16 будет 31.
Then you have, you add these bits in the 3rd octet,|Затем вы добавляете эти биты в третий октет,
which you 255, then you have 255.|что у вас 255, то у вас есть 255.
And then the last octet, you add those bits right there, 255, 255.|И затем последний октет, вы добавляете эти биты прямо здесь, 255, 255.
So that's indeed how Cisco, in their, in their books,|Вот как Cisco в своих книгах
they go into that granular detail to show you how they came about that range from 16 to 31.|они углубляются в детали, чтобы показать вам, как они пришли к диапазону от 16 до 31.
It's truly, a CIDR 12.|Это действительно CIDR 12.
And Cisco books are the only ones that you'll see something like that.|И книги Cisco - единственные, в которых вы увидите нечто подобное.
Because that's the detail that they go into.|Потому что это детали, в которые они входят.
They want you to know everything, how everything breaks down.|Они хотят, чтобы вы все знали, как все ломается.
Which is great, and it's interesting,|Что здорово и интересно,
because there's always a curiosity as,|потому что всегда есть любопытство,
hey, why, why isn't it, why do they stop at 31?|эй, почему, почему нет, почему они останавливаются на 31?
Why isn't it 172.16, 172.16?|Почему это не 172,16, 172,16?
Why do they pick 172.16 to 172.31?|Почему они выбирают 172,16–172,31?
Why those numbers?|Почему эти числа?
Well, now you know.|Что ж, теперь вы знаете.
Because the true CIDR is really in the second octet with a,|Поскольку истинный CIDR действительно находится во втором октете с символом
the, that's a CIDR 12.|это CIDR 12.
That's how they come up with that incrementation of 16,|Вот как они пришли к приращению 16,
and they go way to 31.|и они идут до 31.
Now I'm not telling you when you go take a test it asks you,|Я не говорю тебе, когда ты идешь на тест, тебя спрашивают,
what is the default mask for a class B address,|какая маска по умолчанию для адреса класса B,
you're gonna say well Laz told me a CIDR 12.|Ты скажешь, что Лаз сказал мне CIDR 12.
No, no, no, no, we're doing private IP addressing.|Нет, нет, нет, нет, мы занимаемся частной IP-адресацией.
In an examination, they're not going into that granular detail either.|На экзамене они также не вдавались в подробности.
So if they ask you what is the default subnet mask of a class B,|Поэтому, если вас спросят, какая маска подсети по умолчанию для класса B,
you will say CIDR 16 or 255.255.0.0.|вы скажете CIDR 16 или 255.255.0.0.
Because, like I said, if you were to put this address,|Потому что, как я сказал, если вы укажете этот адрес,
that 172.16.0.1 into your TCP/IP properties under the IP address field and hit tab, your subnet mask will automatically fill with 255.255.0.0.|что 172.16.0.1 в ваши свойства TCP / IP в поле IP-адреса и нажмите вкладку, ваша маска подсети автоматически заполнится 255.255.0.0.
But, if sometime in the future they decide to give you a more granular question that states something to this effect.|Но, если когда-нибудь в будущем они решат задать вам более подробный вопрос, в котором будет что-то указано на этот счет.
In private IP addressing, the Class B range, what is the true subnet mask?|Какова истинная маска подсети при частной IP-адресации, диапазон класса B?
If they ask you something like that,|Если они спросят у вас что-то подобное,
then they're hinting to the CIDR /12 as you see over here on this side.|то они намекают на CIDR / 12, как вы видите здесь, с этой стороны.
That's CIDR /12, right, because that's where your line is at.|Это CIDR / 12, верно, потому что там находится ваша линия.
But there hasn't been any question like that asked at all.|Но такого вопроса вообще не было.
There hasn't even been a question about what's subnet mask,|Даже не было вопроса о том, что такое маска подсети,
what's the default subnet mask of a class B for the CCNA.|какая маска подсети по умолчанию для класса B для CCNA.
But again, if asked, at least now you know.|Но опять же, если спросить, по крайней мере, теперь вы знаете.
You can do it at cocktail parties.|Вы можете сделать это на коктейльных вечеринках.
You can let them know what the real subnet mask is for a private class B address.|Вы можете сообщить им, какова реальная маска подсети для частного адреса класса B.
Why the range, you can say, why the range is from 16 to 31.|Почему диапазон, можно сказать, почему диапазон от 16 до 31.
Because of that CIDR 12.|Из-за этого CIDR 12.
But again, do your research, do your research.|Но опять же, сделайте свое исследование, сделайте свое исследование.
Go to Cisco Press Books,|Перейдите в Cisco Press Books,
and that's where you're gonna see that information, all right?|и вот где вы увидите эту информацию, хорошо?
All right.|Отлично.
Now, now that you know that I've took you behind the curtain and you saw the secret to that,|Теперь, когда вы знаете, что я отвел вас за занавеску, и вы увидели секрет этого,
now let me see if you know the answer to this next, to the C.|Теперь позвольте мне посмотреть, знаете ли вы ответ на следующий вопрос, на C.
Okay?|Ладно?
In the C we have 192.168.0.1 to 192.168.255.254.|В C мы имеем 192.168.0.1 до 192.168.255.254.
Interesting once again.|Еще раз интересно.
[BLANK_AUDIO]|[BLANK_AUDIO]
Yes, and things just get shifted all over the place.|Да, и вещи просто меняются повсюду.
Okay.|Ладно.
We can do a Ctrl+Z there.|Мы можем сделать там Ctrl + Z.
I don't, I don't like that all.|Я не люблю, мне все это не нравится.
Let me just go into, get this right here.|Позвольте мне войти, сделайте это прямо здесь.
Format painter there with a number, and it still gets shifted this way, that's lovely, all right.|Отформатируйте рисовальщик там с номером, и он все равно сдвигается в эту сторону, это прекрасно, хорошо.
So we're just gonna bring them in like this.|Так что мы просто приведем их вот так.
We'll bold it, and we'll just increase the size of it, slowly but surely.|Мы выделим его жирным шрифтом и просто увеличим его размер, медленно, но верно.
And then we'll bring it out this way.|А потом мы вынесем это таким образом.
Bring it out this way.|Выведи это так.
There we go, good enough.|Вот и все, достаточно хорошо.
So what's the secret there?|Так в чем же секрет?
What is the mask, the broadcast, obviously we know what that is.|Что это за маска, трансляция, очевидно, мы знаем, что это такое.
That's going to be, let me format this real quick.|Это будет, позвольте мне отформатировать это очень быстро.
I try to make life easy on myself.|Я стараюсь облегчить себе жизнь.
I, I don't think I have.|Я не думаю, что у меня есть.
192.168.255.255, all right,|192.168.255.255, ладно,
that's what the broadcast is for that one.|вот что такое трансляция для этого.
But what is the CIDR?|Но что такое CIDR?
As we all know for a class C,|Как мы все знаем, для класса C,
it's a CIDR 24, but is it?|это CIDR 24, но так ли это?
Take a look at the example above.|Взгляните на приведенный выше пример.
And take a look at what's happening below.|И посмотрите, что происходит ниже.
What is the true subnet mask?|Какова настоящая маска подсети?
You have the 192.168, that doesn't change.|У вас 192.168, это не меняется.
What actually changes is, starts in the third octet.|Фактически изменяется то, что начинается с третьего октета.
You have from 0 to 255.|У вас от 0 до 255.
So really what they did, was just cut it down the middle.|Так что на самом деле то, что они сделали, было просто разрезано пополам.
So Cisco's explanation as to why that happens is because.|Итак, Cisco объясняет, почему это происходит, потому что.
[BLANK_AUDIO]|[BLANK_AUDIO]
It's a CIDR 16.|Это CIDR 16.
[BLANK_AUDIO]|[BLANK_AUDIO]
But again, you will never ever, unless specifically asked the question,|Но опять же, вы никогда не будете, если специально не зададите вопрос,
like I stated previously, you will always answer a CIDR 24.|как я уже говорил ранее, вы всегда будете отвечать на CIDR 24.
But now you know that, really,|Но теперь вы знаете, что на самом деле
the dividing line is between the second and third octet.|разделительная линия проходит между вторым и третьим октетами.
That's why the third octet can change, but the first two do not.|Вот почему третий октет может изменяться, а первые два - нет.
If by default, it was here, in the 24,|Если по умолчанию он был здесь, в 24,
then nothing can change after that.|после этого ничего не может измениться.
But it will.|Но это будет.
So that's why you're allowed so many networks using that type of address because the line actually is a CIDR 16.|Вот почему вам разрешено использовать такой тип адреса во многих сетях, потому что линия на самом деле является CIDR 16.
And again, these private IP addresses,|И снова эти частные IP-адреса,
again, used internally they,|опять же, внутренне они,
they were made on purpose for us to use internally.|они были созданы специально для использования внутри компании.
They took out chunks from the entire range and said okay, this will be used.|Они вынули куски из всего ассортимента и сказали, хорошо, это будет использовано.
You can do whatever you want with them inside your network.|Вы можете делать с ними все, что хотите, внутри своей сети.
Just know that you can't route with them outside, like in the,|Просто знайте, что вы не можете проехать с ними снаружи, как в,
we talked about it in the previous lecture.|мы говорили об этом в предыдущей лекции.
They're not routable on the internet,|Они не маршрутизируются в Интернете,
unless you use, you know, some,|если вы не используете, знаете, некоторые,
some type of net in order to get out.|какой-то тип сети, чтобы выбраться.
You need a public IP address.|Вам нужен публичный IP-адрес.
But for class E, that's your range.|Но для класса E это ваш диапазон.
Do you need to know this?|Вам нужно это знать?
Yes, you do need to know this, at least the default CIDRs, we all know,|Да, вам нужно это знать, по крайней мере, CIDR по умолчанию, все мы знаем,
as we explained it earlier in the course.|как мы объясняли ранее в курсе.
But you need to know the range of a private IP address.|Но вам нужно знать диапазон частного IP-адреса.
You must know the range of a private IP address if you're gonna be in networking.|Вы должны знать диапазон частного IP-адреса, если собираетесь работать в сети.
As well as, you know, that we learn how to classify an address.|А также, как вы знаете, мы учимся классифицировать адрес.
You need to learn how to classify private IP addresses as well.|Вам также необходимо научиться классифицировать частные IP-адреса.
All right.|Отлично.
All right, we've come to the end of the lecture.|Хорошо, мы подошли к концу лекции.
That's not a big deal.|Это не имеет большого значения.
Private IP addressing, not routable on the internet, only use internal.|Частный IP-адрес, не маршрутизируемый в Интернете, используется только внутренний.
I'll see you in the next one.|Увидимся в следующем.
[BLANK_AUDIO]|[BLANK_AUDIO]