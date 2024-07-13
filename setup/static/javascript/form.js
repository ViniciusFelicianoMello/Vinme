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

// remember me
document.querySelector('.checkbox_box').addEventListener('change', function() {
    const label = this.nextElementSibling;
    if (this.checked) {
        label.classList.add('checked');
    } else {
        label.classList.remove('checked');
    }
});