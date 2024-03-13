const cloud = document.getElementById("cloud");
const barraLateral = document.querySelector(".barra-lateral");
const spans = document.querySelectorAll("span");
const palanca = document.querySelector(".switch");
const circulo = document.querySelector(".circulo");
const menu = document.querySelector(".menu");
const main = document.querySelector("main");

menu.addEventListener("click",()=>{
    barraLateral.classList.toggle("max-barra-lateral");
    if(barraLateral.classList.contains("max-barra-lateral")){
        menu.children[0].style.display = "none";
        menu.children[1].style.display = "block";
    }
    else{
        menu.children[0].style.display = "block";
        menu.children[1].style.display = "none";
    }
    if(window.innerWidth<=320){
        barraLateral.classList.add("mini-barra-lateral");
        main.classList.add("min-main");
        spans.forEach((span)=>{
            span.classList.add("oculto");
        })
    }
});

palanca.addEventListener("click",()=>{
    let body = document.body;
    body.classList.toggle("dark-mode");
    body.classList.toggle("");
    circulo.classList.toggle("prendido");
});

cloud.addEventListener("click",()=>{
    barraLateral.classList.toggle("mini-barra-lateral");
    main.classList.toggle("min-main");
    spans.forEach((span)=>{
        span.classList.toggle("oculto");
    });
});

document.getElementById('menuUsuarios').addEventListener('click', function() {
    var seccionUsuarios = document.getElementById('usuarios');
    
    if (seccionUsuarios.style.display === 'none') {
        seccionUsuarios.style.display = 'block';
    } else {
        seccionUsuarios.style.display = 'none';
    }
});

function horaActual() {
    var elementoHora = document.getElementById("hora-actual");
    var fecha = new Date();
    var horas = fecha.getHours();
    var minutos = fecha.getMinutes();
    var segundos = fecha.getSeconds();
    var ampm = horas >= 12 ? "PM" : "AM";
    // Convierte las horas al formato de 12 horas
    if (horas > 12) {
      horas -= 12;
    } else if (horas === 0) {
      horas = 12;
    }

    // Formatea la hora, minutos y segundos para que siempre tengan dos dígitos
    if (horas < 10) horas = "0" + horas;
    if (minutos < 10) minutos = "0" + minutos;
    if (segundos < 10) segundos = "0" + segundos;

    var horaActual = horas + ":" + minutos + ":" + segundos + " " + ampm;
    elementoHora.innerHTML = horaActual;
  }
  // Actualiza la hora cada segundo
  setInterval(horaActual, 1000);
  // Llama a horaActual para mostrar la hora en formato de 12 horas inmediatamente
  horaActual();
  
  //Confirmación de eliminar 
  function confirmarEliminar() {
    // Muestra un cuadro de diálogo de confirmación
    var confirmacion = confirm("¿Estás seguro de que deseas eliminar este registro?");

    // Devuelve true si el usuario hace clic en "Aceptar", de lo contrario, devuelve false
    return confirmacion;

  }

//   Esta función se encarga de cargar el contenido de crudUsuarios

  function cargarContenido(url, contenedorId) {
    var xhttp = new XMLHttpRequest();
    // Evento onreadystatechange: Este evento se activa cada vez que cambia el estado de la solicitud. La función anónima asociada se ejecuta cuando el estado de la solicitud es 4 (solicitud completada) y el estado HTTP es 200 (OK).
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById(contenedorId).innerHTML = this.responseText;
        }
    };
    xhttp.open("GET", url, true);
    xhttp.send();
}


/** Alerta personalizadas */
function mensajeAlerta(msg, tipo_msg='') {
    let text  = document.querySelector('.text-2').textContent = `${msg}`;

    const toast    = document.querySelector(".toast");
        closeIcon  = document.querySelector(".close"),
        progress   = document.querySelector(".progress");


    toast.classList.add("active");
    progress.classList.add("active");

    setTimeout(() => {
        toast.classList.remove("active");
    }, 5000);

    closeIcon.addEventListener("click", () => {
        toast.classList.remove("active");
    });
}

function mostrarOcultarCampo() {
    var seleccion = document.getElementById("agregar").value;
    var campoDoc = document.getElementById("documento");

    if (seleccion === "Y") {
        campoDoc.style.display = "block";
    } else {
        campoDoc.style.display = "none";
    }
}

