/**
 * Created by neon on 12/28/16.
 *
 // *

 **/

/**
function abs(x){
    if (x >=0){
        return x;
    }
    else{
        return -x;
    }
}


var abs = function (x) {

    if (typeof x !== 'number'){
        throw "Not a number";
    }


    if (x >= 0){
        return x;
    }
    else{
        return -x;
    }
};
 **/




function foo(x){
    alert(x);
    alert(arguments);
    for (var i=0; i< arguments.length; i++){
        alert(arguments[i]);
    }
}

foo(10, 20, 30);

































