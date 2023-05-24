document.addEventListener("DOMContentLoaded", function() {
    let secret_code = document.getElementById("secret_code_input");

    secret_code.addEventListener('input', function (e){
        e.preventDefault();
        let value = this.value;
        if (value.length >= 4) {
            this.value = value.slice(0,4);
            document.getElementById('email_verification_form').submit();
        }
    });
});
