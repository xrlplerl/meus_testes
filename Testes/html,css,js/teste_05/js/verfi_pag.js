export function pag_verif(){
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