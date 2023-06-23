const email = document.getElementById("email")
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