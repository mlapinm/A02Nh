D:\mailCloud\prjother\tmp\1\c35_Definition of Private addressing.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
All right.|Отлично.
Welcome back, everyone.|С возвращением, все.
It is time for private IP addressing.|Пришло время частной IP-адресации.
But before we start, as you notice, my shirt.|Но прежде чем мы начнем, как вы заметили, моя рубашка.
We have rock, paper scissors, lizard,|У нас есть камень, ножницы для бумаги, ящерица,
spock, right?|спок, да?
That's the new version, the original version of rock paper scissors.|Это новая версия, оригинальная версия "камень-ножницы-бумага".
Do you know where it started from?|Вы знаете, откуда это началось?
Where it originated from?|Откуда это взялось?
The birth of rock, paper, scissors rock,|Рождение камня, бумаги, ножницы, камня,
rock,|рок,
paper, scissors sorry now the origination of that I'm not going to tell you now I'm going to keep you in suspense, I'm gonna tell you after the lecture.|бумага, ножницы, извините, что возникло, я не собираюсь вам сейчас рассказывать, я буду держать вас в напряжении, я расскажу вам после лекции.
And I'm gonna tell you the importance of it.|И я скажу вам, насколько это важно.
What people actually used to do with rock,|Что люди на самом деле делали с роком,
paper, scissors, whatever.|бумага, ножницы, что угодно.
All right.|Отлично.
So just so you know.|Просто чтобы вы знали.
Anyway, private IP addressing.|Во всяком случае, частный IP-адрес.
What does it mean to be private?|Что значит быть приватным?
It means that, these addresses are not routable on the internet,|Это означает, что эти адреса не маршрутизируются в Интернете,
or the public interface.|или публичный интерфейс.
When you take the CCNA exam, you're more than likely gonna be asked, very few questions, but you'll be asked questions nonetheless, something geared towards hey,|Когда вы сдаетесь на экзамен CCNA, вам, скорее всего, зададут очень мало вопросов, но тем не менее вам будут задавать вопросы, относящиеся к эй,
what would happen if you put a private IP address on a public interface?|что произойдет, если вы поместите частный IP-адрес в общедоступный интерфейс?
Something to that effect.|Что-то в этом роде.
Obviously, you're, they're not routable.|Очевидно, что они не маршрутизируемые.
They're not routable on the internet.|Они не маршрутизируются в Интернете.
So how in the world then, do we get outside?|Так как же тогда нам выбраться наружу?
Cuz everybody internally has a private IP address.|Потому что у всех внутри есть частный IP-адрес.
At home, you have a private IP address.|Дома у вас есть частный IP-адрес.
In business, you have a private IP address.|В бизнесе у вас есть частный IP-адрес.
So, how is it that we're able to get out to the internet?|Итак, как же мы можем выйти в Интернет?
And the quick, you know, answer to that is obviously, NAT.|И самый быстрый ответ на это, очевидно, - NAT.
All right.|Отлично.
The NAT overload, PAT.|Перегрузка NAT, PAT.
Whatever you want to call it.|Как бы вы это ни называли.
That's what everybody uses.|Это то, что все используют.
That's why it translates that private IP address to a public IP address and you're able to get out on the internet.|Вот почему он переводит этот частный IP-адрес в общедоступный IP-адрес, и вы можете выйти в Интернет.
But just to even elaborate further on that and I know some of you are saying,|Но просто чтобы уточнить это, и я знаю, что некоторые из вас говорят:
how can he elaborate further on that,|как он может подробнее рассказать об этом,
Jesus.|Иисус.
It's really not that the, the, they're,|Это действительно не то, что они,
yes, they're not routable.|да, они не маршрутизируемые.
They're not routable because they're being blocked.|Их нельзя маршрутизировать, потому что они заблокированы.
There's not something special,|Нет ничего особенного,
at least not that I'm aware of, there's nothing special in the header.|по крайней мере не то что в курсе, в шапке ничего особенного.
All these private IP addresses that say,|Все эти частные IP-адреса, которые говорят:
haha.|ха-ха.
Can't, you can't be on the internet,|Не могу, ты не можешь быть в Интернете,
sorry.|Прости.
Right?|Правильно?
And, then, they're just,|И тогда они просто,
they just don't work.|они просто не работают.
No, they're being blocked.|Нет, они заблокированы.
That's one of the, one of the things that you wanna do.|Это одна из тех вещей, которые вы хотите делать.
You wanna block private IP addresses from coming internally into your network anyway, through use of access list.|Вы в любом случае хотите заблокировать частные IP-адреса от внутреннего входа в вашу сеть с помощью списка доступа.
So this is the reason why you can't have a private IP address on a public interface, you have to have a public IP address on the internet.|Вот почему у вас не может быть частного IP-адреса в общедоступном интерфейсе, у вас должен быть общедоступный IP-адрес в Интернете.
But that's all gonna change isn't it, once we get to IPv6|Но это все изменится, не так ли, как только мы перейдем к IPv6
where NAT will no longer be needed because we will all, we publicly assigned IP addresses.|где NAT больше не будет нужен, потому что мы все будем публично назначать IP-адреса.
We no longer need that, its all going to work just fine.|Нам это больше не нужно, все будет работать нормально.
So, just to give you a final definition of that, was,|Итак, чтобы дать вам окончательное определение этого, было,
is that these IP addresses, within their private ranges, which we're gonna explain in the next lecture, each and everyone or A, B and C, really.|заключается в том, что эти IP-адреса в пределах их частных диапазонов, которые мы собираемся объяснить в следующей лекции, на самом деле, каждый или A, B и C.
Th, They're just not routable.|Чх, они просто не маршрутизируемы.
That's what you need to say.|Вот что вам нужно сказать.
They're just not routable on the internet,|Они просто не маршрутизируются в Интернете,
you need something like a MAC server in order to get out.|вам нужно что-то вроде MAC-сервера, чтобы выйти.
Now, before we end the lecture.|А теперь, прежде чем мы закончим лекцию.
Before we end it.|Прежде, чем мы закончим.
I said I was gonna give you the answer to this.|Я сказал, что дам тебе ответ на это.
Rock, paper, scissors, actually originated in China.|Камень, ножницы, бумага, на самом деле возникли в Китае.
Long time ago and then it went to England and then in England it was used as actually laws where nobody was allowed to use,|Давным-давно, а затем он попал в Англию, а затем в Англии он фактически использовался как закон, где никому не разрешалось использовать,
to play rock-paper-scissors because business deals were made this way.|играть камень-ножницы-бумага, потому что так заключались коммерческие сделки.
Even here in Florida parts of Florida,|Даже здесь, во Флориде, в частях Флориды,
judgements were made,|были вынесены приговоры,
court cases were decided where they're gonna be based on rock, paper, scissors.|Судебные дела были решены, где они будут основываться на камне, ножницах, бумаге.
Art deals, major art galleries, million dollar art galleries were actually, said okay,|Художественные сделки, крупные художественные галереи, художественные галереи за миллион долларов были на самом деле, сказал хорошо,
well, whoever wins the rock-paper-scissors gets this particular collection.|Что ж, тот, кто выиграет «камень-ножницы-бумага», получит именно эту коллекцию.
And every year just to end it every year in California there is a,|И каждый год, чтобы закончить это каждый год в Калифорнии,
I think it's in California, a rock-paper-scissor competition where they have actual referees and everything that the winner of rock paper|Я думаю, что это в Калифорнии, соревнование камень-ножницы-бумага, где есть настоящие рефери и все, что победитель конкурса рок-бумага
scissors very serious gets a $50,000|ножницы очень серьезные получают 50 000 долларов
reward, how about that one?|награда, как насчет того?
So, we'll end with that.|Итак, на этом мы закончим.
So I hope you enjoyed the lecture.|Надеюсь, вам понравилась лекция.
Now you know about private IP addresses and rock, paper, scissors.|Теперь вы знаете о частных IP-адресах и о камнях, ножницах, бумаге.
But do you know where rock, paper,|Но знаете ли вы, где камень, бумага,
scissors, lizards, spock came from?|ножницы, ящерицы, спок?
That'll be the next one.|Это будет следующий.
[BLANK_AUDIO]|[BLANK_AUDIO]