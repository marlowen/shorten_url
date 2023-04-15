/*..............................................................................................
... PARA VALIDAR LOS DATOS .....................................................
.............................................................................................*/
var csrftoken = $.cookie('csrftoken');
function csrfSafeMethod(method){
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
/*..............................................................................................
... TODOS LOS CURSOS .............................................................
............................................................................................. */


/*$('#boton1').click(function(){
var valor;
valor = document.getElementById("urloriginal").value;//obtener valor del input
console.log("hola");
console.log(valor);
respuesta(valor) //declarar valor a la variable a usar en el ajax
});*/


function respuesta(valor){
    $.ajax({
        beforeSend : function(xhr, settings){
			if(!csrfSafeMethod(settings.type) && !this.crossDomain){
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		},
		url : "/cortar_url_ajax/",
		type : "GET",
		data : { valor : valor,},
		success : function(json){
            $("#urloriginal2").val(json[0].url_cortado);
		},
		error : function(xhr, errmsg, err){
			console.log('Error en carga de respuesta');
		},
    });
}