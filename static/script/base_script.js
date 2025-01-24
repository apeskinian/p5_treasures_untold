// enable tooltips
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

// stop the realm collapse menu from triggering the
document.querySelector('#by-realm-menu-mobile a').addEventListener('click', function (event) {
    event.stopPropagation();
  });

// sort selector
$('#sort-selector').change(function() {
  console.log('SELECTOR INITIALISED')
  var selector = $(this);
  var currentUrl = new URL(window.location);
  var selectedVal = selector.val();

  if(selectedVal != 'reset') {
    var sort = selectedVal.split('_')[0];
    var direction = selectedVal.split('_')[1];
    currentUrl.searchParams.set('sort', sort);
    currentUrl.searchParams.set('direction', direction);
    window.location.replace(currentUrl);
  } else {
    currentUrl.searchParams.delete('sort');
    currentUrl.searchParams.delete('direction');
    window.location.replace(currentUrl);
  }
})

// filter menu
const baseUrl = '/products/';
var filterStockList = [];
var filterRealmList = [];

$('#submit-filter').click(function() {
// $('#filter-form input[type="checkbox"]').on('change', function () {
  $('#filter-form input[type="checkbox"]').each(function () {
    if ($(this).is(':checked')) {
      if ($(this).attr('name')=='stock') {
        filterStockList.push($(this).val());
      } else if ($(this).attr('name')=='realm') {
        filterRealmList.push($(this).val());
      }
    }
  })
  var filterList = `?`
  if (filterStockList.length > 0) {
    filterList += `stock=${filterStockList}`
  }
  if (filterStockList.length > 0 && filterRealmList.length > 0) {
    filterList += `&`
  }
  if (filterRealmList.length > 0) {
    filterList += `realm=${filterRealmList}`
  }
  const url = `${baseUrl}${filterList}`;
  window.location.replace(url);
})




// scroll to top button
$('.scroll-link').click(function(e) {
  window.scrollTo(0,0);
})