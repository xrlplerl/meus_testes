var itens = [];

function atualizar() {
    var table = window.document.getElementById("ta")
    var tb = "<tr><td>Nomes</td><td>Email's</td><td>Idades</td><td>Cargos</td></tr>"
    for (var i of itens) {
        tb = tb + `<tr><td>${i[0]}</td><td>${i[1]}</td><td>${i[2]}</td><td>${i[3]}</td></tr>`;
    }
    table.innerHTML = tb;
}

function add() {
    var nome = window.document.getElementById("nome");
    var email = window.document.getElementById("email");
    var idade = window.document.getElementById("idade");
    var cargo = window.document.getElementById("cargo");
    if (nome.value !== "" && email.value !== "" && idade.value !== "" && cargo.value !== "") {
        itens.push([nome.value, email.value, idade.value, cargo.value]);
    }
    nome.value = "";
    email.value = "";
    idade.value = "";
    cargo.value = "";
    atualizar();
}

function remove() {
    var email = window.document.getElementById("email");
    var inr = [];
    for (var i of itens) {
        if (i[1] === email.value) {
            email.value = "";
        } 
        else {
            inr.push(i);
        }
    }
    itens = inr;
    atualizar();
}
/*
Como ler json:

function carregar(json) {

    for(var l of json) {

        console.log(`[ ${l["titulo"]} ] ]===> Autor: ${l["autores"]} | Categoria: ${l["categoria"]} | Descrição: ${l["descricao"]}`)
    
    }
    
}

fetch("http://my-json-server.typicode.com/maujor/livros-json/livros").then(resposta => resposta.json()).then(json => carregar(json))

*/