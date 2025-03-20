/* jshint esversion: 11, jquery: true */
const spinnerButtons = document.getElementsByClassName('btn-with-spinner');

// Activating spinner on anchor elements.
Array.from(spinnerButtons).forEach(button => {
    button.addEventListener('click', function(event) {
        const buttonElement = this;
        
        buttonElement.querySelector('.btn-text').classList.add('d-none');
        buttonElement.querySelector('.spinner-border').classList.remove('d-none');

        Array.from(spinnerButtons).forEach(btn => {
            btn.classList.add('disabled');
        });
    });
});