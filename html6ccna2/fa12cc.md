## Part II Implementing Ethernet LANs
Часть II Реализация локальных сетей Ethernet   
__|__
--|--
Part II Review|Часть II Обзор
## Chapter 4 Using the Command-Line Interface
Глава 4 Использование интерфейса командной строки   
__|__
--|--
This chapter covers the following exam topics:|В этой главе рассматриваются следующие экзаменационные темы:
None This chapter explains foundational skills required before you can learn about the roughly 15 exam topics that use the verbs configure and verify.|Нет В этой главе объясняются базовые навыки, необходимые для изучения примерно 15 экзаменационных тем, в которых используются глаголы configure и verify.
However, Cisco does not list the foundational skills described in this chapter as a separate exam topic, so there are no specific exam topics included in this chapter.|Однако Cisco не перечисляет основные навыки, описанные в этой главе, в качестве отдельной темы экзамена, поэтому в эту главу не включены конкретные темы экзамена.
To create an Ethernet LAN, network engineers start by planning.|Чтобы создать локальную сеть Ethernet, сетевые инженеры начинают с планирования.
They consider the requirements, create a design, buy the switches, contract to install cables, and configure the switches to use the right features.|Они рассматривают требования, создают дизайн, покупают коммутаторы, заключают договор на установку кабелей и настраивают коммутаторы для использования нужных функций.
The CCNA exam focuses on skills like understanding how LANs work, configuring different switch features, verifying that those features work correctly, and finding the root cause of the problem when a feature is not working correctly.|Экзамен CCNA фокусируется на таких навыках, как понимание того, как работают локальные сети, настройка различных функций коммутатора, проверка правильности работы этих функций и обнаружение основной причины проблемы, когда функция работает неправильно.
The first skill you need to learn before doing all the configuration and verification tasks is to learn how to access and use the user interface of the switch, called the command-line interface (CLI).|Первый навык, который вам необходимо освоить перед выполнением всех задач настройки и проверки, - это узнать, как получить доступ и использовать пользовательский интерфейс коммутатора, называемый интерфейсом командной строки (CLI).
This chapter begins that process by showing the basics of how to access the switch’s CLI.|В этой главе этот процесс начинается с демонстрации основ доступа к интерфейсу командной строки коммутатора.
These skills include how to access the CLI and how to issue verification commands to check on the status of the LAN. This chapter also includes the processes of how to configure the switch and how to save that configuration.|Эти навыки включают в себя доступ к интерфейсу командной строки и запуск команд проверки для проверки состояния локальной сети. В этой главе также описаны процессы настройки коммутатора и сохранения этой конфигурации.
Note that this chapter focuses on processes that provide a foundation for most every exam topic that includes the verbs configure and/or verify.|Обратите внимание, что в этой главе основное внимание уделяется процессам, которые составляют основу практически каждой темы экзамена, включающей команды configure и / или verify.
Most of the rest of the chapters in Parts II and III of this book then go on to include details of the particular commands you can use to verify and configure different switch features.|В остальных главах частей II и III этой книги подробно описываются команды, которые можно использовать для проверки и настройки различных функций коммутатора.
### “Do I Know This Already?” Quiz
«Знаю ли я это уже?» Викторина   
__|__
--|--
Take the quiz (either here or use the PTP software) if you want to use the score to help you decide how much time to spend on this chapter.|Пройдите тест (здесь или воспользуйтесь программой PTP), если вы хотите использовать оценку, чтобы решить, сколько времени потратить на эту главу.
The letter answers are listed at the bottom of the page following the quiz.|Ответы на письма перечислены внизу страницы после викторины.
Appendix C, found both at the end of the book as well as on the companion website, includes both the answers and explanations.|Приложение C, которое можно найти как в конце книги, так и на сопутствующем веб-сайте, включает как ответы, так и пояснения.
You can also find both answers and explanations in the PTP testing software.|Вы также можете найти ответы и пояснения в программе тестирования PTP.
Table 4-1 “Do I Know This Already?” Foundation Topics Section-to-Question Mapping|Таблица 4-1 «Знаю ли я это уже?» Сопоставление разделов с вопросами по основным темам
### Foundation Topics
Основные темы   
### Accessing the Cisco Catalyst Switch CLI
Доступ к интерфейсу командной строки коммутатора Cisco Catalyst   
__|__
--|--
Configuring Cisco IOS Software 4–6 CHAPTER 4 1.|Настройка программного обеспечения Cisco IOS 4–6 ГЛАВА 4 1.
In what modes can you type the command show mac address-table and expect to get a response with MAC table entries? (Choose two answers.)|В каких режимах вы можете ввести команду show mac address-table и ожидать ответа с записями таблицы MAC? (Выберите два ответа.)
a. User mode b.|а. Пользовательский режим b.
Enable mode c.|Включить режим c.
Global configuration mode d.|Режим глобальной конфигурации d.
Interface configuration mode 2.|Режим настройки интерфейса 2.
In which of the following modes of the CLI could you type the command reload and expect the switch to reboot?|В каком из следующих режимов интерфейса командной строки вы могли бы ввести команду reload и ожидать, что коммутатор перезагрузится?
a. User mode b.|а. Пользовательский режим b.
Enable mode c.|Включить режим c.
Global configuration mode d.|Режим глобальной конфигурации d.
Interface configuration mode 3.|Режим настройки интерфейса 3.
Which of the following is a difference between Telnet and SSH as supported by a Cisco switch?|В чем разница между Telnet и SSH, поддерживаемыми коммутатором Cisco?
a. SSH encrypts the passwords used at login, but not other traffic; Telnet encrypts nothing.|а. SSH шифрует пароли, используемые при входе в систему, но не другой трафик; Telnet ничего не шифрует.
b. SSH encrypts all data exchange, including login passwords; Telnet encrypts nothing.|б. SSH шифрует весь обмен данными, включая пароли для входа; Telnet ничего не шифрует.
c. Telnet is used from Microsoft operating systems, and SSH is used from UNIX and Linux operating systems.|c. Telnet используется в операционных системах Microsoft, а SSH используется в операционных системах UNIX и Linux.
d. Telnet encrypts only password exchanges; SSH encrypts all data exchanges.|d. Telnet шифрует только обмен паролями; SSH шифрует все обмены данными.
4 What type of switch memory is used to store the configuration used by the switch when it is up and working?|4 Какой тип памяти коммутатора используется для хранения конфигурации, используемой коммутатором, когда он включен и работает?
a. RAM b.|а. RAM b.
ROM c.|ROM c.
Flash d.|Вспышка d.
NVRAM e.|NVRAM e.
Bubble 5.|Пузырь 5.
What command copies the configuration from RAM into NVRAM?|Какая команда копирует конфигурацию из RAM в NVRAM?
a. copy running-config tftp b. copy tftp running-config c. copy running-config start-up-config d. copy start-up-config running-config e. copy startup-config running-config f. copy running-config startup-config 6.|а. скопировать running-config tftp b. скопируйте tftp running-config c. скопировать рабочую конфигурацию start-up-config d. скопировать start-up-config, running-config e. скопировать start-config, running-config f. скопировать running-config startup-config 6.
A switch user is currently in console line configuration mode.|Пользователь коммутатора в настоящее время находится в режиме конфигурации линии консоли.
Which of the following would place the user in enable mode? (Choose two answers.)|Что из следующего переведет пользователя в режим включения? (Выберите два ответа.)
a. Using the exit command once b.|а. Однократное использование команды выхода b.
Using the end command once c.|Однократное использование команды завершения c.
Pressing the Ctrl+Z key sequence once d.|Однократное нажатие комбинации клавиш Ctrl + Z d.
Using the quit command Foundation Topics Accessing the Cisco Catalyst Switch CLI Cisco uses the concept of a command-line interface (CLI) with its router products and most of its Catalyst LAN switch products.|Использование команды quit Основные темы Доступ к интерфейсу командной строки коммутатора Cisco Catalyst Cisco использует концепцию интерфейса командной строки (CLI) в своих маршрутизаторах и большинстве коммутаторов Catalyst LAN.
The CLI is a text-based interface in which the user, typically a network engineer, enters a text command and presses Enter.|CLI - это текстовый интерфейс, в котором пользователь, обычно сетевой инженер, вводит текстовую команду и нажимает Enter.
Pressing Enter sends the command to the switch, which tells the device to do something.|Нажатие Enter отправляет команду на коммутатор, который говорит устройству что-то сделать.
The switch does what the command says, and in some cases, the switch replies with some messages stating the results of the command.|Коммутатор выполняет то, что говорит команда, и в некоторых случаях коммутатор отвечает некоторыми сообщениями, в которых указываются результаты выполнения команды.
Cisco Catalyst switches also support other methods to both monitor and configure a switch.|Коммутаторы Cisco Catalyst также поддерживают другие методы как для мониторинга, так и для настройки коммутатора.
For example, a switch can provide a web interface so that an engineer can open a web browser to connect to a web server running in the switch.|Например, коммутатор может предоставлять веб-интерфейс, чтобы инженер мог открыть веб-браузер для подключения к веб-серверу, работающему в коммутаторе.
Switches also can be controlled and operated using network management software.|Коммутаторами также можно управлять с помощью программного обеспечения для управления сетью.
This book discusses only Cisco Catalyst enterprise-class switches, and in particular, how to use the Cisco CLI to monitor and control these switches.|В этой книге обсуждаются только коммутаторы Cisco Catalyst корпоративного класса, и в частности, как использовать Cisco CLI для мониторинга и управления этими коммутаторами.
This first major section of the chapter first examines these Catalyst switches in more detail and then explains how a network engineer can get access to the CLI to issue commands.|В этом первом основном разделе главы сначала рассматриваются эти коммутаторы Catalyst более подробно, а затем объясняется, как сетевой инженер может получить доступ к интерфейсу командной строки для выполнения команд.
#### Cisco Catalyst Switches
Коммутаторы Cisco Catalyst   
__|__
--|--
Within the Cisco Catalyst brand of LAN switches, Cisco produces a wide variety of switch series or families.|В рамках торговой марки коммутаторов LAN Cisco Catalyst Cisco производит широкий выбор серий или семейств коммутаторов.
Each switch series includes several specific models of switches that have similar features, similar price-versus-performance tradeoffs, and similar internal components.|Каждая серия коммутаторов включает в себя несколько конкретных моделей коммутаторов, которые имеют схожие характеристики, одинаковое соотношение цены и производительности и аналогичные внутренние компоненты.
For example, at the time this book was published, the Cisco 2960-XR series of switches was a current switch model series.|Например, на момент публикации этой книги серия коммутаторов Cisco 2960-XR была текущей серией моделей коммутаторов.
Cisco positions the 2960-XR series (family) of switches as full-featured, low-cost wiring closet switches for enterprises.|Cisco позиционирует коммутаторы серии 2960-XR как полнофункциональные недорогие коммутаторы для коммутационных шкафов для предприятий.
That means that you would expect to use 2960-XR switches as access switches in a typical campus LAN design.|Это означает, что вы ожидаете использовать коммутаторы 2960-XR в качестве коммутаторов доступа в типичной конструкции локальной сети кампуса.
Figure 4-1 shows a photo of 10 different models from the 2960-XR switch model series from Cisco.|На рис. 4-1 показаны фотографии 10 различных моделей коммутаторов серии 2960-XR от Cisco.
Each switch series includes several models, with a mix of features.|Каждая серия переключателей включает в себя несколько моделей со множеством функций.
For example, some of the switches have 48 RJ-45 unshielded twisted-pair (UTP) 10/100/1000 ports, meaning that these ports can autonegotiate the use of 10BASE-T (10 Mbps), 100BASE-T (100 Mbps), or 1000BASE-T (1 Gbps) Ethernet.|Например, некоторые из коммутаторов имеют 48 портов неэкранированной витой пары (UTP) RJ-45 10/100/1000, что означает, что эти порты могут автоматически согласовывать использование 10BASE-T (10 Мбит / с), 100BASE-T (100 Мбит / с). или 1000BASE-T (1 Гбит / с) Ethernet.
Figure 4-1 Cisco 2960-XR Catalyst Switch Series Cisco refers to a switch’s physical connectors as either interfaces or ports, with an interface type and interface number.|Рис. 4-1. Коммутаторы серии Cisco 2960-XR Catalyst Cisco называет физические разъемы коммутатора интерфейсами или портами с указанием типа и номера интерфейса.
The interface type, as used in commands on the switch, is either Ethernet, Fast Ethernet, Gigabit Ethernet, and so on for faster speeds.|Тип интерфейса, используемый в командах на коммутаторе, - Ethernet, Fast Ethernet, Gigabit Ethernet и т. Д. Для более высоких скоростей.
For Ethernet interfaces that support running at multiple speeds, the permanent name for the interface refers to the fastest supported speed.|Для интерфейсов Ethernet, которые поддерживают работу на нескольких скоростях, постоянное имя интерфейса относится к максимальной поддерживаемой скорости.
For example, a 10/100/1000 interface (that is, an interface that runs at 10 Mbps, 100 Mbps, or 1000 Mbps) would be called Gigabit Ethernet no matter what speed is currently in use.|Например, интерфейс 10/100/1000 (то есть интерфейс, работающий на скорости 10, 100 или 1000 Мбит / с) будет называться Gigabit Ethernet независимо от того, какая скорость используется в настоящее время.
To uniquely number each different interface, some Catalyst switches use a two-digit interface number (x/y), while others have a three-digit number (x/y/z).|Чтобы однозначно пронумеровать каждый интерфейс, некоторые коммутаторы Catalyst используют двузначный номер интерфейса (x / y), а другие - трехзначный номер (x / y / z).
For instance, two 10/100/1000 ports on many older Cisco Catalyst switches would be called GigabitEthernet 0/0 and GigabitEthernet 0/1, while on the newer 2960-XR series, two interfaces would be GigabitEthernet 1/0/1 and GigabitEthernet 1/0/2.|Например, два порта 10/100/1000 на многих старых коммутаторах Cisco Catalyst будут называться GigabitEthernet 0/0 и GigabitEthernet 0/1, в то время как в более новой серии 2960-XR два интерфейса будут называться GigabitEthernet 1/0/1 и GigabitEthernet. 1/0/2.
#### Accessing the Cisco IOS CLI
Доступ к интерфейсу командной строки Cisco IOS   
__|__
--|--
Like any other piece of computer hardware, Cisco switches need some kind of operating system software.|Как и любому другому компьютерному оборудованию, коммутаторам Cisco требуется какое-то программное обеспечение операционной системы.
Cisco calls this OS the Internetwork Operating System (IOS).|Cisco называет эту ОС Межсетевой операционной системой (IOS).
Cisco IOS Software for Catalyst switches implements and controls logic and functions performed by a Cisco switch.|Программное обеспечение Cisco IOS для коммутаторов Catalyst реализует и контролирует логику и функции, выполняемые коммутатором Cisco.
Besides controlling the switch’s performance and behavior, Cisco IOS also defines an interface for humans called the CLI. The Cisco IOS CLI allows the user to use a terminal emulation program, which accepts text entered by the user.|Помимо управления производительностью и поведением коммутатора, Cisco IOS также определяет интерфейс для людей, называемый CLI. Интерфейс командной строки Cisco IOS позволяет пользователю использовать программу эмуляции терминала, которая принимает текст, введенный пользователем.
When the user presses Enter, the terminal emulator sends that text to the switch.|Когда пользователь нажимает Enter, эмулятор терминала отправляет этот текст коммутатору.
The switch processes the text as if it is a command, does what the command says, and sends text back to the terminal emulator.|Коммутатор обрабатывает текст, как будто это команда, выполняет то, что команда говорит, и отправляет текст обратно в эмулятор терминала.
The switch CLI can be accessed through three popular methods—the console, Telnet, and Secure Shell (SSH). Two of these methods (Telnet and SSH) use the IP network in which the switch resides to reach the switch.|Доступ к интерфейсу командной строки коммутатора можно получить с помощью трех популярных методов - консоли, Telnet и Secure Shell (SSH). Два из этих методов (Telnet и SSH) используют IP-сеть, в которой находится коммутатор, для достижения коммутатора.
The console is a physical port built specifically to allow access to the CLI. Figure 4-2 depicts the options.|Консоль - это физический порт, созданный специально для доступа к CLI. На рис. 4-2 показаны варианты.
Figure 4-2 CLI Access Options Console access requires both a physical connection between a PC (or other user device) and the switch’s console port, as well as some software on the PC. Telnet and SSH require software on the user’s device, but they rely on the existing TCP/IP network to transmit data.|Рис. 4-2 Параметры доступа через интерфейс командной строки Для доступа к консоли требуется физическое соединение между ПК (или другим пользовательским устройством) и консольным портом коммутатора, а также некоторое программное обеспечение на ПК. Telnet и SSH требуют наличия программного обеспечения на устройстве пользователя, но для передачи данных они полагаются на существующую сеть TCP / IP.
The next few pages detail how to connect the console and set up the software for each method to access the CLI.|На следующих нескольких страницах подробно описано, как подключить консоль и настроить программное обеспечение для каждого метода доступа к интерфейсу командной строки.
##### Cabling the Console Connection
Кабельное соединение с консолью   
__|__
--|--
The physical console connection, both old and new, uses three main components: the physical console port on the switch, a physical serial port on the PC, and a cable that works with the console and serial ports.|Физическое консольное соединение, как старое, так и новое, использует три основных компонента: физический консольный порт на коммутаторе, физический последовательный порт на ПК и кабель, который работает с консолью и последовательными портами.
However, the physical cabling details have changed slowly over time, mainly because of advances and changes with serial interfaces on PC hardware.|Однако детали физических кабелей со временем менялись медленно, в основном из-за достижений и изменений в последовательных интерфейсах на оборудовании ПК.
For this next topic, the text looks at three cases: newer connectors on both the PC and the switch, older connectors on both, and a third case with the newer (USB) connector on the PC but with an older connector on the switch.|В этой следующей теме в тексте рассматриваются три случая: более новые разъемы на ПК и коммутаторе, более старые разъемы на обоих и третий случай с более новым (USB) разъемом на ПК, но со старым разъемом на коммутаторе.
Most PCs today use a familiar standard USB cable for the console connection.|В большинстве современных ПК для подключения консоли используется знакомый стандартный USB-кабель.
Cisco has been including USB ports as console ports in newer routers and switches as well.|Cisco также включает порты USB в качестве консольных портов в новые маршрутизаторы и коммутаторы.
All you have to do is look at the switch to make sure you have the correct style of USB cable end to match the USB console port.|Все, что вам нужно сделать, это посмотреть на коммутатор, чтобы убедиться, что у вас правильный тип конца USB-кабеля, соответствующий консольному порту USB.
In the simplest form, you can use any USB port on the PC, with a USB cable, connected to the USB console port on the switch or router, as shown on the far right side of Figure 4-3.|В простейшей форме вы можете использовать любой порт USB на ПК с помощью кабеля USB, подключенного к консольному порту USB на коммутаторе или маршрутизаторе, как показано в правой части рисунка 4-3.
Figure 4-3 Console Connection to a Switch Older console connections use a PC serial port that pre-dates USB, a UTP cable, and an RJ-45 console port on the switch, as shown on the left side of Figure 4-3.|Рисунок 4-3 Подключение консоли к коммутатору В старых версиях консольных подключений используется последовательный порт ПК, предшествующий USB, кабель UTP и консольный порт RJ-45 на коммутаторе, как показано в левой части рисунка 4-3.
The PC serial port typically has a D-shell connector (roughly rectangular) with nine pins (often called a DB-9).|Последовательный порт ПК обычно имеет D-образный разъем (примерно прямоугольной формы) с девятью контактами (часто называемый DB-9).
The console port looks like any Ethernet RJ-45 port (but is typically colored in blue and with the word console beside it on the switch).|Консольный порт выглядит как любой порт Ethernet RJ-45 (но обычно окрашен в синий цвет, а рядом с ним на коммутаторе написано слово console).
The cabling for this older-style console connection can be simple or require some effort, depending on what cable you use.|Кабели для этого консольного подключения старого типа могут быть простыми или потребовать некоторых усилий, в зависимости от того, какой кабель вы используете.
You can use the purpose-built console cable that ships with new Cisco switches and routers and not think about the details.|Вы можете использовать специальный консольный кабель, который поставляется с новыми коммутаторами и маршрутизаторами Cisco, и не думать о деталях.
However, you can make Answers to the “Do I Know This Already?” quiz:|Однако вы можете ответить на вопрос «Знаю ли я это уже?» викторина:
1 A, B 2 B 3 B 4 A 5 F 6 B, C your own cable with a standard serial cable (with a connector that matches the PC), a standard RJ-45 to DB-9 converter plug, and a UTP cable.|1 A, B 2 B 3 B 4 A 5 F 6 B, C собственный кабель со стандартным последовательным кабелем (с разъемом, который соответствует компьютеру), стандартный переходник RJ-45 в DB-9 и кабель UTP .
However, the UTP cable does not use the same pinouts as Ethernet; instead, the cable uses rollover cable pinouts rather than any of the standard Ethernet cabling pinouts.|Однако кабель UTP не использует те же выводы, что и Ethernet; вместо этого в кабеле используются выводы переключаемого кабеля, а не какие-либо стандартные выводы кабелей Ethernet.
The rollover pinout uses eight wires, rolling the wire at pin 1 to pin 8, pin 2 to pin 7, pin 3 to pin 6, and so on.|Распиновка для опрокидывания использует восемь проводов, наматывающих провод от контакта 1 к контакту 8, от контакта 2 к контакту 7, контакта 3 к контакту 6 и так далее.
As it turns out, USB ports became common on PCs before Cisco began commonly using USB for its console ports.|Как оказалось, порты USB стали обычным явлением на ПК до того, как Cisco начала широко использовать USB для своих консольных портов.
So, you also have to be ready to use a PC that has only a USB port and not an old serial port, but a router or switch that has the older RJ-45 console port (and no USB console port).|Таким образом, вы также должны быть готовы к использованию ПК, у которого есть только порт USB, а не старый последовательный порт, а маршрутизатор или коммутатор с более старым консольным портом RJ-45 (и без консольного порта USB).
The center of Figure 4-3 shows that case.|В центре рисунка 4-3 показан этот случай.
To connect such a PC to a router or switch console, you need a USB converter that converts from the older console cable to a USB connector, and a rollover UTP cable, as shown in the middle of Figure 4-3.|Чтобы подключить такой ПК к маршрутизатору или консоли коммутатора, вам понадобится USB-преобразователь, который преобразует старый консольный кабель в USB-разъем, и переключаемый кабель UTP, как показано в середине рисунка 4-3.
NOTE When using the USB options, you typically also need to install a software driver so that your PC’s OS knows that the device on the other end of the USB connection is the console of a Cisco device.|ПРИМЕЧАНИЕ. При использовании опций USB обычно также необходимо установить драйвер программного обеспечения, чтобы ОС вашего ПК знала, что устройство на другом конце USB-соединения является консолью устройства Cisco.
Also, you can easily find photos of these cables and components online, with searches like “cisco console cable,” “cisco usb console cable,” or “console cable converter.”|Кроме того, вы можете легко найти фотографии этих кабелей и компонентов в Интернете по запросу «консольный кабель cisco», «консольный кабель cisco usb» или «преобразователь консольного кабеля».
The 2960-XR series, for instance, supports both the older RJ-45 console port and a USB console port.|Например, серия 2960-XR поддерживает как старый консольный порт RJ-45, так и консольный порт USB.
Figure 4-4 points to the two console ports; you would use only one or the other.|Рисунок 4-4 указывает на два консольных порта; вы бы использовали только один или другой.
Note that the USB console port uses a mini-B port rather than the more commonly seen rectangular standard USB Type A port.|Обратите внимание, что для консольного порта USB используется порт mini-B, а не более часто встречающийся прямоугольный стандартный порт USB типа A.
Figure 4-4 A Part of a 2960-XR Switch with Console Ports Shown After the PC is physically connected to the console port, a terminal emulator software package must be installed and configured on the PC. The terminal emulator software treats all data as text.|Рисунок 4-4. Показана часть коммутатора 2960-XR с консольными портами. После того, как ПК физически подключен к консольному порту, на ПК должен быть установлен и настроен программный пакет эмулятора терминала. Программное обеспечение эмулятора терминала обрабатывает все данные как текст.
It accepts the text typed by the user and sends it over the console connection to the switch.|Он принимает текст, введенный пользователем, и отправляет его через консольное соединение на коммутатор.
Similarly, any bits coming into the PC over the console connection are displayed as text for the user to read.|Точно так же любые биты, поступающие в ПК через консольное соединение, отображаются в виде текста для чтения пользователем.
The emulator must be configured to use the PC’s serial port to match the settings on the switch’s console port settings.|Эмулятор должен быть настроен на использование последовательного порта ПК в соответствии с настройками консольного порта коммутатора.
The default console port settings on a switch are as follows.|Настройки консольного порта по умолчанию на коммутаторе следующие.
Note that the last three parameters are referred to collectively as 8N1:|Обратите внимание, что последние три параметра вместе называются 8N1:
###### 9600 bits/second
9600 бит / сек   
###### No hardware flow control
Нет аппаратного управления потоком   
###### 8-bit ASCII
8-битный ASCII   
###### No parity bits
Нет битов четности   
###### 1 stop bit
1 стоповый бит   
__|__
--|--
Figure 4-5 shows one such terminal emulator.|На рис. 4-5 показан один из таких эмуляторов терминала.
The image shows the window created by the emulator software in the background, with some output of a show command.|На изображении показано окно, созданное программным обеспечением эмулятора в фоновом режиме, с некоторыми выходными данными команды show.
The foreground, in the upper right, shows a settings window that lists the default console settings as listed just before this paragraph.|На переднем плане в правом верхнем углу показано окно настроек, в котором перечислены настройки консоли по умолчанию, перечисленные непосредственно перед этим абзацем.
Figure 4-5 Terminal Settings for Console Access|Рисунок 4-5 Настройки терминала для консольного доступа
##### Accessing the CLI with Telnet and SSH
Доступ к CLI с помощью Telnet и SSH   
__|__
--|--
For many years, terminal emulator applications have supported far more than the ability to communicate over a serial port to a local device (like a switch’s console).|В течение многих лет приложения-эмуляторы терминала поддерживали гораздо больше, чем просто возможность связи через последовательный порт с локальным устройством (например, с консолью коммутатора).
Terminal emulators support a variety of TCP/IP applications as well, including Telnet and SSH. Telnet and SSH both allow the user to connect to another device’s CLI, but instead of connecting through a console cable to the console port, the traffic flows over the same IP network that the networking devices are helping to create.|Эмуляторы терминала также поддерживают множество приложений TCP / IP, включая Telnet и SSH. Telnet и SSH позволяют пользователю подключаться к интерфейсу командной строки другого устройства, но вместо подключения через консольный кабель к консольному порту трафик проходит по той же IP-сети, которую сетевые устройства помогают создать.
Telnet uses the concept of a Telnet client (the terminal application) and a Telnet server (the switch in this case).|Telnet использует концепцию клиента Telnet (терминальное приложение) и сервера Telnet (в данном случае коммутатора).
A Telnet client, the device that sits in front of the user, accepts keyboard input and sends those commands to the Telnet server.|Клиент Telnet, устройство, которое находится перед пользователем, принимает ввод с клавиатуры и отправляет эти команды на сервер Telnet.
The Telnet server accepts the text, interprets the text as a command, and replies back.|Сервер Telnet принимает текст, интерпретирует текст как команду и отвечает в ответ.
Cisco Catalyst switches enable a Telnet server by default, but switches need a few more configuration settings before you can successfully use Telnet to connect to a switch.|Коммутаторы Cisco Catalyst включают сервер Telnet по умолчанию, но коммутаторам требуется еще несколько параметров конфигурации, прежде чем вы сможете успешно использовать Telnet для подключения к коммутатору.
Chapter 6, “Configuring Basic Switch Management,” covers switch configuration to support Telnet and SSH in detail.|В главе 6 «Настройка базового управления коммутатором» подробно рассматривается настройка коммутатора для поддержки Telnet и SSH.
Using Telnet in a lab today makes sense, but Telnet poses a significant security risk in production networks.|Использование Telnet в лабораторных условиях сегодня имеет смысл, но Telnet представляет собой значительную угрозу безопасности в производственных сетях.
Telnet sends all data (including any username and password for login to the switch) as clear-text data.|Telnet отправляет все данные (включая любое имя пользователя и пароль для входа в коммутатор) в виде данных в открытом виде.
SSH gives us a much better option.|SSH дает нам гораздо лучший вариант.
Think of SSH as the much more secure Telnet cousin.|Думайте о SSH как о гораздо более безопасном родственнике Telnet.
Outwardly, you still open a terminal emulator, connect to the switch’s IP address, and see the switch CLI, no matter whether you use Telnet or SSH. The differences exist behind the scenes: SSH encrypts the contents of all messages, including the passwords, avoiding the possibility of someone capturing packets in the network and stealing the password to network devices.|Внешне вы по-прежнему открываете эмулятор терминала, подключаетесь к IP-адресу коммутатора и видите интерфейс командной строки коммутатора, независимо от того, используете ли вы Telnet или SSH. Различия существуют за кулисами: SSH шифрует содержимое всех сообщений, включая пароли, избегая возможности перехвата пакетов в сети и кражи пароля к сетевым устройствам.
##### User and Enable \(Privileged\) Modes
Пользовательский и Включить \ (Привилегированные \) режимы   
__|__
--|--
All three CLI access methods covered so far (console, Telnet, and SSH) place the user in an area of the CLI called user EXEC mode.|Все три метода доступа к интерфейсу командной строки, рассмотренные до сих пор (консоль, Telnet и SSH), помещают пользователя в область интерфейса командной строки, называемую режимом пользовательского EXEC.
User EXEC mode, sometimes also called user mode, allows the user to look around but not break anything.|Пользовательский режим EXEC, иногда также называемый пользовательским режимом, позволяет пользователю смотреть вокруг, но ничего не ломать.
The “EXEC mode” part of the name refers to the fact that in this mode, when you enter a command, the switch executes the command and then displays messages that describe the command’s results.|Часть имени «EXEC mode» относится к тому факту, что в этом режиме, когда вы вводите команду, коммутатор выполняет команду, а затем отображает сообщения, описывающие результаты команды.
NOTE If you have not used the CLI before, you might want to experiment with the CLI from the Sim Lite product, or view the video about CLI basics.|ПРИМЕЧАНИЕ. Если вы раньше не использовали интерфейс командной строки, возможно, вы захотите поэкспериментировать с интерфейсом командной строки из продукта Sim Lite или просмотреть видео об основах интерфейса командной строки.
You can find these resources on the companion website as mentioned in the Introduction.|Вы можете найти эти ресурсы на сопутствующем веб-сайте, как указано во введении.
Cisco IOS supports a more powerful EXEC mode called enable mode (also known as privileged mode or privileged EXEC mode).|Cisco IOS поддерживает более мощный режим EXEC, называемый режимом включения (также известный как привилегированный режим или привилегированный режим EXEC).
Enable mode gets its name from the enable command, which moves the user from user mode to enable mode, as shown in Figure 4-6.|Режим включения получил свое название от команды enable, которая переводит пользователя из пользовательского режима в режим включения, как показано на рисунке 4-6.
The other name for this mode, privileged mode, refers to the fact that powerful (or privileged)|Другое название этого режима, привилегированный режим, относится к тому факту, что мощный (или привилегированный)
commands can be executed there.|команды могут быть выполнены там.
For example, you can use the reload command, which tells the switch to reinitialize or reboot Cisco IOS, only from enable mode.|Например, вы можете использовать команду reload, которая сообщает коммутатору о необходимости повторной инициализации или перезагрузки Cisco IOS только из режима включения.
NOTE If the command prompt lists the hostname followed by a >, the user is in user mode;|ПРИМЕЧАНИЕ. Если в командной строке указано имя хоста, за которым следует>, пользователь находится в пользовательском режиме;
if it is the hostname followed by the #, the user is in enable mode.|если это имя хоста, за которым следует #, пользователь находится в режиме включения.
Figure 4-6 User and Privileged Modes Example 4-1 demonstrates the differences between user and enable modes.|Рис. 4-6 Пользовательский и привилегированный режимы Пример 4-1 демонстрирует различия между пользовательским и активным режимами.
The example shows the output that you could see in a terminal emulator window, for instance, when connecting from the console.|В примере показан вывод, который вы могли видеть в окне эмулятора терминала, например, при подключении с консоли.
In this case, the user sits at the user mode prompt (“Certskills1>”)|В этом случае пользователь сидит в приглашении пользовательского режима («Certskills1>»).
and tries the reload command.|и пытается выполнить команду перезагрузки.
The reload command tells the switch to reinitialize or reboot Cisco IOS, so IOS allows this powerful command to be used only from enable mode.|Команда reload сообщает коммутатору о необходимости повторной инициализации или перезагрузки Cisco IOS, поэтому IOS позволяет использовать эту мощную команду только в режиме включения.
IOS rejects the reload command when used in user mode.|IOS отклоняет команду перезагрузки при использовании в пользовательском режиме.
Then the user moves to enable mode—|Затем пользователь переходит в режим включения -
also called privileged mode—(using the enable EXEC command).|также называется привилегированным режимом - (с помощью команды enable EXEC).
At that point, IOS accepts the reload command now that the user is in enable mode.|В этот момент IOS принимает команду перезагрузки теперь, когда пользователь находится в режиме включения.
Example 4-1 Example of Privileged Mode Commands Being Rejected in User Mode Example end.|Пример 4-1. Пример отклонения команд привилегированного режима в пользовательском режиме. Пример конец.
NOTE The commands that can be used in either user (EXEC) mode or enable (EXEC)|ПРИМЕЧАНИЕ Команды, которые можно использовать в пользовательском (EXEC) режиме или разрешающем (EXEC) режиме.
mode are called EXEC commands.|mode называются командами EXEC.
This example is the first instance of this book showing you the output from the CLI, so it is worth noting a few conventions.|Этот пример является первым экземпляром в этой книге, показывающим результаты работы интерфейса командной строки, поэтому стоит отметить несколько соглашений.
The bold text represents what the user typed, and the nonbold text is what the switch sent back to the terminal emulator.|Полужирный текст представляет то, что набрал пользователь, а жирный текст - это то, что коммутатор отправил обратно в эмулятор терминала.
Also, the typed passwords do not show up on the screen for security purposes.|Кроме того, введенные пароли не отображаются на экране в целях безопасности.
Finally, note that this switch has been preconfigured with a hostname of Certskills1, so the command prompt on the left shows that hostname on each line.|Наконец, обратите внимание, что этот переключатель был предварительно настроен с именем хоста Certskills1, поэтому в командной строке слева отображается это имя хоста в каждой строке.
##### Password Security for CLI Access from the Console
Защита паролем для доступа через интерфейс командной строки из консоли   
__|__
--|--
A Cisco switch, with default settings, remains relatively secure when locked inside a wiring closet, because by default, a switch allows console access only.|Коммутатор Cisco с настройками по умолчанию остается относительно безопасным, когда он заблокирован внутри коммутационного шкафа, поскольку по умолчанию коммутатор разрешает доступ только к консоли.
By default, the console requires no password at all, and no password to reach enable mode for users that happened to connect from the console.|По умолчанию консоль вообще не требует пароля и пароля для перехода в режим включения для пользователей, которые подключились с консоли.
The reason is that if you have access to the physical console port of the switch, you already have pretty much complete control over the switch.|Причина в том, что если у вас есть доступ к физическому консольному порту коммутатора, у вас уже есть практически полный контроль над коммутатором.
You could literally get out your screwdriver and walk off with it, or you could unplug the power, or follow well-published procedures to go through password recovery to break into the CLI and then configure anything you want to configure.|Вы можете буквально достать отвертку и уйти с ней, или вы можете отключить питание, или следовать хорошо опубликованным процедурам, чтобы пройти восстановление пароля, чтобы взломать CLI, а затем настроить все, что вы хотите настроить.
However, many people go ahead and set up simple password protection for console users.|Однако многие люди устанавливают простую защиту паролем для пользователей консоли.
Simple passwords can be configured at two points in the login process from the console:|Простые пароли можно настроить на двух этапах процесса входа в систему с консоли:
when the user connects from the console, and when any user moves to enable mode (using the enable EXEC command).|когда пользователь подключается с консоли, и когда любой пользователь переходит в режим включения (с помощью команды enable EXEC).
You may have noticed that back in Example 4-1, the user saw a password prompt at both points.|Возможно, вы заметили, что в примере 4-1 пользователь видел запрос пароля в обеих точках.
Example 4-2 shows the additional configuration commands that were configured prior to collecting the output in Example 4-1.|В примере 4-2 показаны дополнительные команды конфигурации, которые были настроены до сбора выходных данных в примере 4-1.
The output holds an excerpt from the EXEC command show running-config, which lists the current configuration in the switch.|Выходные данные содержат отрывок из команды EXEC show running-config, в которой отображается текущая конфигурация коммутатора.
Example 4-2 Nondefault Basic Configuration Example end.|Пример 4-2 Пример базовой конфигурации нестандартной конфигурации конец.
Working from top to bottom, note that the first configuration command listed by the show running-config command sets the switch’s hostname to Certskills1.|Работая сверху вниз, обратите внимание, что первая команда настройки, указанная в команде show running-config, устанавливает имя хоста коммутатора Certskills1.
You might have noticed that the command prompts in Example 4-1 all began with Certskills1, and that’s why the command prompt begins with the hostname of the switch.|Вы могли заметить, что все командные запросы в примере 4-1 начинались с Certskills1, и поэтому командная строка начинается с имени хоста коммутатора.
Next, note that the lines with a ! in them are comment lines, both in the text of this book and in the real switch CLI.|Затем обратите внимание, что строки с символом! в них есть строки комментариев, как в тексте этой книги, так и в реальном CLI коммутатора.
The enable secret love configuration command defines the password that all users must use to reach enable mode.|Команда настройки enable secret love определяет пароль, который должны использовать все пользователи для перехода в режим включения.
So, no matter whether users connect from the console, Telnet, or SSH, they would use the password love when prompted for a password after typing the enable EXEC command.|Таким образом, независимо от того, подключаются ли пользователи через консоль, Telnet или SSH, они будут использовать пароль love при запросе пароля после ввода команды enable EXEC.
Finally, the last three lines configure the console password.|Наконец, последние три строки настраивают пароль консоли.
The first line (line console 0) is the command that identifies the console, basically meaning “these next commands apply to the console only.” The login command tells IOS to perform simple password checking (at the console).|Первая строка (строка console 0) - это команда, которая идентифицирует консоль, в основном это означает, что «следующие команды применяются только к консоли». Команда входа в систему указывает IOS выполнить простую проверку пароля (на консоли).
Remember, by default, the switch does not ask for a password for console users.|Помните, что по умолчанию коммутатор не запрашивает пароль для пользователей консоли.
Finally, the password faith command defines the password the console user must type when prompted.|И, наконец, команда password trust определяет пароль, который пользователь консоли должен вводить при появлении запроса.
This example just scratches the surface of the kinds of security configuration you might choose to configure on a switch, but it does give you enough detail to configure switches in your lab and get started (which is the reason I put these details in this first chapter of Part II). Note that Chapter 6 shows the configuration steps to add support for Telnet and SSH Volume 2, “Securing Network Devices,” shows additional security configuration as well.|Этот пример лишь поверхностно описывает типы конфигурации безопасности, которые вы можете выбрать для настройки на коммутаторе, но он дает вам достаточно подробностей для настройки коммутаторов в вашей лаборатории и начала работы (поэтому я поместил эти подробности в эту первую главу). части II). Обратите внимание, что в главе 6 показаны шаги настройки для добавления поддержки Telnet и SSH. В томе 2 «Защита сетевых устройств» также показаны дополнительные настройки безопасности.
#### CLI Help Features
Функции справки CLI   
__|__
--|--
If you printed the Cisco IOS Command Reference documents, you would end up with a stack of paper several feet tall.|Если бы вы распечатали справочные документы по командам Cisco IOS, у вас получилась бы стопка бумаги высотой в несколько футов.
No one should expect to memorize all the commands—and no one does.|Никто не должен запоминать все команды - и никто этого не делает.
You can use several very easy, convenient tools to help remember commands and save time typing.|Вы можете использовать несколько очень простых и удобных инструментов, которые помогут запомнить команды и сэкономить время на вводе текста.
As you progress through your Cisco certifications, the exams will cover progressively more commands.|По мере прохождения сертификации Cisco экзамены будут охватывать все больше команд.
However, you should know the methods of getting command help.|Однако вы должны знать методы получения справки по командам.
Table 4-2 summarizes command-recall help options available at the CLI. Note that, in the first column, command represents any command.|В таблице 4-2 приведены параметры справки по вызову команд, доступные в интерфейсе командной строки. Обратите внимание, что в первом столбце команда представляет любую команду.
Likewise, parm represents a command’s parameter.|Точно так же parm представляет параметр команды.
For example, the second row lists command ?, which means that commands such as show ? and copy ? would list help for the show and copy commands, respectively.|Например, во второй строке перечислены команды?, Что означает, что такие команды, как show? и скопировать? будет отображать справку по командам show и copy соответственно.
Table 4-2 Cisco IOS Software Command Help Table end.|Таблица 4-2 Конец таблицы справки по командам программного обеспечения Cisco IOS.
When you enter the ?, the Cisco IOS CLI reacts immediately; that is, you don’t need to press the Enter key or any other keys.|Когда вы вводите?, Интерфейс командной строки Cisco IOS реагирует немедленно; то есть вам не нужно нажимать клавишу Enter или какие-либо другие клавиши.
The device running Cisco IOS also redisplays what you entered before the ? to save you some keystrokes.|Устройство под управлением Cisco IOS также повторно отображает то, что вы ввели до? чтобы сэкономить несколько нажатий клавиш.
If you press Enter immediately after the ?, Cisco IOS tries to execute the command with only the parameters you have entered so far.|Если вы нажмете Enter сразу после?, Cisco IOS попытается выполнить команду только с теми параметрами, которые вы ввели до сих пор.
The information supplied by using help depends on the CLI mode.|Информация, предоставляемая с помощью справки, зависит от режима интерфейса командной строки.
For example, when ? is entered in user mode, the commands allowed in user mode are displayed, but commands available only in enable mode (not in user mode) are not displayed.|Например, когда? вводится в пользовательском режиме, отображаются команды, разрешенные в пользовательском режиме, но команды, доступные только в активном режиме (не в пользовательском режиме), не отображаются.
Also, help is available in configuration mode, which is the mode used to configure the switch.|Кроме того, справка доступна в режиме конфигурации, который используется для настройки коммутатора.
In fact, configuration mode has many different subconfiguration modes, as explained in the section “Configuration Submodes and Contexts,” later in this chapter.|Фактически, режим конфигурации имеет много различных режимов подконфигурации, как объясняется в разделе «Подрежимы и контексты конфигурации» далее в этой главе.
So, you can get help for the commands available in each configuration submode as well. (Note that this might be a good time to use the free Sim Lite product on the companion website—open any lab, use the question mark, and try some commands.)|Таким образом, вы также можете получить справку по командам, доступным в каждом подрежиме конфигурации. (Обратите внимание, что сейчас самое время использовать бесплатный продукт Sim Lite на сопутствующем веб-сайте - откройте любую лабораторию, используйте знак вопроса и попробуйте несколько команд.)
Cisco IOS stores the commands that you enter in a history buffer, storing ten commands by default.|Cisco IOS хранит команды, которые вы вводите, в буфере истории, по умолчанию сохраняя десять команд.
The CLI allows you to move backward and forward in the historical list of commands and then edit the command before reissuing it.|Интерфейс командной строки позволяет перемещаться вперед и назад по историческому списку команд, а затем редактировать команду перед ее повторным вводом.
These key sequences can help you use the CLI more quickly on the exams.|Эти последовательности клавиш могут помочь вам быстрее использовать интерфейс командной строки на экзаменах.
Table 4-3 lists the commands used to manipulate previously entered commands.|В таблице 4-3 перечислены команды, используемые для управления ранее введенными командами.
Table 4-3 Key Sequences for Command Edit and Recall Table end.|Таблица 4-3 Последовательности клавиш для редактирования команд и вызова таблицы конец.
#### The debug and show Commands
Команды debug и show   
__|__
--|--
By far, the single most popular Cisco IOS command is the show command.|Безусловно, самая популярная команда Cisco IOS - это команда show.
The show command has a large variety of options, and with those options, you can find the status of almost every feature of Cisco IOS. Essentially, the show command lists the currently known facts about the switch’s operational status.|Команда show имеет большое количество параметров, и с помощью этих параметров вы можете узнать состояние почти каждой функции Cisco IOS. По сути, команда show перечисляет известные на данный момент факты о рабочем состоянии коммутатора.
The only work the switch does in reaction to show commands is to find the current status and list the information in messages sent to the user.|Единственная работа, которую коммутатор выполняет в ответ на команды show, - это найти текущий статус и перечислить информацию в сообщениях, отправленных пользователю.
For example, consider the output from the show mac address-table dynamic command listed in Example 4-3.|Например, рассмотрим выходные данные динамической команды show mac address-table, перечисленные в Примере 4-3.
This show command, issued from user mode, lists the table the switch uses to make forwarding decisions.|Эта команда show, выданная из пользовательского режима, перечисляет таблицу, которую коммутатор использует для принятия решений о пересылке.
A switch’s MAC address table basically lists the data a switch uses to do its primary job.|Таблица MAC-адресов коммутатора в основном перечисляет данные, которые коммутатор использует для выполнения своей основной работы.
Example 4-3 Nondefault Basic Configuration Example end.|Пример 4-3 Пример базовой конфигурации не по умолчанию.
The debug command also tells the user details about the operation of the switch.|Команда отладки также сообщает пользователю подробную информацию о работе переключателя.
However, while the show command lists status information at one instant of time—more like a photograph—|Однако, хотя команда show выводит информацию о состоянии в один момент времени - больше похоже на фотографию -
the debug command acts more like a live video camera feed.|команда отладки больше похожа на прямую трансляцию с видеокамеры.
Once you issue a debug command, IOS remembers, issuing messages that any switch user can choose to see.|Когда вы вводите команду отладки, IOS запоминает, выдавая сообщения, которые может просмотреть любой пользователь коммутатора.
The console sees these messages by default.|Консоль видит эти сообщения по умолчанию.
Most of the commands used throughout this book to verify operation of switches and routers are show commands.|Большинство команд, используемых в этой книге для проверки работы коммутаторов и маршрутизаторов, являются командами show.
### Configuring Cisco IOS Software
Настройка программного обеспечения Cisco IOS   
__|__
--|--
You will want to configure every switch in an Enterprise network, even though the switches will forward traffic even with default configuration.|Вам нужно настроить каждый коммутатор в корпоративной сети, даже если коммутаторы будут пересылать трафик даже с конфигурацией по умолчанию.
This section covers the basic configuration processes, including the concept of a configuration file and the locations in which the configuration files can be stored.|В этом разделе рассматриваются основные процессы конфигурации, включая концепцию файла конфигурации и места, в которых файлы конфигурации могут храниться.
Although this section focuses on the configuration process, and not on the configuration commands themselves, you should know all the commands covered in this chapter for the exams, in addition to the configuration processes.|Хотя в этом разделе основное внимание уделяется процессу настройки, а не самим командам настройки, вы должны знать все команды, описанные в этой главе для экзаменов, в дополнение к процессам настройки.
Configuration mode is another mode for the Cisco CLI, similar to user mode and privileged mode.|Режим конфигурации - это еще один режим для интерфейса командной строки Cisco, аналогичный пользовательскому режиму и привилегированному режиму.
User mode lets you issue nondisruptive commands and displays some information.|Пользовательский режим позволяет выполнять команды без прерывания работы и отображать некоторую информацию.
Privileged mode supports a superset of commands compared to user mode, including commands that might disrupt switch operations.|Привилегированный режим поддерживает расширенный набор команд по сравнению с пользовательским режимом, включая команды, которые могут нарушить операции переключения.
However, not one of the commands in user or privileged mode changes the switch’s configuration.|Однако ни одна из команд в пользовательском или привилегированном режиме не изменяет конфигурацию коммутатора.
Configuration mode accepts configuration commands—commands that tell the switch the details of what to do and how to do it.|Режим настройки принимает команды настройки - команды, которые сообщают коммутатору подробную информацию о том, что делать и как это делать.
Figure 4-7 illustrates the relationships among configuration mode, user EXEC mode, and privileged EXEC mode.|На рис. 4-7 показаны отношения между режимом конфигурации, пользовательским режимом EXEC и привилегированным режимом EXEC.
Figure 4-7 CLI Configuration Mode Versus EXEC Modes Commands entered in configuration mode update the active configuration file.|Рис. 4-7 Сравнение режима конфигурации CLI и режимов EXEC. Команды, введенные в режиме конфигурации, обновляют активный файл конфигурации.
These changes to the configuration occur immediately each time you press the Enter key at the end of a command.|Эти изменения конфигурации происходят немедленно каждый раз, когда вы нажимаете клавишу Enter в конце команды.
Be careful when you enter a configuration command!|Будьте осторожны при вводе команды настройки!
#### Configuration Submodes and Contexts
Подрежимы и контексты конфигурации   
__|__
--|--
Configuration mode itself contains a multitude of commands.|Сам режим настройки содержит множество команд.
To help organize the configuration, IOS groups some kinds of configuration commands together.|Чтобы помочь организовать конфигурацию, IOS группирует некоторые виды команд конфигурации вместе.
To do that, when using configuration mode, you move from the initial mode—global configuration mode—into subcommand modes.|Для этого при использовании режима конфигурации вы переходите из начального режима - режима глобальной конфигурации - в режим подкоманд.
Context-setting commands move you from one configuration subcommand mode, or context, to another.|Команды настройки контекста переводят вас из одного режима подкоманд конфигурации или контекста в другой.
These context-setting commands tell the switch the topic about which you will enter the next few configuration commands.|Эти команды настройки контекста сообщают коммутатору тему, по которой вы будете вводить следующие несколько команд конфигурации.
More importantly, the context tells the switch the topic you care about right now, so when you use the ? to get help, the switch gives you help about that topic only.|Что еще более важно, контекст подсказывает переключателю, какая тема для вас сейчас важна, поэтому, когда вы используете? чтобы получить помощь, переключатель дает вам справку только по этой теме.
NOTE Context-setting is not a Cisco term.|ПРИМЕЧАНИЕ. Настройка контекста - это не термин Cisco.
It is just a description used here to help make sense of configuration mode.|Это просто описание, используемое здесь, чтобы помочь понять режим конфигурации.
The best way to learn about configuration submodes is to use them, but first, take a look at these upcoming examples.|Лучший способ узнать о подрежимах конфигурации - использовать их, но сначала взгляните на следующие примеры.
For instance, the interface command is one of the most commonly used context-setting configuration commands.|Например, команда интерфейса - одна из наиболее часто используемых команд настройки контекста.
For example, the CLI user could enter interface configuration mode by entering the interface FastEthernet 0/1 configuration command.|Например, пользователь CLI может войти в режим настройки интерфейса, введя команду настройки интерфейса FastEthernet 0/1.
Asking for help in interface configuration mode displays only commands that are useful when configuring Ethernet interfaces.|При запросе помощи в режиме настройки интерфейса отображаются только команды, которые полезны при настройке интерфейсов Ethernet.
Commands used in this context are called subcommands—|Команды, используемые в этом контексте, называются подкомандами -
or, in this specific case, interface subcommands.|или, в данном конкретном случае, подкоманды интерфейса.
When you begin practicing with the CLI with real equipment, the navigation between modes can become natural.|Когда вы начнете практиковаться с CLI на реальном оборудовании, переход между режимами станет естественным.
For now, consider Example 4-4, which shows the following:|А пока рассмотрим пример 4-4, который показывает следующее:
###### Movement from enable mode to global configuration mode by using the configure
Переход из режима включения в режим глобальной конфигурации с помощью команды configure   
__|__
--|--
terminal EXEC command|команда терминала EXEC
###### Using a hostname Fred global configuration command to configure the switch’s name
Использование команды глобальной конфигурации hostname Fred для настройки имени коммутатора   
###### Movement from global configuration mode to console line configuration mode (using the
Переход из режима глобальной настройки в режим настройки линии консоли (с помощью   
__|__
--|--
line console 0 command)|строка консоли 0 команда)
###### Setting the console’s simple password to hope (using the password hope line
Установка простого пароля консоли на надежду (с помощью строки пароля надежды   
__|__
--|--
subcommand)|подкоманда)
###### Movement from console configuration mode to interface configuration mode (using the
Переход из режима настройки консоли в режим настройки интерфейса (с помощью   
__|__
--|--
interface type number command)|команда номера типа интерфейса)
###### Setting the speed to 100 Mbps for interface Fa0/1 (using the speed 100 interface
Установка скорости на 100 Мбит / с для интерфейса Fa0 / 1 (при использовании интерфейса speed 100   
__|__
--|--
subcommand)|подкоманда)
###### Movement from interface configuration mode back to global configuration mode (using
Переход из режима конфигурации интерфейса обратно в режим глобальной конфигурации (с использованием   
__|__
--|--
the exit command)|команда выхода)
Example 4-4 Navigating Between Different Configuration Modes Example end.|Пример 4-4 Перемещение между различными режимами конфигурации Пример конец.
The text inside parentheses in the command prompt identifies the configuration mode.|Текст в круглых скобках в командной строке определяет режим конфигурации.
For example, the first command prompt after you enter configuration mode lists (config), meaning global configuration mode.|Например, первая командная строка после входа в режим конфигурации списки (config), что означает режим глобальной конфигурации.
After the line console 0 command, the text expands to (config-|После команды line console 0 текст расширяется до (config-
line), meaning line configuration mode.|line), что означает режим конфигурации линии.
Each time the command prompt changes within config mode, you have moved to another configuration mode.|Каждый раз, когда командная строка изменяется в режиме конфигурации, вы переходите в другой режим конфигурации.
Table 4-4 shows the most common command prompts in configuration mode, the names of those modes, and the context-setting commands used to reach those modes.|В таблице 4-4 показаны наиболее распространенные командные запросы в режиме конфигурации, названия этих режимов и команды настройки контекста, используемые для доступа к этим режимам.
Table 4-4 Common Switch Configuration Modes Table end.|Таблица 4-4 Общие режимы конфигурации коммутатора Конец таблицы.
You should practice until you become comfortable moving between the different configuration modes, back to enable mode, and then back into the configuration modes.|Вы должны практиковаться, пока не научитесь комфортно перемещаться между различными режимами конфигурации, обратно в режим включения, а затем обратно в режимы конфигурации.
However, you can learn these skills just doing labs about the topics in later chapters of the book.|Однако вы можете освоить эти навыки, просто выполняя лабораторные работы по темам из следующих глав книги.
For now, Figure 4-8 shows most of the navigation between global configuration mode and the four configuration submodes listed in Table 4-4.|На данный момент на рис. 4-8 показана большая часть навигации между режимом глобальной конфигурации и четырьмя подрежимами конфигурации, перечисленными в таблице 4-4.
NOTE You can also move directly from one configuration submode to another, without first using the exit command to move back to global configuration mode.|ПРИМЕЧАНИЕ. Вы также можете перейти непосредственно из одного подрежима конфигурации в другой, не используя предварительно команду выхода, чтобы вернуться в режим глобальной конфигурации.
Just use the commands listed in bold in the center of the figure.|Просто используйте команды, выделенные жирным шрифтом в центре рисунка.
Figure 4-8 Navigation In and Out of Switch Configuration Modes You really should stop and try navigating around these configuration modes.|Рис. 4-8. Переход в режимы конфигурации коммутатора и выход из него. Вам действительно следует остановиться и попробовать перемещаться по этим режимам конфигурации.
If you have not yet decided on a lab strategy, install the Pearson Sim Lite software from the companion website.|Если вы еще не определились с лабораторной стратегией, установите программное обеспечение Pearson Sim Lite с сопутствующего веб-сайта.
It includes the simulator and a couple of lab exercises.|Он включает тренажер и несколько лабораторных упражнений.
Start any lab, ignore the instructions, and just get into configuration mode and move around between the configuration modes shown in Figure 4-8.|Запустите любую лабораторную работу, игнорируйте инструкции и просто войдите в режим конфигурации и переходите между режимами конфигурации, показанными на рисунке 4-8.
No set rules exist for what commands are global commands or subcommands.|Не существует установленных правил для того, какие команды являются глобальными командами или подкомандами.
Generally, however, when multiple instances of a parameter can be set in a single switch, the command used to set the parameter is likely a configuration subcommand.|Как правило, однако, когда несколько экземпляров параметра могут быть установлены в одном переключателе, команда, используемая для установки параметра, скорее всего, является подкомандой конфигурации.
Items that are set once for the entire switch are likely global commands.|Элементы, которые устанавливаются один раз для всего коммутатора, скорее всего, являются глобальными командами.
For example, the hostname command is a global command because there is only one hostname per switch.|Например, команда hostname является глобальной командой, потому что для каждого коммутатора существует только одно имя хоста.
Conversely, the speed command is an interface subcommand that applies to each switch interface that can run at different speeds, so it is a subcommand, applying to the particular interface under which it is configured.|И наоборот, команда скорости - это подкоманда интерфейса, которая применяется к каждому интерфейсу коммутатора, который может работать на разных скоростях, поэтому это подкоманда, применяемая к конкретному интерфейсу, для которого она настроена.
#### Storing Switch Configuration Files
Хранение файлов конфигурации коммутатора   
__|__
--|--
When you configure a switch, it needs to use the configuration.|Когда вы настраиваете коммутатор, он должен использовать эту конфигурацию.
It also needs to be able to retain the configuration in case the switch loses power.|Он также должен иметь возможность сохранять конфигурацию в случае отключения питания коммутатора.
Cisco switches contain randomaccess memory (RAM) to store data while Cisco IOS is using it, but RAM loses its contents when the switch loses power or is reloaded.|Коммутаторы Cisco содержат оперативную память (RAM) для хранения данных, пока ее использует Cisco IOS, но RAM теряет свое содержимое, когда коммутатор теряет питание или перезагружается.
To store information that must be retained when the switch loses power or is reloaded, Cisco switches use several types of more permanent memory, none of which has any moving parts.|Для хранения информации, которую необходимо сохранить, когда коммутатор теряет питание или перезагружается, коммутаторы Cisco используют несколько типов более постоянной памяти, ни одна из которых не имеет движущихся частей.
By avoiding components with moving parts (such as traditional disk drives), switches can maintain better uptime and availability.|Избегая компонентов с движущимися частями (таких как традиционные дисковые накопители), коммутаторы могут поддерживать время безотказной работы и доступность.
The following list details the four main types of memory found in Cisco switches, as well as the most common use of each type:|В следующем списке подробно описаны четыре основных типа памяти в коммутаторах Cisco, а также наиболее распространенное использование каждого типа:
###### RAM: Sometimes called DRAM, for dynamic random-access memory, RAM is used
RAM: иногда называется DRAM, для динамической памяти с произвольным доступом используется RAM   
__|__
--|--
by the switch just as it is used by any other computer: for working storage.|переключателем, как и на любом другом компьютере: для рабочей памяти.
The running (active) configuration file is stored here.|Здесь хранится текущий (активный) файл конфигурации.
###### Flash memory: Either a chip inside the switch or a removable memory card, flash memory
Флэш-память: либо микросхема внутри коммутатора, либо съемная карта памяти, флэш-память.   
__|__
--|--
stores fully functional Cisco IOS images and is the default location where the switch gets its Cisco IOS at boot time.|хранит полнофункциональные образы Cisco IOS и является местом по умолчанию, куда коммутатор получает Cisco IOS во время загрузки.
Flash memory also can be used to store any other files, including backup copies of configuration files.|Флэш-память также может использоваться для хранения любых других файлов, включая резервные копии файлов конфигурации.
###### ROM: Read-only memory (ROM) stores a bootstrap (or boothelper) program that is loaded
ПЗУ: постоянное запоминающее устройство (ПЗУ) хранит загруженную программу начальной загрузки (или загрузчика).   
__|__
--|--
when the switch first powers on.|при первом включении переключателя.
This bootstrap program then finds the full Cisco IOS image and manages the process of loading Cisco IOS into RAM, at which point Cisco IOS takes over operation of the switch.|Затем эта программа начальной загрузки находит полный образ Cisco IOS и управляет процессом загрузки Cisco IOS в RAM, после чего Cisco IOS берет на себя работу коммутатора.
###### NVRAM: Nonvolatile RAM (NVRAM) stores the initial or startup configuration file that
NVRAM: энергонезависимая RAM (NVRAM) хранит файл начальной или начальной конфигурации, который   
__|__
--|--
is used when the switch is first powered on and when the switch is reloaded.|используется при первом включении коммутатора и при повторной загрузке коммутатора.
Figure 4-9 summarizes this same information in a briefer and more convenient form for memorization and study.|На рис. 4-9 эта же информация суммирована в более краткой и удобной форме для запоминания и изучения.
Figure 4-9 Cisco Switch Memory Types Cisco IOS stores the collection of configuration commands in a configuration file.|Рис. 4-9 Типы памяти коммутатора Cisco Cisco IOS хранит набор команд конфигурации в файле конфигурации.
In fact, switches use multiple configuration files—one file for the initial configuration used when powering on, and another configuration file for the active, currently used running configuration as stored in RAM. Table 4-5 lists the names of these two files, their purpose, and their storage location.|Фактически, коммутаторы используют несколько файлов конфигурации - один файл для начальной конфигурации, используемой при включении, и другой файл конфигурации для активной, используемой в настоящее время рабочей конфигурации, хранящейся в ОЗУ. В Таблице 4-5 перечислены имена этих двух файлов, их назначение и место хранения.
Table 4-5 Names and Purposes of the Two Main Cisco IOS Configuration Files Table end.|Таблица 4-5 Имена и назначение двух основных файлов конфигурации Cisco IOS Конец таблицы.
Essentially, when you use configuration mode, you change only the running-config file.|По сути, когда вы используете режим конфигурации, вы изменяете только файл рабочей конфигурации.
This means that the configuration example earlier in this chapter (Example 4-4) updates only the running-config file.|Это означает, что в примере конфигурации ранее в этой главе (Пример 4-4) обновляется только файл рабочей конфигурации.
However, if the switch lost power right after that example, all that configuration would be lost.|Однако, если коммутатор потеряет питание сразу после этого примера, вся эта конфигурация будет потеряна.
If you want to keep that configuration, you have to copy the running-config file into NVRAM, overwriting the old startup-config file.|Если вы хотите сохранить эту конфигурацию, вам необходимо скопировать файл рабочей конфигурации в NVRAM, перезаписав старый файл начальной конфигурации.
Example 4-5 demonstrates that commands used in configuration mode change only the running configuration in RAM. The example shows the following concepts and steps:|Пример 4-5 демонстрирует, что команды, используемые в режиме конфигурации, изменяют только текущую конфигурацию в ОЗУ. В примере показаны следующие концепции и шаги:
Step 1.|Шаг 1.
The example begins with both the running and startup-config having the same hostname, per the hostname hannah command.|Пример начинается с того, что как запущенная, так и конфигурация запуска имеют одно и то же имя хоста в соответствии с командой hostname hannah.
Step 2.|Шаг 2.
The hostname is changed in configuration mode using the hostname harold command.|Имя хоста изменяется в режиме конфигурации с помощью команды hostname harold.
Step 3.|Шаг 3.
The show running-config and show startup-config commands show the fact that the hostnames are now different, with the hostname harold command found only in the running-config.|Команды show running-config и show startup-config показывают тот факт, что имена хостов теперь разные, а команда harold hostname находится только в файле running-config.
Example 4-5 How Configuration Mode Commands Change the Running-Config File, Example end.|Пример 4-5. Как команды режима конфигурации изменяют файл рабочей конфигурации, пример end.
#### Copying and Erasing Configuration Files
Копирование и стирание файлов конфигурации   
__|__
--|--
The configuration process updates the running-config file, which is lost if the router loses power or is reloaded.|В процессе настройки обновляется файл рабочей конфигурации, который теряется, если маршрутизатор теряет питание или перезагружается.
Clearly, IOS needs to provide us a way to copy the running configuration so that it will not be lost, so it will be used the next time the switch reloads or powers on.|Ясно, что IOS должна предоставить нам возможность скопировать текущую конфигурацию, чтобы она не была потеряна и использовалась при следующей перезагрузке или включении коммутатора.
For instance, Example 4-5 ended with a different running configuration (with the hostname harold command) versus the startup configuration.|Например, пример 4-5 завершился другой рабочей конфигурацией (с командой harold имени хоста) по сравнению с конфигурацией запуска.
In short, the EXEC command copy running-config startup-config backs up the runningconfig to the startup-config file.|Короче говоря, команда EXEC copy running-config startup-config создает резервную копию файла runningconfig в файле конфигурации запуска.
This command overwrites the current startup-config file with what is currently in the running-configuration file.|Эта команда перезаписывает текущий файл начальной конфигурации тем, что находится в текущем файле конфигурации.
In addition, in the lab, you may want to just get rid of all existing configuration and start over with a clean configuration.|Кроме того, в лабораторной работе вы можете просто избавиться от всей существующей конфигурации и начать заново с чистой конфигурации.
To do that, you can erase the startup-config file using three different commands:|Для этого вы можете стереть файл начальной конфигурации, используя три разные команды:
write erase erase startup-config erase nvram:|записать стереть стереть start-config стереть nvram:
Once the startup-config file is erased, you can reload or power off/on the switch, and it will boot with the now-empty startup configuration.|После стирания файла начальной конфигурации вы можете перезагрузить или выключить / включить коммутатор, и он загрузится с пустой загрузочной конфигурацией.
Note that Cisco IOS does not have a command that erases the contents of the runningconfig file.|Обратите внимание, что в Cisco IOS нет команды, стирающей содержимое файла runningconfig.
To clear out the running-config file, simply erase the startup-config file, and then reload the switch, and the running-config will be empty at the end of the process.|Чтобы очистить файл рабочей конфигурации, просто сотрите файл конфигурации запуска, а затем перезагрузите коммутатор, и в конце процесса рабочая конфигурация будет пустой.
NOTE Cisco uses the term reload to refer to what most PC operating systems call rebooting or restarting.|ПРИМЕЧАНИЕ Cisco использует термин перезагрузка для обозначения того, что большинство операционных систем ПК называют перезагрузкой или перезапуском.
In each case, it is a re-initialization of the software.|В каждом случае это повторная инициализация программного обеспечения.
The reload EXEC command causes a switch to reload.|Команда reload EXEC вызывает перезагрузку коммутатора.
### Chapter Review
Обзор главы   
__|__
--|--
One key to doing well on the exams is to perform repetitive spaced review sessions.|Один из ключей к успешной сдаче экзаменов - повторение повторных сессий с интервалом.
Review this chapter’s material using either the tools in the book or on the book’s companion website.|Просмотрите материал этой главы, используя инструменты в книге или на сопутствующем веб-сайте книги.
Refer to the “Your Study Plan” element section titled “Step 2: Build Your Study Habits Around the Chapter” for more details.|Обратитесь к разделу элемента «Ваш учебный план», озаглавленному «Шаг 2: выработайте учебу вокруг главы» для получения более подробной информации.
Table 4-6 outlines the key review elements and where you can find them.|В Таблице 4-6 представлены ключевые элементы обзора и их местонахождение.
To better track your study progress, record when you completed these activities in the second column.|Чтобы лучше отслеживать свои успехи в учебе, отметьте, когда вы выполнили эти задания, во втором столбце.
Table 4-6 Chapter Review Tracking Table end.|Таблица 4-6 Окончание таблицы отслеживания обзора главы.
Review All the Key Topics Key Terms You Should Know command-line interface (CLI), Telnet, Secure Shell (SSH), enable mode, user mode, configuration mode, startup-config file, running-config file Command References Tables 4-8 and 4-9 list configuration and verification commands used in this chapter, respectively.|Ознакомьтесь со всеми ключевыми темами. Ключевые термины, которые вы должны знать интерфейс командной строки (CLI), Telnet, Secure Shell (SSH), режим включения, пользовательский режим, режим конфигурации, файл конфигурации запуска, файл рабочей конфигурации Ссылки на команды Таблицы 4-8 и 4-9 перечисляют команды настройки и проверки, используемые в этой главе, соответственно.
As an easy review exercise, cover the left column in a table, read the right column, and try to recall the command without looking.|В качестве простого упражнения на повторение закройте левый столбец таблицы, прочтите правый столбец и попытайтесь вспомнить команду, не глядя.
Then repeat the exercise, covering the right column, and try to recall what the command does.|Затем повторите упражнение, охватывая правый столбец, и попытайтесь вспомнить, что делает команда.
Table 4-8 Chapter 4 Configuration Commands Table end.|Таблица 4-8 Глава 4 Команды конфигурации Конец таблицы.
Table 4-9 Chapter 4 EXEC Command Reference Table end.|Таблица 4-9 Глава 4 Справочник команд EXEC Конец таблицы.
## Chapter 5 Analyzing Ethernet LAN Switching
Глава 5 Анализ коммутации Ethernet LAN   
__|__
--|--
This chapter covers the following exam topics:|В этой главе рассматриваются следующие экзаменационные темы:
###### 1.0 Network Fundamentals
1.0 Основы сети   
###### 1.1 Explain the role and function of network components
1.1 Объясните роль и функции сетевых компонентов   
###### 1.1.b L2 and L3 Switches
1.1.b Коммутаторы L2 и L3   
###### 1.13 Describe switching concepts
1.13 Описание концепций переключения   
###### 1.13.a MAC learning and aging
1.13.a Изучение MAC и старение   
###### 1.13.b Frame switching
1.13.b Переключение кадров   
###### 1.13.c Frame flooding
1.13.c Фрейм флуд   
###### 1.13.d MAC address table
1.13.d Таблица MAC-адресов   
###### 2.0 Network Access
2.0 Доступ к сети   
###### 2.5 Describe the need for and basic operations of Rapid PVST+ Spanning Tree Protocol
2.5. Опишите необходимость и основные операции Rapid PVST + Spanning Tree Protocol.   
__|__
--|--
and identify basic operations When you buy a Cisco Catalyst Ethernet switch, the switch is ready to work.|и определение основных операций. Когда вы покупаете коммутатор Cisco Catalyst Ethernet, он готов к работе.
All you have to do is take it out of the box, power on the switch by connecting the power cable to the switch and a power outlet, and connect hosts to the switch using the correct unshielded twisted-pair (UTP) cables.|Все, что вам нужно сделать, это вынуть его из коробки, включить коммутатор, подключив кабель питания к коммутатору и розетке питания, и подключить хосты к коммутатору с помощью правильных кабелей неэкранированной витой пары (UTP).
You do not have to configure anything else, or connect to the console and login, or do anything: the switch just starts forwarding Ethernet frames.|Вам не нужно ничего настраивать, подключаться к консоли и входить в систему, или что-то делать: коммутатор просто начинает пересылку кадров Ethernet.
In Part II of this book, you will learn how to build, configure, and verify the operation of Ethernet LANs. In Chapter 4, “Using the Command-Line Interface,” you learned how to move around in the CLI, issue commands, and configure the switch.|В части II этой книги вы узнаете, как создавать, настраивать и проверять работу локальных сетей Ethernet. В главе 4 «Использование интерфейса командной строки» вы узнали, как перемещаться по интерфейсу командной строки, вводить команды и настраивать коммутатор.
This chapter takes a short but important step in that journey by explaining the logic a switch uses when forwarding Ethernet frames.|В этой главе делается короткий, но важный шаг на этом пути, объясняется логика, которую коммутатор использует при пересылке кадров Ethernet.
This chapter breaks the content into two major sections.|В этой главе содержание разбито на два основных раздела.
The first reviews and then further develops the concepts behind LAN switching, which were first introduced back in Chapter 2, “Fundamentals of Ethernet LANs.” The second section then uses IOS show commands to verify that Cisco switches actually learned the MAC addresses, built the MAC address table, and forwarded frames.|В первом обзоре, а затем дальнейшее развитие концепций коммутации LAN, которые были впервые представлены еще в главе 2 «Основы сетей Ethernet». Затем во втором разделе используются команды show IOS для проверки того, что коммутаторы Cisco действительно узнали MAC-адреса, создали таблицу MAC-адресов и пересылали кадры.
### “Do I Know This Already?” Quiz
«Знаю ли я это уже?» Викторина   
__|__
--|--
Take the quiz (either here or use the PTP software) if you want to use the score to help you decide how much time to spend on this chapter.|Пройдите тест (здесь или воспользуйтесь программой PTP), если вы хотите использовать оценку, чтобы решить, сколько времени потратить на эту главу.
The letter answers are listed at the bottom of the page following the quiz.|Ответы на письма перечислены внизу страницы после викторины.
Appendix C, found both at the end of the book as well as on the companion website, includes both the answers and explanations.|Приложение C, которое можно найти как в конце книги, так и на сопутствующем веб-сайте, включает как ответы, так и пояснения.
You can also find both answers and explanations in the PTP testing software.|Вы также можете найти ответы и пояснения в программе тестирования PTP.
CHAPTER 5 Table 5-1 “Do I Know This Already?” Foundation Topics Section-to-Question Mapping|ГЛАВА 5 Таблица 5-1 «Знаю ли я это уже?» Сопоставление разделов с вопросами по основным темам
### Foundation Topics
Основные темы   
### LAN Switching Concepts
Концепции коммутации LAN   
__|__
--|--
Verifying and Analyzing Ethernet Switching 5–6 1.|Проверка и анализ коммутации Ethernet 5–6 1.
Which of the following statements describes part of the process of how a switch decides to forward a frame destined for a known unicast MAC address?|Какое из следующих утверждений описывает часть процесса принятия коммутатором решения о пересылке кадра, предназначенного для известного одноадресного MAC-адреса?
a. It compares the unicast destination address to the bridging, or MAC address, table.|а. Он сравнивает адрес назначения одноадресной рассылки с таблицей мостовых или MAC-адресов.
b. It compares the unicast source address to the bridging, or MAC address, table.|б. Он сравнивает адрес источника одноадресной передачи с таблицей мостовых или MAC-адресов.
c. It forwards the frame out all interfaces in the same VLAN except for the incoming interface.|c. Он пересылает кадр на все интерфейсы в той же VLAN, за исключением входящего интерфейса.
d. It compares the destination IP address to the destination MAC address.|d. Он сравнивает IP-адрес назначения с MAC-адресом назначения.
e. It compares the frame’s incoming interface to the source MAC entry in the MAC address table.|е. Он сравнивает входящий интерфейс кадра с записью MAC-адреса источника в таблице MAC-адресов.
2. Which of the following statements describes part of the process of how a LAN switch decides to forward a frame destined for a broadcast MAC address?|2. Какое из следующих утверждений описывает часть процесса принятия коммутатором локальной сети решения о пересылке кадра, предназначенного для широковещательного MAC-адреса?
a. It compares the unicast destination address to the bridging, or MAC address, table.|а. Он сравнивает адрес назначения одноадресной рассылки с таблицей мостовых или MAC-адресов.
b. It compares the unicast source address to the bridging, or MAC address, table.|б. Он сравнивает адрес источника одноадресной передачи с таблицей мостовых или MAC-адресов.
c. It forwards the frame out all interfaces in the same VLAN except for the incoming interface.|c. Он пересылает кадр на все интерфейсы в той же VLAN, за исключением входящего интерфейса.
d. It compares the destination IP address to the destination MAC address.|d. Он сравнивает IP-адрес назначения с MAC-адресом назначения.
e. It compares the frame’s incoming interface to the source MAC entry in the MAC address table.|е. Он сравнивает входящий интерфейс кадра с записью MAC-адреса источника в таблице MAC-адресов.
3. Which of the following statements best describes what a switch does with a frame destined for an unknown unicast address?|3. Какое из следующих утверждений лучше всего описывает, что коммутатор делает с кадром, предназначенным для неизвестного одноадресного адреса?
a. It forwards out all interfaces in the same VLAN except for the incoming interface.|а. Он перенаправляет все интерфейсы в той же VLAN, за исключением входящего интерфейса.
b. It forwards the frame out the one interface identified by the matching entry in the MAC address table.|б. Он пересылает кадр через один интерфейс, идентифицированный соответствующей записью в таблице MAC-адресов.
c. It compares the destination IP address to the destination MAC address.|c. Он сравнивает IP-адрес назначения с MAC-адресом назначения.
d. It compares the frame’s incoming interface to the source MAC entry in the MAC address table.|d. Он сравнивает входящий интерфейс кадра с записью MAC-адреса источника в таблице MAC-адресов.
4. Which of the following comparisons does a switch make when deciding whether a new MAC address should be added to its MAC address table?|4. Какое из следующих сравнений делает коммутатор при принятии решения о добавлении нового MAC-адреса в его таблицу MAC-адресов?
a. It compares the unicast destination address to the bridging, or MAC address, table.|а. Он сравнивает адрес назначения одноадресной рассылки с таблицей мостовых или MAC-адресов.
b. It compares the unicast source address to the bridging, or MAC address, table.|б. Он сравнивает адрес источника одноадресной передачи с таблицей мостовых или MAC-адресов.
c. It compares the VLAN ID to the bridging, or MAC address, table.|c. Он сравнивает идентификатор VLAN с таблицей моста или MAC-адресов.
d. It compares the destination IP address’s ARP cache entry to the bridging, or MAC address, table.|d. Он сравнивает запись кэша ARP IP-адреса назначения с таблицей мостовых или MAC-адресов.
5. A Cisco Catalyst switch has 24 10/100 ports, numbered 0/1 through 0/24.|5. Коммутатор Cisco Catalyst имеет 24 порта 10/100, пронумерованных от 0/1 до 0/24.
Ten PCs connect to the 10 lowest numbered ports, with those PCs working and sending data over the network.|Десять компьютеров подключаются к 10 портам с наименьшими номерами, и эти компьютеры работают и отправляют данные по сети.
The other ports are not connected to any device.|Остальные порты не подключены ни к какому устройству.
Which of the following answers lists facts displayed by the show interfaces status command?|В каком из следующих ответов перечислены факты, отображаемые командой show interfaces status?
a. Port Ethernet 0/1 is in a connected state.|а. Порт Ethernet 0/1 находится в подключенном состоянии.
b. Port Fast Ethernet 0/11 is in a connected state.|б. Порт Fast Ethernet 0/11 находится в подключенном состоянии.
c. Port Fast Ethernet 0/5 is in a connected state.|c. Порт Fast Ethernet 0/5 находится в подключенном состоянии.
d. Port Ethernet 0/15 is in a notconnected state.|d. Порт Ethernet 0/15 находится в неподключенном состоянии.
6. Consider the following output from a Cisco Catalyst switch:|6. Рассмотрим следующие выходные данные коммутатора Cisco Catalyst:
SW1# show mac address-table dynamic Mac Address Table|SW1 # показать таблицу MAC-адресов динамическую таблицу Mac-адресов
------------------------------------------- 
Порты типа Vlan Mac-адреса   
__|__
--|--
Vlan Mac Address Type Ports---- ----------- -------- -----
----------- -------- -----   
__|__
--|--
1 02AA.AAAA.AAAA DYNAMIC Gi0/1 1 02BB.BBBB.BBBB DYNAMIC Gi0/2 1 02CC.CCCC.CCCC DYNAMIC Gi0/3 Total Mac Addresses for this criterion: 3 Which of the following answers is true about this switch?|1 02AA.AAAA.AAAA DYNAMIC Gi0 / 1 1 02BB.BBBB.BBBB DYNAMIC Gi0 / 2 1 02CC.CCCC.CCCC DYNAMIC Gi0 / 3 Общее количество Mac-адресов для этого критерия: 3 Какой из следующих ответов верен об этом переключателе?
a. The output proves that port Gi0/2 connects directly to a device that uses address 02BB.BBBB.BBBB.|а. Выходные данные подтверждают, что порт Gi0 / 2 напрямую подключается к устройству, которое использует адрес 02BB.BBBB.BBBB.
b. The switch has learned three MAC addresses since the switch powered on.|б. Коммутатор запомнил три MAC-адреса с момента включения коммутатора.
c. The three listed MAC addresses were learned based on the destination MAC address of frames forwarded by the switch.|c. Три перечисленных MAC-адреса были изучены на основе MAC-адреса назначения кадров, пересылаемых коммутатором.
d. 02CC.CCCC.CCCC was learned from the source MAC address of a frame that entered port Gi0/3.|d. 02CC.CCCC.CCCC был получен из MAC-адреса источника кадра, поступившего в порт Gi0 / 3.
Foundation Topics LAN Switching Concepts A modern Ethernet LAN connects user devices as well as servers into some switches, with the switches then connecting to each other, sometimes in a design like Figure 5-1.|Основные темы Концепции коммутации LAN Современная локальная сеть Ethernet соединяет пользовательские устройства, а также серверы в некоторые коммутаторы, при этом коммутаторы затем подключаются друг к другу, иногда в конструкции, подобной рис.
Part of the LAN, called a campus LAN, supports the end-user population as shown on the left of the figure.|Часть LAN, называемая LAN кампуса, поддерживает конечных пользователей, как показано на рисунке слева.
End-user devices connect to LAN switches, which in turn connect to other switches so that a path exists to the rest of the network.|Устройства конечных пользователей подключаются к коммутаторам LAN, которые, в свою очередь, подключаются к другим коммутаторам, так что существует путь к остальной части сети.
The campus LAN switches sit in wiring closets close to the end users.|Коммутаторы локальной сети кампуса располагаются в коммутационных шкафах рядом с конечными пользователями.
On the right, the servers used to provide information to the users also connect to the LAN. Those servers and switches often sit in a closed room called a data center, with connections to the campus LAN to support traffic to/from the users.|Справа серверы, используемые для предоставления информации пользователям, также подключаются к локальной сети. Эти серверы и коммутаторы часто находятся в закрытом помещении, называемом центром обработки данных, с подключениями к локальной сети кампуса для поддержки трафика к / от пользователей.
To forward traffic from a user device to a server and back, each switch performs the same kind of logic, independently from each other.|Для пересылки трафика с пользовательского устройства на сервер и обратно каждый коммутатор выполняет одну и ту же логику независимо друг от друга.
The first half of this chapter examines the logic: how a switch chooses to forward an Ethernet frame, when the switch chooses to not forward the frame, and so on.|В первой половине этой главы исследуется логика: как коммутатор выбирает пересылку кадра Ethernet, когда коммутатор предпочитает не пересылать кадр и т. Д.
Figure 5-1 Campus LAN and Data Center LAN, Conceptual Drawing|Рисунок 5-1 ЛВС кампуса и ЛВС центра обработки данных, концептуальный чертеж
#### Overview of Switching Logic
Обзор логики переключения   
__|__
--|--
Ultimately, the role of a LAN switch is to forward Ethernet frames.|В конечном счете, роль коммутатора LAN заключается в пересылке кадров Ethernet.
LANs exist as a set of user devices, servers, and other devices that connect to switches, with the switches connected to each other.|ЛВС существуют как набор пользовательских устройств, серверов и других устройств, которые подключаются к коммутаторам, причем коммутаторы подключены друг к другу.
The LAN switch has one primary job: to forward frames to the correct destination (MAC) address.|Коммутатор LAN выполняет одну основную задачу: пересылать кадры на правильный адрес назначения (MAC).
And to achieve that goal, switches use logic—logic based on the source and destination MAC address in each frame’s Ethernet header.|И для достижения этой цели коммутаторы используют логику - логику, основанную на MAC-адресах источника и назначения в заголовке Ethernet каждого кадра.
LAN switches receive Ethernet frames and then make a switching decision: either forward the frame out some other ports or ignore the frame.|Коммутаторы LAN получают кадры Ethernet, а затем принимают решение о коммутации: либо перенаправить кадр на другие порты, либо игнорировать кадр.
To accomplish this primary mission, switches perform three actions:|Для выполнения этой основной задачи коммутаторы выполняют три действия:
1. Deciding when to forward a frame or when to filter (not forward) a frame, based on the destination MAC address 2.|1. Решение, когда пересылать кадр или когда фильтровать (не пересылать) кадр, на основе MAC-адреса назначения 2.
Preparing to forward frames by learning MAC addresses by examining the source MAC address of each frame received by the switch 3.|Подготовка к пересылке кадров путем изучения MAC-адресов путем изучения исходного MAC-адреса каждого кадра, полученного коммутатором 3.
Preparing to forward only one copy of the frame to the destination by creating a (Layer 2) loop-free environment with other switches by using Spanning Tree Protocol (STP)|Подготовка к пересылке только одной копии кадра в пункт назначения путем создания среды (уровня 2) без петель с другими коммутаторами с использованием протокола связующего дерева (STP)
The first action is the switch’s primary job, whereas the other two items are overhead functions.|Первое действие - это основная задача коммутатора, а два других элемента - служебные.
NOTE Throughout this book’s discussion of LAN switches, the terms switch port and switch interface are synonymous.|ПРИМЕЧАНИЕ. В этой книге, посвященной коммутаторам LAN, термины "порт коммутатора" и "интерфейс коммутатора" являются синонимами.
Although Chapter 2’s section titled “Ethernet Data-Link Protocols” already discussed the frame format, this discussion of Ethernet switching is pretty important, so reviewing the Ethernet frame at this point might be helpful.|Хотя в разделе главы 2, озаглавленном «Протоколы канала передачи данных Ethernet», уже обсуждался формат кадра, это обсуждение коммутации Ethernet очень важно, поэтому рассмотрение кадра Ethernet на этом этапе может оказаться полезным.
Figure 5-2 shows one popular format for an Ethernet frame.|На рис. 5-2 показан один из популярных форматов кадра Ethernet.
Basically, a switch would take the frame shown in the figure, make a decision of where to forward the frame, and send the frame out that other interface.|По сути, коммутатор берет кадр, показанный на рисунке, принимает решение о том, куда пересылать кадр, и отправляет его через этот другой интерфейс.
Figure 5-2 IEEE 802.3 Ethernet Frame (One Variation)|Рисунок 5-2 Кадр Ethernet IEEE 802.3 (один вариант)
Most of the upcoming discussions and figures about Ethernet switching focus on the use of the destination and source MAC address fields in the header.|Большинство предстоящих обсуждений и цифр о коммутации Ethernet сосредоточены на использовании полей MAC-адреса назначения и источника в заголовке.
All Ethernet frames have both a destination and source MAC address.|Все кадры Ethernet имеют MAC-адрес назначения и источника.
Both are 6-bytes long (represented as 12 hex digits in the book) and are a key part of the switching logic discussed in this section.|Оба имеют длину 6 байтов (в книге представлены 12 шестнадцатеричными цифрами) и являются ключевой частью логики переключения, обсуждаемой в этом разделе.
Refer back to Chapter 2’s discussion of the header in detail for more info on the rest of the Ethernet frame.|Вернитесь к подробному обсуждению заголовка в главе 2 для получения дополнительной информации об остальной части кадра Ethernet.
NOTE The companion website includes a video that explains the basics of Ethernet switching.|ПРИМЕЧАНИЕ На сопутствующем веб-сайте есть видео, в котором объясняются основы коммутации Ethernet.
Now on to the details of how Ethernet switching works!|А теперь подробнее о том, как работает коммутация Ethernet!
#### Forwarding Known Unicast Frames
Пересылка известных одноадресных кадров   
__|__
--|--
To decide whether to forward a frame, a switch uses a dynamically built table that lists MAC addresses and outgoing interfaces.|Чтобы решить, следует ли пересылать кадр, коммутатор использует динамически построенную таблицу, в которой перечислены MAC-адреса и исходящие интерфейсы.
Switches compare the frame’s destination MAC address to this table to decide whether the switch should forward a frame or simply ignore it.|Коммутаторы сравнивают MAC-адрес назначения кадра с этой таблицей, чтобы решить, должен ли коммутатор пересылать кадр или просто игнорировать его.
For example, consider the simple network shown in Figure 5-3, with Fred sending a frame to Barney.|Например, рассмотрим простую сеть, показанную на рисунке 5-3, в которой Фред отправляет кадр Барни.
In this figure, Fred sends a frame with destination address 0200.2222.2222 (Barney’s MAC address).|На этом рисунке Фред отправляет кадр с адресом назначения 0200.2222.2222 (MAC-адрес Барни).
The switch compares the destination MAC address (0200.2222.2222) to the MAC address table, matching the bold table entry.|Коммутатор сравнивает MAC-адрес назначения (0200.2222.2222) с таблицей MAC-адресов, соответствующей записи в таблице, выделенной жирным шрифтом.
That matched table entry tells the switch to forward the frame out port F0/2, and only port F0/2.|Эта совпадающая запись в таблице сообщает коммутатору, что нужно перенаправить порт вывода кадра F0 / 2 и только порт F0 / 2.
Answers to the “Do I Know This Already?” quiz:|Ответы на вопрос «Знаю ли я это уже?» викторина:
1 A 2 C 3 A 4 B 5 C 6 D NOTE A switch’s MAC address table is also called the switching table, or bridging table, or even the Content-Addressable Memory (CAM) table, in reference to the type of physical memory used to store the table.|1 A 2 C 3 A 4 B 5 C 6 D ПРИМЕЧАНИЕ Таблица MAC-адресов коммутатора также называется таблицей коммутации, таблицей мостов или даже таблицей адресуемой памяти (CAM) в зависимости от типа используемой физической памяти. для хранения таблицы.
Figure 5-3 Sample Switch Forwarding and Filtering Decision A switch’s MAC address table lists the location of each MAC relative to that one switch.|Рисунок 5-3 Пример решения о пересылке и фильтрации коммутатора В таблице MAC-адресов коммутатора указано расположение каждого MAC-адреса относительно этого коммутатора.
In LANs with multiple switches, each switch makes an independent forwarding decision based on its own MAC address table.|В локальных сетях с несколькими коммутаторами каждый коммутатор принимает независимое решение о пересылке на основе своей собственной таблицы MAC-адресов.
Together, they forward the frame so that it eventually arrives at the destination.|Вместе они пересылают кадр, чтобы он в конечном итоге прибыл в пункт назначения.
For example, Figure 5-4 shows the first switching decision in a case in which Fred sends a frame to Wilma, with destination MAC 0200.3333.3333.|Например, на рис. 5-4 показано первое решение о переключении в случае, когда Фред отправляет кадр в Wilma с MAC-адресом назначения 0200.3333.3333.
The topology has changed versus the previous figure, this time with two switches, and Fred and Wilma connected to two different switches.|Топология изменилась по сравнению с предыдущим рисунком, на этот раз с двумя коммутаторами, а Фред и Вильма подключены к двум разным коммутаторам.
Figure 5-3 shows the first switch’s logic, in reaction to Fred sending the original frame.|На рис. 5-3 показана логика первого переключателя в ответ на отправку Фредом исходного кадра.
Basically, the switch receives the frame in port F0/1, finds the destination MAC (0200.3333.3333) in the MAC address table, sees the outgoing port of G0/1, so SW1 forwards the frame out its G0/1 port.|По сути, коммутатор получает кадр в порту F0 / 1, находит MAC-адрес назначения (0200.3333.3333) в таблице MAC-адресов, видит исходящий порт G0 / 1, поэтому SW1 пересылает кадр на свой порт G0 / 1.
F0/2 Fred Barney 0200.2222.2222 F0/1 Dest 0200.2222.2222 G0/1 F0/4 F0/3 Wilma 0200.3333.3333 Betty 0200.4444.4444 MAC Address F0/1 F0/2 G0/1 G0/1 0200.1111.1111 0200.2222.2222 0200.3333.3333 0200.4444.4444 Output SW1 Address Table MAC Address G0/2 G0/2 F0/3 F0/4 0200.1111.1111 0200.2222.2222 0200.3333.3333 0200.4444.4444 Output SW2 Address Table G0/2 1) Frame Entered F0/1...|F0 / 2 Fred Barney 0200.2222.2222 F0 / 1 Dest 0200.2222.2222 G0 / 1 F0 / 4 F0 / 3 Wilma 0200.3333.3333 Betty 0200.4444.4444 MAC-адрес F0 / 1 F0 / 2 G0 / 1 G0 / 1 0200.1111.1111 0200.2222 .2222 0200.3333.3333 0200.4444.4444 Таблица адресов выходного SW1 MAC-адрес G0 / 2 G0 / 2 F0 / 3 F0 / 4 0200.1111.1111 0200.2222.2222 0200.3333.3333 0200.4444.4444 Таблица адресов выходного SW2 G0 / 2 1) Введенный кадр F0 / 1 ...
Figure 5-4 Forwarding Decision with Two Switches: First Switch That same frame next arrives at switch SW2, entering SW2’s G0/2 interface.|Рис. 5-4. Решение о пересылке с двумя коммутаторами: первый коммутатор. Затем тот же самый кадр поступает на коммутатор SW2, входя в интерфейс G0 / 2 SW2.
As shown in Figure 5-5, SW2 uses the same logic steps, but using SW2’s table.|Как показано на Рисунке 5-5, SW2 использует те же логические шаги, но с использованием таблицы SW2.
The MAC table lists the forwarding instructions for that switch only.|В таблице MAC перечислены инструкции по пересылке только для этого коммутатора.
In this case, switch SW2 forwards the frame out its F0/3 port, based on SW2’s MAC address table.|В этом случае коммутатор SW2 пересылает кадр на свой порт F0 / 3 на основе таблицы MAC-адресов SW2.
F0/2 Fred Barney 0200.2222.2222 F0/1 Dest 0200.3333.3333 G0/1 F0/4 F0/3 Wilma 0200.3333.3333 Betty 0200.4444.4444 MAC Address F0/1 F0/2 G0/1 G0/1 0200.1111.1111 0200.2222.2222 0200.3333.3333 0200.4444.4444 Output SW1 Address Table MAC Address G0/2 G0/2 F0/3 F0/4 0200.1111.1111 0200.2222.2222 0200.3333.3333 0200.4444.4444 Output SW2 Address Table G0/2 1) Frame Entered G0/2...|F0 / 2 Fred Barney 0200.2222.2222 F0 / 1 Dest 0200.3333.3333 G0 / 1 F0 / 4 F0 / 3 Wilma 0200.3333.3333 Betty 0200.4444.4444 MAC-адрес F0 / 1 F0 / 2 G0 / 1 G0 / 1 0200.1111.1111 0200.2222 .2222 0200.3333.3333 0200.4444.4444 Таблица адресов выходного SW1 MAC-адрес G0 / 2 G0 / 2 F0 / 3 F0 / 4 0200.1111.1111 0200.2222.2222 0200.3333.3333 0200.4444.4444 Таблица адресов выходного SW2 G0 / 2 1) Введенный кадр G0 / 2 ...
Figure 5-5 Forwarding Decision with Two Switches: Second Switch NOTE The forwarding choice by a switch was formerly called a forward-versus-filter decision, because the switch also chooses to not forward (to filter) frames, not sending the frame out some ports.|Рисунок 5-5 Решение о пересылке с двумя коммутаторами: второй коммутатор ПРИМЕЧАНИЕ. Выбор пересылки коммутатором ранее назывался решением о пересылке или фильтрации, потому что коммутатор также предпочитает не пересылать (фильтровать) кадры, не отправляя кадр из некоторых порты.
The examples so far use switches that happen to have a MAC table with all the MAC addresses listed.|В примерах до сих пор используются переключатели, у которых есть таблица MAC со всеми перечисленными MAC-адресами.
As a result, the destination MAC address in the frame is known to the switch.|В результате MAC-адрес назначения в кадре известен коммутатору.
The frames are called known unicast frames, or simply known unicasts, because the destination address is a unicast address, and the destination is known.|Эти кадры называются известными одноадресными кадрами или просто известными одноадресными передачами, потому что адрес назначения является адресом одноадресной передачи, а пункт назначения известен.
As shown in these examples, switches forward known unicast frames out one port: the port as listed in the MAC table entry for that MAC address.|Как показано в этих примерах, коммутаторы пересылают известные одноадресные кадры на один порт: порт, указанный в записи таблицы MAC-адресов для этого MAC-адреса.
#### Learning MAC Addresses
Изучение MAC-адресов   
__|__
--|--
Thankfully, the networking staff does not have to type in all those MAC table entries.|К счастью, сетевому персоналу не нужно вводить все эти записи в таблице MAC-адресов.
Instead, each switch does its second main function: to learn the MAC addresses and interfaces to put into its address table.|Вместо этого каждый коммутатор выполняет свою вторую основную функцию: изучает MAC-адреса и интерфейсы, которые необходимо поместить в свою таблицу адресов.
With a complete MAC address table, the switch can make accurate forwarding and filtering decisions as just discussed.|Имея полную таблицу MAC-адресов, коммутатор может принимать точные решения по пересылке и фильтрации, как только что обсуждалось.
Switches build the address table by listening to incoming frames and examining the source MAC address in the frame.|Коммутаторы создают таблицу адресов, прослушивая входящие кадры и проверяя MAC-адрес источника в кадре.
If a frame enters the switch and the source MAC address is not in the MAC address table, the switch creates an entry in the table.|Если кадр поступает в коммутатор, а MAC-адрес источника отсутствует в таблице MAC-адресов, коммутатор создает запись в таблице.
That table entry lists the interface from which the frame arrived.|В этой записи таблицы указан интерфейс, из которого пришел фрейм.
Switch learning logic is that simple.|Логика обучения переключению настолько проста.
Figure 5-6 depicts the same single-switch topology network as Figure 5-3, but before the switch has built any address table entries.|На рис. 5-6 изображена та же топология сети с одним коммутатором, что и на рис. 5-3, но до того, как коммутатор создал какие-либо записи в таблице адресов.
The figure shows the first two frames sent in this network—first a frame from Fred, addressed to Barney, and then Barney’s response, addressed to Fred.|На рисунке показаны первые два кадра, отправленные в этой сети - сначала кадр от Фреда, адресованный Барни, а затем ответ Барни, адресованный Фреду.
Figure 5-6 Switch Learning: Empty Table and Adding Two Entries (Figure 5-6 depicts the MAC learning process only, and ignores the forwarding process and therefore ignores the destination MAC addresses.)|Рисунок 5-6 Обучение коммутатора: пустая таблица и добавление двух записей (Рисунок 5-6 отображает только процесс обучения MAC, игнорируя процесс пересылки и, следовательно, игнорирует MAC-адреса назначения.)
Focus on the learning process and how the MAC table grows at each step as shown on the right side of the figure.|Сосредоточьтесь на процессе обучения и на том, как таблица MAC растет на каждом этапе, как показано в правой части рисунка.
The switch begins with an empty MAC table, as shown in the upperright part of the figure.|Коммутатор начинается с пустой таблицы MAC-адресов, как показано в правой верхней части рисунка.
Then Fred sends his first frame (labeled “1”) to Barney, so the switch adds an entry for 0200.1111.1111, Fred’s MAC address, associated with interface F0/1.|Затем Фред отправляет свой первый кадр (помеченный «1») Барни, поэтому коммутатор добавляет запись для 0200.1111.1111, MAC-адреса Фреда, связанного с интерфейсом F0 / 1.
Why F0/1?|Почему F0 / 1?
The frame sent by Fred entered the switch’s F0/1 port.|Фрейм, посланный Фредом, поступил в порт F0 / 1 коммутатора.
SW1’s logic runs something like this: “The source is MAC 0200.1111.1111, the frame entered F0/1, so from my perspective, 0200.1111.1111 must be reachable out my port F0/1.”|Логика SW1 выглядит примерно так: «Источник - MAC 0200.1111.1111, кадр вошел в F0 / 1, поэтому, с моей точки зрения, 0200.1111.1111 должен быть доступен через мой порт F0 / 1».
Continuing the example, when Barney replies in Step 2, the switch adds a second entry, this one for 0200.2222.2222, Barney’s MAC address, along with interface F0/2.|Продолжая пример, когда Барни отвечает на шаге 2, коммутатор добавляет вторую запись, на этот раз для 0200.2222.2222, MAC-адреса Барни, вместе с интерфейсом F0 / 2.
Why F0/2?|Почему F0 / 2?
The frame Barney sent entered the switch’s F0/2 interface.|Фрейм, посланный Барни, вошел в интерфейс F0 / 2 коммутатора.
Learning always occurs by looking at the source MAC address in the frame and adds the incoming interface as the associated port.|Обучение всегда происходит путем просмотра исходного MAC-адреса в кадре и добавления входящего интерфейса в качестве связанного порта.
#### Flooding Unknown Unicast and Broadcast Frames
Заливка неизвестных одноадресных и широковещательных кадров   
__|__
--|--
Now again turn your attention to the forwarding process, using the topology in Figure 5-5.|Теперь снова обратим ваше внимание на процесс пересылки, используя топологию на рисунке 5-5.
What do you suppose the switch does with Fred’s first frame, the one that occurred when there were no entries in the MAC address table?|Как вы думаете, что коммутатор делает с первым кадром Фреда, который произошел, когда в таблице MAC-адресов не было записей?
As it turns out, when there is no matching entry in the table, switches forward the frame out all interfaces (except the incoming interface)|Оказывается, когда в таблице нет соответствующей записи, переключатели пересылают кадр из всех интерфейсов (кроме входящего интерфейса)
using a process called flooding.|с помощью процесса, называемого наводнением.
And the frame whose destination address is unknown to the switch is called an unknown unicast frame, or simply an unknown unicast.|И кадр, адрес назначения которого неизвестен коммутатору, называется неизвестным одноадресным кадром или просто неизвестным одноадресным.
Switches flood unknown unicast frames.|Коммутаторы лавинно рассылают неизвестные одноадресные кадры.
Flooding means that the switch forwards copies of the frame out all ports, except the port on which the frame was received.|Флудинг означает, что коммутатор пересылает копии кадра на все порты, кроме порта, на котором кадр был получен.
The idea is simple:|Идея проста:
if you do not know where to send it, send it everywhere, to deliver the frame.|если не знаете, куда его отправить, отправьте его везде, чтобы доставить рамку.
And, by the way, that device will likely then send a reply—and then the switch can learn that device’s MAC address and forward future frames out one port as a known unicast frame.|И, кстати, это устройство, скорее всего, затем отправит ответ, а затем коммутатор сможет узнать MAC-адрес этого устройства и пересылать будущие кадры через один порт как известный одноадресный кадр.
Switches also flood LAN broadcast frames (frames destined to the Ethernet broadcast address of FFFF.FFFF.FFFF) because this process helps deliver a copy of the frame to all devices in the LAN.|Коммутаторы также рассылают широковещательные кадры LAN (кадры, предназначенные для широковещательного адреса Ethernet FFFF.FFFF.FFFF), потому что этот процесс помогает доставить копию кадра на все устройства в LAN.
For example, Figure 5-7 shows the same first frame sent by Fred, when the switch’s MAC table is empty.|Например, на рис. 5-7 показан тот же самый первый кадр, отправленный Фредом, когда таблица MAC-адресов коммутатора пуста.
At step 1, Fred sends the frame.|На шаге 1 Фред отправляет фрейм.
At step 2, the switch sends a copy of the frame out all three of the other interfaces.|На шаге 2 коммутатор отправляет копию кадра на все три других интерфейса.
Figure 5-7 Switch Flooding: Unknown Unicast Arrives, Floods Out Other Ports|Рисунок 5-7 Переполнение коммутатора: прибывает неизвестная одноадресная рассылка, затопление других портов
#### Avoiding Loops Using Spanning Tree Protocol
Избежание циклов с помощью протокола связующего дерева   
__|__
--|--
The third primary feature of LAN switches is loop prevention, as implemented by Spanning Tree Protocol (STP). Without STP, any flooded frames would loop for an indefinite period of time in Ethernet networks with physically redundant links.|Третьей основной функцией коммутаторов LAN является предотвращение петель, реализованное протоколом Spanning Tree Protocol (STP). Без STP любые лавинные кадры будут зацикливаться в течение неопределенного периода времени в сетях Ethernet с физически избыточными каналами.
To prevent looping frames, STP blocks some ports from forwarding frames so that only one active path exists between any pair of LAN segments.|Чтобы предотвратить зацикливание кадров, STP блокирует пересылку кадров некоторыми портами, поэтому между любой парой сегментов LAN существует только один активный путь.
The result of STP is good: frames do not loop infinitely, which makes the LAN usable.|Результат STP хороший: кадры не зацикливаются бесконечно, что делает LAN пригодной для использования.
However, STP has negative features as well, including the fact that it takes some work to balance traffic across the redundant alternate links.|Однако у STP есть и отрицательные особенности, в том числе то, что требуется некоторая работа для балансировки трафика через резервные альтернативные каналы.
A simple example makes the need for STP more obvious.|Простой пример делает необходимость STP более очевидной.
Remember, switches flood unknown unicast frames and broadcast frames.|Помните, что коммутаторы лавинно рассылают неизвестные одноадресные и широковещательные кадры.
Figure 5-8 shows an unknown unicast frame, sent by Larry to Bob, which loops forever because the network has redundancy but no STP.|На рисунке 5-8 показан неизвестный одноадресный кадр, отправленный Ларри Бобу, который зацикливается навсегда, потому что в сети есть избыточность, но нет STP.
Note that the figure shows one direction of the looping frame only, just to reduce clutter, but a copy of the frame would also loop the other direction.|Обратите внимание, что на рисунке показано только одно направление зацикленного кадра, чтобы уменьшить беспорядок, но копия кадра также зацикливается в другом направлении.
Figure 5-8 Network with Redundant Links but Without STP: The Frame Loops Forever The flooding of this frame would result in the frame repeatedly rotating around the three switches, because none of the switches list Bob’s MAC address in their address tables—so each switch floods the frame.|Рис. 5-8 Сеть с избыточными ссылками, но без STP: цикл кадра вечно Заливка этого кадра приведет к тому, что кадр будет постоянно вращаться вокруг трех переключателей, потому что ни один из коммутаторов не перечисляет MAC-адрес Боба в своих адресных таблицах, поэтому каждый коммутатор заливает кадр.
And while the flooding process is a good mechanism for forwarding unknown unicasts and broadcasts, the continual flooding of traffic frames as in the figure can completely congest the LAN to the point of making it unusable.|И хотя процесс лавинной рассылки является хорошим механизмом для пересылки неизвестных одноадресных и широковещательных рассылок, непрерывная лавинная рассылка кадров трафика, как показано на рисунке, может полностью перегружать LAN до такой степени, что она становится непригодной для использования.
A topology like Figure 5-8, with redundant links, is good, but we need to prevent the bad effect of those looping frames.|Топология, подобная рис. 5-8, с избыточными ссылками, хороша, но нам нужно предотвратить плохой эффект этих циклических кадров.
To avoid Layer 2 loops, all switches need to use STP. STP causes each interface on a switch to settle into either a blocking state or a forwarding state.|Чтобы избежать петель уровня 2, все коммутаторы должны использовать протокол STP. STP заставляет каждый интерфейс на коммутаторе переходить либо в состояние блокировки, либо в состояние пересылки.
Blocking means that the interface cannot forward or receive data frames, while forwarding means that the interface can send and receive data frames.|Блокировка означает, что интерфейс не может пересылать или получать кадры данных, в то время как пересылка означает, что интерфейс может отправлять и получать кадры данных.
If a correct subset of the interfaces is blocked, only a single currently active logical path exists between each pair of LANs.|Если правильное подмножество интерфейсов заблокировано, между каждой парой локальных сетей существует только один активный в настоящий момент логический путь.
NOTE STP behaves identically for a transparent bridge and a switch.|ПРИМЕЧАНИЕ STP ведет себя одинаково для прозрачного моста и коммутатора.
Therefore, the terms bridge, switch, and bridging device all are used interchangeably when discussing STP.|Таким образом, при обсуждении протокола STP термины «мост», «коммутатор» и «мостовое устройство» используются как взаимозаменяемые.
Chapter 9 of this book, “Spanning Tree Protocol Concepts,” examines STP in depth, including how STP prevents loops.|В главе 9 этой книги «Концепции протокола связующего дерева» подробно рассматривается протокол STP, в том числе то, как STP предотвращает образование петель.
#### LAN Switching Summary
Обзор коммутации LAN   
__|__
--|--
Switches use Layer 2 logic, examining the Ethernet data-link header to choose how to process frames.|Коммутаторы используют логику уровня 2, исследуя заголовок канала передачи данных Ethernet, чтобы выбрать способ обработки кадров.
In particular, switches make decisions to forward and filter frames, learn MAC addresses, and use STP to avoid loops, as follows:|В частности, коммутаторы принимают решения о пересылке и фильтрации кадров, изучении MAC-адресов и использовании протокола STP для предотвращения петель следующим образом:
Step 1.|Шаг 1.
Switches forward frames based on the destination MAC address:|Переключает пересылку кадров на основе MAC-адреса назначения:
A. If the destination MAC address is a broadcast, multicast, or unknown destination unicast (a unicast not listed in the MAC table), the switch floods the frame.|A. Если MAC-адрес назначения является широковещательной, многоадресной или одноадресной рассылкой неизвестного назначения (одноадресная передача, не указанная в таблице MAC-адресов), коммутатор лавинно рассылает кадр.
B. If the destination MAC address is a known unicast address (a unicast address found in the MAC table):|B. Если MAC-адрес назначения является известным одноадресным адресом (одноадресный адрес, указанный в таблице MAC):
i. If the outgoing interface listed in the MAC address table is different from the interface in which the frame was received, the switch forwards the frame out the outgoing interface.|я. Если исходящий интерфейс, указанный в таблице MAC-адресов, отличается от интерфейса, в котором был получен кадр, коммутатор пересылает этот кадр из исходящего интерфейса.
ii.|II.
If the outgoing interface is the same as the interface in which the frame was received, the switch filters the frame, meaning that the switch simply ignores the frame and does not forward it.|Если исходящий интерфейс совпадает с интерфейсом, в котором был получен кадр, коммутатор фильтрует кадр, что означает, что коммутатор просто игнорирует кадр и не пересылает его.
Step 2.|Шаг 2.
Switches use the following logic to learn MAC address table entries:|Коммутаторы используют следующую логику для изучения записей таблицы MAC-адресов:
A. For each received frame, examine the source MAC address and note the interface from which the frame was received.|A. Для каждого полученного кадра проверьте MAC-адрес источника и обратите внимание на интерфейс, с которого был получен кадр.
B. If it is not already in the table, add the MAC address and interface it was learned on.|B. Если его еще нет в таблице, добавьте MAC-адрес и интерфейс, на котором он был изучен.
Step 3.|Шаг 3.
Switches use STP to prevent loops by causing some interfaces to block, meaning that they do not send or receive frames.|Коммутаторы используют протокол STP для предотвращения петель, вызывая блокировку некоторых интерфейсов, что означает, что они не отправляют и не принимают фреймы.
### Verifying and Analyzing Ethernet Switching
Проверка и анализ коммутации Ethernet   
__|__
--|--
A Cisco Catalyst switch comes from the factory ready to switch frames.|Коммутатор Cisco Catalyst поставляется с завода готовым к переключению кадров.
All you have to do is connect the power cable, plug in the Ethernet cables, and the switch starts switching incoming frames.|Все, что вам нужно сделать, это подключить кабель питания, подключить кабели Ethernet, и коммутатор начнет переключение входящих кадров.
Connect multiple switches together, and they are ready to forward frames between the switches as well.|Соедините несколько коммутаторов вместе, и они также готовы пересылать кадры между коммутаторами.
And the big reason behind this default behavior has to do with the default settings on the switches.|И основная причина такого поведения по умолчанию связана с настройками переключателей по умолчанию.
Cisco Catalyst switches come ready to get busy switching frames because of settings like these:|Коммутаторы Cisco Catalyst готовы принять занятые кадры коммутации из-за таких настроек:
###### The interfaces are enabled by default, ready to start working once a cable is connected.
Интерфейсы включены по умолчанию и готовы начать работу после подключения кабеля.   
###### All interfaces are assigned to VLAN 1.
Все интерфейсы назначены VLAN 1.   
###### 10/100 and 10/100/1000 interfaces use autonegotiation by default.
Интерфейсы 10/100 и 10/100/1000 по умолчанию используют автосогласование.   
###### The MAC learning, forwarding, flooding logic all works by default.
Логика обучения MAC, пересылки и лавинной рассылки работает по умолчанию.   
###### STP is enabled by default.
По умолчанию протокол STP включен.   
__|__
--|--
This second section of the chapter examines how switches will work with these default settings, showing how to verify the Ethernet learning and forwarding process.|Во втором разделе главы исследуется, как коммутаторы будут работать с этими настройками по умолчанию, и показано, как проверить процесс обучения и пересылки Ethernet.
#### Demonstrating MAC Learning
Демонстрация обучения MAC   
__|__
--|--
To see a switch’s MAC address table, use the show mac address-table command.|Чтобы просмотреть таблицу MAC-адресов коммутатора, используйте команду show mac address-table.
With no additional parameters, this command lists all known MAC addresses in the MAC table, including some overhead static MAC addresses that you can ignore.|Без дополнительных параметров эта команда перечисляет все известные MAC-адреса в таблице MAC-адресов, включая некоторые служебные статические MAC-адреса, которые можно игнорировать.
To see all the dynamically learned MAC addresses only, instead use the show mac address-table dynamic command.|Чтобы увидеть только все динамически полученные MAC-адреса, используйте вместо этого динамическую команду show mac address-table dynamic.
The examples in this chapter use almost no configuration, as if you just unboxed the switch when you first purchased it.|Примеры в этой главе почти не используют конфигурацию, как если бы вы только что распаковали коммутатор, когда впервые купили его.
For the examples, the switches have no configuration other than the hostname command to set a meaningful hostname.|В примерах переключатели не имеют конфигурации, кроме команды hostname для установки значимого имени хоста.
Note that to do this in lab, all I did was|Обратите внимание: чтобы сделать это в лаборатории, я всего лишь
###### Use the erase startup-config EXEC command to erase the startup-config file
Используйте команду EXEC erase startup-config, чтобы стереть файл конфигурации запуска.   
###### Use the delete vlan.dat EXEC command to delete the VLAN configuration details
Используйте команду EXEC delete vlan.dat, чтобы удалить детали конфигурации VLAN.   
###### Use the reload EXEC command to reload the switch (thereby using the empty startupconfig,
Используйте команду reload EXEC, чтобы перезагрузить коммутатор (тем самым используя пустой файл startupconfig,   
__|__
--|--
with no VLAN information configured)|без настроенной информации о VLAN)
###### Configure the hostname SW1 command to set the switch hostname
Настройте команду hostname SW1, чтобы установить имя хоста коммутатора.   
__|__
--|--
Once done, the switch starts forwarding and learning MAC addresses, as demonstrated in Example 5-1.|После этого коммутатор начинает пересылку и изучение MAC-адресов, как показано в Примере 5-1.
Example 5-1 Show mac address-table dynamic for Figure 5-7 Example end.|Пример 5-1. Показать динамическую таблицу MAC-адресов для рисунка 5-7. Конец примера.
First, focus on two columns of the table: the MAC Address and Ports columns of the table.|Сначала сфокусируйтесь на двух столбцах таблицы: столбцах MAC-адреса и портов.
The values should look familiar: they match the earlier single-switch example, as repeated here as Figure 5-9.|Значения должны выглядеть знакомыми: они соответствуют более раннему примеру с одним переключателем, как показано на рисунке 5-9.
Note the four MAC addresses listed, along with their matching ports, as shown in the figure.|Обратите внимание на четыре перечисленных MAC-адреса и соответствующие им порты, как показано на рисунке.
Figure 5-9 Single Switch Topology Used in Verification Section Next, look at the Type field in the heading of the output table.|Рис. 5-9 Топология с одним коммутатором, используемая в разделе проверки. Затем посмотрите на поле Type в заголовке выходной таблицы.
The column tells us how the switch learned the MAC address as described earlier in this chapter; in this case, the switch learned all MAC addresses dynamically.|Столбец сообщает нам, как коммутатор узнал MAC-адрес, как описано ранее в этой главе; в этом случае коммутатор запоминал все MAC-адреса динамически.
You can also statically predefine MAC table entries using a couple of different features, including port security, and those would appear as Static in the Type column.|Вы также можете статически предопределить записи таблицы MAC-адресов, используя несколько различных функций, включая безопасность порта, и они будут отображаться как статические в столбце Тип.
Finally, the VLAN column of the output gives us a chance to briefly discuss how VLANs impact switching logic.|Наконец, столбец VLAN в выходных данных дает нам возможность кратко обсудить, как VLAN влияют на логику коммутации.
LAN switches forward Ethernet frames inside a VLAN. What that means is if a frame enters via a port in VLAN 1, then the switch will forward or flood that frame out other ports in VLAN 1 only, and not out any ports that happen to be assigned to another VLAN. Chapter 8, “Implementing Ethernet Virtual LANs,” looks at all the details of how switches forward frames when using VLANs.|Коммутаторы LAN пересылают кадры Ethernet внутри VLAN. Это означает, что если фрейм поступает через порт в VLAN 1, то коммутатор будет перенаправлять или лавировать этот фрейм только для других портов в VLAN 1, а не из каких-либо портов, которые были назначены другой VLAN. Глава 8 «Реализация виртуальных локальных сетей Ethernet» рассматривает все детали того, как коммутаторы пересылают кадры при использовании виртуальных локальных сетей.
#### Switch Interfaces
Коммутатор Интерфейсы   
__|__
--|--
The first example assumes that you installed the switch and cabling correctly, and that the switch interfaces work.|В первом примере предполагается, что вы правильно установили коммутатор и кабели и что интерфейсы коммутатора работают.
Once you do the installation and connect to the Console, you can easily check the status of those interfaces with the show interfaces status command, as shown in Example 5-2.|После того, как вы выполните установку и подключитесь к консоли, вы можете легко проверить состояние этих интерфейсов с помощью команды show interfaces status, как показано в примере 5-2.
Example 5-2 Show interfaces status on Switch SW1 Example end.|Пример 5-2 Показать статус интерфейсов на переключателе SW1 Пример конец.
Focus on the port column for a moment.|Сосредоточьтесь на колонке портов на мгновение.
As a reminder, Cisco Catalyst switches name their ports based on the fastest specification supported, so in this case, the switch has 24 interfaces named FastEthernet, and two named GigabitEthernet.|Напоминаем, что коммутаторы Cisco Catalyst называют свои порты на основе самой быстрой из поддерживаемых спецификаций, поэтому в этом случае коммутатор имеет 24 интерфейса с именем FastEthernet и два с именем GigabitEthernet.
Many commands abbreviate those terms, this time as Fa for FastEthernet and Gi for GigabitEthernet. (The example happens to come from a Cisco Catalyst switch that has 24 10/100 ports and two 10/100/1000 ports.)|Многие команды сокращают эти термины, на этот раз как Fa для FastEthernet и Gi для GigabitEthernet. (Примером является коммутатор Cisco Catalyst, который имеет 24 порта 10/100 и два порта 10/100/1000.)
The Status column, of course, tells us the status or state of the port.|Столбец Status, конечно же, сообщает нам статус или состояние порта.
In this case, the lab switch had cables and devices connected to ports F0/1–F0/4 only, with no other cables connected.|В этом случае лабораторный коммутатор имел кабели и устройства, подключенные только к портам F0 / 1 – F0 / 4, без других подключенных кабелей.
As a result, those first four ports have a state of connected, meaning that the ports have a cable and are functional.|В результате эти первые четыре порта находятся в состоянии «подключено», что означает, что порты имеют кабель и работают.
The notconnect state means that the port is not yet functioning.|Состояние notconnect означает, что порт еще не работает.
It may mean that there is no cable installed, but other problems may exist as well. (The section “Analyzing Switch Interface Status and Statistics,” in Chapter 7, “Configuring and Verifying Switch Interfaces,” works through the details of what causes a switch interface to fail.)|Это может означать, что кабель не установлен, но могут существовать и другие проблемы. (В разделе «Анализ состояния и статистики интерфейса коммутатора» главы 7 «Настройка и проверка интерфейсов коммутатора» подробно рассматриваются причины сбоя интерфейса коммутатора.)
NOTE You can see the status for a single interface in a couple of ways.|ПРИМЕЧАНИЕ. Вы можете увидеть состояние отдельного интерфейса двумя способами.
For instance, for F0/1, the command show interfaces f0/1 status lists the status in a single line of output as in Example 5-2.|Например, для F0 / 1 команда show interfaces f0 / 1 status перечисляет состояние в одной строке вывода, как в примере 5-2.
The show interfaces f0/1 command (without the status keyword) displays a detailed set of messages about the interface.|Команда show interfaces f0 / 1 (без ключевого слова status) отображает подробный набор сообщений об интерфейсе.
The show interfaces command has a large number of options.|Команда show interfaces имеет большое количество параметров.
One particular option, the counters option, lists statistics about incoming and outgoing frames on the interfaces.|Одна конкретная опция, опция счетчиков, перечисляет статистику о входящих и исходящих кадрах на интерфейсах.
In particular, it lists the number of unicast, multicast, and broadcast frames (both the in and out directions), and a total byte count for those frames.|В частности, он перечисляет количество одноадресных, многоадресных и широковещательных кадров (как входящие, так и исходящие), а также общее количество байтов для этих кадров.
Example 5-3 shows an example, again for interface F0/1.|В примере 5-3 показан пример снова для интерфейса F0 / 1.
Example 5-3 Show interfaces f0/1 counters on Switch SW1 Example end.|Пример 5-3 Показать интерфейсы счетчиков f0 / 1 на коммутаторе SW1 Пример конец.
#### Finding Entries in the MAC Address Table
Поиск записей в таблице MAC-адресов   
__|__
--|--
With a single switch and only four hosts connected to it, you can just read the details of the MAC address table and find the information you want to see.|С одним коммутатором и подключенными к нему всего четырьмя хостами, вы можете просто прочитать детали таблицы MAC-адресов и найти информацию, которую хотите увидеть.
However, in real networks, with lots of interconnected hosts and switches, just reading the output to find one MAC address can be hard to do.|Однако в реальных сетях с большим количеством взаимосвязанных хостов и коммутаторов просто прочитать выходные данные, чтобы найти один MAC-адрес, может быть сложно.
You might have hundreds of entries—page after page of output—|У вас могут быть сотни записей - страница за страницей вывода -
with each MAC address looking like a random string of hex characters. (The book uses easyto-|где каждый MAC-адрес выглядит как случайная строка шестнадцатеричных символов. (В книге используется легкое-
recognize MAC addresses to make it easier to learn.)|распознавать MAC-адреса, чтобы облегчить изучение.)
Thankfully, Cisco IOS supplies several more options on the show mac address-table command to make it easier to find individual entries.|К счастью, Cisco IOS предоставляет несколько дополнительных опций для команды show mac address-table, чтобы упростить поиск отдельных записей.
First, if you know the MAC address, you can search for it—just type in the MAC address at the end of the command, as shown in Example 5-4.|Во-первых, если вам известен MAC-адрес, вы можете найти его - просто введите MAC-адрес в конце команды, как показано в примере 5-4.
All you have to do is include the address keyword, followed by the actual MAC address.|Все, что вам нужно сделать, это включить ключевое слово адреса, за которым следует фактический MAC-адрес.
If the address exists, the output lists the address.|Если адрес существует, в выходных данных указан адрес.
Note that the output lists the exact same information in the exact same format, but it lists only the line for the matching MAC address.|Обратите внимание, что вывод содержит точно такую ??же информацию в том же формате, но содержит только строку для совпадающего MAC-адреса.
Example 5-4 Show mac address-table dynamic with the address Keyword Example end.|Пример 5-4 Показать динамическую таблицу MAC-адресов с концом примера ключевого слова адреса.
While this information is useful, often the engineer troubleshooting a problem does not know the MAC addresses of the devices connected to the network.|Хотя эта информация полезна, часто инженер, решающий проблему, не знает MAC-адреса устройств, подключенных к сети.
Instead, the engineer has a topology diagram, knowing which switch ports connect to other switches and which connect to endpoint devices.|Вместо этого у инженера есть схема топологии, зная, какие порты коммутатора подключаются к другим коммутаторам, а какие - к конечным устройствам.
Sometimes you might be troubleshooting while looking at a network topology diagram and want to look at all the MAC addresses learned off a particular port.|Иногда вы можете устранять неполадки, глядя на диаграмму топологии сети и желая просмотреть все MAC-адреса, полученные от определенного порта.
IOS supplies that option with the show mac address-table dynamic interface command.|IOS предоставляет эту опцию с помощью команды динамического интерфейса show mac address-table.
Example 5-5 shows one example, for switch SW1’s F0/1 interface.|В примере 5-5 показан один из примеров интерфейса F0 / 1 переключателя SW1.
Example 5-5 Show mac address-table dynamic with the interface Keyword Example end.|Пример 5-5. Показ динамической таблицы MAC-адресов с интерфейсом Keyword Example end.
Finally, you may also want to find the MAC address table entries for one VLAN. You guessed it—you can add the vlan parameter, followed by the VLAN number.|Наконец, вы также можете найти записи в таблице MAC-адресов для одной VLAN. Как вы уже догадались - вы можете добавить параметр vlan, а затем номер VLAN.
Example 5-6 shows two such examples from the same switch SW1 from Figure 5-7—one for VLAN 1, where all four devices reside, and one for a nonexistent VLAN 2.|В примере 5-6 показаны два таких примера для одного и того же коммутатора SW1 из рисунка 5-7 - один для VLAN 1, где находятся все четыре устройства, и один для несуществующей VLAN 2.
Example 5-6 The show mac address-table vlan Command Example end.|Пример 5-6 Пример команды show mac address-table vlan end.
#### Managing the MAC Address Table (Aging, Clearing)
Управление таблицей MAC-адресов (устаревание, очистка)   
__|__
--|--
This chapter closes with a few comments about how switches manage their MAC address tables.|Эта глава завершается несколькими комментариями о том, как коммутаторы управляют своими таблицами MAC-адресов.
Switches do learn MAC addresses, but those MAC addresses do not remain in the table indefinitely.|Коммутаторы изучают MAC-адреса, но эти MAC-адреса не остаются в таблице на неопределенный срок.
The switch will remove the entries due to age, due to the table filling, and you can remove entries using a command.|Переключатель удалит записи из-за возраста, из-за заполнения таблицы, и вы можете удалить записи с помощью команды.
First, for aging out MAC table entries, switches remove entries that have not been used for a defined number of seconds (default of 300 seconds on many switches).|Во-первых, для устаревания записей таблицы MAC-адресов коммутаторы удаляют записи, которые не использовались в течение определенного количества секунд (по умолчанию 300 секунд на многих коммутаторах).
To do that, switches look at every incoming frame and every source MAC address, and do something related to learning.|Для этого коммутаторы просматривают каждый входящий кадр и каждый исходный MAC-адрес и делают что-то, связанное с обучением.
If it is a new MAC address, the switch adds the correct entry to the table, of course.|Если это новый MAC-адрес, коммутатор, конечно, добавляет правильную запись в таблицу.
However, if that entry already exists, the switch still does something: it resets the inactivity timer back to 0 for that entry.|Однако, если эта запись уже существует, переключатель все равно что-то делает: он сбрасывает таймер бездействия обратно на 0 для этой записи.
Each entry’s timer counts upward over time to measure how long the entry has been in the table.|Таймер каждой записи ведет отсчет в возрастающем порядке, чтобы измерить, как долго запись находилась в таблице.
The switch times out (removes) any entries whose timer reaches the defined aging time.|Коммутатор отключает (удаляет) все записи, таймер которых достигает заданного времени устаревания.
Example 5-7 shows the aging timer setting for the entire switch.|В примере 5-7 показана установка таймера старения для всего коммутатора.
The aging time can be configured to a different time, globally and per-VLAN using the mac address-table aging-time time-in-seconds [vlan vlan-number] global configuration command.|Время устаревания может быть настроено на другое время, глобально и для каждой VLAN, с помощью команды глобальной настройки mac-address-table age-time-time-in-seconds [vlan vlan-number].
The example shows a case with all defaults, with the global setting of 300 seconds, and no per-VLAN overrides.|В примере показан случай со всеми значениями по умолчанию, с глобальным значением 300 секунд и без переопределений для каждой VLAN.
Example 5-7 The MAC Address Default Aging Timer Displayed Example end.|Пример 5-7 Отображаемый таймер устаревания MAC-адреса по умолчанию Пример конец.
Each switch also removes the oldest table entries, even if they are younger than the aging time setting, if the table fills.|Каждый переключатель также удаляет самые старые записи таблицы, даже если они моложе установленного времени устаревания, если таблица заполняется.
The MAC address table uses content-addressable memory (CAM), a physical memory that has great table lookup capabilities.|Таблица MAC-адресов использует память с адресацией по содержимому (CAM), физическую память, которая имеет отличные возможности поиска в таблице.
However, the size of the table depends on the size of the CAM in a particular model of switch and based on some configurable settings in the switch.|Однако размер таблицы зависит от размера CAM в конкретной модели коммутатора и от некоторых настраиваемых параметров коммутатора.
When a switch tries to add a new MAC table entry and finds the table full, the switch times out (removes) the oldest table entry to make space.|Когда коммутатор пытается добавить новую запись в таблицу MAC-адресов и обнаруживает, что таблица заполнена, коммутатор отключает (удаляет) самую старую запись таблицы, чтобы освободить место.
For perspective, the end of Example 5-7 lists the size of a Cisco Catalyst switch’s MAC table at about 8000 entries—the same four existing entries from the earlier examples, with space for 7299 more.|Для сравнения, в конце примера 5-7 указан размер таблицы MAC-адресов коммутатора Cisco Catalyst примерно в 8000 записей - те же четыре существующие записи из предыдущих примеров, с пространством для дополнительных 7299 записей.
Finally, you can remove the dynamic entries from the MAC address table with the clear mac address-table dynamic command.|Наконец, вы можете удалить динамические записи из таблицы MAC-адресов с помощью динамической команды clear mac address-table dynamic.
Note that the show commands in this chapter can be executed from user and enable mode, but the clear command happens to be an enable mode command.|Обратите внимание, что команды show в этой главе могут выполняться из режима пользователя и режима включения, но команда clear оказывается командой режима включения.
The command also allows parameters to limit the types of entries cleared, as follows:|Команда также позволяет параметрам ограничивать типы очищаемых записей следующим образом:
###### By VLAN: clear mac address-table dynamic vlan vlan-number
По VLAN: очистить таблицу MAC-адресов, динамический vlan, номер vlan   
###### By Interface: clear mac address-table dynamic interface interface-id
По интерфейсу: очистить идентификатор интерфейса динамического интерфейса таблицы MAC-адресов   
###### By MAC address: clear mac address-table dynamic address mac-address
По MAC-адресу: очистить таблицу MAC-адресов, динамический MAC-адрес   
#### MAC Address Tables with Multiple Switches
Таблицы MAC-адресов с несколькими коммутаторами   
__|__
--|--
Finally, to complete the discussion, it helps to think about an example with multiple switches, just to emphasize how MAC learning, forwarding, and flooding happen independently on each LAN switch.|Наконец, чтобы завершить обсуждение, полезно подумать о примере с несколькими коммутаторами, просто чтобы подчеркнуть, как изучение MAC, пересылка и лавинная рассылка происходят независимо на каждом коммутаторе LAN.
Consider the topology in Figure 5-10, and pay close attention to the port numbers.|Рассмотрим топологию на рисунке 5-10 и обратите особое внимание на номера портов.
The ports were purposefully chosen so that neither switch used any of the same ports for this example.|Порты были выбраны специально, чтобы ни один из коммутаторов не использовал одни и те же порты в этом примере.
That is, switch SW2 does have a port F0/1 and F0/2, but I did not plug any devices into those ports when making this example.|То есть у коммутатора SW2 есть порты F0 / 1 и F0 / 2, но я не подключал к этим портам какие-либо устройства при создании этого примера.
Also note that all ports are in VLAN 1, and as with the other examples in this chapter, all default configuration is used other than the hostname on the switches.|Также обратите внимание, что все порты находятся в VLAN 1, и, как и в других примерах в этой главе, на коммутаторах используется вся конфигурация по умолчанию, кроме имени хоста.
Figure 5-10 Two-Switch Topology Example Think about a case in which both switches learn all four MAC addresses.|Рисунок 5-10 Пример топологии с двумя коммутаторами Подумайте о случае, когда оба коммутатора узнают все четыре MAC-адреса.
For instance, that would happen if the hosts on the left communicate with the hosts on the right.|Например, это произойдет, если хосты слева будут общаться с хостами справа.
SW1’s MAC address table would list SW1’s own port numbers (F0/1, F0/2, and G0/1) because SW1 uses that information to decide where SW1 should forward frames.|В таблице MAC-адресов SW1 будут перечислены собственные номера портов SW1 (F0 / 1, F0 / 2 и G0 / 1), поскольку SW1 использует эту информацию, чтобы решить, куда SW1 должен пересылать кадры.
Similarly, SW2’s MAC table lists SW2’s port numbers (F0/3, F0/4, G0/2 in this example).|Точно так же в таблице MAC SW2 перечислены номера портов SW2 (F0 / 3, F0 / 4, G0 / 2 в этом примере).
Example 5-8 shows the MAC address tables on both switches for that scenario.|В примере 5-8 показаны таблицы MAC-адресов на обоих коммутаторах для этого сценария.
Example 5-8 The MAC Address Table on Two Switches Example end.|Пример 5-8 Таблица MAC-адресов на двух коммутаторах Пример конец.
### Chapter Review
Обзор главы   
__|__
--|--
Review this chapter’s material using either the tools in the book or interactive tools for the same material found on the book’s companion website.|Просмотрите материал этой главы, используя инструменты из книги или интерактивные инструменты для тех же материалов, которые можно найти на сопутствующем веб-сайте книги.
Table 5-2 outlines the key review elements and where you can find them.|В Таблице 5-2 представлены основные элементы обзора и их местонахождение.
To better track your study progress, record when you completed these activities in the second column.|Чтобы лучше отслеживать свои успехи в учебе, отметьте, когда вы выполнили эти задания, во втором столбце.
Table 5-2 Chapter Review Tracking Table end.|Таблица 5-2. Конец таблицы отслеживания обзора главы.
Review All the Key Topics Do Labs The Sim Lite software is a version of Pearson’s full simulator learning product with a subset of the labs, included free with this book.|Просмотрите все ключевые темы. Выполните лабораторные работы. Программное обеспечение Sim Lite - это версия полного учебного продукта Pearson на симуляторах с подмножеством лабораторных работ, бесплатно включенных в эту книгу.
The subset of labs mostly relate to this part of the book, so take the time to try some of the labs.|Подмножество лабораторных работ в основном относится к этой части книги, поэтому найдите время, чтобы попробовать некоторые из них.
As always, also check the author’s blog site pages for configuration exercises (Config Labs)|Как всегда, также проверьте страницы блога автора на предмет упражнений по настройке (Лаборатория конфигурации)
at http://blog.certskills.com.|на http://blog.certskills.com.
Key Terms You Should Know broadcast frame, known unicast frame, Spanning Tree Protocol (STP), unknown unicast frame, MAC address table, forward, flood Command References Table 5-4 lists the verification commands used in this chapter.|Ключевые термины, которые вы должны знать: широковещательный кадр, известный одноадресный кадр, протокол связующего дерева (STP), неизвестный одноадресный кадр, таблица MAC-адресов, пересылка, лавинная рассылка. Ссылки на команды В таблице 5-4 перечислены команды проверки, используемые в этой главе.
As an easy review exercise, cover the left column, read the right, and try to recall the command without looking.|В качестве простого упражнения на повторение закройте левый столбец, прочтите правый и попытайтесь вспомнить команду, не глядя.
Then repeat the exercise, covering the right column, and try to recall what the command does.|Затем повторите упражнение, охватывая правый столбец, и попытайтесь вспомнить, что делает команда.
Table 5-4 Chapter 5 EXEC Command Reference Table end.|Таблица 5-4 Глава 5 Справочник команд EXEC Конец таблицы.
Note that this chapter also includes reference to one configuration command, so it does not call for the use of a separate table.|Обратите внимание, что эта глава также включает ссылку на одну команду конфигурации, поэтому она не требует использования отдельной таблицы.
For review, the command is mac address-table aging-time time-in-seconds [vlan vlan-number]|Для обзора, команда - это время-время-время-старение таблицы MAC-адресов в секундах [vlan-номер-vlan]
## Chapter 6 Configuring Basic Switch Management
Глава 6 Настройка базового управления коммутатором   
__|__
--|--
This chapter covers the following exam topics:|В этой главе рассматриваются следующие экзаменационные темы:
###### 1.0 Network Fundamentals
1.0 Основы сети   
###### 1.6 Configure and verify IPv4 addressing and subnetting
1.6 Настройка и проверка адресации IPv4 и подсетей   
###### 4.0 IP Services
4.0 IP-услуги   
###### 4.6 Configure and verify DHCP client and relay
4.6 Настройка и проверка DHCP-клиента и ретранслятора   
###### 4.8 Configure network devices for remote access using SSH
4.8 Настройка сетевых устройств для удаленного доступа по SSH   
###### 5.0 Security Fundamentals
5.0 Основы безопасности   
###### 5.3 Configure device access control using local passwords
5.3 Настройка контроля доступа к устройствам с использованием локальных паролей   
__|__
--|--
The work performed by a networking device can be divided into three broad categories.|Работу, выполняемую сетевым устройством, можно разделить на три большие категории.
The first and most obvious, called the data plane, is the work a switch does to forward frames generated by the devices connected to the switch.|Первая и наиболее очевидная, называемая плоскостью данных, - это работа, выполняемая коммутатором по пересылке кадров, генерируемых устройствами, подключенными к коммутатору.
In other words, the data plane is the main purpose of the switch.|Другими словами, плоскость данных - основное назначение коммутатора.
Second, the control plane refers to the configuration and processes that control and change the choices made by the switch’s data plane.|Во-вторых, плоскость управления относится к конфигурации и процессам, которые контролируют и изменяют выбор, сделанный плоскостью данных коммутатора.
The network engineer can control which interfaces are enabled and disabled, which ports run at which speeds, how Spanning Tree blocks some ports to prevent loops, and so on.|Сетевой инженер может контролировать, какие интерфейсы включены и отключены, какие порты работают с какой скоростью, как Spanning Tree блокирует некоторые порты для предотвращения петель и т. Д.
The third category, the management plane, is the topic of this chapter.|Третья категория, уровень управления, является темой данной главы.
The management plane deals with managing the device itself, rather than controlling what the device is doing.|Уровень управления имеет дело с управлением самим устройством, а не с контролем того, что оно делает.
In particular, this chapter looks at the most basic management features that can be configured in a Cisco switch.|В частности, в этой главе рассматриваются самые основные функции управления, которые можно настроить в коммутаторе Cisco.
The first section of the chapter works through the configuration of different kinds of login security.|Первый раздел главы посвящен настройке различных видов безопасности входа.
The second section shows how to configure IPv4 settings on a switch so it can be remotely managed.|Во втором разделе показано, как настроить параметры IPv4 на коммутаторе, чтобы им можно было управлять удаленно.
The last (short) section then explains a few practical matters that can make your life in the lab a little easier.|В последнем (коротком) разделе объясняются несколько практических вопросов, которые могут немного облегчить вашу жизнь в лаборатории.
### “Do I Know This Already?” Quiz
«Знаю ли я это уже?» Викторина   
__|__
--|--
Take the quiz (either here or use the PTP software) if you want to use the score to help you decide how much time to spend on this chapter.|Пройдите тест (здесь или воспользуйтесь программой PTP), если вы хотите использовать оценку, чтобы решить, сколько времени потратить на эту главу.
The letter answers are listed at the bottom of the page following the quiz.|Ответы на письма перечислены внизу страницы после викторины.
Appendix C, found both at the end of the book as well as on the companion website, includes both the answers and explanations.|Приложение C, которое можно найти как в конце книги, так и на сопутствующем веб-сайте, включает как ответы, так и пояснения.
You can also find both answers and explanations in the PTP testing software.|Вы также можете найти ответы и пояснения в программе тестирования PTP.
CHAPTER 6 Table 6-1 “Do I Know This Already?” Foundation Topics Section-to-Question Mapping|ГЛАВА 6 Таблица 6-1 «Знаю ли я это уже?» Сопоставление разделов с вопросами по основным темам
### Foundation Topics
Основные темы   
### Securing the Switch CLI
Защита интерфейса командной строки коммутатора   
__|__
--|--
Enabling IP for Remote Access 4–5 Miscellaneous Settings Useful in Lab 6 1.|Включение IP для удаленного доступа 4–5 Прочие настройки, полезные в лабораторной работе 6 1.
Imagine that you have configured the enable secret command, followed by the enable password command, from the console.|Представьте, что вы настроили в консоли команду enable secret, за которой следует команда enable password.
You log out of the switch and log back in at the console.|Вы выходите из коммутатора и снова входите в систему с консоли.
Which command defines the password that you had to enter to access privileged mode?|Какая команда определяет пароль, который вам нужно было ввести для доступа к привилегированному режиму?
a. enable password b. enable secret c.|а. включить пароль b. включить секрет c.
Neither d.|Ни d.
The password command, if it is configured 2.|Команда пароля, если она настроена 2.
An engineer wants to set up simple password protection with no usernames for some switches in a lab, for the purpose of keeping curious coworkers from logging in to the lab switches from their desktop PCs. Which of the following commands would be a useful part of that configuration?|Инженер хочет установить простую защиту паролем без имен пользователей для некоторых коммутаторов в лаборатории, чтобы не дать любопытным коллегам войти в лабораторные коммутаторы со своих настольных компьютеров. Какая из следующих команд была бы полезной частью этой конфигурации?
a. A login vty mode subcommand b.|а. Подкоманда входа в режим VTY b.
A password password console subcommand c.|Подкоманда консоли пароль пароль c.
A login local vty subcommand d.|Подкоманда login local vty d.
A transport input ssh vty subcommand 3.|Подкоманда транспортного ввода ssh vty 3.
An engineer had formerly configured a Cisco 2960 switch to allow Telnet access so that the switch expected a password of mypassword from the Telnet user.|Инженер ранее настроил коммутатор Cisco 2960 для разрешения доступа через Telnet, чтобы коммутатор ожидал ввода пароля mypassword от пользователя Telnet.
The engineer then changed the configuration to support Secure Shell.|Затем инженер изменил конфигурацию для поддержки Secure Shell.
Which of the following commands could have been part of the new configuration? (Choose two answers.)|Какая из следующих команд могла быть частью новой конфигурации? (Выберите два ответа.)
a. A username name secret password vty mode subcommand b.|а. Подкоманда vty mode секретного пароля имени пользователя b.
A username name secret password global configuration command c.|Команда глобальной настройки имени пользователя, секретного пароля c.
A login local vty mode subcommand d.|Подкоманда входа в локальный режим VTY d.
A transport input ssh global configuration command 4.|Команда глобальной конфигурации транспортного входа ssh 4.
An engineer’s desktop PC connects to a switch at the main site.|Настольный компьютер инженера подключается к коммутатору на главном объекте.
A router at the main site connects to each branch office through a serial link, with one small router and switch at each branch.|Маршрутизатор на главном сайте подключается к каждому филиалу через последовательный канал с одним небольшим маршрутизатором и коммутатором в каждом филиале.
Which of the following commands must be configured on the branch office switches, in the listed configuration mode, to allow the engineer to telnet to the branch office switches and supply only a password to login? (Choose three answers.)|Какая из следующих команд должна быть настроена на коммутаторах филиала в указанном режиме конфигурации, чтобы позволить инженеру подключаться к коммутаторам филиала по telnet и предоставлять только пароль для входа? (Выберите три ответа.)
a. The ip address command in interface configuration mode b.|а. Команда ip address в режиме настройки интерфейса b.
The ip address command in global configuration mode c.|Команда ip address в режиме глобальной конфигурации c.
The ip default-gateway command in VLAN configuration mode d.|Команда ip default-gateway в режиме конфигурации VLAN d.
The ip default-gateway command in global configuration mode e.|Команда ip default-gateway в режиме глобальной конфигурации e.
The password command in console line configuration mode f.|Команда пароля в режиме настройки строки консоли f.
The password command in vty line configuration mode 5.|Команда пароля в режиме конфигурации vty line 5.
A Layer 2 switch configuration places all its physical ports into VLAN 2.|Конфигурация коммутатора уровня 2 помещает все свои физические порты в сеть VLAN 2.
The IP addressing plan shows that address 172.16.2.250 (with mask 255.255.255.0) is reserved for use by this new LAN switch and that 172.16.2.254 is already configured on the router connected to that same VLAN. The switch needs to support SSH connections into the switch from any subnet in the network.|План IP-адресации показывает, что адрес 172.16.2.250 (с маской 255.255.255.0) зарезервирован для использования этим новым коммутатором LAN и что 172.16.2.254 уже настроен на маршрутизаторе, подключенном к той же VLAN. Коммутатор должен поддерживать SSH-подключения к коммутатору из любой подсети в сети.
Which of the following commands are part of the required configuration in this case? (Choose two answers.)|Какие из следующих команд являются частью необходимой конфигурации в этом случае? (Выберите два ответа.)
a. The ip address 172.16.2.250 255.255.255.0 command in interface vlan 1 configuration mode.|а. Команда ip address 172.16.2.250 255.255.255.0 в режиме настройки интерфейса vlan 1.
b. The ip address 172.16.2.250 255.255.255.0 command in interface vlan 2 configuration mode.|б. Команда ip address 172.16.2.250 255.255.255.0 в режиме настройки интерфейса vlan 2.
c. The ip default-gateway 172.16.2.254 command in global configuration mode.|c. Команда ip default-gateway 172.16.2.254 в режиме глобальной конфигурации.
d. The switch cannot support SSH because all its ports connect to VLAN 2, and the IP address must be configured on interface VLAN 1.|d. Коммутатор не может поддерживать SSH, потому что все его порты подключаются к VLAN 2, а IP-адрес должен быть настроен на интерфейсе VLAN 1.
6. Which of the following line subcommands tells a switch to wait until a show command’s output has completed before displaying log messages on the screen?|6. Какая из следующих подкоманд в строке указывает коммутатору дождаться завершения вывода команды show перед отображением сообщений журнала на экране?
a. logging synchronous b. no ip domain-lookup c. exec-timeout 0 0 d. history size 15 Foundation Topics Securing the Switch CLI By default, a Cisco Catalyst switch allows anyone to connect to the console port, access user mode, and then move on to enable and configuration modes without any kind of security.|а. регистрация синхронная b. нет IP-поиска домена c. exec-timeout 0 0 d. размер истории 15 Основные темы Защита интерфейса командной строки коммутатора По умолчанию коммутатор Cisco Catalyst позволяет любому подключиться к консольному порту, получить доступ к пользовательскому режиму, а затем перейти к включению и настройке режимов без какой-либо защиты.
That default makes sense, given that if you can get to the console port of the switch, you already have control over the switch physically.|Это значение по умолчанию имеет смысл, учитывая, что если вы можете получить доступ к консольному порту коммутатора, у вас уже есть физический контроль над коммутатором.
However, everyone needs to operate switches remotely, and the first step in that process is to secure the switch so that only the appropriate users can access the switch command-line interface (CLI).|Однако всем необходимо управлять коммутаторами удаленно, и первым шагом в этом процессе является защита коммутатора, чтобы только соответствующие пользователи могли получить доступ к интерфейсу командной строки коммутатора (CLI).
This first topic in the chapter examines how to configure login security for a Cisco Catalyst switch.|В этом первом разделе главы рассматривается, как настроить безопасность входа в систему для коммутатора Cisco Catalyst.
Securing the CLI includes protecting access to enable mode, because from enable mode, an attacker could reload the switch or change the configuration.|Защита интерфейса командной строки включает в себя защиту доступа в активный режим, поскольку из этого режима злоумышленник может перезагрузить коммутатор или изменить конфигурацию.
Protecting user mode is also important, because attackers can see the status of the switch, learn about the network, and find new ways to attack the network.|Защита пользовательского режима также важна, потому что злоумышленники могут видеть состояние коммутатора, узнавать о сети и находить новые способы атаки на сеть.
Note that all remote access and management protocols require that the switch IP configuration be completed and working.|Обратите внимание, что все протоколы удаленного доступа и управления требуют, чтобы IP-конфигурация коммутатора была завершена и работала.
A switch’s IPv4 configuration has nothing to do with how a Layer 2 switch forwards Ethernet frames (as discussed in Chapter 5, “Analyzing Ethernet LAN Switching”).|Конфигурация IPv4 коммутатора не имеет ничего общего с тем, как коммутатор уровня 2 пересылает кадры Ethernet (как описано в главе 5 «Анализ коммутации Ethernet LAN»).
Instead, to support Telnet and Secure Shell (SSH) into a switch, the switch needs to be configured with an IP address.|Вместо этого для поддержки Telnet и Secure Shell (SSH) в коммутаторе необходимо настроить коммутатор с IP-адресом.
This chapter also shows how to configure a switch’s IPv4 settings in the upcoming section “Enabling IPv4 for Remote Access.”|В этой главе также показано, как настроить параметры IPv4 коммутатора в следующем разделе «Включение IPv4 для удаленного доступа».
In particular, this section covers the following login security topics:|В частности, в этом разделе рассматриваются следующие темы безопасности входа в систему:
###### Securing user mode and privileged mode with simple passwords
Защита пользовательского режима и привилегированного режима с помощью простых паролей   
###### Securing user mode access with local usernames
Обеспечение доступа в пользовательском режиме с помощью локальных имен пользователей   
###### Securing user mode access with external authentication servers
Обеспечение доступа в пользовательском режиме с помощью внешних серверов аутентификации   
###### Securing remote access with Secure Shell (SSH)
Обеспечение удаленного доступа с помощью Secure Shell (SSH)   
#### Securing User Mode and Privileged Mode with Simple Passwords
Защита пользовательского режима и привилегированного режима с помощью простых паролей   
__|__
--|--
By default, Cisco Catalyst switches allow full access from the console but no access via Telnet or SSH. Using default settings, a console user can move into user mode and then privileged mode with no passwords required; however, default settings prevent remote users from accessing even user mode.|По умолчанию коммутаторы Cisco Catalyst разрешают полный доступ с консоли, но не разрешают доступ через Telnet или SSH. Используя настройки по умолчанию, пользователь консоли может перейти в пользовательский режим, а затем в привилегированный режим без необходимости ввода пароля; однако настройки по умолчанию не позволяют удаленным пользователям получить доступ даже к пользовательскому режиму.
The defaults work great for a brand new switch, but in production, you will want to secure access through the console as well as enable remote login via Telnet and/or SSH so you can sit at your desk and log in to all the switches in the LAN. Keep in mind, however, that you should not open the switch for just anyone to log in and change the configuration, so some type of secure login should be used.|Значения по умолчанию отлично подходят для нового коммутатора, но на производстве вам потребуется обеспечить безопасный доступ через консоль, а также включить удаленный вход через Telnet и / или SSH, чтобы вы могли сидеть за своим столом и входить на все коммутаторы. ЛВС. Однако имейте в виду, что вы не должны открывать переключатель, чтобы кто-либо мог войти в систему и изменить конфигурацию, поэтому следует использовать какой-либо тип безопасного входа.
Most people use a simple shared password for access to lab gear.|Большинство людей используют простой общий пароль для доступа к лабораторному оборудованию.
This method uses a password only—with no username—with one password for console users and a different password for Telnet users.|В этом методе используется только пароль - без имени пользователя - с одним паролем для пользователей консоли и другим паролем для пользователей Telnet.
Console users must supply the console password, as configured in console line configuration mode.|Пользователи консоли должны указать пароль консоли, настроенный в режиме конфигурации строки консоли.
Telnet users must supply the Telnet password, also called the vty password, so called because the configuration sits in vty line configuration mode.|Пользователи Telnet должны предоставить пароль Telnet, также называемый паролем vty, так называемый, потому что конфигурация находится в режиме конфигурации линии vty.
Figure 6-1 summarizes these options for using shared passwords from the perspective of the user logging in to the switch.|На рис. 6-1 показаны эти варианты использования общих паролей с точки зрения входа пользователя в коммутатор.
Figure 6-1 Simple Password Security Concepts NOTE This section refers to several passwords as shared passwords.|Рисунок 6-1 Простые концепции защиты паролей ПРИМЕЧАНИЕ В этом разделе несколько паролей называются общими паролями.
Users share these passwords in that all users must know and use that same password.|Пользователи разделяют эти пароли, поскольку все пользователи должны знать и использовать один и тот же пароль.
In other words, each user does not have a unique username/password to use, but rather, all the appropriate staff knows and uses the same password.|Другими словами, у каждого пользователя нет уникального имени пользователя / пароля для использования, скорее, весь соответствующий персонал знает и использует один и тот же пароль.
In addition, Cisco switches protect enable mode (also called privileged mode) with yet another shared password called the enable password.|Кроме того, коммутаторы Cisco защищают режим включения (также называемый привилегированным режимом) еще одним общим паролем, который называется паролем включения.
From the perspective of the network engineer connecting to the CLI of the switch, once in user mode, the user types the enable EXEC command.|С точки зрения сетевого инженера, подключающегося к интерфейсу командной строки коммутатора, в пользовательском режиме пользователь вводит команду enable EXEC.
This command prompts the user for this enable password; if the user types the correct password, IOS moves the user to enable mode.|Эта команда запрашивает у пользователя этот пароль включения; если пользователь вводит правильный пароль, IOS переводит пользователя в режим включения.
Example 6-1 shows an example of the user experience of logging in to a switch from the console when the shared console password and the shared enable password have both been set.|В примере 6-1 показан пример пользовательского опыта входа в систему на коммутаторе с консоли, когда были установлены как пароль общей консоли, так и общий пароль включения.
Note that before this example began, the user started the terminal emulator, physically connected a laptop to the console cable, and then pressed the Return key to make the switch respond as shown at the top of the example.|Обратите внимание, что до того, как этот пример начался, пользователь запустил эмулятор терминала, физически подключил портативный компьютер к консольному кабелю, а затем нажал клавишу Return, чтобы переключатель сработал, как показано в верхней части примера.
Example 6-1 Console Login and Movement to Enable Mode Example end.|Пример 6-1. Вход в консоль и переход в режим включения. Пример конец.
Note that the example shows the password text as if typed (faith and love), along with the enable command that moves the user from user mode to enable mode.|Обратите внимание, что в примере показан текст пароля, как если бы он был введен (вера и любовь), вместе с командой enable, которая переводит пользователя из режима пользователя в режим включения.
In reality, the switch hides the passwords when typed, to prevent someone from reading over your shoulder to see the passwords.|На самом деле переключатель скрывает пароли при вводе, чтобы никто не прочитал через ваше плечо, чтобы увидеть пароли.
To configure the shared passwords for the console, Telnet, and for enable mode, you need to configure several commands.|Чтобы настроить общие пароли для консоли, Telnet и для режима включения, вам необходимо настроить несколько команд.
However, the parameters of the commands can be pretty intuitive.|Однако параметры команд могут быть довольно интуитивно понятными.
Figure 6-2 shows the configuration of all three of these passwords.|На рис. 6-2 показана конфигурация всех трех паролей.
The configuration for these three passwords does not require a lot of work.|Настройка этих трех паролей не требует много работы.
First, the console and vty password configuration sets the password based on the context: console mode for the console (line con 0), and vty line configuration mode for the Telnet password (line vty 0 15).|Во-первых, конфигурация консоли и пароля vty устанавливает пароль на основе контекста: режим консоли для консоли (строка con 0) и режим конфигурации строки vty для пароля Telnet (строка vty 0 15).
Figure 6-2 Simple Password Security Configuration The configured enable password, shown on the right side of the figure, applies to all users, no matter whether they connect to user mode via the console, Telnet, or otherwise.|Рис. 6-2 Конфигурация безопасности с простым паролем. Сконфигурированный пароль включения, показанный в правой части рисунка, применяется ко всем пользователям, независимо от того, подключаются ли они к пользовательскому режиму через консоль, Telnet или иначе.
The command to configure the enable password is a global configuration command: enable secret password-value.|Команда для настройки пароля включения является командой глобальной конфигурации: enable secret password-value.
NOTE Older IOS versions used the command enable password password-value to set the enable password, and that command still exists in IOS. However, the enable secret command is much more secure.|ПРИМЕЧАНИЕ. В более ранних версиях IOS для установки пароля включения использовалась команда enable password password-value, и эта команда все еще существует в IOS. Однако команда enable secret намного безопаснее.
In real networks, use enable secret.|В реальных сетях используйте enable secret.
Chapter 5, “Securing Network security levels of various password mechanisms, including a comparison of the enable secret and enable password commands.|Глава 5, «Обеспечение уровней безопасности сети различных механизмов паролей, включая сравнение команд enable secret и enable password.
To help you follow the process, and for easier study later, use the configuration checklist before the example.|Чтобы помочь вам следить за процессом и облегчить дальнейшее изучение, используйте контрольный список конфигурации перед примером.
The configuration checklist collects the required and optional steps to configure a feature as described in this book.|В контрольном списке конфигурации собраны необходимые и дополнительные шаги для настройки функции, как описано в этой книге.
The configuration checklist for shared passwords for the console, Telnet, and enable passwords is Step 1.|Контрольный список конфигурации для общих паролей для консоли, Telnet и паролей включения - это Шаг 1.
Configure the enable password with the enable secret password-value command.|Настройте пароль включения с помощью команды enable secret password-value.
Step 2.|Шаг 2.
Configure the console password:|Настройте пароль консоли:
A. Use the line con 0 command to enter console configuration mode.|A. Используйте команду line con 0 для входа в режим настройки консоли.
B. Use the password password-value subcommand to set the value of the console password.|B. Используйте подкоманду password password-value, чтобы установить значение пароля консоли.
C. Use the login subcommand to enable console password security using a simple password.|C. Используйте подкоманду login, чтобы включить защиту паролем консоли с помощью простого пароля.
Config Checklist Step 3.|Контрольный список конфигурации Шаг 3.
Configure the Telnet (vty) password:|Настройте пароль Telnet (vty):
A. Use the line vty 0 15 command to enter vty configuration mode for all 16 vty lines (numbered 0 through 15).|A. Используйте команду line vty 0 15, чтобы войти в режим конфигурации VTY для всех 16 линий VTY (пронумерованных от 0 до 15).
B. Use the password password-value subcommand to set the value of the console password.|B. Используйте подкоманду password password-value, чтобы установить значение пароля консоли.
C. Use the login subcommand to enable console password security using a simple password.|C. Используйте подкоманду login, чтобы включить защиту паролем консоли с помощью простого пароля.
Example 6-2 shows the configuration process as noted in the configuration checklist, along with setting the enable secret password.|В примере 6-2 показан процесс настройки, указанный в контрольном списке конфигурации, а также установка секретного пароля включения.
Note that the lines which begin with a ! are comment lines; they are there to guide you through the configuration.|Обратите внимание, что строки, начинающиеся с символа! строки комментариев; они помогут вам в настройке.
Example 6-2 Configuring Basic Passwords Example end.|Пример 6-2 Настройка основных паролей Пример конец.
Example 6-3 shows the resulting configuration in the switch per the show running-config command.|В примере 6-3 показана результирующая конфигурация коммутатора для команды show running-config.
The gray lines highlight the new configuration.|Серые линии выделяют новую конфигурацию.
Note that many unrelated lines of output have been deleted from the output to keep focused on the password configuration.|Обратите внимание, что многие несвязанные строки вывода были удалены из вывода, чтобы сосредоточиться на конфигурации пароля.
Example 6-3 Resulting Running-Config File (Subset) Per Example 6-2 Configuration Example end.|Пример 6-3 Полученный файл рабочей конфигурации (подмножество) Согласно примеру 6-2 Пример конфигурации конец.
NOTE For historical reasons, the output of the show running-config command, in the last six lines of Example 6-3, separates the first five vty lines (0 through 4) from the rest (5 through 15).|ПРИМЕЧАНИЕ. По историческим причинам выходные данные команды show running-config в последних шести строках примера 6-3 отделяют первые пять строк vty (с 0 по 4) от остальных (с 5 по 15).
#### Securing User Mode Access with Local Usernames and Passwords
Защита доступа в режиме пользователя с помощью локальных имен пользователей и паролей   
__|__
--|--
Cisco switches support two other login security methods that both use per-user username/|Коммутаторы Cisco поддерживают два других метода безопасности входа в систему, которые используют для каждого пользователя имя пользователя /
password pairs instead of a shared password with no username.|пары паролей вместо общего пароля без имени пользователя.
One method, referred to as local usernames and passwords, configures the username/password pairs locally—that is, in the switch’s configuration.|Один метод, называемый локальными именами пользователей и паролями, настраивает пары имя пользователя / пароль локально, то есть в конфигурации коммутатора.
Switches support this local username/password option for the console, for Telnet, and even for SSH, but do not replace the enable password used to reach enable mode.|Коммутаторы поддерживают этот параметр локального имени пользователя и пароля для консоли, для Telnet и даже для SSH, но не заменяют пароль включения, используемый для перехода в режим включения.
The configuration to migrate from using the simple shared passwords to instead using local usernames/passwords requires only some small configuration changes, as shown in Figure 6-3.|Конфигурация для перехода от использования простых общих паролей к использованию локальных имен пользователей / паролей требует лишь некоторых небольших изменений конфигурации, как показано на рисунке 6-3.
Figure 6-3 Configuring Switches to Use Local Username Login Authentication Working through the configuration in the figure, first, the switch of course needs to know the list of username/password pairs.|Рис. 6-3 Настройка коммутаторов для использования аутентификации при входе в систему с локальным именем пользователя Работая с конфигурацией, показанной на рисунке, сначала коммутатор, конечно, должен знать список пар имя пользователя / пароль.
To create these, repeatedly use the username name secret password global configuration command.|Для их создания несколько раз используйте команду глобальной конфигурации username name secret password.
Then, to enable this different type of console or Telnet security, simply enable this login security method with the login local line.|Затем, чтобы включить этот другой тип консоли или безопасности Telnet, просто включите этот метод безопасности входа в систему с помощью локальной линии входа.
Basically, this command means “use the local list of usernames for login.” You can also use the no password command (without even typing in the password) to clean up any remaining password subcommands from console or vty mode because these commands are not needed when using local usernames and passwords.|По сути, эта команда означает «использовать локальный список имен пользователей для входа». Вы также можете использовать команду no password (даже не вводя пароль) для очистки любых оставшихся подкоманд пароля из режима консоли или vty, поскольку эти команды не нужны при использовании локальных имен пользователей и паролей.
The following checklist details the commands to configure local username login, mainly as a method for easier study and review:|В следующем контрольном списке подробно описаны команды для настройки входа в систему с локальным именем пользователя, в основном как метод для облегчения изучения и проверки:
Step 1.|Шаг 1.
Use the username name secret password global configuration command to add one or more username/password pairs on the local switch.|Используйте команду глобальной конфигурации username name secret password, чтобы добавить одну или несколько пар имя пользователя / пароль на локальном коммутаторе.
Step 2.|Шаг 2.
Configure the console to use locally configured username/password pairs:|Настройте консоль для использования локально настроенных пар имени пользователя и пароля:
A. Use the line con 0 command to enter console configuration mode.|A. Используйте команду line con 0 для входа в режим настройки консоли.
B. Use the login local subcommand to enable the console to prompt for both username and password, checked versus the list of local usernames/passwords.|B. Используйте подкоманду login local, чтобы консоль запрашивала как имя пользователя, так и пароль, проверенные по сравнению со списком локальных имен пользователей / паролей.
C. (Optional) Use the no password subcommand to remove any existing simple shared passwords, just for good housekeeping of the configuration file.|C. (Необязательно) Используйте подкоманду no password, чтобы удалить все существующие простые общие пароли, просто для хорошего обслуживания файла конфигурации.
Step 3.|Шаг 3.
Configure Telnet (vty) to use locally configured username/password pairs.|Настройте Telnet (vty) для использования локально настроенных пар имя пользователя / пароль.
A. Use the line vty 0 15 command to enter vty configuration mode for all 16 vty lines (numbered 0 through 15).|A. Используйте команду line vty 0 15, чтобы войти в режим конфигурации VTY для всех 16 линий VTY (пронумерованных от 0 до 15).
B. Use the login local subcommand to enable the switch to prompt for both username and password for all inbound Telnet users, checked versus the list of local usernames/passwords.|B. Используйте подкоманду login local, чтобы коммутатор запрашивал имя пользователя и пароль для всех входящих пользователей Telnet, проверенных по сравнению со списком локальных имен пользователей / паролей.
C. (Optional) Use the no password subcommand to remove any existing simple shared passwords, just for good housekeeping of the configuration file.|C. (Необязательно) Используйте подкоманду no password, чтобы удалить все существующие простые общие пароли, просто для хорошего обслуживания файла конфигурации.
Config Checklist When a Telnet user connects to the switch configured as shown in Figure 6-3, the user will be prompted first for a username and then for a password, as shown in Example 6-4.|Контрольный список конфигурации Когда пользователь Telnet подключается к коммутатору, настроенному, как показано на рисунке 6-3, пользователю сначала будет предложено ввести имя пользователя, а затем пароль, как показано в примере 6-4.
The username/password pair must be from the list of local usernames; otherwise, the login is rejected.|Пара имя пользователя / пароль должна быть из списка локальных имен пользователей; в противном случае вход в систему отклоняется.
Example 6-4 Telnet Login Process After Applying Configuration in Figure 6-3 Example end.|Пример 6-4. Процесс входа в Telnet после применения конфигурации, показанной на рисунке 6-3. Конец примера.
NOTE Example 6-4 does not show the password value as having been typed because Cisco switches do not display the typed password for security reasons.|ПРИМЕЧАНИЕ. Пример 6-4 не показывает значение пароля как введенное, поскольку коммутаторы Cisco не отображают введенный пароль по соображениям безопасности.
#### Securing User Mode Access with External Authentication Servers
Защита доступа в режиме пользователя с помощью внешних серверов аутентификации   
__|__
--|--
The end of Example 6-4 points out one of the many security improvements when requiring each user to log in with their own username.|В конце примера 6-4 указано на одно из многих улучшений безопасности, когда от каждого пользователя требуется входить под своим именем.
The end of the example shows the user entering configuration mode (configure terminal) and then immediately leaving (end).|В конце примера показано, как пользователь входит в режим конфигурации (терминал настройки), а затем немедленно выходит (конец).
Note that when a user exits configuration mode, the switch generates a log message.|Обратите внимание, что когда пользователь выходит из режима конфигурации, коммутатор генерирует сообщение журнала.
If the user logged in with a username, the log message identifies that username; note the “wendell” in the log message.|Если пользователь вошел в систему с именем пользователя, сообщение журнала идентифицирует это имя пользователя; обратите внимание на «wendell» в сообщении журнала.
However, using a username/password configured directly on the switch causes some administrative headaches.|Однако использование имени пользователя и пароля, настроенного непосредственно на коммутаторе, вызывает некоторые административные проблемы.
For instance, every switch and router needs the configuration for all users who might need to log in to the devices.|Например, каждому коммутатору и маршрутизатору требуется конфигурация для всех пользователей, которым может потребоваться вход на устройства.
Then, when any changes need to happen, like an occasional change to the passwords for good security practices, the configuration of all devices must be changed.|Затем, когда должны произойти какие-либо изменения, например, случайное изменение паролей для надлежащей практики безопасности, необходимо изменить конфигурацию всех устройств.
A better option would be to use tools like those used for many other IT login functions.|Лучшим вариантом было бы использовать инструменты, подобные тем, которые используются для многих других функций входа в систему.
Those tools allow for a central place to securely store all username/password pairs, with tools to make users change their passwords regularly, tools to revoke users when they leave their current jobs, and so on.|Эти инструменты представляют собой централизованное место для безопасного хранения всех пар имени пользователя и пароля, с инструментами, позволяющими пользователям регулярно менять свои пароли, инструментами для отзыва пользователей, когда они покидают свою текущую работу, и так далее.
Cisco switches allow exactly that option using an external server called an authentication, authorization, and accounting (AAA) server.|Коммутаторы Cisco позволяют использовать именно этот вариант с использованием внешнего сервера, называемого сервером аутентификации, авторизации и учета (AAA).
These servers hold the usernames/passwords.|На этих серверах хранятся имена пользователей / пароли.
Typically, these servers allow users to do self-service and forced maintenance to their passwords.|Обычно эти серверы позволяют пользователям выполнять самообслуживание и принудительное обслуживание своих паролей.
Many production networks use AAA servers for their switches and routers today.|Сегодня многие производственные сети используют серверы AAA для своих коммутаторов и маршрутизаторов.
The underlying login process requires some additional work on the part of the switch for each user login, but once set up, the username/password administration is much less.|Базовый процесс входа в систему требует некоторой дополнительной работы со стороны коммутатора для каждого входа пользователя в систему, но после настройки администрирование имени пользователя / пароля намного меньше.
When using a AAA server for authentication, the switch (or router) simply sends a message to the AAA server asking whether the username and password are allowed, and the AAA server replies.|При использовании сервера AAA для аутентификации коммутатор (или маршрутизатор) просто отправляет сообщение серверу AAA, спрашивая, разрешены ли имя пользователя и пароль, и сервер AAA отвечает.
Figure 6-4 shows an example, with the user first supplying a username/password, the switch asking the AAA server, and the server replying to the switch stating that the username/|На рис. 6-4 показан пример, в котором пользователь сначала вводит имя пользователя / пароль, коммутатор запрашивает сервер AAA, а сервер отвечает коммутатору, заявляя, что имя пользователя /
password is valid.|пароль действителен.
Figure 6-4 Basic Authentication Process with an External AAA Server While the figure shows the general idea, note that the information flows with a couple of different protocols.|Рис. 6-4. Базовый процесс аутентификации с внешним сервером AAA Хотя на рисунке показана общая идея, обратите внимание, что информация передается по нескольким различным протоколам.
On the left, the connection between the user and the switch or router uses Telnet or SSH. On the right, the switch and AAA server typically use either the RADIUS or TACACS+ protocol, both of which encrypt the passwords as they traverse the network.|Слева соединение между пользователем и коммутатором или маршрутизатором использует Telnet или SSH. Справа коммутатор и сервер AAA обычно используют протокол RADIUS или TACACS +, оба из которых шифруют пароли при прохождении через сеть.
#### Securing Remote Access with Secure Shell
Защита удаленного доступа с помощью Secure Shell   
__|__
--|--
So far, this chapter has focused on the console and on Telnet, mostly ignoring SSH. Telnet has one serious disadvantage: all data in the Telnet session flows as clear text, including the password exchanges.|До сих пор в этой главе основное внимание уделялось консоли и Telnet, в основном игнорируя SSH. У Telnet есть один серьезный недостаток: все данные в сеансе Telnet передаются в виде открытого текста, включая обмен паролями.
So, anyone that can capture the messages between the user and the switch (in what is called a man-in-the-middle attack) can see the passwords.|Таким образом, любой, кто может перехватывать сообщения между пользователем и коммутатором (в так называемой атаке «человек посередине»), может видеть пароли.
SSH encrypts all data transmitted between the SSH client and server, protecting the data and passwords.|SSH шифрует все данные, передаваемые между SSH-клиентом и сервером, защищая данные и пароли.
SSH can use the same local login authentication method as Telnet, with the locally configured username and password. (SSH cannot rely on authentication methods that do not include a username, like shared passwords.) So, the configuration to support local usernames for Telnet, as shown previously in Figure 6-3, also enables local username authentication for incoming SSH connections.|SSH может использовать тот же метод локальной аутентификации при входе, что и Telnet, с локально настроенными именем пользователя и паролем. (SSH не может полагаться на методы аутентификации, которые не включают имя пользователя, например общие пароли.) Таким образом, конфигурация для поддержки локальных имен пользователей для Telnet, как показано ранее на рис. 6-3, также включает аутентификацию локального имени пользователя для входящих SSH-соединений.
Figure 6-5 shows one example configuration of what is required to support SSH. The figure repeats the local username configuration as shown earlier in Figure 6-3, as used for Telnet.|На рис. 6-5 показан один пример конфигурации того, что требуется для поддержки SSH. На рисунке повторяется конфигурация локального имени пользователя, показанная ранее на рисунке 6-3, использованная для Telnet.
Figure 6-5 shows three additional commands required to complete the configuration of SSH on the switch.|На рис. 6-5 показаны три дополнительные команды, необходимые для завершения настройки SSH на коммутаторе.
Figure 6-5 Adding SSH Configuration to Local Username Configuration IOS uses the three SSH-specific configuration commands in the figure to create the SSH encryption keys.|Рис. 6-5. Добавление конфигурации SSH к конфигурации локального имени пользователя IOS использует три команды конфигурации, специфичные для SSH, показанные на рисунке, для создания ключей шифрования SSH.
The SSH server uses the fully qualified domain name (FQDN) of the switch as input to create that key.|Сервер SSH использует полное доменное имя (FQDN) коммутатора в качестве входных данных для создания этого ключа.
The switch creates the FQDN from the hostname and domain name of the switch.|Коммутатор создает полное доменное имя из имени хоста и имени домена коммутатора.
Figure 6-5 begins by setting both values (just in case they are not already configured).|Рисунок 6-5 начинается с установки обоих значений (на случай, если они еще не настроены).
Then the third command, the crypto key generate rsa command, generates the SSH encryption keys.|Затем третья команда, команда crypto key generate rsa, генерирует ключи шифрования SSH.
The configuration in Figure 6-5 relies on two default settings that the figure therefore conveniently ignored.|Конфигурация на Рисунке 6-5 основана на двух настройках по умолчанию, которые поэтому удобно игнорировать.
IOS runs an SSH server by default.|IOS по умолчанию запускает SSH-сервер.
In addition, IOS allows SSH connections into the vty lines by default.|Кроме того, IOS по умолчанию разрешает SSH-подключения к линиям VTY.
Seeing the configuration happen in configuration mode, step by step, can be particularly helpful with SSH configuration.|Наблюдение за тем, как настройка происходит в режиме настройки, шаг за шагом, может быть особенно полезно при настройке SSH.
Note in particular that in this example, the crypto key command prompts the user for the key modulus; you could also add the parameters modulus modulus-value to the end of the crypto key command to add this setting on the command.|В частности, обратите внимание, что в этом примере команда криптографического ключа запрашивает у пользователя модуль ключа; вы также можете добавить параметры модуля значение модуля в конец команды криптографического ключа, чтобы добавить этот параметр в команду.
Example 6-5 shows the commands in Figure 6-5 being configured, with the encryption key as the final step.|В примере 6-5 показаны настраиваемые команды на рис. 6-5 с ключом шифрования в качестве последнего шага.
Example 6-5 SSH Configuration Process to Match Figure 6-5 Example end.|Пример 6-5. Процесс настройки SSH в соответствии с рисунком 6-5. Конец примера.
Earlier, I mentioned that one useful default was that the switch defaults to support both SSH and Telnet on the vty lines.|Ранее я упоминал, что одним полезным значением по умолчанию было то, что по умолчанию коммутатор поддерживает как SSH, так и Telnet на линиях VTY.
However, because Telnet is a security risk, you could disable Telnet to enforce a tighter security policy. (For that matter, you can disable SSH support and allow Telnet on the vty lines as well.)|Однако, поскольку Telnet представляет собой угрозу безопасности, вы можете отключить Telnet, чтобы обеспечить более жесткую политику безопасности. (В этом отношении вы можете отключить поддержку SSH и разрешить Telnet на линиях VTY.)
To control which protocols a switch supports on its vty lines, use the transport input {all ||Чтобы контролировать, какие протоколы поддерживает коммутатор на своих линиях VTY, используйте транспортный вход {all none | telnet | ssh} vty subcommand in vty mode, with the following options:|нет | телнет | ssh} подкоманда vty в режиме vty со следующими параметрами:
transport input all or transport input telnet ssh: Support both Telnet and SSH transport input none: Support neither transport input telnet: Support only Telnet transport input ssh: Support only SSH To complete this section about SSH, the following configuration checklist details the steps for one method to configure a Cisco switch to support SSH using local usernames. (SSH support in IOS can be configured in several ways; this checklist shows one simple way to configure it.) The process shown here ends with a comment to configure local username support on vty lines, as was discussed earlier in the section titled “Securing User Mode Access with Local Usernames and Passwords.”|транспортный ввод все или транспортный ввод telnet ssh: Поддерживает как Telnet, так и SSH транспортный ввод нет: Не поддерживает ни один транспортный ввод telnet: Поддерживает только транспортный ввод Telnet ssh: Поддерживает только SSH Чтобы заполнить этот раздел о SSH, в следующем контрольном списке конфигурации подробно описаны шаги для одного метод настройки коммутатора Cisco для поддержки SSH с использованием локальных имен пользователей. (Поддержка SSH в IOS может быть настроена несколькими способами; в этом контрольном списке показан один простой способ ее настройки.) Показанный здесь процесс заканчивается комментарием для настройки поддержки локального имени пользователя в строках vty, как обсуждалось ранее в разделе под названием «Защита Доступ в пользовательском режиме с локальными именами пользователей и паролями ».
Step 1.|Шаг 1.
Configure the switch to generate a matched public and private key pair to use for encryption:|Настройте коммутатор для создания согласованной пары открытого и закрытого ключей для использования для шифрования:
A. If not already configured, use the hostname name in global configuration mode to configure a hostname for this switch.|A. Если еще не настроен, используйте имя хоста в режиме глобальной конфигурации, чтобы настроить имя хоста для этого коммутатора.
Config Checklist B.|Контрольный список конфигурации B.
If not already configured, use the ip domain-name name in global configuration mode to configure a domain name for the switch, completing the switch’s FQDN.|Если это еще не было настроено, используйте имя домена ip в режиме глобальной конфигурации, чтобы настроить имя домена для коммутатора, заполнив его полное доменное имя.
C. Use the crypto key generate rsa command in global configuration mode (or the crypto key generate rsa modulus modulus-value command to avoid being prompted for the key modulus) to generate the keys. (Use at least a 768-bit key to support SSH version 2.)|C. Используйте команду crypto key generate rsa в режиме глобальной конфигурации (или команду crypto key generate rsa modulus-value, чтобы не запрашивать модуль ключа) для генерации ключей. (Используйте как минимум 768-битный ключ для поддержки SSH версии 2.)
Step 2. (Optional) Use the ip ssh version 2 command in global configuration mode to override the default of supporting both versions 1 and 2, so that only SSHv2 connections are allowed.|Шаг 2. (Необязательно) Используйте команду ip ssh version 2 в режиме глобальной конфигурации, чтобы изменить значение по умолчанию, поддерживающее обе версии 1 и 2, чтобы были разрешены только соединения SSHv2.
Step 3. (Optional) If not already configured with the setting you want, configure the vty lines to accept SSH and whether to also allow Telnet:|Шаг 3. (Необязательно) Если желаемый параметр еще не настроен, настройте линии VTY для приема SSH и разрешения Telnet:
A. Use the transport input ssh command in vty line configuration mode to allow SSH only.|A. Используйте команду transport input ssh в режиме конфигурации VTY, чтобы разрешить только SSH.
B. Use the transport input all command (default) or transport input telnet ssh command in vty line configuration mode to allow both SSH and Telnet.|B. Используйте команду transport input all (по умолчанию) или команду transport input telnet ssh в режиме конфигурации линии vty, чтобы разрешить использование SSH и Telnet.
Step 4.|Шаг 4.
Use various commands in vty line configuration mode to configure local username login authentication as discussed earlier in this chapter.|Используйте различные команды в режиме конфигурации линии VTY для настройки аутентификации при входе в систему с локальным именем пользователя, как обсуждалось ранее в этой главе.
NOTE Cisco routers often default to transport input none, so you must add the transport input line subcommand to enable Telnet and/or SSH into a router.|ПРИМЕЧАНИЕ. Маршрутизаторы Cisco часто по умолчанию не используют транспортный ввод, поэтому необходимо добавить подкоманду транспортной строки ввода, чтобы включить Telnet и / или SSH в маршрутизатор.
Two key commands give some information about the status of SSH on the switch.|Две ключевые команды дают некоторую информацию о состоянии SSH на коммутаторе.
First, the show ip ssh command lists status information about the SSH server itself.|Во-первых, команда show ip ssh выводит информацию о состоянии самого SSH-сервера.
The show ssh command then lists information about each SSH client currently connected into the switch.|Затем команда show ssh выводит информацию о каждом SSH-клиенте, который в данный момент подключен к коммутатору.
Example 6-6 shows samples of each, with user wendell currently connected to the switch.|В примере 6-6 показаны образцы каждого из них, когда пользователь Венделл в настоящее время подключен к коммутатору.
Example 6-6 Displaying SSH Status Example end.|Пример 6-6 Отображение статуса SSH Пример конец.
### Enabling IPv4 for Remote Access
Включение IPv4 для удаленного доступа   
__|__
--|--
To allow Telnet or SSH access to the switch, and to allow other IP-based management protocols (for example, Simple Network Management Protocol, or SNMP) to function as intended, the switch needs an IP address, as well as a few other related settings.|Чтобы разрешить доступ Telnet или SSH к коммутатору и разрешить другим протоколам управления на основе IP (например, Simple Network Management Protocol или SNMP) функционировать должным образом, коммутатору необходим IP-адрес, а также несколько других связанных настройки.
The IP address has nothing to do with how switches forward Ethernet frames; it simply exists to support overhead management traffic.|IP-адрес не имеет ничего общего с тем, как коммутаторы пересылают кадры Ethernet; он просто существует для поддержки служебного трафика управления.
This next topic begins by explaining the IPv4 settings needed on a switch, followed by the configuration.|Следующая тема начинается с объяснения настроек IPv4, необходимых для коммутатора, а затем с настройки.
Note that although switches can be configured with IPv6 addresses with commands similar to those shown in this chapter, this chapter focuses solely on IPv4.|Обратите внимание, что хотя коммутаторы могут быть настроены с адресами IPv6 с помощью команд, аналогичных тем, которые показаны в этой главе, эта глава посвящена исключительно IPv4.
All references to IP in this chapter imply IPv4.|Все ссылки на IP в этой главе подразумевают IPv4.
#### Host and Switch IP Settings
Настройки хоста и коммутатора IP   
__|__
--|--
A switch needs the same kind of IP settings as a PC with a single Ethernet interface.|Коммутатор требует таких же настроек IP, как и ПК с одним интерфейсом Ethernet.
For perspective, a PC has a CPU, with the operating system running on the CPU. It has an Ethernet network interface card (NIC). The OS configuration includes an IP address associated with the NIC, either configured or learned dynamically with DHCP.|Для сравнения: у ПК есть центральный процессор, на котором работает операционная система. Он имеет сетевую карту Ethernet (NIC). Конфигурация ОС включает IP-адрес, связанный с сетевой картой, настроенный или полученный динамически с помощью DHCP.
A switch uses the same ideas, except that the switch needs to use a virtual NIC inside the switch.|Коммутатор использует те же идеи, за исключением того, что коммутатор должен использовать виртуальную сетевую карту внутри коммутатора.
Like a PC, a switch has a real CPU, running an OS (called IOS). The switch obviously has lots of Ethernet ports, but instead of assigning its management IP address to any of those ports, the switch then uses a NIC-like concept called a switched virtual interface (SVI), or more commonly, a VLAN interface, that acts like the switch’s own NIC. Then the settings on the switch look something like a host, with the switch configuration assigning IP settings, like an IP address, to this VLAN interface, as shown in Figure 6-6.|Как и ПК, коммутатор имеет реальный ЦП, работающий под управлением ОС (называемой IOS). Коммутатор, очевидно, имеет множество портов Ethernet, но вместо того, чтобы назначать свой управляющий IP-адрес любому из этих портов, коммутатор затем использует концепцию, похожую на сетевую карту, называемую коммутируемым виртуальным интерфейсом (SVI), или, чаще, интерфейсом VLAN, который действует как собственный сетевой адаптер коммутатора. Тогда настройки на коммутаторе будут выглядеть примерно как хост, а конфигурация коммутатора назначает IP-настройки, такие как IP-адрес, этому интерфейсу VLAN, как показано на рис. 6-6.
Figure 6-6 Switch Virtual Interface (SVI) Concept Inside a Switch By using interface VLAN 1 for the IP configuration, the switch can then send and receive frames on any of the ports in VLAN 1.|Рисунок 6-6 Концепция виртуального интерфейса коммутатора (SVI) внутри коммутатора Используя интерфейс VLAN 1 для конфигурации IP, коммутатор может затем отправлять и получать кадры на любом из портов в VLAN 1.
In a Cisco switch, by default, all ports are assigned to VLAN 1.|В коммутаторе Cisco по умолчанию все порты назначены на VLAN 1.
In most networks, switches configure many VLANs, so the network engineer has a choice of where to configure the IP address.|В большинстве сетей коммутаторы настраивают множество VLAN, поэтому сетевой инженер может выбрать, где настроить IP-адрес.
That is, the management IP address does not have to be configured on the VLAN 1 interface (as configured with the interface vlan 1 command seen in Figure 6-6).|То есть IP-адрес управления не нужно настраивать на интерфейсе VLAN 1 (как настроено с помощью команды interface vlan 1, показанной на рис. 6-6).
A Layer 2 Cisco LAN switch needs only one IP address for management purposes.|Коммутатору Cisco LAN уровня 2 для управления нужен только один IP-адрес.
However, you can choose to use any VLAN to which the switch connects.|Однако вы можете использовать любую VLAN, к которой подключается коммутатор.
The configuration then includes a VLAN interface for that VLAN number, with an appropriate IP address.|Затем конфигурация включает интерфейс VLAN для этого номера VLAN с соответствующим IP-адресом.
For example, Figure 6-7 shows a Layer 2 switch with some physical ports in two different VLANs (VLANs 1 and 2).|Например, на рис. 6-7 показан коммутатор уровня 2 с некоторыми физическими портами в двух разных VLAN (VLAN 1 и 2).
The figure also shows the subnets used on those VLANs. The network engineer could choose to use either|На рисунке также показаны подсети, используемые в этих VLAN. Сетевой инженер может использовать либо
###### Interface VLAN 1, with an IP address in subnet 192.168.1.0
Интерфейс VLAN 1, с IP-адресом в подсети 192.168.1.0   
###### Interface VLAN 2, with an IP address in subnet 192.168.2.0.
Интерфейс VLAN 2 с IP-адресом в подсети 192.168.2.0.   
__|__
--|--
Figure 6-7 Choosing One VLAN on Which to Configure a Switch IP Address Note that you should not try to use a VLAN interface for which there are no physical ports assigned to the same VLAN. If you do, the VLAN interface will not reach an up/up state, and the switch will not have the physical ability to communicate outside the switch.|Рисунок 6-7 Выбор одной VLAN для настройки IP-адреса коммутатора Обратите внимание, что вам не следует пытаться использовать интерфейс VLAN, для которого нет физических портов, назначенных той же VLAN. Если вы это сделаете, интерфейс VLAN не перейдет в рабочее состояние, и у коммутатора не будет физической возможности взаимодействовать с ним вне коммутатора.
NOTE Some Cisco switches can be configured to act as either a Layer 2 switch or a Layer 3 switch.|ПРИМЕЧАНИЕ. Некоторые коммутаторы Cisco можно настроить для работы в качестве коммутатора уровня 2 или уровня 3.
When acting as a Layer 2 switch, a switch forwards Ethernet frames as discussed in depth in Chapter 5, “Analyzing Ethernet LAN Switching.” Alternatively, a switch can also act as a multilayer switch or Layer 3 switch, which means the switch can do both Layer 2 switching and Layer 3 IP routing of IP packets, using the Layer 3 logic normally used by routers.|При работе в качестве коммутатора уровня 2 коммутатор пересылает кадры Ethernet, как подробно описано в главе 5 «Анализ коммутации Ethernet LAN». В качестве альтернативы коммутатор также может действовать как многоуровневый коммутатор или коммутатор уровня 3, что означает, что коммутатор может выполнять как коммутацию уровня 2, так и IP-маршрутизацию уровня 3 IP-пакетов, используя логику уровня 3, обычно используемую маршрутизаторами.
This chapter assumes all switches are Layer 2 switches.|В этой главе предполагается, что все коммутаторы являются коммутаторами уровня 2.
Chapter 17, “IP Routing in the LAN,” discusses Layer 3 switching in depth along with using multiple VLAN interfaces at the same time.|В главе 17 «IP-маршрутизация в локальной сети» подробно рассматривается коммутация уровня 3 и одновременное использование нескольких интерфейсов VLAN.
Configuring the IP address (and mask) on one VLAN interface allows the switch to send and receive IP packets with other hosts in a subnet that exists on that VLAN; however, the switch cannot communicate outside the local subnet without another configuration setting called the default gateway.|Настройка IP-адреса (и маски) на одном интерфейсе VLAN позволяет коммутатору отправлять и получать IP-пакеты с другими узлами в подсети, которая существует в этой VLAN; однако коммутатор не может взаимодействовать за пределами локальной подсети без другого параметра конфигурации, который называется шлюзом по умолчанию.
The reason a switch needs a default gateway setting is the same reason that hosts need the same setting—because of how hosts think when sending IP packets.|Причина, по которой коммутатору нужна настройка шлюза по умолчанию, совпадает с той, по которой хостам нужны такие же настройки - из-за того, как хосты думают при отправке IP-пакетов.
Specifically:|В частности:
###### To send IP packets to hosts in the same subnet, send them directly
Чтобы отправлять IP-пакеты на хосты в той же подсети, отправьте их напрямую   
###### To send IP packets to hosts in a different subnet, send them to the local router; that is, the
Чтобы отправить IP-пакеты на хосты в другой подсети, отправьте их на локальный маршрутизатор; это   
__|__
--|--
default gateway Figure 6-8 shows the ideas.|шлюз по умолчанию На рис. 6-8 показаны идеи.
In this case, the switch (on the right) will use IP address 192.168.1.200 as configured on interface VLAN 1.|В этом случае коммутатор (справа) будет использовать IP-адрес 192.168.1.200, как настроено на интерфейсе VLAN 1.
However, to communicate with host A, on the far left of the figure, the switch must use Router R1 (the default gateway) to forward IP packets to host A.|Однако для связи с хостом A в крайнем левом углу рисунка коммутатор должен использовать маршрутизатор R1 (шлюз по умолчанию) для пересылки IP-пакетов на хост A.
To make that work, the switch needs to configure a default gateway setting, pointing to Router R1’s IP address (192.168.1.1 in this case).|Для этого коммутатору необходимо настроить шлюз по умолчанию, указав IP-адрес маршрутизатора R1 (в данном случае 192.168.1.1).
Note that the switch and router both use the same mask, 255.255.255.0, which puts the addresses in the same subnet.|Обратите внимание, что коммутатор и маршрутизатор используют одну и ту же маску 255.255.255.0, которая помещает адреса в одну подсеть.
Figure 6-8 The Need for a Default Gateway|Рисунок 6-8 Необходимость в шлюзе по умолчанию
#### Configuring IPv4 on a Switch
Настройка IPv4 на коммутаторе   
__|__
--|--
A switch configures its IPv4 address and mask on this special NIC-like VLAN interface.|Коммутатор настраивает свой IPv4-адрес и маску на этом специальном сетевом интерфейсе VLAN.
The following steps list the commands used to configure IPv4 on a switch, assuming that the IP address is configured to be in VLAN 1, with Example 6-7 that follows showing an example configuration.|В следующих шагах перечислены команды, используемые для настройки IPv4 на коммутаторе, при условии, что IP-адрес настроен для VLAN 1, а в следующем примере 6-7 показан пример конфигурации.
Step 1.|Шаг 1.
Use the interface vlan 1 command in global configuration mode to enter interface VLAN 1 configuration mode.|Используйте команду interface vlan 1 в режиме глобальной конфигурации, чтобы войти в режим конфигурации интерфейса VLAN 1.
Step 2.|Шаг 2.
Use the ip address ip-address mask command in interface configuration mode to assign an IP address and mask.|Используйте команду ip address ip-address mask в режиме настройки интерфейса, чтобы назначить IP-адрес и маску.
Step 3.|Шаг 3.
Use the no shutdown command in interface configuration mode to enable the VLAN 1 interface if it is not already enabled.|Используйте команду no shutdown в режиме настройки интерфейса, чтобы включить интерфейс VLAN 1, если он еще не включен.
Step 4.|Шаг 4.
Add the ip default-gateway ip-address command in global configuration mode to configure the default gateway.|Добавьте команду ip default-gateway ip-address в режиме глобальной конфигурации, чтобы настроить шлюз по умолчанию.
Step 5. (Optional) Add the ip name-server ip-address1 ip-address2 … command in global configuration mode to configure the switch to use Domain Name System (DNS) to resolve names into their matching IP address.|Шаг 5. (Необязательно) Добавьте команду ip name-server ip-address1 ip-address2… в режиме глобальной конфигурации, чтобы настроить коммутатор на использование системы доменных имен (DNS) для преобразования имен в соответствующие IP-адреса.
Example 6-7 Switch Static IP Address Configuration Example end.|Пример 6-7 Конфигурация статического IP-адреса коммутатора Конец примера.
On a side note, this example shows a particularly important and common command: the [no] shutdown command.|Кстати, в этом примере показана особенно важная и распространенная команда: команда [no] shutdown.
To administratively enable an interface on a switch, use the no shutdown interface subcommand; to disable an interface, use the shutdown interface subcommand.|Чтобы административно включить интерфейс на коммутаторе, используйте подкоманду no shutdown interface; чтобы отключить интерфейс, используйте подкоманду shutdown interface.
This command can be used on the physical Ethernet interfaces that the switch uses to switch Ethernet messages in addition to the VLAN interface shown here in this example.|Эту команду можно использовать на физических интерфейсах Ethernet, которые коммутатор использует для переключения сообщений Ethernet, в дополнение к интерфейсу VLAN, показанному здесь в этом примере.
Also, pause long enough to look at the messages that appear just below the no shutdown command in Example 6-7.|Кроме того, сделайте паузу достаточно долго, чтобы просмотреть сообщения, которые появляются сразу под командой no shutdown в примере 6-7.
Those messages are syslog messages generated by the switch stating that the switch did indeed enable the interface.|Эти сообщения представляют собой сообщения системного журнала, созданные коммутатором, в которых говорится, что коммутатор действительно включил интерфейс.
Switches (and routers) generate syslog messages in response to a variety of events, and by default, those messages appear at the console.|Коммутаторы (и маршрутизаторы) генерируют сообщения системного журнала в ответ на различные события, и по умолчанию эти сообщения появляются на консоли.
Chapter 9, “Device Management Protocols,” in the CCNA 200-301 Official Cert Guide, Volume 2, discusses syslog messages in more detail.|В главе 9 «Протоколы управления устройствами» в официальном руководстве по сертификации CCNA 200-301, том 2, сообщения системного журнала рассматриваются более подробно.
#### Configuring a Switch to Learn Its IP Address with DHCP
Настройка коммутатора для определения его IP-адреса с помощью DHCP   
__|__
--|--
The switch can also use Dynamic Host Configuration Protocol (DHCP) to dynamically learn its IPv4 settings.|Коммутатор также может использовать протокол динамической конфигурации хоста (DHCP) для динамического изучения настроек IPv4.
Basically, all you have to do is tell the switch to use DHCP on the interface and enable the interface.|По сути, все, что вам нужно сделать, это указать коммутатору использовать DHCP на интерфейсе и включить интерфейс.
Assuming that DHCP works in this network, the switch will learn all its settings.|Предполагая, что DHCP работает в этой сети, коммутатор узнает все его настройки.
The following list details the steps, again assuming the use of interface VLAN 1, with Example 6-8 that follows showing an example:|В следующем списке подробно описаны шаги, снова предполагая использование интерфейса VLAN 1, в следующем примере 6-8 показан пример:
Step 1.|Шаг 1.
Enter VLAN 1 configuration mode using the interface vlan 1 global configuration command, and enable the interface using the no shutdown command as necessary.|Войдите в режим конфигурации VLAN 1 с помощью команды глобальной конфигурации interface vlan 1 и включите интерфейс, используя команду no shutdown, если необходимо.
Step 2.|Шаг 2.
Assign an IP address and mask using the ip address dhcp interface subcommand.|Назначьте IP-адрес и маску с помощью подкоманды ip address dhcp interface.
Example 6-8 Switch Dynamic IP Address Configuration with DHCP Example end.|Пример 6-8 Переключить конфигурацию динамического IP-адреса с DHCP Пример конец.
#### Verifying IPv4 on a Switch
Проверка IPv4 на коммутаторе   
__|__
--|--
The switch IPv4 configuration can be checked in several places.|Конфигурацию IPv4 коммутатора можно проверить в нескольких местах.
First, you can always look at the current configuration using the show running-config command.|Во-первых, вы всегда можете посмотреть текущую конфигурацию с помощью команды show running-config.
Second, you can look at the IP address and mask information using the show interfaces vlan x command, which shows detailed status information about the VLAN interface in VLAN x.|Во-вторых, вы можете посмотреть информацию об IP-адресе и маске с помощью команды show interfaces vlan x, которая показывает подробную информацию о состоянии интерфейса VLAN в VLAN x.
Finally, if using DHCP, use the show dhcp lease command to see the (temporarily) leased IP address and other parameters. (Note that the switch does not store the DHCP-learned IP configuration in Config Checklist the running-config file.) Example 6-9 shows sample output from these commands to match the configuration in Example 6-8.|Наконец, при использовании DHCP используйте команду show dhcp lease, чтобы увидеть (временно) арендованный IP-адрес и другие параметры. (Обратите внимание, что коммутатор не сохраняет IP-конфигурацию, полученную с помощью DHCP, в контрольном списке конфигурации в файле рабочей конфигурации.) В примере 6-9 показан пример выходных данных этих команд, соответствующий конфигурации в примере 6-8.
Example 6-9 Verifying DHCP-Learned Information on a Switch Example end.|Пример 6-9 Проверка полученной DHCP информации на конце примера коммутатора.
The output of the show interfaces vlan 1 command lists two very important details related to switch IP addressing.|В выходных данных команды show interfaces vlan 1 перечислены две очень важные детали, относящиеся к IP-адресации коммутатора.
First, this show command lists the interface status of the VLAN 1 interface—in this case, “up and up.” If the VLAN 1 interface is not up, the switch cannot use its IP address to send and receive management traffic.|Во-первых, эта команда show перечисляет статус интерфейса интерфейса VLAN 1 - в данном случае «работает и работает». Если интерфейс VLAN 1 не работает, коммутатор не может использовать свой IP-адрес для отправки и получения трафика управления.
Notably, if you forget to issue the no shutdown command, the VLAN 1 interface remains in its default shutdown state and is listed as “administratively down” in the show command output.|Примечательно, что если вы забудете ввести команду no shutdown, интерфейс VLAN 1 останется в состоянии выключения по умолчанию и будет указан как «административно отключен» в выходных данных команды show.
Second, note that the output lists the interface’s IP address on the third line.|Во-вторых, обратите внимание, что вывод показывает IP-адрес интерфейса в третьей строке.
If you statically configure the IP address, as in Example 6-7, the IP address will always be listed; however, if you use DHCP and DHCP fails, the show interfaces vlan x command will not list an IP address here.|Если вы статически настраиваете IP-адрес, как в Примере 6-7, IP-адрес всегда будет указан; однако, если вы используете DHCP и DHCP не работает, команда show interfaces vlan x не будет указывать здесь IP-адрес.
When DHCP works, you can see the IP address with the show interfaces vlan 1 command, but that output does not remind you whether the address is either statically configured or DHCP leased.|Когда DHCP работает, вы можете увидеть IP-адрес с помощью команды show interfaces vlan 1, но эти выходные данные не напоминают вам, является ли адрес статическим или арендованным DHCP.
So it does take a little extra effort to make sure you know whether the address is statically configured or DHCP-learned on the VLAN interface.|Таким образом, требуется немного дополнительных усилий, чтобы убедиться, что вы знаете, является ли адрес статическим или полученным с помощью DHCP на интерфейсе VLAN.
### Miscellaneous Settings Useful in the Lab
Разные настройки, полезные в лаборатории   
__|__
--|--
This last short section of the chapter touches on a couple of commands that can help you be a little more productive when practicing in a lab.|Этот последний короткий раздел главы касается пары команд, которые могут помочь вам быть немного более продуктивными при занятиях в лаборатории.
#### History Buffer Commands
Команды буфера истории   
__|__
--|--
When you enter commands from the CLI, the switch saves the last several commands in the history buffer.|Когда вы вводите команды из CLI, коммутатор сохраняет последние несколько команд в буфере истории.
Then, as mentioned in Chapter 4, “Using the Command-Line Interface,” you can use the up-arrow key or press Ctrl+P to move back in the history buffer to retrieve a command you entered a few commands ago.|Затем, как упоминалось в главе 4 «Использование интерфейса командной строки», вы можете использовать клавишу со стрелкой вверх или нажать Ctrl + P, чтобы вернуться в буфер истории и получить команду, которую вы вводили несколько команд назад.
This feature makes it very easy and fast to use a set of commands repeatedly.|Эта функция позволяет очень легко и быстро многократно использовать набор команд.
Table 6-2 lists some of the key commands related to the history buffer.|В таблице 6-2 перечислены некоторые ключевые команды, относящиеся к буферу истории.
Table 6-2 Commands Related to the History Buffer Table end.|Таблица 6-2 Команды, относящиеся к концу таблицы буфера истории.
#### The logging synchronous, exec-timeout, and no ip domain-lookup Commands
Команды logging synchronous, exec-timeout и no ip domain-lookup   
__|__
--|--
Commands These next three configuration commands have little in common, other than the fact that they can be useful settings to reduce your frustration when using the console of a switch or router.|Команды Эти следующие три команды настройки имеют мало общего, кроме того факта, что они могут быть полезными настройками, чтобы уменьшить ваше разочарование при использовании консоли коммутатора или маршрутизатора.
The console automatically receives copies of all unsolicited syslog messages on a switch.|Консоль автоматически получает копии всех нежелательных сообщений системного журнала на коммутаторе.
The idea is that if the switch needs to tell the network administrator some important and possibly urgent information, the administrator might be at the console and might notice the message.|Идея состоит в том, что если коммутатору необходимо сообщить сетевому администратору какую-то важную и, возможно, срочную информацию, администратор может находиться у консоли и может заметить это сообщение.
Unfortunately, IOS (by default) displays these syslog messages on the console’s screen at any time—including right in the middle of a command you are entering, or in the middle of the output of a show command.|К сожалению, IOS (по умолчанию) отображает эти сообщения системного журнала на экране консоли в любое время, в том числе прямо в середине вводимой вами команды или в середине вывода команды show.
Having a bunch of text show up unexpectedly can be a bit annoying.|Неожиданное появление кучи текста может немного раздражать.
You could simply disable the feature that sends these messages to the console and then reenable the feature later using the no logging console and logging console global configuration commands.|Вы можете просто отключить функцию, которая отправляет эти сообщения на консоль, а затем повторно включить эту функцию позже, используя команды глобальной конфигурации консоли no logging и logging console.
For example, when working from the console, if you want to temporarily not be bothered by log messages, you can disable the display of these messages with the no logging console global configuration command, and then when finished, enable them again.|Например, при работе с консоли, если вы хотите временно не беспокоиться о сообщениях журнала, вы можете отключить отображение этих сообщений с помощью команды глобальной конфигурации консоли без ведения журнала, а затем, когда закончите, включить их снова.
However, IOS supplies a reasonable compromise, telling the switch to display syslog messages only at more convenient times, such as at the end of output from a show command.|Однако IOS предлагает разумный компромисс, сообщая коммутатору отображать сообщения системного журнала только в более удобное время, например, в конце вывода команды show.
To do so, just configure the logging synchronous console line subcommand, which basically tells IOS to synchronize the syslog message display with the messages requested using show commands.|Для этого просто настройте подкоманду logging synchronous console line, которая в основном сообщает IOS синхронизировать отображение сообщения системного журнала с сообщениями, запрошенными с помощью команд show.
Another way to improve the user experience at the console is to control timeouts of the login session from the console or when using Telnet or SSH. By default, the switch automatically disconnects console and vty (Telnet and SSH) users after 5 minutes of inactivity.|Еще один способ улучшить взаимодействие с пользователем на консоли - управлять таймаутами сеанса входа в систему с консоли или при использовании Telnet или SSH. По умолчанию коммутатор автоматически отключает пользователей консоли и vty (Telnet и SSH) после 5 минут бездействия.
The exec-timeout minutes seconds line subcommand enables you to set the length of that inactivity timer.|Подкоманда строки exec-timeout minutes seconds позволяет вам установить длительность этого таймера неактивности.
In the lab (but not in production), you might want to use the special value of 0 minutes and 0 seconds meaning “never time out.”|В лабораторных условиях (но не в производстве) вы можете использовать специальное значение 0 минут и 0 секунд, означающее «никогда не истекло время ожидания».
Finally, IOS has an interesting combination of features that can make you wait for a minute or so when you mistype a command.|Наконец, в IOS есть интересная комбинация функций, которая может заставить вас подождать минуту или около того, если вы ошиблись в команде.
First, IOS tries to use DNS name resolution on IP hostnames—a generally useful feature.|Во-первых, IOS пытается использовать разрешение DNS-имен для IP-имен хостов - это обычно полезная функция.
If you mistype a command, however, IOS thinks you want to telnet to a host by that name.|Однако, если вы ошиблись при вводе команды, IOS сочтет, что вы хотите подключиться к хосту с таким именем по telnet.
With all default settings in the switch, the switch tries to resolve the hostname, cannot find a DNS server, and takes about a minute to time out and give you control of the CLI again.|Со всеми настройками по умолчанию в коммутаторе коммутатор пытается разрешить имя хоста, не может найти DNS-сервер, и требуется около минуты, чтобы тайм-аут и снова дать вам контроль над CLI.
To avoid this problem, configure the no ip domain-lookup global configuration command, which disables IOS’s attempt to resolve the hostname into an IP address.|Чтобы избежать этой проблемы, настройте команду глобальной конфигурации no ip domain-lookup, которая отключает попытки IOS преобразовать имя хоста в IP-адрес.
Example 6-10 collects all these commands into a single example, as a template for some good settings to add in a lab switch to make you more productive.|В примере 6-10 все эти команды собраны в один пример в качестве шаблона для некоторых хороших настроек, которые можно добавить в лабораторный переключатель, чтобы сделать вас более продуктивным.
Example 6-10 Commands Often Used in the Lab to Increase Productivity Example end.|Пример 6-10 Команды, часто используемые в лабораторной работе для повышения производительности Пример end.
### Chapter Review
Обзор главы   
__|__
--|--
One key to doing well on the exams is to perform repetitive spaced review sessions.|Один из ключей к успешной сдаче экзаменов - повторение повторных сессий с интервалом.
Review this chapter’s material using either the tools in the book or interactive tools for the same material found on the book’s companion website.|Просмотрите материал этой главы, используя инструменты из книги или интерактивные инструменты для тех же материалов, которые можно найти на сопутствующем веб-сайте книги.
Refer to the “Your Study Plan” element section titled “Step 2: Build Your Study Habits Around the Chapter” for more details.|Обратитесь к разделу элемента «Ваш учебный план», озаглавленному «Шаг 2: выработайте учебу вокруг главы» для получения более подробной информации.
Table 6-3 outlines the key review elements and where you can find them.|В Таблице 6-3 перечислены ключевые элементы обзора и указаны места, где их можно найти.
To better track your study progress, record when you completed these activities in the second column.|Чтобы лучше отслеживать свои успехи в учебе, отметьте, когда вы выполнили эти задания, во втором столбце.
Table 6-3 Chapter Review Tracking Table end.|Таблица 6-3 Окончание таблицы отслеживания обзора главы.
Review All the Key Topics Key Terms You Should Know Telnet, Secure Shell (SSH), local username, AAA, AAA server, enable mode, default gateway, VLAN interface, history buffer, DNS, name resolution, log message Do Labs The Sim Lite software is a version of Pearson’s full simulator learning product with a subset of the labs, included with this book for free.|Ознакомьтесь со всеми ключевыми темами. Ключевые термины, которые вы должны знать Telnet, Secure Shell (SSH), локальное имя пользователя, AAA, сервер AAA, режим включения, шлюз по умолчанию, интерфейс VLAN, буфер истории, DNS, разрешение имен, сообщение журнала. Do Labs The Sim Lite Программное обеспечение представляет собой версию полного учебного продукта на симуляторах Pearson с подмножеством лабораторных работ, бесплатно включенных в эту книгу.
The subset of labs mostly relate to this part.|Подмножество лабораторных работ в основном относится к этой части.
Take the time to try some of the labs.|Найдите время, чтобы попробовать некоторые из лабораторных работ.
As always, also check the author’s blog site pages for configuration exercises (Config Labs) at https://blog.certskills.com.|Как всегда, также проверьте страницы блога автора на предмет упражнений по настройке (Лаборатория конфигурирования) по адресу https://blog.certskills.com.
Command References Tables 6-5, 6-6, 6-7, and 6-8 list configuration and verification commands used in this chapter.|Ссылки на команды В таблицах 6-5, 6-6, 6-7 и 6-8 перечислены команды настройки и проверки, используемые в этой главе.
As an easy review exercise, cover the left column in a table, read the right column, and try to recall the command without looking.|В качестве простого упражнения на повторение закройте левый столбец таблицы, прочтите правый столбец и попытайтесь вспомнить команду, не глядя.
Then repeat the exercise, covering the right column, and try to recall what the command does.|Затем повторите упражнение, охватывая правый столбец, и попытайтесь вспомнить, что делает команда.
Table 6-5 Login Security Commands Table end.|Таблица 6-5 Команды безопасности входа в систему Конец таблицы.
Table 6-6 Switch IPv4 Configuration Table end.|Таблица 6-6. Конец таблицы конфигурации IPv4 коммутатора.
Table 6-7 Other Switch Configuration Table end.|Таблица 6-7. Конец таблицы конфигурации других коммутаторов.
Table 6-8 Chapter 6 EXEC Command Reference Table end.|Таблица 6-8 Глава 6 Справочник команд EXEC Конец таблицы.
## Chapter 7 Configuring and Verifying Switch Interfaces
Глава 7 Настройка и проверка интерфейсов коммутатора   
__|__
--|--
This chapter covers the following exam topics:|В этой главе рассматриваются следующие экзаменационные темы:
###### 1.0 Network Fundamentals
1.0 Основы сети   
###### 1.1 Explain the role and function of network components
1.1 Объясните роль и функции сетевых компонентов   
###### 1.1.b L2 and L3 switches
1.1.b Коммутаторы L2 и L3   
###### 1.4 Describe switching concepts
1.4 Описание концепций переключения   
__|__
--|--
So far in this part, you have learned the skills to navigate the command-line interface (CLI)|До сих пор в этой части вы изучили навыки навигации по интерфейсу командной строки (CLI).
and use commands that configure and verify switch features.|и использовать команды для настройки и проверки функций коммутатора.
You learned about the primary purpose of a switch—forwarding Ethernet frames—and learned how to see that process in action by looking at the switch MAC address table.|Вы узнали об основной цели коммутатора - пересылке кадров Ethernet - и узнали, как увидеть этот процесс в действии, просмотрев таблицу MAC-адресов коммутатора.
After learning about the switch data plane in Chapter 5, “Analyzing Ethernet LAN Switching,” you learned a few management plane features in Chapter 6, “Configuring Basic Switch Management,” like how to configure the switch to support Telnet and Secure Shell (SSH) by configuring IP address and login security.|Изучив плоскость данных коммутатора в главе 5 «Анализ коммутации локальной сети Ethernet», вы узнали несколько функций плоскости управления в главе 6 «Настройка базового управления коммутатором», например, как настроить коммутатор для поддержки Telnet и Secure Shell (SSH ) путем настройки IP-адреса и безопасности входа.
This chapter focuses on switch interfaces in two major sections.|Эта глава посвящена интерфейсам коммутатора в двух основных разделах.
The first section shows how you can configure and change the operation of switch interfaces: how to change the speed, duplex, or even disable the interface.|В первом разделе показано, как можно настроить и изменить работу интерфейсов коммутатора: как изменить скорость, дуплекс или даже отключить интерфейс.
The second half then focuses on how to use show commands on a switch to verify switch interface status and how to interpret the output to find some of the more common issues with switch interfaces.|Вторая половина затем фокусируется на том, как использовать команды show на коммутаторе для проверки состояния интерфейса коммутатора и как интерпретировать вывод, чтобы найти некоторые из наиболее распространенных проблем с интерфейсами коммутатора.
### “Do I Know This Already?” Quiz
«Знаю ли я это уже?» Викторина   
__|__
--|--
Take the quiz (either here or use the PTP software) if you want to use the score to help you decide how much time to spend on this chapter.|Пройдите тест (здесь или воспользуйтесь программой PTP), если вы хотите использовать оценку, чтобы решить, сколько времени потратить на эту главу.
The letter answers are listed at the bottom of the page following the quiz.|Ответы на письма перечислены внизу страницы после викторины.
Appendix C, found both at the end of the book as well as on the companion website, includes both the answers and explanations.|Приложение C, которое можно найти как в конце книги, так и на сопутствующем веб-сайте, включает как ответы, так и пояснения.
You can also find both answers and explanations in the PTP testing software.|Вы также можете найти ответы и пояснения в программе тестирования PTP.
Table 7-1 “Do I Know This Already?” Foundation Topics Section-to-Question Mapping|Таблица 7-1 «Знаю ли я это уже?» Сопоставление разделов с вопросами по основным темам
### Foundation Topics
Основные темы   
### Configuring Switch Interfaces
Настройка интерфейсов коммутатора   
__|__
--|--
Analyzing Switch Interface Status and Statistics 4–6 CHAPTER 7 1.|Анализ состояния и статистики интерфейса коммутатора 4–6 ГЛАВА 7 1.
Which of the following describes a way to disable IEEE standard autonegotiation on a 10/100 port on a Cisco switch?|Что из следующего описывает способ отключения стандартного автосогласования IEEE на порту 10/100 коммутатора Cisco?
a. Configure the negotiate disable interface subcommand b.|а. Настройте подкоманду согласования отключения интерфейса b.
Configure the no negotiate interface subcommand c.|Настройте подкоманду без согласования интерфейса c.
Configure the speed 100 interface subcommand d.|Настройте подкоманду интерфейса speed 100 d.
Configure the duplex half interface subcommand e.|Настройте подкоманду дуплексного полуинтерфейса e.
Configure the duplex full interface subcommand f.|Настройте подкоманду дуплексного полного интерфейса f.
Configure the speed 100 and duplex full interface subcommands 2.|Настройте подкоманды speed 100 и duplex full interface 2.
In which of the following modes of the CLI could you configure the duplex setting for interface Fast Ethernet 0/5?|В каком из следующих режимов интерфейса командной строки вы можете настроить дуплексный режим для интерфейса Fast Ethernet 0/5?
a. User mode b.|а. Пользовательский режим b.
Enable mode c.|Включить режим c.
Global configuration mode d.|Режим глобальной конфигурации d.
VLAN mode e.|Режим VLAN e.
Interface configuration mode 3.|Режим настройки интерфейса 3.
A Cisco Catalyst switch connects with its Gigabit0/1 port to an end user’s PC. The end user, thinking the user is helping, manually sets the PC’s OS to use a speed of 1000 Mbps and to use full duplex, and disables the use of autonegotiation.|Коммутатор Cisco Catalyst подключается через порт Gigabit0 / 1 к ПК конечного пользователя. Конечный пользователь, думая, что пользователь помогает, вручную настраивает ОС ПК на скорость 1000 Мбит / с и полный дуплекс, а также отключает использование автосогласования.
The switch’s G0/1 port has default settings for speed and duplex.|Порт G0 / 1 коммутатора имеет настройки по умолчанию для скорости и дуплекса.
What speed and duplex settings will the switch decide to use? (Choose two answers.)|Какие настройки скорости и дуплексного режима выберет коммутатор? (Выберите два ответа.)
a. Full duplex b.|а. Полный дуплекс b.
Half duplex c. 10 Mbps d. 1000 Mbps 4.|Полудуплекс c. 10 Мбит / с d. 1000 Мбит / с 4.
The output of the show interfaces status command on a 2960 switch shows interface Fa0/1 in a “disabled” state.|Выходные данные команды show interfaces status на коммутаторе 2960 показывают интерфейс Fa0 / 1 в «отключенном» состоянии.
Which of the following is true about interface Fa0/1?|Что из следующего верно об интерфейсе Fa0 / 1?
(Choose three answers.)|(Выберите три ответа.)
a. The interface is configured with the shutdown command.|а. Интерфейс настраивается с помощью команды выключения.
b. The show interfaces fa0/1 command will list the interface with two status codes of administratively down and line protocol down.|б. Команда show interfaces fa0 / 1 выведет список интерфейсов с двумя кодами состояния: административно отключен и линейный протокол отключен.
c. The show interfaces fa0/1 command will list the interface with two status codes of up and down.|c. Команда show interfaces fa0 / 1 выведет список интерфейсов с двумя кодами состояния: up и down.
d. The interface cannot currently be used to forward frames.|d. В настоящее время интерфейс не может использоваться для пересылки кадров.
e. The interface can currently be used to forward frames.|е. В настоящее время интерфейс можно использовать для пересылки кадров.
5. Switch SW1 uses its Gigabit 0/1 interface to connect to switch SW2’s Gigabit 0/2 interface.|5. Коммутатор SW1 использует интерфейс Gigabit 0/1 для подключения к интерфейсу Gigabit 0/2 коммутатора SW2.
SW2’s Gi0/2 interface is configured with the speed 1000 and duplex full commands.|Интерфейс Gi0 / 2 SW2 настроен на скорость 1000 и команды полного дуплексного режима.
SW1 uses all defaults for interface configuration commands on its Gi0/1 interface.|SW1 использует все значения по умолчанию для команд настройки интерфейса на своем интерфейсе Gi0 / 1.
Which of the following are true about the link after it comes up? (Choose two answers.)|Что из следующего является верным относительно ссылки после того, как она появится? (Выберите два ответа.)
a. The link works at 1000 Mbps (1 Gbps).|а. Ссылка работает на скорости 1000 Мбит / с (1 Гбит / с).
b. SW1 attempts to run at 10 Mbps because SW2 has effectively disabled IEEE standard autonegotiation.|б. SW1 пытается работать на скорости 10 Мбит / с, поскольку SW2 фактически отключил стандартное автосогласование IEEE.
c. The link runs at 1 Gbps, but SW1 uses half duplex and SW2 uses full duplex.|c. Канал работает со скоростью 1 Гбит / с, но SW1 использует полудуплекс, а SW2 - полный дуплекс.
d. Both switches use full duplex.|d. Оба коммутатора используют полный дуплекс.
6. Switch SW1 connects via a cable to switch SW2’s G0/1 port.|6. Коммутатор SW1 подключается кабелем к порту G0 / 1 переключателя SW2.
Which of the following conditions is the most likely to cause SW1’s late collision counter to continue to increment?|Какое из следующих условий с наибольшей вероятностью приведет к тому, что счетчик поздних столкновений SW1 будет продолжать увеличиваться?
a. SW2’s G0/1 has been configured with a shutdown interface subcommand.|а. G0 / 1 SW2 настроен с помощью подкоманды интерфейса выключения.
b. The two switches have been configured with different values on the speed interface subcommand.|б. Два переключателя настроены с разными значениями подкоманды интерфейса скорости.
c. A duplex mismatch exists with SW1 set to full duplex.|c. Несоответствие дуплексного режима существует с SW1, установленным на полный дуплекс.
d. A duplex mismatch exists with SW1 set to half duplex.|d. Несоответствие дуплексного режима существует с SW1, установленным в полудуплексный режим.
Foundation Topics Configuring Switch Interfaces IOS uses the term interface to refer to physical ports used to forward data to and from other devices.|Основные темы Настройка интерфейсов коммутатора IOS использует термин интерфейс для обозначения физических портов, используемых для пересылки данных на другие устройства и от них.
Each interface can be configured with several settings, each of which might differ from interface to interface.|Для каждого интерфейса можно настроить несколько параметров, каждый из которых может отличаться от интерфейса к интерфейсу.
IOS uses interface subcommands to configure these settings.|IOS использует подкоманды интерфейса для настройки этих параметров.
Each of these settings may be different from one interface to the next, so you would first identify the specific interface, and then configure the specific setting.|Каждая из этих настроек может отличаться от одного интерфейса к другому, поэтому вы должны сначала определить конкретный интерфейс, а затем настроить конкретный параметр.
This section begins with a discussion of three relatively basic per-interface settings: the port speed, duplex, and a text description.|Этот раздел начинается с обсуждения трех относительно базовых настроек интерфейса: скорость порта, дуплекс и текстовое описание.
Following that, the text takes a short look at a pair of the most common interface subcommands: the shutdown and no shutdown commands, which administratively disable and enable the interface, respectively.|После этого в тексте дается краткий обзор пары наиболее распространенных подкоманд интерфейса: команды выключения и отсутствия выключения, которые административно отключают и включают интерфейс соответственно.
This section ends with a discussion about autonegotiation concepts, which in turn dictates what settings a switch chooses to use when using autonegotiation.|Этот раздел заканчивается обсуждением концепций автосогласования, которые, в свою очередь, определяют, какие настройки коммутатор выбирает для использования при использовании автосогласования.
#### Configuring Speed, Duplex, and Description
Настройка скорости, дуплекса и описания   
__|__
--|--
Switch interfaces that support multiple speeds (10/100 and 10/100/1000 interfaces), by default, will autonegotiate what speed to use.|Интерфейсы коммутатора, поддерживающие несколько скоростей (интерфейсы 10/100 и 10/100/1000), по умолчанию будут автоматически согласовывать, какую скорость использовать.
However, you can configure the speed and duplex settings with the duplex {auto | full | half} and speed {auto | 10 | 100 | 1000} interface subcommands.|Однако вы можете настроить скорость и параметры дуплекса с помощью дуплекса {auto | полный | половина} и скорость {авто | 10 | 100 | 1000} интерфейсные подкоманды.
Simple enough.|Достаточно просто.
Most of the time, using autonegotiation makes good sense, so when you set the duplex and speed manually using these commands, you typically have a good reason to do so.|В большинстве случаев использование автосогласования имеет смысл, поэтому, когда вы вручную устанавливаете дуплекс и скорость с помощью этих команд, у вас обычно есть веская причина для этого.
For instance, maybe you want to set the speed to the fastest possible on links between switches just to avoid the chance that autonegotiation chooses a slower speed.|Например, может быть, вы хотите установить максимально возможную скорость на каналах между коммутаторами, чтобы избежать шанса, что автосогласование выберет более низкую скорость.
The description text interface subcommand lets you add a text description to the interface.|Подкоманда description text interface позволяет добавить текстовое описание к интерфейсу.
For instance, if you have good reason to configure the speed and duplex on a port, maybe add a description that says why you did.|Например, если у вас есть веская причина для настройки скорости и дуплекса на порту, возможно, добавьте описание, в котором объясняется, почему вы это сделали.
Example 7-1 shows how to configure duplex and speed, as well as the description command, which is simply a text description that can be configured by the administrator.|В примере 7-1 показано, как настроить дуплекс и скорость, а также команду description, которая представляет собой просто текстовое описание, которое может быть настроено администратором.
Example 7-1 Configuring speed, duplex, and description on Switch Emma Example end.|Пример 7-1 Настройка скорости, дуплекса и описания на Switch Emma. Пример конец.
First, focus on the mechanics of moving around in configuration mode again by looking closely at the command prompts.|Во-первых, снова сосредоточьтесь на механике перемещения в режиме настройки, внимательно посмотрев на командные строки.
The various interface commands move the user from global mode into interface configuration mode for a specific interface.|Различные команды интерфейса переводят пользователя из глобального режима в режим конфигурации интерфейса для конкретного интерфейса.
For instance, the example configures the duplex, speed, and description commands all just after the interface FastEthernet 0/1 command, which means that all three of those configuration settings apply to interface Fa0/1, and not to the other interfaces.|Например, в этом примере команды дуплекса, скорости и описания настраиваются сразу после команды interface FastEthernet 0/1, что означает, что все три из этих параметров конфигурации применяются к интерфейсу Fa0 / 1, а не к другим интерфейсам.
The show interfaces status command lists much of the detail configured in Example 7-1, even with only one line of output per interface.|Команда show interfaces status перечисляет большую часть деталей, настроенных в примере 7-1, даже с одной строкой вывода на интерфейс.
Example 7-2 shows an example, just after the configuration in Example 7-1 was added to the switch.|В примере 7-2 показан пример сразу после того, как к коммутатору была добавлена ??конфигурация из примера 7-1.
Example 7-2 Displaying Interface Status Example end.|Пример 7-2 Отображение статуса интерфейса Пример конец.
Working through the output in the example:|Работаем с выводом в примере:
FastEthernet 0/1 (Fa0/1): This output lists the first few characters of the configured description.|FastEthernet 0/1 (Fa0 / 1): в этих выходных данных перечислены первые несколько символов настроенного описания.
It also lists the configured speed of 100 and duplex full per the speed and duplex commands in Example 7-1.|В нем также перечислены настроенная скорость 100 и полный дуплекс для команд скорости и дуплекса в Примере 7-1.
However, it also states that Fa0/1 has a status of notconnect, meaning that the interface is not currently working. (That switch port did not have a cable connected when collecting this example, on purpose.)|Однако в нем также говорится, что Fa0 / 1 имеет статус notconnect, что означает, что интерфейс в настоящее время не работает. (К этому порту коммутатора специально не был подключен кабель при сборе этого примера.)
FastEthernet 0/2 (Fa0/2): Example 7-1 did not configure this port at all.|FastEthernet 0/2 (Fa0 / 2): в примере 7-1 этот порт вообще не настраивался.
This port had all default configuration.|У этого порта была вся конфигурация по умолчанию.
Note that the “auto” text under the speed and duplex heading means that this port will attempt to autonegotiate both settings when the port comes up.|Обратите внимание, что текст «auto» под заголовком «Скорость и дуплекс» означает, что этот порт попытается выполнить автосогласование обоих параметров при подключении порта.
However, this port also does not have a cable connected (again on purpose, for comparison).|Однако к этому порту также не подключен кабель (опять же специально для сравнения).
FastEthernet 0/4 (Fa0/4): Like Fa0/2, this port has all default configuration but was cabled to another working device to give yet another contrasting example.|FastEthernet 0/4 (Fa0 / 4): Как и Fa0 / 2, этот порт имеет всю конфигурацию по умолчанию, но был подключен к другому рабочему устройству, чтобы дать еще один контрастный пример.
This device completed the autonegotiation process, so instead of “auto” under the speed and duplex headings, the output lists the negotiated speed and duplex (a-full and a-100).|Это устройство завершило процесс автосогласования, поэтому вместо «авто» под заголовками скорости и дуплекса в выходных данных указывается согласованная скорость и дуплекс (a-full и a-100).
Note that the text includes the a- to mean that the listed speed and duplex values were autonegotiated.|Обратите внимание, что в тексте есть символ «-», означающий, что перечисленные значения скорости и дуплексного режима согласованы автоматически.
#### Configuring Multiple Interfaces with the interface range Command
Настройка нескольких интерфейсов с помощью команды interface range   
__|__
--|--
The bottom of the configuration in Example 7-1 shows a way to shorten your configuration work when making the same setting on multiple consecutive interfaces.|В нижней части конфигурации в примере 7-1 показан способ сократить вашу работу по настройке при выполнении одинаковых настроек для нескольких последовательных интерфейсов.
To do so, use the interface range command.|Для этого используйте команду interface range.
In the example, the interface range FastEthernet 0/11 - 20 command tells IOS that the next subcommand(s) apply to interfaces Fa0/11 through Fa0/20.|В этом примере команда interface range FastEthernet 0/11–20 сообщает IOS, что следующая подкоманда (-ы) применяется к интерфейсам с Fa0 / 11 по Fa0 / 20.
You can define a range as long as all interfaces are the same type and are numbered consecutively.|Вы можете определить диапазон, если все интерфейсы одного типа и пронумерованы последовательно.
NOTE This book spells out all parameters fully to avoid confusion.|ПРИМЕЧАНИЕ В этой книге полностью описаны все параметры, чтобы избежать путаницы.
However, most everyone abbreviates what they type in the CLI to the shortest unique abbreviation.|Однако почти все сокращают то, что они вводят в CLI, до самого короткого уникального сокращения.
For instance, the configuration commands int f0/1 and int ran f0/11 - 20 would also be acceptable.|Например, команды конфигурации int f0 / 1 и int ran f0 / 11-20 также будут приемлемы.
IOS does not actually put the interface range command into the configuration.|IOS фактически не помещает команду диапазона интерфейса в конфигурацию.
Instead, it acts as if you had typed the subcommand under every single interface in the specified Answers to the “Do I Know This Already?” quiz:|Вместо этого он действует так, как если бы вы ввели подкоманду под каждым интерфейсом в указанных ответах на вопрос «Знаю ли я это уже?» викторина:
1 F 2 E 3 A, D 4 A, B, D 5 A, D 6 D range.|1 F 2 E 3 A, D 4 A, B, D 5 A, D 6 D. Диапазон.
Example 7-3 shows an excerpt from the show running-config command, listing the configuration of interfaces F0/11–12 from the configuration in Example 7-1.|В примере 7-3 показан отрывок из команды show running-config, в котором перечислена конфигурация интерфейсов F0 / 11–12 из конфигурации в примере 7-1.
The example shows the same description command on both interfaces; to save space, the example does not bother to show all 10 interfaces that have the same description text.|В примере показана одна и та же команда описания для обоих интерфейсов; для экономии места в примере не показаны все 10 интерфейсов с одинаковым текстом описания.
Example 7-3 How IOS Expands the Subcommands Typed After interface range Example end.|Пример 7-3. Как IOS расширяет подкоманды, введенные после диапазона интерфейса. Пример end.
#### Administratively Controlling Interface State with shutdown
Административное управление состоянием интерфейса с выключением   
__|__
--|--
As you might imagine, network engineers need a way to bring down an interface without having to travel to the switch and remove a cable.|Как вы можете себе представить, сетевым инженерам нужен способ вывести из строя интерфейс, не прибегая к коммутатору и отсоединяя кабель.
In short, we need to be able to decide which ports should be enabled and which should be disabled.|Короче говоря, нам нужно решить, какие порты должны быть включены, а какие - отключены.
In an odd turn of phrase, Cisco uses two interface subcommands to configure the idea of administratively enabling and disabling an interface: the shutdown command (to disable) and the no shutdown command (to enable).|Как ни странно, Cisco использует две подкоманды интерфейса для настройки идеи административного включения и отключения интерфейса: команда shutdown (для отключения) и команда no shutdown (для включения).
While the no shutdown command might seem like an odd command to enable an interface at first, you will use this command a lot in the lab, and it will become second nature. (Most people, in fact, use the abbreviations shut and no shut.)|Хотя поначалу команда no shutdown может показаться странной командой для включения интерфейса, вы будете часто использовать эту команду в лаборатории, и она станет вашей второй натурой. (Фактически, большинство людей используют сокращения закрытый и не закрытый.)
Example 7-4 shows an example of disabling an interface using the shutdown interface subcommand.|В примере 7-4 показан пример отключения интерфейса с помощью подкоманды shutdown interface.
In this case, switch SW1 has a working interface F0/1.|В этом случае переключатель SW1 имеет рабочий интерфейс F0 / 1.
The user connects at the console and disables the interface.|Пользователь подключается к консоли и отключает интерфейс.
IOS generates a log message each time an interface fails or recovers, and log messages appear at the console, as shown in the example.|IOS генерирует сообщение журнала каждый раз, когда интерфейс выходит из строя или восстанавливается, и сообщения журнала появляются на консоли, как показано в примере.
Example 7-4 Administratively Disabling an Interface with shutdown Example end.|Пример 7-4 Административное отключение интерфейса с выключением Пример конец.
To bring the interface back up again, all you have to do is follow the same process but use the no shutdown command instead.|Чтобы снова запустить интерфейс, все, что вам нужно сделать, это выполнить тот же процесс, но вместо этого использовать команду no shutdown.
Before leaving the simple but oddly named shutdown/no shutdown commands, take a look at two important show commands that list the status of a shutdown interface.|Прежде чем оставить простые, но странно названные команды shutdown / no shutdown, взгляните на две важные команды show, в которых отображается статус интерфейса завершения работы.
The show interfaces status command lists one line of output per interface, and when shut down, lists the interface status as “disabled.” That makes logical sense to most people.|Команда show interfaces status перечисляет одну строку вывода для каждого интерфейса, а при выключении отображает состояние интерфейса как «отключено». Для большинства людей это имеет логический смысл.
The show interfaces command (without the status keyword) lists many lines of output per interface, giving a much more detailed picture of interface status and statistics.|Команда show interfaces (без ключевого слова status) перечисляет множество строк вывода для каждого интерфейса, давая гораздо более подробную картину состояния и статистики интерфейса.
With that command, the interface status comes in two parts, with one part using the phrase “administratively down,” matching the highlighted log message in Example 7-4.|С помощью этой команды состояние интерфейса состоит из двух частей, в одной части используется фраза «административно отключена», что соответствует выделенному сообщению журнала в примере 7-4.
Example 7-5 shows an example of each of these commands.|В примере 7-5 показан пример каждой из этих команд.
Note that both examples also use the F0/1 parameter (short for Fast Ethernet0/1), which limits the output to the messages about F0/1 only.|Обратите внимание, что в обоих примерах также используется параметр F0 / 1 (сокращение от Fast Ethernet0 / 1), который ограничивает вывод только сообщениями о F0 / 1.
Also note that F0/1 is still shut down at this point.|Также обратите внимание, что F0 / 1 все еще отключен в этот момент.
Example 7-5 The Different Status Information About Shutdown in Two Different show Example end.|Пример 7-5. Различная информация о состоянии выключения в двух разных вариантах.
#### Removing Configuration with the no Command
Удаление конфигурации с помощью команды no   
__|__
--|--
One purpose for the specific commands shown in Part II of the book is to teach you about that command.|Одна из целей конкретных команд, показанных во второй части книги, - научить вас этой команде.
In some cases, the commands are not the end goal, and the text is attempting to teach you something about how the CLI works.|В некоторых случаях команды не являются конечной целью, и текст пытается научить вас чему-то о том, как работает CLI.
This next short topic is more about the process than about the commands.|Следующая короткая тема больше о процессе, чем о командах.
With some IOS configuration commands (but not all), you can revert to the default setting by issuing a no version of the command.|С некоторыми командами конфигурации IOS (но не всеми) вы можете вернуться к настройкам по умолчанию, введя no версию команды.
What does that mean?|Что это значит?
Let me give you a few examples:|Приведу несколько примеров:
###### If you earlier had configured speed 100 on an interface, the no speed command on that
Если вы ранее настроили скорость 100 на интерфейсе, команда no speed на этом   
__|__
--|--
same interface reverts to the default speed setting (which happens to be speed auto).|тот же интерфейс возвращается к настройке скорости по умолчанию (которая оказывается автоматической).
###### Same idea with the duplex command: an earlier configuration of duplex half or duplex
Та же идея с командой дуплекса: более ранняя конфигурация дуплексного полу- или дуплексного режима   
__|__
--|--
full, followed by no duplex on the same interface, reverts the configuration back to the default of duplex auto.|полный, за которым следует отсутствие дуплекса на том же интерфейсе, возвращает конфигурацию обратно к автоматическому дуплексному режиму по умолчанию.
###### If you had configured a description command with some text, to go back to the default
Если вы настроили команду описания с некоторым текстом, чтобы вернуться к значениям по умолчанию   
__|__
--|--
state of having no description command at all for that interface, use the no description command.|состояние отсутствия команды описания для этого интерфейса, используйте команду no description.
Example 7-6 shows the process.|Пример 7-6 показывает процесс.
In this case, switch SW1’s F0/2 port has been configured with speed 100, duplex half, description link to 2901-2, and shutdown.|В этом случае порт F0 / 2 коммутатора SW1 настроен на скорость 100, полудуплексный режим, ссылку описания на 2901-2 и отключение.
You can see evidence of all four settings in the command that begins the example. (This command lists the running-config, but only the part for that one interface.) The example then shows the no versions of those commands and closes with a confirmation that all the commands have reverted to default.|Вы можете увидеть подтверждение всех четырех настроек в команде, с которой начинается пример. (Эта команда перечисляет рабочую конфигурацию, но только часть для этого интерфейса.) Затем пример показывает, что версии этих команд отсутствуют, и закрывается с подтверждением того, что все команды вернулись к значениям по умолчанию.
Example 7-6 Removing Various Configuration Settings Using the no Command Example end.|Пример 7-6 Удаление различных настроек конфигурации с помощью команды no Пример end.
NOTE The show running-config and show startup-config commands typically do not display default configuration settings, so the absence of commands listed under interface F0/2 at the end of the example means that those commands now use default values.|ПРИМЕЧАНИЕ. Команды show running-config и show startup-config обычно не отображают параметры конфигурации по умолчанию, поэтому отсутствие команд, перечисленных в интерфейсе F0 / 2 в конце примера, означает, что эти команды теперь используют значения по умолчанию.
#### Autonegotiation
Автосогласование   
__|__
--|--
For any 10/100 or 10/100/1000 interfaces—that is, interfaces that can run at different speeds—Cisco Catalyst switches default to a setting of duplex auto and speed auto.|Для любых интерфейсов 10/100 или 10/100/1000, т. Е. Интерфейсов, которые могут работать на разных скоростях, коммутаторы Cisco Catalyst по умолчанию используют автоматический дуплексный режим и автоматический режим скорости.
As a result, those interfaces attempt to automatically determine the speed and duplex setting to use.|В результате эти интерфейсы пытаются автоматически определить используемую скорость и настройку дуплекса.
Alternatively, you can configure most devices, switch interfaces included, to use a specific speed and/or duplex.|В качестве альтернативы вы можете настроить большинство устройств, включая интерфейсы коммутатора, на использование определенной скорости и / или дуплекса.
In practice, using autonegotiation is easy: just leave the speed and duplex at the default setting, and let the switch port negotiate what settings to use on each port.|На практике использовать автосогласование просто: просто оставьте скорость и дуплекс по умолчанию и позвольте порту коммутатора согласовать, какие настройки использовать для каждого порта.
However, problems can occur due to unfortunate combinations of configuration.|Однако проблемы могут возникнуть из-за неудачных комбинаций конфигурации.
Therefore, this next topic walks through more detail about the concepts behind autonegotiation, so you know better how to interpret the meaning of the switch show commands and when to choose to use a particular configuration setting.|Таким образом, в следующем разделе более подробно рассматриваются концепции автосогласования, чтобы вы лучше знали, как интерпретировать значение команд show switch и когда использовать тот или иной параметр конфигурации.
#### Autonegotiation Under Working Conditions
Автосогласование в рабочих условиях   
__|__
--|--
Ethernet devices on the ends of a link must use the same standard; otherwise, they cannot correctly send data.|Устройства Ethernet на концах канала должны использовать один и тот же стандарт; в противном случае они не смогут правильно отправить данные.
For example, a NIC cannot use 100BASE-T, which uses a two-pair UTP cable with a 100-Mbps speed, while the switch port on the other end of the link uses 1000BASE-T.|Например, сетевая карта не может использовать 100BASE-T, который использует двухпарный кабель UTP со скоростью 100 Мбит / с, в то время как порт коммутатора на другом конце канала использует 1000BASE-T.
Even if you used a cable that works with Gigabit Ethernet, the link would not work with one end trying to send at 100 Mbps while the other tried to receive the data at 1000 Mbps.|Даже если вы использовали кабель, который работает с Gigabit Ethernet, соединение не будет работать, если один конец будет пытаться отправить со скоростью 100 Мбит / с, а другой попытается получить данные со скоростью 1000 Мбит / с.
Upgrading to new and faster Ethernet standards becomes a problem because both ends have to use the same standard.|Обновление до новых и более быстрых стандартов Ethernet становится проблемой, потому что оба конца должны использовать один и тот же стандарт.
For example, if you replace an old PC with a new one, the old one might have been using 100BASE-T while the new one uses 1000BASE-T.|Например, если вы заменяете старый компьютер на новый, старый может использовать 100BASE-T, а новый - 1000BASE-T.
The switch port on the other end of the link needs to now use 1000BASE-T, so you upgrade the switch.|Порт коммутатора на другом конце канала должен теперь использовать 1000BASE-T, поэтому вы обновите коммутатор.
If that switch had ports that would use only 1000BASE-T, you would need to upgrade all the other PCs connected to the switch.|Если бы у этого коммутатора были порты, которые использовали бы только 1000BASE-T, вам необходимо было бы обновить все остальные ПК, подключенные к коммутатору.
So, having both PC network interface cards (NIC) and switch ports that support multiple standards/speeds makes it much easier to migrate to the next better standard.|Таким образом, наличие как сетевых карт (NIC) ПК, так и портов коммутатора, поддерживающих несколько стандартов / скоростей, значительно упрощает переход на следующий лучший стандарт.
The IEEE autonegotiation protocol helps makes it much easier to operate a LAN when NICs and switch ports support multiple speeds.|Протокол автосогласования IEEE помогает значительно упростить работу в локальной сети, когда сетевые адаптеры и порты коммутатора поддерживают несколько скоростей.
IEEE autonegotiation (IEEE standard 802.3u)|Автосогласование IEEE (стандарт IEEE 802.3u)
defines a protocol that lets the two UTP-based Ethernet nodes on a link negotiate so that they each choose to use the same speed and duplex settings.|определяет протокол, который позволяет двум узлам Ethernet на основе UTP на канале согласовывать свои действия, чтобы каждый из них мог использовать одну и ту же скорость и настройки дуплекса.
The protocol messages flow outside the normal Ethernet electrical frequencies as out-of-band signals over the UTP cable.|Сообщения протокола передаются за пределы обычных электрических частот Ethernet как внеполосные сигналы по кабелю UTP.
Basically, each node states what it can do, and then each node picks the best options that both nodes support: the fastest speed and the best duplex setting, with full duplex being better than half duplex.|По сути, каждый узел заявляет, что он может делать, а затем каждый узел выбирает лучшие варианты, которые поддерживают оба узла: максимальную скорость и лучшую настройку дуплекса, причем полный дуплекс лучше, чем полудуплекс.
NOTE Autonegotiation relies on the fact that the IEEE uses the same wiring pinouts for 10BASE-T and 100BASE-T, and that 1000BASE-T simply adds to those pinouts, adding two pairs.|ПРИМЕЧАНИЕ. Автосогласование основывается на том факте, что IEEE использует одинаковые выводы разводки для 10BASE-T и 100BASE-T, а 1000BASE-T просто добавляет к этим выводам, добавляя две пары.
Many networks use autonegotiation every day, particularly between user devices and the access layer LAN switches, as shown in Figure 7-1.|Многие сети используют автосогласование каждый день, особенно между пользовательскими устройствами и коммутаторами LAN уровня доступа, как показано на рисунке 7-1.
The company installed four-pair cabling of the right quality to support 1000BASE-T, to be ready to support Gigabit Ethernet.|Компания установила четырехпарный кабель надлежащего качества для поддержки 1000BASE-T, чтобы быть готовым к поддержке Gigabit Ethernet.
As a result, the wiring supports 10-Mbps, 100-Mbps, and 1000-Mbps Ethernet options.|В результате проводка поддерживает варианты Ethernet со скоростью 10, 100 и 1000 Мбит / с.
Both nodes on each link send autonegotiation messages to each other.|Оба узла на каждом канале отправляют друг другу сообщения автосогласования.
The switch in this case has all 10/100/1000 ports, while the PC NICs support different options.|Коммутатор в этом случае имеет все порты 10/100/1000, а сетевые адаптеры ПК поддерживают различные параметры.
Figure 7-1 IEEE Autonegotiation Results with Both Nodes Working Correctly The following list breaks down the logic, one PC at a time:|Рисунок 7-1 Результаты автосогласования IEEE при правильной работе обоих узлов В следующем списке представлена ??логическая разбивка по одному ПК за раз:
PC1: The switch port claims it can go as fast as 1000 Mbps, but PC1’s NIC claims a top speed of 10 Mbps.|PC1: порт коммутатора утверждает, что он может работать со скоростью до 1000 Мбит / с, но сетевая карта PC1 утверждает, что максимальная скорость составляет 10 Мбит / с.
Both the PC and the switch choose the fastest speed that each supports (10 Mbps) and the best duplex that each supports (full).|И ПК, и коммутатор выбирают максимальную скорость, которую поддерживает каждый (10 Мбит / с), и лучший дуплекс, который поддерживает каждый (полный).
PC2: PC2 claims a best speed of 100 Mbps, which means it can use 10BASE-T or 100BASE-T.|PC2: PC2 заявляет о максимальной скорости 100 Мбит / с, что означает, что он может использовать 10BASE-T или 100BASE-T.
The switch port and NIC negotiate to use the best speed of 100 Mbps and full duplex.|Порт коммутатора и сетевая карта согласовывают использование максимальной скорости 100 Мбит / с и полного дуплекса.
PC3: It uses a 10/100/1000 NIC, supporting all three speeds and standards, so both the NIC and switch port choose 1000 Mbps and full duplex.|PC3: в нем используется сетевая карта 10/100/1000, поддерживающая все три скорости и стандарта, поэтому и сетевая карта, и порт коммутатора выбирают 1000 Мбит / с и полнодуплексный режим.
##### Autonegotiation Results When Only One Node Uses
Результаты автосогласования при использовании только одного узла   
__|__
--|--
Figure 7-1 shows the IEEE autonegotiation results when both nodes use the process.|На рисунке 7-1 показаны результаты автосогласования IEEE, когда оба узла используют процесс.
However, most Ethernet devices can disable autonegotiation, so it is just as important to know what happens when a node tries to use autonegotiation but the node gets no response.|Однако большинство устройств Ethernet могут отключить автосогласование, поэтому не менее важно знать, что происходит, когда узел пытается использовать автосогласование, но не получает ответа.
Disabling autonegotiation is not always a bad idea.|Отключение автосогласования - не всегда плохая идея.
For instance, many network engineers disable autonegotiation on links between switches and simply configure the desired speed and duplex on both switches.|Например, многие сетевые инженеры отключают автосогласование на каналах между коммутаторами и просто настраивают желаемую скорость и дуплекс на обоих коммутаторах.
However, mistakes can happen when one device on an Ethernet predefines speed and duplex (and disables autonegotiation), while the device on the other end attempts autonegotiation.|Однако ошибки могут произойти, когда одно устройство в сети Ethernet заранее определяет скорость и дуплекс (и отключает автосогласование), в то время как устройство на другом конце пытается выполнить автосогласование.
In that case, the link might not work at all, or it might just work poorly.|В этом случае ссылка может не работать вообще или просто работать плохо.
NOTE Configuring both the speed and duplex on a Cisco Catalyst switch interface disables autonegotiation.|ПРИМЕЧАНИЕ. Настройка скорости и дуплексного режима на интерфейсе коммутатора Cisco Catalyst отключает автосогласование.
IEEE autonegotiation defines some rules (defaults) that nodes should use as defaults when autonegotiation fails—that is, when a node tries to use autonegotiation but hears nothing from the device.|Автосогласование IEEE определяет некоторые правила (значения по умолчанию), которые узлы должны использовать по умолчанию, когда автосогласование не удается, то есть когда узел пытается использовать автосогласование, но ничего не слышит от устройства.
The rules:|Правила:
###### Speed: Use your slowest supported speed (often 10 Mbps).
Скорость: используйте самую низкую из поддерживаемых скоростей (часто 10 Мбит / с).   
###### Duplex: If your speed = 10 or 100, use half duplex; otherwise, use full duplex.
Дуплекс: если ваша скорость = 10 или 100, используйте полудуплекс; в противном случае используйте полный дуплекс.   
__|__
--|--
Cisco switches can make a better choice than that base IEEE speed default because Cisco switches can actually sense the speed used by other nodes, even without IEEE autonegotiation.|Коммутаторы Cisco могут сделать лучший выбор, чем базовая скорость по умолчанию IEEE, поскольку коммутаторы Cisco действительно могут определять скорость, используемую другими узлами, даже без автосогласования IEEE.
As a result, Cisco switches use this slightly different logic to choose the speed when autonegotiation fails:|В результате коммутаторы Cisco используют эту несколько иную логику для выбора скорости при сбое автосогласования:
###### Speed: Sense the speed (without using autonegotiation), but if that fails, use the IEEE
Скорость: определите скорость (без использования автосогласования), но если это не удается, используйте IEEE   
__|__
--|--
default (slowest supported speed, often 10 Mbps).|по умолчанию (самая низкая поддерживаемая скорость, часто 10 Мбит / с).
###### Duplex: Use the IEEE defaults: If speed = 10 or 100, use half duplex; otherwise, use full
Дуплекс: используйте значения по умолчанию IEEE: если скорость = 10 или 100, используйте полудуплекс; в противном случае используйте полный   
__|__
--|--
duplex.|дуплекс.
NOTE Ethernet interfaces using speeds faster than 1 Gbps always use full duplex.|ПРИМЕЧАНИЕ Интерфейсы Ethernet, использующие скорости выше 1 Гбит / с, всегда используют полнодуплексный режим.
Figure 7-2 shows three examples in which three users change their NIC settings and disable autonegotiation, while the switch (with all 10/100/1000 ports) attempts autonegotiation.|На рис. 7-2 показаны три примера, в которых три пользователя изменяют настройки своей сетевой карты и отключают автосогласование, в то время как коммутатор (со всеми портами 10/100/1000) пытается выполнить автосогласование.
That is, the switch ports all default to speed auto and duplex auto.|То есть все порты коммутатора по умолчанию работают в автоматическом режиме и в дуплексном режиме.
The top of the figure shows the configured settings on each PC NIC, with the choices made by the switch listed next to each switch port.|В верхней части рисунка показаны сконфигурированные параметры для каждой сетевой карты ПК, причем варианты, сделанные коммутатором, перечислены рядом с каждым портом коммутатора.
Figure 7-2 IEEE Autonegotiation Results with Autonegotiation Disabled on One Side Reviewing each link, left to right:|Рисунок 7-2 Результаты автосогласования IEEE с отключенным автосогласованием на одной стороне Просмотр каждой ссылки слева направо:
###### PC1: The switch receives no autonegotiation messages, so it senses the electrical signal
ПК1: коммутатор не получает сообщений автосогласования, поэтому он воспринимает электрический сигнал.   
__|__
--|--
to learn that PC1 is sending data at 100 Mbps.|чтобы узнать, что ПК1 отправляет данные со скоростью 100 Мбит / с.
The switch uses the IEEE default duplex based on the 100 Mbps speed (half duplex).|Коммутатор использует дуплексный режим по умолчанию IEEE на основе скорости 100 Мбит / с (полудуплекс).
###### PC2: The switch uses the same steps and logic as with the link to PC1, except that the
ПК2: коммутатор использует те же шаги и логику, что и связь с ПК1, за исключением того, что   
__|__
--|--
switch chooses to use full duplex because the speed is 1000 Mbps.|Коммутатор выбирает полный дуплекс, потому что скорость составляет 1000 Мбит / с.
###### PC3: The user picks poorly, choosing the slower speed (10 Mbps) and the worse duplex
PC3: пользователь плохо выбирает, выбирая меньшую скорость (10 Мбит / с) и худший дуплекс   
__|__
--|--
setting (half).|установка (половина).
However, the Cisco switch senses the speed without using IEEE autonegotiation and then uses the IEEE duplex default for 10-Mbps links (half duplex).|Однако коммутатор Cisco определяет скорость без использования автосогласования IEEE, а затем использует дуплексный режим IEEE по умолчанию для каналов со скоростью 10 Мбит / с (полудуплекс).
PC1 shows a classic and unfortunately common end result: a duplex mismatch.|PC1 показывает классический и, к сожалению, общий конечный результат: несовпадение дуплексных параметров.
The two nodes (PC1 and SW1’s port G0/1) both use 100 Mbps, so they can send data.|Оба узла (ПК1 и порт G0 / 1 SW1) оба используют 100 Мбит / с, поэтому они могут отправлять данные.
However, PC1, using full duplex, does not attempt to use carrier sense multiple access with collision detection (CSMA/CD) logic and sends frames at any time.|Однако ПК1, использующий полнодуплексный режим, не пытается использовать множественный доступ с контролем несущей и логикой обнаружения коллизий (CSMA / CD) и отправляет кадры в любое время.
Switch port F0/1, with half duplex, does use CSMA/CD. As a result, switch port F0/1 will believe collisions occur on the link, even if none physically occur.|Порт коммутатора F0 / 1 с полудуплексным режимом использует CSMA / CD. В результате порт коммутатора F0 / 1 будет считать, что на канале возникают конфликты, даже если их не происходит физически.
The switch port will stop transmitting, back off, resend frames, and so on.|Порт коммутатора прекратит передачу, отключается, повторно отправляет кадры и т. Д.
As a result, the link is up, but it performs poorly.|В результате канал работает, но работает плохо.
The upcoming section titled “Interface Speed and Duplex Issues” will revisit this problem with a focus on how to recognize the symptoms of a duplex mismatch.|В следующем разделе, озаглавленном «Проблемы со скоростью интерфейса и дуплексным режимом», мы еще раз рассмотрим эту проблему с упором на то, как распознать симптомы несоответствия дуплексного режима.
##### Autonegotiation and LAN Hubs
Автосогласование и концентраторы LAN   
__|__
--|--
LAN hubs also impact how autonegotiation works.|Концентраторы LAN также влияют на работу автосогласования.
Basically, hubs do not react to autonegotiation messages, and they do not forward the messages.|По сути, концентраторы не реагируют на сообщения автосогласования и не пересылают сообщения.
As a result, devices connected to a hub must use the IEEE rules for choosing default settings, which often results in the devices using 10 Mbps and half duplex.|В результате устройства, подключенные к концентратору, должны использовать правила IEEE для выбора настроек по умолчанию, что часто приводит к тому, что устройства используют 10 Мбит / с и полудуплекс.
Figure 7-3 shows an example of a small Ethernet LAN that uses a 20-year-old 10BASE-T hub.|На рис. 7-3 показан пример небольшой локальной сети Ethernet, в которой используется концентратор 10BASE-T 20-летней давности.
In this LAN, all devices and switch ports are 10/100/1000 ports.|В этой локальной сети все устройства и порты коммутатора являются портами 10/100/1000.
The hub supports only 10BASE-T.|Концентратор поддерживает только 10BASE-T.
Figure 7-3 IEEE Autonegotiation with a LAN Hub Note that the devices on the right need to use half duplex because the hub requires the use of the CSMA/CD algorithm to avoid collisions.|Рис. 7-3. Автосогласование IEEE с концентратором LAN Обратите внимание, что устройства справа должны использовать полудуплекс, потому что концентратор требует использования алгоритма CSMA / CD, чтобы избежать коллизий.
NOTE If you would like to learn more about collision domains and the impact of these older LAN hubs, look to the companion website for Appendix K, “Analyzing Ethernet LAN Designs,” to the section titled “Ethernet Collision Domains.”|ПРИМЕЧАНИЕ. Если вы хотите узнать больше о доменах коллизий и влиянии этих старых концентраторов LAN, загляните на сопутствующий веб-сайт, где вы найдете Приложение K, «Анализ схем локальной сети Ethernet», к разделу «Домены коллизий Ethernet».
### Analyzing Switch Interface Status and Statistics
Анализ состояния и статистики интерфейса коммутатора   
__|__
--|--
Now that you have seen some of the ways to configure switch interfaces, the rest of the chapter takes a closer look at how to verify the interfaces work correctly.|Теперь, когда вы ознакомились с некоторыми способами настройки интерфейсов коммутатора, в оставшейся части главы более подробно рассматривается, как проверить правильность работы интерфейсов.
This section also looks at those more unusual cases in which the interface is working but not working well, as revealed by different interface status codes and statistics.|В этом разделе также рассматриваются более необычные случаи, когда интерфейс работает, но не работает должным образом, о чем свидетельствуют различные коды состояния интерфейса и статистика.
#### Interface Status Codes and Reasons for Nonworking States
Коды состояния интерфейса и причины нерабочего состояния   
__|__
--|--
Cisco switches actually use two different sets of interface status codes—one set of two codes (words) that use the same conventions as do router interface status codes, and another set with a single code (word).|Коммутаторы Cisco фактически используют два разных набора кодов состояния интерфейса: один набор из двух кодов (слов), которые используют те же соглашения, что и коды состояния интерфейса маршрутизатора, а другой набор с одним кодом (словом).
Both sets of status codes can determine whether an interface is working.|Оба набора кодов состояния могут определять, работает ли интерфейс.
The switch show interfaces and show interfaces description commands list the two-code status named the line status and protocol status.|Команды switch show interfaces и show interfaces description перечисляют состояние с двумя кодами, называемое состоянием линии и состоянием протокола.
The line status generally refers to whether Layer 1 is working, with protocol status generally referring to whether Layer 2 is working.|Статус линии обычно указывает, работает ли уровень 1, а статус протокола обычно указывает, работает ли уровень 2.
NOTE This book refers to these two status codes in shorthand by just listing the two codes with a slash between them, such as up/up.|ПРИМЕЧАНИЕ В этой книге эти два кода состояния обозначаются сокращенно, просто перечисляя два кода с косой чертой между ними, например, вверх / вверх.
The single-code interface status corresponds to different combinations of the traditional two-code interface status codes and can be easily correlated to those codes.|Состояние однокодового интерфейса соответствует различным комбинациям традиционных кодов состояния двухкодового интерфейса и может быть легко сопоставлено с этими кодами.
For example, the show interfaces status command lists a single-word state of connected state for working interfaces, with the same meaning as the two-word up/up state seen with the show interfaces and show interfaces description commands.|Например, команда show interfaces status перечисляет состояние подключения из одного слова для рабочих интерфейсов с тем же значением, что и состояние подключения из двух слов, наблюдаемое с командами show interfaces и show interfaces description.
Table 7-2 lists the code combinations and some root causes that could have caused a particular interface status.|В таблице 7-2 перечислены кодовые комбинации и некоторые основные причины, которые могли вызвать определенное состояние интерфейса.
Table 7-2 LAN Switch Interface Status Codes Table end.|Таблица 7-2 Коды состояния интерфейса коммутатора LAN Конец таблицы.
Examining the notconnect state for a moment, note that this state has many causes that have been mentioned through this book.|Рассматривая на мгновение состояние отсутствия соединения, обратите внимание, что у этого состояния много причин, упомянутых в этой книге.
For example, using incorrect cabling pinouts, instead of the correct pinouts explained in Chapter 2, “Fundamentals of Ethernet LANs,” causes a problem.|Например, использование неправильных выводов кабелей вместо правильных выводов, описанных в главе 2 «Основы локальных сетей Ethernet», вызывает проблему.
However, one topic can be particularly difficult to troubleshoot—the possibility for both speed and duplex mismatches, as explained in the next section.|Однако одна тема может быть особенно сложной для устранения неполадок - возможность несовпадения скорости и дуплексного режима, как объясняется в следующем разделе.
As you can see in the table, having a bad cable is just one of many reasons for the down/down state (or notconnect, per the show interfaces status command).|Как вы можете видеть в таблице, плохой кабель - это лишь одна из многих причин неработающего / неработающего состояния (или отсутствия соединения согласно команде show interfaces status).
Some examples of the root causes of cabling problems include the following:|Вот некоторые примеры основных причин проблем с кабелями:
###### The installation of any equipment that uses electricity, even non-IT equipment, can interfere
Установка любого оборудования, которое использует электричество, даже не ИТ-оборудования, может помешать   
__|__
--|--
with the transmission on the cabling and make the link fail.|с передачей по кабелю и отключите связь.
###### The cable could be damaged, for example, if it lies under carpet. If the user’s chair keeps
Кабель может быть поврежден, например, если он пролегает под ковром. Если стул пользователя остается   
__|__
--|--
squashing the cable, eventually the electrical signal can degrade.|сдавливание кабеля может привести к ухудшению электрического сигнала.
###### Although optical cables do not suffer from electromagnetic interference (EMI), someone
Хотя оптические кабели не страдают от электромагнитных помех (EMI), кто-то   
__|__
--|--
can try to be helpful and move a fiber-optic cable out of the way—bending it too much.|может попытаться помочь и убрать с пути оптоволоконный кабель - слишком сильно его согнуть.
A bend into too tight a shape can prevent the cable from transmitting bits (called macrobending).|Слишком плотный изгиб может помешать кабелю передавать биты (это называется макроизгибом).
For the other interface states listed in Table 7-2, only the up/up (connected) state needs more discussion.|Для других состояний интерфейса, перечисленных в Таблице 7-2, более подробного обсуждения требует только состояние "включено" / "включено".
An interface can be in a working state, and it might really be working—or it might be working in a degraded state.|Интерфейс может быть в рабочем состоянии, и он может действительно работать - или он может работать в ухудшенном состоянии.
The next few topics discuss how to examine an up/up (connected) interface to find out whether it is working well or having problems.|В следующих нескольких темах обсуждается, как проверить подключенный интерфейс, чтобы выяснить, хорошо ли он работает или есть проблемы.
#### Interface Speed and Duplex Issues
Скорость интерфейса и проблемы с дуплексом   
__|__
--|--
To discuss some of the speed and duplex issues, first consider the output from the show interfaces status and show interfaces commands as demonstrated in Example 7-7.|Чтобы обсудить некоторые проблемы скорости и дуплекса, сначала рассмотрим выходные данные команд show interfaces status и show interfaces, как показано в Примере 7-7.
The first of these commands lists a one-line summary of the interface status, while the second command gives many details—but surprisingly, the briefer show interfaces status command tells us more about autonegotiation.|Первая из этих команд перечисляет однострочную сводку состояния интерфейса, а вторая дает много деталей - но, что удивительно, более короткая команда show interfaces status сообщает нам больше об автосогласовании.
Example 7-7 Displaying Speed and Duplex Settings on Switch Interfaces Example end.|Пример 7-7 Отображение настроек скорости и дуплексного режима на интерфейсах коммутатора Конец примера.
Although both commands in the example can be useful, only the show interfaces status command implies how the switch determined the speed and duplex settings.|Хотя обе команды в примере могут быть полезны, только команда show interfaces status показывает, как коммутатор определил скорость и параметры дуплекса.
The command output lists autonegotiated settings with a prefix of a- and the manually set values without the a- prefix.|В выходных данных команды перечислены параметры автосогласования с префиксом a- и значения, установленные вручную без префикса a-.
For example, consider ports Fa0/12 and Fa0/13 in the output of the show interfaces status command.|Например, рассмотрите порты Fa0 / 12 и Fa0 / 13 в выходных данных команды show interfaces status.
For Fa0/13, a-full means full duplex as autonegotiated, whereas half on Fa0/12 means half duplex but as manually configured.|Для Fa0 / 13 полный означает полный дуплекс с автосогласованием, тогда как половина в Fa0 / 12 означает полудуплекс, но настроенный вручную.
The example shades the command output that implies that the switch’s Fa0/12 interface’s speed and duplex were not found through autonegotiation, but Fa0/13 did use autonegotiation.|В примере затемнен вывод команды, который подразумевает, что скорость и дуплексный режим интерфейса Fa0 / 12 коммутатора не были обнаружены посредством автосогласования, но Fa0 / 13 действительно использовал автосогласование.
In comparison, note that the show interfaces fa0/13 command (without the status option)|Для сравнения обратите внимание, что команда show interfaces fa0 / 13 (без параметра состояния)
simply lists the speed and duplex for interface Fast Ethernet 0/13, with nothing implying that the values were learned through autonegotiation.|просто перечисляет скорость и дуплекс для интерфейса Fast Ethernet 0/13, при этом ничего не подразумевает, что значения были получены посредством автосогласования.
When the IEEE autonegotiation process works on both devices—that is, both are sending autonegotiation messages—both devices agree to the fastest speed and best duplex supported by both devices.|Когда процесс автосогласования IEEE работает на обоих устройствах, то есть оба отправляют сообщения автосогласования, оба устройства соглашаются на максимальную скорость и лучший дуплекс, поддерживаемые обоими устройствами.
However, when one device uses autonegotiation and the other disables it, the first device must resort to default settings as detailed earlier in section “Autonegotiation Results When Only One Node Uses Autonegotiation.” As a reminder, those defaults are|Однако, когда одно устройство использует автосогласование, а другое отключает его, первое устройство должно прибегнуть к настройкам по умолчанию, как подробно описано ранее в разделе «Результаты автосогласования, когда только один узел использует автосогласование». Напоминаем, что по умолчанию
###### Speed: Sense the speed (without using autonegotiation), but if that fails, use the IEEE
Скорость: определите скорость (без использования автосогласования), но если это не удается, используйте IEEE   
__|__
--|--
default (slowest supported speed, often 10 Mbps).|по умолчанию (самая низкая поддерживаемая скорость, часто 10 Мбит / с).
###### Duplex: Use the IEEE defaults: If speed = 10 or 100, use half duplex; otherwise, use full
Дуплекс: используйте значения по умолчанию IEEE: если скорость = 10 или 100, используйте полудуплекс; в противном случае используйте полный   
__|__
--|--
duplex.|дуплекс.
When a switch must use its defaults, it should get the speed correct, but it may choose the wrong duplex setting, creating a duplex mismatch.|Когда коммутатор должен использовать свои настройки по умолчанию, он должен получить правильную скорость, но он может выбрать неправильную настройку дуплекса, создавая несоответствие дуплексного режима.
For example, in Figure 7-4, imagine that SW2’s Gi0/2 interface was configured with the speed 100 and duplex full commands (these settings are not recommended on a Gigabitcapable interface, by the way).|Например, на рис. 7-4 представьте, что интерфейс Gi0 / 2 SW2 был настроен на скорость 100 и дуплексные полные команды (кстати, эти настройки не рекомендуются для интерфейса с гигабитным интерфейсом).
On Cisco switches, configuring both the speed and duplex commands disables IEEE autonegotiation on that port.|На коммутаторах Cisco настройка команд скорости и дуплекса отключает автосогласование IEEE для этого порта.
If SW1’s Gi0/1 interface tries to use autonegotiation, SW1 would also use a speed of 100 Mbps, but default to use half duplex.|Если интерфейс Gi0 / 1 SW1 пытается использовать автосогласование, SW1 также будет использовать скорость 100 Мбит / с, но по умолчанию будет использовать полудуплекс.
Example 7-8 shows the results of this specific case on SW1.|В примере 7-8 показаны результаты этого конкретного случая на SW1.
Figure 7-4 Conditions to Create a Duplex Mismatch Between SW1 and SW2 Example 7-8 Confirming Duplex Mismatch on Switch SW1 Example end.|Рисунок 7-4 Условия для создания дуплексного несоответствия между SW1 и SW2 Пример 7-8 Подтверждение дуплексного несоответствия на переключателе SW1 Пример окончен.
First, note that even though SW1 had to use an autonegotiation default, the show interfaces status command still shows the speed and duplex with the a- prefix.|Во-первых, обратите внимание, что хотя SW1 должен был использовать по умолчанию автосогласование, команда show interfaces status все еще показывает скорость и дуплекс с префиксом a-.
SW2’s port was manually set to 100/Full, so SW1 sensed the speed and runs at 100 Mbps; however, the autonegotiation rules then tell SW1 to use half duplex, as confirmed by the output in Example 7-8.|Порт SW2 был вручную установлен на 100 / Full, поэтому SW1 определил скорость и работал со скоростью 100 Мбит / с; однако правила автосогласования затем указывают SW1 использовать полудуплекс, что подтверждается выходными данными в примере 7-8.
The output does not identify the duplex mismatch in any way; in fact, finding a duplex mismatch can be much more difficult than finding a speed mismatch.|Выходные данные никоим образом не определяют несоответствие дуплексного режима; Фактически, обнаружение несоответствия дуплексных параметров может быть намного сложнее, чем обнаружение несоответствия скорости.
For instance, if you purposefully set the speed on the link in Figure 7-4 to be 10 Mbps on one switch and 100 Mbps on the other, both switches would list the port in a down/down or notconnect state.|Например, если вы целенаправленно установите скорость канала на рисунке 7-4, равную 10 Мбит / с на одном коммутаторе и 100 Мбит / с на другом, оба коммутатора будут указывать порт в состоянии неработающего / неактивного или неподключенного состояния.
However, in the case shown in Example 7-8, with a duplex mismatch, if the duplex settings do not match on the ends of an Ethernet segment, the switch interface will still be in a connected (up/up) or connected state.|Однако в случае, показанном в Примере 7-8, с несоответствием дуплексного режима, если настройки дуплекса не совпадают на концах сегмента Ethernet, интерфейс коммутатора все равно будет находиться в подключенном (вверх / вверх) или подключенном состоянии.
Not only does the show command give an appearance that the link has no issues, but the link will likely work poorly, with symptoms of intermittent problems.|Команда show не только создает видимость того, что ссылка не имеет проблем, но она, скорее всего, будет работать плохо с признаками периодических проблем.
The reason is that the device using half duplex (SW1 in this case) uses carrier sense multiple access collision detect (CSMA/CD) logic, waiting to send when receiving a frame, believing collisions occur when they physically do not—and actually stopping sending a frame because the switch thinks a collision occurred.|Причина в том, что устройство, использующее полудуплекс (в данном случае SW1), использует логику обнаружения коллизий множественного доступа с контролем несущей (CSMA / CD), ожидая отправки при получении кадра, полагая, что коллизии возникают, когда их физически не происходит, и фактически прекращает отправку. кадр, потому что коммутатор считает, что произошло столкновение.
With enough traffic load, the interface could be in a connect state, but it’s extremely inefficient for passing traffic.|При достаточной загрузке трафика интерфейс может находиться в состоянии подключения, но он крайне неэффективен для передачи трафика.
To identify duplex mismatch problems, check the duplex setting on each end of the link to see if the values mismatch.|Чтобы определить проблемы несоответствия дуплексного режима, проверьте настройки дуплексного режима на каждом конце ссылки, чтобы увидеть, не совпадают ли значения.
You can also watch for incrementing collision and late collision counters, as explained in the next section.|Вы также можете следить за увеличением счетчиков столкновений и поздних столкновений, как описано в следующем разделе.
#### Common Layer 1 Problems on Working Interfaces
Распространенные проблемы уровня 1 на рабочих интерфейсах   
__|__
--|--
When the interface reaches the connect (up/up) state, the switch considers the interface to be working.|Когда интерфейс достигает состояния подключения (up / up), коммутатор считает, что интерфейс работает.
The switch, of course, tries to use the interface, and at the same time, the switch keeps various interface counters.|Коммутатор, конечно, пытается использовать интерфейс, и в то же время коммутатор поддерживает различные счетчики интерфейса.
These interface counters can help identify problems that can occur even though the interface is in a connect state, like issues related to the duplex mismatch problem that was just described.|Эти счетчики интерфейса могут помочь выявить проблемы, которые могут возникнуть, даже если интерфейс находится в состоянии подключения, например проблемы, связанные с проблемой несоответствия дуплексного режима, которая была только что описана.
This section explains some of the related concepts and a few of the most common problems.|В этом разделе объясняются некоторые связанные концепции и некоторые из наиболее распространенных проблем.
Whenever the physical transmission has problems, the receiving device might receive a frame whose bits have changed values.|Если при физической передаче возникают проблемы, принимающее устройство может получить кадр, биты которого изменили значения.
These frames do not pass the error detection logic as implemented in the FCS field in the Ethernet trailer, as covered in Chapter 2.|Эти кадры не проходят логику обнаружения ошибок, реализованную в поле FCS в трейлере Ethernet, как описано в главе 2.
The receiving device discards the frame and counts it as some kind of input error.|Принимающее устройство отбрасывает фрейм и считает его ошибкой ввода.
Cisco switches list this error as a CRC error, as highlighted in Example 7-9. (Cyclic redundancy check [CRC] is a term related to how the frame check sequence [FCS] math detects an error.)|Коммутаторы Cisco перечисляют эту ошибку как ошибку CRC, как показано в Примере 7-9. (Циклический контроль избыточности [CRC] - это термин, связанный с тем, как математическая последовательность проверки кадра [FCS] обнаруживает ошибку.)
Example 7-9 Interface Counters for Layer 1 Problems Example end.|Пример 7-9 Интерфейсные счетчики для проблем уровня 1 Пример конец.
The number of input errors and the number of CRC errors are just a few of the counters in the output of the show interfaces command.|Количество ошибок ввода и количество ошибок CRC - это лишь некоторые из счетчиков в выходных данных команды show interfaces.
The challenge is to decide which counters you need to think about, which ones show that a problem is happening, and which ones are normal and of no concern.|Задача состоит в том, чтобы решить, о каких счетчиках вам следует подумать, какие из них показывают, что проблема возникает, а какие являются нормальными и не вызывают беспокойства.
The example highlights several of the counters as examples so that you can start to understand which ones point to problems and which ones are just counting normal events that are not problems.|В примере выделено несколько счетчиков в качестве примеров, чтобы вы могли начать понимать, какие из них указывают на проблемы, а какие просто подсчитывают нормальные события, которые не являются проблемами.
The following list shows a short description of each highlighted counter, in the order shown in the example:|В следующем списке показано краткое описание каждого выделенного счетчика в порядке, показанном в примере:
Runts: Frames that did not meet the minimum frame size requirement (64 bytes, including the 18-byte destination MAC, source MAC, type, and FCS). Can be caused by collisions.|Рунты: кадры, которые не соответствуют требованиям к минимальному размеру кадра (64 байта, включая 18-байтовый MAC-адрес назначения, исходный MAC-адрес, тип и FCS). Может быть вызвано столкновениями.
Giants: Frames that exceed the maximum frame size requirement (1518 bytes, including the 18-byte destination MAC, source MAC, type, and FCS).|Giants: кадры, превышающие требования к максимальному размеру кадра (1518 байтов, включая 18-байтовый MAC-адрес назначения, исходный MAC-адрес, тип и FCS).
Input Errors: A total of many counters, including runts, giants, no buffer, CRC, frame, overrun, and ignored counts.|Ошибки ввода: всего много счетчиков, включая ранты, гиганты, отсутствие буфера, CRC, фрейм, переполнение и проигнорированные счетчики.
CRC: Received frames that did not pass the FCS math; can be caused by collisions.|CRC: полученные кадры, которые не прошли математику FCS; могут быть вызваны столкновениями.
Frame: Received frames that have an illegal format, for example, ending with a partial byte; can be caused by collisions.|Кадр: принятые кадры с недопустимым форматом, например, заканчивающиеся неполным байтом; могут быть вызваны столкновениями.
Packets Output: Total number of packets (frames) forwarded out the interface.|Вывод пакетов: общее количество пакетов (кадров), отправленных через интерфейс.
Output Errors: Total number of packets (frames) that the switch port tried to transmit, but for which some problem occurred.|Ошибки вывода: общее количество пакетов (кадров), которые порт коммутатора пытался передать, но для которых возникла проблема.
Collisions: Counter of all collisions that occur when the interface is transmitting a frame.|Коллизии: счетчик всех коллизий, возникающих при передаче кадра интерфейсом.
Late Collisions: The subset of all collisions that happen after the 64th byte of the frame has been transmitted. (In a properly working Ethernet LAN, collisions should occur within the first 64 bytes; late collisions today often point to a duplex mismatch.)|Поздние коллизии: подмножество всех коллизий, которые происходят после передачи 64-го байта кадра. (В правильно работающей локальной сети Ethernet коллизии должны происходить в пределах первых 64 байтов; поздние коллизии сегодня часто указывают на несоответствие дуплексного режима.)
Note that many of these counters occur as part of the CSMA/CD process used when half duplex is enabled.|Обратите внимание, что многие из этих счетчиков возникают как часть процесса CSMA / CD, используемого при включении полудуплекса.
Collisions occur as a normal part of the half-duplex logic imposed by CSMA/CD, so a switch interface with an increasing collisions counter might not even have a problem.|Коллизии возникают как нормальная часть полудуплексной логики, налагаемой CSMA / CD, поэтому интерфейс коммутатора с увеличивающимся счетчиком коллизий может даже не иметь проблем.
However, one problem, called late collisions, points to the classic duplex mismatch problem.|Однако одна проблема, называемая поздними коллизиями, указывает на классическую проблему несоответствия дуплексного режима.
If a LAN design follows cabling guidelines, all collisions should occur by the end of the 64th byte of any frame.|Если при проектировании ЛВС соблюдаются рекомендации по прокладке кабелей, все конфликты должны происходить к концу 64-го байта любого кадра.
When a switch has already sent 64 bytes of a frame, and the switch receives a frame on that same interface, the switch senses a collision.|Когда коммутатор уже отправил 64 байта кадра, и коммутатор получает кадр на том же интерфейсе, коммутатор обнаруживает коллизию.
In this case, the collision is a late collision, and the switch increments the late collision counter in addition to the usual CSMA/CD actions to send a jam signal, wait a random time, and try again.|В этом случае коллизия является поздней коллизией, и коммутатор увеличивает счетчик поздних коллизий в дополнение к обычным действиям CSMA / CD для отправки сигнала блокировки, ожидания случайного времени и повторной попытки.
With a duplex mismatch, like the mismatch between SW1 and SW2 in Figure 7-4, the halfduplex interface will likely see the late collisions counter increment.|При несовпадении дуплексного режима, таком как несоответствие между SW1 и SW2 на рис. 7-4, полудуплексный интерфейс, вероятно, увидит приращение счетчика поздних коллизий.
Why?|Зачем?
The half-duplex interface sends a frame (SW1), but the full-duplex neighbor (SW2) sends at any time, even after the 64th byte of the frame sent by the half-duplex switch.|Полудуплексный интерфейс отправляет кадр (SW1), но полнодуплексный сосед (SW2) отправляет в любое время, даже после 64-го байта кадра, отправленного полудуплексным коммутатором.
So, just keep repeating the show interfaces command, and if you see the late collisions counter incrementing on a halfduplex interface, you might have a duplex mismatch problem.|Итак, просто продолжайте повторять команду show interfaces, и если вы видите, что счетчик поздних столкновений увеличивается на полудуплексном интерфейсе, у вас может быть проблема несоответствия дуплексного режима.
A working interface (in an up/up state) can still suffer from issues related to the physical cabling as well.|Рабочий интерфейс (в активном / активном состоянии) все еще может страдать от проблем, связанных с физической кабельной разводкой.
The cabling problems might not be bad enough to cause a complete failure, but the transmission failures result in some frames failing to pass successfully over the cable.|Проблемы с кабелем могут быть недостаточно серьезными, чтобы вызвать полный отказ, но сбои передачи приводят к тому, что некоторые кадры не могут успешно пройти по кабелю.
For example, excessive interference on the cable can cause the various input error counters to keep growing larger, especially the CRC counter.|Например, чрезмерные помехи в кабеле могут привести к увеличению различных счетчиков ошибок ввода, особенно счетчика CRC.
In particular, if the CRC errors grow, but the collisions counters do not, the problem might simply be interference on the cable. (The switch counts each collided frame as one form of input error as well.)|В частности, если ошибки CRC растут, а счетчики коллизий - нет, проблема может заключаться в помехах в кабеле. (Коммутатор также считает каждый столкнувшийся кадр как одну из форм ошибки ввода.)
### Chapter Review
Обзор главы   
__|__
--|--
One key to doing well on the exams is to perform repetitive spaced review sessions.|Один из ключей к успешной сдаче экзаменов - повторение повторных сессий с интервалом.
Review this chapter’s material using either the tools in the book or interactive tools for the same material found on the book’s companion website.|Просмотрите материал этой главы, используя инструменты из книги или интерактивные инструменты для тех же материалов, которые можно найти на сопутствующем веб-сайте книги.
Refer to the “Your Study Plan” element section titled “Step 2: Build Your Study Habits Around the Chapter” for more details.|Обратитесь к разделу элемента «Ваш учебный план», озаглавленному «Шаг 2: выработайте учебу вокруг главы» для получения более подробной информации.
Table 7-3 outlines the key review elements and where you can find them.|В Таблице 7-3 представлены основные элементы обзора и их местонахождение.
To better track your study progress, record when you completed these activities in the second column.|Чтобы лучше отслеживать свои успехи в учебе, отметьте, когда вы выполнили эти задания, во втором столбце.
Table 7-3 Chapter Review Tracking Table end.|Таблица 7-3 Окончание таблицы отслеживания обзора главы.
Review All the Key Topics Key Terms You Should Know port security, autonegotiation, full duplex, half duplex, 10/100, 10/100/1000 Do Labs The Sim Lite software is a version of Pearson’s full simulator learning product with a subset of the labs, included free with this book.|Ознакомьтесь со всеми ключевыми темами. Ключевые термины, которые вы должны знать. Безопасность портов, автосогласование, полный дуплекс, полудуплекс, 10/100, 10/100/1000. Выполните лабораторные работы. Программное обеспечение Sim Lite - это версия продукта для обучения на полном симуляторе Pearson с подмножеством лаборатории, бесплатно включенные в эту книгу.
The subnet of labs mostly relate to this part.|Подсеть лабораторий в основном относится к этой части.
Take the time to try some of the labs.|Найдите время, чтобы попробовать некоторые из лабораторных работ.
As always, also check the author’s blog site pages for configuration exercises (Config Labs) at https://blog.certskills.com.|Как всегда, также проверьте страницы блога автора на предмет упражнений по настройке (Лаборатория конфигурирования) по адресу https://blog.certskills.com.
Command References Tables 7-5 and 7-6 list configuration and verification commands used in this chapter.|Ссылки на команды В таблицах 7-5 и 7-6 перечислены команды настройки и проверки, используемые в этой главе.
As an easy review exercise, cover the left column in a table, read the right column, and try to recall the command without looking.|В качестве простого упражнения на повторение закройте левый столбец таблицы, прочтите правый столбец и попытайтесь вспомнить команду, не глядя.
Then repeat the exercise, covering the right column, and try to recall what the command does.|Затем повторите упражнение, охватывая правый столбец, и попытайтесь вспомнить, что делает команда.
Table 7-5 Switch Interface Configuration Table end.|Таблица 7-5 Конец таблицы конфигурации интерфейса коммутатора.
Table 7-6 Chapter 7 EXEC Command Reference Table end.|Таблица 7-6 Глава 7 Справочник команд EXEC Конец таблицы.
Keep track of your part review progress with the checklist shown in Table P2-1.|Следите за ходом проверки деталей с помощью контрольного списка, приведенного в Таблице P2-1.
Details on each task follow the table.|Подробности по каждой задаче приведены в таблице.
Table P2-1 Part II Part Review Checklist Activity 1st Date Completed 2nd Date Completed Repeat All DIKTA Questions Answer Part Review Questions Review Key Topics Do Labs Review Appendix P on the Companion Website Videos Repeat All DIKTA Questions For this task, answer the “Do I Know This Already?” questions again for the chapters in this part of the book, using the PCPT software.|Таблица P2-1. Контрольный список проверки части II. Действие 1-я дата завершения 2-я дата завершения Повторить все вопросы DIKTA Ответить на вопросы проверки части Пересмотреть ключевые темы Проверьте ли лаборатория Приложение P на сопутствующем веб-сайте Видео Повторите все вопросы DIKTA Для этой задачи ответьте на вопрос «Могу ли я Уже знаете это? » снова задайте вопросы к главам этой части книги, используя программное обеспечение PCPT.
Answer Part Review Questions For this task, answer the Part Review questions for this part of the book, using the PTP software.|Ответить на вопросы обзора части Для этой задачи ответьте на вопросы обзора части для этой части книги, используя программное обеспечение PTP.
Review Key Topics Review all key topics in all chapters in this part, either by browsing the chapters or by using the Key Topics application on the companion website.|Обзор ключевых тем. Просмотрите все ключевые темы во всех главах этой части, просматривая главы или используя приложение «Ключевые темы» на сопутствующем веб-сайте.
Labs Depending on your chosen lab tool, here are some suggestions for what to do in lab:|Лабораторные работы В зависимости от выбранного вами лабораторного инструмента, вот несколько советов о том, что делать в лаборатории:
Pearson Network Simulator: If you use the full Pearson ICND1 or CCNA simulator, focus more on the configuration scenario and troubleshooting scenario labs associated with the topics in this part of the book.|Симулятор сети Pearson: если вы используете полный симулятор Pearson ICND1 или CCNA, уделите больше внимания сценарию конфигурации и лабораторным работам по сценарию устранения неполадок, связанным с темами в этой части книги.
These types of labs include a larger set of topics and work well as Part Review activities. (See the Introduction for some details about how to find which labs are about topics in this part of the book.)|Эти типы лабораторных работ включают более широкий набор тем и хорошо подходят для работы с обзором деталей. (См. Введение, чтобы узнать, как найти лабораторные работы по темам в этой части книги.)
Blog: Config Labs: The author’s blog includes a series of configuration-focused labs that you can do on paper, each in 10–15 minutes.|Блог: Config Labs: блог автора включает в себя серию лабораторных работ по настройке, которые вы можете выполнить на бумаге, каждая из которых занимает 10–15 минут.
Review and perform the labs for this part of the book, as found at http://blog.certskills.com.|Просмотрите и выполните лабораторные работы для этой части книги, которые можно найти на http://blog.certskills.com.
Then navigate to the Hands-on Config labs.|Затем перейдите к практическим занятиям по настройке.
## Part II Review
Часть II Обзор   
__|__
--|--
Other: If using other lab tools, as a few suggestions: Make sure to experiment heavily with VLAN configuration and VLAN trunking configuration.|Другое: Если вы используете другие лабораторные инструменты, в качестве нескольких предложений: Обязательно поэкспериментируйте с конфигурацией VLAN и конфигурацией транкинга VLAN.
Also, spend some time changing interface settings like speed and duplex on a link between two switches, to make sure that you understand which cases would result in a duplex mismatch.|Кроме того, потратьте некоторое время на изменение настроек интерфейса, таких как скорость и дуплекс на линии между двумя коммутаторами, чтобы убедиться, что вы понимаете, в каких случаях может возникнуть несоответствие дуплексного режима.
Review Appendix P on the Companion Website The previous edition of the CCNA exam blueprint included the word “troubleshoot”|См. Приложение P на сопутствующем веб-сайте. В предыдущем выпуске плана экзамена CCNA было слово «устранение неполадок».
as applied to Ethernet and VLANs, while the current CCNA exam blueprint does not.|применительно к Ethernet и VLAN, тогда как текущий план экзамена CCNA - нет.
Appendix P on the companion website contains a chapter from the previous edition of the book that focused on troubleshooting.|Приложение P на сопутствующем веб-сайте содержит главу из предыдущего издания книги, посвященную поиску и устранению неисправностей.
That appendix, named “LAN Troubleshooting,” can be useful as a tool to review the topics in this part of the book. (Note that if you use this extra appendix, you can ignore the mentions of Port Security until you have reached that Watch Videos Chapters 4 and 5 each recommend a video that can be helpful to anyone who is just learning about the Cisco CLI and basic switching concepts.|Это приложение, названное «Устранение неполадок LAN», может быть полезно в качестве инструмента для ознакомления с темами в этой части книги. (Обратите внимание, что если вы используете это дополнительное приложение, вы можете игнорировать упоминания о безопасности порта, пока не дойдете до того, что Смотреть видео, главы 4 и 5, каждая рекомендует видео, которое может быть полезно для всех, кто только изучает Cisco CLI и основы коммутации. концепции.
If you have not watched those videos yet, take a moment to navigate to the companion website and watch the videos (listed under Chapters 4 and 5).|Если вы еще не смотрели эти видеоролики, найдите время, чтобы перейти на сопутствующий веб-сайт и посмотреть видеоролики (перечисленные в главах 4 и 5).
Part II of this book introduces the basics of Ethernet LANs, both in concept and in how to implement the features.|Часть II этой книги знакомит с основами сетей Ethernet как в концепции, так и в том, как реализовать эти функции.
However, the two primary features discussed in Part III of this book—Virtual LANs (VLANs) and Spanning Tree Protocol (STP)—impact almost everything you have learned about Ethernet so far.|Однако две основные особенности, обсуждаемые в части III этой книги - виртуальные локальные сети (VLAN) и протокол связующего дерева (STP) - влияют почти на все, что вы узнали об Ethernet до сих пор.
VLANs allow a network engineer to create separate Ethernet LANs through simple configuration choices.|Сети VLAN позволяют сетевому инженеру создавать отдельные локальные сети Ethernet с помощью простых вариантов конфигурации.
The ability to separate some switch ports into one VLAN and other switch ports into another VLAN gives network designers a powerful tool for creating networks.|Возможность разделить некоторые порты коммутатора в одну VLAN, а другие порты коммутатора в другую VLAN дает разработчикам сетей мощный инструмент для создания сетей.
Once created, VLANs also have a huge impact on how a switch works, which then impacts how you verify and troubleshoot the operation of a campus LAN.|После создания виртуальные локальные сети также оказывают огромное влияние на работу коммутатора, что затем влияет на то, как вы проверяете и устраняете неполадки в работе локальной сети кампуса.
STP—and the related and similar Rapid STP (RSTP)—acts to prevent frames from looping around a LAN. Without STP or RSTP, in LANs with redundant links, broadcasts and some other frames would be forwarded around and around the LAN, eventually clogging the LAN so much as to make it unusable.|STP - и связанный с ним Rapid STP (RSTP) - предотвращает зацикливание кадров в локальной сети. Без STP или RSTP в локальных сетях с избыточными ссылками широковещательные сообщения и некоторые другие кадры будут пересылаться по локальной сети и вокруг нее, в конечном итоге засоряя локальную сеть настолько, что она становится непригодной для использования.
The current CCNA 200-301 exam blueprint includes exam topics for the configuration and verification of VLANs and related topics.|Текущий план экзамена CCNA 200-301 включает темы экзаменов по настройке и проверке сетей VLAN и связанные темы.
However, the CCNA exam topics only mention RSTP concepts rather than configuration/verification.|Однако в темах экзамена CCNA упоминаются только концепции RSTP, а не настройка / проверка.
To that end, Part III opens with Chapter 8, which goes to the configuration/verification depth with VLAN topics, followed by Chapter 9, which introduces the concepts of STP and RSTP.|С этой целью часть III открывается главой 8, в которой подробно рассказывается о конфигурации / проверке с темами о VLAN, за которой следует глава 9, в которой представлены концепции STP и RSTP.
Part III closes with Chapter 10, which includes some RSTP configuration, along with Layer 2 EtherChannel configuration.|Часть III завершается главой 10, которая включает в себя некоторую конфигурацию RSTP, а также конфигурацию EtherChannel уровня 2.
Other Resources As one additional suggestion for those who intend to move on to CCNP Enterprise, consider skimming or reading Appendix P, “LAN Troubleshooting,” found on the online companion website.|Другие ресурсы В качестве еще одного предложения для тех, кто намеревается перейти на CCNP Enterprise, рассмотрите возможность беглого просмотра или чтения Приложения P «Устранение неполадок LAN», которое можно найти на сопутствующем веб-сайте.
This appendix, a copy of a chapter from the previous edition of the book, takes a troubleshooting approach to many of the topics found in Parts II and III of this book.|В этом приложении, являющемся копией главы из предыдущего издания книги, используется подход к поиску и устранению неисправностей по многим темам, содержащимся в частях II и III этой книги.
Although Cisco completely removed the word troubleshoot from the CCNA exam blueprint in its current CCNA 200-301 version, the topics still remain relevant and can be a help for reviewing and refining what you learned in Parts II and III of this book.|Несмотря на то, что Cisco полностью удалила слово «устранение неполадок» из плана экзамена CCNA в своей текущей версии CCNA 200-301, темы по-прежнему остаются актуальными и могут быть полезны при рассмотрении и уточнении того, что вы узнали в частях II и III этой книги.
