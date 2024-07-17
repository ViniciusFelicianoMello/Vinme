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

// Formulario completar cadastro
document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector(".account_form");
    const profilePictureInput = document.getElementById("id_profile_picture");
    const firstNameInput = document.getElementById("id_first_name");
    const lastNameInput = document.getElementById("id_last_name");
    const birthDateInput = document.getElementById("id_birth_date");
    const nationalityInput = document.getElementById("id_nationality");
    const phoneNumberInput = document.getElementById("id_phone_number");
    const biographyInput = document.getElementById("id_biography");
    const messagesSpan = document.querySelector('.messages span');

    const validateName = (name) => {
        const namePattern = /^[A-Za-z]{2,}$/;
        return namePattern.test(name);
    };

    const formatName = (name) => {
        return name.charAt(0).toUpperCase() + name.slice(1).toLowerCase();
    };

    const validateBirthDate = (date) => {
        const selectedDate = new Date(date);
        const today = new Date();
        return selectedDate <= today;
    };

    const validatePhoneNumber = (phoneNumber) => {
        const phonePattern = /^\d{10,11}$/;
        return phonePattern.test(phoneNumber);
    };

    const validateBiography = (biography) => {
        return biography.length <= 150;
    };

    const validateProfilePicture = (file) => {
        const allowedTypes = ['image/jpeg', 'image/jpg', 'image/png'];
        const maxSize = 2 * 1024 * 1024; // 2MB

        if (file) {
            if (!allowedTypes.includes(file.type)) {
                messagesSpan.textContent = 'A imagem deve ser do tipo jpg, jpeg ou png.';
                return false;
            }

            if (file.size > maxSize) {
                messagesSpan.textContent = 'A imagem não pode ter mais de 2MB.';
                return false;
            }
        }

        return true;
    };

    form.addEventListener('submit', function (event) {
        const firstNameValue = firstNameInput.value.trim();
        const lastNameValue = lastNameInput.value.trim();
        const birthDateValue = birthDateInput.value.trim();
        const nationalityValue = nationalityInput.value.trim();
        const phoneNumberValue = phoneNumberInput.value.trim();
        const biographyValue = biographyInput.value.trim();
        const profilePictureFile = profilePictureInput.files[0];

        if (!validateName(firstNameValue)) {
            event.preventDefault();
            messagesSpan.textContent = 'O campo Nome deve ter pelo menos 2 letras e não pode conter espaços, caracteres especiais ou números.';
        } else {
            firstNameInput.value = formatName(firstNameValue);
        }

        if (!validateName(lastNameValue)) {
            event.preventDefault();
            messagesSpan.textContent = 'O campo Sobrenome deve ter pelo menos 2 letras e não pode conter espaços, caracteres especiais ou números.';
        } else {
            lastNameInput.value = formatName(lastNameValue);
        }

        if (birthDateValue === '' || !validateBirthDate(birthDateValue)) {
            event.preventDefault();
            messagesSpan.textContent = 'O campo Data de Nascimento não pode ser uma data futura.';
        }

        if (!validateName(nationalityValue)) {
            event.preventDefault();
            messagesSpan.textContent = 'O campo Nacionalidade deve ter pelo menos 2 letras.';
        } else {
            nationalityInput.value = formatName(nationalityValue);
        }

        if (!validatePhoneNumber(phoneNumberValue)) {
            event.preventDefault();
            messagesSpan.textContent = 'O campo Telefone deve conter entre 10 e 11 dígitos e não pode conter espaços, letras ou caracteres especiais.';
        }

        if (!validateBiography(biographyValue)) {
            event.preventDefault();
            messagesSpan.textContent = 'O campo Biografia não pode ter mais de 150 caracteres.';
        }

        if (!validateProfilePicture(profilePictureFile)) {
            event.preventDefault();
        }
    });
});