/*

Verificador de paginda

function pag_verif(){
    if(location.href.includes("pag_root.html")){
        if(localStorage.getItem("tipo") !== "root"){
            location.href = "index.html"
        }
        else{}
    }

    else if(location.href.includes("pag_adm.html")){
        if(localStorage.getItem("tipo") !== "admin"){
            location.href = "index.html"
        }
        else{}
    }
    else if(location.href.includes("pag_client.html")){
        if(localStorage.getItem("tipo") !== "client"){
            location.href = "index.html"
        }
        else{}
    }
    else if(location.href.includes("script.js")){
        location.href = "index.html"
    }

    if(localStorage.getItem("id") !== 0){
        if(localStorage.getItem("tipo") === "root"){
            if(localStorage.getItem("nome") !== ""){
                if(location.href.includes("pag_root.html")){}
                else {
                    location.href = "pag_root.html"
                }
            }
            else {

                localStorage.setItem("id",0);
                localStorage.setItem("nome","");
                localStorage.setItem("tipo","");
                window.alert("Tentativa de burlar");
                location.href = "index.html";

            }
        }
        else if(localStorage.getItem("tipo") === "admim"){
            if(localStorage.getItem("nome") !== ""){
                if(location.href.includes("pag_adm.html")){}
                else {
                    location.href = "pag_adm.html"
                }
            }
            else {

                localStorage.setItem("id",0);
                localStorage.setItem("nome","");
                localStorage.setItem("tipo","");
                window.alert("Tentativa de burlar");
                location.href = "index.html";

            }
        }
        else if(localStorage.getItem("tipo") === "client"){
            if(localStorage.getItem("nome") !== ""){
                if(location.href.includes("pag_client.html")){}
                else {
                    location.href = "pag_client.html"
                }
            }
            else {

                localStorage.setItem("id",0);
                localStorage.setItem("nome","");
                localStorage.setItem("tipo","");
                window.alert("Tentativa de burlar");
                location.href = "index.html";

            }
        }
        else {}
    }

    else {}
}

pag_verif()

Desloga

function logout() {

    localStorage.setItem("id",0);
    localStorage.setItem("nome","");
    localStorage.setItem("tipo","");
    location.href = "index.html"

}

Faz as querys

async function query(qr) {

    var resp = await fetch("",{method:"POST",body:JSON.stringify({query:qr})});
    resp = resp.json();
    return resp;

}

confere o login e redireciona para a pagina

async function login() {

    var email = window.document.getElementById("email");
    var senha = window.document.getElementById("senha");
    if(email.value !== "" && senha !== ""){
        var r = await query(`query MyQuery { users(where: {email: {_eq: "${email.value}"}, senha: {_eq: "${senha.value}"}}) { id tipo nome }}`)
        if((r['data']['users']).length >= 1){
            if(r['data']['users'][0]['tipo'] == "root"){
                localStorage.setItem("id",r['data']['users'][0]['id']);
                localStorage.setItem("nome",r['data']['users'][0]['nome']);
                localStorage.setItem("tipo",r['data']['users'][0]['tipo']);
                window.location.href = "pag_root.html";
            }
            else if(r['data']['users'][0]['tipo'] == "admim") {
                localStorage.setItem("id",r['data']['users'][0]['id']);
                localStorage.setItem("nome",r['data']['users'][0]['nome']);
                localStorage.setItem("tipo",r['data']['users'][0]['tipo']);
                window.location.href = "pag_adm.html";
            }
            else if(r['data']['users'][0]['tipo'] == "client") {
                localStorage.setItem("id",r['data']['users'][0]['id']);
                localStorage.setItem("nome",r['data']['users'][0]['nome']);
                localStorage.setItem("tipo",r['data']['users'][0]['tipo']);
                window.location.href = "pag_client.html";
            }
            else {
                
                console.log("usuario invalido");
            }
        }
        else{
            window.alert("Login incorreto");
        }
    }
    else {
        window.alert("Prencha todos os campos");
    }
    

}

envia para a pagina de cadastro

function cadastrar() {

    location.href = "pag_cadastro.html";

}

*/