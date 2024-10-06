let resultado = 1;
function multiplicao(lista){
    for(let i = 0; i < lista.length; i++){
        resultado *= lista[i];
    }
    return resultado;
}


const lista = [2,3,4];

console.log(`Multiplicacao da lista: ${multiplicao(lista)}`);