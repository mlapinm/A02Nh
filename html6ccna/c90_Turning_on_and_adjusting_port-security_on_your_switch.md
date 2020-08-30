D:\mailCloud\prjother\tmp\1\c90_Turning on and adjusting port-security on your switch.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
All right, one of the last things that we're gonna talk about before, by the way,|Хорошо, кстати, одна из последних вещей, о которой мы будем говорить раньше,
welcome back.|Добро пожаловать назад.
Before, we get into inter VLAN connectivity is switch port security.|Перед тем, как мы перейдем к подключению между VLAN, мы рассмотрим безопасность портов коммутатора.
Just like we put that BPDU guard enable.|Точно так же, как мы включили защиту BPDU.
So, you know, when you turn off spanning tree, so if somebody were to plug in an internet working device,|Итак, вы знаете, когда вы выключаете связующее дерево, поэтому, если кто-то подключит рабочее устройство в Интернете,
it would shut down the port into an error disabled state?|он отключил бы порт в состоянии отключения из-за ошибки?
Switch port security is somewhat similar.|Безопасность порта коммутатора в чем-то похожа.
And what switch port security does is you can allow so many MAC addresses per port, one, two.|И что делает безопасность порта коммутатора, так это то, что вы можете разрешить так много MAC-адресов на порт, один, два.
And then you can set a violation on there that says,|И тогда вы можете установить там нарушение, которое говорит:
hey, I want to shut down the port.|эй, я хочу закрыть порт.
Or you don't want to allow them access to the network,|Или вы не хотите разрешать им доступ к сети,
whatever it is that you're trying to do.|что бы вы ни пытались сделать.
Normally it's shut down.|Обычно он выключен.
Now, in the CCNA very doubtful that they'll ask you about,|Сейчас в CCNA очень сомнительно, что вас спросят о том,
they may ask maybe one question about switch port security, but that's about it.|они могут задать один вопрос о безопасности порта коммутатора, но не более того.
Switch port security, you will see that,|Безопасность порта коммутатора, вы увидите это,
and you will configure what I'm about to configure on your CCNA security exam, okay, on your CCNA security exam.|и вы настроите то, что я собираюсь настроить на вашем экзамене безопасности CCNA, хорошо, на вашем экзамене безопасности CCNA.
So we'll do switch port security on the same ports that we turned off spanning tree cuz that's where we're plugging in stuff to, so|Итак, мы будем переключать безопасность портов на тех же портах, которые мы отключили связующее дерево, потому что именно туда мы подключаемся, поэтому
we'll do it in the same ports that we did that on the client switches.|мы сделаем это в тех же портах, что и на клиентских коммутаторах.
Now, let's go ahead and go to the faculty switch.|Теперь давайте перейдем к переключателю факультетов.
And the reason you wanna do this is because you don't want anybody just,|И причина, по которой вы хотите это сделать, заключается в том, что вы не хотите никого просто
because if you have, and the example they give you in the book,|потому что если у вас есть, и пример, который они дают вам в книге,
you're in a conference room.|вы в конференц-зале.
You have your switch with x amount of ports.|У вас есть коммутатор с x количеством портов.
Let's say it's a 12 port switch.|Допустим, это 12-портовый коммутатор.
And then you have somebody coming in with a HUB, plugging in their particular device to that, and then they can put in more|Затем кто-то входит с концентратором, подключает к нему свое конкретное устройство, а затем они могут добавить больше
computers, for whatever reason.|компьютеры по любой причине.
You don't want that, you want to have total control of what gets plugged in to your particular devices.|Вы не хотите этого, вы хотите иметь полный контроль над тем, что подключается к вашим конкретным устройствам.
So, CONFIG T,|Итак, CONFIG T,
INT RANGE F0/1-15.|ВНУТРЕННИЙ ДИАПАЗОН F0 / 1-15.
Another reason not only for me to assign the VLANs.|Еще одна причина не только для меня назначать VLAN.
But if you're gonna do switch port security,|Но если вы собираетесь переключить безопасность порта,
also your ports must be access ports cuz if you turn on switchport security and they're in dynamic auto, they'll let you know, hey, you can't do that.|также ваши порты должны быть портами доступа, потому что, если вы включите безопасность порта коммутатора, и они находятся в динамическом автоматическом режиме, они сообщат вам, эй, вы не можете этого сделать.
Port that are in dynamic auto have to be access ports.|Порт, который находится в динамическом автоматическом режиме, должен быть портом доступа.
So they're already access ports because we have VLANs assigned there.|Так что они уже имеют доступ к портам, потому что у нас там назначены VLAN.
So what I'm going to do is turn on, switch port security.|Итак, что я собираюсь сделать, это включить, переключить безопасность порта.
We should do SWITCH,|Мы должны сделать SWITCH,
T-C-H, PORT,|Т-С-Н, ПОРТ,
PORT, really?|ПОРТ, правда?
T oh, T-C-H, SWITCHPORT PORT-SECURITY.|Ой, T-C-H, SWITCHPORT PORT-SECURITY.
I was thinking, don't know then,|Я тогда подумал, не знаю,
okay,SWITCHPORT PORT-SECURITY.|хорошо, SWITCHPORT PORT-SECURITY.
That turns it on.|Это заводит его.
That turns it on.|Это заводит его.
Now, you up arrow.|Теперь стрелка вверх.
Now, what do you want to do?|Что ты хочешь делать?
This is the way that it learns, okay.|Так оно учится, хорошо.
How do you want it to learn?|Как вы хотите, чтобы это училось?
You want it to learn sticky.|Вы хотите, чтобы он стал липким.
What is sticky?|Что липкое?
Oops, did I type something wrong?|Упс, я что-то не так ввел?
[BLANK_AUDIO]|[BLANK_AUDIO]
Oh, SWITCHPORT PORT-SECURITY mac, sorry,|О, SWITCHPORT PORT-SECURITY mac, извините,
mac sticky, sorry.|Mac липкий, извините.
How do you want it to learn the mac addresses that it's going to,|Как вы хотите, чтобы он узнал MAC-адреса, на которые он собирается,
that you're going to control?|что вы собираетесь контролировать?
You can do it statically or you can do it dynamically.|Вы можете делать это статически или динамически.
That's what sticky means.|Вот что значит липкий.
It will learn it dynamically, but when it adds it to the mac address table,|Он будет изучать его динамически, но когда он добавит его в таблицу MAC-адресов,
it'll show that it is static.|он покажет, что он статичен.
It's there, and it's there to stay.|Он там, и он должен остаться.
So that's what the sticky command does.|Вот что делает липкая команда.
So it learns it dynamically, but it adds it as a static entry into your mac address table.|Таким образом, он изучает его динамически, но добавляет его как статическую запись в вашу таблицу MAC-адресов.
All right, up arrow again, now the maximum, what is the maximum number?|Хорошо, снова стрелка вверх, теперь максимум, какое максимальное число?
You can have up to 133 or 132 maximum mac addresses, right?|У вас может быть до 133 или 132 максимальных MAC-адресов, верно?
You two, you know a laptop, a desktop, and that's it.|Вы двое, вы знаете ноутбук, настольный компьютер и все.
So you wanna allow only two computers with that.|Итак, вы хотите разрешить использовать это только для двух компьютеров.
And then the last one is the violation.|И последнее - нарушение.
What type of violation do you want?|Нарушение какого типа вы хотите?
Do you wanna protect?|Вы хотите защитить?
Do you wanna restrict?|Вы хотите ограничить?
Do you wanna shut down?|Вы хотите выключиться?
If you shut down, that's what we want.|Если вы отключитесь, это то, чего мы хотим.
We wanna put the port in, or disable.|Мы хотим вставить порт или отключить.
If you wanna restrict, then that just does, doesn't allow you onto the network.|Если вы хотите ограничить, то это просто не позволяет вам подключиться к сети.
So, what we're gonna do is, we're gonna say SHUT, done.|Итак, что мы собираемся сделать, мы скажем ВЫКЛЮЧИТЬ, готово.
DO WR, if you want to take a look at it,|DO WR, если вы хотите взглянуть на это,
you can do show Port-security, and it tells you right there.|вы можете показать Port-security, и он вам тут же скажет.
Hey, port security is on these, these particular ports.|Эй, безопасность портов находится на этих портах.
You got, I'm allowing two mac addresses.|У вас есть, я разрешаю два MAC-адреса.
Right now there is no mac addresses on there.|Прямо сейчас там нет MAC-адресов.
There are no violations.|Нарушений нет.
And if there was, if there was a violation, the port would be shut down.|А если бы было, если бы было нарушение, то закрыли бы порт.
So let's do that on switch number 2, which is the student switch.|Итак, давайте сделаем это на переключателе номер 2, который является переключателем ученика.
Same exact thing, very simple, same ports.|То же самое, очень простое, те же порты.
CONFIG T, INT RANGE, F0/1-15.|КОНФИГ T, ВНУТРЕННИЙ ДИАПАЗОН, F0 / 1-15.
Turn it on, Switchport PORT, try and abbreviate too much, PORT-security, Enter.|Включите его, Switchport PORT, попробуйте сократить слишком много, PORT-security, Enter.
Up arrow, mac sticky, all right, that's how it's going to learn the mac addresses.|Стрелка вверх, Mac липкий, хорошо, вот как он будет узнавать MAC-адреса.
Maximum of two MAC addresses, I want them to use, I said, the first two, done.|Максимум два MAC-адреса, я хочу, чтобы они использовали, я сказал, первые два, готово.
If somebody else tries to plug in a third computer that's not part of that,|Если кто-то другой попытается подключить третий компьютер, не являющийся его частью,
that's when it shuts down the port.|вот когда он закрывает порт.
And then, the last one is the violation where we want it to shutdown.|И затем, последнее - нарушение, когда мы хотим, чтобы он отключился.
And this exactly is what you gotta do,|И это именно то, что ты должен делать,
very simple, very simple and all, but very important.|очень просто, очень просто и все такое, но очень важно.
Because you want to be able to allow only certain computers on there, all right,|Потому что вы хотите, чтобы там были только определенные компьютеры, хорошо,
the ones that you plugged in, the ones that you configured, all right.|те, которые вы подключили, те, которые вы настроили, хорошо.
Everybody else comes to work.|Все остальные приходят на работу.
Nobody comes to work with their desktop underneath their hand.|Никто не приходит на работу с рабочим столом под рукой.
And they have the laptop just like in any university.|И у них есть ноутбук, как в любом университете.
In any university, when they start putting,|В любом университете, когда начинают ставить,
let's say mac filtering in wireless,|скажем, фильтрация Mac в беспроводной сети,
they'll ask you, what's your mac address?|Вас спросят, какой у вас MAC-адрес?
And you can have up to two, you can have a desktop and a laptop.|И у вас может быть до двух, у вас может быть настольный компьютер и ноутбук.
And you'll take their mac addresses, put them down, and put them in a mac filter table.|И вы возьмете их MAC-адреса, запишите их и поместите в таблицу фильтров Mac.
So, there's a whole, you know, way,|Итак, есть целый способ,
there's many ways to secure, obviously.|очевидно, есть много способов обезопасить себя.
This is just one of the ways that you do secure the the switches using switch port security, all right?|Это всего лишь один из способов защитить коммутаторы с помощью защиты порта коммутатора, хорошо?
So now we've pretty much.|Итак, теперь у нас довольно много.
Let's do a DO W, let's do a WR to make sure we copy that, okay?|Давайте сделаем DO W, давайте сделаем WR, чтобы убедиться, что мы это скопировали, хорошо?
And I believe we did it on this one,|И я считаю, что мы сделали это на этом,
right?|право?
We did a WR?|Мы сделали WR?
Just in case, let's do a WR.|На всякий случай сделаем WR.
And that's it.|И это все.
That's your switch port security.|Это безопасность вашего порта коммутатора.
Now next, we gotta get these two computers to talk to each other.|Теперь нам нужно заставить эти два компьютера общаться друг с другом.
There's two different VLANs.|Есть две разные сети VLAN.
Get ready for inter VLAN routing.|Будьте готовы к маршрутизации между VLAN.
I'll see you in the next session.|Увидимся на следующем сеансе.
[BLANK_AUDIO]|[BLANK_AUDIO]