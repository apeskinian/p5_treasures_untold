var stripePublicKey = JSON.parse(document.getElementById('id_stripe_public_key').textContent);
var clientSecret = JSON.parse(document.getElementById('id_client_secret').textContent);

var stripe = Stripe(stripePublicKey);

const appearance = { /* appearance */ };
const options = { 
    layout: 'accordion', /* options */ };
const elements = stripe.elements({ clientSecret, appearance });
const paymentElement = elements.create('payment', options);
paymentElement.mount('#card-element');

// var elements = stripe.elements();
// var paymentElement = elements.create('card');
// paymentElement.mount('#card-element')

// handling realtime validation errors
paymentElement.addEventListener('change', function(event) {
    var errorDiv = $('.card-errors');
    if (event.error) {
        var html = event.error.message;
        $(errorDiv).html(html);
    } else {
        $(errorDiv).html('');
    }
})

// handling payment submit: code from STRIPE
// https://docs.stripe.com/payments/quickstart
// document
//   .querySelector("#payment-form")
//   .addEventListener("submit", handleSubmit);

const form = document.querySelector("#payment-form");
form.addEventListener("submit", handleSubmit);

// var form = $('#payment-form');
// form.on('submit', handleSubmit);

async function handleSubmit(e) {
  e.preventDefault();
  setLoading(true);

  const { error } = await stripe.confirmPayment({
    elements,
    confirmParams: {
      // Make sure to change this to your payment completion page
      return_url: "http://127.0.0.1:8000/checkout/",
    },
  });
  
  
  // This point will only be reached if there is an immediate error when
  // confirming the payment. Otherwise, your customer will be redirected to
  // your `return_url`. For some payment methods like iDEAL, your customer will
  // be redirected to an intermediate site first to authorize the payment, then
  // redirected to the `return_url`.
  if (error.type === "card_error" || error.type === "validation_error") {
    showMessage(error.message);
  } else {
    showMessage("An unexpected error occurred.");
  }
  
  setLoading(false);
}

// ------- UI helpers -------
function showMessage(messageText) {
  const messageContainer = document.querySelector("#payment-message");

  messageContainer.classList.remove("hidden");
  messageContainer.textContent = messageText;

  setTimeout(function () {
    messageContainer.classList.add("hidden");
    messageContainer.textContent = "";
  }, 4000);
}

// Show a spinner on payment submission
function setLoading(isLoading) {
  if (isLoading) {
    // Disable the button and show a spinner
    document.querySelector("#submit").disabled = true;
    document.querySelector("#adjust").disabled = true;
    document.querySelector("#spinner").classList.remove("hidden");
    document.querySelector("#button-text").classList.add("hidden");
  } else {
    document.querySelector("#submit").disabled = false;
    document.querySelector("#adjust").disabled = false;
    document.querySelector("#spinner").classList.add("hidden");
    document.querySelector("#button-text").classList.remove("hidden");
  }
}





// Handle form submit
// var form = document.getElementById('payment-form');

// form.addEventListener('submit', function(ev) {
//     ev.preventDefault();
//     paymentElement.update({ 'disabled': true});
//     $('#submit').attr('disabled', true);
//     stripe.confirmCardPayment(clientSecret, {
//         payment_method: {
//             card: paymentElement,
//         }
//     }).then(function(result) {
//         if (result.error) {
//             var errorDiv = document.getElementById('card-errors');
//             var html = `
//                 <span class="icon" role="alert">
//                 <i class="fas fa-times"></i>
//                 </span>
//                 <span>${result.error.message}</span>`;
//             $(errorDiv).html(html);
//             paymentElement.update({ 'disabled': false});
//             $('#submit-button').attr('disabled', false);
//         } else {
//             if (result.paymentIntent.status === 'succeeded') {
//                 console.log('WORKED')
//             }
//         }
//     });
// });