programa {
  funcao inicio() {
    inteiro ano
    escreva("Digite o ano: ")
    leia(ano)
    se(ano % 4 == 0){
      se(ano % 100 == 0){
        se(ano % 400 == 0){
          escreva("O ano e bissexto")
        }senao{
          escreva("O ano nao e bissexto")
        }
      }senao{
        escreva("O ano e bissexto")
      }
    }senao{
      escreva("O ano nao e bissexto")
    }
  }
}
