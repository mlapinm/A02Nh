D:\mailCloud\prjother\tmp\1\c109_Configuring PPP and Verifying PPP.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
And now it comes time to configure P-P-P.|А теперь пришло время настроить P-P-P.
Very simple only two routers, not a big deal.|Очень просто всего два роутера, не беда.
This is gonna example that you will see in the certification.|Это будет пример, который вы увидите в сертификации.
Alright, so we'll make it simple, straight to the point so we get there you know what to look for.|Хорошо, поэтому мы сделаем это просто, прямо к делу, чтобы вы знали, что искать.
So we're going to configure [UNKNOWN].|Итак, мы собираемся настроить [НЕИЗВЕСТНО].
The first thing obviously, let's put the ip addresses.|Первым делом очевидно поставим ip адреса.
These routers are not configured,|Эти маршрутизаторы не настроены,
you can see with the red dots that's there no ip address on there.|вы можете видеть с помощью красных точек, что там нет IP-адреса.
I will wave my magic wand, no I'm just kidding.|Я взмахну волшебной палочкой, нет, я шучу.
So like Vanna White here, all right.|Итак, как здесь Ванна Уайт, хорошо.
So let's go ahead, this is 10114 network,|Итак, давайте, это сеть 10114,
very simple, very simple.|очень просто, очень просто.
S triple zero.|S тройной ноль.
Okay.|Ладно.
So we're gonna enable config T.|Итак, мы собираемся включить конфигурацию T.
Now I'm actually configuring.|Сейчас собственно настраиваю.
When you do these labs be careful.|Будьте осторожны при выполнении этих лабораторных работ.
Because I know one of the students in the classroom they actually start doing these labs even with two routers, they for whatever reason,|Поскольку я знаю одного из студентов в классе, они фактически начинают выполнять эти лабораторные работы даже с двумя маршрутизаторами, они по какой-то причине,
the labs become an ordeal and this is why,|лаборатории становятся тяжелым испытанием, и вот почему,
and this is what I tell them.|и вот что я им говорю.
This is not an English class, don't worry about proper grammar meaning capitalize the first letter and on the list though|Это не урок английского языка, не беспокойтесь о правильной грамматике, это означает, что первая буква в списке должна быть заглавной.
because they forget.|потому что они забывают.
And then, they don't have, their passwords don't match or their username don't match.|А потом у них нет, их пароли не совпадают или их имя пользователя не совпадает.
So either do everything in lowercase or do everything in upper case, or have very good memory, cuz my memory is pretty much trashed.|Так что либо делайте все в нижнем регистре, либо делайте все в верхнем регистре, либо у меня очень хорошая память, потому что моя память в значительной степени испорчена.
On how you type these usernames and host names,|О том, как вы вводите эти имена пользователей и имена хостов,
because they're important, especially when it comes to PBP.|потому что они важны, особенно когда речь идет о PBP.
All right, so I'm doing everything in caps, that doesn't mean you have to.|Хорошо, я все делаю заглавными буквами, это не значит, что вы должны.
I just CONFIG T, ho, HOSTNAME, R1.|Я просто КОНФИГУРИРУЮ T, ho, HOSTNAME, R1.
[BLANK_AUDIO]|[BLANK_AUDIO]
So when I create the username on the other router it has to be, the same,|Поэтому, когда я создаю имя пользователя на другом маршрутизаторе, оно должно быть таким же,
if it's different it will not work.|если другое, работать не будет.
All right so what am I gonna do?|Хорошо, так что мне делать?
What do I think?|Что я думаю?
Well the IP address.|Ну IP-адрес.
Interface F0/0/0.|Интерфейс F0 / 0/0.
IP address 10.1.1.5,|IP-адрес 10.1.1.5,
255.255.255.252 using a slider 30.|255.255.255.252 с помощью ползунка 30.
So we need a clock rate.|Итак, нам нужна тактовая частота.
Clock rate.|Тактовая частота.
No frame relay cloud here right?|Здесь нет облака Frame Relay?
Clock rate.|Тактовая частота.
Formulating.|Разработка.
One, two, three.|Раз два три.
One, two, three.|Раз два три.
Because we've got it like that.|Потому что у нас это так.
Do WR.|Сделайте WR.
Cool?|Круто?
Ctrl+Z.|Ctrl + Z.
Ctrl+Z.|Ctrl + Z.
All right.|Все в порядке.
So that's all we're going to do for right now.|Так что это все, чем мы сейчас займемся.
We'll go to the IP addresses.|Пойдем по IP-адресам.
And let's go to this one.|И перейдем к этому.
And this is router two, router two.|А это второй маршрутизатор, второй маршрутизатор.
We're going to say no.|Мы скажем нет.
We want to do things from scratch.|Мы хотим делать все с нуля.
Ctrl+Shift+6 config t false name r2.|Ctrl + Shift + 6 config t false name r2.
All right so we go, what is this?|Хорошо, пошли, что это?
This is interface 001 right?|Это интерфейс 001, верно?
I'm pretty sure.|Я точно уверен.
All right [INAUDIBLE],|Хорошо [НЕРАЗБОРЧИВО],
yes 001.|да 001.
Hint 0/0/1 IP address,|Подсказка 0/0/1 IP-адрес,
depends on what I want to fix.|зависит от того, что я хочу исправить.
255.255.255.252.|255.255.255.252.
No shut is the DTE portion of it and change state to down.|Нет выключения - это часть DTE, и он не изменит состояние на выключенное.
You know, if I did it on the S, 00,|Знаешь, если бы я сделал это на S, 00,
both, no, no, okay, why is it down?|оба, нет, нет, хорошо, почему он не работает?
It should have came up.|Это должно было произойти.
10116, okay, hm, interesting.|10116, ладно, хм, интересно.
All right, interface is 001, right, is that yeah 001, okay.|Хорошо, интерфейс 001, да, это 001, хорошо.
IP address [UNKNOWN] okay, Ctrl+Z.|IP-адрес [НЕИЗВЕСТНО] хорошо, Ctrl + Z.
Ctrl+Z, WR show IP in brief its telling me down down that's a physical error problem, okay interesting,|Ctrl + Z, WR показывает IP вкратце, он говорит мне, что это проблема с физической ошибкой, хорошо, интересно,
let's take a look at the other side there,|давайте посмотрим на другую сторону там,
not doing no shut over here.|не закрываясь здесь.
Oh yes I forgot to do a no shut.|О да, я забыл сделать «нет, заткнись».
You see?|Ты видишь?
Brain is gone.|Мозга больше нет.
Int S 0/0/0.|Инт S 0/0/0.
No shut.|Нет, заткнись.
DO WR.|DO WR.
Ctrl+Z.|Ctrl + Z.
Show IP and brief, and now it's up down.|Покажи IP и бриф, а теперь вверх вниз.
Change date to up to go a little bit.|Измените дату на более высокую, чтобы немного уйти.
Now it's up, up.|Теперь все вверх, вверх.
We can ping.|Мы можем пинговать.
10.1.1.6.|10.1.1.6.
So we have connectivity, right?|Итак, у нас есть связь, верно?
Point to point.|Точка-точка.
We haven't configured any, any protocols or anything.|Мы не настроили никаких протоколов или чего-то еще.
They're just connected.|Они просто связаны.
You know, one router to the next.|Вы знаете, от одного маршрутизатора к другому.
So let's take a look at the interface.|Итак, давайте посмотрим на интерфейс.
Show IP interface S0/0/0.|Показать IP-интерфейс S0 / 0/0.
Wrong command.|Неправильная команда.
Show interface S0/0/0.|Показать интерфейс S0 / 0/0.
So [UNKNOWN].|Итак [НЕИЗВЕСТНО].
All right, what is it that we're looking at?|Хорошо, на что мы смотрим?
Right here, by default Encapsulation HDLC.|Прямо здесь по умолчанию инкапсуляция HDLC.
That's why it's working.|Вот почему это работает.
Because that's the default encapsulation.|Потому что это инкапсуляция по умолчанию.
They're both Cisco routers, so they're going to be talking to each other.|Это оба маршрутизатора Cisco, поэтому они будут разговаривать друг с другом.
They have the same proprietary information within their headers so there are no issues.|У них в заголовках одинаковая конфиденциальная информация, поэтому проблем нет.
So once you put in the IP addresses, hey we're talking.|Итак, как только вы введете IP-адреса, мы говорим.
Not a big deal.|Не так уж и важно.
But it's gonna be a big deal now because we're gonna change the encapsulation time to PPP all right?|Но сейчас это будет иметь большое значение, потому что мы собираемся изменить время инкапсуляции на PPP, хорошо?
So let's go ahead and do that.|Так что давайте продолжим и сделаем это.
So, show interface as 000 you see, that's gonna be [UNKNOWN] by default.|Итак, покажите интерфейс как 000, как вы видите, по умолчанию он будет [НЕИЗВЕСТНО].
Let's change that.|Давай изменим это.
Config T.|Конфиг T.
Interface.|Интерфейс.
S, 0/0/0.|S, 0/0/0.
WNCAP, PPP.|WNCAP, PPP.
That's all we're going to do.|Это все, что мы собираемся сделать.
Do WR, Ctrl+Z, show IP in brief.|Сделайте WR, Ctrl + Z, кратко покажите IP.
[BLANK_AUDIO].|[BLANK_AUDIO].
Now we have an up, down.|Теперь у нас есть вверх и вниз.
When you have that, that means there's an encapsulation issue.|Когда он у вас есть, это означает, что есть проблема с инкапсуляцией.
All right.|Все в порядке.
There's, and you'll see print screens,|Вот и вы увидите экраны печати,
I'll show you maybe this.|Я покажу тебе, может быть, это
All right?|Все в порядке?
But it's, when they show you that it's up,|Но это когда они показывают тебе, что все кончено,
down, you know it's either a clock rate that's not on there or some sort of protocol right?|вниз, вы знаете, что это либо тактовая частота, которой нет, либо какой-то протокол, верно?
Encapsulation mismatch.|Несоответствие инкапсуляции.
That will be the errors that you'd be getting or it could also be CRC errors.|Это будут ошибки, которые вы получите, или это также могут быть ошибки CRC.
Okay.|Ладно.
That you're getting duplex mismatch.|Что вы получаете дуплексное несовпадение.
All right or it will give you that as well.|Ладно, или это даст вам и это.
But normally we're looking for encapsulation issues, or clock rate issues here.|Но обычно мы ищем здесь проблемы с инкапсуляцией или тактовой частотой.
But we know for a fact show interface as 0/0/0.|Но мы точно знаем, что интерфейс показан как 0/0/0.
Then now we see this is what we don't wanna see.|Тогда теперь мы видим, что это то, чего мы не хотим видеть.
We see, well here we see that the encap is now PPP.|Мы видим, здесь мы видим, что теперь инкапция является PPP.
But look what goes on.|Но посмотрите, что происходит.
LCP, the link control protocol is closed.|LCP, протокол управления каналом закрыт.
And the discovery protocol, control protocol, all right, it also closed.|И протокол обнаружения, протокол управления, да ладно, тоже закрытый.
Those major two and internet protocol,|Эти два основных и интернет-протокол,
closed.|закрыто.
So, but this one, this is what creates the link, right?|Итак, но вот что создает ссылку, не так ли?
This is the one with the authentication,|Это тот, у которого есть аутентификация,
with the compression.|со сжатием.
And remember, PPP has an establishment phase and the first part of that phase is the link.|И помните, у PPP есть фаза установления, и первая часть этой фазы - это связь.
So, it tries to create a link with the other router.|Таким образом, он пытается установить связь с другим маршрутизатором.
It can't.|Не может.
They can't at this point, because now the other router's running ACLC this was running PPP so it's not gonna work.|На данный момент они не могут, потому что теперь другой маршрутизатор работает с ACLC, он использует PPP, поэтому он не будет работать.
All right, well let's go to the other router.|Хорошо, перейдем к другому роутеру.
Let's go to the other router and change it to PPP and see what happens.|Давайте перейдем к другому маршрутизатору, изменим его на PPP и посмотрим, что произойдет.
So a RNCAP, PPP look at this!|Итак, RNCAP, PPP посмотрите на это!
Something came up there.|Что-то там произошло.
Look at that, interesting.|Посмотри, интересно.
Show IP INT BRIEF.|Показать краткое изложение IP INT.
Now it came back up, up, up.|Теперь он вернулся вверх, вверх, вверх.
Look at that, all right?|Посмотри на это, хорошо?
Up, up, let's take a look at the interface.|Вверх, вверх, взглянем на интерфейс.
What is the interface telling us?|О чем нам сообщает интерфейс?
Show interface S0/01/1.|Показать интерфейс S0 / 01/1.
Now, this is what we wanna see.|Вот что мы хотим увидеть.
LCP is open.|ЛКП открыта.
Internet protocol control protocol, open.|Протокол управления интернет-протоколом, открытый.
Discovery protocol control protocol is open.|Протокол управления протоколом обнаружения открыт.
That is what we wanna see when we're troubleshooting PVP.|Это то, что мы хотим видеть при устранении неполадок PVP.
If you see that these lines are closed.|Если вы видите, что эти линии закрыты.
There's something going on.|Что-то происходит.
Either there's a mismatch and, and, and I encapsulation type.|Либо есть несоответствие и, и, и типа инкапсуляции.
Or the wrong user name.|Или неправильное имя пользователя.
Or the wrong authentication.|Или неправильная аутентификация.
Things of that nature.|Вещи такого рода.
All right, so we gotten our both routers running PPP.|Итак, мы получили оба маршрутизатора, работающие по протоколу PPP.
But we need to add authentication, for this add authentication.|Но нам нужно добавить аутентификацию, для этого добавьте аутентификацию.
So we need to create a username, and we need to decide what type of authentication to use.|Итак, нам нужно создать имя пользователя и решить, какой тип аутентификации использовать.
PPP can use two types of authentication.|PPP может использовать два типа аутентификации.
CHAP, PAP.|ЧАП, ПАП.
And it just so happens that the second part of the link establishment phase of PPP Is authentication.|И так уж получилось, что вторая часть фазы установления соединения PPP - это аутентификация.
So there is an authentication in this point, so they didn't even bother to look at it.|Так что здесь есть аутентификация, поэтому они даже не удосужились взглянуть на нее.
But now when we configure it, now it will look at it.|Но теперь, когда мы его настраиваем, теперь он будет смотреть на это.
So, let's go in first.|Итак, займемся первым.
Go to global configuration.|Заходим в глобальную конфигурацию.
Let's create a username.|Создадим имя пользователя.
Username R1 goes right in R2, password CISCO.|Имя пользователя R1 идет прямо в R2, пароль CISCO.
And then we go inside the interface,|А затем заходим внутрь интерфейса,
S0/0/1 and go PPP authentication check path.|S0 / 0/1 и перейдите по пути проверки аутентификации PPP.
Why are you gonna do both?|Почему ты собираешься сделать и то, и другое?
If one fails, the other one takes over.|Если один терпит неудачу, другой берет верх.
Obviously, we want CHAP first because it uses MV5.|Очевидно, что сначала нам нужен CHAP, потому что он использует MV5.
Where PAP is plain text.|Где PAP - это обычный текст.
But at least it will be something right?|Но хоть что-то будет правильно?
So you can use either both or just use CHAP.|Таким образом, вы можете использовать оба или просто использовать CHAP.
The one second one will always be the fallback.|Один второй всегда будет запасным вариантом.
Now you gotta do it in the same order in the other side as well.|Теперь вы должны сделать это в том же порядке и с другой стороны.
So if in this side you do CHAP PAP, you can't do PAP CHAP on the other side because it will look at the first type of authentication that you're using.|Поэтому, если на этой стороне вы выполняете CHAP PAP, вы не можете использовать PAP CHAP на другой стороне, потому что он будет рассматривать первый тип аутентификации, который вы используете.
All right?|Все в порядке?
So, what's going on?|Так что же происходит?
It said it changed state to down.|Он сказал, что он изменил состояние на выключенное.
Let's take a look again.|Давайте посмотрим еще раз.
Let's do a WR, let's do a show IP INT brief, and again, up down.|Давайте сделаем WR, давайте покажем IP INT бриф и снова вверх-вниз.
Let me take a look here.|Позвольте мне взглянуть сюда.
Show Interface S0/0/1 and,|Показать интерфейс S0 / 0/1 и,
again, we have our LCP closed.|Опять же, наша LCP закрыта.
And then our [INAUDIBLE] protocol closed.|А потом наш [НЕВНЯТНО] протокол закрылся.
Right?|Правильно?
CDP control protocol closed.|Протокол управления CDP закрыт.
So, and the reason is, now we're using authentication on one side but we're not on the other.|Итак, и причина в том, что теперь мы используем аутентификацию с одной стороны, но не с другой.
So again, they both sides must be match.|Итак, опять же, обе стороны должны совпадать.
Must match.|Должен совпадать.
So let's go to router one.|Итак, перейдем к маршрутизатору один.
And this is exactly, I'm telling you now,|И это именно то, что я вам сейчас говорю,
this is what they're gonna be looking for in the certification.|это то, что они будут искать в сертификации.
Again, another configuration because you're not gonna be configuring this.|Опять же, другая конфигурация, потому что вы не собираетесь ее настраивать.
But you'll have print screens.|Но у вас будут экраны для печати.
So, these are the things you need to look for.|Итак, это то, что вам нужно искать.
Now, that's why I'm doing it like this,|Вот почему я делаю это так,
okay?|Ладно?
So, again, let's configure a user name so if I'm on router one,|Итак, снова давайте настроим имя пользователя, чтобы, если я нахожусь на первом маршрутизаторе,
it will be router two.|это будет второй роутер.
So, user name, R2, password, Cisco.|Итак, имя пользователя, R2, пароль, Cisco.
Passwords must be identical.|Пароли должны быть идентичными.
You're gonna have different passwords.|У вас будут разные пароли.
Must be identical, everything is case sensitive.|Должны быть идентичны, все с учетом регистра.
Okay?|Ладно?
Look at that.|Посмотри на это.
Just by putting the username, you see it changed state up.|Просто введя имя пользователя, вы увидите, что его состояние изменилось.
But we still need to do the authentication.|Но нам еще нужно пройти аутентификацию.
So we go end, as 0/0/0.|Итак, идем в конец, как 0/0/0.
PPP authentication chap pac.|Аутентификация PPP глава pac.
Do WR.|Сделайте WR.
Ctrl+Z.|Ctrl + Z.
Show IP in brief.|Покажите кратко IP.
Now we're up, up again.|Теперь мы встали, снова встали.
So we look at the interface.|Итак, смотрим на интерфейс.
Show interface as 0/0 oops.|Показать интерфейс как 0/0 ой.
Slide zero.|Сдвиньте ноль.
Enter.|Войти.
Now we see again.|Теперь мы снова видим.
LCP is open.|ЛКП открыта.
And IP CP and CDP CP is open.|И IP CP и CDP CP открыты.
And that is what you want to see.|И это то, что вы хотите увидеть.
You want to see that that's open.|Вы хотите увидеть, что это открыто.
So ways that they, they'll trick you in the exams,|Таким образом, они обманывают вас на экзаменах,
is just that you've got two routers.|просто у вас есть два роутера.
And they'll show you the passwords for either or, or for both, and usernames for both.|И они покажут вам пароли для одного или, или для обоих, и имена пользователей для обоих.
And you gotta look and see if everything's okay.|И ты должен посмотреть, все ли в порядке.
Cuz now remember, the username.|Потому что теперь помните, имя пользователя.
[BLANK_AUDIO]|[BLANK_AUDIO]
Should start.|Должен начаться.
The username is of the other router.|Имя пользователя принадлежит другому маршрутизатору.
And it's plain text you see there, that's why it's zero.|И вы видите там обычный текст, поэтому его ноль.
I didn't put it in there, it put it in there by itself.|Я не вставлял его туда, он сам вставлял.
All right.|Все в порядке.
So, R2, right, on R1 and R1 on R2.|Итак, R2, справа, на R1 и R1 на R2.
So the username is the host name of the other router.|Таким образом, имя пользователя - это имя хоста другого маршрутизатора.
And, the passwords must be identical.|И пароли должны быть идентичными.
So that's something that we'll mess around with as well.|Так что это то, с чем мы тоже будем возиться.
Also, look to see if the end of print screen, again,|Кроме того, посмотрите, снова ли в конце экрана печати
when you're looking at it, that the encapsulation type.|когда вы смотрите на это, тип инкапсуляции.
So they give you a screenshot like show interface.|Так что они дают вам скриншот, как интерфейс шоу.
S0, where am I, 1/0/0.|S0, где я, 1/0/0.
Make sure the, cuz they'll give you, you know, a side by side comparison.|Убедитесь, что они дадут вам параллельное сравнение.
That they're, you know, look at the encapsulation.|Что они, вы знаете, посмотрите на инкапсуляцию.
You look at the encapsulation.|Вы смотрите на инкапсуляцию.
Make sure that they're both using the same, all right?|Убедитесь, что они оба используют одно и то же, хорошо?
Cuz if you have PPP on one, HDLC on the other, [NOISE], not gonna work.|Потому что, если у вас PPP на одном, HDLC на другом, [NOISE] не будет работать.
Not going to work so these are the things that they look for.|Это не сработает, так что это то, что они ищут.
PPP is not difficult at all and the questions related to PPP is exactly what I just showed you.|PPP совсем несложен, и вопросы, связанные с PPP, - это именно то, что я вам только что показал.
They're going to be looking that you know they're going to be looking for that you know that has to be the same type of encapsulation.|Они будут искать, что, как вы знаете, они будут искать, что, как вы знаете, должна быть инкапсуляция того же типа.
That if you're going to use PPP, it can be whatever manufacturer or router.|Что если вы собираетесь использовать PPP, это может быть любой производитель или маршрутизатор.
If you're going to use ADLC, they better be the same.|Если вы собираетесь использовать ADLC, лучше они будут такими же.
That's another way they can trick you.|Это еще один способ обмануть вас.
They can have Cisco router, Juniper router.|У них может быть маршрутизатор Cisco, маршрутизатор Juniper.
They're both using ADLC.|Они оба используют ADLC.
Will they talk?|Они будут говорить?
No they won't, because it's proprietary.|Нет, они не будут, потому что это проприетарно.
These are the pitfalls right there.|Вот и все подводные камни.
This is the configuration of PPP.|Это конфигурация PPP.
There's nothing to it.|Ничего особенного.
And you can see, let's ping again.|И видите, давайте снова пингуем.
10.1.1.6.|10.1.1.6.
We're back in business.|Мы снова в деле.
We're back in business.|Мы снова в деле.
We have the same, we have the correct username and password.|У нас то же самое, у нас правильный логин и пароль.
We have the right type of authentication,|У нас есть правильный тип аутентификации,
the right order.|правильный порядок.
[UNKNOWN] on bull.|[НЕИЗВЕСТНО] о быке.
And we have the right encapsulation type,|И у нас есть правильный тип инкапсуляции,
which is PBP.|что и есть PBP.
Though obviously, the IP address has to be correct.|Хотя, очевидно, IP-адрес должен быть правильным.
All right.|Все в порядке.
So PBP most definitely is the most popular one of all.|Итак, PBP определенно является самым популярным из всех.
It's an open standard.|Это открытый стандарт.
You don't have to worry about it.|Вам не о чем беспокоиться.
Everybody uses it.|Все используют это.
But on your test, please be aware of that.|Но помните об этом на своем тесте.
Be aware, and be careful, pay attention to detail, that the routers are,|Имейте в виду, и будьте осторожны, обратите внимание на детали, что маршрутизаторы,
the routers are Cisco, or they're not Cis,|маршрутизаторы Cisco или не СНГ,
well yeah Cisco or non Cisco, all right,|ну да Cisco или не Cisco, хорошо,
for the encapsulation.|для инкапсуляции.
All right ladies and gentleman, this is PPP.|Хорошо, дамы и господа, это PPP.
I'll see you in the next one.|Увидимся в следующем.
[BLANK_AUDIO]|[BLANK_AUDIO]
  
  
