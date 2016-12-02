/**
 * Created by neon on 11/25/16.
 */


不同的数据，需要不同的数据类型。

Number
js 不区分整数和浮点数， 统一用Number表示：
    123;
    0.123;
    1.23e3;
    -99;
    NaN;
    Infinity;
Number 可以直接做四则运算：
    1 + 2; // 3
    (1 + 2) * 5 / 2; // 7.5
    2 / 0; // Infinity
    0 / 0; // NaN
    10 % 3; // 1
    10.5 % 3; // 1.5

字符串
    ''或""本身只是一种表示方式，不是字符串的一部分，因此，字符串'abc'只有a，b，c这3个字符。

布尔值
    true ； false；

    true && true;
    true && false;
    false && true || false;

    false || false;
    true || false;
    false || true || false;

    ! true;
    ! false;
    ! (2 < 5);


var age = 12;
if (age >= 18){
    alert('adult');
}
else{
    alert('teenager');
}


比较运算符

 2 > 5; false
 5 >= 2; true
 7 == 7; true

false == 0; true
false === 0; false


要特别注意相等运算符==。JavaScript在设计时，有两种比较运算符：

第一种是==比较，它会自动转换数据类型再比较，很多时候，会得到非常诡异的结果；

第二种是===比较，它不会自动转换数据类型，如果数据类型不一致，返回false，如果一致，再比较。

由于JavaScript这个设计缺陷，不要使用==比较，始终坚持使用===比较。

另一个例外是NaN这个特殊的Number与所有其他值都不相等，包括它自己：

NaN === NaN; //false

isNaN(NaN); // true

1 / 3 === (1 - 2 / 3); //false
浮点数在运算过程中会产生误差，因为计算机无法精确表示无限循环小数。

null 和 undefined

// null 表示一个‘空’值， 它和0以及空字符串‘’不同
// 0 是一个数值， ‘’表示长度为0的字符串，
// 而null表示空。


// 在JavaScript中，还有一个和null类似的undefined，它表示“未定义”。
//
//
// 大多数情况下，我们都应该用null。
// undefined仅仅在判断函数参数是否传递的情况下有用。



// 数组
// 数组是一组按顺序排列的集合，集合的每个值称为元素。
[1, 2, 3.14, 'hello', null, true, undefined]

// 数组用[]表示，元素之间用分隔。

// 通过Array()函数实现数组
new Array(1, 2, 3); // [1, 2, 3]


// 然而，出于代码的可读性考虑，强烈建议直接使用[]。

// 数组的元素可以通过索引来访问。请注意，索引的起始值为0：

var arr = [1, 2, 3.14, 'Hello', null, true];
arr[0]; // 返回索引为0的元素，即1
arr[5]; // 返回索引为5的元素，即true
arr[6]; // 索引超出了范围，返回undefined



对象
JavaScript的对象是一组由键-值组成的无序集合：
var person ={
    name : 'bob',
    age : 2,
    tags : ['js', 'web'],
    city: 'beijing',
};
// Js 的对象的键都是字符串类型的， 值可以是任意数据类型。
// 每个键又称为对象的属性。
// 要获取一个对象的属性，使用

// 对象变量.属性名 的方式获取
person.age;
person.name;


// 变量/

// 变量名是大小写英文、数字、$和_的组合，且不能用数字开头。
// 变量名也不能是JavaScript的关键字
申明一个变量用 var 语句
 var a;
var $b = 1;
var s_007 = '007';
var answer = true;
var t = null;

// 在JavaScript中，使用等号=对变量进行赋值。

// 只能用var申明一次
var a = 123; // a 的值是整数123
a = 'ABC';  // a 变为字符串


strict模式

// 如果一个变量没有通过var申明就被使用，那么该变量就自动被申明为全局变量：
i = 10; // i 现在是全局变量。

启用strict模式的方法是在JavaScript代码的第一行写上：
'use strict';




















































