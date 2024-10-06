const string = "Codigo Brazuca e Polkadot sao os melhores do MUNDO!!";
const letra = "o";
let cont = 0;
for(let i = 0; i < string.length; i++){
    if(letra.includes(string[i])){
        cont++;
    }
}

console.log(`A letra ${letra} aparece: ${cont} na frase ${string}`);