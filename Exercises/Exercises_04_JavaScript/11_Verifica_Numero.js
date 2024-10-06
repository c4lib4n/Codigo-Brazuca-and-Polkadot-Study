const numeros = [];
numeros.push(4,5,3,44,55,234,12,12,45,656,);
const escolhido = 999;
let existe = 0;
let naoExiste = 0;

for(let i = 0; i < numeros.length; i++){
    if(escolhido == numeros[i]){
        existe = 1;
    }else{
        naoExiste = 1;
    }
}

if(existe == naoExiste){
    console.log("Numero existe na lista");
}else{
    console.log("Nao existe na lista");
}