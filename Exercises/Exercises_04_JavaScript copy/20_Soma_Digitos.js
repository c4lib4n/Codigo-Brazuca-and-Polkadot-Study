let num1 = Math.floor(Math.random() * 999999) + 1;
let soma = 0;


var digitos = [];
while (num1 != 0) {
    digitos.push(num1 % 10);
    num1 = Math.trunc(num1 / 10);
}
digitos.reverse();
console.log(digitos);

for(let i = 0; i < digitos.length; i++){
    soma += digitos[i];
}


console.log(`Numero selecionado: ${num1} e a soma dele eh: `, soma);
