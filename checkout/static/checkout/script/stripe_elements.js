/* jshint esversion: 11, jquery: true */
// Core logic/payment flow for this comes from here:
// https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=elements

var stripePublicKey = JSON.parse(document.getElementById('id_stripe_public_key').textContent);
var clientSecret = JSON.parse(document.getElementById('id_client_secret').textContent);

var stripe = Stripe(stripePublicKey);

const options = {
    clientSecret,
    appearance: {},
};

// Set up Stripe.js and Elements to use in checkout form, passing the client secret.
const elements = stripe.elements(options);

// Create and mount the Payment Element
const paymentElementOptions = { layout: 'accordion' };
const paymentElement = elements.create('payment', paymentElementOptions);
paymentElement.mount('#payment-element');

// Handling realtime validation errors.
paymentElement.addEventListener('change', function (event) {
    var errorDiv = $('#payment-errors');
    if (event.error) {
        var html = event.error.message;
        $(errorDiv).html(html);
    } else {
        $(errorDiv).html('');
    }
});

const form = document.getElementById('payment-form');

// Listen for form submission then take over and submit to Stripe.
form.addEventListener('submit', function (event) {
    event.preventDefault();
    setLoading(true);

    var saveInfo = Boolean($('#id-save-info').prop('checked'));
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';

    // Get updated metadata from cache_checkout_data view then submit to Stripe.
    $.post(url, postData).done(function () {
        stripe.confirmPayment({
            elements,
            redirect: 'if_required',
            confirmParams: {
                payment_method_data: {
                    billing_details: {
                        name: $.trim(form.full_name.value),
                        email: $.trim(form.email.value),
                        phone: $.trim(form.phone_number.value),
                        address: {
                            line1: $.trim(form.street_address_1.value),
                            line2: $.trim(form.street_address_2.value),
                            city: $.trim(form.town_city.value),
                            state: $.trim(form.county.value),
                            country: $.trim(form.country.value),
                        }
                    }
                },
                shipping: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    address: {
                        line1: $.trim(form.street_address_1.value),
                        line2: $.trim(form.street_address_2.value),
                        city: $.trim(form.town_city.value),
                        state: $.trim(form.county.value),
                        postal_code: $.trim(form.postcode.value),
                        country: $.trim(form.country.value),
                    }
                },
            },
        }).then(function (result) {
            if (result.error) {
                // Show any errors to the user.
                var errorDiv = $('#payment-errors');
                var html = result.error.message;
                $(errorDiv).html(html);
                setLoading(false);
            } else {
                // Submit the form.
                if (result.paymentIntent.status === 'succeeded') {
                    //form.submit();
                }
            }
        });
    }).fail(function () {
        location.reload();
    });

});

// Disable submit and adjust buttons and show a spinner to user.
function setLoading(isLoading) {
    if (isLoading) {
        $('#submit-button').attr('disabled', true);
        $('#adjust-button').addClass('disabled');
        $('#payment-form').fadeToggle(100);
        $('#loading-overlay').removeClass('d-none');
        $('#loading-overlay').addClass('d-flex');
        $('#checkout-container').fadeToggle(100);
        $('#spinner').removeClass('hidden');
        $('#button-text').addClass('hidden');
    } else {
        $('#submit-button').attr('disabled', false);
        $('#adjust-button').removeClass('disabled');
        $('#payment-form').fadeToggle(100);
        $('#loading-overlay').removeClass('d-flex');
        $('#loading-overlay').addClass('d-none');
        $('#checkout-container').fadeToggle(100);
        $('#spinner').addClass('hidden');
        $('#button-text').removeClass('hidden');
    }
}

// Re-report form validity after focusing on out of view field.
const submitButton = document.getElementById('submit-button');
submitButton.addEventListener('click', function () {
    const currentPosition = window.scrollY;
    const firstInvalid = form.querySelector(':invalid');
    setTimeout(() => {
        const newPosition = window.scrollY;
        if (newPosition !== currentPosition) {
            if ((firstInvalid)) {
                    setTimeout(() => {
                        form.reportValidity();
                    }, 500);
            }
        }
    }, 100);
})