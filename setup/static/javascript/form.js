// senha para texto
function togglePassword(element) {
    const passwordField = element.closest('.account_control').querySelector('input[type="password"], input[type="text"]');
    
    if (passwordField.type === 'password') {
        passwordField.type = 'text';
        element.classList.remove('fa-eye-slash');
        element.classList.add('fa-eye');
    } else {
        passwordField.type = 'password';
        element.classList.remove('fa-eye');
        element.classList.add('fa-eye-slash');
    }
}

// validações de senha
// senhas iguais e força
function validatePassword() {
    var password1 = document.getElementById("password1").value;
    var password2 = document.getElementById("password2").value;
    var mismatchMessage = document.getElementById("passwordMismatch");

    var lengthMessage = document.getElementById("passwordLengthMessage");
    var lowercaseMessage = document.getElementById("passwordLowercaseMessage");
    var uppercaseMessage = document.getElementById("passwordUppercaseMessage");
    var numberMessage = document.getElementById("passwordNumberMessage");
    var specialCharMessage = document.getElementById("passwordSpecialCharMessage");

    var valid = true;

     // Verifica se as senhas coincidem
     if (password1 !== password2) {
        mismatchMessage.style.display = "block";
        valid = false;
    } else {
        mismatchMessage.style.display = "none";
    }

    // Verifica o comprimento mínimo
    if (password1.length < 8) {
        lengthMessage.style.display = "block";
        valid = false;
    } else {
        lengthMessage.style.display = "none";
    }

    // Verifica letras minúsculas
    if (!/[a-z]/.test(password1)) {
        lowercaseMessage.style.display = "block";
        valid = false;
    } else {
        lowercaseMessage.style.display = "none";
    }

    // Verifica letras maiúsculas
    if (!/[A-Z]/.test(password1)) {
        uppercaseMessage.style.display = "block";
        valid = false;
    } else {
        uppercaseMessage.style.display = "none";
    }

    // Verifica números
    if (!/\d/.test(password1)) {
        numberMessage.style.display = "block";
        valid = false;
    } else {
        numberMessage.style.display = "none";
    }

    // Verifica caracteres especiais
    if (!/[!@#$%^&*()_+}{":;?/>.<,]/.test(password1)) {
        specialCharMessage.style.display = "block";
        valid = false;
    } else {
        specialCharMessage.style.display = "none";
    }

    return valid;
}
