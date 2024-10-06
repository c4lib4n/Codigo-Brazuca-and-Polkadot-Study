function listaCrescente(lista){
    for(let i = 0; i < lista.length; i++){
        if(lista[i] > lista[i + 1]){
            return false;
        }
    }
    return true;
    
}

const numeros = [1,2,3,4,10,8];

console.log(`Lista em order crescente? ${listaCrescente(numeros)}`);

