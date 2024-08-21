programa {
  funcao inicio() {
    inteiro numero, contador = 0

    para(inteiro i =0; i <= 5; i++){
      escreva("Digite o numero: ", i, " : ")
      leia(numero)

      se(numero % 2 == 0){
        contador++
      }
    }

    escreva("Voce digitou: ", contador, " numeros positivos.")

  }
}
