// disabling qty modifiers outside of stock ranges
function handleEnableDisable(itemId) {
    var currentValue = parseInt($(`#id-qty-${itemId}`).val());
    var minusDisabled = currentValue < 2;
    var plusDisabled = currentValue === parseInt($(`#id-qty-${itemId}`).attr('max'));
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