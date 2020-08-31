D:\mailCloud\prjother\tmp\1\c98_How does NAT work.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
All right, so now how does NAT exactly works?|Хорошо, а как теперь работает NAT?
As you can see here, I put, really this is the terminology you need to be aware of.|Как вы можете видеть, я сказал, что вам действительно нужно знать эту терминологию.
Anything that says local,|Все, что говорит местное,
[BLANK_AUDIO]|[BLANK_AUDIO]
Is before NAT translation, before NAT translation.|Есть до трансляции NAT, до трансляции NAT.
So this inside local is your internal IP address of your PC.|Итак, внутри local - это ваш внутренний IP-адрес вашего ПК.
That 192.168 or 10 dot whatever or 172|Это 192,168 или 10 точек, или 172
whatever,|без разницы,
that is your inside source address.|это ваш внутренний исходный адрес.
When it goes through the net router, it becomes the inside global address,|Когда он проходит через сетевой маршрутизатор, он становится внутренним глобальным адресом,
which means that source IP address that you have just pulled out and get's replaced by the public IP address that your provider gives to you.|Это означает, что исходный IP-адрес, который вы только что вытащили и заменили публичным IP-адресом, который вам дает ваш провайдер.
Because normally, let's say you purchase a T1, just to say a, a, a connection type you get five IPs, one's for the router,|Потому что обычно, скажем, вы покупаете T1, просто говоря a, a, тип подключения вы получаете пять IP-адресов, один для маршрутизатора,
the other four you can do what you want.|остальные четыре вы можете делать, что хотите.
Usually the other one, the other two you know, the other, the second one, or the other two, I use for firewalls.|Обычно другой, два других, вы знаете, другой, второй или два других, я использую для межсетевых экранов.
Then, you got two left to do whatever you want to do with, okay?|Значит, у вас осталось двое, чтобы делать все, что вы хотите, хорошо?
But again, inside global, that is your translated through NAT private IP address,|Но опять же, внутри global, это ваш преобразованный через NAT частный IP-адрес,
all right?|отлично?
That's, now just became public.|Вот только что стало достоянием общественности.
Your outside local and your outside global never change.|Ваше внешнее локальное и ваше внешнее глобальное никогда не меняются.
They're the destination.|Они цель.
This is where you're going.|Вот куда вы идете.
Yahoo!, Google, whatever, YouTube,|Yahoo !, Google, что угодно, YouTube,
wherever it is that you're gonna go, the,|куда бы вы ни пошли,
these IP addresses remain the same before the translation and after the translation.|эти IP-адреса остаются неизменными до трансляции и после трансляции.
All right, they have their own destination ports, everything.|Хорошо, у них есть свои порты назначения, все.
So the destination port is the destination port, period.|Таким образом, порт назначения - это порт назначения, точка.
Whether you're FTPing, you're Telneting,|Если вы используете FTP или Telnet,
you're just looking for a webpage, HTTP, de, destination port is always the same.|вы просто ищете веб-страницу, HTTP, de, порт назначения всегда один и тот же.
And so is the public IP address whether it's before or after the translation.|То же самое и с публичным IP-адресом, до или после перевода.
So those two do not change.|Так что эти двое не меняются.
What do change, what does change, I'm sorry, is the inside local and the, gets changed to the inside global.|Что изменится, что изменится, извините, это внутреннее локальное, а внутреннее глобальное.
So that is what you're gonna need ot look at.|Так что это то, на что вам нужно не смотреть.
That's what NAT does, it translates the private to public or vice versa, public to private.|Это то, что делает NAT: он переводит частное в общедоступное или наоборот, общедоступное в частное.
If you're using NAT overload is when it starts changing the source port number,|Если вы используете перегрузку NAT, это когда он начинает изменять номер исходного порта,
cuz you only got one public IP address.|Потому что у вас есть только один публичный IP-адрес.
So how does it, you know, because, if you have dynamic, using dynamic NAT,|Итак, как это происходит, потому что, если у вас есть динамический, с использованием динамического NAT,
then you have an IP address to match with that private, private, public, private,|тогда у вас есть IP-адрес, который будет соответствовать этому частному, частному, общедоступному, частному,
public, private, public.|публичные, частные, публичные.
But with NAT overload or PAT, that's why it's called port address translation, you only have one IP address.|Но с перегрузкой NAT или PAT, поэтому это называется трансляцией адресов порта, у вас есть только один IP-адрес.
So, what it does,|Итак, что он делает,
it changes the port number to identify that particular IP address.|он изменяет номер порта, чтобы идентифицировать этот конкретный IP-адрес.
So, that exactly, that's pretty much,|Так вот, это в значительной степени,
really, what you need to be concerned with.|действительно то, о чем вам нужно беспокоиться.
They did in the past, in the old test I know they asked about this, at what point is your inside local or inside global or|Они делали это в прошлом, в старом тесте, я знаю, они спрашивали об этом, в какой момент ваш внутренний локальный или внутренний глобальный или
outside local and outside global?|вне локального и вне глобального?
And I still believe there are similar questions in the test now about that.|И я до сих пор верю, что в тесте есть похожие вопросы по этому поводу.
So all you need to remember: anything that's local is before the translation.|Итак, все, что вам нужно запомнить: все, что является локальным, находится до перевода.
Anything after the NAT router is global,|Все, что после маршрутизатора NAT является глобальным,
all right?|отлично?
So, let, let's take a look at this lab real quick, just to show you.|Итак, позвольте, давайте быстро взглянем на эту лабораторию, просто чтобы показать вам.
So, there's your NAT router.|Итак, вот и ваш NAT-маршрутизатор.
So, anything over here you see, this is private.|Итак, все, что вы видите здесь, это личное.
Let me zoom in so you can see it better.|Позвольте мне увеличить масштаб, чтобы вам было лучше видно.
[BLANK_AUDIO]|[BLANK_AUDIO]
Okay?|Ладно?
So this is your NAT router right here, so this is your private scheme right here,|Итак, это ваш NAT-маршрутизатор прямо здесь, так что это ваша частная схема прямо здесь,
192.268.1.0,|192.268.1.0,
this is private, so this is your local,|это личное, так что это ваш местный,
inside local,|внутри местного,
this is your public over here, so this is your inside global, all right?|это ваша публика, так что это ваш внутренний мир, хорошо?
Outside local, outside global,|За пределами местного, за пределами глобального,
inside local, inside global.|внутри локальный, внутри глобальный.
And remember, only the inside local gets translated to the inside global.|И помните, только внутренний локальный переводится во внутренний глобальный.
Those two are the source addresses where the outside is your destination addresses.|Эти два адреса являются исходными, а внешний - адресами назначения.
So if you understand that, you're not gonna have any issues with nat.|Так что, если вы это понимаете, у вас не будет проблем с nat.
Now, what we're gonna do though, we're obviously gonna configure NAT, but we're gonna configure NAT overload.|Теперь, что мы собираемся сделать, мы, очевидно, настроим NAT, но мы собираемся настроить перегрузку NAT.
That's the one we're gonna configure.|Это тот, который мы собираемся настроить.
We're gonna configure NAT overload, and then I will show you.|Мы собираемся настроить перегрузку NAT, а потом я вам покажу.
And we'll do everything in Notepad first so I can show you the differences between dynamic NAT and NAT overload.|И сначала мы сделаем все в Блокноте, чтобы я мог показать вам разницу между динамическим NAT и перегрузкой NAT.
But we will be configuring NAT overload.|Но мы будем настраивать перегрузку NAT.
And since we have no real active IPs, the IPs that we'll use will be the public IP, quote unquote,|И поскольку у нас нет реальных активных IP-адресов, IP-адреса, которые мы будем использовать, будут общедоступными IP-адресами, цитата без кавычек,
to .111.|до .111.
We'll be using, we'll just use RIP.|Мы будем использовать, мы просто будем использовать RIP.
Well we don't think we need to use, you know, a routing protocol,|Ну, мы не думаем, что нам нужно использовать протокол маршрутизации,
we're connected to the same router.|мы подключены к одному роутеру.
So we don't need to use a routing protocol.|Поэтому нам не нужно использовать протокол маршрутизации.
But we'll use the IP address on the public's side whatever we assign here.|Но мы будем использовать публичный IP-адрес независимо от того, что мы здесь назначаем.
That will be the actual IP address that we're gonna use for the pool of address that we're gonna create with NAT overload, okay?|Это будет фактический IP-адрес, который мы собираемся использовать для пула адресов, который мы собираемся создать с перегрузкой NAT, хорошо?
But that's essentially how NAT works.|Но вот как работает NAT.
It's just translating from private to public.|Он просто переводится с частного на публичный.
The terminology, the terminology is what you need to understand from inside local,|Терминология, терминология - это то, что вам нужно понять изнутри,
to inside global, outside local, to outside global.|к внутреннему глобальному, внешнему локальному, внешнему глобальному.
That's it.|Вот и все.
Pretty straightforward, pretty simple.|Довольно просто, довольно просто.
And once you get to the configurations in the next lesson,|И как только вы перейдете к настройкам на следующем уроке,
you'll start getting a better handle on it.|вы начнете лучше справляться с этим.
So I'll see you there.|Так что увидимся там.
[BLANK_AUDIO]|[BLANK_AUDIO]