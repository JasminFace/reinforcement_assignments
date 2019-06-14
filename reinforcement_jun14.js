list = ["Totam", "ut", "odit","quis", "Maiores", "unde", "EX", "EST", "corporis"]

function words(word) {
    list.forEach(function(word) {
        if (word == word.toLowerCase() && word.length > 4) {
            console.log('long and lowercase');
        } else if (word.length > 4)  {
            console.log('long');
        } else if (word == word.toLowerCase()) {
            console.log('lowercase');
        } else {
            console.log(word);
        }
    });
}

words()