D:\mailCloud\prjother\tmp\1\c40_The Auto-configuration feature.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
Well, I'm back.|Хорошо, я вернулся.
We're gonna discuss now one of the new features, which is auto configuration.|Сейчас мы собираемся обсудить одну из новых функций, а именно автоматическую настройку.
What is that?|Что это такое?
Now in this lab that I've shown you previously,|Теперь в этой лаборатории, которую я показывал вам ранее,
I've been using it throughout the IPv6|Я использовал его во всем IPv6
section of the course.|раздел курса.
This is the lab, and I told you that I usually use everything statically.|Это лаборатория, и я сказал вам, что обычно использую все статически.
I even assigned, the IP addresses on each interface statically.|Я даже назначил IP-адреса для каждого интерфейса статически.
But I went ahead and I added a computer just to show you on another interface, completely different network altogether, just to show you how|Но я пошел дальше и добавил компьютер, чтобы показать вам другой интерфейс, совершенно другую сеть, просто чтобы показать вам, как
the outer configuration feature does work.|функция внешней конфигурации действительно работает.
Now what I went ahead and did, I went inside this PC,|Теперь то, что я сделал, я вошел в этот компьютер,
and I'll bring it over here.|и я принесу это сюда.
I went into the IP configuration and I used the 2001 48 FACE 1000::1.|Я вошел в конфигурацию IP и использовал 2001 48 FACE 1000 :: 1.
Using on static 56.|Использование на статике 56.
And then the gateway is 2001 4800 FACE,|И тогда шлюз 2001 4800 FACE,
1000::f.|1000 :: ф.
So, that's fine.|Так что все в порядке.
I, I assigned it there statically.|Я там статически назначил.
But what I'm gonna do is, I'm actually gonna, in this router under that particular interface, I'm gonna go ahead and assign, do the auto configuration.|Но что я собираюсь сделать, я на самом деле собираюсь, в этом маршрутизаторе под этим конкретным интерфейсом, я собираюсь назначить, выполнить автоматическую настройку.
That way you can see how it assigns the,|Таким образом, вы можете увидеть, как он назначает,
end of that particular address.|конец этого конкретного адреса.
So, now really I shouldn't have set it statically, I should have said.|Так что теперь мне действительно не следовало устанавливать его статически, я должен был сказать.
[BLANK_AUDIO]|[BLANK_AUDIO]
Auto config.|Автоконфигурация.
Right?|Правильно?
And let's see what happens.|И посмотрим, что получится.
All right, let's go ahead and, cuz there's a command, you can do like an IP config,|Хорошо, давайте продолжим и, потому что есть команда, вы можете сделать как конфигурацию IP,
IPv6 config, release, renew type of thing.|Конфигурация IPv6, выпуск, обновление типа вещей.
So, it's there, but our concern is not in the PC, it's in the actual router.|Итак, он есть, но нас беспокоит не ПК, а сам маршрутизатор.
All right, if you're going to route,|Хорошо, если собираешься по маршруту,
and again this is giving you a heads up into your routing portion of the course.|и снова это дает вам возможность начать маршрутную часть курса.
And this already has it, and I'll show you.|А в этом уже есть, и я вам покажу.
I'm sure you can see that there.|Я уверен, вы это видите.
Show start, not starat, show start.|Показывать старт, а не старать, показывать старт.
You must type ipv6 unicast-routing.|Вы должны ввести ipv6 unicast-routing.
That's one command that you must type if you do any kind of routing on your routers, whether it be static or dynamic.|Это одна из команд, которую вы должны ввести, если вы выполняете любую маршрутизацию на своих маршрутизаторах, будь то статическая или динамическая.
You must type that.|Вы должны это ввести.
So what I want to do, I'm gonna do Ctrl+C.|Итак, что я хочу сделать, я сделаю Ctrl + C.
I'm gonna go to config T, global configuration.|Я собираюсь перейти к конфигурации T, глобальной конфигурации.
Now, just to let you know, when you go take your test,|Теперь, просто чтобы вы знали, когда вы пойдете на тест,
once you're inside the router, there's always questions.|как только вы окажетесь внутри маршрутизатора, всегда возникают вопросы.
Hey Laz, can we type config T, can we use,|Эй, Лаз, мы можем ввести config T, можем ли мы использовать,
you know, conf T, can we use int?|вы знаете, conf T, мы можем использовать int?
Cuz I do a lot of abbreviations.|Потому что я делаю много сокращений.
Some things you can, like config T I think is permissible.|Некоторые вещи, которые вы можете, например config T, я считаю допустимыми.
You can do config T, I don't think they want you to type on configure terminal.|Вы можете выполнить config T, я не думаю, что они хотят, чтобы вы вводили его на терминале настройки.
I really don't.|Я действительно не знаю.
If you can't type config T then type out configure terminal.|Если вы не можете ввести config T, введите configure terminal.
But I think that should be okay.|Но я думаю, что все в порядке.
Int?|Инт?
Mm, they may want to see interface then F-0-0.|Мм, они могут захотеть увидеть интерфейс тогда F-0-0.
But int F 0 0 should be okay.|Но int F 0 0 должно быть в порядке.
Definitely can do WR, which is write.|Определенно умею делать WR, то есть писать.
You can do copy.|Вы можете сделать копию.
You have to, you have to go back to privileged mode and do a copy, run, start.|Вы должны, вы должны вернуться в привилегированный режим и сделать копию, запустить, запустить.
You cannot stay within an interface or a line configuration interface and do, DO ping, DO whatever.|Вы не можете оставаться в интерфейсе или интерфейсе конфигурации линии и делать, делать ping, делать что угодно.
They don't allow the do command.|Они не разрешают команду do.
And, but for some reason, there was a student not too long ago who told me that he was able to tab and use question marks.|И, по какой-то причине, не так давно был студент, который сказал мне, что он может использовать табуляцию и использовать вопросительные знаки.
That's kind of funny.|Забавно.
But either way, you see what you can and can't do.|Но в любом случае вы видите, что можно, а что нельзя.
If you learn the complete command, that's perfect.|Если вы выучите всю команду, это прекрасно.
That's great well, for the exam.|Отлично для экзамена.
Once you get to the real world, you want to be quick.|Как только вы попадете в реальный мир, вам захочется действовать быстро.
[SOUND] You learn how to abbreviate real quickly.|[ЗВУК] Вы очень быстро научитесь сокращать.
All right, so what am I doing?|Хорошо, так что я делаю?
Oh yes, I'm going to the interface.|Ах да, пойду в интерфейс.
I'm going to do a do, which you can't do on the test.|Я собираюсь сделать то, чего ты не сможешь сделать на тесте.
Show IP int brief, or IP, yeah, IP int brief.|Показать краткий IP-адрес или краткий IP-адрес.
All right, these are my IP addresses or my interfaces.|Хорошо, это мои IP-адреса или мои интерфейсы.
That's what I want to see.|Вот что я хочу увидеть.
So I'm going to the F0/1 interface.|Итак, я перехожу к интерфейсу F0 / 1.
That's where I attach that PC to.|Вот куда я подключаю этот компьютер.
So I'm going to go int f0/1.|Итак, я собираюсь пойти int f0 / 1.
Enter.|Войти.
And in order to put in IPv6 address, I'm going to go IPv6,|И чтобы ввести адрес IPv6, я собираюсь использовать IPv6,
address and let me expand it since this is a long address.|адрес и позвольте мне расширить его, так как это длинный адрес.
All right, it's gonna be 2001, global,|Хорошо, это будет 2001 год, глобальный,
right?|право?
4800 is my provider.|4800 - мой провайдер.
I am part of Facebook, ha ha ha.|Я участник Facebook, ха-ха-ха.
Well now, I just pick 1000 here for my subnet, ::F.|Итак, я просто выбираю 1000 здесь для моей подсети, :: F.
Well now it doesn't do anything.|Что ж, теперь он ничего не делает.
Colon, colon.|Толстая кишка, толстая кишка.
We might as well put F, why not?|С таким же успехом можно поставить F, почему бы и нет?
Put F and then put, put the rest of the address.|Поставьте F, а затем поставьте, оставьте адрес.
Let's put a CIDR 56 and then we're gonna do EUI-,|Давайте поставим CIDR 56, а затем сделаем EUI-,
oops, 64.|ой, 64.
Okay?|Ладно?
Now we've done that.|Теперь мы это сделали.
EUI-64 is what auto-configuration does.|EUI-64 - это то, что делает автоконфигурация.
What it does is, it's now gonna get the MAC address of this particular interface and it's going to put it as a portion of|Что он делает: теперь он получает MAC-адрес этого конкретного интерфейса и помещает его как часть
the IP address of the,|IP-адрес,
the actual IPv6 address.|фактический адрес IPv6.
But your MAC address is only 48 bits in length.|Но ваш MAC-адрес имеет длину всего 48 бит.
You need a 64 bit address, the interface ID portion of it, right?|Вам нужен 64-битный адрес, часть идентификатора интерфейса, верно?
So what does it do?|Так что он делает?
It puts a triple FE, FF, FE, smack in the middle of that MAC address.|Он помещает тройной FE, FF, FE, удар в середине этого MAC-адреса.
So let's take a look at, we've done, I'm gonna copy what I've done and I'll do a DO WR.|Итак, давайте посмотрим, что мы сделали, я скопирую то, что сделал, и сделаю DO WR.
Yes, you cannot do that in the test.|Да, в тесте этого сделать нельзя.
You have to exit, exit.|Вы должны выйти, выйти.
Copy from start.|Скопируйте с начала.
I'm gonna do a, yeah, let me go, let me,|Я собираюсь сделать, да, отпусти меня, позволь мне,
let me, do the right way.|позволь мне поступить правильно.
Here you go.|Ну вот.
Not the right way, the test way.|Не правильный путь, тестовый путь.
I'm gonna do show, ipv6, show ipv6|Я покажу, ipv6, покажу ipv6
address.|адрес.
Oh int brief, sorry.|Ой, кратко, извините.
Int brief, and you can see that in my fast Ethernet, right here, right?|Кратко, и вы можете видеть это в моем быстром Ethernet, прямо здесь, не так ли?
Here is my face, right?|Вот мое лицо, да?
1000, there's my network ID.|1000, вот и мой сетевой идентификатор.
And here is the interface portion, which I didn't put,|А вот интерфейсная часть, которую я не ставил,
it automatically did it for me.|он автоматически сделал это за меня.
There is the triple FE that I was telling you about,|Есть тройной FE, о котором я вам говорил,
that it put smack in the middle of the MAC address.|что он поставил удар в середине MAC-адреса.
Not to get too deep on it cuz that number two does mean something,|Не вдаваться в подробности, потому что номер два что-то значит,
the universal bit and all that.|универсальный бит и все такое.
No need to get into that.|Не нужно вдаваться в подробности.
What you need to get into is, hey,|Тебе нужно попасть туда, эй,
auto-configuration.|автоконфигурация.
You're using the EUI 64, which is going to use the triple FE padding to create a for,|Вы используете EUI 64, который будет использовать тройное заполнение FE для создания for,
from a 48 bit MAC address into a 64 bit MAC address for my interface ID portion of the IPv6|из 48-битного MAC-адреса в 64-битный MAC-адрес для моей части идентификатора интерфейса IPv6
address.|адрес.
And that's what that's for.|И это для чего.
That's it.|Вот и все.
My curiosity is in the PC.|Мое любопытство связано с ПК.
I wanna see, oh, I didn't do a no shut.|Я хочу увидеть, о, я не закрыл глаза.
[SOUND] Ouch.|[ЗВУК] Ой.
But it's, oh yeah, I didn't do a no shut.|Но это, о да, я не закрыл глаза.
Whoops, let me go back in.|Упс, позволь мне вернуться.
Int f0/1 no shut.|Int f0 / 1 не закрыто.
All right.|Отлично.
[BLANK_AUDIO]|[BLANK_AUDIO]
There she blows.|Вот она и дует.
And just out curiosity, let me take a look at that.|И просто из любопытства, позвольте мне взглянуть на это.
It didn't do anything.|Это ничего не дало.
All right.|Отлично.
It just assigned it to that interface.|Он просто назначил его этому интерфейсу.
I would have to, I think there's a command here you can do.|Мне бы пришлось, я думаю, здесь есть команда, которую вы можете выполнить.
IPv6, IPv6 config forward slash renew.|IPv6, обновление косой черты конфигурации IPv6.
Is it?|Это?
That's what it is?|Это и есть?
No.|Нет.
So then [INAUDIBLE] that.|Так что [НЕРАЗБОРЧИВО] это.
IPv6 config,|Конфигурация IPv6,
forward slash, all.|косая черта, все.
Okay.|Ладно.
IPv6config /all for the v renew then.|Затем обновите IPv6config / all для v.
Nope, there's no renew.|Нет, продления нет.
Is that a question mark?|Это вопросительный знак?
Yeah, there's a renew.|Да, есть обновление.
It's right there.|Это прямо там.
Why is it telling me that it's not doing that?|Почему он говорит мне, что этого не делает?
I guess you need a DHCP or something for it to do it.|Я думаю, вам нужен DHCP или что-то еще для этого.
So I can do it.|Так что я могу это сделать.
I can actually put it in manually since it won't do it.|Я действительно могу вставить его вручную, потому что он этого не сделает.
But you can see I do have my Link-local address, right there.|Но вы можете видеть, что у меня есть мой локальный адрес ссылки прямо здесь.
All right, so I can go ahead and ping that.|Хорошо, я могу пойти и проверить это.
But I really don't want that, I wanted to go ahead and, see,|Но я действительно не хочу этого, я хотел пойти дальше и, видите ли,
the ACP version 6 request failed.|запрос ACP версии 6 завершился неудачно.
So that's the reason that's doing that.|Вот почему это происходит.
But now you see the reason for the auto-configuration.|Но теперь вы видите причину автоконфигурации.
You can dynamically assign, IP, the interface ID portion of it dynamically, automatically,|Вы можете динамически назначать IP, часть идентификатора интерфейса, динамически, автоматически,
by itself, just by using that EUI 64.|сам по себе, просто используя этот EUI 64.
The only thing is that now your Mac address is part of your IP address.|Единственное, что теперь ваш Mac-адрес является частью вашего IP-адреса.
Some people don't like that within Windows you can go ahead an generate random numbers, you don't have to use that padding.|Некоторым людям не нравится, что в Windows вы можете генерировать случайные числа, вам не нужно использовать это заполнение.
But again, it it's a small network, you really don't have to be concerned with it.|Но опять же, если это небольшая сеть, вам действительно не нужно о ней беспокоиться.
You can just put it in, you know, ::1 like I do.|Вы можете просто вставить его, знаете, :: 1, как я.
::2, ::3, and you know, you can go that way.|:: 2, :: 3, и вы знаете, вы можете пойти этим путем.
I mean you have, my God, you have eight,|Я имею в виду, что у тебя есть, боже мой, у тебя восемь,
you have four sections and you can just start making up numbers or have your own scheme if you wanted to.|у вас есть четыре раздела, и вы можете просто начать придумывать числа или иметь свою собственную схему, если хотите.
But if you have, if you work in a pretty large network, you may just wanna, you know, configure DHCP version 6 and have it|Но если у вас есть, если вы работаете в довольно большой сети, вы можете просто захотеть настроить DHCP версии 6 и получить ее.
assign these addresses dynamically.|назначать эти адреса динамически.
Well there it is, auto-configuration.|Ну вот, автоконфигурация.
I's not really that, that difficult to configure, and it actually, let me,|Я не такой уж сложный в настройке, и на самом деле, позвольте мне,
so we can take a look at it again, so you don't forget what it looks like.|чтобы мы могли взглянуть на него еще раз, чтобы вы не забыли, как он выглядит.
Show IPv6, in brief, I should have just done an up arrow.|Покажи вкратце IPv6, я должен был сделать стрелку вверх.
All right, and there's, it actually assigned that particular portion of the address dynamically because of auto-configuration.|Хорошо, и вот, он фактически назначил эту конкретную часть адреса динамически из-за автоконфигурации.
Pretty cool feature in IPv6.|Довольно крутая функция в IPv6.
Now you know what it is.|Теперь вы знаете, что это такое.
The mystery is over.|Тайна окончена.
All right.|Отлично.
Play around with it.|Поиграйте с этим.
And and see what you can do.|И посмотрите, что вы можете сделать.
I'll see you in the next one.|Увидимся в следующем.
[BLANK_AUDIO]|[BLANK_AUDIO]