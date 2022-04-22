import {pag_verif} from "./verfi_pag.js"
import {pag_home,pag_root} from "./buttons.js"
import {apagar_elemento} from "./ap_list.js"

pag_verif();

if(apagar_elemento(location.href.split("/"),"").length == 3 || location.href.includes("index.html")){
    pag_home();
}
else if(location.href.includes("pag_root.html")){
    pag_root()
}