D:\mailCloud\prjother\tmp\1\c30_Definition of Ethernet Networks.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
Welcome back everyone.|С возвращением всех.
It is time now to give a definition to this Ethernet word.|Пришло время дать определение этому слову Ethernet.
And all it really is is a contingent based access method.|И все это на самом деле - это метод случайного доступа.
Woof.|Гав.
Big word.|Большое слово.
Right, but that's all it really is.|Верно, но это все, что есть на самом деле.
It's just a way that, and it comes from a long,|Это просто способ, и он исходит из долгого,
long time ago back in the day of the dino no.|давным-давно еще во времена дино нет.
It comes back you know, in the 80s.|Вы знаете, это возвращается в 80-е.
Times of bus topologies and the beginning of star topologies,|Времена шинных топологий и начала звездных топологий,
Ethernet the way data access a network.|Ethernet - это способ доступа данных к сети.
So let's go back in time and so we can start understanding from the,|Итак, давайте вернемся в прошлое и начнем понимать с того,
from then to now because I really don't want to break down CSMA/CD here.|с тех пор и по сей день, потому что я действительно не хочу здесь разбирать CSMA / CD.
We'll break it down in the next lesson.|Мы разберем это в следующем уроке.
But you can have an idea of what's happening, okay.|Но вы можете иметь представление о том, что происходит, хорошо.
And I've got my handy dandy drawing tools here and I'm going to try and draw though I need the pencil, not the highlighter, sorry.|И у меня здесь есть свои удобные инструменты для рисования денди, и я собираюсь попробовать рисовать, хотя мне нужен карандаш, а не маркер, извините.
I'm going to try and draw with my hand, I have told hold my hand, as you know I have an injury.|Я собираюсь попробовать рисовать рукой, я сказал, держи меня за руку, потому что ты знаешь, что у меня травма.
Back, well in the day, we used to use something called a bus,|Раньше мы ездили на автобусе,
all right?|отлично?
And we have everything that was attached to that bus, right?|И у нас есть все, что было прикреплено к этому автобусу, верно?
We have a single cable, it was usually coaxial, coaxial cabling.|У нас один кабель, обычно это был коаксиальный, коаксиальный кабель.
And yes, my drawing is not the best in the world.|И да, мой рисунок не самый лучший в мире.
That's why normally use Visio to have a visual drawing here for you.|Вот почему обычно используйте Visio, чтобы иметь здесь визуальный рисунок.
So I'll, we'll do like my Picasso some day when I'm not here anymore,|Так что я, когда-нибудь мы сделаем так, как мой Пикассо, когда меня здесь больше нет,
this will be worth a lot of money.|это будет стоить больших денег.
Okay?|Ладно?
What is this?|Что это?
This is a bus topology.|Это топология шины.
Right we have a coaxial cable going across.|Справа идет коаксиальный кабель.
And we use what's called BNC connectors in our NIC cards and here we actually crimp on to the coaxial cable using something called vampire teeth.|И мы используем так называемые разъемы BNC в наших сетевых картах, и здесь мы фактически обжимаем коаксиальный кабель, используя нечто, называемое зубами вампира.
Okay.|Ладно.
Each side of the bus topology had to be terminated, had to be terminated and obviously grounded.|Каждая сторона топологии шины должна быть завершена, должна быть завершена и, очевидно, заземлена.
The reason the grounding, and again I don't want to get into any Network Plus stuff but the reason that it was grounded because if, as those books back in|Причина заземления, и опять же, я не хочу вдаваться в подробности Network Plus, но причина, по которой она была заземлена, потому что если, как эти книги вернулись в
the day would say, lightning will come down and hit the cable.|день сказал бы, что сойдет молния и ударит по кабелю.
It would just run through the cable and ground down to the floor.|Он просто проходил через кабель и заземлялся на пол.
Not going to each machine frying it as it went on it's little merry way.|Не собираюсь жарить его на каждой машине, как шло немного веселее.
But the problem with this, since it is Ethernet.|Но проблема с этим, так как это Ethernet.
Since it is Ethernet what would happen is if there was a break anywhere in the cable, anywhere in the cable,|Поскольку это Ethernet, что произойдет, если в любом месте кабеля, в любом месте кабеля будет разрыв,
if there was a break nobody in the whole entire network would be down.|если бы произошел обрыв, то никто во всей сети не отключился бы.
Because of that, because of the nature of Ethernet, of noise.|Из-за этого, из-за природы Ethernet, шума.
Because what would happen is that reflection would come back onto the wire, and everybody would be listening, they would hear noise,|Потому что произойдет то, что отражение вернется на провод, и все будут слушать, они будут слышать шум,
so they wouldn't transmit.|чтобы они не передавали.
So it didn't matter where the break was.|Так что не имело значения, где был перерыв.
The break could have been here.|Перерыв мог быть здесь.
The break could have been right there, and then nobody could have communicated.|Там мог быть разрыв, и тогда никто не мог бы общаться.
So anywhere that there was a break on there, there was an issue.|Так что везде, где был перерыв, была проблема.
If you forgot to terminate it, on one side because you wanted to go to lunch, and you forgot to terminate it on one side,|Если вы забыли прервать его, с одной стороны, потому что вы хотели пойти на обед, и вы забыли прервать его с одной стороны,
nobody would have communication.|ни у кого не было бы связи.
So a bus topology really wasn't the most ideal in the world.|Так что топология шины действительно не была самой идеальной в мире.
And that's why we kept moving up.|И поэтому мы продолжали двигаться вверх.
So we decided, that we wanted to go head and create a more centralized system,|Поэтому мы решили, что хотим пойти вперед и создать более централизованную систему,
and that's why we created the star, right?|и поэтому мы создали звезду, верно?
And then we had computers, and I like doing it this way,|А потом у нас были компьютеры, и мне нравится это делать,
cuz it's just quicker, cuz I can't draw.|Потому что это быстрее, потому что я не умею рисовать.
Right.|Правильно.
So we got a centralized system where all computers.|Итак, мы получили централизованную систему, в которой все компьютеры.
Let's say this is computer one and this is computer two.|Допустим, это компьютер один, а это компьютер два.
And this is computer three and this is computer four.|А это третий компьютер, а это четвертый.
Again, Ethernet.|Опять же, Ethernet.
Ethernet.|Ethernet.
All right, so anybody can talk to anybody depending,|Хорошо, так что любой может поговорить с кем угодно в зависимости,
depending on the central device.|в зависимости от центрального устройства.
Now, if we know we have one line right.|Теперь, если мы знаем, что у нас есть одна правильная линия.
We had a hub.|У нас был хаб.
That was not a good thing because hubs is what?|Это было нехорошо, потому что хабы - это что?
One broadcast domain and one collision domain.|Один широковещательный домен и один конфликтный домен.
Cause chaos.|Вызвать хаос.
We don't want that.|Мы этого не хотим.
If we had you know, two lines right, then we have a switch.|Если бы у нас были две строчки, значит, у нас есть переключатель.
We have a switch going on.|У нас есть переключатель.
Now we hey, now we're talking.|Эй, мы говорим.
Things are a lot better.|Все намного лучше.
It's still Ethernet.|Это все еще Ethernet.
We still have one point of failure because if this goes down, then everybody's down.|У нас все еще есть одна точка отказа, потому что если она упадет, то все упадут.
But if that switch goes down, rarely that that would happen, but if it does,|Но если этот переключатель выйдет из строя, такое случится редко, но если это произойдет,
then everybody's down.|тогда все упали.
So we still have one single point of failure, that's why redundancy is so important in your network.|Таким образом, у нас все еще есть одна единственная точка отказа, поэтому избыточность так важна в вашей сети.
But because of the nature of Ethernet, and the nature that the data accesses the wire in order to transmit information.|Но из-за природы Ethernet и того, что данные обращаются к проводам для передачи информации.
With Ethernet it's a, it's a challenge for networking,|С Ethernet это проблема для сети,
it's a challenge for networking.|это вызов для нетворкинга.
And though Ethernet has taken over, even wide area networks everything's turning to Ethernet, so that's that's the way things are going to roll, all right?|И хотя Ethernet взял верх, даже в глобальных сетях все превращается в Ethernet, так что именно так все и будет, хорошо?
So ours all types of network is due to,|Итак, все наши сети связаны с
it's going to be Ethernet, all right?|это будет Ethernet, хорошо?
But definitely using a switch node is going to be,|Но определенно использование узла переключения будет,
it is a lot better than a bus or a hub.|это намного лучше, чем автобус или хаб.
But again we came from what you don't see anymore cuz I when we did I used to draw this topology, and I would ask the question.|Но мы снова пришли из того, чего вы больше не видите, потому что когда мы это сделали, я рисовал эту топологию и задавал вопрос.
[BLANK_AUDIO]|[BLANK_AUDIO]
Is this a star?|Это звезда?
Or a ring?|Или кольцо?
They wouldn't know what to say.|Они не знали, что сказать.
Why?|Зачем?
Because, there, it looks like a star.|Потому что там это похоже на звезду.
But if it's a MAU, M-A-U, multi access unit,|Но если это MAU, M-A-U, блок множественного доступа,
that would turn it into a ring, meaning it is a physical star,|что превратит его в кольцо, то есть это физическая звезда,
but a logical ring where depending if you're using the IBM or IBM method.|но логическое кольцо, в зависимости от того, используете ли вы метод IBM или IBM.
Because IBM was or, was a creator of token ring.|Потому что IBM была или была создателем Token Ring.
And then you have the IEEE 802.5, all right.|И тогда у вас есть IEEE 802.5, хорошо.
You go either this way, or you go this way.|Вы идете либо в эту сторону, либо в другую сторону.
All right?|Отлично?
Meaning it will go to it's lower device.|Это означает, что он перейдет на его нижнее устройство.
Say, hey, is this you?|Скажи, эй, это ты?
Is this packet for you?|Этот пакет для вас?
Yes, no, and then we send it off to the next way.|Да, нет, а потом отправляем в следующий путь.
Very slow, very reliable.|Очень медленно, очень надежно.
It was based on token passing, that was it's access method,|Это было основано на передаче токена, это был метод доступа,
only the person with the token would actually speak.|только человек с жетоном будет говорить.
So, it was a very reliable network, but it was a very slow network at the same time.|Итак, это была очень надежная сеть, но в то же время это была очень медленная сеть.
Therefore Ethernet became king.|Таким образом, Ethernet стал королем.
So in the next lesson, we'll talk about the standard of Ethernet and we'll give explanations as far as to,|Итак, в следующем уроке мы поговорим о стандарте Ethernet и дадим пояснения относительно того,
what is this CSMA CD and how it works.|что это за CSMA CD и как он работает.
I'll see you in the next lesson.|Увидимся на следующем уроке.
[BLANK_AUDIO]|[BLANK_AUDIO]