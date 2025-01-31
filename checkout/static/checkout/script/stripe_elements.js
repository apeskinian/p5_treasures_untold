console.log('LOADED STRIPE')

var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);

// const appearance = { /* appearance */ };
// const options = { layout: 'accordion', /* options */ };
// const elements = stripe.elements({ client_secret, appearance });
// const paymentElement = elements.create('payment', options);
// paymentElement.mount('#card-element');

var elements = stripe.elements();
var card = elements.create('card');
card.mount('#card-element')
