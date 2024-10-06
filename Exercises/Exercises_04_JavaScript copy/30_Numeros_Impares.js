let cont = 0;
function impares(lista){
    for(let i = 0; i < lista.length; i++){
        if(lista[i] % 2 !== 0){
            cont++;
        }  
    }
    return cont;
}

const numeros = [3,4,5,6,7];

console.log(`Quantidade de numeros impares na lista: ${impares(numeros)}`);