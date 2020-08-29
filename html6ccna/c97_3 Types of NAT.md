D:\mailCloud\prjother\tmp\1\c97_3 Types of NAT.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
Welcome back, everyone.|С возвращением, все.
Up to this point, we've been dealing pretty much with just internal addresses,|До этого момента мы в значительной степени имели дело только с внутренними адресами,
private addresses.|частные адреса.
Now, it comes time for us to travel onto the world of the internet.|Теперь пришло время отправиться в мир Интернета.
All right?|Отлично?
Or if you're gonna pretend to.|Или если ты собираешься притвориться.
And the way we do that, because as we know already that private IP addresses are not routable on a public interface.|И как мы это делаем, потому что, как мы уже знаем, частные IP-адреса не маршрутизируются на общедоступном интерфейсе.
Sounds like a test question to me.|Для меня это похоже на тестовый вопрос.
Private IP addresses are not routable on public interface.|Частные IP-адреса не маршрутизируются на общедоступном интерфейсе.
So we must something called Network Address Translation or NAT.|Итак, нам нужно нечто, называемое преобразованием сетевых адресов или NAT.
Really NAT just like VSLM is a mechanism to slow down the death of IPv4.|На самом деле NAT, как и VSLM, является механизмом, замедляющим смерть IPv4.
But of course, IPv4 already died.|Но, конечно, IPv4 уже умер.
That's why IPv6 is already taking over.|Вот почему IPv6 уже берет верх.
It's just been a very slow transition.|Просто это был очень медленный переход.
And when IPv6 does come around, NAT is going to,|И когда IPv6 действительно появится, NAT собирается,
when it's fully implemented in your network, NAT will disappear.|когда он будет полностью реализован в вашей сети, NAT исчезнет.
There will be no need for NAT.|NAT не понадобится.
Is your transition mechanism called NAT PT?|Ваш механизм перехода называется NAT PT?
Yes.|Да.
Is it recommended to be used?|Рекомендуется ли использовать?
No.|Нет.
Are you gonna be asked questions about it?|Вам будут задавать вопросы об этом?
Not at all.|Не за что.
They may ask you what are the three transition mechanisms.|Они могут спросить вас, каковы три механизма перехода.
That's one of them, NAT PT.|Это один из них, NAT PT.
All right.|Отлично.
But other than that, that's about it.|Но в остальном это все.
But you will get print screens on NAT itself.|Но вы получите экраны печати на самом NAT.
So there's three different types of NAT.|Итак, существует три разных типа NAT.
The first one, as you can see up here is static nat.|Первый, как вы можете видеть здесь, - это static nat.
And static nat means a one to one mapping.|А статический нат означает отображение один к одному.
That means if you have 1000 nodes that have to go out onto the public internet,|Это означает, что если у вас есть 1000 узлов, которые должны выйти в общедоступный Интернет,
you need to purchase 1000 IP addresses.|вам необходимо приобрести 1000 IP-адресов.
And then statically, send somebody down,|А затем статически отправить кого-нибудь вниз,
pay them,|плати им,
you know, 52 bucks an hour to go ahead and say,|вы знаете, 52 доллара в час, чтобы пойти дальше и сказать:
IP nat inside source static private,|IP nat внутри источника статический частный,
public.|общественность.
IP nat inside source static private,|IP nat внутри источника статический частный,
public.|общественность.
Okay?|Ладно?
That is completely,|Это полностью,
[SOUND] I will go insane doing something like that, even for 52, 52 bucks an hour.|[ЗВУК] Я сойду с ума, делая что-то подобное, даже за 52, 52 доллара в час.
I wouldn't I wouldn't want to do that.|Я бы не стал этого делать.
That is not feasable for a company to do that.|Для компании это невыполнимо.
You're, it's a 1000 IPs at five bucks that's $5,000.|Вы, это 1000 IP-адресов за пять баксов, это 5000 долларов.
Now, I can tell you this much.|Теперь я могу вам многое сказать.
One of my students, many years ago, he actually told, hey, Laz.|Один из моих учеников много лет назад сказал: «Эй, Лаз.
Where we work, which was a hospital, we use static nat for our printers,|Там, где мы работаем, в больнице, мы используем статический нат для наших принтеров,
because we use a third party to print our medical records.|потому что мы пользуемся услугами третьих лиц для печати наших медицинских карт.
So they have to be statically assigned.|Поэтому они должны быть статически назначены.
They have a lot of printers.|У них много принтеров.
I'm gonna say, thousands, but a couple hundred.|Я скажу тысячи, но пара сотен.
All right.|Отлично.
So, it's like okay.|Так что все в порядке.
I guess, maybe because of the HIPAA.|Думаю, может быть, из-за HIPAA.
They have to do it that way.|Они должны так делать.
But wow, that's the, that's the only person in the,|Но ничего себе, это единственный человек в
now, more than 14 years [LAUGH] that I've been doing this.|Теперь, более 14 лет [СМЕЕТ] я этим занимаюсь.
You know, that they've told me just that.|Вы знаете, что они мне сказали именно это.
That they use static nat, because of that.|Из-за этого они используют статический нат.
So, I guess it's a HIPAA thing.|Так что, думаю, это HIPAA.
But again, it's not feasable.|Но опять же, это невыполнимо.
It's not feasable for the company to purchase all those IP addresses and it's not feasable to have somebody sitting there, typing all those things.|Для компании невозможно приобрести все эти IP-адреса, и невозможно, чтобы кто-то сидел и набирал все эти вещи.
You know, one by one by one by one.|Вы знаете, один за другим.
Obviously, you can create a script for this, but still not feasable.|Очевидно, вы можете создать сценарий для этого, но это все равно не выполнимо.
Not feasible.|Неосуществимо.
The next one is dynamic nat.|Следующий - динамический нац.
Now dynamic nat, at least it eases the burden,|Теперь динамический нат, по крайней мере, облегчает бремя,
because you create a pool of a thousand addresses.|потому что вы создаете пул из тысячи адресов.
No longer are you doing one by one by one manually.|Вы больше не занимаетесь по одному вручную.
It's still a one to one mapping, because you still, if you have thousand people need to get out, you still need to purchase thousand IPs.|Это по-прежнему сопоставление один к одному, потому что вам все равно, если у вас есть тысяча человек, вам все равно нужно купить тысячу IP-адресов.
So you're still wasting 5 Gs, that's a lot of money.|Так что вы все еще тратите 5G, это большие деньги.
All right.|Отлично.
Just all so people can go out to the internet.|Просто все, чтобы люди могли выходить в интернет.
If you have a thousand people in your company.|Если в вашей компании тысяча человек.
Obviously, there must be an important reason why they are going out to the internet.|Очевидно, должна быть важная причина, по которой они выходят в Интернет.
But still, that's $5,000.|Но все же это 5000 долларов.
Now still not feasable, but at least you create a pool.|Сейчас все еще неосуществимо, но вы хотя бы создаете пул.
Cut your workload in half, right?|Сократите рабочую нагрузку вдвое, верно?
A lot easier to do.|Намного проще сделать.
The last one is nat overload.|Последний - нац перегрузка.
That's the most popular one.|Это самый популярный.
Nat overload.|Нат перегрузка.
That's the one that everybody uses when you purchase your Linksys routers or D-link routers or whatever manufacturer you use.|Это тот, который все используют, когда вы покупаете маршрутизаторы Linksys, маршрутизаторы D-link или любого другого производителя, которого вы используете.
Okay?|Ладно?
Everybody uses nat overload or as, or as it is also called port address translation, PAT.|Все используют перегрузку nat или как, или как это еще называют, преобразование адресов порта, PAT.
Because what it does, you have one public IP address that can hold up to 65,000 plus private addresses.|Потому что у вас есть один общедоступный IP-адрес, который может содержать до 65 000 плюс частные адреса.
So just with one public address.|Так что только с одним публичным адресом.
That's pretty feasible to me, right?|Для меня это вполне возможно, правда?
If I have 65,000 people in my company, I would be doing very well.|Если бы в моей компании было 65 000 человек, у меня все было бы хорошо.
Okay?|Ладно?
And so this is the most feasable one.|Так что это самый реальный вариант.
What you are gonna get tested on, they may ask, may, rare.|Они могут спросить, на что вы собираетесь пройти тестирование, может, редко.
They'll ask you the three different types of NAT, just know that it's static,|Они спросят вас о трех разных типах NAT, просто знайте, что он статический,
dynamic and and nat overload.|динамическая и перегрузка нац.
But again, all these three things, all that they do is just that.|Но опять же, все эти три вещи, все, что они делают, - это просто так.
Is just translate from private to public.|Это просто перевод с частного на публичный.
And again, doing it statically, not very feasable.|И опять же, делать это статически не очень-то реально.
Doing it dynamically, okay.|Делаем это динамически, хорошо.
But again, you're creating a pool,|Но опять же, вы создаете пул,
you're creating a pool of a thousand IP addresses.|вы создаете пул из тысячи IP-адресов.
It's matching up with that particular, as a computer goes through there,|Это совпадает с этим, поскольку компьютер проходит через это,
it will take out the private, put in the public, so forth.|он уберет частное, станет публичным и так далее.
And then you have nat overload, a ll right?|А то у вас нат перегрузка, все так?
Which it changes the port.|Который меняет порт.
It changes the source port number for it to go across.|Он изменяет номер порта источника, чтобы он проходил.
So definitely, still today, we still need NAT.|Так что определенно, и сегодня нам все еще нужен NAT.
We, we kinda hide behind NAT like a firewall, actually.|Мы как бы прячемся за NAT, как брандмауэр.
But we still need NAT, because we do have private IP addresses internally.|Но нам все еще нужен NAT, потому что у нас есть внутренние IP-адреса.
And for us to get outside, we need some method to get a public IP address and this where NAT comes in.|А чтобы выйти наружу, нам нужен какой-то метод получения общедоступного IP-адреса, и здесь нам пригодится NAT.
All your devices, all your devices that you purchase any, you know,|Все ваши устройства, все ваши устройства, которые вы покупаете,
any your provider Comca, you know,|любой ваш провайдер Comca, вы знаете,
whatever provider you use, where in your location, your gonna go ahead on their devices and do the same thing.|Какой бы провайдер вы ни использовали, где бы вы ни находились, вы будете использовать их устройства и делать то же самое.
You don't need anymore really to purchase these wireless routers,|Вам больше не нужно покупать эти беспроводные маршрутизаторы,
because your providers have wireless routers that do give you a private IP address with public access.|потому что у ваших провайдеров есть беспроводные маршрутизаторы, которые предоставляют вам частный IP-адрес с общедоступным доступом.
They do their internal NAT themselves.|Они сами делают свой внутренний NAT.
So still today is very prevalent.|Так что все еще очень распространено сегодня.
But again, the most prevalent of all, the most popular of all.|Но опять же, самый распространенный, самый популярный из всех.
It is nat overload, nat overload.|Это нац перегрузка, нац перегрузка.
And we will be discussing exactly how NAT works and the configurations for dynamic and nat over, and nat overload.|И мы будем обсуждать, как именно работает NAT, и конфигурации для динамической, натурной и естественной перегрузки.
And then we'll get into the pitfalls and things like that when you get to certification.|А потом мы столкнемся с подводными камнями и тому подобным, когда вы доберетесь до сертификации.
What to look for, just to make sure you know, you know,|Что искать, просто чтобы убедиться, что вы знаете,
what to point out to make sure you don't get caught in a trap.|на что обратить внимание, чтобы не попасться в ловушку.
All right?|Отлично?
So, I will see you in the next lesson and we'll explain exactly how NAT works.|Итак, увидимся на следующем уроке, и мы объясним, как именно работает NAT.
[BLANK_AUDIO]|[BLANK_AUDIO]