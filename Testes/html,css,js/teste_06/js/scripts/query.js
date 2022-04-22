export async function query(qr) {

    var result = await fetch("",{method:"POST",body:JSON.stringify({query:qr})});
    return result.json();

}