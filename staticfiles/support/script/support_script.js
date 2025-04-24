/* jshint esversion: 11 */
//Adding spinner to submit button on submit
const submitButton = document.getElementById('message-submit-button');

submitButton.addEventListener('click', function(event) {
    submitButton.querySelector('#btn-text').classList.add('d-none');
    submitButton.querySelector('.spinner').classList.remove('d-none');
    submitButton.classList.add('disabled');

    setTimeout(() => {
        submitButton.querySelector('#btn-text').classList.remove('d-none');
        submitButton.querySelector('.spinner').classList.add('d-none');
        submitButton.classList.remove('disabled');
    }, 3000);
});