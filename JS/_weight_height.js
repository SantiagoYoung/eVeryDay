/**
 * Created by neon on 12/28/16.
 */


var arr = ['Apple', 'Google', 'Microsoft'];
var i, x;
for (i=0; i<arr.length; i++){
    x = arr[i];
    alert(x);
}


var x = 0;
fro (;;){
    if (x > 100){
        break;
    }
    x ++;
}

var o = {
    name: 'Jack',
    age: 20,
    city: 'Beijing',
};
for (var in o) {
    alert(key);
}


var o = {
    name:'jack',
    age:20,
    city:'beijing'
}
for (var key in o){
    if (o.hasOwnProperty(key)){
        alert(key);
    }
}


var a = ['A', 'B', 'C'];
for (var i in a){
    alert(i);
    aler(a[i]);
}


for (i in arr){
alert('hello,'+ arr[i]);}

var i = 0;
while(i < arr.length){
alert('hello,'+arr[i]);
i ++;}




for (var i in arr){
alert('hello,'+ arr(arr.length-i-1);}




var m = new Map([['michael', 95], ['bob', 75],['tracy', 85]]);
m.get('michael');

var m = new Map();
m.set('adam', 87);
m.set('bob', 234);

m.has('adam');
m.get('adam');
m.delete('adam');
m.get('adam');

var m = new Map();
m.set('Adam', 23);
m.set('Adam', 34);
m.get('Adam');


var s1 = new Set();
var s2 = new Set([1, 2, 3]);

var s = new Set([1, 2, 3, 3, '3']);
s;

s.add(4);
s;

s.delete(3);
s;


var a = ['A', 'B', 'C'];
var s = new Set(['A', 'B', 'C']);
var m = new Map([[1, 'x'], [2, 'y'], [3, 'z']]);

for (var x of a){
    alert(x);
}


var a = ['A', 'B', 'C'];

a.forEach(function (element, index, arrat){
    alert(element);
})

var s = new Set(['A', 'B', 'C']);
s.forEach(function (element, sameElement, set){
    alert(element);
})


var m = new Map([[1, 'x'], [2, 'y'], [3, 'z']]);
m.forEach(function (value, key, map){
    alert(value);
})

var a = ['A', 'B', 'C'];
m.forEach(function (element){
    alert(element);
})














