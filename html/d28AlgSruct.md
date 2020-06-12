### Algorithms
### Data Structures

### Algorithms

[Introduction to the Coding Interview Algorithms](#Introduction-to-the-Coding-Interview-Algorithms)  
[1. Find the Symmetric Difference](#1.-Find-the-Symmetric-Difference)  
[2. Inventory Update](#2.-Inventory-Update)  
[3. No Repeats Please](#3.-No-Repeats-Please)  
[4. Pairwise](#4.-Pairwise)  
[5. Implement Bubble Sort](#5.-Implement-Bubble-Sort)  
[6. Implement Selection Sort](#6.-Implement-Selection-Sort)  
[7. Implement Insertion Sort](#7.-Implement-Insertion-Sort)  
[8. Implement Quick Sort](#8.-Implement-Quick-Sort)  
[9. Implement Merge Sort](#9.-Implement-Merge-Sort)



### Data Structures

[Introduction to the Coding Interview Data Structure Questions](#Introduction-to-the-Coding-Interview-Data-Structure-Questions)  
[1. Typed Arrays](#1.-Typed-Arrays)  
[2. Learn how a Stack Works](#2.-Learn-how-a-Stack-Works)  
[3. Create a Stack Class](#3.-Create-a-Stack-Class)  
[4. Create a Queue Class](#4.-Create-a-Queue-Class)  
[5. Create a Priority Queue Class](#5.-Create-a-Priority-Queue-Class)  
[6. Create a Circular Queue](#6.-Create-a-Circular-Queue)  
[7. Create a Set Class](#7.-Create-a-Set-Class)  
[8. Perform a Union on Two Sets](#8.-Perform-a-Union-on-Two-Sets)  
[9. Perform an Intersection on Two Sets of Data](#9.-Perform-an-Intersection-on-Two-Sets-of-Data)  
[10. Perform a Difference on Two Sets of Data](#10.-Perform-a-Difference-on-Two-Sets-of-Data)  
[11. Perform a Subset Check on Two Sets of Data](#11.-Perform-a-Subset-Check-on-Two-Sets-of-Data)  
[12. Create and Add to Sets in ES6](#12.-Create-and-Add-to-Sets-in-ES6)  
[13. Remove items from a set in ES6](#13.-Remove-items-from-a-set-in-ES6)  
[14. Use .has and .size on an ES6 Set](#14.-Use-.has-and-.size-on-an-ES6-Set)  
[15. Use Spread and Notes for ES5 Set() Integration](#15.-Use-Spread-and-Notes-for-ES5-Set()-Integration)  
[16. Create a Map Data Structure](#16.-Create-a-Map-Data-Structure)  
[17. Create an ES6 JavaScript Map](#17.-Create-an-ES6-JavaScript-Map)  
[18. Create a Hash Table](#18.-Create-a-Hash-Table)  
[19. Work with Nodes in a Linked List](#19.-Work-with-Nodes-in-a-Linked-List)  
[20. Create a Linked List Class](#20.-Create-a-Linked-List-Class)  
[21. Remove Elements from a Linked List](#21.-Remove-Elements-from-a-Linked-List)  
[22. Search within a Linked List](#22.-Search-within-a-Linked-List)  
[23. Remove Elements from a Linked List by Index](#23.-Remove-Elements-from-a-Linked-List-by-Index)  
[24. Add Elements at a Specific Index in a Linked List](#24.-Add-Elements-at-a-Specific-Index-in-a-Linked-List)  
[25. Create a Doubly Linked List](#25.-Create-a-Doubly-Linked-List)  
[26. Reverse a Doubly Linked List](#26.-Reverse-a-Doubly-Linked-List)  
[27. Add a New Element to a Binary Search Tree](#27.-Add-a-New-Element-to-a-Binary-Search-Tree)  
[28. Find the Minimum and Maximum Value in a Binary Search Tree](#28.-Find-the-Minimum-and-Maximum-Value-in-a-Binary-Search-Tree)  
[29. Check if an Element is Present in a Binary Search Tree](#29.-Check-if-an-Element-is-Present-in-a-Binary-Search-Tree)  
[30. Check if Tree is Binary Search Tree](#30.-Check-if-Tree-is-Binary-Search-Tree)  
[31. Find the Minimum and Maximum Height of a Binary Search Tree](#31.-Find-the-Minimum-and-Maximum-Height-of-a-Binary-Search-Tree)  
[32. Use Depth First Search in a Binary Search Tree](#32.-Use-Depth-First-Search-in-a-Binary-Search-Tree)  
[33. Use Breadth First Search in a Binary Search Tree](#33.-Use-Breadth-First-Search-in-a-Binary-Search-Tree)  
[34. Delete a Leaf Node in a Binary Search Tree](#34.-Delete-a-Leaf-Node-in-a-Binary-Search-Tree)  
[35. Delete a Node with One Child in a Binary Search Tree](#35.-Delete-a-Node-with-One-Child-in-a-Binary-Search-Tree)  
[36. Delete a Node with Two Children in a Binary Search Tree](#36.-Delete-a-Node-with-Two-Children-in-a-Binary-Search-Tree)  
[37. Invert a Binary Tree](#37.-Invert-a-Binary-Tree)  
[38. Create a Trie Search Tree](#38.-Create-a-Trie-Search-Tree)  
[39. Insert an Element into a Max Heap](#39.-Insert-an-Element-into-a-Max-Heap)  
[40. Remove an Element from a Max Heap](#40.-Remove-an-Element-from-a-Max-Heap)  
[41. Implement Heap Sort with a Min Heap](#41.-Implement-Heap-Sort-with-a-Min-Heap)  
[42. Adjacency List](#42.-Adjacency-List)  
[43. Adjacency Matrix](#43.-Adjacency-Matrix)  
[44. Incidence Matrix](#44.-Incidence-Matrix)  
[45. Breadth-First Search](#45.-Breadth-First-Search)  
[46. Depth-First Search](#46.-Depth-First-Search)  



### Algorithms

#### Introduction to the Coding Interview Algorithms
```
```
#### 1. Find the Symmetric Difference
```
function sym2(a,b){
  var c = sub(a,b).concat(sub(b,a));
  return c.sort();
}

function sub(a,b){
var s = new Set(a);
a = [...s];
a.sort();
s = new Set(b);
b = [...s];
b.sort();
var accum = [];
var k = 0;
var knext = 0;
var kmax = b.length
var c = []
for(var i=0; i<a.length;i++){
  k = knext;
  while(k < kmax){
    if(a[i]==b[k]){
      knext = k+1;
      break;
    }
    k++;
  }
    accum.push(a[i]);
  if(k==kmax){
      c.push(a[i]);
  }
}
return c;
}

function sym(...args){
var a = args[0];
var b =[];
for(var i=1;i<args.length;i++){
  b=sym2(a, args[i]);
  a = b;
}
  return b; 
}
sym2([1, 2, 4, 5],[1, 2, 3]);
var a = sym([1, 2, 5], [2, 3, 5], [3, 4, 5]);
console.log(a)
```

#### 2. Inventory Update
```
function updateInventory(arr1, arr2) {

    var arrc = [];
    for(var i in arr1){

        for(var j=0; j<arr2.length;j++){
          if(arr1[i][1] == arr2[j][1] ){
arr1[i][0] +=arr2[j][0];
arr2.splice(j, 1);
break;
          }
      }
    }
    arrc = arr1.concat(arr2)
arrc.sort((a,b) => 
a[1]>b[1]?1:a[1]<b[1]?-1:0);
    console.log(arrc.length, arrc);
    // All inventory must be accounted for or you're fired!
    return arrc;
}

// Example inventory lists
var curInv = [
    [21, "Bowling Ball"],
    [2, "Dirty Sock"],
    [1, "Hair Pin"],
    [5, "Microphone"]
];

var newInv = [
    [2, "Hair Pin"],
    [3, "Half-Eaten Apple"],
    [67, "Bowling Ball"],
    [7, "Toothpaste"]
];

updateInventory(curInv,newInv);
```

#### 3. No Repeats Please
##### next
правое значение из левого массива надо
заменить на наименьшее значение из прового,
но которое больше этого значения.
а оставшийся правый массив отсортировать по порядку.
  
```
equalArrays next repeatFirst repeat setSymv nextAll fact
```

```
var log = console.log;

function equalArrays(arr1, arr2){
  return arr1.join()==arr2.join();
}

function getArrR(arr){
  var arrEnd=[];
  var k = arr.length - 1;
  var a0 = arr[k];
  var n=0;
  arrEnd.push(arr[k]);
  k--;
  while(k>=0){
    if(arr[k]<a0){
      break;
    }else{
      arrEnd.unshift(arr[k]);
      a0 = arr[k];
    }
    k--;
  }
  //log(arrEnd);
  return arrEnd;
}

function getArrL(arr, arrR)
{
  var arrEnd = [];
  arrEnd= arr.slice(0, -arrR.length);
  return arrEnd;
}
function plus(arrL, arrR){
  var arr1 = arrL.slice();
  var arr2 = arrR.slice();
  var arrEnd=[];
  var vr = arr1[arr1.length-1];
  arr1.splice(-1);
  arr2.sort();
  for(var i=0;i<arr2.length;i++){
    if(vr<arr2[i]){
      arr1.push(arr2[i]);
      arr2.splice(i, 1);
      arr2.push(vr);
      break;
    }
  }
  arr2.sort();

  arrEnd=arr1.concat(arr2);
  return arrEnd;
}

function next(arr){
  var endArr = [];
  var arrR = getArrR(arr);
  var arrL = getArrL(arr, arrR);
  endArr = plus(arrL, arrR);

  return endArr;
}

function nextAll(n){
  var res = 1;
  var arrFirst=[];
  var arrLast=[];
  for(var i=0;i<n;i++){
    arrFirst.push(i+1);
    arrLast.unshift(i+1);
  }
  var n = 0;
  var arr=arrFirst;
  var arrEnd = [];
  arrEnd.push(arr.concat());
  while(1){
    arr = next(arr);
    arrEnd.push(arr.concat());
    res++;
    if(equalArrays(arr,arrLast)){
      break;
    }
    n++;
  }
  return arrEnd;
}

function repeatFirst(arrv){
  var res = false;
  var arr = arrv.slice();
  arr.sort();
  var arrSum = [];
  var a0 = arr[0];
  arrSum.push([a0, 1]);
  var k = 0;
  for(var i=1; i<arr.length; i++){
    if(arr[i] == a0){
     arrSum[k][1]+=1;
    }else{
      arrSum.push([arr[i], 1]);
      a0 = arr[i];
      k++;
    }
  }
  if(arrSum.length == 1){
    if(arrSum[0][1]>1)
    return true;
    else return false;
  }
arrSum.sort((a,b)=>b[1]-a[1]);
var v = arrSum.reduce((a,v,i)=>{
  if(i>0){
  return a+v[1];
  }else{return a;}
},0);
arrSum[1][1] = v;
if(arrSum[0][1]-arrSum[1][1]>=2){
  res = true;
}
  return res;
}


function repeat(arrv){
  var res = false;
  var arr = arrv.slice();
  var a0 = arr[0];
  for(var i=1;i<arr.length;i++){
    if(a0 == arr[i]){
      res = true;
      break;
    }
    a0 = arr[i];
  }
  return res;
}

function setSymv(arra, arr1){
  var arrRes = [];
  for(var i in arr1){
    arrRes[i] = arra[arr1[i]-1];
  }
  return arrRes;
}

function fact(k){
  var arr = [1, 2, 6, 24, 120, 720, 5040, 40320];
  return +arr[k-1];
}

function permAlone(str) {
  var t= []; 
  var arrav = str.split("");
  if(repeatFirst(arrav)){
    return 0;
  }
  var length = arrav.length;
  var arr1v = [];
  for(var i in arrav){
    arr1v.push(+i+1);
  }
  var count = fact(length);
  var arr1=arr1v.slice();
  var arra=arrav.slice();
  var arrb = [];
  var noRepeat = 0; 
  for(var i=0;i<count;i++){
    arrb = setSymv(arra,arr1);
    if(!repeat(arrb)){
      noRepeat++;
    }
    arr1=next(arr1);
//    log(arr1,arrb,repeat(arrb));
  }
  t = count;
  log(t.length,t);
  return noRepeat;
}

var nr = permAlone('aab');
log(nr);
```

#### 4. Pairwise
```
var log = console.log;

function pairwise(arr, arg) {
  var count = arr.length;
  var arrUse = [];
  for(var i in arr){
    arrUse.push(0);
  }
  var arri = [];
  var j = 0;
  for(var i=0;i<count;i++){
    j = i+1;
    while(j<count){
       if(arr[i]+arr[j]==arg){
         if(arrUse[i]+arrUse[j]==0){
         arri.push([i,j]);
         arrUse[i]=1;
         arrUse[j]=1;
         }
       }
      j++;
    }
  }
  var sum = 0
  for(var i in arri){
    sum += arri[i][0] + arri[i][1];
  }
//  log(sum, arri, arrUse);
  return sum;
}

var arr = [];var arg;
arr = [1,4,2,3,0,5];arg=7;
//arr = [7, 9, 11, 13, 15];arg=20;
var t = pairwise(arr, arg);
log(t);
```

#### 5. Implement Bubble Sort
```
var log = console.log;

function bubbleSort(array) {
  // change code below this line
  var count=array.length;
  var arr = array.slice();
  var i = count;
  while(i > 0){
    var j = 1;
    var a0 = arr[0];
    while(j < i){
      if(a0>arr[j]){
        arr[j-1] = arr[j];
        arr[j] = a0;
      }
      a0 = arr[j];
//      log(arr);
      j++;
    }
    i--;
  }
  return arr;
  // change code above this line
}

var arr = [];
arr = [1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92];
//arr = [1, 4, 2, 8];

var t = bubbleSort(arr);
log(t);
```

#### 6. Implement Selection Sort
```
var log = console.log;

function selectionSort(arr) {
  var i = 0;
  var count = arr.length;
  var index = 0;
  while(i < count){
    var j = i + 1;
    var a0 = arr[i];
    index = i;
    while(j<count){
      if(arr[j]<a0){
        a0 = arr[j];
        index = j;
      }
      j++;
    }
    a0=arr[index];
    arr[index]=arr[i];
    arr[i]=a0;
    i++;
  }
  return arr;
  // change code above this line
}

var arr = [1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92];
//arr = [5, 1, 3];
selectionSort(arr);
log(arr);
```



#### 7. Implement Insertion Sort
```
var log = console.log;
function insert(arr, a){
var arrRes = [];
var count = arr.length;
var i = 0;
var once = true;
while(i<count){
  if(arr[i]>a){
    if(once){
      arrRes.push(a);
      once = false;
    }
  }
  arrRes.push(arr[i]);
  i++;
}
if(once){
  arrRes.push(a);
}
return arrRes;
}

function insertionSort(arrv) {
  var arrRes=[];
  var arr = [arrv[0]];
  // change code below this line
  var count = arrv.length;
  var i = 1;
  while(i < count){
    arr = insert(arr, arrv[i]); 
    i++;
  }
  return arr;
  // change code above this line
}

var arr = [1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92];
//arr = [5, 1, 3, 2];
var res = insertionSort(arr);
log(res);
```





```
```

#### 8. Implement Quick Sort
Пивотом назначается 1-й элемент(с нулевым индексом) самый левый элемент.
Массив перебирается со 2-го элемента.
Перебирается следующим образом. 
Получается разбивка массива на две части, левая - меньше пивота, правая больше. 
Если элемент меньше пивота, то индекс правого края левого массива ползет вправо.
Если элемент больше, то индекс останавливается.
Если попадаются элементы меньше, то они меняются местами с первым элементом правого массива и соответственно этот элемент становится правым элементом левого массива.
По окончаниии сортировки пивот встает на правый край левого массива. 
функция возвращает индек пивота.  
Дальше.
если левый индекс равен правому возвращаем массив. Если это не так, то бьем массив на две части и для каждой части вызываем сортировку.



[Информатика в JavaScript: Быстрая сортировка (Quicksort)](https://medium.com/devschacht/nicholas-c-zakas-computer-science-in-javascript-quicksort-afa07c0a47f0)  
```
//Swapping array elements via ES6 array destructuring
function swap(arr, x, y) {
  [arr[x], arr[y]] = [arr[y], arr[x]];
}

//Pivot function returns the fixed pivot point
function pivot(arr, left = 0, right = arr.length - 1) {
  let shift = left;
  for (let i = left + 1; i <= right; i++) {
    //Move all the small elements on the left side
    if (arr[i] < arr[left]) swap(arr, i, ++shift);
  }

  //Finally swapping the last element with the left
  swap(arr, left, shift);
  return shift;
}

function quickSort(array, left = 0, right = array.length - 1) {
  if (left < right) {
    let pivotIndex = pivot(array, left, right);

    //Recusrively calling the function to the left of the pivot and to the right of the pivot
    quickSort(array, left, pivotIndex - 1);
    quickSort(array, pivotIndex + 1, right);
  }
  return array;
}
console.log(quickSort([5,1,3]))
```
ddddddddddddddddddddd
```
var log = console.log;
var k = 0;
function swap(arr, x, y){
  [arr[x],arr[y]]=[arr[y],arr[x]];
}

function pivot(arr, left=0, right=arr.length-1){
let shift=left;
for(let i=left+1;i<=right;i++){
   if(arr[i]<arr[left]){
     swap(arr, i, ++shift)
   }
}
   swap(arr, left, shift);
   return shift;
}

function quickSort(arr, left=0, right=arr.length-1) {
  // change code below this line
  if( left < right){
    let index = pivot(arr, left, right);
    quickSort(arr, left, index);
    quickSort(arr, index+1, right);
  }
  //log(k++,arr);
    return arr;
}

// test array:
// 
var arr;
arr = [1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]
//arr = [4, 5, 3];
var res = quickSort(arr);
log(res);

```

#### 9. Implement Merge Sort
[Сортировка слиянием, JavaScript.](https://medium.com/@alivander/%D1%81%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0-%D1%81%D0%BB%D0%B8%D1%8F%D0%BD%D0%B8%D0%B5%D0%BC-javascript-1c0b0e8ff737)  
```
var log = console.log;

const merge = (arrFirst, arrSecond) => {
    const arrSort = [];
    let j = 0;
    let i = j = 0;
    // сравниваем два массива, поочередно сдвигая указатели
    while (i < arrFirst.length && j < arrSecond.length) {
        arrSort.push(
            (arrFirst[i] < arrSecond[j]) ?
                arrFirst[i++] : arrSecond[j++]
        );
    }
    // обрабатываем последний элемент при разной длине массивов
    // и возвращаем один отсортированный массив
    return [
        ...arrSort,
        ...arrFirst.slice(i),
        ...arrSecond.slice(j)
    ];
};


const mergeSort = arr => {
    // Проверяем корректность переданных данных
    if (!arr || !arr.length) {
        return null;
    }
    //Если массив содержит один элемент просто возвращаем его
    if (arr.length <= 1) {
        return arr;
    }
    // Находим середину массива и делим его на два
    const middle = Math.floor(arr.length / 2);
    const arrLeft = arr.slice(0, middle);
    const arrRight = arr.slice(middle);
    // Для новых массивов снова вызываем сортировку,
    // сливаем их и возвращаем снова единый массив
    return merge(mergeSort(arrLeft), mergeSort(arrRight));;
};
var arr;
arr = mergeSort([5,1,3]);
log(arr);
```

```
var log = console.log;

function merge(arrl, arrr){
  var arrRes = [];
  var cl = arrl.length;
  var cr = arrr.length;
  var i=0,j=0; 
  var n=0;
  while((i<cl || j<cr)&& n++<40){
    if(i<cl && j<cr){
    if(arrl[i]<arrr[j]){
      arrRes.push(arrl[i]);
      i++;
    }else{
      arrRes.push(arrr[j]);
      j++;
    }
    }else{
      if(i<cl){
        arrRes.push(arrl[i]);
        i++;
      }
      if(j<cr){
        arrRes.push(arrr[j]);
        j++;
      }
    }
  }
  return arrRes;
}

function sortArray(arr){
var count = arr.length;
if(count==1){
  return arr;
}

var count2 = count/2;
var arr1 = arr.slice(0,count2);
var arr2 = arr.slice(count2);
var c1 = arr1.length;
var c2 = arr2.length;

return merge(sortArray(arr1), sortArray(arr2));
}

function mergeSort(array) {
  // change code below this line
var arr = sortArray(array);
  // change code above this line
  return arr;
}
// test array:
var arr;
arr = [1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]
var res = mergeSort(arr);
log(res);
```

### Data Structures

#### Introduction to the Coding Interview Data Structure Questions
#### 1. Typed Arrays
```
```
First create a buffer that is 64-bytes. Then create a Int32Array typed array with a view of it called i32View.  
```
var buffer = new ArrayBuffer(64);
var i32View = new Int32Array(buffer);
```
#### 2. Learn how a Stack Works
```
var homeworkStack = ["BIO12","HIS80","MAT122","PSY44"];
// Only change code below this line

homeworkStack.pop();
homeworkStack.push("CS50");
console.log(homeworkStack);
```


#### 3. Create a Stack Class
```
function Stack() {
  var collection = [];
  this.print = function() {
    console.log(collection);
  };
  // Only change code below this line
  this.push = function(val){
    collection.push(val);
  };
  this.pop = function(){
    return collection.pop();
  };
  this.peek = function(){
    return collection[0];
  };
  this.isEmpty = function(){
    return collection.length==0? true: false;
  };
  this.clear = function(){
    collection=[];
  };
 
  // Only change code above this line
}
var stack = new Stack();
stack.push(1);
stack.push(3);
stack.push(5);
stack.pop();
stack.peek();
stack.print();
```


#### 4. Create a Queue Class
```
var log = console.log;

function Queue() {
  var collection = [];
  this.print = function() {
    console.log(collection);
  };
  // Only change code below this line
  this.enqueue = function(val){
    collection.push(val);
  }
  this.dequeue = function(){
    return collection.shift();
  }
  this.front = function(){
    return collection[0];
  }
  this.size = function(){
    return collection.length;
  }
  this.isEmpty = function(){
    return collection.length == 0 ? true : false;
  }

  // Only change code above this line
}

var queue = new Queue();
queue.enqueue(1);
queue.enqueue(2);
queue.enqueue(3); 
var res;
res = queue.dequeue();
log(res);
```
#### 5. Create a Priority Queue Class
```
var log = console.log;
function PriorityQueue () {
    this.collection = [];
    this.printCollection = function() {
      console.log(this.collection);
    };
    // Only change code below this line
this.enqueue = function(val){
  var count = this.collection.length;
  if(count==0){
    this.collection.push(val);
    return;
  }
  if(count==1){
    if(this.collection[0][1]<=val[1]){
      this.collection.push(val);
    }else{
      this.collection.unshift(val);
    }
    return;
  }
  var index0 = count - 1;
  var once = false;
  for(var i=count-1;i>=0;i--){
    if(val[1]<this.collection[i][1]){
      index0 = i;
      once = true;
    }else{
      break;
    }
  }
if(once){
this.collection = [
...this.collection.slice(0,index0),
val,
...this.collection.slice(index0)];
}else{
  this.collection.push(val);
}
}
this.dequeue = function(){
  return this.collection.shift()[0];
}
  this.front = function(){
    return this.collection[0];
  }
  this.size = function(){
    return this.collection.length;
  }
  this.isEmpty = function(){
    return this.collection.length == 0 ? true : false;
  }
    // Only change code above this line
}

var queue = new PriorityQueue();
queue.enqueue(['a',3]);
queue.enqueue(['c',1]);
queue.enqueue(['d',3]); 
queue.enqueue(['b',1]);
 var res;
 queue.printCollection();
 res = queue.dequeue();
 queue.printCollection();
```

#### 6. Create a Circular Queue
```
var log = console.log

class CircularQueue {
   constructor(size) {

     this.queue = [];
     this.read = 0;
     this.write = 0;
     this.max = size - 1;

     while (size > 0) {
        this.queue.push(null);
        size--;
     }
   }

   print() {
     return this.queue;
   }

   enqueue(item) {
    // Only change code below this line
    if(this.write > this.max){
      this.write = 0
    }
var val = this.queue[this.write]
if(val == null){
  this.queue[this.write] = item;
  this.write++
  return item
}else{
  return null
}    
    // Only change code above this line
   }

   dequeue() {
    // Only change code below this line
var res = null    
if(this.read >= this.max+1){
  this.read = 0
}
res = this.queue[this.read]
this.queue[this.read] = null
if(res != null){
this.read++;
}
this.r = this.write - this.read
return res
    // Only change code above this line
   }
}

var cq = new CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
log(cq.write, cq.read, cq.queue)
log(cq.dequeue())
log(cq.write, cq.read, cq.queue)
// 2 0 [ 1, 2, null, null, null ]
// 1
// 2 1 [ null, 2, null, null, null ]

```

#### 7. Create a Set Class
```
var log = console.log

class Set {
  constructor() {
    // Dictionary will hold the items of our set
    this.dictionary = [];
    this.length = 0;
  }

  // This method will check for the presence of an element and return true or false
  has(element) {
    return this.dictionary.indexOf(element) !== -1;
  }

  // This method will return all the values in the set as an array
  values() {
    return this.dictionary;
  }

  // change code below this line
  // write your add method here
  add(item){
    if(this.dictionary.indexOf(item)==-1){
   this.dictionary.push(item)
   this.length++
   return true
    }
   return false 
  }
  // write your remove method here
  remove(item){
    if(this.dictionary.indexOf(item) == -1){
      return false
    }else{
      this.dictionary=this.dictionary.filter(v => v != item)
      this.length--
      return true
    }
  }
  // write your size method here
    size(){
      return this.length
    }
  // change code above this line
}

var set = new Set()
set.add(1)
set.add(3)
set.remove(1)
log(set.has(3),set, set.size())
//true { dictionary: [ 3 ], length: 1 } 1
```

#### 8. Perform a Union on Two Sets
```
var log = console.log

class Set {
  constructor() {
    // This will hold the set
    this.dictionary = {};
    this.length = 0;
  }
  // this method will check for the presence of an element and return true or false
  has(element) {
    return this.dictionary[element] !== undefined;
  }
  // this method will return all the values in the set
  values() {
    return Object.keys(this.dictionary);
  }
  // this method will add an element to the set
  add(element) {
    if (!this.has(element)) {
      this.dictionary[element] = true;
      this.length++;
      return true;
    }
    return false;
  }
  // this method will remove an element from a set
  remove(element) {
    if (this.has(element)) {
      delete this.dictionary[element];
      this.length--;
      return true;
    }
    return false;
  }
  // this method will return the size of the set
  size() {
    return this.length;
  }
  union(set) {
    const newSet = new Set();
    this.values().forEach(value => {
      newSet.add(value);
    })
    set.values().forEach(value => {
      newSet.add(value);
    })
    return newSet;
  }
  // change code above this line
}

var setA = new Set()
setA.add("a")
setA.add("b")
setA.add("c")
var setB = new Set()
setB.add("c")
setB.add("d")
log(setA.union(setB).values())
//[ 'a', 'b', 'c', 'd' ]
```

#### 9. Perform an Intersection on Two Sets of Data
```
var log = console.log

class Set {
  constructor() {
    // This will hold the set
    this.dictionary = {};
    this.length = 0;
  }
  // this method will check for the presence of an element and return true or false
  has(element) {
    return this.dictionary[element] !== undefined;
  }
  // this method will return all the values in the set
  values() {
    return Object.keys(this.dictionary);
  }
  // this method will add an element to the set
  add(element) {
    if (!this.has(element)) {
      this.dictionary[element] = true;
      this.length++;
      return true;
    }

    return false;
  }
  // this method will remove an element from a set
  remove(element) {
    if (this.has(element)) {
      delete this.dictionary[element];
      this.length--;
      return true;
    }

    return false;
  }
  // this method will return the size of the set
  size() {
    return this.length;
  }
  // This is our union method from that lesson
  union(set) {
    const newSet = new Set();
    this.values().forEach(value => {
      newSet.add(value);
    })
    set.values().forEach(value => {
      newSet.add(value);
    })

    return newSet;
  }
  // change code below this line
  intersection(setB){
    var setC = new Set()
    this.values().forEach(i=>{
      setB.values().forEach(j=>{
        if(i==j){
          setC.add(i)
        }
      })
    })
    return setC
  }
  // change code above this line
}

var setA = new Set()
setA.add("a")
setA.add("b")
setA.add("c")
var setB = new Set()
setB.add("a")
setB.add("b")
setB.add("d")
setB.add("e")
log(setA.intersection(setB).values())
//[ 'a', 'b' ]
```

#### 10. Perform a Difference on Two Sets of Data
```
var log = console.log
class Set {
  constructor() {
    // This will hold the set
    this.dictionary = {};
    this.length = 0;
  }
  // this method will check for the presence of an element and return true or false
  has(element) {
    return this.dictionary[element] !== undefined;
  }
  // this method will return all the values in the set
  values() {
    return Object.keys(this.dictionary);
  }
  // this method will add an element to the set
  add(element) {
    if (!this.has(element)) {
      this.dictionary[element] = true;
      this.length++;
      return true;
    }
    return false;
  }
  // this method will remove an element from a set
  remove(element) {
    if (this.has(element)) {
      delete this.dictionary[element];
      this.length--;
      return true;
    }
    return false;
  }
  // this method will return the size of the set
  size() {
    return this.length;
  }
  // This is our union method from that lesson
  union(set) {
    const newSet = new Set();
    this.values().forEach(value => {
      newSet.add(value);
    })
    set.values().forEach(value => {
      newSet.add(value);
    })
    return newSet;
  }
  // This is our intersection method from that lesson
  intersection(set) {
    const newSet = new Set();
    let largeSet;
    let smallSet;
    if (this.dictionary.length > set.length) {
      largeSet = this;
      smallSet = set;
    } else {
      largeSet = set;
      smallSet = this;
    }
    smallSet.values().forEach(value => {
      if (largeSet.dictionary[value]) {
        newSet.add(value);
      }
    })
    return newSet;
  }
  // change code below this line
difference(setB){
  var setC = new Set()
this.values().forEach(i=>{
  var br = false
  setB.values().forEach(j=>{
    if(i == j){
      br = true
      return
    }
  })
  if(br == false){
    setC.add(i)
  }
})
  return setC
}  
  // change code above this line
}

var setA = new Set()
setA.add("a")
setA.add("b")
setA.add("c")
var setB = new Set()
setB.add("a")
setB.add("b")
setB.add("d")
setB.add("e")
log(setA.difference(setB).values())
//[ 'c' ]
```

#### 11. Perform a Subset Check on Two Sets of Data
```
isSubsetOf(setB){
//если длина массива одинаковых элементов равна длине подмассива  
  var res = false
  var count = this.length
  var c = 0
  this.values().forEach(i=>{
  var eq = false
  setB.values().forEach(j=>{
    if(i == j){
      eq = true
      c++
      return
    }
   })
  })
  if(c == count){
    res = true
  }
  return res
}
  // change code above this line
}
//['a','b'] isSubsetOf ['a','b','c','d'] true
```

#### 12. Create and Add to Sets in ES6
```
function checkSet() {
  var set = new Set([1, 2, 3, 3, 2, 1, 2, 3, 1]);
  // change code below this line
set.add('Taco')
set.add('Cat')
set.add('Awesome')
  // change code above this line
  console.log(Array.from(set));
  return set;
}
checkSet();
//[ 1, 2, 3, 'Taco', 'Cat', 'Awesome' ]
```

#### 13. Remove items from a set in ES6
```
function checkSet(){
   var set = new Set([1, 2, 3, 4, 5])//Create a set with values 1, 2, 3, 4, & 5
   set.delete(2)
   set.delete(5)
   //Remove the value 2
   //Remove the value 5
   //Return the set
   return set;
}
console.log(Array.from(checkSet())) 
//[ 1, 3, 4 ]
```

#### 14. Use .has and .size on an ES6 Set
```
function checkSet(arrToBeSet, checkValue){
   // change code below this line
var set = new Set(arrToBeSet);
var check = set.has(2)
return [check, set.size]
   // change code above this line
}

console.log(checkSet([ 1, 2, 3], 2)); // Should return [ true, 3 ]
```

#### 15. Use Spread and Notes for ES5 Set() Integration
```
function checkSet(set){
   // change code below this line
   var set = new Set(set)
   return Array.from(set)
   // change code above this line
}

console.log(checkSet([1,2,3]))
//[ 1, 2, 3 ]
```

#### 16. Create a Map Data Structure
```
var log = console.log
var Map = function() {
  this.collection = {}; 
  // change code below this line
  // change code above this line
  this.add = function(key, value){
    this.collection[key]=value
    return this.collection[key] 
    } 
  this.remove = function(key){
    if(this.collection[key] != undefined){
    //this.collection[key].delete()
    //Object.delete(this.collection[key])
    delete this.collection[key]
    }
  }
this.get = function(key){
  return this.collection[key]
}

this.has = function(key){
    if(this.collection[key]==undefined){
      return false
    }  
    return true
}
this.values = function(){
  var arr = []
  for(var v in this.collection){
    arr.push(this.collection[v])
  }
  //var arr = Object.entries(this.collection) 
  return arr
}
this.size = function(){
  return Object.entries(this.collection).length
}
this.clear = function(){
  this.collection={}
}
}; 

var map = new Map()
map.add('a','b')
map.add('c','d')
//map.remove('c')
//log(map.size())
//log(map.get('a'))
log(map.values())
//[ 'b', 'd' ]
```











#### 17. Create an ES6 JavaScript Map
```
// change code below this line

var myMap = new Map()
myMap.set('freeCodeCamp','Awesome!')
myMap.set('a', 2)
console.log(...myMap.values()) 
console.log(...myMap.entries()) 
console.log(...myMap.keys())
//Awesome! 2
//[ 'freeCodeCamp', 'Awesome!' ] [ 'a', 2 ]
//freeCodeCamp a
```

#### 18. Create a Hash Table

hasOwnProperty

[codepen.io Hash Tables](https://codepen.io/beaucarnes/pen/VbYGMb?editors=0012) 
[youtube Hash Tables - Beau teaches JavaScript](https://www.youtube.com/watch?v=F95z5Wxd9ks) 
[]() 
[]() 


add - key, val
 - индекса нет - добавляется пустой объкт
 - записываетс индекс, кей, валуе

remove - key
 - коллекция с индексом имеет ключ - удаляем ключ
 - при нулевой длине индекса, удаляем и ключ
 
lookup - key - null, val
 -  при наличие индекса - по ключу возвращаем вад
 - нет индекса - null

```
var log = console.log
var called = 0;
var hash = string => {
  called++;
  var hashed = 0;
  for (var i = 0; i < string.length; i++) {
    hashed += string.charCodeAt(i);
  }
  return hashed;
};
var HashTable = function() {
  this.collection = {};
  // change code below this line
 
  this.add = function(key, val){
    var index = hash(key)
    var collectIndex = this.collection[index] 
    if(this.collection[index] == undefined){
      this.collection[index] = {}
    }
    this.collection[index][key] = val 
  }
 
  this.remove = function(key, val){
  var index = hash(key)
  if(this.collection[index]!=undefined){
    if(this.collection[index][key]!=undefined){
      delete this.collection[index][key]
    }
    if(Object.keys(this.collection[index]).length == 0){
      delete this.collection[index]
    }
  }
}
  this.lookup = function(key){
    var index = hash(key)
    if(this.collection[index]!=undefined){
      if(this.collection[index][key]!=undefined){
        return this.collection[index][key]
      }
      return null
    }

    log(index, this.collection[index])
return null
  }
  
  // change code above this line
};

var ht = new HashTable()
ht.add('a','b')
// ht.add('a','bb') 
// ht.add('a','b')
// ht.add('a','bbb')  
//ht.remove('a','b')

log(ht.lookup('a'))
```

##### варианты
- index[ { a: 'bb' }, { a: 'bbb' } ]
- index{a: ['bb', 'bbb']}
- index{a:b}

```
00:00
a hash-table is used to implement
00:02
associative arrays or mappings of key
00:05
value pairs hash tables are a common way
00:08
to implement the map data structure or
00:10
objects they are widely used because of
00:13
how efficient they are the average time
00:15
for each lookup is not tied to the
00:17
number of elements stored in the table
00:19
in fact the average time complexity of
00:22
hash tables and big notation is o of 1
00:25
for a search insert and delete that's
00:28
very fast the way a hash table works is
00:32
that it takes a key input and then runs
00:35
it through a hash function a hash
00:37
function basically just Maps strings to
00:40
numbers and usually the numbers just
00:42
correspond to indexes in an array so for
00:45
example here are the strings we pass
00:48
through the hash function and then we
00:50
get the numbers over here a hash
00:52
function needs to be consistent so when
00:55
you run a key through the hash function
00:57
it always gives the same number and it
01:00
should map different words to different
01:02
numbers if two words get hashed to the
01:05
same number this is called a collision
01:08
you can see in this example John Smith
01:10
gets hashed to two Lisa Smith gets
01:13
hashed to what was either one Sam dofor
01:17
and then Sandra D also gets hashed to
01:19
two so this is a collision because both
01:21
these names once they run through the
01:23
hash function get turned into the same
01:26
number or the same index for the array
01:29
one way to handle collisions is just to
01:32
store both key value pairs at that index
01:34
then upon lookup of either you would
01:38
have to iterate through the bucket of
01:39
items to find the key you are looking
01:41
for this could take a little extra time
01:44
because of the iteration so here's
01:47
another example where it's showing that
01:48
the names are going through the hash
01:50
function and then it's showing basically
01:52
the information that's being stored in
01:55
the bucket so this would be the array
01:57
index and then in that array index or
02:00
the bucket we would store the phone
02:02
number so this would be like a phone
02:04
book the numerical value from the hash
02:07
function is then you
02:09
and the index to store that information
02:11
then if you try to access the same key
02:14
again the hashing function will process
02:16
the key and return the same numerical
02:18
result which will then be used to look
02:21
up the associate value which just means
02:23
that once you store all these things in
02:25
the array once you want to get the
02:28
number again you would just pass in the
02:31
key John Smith into the hash function it
02:33
would give you the exact same array
02:35
index too and then you would get the
02:37
information returned to you which is the
02:39
phone number
02:40
now you will probably never have to
02:42
implement hash tables yourself because
02:45
most languages including Java Script
02:47
already have them built-in in JavaScript
02:49
hash tables are usually used to
02:51
implement objects however it can be
02:53
helpful to see how they are implemented
02:55
just to gain a better understanding so
02:58
I'm going to show you the code for a
02:59
hash table so you can see how they work
03:02
first of all we have our hash function
03:04
where we're gonna pass in the string
03:07
that we want to hash and then the Max
03:09
Max is the number of buckets that we're
03:12
using in our hash table to store values
03:15
we're gonna start with hash being 0 and
03:18
we are going to for each character in
03:21
the string string that length for as
03:22
long as the string is we are going to
03:25
add the care code of each character each
03:30
string character has a numerical value
03:32
associated with it so basically we're
03:35
just adding up the character codes for
03:37
each character in the string and putting
03:39
into the hash now instead of returning
03:42
the hash we're gonna return hash modulus
03:45
maths that just means we are going to
03:48
divide by the number of buckets and then
03:51
return the remainder so if we had 5
03:54
buckets if we're divided by 5 the
03:57
remainder is either there going to be 0
03:58
1 2 3 or 4 and then that would be the
04:01
index that we're going to place the item
04:03
into the array now this is a very simple
04:06
hash function just for an example but
04:09
they can get much more complicated now
04:11
let's go into the hash table function so
04:15
in the hash table function we're gonna
04:16
have our storage array which is where
04:18
we're gonna store all that data we're
04:21
putting
04:21
to it and the storage limit now this is
04:24
the number of buckets in the array at
04:27
first I'm just gonna show you with just
04:28
four different buckets but normally
04:30
actually this number would be much
04:31
higher and this is just a utility
04:34
function just for this example so I can
04:37
easily print all the items in this
04:39
storage array I can easily log them so
04:42
here's where the real methods come in
04:43
for the hash table if we want to add
04:46
some information so first you're gonna
04:48
pass in a key and a value we're gonna
04:50
figure out the index of the array by
04:53
running it through the hash function so
04:55
we create this hash function where we're
04:57
gonna pass in the key and the storage
04:58
limit the number of buckets that we're
05:01
gonna have in our hash table and that's
05:04
going to return an index that we went
05:06
over before if there's nothing in that
05:09
index in the storage array if it's
05:11
undefined we're just going to set the
05:14
index to be this key value pair array
05:17
else if it's not undefined that means
05:20
there's already something in that bucket
05:22
so first we're gonna set insert it to
05:24
false and then we're gonna go through
05:26
each index to see if the key already
05:30
exists if the key already exists we're
05:33
gonna set the new value here and set
05:36
insert the true if the key does not
05:39
exist then insert is still gonna be
05:42
equal to false so we're going to push in
05:45
the new item that's where we'll get
05:47
multiple entries into one bucket so the
05:51
next thing is if we're going to remove
05:53
an item from the hash table so if we're
05:56
gonna remove you're just passing the key
05:58
of what you want to remove and now we're
06:00
gonna look up the index by passing it
06:02
into the hash function if the index that
06:05
length equals one that means there's
06:07
only going to be one item in that bucket
06:08
and the item in that bucket equals the
06:13
key that you passed in then you can just
06:16
delete that index you can just sleep
06:18
that item
06:18
but if it does not equal one that means
06:22
there's probably a few different items
06:24
at that index and we want to only delete
06:27
the item associated with that key so
06:30
we're going to go through each item in
06:32
that bucket or in the
06:33
next and if the key equals the key we
06:37
passed in then we can delete that item
06:39
the zero index is the key the one index
06:44
is the value so let's go how we would
06:47
look up an item again we're gonna set
06:49
the index using our hash function with
06:51
the key that we passed in and the
06:53
storage limit if the index there is
06:55
undefined we just return undefined it's
06:57
not the item is not in the hash table
07:00
else we're going to go through each
07:02
element in that bucket if the element
07:05
equals the key then we can return that
07:08
element so let's look at a few examples
07:10
first I'm going to show you an example
07:12
of the hash function here if we run that
07:15
for me three and every time I run that
07:17
you'll see in the console three three
07:19
three every time I put Bo it's gonna put
07:22
three but if I put a different name here
07:24
and I run that you can see on the
07:28
console it's gonna be five and now every
07:29
time I run that's gonna be five so with
07:31
this hash function it's going to always
07:33
be a number between zero and nine
07:35
because we're passing in ten as the
07:38
number of buckets so now let's actually
07:40
see the hash table so here we're gonna
07:44
create a new hash table called hte for a
07:47
hash table we're gonna add Bo who's a
07:49
person and find out it was a dog retsu
07:52
the dinosaur tux who's a penguin then
07:54
we're gonna look up tux and then we're
07:57
just gonna print the entire thing so
07:59
let's see what happens in the console so
08:02
we saw that tux is a penguin now let me
08:06
bring this over a little bit it's going
08:09
to show our entire half state well not
08:11
normally you're never gonna print out
08:13
the hash table like I did to the console
08:15
but I just did that just for learning
08:17
purposes if you remember up here we have
08:22
the storage limit set up for so we only
08:25
have four buckets the reason why I had
08:28
it set up for is so we'll see what it
08:30
looks like when there's a collision when
08:32
there's two things in one bucket just by
08:35
coincidence the first buck is undefined
08:37
that means none of these words hashed to
08:40
zero and then if we look at the second
08:44
bucket that's right here there's
08:45
actually two key value pairs
08:47
in the second bucket so both bow and tux
08:51
both gave one when it went through the
08:54
hash function and then you can see in
08:57
this bucket right here
08:59
we just have one item and then this
09:01
bucket right here we just have one item
09:03
so when we pass in Rex to the hash
09:05
function we got three returned but if we
09:07
go up here and we change the number of
09:10
buckets to something like 14 now I'm
09:14
gonna try running that again if you look
09:16
right here now there's a lot more
09:18
undefined because most of the buckets
09:20
are now empty but this bucket only has
09:22
one item that bug is one item and then
09:27
the last two bucks have one item and
09:28
there are no collisions now each bucket
09:31
only has one item now this has just been
09:34
a pretty simple example of a hash table
09:37
implementation but it's enough to give
09:39
you a basic idea of the hash table
09:41
thanks for watching my name is Bo Carnes
09:44
don't forget to subscribe and remember
09:47
use your code for good
Hash Tables - Beau teaches JavaScript
39 715 просмотров•15 апр. 2
```

#### 19. Work with Nodes in a Linked List
```
var log = console.log
var Node = function(element) {
  this.element = element;
  this.next = null;
};
var Kitten = new Node('Kitten');
var Puppy = new Node('Puppy');

Kitten.next = Puppy;
// only add code below this line
var Cat = new Node('Cat')
Puppy.next = Cat
var Dog = new Node('Dog')
Cat.next = Dog

// test your code
//console.log(Kitten.next);  
log(Kitten.next)
```

#### 20. Create a Linked List Class
```
var log = console.log
function LinkedList() {
  var length = 0;
  var head = null;

  var Node = function(element){
    this.element = element;
    this.next = null;
  };

  this.head = function(){
    return head;
  };

  this.size = function(){
    return length;
  };

  this.add = function(element){
    // Only change code below this line
var node = new Node(element)
var nodeVal = head
//log(nodeVal)
if(length==0){
  head = node
}else{
  for(var i=0;i<length;i++)
  {
    // log(i, nodeVal)
  if(nodeVal.next == null){
    nodeVal.next = node 
  }else{
    nodeVal = nodeVal.next
  }
  }
}
length++
    // Only change code above this line
  };
}

var ll = new LinkedList()
ll.add('a')
ll.add('b')
ll.add('c')
ll.add('d')
var node = ll.head()
for(var i=0;i<ll.size();i++){
    log(i, node.element, node.next!=null ? node.next.element:null)
  if(node!=null){
    node = node.next
  }
}
// 0 a b
// 1 b c
// 2 c d
// 3 d null
```







#### 21. Remove Elements from a Linked List
```
```

#### 22. Search within a Linked List
```
```

#### 23. Remove Elements from a Linked List by Index
```
```





































#### 24. Add Elements at a Specific Index in a Linked List
```
```
#### 25. Create a Doubly Linked List
```
```
#### 26. Reverse a Doubly Linked List
```
```
#### 27. Add a New Element to a Binary Search Tree
```
```
#### 28. Find the Minimum and Maximum Value in a Binary Search Tree
```
```
#### 29. Check if an Element is Present in a Binary Search Tree
```
```
#### 30. Check if Tree is Binary Search Tree
```
```
#### 31. Find the Minimum and Maximum Height of a Binary Search Tree
```
```
#### 32. Use Depth First Search in a Binary Search Tree
```
```
#### 33. Use Breadth First Search in a Binary Search Tree
```
```
#### 34. Delete a Leaf Node in a Binary Search Tree
```
```
#### 35. Delete a Node with One Child in a Binary Search Tree
```
```
#### 36. Delete a Node with Two Children in a Binary Search Tree
```
```
#### 37. Invert a Binary Tree
```
```
#### 38. Create a Trie Search Tree
```
```
#### 39. Insert an Element into a Max Heap
```
```
#### 40. Remove an Element from a Max Heap
```
```
#### 41. Implement Heap Sort with a Min Heap
```
```
#### 42. Adjacency List
```
```
#### 43. Adjacency Matrix
```
```
#### 44. Incidence Matrix
```
```
#### 45. Breadth-First Search
```
```
#### 46. Depth-First Search
```
```







[freecodecamp](https://www.freecodecamp.org/)  
[]()  
[]()  
[]()  
[]()  
[]()  
[]()  
[]()  

