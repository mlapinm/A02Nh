D:\mailCloud\prjother\tmp\1\c49_Do we need to subnet In IPv6.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
Welcome back, everyone.|С возвращением, все.
I hope you're ready.|Надеюсь, ты готов.
Subnetting in IPv6.|Подсети в IPv6.
Do we really need to subnet in IPv6?|Нам действительно нужно подсеть в IPv6?
Let me give you the short answer.|Позвольте дать вам краткий ответ.
Yes, we do.|Да.
As you've seen in previous lectures, when we broke down the IPv6 address.|Как вы видели на предыдущих лекциях, когда мы разобрали IPv6-адрес.
That we have the last section, right here,|Что у нас есть последний раздел, прямо здесь,
where you see that number 12.|где вы видите число 12.
I see that you have 12, 1100, or 1200,|Я вижу, что у вас 12, 1100 или 1200,
1100 and 1000.|1100 и 1000.
That is the subnet portion of the address.|Это часть адреса, содержащая подсеть.
That is the address that they've given us,|Это адрес, который они нам дали,
or the section that they've given us to allow us to subnet IPv6.|или раздел, который они предоставили нам, чтобы позволить нам подсеть IPv6.
Of course, we need to subnet.|Конечно, нам нужно подсеть.
Just because we have quintillion or 340|Просто потому, что у нас квинтиллион или 340
undecillion, billion,|ундециллион, миллиард,
trillion, zillion, gillion addresses.|триллион, миллиард, миллиард адресов.
We still need to subnet.|Нам все еще нужно подсеть.
We still need to have separate networks.|Нам по-прежнему нужны отдельные сети.
We still are running with ethernets and the contention based media access method that it runs in.|Мы все еще используем Ethernet и метод доступа к среде на основе конкуренции, в котором он работает.
So, we definitely need to have separate networks.|Итак, нам обязательно нужны отдельные сети.
Now, can you really make, you know, make up any number?|Вы действительно можете, знаете ли, составить любое число?
You probably could.|Вы, наверное, могли бы.
Yeah, so many numbers, you can probably do whatever you want.|Да, столько цифр, что ты, наверное, можешь делать все, что хочешь.
Okay, because that section is just for you.|Хорошо, потому что этот раздел только для вас.
Just like in the interface ID portion of the address.|Точно так же, как в части адреса, содержащей идентификатор интерфейса.
If you have a small network and you just go one, two, three, four, five, six,|Если у вас небольшая сеть, и вы просто идете один, два, три, четыре, пять, шесть,
seven, eight, nine, eight, four addresses for your router, of course.|Конечно, семь, восемь, девять, восемь, четыре адреса для вашего роутера.
Of course, but as you grow, if you're a world wide company.|Конечно, но по мере роста, если вы всемирная компания.
You're a company across an entire state,|Вы - компания во всем штате,
if you have plenty of routers, then you want to organize it because remember, our routing tables, our routing tables.|если у вас много маршрутизаторов, вы хотите организовать это, потому что помните, наши таблицы маршрутизации, наши таблицы маршрутизации.
Because now with IPv6, no longer do we have a mask.|Потому что теперь с IPv6 у нас больше нет маски.
It's called a network prefix.|Это называется сетевой префикс.
It's based on routing and routing only.|Он основан только на маршрутизации и маршрутизации.
We want to create that hierarchy of addresses and we are with you know the global unique address given by error.|Мы хотим создать эту иерархию адресов, и мы с вами знаем глобальный уникальный адрес, полученный по ошибке.
And then, we have the our ISP assigning us a particular address.|И затем наш интернет-провайдер назначает нам конкретный адрес.
Then we have our company, and then we have that subnet section.|Затем у нас есть наша компания, а затем у нас есть раздел подсети.
So, definitely within your company, you still want a subnet.|Итак, определенно внутри вашей компании вам по-прежнему нужна подсеть.
That has not changed.|Это не изменилось.
Now, the method of subnetting, which we will discuss,|Теперь о методе разделения на подсети, который мы обсудим,
it will end up in the next lecture.|это закончится на следующей лекции.
I have taken that IPv4 subnetting,|Я взял это подсети IPv4,
and, used it in IPv6.|и использовал его в IPv6.
All right?|Отлично?
So, it will work.|Итак, это будет работать.
But yes, you must definitely subnet.|Но да, вы обязательно должны подсеть.
You still wanna break up those broadcast domains, if you will, segmented and networking, even though with IPv6, one of the latest features is what?|Вы по-прежнему хотите разбить эти широковещательные домены, если хотите, сегментированные и сетевые, хотя с IPv6 одна из последних функций - это что?
No broadcast anymore.|Трансляции больше нет.
You still wanna go ahead and break things up.|Ты все еще хочешь пойти дальше и разбить вещи.
Yes, we have neighbor discovery with ICMP version six.|Да, у нас есть обнаружение соседей с помощью шестой версии ICMP.
So, there is no ARP going on back and forth.|Таким образом, ARP не идет туда-сюда.
Yes, we have no broadcast.|Да, у нас нет трансляции.
We have new IP addresses that weren't to near us.|У нас есть новые IP-адреса, которых не было поблизости.
We have all these brand new features.|У нас есть все эти новые функции.
The protocol is working a lot faster.|Протокол работает намного быстрее.
Its more streamline now, but we still wanna separate our segments, so we know which networks are which.|Сейчас это более упорядочено, но мы все еще хотим разделить наши сегменты, чтобы знать, какие сети есть.
So, subnetting is here to stay, there is no getting around it.|Таким образом, подсети никуда не денутся.
We still need to study IPv6.|Нам еще нужно изучить IPv6.
So in the next lecture, we're going to begin to show you how to subnet.|Итак, в следующей лекции мы собираемся показать вам, как создавать подсети.
See you then.|Увидимся тогда.
[BLANK_AUDIO]|[BLANK_AUDIO]