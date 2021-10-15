// Ejecutar funcion en el evento click

document.getElementById('btn__open').addEventListener("click",open_close_menu)

// Declaramos variables

var side_menu = document.getElementById("menu__side")
var btn__open = document.getElementById("btn__open")
var body = document.getElementById("body")

// Evento para mostrar y ocultar el menu

function open_close_menu(){
    body.classList.toggle("body_move")
    side_menu.classList.toggle("menu_side_move")
}

//Si el ancho de la página es menor a 760px, ocultará el menú al recargar la página

if (window.innerWidth < 760){

    body.classList.add("body_move");
    side_menu.classList.add("menu_side_move");
}

//Haciendo el menú responsive(adaptable)

window.addEventListener("resize", function(){

    if (window.innerWidth > 760){

        body.classList.remove("body_move");
        side_menu.classList.remove("menu_side_move");
    }

    if (window.innerWidth < 760){

        body.classList.add("body_move");
        side_menu.classList.add("menu_side_move");
    }

});