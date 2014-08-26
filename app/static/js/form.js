function entroEnFoco(elemento) {
    
    elemento.className='enfoco';
    
    
}
function salioDeFoco(elemento) {
    
    elemento.className='';
    
}
function revisarObligatorio(elemento){
    var elementoLista = elemento.parentNode;
    var ayuda = document.getElementById("ayuda");
    if (ayuda !=undefined) {
        ayuda.parentNode.removeChild(ayuda);
        
    }
    
    if (elemento.value == "") {
        elemento.className='error';
        elementoLista.innerHTML+= "<p class='ayuda' id='ayuda'>Campo Obligatorio</p>"
        
        
    }else{
        elemento.className='';
        ayuda.parentNode.removeChild(ayuda);
        
    
    }
}
function validar() {
    
    var estaTodoOk = true;
    if (document.getElementById("nombre").value.length < 2) {
        estaTodoOk = false;
    }
    if (document.getElementById("direccion").value.length < 8) {
        estaTodoOk = false;
    }
    if (document.getElementById("numeroStaff").value!="") {
        if (isNaN(document.getElementById("numeroStaff").value)) {
            estaTodoOk = false;
        } 
    }
    var expresion = /^([a-zA-Z0-9_.-])+@(([a-zA-Z0-9-])+.)+([a-zA-Z0-9]{2,4})+$/;
    if (!expresion.test(document.getElementById("correo").value)) {
            estaTodoOK = false;	
    }
    if (document.getElementById("tipOrg").value=="") {
            estaTodoOK = false;
    }	
    if (!estaTodoOK) {
            alert("Algunos datos tienen errores, por favor corríjalos antes de volver a enviar");	
    }
    return estaTodoOk;
}