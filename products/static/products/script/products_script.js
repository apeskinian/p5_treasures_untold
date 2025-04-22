/* jshint esversion: 11, jquery: true */
// Set spinner on add to basket button when clicked
const addToBasketButton = document.getElementById('add-button');

if (addToBasketButton) {
    addToBasketButton.addEventListener('click', function() {
        $('#add-button').addClass('disabled');
        $('#spinner').removeClass('hidden');
        $('#button-text').addClass('hidden');

        setTimeout(() => {
            $('#add-button').removeClass('disabled');
            $('#spinner').addClass('hidden');
            $('#button-text').removeClass('hidden');
        }, 2000);
    });
}