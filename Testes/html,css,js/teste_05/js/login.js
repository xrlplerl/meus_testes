import {query} from "./query.js"
export function loginout() {

    localStorage.setItem("id",0);
    localStorage.setItem("nome","");
    localStorage.setItem("tipo","");
    location.href = "index.html";

}

export async function login() {

    var email = window.document.getElementById("email");
    var senha = window.document.getElementById("senha");
    if(email.value !== "" && senha.value !== ""){
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

export function cadastro() {

    location.href = "pag_cadastro.html";

}