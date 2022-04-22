export function desabilitar(item) {
    
    item.setAttribute("disabled","disabled");

}

export function habilitar(item) {
    
    item.removeAttribute("disabled","disabled")
}