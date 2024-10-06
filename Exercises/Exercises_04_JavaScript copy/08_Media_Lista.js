const numeros = [];
let soma = 0;
numeros.push(2,3,10);

for(let i =0; i < numeros.length; i++){
    soma += numeros[i];
}

media = soma / numeros.length;

console.log("Media: ", media)