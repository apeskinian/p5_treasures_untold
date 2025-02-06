// Core logic/payment flow for this comes from here:
// https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=elements

var stripePublicKey = JSON.parse(document.getElementById('id_stripe_public_key').textContent);
var clientSecret = JSON.parse(document.getElementById('id_client_secret').textContent);

var stripe = Stripe(stripePublicKey);

const options = {
  clientSecret,
  appearance: {/*...*/},
};

// Set up Stripe.js and Elements to use in checkout form, passing the client secret
const elements = stripe.elements(options);

// // create and mount the address element
// const addressElementOptions = { mode: 'shipping' }
// const addressElement = elements.create('address', addressElementOptions)
// addressElement.mount('#address-element')

// Create and mount the Payment Element
const paymentElementOptions = { layout: 'accordion'};
const paymentElement = elements.create('payment', paymentElementOptions);
paymentElement.mount('#payment-element');

// handling realtime validation errors
paymentElement.addEventListener('change', function(event) {
    var errorDiv = $('#payment-errors');
    if (event.error) {
        var html = event.error.message;
        $(errorDiv).html(html);
    } else {
        $(errorDiv).html('');
    }
})

const form = document.getElementById('payment-form');



form.addEventListener('submit', function(event) {
  event.preventDefault();
  setLoading(true);

  var saveInfo = Boolean($('#id-save-info').prop('checked'));
  console.log(saveInfo);
  var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
  var postData = {
    'csrfmiddlewaretoken': csrfToken,
    'client_secret': clientSecret,
    'save_info': saveInfo,
  };
  var url = '/checkout/cache_checkout_data/';

  $.post(url, postData).done(function() {
    stripe.confirmPayment({
      //`Elements` instance that was used to create the Payment Element
      elements,
      redirect: 'if_required',
      confirmParams: {
        payment_method_data: {
          billing_details: {
            name: $.trim(form.full_name.value),
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
    }).then(function(result) {
      if (result.error) {
        // show any errors to the user
        var errorDiv = $('#payment-errors');
        var html = result.error.message;
        $(errorDiv).html(html);
        setLoading(false);
      } else {
        // submit the form
        if (result.paymentIntent.status === 'succeeded') {
          form.submit();
        }
      }
    });
  }).fail(function () {
    location.reload();
  })

})

// disable submit and adjust buttons and show a spinner to user
function setLoading(isLoading) {
  if (isLoading) {
    $('#submit-button').attr('disabled', true);
    $('#adjust-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);
    $('#spinner').removeClass('hidden');
    $('#button-text').addClass('hidden');
  } else {
    $('#submit-button').attr('disabled', false);
    $('#adjust-button').attr('disabled', false);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);
    $('#spinner').addClass('hidden');
    $('#button-text').removeClass('hidden');
  }
}