export async function query(qr) {

    var resp = await fetch("",{method:"POST",body:JSON.stringify({query:qr})});
    resp = resp.json();
    return resp;

}