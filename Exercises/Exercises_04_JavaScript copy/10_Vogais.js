const string = "Codigo Brazuca e Polkadot!";
const vogais = "aeiouAEIOU";
let cont = 0;

for(let i =0; i < string.length; i++){
    if(vogais.includes(string[i])){
        cont++;
    }
}

console.log("Quantidades de fogais na frase: ", cont);


