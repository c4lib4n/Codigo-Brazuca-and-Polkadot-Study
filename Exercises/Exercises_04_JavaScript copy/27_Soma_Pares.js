let soma = 0;
function somaPares(lista){
    for(let i =0; i < lista.length; i++ ){
        if(lista[i] % 2 === 0){
            soma += lista[i];
        }
    }
    return soma;
}


const numeros = [2,3,4,6,7,8,9,20];

console.log(`Soma dos numeros pare: ${somaPares(numeros)}`);