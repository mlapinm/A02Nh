## Part I Introduction to Networking
Часть I Введение в сеть   
## Chapter 1 Introduction to TCP/IP Networking
Глава 1 Введение в сеть TCP / IP   
__|__
--|--
|
This chapter covers the following exam topics:|В этой главе рассматриваются следующие экзаменационные темы:
###### 1.0 Network Fundamentals
1.0 Основы сети   
###### 1.3 Compare physical interface and cabling types
1.3 Сравните физический интерфейс и типы кабелей   
###### 1.3.a Single-mode fiber, multimode fiber, copper
1.3.a Одномодовое волокно, многомодовое волокно, медь   
###### 1.3.b Connections (Ethernet shared media and point-to-point)
1.3.b Подключения (общая среда Ethernet и точка-точка)   
__|__
--|--
|
Welcome to the first chapter in your study for CCNA! This chapter begins Part I, which focuses on the basics of networking.|Добро пожаловать в первую главу вашего исследования CCNA! Эта глава начинается с части I, в которой основное внимание уделяется основам работы в сети.
|
Networks work correctly because the various devices and software follow the rules.|Сети работают правильно, потому что различные устройства и программное обеспечение подчиняются правилам.
Those rules come in the form of standards and protocols, which are agreements of a particular part of how a network should work.|Эти правила представлены в форме стандартов и протоколов, которые являются соглашениями о том, как должна работать сеть.
However, the sheer number of standards and protocols available can make it difficult for the average network engineer to think about and work with networks—so the world of networking has used several networking models over time.|Однако из-за огромного количества доступных стандартов и протоколов среднему сетевому инженеру сложно думать о сетях и работать с ними, поэтому в мире сетевых технологий с течением времени использовалось несколько сетевых моделей.
|
Networking models define a structure and different categories (layers) of standards and protocols.|Сетевые модели определяют структуру и различные категории (уровни) стандартов и протоколов.
|
As new standards and protocols emerge over time, networkers can think of those new details in the context of a working model.|По мере появления новых стандартов и протоколов сетевики могут рассматривать эти новые детали в контексте работающей модели.
|
You can think of a networking model as you think of a set of architectural plans for building a house.|Вы можете думать о сетевой модели, как о наборе архитектурных планов для строительства дома.
A lot of different people work on building your house, such as framers, electricians, bricklayers, painters, and so on.|Над строительством вашего дома работает множество разных людей, например, строители, электрики, каменщики, маляры и так далее.
The blueprint helps ensure that all the different pieces of the house work together as a whole.|План помогает гарантировать, что все различные части дома работают вместе как единое целое.
Similarly, the people who make networking products, and the people who use those products to build their own computer networks, follow a particular networking model.|Точно так же люди, которые создают сетевые продукты, и люди, которые используют эти продукты для построения своих собственных компьютерных сетей, следуют определенной сетевой модели.
That networking model defines rules about how each part of the network should work, as well as how the parts should work together so that the entire network functions correctly.|Эта сетевая модель определяет правила о том, как должна работать каждая часть сети, а также о том, как части должны работать вместе, чтобы вся сеть функционировала правильно.
|
Today, TCP/IP rules as the most pervasive networking model in use.|Сегодня правила TCP / IP являются наиболее распространенной сетевой моделью.
You can find support for TCP/IP on practically every computer operating system (OS) in existence today, from mobile phones to mainframe computers.|Вы можете найти поддержку TCP / IP практически во всех компьютерных операционных системах (ОС), существующих сегодня, от мобильных телефонов до мэйнфреймов.
Every network built using Cisco products today supports TCP/IP. And not surprisingly, the CCNA exam focuses heavily on TCP/IP. This chapter uses TCP/IP for one of its main purposes: to present various concepts about networking using the context of the different roles and functions in the TCP/IP model.|Каждая сеть, построенная с использованием продуктов Cisco, сегодня поддерживает TCP / IP. И неудивительно, что экзамен CCNA уделяет большое внимание TCP / IP. В этой главе TCP / IP используется для одной из основных целей: представить различные концепции сети с использованием контекста различных ролей и функций в модели TCP / IP.
### “Do I Know This Already?” Quiz
«Знаю ли я это уже?» Викторина   
__|__
--|--
|
Take the quiz (either here or use the PTP software) if you want to use the score to help you decide how much time to spend on this chapter.|Пройдите тест (здесь или воспользуйтесь программой PTP), если вы хотите использовать оценку, чтобы решить, сколько времени потратить на эту главу.
The letter answers are listed at the bottom of the page following the quiz.|Ответы на письма перечислены внизу страницы после викторины.
Appendix C, found both at the end of the book as well as on the companion website, includes both the answers and explanations.|Приложение C, которое можно найти как в конце книги, так и на сопутствующем веб-сайте, включает как ответы, так и пояснения.
You can also find both answers and explanations in the PTP testing software.|Вы также можете найти ответы и пояснения в программе тестирования PTP.
|
CHAPTER 1 Table 1-1 “Do I Know This Already?” Foundation Topics Section-to-Question Mapping|ГЛАВА 1 Таблица 1-1 «Знаю ли я это уже?» Сопоставление разделов с вопросами по основным темам
### Foundation Topics
Основные темы   
### Perspectives on Networking
Перспективы сетевых технологий   
### TCP/IP Networking Model
Модель сети TCP / IP   
__|__
--|--
|
Data Encapsulation Terminology 5–7 1.|Терминология инкапсуляции данных 5–7 1.
Which of the following protocols are examples of TCP/IP transport layer protocols?|Какие из следующих протоколов являются примерами протоколов транспортного уровня TCP / IP?
|
(Choose two answers.)|(Выберите два ответа.)
|
a. Ethernet b.|а. Ethernet б.
HTTP c.|HTTP c.
IP d.|IP d.
UDP e.|UDP e.
SMTP f.|SMTP f.
TCP 2.|TCP 2.
Which of the following protocols are examples of TCP/IP data-link layer protocols?|Какие из следующих протоколов являются примерами протоколов уровня канала передачи данных TCP / IP?
|
(Choose two answers.)|(Выберите два ответа.)
|
a. Ethernet b.|а. Ethernet б.
HTTP c.|HTTP c.
IP d.|IP d.
UDP e.|UDP e.
SMTP f.|SMTP f.
TCP g.|TCP g.
PPP 3.|ГЧП 3.
The process of HTTP asking TCP to send some data and making sure that it is received correctly is an example of what?|Примером чего является процесс HTTP-запроса TCP на отправку некоторых данных и проверки их правильности?
|
a. Same-layer interaction b.|а. Взаимодействие на одном уровне b.
Adjacent-layer interaction c.|Взаимодействие прилегающих слоев c.
OSI model d.|Модель OSI d.
All of these answers are correct.|Все эти ответы верны.
|
4. The process of TCP on one computer marking a TCP segment as segment 1, and the receiving computer then acknowledging the receipt of TCP segment 1 is an example of what?|4. Примером чего является процесс TCP на одном компьютере, помечающий сегмент TCP как сегмент 1, а принимающий компьютер затем подтверждает получение сегмента 1 TCP?
|
a. Data encapsulation b.|а. Инкапсуляция данных b.
Same-layer interaction c.|Взаимодействие на одном уровне c.
Adjacent-layer interaction d.|Взаимодействие соседних слоев d.
OSI model e.|Модель OSI e.
All of these answers are correct.|Все эти ответы верны.
|
5. The process of a web server adding a TCP header to the contents of a web page, followed by adding an IP header and then adding a data-link header and trailer, is an example of what?|5. Примером чего является процесс добавления веб-сервером заголовка TCP к содержимому веб-страницы с последующим добавлением заголовка IP и последующим добавлением заголовка и концевика ссылки на данные?
|
a. Data encapsulation b.|а. Инкапсуляция данных b.
Same-layer interaction c.|Взаимодействие на одном уровне c.
OSI model d.|Модель OSI d.
All of these answers are correct.|Все эти ответы верны.
|
6. Which of the following terms is used specifically to identify the entity created when encapsulating data inside data-link layer headers and trailers?|6. Какой из следующих терминов используется специально для обозначения объекта, созданного при инкапсуляции данных внутри заголовков и трейлеров канального уровня?
|
a. Data b.|а. Данные b.
Chunk c.|Чанк c.
Segment d.|Сегмент d.
Frame e.|Рамка e.
Packet 7.|Пакет 7.
Which OSI encapsulation term can be used instead of the term frame?|Какой термин инкапсуляции OSI можно использовать вместо термина фрейм?
|
a. Layer 1 PDU b.|а. PDU уровня 1 b.
Layer 2 PDU c.|PDU уровня 2 c.
Layer 3 PDU d.|PDU уровня 3 d.
Layer 5 PDU e.|PDU уровня 5 e.
Layer 7 PDU Foundation Topics Perspectives on Networking So, you are new to networking.|Основные темы PDU уровня 7 Перспективы сетевых технологий Итак, вы новичок в сетевых технологиях.
Like many people, your perspective about networks might be that of a user of the network, as opposed to the network engineer who builds networks.|Как и у многих людей, ваше видение сетей может быть взглядом пользователя сети, а не сетевого инженера, который строит сети.
|
For some, your view of networking might be based on how you use the Internet, from home, using a high-speed Internet connection like digital subscriber line (DSL) or cable TV, as shown in Figure 1-1.|Для некоторых ваше представление о сети может быть основано на том, как вы используете Интернет из дома, используя высокоскоростное Интернет-соединение, такое как цифровая абонентская линия (DSL) или кабельное телевидение, как показано на рисунке 1-1.
|
Figure 1-1 End-User Perspective on High-Speed Internet Connections 1 The top part of the figure shows a typical high-speed cable Internet user.|Рисунок 1-1. Взгляд конечного пользователя на высокоскоростное подключение к Интернету 1 В верхней части рисунка показан типичный пользователь высокоскоростного кабельного Интернета.
The PC connects to a cable modem using an Ethernet cable.|ПК подключается к кабельному модему с помощью кабеля Ethernet.
The cable modem then connects to a cable TV (CATV) outlet in the wall using a round coaxial cable—the same kind of cable used to connect your TV to the CATV wall outlet.|Затем кабельный модем подключается к розетке кабельного телевидения (CATV) в стене с помощью круглого коаксиального кабеля - того же типа кабеля, который используется для подключения вашего телевизора к розетке CATV.
Because cable Internet services provide service continuously, the user can just sit down at the PC and start sending email, browsing websites, making Internet phone calls, and using other tools and applications.|Поскольку услуги кабельного Интернета предоставляют услуги непрерывно, пользователь может просто сесть за компьютер и начать отправлять электронную почту, просматривать веб-сайты, совершать телефонные звонки в Интернете и использовать другие инструменты и приложения.
|
The lower part of the figure uses two different technologies.|В нижней части рисунка используются две разные технологии.
First, the tablet computer uses wireless technology that goes by the name wireless local-area network (wireless LAN), or Wi-Fi, instead of using an Ethernet cable.|Во-первых, планшетный компьютер использует беспроводную технологию, известную как беспроводная локальная сеть (беспроводная локальная сеть) или Wi-Fi, вместо использования кабеля Ethernet.
In this example, the router uses a different technology, DSL, to communicate with the Internet.|В этом примере маршрутизатор использует другую технологию, DSL, для связи с Интернетом.
|
Both home-based networks and networks built for use by a company make use of similar networking technologies.|И домашние сети, и сети, созданные для использования компанией, используют аналогичные сетевые технологии.
The Information Technology (IT) world refers to a network created by one corporation, or enterprise, for the purpose of allowing its employees to communicate, as an enterprise network.|Под миром информационных технологий (ИТ) понимается сеть, созданная одной корпорацией или предприятием с целью позволить своим сотрудникам общаться, как корпоративная сеть.
The smaller networks at home, when used for business purposes, often go by the name small office/home office (SOHO) networks.|Домашние сети меньшего размера, когда они используются для деловых целей, часто называются сетями малого офиса / домашнего офиса (SOHO).
|
Users of enterprise networks have some idea about the enterprise network at their company or school.|Пользователи корпоративных сетей имеют некоторое представление о корпоративной сети в своей компании или школе.
People realize that they use a network for many tasks.|Люди понимают, что они используют сеть для множества задач.
PC users might realize that their PC connects through an Ethernet cable to a matching wall outlet, as shown at the top of Figure 1-2.|Пользователи ПК могут понять, что их ПК подключается через кабель Ethernet к соответствующей розетке, как показано в верхней части рисунка 1-2.
Those same users might use wireless LANs with their laptop when going to a meeting in the conference room as well.|Те же пользователи могут использовать беспроводные локальные сети со своим ноутбуком, когда собираются на встречу в конференц-зале.
Figure 1-2 shows these two end-user perspectives on an enterprise network.|На рис. 1-2 показаны эти две точки зрения конечного пользователя в корпоративной сети.
|
Figure 1-2 Example Representation of an Enterprise Network NOTE In networking diagrams, a cloud represents a part of a network whose details are not important to the purpose of the diagram.|Рисунок 1-2 Пример представления корпоративной сети ПРИМЕЧАНИЕ На сетевых диаграммах облако представляет собой часть сети, детали которой не важны для цели диаграммы.
In this case, Figure 1-2 ignores the details of how to create an enterprise network.|В этом случае на рис. 1-2 игнорируются детали того, как создать корпоративную сеть.
|
Some users might not even have a concept of the network at all.|Некоторые пользователи могут вообще не иметь представления о сети.
Instead, these users just enjoy the functions of the network—the ability to post messages to social media sites, make phone calls, search for information on the Internet, listen to music, and download countless apps to their phones—without caring about how it works or how their favorite device connects to the network.|Вместо этого эти пользователи просто наслаждаются функциями сети - возможностью публиковать сообщения в социальных сетях, совершать телефонные звонки, искать информацию в Интернете, слушать музыку и загружать бесчисленные приложения на свои телефоны - не заботясь о том, как это работает или как их любимое устройство подключается к сети.
|
Regardless of how much you already know about how networks work, this book and the related certification help you learn how networks do their job.|Независимо от того, сколько вы уже знаете о том, как работают сети, эта книга и соответствующий сертификат помогут вам узнать, как сети выполняют свою работу.
That job is simply this:|Эта работа проста:
|
moving data from one device to another.|перенос данных с одного устройства на другое.
The rest of this chapter, and the rest of this first part of the book, reveals the basics of how to build enterprise networks so that they can deliver data between two devices.|Остальная часть этой главы и оставшаяся часть этой первой части книги раскрывают основы построения корпоративных сетей, позволяющих передавать данные между двумя устройствами.
|
TCP/IP Networking Model A networking model, sometimes also called either a networking architecture or networking blueprint, refers to a comprehensive set of documents.|Сетевая модель TCP / IP Сетевая модель, иногда также называемая сетевой архитектурой или сетевым планом, относится к исчерпывающему набору документов.
Individually, each document describes one small function required for a network; collectively, these documents define everything that should happen for a computer network to work.|По отдельности каждый документ описывает одну небольшую функцию, необходимую для сети; В совокупности эти документы определяют все, что должно происходить для работы компьютерной сети.
Some documents define a protocol, which is a set of logical rules that devices must follow to communicate.|Некоторые документы определяют протокол, который представляет собой набор логических правил, которым устройства должны следовать для связи.
Other documents define some physical requirements for networking.|В других документах определены некоторые физические требования к сети.
For example, a document could define the voltage and current levels used on a particular cable when transmitting data.|Например, документ может определять уровни напряжения и тока, используемые на конкретном кабеле при передаче данных.
|
You can think of a networking model as you think of an architectural blueprint for building a house.|Вы можете думать о сетевой модели, как об архитектурном проекте для строительства дома.
Sure, you can build a house without the blueprint.|Конечно, вы можете построить дом без чертежа.
However, the blueprint can ensure that the house has the right foundation and structure so that it will not fall down, and it has the correct hidden spaces to accommodate the plumbing, electrical, gas, and so on.|Тем не менее, план может гарантировать, что дом имеет правильный фундамент и структуру, чтобы он не упал, и в нем есть правильные скрытые пространства для размещения водопровода, электричества, газа и т. Д.
Also, the many different people that build the house using the blueprint—such as framers, electricians, bricklayers, painters, and so on—know that if they follow the blueprint, their part of the work should not cause problems for the other workers.|Кроме того, множество разных людей, которые строят дом по чертежу - например, строители, электрики, каменщики, маляры и т. Д. - знают, что, если они следуют плану, их часть работы не должна создавать проблем для других рабочих.
|
Similarly, you could build your own network—write your own software, build your own networking cards, and so on—to create a network.|Точно так же вы можете построить свою собственную сеть - написать собственное программное обеспечение, построить свои собственные сетевые карты и так далее - чтобы создать сеть.
However, it is much easier to simply buy and use products that already conform to some well-known networking model or blueprint.|Однако гораздо проще просто купить и использовать продукты, которые уже соответствуют какой-либо известной сетевой модели или плану.
|
Because the networking product vendors build their products with some networking model in mind, their products should work well together.|Поскольку поставщики сетевых продуктов создают свои продукты с учетом определенной сетевой модели, их продукты должны хорошо работать вместе.
#### History Leading to TCP/IP
История, ведущая к TCP / IP   
__|__
--|--
|
Today, the world of computer networking uses one networking model: TCP/IP. However, the world has not always been so simple.|Сегодня в мире компьютерных сетей используется одна сетевая модель: TCP / IP. Однако мир не всегда был таким простым.
Once upon a time, networking protocols didn’t exist, including TCP/IP. Vendors created the first networking protocols; these protocols supported only that vendor’s computers.|Когда-то не существовало сетевых протоколов, включая TCP / IP. Производители создали первые сетевые протоколы; эти протоколы поддерживают только компьютеры этого производителя.
|
For example, IBM, the computer company with the largest market share in many markets back in the 1970s and 1980s, published its Systems Network Architecture (SNA) networking model in 1974.|Например, IBM, компьютерная компания с самой большой долей рынка на многих рынках в 1970-х и 1980-х годах, опубликовала свою сетевую модель системной сетевой архитектуры (SNA) в 1974 году.
Other vendors also created their own proprietary networking models.|Другие производители также создали свои собственные сетевые модели.
As a result, if your company bought computers from three vendors, network engineers often had to create three different networks based on the networking models created by each company, and then somehow connect those networks, making the combined networks much more complex.|В результате, если ваша компания покупала компьютеры у трех поставщиков, сетевым инженерам часто приходилось создавать три разные сети на основе сетевых моделей, созданных каждой компанией, а затем каким-то образом соединять эти сети, что значительно усложняло объединенные сети.
The left side of Figure 1-3 shows the general idea of what a company’s enterprise network might have looked like back in the 1980s, before TCP/IP became common in enterprise internetworks.|В левой части рисунка 1-3 показано общее представление о том, как могла бы выглядеть корпоративная сеть компании в 1980-х годах, до того, как TCP / IP стал обычным явлением в корпоративных объединенных сетях.
|
Answers to the “Do I Know This Already?” quiz:|Ответы на вопрос «Знаю ли я это уже?» викторина:
|
1 D and F 2 A and G 3 B 4 B 5 A 6 D 7 B.|1 D и F 2 A и G 3 B 4 B 5 A 6 D 7 B.
|
Figure 1-3 Historical Progression: Proprietary Models to the Open TCP/IP Model Although vendor-defined proprietary networking models often worked well, having an open, vendor-neutral networking model would aid competition and reduce complexity.|Рисунок 1-3 Историческое развитие: проприетарные модели к открытой модели TCP / IP Хотя проприетарные сетевые модели, определяемые поставщиком, часто работают хорошо, наличие открытой сетевой модели, не зависящей от поставщика, может способствовать конкуренции и снизить сложность.
|
The International Organization for Standardization (ISO) took on the task to create such a model, starting as early as the late 1970s, beginning work on what would become known as the Open Systems Interconnection (OSI) networking model.|Международная организация по стандартизации (ISO) взяла на себя задачу создать такую ​​модель, начиная с конца 1970-х годов, начав работу над тем, что впоследствии стало известно как сетевая модель взаимодействия открытых систем (OSI).
ISO had a noble goal for the OSI model: to standardize data networking protocols to allow communication among all computers across the entire planet.|ИСО поставила перед моделью OSI благородную цель: стандартизировать сетевые протоколы передачи данных, чтобы обеспечить связь между всеми компьютерами по всей планете.
ISO worked toward this ambitious and noble goal, with participants from most of the technologically developed nations on Earth participating in the process.|ISO работала над достижением этой амбициозной и благородной цели, в этом процессе участвовали участники из большинства технологически развитых стран Земли.
|
A second, less-formal effort to create an open, vendor-neutral, public networking model sprouted forth from a U.S.|Вторая, менее формальная попытка создать открытую, нейтральную по отношению к поставщикам модель общедоступных сетей возникла в США.
Department of Defense (DoD) contract.|Контракт Министерства обороны (DoD).
Researchers at various universities volunteered to help further develop the protocols surrounding the original DoD work.|Исследователи из различных университетов вызвались помочь в дальнейшей разработке протоколов, относящихся к исходной работе Министерства обороны США.
These efforts resulted in a competing open networking model called TCP/IP.|Эти усилия привели к созданию конкурирующей открытой сетевой модели под названием TCP / IP.
|
During the 1990s, companies began adding OSI, TCP/IP, or both to their enterprise networks.|В течение 1990-х годов компании начали добавлять OSI, TCP / IP или и то, и другое в свои корпоративные сети.
|
However, by the end of the 1990s, TCP/IP had become the common choice, and OSI fell away.|Однако к концу 1990-х TCP / IP стал обычным выбором, и OSI отпала.
The center part of Figure 1-3 shows the general idea behind enterprise networks in that decade—still with networks built upon multiple networking models but including TCP/IP.|Центральная часть рисунка 1-3 показывает общую идею корпоративных сетей того десятилетия - сети, построенные на нескольких сетевых моделях, но включающие TCP / IP.
|
Here in the twenty-first century, TCP/IP dominates.|Здесь, в двадцать первом веке, доминирует TCP / IP.
Proprietary networking models still exist, but they have mostly been discarded in favor of TCP/IP. The OSI model, whose development suffered in part because of a slower formal standardization process as compared with TCP/IP, never succeeded in the marketplace.|Проприетарные сетевые модели все еще существуют, но в основном от них отказались в пользу TCP / IP. Модель OSI, развитие которой частично пострадало из-за более медленного формального процесса стандартизации по сравнению с TCP / IP, так и не добилось успеха на рынке.
And TCP/IP, the networking model originally created almost entirely by a bunch of volunteers, has become the most prolific network model ever, as shown on the right side of Figure 1-3.|И TCP / IP, сетевая модель, изначально созданная почти целиком группой добровольцев, стала самой плодотворной сетевой моделью за всю историю, как показано на правой стороне рисунка 1-3.
|
In this chapter, you will read about some of the basics of TCP/IP. Although you will learn some interesting facts about TCP/IP, the true goal of this chapter is to help you understand what a networking model or networking architecture really is and how it works.|В этой главе вы прочитаете о некоторых основах TCP / IP. Хотя вы узнаете некоторые интересные факты о TCP / IP, истинная цель этой главы - помочь вам понять, что на самом деле представляет собой сетевая модель или сетевая архитектура и как она работает.
|
Also in this chapter, you will learn about some of the jargon used with OSI. Will any of you ever work on a computer that is using the full OSI protocols instead of TCP/IP? Probably not.|Также в этой главе вы узнаете о некоторых жаргонах, используемых в OSI. Будет ли кто-нибудь из вас когда-нибудь работать на компьютере, который использует полные протоколы OSI вместо TCP / IP? Возможно нет.
However, you will often use terms relating to OSI.|Однако вы часто будете использовать термины, относящиеся к OSI.
#### Overview of the TCP/IP Networking Model
Обзор сетевой модели TCP / IP   
__|__
--|--
|
The TCP/IP model both defines and references a large collection of protocols that allow computers to communicate.|Модель TCP / IP определяет и ссылается на большой набор протоколов, позволяющих компьютерам обмениваться данными.
To define a protocol, TCP/IP uses documents called Requests For Comments (RFC). (You can find these RFCs using any online search engine.) The TCP/IP model also avoids repeating work already done by some other standards body or vendor consortium by simply referring to standards or protocols created by those groups.|Для определения протокола TCP / IP использует документы, называемые запросами на комментарии (RFC). (Вы можете найти эти RFC с помощью любой поисковой системы в Интернете.) Модель TCP / IP также позволяет избежать повторения работы, уже проделанной другим органом по стандартизации или консорциумом поставщиков, просто ссылаясь на стандарты или протоколы, созданные этими группами.
For example, the Institute of Electrical and Electronic Engineers (IEEE) defines Ethernet LANs; the TCP/IP model does not define Ethernet in RFCs, but refers to IEEE Ethernet as an option.|Например, Институт инженеров по электротехнике и электронике (IEEE) определяет локальные сети Ethernet; модель TCP / IP не определяет Ethernet в RFC, но в качестве опции ссылается на IEEE Ethernet.
|
The TCP/IP model creates a set of rules that allows us all to take a computer (or mobile device) out of the box, plug in all the right cables, turn it on, and connect to and use the network.|Модель TCP / IP создает набор правил, который позволяет всем нам вынуть компьютер (или мобильное устройство) из коробки, подключить все нужные кабели, включить его, подключиться к сети и использовать ее.
You can use a web browser to connect to your favorite website, use most any app, and it all works.|Вы можете использовать веб-браузер для подключения к любимому веб-сайту, использовать практически любое приложение, и все это работает.
How?|Как?
Well, the OS on the computer implements parts of the TCP/IP model.|Что ж, ОС на компьютере реализует части модели TCP / IP.
|
The Ethernet card, or wireless LAN card, built in to the computer implements some LAN standards referenced by the TCP/IP model.|Карта Ethernet или карта беспроводной локальной сети, встроенная в компьютер, реализует некоторые стандарты локальной сети, на которые ссылается модель TCP / IP.
In short, the vendors that created the hardware and software implemented TCP/IP.|Короче говоря, поставщики, создавшие аппаратное и программное обеспечение, реализовали TCP / IP.
|
To help people understand a networking model, each model breaks the functions into a small number of categories called layers.|Чтобы помочь людям понять сетевую модель, каждая модель разбивает функции на небольшое количество категорий, называемых уровнями.
Each layer includes protocols and standards that relate to that category of functions, as shown in Figure 1-4.|Каждый уровень включает протоколы и стандарты, относящиеся к этой категории функций, как показано на рисунке 1-4.
|
Figure 1-4 The TCP/IP Networking Models The TCP/IP model shows the more common terms and layers used when people talk about TCP/IP today.|Рисунок 1-4. Сетевые модели TCP / IP Модель TCP / IP показывает наиболее общие термины и уровни, которые сегодня используются, когда люди говорят о TCP / IP.
The bottom layer focuses on how to transmit bits over each individual link.|Нижний уровень фокусируется на том, как передавать биты по каждому отдельному каналу.
|
The data-link layer focuses on sending data over one type of physical link: for instance, networks use different data-link protocols for Ethernet LANs versus wireless LANs. The network layer focuses on delivering data over the entire path from the original sending computer to the final destination computer.|Уровень канала передачи данных ориентирован на отправку данных по одному типу физического канала: например, сети используют разные протоколы канала передачи данных для локальных сетей Ethernet по сравнению с беспроводными локальными сетями. Сетевой уровень ориентирован на доставку данных по всему пути от исходного компьютера-отправителя до конечного компьютера-получателя.
And the top two layers focus more on the applications that need to send and receive data.|И два верхних уровня больше ориентированы на приложения, которым необходимо отправлять и получать данные.
|
NOTE A slightly different four-layer original version of the TCP/IP model exists in RFC 1122, but for the purposes of both real networking and for today’s CCNA, use the five-layer model shown here in Figure 1-4.|ПРИМЕЧАНИЕ. Немного отличная четырехуровневая исходная версия модели TCP / IP существует в RFC 1122, но как для реальных сетей, так и для сегодняшней CCNA, используйте пятиуровневую модель, показанную здесь на рисунке 1-4.
|
Many of you will have already heard of several TCP/IP protocols, like the examples listed in Table 1-2.|Многие из вас уже слышали о нескольких протоколах TCP / IP, например о примерах, перечисленных в Таблице 1-2.
Most of the protocols and standards in this table will be explained in more detail as you work through this book.|Большинство протоколов и стандартов в этой таблице будут объяснены более подробно по мере работы с этой книгой.
Following the table, this section takes a closer look at the layers of the TCP/IP model.|Следуя таблице, в этом разделе более подробно рассматриваются уровни модели TCP / IP.
|
1 Table 1-2 TCP/IP Architectural Model and Example Protocols Table end.|1 Таблица 1-2 Архитектурная модель TCP / IP и примеры протоколов Окончание таблицы.
#### TCP/IP Application Layer
Уровень приложений TCP / IP   
__|__
--|--
|
TCP/IP application layer protocols provide services to the application software running on a computer.|Протоколы прикладного уровня TCP / IP предоставляют услуги прикладному программному обеспечению, работающему на компьютере.
The application layer does not define the application itself, but it defines services that applications need.|Уровень приложения не определяет само приложение, но определяет службы, которые необходимы приложениям.
For example, application protocol HTTP defines how web browsers can pull the contents of a web page from a web server.|Например, протокол приложения HTTP определяет, как веб-браузеры могут извлекать содержимое веб-страницы с веб-сервера.
In short, the application layer provides an interface between software running on a computer and the network itself.|Короче говоря, уровень приложений обеспечивает интерфейс между программным обеспечением, работающим на компьютере, и самой сетью.
|
Arguably, the most popular TCP/IP application today is the web browser.|Пожалуй, самым популярным приложением TCP / IP сегодня является веб-браузер.
Many major software vendors either have already changed or are changing their application software to support access from a web browser.|Многие крупные поставщики программного обеспечения либо уже изменили, либо меняют свое прикладное программное обеспечение для поддержки доступа через веб-браузер.
And thankfully, using a web browser is easy: You start a web browser on your computer and select a website by typing the name of the website, and the web page appears.|И, к счастью, использовать веб-браузер очень просто: вы запускаете веб-браузер на своем компьютере и выбираете веб-сайт, вводя имя веб-сайта, и появляется веб-страница.
##### HTTP Overview
Обзор HTTP   
__|__
--|--
|
What really happens to allow that web page to appear on your web browser?|Что на самом деле происходит, чтобы эта веб-страница отображалась в вашем браузере?
|
Imagine that Bob opens his browser.|Представьте, что Боб открывает свой браузер.
His browser has been configured to automatically ask for web server Larry’s default web page, or home page.|Его браузер был настроен так, чтобы автоматически запрашивать веб-страницу Ларри по умолчанию или домашнюю страницу.
The general logic looks like Figure 1-5.|Общая логика выглядит как рисунок 1-5.
|
Figure 1-5 Basic Application Logic to Get a Web Page So, what really happened?|Рис. 1-5 Базовая логика приложения для получения веб-страницы Итак, что же произошло на самом деле?
Bob’s initial request actually asks Larry to send his home page back to Bob.|Первоначальный запрос Боба на самом деле просит Ларри отправить его домашнюю страницу обратно Бобу.
Larry’s web server software has been configured to know that the default web page is contained in a file called home.htm.|Программное обеспечение веб-сервера Ларри настроено так, чтобы знать, что веб-страница по умолчанию содержится в файле с именем home.htm.
Bob receives the file from Larry and displays the contents of the file in Bob’s web browser window.|Боб получает файл от Ларри и отображает содержимое файла в окне веб-браузера Боба.
##### HTTP Protocol Mechanisms
Механизмы протокола HTTP   
__|__
--|--
|
Taking a closer look, this example shows how applications on each endpoint computer—specifically, the web browser application and web server application—use a TCP/IP application layer protocol.|При более внимательном рассмотрении этот пример показывает, как приложения на каждом конечном компьютере - в частности, приложение веб-браузера и приложение веб-сервера - используют протокол уровня приложений TCP / IP.
To make the request for a web page and return the contents of the web page, the applications use the Hypertext Transfer Protocol (HTTP).|Чтобы сделать запрос на веб-страницу и вернуть ее содержимое, приложения используют протокол передачи гипертекста (HTTP).
|
HTTP did not exist until Tim Berners-Lee created the first web browser and web server in the early 1990s.|HTTP не существовал до тех пор, пока Тим Бернерс-Ли не создал первый веб-браузер и веб-сервер в начале 1990-х годов.
Berners-Lee gave HTTP functionality to ask for the contents of web pages, specifically by giving the web browser the ability to request files from the server and giving the server a way to return the content of those files.|Бернерс-Ли предоставил функцию HTTP для запроса содержимого веб-страниц, в частности, предоставив веб-браузеру возможность запрашивать файлы с сервера и предоставив серверу возможность возвращать содержимое этих файлов.
The overall logic matches what was shown in Figure 1-5; Figure 1-6 shows the same idea, but with details specific to HTTP.|Общая логика соответствует тому, что показано на рис. 1-5; На рис. 1-6 показана та же идея, но с подробностями, относящимися к HTTP.
|
NOTE The full version of most web addresses—also called Uniform Resource Locators (URL) or Universal Resource Identifiers (URI)—begins with the letters http, which means that HTTP is used to transfer the web pages.|ПРИМЕЧАНИЕ. Полная версия большинства веб-адресов, также называемых унифицированными указателями ресурсов (URL) или универсальными идентификаторами ресурсов (URI), начинается с букв http, что означает, что HTTP используется для передачи веб-страниц.
|
Figure 1-6 HTTP GET Request, HTTP Reply, and One Data-Only Message To get the web page from Larry, at Step 1, Bob sends a message with an HTTP header.|Рисунок 1-6. HTTP-запрос GET, HTTP-ответ и одно сообщение только с данными. Чтобы получить веб-страницу от Ларри, на шаге 1 Боб отправляет сообщение с HTTP-заголовком.
|
Generally, protocols use headers as a place to put information used by that protocol.|Обычно протоколы используют заголовки как место для размещения информации, используемой этим протоколом.
This HTTP header includes the request to “get” a file.|Этот HTTP-заголовок включает запрос на «получение» файла.
The request typically contains the name of the file (home.htm, in this case), or if no filename is mentioned, the web server assumes that Bob wants the default web page.|Запрос обычно содержит имя файла (в данном случае home.htm) или, если имя файла не упоминается, веб-сервер предполагает, что Бобу нужна веб-страница по умолчанию.
|
Step 2 in Figure 1-6 shows the response from web server Larry.|Шаг 2 на рис. 1-6 показывает ответ веб-сервера Ларри.
The message begins with an HTTP header, with a return code (200), which means something as simple as “OK” returned in the header.|Сообщение начинается с HTTP-заголовка с кодом возврата (200), что означает что-то очень простое, например «ОК», возвращаемое в заголовке.
HTTP also defines other return codes so that the server can tell the browser whether the request worked. (Here is another example: If you ever looked for a web page that was not found, and then received an HTTP 404 “not found” error, you received an HTTP return code of 404.) The second message also includes the first part of the requested file.|HTTP также определяет другие коды возврата, чтобы сервер мог сообщить браузеру, сработал ли запрос. (Вот еще один пример: если вы когда-либо искали веб-страницу, которая не была найдена, а затем получили ошибку HTTP 404 «не найден», вы получили код возврата HTTP 404.) Второе сообщение также включает первую часть запрошенный файл.
|
Step 3 in Figure 1-6 shows another message from web server Larry to web browser Bob, but this time without an HTTP header.|Шаг 3 на рис. 1-6 показывает другое сообщение от веб-сервера Ларри веб-браузеру Бобу, но на этот раз без HTTP-заголовка.
HTTP transfers the data by sending multiple messages, each with a part of the file.|HTTP передает данные, отправляя несколько сообщений, каждое с частью файла.
Rather than wasting space by sending repeated HTTP headers that list the same information, these additional messages simply omit the header.|Вместо того, чтобы тратить место на отправку повторяющихся заголовков HTTP, содержащих ту же информацию, эти дополнительные сообщения просто опускают заголовок.
#### TCP/IP Transport Layer
Транспортный уровень TCP / IP   
__|__
--|--
|
Although many TCP/IP application layer protocols exist, the TCP/IP transport layer includes a smaller number of protocols.|Хотя существует множество протоколов прикладного уровня TCP / IP, транспортный уровень TCP / IP включает меньшее количество протоколов.
The two most commonly used transport layer protocols are the Transmission Control Protocol (TCP) and the User Datagram Protocol (UDP).|Два наиболее часто используемых протокола транспортного уровня - это протокол управления передачей (TCP) и протокол пользовательских дейтаграмм (UDP).
|
Transport layer protocols provide services to the application layer protocols that reside one layer higher in the TCP/IP model.|Протоколы транспортного уровня предоставляют услуги протоколам прикладного уровня, которые находятся на один уровень выше в модели TCP / IP.
How does a transport layer protocol provide a service to a higher-layer protocol?|Как протокол транспортного уровня предоставляет услуги протоколу более высокого уровня?
This section introduces that general concept by focusing on a single 2, includes a chapter, “Introduction to TCP/IP Transport and Applications,” which examines the transport layer.|Этот раздел вводит эту общую концепцию, сосредоточив внимание на одном 2, включает главу «Введение в транспорт и приложения TCP / IP», в которой исследуется транспортный уровень.
|
1|1
##### TCP Error Recovery Basics
Основы восстановления после ошибок TCP   
__|__
--|--
|
To appreciate what the transport layer protocols do, you must think about the layer above the transport layer, the application layer.|Чтобы понять, что делают протоколы транспортного уровня, вы должны подумать об уровне выше транспортного уровня, о прикладном уровне.
Why?|Зачем?
Well, each layer provides a service to the layer above it, like the error-recovery service provided to application layer protocols by TCP.|Что ж, каждый уровень предоставляет услугу вышестоящему уровню, подобно сервису исправления ошибок, предоставляемому протоколам прикладного уровня TCP.
|
For example, in Figure 1-5, Bob and Larry used HTTP to transfer the home page from web server Larry to Bob’s web browser.|Например, на рис. 1-5 Боб и Ларри использовали HTTP для передачи домашней страницы с веб-сервера Ларри в веб-браузер Боба.
But what would have happened if Bob’s HTTP GET request had been lost in transit through the TCP/IP network?|Но что бы произошло, если бы HTTP-запрос Боба GET был потерян при передаче через сеть TCP / IP?
Or, what would have happened if Larry’s response, which included the contents of the home page, had been lost?|Или что бы произошло, если бы ответ Ларри, который включал содержание домашней страницы, был утерян?
Well, as you might expect, in either case, the page would not have shown up in Bob’s browser.|Что ж, как и следовало ожидать, в любом случае страница не отобразилась бы в браузере Боба.
|
TCP/IP needs a mechanism to guarantee delivery of data across a network.|TCP / IP нуждается в механизме, гарантирующем доставку данных по сети.
Because many application layer protocols probably want a way to guarantee delivery of data across a network, the creators of TCP included an error-recovery feature.|Поскольку многим протоколам прикладного уровня, вероятно, нужен способ гарантировать доставку данных по сети, создатели TCP включили функцию восстановления после ошибок.
To recover from errors, TCP uses the concept of acknowledgments.|Для восстановления после ошибок TCP использует концепцию подтверждений.
Figure 1-7 outlines the basic idea behind how TCP notices lost data and asks the sender to try again.|На рис. 1-7 представлена ​​основная идея того, как TCP обнаруживает потерянные данные и просит отправителя повторить попытку.
|
Figure 1-7 TCP Error-Recovery Services as Provided to HTTP Figure 1-7 shows web server Larry sending a web page to web browser Bob, using three separate messages.|Рис. 1-7. Службы восстановления после ошибок TCP, предоставляемые HTTP. На рис. 1-7 показан веб-сервер Ларри, отправляющий веб-страницу веб-браузеру Бобу, используя три отдельных сообщения.
Note that this figure shows the same HTTP headers as Figure 1-6, but it also shows a TCP header.|Обратите внимание, что на этом рисунке показаны те же заголовки HTTP, что и на рисунке 1-6, но также показан заголовок TCP.
The TCP header shows a sequence number (SEQ) with each message.|Заголовок TCP показывает порядковый номер (SEQ) каждого сообщения.
In this example, the network has a problem, and the network fails to deliver the TCP message (called a segment) with sequence number 2.|В этом примере в сети возникла проблема, и сеть не может доставить TCP-сообщение (называемое сегментом) с порядковым номером 2.
When Bob receives messages with sequence numbers 1 and 3, but does not receive a message with sequence number 2, Bob realizes that message 2 was lost.|Когда Боб получает сообщения с порядковыми номерами 1 и 3, но не получает сообщения с порядковыми номерами 2, Боб понимает, что сообщение 2 было потеряно.
That realization by Bob’s TCP logic causes Bob to send a TCP segment back to Larry, asking Larry to send message 2 again.|Эта реализация логикой TCP Боба заставляет Боба отправить сегмент TCP обратно Ларри, прося Ларри снова отправить сообщение 2.
##### Same-Layer and Adjacent-Layer Interactions
Взаимодействие на одном и том же уровне и на смежном уровне   
__|__
--|--
|
Figure 1-7 also demonstrates a function called adjacent-layer interaction, which refers to the concepts of how adjacent layers in a networking model, on the same computer, work together.|На рисунке 1-7 также показана функция, называемая взаимодействием смежных уровней, которая относится к концепциям того, как смежные уровни в сетевой модели на одном компьютере работают вместе.
In this example, the higher-layer protocol (HTTP) wants error recovery, so it uses the next lower-layer protocol (TCP) to perform the service of error recovery; the lower layer provides a service to the layer above it.|В этом примере протокол верхнего уровня (HTTP) требует восстановления после ошибок, поэтому он использует следующий протокол нижнего уровня (TCP) для выполнения услуги восстановления после ошибок; нижний уровень обслуживает более высокий уровень.
|
Figure 1-7 also shows an example of a similar function called same-layer interaction.|На рис. 1-7 также показан пример аналогичной функции, называемой взаимодействием на одном уровне.
|
When a particular layer on one computer wants to communicate with the same layer on another computer, the two computers use headers to hold the information that they want to communicate.|Когда определенный уровень на одном компьютере хочет взаимодействовать с тем же уровнем на другом компьютере, два компьютера используют заголовки для хранения информации, которую они хотят передать.
For example, in Figure 1-7, Larry set the sequence numbers to 1, 2, and 3 so that Bob could notice when some of the data did not arrive.|Например, на рисунке 1-7 Ларри установил порядковые номера на 1, 2 и 3, чтобы Боб мог заметить, когда некоторые данные не поступают.
Larry’s TCP process created that TCP header with the sequence number; Bob’s TCP process received and reacted to the TCP segments.|Процесс TCP Ларри создал этот заголовок TCP с порядковым номером; Процесс TCP Боба получил и отреагировал на сегменты TCP.
|
Table 1-3 summarizes the key points about how adjacent layers work together on a single computer and how one layer on one computer works with the same networking layer on another computer.|В Таблице 1-3 обобщены ключевые моменты того, как смежные уровни работают вместе на одном компьютере и как один уровень на одном компьютере работает с одним и тем же сетевым уровнем на другом компьютере.
|
Table 1-3 Summary: Same-Layer and Adjacent-Layer Interactions Table end.|Таблица 1-3 Сводка: Взаимодействие на одном и том же и прилегающем уровнях Конец таблицы.
#### TCP/IP Network Layer
Сетевой уровень TCP / IP   
__|__
--|--
|
The application layer includes many protocols.|Уровень приложений включает в себя множество протоколов.
The transport layer includes fewer protocols, most notably, TCP and UDP. The TCP/IP network layer includes a small number of protocols, but only one major protocol: the Internet Protocol (IP). In fact, the name TCP/IP is simply the names of the two most common protocols (TCP and IP) separated by a /.|Транспортный уровень включает меньше протоколов, в первую очередь TCP и UDP. Сетевой уровень TCP / IP включает небольшое количество протоколов, но только один основной протокол: Интернет-протокол (IP). Фактически, имя TCP / IP - это просто имена двух наиболее распространенных протоколов (TCP и IP), разделенные знаком /.
|
IP provides several features, most importantly, addressing and routing.|IP предоставляет несколько функций, в первую очередь адресацию и маршрутизацию.
This section begins by comparing IP’s addressing and routing with another commonly known system that uses addressing and routing: the postal service.|Этот раздел начинается со сравнения IP-адресации и маршрутизации с другой широко известной системой, использующей адресацию и маршрутизацию: почтовой службой.
Following that, this section introduces IP addressing and routing. (More details follow in Chapter 3, “Fundamentals of WANs and IP Routing.”)|После этого в этом разделе рассказывается об IP-адресации и маршрутизации. (Более подробная информация представлена ​​в главе 3 «Основы WAN и IP-маршрутизации».)
##### Internet Protocol and the Postal Service
Интернет-протокол и почтовая служба   
__|__
--|--
|
Imagine that you just wrote two letters: one to a friend on the other side of the country and one to a friend on the other side of town.|Представьте, что вы только что написали два письма: одно другу на другом конце страны и одно другу на другом конце города.
You addressed the envelopes and put on the stamps, so both are ready to give to the postal service.|Вы адресовали конверты и ставили марки, так что оба готовы отдать на почту.
Is there much difference in how you treat each letter?|Есть ли разница в том, как вы относитесь к каждой букве?
Not really.|На самом деле, нет.
Typically, you would just put them in the same mailbox and expect the postal service to deliver both letters.|Обычно вы просто кладете их в один почтовый ящик и ожидаете, что почтовая служба доставит оба письма.
|
The postal service, however, must think about each letter separately, and then make a decision of where to send each letter so that it is delivered.|Почтовая служба, однако, должна думать о каждом письме отдельно, а затем принимать решение о том, куда отправить каждое письмо, чтобы оно было доставлено.
For the letter sent across town, the people in the local post office probably just need to put the letter on another truck.|Что касается письма, отправленного через город, людям в местном почтовом отделении, вероятно, нужно просто положить письмо в другой грузовик.
|
For the letter that needs to go across the country, the postal service sends the letter to another post office, then another, and so on, until the letter gets delivered across the country.|Для письма, которое необходимо пересечь страну, почтовая служба отправляет письмо в другое почтовое отделение, затем в другое и так далее, пока письмо не будет доставлено по всей стране.
At each post office, the postal service must process the letter and choose where to send it next.|В каждом почтовом отделении почтовая служба должна обработать письмо и выбрать, куда его отправить дальше.
|
To make it all work, the postal service has regular routes for small trucks, large trucks, planes, boats, and so on, to move letters between postal service sites.|Чтобы все это работало, у почтовой службы есть регулярные маршруты для небольших грузовиков, больших грузовиков, самолетов, лодок и т. Д. Для перемещения писем между сайтами почтовых служб.
The service must be able to receive and forward the letters, and it must make good decisions about where to send each letter next, as shown in Figure 1-8.|Служба должна иметь возможность получать и пересылать письма, и она должна принимать правильные решения о том, куда отправлять каждое письмо в следующий раз, как показано на рисунке 1-8.
|
Figure 1-8 Postal Service Forwarding (Routing) Letters Still thinking about the postal service, consider the difference between the person sending the letter and the work that the postal service does.|Рис. 1-8. Пересылка (маршрутизация) писем почтовой службой. Продолжая думать о почтовой службе, рассмотрите разницу между человеком, отправляющим письмо, и работой, которую выполняет почтовая служба.
The person sending the letters expects that the postal service will deliver the letter most of the time.|Человек, отправляющий письма, ожидает, что почтовая служба будет доставить письмо большую часть времени.
However, the person sending the letter does not need to know the details of exactly what path the letters take.|Однако человеку, отправляющему письмо, необязательно знать подробности того, по какому пути идут письма.
In contrast, the postal service does not create the letter, but it accepts the letter from the customer.|Почтовая служба, напротив, не создает письмо, но принимает письмо от клиента.
|
Then, the postal service must know the details about addresses and postal codes that group addresses into larger groups, and it must have the ability to deliver the letters.|Затем почтовая служба должна знать подробности об адресах и почтовых индексах, которые объединяют адреса в более крупные группы, и иметь возможность доставлять письма.
|
The TCP/IP application and transport layers act like the person sending letters through the postal service.|Приложение TCP / IP и транспортный уровень действуют как человек, отправляющий письма через почтовую службу.
These upper layers work the same way regardless of whether the endpoint host computers are on the same LAN or are separated by the entire Internet.|Эти верхние уровни работают одинаково независимо от того, находятся ли хост-компьютеры конечных точек в одной локальной сети или разделены всем Интернетом.
To send a message, these upper layers ask the layer below them, the network layer, to deliver the message.|Чтобы отправить сообщение, эти верхние уровни запрашивают уровень ниже, сетевой уровень, чтобы доставить сообщение.
|
The lower layers of the TCP/IP model act more like the postal service to deliver those messages to the correct destinations.|Нижние уровни модели TCP / IP действуют больше как почтовая служба, доставляя эти сообщения по правильным адресатам.
To do so, these lower layers must understand the underlying physical network because they must choose how to best deliver the data from one host to another.|Для этого эти нижние уровни должны понимать базовую физическую сеть, поскольку они должны выбирать, как лучше всего доставлять данные от одного хоста к другому.
|
So, what does this all matter to networking?|Итак, какое все это имеет значение для сетей?
Well, the network layer of the TCP/IP networking model, primarily defined by the Internet Protocol (IP), works much like the postal service.|Что ж, сетевой уровень сетевой модели TCP / IP, в первую очередь определяемый Интернет-протоколом (IP), работает во многом как почтовая служба.
|
IP defines that each host computer should have a different IP address, just as the postal service defines addressing that allows unique addresses for each house, apartment, and business.|IP определяет, что каждый хост-компьютер должен иметь другой IP-адрес, так же как почтовая служба определяет адресацию, которая позволяет использовать уникальные адреса для каждого дома, квартиры или предприятия.
|
Similarly, IP defines the process of routing so that devices called routers can work like the post office, forwarding packets of data so that they are delivered to the correct destinations.|Точно так же IP определяет процесс маршрутизации, так что устройства, называемые маршрутизаторами, могут работать как почтовое отделение, пересылая пакеты данных, чтобы они доставлялись в правильные места назначения.
|
Just as the postal service created the necessary infrastructure to deliver letters—post offices, sorting machines, trucks, planes, and personnel—the network layer defines the details of how a network infrastructure should be created so that the network can deliver data to all computers in the network.|Подобно тому, как почтовая служба создала необходимую инфраструктуру для доставки писем - почтовые отделения, сортировочные машины, грузовики, самолеты и персонал, - сетевой уровень определяет детали того, как должна быть создана сетевая инфраструктура, чтобы сеть могла доставлять данные на все компьютеры. в сети.
##### Internet Protocol Addressing Basics
Основы адресации интернет-протокола   
__|__
--|--
|
IP defines addresses for several important reasons.|IP определяет адреса по нескольким важным причинам.
First, each device that uses TCP/IP—each TCP/IP host—needs a unique address so that it can be identified in the network.|Во-первых, каждому устройству, использующему TCP / IP - каждому узлу TCP / IP - нужен уникальный адрес, чтобы его можно было идентифицировать в сети.
IP also defines how to group addresses together, just like the postal system groups addresses based on postal codes (like ZIP codes in the United States).|IP также определяет, как группировать адреса вместе, точно так же, как почтовая система группирует адреса на основе почтовых индексов (например, почтовые индексы в США).
|
To understand the basics, examine Figure 1-9, which shows the familiar web server Larry and web browser Bob; but now, instead of ignoring the network between these two computers, part of the network infrastructure is included.|Чтобы понять основы, изучите рисунок 1-9, на котором показаны знакомый веб-сервер Ларри и веб-браузер Боб; но теперь, вместо того, чтобы игнорировать сеть между этими двумя компьютерами, включена часть сетевой инфраструктуры.
|
Figure 1-9 Simple TCP/IP Network: Three Routers with IP Addresses Grouped First, note that Figure 1-9 shows some sample IP addresses.|Рисунок 1-9 Простая сеть TCP / IP: сначала сгруппированы три маршрутизатора с IP-адресами, обратите внимание, что на Рисунке 1-9 показаны некоторые примеры IP-адресов.
Each IP address has four numbers, separated by periods.|Каждый IP-адрес имеет четыре числа, разделенных точками.
In this case, Larry uses IP address 1.1.1.1, and Bob uses 2.2.2.2.|В этом случае Ларри использует IP-адрес 1.1.1.1, а Боб - 2.2.2.2.
|
This style of number is called a dotted-decimal notation (DDN).|Этот стиль чисел называется десятичной системой с разделительными точками (DDN).
|
Figure 1-9 also shows three groups of addresses.|На рисунке 1-9 также показаны три группы адресов.
In this example, all IP addresses that begin with 1 must be on the upper left, as shown in shorthand in the figure as 1.__.__.__.|В этом примере все IP-адреса, начинающиеся с 1, должны находиться в верхнем левом углу, как показано в сокращении на рисунке как 1 .__.__.__.
|
All addresses that begin with 2 must be on the right, as shown in shorthand as 2.__.__.__.|Все адреса, начинающиеся с 2, должны быть справа, как показано в сокращении как 2 .__.__.__.
|
Finally, all IP addresses that begin with 3 must be at the bottom of the figure.|Наконец, все IP-адреса, начинающиеся с 3, должны быть внизу рисунка.
|
In addition, Figure 1-9 introduces icons that represent IP routers.|Кроме того, на рис. 1-9 представлены значки, представляющие IP-маршрутизаторы.
Routers are networking devices that connect the parts of the TCP/IP network together for the purpose of routing (forwarding) IP packets to the correct destination.|Маршрутизаторы - это сетевые устройства, которые соединяют части сети TCP / IP вместе с целью маршрутизации (пересылки) IP-пакетов в правильное место назначения.
Routers do the equivalent of the work done by each post office site: They receive IP packets on various physical interfaces, make decisions based on the IP address included with the packet, and then physically forward the packet out some other network interface.|Маршрутизаторы выполняют эквивалент работы, выполняемой каждым узлом почтового отделения: они получают IP-пакеты на различных физических интерфейсах, принимают решения на основе IP-адреса, включенного в пакет, а затем физически пересылают пакет через какой-либо другой сетевой интерфейс.
##### IP Routing Basics
Основы IP-маршрутизации   
__|__
--|--
|
The TCP/IP network layer, using the IP protocol, provides a service of forwarding IP packets from one device to another.|Сетевой уровень TCP / IP, использующий протокол IP, предоставляет услугу пересылки IP-пакетов от одного устройства к другому.
Any device with an IP address can connect to the TCP/IP network and send packets.|Любое устройство с IP-адресом может подключаться к сети TCP / IP и отправлять пакеты.
This section shows a basic IP routing example for perspective.|В этом разделе для перспективы показан базовый пример IP-маршрутизации.
|
NOTE The term IP host refers to any device, regardless of size or power, that has an IP address and connects to any TCP/IP network.|ПРИМЕЧАНИЕ Термин IP-хост относится к любому устройству, независимо от размера или мощности, которое имеет IP-адрес и подключается к любой сети TCP / IP.
|
Figure 1-10 repeats the familiar case in which web server Larry wants to send part of a web page to Bob, but now with details related to IP. On the lower left, note that server Larry has the familiar application data, HTTP header, and TCP header ready to send.|На рис. 1-10 повторяется знакомый случай, когда веб-сервер Ларри хочет отправить часть веб-страницы Бобу, но теперь с деталями, связанными с IP. В левом нижнем углу обратите внимание, что на сервере Ларри есть уже знакомые данные приложения, заголовок HTTP и заголовок TCP, готовые к отправке.
In addition, the message now contains an IP header.|Кроме того, сообщение теперь содержит заголовок IP.
The IP header includes a source IP address of Larry’s IP address (1.1.1.1) and a destination IP address of Bob’s IP address (2.2.2.2).|Заголовок IP включает в себя исходный IP-адрес IP-адреса Ларри (1.1.1.1) и IP-адрес назначения IP-адреса Боба (2.2.2.2).
|
Figure 1-10 Basic Routing Example Step 1, on the left of Figure 1-10, begins with Larry being ready to send an IP packet.|Рисунок 1-10. Базовый пример маршрутизации Шаг 1 слева на рисунке 1-10 начинается с того, что Ларри готов отправить IP-пакет.
|
Larry’s IP process chooses to send the packet to some router—a nearby router on the same LAN—with the expectation that the router will know how to forward the packet. (This logic is much like you or me sending all our letters by putting them in a nearby mailbox.) Larry doesn’t need to know anything more about the topology or the other routers.|IP-процесс Ларри решает отправить пакет на какой-то маршрутизатор - ближайший маршрутизатор в той же локальной сети, - ожидая, что маршрутизатор будет знать, как пересылать пакет. (Эта логика очень похожа на то, как мы с вами отправляем все наши письма, складывая их в ближайший почтовый ящик.) Ларри не нужно больше ничего знать о топологии или других маршрутизаторах.
|
At Step 2, Router R1 receives the IP packet, and R1’s IP process makes a decision.|На шаге 2 маршрутизатор R1 получает IP-пакет, а IP-процесс R1 принимает решение.
R1 looks at the destination address (2.2.2.2), compares that address to its known IP routes, and chooses to forward the packet to Router R2. This process of forwarding the IP packet is called IP routing (or simply routing).|R1 смотрит на адрес назначения (2.2.2.2), сравнивает этот адрес со своими известными IP-маршрутами и выбирает пересылку пакета на маршрутизатор R2. Этот процесс пересылки IP-пакета называется IP-маршрутизацией (или просто маршрутизацией).
|
At Step 3, Router R2 repeats the same kind of logic used by Router R1. R2’s IP process will compare the packet’s destination IP address (2.2.2.2) to R2’s known IP routes and make a choice to forward the packet to the right, on to Bob.|На шаге 3 маршрутизатор R2 повторяет ту же логику, что и маршрутизатор R1. IP-процесс R2 сравнивает IP-адрес назначения пакета (2.2.2.2) с известными IP-маршрутами R2 и выбирает пересылку пакета направо, Бобу.
|
You will learn IP in more depth than any other protocol while preparing for CCNA. More than half the chapters in this book discuss some feature that relates to addressing, IP routing, and how routers perform routing.|Вы изучите IP глубже, чем любой другой протокол, при подготовке к CCNA. Более чем в половине глав этой книги обсуждаются некоторые особенности, связанные с адресацией, IP-маршрутизацией и тем, как маршрутизаторы выполняют маршрутизацию.
#### TCP/IP Data-Link and Physical Layers
Канал передачи данных TCP / IP и физические уровни   
__|__
--|--
|
The TCP/IP model’s data-link and physical layers define the protocols and hardware required to deliver data across some physical network.|Канальный и физический уровни модели TCP / IP определяют протоколы и оборудование, необходимые для доставки данных по какой-либо физической сети.
The two work together quite closely; in fact, some standards define both the data-link and physical layer functions.|Эти двое работают вместе довольно тесно; фактически, некоторые стандарты определяют функции как канала передачи данных, так и физического уровня.
The physical layer defines the cabling and energy (for example, electrical signals) that flow over the cables.|Физический уровень определяет кабели и энергию (например, электрические сигналы), которые проходят по кабелям.
|
Some rules and conventions exist when sending data over the cable; however, those rules exist in the data-link layer of the TCP/IP model.|При передаче данных по кабелю существуют некоторые правила и соглашения; однако эти правила существуют на канальном уровне модели TCP / IP.
|
Focusing on the data-link layer for a moment, just like every layer in any networking model, the TCP/IP data-link layer provides services to the layer above it in the model (the network layer).|Сосредоточившись на уровне канала передачи данных на мгновение, как и каждый уровень в любой сетевой модели, уровень канала передачи данных TCP / IP предоставляет услуги вышестоящему уровню модели (сетевой уровень).
When a host’s or router’s IP process chooses to send an IP packet to another router or host, that host or router then uses link-layer details to send that packet to the next host/|Когда IP-процесс хоста или маршрутизатора решает отправить IP-пакет другому маршрутизатору или хосту, этот хост или маршрутизатор затем использует данные канального уровня для отправки этого пакета на следующий хост /
|
router.|роутер.
|
Because each layer provides a service to the layer above it, take a moment to think about the IP logic related to Figure 1-10.|Поскольку каждый уровень предоставляет услуги вышестоящему уровню, подумайте о логике IP, показанной на рис. 1-10.
In that example, host Larry’s IP logic chooses to send the IP packet to a nearby router (R1).|В этом примере логика IP хоста Ларри решает отправить IP-пакет на ближайший маршрутизатор (R1).
However, while Figure 1-10 shows a simple line between Larry and router R1, that drawing means that some Ethernet LAN sits between the two.|Однако, хотя на рис. 1-10 показана простая линия между Ларри и маршрутизатором R1, этот рисунок означает, что некоторая локальная сеть Ethernet находится между ними.
Figure 1-11 shows four steps of what occurs at the link layer to allow Larry to send the IP packet to R1.|На рис. 1-11 показаны четыре шага того, что происходит на канальном уровне, чтобы Ларри мог отправить IP-пакет на маршрутизатор R1.
|
Larry|Ларри
###### 1.1.1.1
1.1.1.1   
__|__
--|--
|
Ethernet IP Packet Eth.|Ethernet IP Packet Eth.
|
IP Packet 1 Encapsulate 2 Transmit 3 IP Packet 4 De-encapsulate Receive R1 Header Trailer Ethernet IP Packet Eth.|IP-пакет 1 Инкапсуляция 2 Передача 3 IP-пакет 4 Деинкапсуляция Прием R1 Заголовок Прицеп Ethernet IP-пакет Eth.
|
Figure 1-11 Larry Using Ethernet to Forward an IP Packet to Router R1 NOTE Figure 1-11 depicts the Ethernet as a series of lines.|Рисунок 1-11. Ларри, использующий Ethernet для пересылки IP-пакета на маршрутизатор R1. ПРИМЕЧАНИЕ. Рисунок 1-11 изображает Ethernet как серию линий.
Networking diagrams often use this convention when drawing Ethernet LANs, in cases where the actual LAN cabling and LAN devices are not important to some discussion, as is the case here.|Сетевые схемы часто используют это соглашение при рисовании локальных сетей Ethernet, в случаях, когда фактические кабели и устройства локальной сети не важны для обсуждения, как здесь.
The LAN would have cables and devices, like LAN switches, which are not shown in this figure.|В локальной сети будут кабели и устройства, такие как коммутаторы локальной сети, которые не показаны на этом рисунке.
|
Figure 1-11 shows four steps.|На рисунке 1-11 показаны четыре шага.
The first two occur on Larry, and the last two occur on Router R1, as follows:|Первые два происходят на Ларри, а последние два - на маршрутизаторе R1, а именно:
|
Step 1.|Шаг 1.
Larry encapsulates the IP packet between an Ethernet header and Ethernet trailer, creating an Ethernet frame.|Ларри инкапсулирует IP-пакет между заголовком Ethernet и концом Ethernet, создавая кадр Ethernet.
|
Step 2.|Шаг 2.
Larry physically transmits the bits of this Ethernet frame, using electricity flowing over the Ethernet cabling.|Ларри физически передает биты этого кадра Ethernet, используя электричество, протекающее по кабелям Ethernet.
|
Step 3.|Шаг 3.
Router R1 physically receives the electrical signal over a cable and re-creates the same bits by interpreting the meaning of the electrical signals.|Маршрутизатор R1 физически принимает электрический сигнал по кабелю и воссоздает те же биты, интерпретируя значение электрических сигналов.
|
Step 4.|Шаг 4.
Router R1 de-encapsulates the IP packet from the Ethernet frame by removing and discarding the Ethernet header and trailer.|Маршрутизатор R1 деинкапсулирует IP-пакет из кадра Ethernet, удаляя и отбрасывая заголовок и трейлер Ethernet.
|
By the end of this process, Larry and R1 have worked together to deliver the packet from Larry to Router R1.|К концу этого процесса Ларри и R1 работали вместе, чтобы доставить пакет от Ларри к маршрутизатору R1.
|
NOTE Protocols define both headers and trailers for the same general reason, but headers exist at the beginning of the message and trailers exist at the end.|ПРИМЕЧАНИЕ Протоколы определяют как заголовки, так и трейлеры по одной и той же общей причине, но заголовки существуют в начале сообщения, а трейлеры - в конце.
|
The data-link and physical layers include a large number of protocols and standards.|Канальный и физический уровни включают большое количество протоколов и стандартов.
For example, the link layer includes all the variations of Ethernet protocols and wireless LAN protocols discussed throughout this book.|Например, канальный уровень включает в себя все варианты протоколов Ethernet и протоколов беспроводной локальной сети, обсуждаемые в этой книге.
|
1 In short, the TCP/IP physical and data-link layers include two distinct functions, respectively:|1 Короче говоря, физический уровень TCP / IP и уровень канала передачи данных включают две различные функции, соответственно:
|
functions related to the physical transmission of the data, plus the protocols and rules that control the use of the physical media.|функции, связанные с физической передачей данных, а также протоколы и правила, управляющие использованием физических носителей.
### Data Encapsulation Terminology
Терминология инкапсуляции данных   
__|__
--|--
|
As you can see from the explanations of how HTTP, TCP, IP, and Ethernet do their jobs, when sending data, each layer adds its own header (and for data-link protocols, also a trailer)|Как вы можете видеть из объяснений того, как HTTP, TCP, IP и Ethernet выполняют свою работу, при отправке данных каждый уровень добавляет свой собственный заголовок (а для протоколов передачи данных также трейлер)
|
to the data supplied by the higher layer.|к данным, предоставленным более высоким уровнем.
The term encapsulation refers to the process of putting headers (and sometimes trailers) around some data.|Термин инкапсуляция относится к процессу размещения заголовков (а иногда и трейлеров) вокруг некоторых данных.
|
Many of the examples in this chapter show the encapsulation process.|Многие примеры в этой главе показывают процесс инкапсуляции.
For example, web server Larry encapsulated the contents of the home page inside an HTTP header in Figure 1-6.|Например, веб-сервер Ларри инкапсулировал содержимое домашней страницы в заголовок HTTP на рис. 1-6.
The TCP layer encapsulated the HTTP headers and data inside a TCP header in Figure 1-7.|Уровень TCP инкапсулировал заголовки и данные HTTP внутри заголовка TCP, показанного на рисунке 1-7.
IP encapsulated the TCP headers and the data inside an IP header in Figure 1-10.|IP инкапсулировал заголовки TCP и данные внутри заголовка IP на рис. 1-10.
Finally, the Ethernet link layer encapsulated the IP packets inside both a header and a trailer in Figure 1-11.|Наконец, канальный уровень Ethernet инкапсулировал IP-пакеты как в заголовке, так и в конце, как показано на рисунке 1-11.
|
The process by which a TCP/IP host sends data can be viewed as a five-step process.|Процесс, посредством которого хост TCP / IP отправляет данные, можно рассматривать как пятиэтапный процесс.
The first four steps relate to the encapsulation performed by the four TCP/IP layers, and the last step is the actual physical transmission of the data by the host.|Первые четыре шага относятся к инкапсуляции, выполняемой четырьмя уровнями TCP / IP, а последний шаг - это фактическая физическая передача данных хостом.
In fact, if you use the fivelayer TCP/IP model, one step corresponds to the role of each layer.|Фактически, если вы используете пятиуровневую модель TCP / IP, один шаг соответствует роли каждого уровня.
The steps are summarized in the following list:|Шаги приведены в следующем списке:
|
Step 1.|Шаг 1.
Create and encapsulate the application data with any required application layer headers.|Создайте и инкапсулируйте данные приложения с любыми необходимыми заголовками уровня приложения.
For example, the HTTP OK message can be returned in an HTTP header, followed by part of the contents of a web page.|Например, сообщение HTTP OK может быть возвращено в заголовке HTTP, за которым следует часть содержимого веб-страницы.
|
Step 2.|Шаг 2.
Encapsulate the data supplied by the application layer inside a transport layer header.|Инкапсулируйте данные, предоставленные прикладным уровнем, внутри заголовка транспортного уровня.
For end-user applications, a TCP or UDP header is typically used.|Для приложений конечного пользователя обычно используется заголовок TCP или UDP.
|
Step 3.|Шаг 3.
Encapsulate the data supplied by the transport layer inside a network layer (IP) header.|Инкапсулируйте данные, предоставленные транспортным уровнем, внутри заголовка сетевого уровня (IP).
IP defines the IP addresses that uniquely identify each computer.|IP определяет IP-адреса, которые однозначно идентифицируют каждый компьютер.
|
Step 4.|Шаг 4.
Encapsulate the data supplied by the network layer inside a data-link layer header and trailer.|Инкапсулируйте данные, предоставленные сетевым уровнем, внутри заголовка и трейлера уровня канала данных.
This layer uses both a header and a trailer.|Этот слой использует как заголовок, так и трейлер.
|
Step 5.|Шаг 5.
Transmit the bits.|Передайте биты.
The physical layer encodes a signal onto the medium to transmit the frame.|Физический уровень кодирует сигнал на носителе для передачи кадра.
|
The numbers in Figure 1-12 correspond to the five steps in this list, graphically showing the same concepts.|Цифры на рис. 1-12 соответствуют пяти шагам в этом списке, графически демонстрируя те же концепции.
Note that because the application layer often does not need to add a header, the figure does not show a specific application layer header, but the application layer will also at times add a header as well.|Обратите внимание, что, поскольку на уровне приложения часто не требуется добавлять заголовок, на рисунке не показан конкретный заголовок уровня приложения, но уровень приложения также иногда добавляет заголовок.
|
Figure 1-12 Five Steps of Data Encapsulation: TCP/IP|Рисунок 1-12 Пять шагов инкапсуляции данных: TCP / IP
#### Names of TCP/IP Messages
Имена сообщений TCP / IP   
__|__
--|--
|
One reason this chapter takes the time to show the encapsulation steps in detail has to do with terminology.|Одна из причин, по которой в этой главе уделено время подробному описанию этапов инкапсуляции, связана с терминологией.
When talking and writing about networking, people use segment, packet, and frame to refer to the messages shown in Figure 1-13 and the related list.|Когда говорят и пишут о сети, люди используют сегмент, пакет и фрейм для ссылки на сообщения, показанные на рис. 1-13, и связанный список.
Each term has a specific meaning, referring to the headers (and possibly trailers) defined by a particular layer and the data encapsulated following that header.|Каждый термин имеет определенное значение, относящееся к заголовкам (и, возможно, трейлерам), определенным конкретным уровнем, и данным, инкапсулированным после этого заголовка.
Each term, however, refers to a different layer: segment for the transport layer, packet for the network layer, and frame for the link layer.|Однако каждый термин относится к разному уровню: сегменту для транспортного уровня, пакету для сетевого уровня и кадру для канального уровня.
Figure 1-13 shows each layer along with the associated term.|На рис. 1-13 показан каждый уровень вместе с соответствующим термином.
|
Figure 1-13 Perspectives on Encapsulation and “Data”1 1 The letters LH and LT stand for link header and link trailer, respectively, and refer to the data-link layer header and trailer.|Рисунок 1-13 Перспективы инкапсуляции и «данных» 1 1 Буквы LH и LT обозначают заголовок ссылки и концевую часть ссылки, соответственно, и относятся к заголовку и завершению уровня звена данных.
|
Figure 1-13 also shows the encapsulated data as simply “data.” When focusing on the work done by a particular layer, the encapsulated data typically is unimportant.|На рис. 1-13 также показаны инкапсулированные данные как просто «данные». Если сосредоточиться на работе, выполняемой определенным уровнем, инкапсулированные данные обычно не важны.
For example, an IP packet can indeed have a TCP header after the IP header, an HTTP header after the TCP header, and data for a web page after the HTTP header.|Например, IP-пакет действительно может иметь заголовок TCP после заголовка IP, заголовок HTTP после заголовка TCP и данные для веб-страницы после заголовка HTTP.
However, when discussing IP, you probably just care about the IP header, so everything after the IP header is just called data.|Однако, обсуждая IP, вы, вероятно, заботитесь только о заголовке IP, поэтому все, что находится после заголовка IP, просто называется данными.
|
So, when drawing IP packets, everything after the IP header is typically shown simply as data.|Таким образом, при отрисовке IP-пакетов все, что находится после IP-заголовка, обычно отображается просто как данные.
#### OSI Networking Model and Terminology
Сетевая модель и терминология OSI   
__|__
--|--
|
At one point in the history of the OSI model, many people thought that OSI would win the battle of the networking models discussed earlier.|В какой-то момент истории модели OSI многие люди думали, что OSI выиграет битву сетевых моделей, обсуждавшихся ранее.
If that had occurred, instead of running TCP/IP on every computer in the world, those computers would be running with OSI.|Если бы это произошло, вместо запуска TCP / IP на каждом компьютере в мире эти компьютеры работали бы с OSI.
|
1 However, OSI did not win that battle.|1 Однако OSI не выиграла эту битву.
In fact, OSI no longer exists as a networking model that could be used instead of TCP/IP, although some of the original protocols referenced by the OSI model still exist.|Фактически, OSI больше не существует как сетевая модель, которую можно было бы использовать вместо TCP / IP, хотя некоторые из исходных протоколов, на которые ссылается модель OSI, все еще существуют.
|
So, why is OSI even in this book?|Итак, почему OSI даже в этой книге?
Terminology.|Терминология.
During those years in which many people thought the OSI model would become commonplace in the world of networking (mostly in the late 1980s and early 1990s), many vendors and protocol documents started using terminology from the OSI model.|В те годы, когда многие думали, что модель OSI станет обычным явлением в мире сетей (в основном в конце 1980-х - начале 1990-х годов), многие поставщики и протоколы начали использовать терминологию модели OSI.
That terminology remains today.|Эта терминология сохраняется и сегодня.
So, while you will never need to work with a computer that uses OSI, to understand modern networking terminology, you need to understand something about OSI.|Итак, хотя вам никогда не придется работать с компьютером, использующим OSI, для понимания современной сетевой терминологии вам необходимо кое-что понять об OSI.
##### Comparing OSI and TCP/IP Layer Names and Numbers
Сравнение имен и номеров уровней OSI и TCP / IP   
__|__
--|--
|
The OSI model has many similarities to the TCP/IP model from a basic conceptual perspective.|Модель OSI имеет много общего с моделью TCP / IP с базовой концептуальной точки зрения.
|
It has layers, and each layer defines a set of typical networking functions.|Он имеет уровни, и каждый уровень определяет набор типичных сетевых функций.
As with TCP/|Как и в случае с TCP /
|
IP, the OSI layers each refer to multiple protocols and standards that implement the functions specified by each layer.|IP, каждый уровень OSI относится к нескольким протоколам и стандартам, которые реализуют функции, указанные на каждом уровне.
In other cases, just as for TCP/IP, the OSI committees did not create new protocols or standards, but instead referenced other protocols that were already defined.|В других случаях, как и в случае TCP / IP, комитеты OSI не создавали новые протоколы или стандарты, а вместо этого ссылались на другие протоколы, которые уже были определены.
|
For example, the IEEE defines Ethernet standards, so the OSI committees did not waste time specifying a new type of Ethernet; it simply referred to the IEEE Ethernet standards.|Например, IEEE определяет стандарты Ethernet, поэтому комитеты OSI не тратили время на определение нового типа Ethernet; он просто ссылался на стандарты IEEE Ethernet.
|
Today, the OSI model can be used as a standard of comparison to other networking models.|Сегодня модель OSI может использоваться как стандарт для сравнения с другими сетевыми моделями.
|
Figure 1-14 compares the seven-layer OSI model with both the four-layer and five-layer TCP/IP models.|На рисунке 1-14 сравнивается семиуровневая модель OSI с четырехуровневой и пятиуровневой моделями TCP / IP.
|
Figure 1-14 OSI Model Compared to the Two TCP/IP Models Note that the TCP/IP model in use today, on the right side of the figure, uses the exact same layer names as OSI at the lower layers.|Рисунок 1-14 Модель OSI в сравнении с двумя моделями TCP / IP Обратите внимание, что в модели TCP / IP, используемой сегодня, в правой части рисунка, используются те же имена уровней, что и в OSI на нижних уровнях.
The functions generally match as well, so for the purpose of discussing networking, and reading networking documentation, think of the bottom four layers as equivalent, in name, in number, and in meaning.|Функции, как правило, также совпадают, поэтому при обсуждении сети и чтении сетевой документации подумайте о нижних четырех уровнях как о эквивалентных по названию, количеству и значению.
|
Even though the world uses TCP/IP today rather than OSI, we tend to use the numbering from the OSI layer.|Хотя сегодня в мире используется TCP / IP, а не OSI, мы склонны использовать нумерацию уровня OSI.
For instance, when referring to an application layer protocol in a TCP/IP network, the world still refers to the protocol as a “Layer 7 protocol.” Also, while TCP/IP includes more functions at its application layer, OSI breaks those intro session, presentation, and application layers.|Например, когда речь идет о протоколе прикладного уровня в сети TCP / IP, мир по-прежнему называет этот протокол «протоколом уровня 7». Кроме того, в то время как TCP / IP включает больше функций на уровне приложений, OSI нарушает эти вводные сеансы, представления и уровни приложений.
Most of the time, no one cares much about the distinction, so you will see references like “Layer 5–7 protocol,” again using OSI numbering.|В большинстве случаев никто не заботится о различиях, поэтому вы увидите такие ссылки, как «Протокол уровня 5–7», опять же с использованием нумерации OSI.
|
For the purposes of this book, know the mapping between the five-layer TCP/IP model and the seven-layer OSI model shown in Figure 1-14, and know that layer number references to Layer 7 really do match the application layer of TCP/IP as well.|Для целей этой книги необходимо знать соответствие между пятиуровневой моделью TCP / IP и семиуровневой моделью OSI, показанной на рис. 1-14, и знать, что ссылки на номер уровня на уровень 7 действительно соответствуют прикладному уровню TCP. / IP тоже.
##### OSI Data Encapsulation Terminology
Терминология инкапсуляции данных OSI   
__|__
--|--
|
Like TCP/IP, each OSI layer asks for services from the next lower layer.|Как и TCP / IP, каждый уровень OSI запрашивает услуги у следующего нижнего уровня.
To provide the services, each layer makes use of a header and possibly a trailer.|Для предоставления услуг каждый уровень использует заголовок и, возможно, трейлер.
The lower layer encapsulates the higher layer’s data behind a header.|Нижний уровень инкапсулирует данные верхнего уровня за заголовком.
|
OSI uses a more generic term to refer to messages, rather than frame, packet, and segment.|OSI использует более общий термин для обозначения сообщений, а не кадра, пакета и сегмента.
|
OSI uses the term protocol data unit (PDU). A PDU represents the bits that include the headers and trailers for that layer, as well as the encapsulated data.|OSI использует термин блок данных протокола (PDU). PDU представляет биты, которые включают заголовки и трейлеры для этого уровня, а также инкапсулированные данные.
For example, an IP packet, as shown in Figure 1-13, using OSI terminology, is a PDU, more specifically a Layer 3 PDU (abbreviated L3PDU) because IP is a Layer 3 protocol.|Например, IP-пакет, как показано на рис. 1-13, используя терминологию OSI, является PDU, а точнее PDU уровня 3 (сокращенно L3PDU), поскольку IP является протоколом уровня 3.
OSI simply refers to the Layer x PDU (LxPDU), with x referring to the number of the layer being discussed, as shown in Figure 1-15.|OSI просто относится к PDU уровня x (LxPDU), где x относится к номеру обсуждаемого уровня, как показано на рисунке 1-15.
|
Figure 1-15 OSI Encapsulation and Protocol Data Units|Рисунок 1-15 Инкапсуляция OSI и блоки данных протокола
### Chapter Review
Обзор главы   
__|__
--|--
|
The “Your Study Plan” element, just before Chapter 1, discusses how you should study and practice the content and skills for each chapter before moving on to the next chapter.|Элемент «Ваш учебный план», расположенный непосредственно перед главой 1, обсуждает, как вы должны изучать и практиковать содержание и навыки для каждой главы, прежде чем переходить к следующей главе.
That element introduces the tools used here at the end of each chapter.|Этот элемент знакомит с инструментами, используемыми здесь, в конце каждой главы.
If you haven’t already done so, take a few minutes to read that section.|Если вы еще этого не сделали, уделите несколько минут, чтобы прочитать этот раздел.
Then come back here and do the useful work of reviewing the chapter to help lock into memory what you just read.|Затем вернитесь сюда и проделайте полезную работу по просмотру главы, чтобы закрепить в памяти то, что вы только что прочитали.
|
Review this chapter’s material using either the tools in the book or the interactive tools for the same material found on the book’s companion website.|Просмотрите материал этой главы, используя инструменты в книге или интерактивные инструменты для того же материала, которые можно найти на сопутствующем веб-сайте книги.
Table 1-4 outlines the key review elements and where you can find them.|В Таблице 1-4 представлены основные элементы обзора и их местонахождение.
To better track your study progress, record when you completed these activities in the second column.|Чтобы лучше отслеживать свои успехи в учебе, отметьте, когда вы выполнили эти задания, во втором столбце.
|
1 Table 1-4 Chapter Review Tracking Table end.|1 Таблица 1-4. Конец таблицы отслеживания обзора главы.
|
Review All the Key Topics Key Terms You Should Know adjacent-layer interaction, de-encapsulation, encapsulation, frame, networking model, packet, protocol data unit (PDU), same-layer interaction, segment|Ознакомьтесь со всеми ключевыми темами. Ключевые термины, которые вы должны знать. Взаимодействие на смежном уровне, деинкапсуляция, инкапсуляция, кадр, сетевая модель, пакет, блок данных протокола (PDU), взаимодействие на одном уровне, сегмент.
## Chapter 2 Fundamentals of Ethernet LANs
Глава 2 Основы локальных сетей Ethernet   
__|__
--|--
|
This chapter covers the following exam topics:|В этой главе рассматриваются следующие экзаменационные темы:
###### 1.0 Network Fundamentals
1.0 Основы сети   
###### 1.1 Explain the role and function of network components
1.1 Объясните роль и функции сетевых компонентов   
###### 1.1.b L2 and L3 Switches
1.1.b Коммутаторы L2 и L3   
###### 1.2 Describe characteristics of network topology architectures
1.2 Описание характеристик архитектур топологии сети   
###### 1.2.e Small office/home office (SOHO)
1.2.e Малый офис / домашний офис (SOHO)   
###### 1.3 Compare physical interface and cabling types
1.3 Сравните физический интерфейс и типы кабелей   
###### 1.3.a Single-mode fiber, multimode fiber, copper
1.3.a Одномодовое волокно, многомодовое волокно, медь   
###### 1.3.b Connections (Ethernet shared media and point-to-point)
1.3.b Подключения (общая среда Ethernet и точка-точка)   
__|__
--|--
|
Most enterprise computer networks can be separated into two general types of technology:|Большинство корпоративных компьютерных сетей можно разделить на два основных типа технологий:
|
local-area networks (LANs) and wide-area networks (WANs).|локальные сети (LAN) и глобальные сети (WAN).
LANs typically connect nearby devices: devices in the same room, in the same building, or in a campus of buildings.|К локальным сетям обычно подключаются соседние устройства: устройства в одной комнате, в одном здании или в комплексе зданий.
|
In contrast, WANs connect devices that are typically relatively far apart.|Напротив, глобальные сети соединяют устройства, которые обычно находятся на относительно большом расстоянии друг от друга.
Together, LANs and WANs create a complete enterprise computer network, working together to do the job of a computer network: delivering data from one device to another.|Вместе локальные и глобальные сети создают законченную компьютерную сеть предприятия, работая вместе, чтобы выполнять работу компьютерной сети: доставлять данные от одного устройства к другому.
|
Many types of LANs have existed over the years, but today’s networks use two general types of LANs: Ethernet LANs and wireless LANs. Ethernet LANs happen to use cables for the links between nodes, and because many types of cables use copper wires, Ethernet LANs are often called wired LANs. Ethernet LANs also make use of fiber-optic cabling, which includes a fiberglass core that devices use to send data using light.|На протяжении многих лет существовало множество типов локальных сетей, но современные сети используют два основных типа локальных сетей: локальные сети Ethernet и беспроводные локальные сети. В локальных сетях Ethernet используются кабели для связи между узлами, и поскольку многие типы кабелей используют медные провода, локальные сети Ethernet часто называют проводными локальными сетями. В локальных сетях Ethernet также используются волоконно-оптические кабели, которые включают в себя стекловолоконную сердцевину, которую устройства используют для передачи данных с помощью света.
In comparison to Ethernet, wireless LANs do not use wires or cables, instead using radio waves for the links between nodes; Part V of this book discusses Wireless LANs at length.|По сравнению с Ethernet, в беспроводных локальных сетях не используются провода или кабели, вместо этого используются радиоволны для связи между узлами; В части V этой книги подробно рассматриваются беспроводные локальные сети.
|
This chapter introduces Ethernet LANs, with more detailed coverage in Parts II and III of this book.|В этой главе представлены локальные сети Ethernet с более подробным описанием в частях II и III этой книги.
### “Do I Know This Already?” Quiz
«Знаю ли я это уже?» Викторина   
__|__
--|--
|
Take the quiz (either here or use the PTP software) if you want to use the score to help you decide how much time to spend on this chapter.|Пройдите тест (здесь или воспользуйтесь программой PTP), если вы хотите использовать оценку, чтобы решить, сколько времени потратить на эту главу.
The letter answers are listed at the bottom of the page following the quiz.|Ответы на письма перечислены внизу страницы после викторины.
Appendix C, found both at the end of the book as well as on the companion website, includes both the answers and explanations.|Приложение C, которое можно найти как в конце книги, так и на сопутствующем веб-сайте, включает как ответы, так и пояснения.
You can also find both answers and explanations in the PTP testing software.|Вы также можете найти ответы и пояснения в программе тестирования PTP.
|
CHAPTER 2 Table 2-1 “Do I Know This Already?” Foundation Topics Section-to-Question Mapping|ГЛАВА 2 Таблица 2-1 «Знаю ли я это уже?» Сопоставление разделов с вопросами по основным темам
### Foundation Topics
Основные темы   
### An Overview of LANs
Обзор локальных сетей   
__|__
--|--
|
Building Physical Ethernet LANs with UTP 3–4 Building Physical Ethernet LANs with Fiber 5 Sending Data in Ethernet Networks 6–9 1.|Создание физических локальных сетей Ethernet с использованием UTP 3–4 Создание физических локальных сетей Ethernet с использованием оптоволокна 5 Отправка данных в сетях Ethernet 6–9 1.
In the LAN for a small office, some user devices connect to the LAN using a cable, while others connect using wireless technology (and no cable).|В локальной сети для небольшого офиса некоторые пользовательские устройства подключаются к локальной сети с помощью кабеля, а другие подключаются с помощью беспроводной технологии (без кабеля).
Which of the following is true regarding the use of Ethernet in this LAN?|Что из следующего верно относительно использования Ethernet в этой локальной сети?
|
a. Only the devices that use cables are using Ethernet.|а. Только устройства, которые используют кабели, используют Ethernet.
|
b. Only the devices that use wireless are using Ethernet.|б. Только устройства, использующие беспроводную связь, используют Ethernet.
|
c. Both the devices using cables and those using wireless are using Ethernet.|c. И устройства, использующие кабели, и устройства, использующие беспроводную связь, используют Ethernet.
|
d. None of the devices are using Ethernet.|d. Ни одно из устройств не использует Ethernet.
|
2. Which of the following Ethernet standards defines Gigabit Ethernet over UTP cabling?|2. Какой из следующих стандартов Ethernet определяет кабели Gigabit Ethernet через UTP?
|
a. 10GBASE-T b. 100BASE-T c. 1000BASE-T d.|а. 10GBASE-T б. 100BASE-T c. 1000BASE-T d.
None of the other answers is correct.|Ни один из других ответов не верен.
|
3. Which of the following is true about Ethernet crossover cables for Fast Ethernet?|3. Что из следующего верно относительно кроссоверных кабелей Ethernet для Fast Ethernet?
|
a. Pins 1 and 2 are reversed on the other end of the cable.|а. Контакты 1 и 2 на другом конце кабеля переставлены.
|
b. Pins 1 and 2 on one end of the cable connect to pins 3 and 6 on the other end of the cable.|б. Контакты 1 и 2 на одном конце кабеля подключаются к контактам 3 и 6 на другом конце кабеля.
|
c. Pins 1 and 2 on one end of the cable connect to pins 3 and 4 on the other end of the cable.|c. Контакты 1 и 2 на одном конце кабеля подключаются к контактам 3 и 4 на другом конце кабеля.
|
d. The cable can be up to 1000 meters long to cross over between buildings.|d. Кабель может быть длиной до 1000 метров для перехода между зданиями.
|
e. None of the other answers is correct.|е. Ни один из других ответов не верен.
|
4. Each answer lists two types of devices used in a 100BASE-T network.|4. В каждом ответе перечислены два типа устройств, используемых в сети 100BASE-T.
If these devices were connected with UTP Ethernet cables, which pairs of devices would require a straight-through cable? (Choose three answers.)|Если бы эти устройства были подключены с помощью кабелей UTP Ethernet, для каких пар устройств потребовался бы прямой кабель? (Выберите три ответа.)
|
a. PC and router b.|а. ПК и маршрутизатор b.
PC and switch c.|ПК и коммутатор c.
Hub and switch d.|Концентратор и переключатель d.
Router and hub e.|Маршрутизатор и концентратор e.
Wireless access point (Ethernet port) and switch 5.|Точка беспроводного доступа (порт Ethernet) и коммутатор 5.
Which of the following are advantages of using multimode fiber for an Ethernet link instead of UTP or single-mode fiber?|Каковы преимущества использования многомодового волокна для канала Ethernet вместо UTP или одномодового волокна?
|
a. To achieve the longest distance possible for that single link.|а. Для достижения максимально возможного расстояния для этого одиночного звена.
|
b. To extend the link beyond 100 meters while keeping initial costs as low as possible.|б. Расширить линию связи более чем на 100 метров при минимально возможных начальных затратах.
|
c. To make use of an existing stock of laser-based SFP/SFP+ modules.|c. Чтобы использовать существующий запас лазерных модулей SFP / SFP +.
|
d. To make use of an existing stock of LED-based SFP/SFP+ modules.|d. Чтобы использовать существующий запас модулей SFP / SFP + на основе светодиодов.
|
6. Which of the following is true about the CSMA/CD algorithm?|6. Что из следующего верно об алгоритме CSMA / CD?
|
a. The algorithm never allows collisions to occur.|а. Алгоритм никогда не допускает возникновения коллизий.
|
b. Collisions can happen, but the algorithm defines how the computers should notice a collision and how to recover.|б. Коллизии могут происходить, но алгоритм определяет, как компьютеры должны замечать коллизию и как восстанавливаться.
|
c. The algorithm works with only two devices on the same Ethernet.|c. Алгоритм работает только с двумя устройствами в одном Ethernet.
|
d. None of the other answers is correct.|d. Ни один из других ответов не верен.
|
7. Which of the following is true about the Ethernet FCS field?|7. Что из следующего верно о поле Ethernet FCS?
|
a. Ethernet uses FCS for error recovery.|а. Ethernet использует FCS для устранения ошибок.
|
b. It is 2 bytes long.|б. Его длина составляет 2 байта.
|
c. It resides in the Ethernet trailer, not the Ethernet header.|c. Он находится в трейлере Ethernet, а не в заголовке Ethernet.
|
d. It is used for encryption.|d. Он используется для шифрования.
|
8. Which of the following are true about the format of Ethernet addresses? (Choose three answers.)|8. Что из следующего является верным относительно формата адресов Ethernet? (Выберите три ответа.)
|
a. Each manufacturer puts a unique OUI code into the first 2 bytes of the address.|а. Каждый производитель помещает уникальный код OUI в первые 2 байта адреса.
|
b. Each manufacturer puts a unique OUI code into the first 3 bytes of the address.|б. Каждый производитель помещает уникальный код OUI в первые 3 байта адреса.
|
c. Each manufacturer puts a unique OUI code into the first half of the address.|c. Каждый производитель помещает уникальный код OUI в первую половину адреса.
|
d. The part of the address that holds this manufacturer’s code is called the MAC.|d. Часть адреса, содержащая код этого производителя, называется MAC.
|
e. The part of the address that holds this manufacturer’s code is called the OUI.|е. Часть адреса, содержащая код этого производителя, называется OUI.
|
f. The part of the address that holds this manufacturer’s code has no specific name.|f. Часть адреса, содержащая код этого производителя, не имеет конкретного названия.
|
9. Which of the following terms describe Ethernet addresses that can be used to send one frame that is delivered to multiple devices on the LAN? (Choose two answers.)|9. Какие из следующих терминов описывают адреса Ethernet, которые можно использовать для отправки одного кадра, который доставляется на несколько устройств в локальной сети? (Выберите два ответа.)
|
a. Burned-in address b.|а. Выгоревший адрес b.
Unicast address c.|Одноадресный адрес c.
Broadcast address d.|Адрес трансляции d.
Multicast address Foundation Topics An Overview of LANs The term Ethernet refers to a family of LAN standards that together define the physical and data-link layers of the world’s most popular wired LAN technology.|Основные темы многоадресного адреса Обзор LAN Термин Ethernet относится к семейству стандартов LAN, которые вместе определяют физический уровень и уровень канала передачи данных самой популярной в мире технологии проводных LAN.
The standards, defined by the Institute of Electrical and Electronics Engineers (IEEE), define the cabling, the connectors on the ends of the cables, the protocol rules, and everything else required to create an Ethernet LAN.|Стандарты, определенные Институтом инженеров по электротехнике и электронике (IEEE), определяют кабели, разъемы на концах кабелей, правила протокола и все остальное, необходимое для создания локальной сети Ethernet.
#### Typical SOHO LANs
Типичные локальные сети SOHO   
__|__
--|--
|
To begin, first think about a small office/home office (SOHO) LAN today, specifically a LAN that uses only Ethernet LAN technology.|Для начала сначала подумайте о ЛВС небольшого офиса / домашнего офиса (SOHO) сегодня, особенно о ЛВС, в которой используется только технология ЛВС Ethernet.
First, the LAN needs a device called an Ethernet LAN switch, which provides many physical ports into which cables can be connected.|Во-первых, для локальной сети требуется устройство, называемое коммутатором локальной сети Ethernet, который предоставляет множество физических портов, к которым можно подключать кабели.
|
An Ethernet uses Ethernet cables, which is a general reference to any cable that conforms to any of several Ethernet standards.|Ethernet использует кабели Ethernet, которые являются общим обозначением любого кабеля, который соответствует любому из нескольких стандартов Ethernet.
The LAN uses Ethernet cables to connect different Ethernet devices or nodes to one of the switch’s Ethernet ports.|В локальной сети используются кабели Ethernet для подключения различных устройств или узлов Ethernet к одному из портов Ethernet коммутатора.
|
Figure 2-1 shows a drawing of a SOHO Ethernet LAN. The figure shows a single LAN switch, five cables, and five other Ethernet nodes: three PCs, a printer, and one network device called a router. (The router connects the LAN to the WAN, in this case to the Internet.).|На Рис. 2-1 показан чертеж локальной сети Ethernet SOHO. На рисунке показан один коммутатор LAN, пять кабелей и пять других узлов Ethernet: три ПК, принтер и одно сетевое устройство, называемое маршрутизатором. (Маршрутизатор соединяет локальную сеть с глобальной сетью, в данном случае с Интернетом).
|
Figure 2-1 Typical Small Ethernet-Only SOHO LAN Although Figure 2-1 shows the switch and router as separate devices, many SOHO Ethernet LANs today combine the router and switch into a single device.|Рис. 2-1 Типичная небольшая локальная сеть SOHO только для Ethernet Хотя на рис. 2-1 коммутатор и маршрутизатор показаны как отдельные устройства, сегодня многие локальные сети Ethernet для SOHO объединяют маршрутизатор и коммутатор в одно устройство.
Vendors sell consumer-grade integrated networking devices that work as a router and Ethernet switch, as well as doing other functions.|Продавцы продают интегрированные сетевые устройства потребительского уровня, которые работают как маршрутизатор и коммутатор Ethernet, а также выполняют другие функции.
These devices typically have “router” on the packaging, but many models also have four-port or eight-port Ethernet LAN switch ports built in to the device.|Эти устройства обычно имеют «маршрутизатор» на упаковке, но многие модели также имеют порты коммутатора LAN с четырьмя или восемью портами, встроенные в устройство.
|
Typical SOHO LANs today also support wireless LAN connections.|Типичные локальные сети SOHO сегодня также поддерживают подключения к беспроводной локальной сети.
You can build a single SOHO LAN that includes both Ethernet LAN technology as well as wireless LAN technology, which is also defined by the IEEE. Wireless LANs, defined by the IEEE using standards that begin with 802.11, use radio waves to send the bits from one node to the next.|Вы можете построить одну локальную сеть SOHO, которая включает как технологию локальной сети Ethernet, так и технологию беспроводной локальной сети, которая также определена IEEE. Беспроводные локальные сети, определенные IEEE с использованием стандартов, начинающихся с 802.11, используют радиоволны для передачи битов от одного узла к другому.
|
Most wireless LANs rely on yet another networking device: a wireless LAN access point (AP). The AP acts somewhat like an Ethernet switch, in that all the wireless LAN nodes communicate with the wireless AP. If the network uses an AP that is a separate physical device, the AP then needs a single Ethernet link to connect the AP to the Ethernet LAN, as shown in Figure 2-2.|Большинство беспроводных локальных сетей полагаются на еще одно сетевое устройство: точку доступа (AP) беспроводной локальной сети. Точка доступа действует как коммутатор Ethernet, поскольку все узлы беспроводной локальной сети обмениваются данными с беспроводной точкой доступа. Если в сети используется точка доступа, которая является отдельным физическим устройством, тогда этой точке доступа потребуется один канал Ethernet для подключения точки доступа к локальной сети Ethernet, как показано на рисунке 2-2.
|
Note that Figure 2-2 shows the router, Ethernet switch, and wireless LAN access point as three separate devices so that you can better understand the different roles.|Обратите внимание, что на Рис. 2-2 маршрутизатор, коммутатор Ethernet и точка доступа к беспроводной локальной сети показаны как три отдельных устройства, чтобы вы могли лучше понять различные роли.
However, most SOHO networks today would use a single device, often labeled as a “wireless router,” that does all these functions.|Однако в большинстве сетей SOHO сегодня используется одно устройство, часто обозначаемое как «беспроводной маршрутизатор», которое выполняет все эти функции.
|
Figure 2-2 Typical Small Wired and Wireless SOHO LAN|Рисунок 2-2 Типичная небольшая проводная и беспроводная локальная сеть SOHO.
#### Typical Enterprise LANs
Типичные корпоративные локальные сети   
__|__
--|--
|
Enterprise networks have similar needs compared to a SOHO network, but on a much larger scale.|У корпоративных сетей аналогичные потребности по сравнению с сетью SOHO, но в гораздо большем масштабе.
For example, enterprise Ethernet LANs begin with LAN switches installed in a wiring closet behind a locked door on each floor of a building.|Например, корпоративные локальные сети Ethernet начинаются с коммутаторов локальной сети, установленных в коммутационном шкафу за запертой дверью на каждом этаже здания.
The electricians install the Ethernet cabling from that wiring closet to cubicles and conference rooms where devices might need to connect to the LAN. At the same time, most enterprises also support wireless LANs in the same space, to allow people to roam around and still work and to support a growing number of devices that do not have an Ethernet LAN interface.|Электрики устанавливают кабели Ethernet от этого коммутационного шкафа до кабинетов и конференц-залов, где устройствам может потребоваться подключение к локальной сети. В то же время большинство предприятий также поддерживают беспроводные локальные сети в том же пространстве, чтобы люди могли перемещаться и продолжать работать, а также для поддержки растущего числа устройств, не имеющих интерфейса Ethernet LAN.
|
Figure 2-3 shows a conceptual view of a typical enterprise LAN in a three-story building.|На рис. 2-3 показано концептуальное представление типичной корпоративной локальной сети в трехэтажном здании.
Each floor has an Ethernet LAN switch and a wireless LAN AP. To allow communication between floors, each per-floor switch connects to one centralized distribution switch.|На каждом этаже есть коммутатор локальной сети Ethernet и точка доступа беспроводной локальной сети. Для обеспечения связи между этажами каждый этажный коммутатор подключается к одному централизованному распределительному коммутатору.
For example, PC3 can send data to PC2, but it would first flow through switch SW3 to the first floor to the distribution switch (SWD) and then back up through switch SW2 on the second floor.|Например, ПК3 может отправлять данные на ПК2, но сначала они будут проходить через переключатель SW3 на первый этаж к распределительному переключателю (SWD), а затем обратно через переключатель SW2 на втором этаже.
|
Figure 2-3 Single-Building Enterprise Wired and Wireless LAN Answers to the “Do I Know This Already?” quiz:|Рис. 2-3. Проводная и беспроводная локальная сеть в одном здании. Ответы на вопрос «Знаю ли я это уже?» викторина:
|
1 A 2 C 3 B 4 B, D, and E 5 B 6 B 7 C 8 B, C, and E 9 C and D The figure also shows the typical way to connect a LAN to a WAN using a router.|1 A 2 C 3 B 4 B, D и E 5 B 6 B 7 C 8 B, C и E 9 C и D На рисунке также показан типичный способ подключения LAN к WAN с помощью маршрутизатора.
LAN switches and wireless access points work to create the LAN itself.|Коммутаторы LAN и точки беспроводного доступа создают саму LAN.
Routers connect to both the LAN and the WAN. To connect to the LAN, the router simply uses an Ethernet LAN interface and an Ethernet cable, as shown on the lower right of Figure 2-3.|Маршрутизаторы подключаются как к локальной, так и к глобальной сети. Для подключения к локальной сети маршрутизатор просто использует интерфейс локальной сети Ethernet и кабель Ethernet, как показано в правом нижнем углу рисунка 2-3.
|
The rest of this chapter focuses on Ethernet in particular.|Остальная часть этой главы посвящена, в частности, Ethernet.
#### The Variety of Ethernet Physical Layer Standards
Разнообразие стандартов физического уровня Ethernet   
__|__
--|--
|
The term Ethernet refers to an entire family of standards.|Термин Ethernet относится к целому семейству стандартов.
Some standards define the specifics of how to send data over a particular type of cabling, and at a particular speed.|Некоторые стандарты определяют особенности передачи данных по определенному типу кабеля и с определенной скоростью.
Other standards define protocols, or rules, that the Ethernet nodes must follow to be a part of an Ethernet LAN. All these Ethernet standards come from the IEEE and include the number 802.3 as the beginning part of the standard name.|Другие стандарты определяют протоколы или правила, которым должны следовать узлы Ethernet, чтобы стать частью локальной сети Ethernet. Все эти стандарты Ethernet исходят от IEEE и включают номер 802.3 в начале названия стандарта.
|
Ethernet supports a large variety of options for physical Ethernet links given its long history over the last 40 or so years.|Ethernet поддерживает большое количество вариантов физических каналов Ethernet, учитывая его долгую историю за последние 40 лет или около того.
Today, Ethernet includes many standards for different kinds of optical and copper cabling, and for speeds from 10 megabits per second (Mbps) up to 400 gigabits per second (Gbps).|Сегодня Ethernet включает множество стандартов для различных типов оптических и медных кабелей, а также для скоростей от 10 мегабит в секунду (Мбит / с) до 400 гигабит в секунду (Гбит / с).
The standards also differ as far as the types and length of the cables.|Стандарты также различаются по типам и длине кабелей.
|
The most fundamental cabling choice has to do with the materials used inside the cable for the physical transmission of bits: either copper wires or glass fibers.|Самый важный выбор кабеля связан с материалами, используемыми внутри кабеля для физической передачи битов: либо медные провода, либо стеклянные волокна.
Devices using UTP cabling transmit data over electrical circuits via the copper wires inside the cable.|Устройства, использующие кабели UTP, передают данные по электрическим цепям через медные провода внутри кабеля.
Fiber-optic cabling, the more expensive alternative, allows Ethernet nodes to send light over glass fibers in the center of the cable.|Оптоволоконный кабель, более дорогая альтернатива, позволяет узлам Ethernet передавать свет по стеклянным волокнам в центре кабеля.
Although more expensive, optical cables typically allow longer cabling distances between nodes.|Хотя оптические кабели более дорогие, они обычно позволяют прокладывать большие расстояния между узлами.
|
To be ready to choose the products to purchase for a new Ethernet LAN, a network engineer must know the names and features of the different Ethernet standards supported in Ethernet products.|Чтобы быть готовым выбрать продукты для покупки для новой локальной сети Ethernet, сетевой инженер должен знать названия и особенности различных стандартов Ethernet, поддерживаемых в продуктах Ethernet.
The IEEE defines Ethernet physical layer standards using a couple of naming conventions.|IEEE определяет стандарты физического уровня Ethernet, используя несколько соглашений об именах.
|
The formal name begins with 802.3 followed by some suffix letters.|Официальное имя начинается с 802.3, за которым следуют несколько букв суффикса.
The IEEE also uses more meaningful shortcut names that identify the speed, as well as a clue about whether the cabling is UTP (with a suffix that includes T) or fiber (with a suffix that includes X).|IEEE также использует более понятные имена, определяющие скорость, а также подсказку о том, является ли проводка UTP (с суффиксом, включающим T) или оптоволоконным (с суффиксом, включающим X).
|
Table 2-2 lists a few Ethernet physical layer standards.|В таблице 2-2 перечислены несколько стандартов физического уровня Ethernet.
First, the table lists enough names so that you get a sense of the IEEE naming conventions.|Во-первых, в таблице перечислено достаточно имен, чтобы вы могли понять соглашения об именах IEEE.
|
Table 2-2 Examples of Types of Ethernet Table end.|Таблица 2-2 Примеры типов конца таблицы Ethernet.
|
NOTE Fiber-optic cabling contains long thin strands of fiberglass.|ПРИМЕЧАНИЕ. Волоконно-оптические кабели содержат длинные тонкие жилы из стекловолокна.
The attached Ethernet nodes send light over the glass fiber in the cable, encoding the bits as changes in the light.|Подключенные узлы Ethernet посылают свет по стекловолокну в кабеле, кодируя биты как изменения света.
|
NOTE You might expect that a standard that began at the IEEE almost 40 years ago would be stable and unchanging, but the opposite is true.|ПРИМЕЧАНИЕ. Можно было ожидать, что стандарт, появившийся в IEEE почти 40 лет назад, будет стабильным и неизменным, но верно обратное.
The IEEE, along with active industry partners, continues to develop new Ethernet standards with longer distances, different cabling options, and faster speeds.|IEEE вместе с активными отраслевыми партнерами продолжает разрабатывать новые стандарты Ethernet с более длинными расстояниями, различными вариантами кабелей и более высокими скоростями.
Check out the Ethernet Alliance web page (www.EthernetAlliance.org) and look for the roadmap for some great graphics and tables about the latest happenings with Ethernet.|Посетите веб-страницу Ethernet Alliance (www.EthernetAlliance.org) и поищите дорожную карту с отличными графиками и таблицами о последних событиях в области Ethernet.
#### Consistent Behavior over All Links Using the Ethernet Data-Link Layer
Согласованное поведение по всем каналам с использованием уровня канала передачи данных Ethernet   
__|__
--|--
|
Although Ethernet includes many physical layer standards, Ethernet acts like a single LAN technology because it uses the same data-link layer standard over all types of Ethernet physical links.|Хотя Ethernet включает в себя множество стандартов физического уровня, Ethernet действует как технология единой локальной сети, поскольку использует один и тот же стандарт уровня канала передачи данных для всех типов физических каналов Ethernet.
That standard defines a common Ethernet header and trailer. (As a reminder, the header and trailer are bytes of overhead data that Ethernet uses to do its job of sending data over a LAN.) No matter whether the data flows over a UTP cable or any kind of fiber cable, and no matter the speed, the data-link header and trailer use the same format.|Этот стандарт определяет общий заголовок и трейлер Ethernet. (Напоминаем, что заголовок и трейлер представляют собой байты служебных данных, которые Ethernet использует для выполнения своей работы по отправке данных по локальной сети.) Независимо от того, передаются ли данные по кабелю UTP или любому типу оптоволоконного кабеля, и speed, заголовок и трейлер канала передачи данных используют один и тот же формат.
|
While the physical layer standards focus on sending bits over a cable, the Ethernet data-link protocols focus on sending an Ethernet frame from source to destination Ethernet node.|В то время как стандарты физического уровня сосредоточены на отправке битов по кабелю, протоколы передачи данных Ethernet сосредоточены на отправке кадра Ethernet от источника к узлу Ethernet назначения.
|
From a data-link perspective, nodes build and forward frames.|С точки зрения канала передачи данных узлы создают и пересылают кадры.
As first defined in Chapter 1, “Introduction to TCP/IP Networking,” the term frame specifically refers to the header and trailer of a data-link protocol, plus the data encapsulated inside that header and trailer.|Как впервые было определено в главе 1 «Введение в сеть TCP / IP», термин «фрейм» конкретно относится к заголовку и завершению протокола канала передачи данных, а также к данным, инкапсулированным внутри этого заголовка и конечного элемента.
The various Ethernet nodes simply forward the frame, over all the required links, to deliver the frame to the correct destination.|Различные узлы Ethernet просто пересылают кадр по всем необходимым каналам, чтобы доставить кадр в нужное место назначения.
|
Figure 2-4 shows an example of the process.|На рис. 2-4 показан пример процесса.
In this case, PC1 sends an Ethernet frame to PC3. The frame travels over a UTP link to Ethernet switch SW1, then over fiber links to Ethernet switches SW2 and SW3, and finally over another UTP link to PC3. Note that the bits actually travel at four different speeds in this example: 10 Mbps, 1 Gbps, 10 Gbps, and 100 Mbps, respectively.|В этом случае ПК1 отправляет кадр Ethernet на ПК3. Кадр передается по каналу UTP к коммутатору Ethernet SW1, затем по оптоволоконным каналам к коммутаторам Ethernet SW2 и SW3 и, наконец, по другому каналу UTP к ПК3. Обратите внимание, что в этом примере биты фактически передаются с четырьмя разными скоростями: 10 Мбит / с, 1 Гбит / с, 10 Гбит / с и 100 Мбит / с соответственно.
|
Figure 2-4 Ethernet LAN Forwards a Data-Link Frame over Many Types of Links So, what is an Ethernet LAN? It is a combination of user devices, LAN switches, and different kinds of cabling.|Рисунок 2-4 Ethernet LAN пересылает кадр канала данных по многим типам каналов Итак, что такое локальная сеть Ethernet? Это комбинация пользовательских устройств, коммутаторов LAN и различных типов кабелей.
Each link can use different types of cables, at different speeds.|Каждое соединение может использовать разные типы кабелей с разной скоростью.
|
However, they all work together to deliver Ethernet frames from the one device on the LAN to some other device.|Однако все они работают вместе, чтобы доставлять кадры Ethernet от одного устройства в локальной сети к другому устройству.
|
The rest of this chapter takes these concepts a little deeper.|В оставшейся части этой главы эти концепции рассматриваются немного глубже.
The next section examines how to build a physical Ethernet network using UTP cabling, followed by a similar look at using fiber cabling to build Ethernet LANs. The chapter ends with some discussion of the rules for forwarding frames through an Ethernet LAN.|В следующем разделе исследуется, как построить физическую сеть Ethernet с использованием кабеля UTP, а затем аналогичным образом рассматривается использование оптоволоконного кабеля для построения локальных сетей Ethernet. Глава заканчивается обсуждением правил пересылки кадров через локальную сеть Ethernet.
### Building Physical Ethernet LANs with UTP
Создание физических локальных сетей Ethernet с UTP   
__|__
--|--
|
The next section of this chapter focuses on the individual physical links between any two Ethernet nodes, specifically those that use Unshielded Twisted Pair (UTP) cabling.|Следующий раздел этой главы посвящен отдельным физическим каналам между любыми двумя узлами Ethernet, особенно тем, которые используют кабели с неэкранированной витой парой (UTP).
Before the Ethernet network as a whole can send Ethernet frames between user devices, each node must be ready and able to send data over an individual physical link.|Прежде чем сеть Ethernet в целом сможет отправлять кадры Ethernet между пользовательскими устройствами, каждый узел должен быть готов и способен отправлять данные по отдельному физическому каналу.
|
This section focuses on the three most commonly used Ethernet standards: 10BASE-T (Ethernet), 100BASE-T (Fast Ethernet, or FE), and 1000BASE-T (Gigabit Ethernet, or GE).|В этом разделе рассматриваются три наиболее часто используемых стандарта Ethernet: 10BASE-T (Ethernet), 100BASE-T (Fast Ethernet или FE) и 1000BASE-T (Gigabit Ethernet или GE).
|
Specifically, this section looks at the details of sending data in both directions over a UTP cable.|В частности, в этом разделе рассматриваются детали отправки данных в обоих направлениях по кабелю UTP.
It then examines the specific wiring of the UTP cables used for 10-Mbps, 100-Mbps, and 1000-Mbps Ethernet.|Затем он исследует конкретную проводку кабелей UTP, используемых для 10-Мбит / с, 100-Мбит / с и 1000-Мбит / с Ethernet.
#### Transmitting Data Using Twisted Pairs
Передача данных с использованием витой пары   
__|__
--|--
|
While it is true that Ethernet sends data over UTP cables, the physical means to send the data uses electricity that flows over the wires inside the UTP cable.|Хотя это правда, что Ethernet отправляет данные по кабелям UTP, физические средства передачи данных используют электричество, которое течет по проводам внутри кабеля UTP.
To better understand how Ethernet sends data using electricity, break the idea down into two parts: how to create an electrical circuit and then how to make that electrical signal communicate 1s and 0s.|Чтобы лучше понять, как Ethernet передает данные, используя электричество, разделите идею на две части: как создать электрическую цепь, а затем как заставить этот электрический сигнал передавать единицы и нули.
|
First, to create one electrical circuit, Ethernet defines how to use the two wires inside a single twisted pair of wires, as shown in Figure 2-5.|Во-первых, для создания одной электрической цепи Ethernet определяет, как использовать два провода внутри одной витой пары проводов, как показано на рис. 2-5.
The figure does not show a UTP cable between two nodes, but instead shows two individual wires that are inside the UTP cable.|На рисунке не показан кабель UTP между двумя узлами, а показаны два отдельных провода, которые находятся внутри кабеля UTP.
|
An electrical circuit requires a complete loop, so the two nodes, using circuitry on their Ethernet ports, connect the wires in one pair to complete a loop, allowing electricity to flow.|Для электрической цепи требуется замкнутая петля, поэтому два узла, используя схемы на своих портах Ethernet, соединяют провода в одну пару, образуя петлю, позволяющую течь электричеству.
|
Figure 2-5 Creating One Electrical Circuit over One Pair to Send in One Direction To send data, the two devices follow some rules called an encoding scheme.|Рисунок 2-5. Создание одной электрической цепи по одной паре для отправки в одном направлении. Для отправки данных два устройства следуют некоторым правилам, называемым схемой кодирования.
The idea works a lot like when two people talk using the same language: The speaker says some words in a particular language, and the listener, because she speaks the same language, can understand the spoken words.|Идея во многом срабатывает, когда два человека говорят на одном языке: говорящий произносит несколько слов на определенном языке, а слушатель, поскольку он говорит на одном языке, может понимать произносимые слова.
With an encoding scheme, the transmitting node changes the electrical signal over time, while the other node, the receiver, using the same rules, interprets those changes as either 0s or 1s. (For example, 10BASE-T uses an encoding scheme that encodes a binary 0 as a transition from higher voltage to lower voltage during the middle of a 1/10,000,000th-of-a-second interval.)|При использовании схемы кодирования передающий узел изменяет электрический сигнал с течением времени, в то время как другой узел, приемник, используя те же правила, интерпретирует эти изменения как 0 или 1. (Например, 10BASE-T использует схему кодирования, которая кодирует двоичный 0 как переход от более высокого напряжения к более низкому напряжению в середине интервала 1/10 000 000-й секунды.)
|
Note that in an actual UTP cable, the wires will be twisted together, instead of being parallel as shown in Figure 2-5.|Обратите внимание, что в реальном кабеле UTP провода будут скручены вместе, а не параллельны, как показано на Рисунке 2-5.
The twisting helps solve some important physical transmission issues.|Скручивание помогает решить некоторые важные проблемы физической передачи.
When electrical current passes over any wire, it creates electromagnetic interference (EMI) that interferes with the electrical signals in nearby wires, including the wires in the same cable. (EMI between wire pairs in the same cable is called crosstalk.) Twisting the wire pairs together helps cancel out most of the EMI, so most networking physical links that use copper wires use twisted pairs.|Когда электрический ток проходит по любому проводу, он создает электромагнитные помехи (EMI), которые мешают электрическим сигналам в соседних проводах, включая провода в том же кабеле. (Электромагнитные помехи между парами проводов в одном кабеле называются перекрестными помехами.) Скручивание пар проводов вместе помогает нейтрализовать большую часть электромагнитных помех, поэтому в большинстве сетевых физических соединений, в которых используются медные провода, используются витые пары.
#### Breaking Down a UTP Ethernet Link
Разрыв соединения UTP Ethernet   
__|__
--|--
|
The term Ethernet link refers to any physical cable between two Ethernet nodes.|Термин «канал Ethernet» относится к любому физическому кабелю между двумя узлами Ethernet.
To learn about how a UTP Ethernet link works, it helps to break down the physical link into those basic pieces, as shown in Figure 2-6: the cable itself, the connectors on the ends of the cable, and the matching ports on the devices into which the connectors will be inserted.|Чтобы узнать, как работает канал Ethernet UTP, можно разбить физический канал на эти основные части, как показано на рис. 2-6: сам кабель, разъемы на концах кабеля и соответствующие порты на устройства, в которые будут вставляться разъемы.
|
Figure 2-6 Basic Components of an Ethernet Link First, think about the UTP cable itself.|Рисунок 2-6 Основные компоненты канала Ethernet Сначала подумайте о самом кабеле UTP.
The cable holds some copper wires, grouped as twisted pairs.|Кабель содержит несколько медных проводов, сгруппированных в виде витых пар.
The 10BASE-T and 100BASE-T standards require two pairs of wires, while the 1000BASE-T standard requires four pairs.|Стандарты 10BASE-T и 100BASE-T требуют двух пар проводов, а стандарт 1000BASE-T требует четырех пар.
Each wire has a color-coded plastic coating, with the wires in a pair having a color scheme.|Каждый провод имеет пластиковое покрытие с цветовой кодировкой, при этом пары проводов имеют цветовую схему.
For example, for the blue wire pair, one wire’s coating is all blue, while the other wire’s coating is blue-and-white striped.|Например, для синей пары проводов покрытие одного провода полностью синее, а покрытие другого провода - сине-белыми полосами.
|
Many Ethernet UTP cables use an RJ-45 connector on both ends.|Многие кабели Ethernet UTP используют разъем RJ-45 на обоих концах.
The RJ-45 connector has eight physical locations into which the eight wires in the cable can be inserted, called pin positions, or simply pins.|Разъем RJ-45 имеет восемь физических мест, в которые можно вставить восемь проводов кабеля, которые называются позициями контактов или просто контактами.
These pins create a place where the ends of the copper wires can touch the electronics inside the nodes at the end of the physical link so that electricity can flow.|Эти контакты создают место, где концы медных проводов могут соприкасаться с электроникой внутри узлов в конце физического соединения, так что электричество может течь.
|
NOTE If available, find a nearby Ethernet UTP cable and examine the connectors closely.|ПРИМЕЧАНИЕ. Если возможно, найдите ближайший кабель Ethernet UTP и внимательно осмотрите разъемы.
|
Look for the pin positions and the colors of the wires in the connector.|Обратите внимание на расположение контактов и цвета проводов в разъеме.
|
To complete the physical link, the nodes each need an RJ-45 Ethernet port that matches the RJ-45 connectors on the cable so that the connectors on the ends of the cable can connect to each node.|Для завершения физического соединения каждому узлу необходим порт Ethernet RJ-45, который соответствует разъемам RJ-45 на кабеле, чтобы разъемы на концах кабеля могли подключаться к каждому узлу.
PCs often include this RJ-45 Ethernet port as part of a network interface card (NIC), which can be an expansion card on the PC or can be built in to the system itself.|ПК часто включают этот порт Ethernet RJ-45 как часть сетевой карты (NIC), которая может быть картой расширения на ПК или может быть встроена в саму систему.
|
Switches typically have many RJ-45 ports because switches give user devices a place to connect to the Ethernet LAN. Figure 2-7 shows photos of the cables, connectors, and ports.|Коммутаторы обычно имеют много портов RJ-45, потому что коммутаторы предоставляют пользовательским устройствам место для подключения к локальной сети Ethernet. На Рис. 2-7 показаны фотографии кабелей, разъемов и портов.
|
Figure 2-7 RJ-45 Connectors and Ports (Ethernet NIC © Oleg Begunenko/123RF, RJ-45 Connector © Anton Samsonov/123RF)|Рисунок 2-7 Разъемы и порты RJ-45 (Ethernet NIC © Олег Бегуненко / 123RF, разъем RJ-45 © Антон Самсонов / 123RF)
|
The figure shows a connector on the left and ports on the right.|На рисунке слева показан разъем, а справа - порты.
The left shows the eight pin positions in the end of the RJ-45 connector.|Слева показаны восемь позиций контактов на конце разъема RJ-45.
The upper right shows an Ethernet NIC that is not yet installed in a computer.|В правом верхнем углу показана сетевая карта Ethernet, которая еще не установлена ​​на компьютере.
The lower-right part of the figure shows the side of a Cisco switch, with multiple RJ-45 ports, allowing multiple devices to easily connect to the Ethernet network.|В нижней правой части рисунка показана сторона коммутатора Cisco с несколькими портами RJ-45, что позволяет нескольким устройствам легко подключаться к сети Ethernet.
|
Finally, while RJ-45 connectors with UTP cabling can be common, Cisco LAN switches often support other types of connectors as well.|Наконец, хотя разъемы RJ-45 с кабелями UTP могут быть обычным явлением, коммутаторы Cisco LAN часто поддерживают и другие типы разъемов.
When you buy one of the many models of Cisco switches, you need to think about the mix and numbers of each type of physical ports you want on the switch.|Когда вы покупаете одну из множества моделей коммутаторов Cisco, вам необходимо подумать о сочетании и количестве физических портов каждого типа, которые вы хотите использовать в коммутаторе.
|
To give its customers flexibility as to the type of Ethernet links, even after the customer has bought the switch, Cisco switches include some physical ports whose port hardware (the transceiver) can be changed later, after you purchase the switch.|Чтобы предоставить своим клиентам гибкость в отношении типа каналов Ethernet, даже после того, как заказчик купил коммутатор, коммутаторы Cisco включают некоторые физические порты, оборудование портов которых (приемопередатчик) может быть изменено позже, после покупки коммутатора.
|
For example, Figure 2-8 shows a photo of a Cisco switch with one of the swappable transceivers.|Например, на рис. 2-8 показана фотография коммутатора Cisco с одним из заменяемых трансиверов.
|
In this case, the figure shows an enhanced small form-factor pluggable (SFP+) transceiver, which runs at 10 Gbps, just outside two SFP+ slots on a Cisco 3560CX switch.|В этом случае на рисунке показан расширенный съемный приемопередатчик малого форм-фактора (SFP +), который работает на скорости 10 Гбит / с, сразу за двумя слотами SFP + на коммутаторе Cisco 3560CX.
The SFP+ itself is the silver-colored part below the switch, with a black cable connected to it.|Сам SFP + представляет собой серебристую часть под коммутатором, к которой подключен черный кабель.
|
Cable SFP+|Кабель SFP +
|
Figure 2-8 10-Gbps SFP+ with Cable Sitting Just Outside a Catalyst 3560CX Switch Gigabit Ethernet Interface Converter (GBIC): The original form factor for a removable transceiver for Gigabit interfaces; larger than SFPs Small Form Pluggable (SFP): The replacement for GBICs, used on Gigabit interfaces, with a smaller size, taking less space on the side of the networking card or switch.|Рисунок 2-8 10-Гбит / с SFP + с кабелем, проложенным непосредственно за пределами коммутатора Catalyst 3560CX Преобразователь интерфейса Gigabit Ethernet (GBIC): исходный форм-фактор съемного трансивера для интерфейсов Gigabit Ethernet; больше, чем SFP Small Form Pluggable (SFP): замена GBIC, используемых на гигабитных интерфейсах, с меньшим размером, занимающим меньше места на стороне сетевой карты или коммутатора.
|
Small Form Pluggable Plus (SFP+): Same size as the SFP, but used on 10-Gbps interfaces.|Small Form Pluggable Plus (SFP +): тот же размер, что и SFP, но используется на интерфейсах 10 Гбит / с.
|
(The Plus refers to the increase in speed compared to SFPs.)|(Плюс означает увеличение скорости по сравнению с SFP.)
#### UTP Cabling Pinouts for 10BASE-T and 100BASE-T
Выводы кабелей UTP для 10BASE-T и 100BASE-T   
__|__
--|--
|
So far in this section, you have learned about the equivalent of how to drive a truck on a 1000-acre ranch: You could drive the truck all over the ranch, any place you wanted to go, and the police would not mind.|До сих пор в этом разделе вы узнали о том, как водить грузовик на ранчо площадью 1000 акров: вы можете проехать на грузовике по всему ранчо, в любое место, куда хотите, и полиция не будет возражать.
However, as soon as you get on the public roads, the police want you to behave and follow the rules.|Однако, как только вы выезжаете на дорогу общего пользования, полиция требует, чтобы вы вели себя хорошо и соблюдали правила.
Similarly, so far this chapter has discussed the general principles of how to send data, but it has not yet detailed some important rules for Ethernet cabling: the rules of the road so that all the devices send data using the right wires inside the cable.|Точно так же до сих пор в этой главе обсуждались общие принципы отправки данных, но еще не были подробно описаны некоторые важные правила для кабельной разводки Ethernet: правила дорожного движения, согласно которым все устройства отправляют данные, используя правильные провода внутри кабеля.
|
This next topic discusses some of those rules, specifically for the 10-Mbps 10BASE-T and the 100-Mbps 100BASE-T.|В следующем разделе обсуждаются некоторые из этих правил, особенно для 10BASE-T со скоростью 10 Мбит / с и 100BASE-T со скоростью 100 Мбит / с.
Both use UTP cabling in similar ways (including the use of only two wire pairs).|Оба используют кабели UTP аналогичным образом (включая использование только двух пар проводов).
A short comparison of the wiring for 1000BASE-T (Gigabit Ethernet), which uses four pairs, follows.|Ниже приводится краткое сравнение проводки 1000BASE-T (Gigabit Ethernet), в которой используются четыре пары.
##### Straight-Through Cable Pinout
Распиновка прямого кабеля   
__|__
--|--
|
10BASE-T and 100BASE-T use two pairs of wires in a UTP cable, one for each direction, as shown in Figure 2-9.|10BASE-T и 100BASE-T используют две пары проводов в кабеле UTP, по одной для каждого направления, как показано на Рисунке 2-9.
The figure shows four wires, all of which sit inside a single UTP cable that connects a PC and a LAN switch.|На рисунке показаны четыре провода, каждый из которых проложен внутри одного кабеля UTP, соединяющего ПК и коммутатор LAN.
In this example, the PC on the left transmits using the top pair, and the switch on the right transmits using the bottom pair.|В этом примере ПК слева передает с использованием верхней пары, а переключатель справа передает с использованием нижней пары.
|
Figure 2-9 Using One Pair for Each Transmission Direction with 10- and 100-Mbps Ethernet For correct transmission over the link, the wires in the UTP cable must be connected to the correct pin positions in the RJ-45 connectors.|Рисунок 2-9 Использование одной пары для каждого направления передачи с Ethernet 10 и 100 Мбит / с. Для правильной передачи по каналу провода кабеля UTP должны быть подключены к правильным позициям контактов в разъемах RJ-45.
For example, in Figure 2-9, the transmitter on the PC on the left must know the pin positions of the two wires it should use to transmit.|Например, на рис. 2-9 передатчик на ПК слева должен знать положения контактов двух проводов, которые он должен использовать для передачи.
|
Those two wires must be connected to the correct pins in the RJ-45 connector on the switch so that the switch’s receiver logic can use the correct wires.|Эти два провода должны быть подключены к правильным контактам в разъеме RJ-45 на коммутаторе, чтобы логика приемника коммутатора могла использовать правильные провода.
|
To understand the wiring of the cable—which wires need to be in which pin positions on both ends of the cable—you need to first understand how the NICs and switches work.|Чтобы понять проводку кабеля - какие провода должны быть в каких положениях контактов на обоих концах кабеля - вам нужно сначала понять, как работают сетевые адаптеры и коммутаторы.
As a rule, Ethernet NIC transmitters use the pair connected to pins 1 and 2; the NIC receivers use a pair of wires at pin positions 3 and 6.|Как правило, передатчики Ethernet NIC используют пару, подключенную к контактам 1 и 2; приемники NIC используют пару проводов с контактами 3 и 6.
LAN switches, knowing those facts about what Ethernet NICs do, do the opposite: Their receivers use the wire pair at pins 1 and 2, and their transmitters use the wire pair at pins 3 and 6.|Коммутаторы LAN, зная эти факты о том, что делают сетевые адаптеры Ethernet, поступают наоборот: их приемники используют пару проводов на контактах 1 и 2, а их передатчики используют пару проводов на контактах 3 и 6.
|
To allow a PC NIC to communicate with a switch, the UTP cable must also use a straightthrough cable pinout.|Чтобы сетевой адаптер ПК мог обмениваться данными с коммутатором, в кабеле UTP также должна использоваться прямая разводка выводов кабеля.
The term pinout refers to the wiring of which color wire is placed in each of the eight numbered pin positions in the RJ-45 connector.|Термин «распиновка» относится к разводке, цветной провод которой помещается в каждую из восьми пронумерованных позиций контактов в разъеме RJ-45.
An Ethernet straightthrough cable connects the wire at pin 1 on one end of the cable to pin 1 at the other end of the cable; the wire at pin 2 needs to connect to pin 2 on the other end of the cable; pin 3 on one end connects to pin 3 on the other, and so on, as seen in Figure 2-10.|Прямой кабель Ethernet соединяет провод на контакте 1 на одном конце кабеля с контактом 1 на другом конце кабеля; провод на контакте 2 необходимо подключить к контакту 2 на другом конце кабеля; контакт 3 на одном конце соединяется с контактом 3 на другом и так далее, как показано на рисунке 2-10.
Also, it uses the wires in one wire pair at pins 1 and 2, and another pair at pins 3 and 6.|Кроме того, он использует провода одной пары проводов на выводах 1 и 2, а другой пары - на выводах 3 и 6.
|
Ports 1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8 Connectors Figure 2-10 10BASE-T and 100BASE-T Straight-Through Cable Pinout Figure 2-11 shows one final perspective on the straight-through cable pinout.|Порты 1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8 Разъемы Рисунок 2-10 Схема контактов прямого кабеля 10BASE-T и 100BASE-T На Рис. 2-11 показан последний вид распиновки прямого кабеля.
In this case, PC Larry connects to a LAN switch.|В этом случае ПК Ларри подключается к коммутатору локальной сети.
Note that the figure again does not show the UTP cable, but instead shows the wires that sit inside the cable, to emphasize the idea of wire pairs and pins.|Обратите внимание, что на рисунке снова не показан кабель UTP, а вместо этого показаны провода, которые находятся внутри кабеля, чтобы подчеркнуть идею пар проводов и контактов.
|
Figure 2-11 Ethernet Straight-Through Cable Concept A straight-through cable works correctly when the nodes use opposite pairs for transmitting data.|Рисунок 2-11 Концепция прямого кабеля Ethernet Прямой кабель работает правильно, когда узлы используют противоположные пары для передачи данных.
However, when two like devices connect to an Ethernet link, they both transmit on the same pins.|Однако, когда два одинаковых устройства подключаются к каналу Ethernet, они оба передают данные на одних и тех же контактах.
In that case, you then need another type of cabling pinout called a crossover cable.|В этом случае вам понадобится другой тип разводки выводов, называемый перекрестным кабелем.
The crossover cable pinout crosses the pair at the transmit pins on each device to the receive pins on the opposite device.|Распиновка перекрестного кабеля пересекает пару выводов передачи на каждом устройстве с выводами приема на противоположном устройстве.
|
While that previous sentence is true, this concept is much clearer with a figure such as Figure 2-12.|Несмотря на то, что предыдущее предложение верно, эта концепция намного яснее с фигурами, такими как рис. 2-12.
The figure shows what happens on a link between two switches.|На рисунке показано, что происходит при соединении двух коммутаторов.
The two switches both transmit on the pair at pins 3 and 6, and they both receive on the pair at pins 1 and 2.|Оба переключателя передают данные по паре на контакты 3 и 6, и оба получают сигнал на паре на контактах 1 и 2.
|
So, the cable must connect a pair at pins 3 and 6 on each side to pins 1 and 2 on the other side, connecting to the other node’s receiver logic.|Таким образом, кабель должен соединить пару контактов 3 и 6 на каждой стороне с контактами 1 и 2 на другой стороне, подключаясь к логике приемника другого узла.
The top of the figure shows the literal pinouts, and the bottom half shows a conceptual diagram.|Вверху рисунка показаны буквальные распиновки, а в нижней половине - концептуальная схема.
|
Figure 2-12 Crossover Ethernet Cable|Рисунок 2-12 Перекрестный кабель Ethernet
##### Choosing the Right Cable Pinouts
Выбор правильных выводов кабеля   
__|__
--|--
|
For the exam, you should be well prepared to choose which type of cable (straight-through or crossover) is needed in each part of the network.|К экзамену вы должны быть хорошо подготовлены к тому, чтобы выбрать, какой тип кабеля (прямой или перекрестный) необходим в каждой части сети.
The key is to know whether a device acts like a PC NIC, transmitting at pins 1 and 2, or like a switch, transmitting at pins 3 and 6.|Ключ в том, чтобы знать, действует ли устройство как сетевая карта ПК, передавая сигналы на выводах 1 и 2, или как переключатель, передавая сигналы на выводах 3 и 6.
|
Then, just apply the following logic:|Затем просто примените следующую логику:
|
Crossover cable: If the endpoints transmit on the same pin pair Straight-through cable: If the endpoints transmit on different pin pairs Table 2-3 lists the devices and the pin pairs they use, assuming that they use 10BASE-T and 100BASE-T.|Перекрестный кабель: если конечные точки осуществляют передачу по одной и той же паре контактов. Прямой кабель: если конечные точки осуществляют передачу на разных парах контактов. В таблице 2-3 перечислены устройства и пары контактов, которые они используют, при условии, что они используют 10BASE-T и 100BASE-T .
|
Table 2-3 A 10BASE-T and 100BASE-T Pin Pairs Used Table end.|Таблица 2-3 Используемые пары контактов 10BASE-T и 100BASE-T Конец таблицы.
|
For example, Figure 2-13 shows a campus LAN in a single building.|Например, на рис. 2-13 показана локальная сеть кампуса в одном здании.
In this case, several straight-through cables are used to connect PCs to switches.|В этом случае для подключения ПК к коммутаторам используется несколько прямых кабелей.
In addition, the cables connecting the switches require crossover cables.|Кроме того, для кабелей, соединяющих коммутаторы, требуются перекрестные кабели.
|
Figure 2-13 Typical Uses for Straight-Through and Crossover Ethernet Cables NOTE If you have some experience with installing LANs, you might be thinking that you have used the wrong cable before (straight-through or crossover), but the cable worked.|Рис. 2-13 Типичное использование прямых и перекрестных кабелей Ethernet ПРИМЕЧАНИЕ Если у вас есть опыт установки локальных сетей, вы можете подумать, что раньше использовали неправильный кабель (прямой или перекрестный), но кабель работал.
|
Cisco switches have a feature called auto-mdix that notices when the wrong cable is used and automatically changes its logic to make the link work.|Коммутаторы Cisco имеют функцию auto-mdix, которая замечает, когда используется неправильный кабель, и автоматически изменяет свою логику, чтобы соединение работало.
However, for the exams, be ready to identify whether the correct cable is shown in the figures.|Однако перед экзаменом будьте готовы определить, правильный ли кабель показан на рисунках.
#### UTP Cabling Pinouts for 1000BASE-T
Выводы кабелей UTP для 1000BASE-T   
__|__
--|--
|
1000BASE-T (Gigabit Ethernet) differs from 10BASE-T and 100BASE-T as far as the cabling and pinouts.|1000BASE-T (Gigabit Ethernet) отличается от 10BASE-T и 100BASE-T кабельной разводкой и распиновкой.
First, 1000BASE-T requires four wire pairs.|Во-первых, для 1000BASE-T требуется четыре пары проводов.
Second, it uses more advanced electronics that allow both ends to transmit and receive simultaneously on each wire pair.|Во-вторых, он использует более совершенную электронику, которая позволяет обоим концам одновременно передавать и принимать по каждой паре проводов.
|
However, the wiring pinouts for 1000BASE-T work almost identically to the earlier standards, adding details for the additional two pairs.|Тем не менее, разводка выводов для 1000BASE-T работает почти так же, как и в более ранних стандартах, с добавлением деталей для дополнительных двух пар.
|
The straight-through cable for 1000BASE-T uses the four wire pairs to create four circuits, but the pins need to match.|Прямой кабель для 1000BASE-T использует четыре пары проводов для создания четырех цепей, но контакты должны совпадать.
It uses the same pinouts for two pairs as do the 10BASE-T and 100BASE-T standards, and it adds a pair at pins 4 and 5 and the final pair at pins 7 and 8, as shown in Figure 2-14.|Он использует те же выводы для двух пар, что и стандарты 10BASE-T и 100BASE-T, и добавляет пару к контактам 4 и 5 и последнюю пару к контактам 7 и 8, как показано на рисунке 2-14.
|
Figure 2-14 Four-Pair Straight-Through Cable to 1000BASE-T The Gigabit Ethernet crossover cable crosses the same two-wire pairs as the crossover cable for the other types of Ethernet (the pairs at pins 1,2 and 3,6).|Рисунок 2-14 Четырехпарный прямой кабель для 1000BASE-T Перекрестный кабель Gigabit Ethernet пересекает те же двухпроводные пары, что и перекрестный кабель для других типов Ethernet (пары на контактах 1,2 и 3,6) .
It also crosses the two new pairs as well (the pair at pins 4,5 with the pair at pins 7,8).|Он также пересекает две новые пары (пара на контактах 4,5 с парой на контактах 7,8).
### Building Physical Ethernet LANs with Fiber
Создание физических локальных сетей Ethernet с использованием оптоволокна   
__|__
--|--
|
The capability of many UTP-based Ethernet standards to use a cable length up to 100 meters means that the majority of Ethernet cabling in an enterprise uses UTP cables.|Способность многих стандартов Ethernet на основе UTP использовать кабель длиной до 100 метров означает, что большинство кабелей Ethernet на предприятии используют кабели UTP.
The distance from an Ethernet switch to every endpoint on the floor of a building will likely be less than 100m.|Расстояние от коммутатора Ethernet до каждой конечной точки на этаже здания, вероятно, будет менее 100 м.
In some cases, however, an engineer might prefer to use fiber cabling for some links in an Ethernet LAN, first to reach greater distances, but for other reasons as well.|Однако в некоторых случаях инженер может предпочесть использовать оптоволоконные кабели для некоторых каналов в локальной сети Ethernet, сначала для достижения больших расстояний, но также и по другим причинам.
This next section examines a few of the tradeoffs after discussing the basics of how to transmit data over fiber cabling.|В следующем разделе рассматриваются некоторые компромиссы после обсуждения основ передачи данных по оптоволоконным кабелям.
#### Fiber Cabling Transmission Concepts
Концепции передачи по оптоволоконным кабелям   
__|__
--|--
|
Fiber-optic cabling uses glass as the medium through which light passes, varying that light over time to encode 0s and 1s.|В волоконно-оптических кабелях стекло используется в качестве среды, через которую проходит свет, изменяя этот свет с течением времени, чтобы кодировать нули и единицы.
It might seem strange at first to use glass given that most of us think of glass in windows.|Сначала может показаться странным использование стекла, учитывая, что большинство из нас думает о стекле в окнах.
Window glass is hard, unbending, and if you hit or bend it enough, the glass will probably shatter—all bad characteristics for a cabling material.|Оконное стекло твердое, негнущееся, и если вы сильно ударите или согнете его, оно, вероятно, разобьется - все это плохие характеристики для материала кабельной разводки.
|
Instead, fiber-optic cables use fiberglass, which allows a manufacturer to spin a long thin string (fiber) of flexible glass.|Вместо этого в волоконно-оптических кабелях используется стекловолокно, которое позволяет производителю прядать длинную тонкую нить (волокно) из гибкого стекла.
A fiber-optic cable holds the fiber in the middle of the cable, allowing the light to pass through the glass—which is a very important attribute for the purposes of sending data.|Волоконно-оптический кабель удерживает волокно в середине кабеля, позволяя свету проходить через стекло, что является очень важным атрибутом при передаче данных.
|
Although sending data through a glass fiber works well, the glass fiber by itself needs some help.|Хотя отправка данных через стекловолокно работает хорошо, стекловолокно само по себе требует некоторой помощи.
The glass could break, so the glass fiber needs some protection and strengthening.|Стекло может разбиться, поэтому стекловолокну необходимо защитить и укрепить.
|
Figure 2-15 shows a cutout with the components of a fiber cable for perspective.|На Рис. 2-15 показан разрез с компонентами оптоволоконного кабеля для обзора.
|
Figure 2-15 Components of a Fiber-Optic Cable The three outer layers of the cable protect the interior of the cable and make the cables easier to install and manage, while the inner cladding and core work together to create the environment to allow transmission of light over the cable.|Рисунок 2-15 Компоненты волоконно-оптического кабеля Три внешних слоя кабеля защищают внутреннюю часть кабеля и упрощают установку и управление кабелями, в то время как внутренняя оболочка и сердечник работают вместе, создавая среду, позволяющую передавать свет над кабелем.
A light source, called the optical transmitter, shines a light into the core.|Источник света, называемый оптическим передатчиком, направляет свет на сердечник.
Light can pass through the core; however, light reflects off the cladding back into the core.|Свет может проходить через сердцевину; однако свет отражается от оболочки обратно в сердцевину.
Figure 2-16 shows an example with a light emitting diode (LED) transmitter.|На рисунке 2-16 показан пример передатчика на светодиодах (LED).
You can see how the cladding reflects the light back into the core as it travels through the core.|Вы можете видеть, как оболочка отражает свет обратно в сердцевину, когда он проходит через сердцевину.
|
Figure 2-16 Transmission on Multimode Fiber with Internal Reflection The figure shows the normal operation of a multimode fiber, characterized by the fact that the cable allows for multiple angles (modes) of light waves entering the core.|Рисунок 2-16 Передача по многомодовому волокну с внутренним отражением На рисунке показана нормальная работа многомодового волокна, характеризующаяся тем, что кабель допускает попадание световых волн в сердцевину под разными углами (модами).
|
In contrast, single-mode fiber uses a smaller-diameter core, around one-fifth the diameter of common multimode cables (see Figure 2-17).|В отличие от этого, в одномодовом волокне используется сердцевина меньшего диаметра, примерно в пятую часть диаметра обычных многомодовых кабелей (см. Рисунок 2-17).
To transmit light into a much smaller core, a laser-based transmitter sends light at a single angle (hence the name single-mode).|Чтобы передать свет в ядро ​​гораздо меньшего размера, лазерный передатчик излучает свет под одним углом (отсюда и название - одномодовый).
|
Figure 2-17 Transmission on Single-Mode Fiber with Laser Transmitter Both multimode and single-mode cabling have important roles in Ethernet and meet different needs.|Рисунок 2-17 Передача по одномодовому оптоволокну с лазерным передатчиком Как многомодовые, так и одномодовые кабели играют важную роль в Ethernet и удовлетворяют различные потребности.
Multimode improves the maximum distances over UTP, and it uses less expensive transmitters as compared with single-mode.|Многомодовый улучшает максимальные расстояния по UTP и использует менее дорогие передатчики по сравнению с одномодовым.
Standards do vary; for instance, the standards for 10 Gigabit Ethernet over Fiber allow for distances up to 400m, which would often allow for connection of devices in different buildings in the same office park.|Стандарты действительно различаются; например, стандарты для 10 Gigabit Ethernet по оптоволокну допускают расстояния до 400 м, что часто позволяет подключать устройства в разных зданиях в одном офисном парке.
Single-mode allows distances into the tens of kilometers, but with slightly more expensive SFP/SFP+ hardware.|Одномодовый режим позволяет использовать расстояния до десятков километров, но с немного более дорогим оборудованием SFP / SFP +.
|
To transmit between two devices, you need two cables, one for each direction, as shown in Figure 2-18.|Для передачи между двумя устройствами вам понадобятся два кабеля, по одному для каждого направления, как показано на Рисунке 2-18.
The concept works much like having two electrical circuits with the original UTP Ethernet standards.|Эта концепция очень похожа на две электрические цепи с оригинальными стандартами UTP Ethernet.
Note that the transmit port on one device connects to a cable that connects to a receive port on the other device, and vice versa with the other cable.|Обратите внимание, что порт передачи на одном устройстве подключается к кабелю, который подключается к порту приема на другом устройстве, и наоборот, с другим кабелем.
|
Figure 2-18 Two Fiber Cables with Tx Connected to Rx on Each Cable|Рисунок 2-18 Два оптоволоконных кабеля с передатчиком, подключенным к приемнику на каждом кабеле
#### Using Fiber with Ethernet
Использование волокна с Ethernet   
__|__
--|--
|
To use fiber with Ethernet switches, you need to use a switch with either built-in ports that support a particular optical Ethernet standard, or a switch with modular ports that allow you to change the Ethernet standard used on the port.|Чтобы использовать оптоволокно с коммутаторами Ethernet, необходимо использовать коммутатор либо со встроенными портами, поддерживающими определенный оптический стандарт Ethernet, либо коммутатор с модульными портами, которые позволяют изменять стандарт Ethernet, используемый для порта.
Refer back to Figure 2-8, which shows a photo of a switch with two SFP+ ports, into which you could insert any of the supported SFP+ modules.|Вернитесь к рис. 2-8, на котором показана фотография коммутатора с двумя портами SFP +, в которые можно вставить любой из поддерживаемых модулей SFP +.
Those SFP+ ports support a variety of 10-Gbps standards like those listed in Table 2-4.|Эти порты SFP + поддерживают различные стандарты 10 Гбит / с, например, перечисленные в Таблице 2-4.
|
Table 2-4 A Sampling of IEEE 802.3 10-Gbps Fiber Standards Table end.|Таблица 2-4 Выборка стандартов волокна IEEE 802.3 10 Гбит / с Конец таблицы.
|
1 The maximum distances are based on the IEEE standards with no repeaters.|1 Максимальные расстояния основаны на стандартах IEEE без повторителей.
|
For instance, to build an Ethernet LAN in an office park, you might need to use some multimode and single-mode fiber links.|Например, для создания локальной сети Ethernet в офисном парке вам может потребоваться несколько многомодовых и одномодовых оптоволоконных линий.
In fact, many office parks might already have fiber cabling installed for the expected future use by the tenants in the buildings.|Фактически, во многих офисных парках уже могут быть проложены оптоволоконные кабели для предполагаемого использования в зданиях арендаторами в будущем.
If each building was within a few hundred meters of at least one other building, you could use multimode fiber between the buildings and connect switches to create your LAN.|Если каждое здание находится в пределах нескольких сотен метров от хотя бы одного другого здания, вы можете использовать многомодовое оптоволокно между зданиями и подключать коммутаторы для создания вашей локальной сети.
|
NOTE Outside the need to study for CCNA, if you need to look more deeply at fiber Ethernet and SFP/SFP+, check out tmgmatrix.cisco.com as a place to search for and learn about compatible SFP/SFP+ hardware from Cisco.|ПРИМЕЧАНИЕ Помимо необходимости изучения CCNA, если вам нужно более глубоко изучить оптоволоконный Ethernet и SFP / SFP +, посетите tmgmatrix.cisco.com как место для поиска и изучения совместимого оборудования SFP / SFP + от Cisco.
|
Although distance might be the first criterion to consider when thinking about whether to use UTP or fiber cabling, a few other tradeoffs exist as well.|Хотя расстояние может быть первым критерием, который следует учитывать при размышлениях о том, использовать ли UTP или оптоволоконный кабель, существует также несколько других компромиссов.
UTP wins again on cost, because the cost goes up as you move from UTP, to multimode, and then to single-mode, due to the extra cost for the transmitters like the SFP and SFP+ modules.|UTP снова выигрывает по стоимости, потому что стоимость увеличивается при переходе от UTP к многомодовой, а затем к одномодовой из-за дополнительных затрат на передатчики, такие как модули SFP и SFP +.
UTP has some negatives, however.|Однако у UTP есть и недостатки.
First, UTP might work poorly in some electrically noisy environments such as factories, because UTP can be affected by electromagnetic interference (EMI). Also, UTP cables emit a faint signal outside the cable, so highly secure networks may choose to use fiber, which does not create similar emissions, to make the network more secure.|Во-первых, UTP может плохо работать в некоторых электрически шумных средах, таких как фабрики, потому что на UTP могут влиять электромагнитные помехи (EMI). Кроме того, кабели UTP излучают слабый сигнал за пределами кабеля, поэтому высокозащищенные сети могут использовать оптоволокно, которое не создает подобных излучений, чтобы сделать сеть более безопасной.
Table 2-5 summarizes these tradeoffs.|Таблица 2-5 суммирует эти компромиссы.
|
Table 2-5 Comparisons Between UTP, MM, and SM Ethernet Cabling Table end.|Таблица 2-5 Сравнение кабелей Ethernet UTP, MM и SM Конец таблицы.
### Sending Data in Ethernet Networks
Отправка данных в сетях Ethernet   
__|__
--|--
|
Although physical layer standards vary quite a bit, other parts of the Ethernet standards work the same regardless of the type of physical Ethernet link.|Хотя стандарты физического уровня довольно сильно различаются, другие части стандартов Ethernet работают одинаково, независимо от типа физического канала Ethernet.
Next, this final major section of this chapter looks at several protocols and rules that Ethernet uses regardless of the type of link.|Далее, в этом последнем основном разделе этой главы рассматриваются несколько протоколов и правил, которые использует Ethernet независимо от типа канала.
In particular, this section examines the details of the Ethernet data-link layer protocol, plus how Ethernet nodes, switches, and hubs forward Ethernet frames through an Ethernet LAN.|В частности, в этом разделе подробно рассматривается протокол уровня канала передачи данных Ethernet, а также то, как узлы, коммутаторы и концентраторы Ethernet пересылают кадры Ethernet через локальную сеть Ethernet.
#### Ethernet Data-Link Protocols
Протоколы передачи данных Ethernet   
__|__
--|--
|
One of the most significant strengths of the Ethernet family of protocols is that these protocols use the same data-link standard.|Одна из самых сильных сторон семейства протоколов Ethernet состоит в том, что в этих протоколах используется один и тот же стандарт передачи данных.
In fact, the core parts of the data-link standard date back to the original Ethernet standards.|Фактически, основные части стандарта канала передачи данных восходят к исходным стандартам Ethernet.
|
The Ethernet data-link protocol defines the Ethernet frame: an Ethernet header at the front, the encapsulated data in the middle, and an Ethernet trailer at the end.|Протокол канала передачи данных Ethernet определяет фрейм Ethernet: заголовок Ethernet в передней части, инкапсулированные данные в середине и трейлер Ethernet в конце.
Ethernet actually defines a few alternate formats for the header, with the frame format shown in Figure 2-19 being commonly used today.|Ethernet фактически определяет несколько альтернативных форматов для заголовка, при этом формат кадра, показанный на рис. 2-19, обычно используется сегодня.
|
Figure 2-19 Commonly Used Ethernet Frame Format While all the fields in the frame matter, some matter more to the topics discussed in this book.|Рис. 2-19. Обычно используемый формат кадра Ethernet Хотя все поля кадра имеют значение, некоторые имеют большее значение для тем, обсуждаемых в этой книге.
Table 2-6 lists the fields in the header and trailer and a brief description for reference, with the upcoming pages including more detail about a few of these fields.|В таблице 2-6 перечислены поля в заголовке и трейлере, а также краткое описание для справки, а на следующих страницах приведены более подробные сведения о некоторых из этих полей.
|
Table 2-6 IEEE 802.3 Ethernet Header and Trailer Fields Table end.|Таблица 2-6 Поля заголовка и трейлера Ethernet IEEE 802.3 Конец таблицы.
|
1 The IEEE 802.3 specification limits the data portion of the 802.3 frame to a minimum of 46 and a maximum of 1500 bytes.|1 Спецификация IEEE 802.3 ограничивает часть данных кадра 802.3 минимум 46 и максимум 1500 байтами.
The term maximum transmission unit (MTU) defines the maximum Layer 3 packet that can be sent over a medium.|Термин максимальный блок передачи (MTU) определяет максимальный пакет уровня 3, который может быть отправлен по среде.
Because the Layer 3 packet rests inside the data portion of an Ethernet frame, 1500 bytes is the largest IP MTU allowed over an Ethernet.|Поскольку пакет уровня 3 находится внутри части данных кадра Ethernet, 1500 байтов - это наибольший размер IP MTU, разрешенный для Ethernet.
##### Ethernet Addressing
Адресация Ethernet   
__|__
--|--
|
The source and destination Ethernet address fields play a huge role in how Ethernet LANs work.|Поля адресов Ethernet источника и назначения играют огромную роль в работе локальных сетей Ethernet.
The general idea for each is relatively simple: the sending node puts its own address in the source address field and the intended Ethernet destination device’s address in the destination address field.|Общая идея для каждого из них относительно проста: отправляющий узел помещает свой собственный адрес в поле адреса источника и адрес предполагаемого устройства назначения Ethernet в поле адреса назначения.
The sender transmits the frame, expecting that the Ethernet LAN, as a whole, will deliver the frame to that correct destination.|Отправитель передает кадр, ожидая, что локальная сеть Ethernet в целом доставит его в правильное место назначения.
|
Ethernet addresses, also called Media Access Control (MAC) addresses, are 6-byte-long (48-bit-long) binary numbers.|Адреса Ethernet, также называемые адресами управления доступом к среде (MAC), представляют собой двоичные числа длиной 6 байт (48 бит).
For convenience, most computers list MAC addresses as 12-digit hexadecimal numbers.|Для удобства большинство компьютеров указывают MAC-адреса в виде 12-значных шестнадцатеричных чисел.
Cisco devices typically add some periods to the number for easier readability as well; for example, a Cisco switch might list a MAC address as 0000.0C12.3456.|Устройства Cisco обычно добавляют несколько точек к числу для облегчения чтения; например, коммутатор Cisco может указать MAC-адрес как 0000.0C12.3456.
|
Most MAC addresses represent a single NIC or other Ethernet port, so these addresses are often called a unicast Ethernet address.|Большинство MAC-адресов представляют собой один сетевой адаптер или другой порт Ethernet, поэтому эти адреса часто называют одноадресными адресами Ethernet.
The term unicast is simply a formal way to refer to the fact that the address represents one interface to the Ethernet LAN. (This term also contrasts with two other types of Ethernet addresses, broadcast and multicast, which will be defined later in this section.)|Термин одноадресная передача - это просто формальный способ обозначить тот факт, что адрес представляет один интерфейс к локальной сети Ethernet. (Этот термин также контрастирует с двумя другими типами адресов Ethernet, широковещательными и многоадресными, которые будут определены позже в этом разделе.)
|
The entire idea of sending data to a destination unicast MAC address works well, but it works only if all the unicast MAC addresses are unique.|Сама идея отправки данных на одноадресный MAC-адрес назначения работает хорошо, но работает только в том случае, если все одноадресные MAC-адреса уникальны.
If two NICs tried to use the same MAC address, there could be confusion. (The problem would be like the confusion caused to the postal service if you and I both tried to use the same mailing address—would the postal service deliver mail to your house or mine?) If two PCs on the same Ethernet tried to use the same MAC address, to which PC should frames sent to that MAC address be delivered?|Если два сетевых адаптера попытаются использовать один и тот же MAC-адрес, может возникнуть путаница. (Проблема была бы похожа на путаницу, вызванную почтовой службой, если бы вы и я оба попытались использовать один и тот же почтовый адрес - будет ли почтовая служба доставлять почту в ваш дом или в мой?) Если два компьютера в одном Ethernet попытаются использовать тот же MAC-адрес, на какой компьютер следует доставлять кадры, отправленные на этот MAC-адрес?
|
Ethernet solves this problem using an administrative process so that, at the time of manufacture, all Ethernet devices are assigned a universally unique MAC address.|Ethernet решает эту проблему с помощью административного процесса, так что во время производства всем устройствам Ethernet назначается универсальный уникальный MAC-адрес.
Before a manufacturer can build Ethernet products, it must ask the IEEE to assign the manufacturer a universally unique 3-byte code, called the organizationally unique identifier (OUI). The manufacturer agrees to give all NICs (and other Ethernet products) a MAC address that begins with its assigned 3-byte OUI. The manufacturer also assigns a unique value for the last 3 bytes, a number that manufacturer has never used with that OUI. As a result, the MAC address of every device in the universe is unique.|Прежде чем производитель сможет создавать продукты Ethernet, он должен попросить IEEE назначить производителю универсально уникальный 3-байтовый код, называемый уникальным идентификатором организации (OUI). Производитель соглашается предоставить всем сетевым адаптерам (и другим продуктам Ethernet) MAC-адрес, который начинается с назначенного ему 3-байтового OUI. Производитель также присваивает уникальное значение последним 3 байтам, число, которое производитель никогда не использовал с этим OUI. В результате MAC-адрес каждого устройства во вселенной уникален.
|
NOTE The IEEE also calls these universal MAC addresses global MAC addresses.|ПРИМЕЧАНИЕ IEEE также называет эти универсальные MAC-адреса глобальными MAC-адресами.
|
Figure 2-20 shows the structure of the unicast MAC address, with the OUI.|На рисунке 2-20 показана структура одноадресного MAC-адреса с OUI.
|
Figure 2-20 Structure of Unicast Ethernet Addresses Ethernet addresses go by many names: LAN address, Ethernet address, hardware address, burned-in address, physical address, universal address, or MAC address.|Рисунок 2-20 Структура одноадресных адресов Ethernet Адреса Ethernet имеют множество имен: адрес LAN, адрес Ethernet, аппаратный адрес, встроенный адрес, физический адрес, универсальный адрес или MAC-адрес.
For example, the term burned-in address (BIA) refers to the idea that a permanent MAC address has been encoded (burned into) the ROM chip on the NIC. As another example, the IEEE uses the term universal address to emphasize the fact that the address assigned to a NIC by a manufacturer should be unique among all MAC addresses in the universe.|Например, термин записанный адрес (BIA) относится к идее, что постоянный MAC-адрес был закодирован (записан в) микросхему ПЗУ на сетевой карте. В качестве другого примера IEEE использует термин универсальный адрес, чтобы подчеркнуть тот факт, что адрес, присвоенный сетевой карте производителем, должен быть уникальным среди всех MAC-адресов во вселенной.
|
In addition to unicast addresses, Ethernet also uses group addresses.|В дополнение к одноадресным адресам Ethernet также использует групповые адреса.
Group addresses identify more than one LAN interface card.|Групповые адреса идентифицируют более одной интерфейсной карты LAN.
A frame sent to a group address might be delivered to a small set of devices on the LAN, or even to all devices on the LAN. In fact, the IEEE defines two general categories of group addresses for Ethernet:|Кадр, отправленный на групповой адрес, может быть доставлен на небольшой набор устройств в локальной сети или даже на все устройства в локальной сети. Фактически, IEEE определяет две общие категории групповых адресов для Ethernet:
|
Broadcast address: Frames sent to this address should be delivered to all devices on the Ethernet LAN. It has a value of FFFF.FFFF.FFFF.|Широковещательный адрес: кадры, отправленные на этот адрес, должны быть доставлены на все устройства в локальной сети Ethernet. Он имеет значение FFFF.FFFF.FFFF.
|
Multicast addresses: Frames sent to a multicast Ethernet address will be copied and forwarded to a subset of the devices on the LAN that volunteers to receive frames sent to a specific multicast address.|Многоадресные адреса: кадры, отправленные на многоадресный адрес Ethernet, будут скопированы и перенаправлены на подмножество устройств в локальной сети, которые добровольно соглашаются принимать кадры, отправленные на конкретный адрес многоадресной рассылки.
|
Table 2-7 summarizes most of the details about MAC addresses.|Таблица 2-7 суммирует большинство деталей о MAC-адресах.
|
Table 2-7 LAN MAC Address Terminology and Features Table end.|Таблица 2-7 Терминология и характеристики MAC-адресов LAN Конец таблицы.
##### Identifying Network Layer Protocols with the Ethernet Type Field
Идентификация протоколов сетевого уровня с помощью поля типа Ethernet   
__|__
--|--
|
While the Ethernet header’s address fields play an important and more obvious role in Ethernet LANs, the Ethernet Type field plays a much less obvious role.|В то время как поля адреса заголовка Ethernet играют важную и более очевидную роль в локальных сетях Ethernet, поле типа Ethernet играет гораздо менее очевидную роль.
The Ethernet Type field, or EtherType, sits in the Ethernet data-link layer header, but its purpose is to directly help the network processing on routers and hosts.|Поле Ethernet Type, или EtherType, находится в заголовке уровня канала передачи данных Ethernet, но его цель состоит в том, чтобы напрямую помочь сетевой обработке на маршрутизаторах и хостах.
Basically, the Type field identifies the type of network layer (Layer 3) packet that sits inside the Ethernet frame.|По сути, поле Type определяет тип пакета сетевого уровня (Layer 3), который находится внутри кадра Ethernet.
|
First, think about what sits inside the data part of the Ethernet frame shown earlier in Figure 2-14.|Сначала подумайте, что находится внутри части данных кадра Ethernet, показанной ранее на рис. 2-14.
Typically, it holds the network layer packet created by the network layer protocol on some device in the network.|Как правило, он содержит пакет сетевого уровня, созданный протоколом сетевого уровня на каком-либо устройстве в сети.
Over the years, those protocols have included IBM Systems Network Architecture (SNA), Novell NetWare, Digital Equipment Corporation’s DECnet, and Apple Computer’s AppleTalk.|На протяжении многих лет эти протоколы включали IBM Systems Network Architecture (SNA), Novell NetWare, DECnet корпорации Digital Equipment и AppleTalk Apple Computer.
Today, the most common network layer protocols are both from TCP/IP: IP version 4 (IPv4) and IP version 6 (IPv6).|Сегодня наиболее распространенными протоколами сетевого уровня являются протоколы TCP / IP: IP версии 4 (IPv4) и IP версии 6 (IPv6).
|
The original host has a place to insert a value (a hexadecimal number) to identify the type of packet encapsulated inside the Ethernet frame.|На исходном хосте есть место для вставки значения (шестнадцатеричного числа) для идентификации типа пакета, инкапсулированного внутри кадра Ethernet.
However, what number should the sender put in the header to identify an IPv4 packet as the type?|Однако какое число отправитель должен указать в заголовке, чтобы идентифицировать пакет IPv4 как тип?
Or an IPv6 packet?|Или пакет IPv6?
As it turns out, the IEEE manages a list of EtherType values, so that every network layer protocol that needs a unique EtherType value can have a number.|Как оказалось, IEEE управляет списком значений EtherType, так что каждый протокол сетевого уровня, которому требуется уникальное значение EtherType, может иметь номер.
The sender just has to know the list. (Anyone can view the list; just go to www.ieee.org and search for EtherType.)|Отправителю просто нужно знать список. (Кто угодно может просмотреть список; просто перейдите на www.ieee.org и выполните поиск по EtherType.)
|
For example, a host can send one Ethernet frame with an IPv4 packet and the next Ethernet frame with an IPv6 packet.|Например, хост может отправить один кадр Ethernet с пакетом IPv4, а следующий кадр Ethernet - с пакетом IPv6.
Each frame would have a different Ethernet Type field value, using the values reserved by the IEEE, as shown in Figure 2-21.|Каждый кадр будет иметь различное значение поля Ethernet Type с использованием значений, зарезервированных IEEE, как показано на рисунке 2-21.
|
Figure 2-21 Use of Ethernet Type Field|Рисунок 2-21 Использование поля типа Ethernet
##### Error Detection with FCS
Обнаружение ошибок с помощью FCS   
__|__
--|--
|
Ethernet also defines a way for nodes to find out whether a frame’s bits changed while crossing over an Ethernet link. (Usually, the bits could change because of some kind of electrical interference, or a bad NIC.) Ethernet, like most data-link protocols, uses a field in the datalink trailer for the purpose of error detection.|Ethernet также определяет способ, с помощью которого узлы узнают, изменились ли биты кадра при переходе по каналу Ethernet. (Обычно биты могут измениться из-за каких-либо электрических помех или неисправной сетевой карты.) Ethernet, как и большинство протоколов передачи данных, использует поле в трейлере канала передачи данных для обнаружения ошибок.
|
The Ethernet Frame Check Sequence (FCS) field in the Ethernet trailer—the only field in the Ethernet trailer—gives the receiving node a way to compare results with the sender, to discover whether errors occurred in the frame.|Поле Ethernet Frame Check Sequence (FCS) в трейлере Ethernet - единственное поле в трейлере Ethernet - дает принимающему узлу способ сравнить результаты с отправителем, чтобы определить, произошли ли ошибки в кадре.
The sender applies a complex math formula to the frame before sending it, storing the result of the formula in the FCS field.|Отправитель применяет сложную математическую формулу к кадру перед его отправкой, сохраняя результат формулы в поле FCS.
The receiver applies the same math formula to the received frame.|Получатель применяет ту же математическую формулу к полученному кадру.
The receiver then compares its own results with the sender’s results.|Затем получатель сравнивает свои результаты с результатами отправителя.
If the results are the same, the frame did not change; otherwise, an error occurred, and the receiver discards the frame.|Если результаты совпадают, рамка не изменилась; в противном случае произошла ошибка, и получатель отбрасывает кадр.
|
Note that error detection does not also mean error recovery.|Обратите внимание, что обнаружение ошибок также не означает исправление ошибок.
Ethernet defines that the errored frame should be discarded, but Ethernet does not attempt to recover the lost frame.|Ethernet определяет, что ошибочный кадр следует отбросить, но Ethernet не пытается восстановить потерянный кадр.
Other protocols, notably TCP, recover the lost data by noticing that it is lost and sending the data again.|Другие протоколы, в частности TCP, восстанавливают потерянные данные, замечая, что они потеряны, и отправляя данные снова.
#### Sending Ethernet Frames with Switches and Hubs
Отправка кадров Ethernet с помощью коммутаторов и концентраторов   
__|__
--|--
|
Ethernet LANs behave slightly differently depending on whether the LAN has mostly modern devices, in particular, LAN switches instead of some older LAN devices called LAN hubs.|Локальные сети Ethernet ведут себя немного по-разному в зависимости от того, есть ли в локальной сети в основном современные устройства, в частности коммутаторы локальной сети вместо некоторых старых устройств локальной сети, называемых концентраторами локальной сети.
Basically, the use of more modern switches allows the use of full-duplex logic, which is much faster and simpler than half-duplex logic, which is required when using hubs.|По сути, использование более современных коммутаторов позволяет использовать полнодуплексную логику, которая намного быстрее и проще, чем полудуплексная логика, которая требуется при использовании концентраторов.
The final topic in this chapter looks at these basic differences.|В последней теме этой главы рассматриваются эти основные различия.
##### Sending in Modern Ethernet LANs Using Full Duplex
Отправка в современных локальных сетях Ethernet с использованием полного дуплекса   
__|__
--|--
|
Modern Ethernet LANs use a variety of Ethernet physical standards, but with standard Ethernet frames that can flow over any of these types of physical links.|В современных локальных сетях Ethernet используются различные физические стандарты Ethernet, но со стандартными кадрами Ethernet, которые могут передаваться по любому из этих типов физических каналов.
Each individual link can run at a different speed, but each link allows the attached nodes to send the bits in the frame to the next node.|Каждая отдельная ссылка может работать с разной скоростью, но каждая ссылка позволяет подключенным узлам отправлять биты в кадре следующему узлу.
They must work together to deliver the data from the sending Ethernet node to the destination node.|Они должны работать вместе, чтобы доставить данные от отправляющего узла Ethernet к узлу назначения.
|
The process is relatively simple, on purpose; the simplicity lets each device send a large number of frames per second.|Процесс относительно простой, специально; простота позволяет каждому устройству отправлять большое количество кадров в секунду.
Figure 2-22 shows an example in which PC1 sends an Ethernet frame to PC2.|На рис. 2-22 показан пример, в котором ПК1 отправляет кадр Ethernet на ПК2.
|
Figure 2-22 Example of Sending Data in a Modern Ethernet LAN Following the steps in the figure:|Рисунок 2-22 Пример отправки данных в современной локальной сети Ethernet Следуйте инструкциям на рисунке:
|
1. PC1 builds and sends the original Ethernet frame, using its own MAC address as the source address and PC2’s MAC address as the destination address.|1. ПК1 создает и отправляет исходный кадр Ethernet, используя свой собственный MAC-адрес в качестве адреса источника и MAC-адрес ПК2 в качестве адреса назначения.
|
2. Switch SW1 receives and forwards the Ethernet frame out its G0/1 interface (short for Gigabit interface 0/1) to SW2.|2. Коммутатор SW1 принимает и пересылает кадр Ethernet через свой интерфейс G0 / 1 (сокращение от Gigabit interface 0/1) на SW2.
|
3. Switch SW2 receives and forwards the Ethernet frame out its F0/2 interface (short for Fast Ethernet interface 0/2) to PC2.|3. Коммутатор SW2 принимает и пересылает кадр Ethernet через интерфейс F0 / 2 (сокращение от Fast Ethernet interface 0/2) на ПК2.
|
4. PC2 receives the frame, recognizes the destination MAC address as its own, and processes the frame.|4. ПК2 принимает кадр, распознает MAC-адрес назначения как свой собственный и обрабатывает кадр.
|
The Ethernet network in Figure 2-22 uses full duplex on each link, but the concept might be difficult to see.|Сеть Ethernet на рис. 2-22 использует полнодуплексный режим на каждом канале, но эту концепцию трудно понять.
|
Full duplex means that that the NIC or switch port has no half-duplex restrictions.|Полный дуплекс означает, что для сетевого адаптера или порта коммутатора нет ограничений на полудуплекс.
So, to understand full duplex, you need to understand half duplex, as follows:|Итак, чтобы понять полный дуплекс, вам нужно понимать полудуплекс следующим образом:
|
Half duplex: The device must wait to send if it is currently receiving a frame; in other words, it cannot send and receive at the same time.|Полудуплекс: устройство должно дождаться отправки, если оно в данный момент принимает кадр; Другими словами, он не может отправлять и получать одновременно.
|
Full duplex: The device does not have to wait before sending; it can send and receive at the same time.|Полный дуплекс: устройству не нужно ждать перед отправкой; он может отправлять и получать одновременно.
|
So, with all PCs and LAN switches, and no LAN hubs, all the nodes can use full duplex.|Таким образом, со всеми ПК и коммутаторами LAN и без концентраторов LAN все узлы могут использовать полнодуплексный режим.
All nodes can send and receive on their port at the same instant in time.|Все узлы могут отправлять и получать через свой порт в один и тот же момент времени.
For example, in Figure 2-22, PC1 and PC2 could send frames to each other simultaneously, in both directions, without any half-duplex restrictions.|Например, на рис. 2-22 ПК1 и ПК2 могут отправлять кадры друг другу одновременно в обоих направлениях без каких-либо полудуплексных ограничений.
##### Using Half Duplex with LAN Hubs
Использование полудуплекса с концентраторами LAN   
__|__
--|--
|
To understand the need for half-duplex logic in some cases, you have to understand a little about an older type of networking device called a LAN hub.|Чтобы понять необходимость полудуплексной логики в некоторых случаях, вам нужно немного узнать о более старом типе сетевого устройства, называемом концентратором LAN.
When the IEEE first introduced 10BASE-T in 1990, Ethernet switches did not exist yet; instead, networks used a device called a LAN hub.|Когда IEEE впервые представил 10BASE-T в 1990 году, коммутаторов Ethernet еще не существовало; вместо этого в сети использовалось устройство, называемое концентратором LAN.
Like a switch, a LAN hub provided a number of RJ-45 ports as a place to connect links to PCs; however, hubs used different rules for forwarding data.|Подобно коммутатору, концентратор локальной сети предоставляет несколько портов RJ-45 в качестве места для подключения каналов к ПК; однако концентраторы использовали другие правила пересылки данных.
|
LAN hubs forward data using physical layer standards rather than data-link standards and are therefore considered to be Layer 1 devices.|Концентраторы LAN пересылают данные, используя стандарты физического уровня, а не стандарты канала передачи данных, и поэтому считаются устройствами уровня 1.
When an electrical signal comes in one hub port, the hub repeats that electrical signal out all other ports (except the incoming port).|Когда электрический сигнал поступает в один порт концентратора, концентратор повторяет этот электрический сигнал на все другие порты (кроме входящего порта).
By doing so, the data reaches all the rest of the nodes connected to the hub, so the data hopefully reaches the correct destination.|Таким образом, данные достигают всех остальных узлов, подключенных к концентратору, поэтому мы надеемся, что данные достигнут правильного места назначения.
The hub has no concept of Ethernet frames, of addresses, making decisions based on those addresses, and so on.|Концентратор не имеет понятия о кадрах Ethernet, адресах, принятии решений на основе этих адресов и т. Д.
|
The downside of using LAN hubs is that if two or more devices transmitted a signal at the same instant, the electrical signal collides and becomes garbled.|Обратной стороной использования концентраторов LAN является то, что если два или более устройства передают сигнал в один и тот же момент, электрический сигнал сталкивается и становится искаженным.
The hub repeats all received electrical signals, even if it receives multiple signals at the same time.|Концентратор повторяет все полученные электрические сигналы, даже если он принимает несколько сигналов одновременно.
For example, Figure 2-23 shows the idea, with PCs Archie and Bob sending an electrical signal at the same instant of time (at Steps 1A and 1B) and the hub repeating both electrical signals out toward Larry on the left (Step 2).|Например, на рис. 2-23 показана идея, в которой ПК Арчи и Боб посылают электрический сигнал в один и тот же момент времени (на шагах 1A и 1B), а концентратор повторяет оба электрических сигнала в направлении Ларри слева (шаг 2). .
|
Figure 2-23 Collision Occurring Because of LAN Hub Behavior NOTE For completeness, note that the hub floods each frame out all other ports (except the incoming port).|Рисунок 2-23 Коллизия, возникающая из-за поведения концентратора LAN ПРИМЕЧАНИЕ. Для полноты картины обратите внимание, что концентратор лавинно отправляет каждый кадр из всех других портов (кроме входящего порта).
So, Archie’s frame goes to both Larry and Bob; Bob’s frame goes to Larry and Archie.|Итак, фрейм Арчи достается и Ларри, и Бобу; Фрейм Боба достается Ларри и Арчи.
|
If you replace the hub in Figure 2-23 with a LAN switch, the switch prevents the collision on the left.|Если вы замените концентратор на Рисунке 2-23 на коммутатор LAN, коммутатор предотвратит столкновение слева.
The switch operates as a Layer 2 device, meaning that it looks at the data-link header and trailer.|Коммутатор работает как устройство уровня 2, что означает, что он просматривает заголовок и трейлер канала передачи данных.
A switch would look at the MAC addresses, and even if the switch needed to forward both frames to Larry on the left, the switch would send one frame and queue the other frame until the first frame was finished.|Коммутатор будет смотреть на MAC-адреса, и даже если коммутатору необходимо переадресовать оба кадра Ларри слева, коммутатор отправит один кадр и поставит другой кадр в очередь до тех пор, пока не будет завершен первый кадр.
|
Now back to the issue created by the hub’s logic: collisions.|Теперь вернемся к проблеме, созданной логикой хаба: коллизиям.
To prevent these collisions, the Ethernet nodes must use half-duplex logic instead of full-duplex logic.|Чтобы предотвратить эти коллизии, узлы Ethernet должны использовать полудуплексную логику вместо полнодуплексной логики.
A problem occurs only when two or more devices send at the same time; half-duplex logic tells the nodes that if someone else is sending, wait before sending.|Проблема возникает только тогда, когда два или более устройства отправляют одновременно; полудуплексная логика сообщает узлам, что если отправляет кто-то другой, подождите перед отправкой.
|
For example, back in Figure 2-23, imagine that Archie began sending his frame early enough so that Bob received the first bits of that frame before Bob tried to send his own frame.|Например, вернувшись к рисунку 2-23, представьте, что Арчи начал отправлять свой кадр достаточно рано, так что Боб получил первые биты этого кадра до того, как Боб попытался отправить свой собственный кадр.
Bob, at Step 1B, would notice that he was receiving a frame from someone else, and using halfduplex logic, would simply wait to send the frame listed at Step 1B.|Боб на шаге 1B заметил бы, что он получает кадр от кого-то еще, и, используя полудуплексную логику, просто ждал бы отправки кадра, указанного на шаге 1B.
|
Nodes that use half-duplex logic actually use a relatively well-known algorithm called carrier sense multiple access with collision detection (CSMA/CD). The algorithm takes care of the obvious cases but also the cases caused by unfortunate timing.|Узлы, которые используют полудуплексную логику, фактически используют относительно хорошо известный алгоритм, называемый множественным доступом с контролем несущей и обнаружением коллизий (CSMA / CD). Алгоритм учитывает очевидные случаи, но также и случаи, вызванные неудачным расчетом времени.
For example, two nodes could check for an incoming frame at the exact same instant, both realize that no other node is sending, and both send their frames at the exact same instant, causing a collision.|Например, два узла могут проверять входящий кадр в один и тот же момент, оба понимают, что никакой другой узел не отправляет, и оба отправляют свои кадры в один и тот же момент, вызывая коллизию.
CSMA/|CSMA /
|
CD covers these cases as well, as follows:|CD охватывает и эти случаи, а именно:
|
Step 1.|Шаг 1.
A device with a frame to send listens until the Ethernet is not busy.|Устройство с кадром для отправки слушает, пока Ethernet не будет занят.
|
Step 2.|Шаг 2.
When the Ethernet is not busy, the sender begins sending the frame.|Когда Ethernet не занят, отправитель начинает отправку кадра.
|
Step 3.|Шаг 3.
The sender listens while sending to discover whether a collision occurs; collisions might be caused by many reasons, including unfortunate timing.|Отправитель слушает во время отправки, чтобы определить, возникает ли конфликт; Столкновения могут быть вызваны многими причинами, в том числе неудачным временем.
If a collision occurs, all currently sending nodes do the following:|Если происходит коллизия, все отправляющие в данный момент узлы делают следующее:
|
A. They send a jamming signal that tells all nodes that a collision happened.|A. Они посылают сигнал глушения, который сообщает всем узлам, что произошло столкновение.
|
B. They independently choose a random time to wait before trying again, to avoid unfortunate timing.|Б. Они самостоятельно выбирают случайное время ожидания перед повторной попыткой, чтобы избежать неудачного выбора времени.
|
C. The next attempt starts again at Step 1.|C. Следующая попытка снова начинается с шага 1.
|
Although most modern LANs do not often use hubs and therefore do not need to use half duplex, enough old hubs still exist in enterprise networks so that you need to be ready to understand duplex issues.|Хотя большинство современных локальных сетей не часто используют концентраторы и, следовательно, не нуждаются в использовании полудуплекса, в корпоративных сетях все еще существует достаточно старых концентраторов, поэтому вам нужно быть готовым понять проблемы дуплекса.
Each NIC and switch port has a duplex setting.|Каждая сетевая карта и порт коммутатора имеют настройку дуплекса.
For all links between PCs and switches, or between switches, use full duplex.|Для всех каналов связи между ПК и коммутаторами или между коммутаторами используйте полнодуплексный режим.
However, for any link connected to a LAN hub, the connected LAN switch and NIC port should use half duplex.|Однако для любого канала, подключенного к концентратору LAN, подключенный коммутатор LAN и порт NIC должны использовать полудуплекс.
Note that the hub itself does not use half-duplex logic, instead just repeating incoming signals out every other port.|Обратите внимание, что сам концентратор не использует полудуплексную логику, а просто повторяет входящие сигналы через каждый другой порт.
|
Figure 2-24 shows an example, with full-duplex links on the left and a single LAN hub on the right.|На Рис. 2-24 показан пример с полнодуплексными каналами слева и одним концентратором LAN справа.
The hub then requires SW2’s F0/2 interface to use half-duplex logic, along with the PCs connected to the hub.|Затем концентратору требуется интерфейс F0 / 2 SW2 для использования полудуплексной логики вместе с ПК, подключенными к концентратору.
|
Figure 2-24 Full and Half Duplex in an Ethernet LAN Before closing the chapter, note that the discussion of full and half duplex connects to two specific terms from CCNA exam topic 1.3.b, but those connections may not be obvious.|Рисунок 2-24 Полнодуплексный и полудуплексный режим в локальной сети Ethernet Перед закрытием главы обратите внимание, что обсуждение полного и полудуплексного режима связано с двумя конкретными терминами из темы 1.3.b экзамена CCNA, но эти соединения могут быть неочевидными.
|
First, the term Ethernet shared media (from the exam topic) refers to designs that use hubs, require CSMA/CD, and therefore share the bandwidth.|Во-первых, термин совместно используемый носитель Ethernet (из темы экзамена) относится к проектам, которые используют концентраторы, требуют CSMA / CD и, следовательно, совместно используют полосу пропускания.
The idea behind the term comes from the fact that the devices connected to the hub share the network because they must use CSMA/CD, and CSMA/CD enforces rules that allow only one device to successfully send a frame at any point in time.|Идея этого термина исходит из того факта, что устройства, подключенные к концентратору, совместно используют сеть, потому что они должны использовать CSMA / CD, а CSMA / CD обеспечивает соблюдение правил, которые позволяют только одному устройству успешно отправлять кадр в любой момент времени.
|
By contrast, the term Ethernet point-to-point in that same exam topic emphasizes the fact that in a network built with switches, each (point-to-point) link works independently of the others.|Напротив, термин «точка-точка» Ethernet в той же теме экзамена подчеркивает тот факт, что в сети, построенной с использованием коммутаторов, каждое (точка-точка) соединение работает независимо от других.
Because of the full-duplex logic discussed in this section, a frame can be sent on every point-to-point link in an Ethernet at the same time.|Из-за полнодуплексной логики, обсуждаемой в этом разделе, кадр может быть отправлен по каждому каналу точка-точка в Ethernet одновременно.
### Chapter Review
Обзор главы   
__|__
--|--
|
One key to doing well on the exams is to perform repetitive spaced review sessions.|Один из ключей к успешной сдаче экзаменов - повторение повторных сессий с интервалом.
Review this chapter’s material using either the tools in the book or interactive tools for the same material found on the book’s companion website.|Просмотрите материал этой главы, используя инструменты из книги или интерактивные инструменты для тех же материалов, которые можно найти на сопутствующем веб-сайте книги.
Refer to the “Your Study Plan” element for more details.|Обратитесь к элементу «Ваш учебный план» для получения более подробной информации.
Table 2-8 outlines the key review elements and where you can find them.|В Таблице 2-8 перечислены ключевые элементы обзора и указаны места, где их можно найти.
To better track your study progress, record when you completed these activities in the second column.|Чтобы лучше отслеживать свои успехи в учебе, отметьте, когда вы выполнили эти задания, во втором столбце.
|
Table 2-8 Chapter Review Tracking Table end.|Таблица 2-8. Конец таблицы отслеживания обзора главы.
|
Review All the Key Topics Key Terms You Should Know Ethernet, IEEE, wired LAN, wireless LAN, Ethernet frame, 10BASE-T, 100BASE-T, 1000BASE-T, Fast Ethernet, Gigabit Ethernet, Ethernet link, RJ-45, Ethernet port, network interface card (NIC), straight-through cable, crossover cable, Ethernet address, MAC address, unicast address, broadcast address, Frame Check Sequence, transceiver, Multimode (MM), single-mode (SM), electromagnetic Interference (EMI), core, cladding, fiber-optic cable|Ознакомьтесь со всеми ключевыми темами. Ключевые термины, которые вы должны знать Ethernet, IEEE, проводная локальная сеть, беспроводная локальная сеть, рамка Ethernet, 10BASE-T, 100BASE-T, 1000BASE-T, Fast Ethernet, Gigabit Ethernet, канал Ethernet, RJ-45, порт Ethernet. , сетевая карта (NIC), прямой кабель, перекрестный кабель, адрес Ethernet, MAC-адрес, одноадресный адрес, широковещательный адрес, последовательность проверки кадров, приемопередатчик, многомодовый (MM), одномодовый (SM), электромагнитные помехи (EMI) ), жила, оболочка, оптоволоконный кабель
## Chapter 3 Fundamentals of WANs and IP Routing
Глава 3 Основы WAN и IP-маршрутизации   
__|__
--|--
|
This chapter covers the following exam topics:|В этой главе рассматриваются следующие экзаменационные темы:
###### 1.0 Network Fundamentals
1.0 Основы сети   
###### 1.1 Explain the role and function of network components
1.1 Объясните роль и функции сетевых компонентов   
###### 1.1.a Routers
1.1.a Маршрутизаторы   
###### 1.2 Describe characteristics of network topology architectures
1.2 Описание характеристик архитектур топологии сети   
###### 1.2.d WAN
1.2.d WAN   
__|__
--|--
|
This chapter introduces WANs and the various features of the TCP/IP network layer.|В этой главе представлены глобальные сети и различные функции сетевого уровня TCP / IP.
|
First, for WANs, note that the current CCNA blueprint does not examine WANs in detail as an end to themselves.|Во-первых, что касается глобальных сетей, обратите внимание, что текущая схема CCNA не рассматривает глобальные сети подробно как самоцель.
However, to understand IP routing, you need to understand the basics of the two types of WAN links introduced in the first major section of this chapter: serial links and Ethernet WAN links.|Однако для понимания IP-маршрутизации необходимо понимать основы двух типов каналов WAN, представленных в первом основном разделе этой главы: последовательные каналы и каналы Ethernet WAN.
In their most basic form, these WAN links connect routers that sit at sites that can be miles to hundreds of miles apart, allowing communications between remote sites.|В своей самой простой форме эти каналы глобальной сети соединяют маршрутизаторы, расположенные на сайтах, которые могут находиться на расстоянии от нескольких миль до сотен миль, обеспечивая связь между удаленными сайтами.
|
The rest of the chapter then turns to the TCP/IP Network layer, with IP as the center of the discussion.|Остальная часть главы переходит к сетевому уровню TCP / IP, в центре внимания которого - IP.
The second section of the chapter discusses the major features of IP: routing, addressing, and routing protocols.|Во втором разделе главы обсуждаются основные функции IP: маршрутизация, адресация и протоколы маршрутизации.
The final section of the chapter examines a few protocols other than IP that also help the TCP/IP Network layer create a network that allows end-toend communication between endpoints.|В последнем разделе главы рассматриваются несколько протоколов, отличных от IP, которые также помогают сетевому уровню TCP / IP создавать сеть, обеспечивающую сквозную связь между конечными точками.
### “Do I Know This Already?” Quiz
«Знаю ли я это уже?» Викторина   
__|__
--|--
|
Take the quiz (either here or use the PTP software) if you want to use the score to help you decide how much time to spend on this chapter.|Пройдите тест (здесь или воспользуйтесь программой PTP), если вы хотите использовать оценку, чтобы решить, сколько времени потратить на эту главу.
The letter answers are listed at the bottom of the page following the quiz.|Ответы на письма перечислены внизу страницы после викторины.
Appendix C, found both at the end of the book as well as on the companion website, includes both the answers and explanations.|Приложение C, которое можно найти как в конце книги, так и на сопутствующем веб-сайте, включает как ответы, так и пояснения.
You can also find both answers and explanations in the PTP testing software.|Вы также можете найти ответы и пояснения в программе тестирования PTP.
|
Table 3-1 “Do I Know This Already?” Foundation Topics Section-to-Question Mapping|Таблица 3-1 «Знаю ли я это уже?» Сопоставление разделов с вопросами по основным темам
### Foundation Topics
Основные темы   
### Wide-Area Networks
Глобальные сети   
__|__
--|--
|
IP Routing 3–6 Other Network Layer Functions 7 CHAPTER 3 1.|IP-маршрутизация 3–6 Другие функции сетевого уровня 7 ГЛАВА 3 1.
Which of the following fields in the HDLC header used by Cisco routers does Cisco add, beyond the ISO standard HDLC?|Какие из следующих полей в заголовке HDLC, используемом маршрутизаторами Cisco, добавляет Cisco помимо стандартного ISO HDLC?
|
a. Flag b.|а. Флаг b.
Type c.|Тип c.
Address d.|Адрес д.
FCS 2.|FCS 2.
Two routers, R1 and R2, connect using an Ethernet over MPLS service.|Два маршрутизатора, R1 и R2, подключаются с помощью службы Ethernet через MPLS.
The service provides point-to-point service between these two routers only, as a Layer 2 Ethernet service.|Служба обеспечивает двухточечную службу только между этими двумя маршрутизаторами в качестве службы Ethernet уровня 2.
Which of the following are the most likely to be true about this WAN?|Что из следующего, скорее всего, будет правдой об этой глобальной сети?
|
(Choose two answers.)|(Выберите два ответа.)
|
a. R1 will connect to a physical Ethernet link, with the other end of the cable connected to R2.|а. R1 подключится к физическому каналу Ethernet, а другой конец кабеля будет подключен к R2.
|
b. R1 will connect to a physical Ethernet link, with the other end of the cable connected to a device at the WAN service provider point of presence.|б. R1 подключается к физическому каналу Ethernet, а другой конец кабеля подключается к устройству в точке присутствия поставщика услуг глобальной сети.
|
c. R1 will forward data-link frames to R2 using an HDLC header/trailer.|c. R1 пересылает кадры канала данных на R2, используя заголовок / трейлер HDLC.
|
d. R1 will forward data-link frames to R2 using an Ethernet header/trailer.|d. R1 пересылает кадры канала данных на R2, используя заголовок / трейлер Ethernet.
|
3. Imagine a network with two routers that are connected with a point-to-point HDLC serial link.|3. Представьте сеть с двумя маршрутизаторами, соединенными последовательным каналом HDLC «точка-точка».
Each router has an Ethernet, with PC1 sharing the Ethernet with Router1 and PC2 sharing the Ethernet with Router2.|У каждого маршрутизатора есть Ethernet, при этом ПК1 совместно использует Ethernet с Router1, а ПК2 использует Ethernet с Router2.
When PC1 sends data to PC2, which of the following is true?|Когда ПК1 отправляет данные на ПК2, что из следующего верно?
|
a. Router1 strips the Ethernet header and trailer off the frame received from PC1, never to be used again.|а. Router1 удаляет заголовок и трейлер Ethernet из кадра, полученного от ПК1, чтобы никогда не использовать его снова.
|
b. Router1 encapsulates the Ethernet frame inside an HDLC header and sends the frame to Router2, which extracts the Ethernet frame for forwarding to PC2.|б. Маршрутизатор 1 инкапсулирует кадр Ethernet внутри заголовка HDLC и отправляет кадр маршрутизатору 2, который извлекает кадр Ethernet для пересылки на ПК2.
|
c. Router1 strips the Ethernet header and trailer off the frame received from PC1, which is exactly re-created by Router2 before forwarding data to PC2.|c. Router1 удаляет заголовок и трейлер Ethernet из кадра, полученного от ПК1, который точно воссоздается Router2 перед пересылкой данных на ПК2.
|
d. Router1 removes the Ethernet, IP, and TCP headers and rebuilds the appropriate headers before forwarding the packet to Router2.|d. Router1 удаляет заголовки Ethernet, IP и TCP и перестраивает соответствующие заголовки перед пересылкой пакета на Router2.
|
4. Which of the following does a router normally use when making a decision about routing TCP/IP packets?|4. Что из следующего маршрутизатор обычно использует при принятии решения о маршрутизации пакетов TCP / IP?
|
a. Destination MAC address b.|а. MAC-адрес назначения b.
Source MAC address c.|MAC-адрес источника c.
Destination IP address d.|IP-адрес назначения d.
Source IP address e.|Исходный IP-адрес e.
Destination MAC and IP addresses 5.|MAC- и IP-адреса назначения 5.
Which of the following are true about a LAN-connected TCP/IP host and its IP routing (forwarding) choices?|Что из следующего является верным о подключенном к локальной сети узле TCP / IP и его вариантах IP-маршрутизации (пересылки)?
|
a. The host always sends packets to its default gateway.|а. Хост всегда отправляет пакеты на свой шлюз по умолчанию.
|
b. The host never sends packets to its default gateway.|б. Хост никогда не отправляет пакеты на свой шлюз по умолчанию.
|
c. The host sends packets to its default gateway if the destination IP address is in a different subnet than the host.|c. Хост отправляет пакеты на свой шлюз по умолчанию, если IP-адрес назначения находится в другой подсети, чем хост.
|
d. The host sends packets to its default gateway if the destination IP address is in the same subnet as the host.|d. Хост отправляет пакеты на свой шлюз по умолчанию, если IP-адрес назначения находится в той же подсети, что и хост.
|
6. Which of the following are functions of a routing protocol? (Choose two answers.)|6. Что из перечисленного является функциями протокола маршрутизации? (Выберите два ответа.)
|
a. Advertising known routes to neighboring routers b.|а. Реклама известных маршрутов к соседним маршрутизаторам b.
Learning routes for subnets directly connected to the router c.|Изучение маршрутов для подсетей, напрямую подключенных к маршрутизатору c.
Learning routes and putting those routes into the routing table for routes advertised to the router by its neighboring routers d.|Изучение маршрутов и занесение этих маршрутов в таблицу маршрутизации для маршрутов, объявляемых маршрутизатору его соседними маршрутизаторами d.
Forwarding IP packets based on a packet’s destination IP address 7.|Пересылка IP-пакетов на основе IP-адреса назначения пакета 7.
A company implements a TCP/IP network, with PC1 sitting on an Ethernet LAN.|Компания реализует сеть TCP / IP, при этом ПК1 находится в локальной сети Ethernet.
|
Which of the following protocols and features requires PC1 to learn information from some other server device?|Для каких из следующих протоколов и функций ПК1 должен получать информацию от другого серверного устройства?
|
a. ARP b. ping c.|а. ARP б. пинг c.
DNS d.|DNS d.
None of these answers is correct.|Ни один из этих ответов не является правильным.
|
Foundation Topics Wide-Area Networks Imagine a typical day at the branch office at some enterprise.|Основные темы Глобальные сети Представьте себе обычный день в филиале на каком-то предприятии.
The user sits at some endpoint device: a PC, tablet, phone, and so on.|Пользователь сидит на каком-то оконечном устройстве: ПК, планшете, телефоне и т. Д.
It connects to a LAN, either via an Ethernet cable or using a wireless LAN. However, the user happens to be checking information on a website, and that web server sits at the home office of the company.|Он подключается к локальной сети с помощью кабеля Ethernet или беспроводной локальной сети. Однако случается, что пользователь проверяет информацию на веб-сайте, и этот веб-сервер находится в домашнем офисе компании.
To make that work, the data travels over one or more wide-area network (WAN) links.|Чтобы это работало, данные передаются по одному или нескольким каналам глобальной сети (WAN).
|
WAN technologies define the physical (Layer 1) standards and data-link (Layer 2) protocols used to communicate long distances.|Технологии WAN определяют физические стандарты (уровень 1) и протоколы передачи данных (уровень 2), используемые для связи на больших расстояниях.
This first section examines two such technologies:|В этом первом разделе рассматриваются две такие технологии:
|
leased-line WANs and Ethernet WANs. Leased-line WANs have been an option for networks for half a century, are becoming much less common today, but you may still see some leased-line WAN links in the exam.|выделенные линии WAN и Ethernet WAN. Глобальные сети с выделенной линией были вариантом для сетей в течение полувека, сегодня они становятся гораздо менее распространенными, но вы все еще можете увидеть некоторые каналы глобальной сети по выделенной линии на экзамене.
Ethernet WAN links do use the same data-link protocols as Ethernet LANs, but they use additional features to make the links work over the much longer distances required for WANs. The next few pages examine leased-line WANs first, followed by Ethernet WANs.|В каналах Ethernet WAN используются те же протоколы передачи данных, что и в локальных сетях Ethernet, но в них используются дополнительные функции, позволяющие каналам работать на гораздо больших расстояниях, необходимых для глобальных сетей. На следующих нескольких страницах сначала исследуются глобальные сети с выделенными линиями, а затем - сети Ethernet.
#### Leased-Line WANs
WAN с выделенной линией   
__|__
--|--
|
To connect LANs using a WAN, the internetwork uses a router connected to each LAN, with a WAN link between the routers.|Для подключения локальных сетей с помощью глобальной сети межсетевое взаимодействие использует маршрутизатор, подключенный к каждой локальной сети, с каналом глобальной сети между маршрутизаторами.
First, the enterprise’s network engineer would order some kind of WAN link.|Во-первых, сетевой инженер предприятия заказывал какое-то соединение WAN.
A router at each site connects to both the WAN link and the LAN, as shown in Figure 3-1.|Маршрутизатор на каждом сайте подключается как к каналу WAN, так и к локальной сети, как показано на рисунке 3-1.
Note that a crooked line between the routers is the common way to represent a leased line when the drawing does not need to show any of the physical details of the line.|Обратите внимание, что кривая линия между маршрутизаторами является обычным способом представления выделенной линии, когда на чертеже не требуется отображать какие-либо физические детали линии.
|
Figure 3-1 Small Enterprise Network with One Leased Line This section begins by examining the physical details of leased lines, followed by a discussion of the default data-link protocol for leased lines (HDLC).|Рис. 3-1. Сеть малого предприятия с одной выделенной линией. Этот раздел начинается с изучения физических деталей выделенных линий, за которым следует обсуждение протокола передачи данных по умолчанию для выделенных линий (HDLC).
##### Physical Details of Leased Lines
Физические характеристики арендованных линий   
__|__
--|--
|
The leased line service delivers bits in both directions, at a predetermined speed, using fullduplex logic.|Услуга выделенной линии передает биты в обоих направлениях с заданной скоростью с использованием полнодуплексной логики.
In fact, conceptually it acts as if you had a full-duplex crossover Ethernet link between two routers, as shown in Figure 3-2.|Фактически, концептуально это действует так, как если бы между двумя маршрутизаторами был установлен полнодуплексный перекрестный канал Ethernet, как показано на рисунке 3-2.
The leased line uses two pairs of wires, one pair for each direction of sending data, which allows full-duplex operation.|В выделенной линии используются две пары проводов, по одной паре для каждого направления передачи данных, что позволяет работать в полнодуплексном режиме.
|
Figure 3-2 Conceptual View of the Leased-Line Service Of course, leased lines have many differences compared to an Ethernet crossover cable.|Рис. 3-2. Концептуальный вид услуги выделенной линии. Конечно, выделенные линии имеют много отличий от перекрестного кабеля Ethernet.
To create such possibly long links, or circuits, a leased line does not actually exist as a single long cable between the two sites.|Для создания таких возможно длинных соединений или цепей выделенная линия фактически не существует как один длинный кабель между двумя объектами.
Instead, the telephone company (telco) that creates the leased line installs a large network of cables and specialized switching devices to create its own computer network.|Вместо этого телефонная компания (телекоммуникационная компания), которая создает выделенную линию, устанавливает большую сеть кабелей и специализированных коммутационных устройств, чтобы создать свою собственную компьютерную сеть.
The telco network creates a service that acts like a crossover cable between two points, but the physical reality is hidden from the customer.|Сеть телекоммуникационной компании создает услугу, которая действует как перекрестный кабель между двумя точками, но физическая реальность скрыта от клиента.
|
Leased lines come with their own set of terminology as well.|Выделенные линии также имеют свой собственный набор терминологии.
First, the term leased line refers to the fact that the company using the leased line does not own the line but instead pays a monthly lease fee to use it.|Во-первых, термин «арендованная линия» относится к тому факту, что компания, использующая арендованную линию, не владеет линией, а вместо этого платит ежемесячную арендную плату за ее использование.
Table 3-2 lists some of the many names for leased lines, mainly so that in a networking job, you have a chance to translate from the terms each person uses with a basic description as to the meaning of the name.|В таблице 3-2 перечислены некоторые из множества имен выделенных линий, в основном для того, чтобы при работе в сети у вас была возможность перевести термины, которые использует каждый человек, с базовым описанием значения имени.
|
Table 3-2 Different Names for a Leased Line Table end.|Таблица 3-2. Различные имена для конца таблицы выделенных линий.
|
To create a leased line, some physical path must exist between the two routers on the ends of the link.|Чтобы создать выделенную линию, между двумя маршрутизаторами на концах линии должен существовать какой-то физический путь.
The physical cabling must leave the customer buildings where each router sits.|Физические кабели должны покидать здания заказчика, где находится каждый маршрутизатор.
|
However, the telco does not simply install one cable between the two buildings.|Однако телекоммуникационная компания не просто прокладывает один кабель между двумя зданиями.
Instead, it uses what is typically a large and complex network that creates the appearance of a cable between the two routers.|Вместо этого он использует то, что обычно представляет собой большую и сложную сеть, которая создает видимость кабеля между двумя маршрутизаторами.
|
Figure 3-3 gives a little insight into the cabling that could exist inside the telco for a short leased line.|Рисунок 3-3 дает небольшое представление о кабельной разводке, которая может существовать внутри телекоммуникационной компании для короткой выделенной линии.
Telcos put their equipment in buildings called central offices (CO). The telco installs cables from the CO to most every other building in the city, expecting to sell services to the people in those buildings one day.|Телекоммуникационные компании размещают свое оборудование в зданиях, называемых центральными офисами (CO). Телефонная компания прокладывает кабели от центральной станции к почти всем зданиям в городе, ожидая когда-нибудь продавать услуги людям в этих зданиях.
The telco would then configure its switches to use some of the capacity on each cable to send data in both directions, creating the equivalent of a crossover cable between the two routers.|Затем телекоммуникационная компания настраивала свои коммутаторы на использование некоторой емкости каждого кабеля для передачи данных в обоих направлениях, создавая эквивалент перекрестного кабеля между двумя маршрутизаторами.
|
Figure 3-3 Possible Cabling Inside a Telco for a Short Leased Line Answers to the “Do I Know This Already?” quiz:|Рисунок 3-3 Возможная прокладка кабеля внутри телефонной компании для короткой выделенной линии Ответы на вопрос «Знаю ли я это уже?» викторина:
|
1 B 2 B, D 3 A 4 C 5 C 6 A, C 7 C Although the customer does not need to know all the details of how a telco creates a particular leased line, enterprise engineers do need to know about the parts of the link that exist inside the customer’s building at the router.|1 B 2 B, D 3 A 4 C 5 C 6 A, C 7 C Хотя заказчику не нужно знать все детали того, как телекоммуникационная компания создает конкретную выделенную линию, инженеры предприятия должны знать о частях ссылки, которые существуют внутри здания клиента на маршрутизаторе.
However, for the purposes of CCNA, you can think of any serial link as a point-to-point connection between two routers.|Однако для целей CCNA вы можете думать о любом последовательном канале как о двухточечном соединении между двумя маршрутизаторами.
##### HDLC Data-Link Details of Leased Lines
Подробная информация о канале передачи данных HDLC по выделенным линиям   
__|__
--|--
|
A leased line provides a Layer 1 service.|Выделенная линия предоставляет услугу уровня 1.
In other words, it promises to deliver bits between the devices connected to the leased line.|Другими словами, он обещает передавать биты между устройствами, подключенными к выделенной линии.
However, the leased line itself does not define a data-link layer protocol to be used on the leased line.|Однако сама выделенная линия не определяет протокол уровня канала передачи данных, который будет использоваться на выделенной линии.
|
Because leased lines define only the Layer 1 transmission service, many companies and standards organizations have created data-link protocols to control and use leased lines.|Поскольку выделенные линии определяют только службу передачи уровня 1, многие компании и организации по стандартизации создали протоколы каналов передачи данных для управления и использования выделенных линий.
Today, the two most popular data-link layer protocols used for leased lines between two routers are High-Level Data Link Control (HDLC) and Point-to-Point Protocol (PPP).|Сегодня два самых популярных протокола канального уровня, используемых для выделенных линий между двумя маршрутизаторами, - это высокоуровневое управление каналом передачи данных (HDLC) и двухточечный протокол (PPP).
|
All data-link protocols perform a similar role: to control the correct delivery of data over a physical link of a particular type.|Все протоколы каналов передачи данных выполняют аналогичную роль: контролируют правильную доставку данных по физическому каналу определенного типа.
For example, the Ethernet data-link protocol uses a destination address field to identify the correct device that should receive the data and an FCS field that allows the receiving device to determine whether the data arrived correctly.|Например, протокол канала передачи данных Ethernet использует поле адреса назначения для идентификации правильного устройства, которое должно принимать данные, и поле FCS, которое позволяет принимающему устройству определять, правильно ли поступили данные.
HDLC provides similar functions.|HDLC предоставляет аналогичные функции.
|
HDLC has less work to do than Ethernet because of the simple point-to-point topology of a leased line.|У HDLC меньше работы, чем у Ethernet, из-за простой топологии выделенной линии «точка-точка».
When one router sends an HDLC frame, the frame can go only one place: to the other end of the link.|Когда один маршрутизатор отправляет кадр HDLC, он может идти только в одном месте: на другой конец канала.
So, while HDLC has an address field, the destination is implied, and the actual address is unimportant.|Таким образом, хотя HDLC имеет поле адреса, пункт назначения подразумевается, а фактический адрес не имеет значения.
The idea is sort of like when I have lunch with my friend Gary, and only Gary.|Идея вроде как когда я обедаю с моим другом Гэри, и только Гэри.
I do not need to start every sentence with “Hey, Gary”—he knows I am talking to him.|Мне не нужно начинать каждое предложение со слов «Привет, Гэри» - он знает, что я говорю с ним.
|
HDLC has other fields and functions similar to Ethernet as well.|HDLC также имеет другие поля и функции, аналогичные Ethernet.
Table 3-3 lists the HDLC fields, with the similar Ethernet header/trailer field, just for the sake of learning HDLC based on something you have already learned about (Ethernet).|В Таблице 3-3 перечислены поля HDLC с аналогичным полем заголовка / концевой части Ethernet, просто для того, чтобы изучить HDLC на основе того, о чем вы уже узнали (Ethernet).
|
Table 3-3 Comparing HDLC Header Fields to Ethernet Table end.|Таблица 3-3 Сравнение полей заголовка HDLC с концом таблицы Ethernet.
|
HDLC exists today as a standard of the International Organization for Standardization (ISO), the same organization that brought us the OSI model.|HDLC существует сегодня как стандарт Международной организации по стандартизации (ISO), той же организации, которая представила нам модель OSI.
However, ISO standard HDLC does not have a Type field, and routers need to know the type of packet inside the frame.|Однако стандарт ISO HDLC не имеет поля типа, и маршрутизаторам необходимо знать тип пакета внутри кадра.
So, Cisco routers use a Cisco-proprietary variation of HDLC that adds a Type field, as shown in Figure 3-4.|Итак, маршрутизаторы Cisco используют собственный вариант протокола HDLC, который добавляет поле Type, как показано на рисунке 3-4.
|
Figure 3-4 HDLC Framing|Рисунок 3-4 Кадрирование HDLC
##### How Routers Use a WAN Data Link
Как маршрутизаторы используют канал передачи данных WAN   
__|__
--|--
|
Leased lines connect to routers, and routers focus on delivering packets to a destination host.|Выделенные линии подключаются к маршрутизаторам, и маршрутизаторы сосредоточены на доставке пакетов на хост назначения.
|
However, routers physically connect to both LANs and WANs, with those LANs and WANs requiring that data be sent inside data-link frames.|Однако маршрутизаторы физически подключаются как к локальным, так и к глобальным сетям, причем для этих локальных и глобальных сетей требуется, чтобы данные передавались внутри кадров канала передачи данных.
So, now that you know a little about HDLC, it helps to think about how routers use the HDLC protocol when sending data.|Итак, теперь, когда вы немного знаете о HDLC, это помогает подумать о том, как маршрутизаторы используют протокол HDLC при отправке данных.
|
First, the TCP/IP network layer focuses on forwarding IP packets from the sending host to the destination host.|Во-первых, сетевой уровень TCP / IP фокусируется на пересылке IP-пакетов от хоста-отправителя к хосту назначения.
The underlying LANs and WANs just act as a way to move the packets to the next router or end-user device.|Базовые сети LAN и WAN просто служат способом пересылки пакетов на следующий маршрутизатор или устройство конечного пользователя.
Figure 3-5 shows that network layer perspective.|Рисунок 3-5 показывает перспективу сетевого уровня.
|
Figure 3-5 IP Routing Logic over LANs and WANs Following the steps in the figure, for a packet sent by PC1 to PC2’s IP address:|Рисунок 3-5 Логика IP-маршрутизации в локальных и глобальных сетях Следуя шагам, показанным на рисунке, для пакета, отправленного ПК1 на IP-адрес ПК2:
|
1. PC1’s network layer (IP) logic tells it to send the packet to a nearby router (R1).|1. Логика сетевого уровня (IP) ПК1 сообщает ему об отправке пакета ближайшему маршрутизатору (R1).
|
2. Router R1’s network layer logic tells it to forward (route) the packet out the leased line to Router R2 next.|2. Логика сетевого уровня маршрутизатора R1 указывает ему пересылать (маршрутизировать) пакет по выделенной линии на маршрутизатор R2 следующим.
|
3. Router R2’s network layer logic tells it to forward (route) the packet out the LAN link to PC2 next.|3. Логика сетевого уровня маршрутизатора R2 указывает ему пересылать (маршрутизировать) пакет по LAN-каналу на ПК2.
|
While Figure 3-5 shows the network layer logic, the PCs and routers must rely on the LANs and WANs in the figure to actually move the bits in the packet.|Хотя на рис. 3-5 показана логика сетевого уровня, ПК и маршрутизаторы должны полагаться на локальные и глобальные сети, показанные на рисунке, для фактического перемещения битов в пакете.
Figure 3-6 shows the same figure, with the same packet, but this time showing some of the data-link layer logic used by the hosts and routers.|На рис. 3-6 показан тот же рисунок с тем же пакетом, но на этот раз показана логика уровня канала передачи данных, используемая хостами и маршрутизаторами.
Basically, three separate data-link layer steps encapsulate the packet, inside a data-link frame, over three hops through the internetwork: from PC1 to R1, from R1 to R2, and from R2 to PC2.|По сути, три отдельных шага уровня звена данных инкапсулируют пакет внутри кадра звена данных по трем переходам через объединенную сеть: от ПК1 к R1, от R1 к R2 и от R2 к ПК2.
|
Figure 3-6 General Concept of Routers De-encapsulating and Re-encapsulating IP Packets Following the steps in the figure, again for a packet sent by PC1 to PC2’s IP address:|Рисунок 3-6 Общая концепция деинкапсуляции и повторной инкапсуляции IP-пакетов маршрутизаторами Следуя шагам на рисунке, снова для пакета, отправленного ПК1 на IP-адрес ПК2:
|
1. To send the IP packet to Router R1 next, PC1 encapsulates the IP packet in an Ethernet frame that has the destination MAC address of R1.|1. Чтобы затем отправить IP-пакет маршрутизатору R1, ПК1 инкапсулирует IP-пакет в кадр Ethernet, который имеет MAC-адрес назначения R1.
|
2. Router R1 de-encapsulates (removes) the IP packet from the Ethernet frame, encapsulates the packet into an HDLC frame using an HDLC header and trailer, and forwards the HDLC frame to Router R2 next.|2. Маршрутизатор R1 деинкапсулирует (удаляет) IP-пакет из кадра Ethernet, инкапсулирует пакет в кадр HDLC, используя заголовок и трейлер HDLC, а затем пересылает кадр HDLC на маршрутизатор R2.
|
3. Router R2 de-encapsulates (removes) the IP packet from the HDLC frame, encapsulates the packet into an Ethernet frame that has the destination MAC address of PC2, and forwards the Ethernet frame to PC2.|3. Маршрутизатор R2 деинкапсулирует (удаляет) IP-пакет из кадра HDLC, инкапсулирует пакет в кадр Ethernet, который имеет MAC-адрес назначения ПК2, и пересылает кадр Ethernet на ПК2.
|
In summary, a leased line with HDLC creates a WAN link between two routers so that they can forward packets for the devices on the attached LANs. The leased line itself provides the physical means to transmit the bits, in both directions.|Таким образом, выделенная линия с HDLC создает канал WAN между двумя маршрутизаторами, чтобы они могли пересылать пакеты для устройств в подключенных локальных сетях. Сама выделенная линия предоставляет физические средства для передачи битов в обоих направлениях.
The HDLC frames provide the means to encapsulate the network layer packet correctly so that it crosses the link between routers.|Кадры HDLC предоставляют средства для правильной инкапсуляции пакета сетевого уровня, чтобы он пересекал канал между маршрутизаторами.
|
Leased lines have many benefits that have led to their relatively long life in the WAN marketplace.|У выделенных линий есть много преимуществ, которые привели к их относительно долгой жизни на рынке WAN.
|
These lines are simple for the customer, are widely available, are of high quality, and are private.|Эти линии просты для покупателя, широко доступны, имеют высокое качество и являются частными.
However, they do have some negatives as well compared to newer WAN technologies, including a higher cost and typically longer lead times to get the service installed.|Однако у них есть и некоторые недостатки по сравнению с новыми технологиями WAN, включая более высокую стоимость и, как правило, более длительные сроки установки службы.
|
Additionally, by today’s standards, leased-line LANs are slow, with faster speeds in the tens of megabits per second (Mbps).|Кроме того, по сегодняшним стандартам ЛВС с выделенной линией медленные, с более высокими скоростями до десятков мегабит в секунду (Мбит / с).
New faster WAN technology has been replacing leased lines for a long time, including the second WAN technology discussed in this book: Ethernet.|Новая более быстрая технология WAN уже давно заменяет выделенные линии, включая вторую технологию WAN, обсуждаемую в этой книге: Ethernet.
#### Ethernet as a WAN Technology
Ethernet как технология WAN   
__|__
--|--
|
For the first several decades of the existence of Ethernet, Ethernet was only appropriate for LANs. The restrictions on cable lengths and devices might allow a LAN that stretched a kilometer or two, to support a campus LAN, but that was the limit.|В течение первых нескольких десятилетий существования Ethernet Ethernet подходил только для локальных сетей. Ограничения на длину кабелей и устройства могут позволить ЛВС протяженностью один-два километра поддерживать ЛВС кампуса, но это был предел.
|
As time passed, the IEEE improved Ethernet standards in ways that made Ethernet a reasonable WAN technology.|Со временем IEEE улучшил стандарты Ethernet, сделав Ethernet разумной технологией WAN.
For example, the 1000BASE-LX standard uses single-mode fiber cabling, with support for a 5-km cable length; the 1000BASE-ZX standard supports an even longer 70-km cable length.|Например, стандарт 1000BASE-LX использует одномодовый оптоволоконный кабель с поддержкой кабеля длиной 5 км; стандарт 1000BASE-ZX поддерживает даже более длинный кабель длиной 70 км.
As time went by, and as the IEEE improved cabling distances for fiber Ethernet links, Ethernet became a reasonable WAN technology.|Шло время, и по мере того, как IEEE увеличивал длину кабелей для волоконно-оптических линий Ethernet, Ethernet стал разумной технологией WAN.
|
Today, many WAN service providers (SP) offer WAN services that take advantage of Ethernet.|Сегодня многие поставщики услуг WAN (SP) предлагают услуги WAN, которые используют преимущества Ethernet.
SPs offer a wide variety of these Ethernet WAN services, with many different names.|SP предлагают широкий спектр этих услуг Ethernet WAN с множеством разных имен.
But all of them use a similar model, with Ethernet used between the customer site and the SP’s network, as shown in Figure 3-7.|Но все они используют схожую модель с Ethernet, используемым между сайтом клиента и сетью SP, как показано на рисунке 3-7.
|
Figure 3-7 Fiber Ethernet Link to Connect a CPE Router to a Service Provider’s WAN The model shown in Figure 3-7 has many of the same ideas of how a telco creates a leased line, as shown earlier in Figure 3-3, but now with Ethernet links and devices.|Рисунок 3-7 Волоконно-оптический канал Ethernet для подключения CPE-маршрутизатора к глобальной сети поставщика услуг Модель, показанная на Рисунке 3-7, имеет многие из тех же идей того, как телекоммуникационная компания создает выделенную линию, как показано ранее на Рисунке 3-3, но теперь со связями и устройствами Ethernet.
The customer connects to an Ethernet link using a router interface.|Клиент подключается к каналу Ethernet с помощью интерфейса маршрутизатора.
The (fiber) Ethernet link leaves the customer building and connects to some nearby SP location called a point of presence (PoP). Instead of a telco switch as shown in Figure 3-3, the SP uses an Ethernet switch.|(Волоконный) канал Ethernet выходит из здания клиента и подключается к некоторому ближайшему местоположению SP, называемому точкой присутствия (PoP). Вместо коммутатора телефонной компании, как показано на рис. 3-3, SP использует коммутатор Ethernet.
Inside the SP’s network, the SP uses any technology that it wants to create the specific Ethernet WAN services.|Внутри сети SP использует любую технологию, которая нужна ему для создания определенных сервисов Ethernet WAN.
##### Ethernet WANs That Create a Layer 2 Service
Сети Ethernet WAN, которые создают сервис уровня 2   
__|__
--|--
|
Ethernet WAN services include a variety of specific services that vary in ways that change how routers use those services.|Услуги Ethernet WAN включают в себя множество конкретных услуг, которые различаются способами, которые меняют способ использования этих услуг маршрутизаторами.
However, for the purposes of CCNA, you just need to understand the most basic Ethernet WAN service, one that works much like an Ethernet crossover cable—just over a WAN. In other words:|Однако для целей CCNA вам просто нужно понять самую базовую услугу Ethernet WAN, которая работает во многом как перекрестный кабель Ethernet - только через WAN. Другими словами:
###### Logically, behaves like a point-to-point connection between two routers
Логически ведет себя как соединение точка-точка между двумя маршрутизаторами.   
###### Physically, behaves as if a physical fiber Ethernet link existed between the two routers
Физически ведет себя так, как если бы между двумя маршрутизаторами существовал физический оптоволоконный канал Ethernet.   
__|__
--|--
|
NOTE For perspective about the broad world of the service provider network shown in Figure 3-7, look for more information about the Cisco CCNA, CCNP Service Provider, and CCIE Service Provider certifications.|ПРИМЕЧАНИЕ. Чтобы получить представление о широком мире сети поставщиков услуг, показанной на рис. 3-7, поищите дополнительную информацию о сертификатах Cisco CCNA, CCNP Service Provider и CCIE Service Provider.
See www.cisco.com/go/certifications for more details.|См. Www.cisco.com/go/certifications для получения дополнительных сведений.
|
This book refers to this particular Ethernet WAN service with a couple of the common names:|В этой книге этот конкретный сервис Ethernet WAN упоминается под несколькими общими названиями:
|
Ethernet WAN: A generic name to differentiate it from an Ethernet LAN.|Ethernet WAN: общее название, позволяющее отличить его от локальной сети Ethernet.
|
Ethernet Line Service (E-Line): A term from the Metro Ethernet Forum (MEF) for the kind of point-to-point Ethernet WAN service shown throughout this book.|Ethernet Line Service (E-Line): термин из форума Metro Ethernet Forum (MEF) для типа двухточечной услуги Ethernet WAN, показанной в этой книге.
|
Ethernet emulation: A term emphasizing that the link is not a literal Ethernet link from end to end.|Эмуляция Ethernet: термин, подчеркивающий, что соединение не является буквальным соединением Ethernet от конца до конца.
|
Ethernet over MPLS (EoMPLS): A term that refers to Multiprotocol Label Switching (MPLS), a technology that can be used to create the Ethernet service for the customer.|Ethernet через MPLS (EoMPLS): термин, относящийся к многопротокольной коммутации по меткам (MPLS), технологии, которая может использоваться для создания услуги Ethernet для клиента.
|
So, if you can imagine two routers, with a single Ethernet link between the two routers, you understand what this particular EoMPLS service does, as shown in Figure 3-8.|Итак, если вы можете представить себе два маршрутизатора с одним каналом Ethernet между двумя маршрутизаторами, вы поймете, что делает эта конкретная служба EoMPLS, как показано на рисунке 3-8.
In this case, the two routers, R1 and R2, connect with an EoMPLS service instead of a serial link.|В этом случае два маршрутизатора, R1 и R2, подключаются к службе EoMPLS вместо последовательного канала.
The routers use Ethernet interfaces, and they can send data in both directions at the same time.|Маршрутизаторы используют интерфейсы Ethernet и могут отправлять данные в обоих направлениях одновременно.
|
Physically, each router actually connects to some SP PoP, as shown earlier in Figure 3-7, but logically, the two routers can send Ethernet frames to each other over the link.|Физически каждый маршрутизатор фактически подключается к некоторому SP PoP, как показано ранее на рисунке 3-7, но логически два маршрутизатора могут отправлять кадры Ethernet друг другу по каналу.
|
Figure 3-8 EoMPLS Acting Like a Simple Ethernet Link Between Two Routers|Рисунок 3-8 EoMPLS, действующий как простой канал Ethernet между двумя маршрутизаторами
##### How Routers Route IP Packets Using Ethernet Emulation
Как маршрутизаторы маршрутизируют IP-пакеты с помощью эмуляции Ethernet   
__|__
--|--
|
WANs, by their very nature, give IP routers a way to forward IP packets from a LAN at one site, over the WAN, and to another LAN at another site.|Глобальные сети по самой своей природе дают IP-маршрутизаторам возможность пересылать IP-пакеты из локальной сети на одном сайте, через глобальную сеть и в другую локальную сеть на другом сайте.
Routing over an EoMPLS WAN link still uses the WAN like a WAN, as a way to forward IP packets from one site to another.|Маршрутизация по каналу EoMPLS WAN по-прежнему использует WAN, как WAN, как способ пересылки IP-пакетов от одного сайта к другому.
|
However, the WAN link happens to use the same Ethernet protocols as the Ethernet LAN links at each site.|Однако канал WAN использует те же протоколы Ethernet, что и каналы Ethernet LAN на каждом сайте.
|
The EoMPLS link uses Ethernet for both Layer 1 and Layer 2 functions.|Канал EoMPLS использует Ethernet как для функций уровня 1, так и для функций уровня 2.
That means the link uses the same familiar Ethernet header and trailer, as shown in the middle of Figure 3-9.|Это означает, что ссылка использует те же знакомые заголовок и трейлер Ethernet, как показано в середине рисунка 3-9.
Note that the figure shows a small cloud over the Ethernet link as a way to tell us that the link is an Ethernet WAN link, rather than an Ethernet LAN link.|Обратите внимание, что на рисунке показано небольшое облако по каналу Ethernet, чтобы сообщить нам, что этот канал является каналом Ethernet WAN, а не каналом Ethernet LAN.
|
Figure 3-9 Routing over an EoMPLS Link NOTE The 802.3 headers/trailers in the figure are different at each stage!|Рисунок 3-9 Маршрутизация по каналу EoMPLS ПРИМЕЧАНИЕ Заголовки / трейлеры 802.3 на рисунке различны на каждом этапе!
Make sure to notice the reasons in the step-by-step explanations that follow.|Обязательно укажите причины в следующих пошаговых объяснениях.
|
The figure shows the same three routing steps as shown with the serial link in the earlier Figure 3-6.|На рисунке показаны те же три шага маршрутизации, что и для последовательного канала на предыдущем рисунке 3-6.
In this case, all three routing steps use the same Ethernet (802.3) protocol.|В этом случае все три шага маршрутизации используют один и тот же протокол Ethernet (802.3).
|
However, note that each frame’s data-link header and trailer are different.|Однако обратите внимание, что заголовок и трейлер канала передачи данных у каждого кадра разные.
Each router discards the old data-link header/trailer and adds a new set, as described in these steps.|Каждый маршрутизатор отбрасывает старый заголовок / трейлер канала передачи данных и добавляет новый набор, как описано в этих шагах.
|
Focus mainly on Step 2, because compared to the similar example shown in Figure 3-6, Steps 1 and 3 are unchanged:|Сосредоточьтесь в основном на шаге 2, потому что по сравнению с аналогичным примером, показанным на рисунке 3-6, шаги 1 и 3 не изменились:
|
1. To send the IP packet to Router R1 next, PC1 encapsulates the IP packet in an Ethernet frame that has the destination MAC address of R1.|1. Чтобы затем отправить IP-пакет маршрутизатору R1, ПК1 инкапсулирует IP-пакет в кадр Ethernet, который имеет MAC-адрес назначения R1.
|
2. Router R1 de-encapsulates (removes) the IP packet from the Ethernet frame and encapsulates the packet into a new Ethernet frame, with a new Ethernet header and trailer.|2. Маршрутизатор R1 деинкапсулирует (удаляет) IP-пакет из кадра Ethernet и инкапсулирует пакет в новый кадр Ethernet с новым заголовком и концом Ethernet.
|
The destination MAC address is R2’s G0/0 MAC address, and the source MAC address is R1’s G0/1 MAC address.|MAC-адрес назначения - это MAC-адрес G0 / 0 R2, а MAC-адрес источника - это MAC-адрес G0 / 1 R1.
R1 forwards this frame over the EoMPLS service to R2 next.|R1 пересылает этот кадр через службу EoMPLS следующему маршрутизатору R2.
|
3. Router R2 de-encapsulates (removes) the IP packet from the Ethernet frame, encapsulates the packet into an Ethernet frame that has the destination MAC address of PC2, and forwards the Ethernet frame to PC2.|3. Маршрутизатор R2 деинкапсулирует (удаляет) IP-пакет из кадра Ethernet, инкапсулирует пакет в кадр Ethernet, который имеет MAC-адрес назначения ПК2, и пересылает кадр Ethernet на ПК2.
|
Throughout this book, the WAN links (serial and Ethernet) will connect routers as shown here, with the focus being on the LANs and IP routing.|В этой книге каналы WAN (последовательные и Ethernet) будут соединять маршрутизаторы, как показано здесь, с упором на локальные сети и IP-маршрутизацию.
The rest of the chapter turns our attention to a closer look at IP routing.|Остальная часть главы посвящена более подробному рассмотрению IP-маршрутизации.
### IP Routing
IP-маршрутизация   
__|__
--|--
|
Many protocol models have existed over the years, but today the TCP/IP model dominates.|Многие модели протоколов существовали на протяжении многих лет, но сегодня модель TCP / IP доминирует.
|
And at the network layer of TCP/IP, two options exist for the main protocol around which all other network layer functions revolve: IP version 4 (IPv4) and IP version 6 (IPv6).|А на сетевом уровне TCP / IP существует два варианта основного протокола, вокруг которого вращаются все другие функции сетевого уровня: IP версии 4 (IPv4) и IP версии 6 (IPv6).
Both IPv4 and IPv6 define the same kinds of network layer functions, but with different details.|И IPv4, и IPv6 определяют одни и те же виды функций сетевого уровня, но с разными деталями.
This chapter introduces these network layer functions for IPv4.|В этой главе представлены функции сетевого уровня для IPv4.
|
NOTE All references to IP in this chapter refer to the older and more established IPv4.|ПРИМЕЧАНИЕ. Все ссылки на IP в этой главе относятся к более старому и более устоявшемуся IPv4.
|
Internet Protocol (IP) focuses on the job of routing data, in the form of IP packets, from the source host to the destination host.|Интернет-протокол (IP) фокусируется на работе по маршрутизации данных в форме IP-пакетов от исходного хоста к целевому.
IP does not concern itself with the physical transmission of data, instead relying on the lower TCP/IP layers to do the physical transmission of the data.|IP не занимается физической передачей данных, вместо этого полагаясь на нижние уровни TCP / IP для физической передачи данных.
|
Instead, IP concerns itself with the logical details, rather than physical details, of delivering data.|Вместо этого IP занимается скорее логическими, чем физическими деталями доставки данных.
In particular, the network layer specifies how packets travel end to end over a TCP/IP network, even when the packet crosses many different types of LAN and WAN links.|В частности, сетевой уровень определяет, как пакеты передаются из конца в конец по сети TCP / IP, даже когда пакет пересекает множество различных типов каналов LAN и WAN.
|
This next major section of the chapter examines IP routing in more depth.|В следующем основном разделе главы IP-маршрутизация рассматривается более подробно.
First, IP defines what it means to route an IP packet from sending host to destination host, while using successive data-link protocols.|Во-первых, IP определяет, что означает маршрутизация IP-пакета от узла-отправителя к узлу назначения при использовании последовательных протоколов передачи данных.
This section then examines how IP addressing rules help to make IP routing much more efficient by grouping addresses into subnets.|Затем в этом разделе исследуется, как правила IP-адресации помогают сделать IP-маршрутизацию намного более эффективной за счет группировки адресов в подсети.
This section closes by looking at the role of IP routing protocols, which give routers a means by which to learn routes to all the IP subnets in an internetwork.|Этот раздел завершается рассмотрением роли протоколов IP-маршрутизации, которые дают маршрутизаторам средства для изучения маршрутов ко всем IP-подсетям в объединенной сети.
#### Network Layer Routing (Forwarding) Logic
Логика маршрутизации (пересылки) сетевого уровня   
__|__
--|--
|
Routers and end-user computers (called hosts in a TCP/IP network) work together to perform IP routing.|Маршрутизаторы и компьютеры конечных пользователей (называемые хостами в сети TCP / IP) работают вместе для выполнения IP-маршрутизации.
The host operating system (OS) has TCP/IP software, including the software that implements the network layer.|Операционная система хоста (ОС) имеет программное обеспечение TCP / IP, включая программное обеспечение, реализующее сетевой уровень.
Hosts use that software to choose where to send IP packets, often to a nearby router.|Хосты используют это программное обеспечение, чтобы выбирать, куда отправлять IP-пакеты, часто на ближайший маршрутизатор.
Those routers make choices of where to send the IP packet next.|Эти маршрутизаторы выбирают, куда послать IP-пакет следующим.
|
Together, the hosts and routers deliver the IP packet to the correct destination, as shown in the example in Figure 3-10.|Вместе хосты и маршрутизаторы доставляют IP-пакет в правильное место назначения, как показано в примере на рисунке 3-10.
|
Figure 3-10 Routing Logic: PC1 Sending an IP Packet to PC2 The IP packet, created by PC1, goes from the top of the figure all the way to PC2 at the bottom of the figure.|Рисунок 3-10 Логика маршрутизации: ПК1 Отправка IP-пакета на ПК2 IP-пакет, созданный ПК1, идет от верхней части рисунка до ПК2 в нижней части рисунка.
The next few pages discuss the network layer routing logic used by each device along the path.|На следующих нескольких страницах обсуждается логика маршрутизации сетевого уровня, используемая каждым устройством на пути.
|
NOTE The term path selection is sometimes used to refer to the routing process shown in Figure 3-10.|ПРИМЕЧАНИЕ. Термин «выбор пути» иногда используется для обозначения процесса маршрутизации, показанного на рисунке 3-10.
At other times, it refers to routing protocols, specifically how routing protocols select the best route among the competing routes to the same destination.|В других случаях это относится к протоколам маршрутизации, в частности к тому, как протоколы маршрутизации выбирают лучший маршрут среди конкурирующих маршрутов к тому же месту назначения.
##### Host Forwarding Logic: Send the Packet to the Default Router
Логика пересылки хоста: отправьте пакет маршрутизатору по умолчанию   
__|__
--|--
|
In this example, PC1 does some basic analysis and then chooses to send the IP packet to the router so that the router will forward the packet.|В этом примере ПК1 выполняет базовый анализ, а затем решает отправить IP-пакет на маршрутизатор, чтобы маршрутизатор пересылал пакет.
PC1 analyzes the destination address and realizes that PC2’s address (150.150.4.10) is not on the same LAN as PC1. So PC1’s logic tells it to send the packet to a device whose job it is to know where to route data: a nearby router, on the same LAN, called PC1’s default router.|ПК1 анализирует адрес назначения и понимает, что адрес ПК2 (150.150.4.10) не находится в той же локальной сети, что и ПК1. Таким образом, логика ПК1 предписывает ему отправить пакет устройству, задача которого - знать, куда направлять данные: ближайший маршрутизатор в той же локальной сети, который называется маршрутизатором ПК1 по умолчанию.
|
To send the IP packet to the default router, the sender sends a data-link frame across the medium to the nearby router; this frame includes the packet in the data portion of the frame.|Чтобы отправить IP-пакет маршрутизатору по умолчанию, отправитель отправляет кадр канала данных через среду на ближайший маршрутизатор; этот кадр включает пакет в информационную часть кадра.
|
That frame uses data-link layer (Layer 2) addressing in the data-link header to ensure that the nearby router receives the frame.|Этот кадр использует адресацию уровня канала данных (уровень 2) в заголовке канала данных, чтобы гарантировать, что ближайший маршрутизатор получит кадр.
|
NOTE The default router is also referred to as the default gateway.|ПРИМЕЧАНИЕ Маршрутизатор по умолчанию также называется шлюзом по умолчанию.
##### R1 and R2’s Logic: Routing Data Across the Network
Логика R1 и R2: маршрутизация данных по сети   
__|__
--|--
|
All routers use the same general process to route the packet.|Все маршрутизаторы используют один и тот же общий процесс для маршрутизации пакета.
Each router keeps an IP routing table.|Каждый маршрутизатор ведет таблицу IP-маршрутизации.
This table lists IP address groupings, called IP networks and IP subnets.|В этой таблице перечислены группы IP-адресов, называемые IP-сетями и IP-подсетями.
When a router receives a packet, it compares the packet’s destination IP address to the entries in the routing table and makes a match.|Когда маршрутизатор получает пакет, он сравнивает IP-адрес назначения пакета с записями в таблице маршрутизации и находит совпадение.
This matching entry also lists directions that tell the router where to forward the packet next.|В этой совпадающей записи также перечислены направления, которые сообщают маршрутизатору, куда пересылать пакет дальше.
|
In Figure 3-10, R1 would have matched the destination address (150.150.4.10) to a routing table entry, which in turn told R1 to send the packet to R2 next.|На рис. 3-10 R1 сопоставил бы адрес назначения (150.150.4.10) с записью в таблице маршрутизации, которая, в свою очередь, сообщила R1 о необходимости отправки пакета R2.
Similarly, R2 would have matched a routing table entry that told R2 to send the packet, over an Ethernet WAN link, to R3 next.|Точно так же R2 должен сопоставить запись в таблице маршрутизации, которая предписывает R2 послать пакет по каналу Ethernet WAN на R3.
|
The routing concept works a little like driving down the freeway when approaching a big interchange.|Концепция маршрутизации немного похожа на движение по автостраде при приближении к большой развязке.
|
You look up and see signs for nearby towns, telling you which exits to take to go to each town.|Вы смотрите вверх и видите знаки близлежащих городов, которые сообщают вам, по каким выходам нужно пройти в каждый город.
Similarly, the router looks at the IP routing table (the equivalent of the road signs)|Точно так же роутер смотрит на таблицу IP-маршрутизации (эквивалент дорожных знаков)
|
and directs each packet over the correct next LAN or WAN link (the equivalent of a road).|и направляет каждый пакет по правильному следующему каналу LAN или WAN (эквивалент дороги).
##### R3’s Logic: Delivering Data to the End Destination
Логика R3: доставка данных в конечный пункт назначения   
__|__
--|--
|
The final router in the path, R3, uses almost the same logic as R1 and R2, but with one minor difference.|Последний маршрутизатор на пути, R3, использует почти ту же логику, что и R1 и R2, но с одним незначительным отличием.
R3 needs to forward the packet directly to PC2, not to some other router.|R3 необходимо переслать пакет непосредственно на ПК2, а не на какой-либо другой маршрутизатор.
On the surface, that difference seems insignificant.|На первый взгляд эта разница кажется незначительной.
In the next section, when you read about how the network layer uses LANs and WANs, the significance of the difference will become obvious.|В следующем разделе, когда вы прочитаете о том, как сетевой уровень использует локальные и глобальные сети, важность различия станет очевидной.
#### How Network Layer Routing Uses LANs and WANs
Как при маршрутизации на сетевом уровне используются локальные и глобальные сети   
__|__
--|--
|
While the network layer routing logic ignores the physical transmission details, the bits still have to be transmitted.|Хотя логика маршрутизации сетевого уровня игнорирует физические детали передачи, биты все же должны быть переданы.
To do that work, the network layer logic in a host or router must hand off the packet to the data-link layer protocols, which, in turn, ask the physical layer to actually send the data.|Для выполнения этой работы логика сетевого уровня в хосте или маршрутизаторе должна передать пакет протоколам канального уровня, которые, в свою очередь, запрашивают физический уровень для фактической отправки данных.
The data-link layer adds the appropriate header and trailer to the packet, creating a frame, before sending the frames over each physical network.|Уровень канала передачи данных добавляет к пакету соответствующий заголовок и трейлер, создавая кадр, прежде чем отправлять кадры по каждой физической сети.
|
The routing process forwards the network layer packet from end to end through the network, while each data-link frame only takes a smaller part of the trip.|В процессе маршрутизации пакет сетевого уровня пересылается из конца в конец по сети, в то время как каждый кадр канала данных занимает лишь меньшую часть пути.
Each successive datalink layer frame moves the packet to the next device that thinks about network layer logic.|Каждый последующий кадр уровня канала данных перемещает пакет к следующему устройству, которое учитывает логику сетевого уровня.
|
In short, the network layer thinks about the bigger view of the goal, like “Send this packet to the specified next router or host…,” while the data-link layer thinks about the specifics, like “Encapsulate the packet in a data-link frame and transmit it.” The following list summarizes the major steps in a router’s internal network layer routing for each packet beginning with the a frame arriving in a router interface:|Короче говоря, сетевой уровень думает о более широком видении цели, например, «Отправить этот пакет указанному следующему маршрутизатору или хосту…», в ​​то время как уровень канала данных думает о деталях, например «Инкапсулировать пакет в данные- связать кадр и передать его ». В следующем списке перечислены основные этапы внутренней маршрутизации сетевого уровня маршрутизатора для каждого пакета, начиная с кадра, поступающего в интерфейс маршрутизатора:
|
Step 1.|Шаг 1.
Use the data-link Frame Check Sequence (FCS) field to ensure that the frame had no errors; if errors occurred, discard the frame.|Используйте поле «Последовательность проверки кадра (FCS) канала передачи данных», чтобы убедиться, что в кадре нет ошибок; если произошли ошибки, отбросьте фрейм.
|
Step 2.|Шаг 2.
Assuming that the frame was not discarded at Step 1, discard the old data-link header and trailer, leaving the IP packet.|Предполагая, что кадр не был отброшен на шаге 1, отбросьте старый заголовок и трейлер канала передачи данных, оставив IP-пакет.
|
Step 3.|Шаг 3.
Compare the IP packet’s destination IP address to the routing table, and find the route that best matches the destination address.|Сравните IP-адрес назначения IP-пакета с таблицей маршрутизации и найдите маршрут, который лучше всего соответствует адресу назначения.
This route identifies the outgoing interface of the router and possibly the next-hop router IP address.|Этот маршрут идентифицирует исходящий интерфейс маршрутизатора и, возможно, IP-адрес маршрутизатора следующего перехода.
|
Step 4.|Шаг 4.
Encapsulate the IP packet inside a new data-link header and trailer, appropriate for the outgoing interface, and forward the frame.|Инкапсулируйте IP-пакет в новый заголовок и трейлер канала передачи данных, соответствующий исходящему интерфейсу, и пересылайте кадр.
|
Figure 3-11 works through a repeat example of a packet sent by PC1 to PC2, followed by a detailed analysis of each device’s routing logic.|На рис. 3-11 представлен повторный пример пакета, отправленного ПК1 на ПК2, с последующим подробным анализом логики маршрутизации каждого устройства.
Each explanation includes the details about how PC1 and each of the three routers builds the appropriate new data-link headers.|Каждое объяснение включает подробности о том, как ПК1 и каждый из трех маршрутизаторов создают соответствующие новые заголовки канала передачи данных.
|
Figure 3-11 Network Layer and Data-Link Layer Encapsulation The following list explains the forwarding logic at each router, focusing on how the routing integrates with the data link.|Рисунок 3-11 Сетевой уровень и инкапсуляция уровня канала передачи данных В следующем списке объясняется логика пересылки на каждом маршрутизаторе, уделяя особое внимание тому, как маршрутизация интегрируется с каналом передачи данных.
|
Step A.|Шаг А.
PC1 sends the packet to its default router.|ПК1 отправляет пакет своему маршрутизатору по умолчанию.
PC1’s network layer logic builds the IP packet, with a destination address of PC2’s IP address (150.150.4.10).|Логика сетевого уровня ПК1 создает IP-пакет с целевым адресом IP-адреса ПК2 (150.150.4.10).
|
The network layer also performs the analysis to decide that 150.150.4.10 is not in the local IP subnet, so PC1 needs to send the packet to R1 (PC1’s default router).|Сетевой уровень также выполняет анализ, чтобы решить, что 150.150.4.10 не находится в локальной IP-подсети, поэтому ПК1 должен отправить пакет на R1 (маршрутизатор ПК1 по умолчанию).
PC1 places the IP packet into an Ethernet data-link frame, with a destination Ethernet address of R1’s Ethernet address.|ПК1 помещает IP-пакет в кадр канала передачи данных Ethernet с целевым адресом Ethernet или адресом Ethernet маршрутизатора R1.
PC1 sends the frame on to the Ethernet.|ПК1 отправляет кадр в Ethernet.
|
Step B.|Шаг Б.
R1 processes the incoming frame and forwards the packet to R2. Because the incoming Ethernet frame has a destination MAC of R1’s Ethernet MAC, R1 decides to process the frame.|R1 обрабатывает входящий кадр и пересылает пакет R2. Поскольку входящий кадр Ethernet имеет MAC-адрес назначения, равный MAC-адресу Ethernet маршрутизатора R1, маршрутизатор R1 решает обработать кадр.
R1 checks the frame’s FCS for errors, and if none, R1 discards the Ethernet header and trailer.|R1 проверяет FCS кадра на наличие ошибок, и если их нет, R1 отбрасывает заголовок и трейлер Ethernet.
Next, R1 compares the packet’s destination address (150.150.4.10) to its routing table and finds the entry for subnet 150.150.4.0.|Затем R1 сравнивает адрес назначения пакета (150.150.4.10) со своей таблицей маршрутизации и находит запись для подсети 150.150.4.0.
Because the destination address of 150.150.4.10 is in that subnet, R1 forwards the packet out the interface listed in that matching route (Serial0) to next-hop Router R2 (150.150.2.7).|Поскольку адрес назначения 150.150.4.10 находится в этой подсети, R1 пересылает пакет из интерфейса, указанного в этом совпадающем маршруте (Serial0), на маршрутизатор следующего перехода R2 (150.150.2.7).
R1 must first encapsulate the IP packet into an HDLC frame.|R1 должен сначала инкапсулировать IP-пакет в кадр HDLC.
|
Step C.|Шаг C.
R2 processes the incoming frame and forwards the packet to R3. R2 repeats the same general process as R1 when R2 receives the HDLC frame.|R2 обрабатывает входящий кадр и пересылает пакет R3. R2 повторяет тот же общий процесс, что и R1, когда R2 принимает кадр HDLC.
R2 checks the FCS field and finds that no errors occurred and then discards the HDLC header and trailer.|R2 проверяет поле FCS и обнаруживает, что ошибок не произошло, а затем отбрасывает заголовок и трейлер HDLC.
Next, R2 compares the packet’s destination address (150.150.4.10) to its routing table and finds the entry for subnet 150.150.4.0, a route that directs R2 to send the packet out interface Fast Ethernet 0/0 to next-hop router 150.150.3.1 (R3).|Затем R2 сравнивает адрес назначения пакета (150.150.4.10) со своей таблицей маршрутизации и находит запись для подсети 150.150.4.0, маршрут, который указывает R2 отправить интерфейс передачи пакетов Fast Ethernet 0/0 на маршрутизатор следующего перехода 150.150. 3.1 (R3).
But first, R2 must encapsulate the packet in an Ethernet header.|Но сначала R2 должен инкапсулировать пакет в заголовок Ethernet.
That header uses R2’s MAC address and R3’s MAC address on the Ethernet WAN link as the source and destination MAC address, respectively.|Этот заголовок использует MAC-адрес R2 и MAC-адрес R3 в канале Ethernet WAN в качестве MAC-адреса источника и назначения соответственно.
|
Step D.|Шаг D.
R3 processes the incoming frame and forwards the packet to PC2. Like R1 and R2, R3 checks the FCS, discards the old data-link header and trailer, and matches its own route for subnet 150.150.4.0.|R3 обрабатывает входящий кадр и пересылает пакет на ПК2. Подобно R1 и R2, R3 проверяет FCS, отбрасывает старый заголовок и трейлер канала передачи данных и сопоставляет свой собственный маршрут для подсети 150.150.4.0.
R3’s routing table entry for 150.150.4.0 shows that the outgoing interface is R3’s Ethernet interface, but there is no next-hop router because R3 is connected directly to subnet 150.150.4.0.|Запись таблицы маршрутизации R3 для 150.150.4.0 показывает, что исходящий интерфейс является интерфейсом Ethernet R3, но маршрутизатора следующего перехода нет, поскольку R3 подключен непосредственно к подсети 150.150.4.0.
All R3 has to do is encapsulate the packet inside a new Ethernet header and trailer, but with a destination Ethernet address of PC2’s MAC address.|Все, что нужно сделать R3, - это инкапсулировать пакет в новый заголовок и трейлер Ethernet, но с целевым Ethernet-адресом MAC-адреса ПК2.
|
Because the routers build new data-link headers and trailers, and because the new headers contain data-link addresses, the PCs and routers must have some way to decide what datalink addresses to use.|Поскольку маршрутизаторы создают новые заголовки и трейлеры каналов данных, и поскольку новые заголовки содержат адреса каналов данных, ПК и маршрутизаторы должны иметь какой-то способ решить, какие адреса каналов данных использовать.
An example of how the router determines which data-link address to use is the IP Address Resolution Protocol (ARP). ARP dynamically learns the data-link address of an IP host connected to a LAN. For example, at the last step, at the bottom of Figure 3-11, Router R3 would use ARP once to learn PC2’s MAC address before sending any packets to PC2.|Примером того, как маршрутизатор определяет, какой адрес канала передачи данных использовать, является протокол разрешения IP-адресов (ARP). ARP динамически изучает адрес канала передачи данных IP-хоста, подключенного к локальной сети. Например, на последнем шаге в нижней части рисунка 3-11 маршрутизатор R3 будет использовать ARP один раз, чтобы узнать MAC-адрес ПК2 перед отправкой любых пакетов на ПК2.
#### How IP Addressing Helps IP Routing
Как IP-адресация помогает IP-маршрутизации   
__|__
--|--
|
IP defines network layer addresses that identify any host or router interface that connects to a TCP/IP network.|IP определяет адреса сетевого уровня, которые идентифицируют любой интерфейс хоста или маршрутизатора, который подключается к сети TCP / IP.
The idea basically works like a postal address: Any interface that expects to receive IP packets needs an IP address, just like you need a postal address before receiving mail from the postal service.|Идея в основном работает как почтовый адрес: любому интерфейсу, который ожидает получения IP-пакетов, нужен IP-адрес, точно так же, как вам нужен почтовый адрес перед получением почты от почтовой службы.
This next short topic introduces the idea of IP networks and subnets, which are the groups of addresses defined by IP.|В следующем коротком разделе представлена ​​идея IP-сетей и подсетей, которые представляют собой группы адресов, определяемые IP.
|
NOTE IP defines the word network to mean a very specific concept.|ПРИМЕЧАНИЕ IP определяет слово «сеть» как очень конкретное понятие.
To avoid confusion when writing about IP addressing, this book (and others) often avoids using the term network for other uses.|Чтобы избежать путаницы при написании об IP-адресации, в этой (и других) книгах часто избегают использования термина «сеть» для других целей.
In particular, this book uses the term internetwork to refer more generally to a network made up of routers, switches, cables, and other equipment.|В частности, в этой книге термин «объединенная сеть» используется для более общего обозначения сети, состоящей из маршрутизаторов, коммутаторов, кабелей и другого оборудования.
##### Rules for Groups of IP Addresses (Networks and Subnets)
Правила для групп IP-адресов (сетей и подсетей)   
__|__
--|--
|
TCP/IP groups IP addresses together so that IP addresses used on the same physical network are part of the same group.|TCP / IP группирует IP-адреса вместе, так что IP-адреса, используемые в одной физической сети, являются частью одной группы.
IP calls these address groups an IP network or an IP subnet.|IP называет эти группы адресов IP-сетью или IP-подсетью.
|
Using that same postal service analogy, each IP network and IP subnet works like a postal code (or in the United States, a ZIP code).|Используя ту же аналогию с почтовой службой, каждая IP-сеть и IP-подсеть работают как почтовый индекс (или в Соединенных Штатах, как почтовый индекс).
All nearby postal addresses are in the same postal code (ZIP code), while all nearby IP addresses must be in the same IP network or IP subnet.|Все ближайшие почтовые адреса имеют один и тот же почтовый индекс (почтовый индекс), в то время как все ближайшие IP-адреса должны находиться в одной IP-сети или IP-подсети.
|
IP defines specific rules about which IP address should be in the same IP network or IP subnet.|IP определяет определенные правила о том, какой IP-адрес должен находиться в той же IP-сети или IP-подсети.
|
Numerically, the addresses in the same group have the same value in the first part of the addresses.|Численно адреса в одной группе имеют одинаковое значение в первой части адресов.
For example, Figures 3-10 and 3-11 could have used the following conventions:|Например, на рисунках 3-10 и 3-11 могли использоваться следующие условные обозначения:
###### Hosts on the top Ethernet: Addresses start with 150.150.1
Хосты наверху Ethernet: адреса начинаются с 150.150.1   
###### Hosts on the R1–R2 serial link: Addresses start with 150.150.2
Хосты на последовательном канале R1 – R2: адреса начинаются с 150.150.2.   
###### Hosts on the R2–R3 EoMPLS link: Addresses start with 150.150.3
Хосты по ссылке EoMPLS R2 – R3: адреса начинаются с 150.150.3.   
###### Hosts on the bottom Ethernet: Addresses start with 150.150.4
Хосты в нижнем Ethernet: адреса начинаются с 150.150.4   
__|__
--|--
|
From the perspective of IP routing, the grouping of IP addresses means that the routing table can be much smaller.|С точки зрения IP-маршрутизации группировка IP-адресов означает, что таблица маршрутизации может быть намного меньше.
A router can list one routing table entry for each IP network or subnet, instead of one entry for every single IP address.|Маршрутизатор может указать одну запись в таблице маршрутизации для каждой IP-сети или подсети вместо одной записи для каждого IP-адреса.
|
While the list shows just one example of how IP addresses may be grouped, the rules for how to group addresses using subnets will require some work to master the concepts and math.|Хотя в списке показан только один пример того, как могут быть сгруппированы IP-адреса, правила группировки адресов с использованием подсетей потребуют некоторой работы для усвоения концепций и математики.
Part III of this book details IP addressing and subnetting, and you can find other subnetting video and practice products listed in the Introduction to the book.|В части III этой книги подробно описываются IP-адресация и разбиение на подсети, а во введении к книге вы можете найти другие видеоматериалы и практические продукты для разбиения на подсети.
However, the brief version of two of the foundational rules of subnetting can be summarized as follows:|Однако краткую версию двух основополагающих правил разбиения на подсети можно резюмировать следующим образом:
###### Two IP addresses, not separated from each other by a router, must be in the same group
Два IP-адреса, не отделенных друг от друга маршрутизатором, должны быть в одной группе.   
__|__
--|--
|
(subnet).|(подсеть).
###### Two IP addresses, separated from each other by at least one router, must be in different
Два IP-адреса, отделенные друг от друга хотя бы одним маршрутизатором, должны находиться в разных   
__|__
--|--
|
groups (subnets).|группы (подсети).
|
It’s similar to the USPS ZIP code system and how it requires local governments to assign addresses to new buildings.|Он похож на систему почтовых индексов USPS и требует от местных органов власти присваивать адреса новым зданиям.
It would be ridiculous to have two houses next door to each other, whose addresses had different postal/ZIP codes.|Было бы смешно иметь два дома рядом друг с другом, адреса которых имели разные почтовые индексы.
Similarly, it would be silly to have people who live on opposite sides of the country to have addresses with the same postal/|Точно так же было бы глупо иметь людей, живущих на разных концах страны, с одинаковыми почтовыми адресами.
|
ZIP code.|Индекс.
##### The IP Header
Заголовок IP   
__|__
--|--
|
The routing process also makes use of the IPv4 header, as shown in Figure 3-12.|В процессе маршрутизации также используется заголовок IPv4, как показано на рисунке 3-12.
The header lists a 32-bit source IP address, as well as a 32-bit destination IP address.|В заголовке указывается 32-битный IP-адрес источника, а также 32-битный IP-адрес назначения.
The header, of course, has other fields, a few of which matter for other discussions in this book.|В заголовке, конечно же, есть и другие поля, некоторые из которых имеют значение для других обсуждений в этой книге.
The book will refer to this figure as needed, but otherwise, be aware of the 20-byte IP header and the existence of the source and destination IP address fields.|Книга будет ссылаться на этот рисунок по мере необходимости, но в остальном помните о 20-байтовом IP-заголовке и существовании полей IP-адреса источника и назначения.
Note that in the examples so far in this chapter, while routers remove and add data-link headers each time it routes a packet, the IP header remains, with the IP addresses unchanged by the IP routing process.|Обратите внимание, что в примерах, приведенных до сих пор в этой главе, хотя маршрутизаторы удаляют и добавляют заголовки канала передачи данных каждый раз, когда он направляет пакет, заголовок IP остается, а IP-адреса не меняются в процессе маршрутизации IP.
|
Figure 3-12 IPv4 Header, Organized as 4 Bytes Wide for a Total of 20 Bytes|Рисунок 3-12 Заголовок IPv4, организованный как 4 байта, всего 20 байтов
#### How IP Routing Protocols Help IP Routing
Как протоколы IP-маршрутизации помогают IP-маршрутизации   
__|__
--|--
|
For routing logic to work on both hosts and routers, each host and router needs to know something about the TCP/IP internetwork.|Чтобы логика маршрутизации работала как на хостах, так и на маршрутизаторах, каждый хост и маршрутизатор должны кое-что знать об объединенной сети TCP / IP.
Hosts need to know the IP address of their default router so that hosts can send packets to remote destinations.|Хосты должны знать IP-адрес своего маршрутизатора по умолчанию, чтобы хосты могли отправлять пакеты удаленным адресатам.
Routers, however, need to know routes so they forward packets to each and every reachable IP network and IP subnet.|Однако маршрутизаторам необходимо знать маршруты, чтобы они пересылали пакеты в каждую доступную IP-сеть и IP-подсеть.
|
The best method for routers to know all the useful routes is to configure the routers to use the same IP routing protocol.|Лучший способ узнать все полезные маршруты маршрутизаторам - это настроить маршрутизаторы на использование одного и того же протокола IP-маршрутизации.
Alternately, a network engineer could configure (type) all the required routes, on every router.|В качестве альтернативы сетевой инженер может настроить (ввести) все необходимые маршруты на каждом маршрутизаторе.
However, if you enable the same routing protocol on all the routers in a TCP/IP internetwork, with the correct settings, the routers will send routing protocol messages to each other.|Однако, если вы включите один и тот же протокол маршрутизации на всех маршрутизаторах в объединенной сети TCP / IP с правильными настройками, маршрутизаторы будут отправлять сообщения протокола маршрутизации друг другу.
As a result, all the routers will learn routes for all the IP networks and subnets in the TCP/IP internetwork.|В результате все маршрутизаторы узнают маршруты для всех IP-сетей и подсетей в объединенной сети TCP / IP.
|
IP supports a small number of different IP routing protocols.|IP поддерживает небольшое количество различных протоколов IP-маршрутизации.
All use some similar ideas and processes to learn IP routes, but different routing protocols do have some internal differences;|Все они используют схожие идеи и процессы для изучения IP-маршрутов, но разные протоколы маршрутизации имеют некоторые внутренние различия;
|
otherwise, you would not need more than one routing protocol.|в противном случае вам не потребуется более одного протокола маршрутизации.
However, many routing protocols use the same general steps for learning routes:|Однако многие протоколы маршрутизации используют одни и те же общие шаги для изучения маршрутов:
|
Step 1.|Шаг 1.
Each router, independent of the routing protocol, adds a route to its routing table for each subnet directly connected to the router.|Каждый маршрутизатор, независимо от протокола маршрутизации, добавляет маршрут в свою таблицу маршрутизации для каждой подсети, напрямую подключенной к маршрутизатору.
|
Step 2.|Шаг 2.
Each router’s routing protocol tells its neighbors about the routes in its routing table, including the directly connected routes and routes learned from other routers.|Протокол маршрутизации каждого маршрутизатора сообщает своим соседям о маршрутах в своей таблице маршрутизации, включая напрямую подключенные маршруты и маршруты, полученные от других маршрутизаторов.
|
Step 3.|Шаг 3.
After learning a new route from a neighbor, the router’s routing protocol adds a route to its IP routing table, with the next-hop router of that route typically being the neighbor from which the route was learned.|После изучения нового маршрута от соседа протокол маршрутизации маршрутизатора добавляет маршрут в свою таблицу IP-маршрутизации, при этом маршрутизатор следующего перехода этого маршрута обычно является соседом, от которого был получен маршрут.
|
Also, note that at the final step, routers may have to choose between multiple routes to reach a single subnet.|Также обратите внимание, что на последнем этапе маршрутизаторам, возможно, придется выбирать между несколькими маршрутами, чтобы достичь одной подсети.
When that happens, routers place the best currently available route to reach a subnet (based on a measurement called a metric) into the routing table.|Когда это происходит, маршрутизаторы помещают лучший из доступных на данный момент маршрутов для достижения подсети (на основе измерения, называемого метрикой) в таблице маршрутизации.
|
Figure 3-13 shows an example of how a routing protocol works, using the same diagram as in Figures 3-10 and 3-11.|На рисунке 3-13 показан пример того, как работает протокол маршрутизации, с использованием той же схемы, что и на рисунках 3-10 и 3-11.
In this case, IP subnet 150.150.4.0, which consists of all addresses that begin with 150.150.4.0, sits on the Ethernet at the bottom of the figure.|В этом случае IP-подсеть 150.150.4.0, которая состоит из всех адресов, начинающихся с 150.150.4.0, находится в Ethernet в нижней части рисунка.
The figure shows the advertisement of routes for subnet 150.150.4.0 from bottom to top, as described in detail following the figure.|На рисунке показано объявление маршрутов для подсети 150.150.4.0 снизу вверх, как подробно описано после рисунка.
|
Figure 3-13 Example of How Routing Protocols Advertise About Networks and Subnets Follow items A through F shown in the figure to see how each router learns its route to 150.150.4.0.|Рисунок 3-13 Пример того, как протоколы маршрутизации объявляют о сетях и подсетях Следуйте пунктам от A до F, показанным на рисунке, чтобы увидеть, как каждый маршрутизатор изучает свой маршрут к 150.150.4.0.
|
Step A.|Шаг А.
Subnet 150.150.4.0 exists as a subnet at the bottom of the figure, connected to Router R3.|Подсеть 150.150.4.0 существует как подсеть в нижней части рисунка, подключенная к маршрутизатору R3.
|
Step B.|Шаг Б.
R3 adds a connected route for 150.150.4.0 to its IP routing table; this happens without help from the routing protocol.|R3 добавляет подключенный маршрут для 150.150.4.0 в свою таблицу IP-маршрутизации; это происходит без помощи протокола маршрутизации.
|
Step C.|Шаг C.
R3 sends a routing protocol message, called a routing update, to R2, causing R2 to learn about subnet 150.150.4.0.|R3 отправляет сообщение протокола маршрутизации, называемое обновлением маршрутизации, на R2, в результате чего R2 узнает о подсети 150.150.4.0.
|
Step D.|Шаг D.
R2 adds a route for subnet 150.150.4.0 to its routing table.|R2 добавляет маршрут для подсети 150.150.4.0 в свою таблицу маршрутизации.
|
Step E.|Шаг E.
R2 sends a similar routing update to R1, causing R1 to learn about subnet 150.150.4.0.|R2 отправляет аналогичное обновление маршрутизации R1, в результате чего R1 узнает о подсети 150.150.4.0.
|
Step F.|Шаг F.
R1 adds a route for subnet 150.150.4.0 to its routing table.|R1 добавляет маршрут для подсети 150.150.4.0 в свою таблицу маршрутизации.
The route lists R1’s own Serial0 as the outgoing interface and R2 as the next-hop router IP address (150.150.2.7).|Маршрут указывает собственный Serial0 маршрутизатора R1 в качестве исходящего интерфейса, а R2 - в качестве IP-адреса маршрутизатора следующего перехода (150.150.2.7).
### Other Network Layer Features
Другие функции сетевого уровня   
__|__
--|--
|
The TCP/IP network layer defines many functions beyond IP. Sure, IP plays a huge role in networking today, defining IP addressing and IP routing.|Сетевой уровень TCP / IP определяет множество функций помимо IP. Несомненно, IP сегодня играет огромную роль в сетевых технологиях, определяя IP-адресацию и IP-маршрутизацию.
However, other protocols and standards, defined in other Requests For Comments (RFC), play an important role for network layer functions as well.|Однако другие протоколы и стандарты, определенные в других запросах на комментарии (RFC), также играют важную роль для функций сетевого уровня.
For example, routing protocols like Open Shortest Path First (OSPF)|Например, протоколы маршрутизации, такие как Open Shortest Path First (OSPF)
|
exist as separate protocols, defined in separate RFCs.|существуют как отдельные протоколы, определенные в отдельных RFC.
|
This last short section of the chapter introduces three other network layer features that should be helpful to you when reading through the rest of this book.|В этом последнем коротком разделе главы представлены три другие функции сетевого уровня, которые должны быть вам полезны при чтении остальной части этой книги.
These last three topics just help fill in a few holes, helping to give you some perspective and helping you make sense of later discussions as well.|Эти последние три темы просто помогают заполнить несколько пробелов, помогая дать вам некоторую перспективу и помочь вам разобраться в более поздних обсуждениях.
The three topics are|Три темы
###### Domain Name System (DNS)
Система доменных имен (DNS)   
###### Address Resolution Protocol (ARP)
Протокол разрешения адресов (ARP)   
###### Ping
пинг   
#### Using Names and the Domain Name System
Использование имен и системы доменных имен   
__|__
--|--
|
Can you imagine a world in which every time you used an application, you had to refer to it by IP address?|Можете ли вы представить себе мир, в котором каждый раз, когда вы использовали приложение, вам приходилось обращаться к нему по IP-адресу?
Instead of using easy names like google.com or facebook.com, you would have to remember and type IP addresses, like 64.233.177.100. (At press time, 64.233.177.100 was an address used by Google, and you could reach Google’s website by typing that address in a browser.) Certainly, asking users to remember IP addresses would not be user friendly and could drive some people away from using computers at all.|Вместо использования простых имен, таких как google.com или facebook.com, вам нужно запомнить и ввести IP-адреса, например 64.233.177.100. (На момент публикации 64.233.177.100 был адресом, используемым Google, и вы могли попасть на веб-сайт Google, набрав этот адрес в браузере.) Конечно, просить пользователей запомнить IP-адреса было бы неудобно для пользователя и могло бы оттолкнуть некоторых людей от используя компьютеры вообще.
|
Thankfully, TCP/IP defines a way to use hostnames to identify other computers.|К счастью, TCP / IP определяет способ использования имен хостов для идентификации других компьютеров.
The user either never thinks about the other computer or refers to the other computer by name.|Пользователь либо никогда не думает о другом компьютере, либо обращается к нему по имени.
Then, protocols dynamically discover all the necessary information to allow communications based on that name.|Затем протоколы динамически обнаруживают всю необходимую информацию, чтобы разрешить обмен данными на основе этого имени.
|
For example, when you open a web browser and type in the hostname www.google.com, your computer does not send an IP packet with destination IP address www.google.com; it sends an IP packet to an IP address used by the web server for Google.|Например, когда вы открываете веб-браузер и вводите имя хоста www.google.com, ваш компьютер не отправляет IP-пакет с целевым IP-адресом www.google.com; он отправляет IP-пакет на IP-адрес, используемый веб-сервером для Google.
TCP/IP needs a way to let a computer find the IP address used by the listed hostname, and that method uses the Domain Name System (DNS).|TCP / IP необходим способ, позволяющий компьютеру находить IP-адрес, используемый указанным именем хоста, и этот метод использует систему доменных имен (DNS).
|
Enterprises use the DNS process to resolve names into the matching IP address, as shown in the example in Figure 3-14.|Предприятия используют процесс DNS для преобразования имен в соответствующий IP-адрес, как показано в примере на рис. 3-14.
In this case, PC11, on the left, needs to connect to a server named Server1.|В этом случае ПК11 слева должен подключиться к серверу с именем Server1.
At some point, the user either types in the name Server1 or some application on PC11 refers to that server by name.|В какой-то момент пользователь либо вводит имя Server1, либо какое-то приложение на PC11 обращается к этому серверу по имени.
At Step 1, PC11 sends a DNS message—a DNS query—to the DNS server.|На шаге 1 ПК11 отправляет DNS-сообщение - DNS-запрос - DNS-серверу.
At Step 2, the DNS server sends back a DNS reply that lists Server1’s IP address.|На шаге 2 DNS-сервер отправляет ответ DNS, в котором указывается IP-адрес Server1.
At Step 3, PC11 can now send an IP packet to destination address|На шаге 3 ПК11 теперь может отправить IP-пакет на адрес назначения.
###### 10.1.2.3, the address used by Server1.
10.1.2.3, адрес, используемый Server1.   
__|__
--|--
|
Figure 3-14 Basic DNS Name Resolution Request Note that the example in Figure 3-14 shows a cloud for the TCP/IP network because the details of the network, including routers, do not matter to the name resolution process.|Рисунок 3-14 Базовый запрос разрешения имени DNS Обратите внимание, что в примере на рисунке 3-14 показано облако для сети TCP / IP, поскольку детали сети, включая маршрутизаторы, не имеют значения для процесса разрешения имени.
|
Routers treat the DNS messages just like any other IP packet, routing them based on the destination IP address.|Маршрутизаторы обрабатывают сообщения DNS так же, как любой другой IP-пакет, маршрутизируя их на основе IP-адреса назначения.
For example, at Step 1 in the figure, the DNS query will list the DNS server’s IP address as the destination address, which any routers will use to forward the packet.|Например, на шаге 1 на рисунке в запросе DNS будет указан IP-адрес DNS-сервера в качестве адреса назначения, который любой маршрутизатор будет использовать для пересылки пакета.
|
Finally, DNS defines much more than just a few messages.|Наконец, DNS определяет гораздо больше, чем просто несколько сообщений.
DNS defines protocols, as well as standards for the text names used throughout the world, and a worldwide set of distributed DNS servers.|DNS определяет протоколы, а также стандарты для текстовых имен, используемых во всем мире, и всемирный набор распределенных DNS-серверов.
The domain names that people use every day when web browsing, which look like www.example.com, follow the DNS naming standards.|Доменные имена, которые люди используют каждый день при просмотре веб-страниц, которые выглядят как www.example.com, соответствуют стандартам именования DNS.
Also, no single DNS server knows all the names and matching IP addresses, but the information is distributed across many DNS servers.|Кроме того, ни один DNS-сервер не знает все имена и соответствующие IP-адреса, но информация распределяется по многим DNS-серверам.
So, the DNS servers of the world work together, forwarding queries to each other, until the server that knows the answer supplies the desired IP address information.|Итак, мировые DNS-серверы работают вместе, пересылая запросы друг другу, пока сервер, который знает ответ, не предоставит желаемую информацию об IP-адресе.
#### The Address Resolution Protocol
Протокол разрешения адресов   
__|__
--|--
|
As discussed in depth throughout this chapter, IP routing logic requires that hosts and routers encapsulate IP packets inside data-link layer frames.|Как подробно обсуждается в этой главе, логика IP-маршрутизации требует, чтобы хосты и маршрутизаторы инкапсулировали IP-пакеты внутри кадров уровня канала данных.
For Ethernet interfaces, how does a router know what MAC address to use for the destination?|Для интерфейсов Ethernet, как маршрутизатор узнает, какой MAC-адрес использовать для назначения?
It uses ARP.|Он использует ARP.
|
On Ethernet LANs, whenever a host or router needs to encapsulate an IP packet in a new Ethernet frame, the host or router knows all the important facts to build that header—except for the destination MAC address.|В локальных сетях Ethernet, когда хосту или маршрутизатору необходимо инкапсулировать IP-пакет в новый кадр Ethernet, хост или маршрутизатор знает все важные факты для построения этого заголовка, за исключением MAC-адреса назначения.
The host knows the IP address of the next device, either another host IP address or the default router IP address.|Хосту известен IP-адрес следующего устройства, либо IP-адрес другого хоста, либо IP-адрес маршрутизатора по умолчанию.
A router knows the IP route used for forwarding the IP packet, which lists the next router’s IP address.|Маршрутизатору известен IP-маршрут, используемый для пересылки IP-пакета, в котором указан IP-адрес следующего маршрутизатора.
However, the hosts and routers do not know those neighboring devices’ MAC addresses beforehand.|Однако хосты и маршрутизаторы заранее не знают MAC-адреса этих соседних устройств.
|
TCP/IP defines the Address Resolution Protocol (ARP) as the method by which any host or router on a LAN can dynamically learn the MAC address of another IP host or router on the same LAN. ARP defines a protocol that includes the ARP Request, which is a message that makes the simple request “if this is your IP address, please reply with your MAC address.”|TCP / IP определяет протокол разрешения адресов (ARP) как метод, с помощью которого любой хост или маршрутизатор в локальной сети может динамически узнавать MAC-адрес другого IP-хоста или маршрутизатора в той же локальной сети. ARP определяет протокол, который включает запрос ARP, который представляет собой сообщение, которое делает простой запрос «если это ваш IP-адрес, ответьте, указав свой MAC-адрес».
|
ARP also defines the ARP Reply message, which indeed lists both the original IP address and the matching MAC address.|ARP также определяет ответное сообщение ARP, в котором действительно перечислены как исходный IP-адрес, так и соответствующий MAC-адрес.
|
Figure 3-15 shows an example that uses the same router and host from the bottom part of the earlier Figure 3-13.|На рис. 3-15 показан пример, в котором используются тот же маршрутизатор и хост, что и в нижней части предыдущего рисунка 3-13.
The figure shows the ARP Request sent by router R3, on the left of the figure, as a LAN broadcast.|На рисунке слева показан запрос ARP, отправленный маршрутизатором R3, в виде широковещательной рассылки по локальной сети.
All devices on the LAN will then process the received frame.|После этого все устройства в локальной сети обработают полученный кадр.
|
On the right, at Step 2, host PC2 sends back an ARP Reply, identifying PC2’s MAC address.|Справа, на шаге 2, хост ПК2 отправляет ответ ARP, идентифицируя MAC-адрес ПК2.
|
The text beside each message shows the contents inside the ARP message itself, which lets PC2 learn R3’s IP address and matching MAC address, and R3 learn PC2’s IP address and matching MAC address.|Текст рядом с каждым сообщением показывает содержимое самого сообщения ARP, что позволяет ПК2 узнать IP-адрес R3 и соответствующий MAC-адрес, а R3 узнать IP-адрес ПК2 и соответствующий MAC-адрес.
|
Note that hosts and routers remember the ARP results, keeping the information in their ARP cache or ARP table.|Обратите внимание, что хосты и маршрутизаторы запоминают результаты ARP, сохраняя информацию в своем кэше ARP или таблице ARP.
A host or router only needs to use ARP occasionally, to build the ARP cache the first time.|Хосту или маршрутизатору необходимо использовать ARP только время от времени, чтобы создать кэш ARP в первый раз.
Each time a host or router needs to send a packet encapsulated in an Ethernet frame, it first checks its ARP cache for the correct IP address and matching MAC address.|Каждый раз, когда хосту или маршрутизатору необходимо отправить пакет, инкапсулированный в кадр Ethernet, он сначала проверяет свой ARP-кеш на предмет правильного IP-адреса и соответствующего MAC-адреса.
Hosts and routers will let ARP cache entries time out to clean up the table, so occasional ARP Requests can be seen.|Хосты и маршрутизаторы позволят записям кэша ARP истечь время для очистки таблицы, поэтому могут быть видны случайные запросы ARP.
|
Figure 3-15 Sample ARP Process NOTE You can see the contents of the ARP cache on most PC operating systems by using the arp -a command from a command prompt.|Рисунок 3-15 Пример процесса ARP ПРИМЕЧАНИЕ. Вы можете увидеть содержимое кэша ARP в большинстве операционных систем ПК, используя команду arp -a из командной строки.
#### ICMP Echo and the ping Command
ICMP Echo и команда ping   
__|__
--|--
|
After you have implemented a TCP/IP internetwork, you need a way to test basic IP connectivity without relying on any applications to be working.|После того, как вы внедрили объединенную сеть TCP / IP, вам понадобится способ проверить базовое IP-соединение, не полагаясь на какие-либо работающие приложения.
The primary tool for testing basic network connectivity is the ping command.|Основным инструментом для проверки базового сетевого подключения является команда ping.
|
Ping (Packet Internet Groper) uses the Internet Control Message Protocol (ICMP), sending a message called an ICMP echo request to another IP address.|Ping (Packet Internet Groper) использует протокол управляющих сообщений Интернета (ICMP), отправляя сообщение, называемое эхо-запросом ICMP, на другой IP-адрес.
The computer with that IP address should reply with an ICMP echo reply.|Компьютер с этим IP-адресом должен ответить эхо-ответом ICMP.
If that works, you successfully have tested the IP network.|Если это работает, вы успешно протестировали IP-сеть.
In other words, you know that the network can deliver a packet from one host to the other and back.|Другими словами, вы знаете, что сеть может доставить пакет от одного хоста к другому и обратно.
ICMP does not rely on any application, so it really just tests basic IP connectivity—Layers 1, 2, and 3 of the OSI model.|ICMP не полагается на какое-либо приложение, поэтому на самом деле он просто проверяет базовое IP-соединение - уровни 1, 2 и 3 модели OSI.
Figure 3-16 outlines the basic process.|На рис. 3-16 показан основной процесс.
|
Figure 3-16 Sample Network, ping Command Note that while the ping command uses ICMP, ICMP does much more.|Рисунок 3-16. Пример сети, команда ping Обратите внимание, что хотя команда ping использует ICMP, ICMP делает гораздо больше.
ICMP defines many messages that devices can use to help manage and control the IP network.|ICMP определяет множество сообщений, которые устройства могут использовать для управления и контроля IP-сети.
### Chapter Review
Обзор главы   
__|__
--|--
|
The “Your Study Plan” element, just before Chapter 1, discusses how you should study and practice the content and skills for each chapter before moving on to the next chapter.|Элемент «Ваш учебный план», расположенный непосредственно перед главой 1, обсуждает, как вы должны изучать и практиковать содержание и навыки для каждой главы, прежде чем переходить к следующей главе.
That element introduces the tools used here at the end of each chapter.|Этот элемент знакомит с инструментами, используемыми здесь, в конце каждой главы.
If you haven’t already done so, take a few minutes to read that section.|Если вы еще этого не сделали, уделите несколько минут, чтобы прочитать этот раздел.
Then come back here and do the useful work of reviewing the chapter to help lock into memory what you just read.|Затем вернитесь сюда и проделайте полезную работу по просмотру главы, чтобы закрепить в памяти то, что вы только что прочитали.
|
Review this chapter’s material using either the tools in the book or interactive tools for the same material found on the book’s companion website.|Просмотрите материал этой главы, используя инструменты из книги или интерактивные инструменты для тех же материалов, которые можно найти на сопутствующем веб-сайте книги.
Table 3-4 outlines the key review elements and where you can find them.|В Таблице 3-4 представлены ключевые элементы обзора и их местонахождение.
To better track your study progress, record when you completed these activities in the second column.|Чтобы лучше отслеживать свои успехи в учебе, отметьте, когда вы выполнили эти задания, во втором столбце.
|
Table 3-4 Chapter Review Tracking Table end.|Таблица 3-4 Окончание таблицы отслеживания главы обзора.
|
Review All the Key Topics Table 3-5 Key Topics for Chapter 3 Table end.|Просмотрите все ключевые темы Таблица 3-5 Ключевые темы в конце таблицы 3 главы.
|
leased line, wide-area network (WAN), telco, serial interface, HDLC, Ethernet over MPLS, Ethernet Line Service (E-Line), default router (default gateway), routing table, IP network, IP subnet, IP packet, routing protocol, dotted-decimal notation (DDN), IPv4 address, unicast IP address, subnetting, hostname, DNS, ARP, ping|выделенная линия, глобальная сеть (WAN), телекоммуникационная компания, последовательный интерфейс, HDLC, Ethernet через MPLS, линия Ethernet (E-Line), маршрутизатор по умолчанию (шлюз по умолчанию), таблица маршрутизации, IP-сеть, IP-подсеть, IP-пакет, протокол маршрутизации, десятичное представление с точками (DDN), IPv4-адрес, одноадресный IP-адрес, подсети, имя хоста, DNS, ARP, ping
## Part I Review
Часть I Обзор   
__|__
--|--
|
Keep track of your part review progress with the checklist shown in Table P1-1.|Следите за ходом проверки деталей с помощью контрольного списка, приведенного в Таблице P1-1.
Details on each task follow the table.|Подробности по каждой задаче приведены в таблице.
|
Table P1-1 Part I Review Checklist Activity 1st Date Completed 2nd Date Completed Repeat All DIKTA Questions Answer Part Review Questions Review Key Topics Repeat All DIKTA Questions For this task, answer the “Do I Know This Already?” questions again for the chapters in this part of the book, using the PTP software.|Таблица P1-1. Контрольный список части I. Действие 1-я дата завершения 2-я дата завершения Повторить все вопросы по DIKTA Ответить на вопросы по части Обзор ключевых тем Повторить все вопросы DIKTA. еще раз задайте вопросы к главам этой части книги, используя программное обеспечение PTP.
Refer to the Introduction to this book, the section titled “How to View Only DIKTA Questions by Chapter or Part,” for help with how to make the PTP software show you DIKTA questions for this part only.|Обратитесь к введению к этой книге, раздел под названием «Как просмотреть только вопросы DIKTA по главам или частям», чтобы узнать, как заставить программное обеспечение PTP отображать вам вопросы DIKTA только для этой части.
|
Answer Part Review Questions For this task, answer the Part Review questions for this part of the book, using the PTP software.|Ответить на вопросы обзора части Для этой задачи ответьте на вопросы обзора части для этой части книги, используя программное обеспечение PTP.
Refer to the Introduction to this book, the section titled “How to View Part Review Questions,” for help with how to make the PTP software show you Part Review questions for this part only. (Note that if you use the questions but then want even more, get the Premium Edition of the book, as detailed in the Introduction, in the section “Other Features,” under the item labeled “eBook.”)|Обратитесь к введению к этой книге, раздел под названием «Как просматривать вопросы для проверки деталей», чтобы узнать, как заставить программное обеспечение PTP отображать вам вопросы проверки деталей только для этой части. (Обратите внимание, что если вы задали вопросы, но затем захотели еще большего, получите премиум-издание книги, как подробно описано во Введении в разделе «Другие функции», в пункте «Электронная книга».)
|
Review Key Topics Browse back through the chapters and look for the Key Topic icons.|Обзор ключевых тем Просмотрите главы и найдите значки ключевых тем.
If you do not remember some details, take the time to reread those topics, or use the Key Topics application(s)|Если вы не помните некоторые детали, найдите время, чтобы перечитать эти темы, или воспользуйтесь приложением (ями) Key Topics
|
found on the companion website.|найдено на сопутствующем сайте.
|
Use Per-Chapter Interactive Review Elements Using the companion website, browse through the interactive review elements, like memory tables and key term flashcards, to review the content from each chapter.|Использование элементов интерактивного обзора по главам Используя сопутствующий веб-сайт, просмотрите интерактивные элементы обзора, такие как таблицы памяти и карточки с ключевыми терминами, чтобы просмотреть содержание каждой главы.
|
Part I provided a broad look at the fundamentals of all parts of networking, focusing on Ethernet LANs, WANs, and IP routing.|В части I был дан общий обзор основ всех частей сети с упором на локальные сети Ethernet, глобальные сети и IP-маршрутизацию.
Parts II and III now drill into depth about the details of Ethernet, which was introduced in Chapter 2, “Fundamentals of Ethernet LANs.”|В частях II и III подробно рассматриваются детали Ethernet, которые были представлены в главе 2 «Основы локальных сетей Ethernet».
|
Part II begins that journey by discussing the basics of building a small Ethernet LAN with Cisco Catalyst switches.|В части II этот путь начинается с обсуждения основ построения небольшой локальной сети Ethernet с коммутаторами Cisco Catalyst.
The journey begins by showing how to access the user interface of a Cisco switch so that you can see evidence of what the switch is doing and configure the switch to act in the ways you want it to act.|Путешествие начинается с демонстрации того, как получить доступ к пользовательскому интерфейсу коммутатора Cisco, чтобы вы могли видеть доказательства того, что делает коммутатор, и настраивать коммутатор, чтобы он действовал так, как вы хотите.
At this point, you should start using whatever lab practice option you chose in the “Your Study Plan” section that preceded Chapter 1, “Introduction to TCP/IP Networking.” (And if you have not yet finalized your plan for how to practice your hands-on skills, now is the time.)|На этом этапе вам следует начать использовать любой вариант лабораторной практики, который вы выбрали в разделе «Ваш план обучения», который предшествовал главе 1 «Введение в сеть TCP / IP». (И если вы еще не завершили свой план, как практиковать свои практические навыки, сейчас самое время.)
|
After you complete Chapter 4 and see how to get into the command-line interface (CLI)|После того, как вы завершите главу 4 и увидите, как войти в интерфейс командной строки (CLI)
|
of a switch, the next three chapters step through some important foundations of how to implement LANs—foundations used by every company that builds LANs with Cisco gear.|Что касается коммутатора, то в следующих трех главах рассматриваются некоторые важные основы реализации локальных сетей - основы, используемые каждой компанией, строящей локальные сети с использованием оборудования Cisco.
|
Chapter 5 takes a close look at Ethernet switching—that is, the logic used by a switch—and how to know what a particular switch is doing.|В главе 5 подробно рассматривается коммутация Ethernet, то есть логика, используемая коммутатором, и то, как узнать, что делает конкретный коммутатор.
Chapter 6 shows the ways to configure a switch for remote access with Telnet and Secure Shell (SSH), along with a variety of other useful commands that will help you when you work with any real lab gear, simulator, or any other practice tools.|В главе 6 показаны способы настройки коммутатора для удаленного доступа с помощью Telnet и Secure Shell (SSH), а также множество других полезных команд, которые помогут вам при работе с любым реальным лабораторным оборудованием, симулятором или любыми другими инструментами для практики.
Chapter 7, the final chapter in Part II, shows how to configure and verify the operation of switch interfaces for several important features, including speed, duplex, and autonegotiation.|В главе 7, заключительной главе части II, показано, как настроить и проверить работу интерфейсов коммутатора для нескольких важных функций, включая скорость, дуплекс и автосогласование.
