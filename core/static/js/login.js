const email = document.getElementById("username")
const password = document.getElementById("password")
const form = document.getElementById("form")
const warnings = document.getElementById("warnings")

form.addEventListener("submit", e=>{
    e.preventDefault()
    let warnings = ""
    let entrar = false
    let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/
    if(email.value.length <12){
        warnings += `El email no es valido <br>`
        entrar = true
    }
    if(password.value <8){
        warnings += `La contrasena no es valida <br>`
        entrar = true
    }

})

document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault(); // Evitar la redirección por defecto
  
    // Obtener los valores de usuario y contraseña
    var username = document.querySelector('input[name="PanConQueso"]').value;
    var password = document.querySelector('input[name="pan123456"]').value;
  
    // Realizar la validación (aquí debes implementar tu lógica de validación)
    if (username === 'PanConQueso' && password === 'pan123456') {
      // Enviar el formulario si los datos son correctos
      this.submit();
    } else {
      // Mostrar un mensaje de error o realizar otra acción
      alert('Usuario o contraseña incorrectos');
    }
  });
  