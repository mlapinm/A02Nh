_|_|_|_|_|_
--|--|--|--|--|--
mean|означает|essence|сущность|kindly|любезно
moreover|еще|ultimate|окончательный|offer|предложение
although|хотя|assuming|при условии|nessessary|необходимые
acctually|фактически|keep|продолжать|treat|расценивать
otherwise|хотя|average|средний|somewere|где-то
somewere|где-то|similarly|аналогично|bring|приводить
feed|скормить|noticed|отметить||
|||||
|||||


_|_|_|_|_|_
--|--|--|--|--|--
huge|огромный|amnesty|амнистия|throughout|на протяжении
dataset|набор данных|exploration|исследования|accuracy|точность
overfitting|переобучение|somehow|как-то|ahead|впереди
met|встречал|covered|покрывает|decision|решение
embedded|встроенные|wasting|потеря|estimate|оценивает
takes|принимает|evaluate|оценивается|performance|производительность
assuming|предполагаю|Cleanup|уборка|Eager|стремительное
No more|нет больше|consistent|последовательный|gonna|собираюсь
recently|недавно|advantage|преимущества|mean|означает
leave|оставить|redundant|избыточный|particular|конкретная
|||||
|||||
|||||


_|_|_|_|_|_
--|--|--|--|--|--
|||||
origin|происхождения|rather|скорее|frequently|часто
treat|трактуются|amnesty|амнистия|amidst|посреди
fashion|мода|immunised|иммунизированной||
|||||
|||||
|||||


_|_|_|_|_|_
--|--|--|--|--|--
So far|пока|breadth|ширина|away|на расстоянии
reached|достигнуты|aware|знать|Similar|Аналогичный
Whereas|когда|Notice how|обратите внимани|unlike|в отличие
Instead|Вместо|approach|подходить|amazing|удивительный
probably|наверное|mastering|освоение|benefit|выгода
Interacting|взаимодейсвие|secure|безопасность|appreciated|оценили
involved|участвуют|Parsing|разбор|predictions|прогнозы
imply|обычно|scopes|цели|responsibilities|обязанности
|||||
|||||
|||||
|||||
|||||
|||||
|||||



_|_|_|_|_|_
--|--|--|--|--|--
DataFrame|таблица|ransom|выкупная|Eventually|в конце концов
Snooping|искать|suspects|подозреваемые|narrow|сузить
accepts|получает|witness|свидетели||
|||||
|||||
|||||
|||||
|||||


_|_|_|_|_|_
--|--|--|--|--|--
mood|настроение|swings|качели|Hazards|опасности
habit|привычка|sneaky|подлых|approach|подход
issues|проблемы|tense|натянуто|perform|выполнения
exact|точное|indices|индексы|declarative|описательное
offers|предлагает|handle|обрабатывает|write out|описать
instead|вместо|mentioned|упомянутого|avoid|избежать
Consider|рассмотрим|browsing|просматриваем|to track|отследить
made up|сделан|behaviour|поведение|side|побочный
consequences|последствия|confidence|уверенность|traps|ловушки
distinct|особый|exciting|захватывающе|rest|оставшиеся
solve|решили|necessary|необходимо|accomplish|выполнить
vice versa|наоборот|omit|пропустить|arbitrary|произвольный
so far|уже|bolster|укрепить|hesitate|стесняться
approach|подход|navy|флот|Survey|обследование
Definitely|определенно|ensures|гарантирует|involve|включает
improving|улучшать||||
|||||
|||||
|||||


_|_|_|_|_|_
--|--|--|--|--|--
frequent|частый|malicious|вредный|vulnerable|уязвимый
stealing|кражи|sensitive|конфиденциальный|dangerous|опасными
mitigating|смягчать|adopting|применение|heuristic|поисковый
wings|крылья|follower|последователь||
|||||
|||||




_|_|_|_|_|_
--|--|--|--|--|--
|grateful caterwauling tuna|благодарный гусеничный тунец|||
|jelly future ferret|желе будущее хорька|||
|fabulous-stirring-passbook|сказочная-перемешивающая-сберкнижка|||
|creative-everlasting-side|творческая вечная сторона|||
|lofty-clammy-drink|высокий липкий напиток|||
|||||


[Introduction-to-the-JSON-APIs-and-AJAX-Challenges](./d10mongodb.ipynb#1.2.1.-Introduction-to-the-JSON-APIs-and-AJAX-Challenges)  
[Technical-Documentation-Page](./d60siteprj.ipynb#4.-Build-a-Technical-Documentation-Page)  
[]()  
[]()  
[]()  
[]()  


1. Build a Tribute Page






```
f  = () => {
var s = "";
var link = document.location["href"];
var title = document.getElementsByTagName("title")[0].text;
s = `[${title}](${link})   `;
console.log(s);
}
f()
```



 #### to json array


```python
import re
s = '''


RecipePane
#delete-
#edit-
.recipe-body
  ul.ingredient list
    ingredients
  ol.directions list
    directions
--	
Dialog
{this.props.dialogType}
Add a Recipe
Edit Recipe
Recipe
textarea#{this.props.nameID}
Ingredients
textarea#{this.props.ingredientsID}
Directions
textarea#{this.props.directionsID}
button.corner-close
button#{this.props.submitID}
button#{this.props.closeID}
--
IndexView
#index-view
.index-view-item

'''
l = s.split('\n')
l2 = []
for i in l:
    if i.strip() != "":
        l2.append(i)
print(l2)
```

    ['RecipePane', '#delete-', '#edit-', '.recipe-body', '  ul.ingredient list', '    ingredients', '  ol.directions list', '    directions', '--\t', 'Dialog', '{this.props.dialogType}', 'Add a Recipe', 'Edit Recipe', 'Recipe', 'textarea#{this.props.nameID}', 'Ingredients', 'textarea#{this.props.ingredientsID}', 'Directions', 'textarea#{this.props.directionsID}', 'button.corner-close', 'button#{this.props.submitID}', 'button#{this.props.closeID}', '--', 'IndexView', '#index-view', '.index-view-item']
    

### subtitles


```python
import re
s1 = '00:03'
i = re.sub(r'\d\d:\d\d', "", s1) 
print(len(i),s1)
```

    0 00:03
    


```python
import re
s = '''
doesn't Eugene into global variables and
05:09
the tensorflow 2.0 has also removed this
05:12
essence the earlier in tensorflow
05:15
we had to use the system dot run and now
05:19
the tensorflow 2.0 is kindly kind of
05:22
bringing it like a function call and
05:25
moreover now the tensor flew to point X
05:29
R to find zero brings the clearance at
05:33
the core of the tensor flow which
05:35
ultimately increases the you know
05:39
improves the accuracy that that actually
05:43
can increase the accuracy but that is
05:45
not 100% sure that that increases the
05:47
accuracy but moreover it reduced the
05:50
training and the testing time since the
05:52
Kira's has been integrated with the core
05:54
of the tensor flow and in that case the
05:59
its execution will be the faster
06:01
actually and it also takes a less space
06:04
and moreover it is the consistent and if
06:07
you want to know more about the tensor
06:09
flow 2.0 what I it is offering you can
06:13
go ahead and visit this link it has
06:15
Google IO link there and at the Google
06:18
i/o you can you know to see this the
06:22
complete the getting started with the
06:24
tensor flow 2.0 at the Google i/o so the
06:27
air google has released this tensor flow
06:29
2.0 and they have covered almost
06:31
everything what is the new in the tensor
06:34
flow 2.0
06:38
there are so many things to the new into
06:40
the tensorflow 2.0 although this is the
06:43
new video series and we will be learning
06:45
a lot about the tensorflow
06:46
2.0 throughout this video series now the
06:50
let's go ahead the very quickly and I'm
06:52
assuming that you have already installed
06:54
the an akuna at the necessary library
06:56
only you need to install the tensorflow
06:59
and if you do remember the previously
07:01
you need to install the chaos and the
07:03
tensorflow separately but here you only
07:06
need to install that cancer flow you
07:08
actually don't need to install the
07:10
Kiera's so you can call the pip install
07:14
tensorflow equal to equal to the 2.0 RC
07:17
and you can go ahead to this github link
07:21
where you can get the tensorflow the
07:24
released okay so here we have a
07:26
tensorflow 2.0 and you can visit that I
07:30
think with this yes so here we have a
07:35
you know the latest tensorflow the 2.0
07:39
this this one is the not the latest one
07:41
although with the website if you go and
07:44
visit on the website there you will get
07:47
a latest one the tensorflow 2.0 the
07:50
release candidate is available and you
07:52
just go ahead there you will get the
07:54
link here to install this so you can
07:57
keep monitoring this mission this link
08:00
to get the updated version by the time
08:04
I'm making this video this is the latest
08:06
version now let's go ahead and open
08:09
anaconda into administrator mode
08:11
remember you need to open it into the
08:13
administrator mode otherwise it would
08:16
not be able to install the tensorflow
08:18
2.0 in your computer because of the
08:21
right permission now let's go ahead and
08:25
copy this which I can just copy it and
08:31
in the anaconda right the pressing the
08:35
right click it will paste here the PIP
08:37
installed tensorflow equal to equal to
08:39
two point zero point zero RC 0 that if
08:43
the release candidate 0 let's go ahead
08:45
and hit the enter although I have
08:47
already installed the tensorflow 2.0
08:49
that's why it is saying that the
08:51
all the requirement has been already
08:53
satisfied but if you do not have the
08:56
tensorflow 2.0 installed in your
08:58
computer you can install and the
09:00
moreover if you get the any error then
09:02
you can first uninstall the previous
09:05
tensorflow for that you can right there
09:08
pip uninstalled tensorflow so it will
09:12
uninstall your previous versions and
09:14
then you can install a new version of a
09:16
tensorflow
09:17
okay perfect now let's go ahead and see
09:22
if you have a GPU in your computer then
09:25
you can also install a GPU version of a
09:28
tensorflow
09:29
right so these are the two ways where
09:31
you can install a tensorflow in your
09:33
computer now you can pause the video and
09:36
pause this video and that you can
09:39
continue this video after installing the
09:41
tensorflow
09:42
2.0 alright now let's go ahead import
09:46
the fashion mms data set so in this
09:49
lesson we will be working on the finest
09:51
fashion m-miss data set the fashion m
09:55
needs to data set the link is available
09:56
here and this working we working file is
10:00
available in the video description from
10:02
where you can download and if you visit
10:04
this fashion m niche then you see here
10:06
on the github the link is available and
10:10
on the github it says that this is
10:14
Jolanda article images it has 60
10:16
thousands examples and every sample have
10:20
20 28 cross 28 grayscale images and so
10:26
these are the images and it has a 10
10:28
actually it has two total the ten
10:32
classes and that's mean there are 10
10:35
type of the the fashion images are of
10:38
level in this fashion amidst dataset
10:41
okay so these are the images which are
10:44
available and and and and this sixty
10:49
thousand images which we will be using
10:51
to train and ten thousand images to
10:56
we'll be using to evaluate and it has
10:59
total the ten categories of these images
11:02
ok now let's go ahead
11:05
and first import our learner now first
11:12
let's go ahead and import the tensorflow
11:13
and then I'll show you how you can
11:16
download this the amnesty data set
11:20
directly into your Jupiters notebook
11:22
instead of downloading it from a geek
11:24
health ok / pets to import the
11:27
tensorflow you need to write their the
11:29
import and then the tensorflow
11:34
there we have a tensor flow as usual
11:37
tensor flow as DF and then we need to
11:42
improve the care as from the tensor flow
11:44
so here we have a from tensor flow
11:49
import the Kira's okay so now we have
11:55
got sorry we have got the tensor flow
12:00
and in the chaos sorry yeah now we have
12:08
imported the Kira's from a tensor flow
12:10
now let's go ahead and import other
12:12
necessary libraries like numpy pandas
12:15
and the matplotlib so those things we
12:17
can say that a helper liability but
12:19
before that let's go ahead and check a
12:21
tensor flow version which you can just
12:23
check from a print T F dot version so
12:30
this says that we have Overson 2.0
12:32
installed in my computer now let's go
12:35
ahead and import helper libraries like
12:37
an umpire Pentagon the matplotlib so in
12:40
the previous videos we have been
12:41
importing these libraries very
12:44
frequently numpy as in P and import
12:51
pandas HPD and then import might float
12:57
lib dot type lot as PLT so here we have
13:03
matplotlib i the pandas and the numpy
13:06
imported in our computer so these things
13:08
we can treat as a helper libraries now
13:11
let's go ahead and load the amnesty
13:13
person dataset so for that i can write
13:16
here the amidst is equal to
13:19
the Kyra's dot datasets and then I can
13:24
write there the fashion I'm honest so
13:26
with this we will get a pass anemones
13:28
dataset although I have already
13:30
downloaded it my computer otherwise it
13:32
might take a little time in your
13:34
computer to download this data set from
13:36
a internet that might take a few seconds
13:39
if you have a fast internet now let's go
13:41
ahead and check the type of the
13:43
immunised this says that with this
13:47
immunised actually it has downloaded the
13:49
data sets in a tensor flow module
13:52
wrapper now what we need to do now we
13:54
need to actually load the data now we
13:57
need to load this data into into a real
14:01
real variables in this jupiter notebook
14:05
and to do that it actually returns a
14:07
tuple ok the two tuples wonderful for
14:09
the training and another tougher for the
14:11
testing so for this what we can do here
14:14
the m in each dot a load data set as
14:17
usual we have been doing into a scalar
14:19
now in this topple we need to first down
14:22
get the data into our our the training
14:25
dataset that is the extreme and then
14:28
finally Whiterun and the next couple in
14:32
the next it returns the testing data
14:35
sets it has X underscore test and then Y
14:38
underscore test so it has a 60,000 rows
14:42
for a training which we can verify that
14:47
with X train dot safe now there you see
14:50
here there are 60,000 images are
14:55
available there and each images have 28
14:57
cross 28 some since there are 60,000
15:02
images that's mean it should have a
15:04
60,000 y train as well so let's go ahead
15:07
and check the safe of Y trend which says
15:09
that it has a 60,000 okay now let's go
15:13
ahead and print the X train and see what
15:16
happens
15:16
once we print the extreme we see the
15:19
values the most of the values we are
15:21
printing here 0 that is because you note
15:24
at the ages since this is the grayscale
15:27
so at the edges the most of the images
15:30
values are 0
15:32
otherwise the maximum value inside this
15:34
the area which we can find that within P
15:38
dot max okay so that's it the 255 so the
15:44
minimum we have already seen in there
15:46
and that that is the zero but here are
15:49
the max is 255 and if we see the average
15:53
that's mean the N P dot mean the X train
15:59
so it says that something so moreover
16:01
now we can we can say that the values is
16:05
somewhere in between 0 and the 255 okay
16:08
inside this data set which we later we
16:11
need to bring down in between 0 and 1 to
16:14
train with the tensor flow tensor flow
16:17
model okay our deep learning model and
16:20
these 60,000 images are classified into
16:23
ten labels and those labels are encoded
16:28
into a numerical values and those
16:30
numerical values we can see with the Y
16:32
under escort rain and those numerical
16:35
values are in between 0 & 1 sorry 0 1 9
16:39
okay so it starts from the 0 until the 9
16:42
so those are the 10 categories there now
16:45
let's go ahead and write those category
16:47
names although you can get on the pass
16:49
and M minister's category names there
16:51
you should get those category names
16:54
somewhere here
16:55
yes which category names are here okay
16:58
so these are the desert trouser pullover
17:01
dress code sandal cert sneaker back at
17:05
the ankle board now let's go ahead and
17:08
and write that the class names here so
17:13
that we can write in new variable the
17:15
class name and inside those class name
17:18
we need to write it
17:20
okay the desert sign the topic cetera
17:25
like here we have let us go at the top
17:28
and the Ender when we have here at
17:31
rapture and then here we have the
17:36
pullover and then here we have dress
17:42
then we have a court and then finally we
17:46
have the sandal and then we have a cert
17:53
and then we have a sneaker and then
17:59
after that we have back sorry it's bad
18:03
actually not a bad and then we have
18:08
ankle boot so these are dipped in
18:12
classes right now let's go ahead and do
18:15
some the the data exploration so with
18:25
this data exploration we can actually
18:27
understand our data in in more explode
18:32
way okay so since we already have seen
18:37
its you know the same etc so here if we
18:40
see the X underscore the train dot say
18:45
we have 60,000 images but if we see here
18:50
X underscore test dot safe there we see
18:54
we have just 10,000 images
18:55
so this 60,000 images is available for a
18:59
training and these 10,000 images
19:00
available for testing purpose so that we
19:04
can test our model and we can see how
19:07
accurate our model is performing now let
19:10
us go ahead and visualize the visualize
19:14
the data some images so we can visualize
19:18
that with the PLT so here we have a PLT
19:22
door failure and then we have a PLT dot
19:27
image so that's the I am so and inside
19:32
that we are gonna the see first image
19:36
okay that is the extreme zero and then
19:40
I'm gonna just see it and now you will
19:43
see here it has this image okay so this
19:47
is actually the boot okay and how would
19:50
you know this is boot and if we if we
19:55
print here
19:56
the X screen actually there you see its
19:59
nine number and at the nine number you
20:02
see here we have ankle boot okay so this
20:05
is the word and if we see here one
20:08
number and now you see had the one
20:10
number it's a zero and at the zero it is
20:13
at top okay so this is how we can
20:16
visualize and if we print here a color
20:18
bar at the side okay so we can just
20:21
right there the color bar okay so with
20:25
the color bar now you see we have here a
20:28
color bar and this color bar now you see
20:30
the value is somewhere in between 0 and
20:33
the 255 since since neural network model
20:38
doesn't take the value greater than the
20:40
one that's mean we need to bring down
20:42
this the value in the maximum value the
20:44
255 in between somewhere 0 and 1 so what
20:49
we can do to bring it down we can just
20:51
divide the value with 255 I mean the
20:54
training and the testing data set with
20:56
the 255 so we can get here with X
21:00
underscore X underscore train dot sorry
21:08
X underscore train is equal to X
21:10
underscore sorry X underscore train and
21:15
then divide it by two fifty five point
21:19
zero okay perfect
21:21
all right so we have got the extreme in
21:26
between 0 and the 1 and similarly let's
21:28
go ahead and bring the X test in between
21:32
0 & 1 which we can get by dividing X
21:35
test by 255 point 0 so with this we have
21:43
got our X train and the X test in
21:46
between and in in between the 0 to 25
21:51
and what we can do we can just copy it
21:54
although you need to use your keyboard
21:56
control and the C and let's go ahead and
21:59
paste it here and see what happens now
22:02
now with this you can see here we have
22:06
brought it down in between 0 and
22:09
one okay so now this this value is now
22:13
ready to feed into into into a neural
22:17
network and one more thing you might
22:20
have noticed that this size it's a size
22:22
is 28 cross 28 that's mean there are 28
22:26
pixels and these are the pixels which
22:28
you can see okay so these are the pixels
22:31
a square dot there so these are the 28
22:34
dots here and the 28 is here okay
22:37
perfect now let's go ahead now build a
22:40
model a machine learning model with the
22:44
tensorflow
22:45
2.0 with the f 2.0 okay so so so in this
22:59
what we are going to do the basic
23:01
building blocks in any neural network is
23:04
a neural network layers okay so the
23:08
lyric extracts the representation from
23:10
the data and Anthony peered into into
23:15
into it's a hidden layer actually and
23:17
then finally it starts the training okay
23:21
so although this is the very critical
23:23
instance on the tensorflow 2.0 and I'm
23:27
assuming that you know a little about
23:28
the neural network so basically you
23:31
understand how the neural network works
23:33
so let's go ahead and import the
23:36
sequential and the dense model
23:38
sequential and the dense layers from
23:41
tensorflow Kira's to do that what we can
23:44
do the front ends are flow from the
23:47
tensorflow dot Kira's import sequential
23:52
and then from tensorflow dot dot Kira's
24:01
and then got layers import and from here
24:06
I'm gonna import the flatten layer that
24:10
will be used as a first layer and then
24:13
dense layer so we have got the two layer
24:15
and flatten and the dense and the
24:17
sequential model now let's go ahead and
24:20
create our model so here we are gonna
24:23
build
24:23
our model with the sequential model so
24:26
here we have a sequence here and then we
24:31
are gonna pass here ready okay so so the
24:35
area means the how many are the layers
24:37
we need inside our sequential model
24:40
there are many ways to build this but I
24:43
think this is the simplest way where we
24:45
can add all these together otherwise
24:48
there are a few other ways like like
24:50
just defining first sequential and then
24:53
going with the model dot add we can go
24:56
ahead with that one as well like model
24:58
dot add and then we can add there the
25:01
first flatten layer there and inside the
25:04
flatten layer the input shape okay which
25:08
we are gonna use here input shape will
25:11
be the 28 cross a 28 there okay so this
25:16
is an input safe for our the flatten
25:20
layer the flat hair doesn't do anything
25:23
actually it's just transformed the the
25:26
formats of this data which is 28 cross
25:29
to 28 so this this layer just
25:31
transformed this data into a one
25:34
dimensional so that we can fit into the
25:36
next layer okay so the next layer which
25:38
I'm gonna add here in the model dot and
25:41
that is a dense layer okay so this is
25:46
just a dense layer and inside the dense
25:48
layer if you press your sift and double
25:50
tab you will get here detail the
25:52
documentation on it
25:53
so in this I'm gonna pass the number of
25:56
units that's been the number of nodes
25:58
how many the neural neurons actually we
26:02
want and then we will pass here the
26:05
activation function which activation
26:07
function we are gonna use I'll be taking
26:10
a different lessons where I will be
26:11
covering all these things in a very
26:13
detail this is a very quick lesson so
26:15
I'm not going to cover all those things
26:16
here in the detail so activations we
26:19
will be using and other things we will
26:21
be just passing as usual okay so other
26:25
things will be like yeah
26:28
other things will be a default actually
26:30
so here in the dense layer I am gonna
26:33
pass here the 128 new rooms at the
26:36
firstly and the activation function
26:39
which we had talked there that I'm gonna
26:42
use here a raloo activation so this is
26:44
kind of the detective higher the
26:47
activation function there are so many
26:50
other kind of activation function like a
26:52
sigmoid an edge and you know the
26:55
Rayleigh key relive all those so here
26:58
for this listen I'm just gonna use your
27:00
a loop and then the model dot ad and
27:03
then again I'm gonna use the output
27:05
layer in an output layer if you add the
27:09
output layer then we need to define the
27:12
how many outputs are there that's when
27:14
the total number of classes we have a
27:16
ten classes that's when we have to
27:18
define here the ten and the activation
27:21
function here so at the output the real
27:25
you activation things an activation
27:26
cannot be used so there at the output
27:29
either we can use the sigmoid or softmax
27:32
so here we are gonna use a soft max okay
27:37
so here we have a model now let's go
27:39
ahead and print the summary on this
27:41
model and then you might understand how
27:45
it is building so the first model has
27:48
transformed a two-dimensional data into
27:50
a single dimensional and then here we
27:53
have 128-bit 128 neurons so 128 and then
27:58
multiplied by that 784 its complexity
28:02
reaches the number of parameters
28:04
actually then reaches to these digits
28:06
okay so that is the hundred thousands
28:09
and then finally at the output we are
28:12
bringing it down to the ten okay jester
28:15
ten so we have number of parameters at
28:17
the final output to calculate it the
28:19
twelve hundred and ninety okay so the
28:22
total parameter which we which this
28:24
model will be executing is more than
28:26
100,000 okay so this is how we build the
28:31
model now we need to compile our model
28:34
okay so for compliation of the model
28:37
there are a few things which are really
28:38
very important okay the first which need
28:42
we need to actually define sorry we need
28:46
to convert it into a markdown
28:49
yes so the first thing which we need to
28:51
define is a loss function okay
29:08
model compliation
29:11
so to compile the model we need to
29:13
define the loss function which loss
29:15
function we want here and then we want
29:18
optimizer okay and then after optimizer
29:22
we want here metrics so what are these
29:26
things a loss function it will measure
29:31
how accurate the model is during the
29:33
training and testing then okay actually
29:38
the loss function minimize minimize the
29:40
overall error during the training and
29:42
once the error is minimized during the
29:45
training then the testing error will be
29:48
also minimized but that is not always
29:52
the true because sometimes what happens
29:55
if your model overpaid then the oral law
29:58
skit minimized during the training but
30:01
during the testing it get increased
30:03
so here the generalization of model is
30:05
very important that's where optimizer
30:08
comes so this is how model is updated
30:10
based on the data that's been the
30:12
weights of our model applicants updated
30:15
with the you know as we define the
30:19
optimizer now let's go ahead and compile
30:21
this model first so we can compile this
30:24
with the model dot dot the compiled and
30:30
then here we have optimizer is equal to
30:33
Adam and then here we have a loss
30:37
function there a loss is equal to a
30:42
spazz categorical okay so there we have
30:46
a sparse and categorical cross entropy
30:57
okay
30:59
and then finally here we have a matrix
31:02
and inside this matrix we have accuracy
31:10
okay perfect
31:12
now let's go ahead and run this and once
31:16
we run these Suites its of course it's
31:18
it has compiled there now let's go ahead
31:20
and train the model for a training a
31:23
model it is really very simple as we
31:25
have been doing into our SQL library
31:27
there we have a mortal dot paid and then
31:32
here we have X underscore train and then
31:35
here we have y underscore train and then
31:41
finally here we have a total number of
31:43
epochs
31:44
okay is equal to 10 so with this once we
31:49
write this it will start suing a
31:52
progress bar our during the training so
31:56
the first time at the first epoch itself
31:58
the accuracy has increased to 82 now do
32:02
you know the epoch the epoch means at
32:04
the first time the you know the weights
32:08
get initialized randomly and when model
32:11
moves to the second day pork then via
32:14
back propagation it updates the model
32:16
that's mean what it is doing at the ten
32:19
times it is updating the models and then
32:22
it is running on whole data and each
32:25
epoch okay that's minify defining your a
32:28
box is equal to the ten then that so in
32:31
this model this this model is getting
32:34
trained ten times on whole data that's
32:37
mean the weights are getting updated
32:39
ten times on the whole data now let's go
32:43
ahead and finally evaluate the accuracy
32:46
of the model how we can evaluate the
32:48
accuracy to evaluate the accuracy and
32:52
the tensorflow has inbuilt model dot he
32:54
will wait but in this video version that
32:56
is not working very precisely
32:59
that's me let's say if I write here a
33:01
test loss and then the test accuracy is
33:07
equal to model dot
33:10
evaluate okay so there it has X
33:14
underscore test and then Y underscore
33:18
test okay and then if we print here the
33:24
test I Chrissy let's go ahead and see
33:26
how much this tie Chrissy we will get
33:28
here so this this is a kind of there is
33:33
a problem I think perhaps that's why it
33:35
is you know suing these random things
33:37
although this will take us some time
33:39
just around return 10 to 20 seconds and
33:42
then it gets completed and then finally
33:44
it will the source total accuracy on a
33:48
test set
33:49
okay now you see here the tests accuracy
33:52
on test set has been shown at the end of
33:55
this that says that the eighty eight
33:57
point seven five percent of the accuracy
33:59
Rd test and the total loss is zero point
34:03
two five
34:04
now you see here during the training our
34:07
accuracy was a 91% and at the testing
34:10
time accuracy is 88% that shows that the
34:12
overfitting of our model so this is kind
34:15
of a very simple neural network model
34:17
just similarly just a single layer is
34:20
there just a single hidden layer with
34:23
the 128 neurons so we can expect that
34:26
this much of the accuracy with this
34:28
although if we use Union and other
34:31
networks on this then we definitely we
34:33
can get a better accuracy okay and on
34:36
the github it it is claimed that with
34:38
the CNN we can get around to 99%
34:41
accuracy in some other lessons we will
34:43
be also learning it with the CNN as well
34:46
now let's go ahead and do the prediction
34:48
with the now let's go ahead and do the
34:53
prediction with the with the Escalon as
34:58
well okay so what we can do here with
35:00
from s killer dot matrix and then here
35:07
we have import a crazy score okay so now
35:13
we are we have here we have here
35:15
accuracy sorry now we need to first get
35:18
the wipe read as well so that we can get
35:21
here Y prayer is equal to
35:24
the wipe rate is equal to the model dot
35:30
predict okay now you see here we have
35:32
the two classes actually the predict and
35:34
the predict classes and the predict
35:36
probability so the predict will predict
35:39
a set of the array that will be the
35:41
continuous value but we need a predict
35:43
classes so with the predict classes we
35:46
can get actually what is the predicted
35:48
class instead of a continuous value on
35:51
yesterday doesn't that is expressed and
35:54
then finally let's go ahead and bring it
35:57
with the accuracy score that here we
36:00
have y underscore test and then here we
36:03
have y underscore bread so now you see
36:06
we have got the accuracy of eighty eight
36:08
point seven five percent which we have
36:11
caught with thee with the model dot
36:13
evaluate although I think there is some
36:15
bug in this current version of the
36:17
tensorflow that's why these things we
36:18
are coming okay
36:20
perfect now let's go ahead and make a
36:25
prediction on adjust to some random the
36:28
random test the image on us just a
36:30
single image separately and then we will
36:32
stop this lesson okay to do that what we
36:35
can do you can just right there let's go
36:38
ahead with the bread played with the
36:40
model dot a simple predict and then
36:44
finally we have here X underscore test
36:46
now if we print here the bread so the
36:49
prettiest kind of you know a continuous
36:51
array that's why I had not done with the
36:54
predict only that's why I had used here
36:56
the predict classes and if you see there
37:00
the wipe read the wipe read here is
37:03
continuous its its categorical value
37:07
actually that's been the classes okay so
37:10
with this now let's go ahead
37:12
one thing you see and the class has been
37:15
predicted the first class has been
37:16
predicted to nine and if you see here
37:18
the first array the continuous value now
37:22
you see here at the ninth one okay
37:24
that's in the tenth class tenth number
37:26
at the ninth index at the tenth index
37:30
that's mean you know zero it starts from
37:33
the zero that's been here nine so it
37:35
says that at the 98th
37:37
sent with the confidence of the 98% that
37:40
it is the ninth okay what we can do now
37:43
we can prayed here at the zero value now
37:47
with this you can we see it very clearly
37:49
okay so this is the maximum out you know
37:53
the ninth place so that how we can do we
37:59
can do with the org max here okay so
38:02
here we have n P dot arcamax there's
38:05
been the maximum argument at which place
38:07
there so that's the Preds ero at the
38:10
plate 0 you see maximum argument at 0th
38:13
location and similarly we can bring this
38:17
the maximum prediction at at the first
38:20
location as well okay so at the first
38:23
location the maximum is you know the
38:26
argument - okay perfect so this is the
38:30
way how we work with the tensorflow 2.0
38:33
this is all about in this lesson please
38:36
don't forget to like this video and
38:38
subscribe this channel so that you can
38:39
get updates directly into your inbox in
38:43
further lessons all week also covering
38:45
more videos on a tensorflow and deep
38:47
learning till then bye bye and keep
38:50
learning


'''
def noTime(s):
    l = s.split('\n')
    l2 = []
    for i in l:
      i = re.sub(r'\d\d:\d\d', "", i)
      if len(i)!=0:
        l2.append(i)
    s2 = "\n".join(l2)
    return s2
s2 = noTime(s)    
print(s2)
```

    doesn't Eugene into global variables and
    the tensorflow 2.0 has also removed this
    essence the earlier in tensorflow
    we had to use the system dot run and now
    the tensorflow 2.0 is kindly kind of
    bringing it like a function call and
    moreover now the tensor flew to point X
    R to find zero brings the clearance at
    the core of the tensor flow which
    ultimately increases the you know
    improves the accuracy that that actually
    can increase the accuracy but that is
    not 100% sure that that increases the
    accuracy but moreover it reduced the
    training and the testing time since the
    Kira's has been integrated with the core
    of the tensor flow and in that case the
    its execution will be the faster
    actually and it also takes a less space
    and moreover it is the consistent and if
    you want to know more about the tensor
    flow 2.0 what I it is offering you can
    go ahead and visit this link it has
    Google IO link there and at the Google
    i/o you can you know to see this the
    complete the getting started with the
    tensor flow 2.0 at the Google i/o so the
    air google has released this tensor flow
    2.0 and they have covered almost
    everything what is the new in the tensor
    flow 2.0
    there are so many things to the new into
    the tensorflow 2.0 although this is the
    new video series and we will be learning
    a lot about the tensorflow
    2.0 throughout this video series now the
    let's go ahead the very quickly and I'm
    assuming that you have already installed
    the an akuna at the necessary library
    only you need to install the tensorflow
    and if you do remember the previously
    you need to install the chaos and the
    tensorflow separately but here you only
    need to install that cancer flow you
    actually don't need to install the
    Kiera's so you can call the pip install
    tensorflow equal to equal to the 2.0 RC
    and you can go ahead to this github link
    where you can get the tensorflow the
    released okay so here we have a
    tensorflow 2.0 and you can visit that I
    think with this yes so here we have a
    you know the latest tensorflow the 2.0
    this this one is the not the latest one
    although with the website if you go and
    visit on the website there you will get
    a latest one the tensorflow 2.0 the
    release candidate is available and you
    just go ahead there you will get the
    link here to install this so you can
    keep monitoring this mission this link
    to get the updated version by the time
    I'm making this video this is the latest
    version now let's go ahead and open
    anaconda into administrator mode
    remember you need to open it into the
    administrator mode otherwise it would
    not be able to install the tensorflow
    2.0 in your computer because of the
    right permission now let's go ahead and
    copy this which I can just copy it and
    in the anaconda right the pressing the
    right click it will paste here the PIP
    installed tensorflow equal to equal to
    two point zero point zero RC 0 that if
    the release candidate 0 let's go ahead
    and hit the enter although I have
    already installed the tensorflow 2.0
    that's why it is saying that the
    all the requirement has been already
    satisfied but if you do not have the
    tensorflow 2.0 installed in your
    computer you can install and the
    moreover if you get the any error then
    you can first uninstall the previous
    tensorflow for that you can right there
    pip uninstalled tensorflow so it will
    uninstall your previous versions and
    then you can install a new version of a
    tensorflow
    okay perfect now let's go ahead and see
    if you have a GPU in your computer then
    you can also install a GPU version of a
    tensorflow
    right so these are the two ways where
    you can install a tensorflow in your
    computer now you can pause the video and
    pause this video and that you can
    continue this video after installing the
    tensorflow
    2.0 alright now let's go ahead import
    the fashion mms data set so in this
    lesson we will be working on the finest
    fashion m-miss data set the fashion m
    needs to data set the link is available
    here and this working we working file is
    available in the video description from
    where you can download and if you visit
    this fashion m niche then you see here
    on the github the link is available and
    on the github it says that this is
    Jolanda article images it has 60
    thousands examples and every sample have
    20 28 cross 28 grayscale images and so
    these are the images and it has a 10
    actually it has two total the ten
    classes and that's mean there are 10
    type of the the fashion images are of
    level in this fashion amidst dataset
    okay so these are the images which are
    available and and and and this sixty
    thousand images which we will be using
    to train and ten thousand images to
    we'll be using to evaluate and it has
    total the ten categories of these images
    ok now let's go ahead
    and first import our learner now first
    let's go ahead and import the tensorflow
    and then I'll show you how you can
    download this the amnesty data set
    directly into your Jupiters notebook
    instead of downloading it from a geek
    health ok / pets to import the
    tensorflow you need to write their the
    import and then the tensorflow
    there we have a tensor flow as usual
    tensor flow as DF and then we need to
    improve the care as from the tensor flow
    so here we have a from tensor flow
    import the Kira's okay so now we have
    got sorry we have got the tensor flow
    and in the chaos sorry yeah now we have
    imported the Kira's from a tensor flow
    now let's go ahead and import other
    necessary libraries like numpy pandas
    and the matplotlib so those things we
    can say that a helper liability but
    before that let's go ahead and check a
    tensor flow version which you can just
    check from a print T F dot version so
    this says that we have Overson 2.0
    installed in my computer now let's go
    ahead and import helper libraries like
    an umpire Pentagon the matplotlib so in
    the previous videos we have been
    importing these libraries very
    frequently numpy as in P and import
    pandas HPD and then import might float
    lib dot type lot as PLT so here we have
    matplotlib i the pandas and the numpy
    imported in our computer so these things
    we can treat as a helper libraries now
    let's go ahead and load the amnesty
    person dataset so for that i can write
    here the amidst is equal to
    the Kyra's dot datasets and then I can
    write there the fashion I'm honest so
    with this we will get a pass anemones
    dataset although I have already
    downloaded it my computer otherwise it
    might take a little time in your
    computer to download this data set from
    a internet that might take a few seconds
    if you have a fast internet now let's go
    ahead and check the type of the
    immunised this says that with this
    immunised actually it has downloaded the
    data sets in a tensor flow module
    wrapper now what we need to do now we
    need to actually load the data now we
    need to load this data into into a real
    real variables in this jupiter notebook
    and to do that it actually returns a
    tuple ok the two tuples wonderful for
    the training and another tougher for the
    testing so for this what we can do here
    the m in each dot a load data set as
    usual we have been doing into a scalar
    now in this topple we need to first down
    get the data into our our the training
    dataset that is the extreme and then
    finally Whiterun and the next couple in
    the next it returns the testing data
    sets it has X underscore test and then Y
    underscore test so it has a 60,000 rows
    for a training which we can verify that
    with X train dot safe now there you see
    here there are 60,000 images are
    available there and each images have 28
    cross 28 some since there are 60,000
    images that's mean it should have a
    60,000 y train as well so let's go ahead
    and check the safe of Y trend which says
    that it has a 60,000 okay now let's go
    ahead and print the X train and see what
    happens
    once we print the extreme we see the
    values the most of the values we are
    printing here 0 that is because you note
    at the ages since this is the grayscale
    so at the edges the most of the images
    values are 0
    otherwise the maximum value inside this
    the area which we can find that within P
    dot max okay so that's it the 255 so the
    minimum we have already seen in there
    and that that is the zero but here are
    the max is 255 and if we see the average
    that's mean the N P dot mean the X train
    so it says that something so moreover
    now we can we can say that the values is
    somewhere in between 0 and the 255 okay
    inside this data set which we later we
    need to bring down in between 0 and 1 to
    train with the tensor flow tensor flow
    model okay our deep learning model and
    these 60,000 images are classified into
    ten labels and those labels are encoded
    into a numerical values and those
    numerical values we can see with the Y
    under escort rain and those numerical
    values are in between 0 & 1 sorry 0 1 9
    okay so it starts from the 0 until the 9
    so those are the 10 categories there now
    let's go ahead and write those category
    names although you can get on the pass
    and M minister's category names there
    you should get those category names
    somewhere here
    yes which category names are here okay
    so these are the desert trouser pullover
    dress code sandal cert sneaker back at
    the ankle board now let's go ahead and
    and write that the class names here so
    that we can write in new variable the
    class name and inside those class name
    we need to write it
    okay the desert sign the topic cetera
    like here we have let us go at the top
    and the Ender when we have here at
    rapture and then here we have the
    pullover and then here we have dress
    then we have a court and then finally we
    have the sandal and then we have a cert
    and then we have a sneaker and then
    after that we have back sorry it's bad
    actually not a bad and then we have
    ankle boot so these are dipped in
    classes right now let's go ahead and do
    some the the data exploration so with
    this data exploration we can actually
    understand our data in in more explode
    way okay so since we already have seen
    its you know the same etc so here if we
    see the X underscore the train dot say
    we have 60,000 images but if we see here
    X underscore test dot safe there we see
    we have just 10,000 images
    so this 60,000 images is available for a
    training and these 10,000 images
    available for testing purpose so that we
    can test our model and we can see how
    accurate our model is performing now let
    us go ahead and visualize the visualize
    the data some images so we can visualize
    that with the PLT so here we have a PLT
    door failure and then we have a PLT dot
    image so that's the I am so and inside
    that we are gonna the see first image
    okay that is the extreme zero and then
    I'm gonna just see it and now you will
    see here it has this image okay so this
    is actually the boot okay and how would
    you know this is boot and if we if we
    print here
    the X screen actually there you see its
    nine number and at the nine number you
    see here we have ankle boot okay so this
    is the word and if we see here one
    number and now you see had the one
    number it's a zero and at the zero it is
    at top okay so this is how we can
    visualize and if we print here a color
    bar at the side okay so we can just
    right there the color bar okay so with
    the color bar now you see we have here a
    color bar and this color bar now you see
    the value is somewhere in between 0 and
    the 255 since since neural network model
    doesn't take the value greater than the
    one that's mean we need to bring down
    this the value in the maximum value the
    255 in between somewhere 0 and 1 so what
    we can do to bring it down we can just
    divide the value with 255 I mean the
    training and the testing data set with
    the 255 so we can get here with X
    underscore X underscore train dot sorry
    X underscore train is equal to X
    underscore sorry X underscore train and
    then divide it by two fifty five point
    zero okay perfect
    all right so we have got the extreme in
    between 0 and the 1 and similarly let's
    go ahead and bring the X test in between
    0 & 1 which we can get by dividing X
    test by 255 point 0 so with this we have
    got our X train and the X test in
    between and in in between the 0 to 25
    and what we can do we can just copy it
    although you need to use your keyboard
    control and the C and let's go ahead and
    paste it here and see what happens now
    now with this you can see here we have
    brought it down in between 0 and
    one okay so now this this value is now
    ready to feed into into into a neural
    network and one more thing you might
    have noticed that this size it's a size
    is 28 cross 28 that's mean there are 28
    pixels and these are the pixels which
    you can see okay so these are the pixels
    a square dot there so these are the 28
    dots here and the 28 is here okay
    perfect now let's go ahead now build a
    model a machine learning model with the
    tensorflow
    2.0 with the f 2.0 okay so so so in this
    what we are going to do the basic
    building blocks in any neural network is
    a neural network layers okay so the
    lyric extracts the representation from
    the data and Anthony peered into into
    into it's a hidden layer actually and
    then finally it starts the training okay
    so although this is the very critical
    instance on the tensorflow 2.0 and I'm
    assuming that you know a little about
    the neural network so basically you
    understand how the neural network works
    so let's go ahead and import the
    sequential and the dense model
    sequential and the dense layers from
    tensorflow Kira's to do that what we can
    do the front ends are flow from the
    tensorflow dot Kira's import sequential
    and then from tensorflow dot dot Kira's
    and then got layers import and from here
    I'm gonna import the flatten layer that
    will be used as a first layer and then
    dense layer so we have got the two layer
    and flatten and the dense and the
    sequential model now let's go ahead and
    create our model so here we are gonna
    build
    our model with the sequential model so
    here we have a sequence here and then we
    are gonna pass here ready okay so so the
    area means the how many are the layers
    we need inside our sequential model
    there are many ways to build this but I
    think this is the simplest way where we
    can add all these together otherwise
    there are a few other ways like like
    just defining first sequential and then
    going with the model dot add we can go
    ahead with that one as well like model
    dot add and then we can add there the
    first flatten layer there and inside the
    flatten layer the input shape okay which
    we are gonna use here input shape will
    be the 28 cross a 28 there okay so this
    is an input safe for our the flatten
    layer the flat hair doesn't do anything
    actually it's just transformed the the
    formats of this data which is 28 cross
    to 28 so this this layer just
    transformed this data into a one
    dimensional so that we can fit into the
    next layer okay so the next layer which
    I'm gonna add here in the model dot and
    that is a dense layer okay so this is
    just a dense layer and inside the dense
    layer if you press your sift and double
    tab you will get here detail the
    documentation on it
    so in this I'm gonna pass the number of
    units that's been the number of nodes
    how many the neural neurons actually we
    want and then we will pass here the
    activation function which activation
    function we are gonna use I'll be taking
    a different lessons where I will be
    covering all these things in a very
    detail this is a very quick lesson so
    I'm not going to cover all those things
    here in the detail so activations we
    will be using and other things we will
    be just passing as usual okay so other
    things will be like yeah
    other things will be a default actually
    so here in the dense layer I am gonna
    pass here the 128 new rooms at the
    firstly and the activation function
    which we had talked there that I'm gonna
    use here a raloo activation so this is
    kind of the detective higher the
    activation function there are so many
    other kind of activation function like a
    sigmoid an edge and you know the
    Rayleigh key relive all those so here
    for this listen I'm just gonna use your
    a loop and then the model dot ad and
    then again I'm gonna use the output
    layer in an output layer if you add the
    output layer then we need to define the
    how many outputs are there that's when
    the total number of classes we have a
    ten classes that's when we have to
    define here the ten and the activation
    function here so at the output the real
    you activation things an activation
    cannot be used so there at the output
    either we can use the sigmoid or softmax
    so here we are gonna use a soft max okay
    so here we have a model now let's go
    ahead and print the summary on this
    model and then you might understand how
    it is building so the first model has
    transformed a two-dimensional data into
    a single dimensional and then here we
    have 128-bit 128 neurons so 128 and then
    multiplied by that 784 its complexity
    reaches the number of parameters
    actually then reaches to these digits
    okay so that is the hundred thousands
    and then finally at the output we are
    bringing it down to the ten okay jester
    ten so we have number of parameters at
    the final output to calculate it the
    twelve hundred and ninety okay so the
    total parameter which we which this
    model will be executing is more than
    100,000 okay so this is how we build the
    model now we need to compile our model
    okay so for compliation of the model
    there are a few things which are really
    very important okay the first which need
    we need to actually define sorry we need
    to convert it into a markdown
    yes so the first thing which we need to
    define is a loss function okay
    model compliation
    so to compile the model we need to
    define the loss function which loss
    function we want here and then we want
    optimizer okay and then after optimizer
    we want here metrics so what are these
    things a loss function it will measure
    how accurate the model is during the
    training and testing then okay actually
    the loss function minimize minimize the
    overall error during the training and
    once the error is minimized during the
    training then the testing error will be
    also minimized but that is not always
    the true because sometimes what happens
    if your model overpaid then the oral law
    skit minimized during the training but
    during the testing it get increased
    so here the generalization of model is
    very important that's where optimizer
    comes so this is how model is updated
    based on the data that's been the
    weights of our model applicants updated
    with the you know as we define the
    optimizer now let's go ahead and compile
    this model first so we can compile this
    with the model dot dot the compiled and
    then here we have optimizer is equal to
    Adam and then here we have a loss
    function there a loss is equal to a
    spazz categorical okay so there we have
    a sparse and categorical cross entropy
    okay
    and then finally here we have a matrix
    and inside this matrix we have accuracy
    okay perfect
    now let's go ahead and run this and once
    we run these Suites its of course it's
    it has compiled there now let's go ahead
    and train the model for a training a
    model it is really very simple as we
    have been doing into our SQL library
    there we have a mortal dot paid and then
    here we have X underscore train and then
    here we have y underscore train and then
    finally here we have a total number of
    epochs
    okay is equal to 10 so with this once we
    write this it will start suing a
    progress bar our during the training so
    the first time at the first epoch itself
    the accuracy has increased to 82 now do
    you know the epoch the epoch means at
    the first time the you know the weights
    get initialized randomly and when model
    moves to the second day pork then via
    back propagation it updates the model
    that's mean what it is doing at the ten
    times it is updating the models and then
    it is running on whole data and each
    epoch okay that's minify defining your a
    box is equal to the ten then that so in
    this model this this model is getting
    trained ten times on whole data that's
    mean the weights are getting updated
    ten times on the whole data now let's go
    ahead and finally evaluate the accuracy
    of the model how we can evaluate the
    accuracy to evaluate the accuracy and
    the tensorflow has inbuilt model dot he
    will wait but in this video version that
    is not working very precisely
    that's me let's say if I write here a
    test loss and then the test accuracy is
    equal to model dot
    evaluate okay so there it has X
    underscore test and then Y underscore
    test okay and then if we print here the
    test I Chrissy let's go ahead and see
    how much this tie Chrissy we will get
    here so this this is a kind of there is
    a problem I think perhaps that's why it
    is you know suing these random things
    although this will take us some time
    just around return 10 to 20 seconds and
    then it gets completed and then finally
    it will the source total accuracy on a
    test set
    okay now you see here the tests accuracy
    on test set has been shown at the end of
    this that says that the eighty eight
    point seven five percent of the accuracy
    Rd test and the total loss is zero point
    two five
    now you see here during the training our
    accuracy was a 91% and at the testing
    time accuracy is 88% that shows that the
    overfitting of our model so this is kind
    of a very simple neural network model
    just similarly just a single layer is
    there just a single hidden layer with
    the 128 neurons so we can expect that
    this much of the accuracy with this
    although if we use Union and other
    networks on this then we definitely we
    can get a better accuracy okay and on
    the github it it is claimed that with
    the CNN we can get around to 99%
    accuracy in some other lessons we will
    be also learning it with the CNN as well
    now let's go ahead and do the prediction
    with the now let's go ahead and do the
    prediction with the with the Escalon as
    well okay so what we can do here with
    from s killer dot matrix and then here
    we have import a crazy score okay so now
    we are we have here we have here
    accuracy sorry now we need to first get
    the wipe read as well so that we can get
    here Y prayer is equal to
    the wipe rate is equal to the model dot
    predict okay now you see here we have
    the two classes actually the predict and
    the predict classes and the predict
    probability so the predict will predict
    a set of the array that will be the
    continuous value but we need a predict
    classes so with the predict classes we
    can get actually what is the predicted
    class instead of a continuous value on
    yesterday doesn't that is expressed and
    then finally let's go ahead and bring it
    with the accuracy score that here we
    have y underscore test and then here we
    have y underscore bread so now you see
    we have got the accuracy of eighty eight
    point seven five percent which we have
    caught with thee with the model dot
    evaluate although I think there is some
    bug in this current version of the
    tensorflow that's why these things we
    are coming okay
    perfect now let's go ahead and make a
    prediction on adjust to some random the
    random test the image on us just a
    single image separately and then we will
    stop this lesson okay to do that what we
    can do you can just right there let's go
    ahead with the bread played with the
    model dot a simple predict and then
    finally we have here X underscore test
    now if we print here the bread so the
    prettiest kind of you know a continuous
    array that's why I had not done with the
    predict only that's why I had used here
    the predict classes and if you see there
    the wipe read the wipe read here is
    continuous its its categorical value
    actually that's been the classes okay so
    with this now let's go ahead
    one thing you see and the class has been
    predicted the first class has been
    predicted to nine and if you see here
    the first array the continuous value now
    you see here at the ninth one okay
    that's in the tenth class tenth number
    at the ninth index at the tenth index
    that's mean you know zero it starts from
    the zero that's been here nine so it
    says that at the 98th
    sent with the confidence of the 98% that
    it is the ninth okay what we can do now
    we can prayed here at the zero value now
    with this you can we see it very clearly
    okay so this is the maximum out you know
    the ninth place so that how we can do we
    can do with the org max here okay so
    here we have n P dot arcamax there's
    been the maximum argument at which place
    there so that's the Preds ero at the
    plate 0 you see maximum argument at 0th
    location and similarly we can bring this
    the maximum prediction at at the first
    location as well okay so at the first
    location the maximum is you know the
    argument - okay perfect so this is the
    way how we work with the tensorflow 2.0
    this is all about in this lesson please
    don't forget to like this video and
    subscribe this channel so that you can
    get updates directly into your inbox in
    further lessons all week also covering
    more videos on a tensorflow and deep
    learning till then bye bye and keep
    learning
    

### to link


```python
s = '''
Introduction to the Machine Learning Projects
Not Passed
Rock Paper Scissors
Not Passed
Cat and Dog Image Classifier
Not Passed
Book Recommendation Engine using KNN
Not Passed
Linear Regression Health Costs Calculator
Not Passed
Neural Network SMS Text Classifier





'''
l = s.split('\n')
l2 = []
for i in l:
    if i.find("Passed") == -1 \
    and i.strip() != "":
        l2.append(i)
l3 = []
index = 0
bigIndex = ""
shead = ""
words = ["glich work", "glich view"]
for i in l2: 
   shead = bigIndex + str(index) + ". " + i
#    i = re.sub(r'Problem.*?: ', "", i) 
   if index != 0:
        shead = str(index) + " " + i
   else:
        shead = i
   shead = shead.replace("####", "") 
   shead = shead.strip()
   slink = shead.replace(" ", "-")
#    shead = words[index-1]
   shead = "[" + shead + "]" 
   slink = "(#" + slink + ")  " 
   l3.append(shead + slink)
   index += 1
s2 = "\n".join(l3)
print(s2)
```

    [Introduction to the Machine Learning Projects](#Introduction-to-the-Machine-Learning-Projects)  
    [1 Rock Paper Scissors](#1-Rock-Paper-Scissors)  
    [2 Cat and Dog Image Classifier](#2-Cat-and-Dog-Image-Classifier)  
    [3 Book Recommendation Engine using KNN](#3-Book-Recommendation-Engine-using-KNN)  
    [4 Linear Regression Health Costs Calculator](#4-Linear-Regression-Health-Costs-Calculator)  
    [5 Neural Network SMS Text Classifier](#5-Neural-Network-SMS-Text-Classifier)  
    

  


```python
import re
# s = '''
# '''
l = s.split('\n')
l2 = []
for i in l:
    if i.find("Passed") == -1 \
    and i.strip() != "":
        l2.append(i)
l3 = []
index = 0
for i in l2: 
   i = re.sub(r'Problem.*?: ', "", i) 
   if index != 0:
        l3.append("#### " + bigIndex + str(index) + " " + i)
   else:
        l3.append("#### " + bigIndex + i)
#    l3.append("#### " + bigIndex +  i)
   l3.append("```")
   l3.append("```")
   index += 1
s2 = "\n".join(l3)
print(s2)
```

    #### Introduction to the Machine Learning Projects
    ```
    ```
    #### 1 Rock Paper Scissors
    ```
    ```
    #### 2 Cat and Dog Image Classifier
    ```
    ```
    #### 3 Book Recommendation Engine using KNN
    ```
    ```
    #### 4 Linear Regression Health Costs Calculator
    ```
    ```
    #### 5 Neural Network SMS Text Classifier
    ```
    ```
    




```python
s = '''
'''
l = s.split('\n')
l2 = []
for i in l:
    if i.find("Passed") == -1 \
    and i.strip() != "":
        l2.append(i)
l3 = []
index = 1
for i in l2: 
   l3.append("### "+ "3." + str(index) + ". " + i)
   index += 1
s = "\n".join(l3)
print(s)
```

    
    



[Google Переводчик](https://chrome.google.com/webstore/detail/google-translate/aapbdbdomjkkjkaonfhkkikfgjllcleb/related?hl=ru)  
[4 расширения Chrome, которые мгновенно переводят выделенный текст](https://lifehacker.ru/chrome-translator/)  
[]()  
[]()  
[]()  
[]()  

