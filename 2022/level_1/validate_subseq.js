/**
 * 
What is validate subsequence?
    Given two non-empty arrays of integers, write a function that determines whether 
    the second array is a subsequence of the first one. 
    A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array
    but that are in the same order as they appear in the array.
*/


function validateSubSeq_b(numbers,sequence){

    let seqIndx = 0;
    
    for (let value in numbers) {

        if(seqIndx == sequence.length) {
            return true; // stop early
        }

        if(numbers[value] == sequence[seqIndx]) {
            seqIndx++;
        }

    }

    return (sequence.length == seqIndx) ? true : false; 
}

// O(n) Time | O(1) Space
function validateSubSeq(numbers,sequence){

    let l = 0, r = 0;

    // stops when we reach the end of sequence
    // but will continue if no match is found
    while( l < numbers.length && r < sequence.length ){

        if(numbers[l] == sequence[r]) {
            r += 1;
        }
        l += 1
        
    }
    
    return (r == sequence.length)? true : false;

}

var rs = validateSubSeq_b(
    [5,1,22,25,6,-1,8,10,11,7]
    ,[1,6,-1,10]);

if(rs){
    console.log("Found");
}else{
    console.log("Not found");
}

console.log("finished...");