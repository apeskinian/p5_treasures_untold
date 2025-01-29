// disabling qty modifiers outside of stock ranges
function handleEnableDisable(itemId) {
  var currentValue = parseInt($(`#id-qty-${itemId}`).val());
  var maxPurchase = parseInt($(`#id-qty-${itemId}`).attr('max'));
  var minPurchase = parseInt($(`#id-qty-${itemId}`).attr('min'));
  var minusDisabled = currentValue === minPurchase;
  var plusDisabled = currentValue === maxPurchase; 
  $(`#decrement-qty-${itemId}`).prop('disabled', minusDisabled);
  $(`#increment-qty-${itemId}`).prop('disabled', plusDisabled);
}
  
// check enable/disable inputs on page load
var allQtyInputs = $('.qty-input');
for(var i = 0; i < allQtyInputs.length; i++){
  var itemId = $(allQtyInputs[i]).data('item-id');
  handleEnableDisable(itemId);
}

// enforce limits on built in modifiers
$('.qty-input').change(function() {
  var itemId = $(this).data('item-id');
  handleEnableDisable(itemId);
})

//increment qty
$('.increment-qty').click(function(e) {
  e.preventDefault();
  var closestInput = $(this).closest('.input-group').find('.qty-input')[0];
  var currentValue = parseInt($(closestInput).val());
  $(closestInput).val(currentValue + 1);
  var itemId = $(this).data('item-id');
  handleEnableDisable(itemId);
});

//decrement qty
$('.decrement-qty').click(function(e) {
  e.preventDefault();
  var closestInput = $(this).closest('.input-group').find('.qty-input')[0];
  var currentValue = parseInt($(closestInput).val());
  $(closestInput).val(currentValue - 1);
  var itemId = $(this).data('item-id');
  handleEnableDisable(itemId);
});

// update form
$('.update-basket').click(function(e) {
  e.preventDefault();

  // preventing double clicking
  var updateLink = $(this);
  if (updateLink.hasClass('disabled')) return;
  updateLink.addClass('disabled');

  var form = $(this).prev('.update-form');
  var inputField = form.find('input[type="number"]')[0];

  if (inputField.checkValidity()) {
    form.submit();
  } else {
    inputField.reportValidity();
    updateLink.removeClass('disabled');
  }

});

// get csrf token from meta
function getCsrfToken() {
  return $('meta[name="csrf-token"]').attr('content');
}

// remove items
$('.remove-item').click(function(e) {
    e.preventDefault()

    // prevent double clicking
    var removeLink = $(this);
    if (removeLink.hasClass('disabled')) return;
    removeLink.addClass('disabled');

    var csrfToken = getCsrfToken();
    var itemId = $(this).attr('id').split('remove-')[1];
    var quantity = $(this).data('qty');
    var url = `/basket/remove/${itemId}/`;
    var data = {'csrfmiddlewaretoken': csrfToken, 'quantity': quantity};

    $.post(url, data)
        .done(function() {
            location.reload();
        })
        .fail(function () {
          removeLink.removeClass('disabled');
      });
})

