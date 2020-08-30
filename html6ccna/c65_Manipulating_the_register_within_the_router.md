D:\mailCloud\prjother\tmp\1\c65_Manipulating the register within the router.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
Welcome back everyone.|С возвращением всех.
We're gonna learn now about the registry or the register.|Мы собираемся узнать сейчас о реестре или реестре.
How do I manipulate it, while we're inside the router?|Как мне им манипулировать, пока мы внутри роутера?
Now, the register there's really only three,|Теперь в реестре всего три,
I'm gonna open up notepad real quick.|Я собираюсь быстро открыть блокнот.
There's only three that you really need to, three, or really two that you need to know of, okay?|Вам действительно нужно всего три, три или два, о которых вам нужно знать, хорошо?
I'm gonna make this smaller here.|Я сделаю это здесь меньше.
All right, this deals with the register of the router.|Ладно, это касается реестра роутера.
[BLANK_AUDIO]|[BLANK_AUDIO]
All right.|Отлично.
We need to deal with 0x2102.|Нам нужно разобраться с 0x2102.
I think we mentioned it previously.|Думаю, мы уже упоминали об этом ранее.
Briefly mentioned it, 2141.|Кратко упомянул, 2141.
2102 [NOISE],|2102 [ШУМ],
what, what that means is LOOK AT NVRAM.|что это означает, ПОСМОТРЕТЬ NVRAM.
And this is the default setting so right by default as the router boot process remember when we spoke on the router boot process|И это настройка по умолчанию, так что по умолчанию, поскольку процесс загрузки маршрутизатора помнит, когда мы говорили о процессе загрузки маршрутизатора
that after the iOS image is found and it's gonna load.|это после того, как изображение iOS будет найдено и оно загрузится.
What does it look at next?|На что он смотрит дальше?
It looks at the registry settings.|Смотрит в настройках реестра.
One of the things that it's looking at is that number.|Одна из вещей, на которую он смотрит, - это номер.
Is, one of, one of these numbers.|Это одно из этих чисел.
Or not 2141, I'm sorry, 2142.|Или не 2141, извини, 2142.
Sorry about that.|Извини за это.
2102, the, the, these are hex numbers,|2102, the, the, это шестнадцатеричные числа,
obviously.|очевидно.
The 0x is just an identifier.|0x - это просто идентификатор.
If it's set to 2102 which is the default setting,|Если установлено значение 2102, которое является настройкой по умолчанию,
it's going to take a look at the NVRAM.|он собирается взглянуть на NVRAM.
Meaning taking a look at the starting configuration file to see if there's any configurations.|Это означает взглянуть на файл начальной конфигурации, чтобы увидеть, есть ли какие-либо конфигурации.
And if so, it will load them.|И если так, он их загрузит.
That is the default setting.|Это настройка по умолчанию.
All right?|Отлично?
2142, if you change it to that,|2142, если вы измените его на это,
it would BYPASS NVRAM.|он будет ОБХОДИТЬ NVRAM.
No you would need to change it to that in order for, you know, for it to do that.|Нет, вам нужно будет изменить его на это, чтобы, знаете ли, для этого.
So on the boot up process, when they find the iOS image, and the flash is going to load.|Итак, в процессе загрузки, когда они находят образ iOS, и флеш-память загружается.
The flash what does it look at?|Вспышка на что смотрит?
It looks at the registry setting.|Смотрит на настройку реестра.
It says, hey, 2142.|Там написано: "Эй, 2142".
I'm not going to bother even looking at the start up config.|Я не собираюсь даже смотреть на конфигурацию запуска.
I'm going to go ahead and go straight to RAM and just load the router in set up mode, in set up mode.|Я собираюсь пойти дальше и сразу перейти к ОЗУ и просто загрузить маршрутизатор в режиме настройки, в режиме настройки.
And then just let whoever's there get inside the router and do what they gotta do.|А затем просто позвольте всем, кто там есть, проникнуть внутрь маршрутизатора и сделать то, что они должны делать.
Normally you do this 2142 when you, for whatever reason, you forget your password and this how the,|Обычно вы делаете это 2142, когда по какой-то причине забываете свой пароль, и вот как
the, the book wants to show you to reset your password.|книга хочет показать вам, как сбросить пароль.
You actually change the registry setting to 2142.|Фактически вы меняете параметр реестра на 2142.
But you can't do it while, if you can't get inside the router,|Но пока нельзя, если внутрь роутера не попасть,
you just can't do it the way we are about to do it.|вы просто не можете сделать это так, как мы.
Though in another lesson, I'll show you how to bypass all that and do it within inside ROMmon, ROMmon.|Хотя в другом уроке я покажу вам, как все это обойти и сделать это внутри ROMmon, ROMmon.
Okay.|Ладно.
Be careful.|Быть осторожен.
A word of warning.|Слово предупреждения.
You can work perfectly.|Вы можете отлично работать.
Let's say you change it to 2142, which we're about to do, and your router reboots, it's gonna reboot with an empty configuration.|Допустим, вы изменили его на 2142, что мы собираемся сделать, и ваш маршрутизатор перезагрузится, он перезагрузится с пустой конфигурацией.
Real story, a location, or a training center that I worked at,|Реальная история, место или учебный центр, в котором я работал,
they had I remember one manufacturer router for whatever reason the previous individual that was there changed the registry settings to 2142, and one Monday|у них был, я помню, один маршрутизатор производителя по какой-либо причине предыдущий человек, который был там, изменил настройки реестра на 2142, и один понедельник
morning when everybody came into work there nobody could get access to the internet and to other things all cuz they needed the router to do that.|Утром, когда все пришли на работу, никто не мог получить доступ к Интернету и прочему, потому что для этого им нужен был маршрутизатор.
The reason for it was because it booted up in a blank configuration even though you can leave it at 2142 and you can work|Причина в том, что он загрузился в пустой конфигурации, хотя вы можете оставить его на 2142 и работать.
perfectly fine not a problem you can go back and fourth sideways in and out it doesn't matter.|отлично, не проблема, вы можете возвращаться и четверть боком внутрь и наружу, это не имеет значения.
The problem comes if there is a power outage.|Проблема возникает при отключении электроэнергии.
If there is a power outage or a brownout for whatever reason,|Если по какой-либо причине произошло отключение электроэнергии или отключение электричества,
that router reboots and comes back up and the setting of the register is set to 2142, it will load and empty configuration file.|этот маршрутизатор перезагружается и возвращается в рабочее состояние, а значение регистра установлено на 2142, он загрузит и очистит файл конфигурации.
There will be no configurations whatsoever.|Никаких конфигураций не будет.
You're gonna get a lot of help desk calls.|Тебе будут звонить в службу поддержки.
So if you do change the register settings to 2142 or any other setting for that matter because you have to troubleshoot or|Поэтому, если вы измените настройки реестра на 2142 или любой другой параметр в этом отношении, потому что вам нужно устранить неполадки или
you do whatever it is you need to do make sure that you always set it back to 2102, because, so we can look at that particular,|вы делаете то, что вам нужно, убедитесь, что вы всегда устанавливаете его обратно на 2102, потому что, чтобы мы могли посмотреть на это,
file to load the, the configurations.|файл для загрузки, конфигурации.
The only exception, the only exception to that rule is if you're deliberately putting in boot system commands that will tell the router to look for|Единственное исключение, единственное исключение из этого правила - если вы намеренно вводите команды загрузочной системы, которые будут указывать маршрутизатору искать
configuration files or iOS's somewhere else.|файлы конфигурации или iOS где-нибудь еще.
That will be the only exception to that rule, but nor, normally, that will look for, first of all it will look at flash,|Это будет единственным исключением из этого правила, но, как правило, он не будет искать, прежде всего он будет смотреть на вспышку,
right, for the iOS and then it will look at the NVRAM for the startup-config file to load those configs.|верно, для iOS, а затем он будет искать в NVRAM файл начальной конфигурации, чтобы загрузить эти конфигурации.
So what I'm going to show you now is, I'm going to show you how to manipulate and look at the registry when you're in the|Итак, сейчас я покажу вам, как управлять реестром и просматривать его, когда вы находитесь в
router, nothing too difficult,|роутер, ничего сложного,
nothing too difficult.|ничего сложного.
So this is router two.|Итак, это второй маршрутизатор.
Let's first take a look at a registry and see what it's set at.|Давайте сначала взглянем на реестр и посмотрим, на что он настроен.
So, SH VER, short for version.|Итак, Ш ВЕР, сокращение от версии.
We hit Enter and I hit space bar all the way to the bottom.|Мы нажимаем Enter, а я нажимаю пробел до конца.
And I'm gonna enter a couple times just to bring it up.|И я собираюсь войти пару раз, чтобы поднять этот вопрос.
And you can see right there it's set to 2102.|И вы можете видеть, что он установлен на 2102.
That is the default setting.|Это настройка по умолчанию.
That is the default setting.|Это настройка по умолчанию.
Well, I want to change that.|Что ж, я хочу это изменить.
I wanna change it up to 2142 for whatever reason I need to change that.|Я хочу поменять его на 2142 по какой-то причине.
Okay, so I'm going to go CONFIG, I have to be in global configuration, so I put myself there and then go CONFIG-|Хорошо, я собираюсь перейти в CONFIG, я должен быть в глобальной конфигурации, поэтому я помещаю себя туда, а затем перехожу в CONFIG-
sorry REG,|извините REG,
which is register, CONFIG REGISTER, and then I change it to 0X2142, Enter.|Это регистр, НАСТРОЙКА РЕГИСТРАЦИИ, а затем я меняю его на 0X2142, Enter.
And I'm going to copy that.|И я собираюсь скопировать это.
And, I'm going to do my shortcut.|И я собираюсь сделать свой ярлык.
Do WR.|Сделайте WR.
And now I'm going to do a DO SH VER.|А теперь я сделаю ДЕЛАТЬ ВЕР.
And again, these are only things you are allowed to do when you are in the field.|И опять же, это только то, что вам разрешено делать, когда вы находитесь в поле.
Remember, ladies and gentlemen, when you take your test.|Помните, дамы и господа, когда будете сдавать тест.
This is the disclaimer,|Это отказ от ответственности,
when you take your test, you have to go back to privilege mode.|при прохождении теста вы должны вернуться в привилегированный режим.
You have to exit, exit, or just exit from where you're already at.|Вы должны выйти, выйти или просто выйти из того места, где вы уже находитесь.
Go back to privileged mode.|Вернитесь в привилегированный режим.
Do your any show commands, ping commands,|Выполняйте любые команды шоу, команды ping,
everything like that.|все так.
Copy run start, all that stuff is from Pearly's book.|Скопируйте запуск, все это из книги Перли.
All right, so I'll do a SO SH VER and look what it says.|Хорошо, я сделаю ТАК ШВЕР и посмотрю, что там написано.
I did change the registry setting, but it says, it will be 2142 at next reload.|Я изменил настройки реестра, но там написано, что при следующей перезагрузке будет 2142.
So once the router reloads, then it will be 2142.|Итак, как только маршрутизатор перезагрузится, он будет 2142.
Okay, so I'm gonna reload the router.|Хорошо, я перезагружу роутер.
I'm going to reload.|Я собираюсь перезагрузить.
[BLANK_AUDIO]|[BLANK_AUDIO]
And, of course, lightning speed, right?|И, конечно, молниеносно, правда?
The router is decompressing the iOS into RAM.|Маршрутизатор распаковывает iOS в ОЗУ.
And now we're in setup mode.|И теперь мы в режиме настройки.
This is, we configured this router.|Это мы настроили этот роутер.
So, we're gonna say no.|Итак, мы скажем нет.
We don't wanna go through configuration dialog.|Мы не хотим проходить диалог конфигурации.
I don't have a host name.|У меня нет имени хоста.
Name, no passwords whatsoever, oh my God let's take a look at the SH RUN.|Имя, никаких паролей, боже мой, давай взглянем на SH RUN.
Now the start,|Теперь начало,
because there is something in the start,|потому что в начале что-то есть,
there's nothing in the run though.|хотя в бегах ничего нет.
For whatever reason, it's keeps the domain name, I don't know why,|По какой-то причине он сохраняет доменное имя, я не знаю почему,
packet tracer thing, all right, but there's no configurations in here.|трассировщик пакетов, хорошо, но здесь нет никаких конфигураций.
All right so that's a problem.|Хорошо, это проблема.
Why is that a problem?|Почему это проблема?
Cuz if you were to look at, look, my interfaces are down.|Потому что, если вы посмотрите, посмотрите, мои интерфейсы не работают.
My LAN is down.|Моя локальная сеть не работает.
Nobody can get to anywhere.|Никто никуда не денется.
That's a bad thing.|Это плохо.
So you wanna make sure, you wanna make sure that you're very careful, and if you do change that registry to put it back.|Итак, вы хотите убедиться, вы хотите убедиться, что вы очень осторожны, и если вы действительно измените этот реестр, чтобы вернуть его.
So what we're gonna do is in this case you know we need to get up and running what we're going to do is the opposite of copy copy run start we're gonna do a|Итак, что мы собираемся сделать, в этом случае вы знаете, что нам нужно встать и запустить то, что мы собираемся сделать, это противоположно запуску копирования, запуску, мы собираемся сделать
COPY START RUN.|КОПИРОВАТЬ ЗАПУСК.
Do you wanna copy to the run?|Вы хотите скопировать в ход?
Yes I do.|Да.
Now look all of a sudden I got a host name, and then I do a SH RUN.|А теперь посмотрите, как вдруг я получил имя хоста, а затем я выполняю SH RUN.
There's all my configs right there.|Там все мои конфиги.
Lovely.|Прекрасно.
Now I'm gonna say, okay, awesome.|Теперь я скажу, хорошо, круто.
And you're just gonna I'm gonna go back and change the register setting back to 2102.|И ты просто собираешься вернуться и изменить настройку регистра обратно на 2102.
So I'm gonna go GLOBAL.|Так что я собираюсь стать ГЛОБАЛЬНЫМ.
And then CONFIG-REG, for short,|А потом CONFIG-REG, для краткости,
0X2142, I mean 02.|0X2142, то есть 02.
And then I'm gonna do DO WR.|А потом я сделаю DO WR.
And then to see it, show version, or SHOW VER, and then it will be 2102 on next reload.|А затем, чтобы увидеть это, показать версию или ПОКАЗАТЬ ВЕР, и тогда при следующей перезагрузке будет 2102.
I can leave it like this.|Я могу оставить это так.
I don't need to reload.|Мне не нужно перезагружать.
It can stay like this all day every day 365 days a year,|Он может оставаться таким весь день каждый день 365 дней в году,
as long as this router doesn't reboot.|пока этот маршрутизатор не перезагружается.
Even if it does reboot it's gonna come back up and it's gonna actually look at the NVRAM because we set it to that.|Даже если он перезагрузится, он вернется и действительно будет смотреть на NVRAM, потому что мы настроили его на это.
Well, let's prove that.|Что ж, давайте это докажем.
Let's reload the router.|Перезагрузим роутер.
And now when it comes back up it should ask me to log in, because it's looking at the configurations, and I do have a user name and password in there.|И теперь, когда он вернется, он должен попросить меня войти в систему, потому что он просматривает конфигурации, и у меня там есть имя пользователя и пароль.
So it should ask me to log in.|Поэтому он должен попросить меня войти в систему.
And sure enough,|И конечно же,
LDIAZ, and then Cisco, okay?|ЛДИАЗ, а потом Cisco, ладно?
So, that's why or that's how, I'm sorry,|Так вот почему или вот как, прости,
that's how you play around with the registry while you're in the router.|вот как вы играете с реестром в роутере.
Just remember, be very, very careful.|Просто помните, будьте очень и очень осторожны.
All right, and when your doing that then for whatever reason you need to set it to something other then the default once your done doing what you're doing,|Хорошо, и когда вы это делаете, тогда по какой-либо причине вам нужно установить его на что-то другое, кроме значения по умолчанию, когда вы закончите делать то, что делаете,
put it back unless those exceptions that I told you to that you're deliberately making it look somewhere else, if not you|верните его, если только те исключения, о которых я вам сказал, что вы намеренно заставляете его искать в другом месте, если не вы
wanna set it back to the default in case your router reboots because of a power outage or what have you.|хочу вернуть значение по умолчанию на случай, если ваш маршрутизатор перезагрузится из-за отключения электроэнергии или чего-то еще.
Okay?|Ладно?
That's it for this lesson.|На этом урок закончен.
This is the registry.|Это реестр.
The next lesson we'll see how to mess around with ROMmon.|В следующем уроке мы увидим, как возиться с ROMmon.
[BLANK_AUDIO]|[BLANK_AUDIO]