D:\mailCloud\prjother\tmp\1\c21_The tables we use when converting.md  


__|__
--|--
[BLANK_AUDIO]|[BLANK_AUDIO]
All right, welcome back everyone.|Хорошо, с возвращением всех.
This next lesson is on hexadecimal to decimal to binary vice versa conversions.|Следующий урок посвящен преобразованию шестнадцатеричного числа в десятичное и наоборот.
Not that you're gonna see any conversions on the test, cuz you won't.|Не то, чтобы вы увидели какие-либо конверсии на тесте, потому что вы этого не сделаете.
It's been a very, very,|Это было очень, очень,
very long time where Cisco actually put some conversions on the exam.|очень долгое время, когда Cisco фактически ставила на экзамен некоторые преобразования.
Now you do need to be familiar, especially now-a-days, with hexadecimal numbers.|Теперь вам действительно нужно знать, особенно в наши дни, шестнадцатеричные числа.
Because since IB, IPB6 is on hex and when we start doing the sub-netting in IPB6.|Потому что, начиная с IB, IPB6 находится в шестнадцатеричном формате, а когда мы начинаем делать подсети в IPB6.
We kinda you know, need to know that each hexa, hexadecimal number is four bits long and that's how they create each section that's 16,|Мы вроде как знаете, нужно знать, что каждое шестнадцатеричное, шестнадцатеричное число имеет длину четыре бита, и именно так они создают каждый раздел, равный 16,
cuz you got four hexadecimal numbers and so forth.|Потому что у вас есть четыре шестнадцатеричных числа и так далее.
So you need to be comfortable.|Так что вам нужно чувствовать себя комфортно.
And also, this is gonna show you especially the bit to decimal table because these are the tables that we use when we're converting from, you know,|Кроме того, это особенно покажет вам бит в десятичную таблицу, потому что это таблицы, которые мы используем при преобразовании, вы знаете,
whether you're converting binary number or decimal number or hexadecimal number, so I'm just gonna show you the tables that we use.|преобразовываете ли вы двоичное, десятичное или шестнадцатеричное число, поэтому я просто покажу вам таблицы, которые мы используем.
One of the things that you really need to pay attention, not pay attention but memorize, memorize.|Одна из вещей, на которую действительно нужно обращать внимание, не обращать внимание, а запоминать, запоминать.
Is this table right here.|Эта таблица прямо здесь.
I tell everyone this bit to decimal table,|Я говорю всем этот бит в десятичной таблице,
this is a life saver, okay?|это спасатель, хорошо?
This is a tremendous life saver because this will let you know,|Это отличное средство для спасения жизни, потому что это даст вам знать,
when somebody gives you a CIDR notation,|когда кто-то дает вам нотацию CIDR,
CIDR 24, or CIDR 20, whatever it is,|CIDR 24 или CIDR 20, что бы это ни было,
this will let you know how many bits in,|это позволит вам узнать, сколько бит в,
if it's CIDR 20 you have what?|если это CIDR 20 у вас что?
You have four bits, I mean eight bits and eight bits is sixteen, plus four more.|У вас четыре бита, я имею в виду восемь бит, восемь бит - это шестнадцать плюс еще четыре.
So 4 bits is what, 4 bits is 240.|Итак, 4 бита - это что, 4 бита - это 240.
So this table is definitely going to help you.|Так что эта таблица определенно вам поможет.
Not only for the conversions that we're going to do here but also for the fact that when you're turning from CIDR notation to dotted decimal, or|Не только для преобразований, которые мы собираемся сделать здесь, но и для того факта, что когда вы переходите от нотации CIDR к десятичной системе с точками, или
vice versa, this table comes in handy.|наоборот, эта таблица пригодится.
This bit values, these bit values.|Это битовые значения, эти битовые значения.
In an IP address, an IP version 4 address,|В IP-адресе - IP-адрес версии 4,
you know there's four octets.|вы знаете, что там четыре октета.
Each octet is made up of eight bits.|Каждый октет состоит из восьми битов.
Eight bits creates a byte.|Восемь бит создают байт.
So when you,|Итак, когда вы,
these bit values exist on the very top,|эти битовые значения существуют на самом верху,
that's what I write, on the very top.|вот что я пишу, на самом верху.
The bit values of each one of the zeros if you will or the values or the spaces whatever you want to call it, each one of|Битовые значения каждого из нулей, если хотите, или значения или пробелы, как хотите, каждый из
those has its particular bit value.|у них есть свое конкретное битовое значение.
And they're the same throughout each octet so of course here we're not going to be converting IP addresses or nothing like|И они одинаковы для каждого октета, поэтому, конечно, здесь мы не собираемся преобразовывать IP-адреса или что-то подобное.
that but so you know.|это, но чтобы вы знали.
Because if you were to add all of these bit values together,|Потому что, если бы вы сложили все эти битовые значения вместе,
it will come out to 255, so that let's you know right there that the maximum value of any octet is 255.|он будет равен 255, чтобы вы сразу знали, что максимальное значение любого октета равно 255.
So, again, we use this to convert.|Итак, мы снова используем это для преобразования.
And then, of course, we have our hex table.|И, конечно же, у нас есть шестнадцатеричная таблица.
Let me scroll down here so you can see the whole thing.|Позвольте мне прокрутить здесь вниз, чтобы вы могли увидеть все.
All right.|Отлично.
Our hex table is 16 numbers.|Наша шестнадцатеричная таблица состоит из 16 чисел.
Because we start from zero and we go all the way down to F.|Потому что мы начинаем с нуля и спускаемся до F.
But, starting at A.|Но, начиная с А.
A equals 10, B 11, C 12, D 13, E 14 and F 15.|A равно 10, B 11, C 12, D 13, E 14 и F 15.
So, that is important to know, all right?|Итак, это важно знать, хорошо?
But this, this is, this is it.|Но это, это, это оно.
This is all you need right here in order to convert, or do whatever it is that you need to do,|Это все, что вам нужно прямо здесь, чтобы конвертировать или делать то, что вам нужно,
these little tables right here.|эти столики прямо здесь.
And that bit to decimal table, like I said earlier, it is key,|И этот бит в десятичной таблице, как я сказал ранее, это ключ,
you must memorize that little table.|вы должны запомнить этот столик.
This little thing right here.|Вот эта мелочь.
Its nothing, 1 consec, you know, 1 bit on is 128,|Ничего особенного, 1 раз, знаете ли, 1 бит равен 128,
2 consecutive bits on, is 192, 3, 224, and so forth.|Включены 2 последовательных бита - 192, 3, 224 и т. Д.
If you memorize this, you're not going to have issues.|Если вы запомните это, у вас не будет проблем.
You're gonna.|Ты собираешься.
When we get into IP addressing,|Когда мы переходим к IP-адресации,
you're going to find that magic line.|вы найдете эту волшебную линию.
But, we are going to use it for conversions.|Но мы собираемся использовать его для конверсий.
Okay?|Ладно?
So anyway, these are the tables that we use when we convert from hex to decimal, from a decimal to a hex, from a binary,|Так или иначе, это таблицы, которые мы используем при преобразовании из шестнадцатеричного в десятичное, из десятичного в шестнадцатеричное, из двоичного,
and always remember, binary, binary is always your middle ground.|и всегда помните, двоичное, двоичное - это всегда ваша золотая середина.
Always your middle ground.|Всегда твоя золотая середина.
Okay well,|Хорошо хорошо
these are the tables, next video we'll start the conversions, I'll see you then.|это таблицы, в следующем видео мы начнем преобразования, увидимся тогда.