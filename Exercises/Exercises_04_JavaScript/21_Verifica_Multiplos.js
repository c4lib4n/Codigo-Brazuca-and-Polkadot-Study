function multiplo (num1, num2){
    if(num1 % num2 == 0){
        return true;
    }else{
        return false;
    }
}


const num1 = Math.floor(Math.random() * 100) + 1;
const num2 = Math.floor(Math.random() * 100) + 1;

console.log(`Numero 1: ${num1} Numero 2: ${num2} ---- `, multiplo(num1, num2));
