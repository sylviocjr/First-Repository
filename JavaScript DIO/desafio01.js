
// Dúvida ... como exibir todas as mensagens correspondentes numa só linha/string, conforme solicitado no desafio. //

// Incorporado o uso de template strings, que permitem o uso do 'alert' com variáveis. //

alert("Primeiro desafio do curso de JS. Entrar com dois números e verificar sua soma, informando ainda se é menor ou maior que 10 e menor ou maior que 20.")
alert("Entrar com dois números e verificar sua soma, informando ainda se é menor ou maior que 10 e menor ou maior que 20.")
alert("Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil")


function somaNumeros(x,y)
{
    prompt("A soma dos números é:", x+y)
    
    if (x === y)
    {
        console.log("Os números", x, "e", y, "são iguais.");
        alert(`Os números ${x} e ${y} são iguais.`);   // Uso de template strings //
    }
    else
    {
        console.log("Os números", x, "e", y, "NÂO são iguais");
        alert(`Os números ${x} e ${y} NÃO são iguais.`)   // Uso de template strings //
    }
    console.log("Sua soma é ", x+y);
    alert(`Sua soma é ${x+y}`)   // Uso de template strings //
    
    if ((x+y) < 10)
    {
        console.log("que é menor que 10 e");
    }
    if ((x+y) > 10)
    {
        console.log("que é maior que 10 e");
    }

    if ((x+y) < 20)
    {
        console.log("menor que 20.");
    }
    
    if ((x+y) > 20)
    {
        console.log("maior que 20.");
    }
    return(x+y);
}

var soma;

n1 = Number(prompt("Informe o primeiro número: "));
prompt("Você digitou", n1);
console.log("Você digitou", n1)

n2 = Number(prompt("Informe o segundo número: "));
prompt("Você digitou", n2);
console.log("Você digitou", n2)

soma = somaNumeros(n1,n2);
console.log("A soma dos números é:", soma)