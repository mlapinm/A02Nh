D:\mailCloud\prjother\tmp\1\c25_Core Layer.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
All right, another model.|Хорошо, другая модель.
So let's go to model.|Итак, перейдем к модели.
We got to learn it, we got to know a little bit about it.|Мы должны это узнать, мы должны узнать об этом немного.
Then we'll ask you, you know, they'll ask you about the core, the distribution,|Потом мы вас спросим, ​​понимаете, вас спросят про ядро, дистрибутив,
the access.|доступ.
They got them back here.|Они вернули их сюда.
All right.|Отлично.
And we'll explain,|И мы объясним,
I'll explain a little bit about everything briefly.|Я немного обо всем объясню вкратце.
And then we'll do different lessons because remember I am breaking this up into little, little tiny morsels.|А потом мы будем проводить разные уроки, потому что помните, я разбиваю это на маленькие, маленькие кусочки.
All right so you guys can understand.|Хорошо, ребята, вы понимаете.
Again, you don't need to get into no major detail.|Опять же, вам не нужно вдаваться в подробности.
No major detail.|Никаких важных деталей.
In this, in this particular lesson, we'll talk about the core.|В этом конкретном уроке мы поговорим о ядре.
The core is literally the core of your network, right.|Ядро - это буквально ядро ​​вашей сети, верно.
The main router, that router that's gonna send information from one building to another building,|Главный маршрутизатор, тот маршрутизатор, который будет отправлять информацию из одного здания в другое,
from one campus to another campus.|из одного кампуса в другой.
What is it that you need to be concerned with at the core?|О чем вам нужно заботиться по сути?
Speed.|Скорость.
Right, you're not gonna have a 56k connection going up there right?|Хорошо, у вас не будет соединения 56k, верно?
You're gonna have metro e, you're gonna have you know,|У вас будет метро E, вы узнаете,
OC151 lines you know, you're gonna have, I don't know if even that exists.|Линии OC151, вы знаете, у вас будут, я даже не знаю, существует ли даже такое.
You're gonna have major bandwidth going across,|У вас будет большая пропускная способность,
you want to minimize the amount of things are going, you don't wanna have intra-VLAN connectivity going on in your core router,|вы хотите свести к минимуму объем выполняемых операций, вы не хотите, чтобы в вашем основном маршрутизаторе было соединение внутри VLAN,
right.|право.
Your core router has to be the one with the least amount of work.|Ваш основной маршрутизатор должен иметь наименьший объем работы.
Its main purpose is to pass information across, and one of the things you need to be concerned with, with your core router,|Его основная цель - передавать информацию, и одна из вещей, о которых вам нужно беспокоиться, - это ваш основной маршрутизатор,
not only speed.|не только скорость.
Now I only speed cuz remember, everything gets, you now, filtered or whatever, within your distribution layer.|Теперь я только ускоряю, потому что помню, все попадает, теперь, отфильтровано или что-то еще, в ваш уровень распространения.
But we'll get into that one in the next lesson.|Но мы поговорим об этом на следующем уроке.
But your core router.|Но ваш основной маршрутизатор.
Definitely this is not a good representation because I'm just showing you the three layers because your core router, you need to have redundancy.|Определенно это не очень хорошее представление, потому что я просто показываю вам три уровня, потому что ваш основной маршрутизатор должен иметь избыточность.
Because, if the, if one of those links goes down, every user gets effected,|Потому что, если одна из этих ссылок перестанет работать, это затронет каждого пользователя,
right?|право?
So you definitely want major redundancy on your core routers in case a link goes down somewhere.|Таким образом, вам определенно требуется серьезное резервирование на основных маршрутизаторах на случай, если где-то произойдет сбой канала.
Unless a link goes down, both links,|Если ссылка не будет отключена, обе ссылки,
let's say you have two links going to the,|скажем, у вас есть две ссылки на,
to the other side of the router, right?|на другую сторону роутера, верно?
You have another router, that's another core router.|У вас есть другой маршрутизатор, это еще один основной маршрутизатор.
You definitely want to have redundant links to all your core connections.|Вы определенно хотите иметь избыточные ссылки для всех ваших основных подключений.
You want to have that.|Вы хотите это иметь.
Cuz if not, it's gonna effect all your users.|Если нет, это повлияет на всех ваших пользователей.
So what Cisco's trying to tell you here is, hey, leave your core router alone.|Итак, Cisco пытается вам сказать: оставьте свой основной маршрутизатор в покое.
Don't do any kind policy based routings or end serve [INAUDIBLE] routings or anything like that.|Не выполняйте никаких видов маршрутизации на основе политик, маршрутизации [НЕИЗБЕЖНО] конечного обслуживания или чего-либо подобного.
You wanna make sure that your core router,|Вы хотите убедиться, что ваш основной маршрутизатор
it's main purpose is speed,|его основная цель - скорость,
get information across.|получить информацию.
So another thing that you need to be considering hey,|Итак, еще одна вещь, о которой вам нужно подумать, эй,
what routing protocol am I gonna use?|какой протокол маршрутизации я собираюсь использовать?
Am I gonna use RIP in there that sends every 30 seconds it's routing table, the,|Я собираюсь использовать там RIP, который каждые 30 секунд отправляет свою таблицу маршрутизации,
the entire routing table, even through you can mess around with the timers.|всю таблицу маршрутизации, даже если вы можете возиться с таймерами.
Am I going to use EHRP?|Собираюсь ли я использовать EHRP?
Well, are you using Cisco routers?|Ну, а маршрутизаторы Cisco используете?
Are you gonna use OSPF or hey, even better,|Вы собираетесь использовать OSPF или эй, даже лучше,
are you gonna use stetter crout depending how big your enterprise network is?|вы собираетесь использовать stetter crout в зависимости от размера вашей корпоративной сети?
You know I'm gonna find a definition for that enterprise network.|Вы знаете, я найду определение этой корпоративной сети.
But anyway, so,|Но все равно так,
depending how big your network is, you may want to use static routes,|в зависимости от размера вашей сети вы можете использовать статические маршруты,
that way there is no overhead whatsoever,|Таким образом, нет никаких накладных расходов,
there's no, nothing being sent out.|нет, ничего не рассылается.
You've got static routes, so, hey, maybe using default routes, who knows?|У вас есть статические маршруты, так что, может быть, с использованием маршрутов по умолчанию, кто знает?
The whole point is that you need to make that decision, but definitely redundancy extremely important at the core router.|Все дело в том, что вам нужно принять это решение, но определенно чрезвычайно важно резервирование на основном маршрутизаторе.
So information and speed, speed to get from one side to the next.|Итак, информация и скорость, скорость перехода от одной стороны к другой.
So you gotta make a decision on how much data is going across, and how important this data is that you can not lose,|Итак, вы должны принять решение о том, сколько данных передается, и насколько они важны, чтобы вы не могли их потерять.
a link and then all sudden nobody can get anywhere.|ссылка, и вдруг никто никуда не денется.
So that's what Cisco is trying to tell you here, in this core layer.|Вот что Cisco пытается сказать вам здесь, на этом базовом уровне.
Now as far as all the layers in total,|Теперь что касается всех слоев в сумме,
remember,|Помните,
one of the things that Cisco says, another conceptual blueprint,|одна из вещей, о которых говорит Cisco, еще один концептуальный план,
not necessarily needs to be three separate layers, okay?|не обязательно должно быть три отдельных слоя, хорошо?
Might just, if you have an idea of what to do, okay?|Может, если у тебя есть идея, что делать, хорошо?
So again, core layer, speed, all right?|Итак, снова уровень ядра, скорость, хорошо?
And redundancy.|И избыточность.
Very important, choose the right, choose the right type of routing, and you're gonna use a dynamic routing protocol.|Очень важно, выберите правильный, выберите правильный тип маршрутизации, и вы будете использовать протокол динамической маршрутизации.
Which routing protocol you're gonna use?|Какой протокол маршрутизации вы собираетесь использовать?
See you in the next one.|Увидимся в следующем.
[BLANK_AUDIO]|[BLANK_AUDIO]