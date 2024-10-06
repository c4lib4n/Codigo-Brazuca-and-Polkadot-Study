const Cambio = {
    usd: 4.17,
    eur: 3.76,
};

let qdtTransacoes = 0;

let transacoesFeitas = [];

document.getElementById('calcular').addEventListener('click',function(){
    let valorTransacao = parseFloat(document.getElementById('valor-transacao').value);
    let complexidade = document.getElementById('complexidade').value;
    let precoGas;

    switch(complexidade){
        case 'baixa':
            precoGas = 0.01;
            break;
        case 'media':
            precoGas = 0.05;
            break;
        case 'alta':
            precoGas = 0.1;
            break;
        
    }

    let custoGas = valorTransacao * precoGas;
    let moedaFiat = document.getElementById('moeda-fiat').value; 
    let valorGasConvertido; 


    if(valorTransacao > 0){

        if(moedaFiat == 'dot'){
            valorGasConvertido = custoGas;
        }else if(moedaFiat == 'eur'){
            valorGasConvertido = custoGas * Cambio[moedaFiat];
        }else{
            valorGasConvertido = custoGas * Cambio[moedaFiat];
        }

        qdtTransacoes++;
        document.getElementById('contador').innerHTML = `Número de Transações Simuladas: ${qdtTransacoes}`
        
        document.getElementById('resultado').innerHTML = `
        <p>Valor da Transação: ${valorTransacao} DOT</p>
        <p>Complexidade: ${complexidade.charAt(0).toUpperCase() + complexidade.slice(1)}</p>
        <p>Custo Estimado do Gas: ${custoGas.toFixed(2)} DOT (${valorGasConvertido.toFixed(2)} ${moedaFiat.toUpperCase()})</p>`
        setTimeout(function(){
            document.getElementById('valor-transacao').focus(); 
        },0);
        document.getElementById('valor-transacao').value = '';
    } else {
        document.getElementById('resultado').innerHTML = '<p style="color:red;">Insira um valor de transação válido. Maior que zero</p>';
        setTimeout(function(){
            document.getElementById('valor-transacao').focus();
        },0);
    }
});


