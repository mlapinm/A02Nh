D:\mailCloud\prjother\tmp\1\c66_Accessing & manipulating the register within ROMMON.md  


__|__
--|--
All right welcome back.|Хорошо, добро пожаловать обратно.
One of the things that before, before we start, one of the things that I forgot to mention in the last lecture but I'm going to show you again, it's related.|Одна из вещей, о которой раньше, прежде чем мы начнем, одна из вещей, о которых я забыл упомянуть в последней лекции, но я собираюсь показать вам снова, это связано.
You can see when we back to 2102 and it did load all my configurations.|Вы можете увидеть, когда мы вернулись к 2102, и он загрузил все мои конфигурации.
My interfaces are still down.|Мои интерфейсы все еще не работают.
What happens when the router reloads and the registries were changed,|Что происходит, когда маршрутизатор перезагружается и реестры были изменены,
the interfaces actually stay down, okay?|интерфейсы на самом деле не работают, хорошо?
So you gotta make sure that you want to go ahead.|Так что вы должны убедиться, что хотите идти вперед.
Because if you were to do a show IP int brief,|Потому что, если бы вы сделали бриф show IP int,
you see they are all administratively down.|вы видите, что все они административно отключены.
So we're going to first go ahead and turn on the F00 and then the F001 because obviously you want connectivity.|Итак, мы собираемся сначала включить F00, а затем F001, потому что, очевидно, вам нужна возможность подключения.
So, config T, not config Y.|Итак, конфигурация T, а не конфигурация Y.
Config T Interface F0/0.|Конфиг Т Интерфейс F0 / 0.
Let's do a no shut on that.|Давайте не будем закрывать глаза на это.
And do interface S0/0/1.|И делаем интерфейс S0 / 0/1.
Let's do a no shut on that.|Давайте не будем закрывать глаза на это.
DWR CTRL+Z, we do a show IP and brief again and we arrow to it.|DWR CTRL + Z, мы снова показываем IP-адрес и брифинг, и переходим к нему.
Now everything is up up.|Теперь все встало.
Once span tree finishes it's thing here,|Как только Span Tree закончит, он здесь,
this amber light will go to green.|этот желтый индикатор станет зеленым.
Now, so I failed to mention that.|Итак, я не упомянул об этом.
I do apologize.|Я действительно сожалею.
But remember when you are changing the rates resettings and you come, you know,|Но помните, когда вы меняете тарифы и приходите, понимаете,
and the router reloads,|и маршрутизатор перезагружается,
what's gonna happen is your interfaces will go administratively down.|что произойдет, так это то, что ваши интерфейсы отключатся административно.
Make sure to check your interfaces.|Обязательно проверьте свои интерфейсы.
That they're all up up, at least the ones that I need to be up up, okay.|Что они все встали, по крайней мере те, которые мне нужны, ладно.
Now, let's exit the router.|Теперь выйдем из роутера.
[COUGH] Let's say, and now because we're at this lesson,|[КАШЕ] Скажем так, и теперь, поскольку мы на этом уроке,
I want to show you how to work,|Я хочу показать тебе, как работать,
and how to get to ROMmon, alright.|и как добраться до ROMmon, хорошо.
Let's say whatever reason, you need to log into a router [NOISE] I have no idea [NOISE] I don't know,|Допустим, по какой-то причине вам нужно войти в маршрутизатор [NOISE] Понятия не имею [NOISE] Не знаю,
I don't know, I don't know.|Не знаю, не знаю.
I forgot my password there's nobody around now this is something that you really don't want to do during the day unless your very quick|Я забыл свой пароль, сейчас вокруг никого нет, это то, чем вы действительно не хотите заниматься в течение дня, если только не очень быстро
[LAUGH] alright but you wanna do this in the middle of the night.|[СМЕХ] Хорошо, но ты хочешь сделать это посреди ночи.
Routers, servers, you know,|Маршрутизаторы, серверы, ну знаете,
they do not yet reboot it.|они его еще не перезагружают.
I think there was a trivia question that I found online.|Я думаю, что я нашел в Интернете один пустяковый вопрос.
The longest router that was ever on,|Самый длинный маршрутизатор, который когда-либо был включен,
that, you know,|это ты знаешь,
never rebooted, was like eight years or something like that.|ни разу не перезагружался, лет восемь или что-то в этом роде.
But you normally don't want to reboot or you know take down the router during the middle of the day.|Но обычно вы не хотите перезагружаться или знаете, что отключите маршрутизатор в середине дня.
If you gonna do something like this you know,|Если ты собираешься сделать что-то подобное, ты знаешь,
maybe wait until the least amount of traffic at least within your network or if you can help it do it after hours,|возможно, дождитесь минимального объема трафика, по крайней мере, в вашей сети, или, если вы можете помочь, сделать это в нерабочее время,
after hours.|в нерабочее время.
There, you more likely will have a maintenance window that it will allow you to do any kinda these changes.|Там у вас, скорее всего, будет окно обслуживания, которое позволит вам вносить любые подобные изменения.
Obviously email people if you're going to do this throughout the day because you will be taking people down.|Очевидно, напишите людям, если вы собираетесь делать это в течение дня, потому что вы будете сбивать людей с толку.
Meaning they wont have access to certain things across these routers.|Это означает, что у них не будет доступа к определенным вещам через эти маршрутизаторы.
All right so you don't know your password.|Хорошо, так что вы не знаете свой пароль.
So obviously here's a real router I got to go to a tab turn off go to another tab and do what I go to do.|Итак, очевидно, что это настоящий маршрутизатор, мне нужно перейти на вкладку, выключить, перейти на другую вкладку и сделать то, что я собираюсь делать.
What you would do is,|Что бы вы сделали,
you would turn off your router.|Вы бы выключили свой роутер.
Turn it back on.|Включите его снова.
And you would use a break command.|И вы могли бы использовать команду break.
And this is why I say it that way.|И поэтому я так говорю.
Your book says CTRL+Pause Break.|В вашей книге написано CTRL + Pause Break.
CTRL+Pause Break.|CTRL + пауза в перерыве.
On my laptop, there's no Pause Break.|На моем ноутбуке нет паузы.
Also matters that control pause break does not work.|Также имеет значение, что не работает контрольная пауза.
So whatever break command you wanna use,|Итак, какую бы команду прерывания вы ни использовали,
use it.|используй это.
CTRL+C, that that works on,|CTRL + C, что работает,
on so, on a lot of routers.|так, на многих маршрутизаторах.
So as long as there's a break command,|Итак, пока есть команда перерыва,
you wanna interrupt is what you're doing.|вы хотите прервать то, что вы делаете.
You're interrupting the boot sequence to allow you to get into ROMmon.|Вы прерываете последовательность загрузки, чтобы вы могли войти в ROMmon.
Because you're going to have to change the registry setting in ROMmon to that 2142.|Потому что вам придется изменить параметр реестра в ROMmon на этот 2142.
That would allow you to go back in,|Это позволит вам вернуться,
so you can change the passwords.|так что вы можете изменить пароли.
All right,|Отлично,
all the passwords that you need to change cause you forgot let's say all of them.|все пароли, которые вам нужно изменить, потому что вы забыли, скажем, все.
And then you can get in your router again.|И тогда вы можете снова войти в свой роутер.
All right so, let's go ahead and do that.|Хорошо, давайте продолжим и сделаем это.
So I want to go aways and go to the.|Итак, я хочу уйти и перейти к.
I will go into the physical tab.|Я перейду в физическую вкладку.
I'm gonna turn off my router.|Я выключу свой роутер.
For now my router's off.|Пока мой роутер выключен.
Meaning, saw my interfaces,|То есть увидел мои интерфейсы,
they're completely down.|они полностью упали.
I'm gonna turn 'em back on.|Я верну их.
I'm gonna go to the CLI tab,|Я перейду на вкладку CLI,
and I'll do CTRL+C.|и я сделаю CTRL + C.
Now you, I am in ROMmon.|Теперь ты, я в ROMmon.
Now I'm gonna bring it up here.|Теперь я подниму это сюда.
I am in ROMmon, ROM monitor mode.|Я нахожусь в режиме ROMmon, монитора ROM.
Again this is a dark dirty place you don't want to be here if you don't have to be here.|Опять же, это темное грязное место, где ты не хочешь быть, если тебе не нужно быть здесь.
Our purposes for being here is to change the register because we could not get into the router to do what we needed to do.|Наша цель здесь - изменить регистр, потому что мы не можем войти в маршрутизатор, чтобы сделать то, что нам нужно.
So here case sensitive commands are slightly different.|Так что здесь команды, чувствительные к регистру, немного отличаются.
In the previous lessens we did config-reg,|В предыдущих уменьшениях мы использовали config-reg,
right?|право?
Short for register.|Сокращение от регистра.
Here we're going to do confreg,|Вот и займемся конфрегом,
and it is case sensitive, so I want to keep everything lowercase.|и он чувствителен к регистру, поэтому я хочу сохранить все в нижнем регистре.
Confreg.|Конфрег.
Hello.|Привет.
Confreg space 0x2142 ENTER.|Confreg space 0x2142 ENTER.
That means configure registry.|Это означает настройку реестра.
All right.|Отлично.
So, we're configuring the registry 2142,|Итак, настраиваем реестр 2142,
there's the command right there.|вот команда прямо там.
All right, confreg 214, 0x2142 and then we type the word reset which will reload our router.|Хорошо, confreg 214, 0x2142, а затем мы набираем слово reset, которое перезагрузит наш маршрутизатор.
So our router should now come up in set up mode again because we changed the register.|Итак, наш маршрутизатор должен снова перейти в режим настройки, потому что мы изменили регистр.
And lets see and here we are in set up mode, we're going to say no, obviously.|И давайте посмотрим, и вот мы находимся в режиме настройки, мы, очевидно, собираемся сказать нет.
And now we're in a blank configuration again, show run,|И теперь мы снова в пустой конфигурации, показываем,
because when we do a show start you're actually going to see what's in the start,|потому что когда мы начинаем шоу, вы действительно увидите, что в самом начале,
you want to see what's in the run,|ты хочешь увидеть, что в бегах,
and there's nothing.|и ничего нет.
So one of the changes, before you make any changes, before you make any changes.|Итак, одно из изменений, прежде чем вносить какие-либо изменения, прежде чем вносить какие-либо изменения.
One of the things that you want to do is like we did before.|Одна из вещей, которую вы хотите сделать, такая же, как и мы.
You want to copy whatever's in your start,|Вы хотите скопировать все, что у вас есть,
whatever's inside that NV RAM,|что бы ни было внутри этой NV RAM,
you want to make sure you copy it to your RAM.|вы хотите убедиться, что вы скопировали его в свою оперативную память.
Into your run, where you're at right now.|В путь, где вы сейчас находитесь.
You wanna do that.|Ты хочешь это сделать.
Why do you wanna do that?|Почему ты хочешь это сделать?
Because if you accidentally, you know,|Потому что, если вы случайно знаете,
you go in there and you make your change you know the password changes, oh great,|вы заходите туда и вносите изменения, вы знаете, что пароль меняется, о, отлично,
I changed my password copy run start.|Я изменил свой пароль на запуск копирования.
So you're copying just what's in ram right now to the same file name so you will overwrite what you did.|Итак, вы сейчас копируете только то, что находится в оперативной памяти, в файл с тем же именем, чтобы перезаписать то, что вы сделали.
So you just blew away everything else.|Значит, вы просто сдули все остальное.
So the first thing that I advise you to do when you did this procedure that you did not know your password.|Итак, первое, что я вам советую сделать при выполнении этой процедуры, чтобы вы не знали своего пароля.
I want you, and you did a CTRL+Break,|Я хочу тебя, и ты сделал CTRL + Break,
you changed confreg,0x2142 and then you hit reset,|вы изменили confreg, 0x2142, а затем нажали сброс,
your router rebooted into set up mode.|ваш роутер перезагрузился в режим настройки.
You're gonna go ahead and copy whatever's in your NV RAM to your RAM.|Вы собираетесь скопировать все, что находится в вашей NV RAM, в вашу RAM.
The opposite, right.|Напротив, верно.
So you're gonna copy start run,|Итак, вы собираетесь копировать, запускать,
that's the exact what we did before but now I'm giving you a reason why to do that cause now all your configurations are in,|это именно то, что мы делали раньше, но теперь я даю вам причину, почему это нужно сделать, потому что теперь все ваши конфигурации находятся в
are in the run alright.|в бегах хорошо.
So lets say you already changed your passwords cause we already know what our passwords are I'm just going to change the registry right now while I'm in there.|Допустим, вы уже изменили свои пароли, потому что мы уже знаем, каковы наши пароли. Я просто собираюсь изменить реестр прямо сейчас, пока я там.
So I want to go ahead and do config-reg 0x2102.|Итак, я хочу продолжить и выполнить config-reg 0x2102.
ENTER.|ВОЙТИ.
And now I can do copy run start.|И теперь я могу запустить копирование.
Oop, can't do it from there.|Уп, не могу сделать это оттуда.
Let me do it the proper way.|Позвольте мне сделать это как следует.
Exit, and then do copy run start ENTER.|Выйдите, а затем выполните копирование, запуск, нажмите ENTER.
It's filing, ENTER.|Это подача, ВВОД.
Not a problem, right.|Не проблема, правда.
If we do a show ver, it's going to show me, because right now, we're on 2142.|Если мы сделаем шоу-вер, это покажет мне, потому что сейчас мы на 2142.
On our next reload we're going to be on 2102.|При следующей перезагрузке мы будем на 2102.
But take a look at our interfaces.|Но взгляните на наши интерфейсы.
They're down.|Они упали.
They're down, so let's go ahead and reload to make sure that everything did take effect.|Они не работают, поэтому давайте продолжим и перезагрузим, чтобы убедиться, что все сработало.
So that little piece right there,|Так что этот маленький кусочек прямо там,
again, to get to ROMmon,|снова, чтобы попасть в ROMmon,
just enter the boot sequence,|просто введите последовательность загрузки,
CTRL+C or CTRL+Pause Break,|CTRL + C или CTRL + пауза,
whatever break command it will allow you to use.|какую бы команду перерыва вы ни использовали.
All right.|Отлично.
And then once you do that,|И как только вы это сделаете,
once you change the registry settings and you reset, the very first thing I'm advising you to do is copy whatever's in your start to your run.|как только вы измените настройки реестра и сбросите настройки, первое, что я советую вам сделать, - это скопировать все, что находится в вашем старте, в ваш запуск.
Then make your changes then save your changes, okay.|Затем внесите изменения, затем сохраните изменения, хорошо.
And then you don't have to reload.|И тогда не нужно перезагружать.
If the router reloads on its on that's his problem.|Если роутер перезагружается, это его проблема.
Okay, but at least you'll have it where its suppose to be and it will look at NV RAM.|Хорошо, но, по крайней мере, он у вас будет там, где он должен быть, и он будет смотреть на NV RAM.
And then Cisco.|А потом Cisco.
And then everything is good to go.|И тогда все хорошо.
We look at the show ver.|Смотрим на шоу вер.
All about it, we're 2102.|В общем, мы 2102.
So now you know how to get into ROMmon if you had to, by doing a CTRL+C.|Итак, теперь вы знаете, как в случае необходимости попасть в ROMmon, нажав CTRL + C.
Now, somebody told me, hey Laz,|Кто-то сказал мне, эй, Лаз,
is that a security, problem?|это проблема безопасности?
Sure, I mean, if your router is sitting at the receptionist desk, but its not.|Конечно, я имею в виду, если ваш роутер стоит у администратора, но это не так.
Its behind a closed door,|Это за закрытой дверью,
with a badge access,|со значком доступа,
that no body has access to your routers.|что никто не имеет доступа к вашим маршрутизаторам.
Only the people that need to have access to your routers.|Только люди, которым нужен доступ к вашим роутерам.
Lets say like in a school environment.|Скажем так, в школьной среде.
If your in a school environment,|Если вы в школьной среде,
unless the, Executive Director or the Director of Education is,|за исключением случаев, когда исполнительный директор или директор по образованию,
are CCNA certified or CCNP or CCIEs, they have no need.|сертифицированы CCNA, CCNP или CCIE, в них нет необходимости.
They have their own job.|У них своя работа.
They have no need to be in my telecommunications closet.|Им незачем находиться в моем телекоммуникационном шкафу.
I am the IT Director, I am the IT administrator, I am the Cisco person.|Я ИТ-директор, я ИТ-администратор, я человек Cisco.
So I am the only one, and whoever I choose to the,|Так что я единственный, и кого бы я ни выбрал,
implement to go ahead and say hey,|реализовать, чтобы идти вперед и сказать привет,
you're going to be my assistant.|ты будешь моим помощником.
You're going to go ahead and go in there and do whatever you need to do.|Вы собираетесь пойти вперед и пойти туда и сделать все, что вам нужно.
We're the only ones that have access to that particular telecommunications closet where your routers are at.|Мы единственные, у кого есть доступ к тому конкретному телекоммуникационному шкафу, где находятся ваши маршрутизаторы.
Nobody else.|Никто другой.
I don't care if you're the owner of the school.|Меня не волнует, являетесь ли вы владельцем школы.
Because if something happens to those routers.|Потому что, если что-то случится с этими роутерами.
Guess what rolls downhill?|Угадайте, что катится под гору?
Okay?|Ладно?
And it's gonna come back to you.|И это вернется к вам.
So, you are in charge of your network, and one of the first things with security is physical security.|Итак, вы отвечаете за свою сеть, и одна из первых задач безопасности - это физическая безопасность.
You gotta make sure that only the people that have,|Вы должны убедиться, что только люди, у которых есть
that need to have access have access to that particular location.|которые должны иметь доступ, имеют доступ к этому конкретному месту.
So do not set your routers or switches in a location where people can do damage to them, okay.|Так что не устанавливайте свои маршрутизаторы или коммутаторы в таком месте, где люди могут нанести им вред, хорошо.
So, just so you know,|Итак, чтобы вы знали,
because they say well,|потому что говорят хорошо,
can you disable the control pause break?|можно отключить контрольную паузу?
Yeah, you can.|Ага, можешь.
But what's going to happen when you forget your password?|Но что произойдет, если вы забудете свой пароль?
What's going to happen then?|Что тогда будет?
You're going to run into a little issue,|Вы столкнетесь с небольшой проблемой,
aren't you?|не так ли?
So careful with that.|Так осторожно с этим.
You don't have to disable it,|Вам не нужно отключать его,
just make sure that you, your routers,|просто убедитесь, что вы, ваши маршрутизаторы,
they're in a telecommunications closet.|они в телекоммуникационном шкафу.
Only IT people, IT personnel,|Только айтишники, айтишники,
that have the level of clearance to get in there need to get in there.|которые имеют уровень допуска, чтобы попасть туда, должны попасть туда.
Other than that,|Помимо этого,
you don't need to be there, okay.|тебе не нужно быть там, ладно.
Just wanna, I know I'm kinda pushing that issue, but I been asked a question many,|Просто хочу, я знаю, что подталкиваю к этой проблеме, но мне задавали вопрос многие,
many times, and it's like,|много раз, и это как
and I seen it with my eyes,|и я видел это своими глазами,
people that don't need to be inside our telecommunications closet, are in there.|там есть люди, которым не обязательно находиться в нашем телекоммуникационном шкафу.
And that's the wrong, wrong answer.|И это неправильный, неправильный ответ.
Wrong answer.|Неправильный ответ.
But again, so that was ROMmon.|Но опять же, это был ROMmon.
Again, you need to turn on your interfaces, don't forget.|Опять же, вам нужно включить ваши интерфейсы, не забывайте.
So config, hyphen T,|Итак, конфиг, дефис T,
same interfaces, interfaces F0/0.|те же интерфейсы, интерфейсы F0 / 0.
We do a no shut.|Мы ничего не делаем.
And interface S0/0/1.|И интерфейс S0 / 0/1.
We do a no shut.|Мы ничего не делаем.
Alright.|Хорошо.
DWR.|DWR.
We got green lights.|У нас есть зеленые огни.
Everything's good to go,|Все хорошо,
we made our changes, we're back at 2102.|мы внесли свои изменения, мы вернулись на 2102.
At the default setting of the registry,|По умолчанию в реестре
we're set to go and that's it.|мы готовы к работе, и все.
So again, for your test, they'll probably ask you very basic questions o, on that.|Опять же, для вашего теста они, вероятно, зададут вам очень простые вопросы по этому поводу.
Okay, but at least know now how to get into ROMmon and how to manipulate the registry by doing either config hyphen register within the router or confreg.|Хорошо, но теперь, по крайней мере, вы знаете, как войти в ROMmon и как манипулировать реестром, выполнив регистрацию дефиса конфигурации в маршрутизаторе или confreg.
C-O-N-F-R-E-G, 0x2042 within ROMmon.|C-O-N-F-R-E-G, 0x2042 в ROMmon.
I'll see you in the next lecture.|Увидимся на следующей лекции.