D:\mailCloud\prjother\tmp\1\c18_The 3 Upper Layers of the OSI.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
All right.|Отлично.
Let's get to it.|Давайте перейдем к этому.
The upper three layers, the Application layer,|Три верхних уровня, уровень приложения,
the Presentation layer, and the Session layer.|уровень представления и уровень сеанса.
The ones in red, which you see DATA, DATA,|Красные, на которых вы видите ДАННЫЕ, ДАННЫЕ,
DATA.|ДАННЫЕ.
That is what's called a PDU, a Protocol Data Unit.|Это то, что называется PDU, блоком данных протокола.
That's what the book defines as it talks to its peer layer.|Это то, что книга определяет, когда разговаривает со своими коллегами.
Okay?|Ладно?
What happens at the Application layer?|Что происходит на прикладном уровне?
What is the Application layer?|Что такое прикладной уровень?
Is that Word, Excel, PowerPoint?|Это Word, Excel, PowerPoint?
Of course not.|Конечно нет.
All right.|Отлично.
The application layer actually accesses the network to see if it's ready to receive information.|Уровень приложения фактически обращается к сети, чтобы узнать, готов ли он к приему информации.
So any application that uses the network,|Итак, любое приложение, использующее сеть,
we're dealing with the application layer.|мы имеем дело с прикладным уровнем.
So, when we're using HTTP or HTTPS,|Итак, когда мы используем HTTP или HTTPS,
meaning we're in a browser.|это означает, что мы в браузере.
The browser is the interface.|Браузер - это интерфейс.
But the protocol is what deals with the application layer.|Но протокол - это то, что имеет дело с прикладным уровнем.
We have FTP, TFTP, all right, where we are transferring files.|У нас есть FTP, TFTP, все в порядке, куда мы передаем файлы.
SMTP, email, if we are using Outlook.|SMTP, электронная почта, если мы используем Outlook.
It is an interface.|Это интерфейс.
But the protocols, whether it be SNTP,|Но протоколы, будь то SNTP,
POP, IMAP, all these different types of protocols that deal with email, those access the network, all right?|POP, IMAP, все эти разные типы протоколов, которые работают с электронной почтой, те, которые имеют доступ к сети, понятно?
So those deal with the application layer.|Итак, это касается прикладного уровня.
TELNET, trouble emulation programs that let you access the network.|TELNET, программы эмуляции неисправностей, позволяющие получить доступ к сети.
SSH, DNS.|SSH, DNS.
DNS uses the application layer.|DNS использует прикладной уровень.
One thing I wanna talk about DNS, I can't help myself.|Одна вещь, которую я хочу сказать о DNS, я не могу с собой поделать.
DNS also uses TCP or UDP.|DNS также использует TCP или UDP.
It all depends on what you're doing with DNS, so keep that in mind, keep that in mind.|Все зависит от того, что вы делаете с DNS, так что имейте это в виду.
DNS uses both TCP and UDP.|DNS использует как TCP, так и UDP.
And though it works with the application layer it's, if you're doing let's say,|И хотя он работает на уровне приложения, если вы, скажем,
a domain replication, you know,|репликация домена, вы знаете,
essentially replication definitely using TCP, because of the size of the file is gonna be big, and something very important, so you have to|по сути, репликация определенно с использованием TCP, потому что размер файла будет большим, и что-то очень важное, поэтому вам нужно
be connection oriented.|быть ориентированным на соединение.
Where, if it's just you're, you're looking for a computer name or a host name an object, it'll use UDP.|Если вы ищете имя компьютера или имя хоста для объекта, он будет использовать UDP.
Keep that in mind, DNS uses both of those two protocols, TCP and UDP.|Имейте в виду, что DNS использует оба этих протокола, TCP и UDP.
It all depends on what it's doing.|Все зависит от того, что он делает.
The NTP news time, SNMP, right?|Время новостей NTP, SNMP, верно?
Network Management Protocol and DHCP.|Протокол сетевого управления и DHCP.
All these things, all these protocols,|Все эти вещи, все эти протоколы,
access the network,|доступ к сети,
therefore they work at the application.|поэтому они работают в приложении.
So do not get them confused that hey,|Так что не путайте их, эй,
Outlook must be in the application layer.|Outlook должен находиться на уровне приложения.
No, Outlook is not in the application layer.|Нет, Outlook не находится на уровне приложений.
That is an interface.|Это интерфейс.
Just like Word.|Также как Word.
It is an interface.|Это интерфейс.
Your browser.|Ваш браузер.
It is an interface.|Это интерфейс.
But how do we get to see what's on the network?|Но как нам увидеть, что находится в сети?
Through the use of those particular protocols, okay?|Благодаря использованию этих конкретных протоколов, хорошо?
HTTP, FTP, and so forth.|HTTP, FTP и так далее.
Presentation layer.|Слой представления.
Again still data.|Опять таки данные.
That's the PDU.|Это PDU.
Nothing's been broken down yet.|Еще ничего не сломано.
Still big, one big chunk.|Все еще большой, один большой кусок.
All right?|Отлично?
But the Presentation layer presents things to the application layer,|Но уровень презентации представляет вещи на уровне приложения,
as it starts coming right back up the OSI model.|как только он начинает возвращаться к модели OSI.
It presents things to the application.|Он представляет вещи приложению.
Because what, what does the presentation layer deal with?|Потому что что, с чем имеет дело уровень представления?
Formatting.|Форматирование.
What are we talking, are we talking ASCII?|Что мы говорим, мы говорим ASCII?
Are we talking EBCDIC which is mainframe?|Мы говорим об EBCDIC, который является мэйнфреймом?
We're dealing with Encryption and Decryption.|Мы имеем дело с шифрованием и дешифрованием.
So then of course, proper delivery and formatting.|Итак, конечно, правильная доставка и форматирование.
So this is what we deal with in the presentation lay.|Это то, чем мы занимаемся в презентации.
This is all you really need to drill down to.|Это все, что вам действительно нужно.
Do you know how to get crazy?|Ты умеешь сходить с ума?
We can spend six months.|Мы можем провести полгода.
All right, six years talking about everything that happens in each layer of the OSI model.|Хорошо, шесть лет говорят обо всем, что происходит на каждом уровне модели OSI.
You don't need to do that.|Вам не нужно этого делать.
You don't need to do that.|Вам не нужно этого делать.
The, this right here, which you will have this is all you really need to know.|Это все, что вам действительно нужно знать.
But again, Presentation layer, is still one big chunk of data.|Но опять же, уровень представления - это все еще один большой кусок данных.
It presents things to the application layer,|Он представляет вещи на прикладном уровне,
which as they say, closest to the user.|который, как говорится, ближе всего к пользователю.
What we see?|Что мы видим?
So, if we're going from mainframe to ASCII,|Итак, если мы перейдем от мэйнфрейма к ASCII,
it's a presentation layers job to make sure to make that translation.|Это задача слоев презентации, чтобы сделать этот перевод.
All right, if we're encrypting information.|Хорошо, если мы шифруем информацию.
It must make it, the encryption, it must do the encryption for us.|Он должен сделать это, шифрование, он должен сделать шифрование за нас.
A, I mean, I'll make it as simple as RTF.|В смысле, я сделаю это так же просто, как RTF.
All right, or your, or JPEG.|Ладно, или ваш, или JPEG.
They type of formatting used.|Тип используемого форматирования.
That it the job of the presentation layer.|Это работа уровня представления.
The next one is a Session layer.|Следующий - это сеансовый уровень.
Again data.|Снова данные.
Nothing's been broken up.|Ничего не сломано.
Nothing's been taken apart.|Ничего не разбиралось.
Mm, Starts, Maintains, and ends communications sessions between applications.|Мм, запускает, поддерживает и завершает сеансы связи между приложениями.
It keeps each application different.|Благодаря этому каждое приложение отличается.
So, if you're using your browser for HTTP,|Итак, если вы используете свой браузер для HTTP,
if you're using FTP,|если вы используете FTP,
if you're Telnetting, if you're using DNS,|если вы используете Telnet, если вы используете DNS,
if you're using mode desktop.|если вы используете режим рабочего стола.
Whatever it is you're using in there,|Что бы вы там ни использовали,
you're using different ports.|вы используете разные порты.
The application layer's job is to make sure,|Задача прикладного уровня - убедиться,
that those applications are separate.|что эти приложения отдельные.
And that it starts the session, that dialog, maintains it,|И что он запускает сеанс, этот диалог, поддерживает его,
and when it's closed out, it makes sure that it's closed.|а когда он закрыт, он следит за тем, чтобы он был закрыт.
So that it's, it's, that is its job.|Так что это, это, это его работа.
All right, to maintain all those applications separate from one another,|Хорошо, чтобы все эти приложения были отделены друг от друга,
and keep them working or if you're over,|и пусть они работают, или, если вы закончили,
and you close the browser, whatever the case may be, that application is closed.|и вы закрываете браузер, в любом случае это приложение закрывается.
So those are your upper three layers.|Итак, это ваши три верхних слоя.
Your upper three layers.|Ваши три верхних слоя.
And that's it.|И это все.
That's it.|Вот и все.
That's all you need to know.|Это все, что вам нужно знать.
All right, and remember where going down now.|Хорошо, и запомни, куда сейчас спускаемся.
We're going down the OSI.|Мы идем вниз по OSI.
We're doing the, from the very top, and we're gonna work our way down.|Мы делаем это с самого верха, и мы будем двигаться вниз.
From the very top, we're gonna work our way down.|С самого верха мы будем двигаться вниз.
And the first three layers, which are called the upper layers.|И первые три слоя, которые называются верхними слоями.
The PDUs, the Protocol data units are data, data, data.|PDU, блоки данных протокола - это данные, данные, данные.
Data, data, data.|Данные, данные, данные.
Do I have a Mnemonic devices for that?|Есть ли у меня для этого мнемонические устройства?
Yes, but I'm saving that for last.|Да, но я оставлю это напоследок.
All right.|Отлично.
Data, data, data.|Данные, данные, данные.
So these are the only things you need to memorize,|Так что это единственное, что вам нужно запомнить,
about the upper three layers of the OSI model.|о трех верхних уровнях модели OSI.
Now one thing that I do, not stress, but you should know.|Одно то, что я делаю, а не стресс, но вы должны знать.
Know the port numbers.|Знайте номера портов.
Port 80, port 443, 21 I forget TFTP SMTP 25, Telnet 22, SSH 23.|Порт 80, порт 443, 21 Я забываю TFTP SMTP 25, Telnet 22, SSH 23.
So you need to know, you should know that is basic port numbers.|Итак, вам нужно знать, вы должны знать, что это основные номера портов.
That is important to know, when especially,|Это важно знать, особенно когда
when you're creating access lists in the test.|когда вы создаете списки доступа в тесте.
So know your port numbers.|Так что знайте свои номера портов.
Know your port numbers.|Знайте свои номера портов.
But again, Application layer,|Но опять же, прикладной уровень,
Presentation, date Session,|Презентация, дата Сессия,
your upper three layers.|ваши три верхних слоя.
And remember, the lower layer will encapsulate the upper layer.|И помните, что нижний слой заключает в себе верхний слой.
The lower layer will encap, encapsulate the upper layer.|Нижний слой инкапсулирует верхний слой.
What does that mean?|Что это значит?
If you get a question that states,|Если вы получите вопрос, в котором говорится,
the presentation layer will encapsulate the session layer.|уровень представления инкапсулирует уровень сеанса.
That is incorrect.|Это неверно.
That is false.|Это неправда.
It is, the presentation layer will encapsulate the application layer.|То есть уровень представления инкапсулирует уровень приложения.
The session layer will encapsulate the presentation layer.|Сеансовый уровень инкапсулирует уровень представления.
So if you get a question like that remember,|Так что если у вас возникнет такой вопрос, помните,
the lower encapsulates the upper.|нижняя заключает в себе верхнюю.
All right.|Отлично.
Those are your upper three layers.|Это ваши три верхних слоя.
Next video, I told you, little by, little morsels.|Следующее видео, я вам рассказал, мало-помалу, маленькие кусочки.
Next video, we're gonna go ahead, and talk about the four lower layers.|В следующем видео мы продолжим и поговорим о четырех нижних слоях.
And those are the ones that are called the meat and potatoes.|И это те, которые называются мясом и картошкой.
I'll see you in the next one.|Увидимся в следующем.
[BLANK_AUDIO]|[BLANK_AUDIO]