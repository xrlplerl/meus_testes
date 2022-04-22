/*
Comandos:

- Para converter para inteiro Number.parseInt()
- Para converter para float Number.parseFloat()
- Para converção automatica de numero Number()
- Para coverter para string String() ou .toString()
- Para contar os caracteres .length
- Para converter os caracateres da string para maiusculas .toUpperCase()
- Para converter os caracateres da string para minusculas .toLowerCase()
- Para converter um valor numerico em monetario .toLocaleString("pt-br",{style:"currency",currency:BRL})
- Formar de seleção:
    window.document.getElementsByTagName("")
    window.document.getElementById("")
    window.document.getElementClassName("")
    window.document.getElementsByName("")
    window.document.querySelector("")----|
    window.document.querySelectorAll("")-|
                                         Nessas duas e utilizado o nome da tag, mais . para class ou # para id e o nome. Exemplo: window.document.querySelector("div#nome")
*/


var nome = String(window.prompt("Qual o seu nome:"));
var idade = Number(window.prompt("Qual a sua idade(anos):"));
var telefone = String(window.prompt("Qual o seu telefone:"));
var prof = String(window.prompt("Qual a sua profissão:"));
var comida = String(window.prompt("Qual a sua comida favorita:"));
var animal = String(window.prompt("Nome do seu animal de estimação:"));

document.write(`<div class="corpo_form" onmouseenter="entrar()" onmousemove="entrar()" onmouseout="sair()"><br><center><h1>Seus dados</h1></center><br><div class="campos"><h2 id="nome">Nome: ${nome}</h2><br><h2>Idade: ${idade}</h2><br><h2>Telefone: ${telefone}</h2><br><h2>Profissão: ${prof}</h2><br><h2>Comida favorita: ${comida}</h2><br><h2>Nome do animal de estimação: ${animal}</h2><br></div></div>`);
var corpo = window.document.querySelector("div.corpo_form");

function entrar() {

    corpo.style.background = "#000";
    corpo.style.color = "#fff";
}

function sair() {

    corpo.style.background = "#fff";
    corpo.style.color = "#000";

}

window.alert(window.document.getElementById("nome").innerText);