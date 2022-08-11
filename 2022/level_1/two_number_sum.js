let sample_numbers = [1,4,2,10,7,'-4','23'];
let sample_target = 33;

function convertToNumber(numbers){
    return numbers.map(i => Number(i))
}

function sortNumbers(numbers) {
    return numbers.sort((a, b) => a - b);
}

// O(nlogn) time | O(1) space

function sumOfTwoNumbers_b(target, numbers){

    numbers = sortNumbers(numbers);
    
    let l = 0, r = numbers.length - 1;

    while( l < r) {

        var total = numbers[l] + numbers[r];

        if(total == target) {
            return [ numbers[l], numbers[r] ];
        }

        // if total is too large then imcrease from the left (l += 1) and 
        // if it is too small then decrease from the right ( r -= 1)

        if( total < target) {
            l += 1;
        }else if( total > target) {
            r -= 1;
        }

    }
    return [];
}

// O(n) time |  O(n) space
function sumOfTwoNumbers(target,numbers){

    let result = [] ;

    let prev_map = {};

    for (let i = 0; i < numbers.length; i++) {

        var el = numbers[i];

        var diff = target - el;

        if( diff in prev_map){

            result[0] = el, result[1] = diff;
            
            break;
        }

        prev_map[el] = diff;

    }
    console.log("//-->",prev_map)


    return result;
}

function main(){

    var target = Number(sample_target);

    var numbers =  convertToNumber(sample_numbers);

    // return sumOfTwoNumbers(target, numbers);

    return sumOfTwoNumbers_b(target, numbers);


}

var sumResult = main(sample_target,sample_numbers);

if(sumResult.length == 2){
    console.log("Sum of two numbers: ",sumResult[0], sumResult[1] )
}else{
    console.log("Couldnot find two number sum.")
}

console.log("finished...");