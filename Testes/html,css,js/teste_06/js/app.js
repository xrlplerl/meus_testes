import {query} from "./scripts/query.js"
import {habilitar,desabilitar} from "./scripts/gen_attribut.js"

var intens = [];
var bt1 = window.document.getElementById("bt1")
bt1.addEventListener("click",add);

function attribut(a,nome){
    a.addEventListener("click",() => {remove(nome)})
}

function atualiza_table() {

    function center(text){
        return `<center>${text}</center>`;
    }

    var tabela = window.document.getElementById("tab");
    var cont = `<tr><td>${center("Nome")}</td><td>${center("Idade")}</td><td>${center("Profissão")}</td><td>${center("X")}</td></tr>`;

    for(var i of intens){
        cont = cont + `<tr><td>${center(i[0])}</td><td>${center(i[1])}</td><td>${center(i[2])}</td><td>${center('<button id="b'+ (intens.indexOf(i)) +'">Apagar</button>')}</td></tr>`;
    }
    tabela.innerHTML = cont;
    for(var i of intens){
        var id = "b" + intens.indexOf(i)
        attribut(window.document.getElementById(id),i[0])
    }

}


function add() {

    var inp1 = window.document.getElementById("nome");
    var inp2 = window.document.getElementById("idade");
    var inp3 = window.document.getElementById("prof");
    if(inp1.value !== "" && inp2.value !== "" && inp3.value !== ""){
        intens.push([inp1.value,inp2.value,inp3.value]);
    }
    inp1.value = ""
    inp2.value = ""
    inp3.value = ""
    atualiza_table();
    
}

function remove(nome) {

    var temp = []
    for(var i of intens){
        if(i[0] == nome){}
        else {
            temp.push(i)
        }
    }
    intens = temp;
    atualiza_table()

}

atualiza_table()