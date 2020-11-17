## Introduction to TCP/IP Networking
Введение в сеть TCP / IP   
### This chapter covers the following exam topics:
В этой главе рассматриваются следующие экзаменационные темы:   
- 1.0 Network Fundamentals   
1.0 Основы сети   
- 1.3 Compare physical interface and cabling types   
1.3 Сравните физический интерфейс и типы кабелей   
- 1.3.a Single-mode fiber, multimode fiber, copper   
1.3.a Одномодовое волокно, многомодовое волокно, медь   
- 1.3.b Connections (Ethernet shared media and point-to-point)   
1.3.b Подключения (общая среда Ethernet и точка-точка)   
__|__
--|--
Welcome to the first chapter in your study for CCNA! This chapter begins Part I, which|Добро пожаловать в первую главу вашего исследования CCNA! Эта глава начинается с части I, в которой
focuses on the basics of networking.|фокусируется на основах работы в сети.
Networks work correctly because the various devices and software follow the rules. Those|Сети работают правильно, потому что различные устройства и программное обеспечение подчиняются правилам. Те
rules come in the form of standards and protocols, which are agreements of a particular|правила представлены в форме стандартов и протоколов, которые являются соглашениями определенных
part of how a network should work. However, the sheer number of standards and protocols|часть того, как сеть должна работать. Однако огромное количество стандартов и протоколов
available can make it difficult for the average network engineer to think about and work|доступность может усложнить работу среднего сетевого инженера
with networks—so the world of networking has used several networking models over time.|с сетями - таким образом, мир сетей использовал несколько сетевых моделей с течением времени.
Networking models define a structure and different categories (layers) of standards and protocols. As new standards and protocols emerge over time, networkers can think of those new|Сетевые модели определяют структуру и различные категории (уровни) стандартов и протоколов. По мере появления новых стандартов и протоколов сетевики могут думать об этих новых
details in the context of a working model.|детали в разрезе действующей модели.
You can think of a networking model as you think of a set of architectural plans for building|Вы можете думать о сетевой модели, как о наборе архитектурных планов для построения
a house. A lot of different people work on building your house, such as framers, electricians,|дом. Над строительством вашего дома работает много разных людей, таких как строители, электрики,
bricklayers, painters, and so on. The blueprint helps ensure that all the different pieces of the|каменщики, маляры и т. д. План помогает гарантировать, что все различные части
house work together as a whole. Similarly, the people who make networking products, and|дом работают вместе в целом. Точно так же люди, которые создают сетевые продукты, и
the people who use those products to build their own computer networks, follow a particular|люди, которые используют эти продукты для построения собственных компьютерных сетей, следуют определенным
networking model. That networking model defines rules about how each part of the network|сетевая модель. Эта сетевая модель определяет правила того, как каждая часть сети
should work, as well as how the parts should work together so that the entire network functions|должны работать, а также как части должны работать вместе, чтобы вся сеть функционировала
correctly.|правильно.
Today, TCP/IP rules as the most pervasive networking model in use. You can find support for|Сегодня правила TCP / IP являются наиболее распространенной сетевой моделью. Вы можете найти поддержку
TCP/IP on practically every computer operating system (OS) in existence today, from mobile|TCP / IP практически во всех компьютерных операционных системах (ОС), существующих сегодня, с мобильных
phones to mainframe computers. Every network built using Cisco products today supports|телефоны к мэйнфреймам. Каждая сеть, построенная с использованием продуктов Cisco, сегодня поддерживает
TCP/IP. And not surprisingly, the CCNA exam focuses heavily on TCP/IP. This chapter uses|TCP / IP. И неудивительно, что экзамен CCNA уделяет большое внимание TCP / IP. В этой главе используется
TCP/IP for one of its main purposes: to present various concepts about networking using the|TCP / IP для одной из основных целей: представить различные концепции сети с использованием
context of the different roles and functions in the TCP/IP model.|контекст различных ролей и функций в модели TCP / IP.
### “Do I Know This Already?” Quiz
«Знаю ли я это уже?» Викторина   
__|__
--|--
Take the quiz (either here or use the PTP software) if you want to use the score to help you|Пройдите тест (здесь или используйте программное обеспечение PTP), если вы хотите использовать оценку, чтобы помочь вам
decide how much time to spend on this chapter. The letter answers are listed at the bottom|решите, сколько времени потратить на эту главу. Ответы на буквы указаны внизу
of the page following the quiz. Appendix C, found both at the end of the book as well as on|страницы после викторины. Приложение C находится как в конце книги, так и на
the companion website, includes both the answers and explanations. You can also find both|сопутствующий веб-сайт включает как ответы, так и пояснения. Вы также можете найти оба
answers and explanations in the PTP testing software.|ответы и пояснения в программе тестирования PTP.
- Table 1-1 “Do I Know This Already?” Foundation Topics Section-to-Question Mapping
Таблица 1-1 «Знаю ли я это уже?» Сопоставление разделов с вопросами по основным темам   
__|__
--|--
Foundation Topics Section Questions|Основные темы раздела Вопросы
Perspectives on Networking None|Перспективы сетевых технологий Нет
TCP/IP Networking Model 1–4|Сетевая модель TCP / IP 1–4
Data Encapsulation Terminology 5–7|Терминология инкапсуляции данных 5–7
- 1. Which of the following protocols are examples of TCP/IP transport layer protocols?
1. Какие из следующих протоколов являются примерами протоколов транспортного уровня TCP / IP?   
__|__
--|--
(Choose two answers.)|(Выберите два ответа.)
a. Ethernet|а. Ethernet
b. HTTP|б. HTTP
c. IP|c. IP
d. UDP|d. UDP
e. SMTP|е. SMTP
f. TCP|f. TCP
- 2. Which of the following protocols are examples of TCP/IP data-link layer protocols?
2. Какие из следующих протоколов являются примерами протоколов уровня канала передачи данных TCP / IP?   
__|__
--|--
(Choose two answers.)|(Выберите два ответа.)
a. Ethernet|а. Ethernet
b. HTTP|б. HTTP
c. IP|c. IP
d. UDP|d. UDP
e. SMTP|е. SMTP
f. TCP|f. TCP
g. PPP|грамм. PPP
- 3. The process of HTTP asking TCP to send some data and making sure that it is received
3. Процесс HTTP-запроса TCP на отправку некоторых данных и обеспечение их получения.   
__|__
--|--
correctly is an example of what?|правильно это пример чего?
a. Same-layer interaction|а. Взаимодействие на одном уровне
b. Adjacent-layer interaction|б. Взаимодействие смежных слоев
c. OSI model|c. Модель OSI
d. All of these answers are correct.|d. Все эти ответы верны.
- 4. The process of TCP on one computer marking a TCP segment as segment 1, and the
4. Процесс TCP на одном компьютере, помечающий сегмент TCP как сегмент 1, и   
__|__
--|--
receiving computer then acknowledging the receipt of TCP segment 1 is an example of|принимающий компьютер, затем подтверждающий получение сегмента TCP 1, является примером
what?|что?
a. Data encapsulation|а. Инкапсуляция данных
b. Same-layer interaction|б. Взаимодействие на одном уровне
c. Adjacent-layer interaction|c. Взаимодействие смежных слоев
d. OSI model|d. Модель OSI
e. All of these answers are correct.|е. Все эти ответы верны.
- 5. The process of a web server adding a TCP header to the contents of a web page, followed by adding an IP header and then adding a data-link header and trailer, is an
5. Процесс добавления веб-сервером заголовка TCP к содержимому веб-страницы, с последующим добавлением заголовка IP и последующим добавлением заголовка и трейлера ссылки на данные, является   
__|__
--|--
example of what?|пример чего?
a. Data encapsulation|а. Инкапсуляция данных
b. Same-layer interaction|б. Взаимодействие на одном уровне
c. OSI model|c. Модель OSI
d. All of these answers are correct.|d. Все эти ответы верны.
- 6. Which of the following terms is used specifically to identify the entity created when
6. Какой из следующих терминов используется специально для обозначения организации, созданной при   
__|__
--|--
encapsulating data inside data-link layer headers and trailers?|инкапсулируют данные внутри заголовков и трейлеров канального уровня?
a. Data|а. Данные
b. Chunk|б. Кусок
c. Segment|c. Сегмент
d. Frame|d. Рамка
e. Packet|е. Пакет
7. Which OSI encapsulation term can be used instead of the term frame?|7. Какой термин инкапсуляции OSI можно использовать вместо термина фрейм?
a. Layer 1 PDU|а. PDU уровня 1
b. Layer 2 PDU|б. PDU уровня 2
c. Layer 3 PDU|c. PDU уровня 3
d. Layer 5 PDU|d. PDU уровня 5
e. Layer 7 PDU|е. PDU уровня 7
## Foundation Topics
Основные темы   
### Perspectives on Networking
Перспективы сетевых технологий   
__|__
--|--
So, you are new to networking. Like many people, your perspective about networks might|Итак, вы новичок в нетворкинге. Как и у многих людей, ваше мнение о сетях может
be that of a user of the network, as opposed to the network engineer who builds networks.|быть пользователем сети, а не сетевым инженером, который строит сети.
For some, your view of networking might be based on how you use the Internet, from home,|Для некоторых ваше представление о сети может быть основано на том, как вы используете Интернет, из дома,
using a high-speed Internet connection like digital subscriber line (DSL) or cable TV, as|используя высокоскоростное Интернет-соединение, такое как цифровая абонентская линия (DSL) или кабельное телевидение, как
shown in Figure 1-1.|показано на рисунке 1-1.
The Internet|Интернет
Ethernet|Ethernet
Cable|Кабель
CATV|Кабельное телевидение
Cable|Кабель
Wireless DSL|Беспроводной DSL
The top part of the figure shows a typical high-speed cable Internet user. The PC connects|В верхней части рисунка показан типичный пользователь высокоскоростного кабельного Интернета. ПК подключает
to a cable modem using an Ethernet cable. The cable modem then connects to a cable TV|к кабельному модему с помощью кабеля Ethernet. Затем кабельный модем подключается к кабельному телевидению.
(CATV) outlet in the wall using a round coaxial cable—the same kind of cable used to connect your TV to the CATV wall outlet. Because cable Internet services provide service continuously, the user can just sit down at the PC and start sending email, browsing websites,|(CATV) в стене с помощью круглого коаксиального кабеля - того же типа кабеля, который используется для подключения вашего телевизора к настенной розетке CATV. Поскольку кабельные интернет-службы предоставляют услуги непрерывно, пользователь может просто сесть за компьютер и начать отправлять электронную почту, просматривать веб-сайты и т. Д.
making Internet phone calls, and using other tools and applications.|совершение телефонных звонков через Интернет и использование других инструментов и приложений.
The lower part of the figure uses two different technologies. First, the tablet computer uses|В нижней части рисунка используются две разные технологии. Во-первых, планшетный компьютер использует
wireless technology that goes by the name wireless local-area network (wireless LAN), or|беспроводная технология, известная как беспроводная локальная сеть (беспроводная локальная сеть), или
Wi-Fi, instead of using an Ethernet cable. In this example, the router uses a different technology, DSL, to communicate with the Internet.|Wi-Fi вместо использования кабеля Ethernet. В этом примере маршрутизатор использует другую технологию, DSL, для связи с Интернетом.
Both home-based networks and networks built for use by a company make use of similar|И домашние сети, и сети, созданные для использования компанией, используют аналогичные
networking technologies. The Information Technology (IT) world refers to a network created|сетевые технологии. Мир информационных технологий (ИТ) относится к сети, созданной
by one corporation, or enterprise, for the purpose of allowing its employees to communicate, as an enterprise network. The smaller networks at home, when used for business purposes, often go by the name small office/home office (SOHO) networks.|одной корпорацией или предприятием, чтобы позволить своим сотрудникам общаться в рамках корпоративной сети. Домашние сети меньшего размера, когда они используются для деловых целей, часто называются сетями малого офиса / домашнего офиса (SOHO).
Users of enterprise networks have some idea about the enterprise network at their company|Пользователи корпоративных сетей имеют некоторое представление о корпоративной сети в своей компании.
or school. People realize that they use a network for many tasks. PC users might realize that|или школа. Люди понимают, что они используют сеть для множества задач. Пользователи ПК могут понять, что
their PC connects through an Ethernet cable to a matching wall outlet, as shown at the top|их компьютер подключается через кабель Ethernet к соответствующей розетке, как показано вверху
of Figure 1-2. Those same users might use wireless LANs with their laptop when going to a|на Рисунке 1-2. Те же пользователи могут использовать беспроводные локальные сети со своим ноутбуком, когда собираются
meeting in the conference room as well. Figure 1-2 shows these two end-user perspectives|встреча в конференц-зале. На рисунке 1-2 показаны эти две точки зрения конечного пользователя.
on an enterprise network.|в корпоративной сети.
Enterprise Network|Корпоративная сеть
Ethernet|Ethernet
Cable|Кабель
Wireless|Беспроводной
SW1|SW1
Figure 1-2 Example Representation of an Enterprise Network|Рисунок 1-2 Пример представления корпоративной сети
NOTE In networking diagrams, a cloud represents a part of a network whose details are|ПРИМЕЧАНИЕ. На сетевых диаграммах облако представляет собой часть сети, детали которой
not important to the purpose of the diagram. In this case, Figure 1-2 ignores the details of|не важно для цели диаграммы. В этом случае на рисунке 1-2 игнорируются детали
how to create an enterprise network.|как создать корпоративную сеть.
Some users might not even have a concept of the network at all. Instead, these users just|Некоторые пользователи могут вообще не иметь представления о сети. Вместо этого эти пользователи просто
enjoy the functions of the network—the ability to post messages to social media sites, make|пользоваться функциями сети - возможностью публиковать сообщения в социальных сетях, делать
phone calls, search for information on the Internet, listen to music, and download countless|телефонные звонки, поиск информации в Интернете, слушать музыку и скачивать бесчисленное количество
apps to their phones—without caring about how it works or how their favorite device connects to the network.|приложения на свои телефоны, не беспокоясь о том, как они работают или как их любимые устройства подключаются к сети.
Regardless of how much you already know about how networks work, this book and the|Независимо от того, сколько вы уже знаете о работе сетей, эта книга и
related certification help you learn how networks do their job. That job is simply this:|соответствующая сертификация поможет вам узнать, как сети выполняют свою работу. Эта работа проста:
moving data from one device to another. The rest of this chapter, and the rest of this first|перенос данных с одного устройства на другое. Остальная часть этой главы и остальная часть этой первой
part of the book, reveals the basics of how to build enterprise networks so that they can|часть книги, раскрывает основы построения корпоративных сетей, чтобы они могли
deliver data between two devices.|передавать данные между двумя устройствами.
## TCP/IP Networking Model
Модель сети TCP / IP   
__|__
--|--
A networking model, sometimes also called either a networking architecture or networking blueprint, refers to a comprehensive set of documents. Individually, each document|Сетевая модель, иногда также называемая сетевой архитектурой или сетевым планом, относится к исчерпывающему набору документов. Индивидуально каждый документ
describes one small function required for a network; collectively, these documents define|описывает одну небольшую функцию, необходимую для сети; в совокупности эти документы определяют
everything that should happen for a computer network to work. Some documents define|все, что должно произойти для работы компьютерной сети. Некоторые документы определяют
a protocol, which is a set of logical rules that devices must follow to communicate. Other|протокол, который представляет собой набор логических правил, которым должны следовать устройства для связи. Другие
documents define some physical requirements for networking. For example, a document|документы определяют некоторые физические требования к сети. Например, документ
could define the voltage and current levels used on a particular cable when transmitting data.|может определять уровни напряжения и тока, используемые на конкретном кабеле при передаче данных.
You can think of a networking model as you think of an architectural blueprint for building a|Вы можете думать о сетевой модели, как об архитектурном проекте для построения
house. Sure, you can build a house without the blueprint. However, the blueprint can ensure|дом. Конечно, вы можете построить дом без чертежа. Однако план может гарантировать
that the house has the right foundation and structure so that it will not fall down, and it has|что у дома правильный фундамент и конструкция, чтобы он не упал, и
the correct hidden spaces to accommodate the plumbing, electrical, gas, and so on. Also, the|правильные скрытые пространства для размещения сантехники, электричества, газа и так далее. Так же
many different people that build the house using the blueprint—such as framers, electricians,|много разных людей, которые строят дом по чертежам, например, строителей, электриков,
bricklayers, painters, and so on—know that if they follow the blueprint, their part of the|каменщики, художники и т. д. - знают, что если они следуют чертежу, их часть
work should not cause problems for the other workers.|работа не должна создавать проблем для других работников.
Similarly, you could build your own network—write your own software, build your own|Точно так же вы можете построить свою собственную сеть - написать собственное программное обеспечение, создать свое собственное
networking cards, and so on—to create a network. However, it is much easier to simply buy|сетевые карты и т. д. - для создания сети. Однако гораздо проще просто купить
and use products that already conform to some well-known networking model or blueprint.|и использовать продукты, которые уже соответствуют какой-либо известной сетевой модели или проекту.
Because the networking product vendors build their products with some networking model|Поскольку поставщики сетевых продуктов создают свои продукты с некоторой сетевой моделью
in mind, their products should work well together.|в виду, их продукты должны хорошо работать вместе.
### History Leading to TCP/IP
История, ведущая к TCP / IP   
__|__
--|--
Today, the world of computer networking uses one networking model: TCP/IP. However, the|Сегодня в мире компьютерных сетей используется одна сетевая модель: TCP / IP. Тем не менее
world has not always been so simple. Once upon a time, networking protocols didn’t exist,|мир не всегда был таким простым. Когда-то сетевых протоколов не существовало,
including TCP/IP. Vendors created the first networking protocols; these protocols supported|включая TCP / IP. Производители создали первые сетевые протоколы; эти протоколы поддерживаются
only that vendor’s computers.|только компьютеры этого производителя.
For example, IBM, the computer company with the largest market share in many markets|Например, IBM, компьютерная компания с самой большой долей рынка на многих рынках.
back in the 1970s and 1980s, published its Systems Network Architecture (SNA) networking|еще в 1970-х и 1980-х годах опубликовал свою Системную сетевую архитектуру (SNA).
model in 1974. Other vendors also created their own proprietary networking models. As a|модель в 1974 году. Другие производители также создали свои собственные сетевые модели. Как
result, if your company bought computers from three vendors, network engineers often had|В результате, если ваша компания покупала компьютеры у трех поставщиков, сетевым инженерам часто приходилось
to create three different networks based on the networking models created by each company, and then somehow connect those networks, making the combined networks much more|создать три разные сети на основе сетевых моделей, созданных каждой компанией, а затем каким-то образом связать эти сети, что сделает объединенные сети намного более удобными.
complex. The left side of Figure 1-3 shows the general idea of what a company’s enterprise|сложный. В левой части рисунка 1-3 показано общее представление о том, что предприятие
network might have looked like back in the 1980s, before TCP/IP became common in enterprise internetworks.|Сеть могла выглядеть так, как в 1980-х, до того, как TCP / IP стал обычным явлением в корпоративных объединенных сетях.
Answers to the “Do I Know This Already?” quiz:|Ответы на вопрос «Знаю ли я это уже?» викторина:
1 D and F 2 A and G 3 B 4 B 5 A 6 D 7 B|1 D и F 2 A и G 3 B 4 B 5 A 6 D 7 B
IBM DEC 1|IBM DEC 1
1980s|1980-е
IBM DEC|IBM DEC
TCP/IP|TCP / IP
Other|Другие
Vendor|Продавец
Other|Другие
Vendor|Продавец
1990s|1990-е
TCP/IP|TCP / IP
2000s|2000-е
Figure 1-3 Historical Progression: Proprietary Models to the Open TCP/IP Model|Рисунок 1-3 История развития: проприетарные модели к открытой модели TCP / IP
Although vendor-defined proprietary networking models often worked well, having an|Хотя проприетарные сетевые модели, определенные производителем, часто работают хорошо,
open, vendor-neutral networking model would aid competition and reduce complexity.|открытая сетевая модель, не зависящая от поставщика, будет способствовать конкуренции и снизить сложность.
The International Organization for Standardization (ISO) took on the task to create such a|Международная организация по стандартизации (ISO) взяла на себя задачу создать такой
model, starting as early as the late 1970s, beginning work on what would become known|модель, начавшаяся еще в конце 1970-х годов, начав работу над тем, что станет известным
as the Open Systems Interconnection (OSI) networking model. ISO had a noble goal for the|как сетевая модель взаимодействия открытых систем (OSI). У ISO была благородная цель
OSI model: to standardize data networking protocols to allow communication among all|Модель OSI: стандартизация сетевых протоколов передачи данных для обеспечения связи между всеми
computers across the entire planet. ISO worked toward this ambitious and noble goal, with|компьютеры по всей планете. ISO работала над достижением этой амбициозной и благородной цели, с
participants from most of the technologically developed nations on Earth participating in|участники из большинства технологически развитых стран на Земле, участвующие в
the process.|процесс.
A second, less-formal effort to create an open, vendor-neutral, public networking model|Вторая, менее формальная попытка создать открытую, независимую от поставщика модель общедоступных сетей.
sprouted forth from a U.S. Department of Defense (DoD) contract. Researchers at various|возникла из контракта с Министерством обороны США (DoD). Исследователи различных
universities volunteered to help further develop the protocols surrounding the original DoD|университеты вызвались помочь в дальнейшей разработке протоколов, относящихся к первоначальному DoD
work. These efforts resulted in a competing open networking model called TCP/IP.|Работа. Эти усилия привели к созданию конкурирующей открытой сетевой модели под названием TCP / IP.
During the 1990s, companies began adding OSI, TCP/IP, or both to their enterprise networks.|В течение 1990-х годов компании начали добавлять OSI, TCP / IP или и то, и другое в свои корпоративные сети.
However, by the end of the 1990s, TCP/IP had become the common choice, and OSI fell|Однако к концу 1990-х TCP / IP стал обычным выбором, и OSI упала.
away. The center part of Figure 1-3 shows the general idea behind enterprise networks in that|прочь. В центральной части рисунка 1-3 показана общая идея корпоративных сетей в
decade—still with networks built upon multiple networking models but including TCP/IP.|десятилетие - сети по-прежнему построены на нескольких сетевых моделях, но включают TCP / IP.
Here in the twenty-first century, TCP/IP dominates. Proprietary networking models still|Здесь, в двадцать первом веке, доминирует TCP / IP. Проприетарные сетевые модели все еще
exist, but they have mostly been discarded in favor of TCP/IP. The OSI model, whose development suffered in part because of a slower formal standardization process as compared|существуют, но в основном от них отказались в пользу TCP / IP. Модель OSI, разработка которой частично пострадала из-за более медленного формального процесса стандартизации по сравнению с
with TCP/IP, never succeeded in the marketplace. And TCP/IP, the networking model originally created almost entirely by a bunch of volunteers, has become the most prolific network|с TCP / IP никогда не добился успеха на рынке. И TCP / IP, сетевая модель, изначально созданная почти полностью группой добровольцев, стала самой плодовитой сетью.
model ever, as shown on the right side of Figure 1-3.|модели, как показано на правой стороне рисунка 1-3.
In this chapter, you will read about some of the basics of TCP/IP. Although you will learn|В этой главе вы прочитаете о некоторых основах TCP / IP. Хотя вы узнаете
some interesting facts about TCP/IP, the true goal of this chapter is to help you understand|некоторые интересные факты о TCP / IP, настоящая цель этой главы - помочь вам понять
what a networking model or networking architecture really is and how it works.|что такое сетевая модель или сетевая архитектура и как она работает.
Also in this chapter, you will learn about some of the jargon used with OSI. Will any of you|Также в этой главе вы узнаете о некоторых жаргонах, используемых в OSI. Будет ли кто-нибудь из вас
ever work on a computer that is using the full OSI protocols instead of TCP/IP? Probably|когда-нибудь работали на компьютере, который использует полные протоколы OSI вместо TCP / IP? Наверное
not. However, you will often use terms relating to OSI.|не. Однако вы часто будете использовать термины, относящиеся к OSI.
### Overview of the TCP/IP Networking Model
Обзор сетевой модели TCP / IP   
__|__
--|--
The TCP/IP model both defines and references a large collection of protocols that allow|Модель TCP / IP определяет и ссылается на большой набор протоколов, которые позволяют
computers to communicate. To define a protocol, TCP/IP uses documents called Requests|компьютеры для связи. Для определения протокола TCP / IP использует документы, называемые запросами.
For Comments (RFC). (You can find these RFCs using any online search engine.) The TCP/IP|Для комментариев (RFC). (Вы можете найти эти RFC с помощью любой поисковой системы в Интернете.) Протокол TCP / IP
model also avoids repeating work already done by some other standards body or vendor consortium by simply referring to standards or protocols created by those groups. For example,|Модель также избегает повторения работы, уже проделанной другим органом по стандартизации или консорциумом поставщиков, просто ссылаясь на стандарты или протоколы, созданные этими группами. Например,
the Institute of Electrical and Electronic Engineers (IEEE) defines Ethernet LANs; the|Институт инженеров по электротехнике и электронике (IEEE) определяет локальные сети Ethernet; то
TCP/IP model does not define Ethernet in RFCs, but refers to IEEE Ethernet as an option.|Модель TCP / IP не определяет Ethernet в RFC, но в качестве опции ссылается на IEEE Ethernet.
The TCP/IP model creates a set of rules that allows us all to take a computer (or mobile|Модель TCP / IP создает набор правил, которые позволяют всем нам использовать компьютер (или мобильный телефон).
device) out of the box, plug in all the right cables, turn it on, and connect to and use the|устройства) прямо из коробки, подключите все нужные кабели, включите его, подключите и используйте
network. You can use a web browser to connect to your favorite website, use most any app,|сеть. Вы можете использовать веб-браузер для подключения к любимому веб-сайту, использовать практически любое приложение,
and it all works. How? Well, the OS on the computer implements parts of the TCP/IP model.|и все работает. Как? Что ж, ОС на компьютере реализует части модели TCP / IP.
The Ethernet card, or wireless LAN card, built in to the computer implements some LAN|Карта Ethernet или карта беспроводной локальной сети, встроенная в компьютер, реализует некоторые функции локальной сети.
standards referenced by the TCP/IP model. In short, the vendors that created the hardware|стандарты, на которые ссылается модель TCP / IP. Короче говоря, поставщики, создавшие оборудование
and software implemented TCP/IP.|и программно реализованный TCP / IP.
To help people understand a networking model, each model breaks the functions into a small|Чтобы помочь людям понять сетевую модель, каждая модель разбивает функции на небольшой
number of categories called layers. Each layer includes protocols and standards that relate to|количество категорий, называемых слоями. Каждый уровень включает протоколы и стандарты, относящиеся к
that category of functions, as shown in Figure 1-4.|эту категорию функций, как показано на рисунке 1-4.
TCP/IP Model|Модель TCP / IP
Application|заявка
Transport|Транспорт
Network|Сеть
Data Link|Канал передачи данных
Physical|Физический
Figure 1-4 The TCP/IP Networking Models|Рисунок 1-4 Сетевые модели TCP / IP
The TCP/IP model shows the more common terms and layers used when people talk about|Модель TCP / IP показывает наиболее общие термины и уровни, используемые, когда люди говорят о
TCP/IP today. The bottom layer focuses on how to transmit bits over each individual link.|TCP / IP сегодня. Нижний уровень фокусируется на том, как передавать биты по каждому отдельному каналу.
The data-link layer focuses on sending data over one type of physical link: for instance,|Уровень канала передачи данных ориентирован на отправку данных по физическому каналу одного типа: например,
networks use different data-link protocols for Ethernet LANs versus wireless LANs. The network layer focuses on delivering data over the entire path from the original sending computer to the final destination computer. And the top two layers focus more on the applications|сети используют разные протоколы передачи данных для локальных сетей Ethernet и беспроводных локальных сетей. Сетевой уровень фокусируется на доставке данных по всему пути от исходного компьютера-отправителя до конечного компьютера-получателя. И два верхних слоя больше ориентированы на приложения.
that need to send and receive data.|которые необходимо отправлять и получать данные.
NOTE A slightly different four-layer original version of the TCP/IP model exists in RFC|ПРИМЕЧАНИЕ. В RFC существует немного другая четырехуровневая исходная версия модели TCP / IP.
1122, but for the purposes of both real networking and for today’s CCNA, use the five-layer|1122, но как для реальных сетей, так и для сегодняшней CCNA используйте пятиуровневую
model shown here in Figure 1-4.|Модель показана здесь на Рисунке 1-4.
Many of you will have already heard of several TCP/IP protocols, like the examples listed in|Многие из вас уже слышали о нескольких протоколах TCP / IP, например о примерах, перечисленных в
Table 1-2. Most of the protocols and standards in this table will be explained in more detail|Таблица 1-2. Большинство протоколов и стандартов в этой таблице будет объяснено более подробно.
as you work through this book. Following the table, this section takes a closer look at the|пока вы работаете над этой книгой. После таблицы в этом разделе более подробно рассматривается
layers of the TCP/IP model.|уровни модели TCP / IP.
Table 1-2 TCP/IP Architectural Model and Example Protocols|Таблица 1-2 Архитектурная модель TCP / IP и примеры протоколов
TCP/IP Architecture Layer Example Protocols|Примеры протоколов уровня архитектуры TCP / IP
Application HTTP, POP3, SMTP|Приложение HTTP, POP3, SMTP
Transport TCP, UDP|Транспортный TCP, UDP
Internet IP, ICMP|Интернет IP, ICMP
Data Link & Physical Ethernet, 802.11 (Wi-Fi)|Канал передачи данных и физический Ethernet, 802.11 (Wi-Fi)
## TCP/IP Application Layer
Уровень приложений TCP / IP   
__|__
--|--
TCP/IP application layer protocols provide services to the application software running on a|Протоколы прикладного уровня TCP / IP предоставляют услуги прикладному программному обеспечению, работающему на
computer. The application layer does not define the application itself, but it defines services|компьютер. Уровень приложения не определяет само приложение, но определяет службы.
that applications need. For example, application protocol HTTP defines how web browsers|что приложениям нужно. Например, протокол приложения HTTP определяет, как веб-браузеры
can pull the contents of a web page from a web server. In short, the application layer provides an interface between software running on a computer and the network itself.|может извлекать содержимое веб-страницы с веб-сервера. Короче говоря, уровень приложений обеспечивает интерфейс между программным обеспечением, работающим на компьютере, и самой сетью.
Arguably, the most popular TCP/IP application today is the web browser. Many major software vendors either have already changed or are changing their application software to support access from a web browser. And thankfully, using a web browser is easy: You start a|Возможно, самым популярным приложением TCP / IP сегодня является веб-браузер. Многие крупные поставщики программного обеспечения либо уже изменили, либо меняют свое прикладное программное обеспечение для поддержки доступа через веб-браузер. К счастью, использовать веб-браузер очень просто: вы запускаете
web browser on your computer and select a website by typing the name of the website, and|веб-браузер на вашем компьютере и выберите веб-сайт, набрав его название, и
the web page appears.|появится веб-страница.
### HTTP Overview
Обзор HTTP   
__|__
--|--
What really happens to allow that web page to appear on your web browser?|Что на самом деле происходит, чтобы эта веб-страница отображалась в вашем браузере?
Imagine that Bob opens his browser. His browser has been configured to automatically|Представьте, что Боб открывает свой браузер. Его браузер настроен на автоматическое
ask for web server Larry’s default web page, or home page. The general logic looks like|спросите веб-сервер, веб-страницу Ларри по умолчанию или домашнюю страницу. Общая логика выглядит так
Figure 1-5.|Рисунок 1-5.
Web Server - Larry Web Browser - Bob|Веб-сервер - Ларри Веб-браузер - Боб
Give me your web page|Дай мне свою веб-страницу
Here is the file home.htm|Вот файл home.htm
1|1
2|2
Figure 1-5 Basic Application Logic to Get a Web Page|Рисунок 1-5 Базовая логика приложения для получения веб-страницы
So, what really happened? Bob’s initial request actually asks Larry to send his home page|Итак, что же произошло на самом деле? Первоначальный запрос Боба на самом деле просит Ларри отправить свою домашнюю страницу
back to Bob. Larry’s web server software has been configured to know that the default web|обратно к Бобу. Программное обеспечение веб-сервера Ларри настроено так, чтобы знать, что веб-сервер по умолчанию
page is contained in a file called home.htm. Bob receives the file from Larry and displays the|страница содержится в файле с именем home.htm. Боб получает файл от Ларри и отображает
contents of the file in Bob’s web browser window.|содержимое файла в окне веб-браузера Боба.
### HTTP Protocol Mechanisms
Механизмы протокола HTTP   
__|__
--|--
Taking a closer look, this example shows how applications on each endpoint computer—specifically, the web browser application and web server application—use a TCP/IP application|При более внимательном рассмотрении этот пример показывает, как приложения на каждом конечном компьютере - в частности, приложение веб-браузера и приложение веб-сервера - используют приложение TCP / IP.
layer protocol. To make the request for a web page and return the contents of the web page,|протокол уровня. Чтобы сделать запрос на веб-страницу и вернуть содержимое веб-страницы,
the applications use the Hypertext Transfer Protocol (HTTP).|приложения используют протокол передачи гипертекста (HTTP).
HTTP did not exist until Tim Berners-Lee created the first web browser and web server in|HTTP не существовал до тех пор, пока Тим Бернерс-Ли не создал первый веб-браузер и веб-сервер в
the early 1990s. Berners-Lee gave HTTP functionality to ask for the contents of web pages,|начало 1990-х гг. Бернерс-Ли предоставил функцию HTTP для запроса содержимого веб-страниц,
specifically by giving the web browser the ability to request files from the server and giving the server a way to return the content of those files. The overall logic matches what was|в частности, предоставляя веб-браузеру возможность запрашивать файлы с сервера и давая серверу возможность возвращать содержимое этих файлов. Общая логика соответствует тому, что было
shown in Figure 1-5; Figure 1-6 shows the same idea, but with details specific to HTTP.|показано на рисунке 1-5; На рис. 1-6 показана та же идея, но с подробностями, относящимися к HTTP.
NOTE The full version of most web addresses—also called Uniform Resource Locators|ПРИМЕЧАНИЕ. Полная версия большинства веб-адресов, также называемых унифицированными указателями ресурсов.
(URL) or Universal Resource Identifiers (URI)—begins with the letters http, which means|(URL) или универсальные идентификаторы ресурсов (URI) - начинается с букв http, что означает
that HTTP is used to transfer the web pages.|что HTTP используется для передачи веб-страниц.
Web|Интернет
Server|Сервер
Larry|Ларри
Web|Интернет
Browser|Браузер
Bob|Боб
1|1
HTTP Header|Заголовок HTTP
GET home.htm|ПОЛУЧИТЬ home.htm
2|2
HTTP Header|Заголовок HTTP
OK|ОК
Data|Данные
home.htm|home.htm
Data|Данные
More of file home.htm 3|Подробнее о файле home.htm 3
Figure 1-6 HTTP GET Request, HTTP Reply, and One Data-Only Message|Рисунок 1-6 HTTP-запрос GET, HTTP-ответ и одно сообщение только с данными
To get the web page from Larry, at Step 1, Bob sends a message with an HTTP header.|Чтобы получить веб-страницу от Ларри, на шаге 1 Боб отправляет сообщение с заголовком HTTP.
Generally, protocols use headers as a place to put information used by that protocol. This|Обычно протоколы используют заголовки как место для размещения информации, используемой этим протоколом. Этот
HTTP header includes the request to “get” a file. The request typically contains the name of|Заголовок HTTP включает запрос на «получение» файла. Запрос обычно содержит имя
the file (home.htm, in this case), or if no filename is mentioned, the web server assumes that|файл (в данном случае home.htm), или, если имя файла не указано, веб-сервер предполагает, что
Bob wants the default web page.|Бобу нужна веб-страница по умолчанию.
Step 2 in Figure 1-6 shows the response from web server Larry. The message begins with an|Шаг 2 на рис. 1-6 показывает ответ веб-сервера Ларри. Сообщение начинается с
HTTP header, with a return code (200), which means something as simple as “OK” returned|Заголовок HTTP с кодом возврата (200), что означает что-то простое, например, возвращенное «ОК».
in the header. HTTP also defines other return codes so that the server can tell the browser|в шапке. HTTP также определяет другие коды возврата, чтобы сервер мог сообщить браузеру
whether the request worked. (Here is another example: If you ever looked for a web page|работал ли запрос. (Вот еще один пример: если вы когда-нибудь искали веб-страницу
that was not found, and then received an HTTP 404 “not found” error, you received an HTTP|который не был найден, а затем получил ошибку HTTP 404 «не найден», вы получили HTTP
return code of 404.) The second message also includes the first part of the requested file.|код возврата 404.) Второе сообщение также включает первую часть запрошенного файла.
Step 3 in Figure 1-6 shows another message from web server Larry to web browser Bob, but|Шаг 3 на рисунке 1-6 показывает другое сообщение от веб-сервера Ларри веб-браузеру Бобу, но
this time without an HTTP header. HTTP transfers the data by sending multiple messages,|на этот раз без заголовка HTTP. HTTP передает данные, отправляя несколько сообщений,
each with a part of the file. Rather than wasting space by sending repeated HTTP headers|каждый с частью файла. Вместо того, чтобы тратить место на отправку повторяющихся заголовков HTTP
that list the same information, these additional messages simply omit the header.|которые содержат ту же информацию, эти дополнительные сообщения просто опускают заголовок.
## TCP/IP Transport Layer
Транспортный уровень TCP / IP   
__|__
--|--
Although many TCP/IP application layer protocols exist, the TCP/IP transport layer includes|Хотя существует множество протоколов прикладного уровня TCP / IP, транспортный уровень TCP / IP включает
a smaller number of protocols. The two most commonly used transport layer protocols are|меньшее количество протоколов. Два наиболее часто используемых протокола транспортного уровня:
the Transmission Control Protocol (TCP) and the User Datagram Protocol (UDP).|протокол управления передачей (TCP) и протокол дейтаграмм пользователя (UDP).
Transport layer protocols provide services to the application layer protocols that reside one|Протоколы транспортного уровня предоставляют услуги протоколам прикладного уровня, которые находятся в одном
layer higher in the TCP/IP model. How does a transport layer protocol provide a service to a|уровень выше в модели TCP / IP. Как протокол транспортного уровня предоставляет услуги
higher-layer protocol? This section introduces that general concept by focusing on a single|протокол верхнего уровня? В этом разделе представлена ​​общая концепция, сосредоточившись на одном
service provided by TCP: error recovery. The CCNA 200-301 Official Cert Guide, Volume|сервис, предоставляемый TCP: исправление ошибок. Официальное руководство по сертификации CCNA 200-301, том
2, includes a chapter, “Introduction to TCP/IP Transport and Applications,” which examines|2, включает главу «Введение в транспорт и приложения TCP / IP», в которой рассматривается
the transport layer.|транспортный уровень.
Technet24|Технет24
### TCP Error Recovery Basics
Основы восстановления после ошибок TCP   
__|__
--|--
To appreciate what the transport layer protocols do, you must think about the layer above|Чтобы понять, что делают протоколы транспортного уровня, вы должны подумать об уровне выше.
the transport layer, the application layer. Why? Well, each layer provides a service to the|транспортный уровень, прикладной уровень. Зачем? Что ж, каждый уровень предоставляет услугу
layer above it, like the error-recovery service provided to application layer protocols by TCP.|уровень выше, как служба исправления ошибок, предоставляемая протоколам прикладного уровня TCP.
For example, in Figure 1-5, Bob and Larry used HTTP to transfer the home page from web|Например, на рис. 1-5 Боб и Ларри использовали HTTP для передачи домашней страницы из Интернета.
server Larry to Bob’s web browser. But what would have happened if Bob’s HTTP GET|сервер Ларри в веб-браузер Боба. Но что бы произошло, если бы HTTP GET Боба
request had been lost in transit through the TCP/IP network? Or, what would have happened|запрос был потерян при передаче через сеть TCP / IP? Или что бы случилось
if Larry’s response, which included the contents of the home page, had been lost? Well, as|если был утерян ответ Ларри, который включал содержание домашней страницы? Хорош как
you might expect, in either case, the page would not have shown up in Bob’s browser.|вы можете ожидать, что в любом случае страница не отобразится в браузере Боба.
TCP/IP needs a mechanism to guarantee delivery of data across a network. Because many|TCP / IP нуждается в механизме, гарантирующем доставку данных по сети. Потому что многие
application layer protocols probably want a way to guarantee delivery of data across a network, the creators of TCP included an error-recovery feature. To recover from errors, TCP|протоколам прикладного уровня, вероятно, нужен способ гарантировать доставку данных по сети, создатели TCP включили функцию восстановления после ошибок. Для восстановления после ошибок TCP
uses the concept of acknowledgments. Figure 1-7 outlines the basic idea behind how TCP|использует концепцию благодарностей. На рисунке 1-7 представлена ​​основная идея того, как TCP
notices lost data and asks the sender to try again.|замечает потерянные данные и просит отправителя повторить попытку.
Web|Интернет
Server|Сервер
Larry|Ларри
Web|Интернет
Browser|Браузер
Bob|Боб
SEQ = 1 1|SEQ = 1 1
TCP|TCP
OK|ОК
HTTP|HTTP
Web Page|Страница интернета
Data|Данные
SEQ = 2 2|SEQ = 2 2
TCP|TCP
More Web Page|Больше веб-страниц
Data Lost!|Данные потеряны!
SEQ = 3|SEQ = 3
TCP|TCP
Rest of Web Page|Остальная часть веб-страницы
Data|Данные
3|3
Send 2 Next 4|Отправить 2 Следующие 4
TCP|TCP
Figure 1-7 TCP Error-Recovery Services as Provided to HTTP|Рисунок 1-7. Службы восстановления после ошибок TCP, предоставляемые HTTP.
Figure 1-7 shows web server Larry sending a web page to web browser Bob, using three separate messages. Note that this figure shows the same HTTP headers as Figure 1-6, but it also|На рис. 1-7 показан веб-сервер Ларри, отправляющий веб-страницу веб-браузеру Бобу с использованием трех отдельных сообщений. Обратите внимание, что на этом рисунке показаны те же заголовки HTTP, что и на рисунке 1-6, но также
shows a TCP header. The TCP header shows a sequence number (SEQ) with each message. In|показывает заголовок TCP. Заголовок TCP показывает порядковый номер (SEQ) каждого сообщения. В
this example, the network has a problem, and the network fails to deliver the TCP message|В этом примере в сети возникла проблема, и сеть не может доставить сообщение TCP.
(called a segment) with sequence number 2. When Bob receives messages with sequence|(называется сегментом) с порядковым номером 2. Когда Боб получает сообщения с последовательностью
numbers 1 and 3, but does not receive a message with sequence number 2, Bob realizes that|номера 1 и 3, но не получает сообщения с порядковым номером 2, Боб понимает, что
message 2 was lost. That realization by Bob’s TCP logic causes Bob to send a TCP segment|сообщение 2 было потеряно. Эта реализация логики TCP Боба заставляет Боба отправить сегмент TCP
back to Larry, asking Larry to send message 2 again.|обратно к Ларри, прося Ларри отправить сообщение 2 еще раз.
### Same-Layer and Adjacent-Layer Interactions
Взаимодействия на одном и том же и прилегающем уровнях   
__|__
--|--
Figure 1-7 also demonstrates a function called adjacent-layer interaction, which refers to|На рисунке 1-7 также показана функция, называемая взаимодействием на соседнем уровне, которая относится к
the concepts of how adjacent layers in a networking model, on the same computer, work|концепции того, как работают смежные уровни в сетевой модели на одном компьютере
together. In this example, the higher-layer protocol (HTTP) wants error recovery, so it uses|все вместе. В этом примере протокол верхнего уровня (HTTP) требует восстановления после ошибок, поэтому он использует
the next lower-layer protocol (TCP) to perform the service of error recovery; the lower layer|следующий протокол нижнего уровня (TCP) для выполнения службы исправления ошибок; нижний слой
provides a service to the layer above it.|предоставляет услугу вышележащему слою.
Figure 1-7 also shows an example of a similar function called same-layer interaction.|На рис. 1-7 также показан пример аналогичной функции, называемой взаимодействием на одном уровне.
When a particular layer on one computer wants to communicate with the same layer on|Когда определенный уровень на одном компьютере хочет взаимодействовать с тем же уровнем на
another computer, the two computers use headers to hold the information that they want|другой компьютер, два компьютера используют заголовки для хранения нужной информации
to communicate. For example, in Figure 1-7, Larry set the sequence numbers to 1, 2, and 3|общаться. Например, на рисунке 1-7 Ларри установил порядковые номера на 1, 2 и 3.
so that Bob could notice when some of the data did not arrive. Larry’s TCP process created|чтобы Боб мог заметить, когда некоторые данные не поступают. TCP-процесс Ларри создан
that TCP header with the sequence number; Bob’s TCP process received and reacted to the|заголовок TCP с порядковым номером; Процесс TCP Боба получил и отреагировал на
TCP segments.|Сегменты TCP.
Table 1-3 summarizes the key points about how adjacent layers work together on a single|В таблице 1-3 приведены основные моменты совместной работы смежных слоев в одном
computer and how one layer on one computer works with the same networking layer on|компьютер и как один уровень на одном компьютере работает с тем же сетевым уровнем на
another computer.|другой компьютер.
Table 1-3 Summary: Same-Layer and Adjacent-Layer Interactions|Таблица 1-3 Сводка: взаимодействия на одном и том же уровне и на смежном уровне
Concept Description|Описание концепции
Same-layer interaction|Взаимодействие на одном уровне
on different computers|на разных компьютерах
The two computers use a protocol to communicate with the same|Два компьютера используют протокол для связи с одним и тем же
layer on another computer. The protocol defines a header that|слой на другом компьютере. Протокол определяет заголовок, который
communicates what each computer wants to do.|сообщает, что каждый компьютер хочет делать.
Adjacent-layer|Соседний слой
interaction on the same|взаимодействие на том же
computer|компьютер
On a single computer, one lower layer provides a service to the layer|На одном компьютере один нижний уровень предоставляет услугу уровню
just above. The software or hardware that implements the higher|чуть выше. Программное или аппаратное обеспечение, реализующее более высокую
layer requests that the next lower layer perform the needed function.|уровень требует, чтобы следующий нижний уровень выполнил необходимую функцию.
## TCP/IP Network Layer
Сетевой уровень TCP / IP   
__|__
--|--
The application layer includes many protocols. The transport layer includes fewer protocols,|Уровень приложений включает в себя множество протоколов. Транспортный уровень включает меньше протоколов,
most notably, TCP and UDP. The TCP/IP network layer includes a small number of protocols,|в первую очередь TCP и UDP. Сетевой уровень TCP / IP включает небольшое количество протоколов,
but only one major protocol: the Internet Protocol (IP). In fact, the name TCP/IP is simply|но только один основной протокол: Интернет-протокол (IP). На самом деле имя TCP / IP просто
the names of the two most common protocols (TCP and IP) separated by a /.|имена двух наиболее распространенных протоколов (TCP и IP), разделенные знаком /.
IP provides several features, most importantly, addressing and routing. This section begins|IP предоставляет несколько функций, в первую очередь адресацию и маршрутизацию. Этот раздел начинается
by comparing IP’s addressing and routing with another commonly known system that uses|сравнивая IP-адресацию и маршрутизацию с другой широко известной системой, которая использует
addressing and routing: the postal service. Following that, this section introduces IP addressing|адресация и маршрутизация: почтовая служба. После этого в этом разделе представлена ​​IP-адресация.
and routing. (More details follow in Chapter 3, “Fundamentals of WANs and IP Routing.”)|и маршрутизация. (Более подробная информация содержится в главе 3 «Основы WAN и IP-маршрутизации».)
### Internet Protocol and the Postal Service
Интернет-протокол и почтовая служба   
__|__
--|--
Imagine that you just wrote two letters: one to a friend on the other side of the country|Представьте, что вы только что написали два письма: одно другу на другой конец страны.
and one to a friend on the other side of town. You addressed the envelopes and put on the|и один другу на другом конце города. Вы адресовали конверты и положили
stamps, so both are ready to give to the postal service. Is there much difference in how you|марки, так что оба готовы отдать на почту. Есть большая разница в том, как ты
treat each letter? Not really. Typically, you would just put them in the same mailbox and|относиться к каждой букве? На самом деле, нет. Обычно вы просто кладете их в тот же почтовый ящик и
expect the postal service to deliver both letters.|ожидайте, что почтовая служба доставит оба письма.
The postal service, however, must think about each letter separately, and then make a decision of where to send each letter so that it is delivered. For the letter sent across town, the|Почтовая служба, однако, должна думать о каждом письме отдельно, а затем принимать решение о том, куда отправить каждое письмо, чтобы оно было доставлено. Для письма, отправленного через город,
people in the local post office probably just need to put the letter on another truck.|людям в местном почтовом отделении, вероятно, просто нужно перебросить письмо в другой грузовик.
For the letter that needs to go across the country, the postal service sends the letter to another post office, then another, and so on, until the letter gets delivered across the country. At|Для письма, которое необходимо пересечь страну, почтовая служба отправляет письмо в другое почтовое отделение, затем в другое и так далее, пока письмо не будет доставлено по всей стране. В
each post office, the postal service must process the letter and choose where to send it next.|В каждом почтовом отделении почтовая служба должна обработать письмо и выбрать, куда его отправить дальше.
To make it all work, the postal service has regular routes for small trucks, large trucks,|Чтобы все это работало, у почтовой службы есть регулярные маршруты для небольших грузовиков, больших грузовиков,
planes, boats, and so on, to move letters between postal service sites. The service must be|самолеты, лодки и т. д. для перемещения писем между сайтами почтовых служб. Услуга должна быть
able to receive and forward the letters, and it must make good decisions about where to send|может получать и пересылать письма, и он должен принимать правильные решения о том, куда отправлять
each letter next, as shown in Figure 1-8.|каждая буква следующая, как показано на Рисунке 1-8.
Technet24|Технет24
Local 1|Местный 1
Postal Service|Почтовая служба
California|Калифорния
Figure 1-8 Postal Service Forwarding (Routing) Letters|Рисунок 1-8 Письма пересылки (маршрутизации) почтовой службой
Still thinking about the postal service, consider the difference between the person sending|Все еще думая о почтовой службе, подумайте, чем отличается человек, отправляющий
the letter and the work that the postal service does. The person sending the letters expects|письмо и работа, которую делает почтовая служба. Отправитель письма ожидает
that the postal service will deliver the letter most of the time. However, the person sending|что почтовая служба доставляет письмо большую часть времени. Однако человек, отправляющий
the letter does not need to know the details of exactly what path the letters take. In contrast, the postal service does not create the letter, but it accepts the letter from the customer.|письму не нужно знать подробности того, какой именно путь идут буквы. Почтовая служба, напротив, не создает письмо, но принимает письмо от клиента.
Then, the postal service must know the details about addresses and postal codes that group|Затем почтовая служба должна знать подробности об адресах и почтовых индексах, которые группируют
addresses into larger groups, and it must have the ability to deliver the letters.|адреса в большие группы, и он должен иметь возможность доставлять письма.
The TCP/IP application and transport layers act like the person sending letters through the|Приложение TCP / IP и транспортные уровни действуют как человек, отправляющий письма через
postal service. These upper layers work the same way regardless of whether the endpoint|Почтовая служба. Эти верхние уровни работают одинаково независимо от того,
host computers are on the same LAN or are separated by the entire Internet. To send a message, these upper layers ask the layer below them, the network layer, to deliver the message.|хост-компьютеры находятся в одной локальной сети или разделены всем Интернетом. Чтобы отправить сообщение, эти верхние уровни запрашивают уровень ниже, сетевой уровень, чтобы доставить сообщение.
The lower layers of the TCP/IP model act more like the postal service to deliver those messages to the correct destinations. To do so, these lower layers must understand the underlying physical network because they must choose how to best deliver the data from one host|Нижние уровни модели TCP / IP действуют больше как почтовая служба, доставляя эти сообщения по правильным адресатам. Для этого эти нижние уровни должны понимать базовую физическую сеть, потому что они должны выбирать, как лучше всего доставлять данные с одного хоста.
to another.|к другому.
So, what does this all matter to networking? Well, the network layer of the TCP/IP networking model, primarily defined by the Internet Protocol (IP), works much like the postal service. IP defines that each host computer should have a different IP address, just as the postal|Итак, какое все это имеет значение для сетей? Что ж, сетевой уровень сетевой модели TCP / IP, в первую очередь определяемый Интернет-протоколом (IP), работает во многом как почтовая служба. IP определяет, что каждый хост-компьютер должен иметь другой IP-адрес, как и почтовый
service defines addressing that allows unique addresses for each house, apartment, and business. Similarly, IP defines the process of routing so that devices called routers can work like|Сервис определяет адресацию, которая позволяет использовать уникальные адреса для каждого дома, квартиры или предприятия. Точно так же IP определяет процесс маршрутизации, чтобы устройства, называемые маршрутизаторами, могли работать как
the post office, forwarding packets of data so that they are delivered to the correct destinations. Just as the postal service created the necessary infrastructure to deliver letters—post|почтовое отделение, пересылающее пакеты данных, чтобы они были доставлены в нужное место назначения. Так же, как почтовая служба создала необходимую инфраструктуру для доставки писем, почта
offices, sorting machines, trucks, planes, and personnel—the network layer defines the|офисы, сортировочные машины, грузовики, самолеты и персонал - сетевой уровень определяет
details of how a network infrastructure should be created so that the network can deliver|подробности о том, как должна быть создана сетевая инфраструктура, чтобы сеть могла предоставлять
data to all computers in the network.|данные на все компьютеры в сети.
### Internet Protocol Addressing Basics
Основы адресации интернет-протокола   
__|__
--|--
IP defines addresses for several important reasons. First, each device that uses TCP/IP—each|IP определяет адреса по нескольким важным причинам. Во-первых, каждое устройство, использующее TCP / IP - каждое
TCP/IP host—needs a unique address so that it can be identified in the network. IP also|Хост TCP / IP - требуется уникальный адрес, чтобы его можно было идентифицировать в сети. IP также
defines how to group addresses together, just like the postal system groups addresses based|определяет, как группировать адреса вместе, точно так же, как почтовая система группирует адреса на основе
on postal codes (like ZIP codes in the United States).|по почтовым индексам (например, почтовые индексы в США).
To understand the basics, examine Figure 1-9, which shows the familiar web server Larry and|Чтобы понять основы, изучите рисунок 1-9, на котором показан знакомый веб-сервер Ларри и
web browser Bob; but now, instead of ignoring the network between these two computers,|веб-браузер Боб; но теперь, вместо того, чтобы игнорировать сеть между этими двумя компьютерами,
part of the network infrastructure is included.|часть сетевой инфраструктуры включена.
Addresses: 1.__.__.__|Адреса: 1 .__.__.__
Addresses: 3.__.__.__|Адреса: 3 .__.__.__
Addresses: 2.__.__.__|Адреса: 2 .__.__.__
Larry|Ларри
1.1.1.1|1.1.1.1
3.3.3.3|3.3.3.3
Bob|Боб
2.2.2.2|2.2.2.2
R1|R1
R3|R3
R2|R2
Archie|Арчи
Figure 1-9 Simple TCP/IP Network: Three Routers with IP Addresses Grouped|Рисунок 1-9 Простая сеть TCP / IP: три маршрутизатора с сгруппированными IP-адресами
First, note that Figure 1-9 shows some sample IP addresses. Each IP address has four numbers, separated by periods. In this case, Larry uses IP address 1.1.1.1, and Bob uses 2.2.2.2.|Во-первых, обратите внимание, что на рис. 1-9 показаны некоторые примеры IP-адресов. Каждый IP-адрес имеет четыре числа, разделенных точками. В этом случае Ларри использует IP-адрес 1.1.1.1, а Боб - 2.2.2.2.
This style of number is called a dotted-decimal notation (DDN).|Этот стиль чисел называется десятичной системой с разделительными точками (DDN).
Figure 1-9 also shows three groups of addresses. In this example, all IP addresses that|На рисунке 1-9 также показаны три группы адресов. В этом примере все IP-адреса,
begin with 1 must be on the upper left, as shown in shorthand in the figure as 1.__.__.__.|начать с 1 должно быть в верхнем левом углу, как показано на рисунке как 1 .__.__.__.
All addresses that begin with 2 must be on the right, as shown in shorthand as 2.__.__.__.|Все адреса, начинающиеся с 2, должны быть справа, как показано в сокращении как 2 .__.__.__.
Finally, all IP addresses that begin with 3 must be at the bottom of the figure.|Наконец, все IP-адреса, начинающиеся с 3, должны быть внизу рисунка.
In addition, Figure 1-9 introduces icons that represent IP routers. Routers are networking|Кроме того, на рис. 1-9 представлены значки, представляющие IP-маршрутизаторы. Маршрутизаторы сетевые
devices that connect the parts of the TCP/IP network together for the purpose of routing|устройства, которые соединяют части сети TCP / IP вместе с целью маршрутизации
(forwarding) IP packets to the correct destination. Routers do the equivalent of the work|(пересылка) IP-пакетов в правильное место назначения. Маршрутизаторы выполняют эквивалентную работу
done by each post office site: They receive IP packets on various physical interfaces, make|выполняется каждым сайтом почтового отделения: они получают IP-пакеты на различных физических интерфейсах, делают
decisions based on the IP address included with the packet, and then physically forward the|решения на основе IP-адреса, включенного в пакет, а затем физически перенаправить
packet out some other network interface.|пакет из другого сетевого интерфейса.
### IP Routing Basics
Основы IP-маршрутизации   
__|__
--|--
The TCP/IP network layer, using the IP protocol, provides a service of forwarding IP packets|Сетевой уровень TCP / IP, использующий протокол IP, предоставляет услугу пересылки IP-пакетов.
from one device to another. Any device with an IP address can connect to the TCP/IP network and send packets. This section shows a basic IP routing example for perspective.|с одного устройства на другое. Любое устройство с IP-адресом может подключаться к сети TCP / IP и отправлять пакеты. В этом разделе для перспективы показан базовый пример IP-маршрутизации.
NOTE The term IP host refers to any device, regardless of size or power, that has an IP|ПРИМЕЧАНИЕ Термин IP-хост относится к любому устройству, независимо от размера или мощности, которое имеет IP-адрес.
address and connects to any TCP/IP network.|адрес и подключается к любой сети TCP / IP.
Figure 1-10 repeats the familiar case in which web server Larry wants to send part of a web|На рис. 1-10 повторяется знакомый случай, когда веб-сервер Ларри хочет отправить часть веб-
page to Bob, but now with details related to IP. On the lower left, note that server Larry has|страницу Бобу, но теперь с подробностями, относящимися к IP. В левом нижнем углу обратите внимание на то, что на сервере Ларри
the familiar application data, HTTP header, and TCP header ready to send. In addition, the|знакомые данные приложения, HTTP-заголовок и TCP-заголовок, готовые к отправке. В дополнение
message now contains an IP header. The IP header includes a source IP address of Larry’s IP|сообщение теперь содержит заголовок IP. Заголовок IP включает исходный IP-адрес IP Ларри.
address (1.1.1.1) and a destination IP address of Bob’s IP address (2.2.2.2).|адрес (1.1.1.1) и IP-адрес назначения IP-адреса Боба (2.2.2.2).
Technet24|Технет24
1|1
Addresses: 2._____|Адреса: 2._____
Larry|Ларри
1.1.1.1|1.1.1.1
1 2 3|1 2 3
To 2._____|К 2 ._____
Send to R2|Отправить на R2
To 2._____|К 2 ._____
Send Locally|Отправить локально
Always to|Всегда
R1|R1
Bob|Боб
2.2.2.2|2.2.2.2
IP TCP HTTP|IP TCP HTTP
Source 1.1.1.1|Источник 1.1.1.1
Destination 2.2.2.2|Пункт назначения 2.2.2.2
R1|R1
R3|R3
R2|R2
Figure 1-10 Basic Routing Example|Рисунок 1-10 Пример базовой маршрутизации
Step 1, on the left of Figure 1-10, begins with Larry being ready to send an IP packet.|Шаг 1 слева на рис. 1-10 начинается с того, что Ларри готов отправить IP-пакет.
Larry’s IP process chooses to send the packet to some router—a nearby router on the same|IP-процесс Ларри решает отправить пакет на какой-то маршрутизатор - соседний маршрутизатор на том же
LAN—with the expectation that the router will know how to forward the packet. (This logic|LAN - с ожиданием, что маршрутизатор знает, как пересылать пакет. (Эта логика
is much like you or me sending all our letters by putting them in a nearby mailbox.) Larry|очень похоже на то, как вы или я отправляем все наши письма, кладя их в ближайший почтовый ящик.) Ларри
doesn’t need to know anything more about the topology or the other routers.|не нужно больше ничего знать о топологии или других маршрутизаторах.
At Step 2, Router R1 receives the IP packet, and R1’s IP process makes a decision. R1 looks at|На шаге 2 маршрутизатор R1 получает IP-пакет, а IP-процесс R1 принимает решение. R1 смотрит на
the destination address (2.2.2.2), compares that address to its known IP routes, and chooses|адрес назначения (2.2.2.2), сравнивает этот адрес с известными IP-маршрутами и выбирает
to forward the packet to Router R2. This process of forwarding the IP packet is called IP|для пересылки пакета на маршрутизатор R2. Этот процесс пересылки IP-пакета называется IP.
routing (or simply routing).|маршрутизация (или просто маршрутизация).
At Step 3, Router R2 repeats the same kind of logic used by Router R1. R2’s IP process will|На шаге 3 маршрутизатор R2 повторяет ту же логику, что и маршрутизатор R1. Процесс IP R2 будет
compare the packet’s destination IP address (2.2.2.2) to R2’s known IP routes and make a|сравните IP-адрес назначения пакета (2.2.2.2) с известными IP-маршрутами R2 и создайте
choice to forward the packet to the right, on to Bob.|выбор пересылать пакет направо, Бобу.
You will learn IP in more depth than any other protocol while preparing for CCNA. More|Вы изучите IP глубже, чем любой другой протокол, при подготовке к CCNA. Больше
than half the chapters in this book discuss some feature that relates to addressing, IP routing,|более чем в половине глав этой книги обсуждаются некоторые особенности, связанные с адресацией, IP-маршрутизацией,
and how routers perform routing.|и как маршрутизаторы выполняют маршрутизацию.
## TCP/IP Data-Link and Physical Layers
Канал передачи данных TCP / IP и физические уровни   
__|__
--|--
The TCP/IP model’s data-link and physical layers define the protocols and hardware required|Канальный и физический уровни модели TCP / IP определяют протоколы и необходимое оборудование.
to deliver data across some physical network. The two work together quite closely; in fact,|для доставки данных по какой-либо физической сети. Эти двое работают вместе довольно тесно; по факту,
some standards define both the data-link and physical layer functions. The physical layer|некоторые стандарты определяют функции как канала передачи данных, так и физического уровня. Физический уровень
defines the cabling and energy (for example, electrical signals) that flow over the cables.|определяет кабели и энергию (например, электрические сигналы), протекающую по кабелям.
Some rules and conventions exist when sending data over the cable; however, those rules|При передаче данных по кабелю существуют некоторые правила и соглашения; однако эти правила
exist in the data-link layer of the TCP/IP model.|существуют на канальном уровне модели TCP / IP.
Focusing on the data-link layer for a moment, just like every layer in any networking model,|Сосредоточимся на уровне канала передачи данных, как и на каждом уровне в любой сетевой модели,
the TCP/IP data-link layer provides services to the layer above it in the model (the network|уровень канала передачи данных TCP / IP предоставляет услуги вышележащему уровню модели (сеть
layer). When a host’s or router’s IP process chooses to send an IP packet to another router|слой). Когда IP-процесс хоста или маршрутизатора решает отправить IP-пакет другому маршрутизатору
or host, that host or router then uses link-layer details to send that packet to the next host/|или хост, этот хост или маршрутизатор затем использует детали канального уровня для отправки этого пакета на следующий хост /
router.|роутер.
Because each layer provides a service to the layer above it, take a moment to think about the|Поскольку каждый уровень предоставляет услугу вышележащему слою, подумайте о том,
IP logic related to Figure 1-10. In that example, host Larry’s IP logic chooses to send the IP|Логика IP, показанная на Рисунке 1-10. В этом примере логика IP-адреса хоста Ларри решает отправить IP-адрес
packet to a nearby router (R1). However, while Figure 1-10 shows a simple line between Larry|пакет к ближайшему маршрутизатору (R1). Однако, хотя на рис. 1-10 показана простая линия между Ларри
and router R1, that drawing means that some Ethernet LAN sits between the two. Figure|и маршрутизатор R1, этот рисунок означает, что между ними находится некая локальная сеть Ethernet. Рисунок
1-11 shows four steps of what occurs at the link layer to allow Larry to send the IP packet|1-11 показаны четыре шага того, что происходит на канальном уровне, чтобы Ларри мог отправить IP-пакет.
to R1.|к R1.
Larry|Ларри
1.1.1.1|1.1.1.1
Ethernet IP Packet Eth.|Ethernet IP Packet Eth.
IP Packet|IP-пакет
1 Encapsulate|1 инкапсулировать
2 Transmit 3|2 Передача 3
IP Packet|IP-пакет
4 De-encapsulate|4 Деинкапсулировать
Receive|Получить
R1|R1
Header Trailer|Заголовок трейлера
Ethernet IP Packet Eth.|Ethernet IP Packet Eth.
Header Trailer|Заголовок трейлера
Figure 1-11 Larry Using Ethernet to Forward an IP Packet to Router R1|Рисунок 1-11. Ларри использует Ethernet для пересылки IP-пакета на маршрутизатор R1.
NOTE Figure 1-11 depicts the Ethernet as a series of lines. Networking diagrams often use|ПРИМЕЧАНИЕ. На рисунке 1-11 Ethernet изображен в виде серии линий. В сетевых схемах часто используются
this convention when drawing Ethernet LANs, in cases where the actual LAN cabling and|это соглашение при рисовании локальных сетей Ethernet, в тех случаях, когда фактическая кабельная разводка и
LAN devices are not important to some discussion, as is the case here. The LAN would have|Устройства LAN не важны для некоторых обсуждений, как здесь. LAN будет иметь
cables and devices, like LAN switches, which are not shown in this figure.|кабели и устройства, такие как коммутаторы LAN, которые не показаны на этом рисунке.
Figure 1-11 shows four steps. The first two occur on Larry, and the last two occur on Router|На рисунке 1-11 показаны четыре шага. Первые два происходят на Ларри, а последние два - на Маршрутизаторе.
R1, as follows:|R1 следующим образом:
Step 1. Larry encapsulates the IP packet between an Ethernet header and Ethernet|Шаг 1. Ларри инкапсулирует IP-пакет между заголовком Ethernet и Ethernet.
trailer, creating an Ethernet frame.|трейлер, создавая фрейм Ethernet.
Step 2. Larry physically transmits the bits of this Ethernet frame, using electricity|Шаг 2. Ларри физически передает биты этого кадра Ethernet, используя электричество.
flowing over the Ethernet cabling.|протекающий по кабелю Ethernet.
Step 3. Router R1 physically receives the electrical signal over a cable and re-creates the|Шаг 3. Маршрутизатор R1 физически принимает электрический сигнал по кабелю и воссоздает
same bits by interpreting the meaning of the electrical signals.|те же биты, интерпретируя значение электрических сигналов.
Step 4. Router R1 de-encapsulates the IP packet from the Ethernet frame by removing|Шаг 4. Маршрутизатор R1 деинкапсулирует IP-пакет из кадра Ethernet, удаляя
and discarding the Ethernet header and trailer.|и отбрасывая заголовок и трейлер Ethernet.
By the end of this process, Larry and R1 have worked together to deliver the packet from|К концу этого процесса Ларри и R1 работали вместе, чтобы доставить пакет из
Larry to Router R1.|Ларри к маршрутизатору R1.
NOTE Protocols define both headers and trailers for the same general reason, but headers|ПРИМЕЧАНИЕ Протоколы определяют как заголовки, так и концы по одной и той же общей причине, но заголовки
exist at the beginning of the message and trailers exist at the end.|существуют в начале сообщения, а трейлеры - в конце.
The data-link and physical layers include a large number of protocols and standards. For|Канальный и физический уровни включают большое количество протоколов и стандартов. За
example, the link layer includes all the variations of Ethernet protocols and wireless LAN|Например, канальный уровень включает в себя все варианты протоколов Ethernet и беспроводной локальной сети.
protocols discussed throughout this book.|протоколы, обсуждаемые в этой книге.
Technet24|Технет24
In short, the TCP/IP physical and data-link layers include two distinct functions, respectively: functions related to the physical transmission of the data, plus the protocols and rules|Короче говоря, физический уровень TCP / IP и уровень канала передачи данных включают в себя две различные функции, соответственно: функции, связанные с физической передачей данных, а также протоколы и правила.
that control the use of the physical media.|которые контролируют использование физических носителей.
## Data Encapsulation Terminology
Терминология инкапсуляции данных   
__|__
--|--
As you can see from the explanations of how HTTP, TCP, IP, and Ethernet do their jobs,|Как видно из объяснений того, как HTTP, TCP, IP и Ethernet выполняют свою работу,
when sending data, each layer adds its own header (and for data-link protocols, also a trailer)|при отправке данных каждый уровень добавляет свой собственный заголовок (а для протоколов передачи данных также трейлер)
to the data supplied by the higher layer. The term encapsulation refers to the process of|к данным, предоставленным более высоким уровнем. Термин инкапсуляция относится к процессу
putting headers (and sometimes trailers) around some data.|размещение заголовков (а иногда и трейлеров) вокруг некоторых данных.
Many of the examples in this chapter show the encapsulation process. For example, web|Многие примеры в этой главе показывают процесс инкапсуляции. Например, веб
server Larry encapsulated the contents of the home page inside an HTTP header in Figure|сервер Ларри инкапсулировал содержимое домашней страницы в заголовок HTTP на рис.
1-6. The TCP layer encapsulated the HTTP headers and data inside a TCP header in Figure|1-6. Уровень TCP инкапсулировал заголовки и данные HTTP внутри заголовка TCP, как показано на рисунке.
1-7. IP encapsulated the TCP headers and the data inside an IP header in Figure 1-10. Finally,|1-7. IP инкапсулировал заголовки TCP и данные внутри заголовка IP на рис. 1-10. В заключение,
the Ethernet link layer encapsulated the IP packets inside both a header and a trailer in|канальный уровень Ethernet инкапсулировал IP-пакеты как в заголовок, так и в трейлер в
Figure 1-11.|Рисунок 1-11.
The process by which a TCP/IP host sends data can be viewed as a five-step process. The|Процесс, посредством которого хост TCP / IP отправляет данные, можно рассматривать как пятиэтапный процесс. В
first four steps relate to the encapsulation performed by the four TCP/IP layers, and the last|первые четыре шага относятся к инкапсуляции, выполняемой четырьмя уровнями TCP / IP, а последний
step is the actual physical transmission of the data by the host. In fact, if you use the fivelayer TCP/IP model, one step corresponds to the role of each layer. The steps are summarized|step - это фактическая физическая передача данных хостом. Фактически, если вы используете пятиуровневую модель TCP / IP, один шаг соответствует роли каждого уровня. Шаги суммированы
in the following list:|в следующем списке:
Step 1. Create and encapsulate the application data with any required application|Шаг 1. Создайте и инкапсулируйте данные приложения с любым требуемым приложением.
layer headers. For example, the HTTP OK message can be returned in an HTTP|заголовки слоев. Например, сообщение HTTP OK может быть возвращено в HTTP
header, followed by part of the contents of a web page.|заголовок, за которым следует часть содержимого веб-страницы.
Step 2. Encapsulate the data supplied by the application layer inside a transport|Шаг 2. Инкапсулируйте данные, предоставленные прикладным уровнем, в транспортном средстве.
layer header. For end-user applications, a TCP or UDP header is typically used.|заголовок слоя. Для приложений конечного пользователя обычно используется заголовок TCP или UDP.
Step 3. Encapsulate the data supplied by the transport layer inside a network layer|Шаг 3. Инкапсулируйте данные, предоставленные транспортным уровнем, внутри сетевого уровня.
(IP) header. IP defines the IP addresses that uniquely identify each computer.|(IP) заголовок. IP определяет IP-адреса, которые однозначно идентифицируют каждый компьютер.
Step 4. Encapsulate the data supplied by the network layer inside a data-link layer|Шаг 4. Инкапсулируйте данные, предоставленные сетевым уровнем, внутри уровня канала передачи данных.
header and trailer. This layer uses both a header and a trailer.|заголовок и трейлер. Этот слой использует как заголовок, так и трейлер.
Step 5. Transmit the bits. The physical layer encodes a signal onto the medium to|Шаг 5. Передайте биты. Физический уровень кодирует сигнал в среде, чтобы
transmit the frame.|передать кадр.
The numbers in Figure 1-12 correspond to the five steps in this list, graphically showing the|Цифры на Рисунке 1-12 соответствуют пяти шагам в этом списке, графически показывая
same concepts. Note that because the application layer often does not need to add a header,|те же концепции. Обратите внимание: поскольку на уровне приложения часто не требуется добавлять заголовок,
the figure does not show a specific application layer header, but the application layer will|на рисунке не показан конкретный заголовок уровня приложения, но уровень приложения будет
also at times add a header as well.|также иногда добавляют заголовок.
Application|заявка
Transport|Транспорт
Network|Сеть
Data Link|Канал передачи данных
Physical|Физический
Data Link IP Data Link|Канал передачи данных IP Канал передачи данных
Data|Данные
TCP Data|Данные TCP
IP TCP Data|Данные IP TCP
Transmit Bits|Передача битов
1|1
2|2
3|3
4|4
5|5
1|1
2|2
3|3
4|4
5|5
4|4
TCP Data|Данные TCP
Figure 1-12 Five Steps of Data Encapsulation: TCP/IP|Рисунок 1-12 Пять шагов инкапсуляции данных: TCP / IP
## Names of TCP/IP Messages
Имена сообщений TCP / IP   
__|__
--|--
One reason this chapter takes the time to show the encapsulation steps in detail has to do|Одна из причин, по которой в этой главе тратится время на подробное описание этапов инкапсуляции, заключается в следующем:
with terminology. When talking and writing about networking, people use segment, packet,|с терминологией. Когда говорят и пишут о сети, люди используют сегмент, пакет,
and frame to refer to the messages shown in Figure 1-13 and the related list. Each term has a|и фрейм для ссылки на сообщения, показанные на Рисунке 1-13 и в соответствующем списке. Каждый термин имеет
specific meaning, referring to the headers (and possibly trailers) defined by a particular layer|конкретное значение, относящееся к заголовкам (и, возможно, трейлерам), определенным конкретным слоем
and the data encapsulated following that header. Each term, however, refers to a different|и данные, инкапсулированные после этого заголовка. Однако каждый термин относится к разным
layer: segment for the transport layer, packet for the network layer, and frame for the link|уровень: сегмент для транспортного уровня, пакет для сетевого уровня и кадр для ссылки
layer. Figure 1-13 shows each layer along with the associated term.|слой. На рис. 1-13 показан каждый уровень вместе с соответствующим термином.
TCP Data|Данные TCP
IP Data|IP данные
LH Data LT|LH Data LT
Segment|Сегмент
Packet|Пакет
Frame|Рамка
Figure 1-13 Perspectives on Encapsulation and “Data”*|Рисунок 1-13 Перспективы инкапсуляции и «данных» *
* The letters LH and LT stand for link header and link trailer, respectively, and refer to the data-link layer|* Буквы LH и LT обозначают заголовок ссылки и конец ссылки, соответственно, и относятся к уровню канала передачи данных.
header and trailer.|заголовок и трейлер.
Figure 1-13 also shows the encapsulated data as simply “data.” When focusing on the work|На рис. 1-13 также показаны инкапсулированные данные как просто «данные». Когда сосредотачиваемся на работе
done by a particular layer, the encapsulated data typically is unimportant. For example, an|выполняется конкретным уровнем, инкапсулированные данные обычно не важны. Например,
IP packet can indeed have a TCP header after the IP header, an HTTP header after the TCP|IP-пакет действительно может иметь заголовок TCP после заголовка IP, заголовок HTTP после TCP.
header, and data for a web page after the HTTP header. However, when discussing IP, you|заголовок и данные для веб-страницы после заголовка HTTP. Однако при обсуждении IP вы
probably just care about the IP header, so everything after the IP header is just called data.|вероятно, просто заботится о заголовке IP, поэтому все, что находится после заголовка IP, просто называется данными.
So, when drawing IP packets, everything after the IP header is typically shown simply as|Итак, при отрисовке IP-пакетов все, что находится после IP-заголовка, обычно отображается просто как
data.|данные.
## OSI Networking Model and Terminology
Сетевая модель и терминология OSI   
__|__
--|--
At one point in the history of the OSI model, many people thought that OSI would win the|В какой-то момент истории модели OSI многие люди думали, что OSI выиграет
battle of the networking models discussed earlier. If that had occurred, instead of running|битва сетевых моделей, обсуждавшаяся ранее. Если бы это произошло, вместо запуска
TCP/IP on every computer in the world, those computers would be running with OSI.|TCP / IP на каждом компьютере в мире, эти компьютеры будут работать с OSI.
Technet24|Технет24
However, OSI did not win that battle. In fact, OSI no longer exists as a networking model|Однако OSI не выиграла эту битву. Фактически, OSI больше не существует как сетевая модель.
that could be used instead of TCP/IP, although some of the original protocols referenced by|который можно использовать вместо TCP / IP, хотя некоторые из исходных протоколов, на которые ссылается
the OSI model still exist.|модель OSI все еще существует.
So, why is OSI even in this book? Terminology. During those years in which many people|Итак, почему OSI даже в этой книге? Терминология. В те годы, когда многие люди
thought the OSI model would become commonplace in the world of networking (mostly in|думал, что модель OSI станет обычным явлением в мире сетей (в основном в
the late 1980s and early 1990s), many vendors and protocol documents started using terminology from the OSI model. That terminology remains today. So, while you will never need|в конце 1980-х - начале 1990-х годов) многие поставщики и документы протокола начали использовать терминологию модели OSI. Эта терминология сохраняется и сегодня. Итак, пока вам никогда не понадобится
to work with a computer that uses OSI, to understand modern networking terminology, you|для работы с компьютером, который использует OSI, чтобы понять современную сетевую терминологию, вы
need to understand something about OSI.|нужно что-то понимать об OSI.
### Comparing OSI and TCP/IP Layer Names and Numbers
Сравнение имен и номеров уровней OSI и TCP / IP   
__|__
--|--
The OSI model has many similarities to the TCP/IP model from a basic conceptual perspective. It has layers, and each layer defines a set of typical networking functions. As with TCP/|Модель OSI имеет много общего с моделью TCP / IP с базовой концептуальной точки зрения. Он имеет уровни, и каждый уровень определяет набор типичных сетевых функций. Как и в случае с TCP /
IP, the OSI layers each refer to multiple protocols and standards that implement the functions|IP, каждый уровень OSI относится к нескольким протоколам и стандартам, реализующим функции
specified by each layer. In other cases, just as for TCP/IP, the OSI committees did not create|определяется каждым слоем. В других случаях, как и в случае TCP / IP, комитеты OSI не создавали
new protocols or standards, but instead referenced other protocols that were already defined.|новые протоколы или стандарты, но вместо этого ссылались на другие протоколы, которые уже были определены.
For example, the IEEE defines Ethernet standards, so the OSI committees did not waste time|Например, IEEE определяет стандарты Ethernet, поэтому комитеты OSI не теряют время зря.
specifying a new type of Ethernet; it simply referred to the IEEE Ethernet standards.|указание нового типа Ethernet; он просто ссылался на стандарты IEEE Ethernet.
Today, the OSI model can be used as a standard of comparison to other networking models.|Сегодня модель OSI может использоваться как стандарт для сравнения с другими сетевыми моделями.
Figure 1-14 compares the seven-layer OSI model with both the four-layer and five-layer|Рисунок 1-14 сравнивает семиуровневую модель OSI с четырехуровневой и пятиуровневой.
TCP/IP models.|Модели TCP / IP.
OSI TCP/IP|OSI TCP / IP
Application|заявка
Transport|Транспорт
Network|Сеть
Data Link|Канал передачи данных
Physical|Физический
5 - 7|5–7
4|4
3|3
2|2
1|1
Transport|Транспорт
Session|Сессия
Presentation|Презентация
Application|заявка
Network|Сеть
Data Link|Канал передачи данных
Physical|Физический
4|4
5|5
6|6
7|7
3|3
2|2
1|1
Figure 1-14 OSI Model Compared to the Two TCP/IP Models|Рисунок 1-14 Модель OSI в сравнении с двумя моделями TCP / IP
Note that the TCP/IP model in use today, on the right side of the figure, uses the exact same|Обратите внимание, что в используемой сегодня модели TCP / IP в правой части рисунка используется точно такая же
layer names as OSI at the lower layers. The functions generally match as well, so for the purpose of discussing networking, and reading networking documentation, think of the bottom|имена слоев как OSI на нижних уровнях. Функции в целом также совпадают, поэтому при обсуждении сети и чтении сетевой документации подумайте о нижнем
four layers as equivalent, in name, in number, and in meaning.|четыре уровня эквивалентны по названию, количеству и значению.
Even though the world uses TCP/IP today rather than OSI, we tend to use the numbering|Несмотря на то, что сегодня в мире используется TCP / IP, а не OSI, мы склонны использовать нумерацию
from the OSI layer. For instance, when referring to an application layer protocol in a TCP/IP|из уровня OSI. Например, при обращении к протоколу прикладного уровня в TCP / IP
network, the world still refers to the protocol as a “Layer 7 protocol.” Also, while TCP/IP|сети, мир по-прежнему называет этот протокол «протоколом уровня 7». Также, хотя TCP / IP
includes more functions at its application layer, OSI breaks those intro session, presentation,|включает больше функций на уровне приложений, OSI прерывает вводную сессию, презентацию,
and application layers. Most of the time, no one cares much about the distinction, so you|и прикладные уровни. В большинстве случаев никто не заботится о различиях, поэтому вы
will see references like “Layer 5–7 protocol,” again using OSI numbering.|будут отображаться ссылки типа «Протокол уровня 5–7», опять же с использованием нумерации OSI.
For the purposes of this book, know the mapping between the five-layer TCP/IP model and|Для целей этой книги необходимо знать соответствие между пятиуровневой моделью TCP / IP и
the seven-layer OSI model shown in Figure 1-14, and know that layer number references to|семиуровневая модель OSI, показанная на рисунке 1-14, и знайте, что номер уровня ссылается на
Layer 7 really do match the application layer of TCP/IP as well.|Уровень 7 действительно соответствует прикладному уровню TCP / IP.
### OSI Data Encapsulation Terminology
Терминология инкапсуляции данных OSI   
__|__
--|--
Like TCP/IP, each OSI layer asks for services from the next lower layer. To provide the services, each layer makes use of a header and possibly a trailer. The lower layer encapsulates|Как и TCP / IP, каждый уровень OSI запрашивает услуги у следующего нижнего уровня. Для предоставления услуг каждый уровень использует заголовок и, возможно, трейлер. Нижний слой инкапсулирует
the higher layer’s data behind a header.|данные более высокого уровня за заголовком.
OSI uses a more generic term to refer to messages, rather than frame, packet, and segment.|OSI использует более общий термин для обозначения сообщений, а не кадра, пакета и сегмента.
OSI uses the term protocol data unit (PDU). A PDU represents the bits that include the|OSI использует термин блок данных протокола (PDU). PDU представляет биты, которые включают
headers and trailers for that layer, as well as the encapsulated data. For example, an IP packet,|заголовки и трейлеры для этого уровня, а также инкапсулированные данные. Например, IP-пакет,
as shown in Figure 1-13, using OSI terminology, is a PDU, more specifically a Layer 3 PDU|как показано на рисунке 1-13, используя терминологию OSI, это PDU, а точнее PDU уровня 3.
(abbreviated L3PDU) because IP is a Layer 3 protocol. OSI simply refers to the Layer x|(сокращенно L3PDU), потому что IP - это протокол уровня 3. OSI просто относится к Layer x
PDU (LxPDU), with x referring to the number of the layer being discussed, as shown in|PDU (LxPDU), где x относится к номеру обсуждаемого уровня, как показано на
Figure 1-15.|Рисунок 1-15.
L#H - Layer # Header|L # H - Заголовок слоя #
L#T - Layer # Trailer|L # T - Layer # Trailer
L7H Data|Данные L7H
L6H Data|Данные L6H
L5H Data|Данные L5H
L4H Data|Данные L4H
L3H Data|Данные L3H
L2H Data L2T|L2H Данные L2T
L7PDU|L7PDU
L6PDU|L6PDU
L5PDU|L5PDU
L4PDU|L4PDU
L3PDU|L3PDU
L2PDU|L2PDU
Figure 1-15 OSI Encapsulation and Protocol Data Units|Рисунок 1-15 Инкапсуляция OSI и блоки данных протокола
## Chapter Review
Обзор главы   
__|__
--|--
The “Your Study Plan” element, just before Chapter 1, discusses how you should study and|Элемент «Ваш учебный план», непосредственно перед главой 1, обсуждает, как вы должны учиться и
practice the content and skills for each chapter before moving on to the next chapter. That|Практикуйте содержание и навыки для каждой главы, прежде чем переходить к следующей главе. Что
element introduces the tools used here at the end of each chapter. If you haven’t already|element представляет инструменты, используемые здесь, в конце каждой главы. Если вы еще не
done so, take a few minutes to read that section. Then come back here and do the useful|Если так, уделите несколько минут, чтобы прочитать этот раздел. Тогда вернись сюда и сделай полезное
work of reviewing the chapter to help lock into memory what you just read.|работа по пересмотру главы, чтобы закрепить в памяти то, что вы только что прочитали.
Review this chapter’s material using either the tools in the book or the interactive tools for|Просмотрите материал этой главы, используя инструменты из книги или интерактивные инструменты для
the same material found on the book’s companion website. Table 1-4 outlines the key review|тот же материал, что и на сопутствующем веб-сайте книги. В таблице 1-4 представлен основной обзор.
elements and where you can find them. To better track your study progress, record when you|элементы и где их можно найти. Чтобы лучше отслеживать прогресс в учебе, записывайте, когда вы
completed these activities in the second column.|завершили эти действия во втором столбце.
Technet24|Технет24
Table 1-4 Chapter Review Tracking|Таблица 1-4 Отслеживание обзора главы
Review Element Review Date(s) Resource Used|Элемент обзора Дата (даты) обзора Используемый ресурс
Review key topics Book, website|Просмотрите ключевые темы Книга, веб-сайт
Review key terms Book, website|Просмотрите основные термины Книга, веб-сайт
Answer DIKTA questions Book, PTP Online|Книга ответов на вопросы ДИКТА, PTP Online
Review All the Key Topics|Просмотрите все ключевые темы
Table 1-5 Key Topics for Chapter 1|Таблица 1-5 Ключевые темы главы 1
Key Topic|Ключевая тема
Elements|Элементы
Description Page|Описание Страница
Number|номер
Table 1-3 Provides definitions of same-layer and adjacent-layer interaction 22|Таблица 1-3 Дает определения взаимодействия одного и того же уровня и соседнего уровня 22
Figure 1-10 Shows the general concept of IP routing 25|На рисунке 1-10 показана общая концепция IP-маршрутизации 25.
Figure 1-11 Depicts the data-link services provided to IP for the purpose of|На Рис. 1-11 изображены услуги канала передачи данных, предоставляемые IP для
delivering IP packets from host to host|доставка IP-пакетов от хоста к хосту
26|26
Figure 1-12 Five steps to encapsulate data on the sending host 28|Рисунок 1-12 Пять шагов для инкапсуляции данных на хосте-отправителе 28
Figure 1-13 Shows the meaning of the terms segment, packet, and frame 28|На рисунке 1-13 показано значение терминов сегмент, пакет и кадр 28.
Figure 1-14 Compares the OSI and TCP/IP network models 29|Рисунок 1-14 Сравнение сетевых моделей OSI и TCP / IP 29
Figure 1-15 Terminology related to encapsulation 30|Рисунок 1-15 Терминология, относящаяся к инкапсуляции 30
Key Terms You Should Know|Ключевые термины, которые вам следует знать
adjacent-layer interaction, de-encapsulation, encapsulation, frame, networking model, packet,|взаимодействие на смежном уровне, деинкапсуляция, инкапсуляция, кадр, сетевая модель, пакет,
protocol data unit (PDU), same-layer interaction, segment|блок данных протокола (PDU), взаимодействие на одном уровне, сегмент
