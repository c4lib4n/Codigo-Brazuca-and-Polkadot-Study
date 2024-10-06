function palindrome(palavra){
    let inverter = palavra.split("").reverse().join("");
    return palavra === inverter;
}


console.log(palindrome("ama"));

