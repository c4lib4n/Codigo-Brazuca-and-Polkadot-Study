const number = 10;
let num1 = 0;
let num2 = 1;
let nextTerm;

console.log('Fibonacci Series:');

for (let i = 1; i <= number; i++) {
    nextTerm = num1 + num2;
    num1 = num2;
    num2 = nextTerm;
}

console.log(num1);