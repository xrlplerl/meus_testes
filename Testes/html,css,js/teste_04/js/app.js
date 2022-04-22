function desativa(ts){

    var input1 = window.document.getElementById(ts);
    var cont = input1.innerHTML.replace(">","");
    cont = cont + "disabled >";
    input1.innerHTML = cont;
    

}

function ativa(ts) {

    var input1 = window.document.getElementById(ts);
    var cont = input1.innerHTML;
    if(cont.includes("disabled")){
        cont = cont.replace('disabled="">',">")
        input1.innerHTML = cont;
    }

}

function buttons(ts) {

    if(ts === "bt1"){
        desativa("teste");
        desativa("teste2");
        ativa("teste3");
    }
    else if(ts === "bt2"){
        ativa("teste");
        ativa("teste2");
        desativa("teste3");
    }

}
