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

// scroll to top button
$('.scroll-link').click(function(e) {
  window.scrollTo(0,0);
})