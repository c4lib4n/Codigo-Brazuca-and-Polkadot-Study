function primo(num){
    let divisores =0;
    for(let i = 1; i <= num; i++){
        if(num % i == 0){
            divisores++;
        }
    } 
    
    if(divisores == 2){
        return true;
    }else{
        return false;
    }
}

const num = 47;
const resultado = primo(num);

console.log(resultado);



