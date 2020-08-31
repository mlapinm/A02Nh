D:\mailCloud\prjother\tmp\1\c41_ICMPv6.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
Welcome back everybody.|С возвращением всем.
Now you know me, you know I like to keep things interesting.|Теперь ты меня знаешь, ты знаешь, что мне нравится делать вещи интересными.
So if you've really been paying close attention,|Итак, если вы действительно уделяете пристальное внимание,
there's something about me that has changed.|что-то во мне изменилось.
What could that be?|Что это могло быть?
I wonder.|Я думаю.
All right?|Отлично?
So, if you can make a comment on the video, hey,|Итак, если вы можете прокомментировать видео, привет,
we shall see if you were paying attention from the previous lesson to this lesson.|посмотрим, обратили ли вы внимание с предыдущего урока на этот урок.
What did I do to myself that's different?|Что я сделал с собой по-другому?
I gotta keep you guys interested.|Я должен держать вас в курсе, ребята.
I gotta keep you guys, you know, paying attention in the video.|Я должен держать вас, ребята, вниманием к видео.
So that's why you see me all crazy.|Вот почему ты видишь меня сумасшедшим.
Now, where in the previous video, we talked about auto-configuration.|Теперь, где в предыдущем видео мы говорили об автоконфигурации.
That's one of the new features of IPv6.|Это одна из новых функций IPv6.
Another, not new feature, but a newer version is ICMP version six which is, very nice.|Еще одна, не новая функция, но более новая версия - это шестая версия ICMP, что очень приятно.
One of the things that IP, oop IP,|Одна из вещей, которые IP, oop IP,
ICMP version 6 does, it does neighbor discovery.|ICMP версии 6 делает, он обнаруживает соседей.
Remember there's no more broadcast in IPv6.|Помните, что в IPv6 больше нет широковещательной передачи.
So now ICMP version 6,|Итак, теперь ICMP версии 6,
what it does it goes out and actually does neighbor solicitations.|что он делает, он выходит и фактически делает запросы соседей.
And then it receives neighbor acknowledgement.|И затем он получает подтверждение соседа.
And with each neighbor solicitation,|И с каждым ходатайством соседа,
there is a little packet that goes with it that's called DAD.|есть маленький пакет, который называется DAD.
D-a-d.|Д-а-д.
All right.|Отлично.
Duplicate address detection.|Обнаружение повторяющегося адреса.
To see that there is no duplicate address on the network.|Чтобы убедиться, что в сети нет повторяющихся адресов.
And I believe earlier in the course I mentioned something like that,|И я думаю, что ранее в курсе я упоминал нечто подобное,
that my guide.|это мой гид.
How can you have a duplicate address when you have over 15 quintillion addresses in an ICM, in an IP version 6 address, but|Как у вас может быть дублированный адрес, если у вас более 15 квинтиллионов адресов в ICM, в IP-адресе версии 6, но
either way.|в любом случае.
It, this kind of communication occurs with the use of ICMPv6,|Такое общение происходит с использованием ICMPv6,
so it has a new job as well, which is namer discovery.|так что у него есть и новая работа - открытие имен.
And it also goes between routers or two routers, and between routers is called router solicitation, and router acknowledgement,|И он также проходит между маршрутизаторами или двумя маршрутизаторами, и между маршрутизаторами это называется запросом маршрутизатора и подтверждением маршрутизатора,
so that's all based on multi task, there is no more broadcast, so that arp is gone.|так что все основано на многозадачности, широковещательной передачи больше нет, так что arp пропал.
That arp is completely gone, now it's all this neighbor discovery, which is great.|Этот arp полностью исчез, теперь это все обнаружение соседей, и это здорово.
So you can see that with IPv6 that we've been talking has many, many,|Итак, вы можете видеть, что с IPv6, о котором мы говорили, много, много,
many new features.|много новых функций.
The one we just talked about, which was autoconfiguration with the padding of the,|Тот, о котором мы только что говорили, это автоконфигурация с заполнением,
of the triple FE using the EUI dash 64.|тройного FE с помощью тире EUI 64.
I mean, that's great.|Я имею ввиду, это здорово.
We don't have to worry about the interface ID.|Нам не нужно беспокоиться об идентификаторе интерфейса.
Now with the new version of ICMP version six with the neighbor discovery,|Теперь с новой версией шестой версии ICMP с обнаружением соседей,
that is arb's no longer needed.|это вилка больше не нужна.
We're actually discovering our neighbors ourselves.|На самом деле мы сами открываем для себя наших соседей.
ICMP [UNKNOWN] IPv6 is the way to go.|ICMP [НЕИЗВЕСТНО] IPv6 - лучший вариант.
There's so many new features to include this one all right that you cannot want to go quick enough to IPv6 and start testing things out.|Есть так много новых функций, которые нужно включить в эту, так что вы не можете достаточно быстро перейти на IPv6 и начать тестирование.
So again, very short lesson.|Итак, снова очень короткий урок.
Very short lesson.|Очень короткий урок.
I'm not gonna get too much into the details because one thing I wanna end this lesson with is, a little advice, all right?|Я не собираюсь вдаваться в подробности, потому что хочу закончить урок небольшим советом, хорошо?
Don't go too insane when you're going through the books,|Не сходи с ума, когда просматриваешь книги,
those of you that are using the book that I recommended, that you studied for the CCNA 200-120, not everything in that book is gonna go to the examination and|те из вас, кто использует книгу, которую я рекомендовал, вы изучали CCNA 200-120, не все в этой книге пойдет на экзамен и
not into as that, that detail.|не вдаваться в подробности.
It's a very good book, it's geared to the certification but again,|Это очень хорошая книга, она предназначена для сертификации, но, опять же,
not everything is going towards it.|не все идет к этому.
You can read like one of, one of the things,|Вы можете читать как одну из вещей,
just to make an example, just to make an example, the, when you're doing,|просто чтобы подать пример, просто чтобы подать пример, когда вы делаете,
let's say that, that padding that we talked previously.|скажем так, то обивка, о которой мы говорили ранее.
That is, there's a UL bit in there.|То есть там есть бит UL.
Once that padding gets done, it's either going to be a two or a zero.|Как только это заполнение будет выполнено, оно будет либо двойкой, либо нулем.
Because of the seventh bit if it's on or off.|Из-за седьмого бита, если он включен или выключен.
You don't have to worry about that math.|Вам не нужно беспокоиться об этой математике.
That's not gonna be on your test.|Это не будет на твоем тесте.
All right.|Отлично.
What's gonna be on your test hey do you know what a valid I,|Что будет на твоем тесте, эй, ты знаешь, какой я действительный,
IPv6 address look like?|Как выглядит IPv6-адрес?
Do you know what auto-configuration is?|Вы знаете, что такое автоконфигурация?
Do you know, what the newest thing with ICMP version 6?|Знаете ли вы, что нового в ICMP версии 6?
What is, you know, ns?|Что, знаете, нс?
Neighbor solicitation.|Ходатайство соседа.
NA, Neighbor advertisements or RA or RS.|NA, реклама соседей или RA или RS.
All right it's, those are the things are gonna be on the test,|Хорошо, это те вещи, которые будут на тесте,
some basic foundations of it.|некоторые основные его основы.
So don't go too crazy especially in the IPv6 section.|Так что не сходите с ума, особенно в разделе IPv6.
They're not going to drill you that deep into it, but definitely know your stuff.|Они не собираются вдувать вас так глубоко, но определенно знают свое дело.
The more you know, the better it is for you.|Чем больше вы знаете, тем лучше для вас.
But remember you're, this is geared Towards a certification exam, and you need to keep focused on that certification exam.|Но помните, что это связано с сертификационным экзаменом, и вам нужно сосредоточиться на этом сертификационном экзамене.
Now, next we're going to get into the transition mechanisms.|Теперь мы перейдем к механизмам перехода.
Again, they're going to be very quick,|Опять же, они будут очень быстрыми,
quick videos explaining what each one does and how would you, you know, I'll probably do a lot for the dual stack to show you or|быстрые видеоролики, объясняющие, что каждый из них делает и как бы вы, знаете, я, вероятно, многое сделаю для двойного стека, чтобы показать вам или
there's already a lot done actually.|на самом деле уже многое сделано.
I did it for you already.|Я уже сделал это для тебя.
And show you how it's working and why would you use these transition mechanisms.|И покажу, как это работает и зачем вам использовать эти механизмы перехода.
All right.|Отлично.
So remember, make a comment.|Так что помните, сделайте комментарий.
What's different?|Что изменилось?
What's different?|Что изменилось?
And then I'll see you in the next section|А потом увидимся в следующем разделе