function binarySearch(sortedArray, num) {
    var found = false;
    var beginning = 0;
    var end = (sortedArray.length) - 1;
    while(beginning <= end && found === false){
        var middle = Math.floor((beginning + end) / 2);
        if(sortedArray[middle] === num) {
            found = true;
        } else if(sortedArray[middle] < num) {
            beginning = middle + 1
        } else {
            end = middle - 1
        }
    }
    return found;
}

function binarySearchIndex(sortedArray, num){
    var index = null;
    var beginning = 0;
    var end = (sortedArray.length) - 1;
    while(beginning <= end){
        var middle = Math.floor((beginning + end) / 2);
        if(sortedArray[middle] === num) {
            index = middle;
            break;
        } else if(sortedArray[middle] < num) {
            beginning = middle + 1;
        } else {
            end = middle - 1;
        }
    }
    return index;
}

var sortedArray = [1,3,7,9,13,15,24,56,89,99];
console.log(binarySearchIndex(sortedArray, 99));