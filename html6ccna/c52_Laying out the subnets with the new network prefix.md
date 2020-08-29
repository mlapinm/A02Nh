D:\mailCloud\prjother\tmp\1\c52_Laying out the subnets with the new network prefix.md  


__|__
--|--
All right, this is the last lecture for this particular section.|Хорошо, это последняя лекция для данного раздела.
We've learned, what have we learned?|Мы узнали, что мы узнали?
We've learned to get that subnet section,|Мы научились получать этот раздел подсети,
break it down into the binary bits for each position,|разбить его на двоичные биты для каждой позиции,
right, first, second, third and fourth.|право, первое, второе, третье и четвертое.
Draw our line with the given network prefix that we had to make our starting point.|Нарисуйте нашу линию с заданным префиксом сети, который мы должны были сделать нашей отправной точкой.
We counted for subnets from left to right,|Считали подсети слева направо,
like we normally would,|как обычно,
found that increment number, right.|нашел это число приращения, верно.
And we saw that we were in position number two that we were incrementing in, okay, by one.|И мы увидели, что мы находимся в позиции номер два, которую мы увеличивали, хорошо, на единицу.
So, how do we lay this out?|Итак, как нам это изложить?
So we come down here.|Итак, мы спустились сюда.
[BLANK_AUDIO]|[BLANK_AUDIO]
Okay, right there, and we see that we have now,|Хорошо, прямо здесь, и мы видим, что теперь у нас есть
we were given this address to start with.|нам изначально дали этот адрес.
So that's the one you need to start with.|Так что это то, с чего вам нужно начать.
But, with a new mask, how do we get 56?|Но как нам получить 56 с новой маской?
Well, we had 50 what is it, 52?|Ну у нас было 50 что это, 52?
Right, we had, had 16, 32, 48, 49, 50, 51,|Да, у нас было, было 16, 32, 48, 49, 50, 51,
52.|52.
Then we added four more bits, 53, 54, 55,|Затем мы добавили еще четыре бита: 53, 54, 55,
56.|56.
That's how we came up with the new network prefix of 56.|Так мы придумали новый сетевой префикс 56.
And then we were incrementing or we are incrementing on the second position.|А затем мы увеличивали или увеличивали на второй позиции.
And we're incrementing by what?|И на что мы увеличиваем?
We're incrementing by one.|Мы увеличиваем на единицу.
So therefore, 1,000, our starting point,|Итак, 1000, наша отправная точка,
1100, 1200, 1300, 1400, 1500,|1100, 1200, 1300, 1400, 1500,
1600, 1700, 1800, 1900.|1600, 1700, 1800, 1900.
Well, what happens when you go beyond the 9?|А что будет, когда вы выйдете за пределы 9?
What happens when you go beyond the 9?|Что произойдет, если вы выйдете за пределы 9?
And Excel is going crazy, okay.|И Excel сходит с ума, хорошо.
Come over here.|Иди сюда.
Did I go beyond that?|Я пошел дальше этого?
No, I didn't.|Нет, не видел.
Okay, but if you would because we needed how many subs?|Хорошо, но если бы вы, потому что нам нужно было сколько подводных лодок?
Oh, we needed 10 so that's why we stopped there, one, two, three.|О, нам нужно было 10, поэтому мы остановились на одном, два, три.
Well, let's, let's, let's do this, one,|Ну, давай, давай, давай сделаем это, один,
two, three, four, five, six, seven, eight,|два, три, четыре, пять, шесть, семь, восемь,
nine, ten.|девять десять.
So, we can only stop right there.|Итак, мы можем только остановиться здесь.
This is not like IPv4.|Это не похоже на IPv4.
We just can't keep going just like that.|Мы просто не можем так продолжать.
It well, we have 16 networks that we can use, all right.|Хорошо, у нас есть 16 сетей, которые мы можем использовать.
So if we stopped at 1900, the next one would be what?|Итак, если бы мы остановились на 1900, что было бы следующим?
A.|А.
And then the next one would be B.|А следующим будет Б.
And then the next one would be C.|А следующим будет C.
And then D, and then E.|А потом D, а потом E.
That's 15 already, all right?|Уже 15, понятно?
Because you've got 10 right there, eh, or not E, yeah, E.|Потому что у вас тут 10, а, или нет E, ага, E.
And then the last one, F, which would be 16.|И затем последний, F, который будет 16.
There will be all your 16 networks,|Будет все ваши 16 сетей,
incrementing by one, by one of each.|увеличиваясь на единицу, на единицу каждого.
Where you've got zero, one, two, three,|Где у тебя ноль, один, два, три,
four, five, six, seven, eight, nine, A, B,|четыре, пять, шесть, семь, восемь, девять, А, Б,
C, D, E, F.|C, D, E, F.
So you got, that's the only thing that makes it a little bit complicated,|Итак, у вас есть, это единственное, что немного усложняет,
all right?|отлично?
We're not going to get, as you see in what it says right there, 1st level subnetting.|Мы не собираемся получить, как вы видите в том, что здесь говорится, подсети 1-го уровня.
We're not gonna get into nothing deeper than that, because right now,|Мы не собираемся вдаваться в подробности, потому что прямо сейчас
nobody is subnetting in IPv6, all right?|никто не разделяет подсети в IPv6, понятно?
Nobody, because it's not needed for your CCNA certification.|Никто, потому что он не нужен для вашей сертификации CCNA.
And a lot of people are still fighting that resistance to change syndrome to get into IPv6.|И многие люди все еще борются с синдромом сопротивления изменениям, чтобы перейти на IPv6.
So, subnetting in IPv6 is something that nobody has embraced yet.|Итак, подсети в IPv6 - это то, что еще никто не принял.
So I am introducing it to you, okay?|Итак, я представляю его вам, хорошо?
That it's not that difficult taking the IPv4 version of it, and bringing it, and kinda tweaking it to the IPv6 address as|Что это не так уж и сложно взять версию IPv4 и принести ее, и вроде как настроить ее на адрес IPv6 как
well,|хорошо,
okay, for 1st level subnetting.|хорошо, для подсетей 1-го уровня.
So this is it, this is the diagram for IPv6 subnetting.|Вот и все, это схема подсети IPv6.
I don't expect you to learn it right off the bat.|Я не жду, что вы научитесь этому сразу.
I, you probably watch this video over and over and over again.|Я, вы, наверное, смотрите это видео снова и снова.
That's fine.|Это хорошо.
That's not our problem.|Это не наша проблема.
Remember, it's not going to be on your test.|Помните, это не будет на вашем тесте.
It's not, you won't be asked to subnet on your test.|Это не так, вам не будет предложено подключиться к подсети в вашем тесте.
But I just want you to start looking at it and start learning it.|Но я просто хочу, чтобы вы начали смотреть на это и начали изучать это.
So when the time comes, you have a heads up on everybody else.|Так что, когда придет время, вы будете знать всех остальных.
All right, ladies and gentleman, that's the end of this lecture.|Хорошо, дамы и господа, это конец лекции.
That's the end of this section.|Это конец этого раздела.
I will be seeing you in the next section.|Увидимся в следующем разделе.
[BLANK_AUDIO]|[BLANK_AUDIO]