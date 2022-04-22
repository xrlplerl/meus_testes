import { loginout,login,cadastro } from "./login.js";
export function pag_home(){

    var bt1 = window.document.getElementById("bt1");
    var bt2 = window.document.getElementById("bt2");
    bt1.addEventListener("click",login);
    bt2.addEventListener("click",cadastro);

}

export function pag_root(){

    var bt3 = window.document.getElementById("bt3");
    bt3.addEventListener("click",loginout);

}