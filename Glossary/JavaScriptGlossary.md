



### Built-In JS Array Methods - Iteration Methods
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array

# .forEach() 
Will execute the same code for each element of an array. Execution only, no return value.
  * groceries.forEach(groceryItem => console.log(groceryItem)); 

# .map()
When .map() is called on an array, it takes an argument of a callback function and returns a new array with those elemets using the return statement. It performs a change or action to every element and return it to the new array, like .forEach but returning an array.
                const numbers = [1, 2, 3, 4, 5]; 

                const bigNumbers = numbers.map(number => {
                return number * 10;
                });
# .filter()
.filter() returns an array of elements after filtering out certain elements from the original array. The callback function for the .filter() method should return true or false depending on the element that is passed to it. The elements that cause the callback function to return true are added to the new array. 

                const words = ['chair', 'music', 'pillow', 'brick', 'pen', 'door']; 

                const shortWords = words.filter(word => {
                return word.length < 6;
                });
# .findIndex()
Calling .findIndex() on an array will return the index of the FIRST and only first element that evaluates to true in the callback function.

# .reduce()
The .reduce() method returns a single value after iterating through the elements of an array, thereby reducing the array.
                const numbers = [1, 2, 4, 10];

                const summedNums = numbers.reduce((accumulator, currentValue) => {
                return accumulator + currentValue
                }, 100)  // <- Second argument for .reduce() OPTIONAL
                console.log(summedNums) // Output: 17 // With optional arg Output: 117

Iteration	accumulator	currentValue	return value
First	        1	        2	            3
Second	        3	        4	            7
Third	        7	        10	            17
You can also set an initial value for the acumulator by adding a second parameter }, 100) 