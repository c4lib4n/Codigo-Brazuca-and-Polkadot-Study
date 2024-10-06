const num1 = Math.floor(Math.random() * 100);
const numero = num1;


function divisores(numero){
    let divisores = [];

    for(let i = 0; i <= num1; i++){
        if(num1 % i ==0 ){
            divisores.push(i);
        }
    }
    return divisores;
    
}



console.log(`Numero selecionado: ${numero}. Divisores: ${divisores(numero)}`);