function temSubstring(frase, substring){
    return frase.includes(substring);
}

const frase = "Codigo Brazuca e Polkadot!!";
const substring = "Matheus";


console.log(`Existe substring? ${temSubstring(frase, substring)}`);