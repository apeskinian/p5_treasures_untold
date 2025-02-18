// enable tooltips
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

// show toasts
$('.toast').each(function(toastEl) {
  var toast = new bootstrap.Toast(this);
  toast.show();
});

// stop the realm collapse menu from triggering the dropdowns
document.querySelector('#by-realm-menu-mobile a').addEventListener('click', function (event) {
    event.stopPropagation();
  });

// sort items selector
$('#sort-selector').change(function() {
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

// product filter menu
const baseUrl = '/products/';
var filterStockList = [];
var filterRealmList = [];
var filterNewList = [];

$('#submit-filter').click(function() {
  $('#filter-form input[type="checkbox"]').each(function () {
    if ($(this).is(':checked')) {
      if ($(this).attr('name')=='new') {
        filterNewList.push($(this).val());
      } else if ($(this).attr('name')=='stock') {
        filterStockList.push($(this).val());
      } else if ($(this).attr('name')=='realm') {
        filterRealmList.push($(this).val());
      }
    }
  })

  var filterList = [];
  if (filterNewList.length > 0) {
      filterList.push(`${filterNewList}`);
  }
  if (filterStockList.length > 0) {
      filterList.push(`stock=${filterStockList}`);
  }
  if (filterRealmList.length > 0) {
      filterList.push(`realm=${filterRealmList}`);
  }
  const queryString = filterList.length > 0 ? `?${filterList.join('&')}` : '';
  const url = `${baseUrl}${queryString}`;
  window.location.replace(url);
})

// scroll to top button
$('.scroll-link').click(function(e) {
  window.scrollTo(0,0);
})

// back button
$('.back-button').click(function(e) {
  e.preventDefault();
  history.back(); screenLeft
})

// // dynamic hero for desktop browsers
function getTriggerHeroHeight() {
  if (window.innerWidth < 1200) {
      return 180;
  } else  {
      return 300;
  }
}

function getTriggerTitleHeight() {
  if (window.innerWidth < 1200) {
      return 90;
  } else {
      return 150;
  }
}

document.addEventListener("scroll", function () {
  const topNav = document.querySelector('.top-nav');
  const heroSpacer = document.querySelector('.hero-spacer')
  const mainTitle = document.querySelector('.main-title')
  const triggerHeroHeight = getTriggerHeroHeight();
  const triggerTitleHeight = getTriggerTitleHeight();

  if (window.scrollY >= triggerHeroHeight) {
      topNav.classList.add('top-nav-small')
      heroSpacer.classList.add('hero-spacer-enabled')
    } else {
      topNav.classList.remove('top-nav-small');
      heroSpacer.classList.remove('hero-spacer-enabled')
  }
 
  if (window.scrollY >= triggerTitleHeight) {
      mainTitle.classList.add('main-title-small')
    } else {
      mainTitle.classList.remove('main-title-small');
  }
});
