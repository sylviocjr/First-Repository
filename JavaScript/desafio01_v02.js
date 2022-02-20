// 07 jan. 2022 //
// Incorporado o uso de template strings, que permitem o uso de mensagens com variáveis. //
// Adicionada rotina para o evento de a soma resultar igual a 10 ou igual a 20, casos não previstos no desafio dado. //

console.log("\nPrimeiros códigos em JS. Entrar com dois números e verificar sua soma, informando ainda se é menor ou maior que 10 e menor ou maior que 20.")
console.log("\nAdicionada rotina para o evento de a soma resultar igual a 10 ou igual a 20, casos não previstos no desafio dado.")
console.log("\nSylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil.\n\n")

function somaNumeros(x,y)
{
    const soma = x + y;
    let saoIguais = 'são';
    let compara10 = 'maior que';
    let compara20 = 'maior que';
        if (x != y)
        {
            saoIguais = 'não são';
        }

        if (soma < 10)
        {
            compara10 = 'menor que'
        }

        if (soma === 10)
        {
            compara10 = 'igual a'
        }

        if (soma < 20)
        {
            compara20 = 'menor que'
        }

        if (soma === 20)
        {
            compara20 = 'igual a'
        }
    /* Uso de Template Strings a seguir ... */
    console.log(`Os números ${x} e ${y} ${saoIguais} iguais. Sua soma é ${soma}, que é ${compara10} 10 e ${compara20} 20.`);
}

var soma;
let n1 = 5;  // Opção de aqui informar os números a serem repassados à função //
let n2 = 4;  // Opção de aqui informar os números a serem repassados à função //

/* A seguir, diversas chamadas à função, a título de exemplos ... */
soma = somaNumeros(n1,n2);  
soma = somaNumeros(5,5);
soma = somaNumeros(5,15);
soma = somaNumeros(10,11);