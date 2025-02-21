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

// Hide main title on scroll and reappear when scrolled to top
document.addEventListener("DOMContentLoaded", function () {
  const mainTitle = document.querySelector("#main-title");
  const navMenu = document.querySelector("#navigation-menu");
  const accountAndBasket = document.querySelector("#account-and-basket");
  const topNav = document.querySelector(".top-nav");
  const floatingNav = document.querySelector(".floating-top-nav");

  let lastScrollTop = 0;

  if (!mainTitle || !topNav) return;

  // Check if the 'fading-nav-page' class is present
  if (document.body.classList.contains('fading-nav-page')) {
    // Define handleScroll function inside the condition
    function handleScroll() {
      let currentScrollTop = window.scrollY || document.documentElement.scrollTop;

      if (window.innerWidth > 767) {
          const navBottom = topNav.getBoundingClientRect().bottom;

          if (navBottom <= 0) {
            // Scrolled past the navbar
            mainTitle.classList.add("main-title-hide");
            mainTitle.classList.remove("main-title-show");
            navMenu.classList.add("main-title-hide");
            navMenu.classList.remove("main-title-show");
            accountAndBasket.classList.add("main-title-hide");
            accountAndBasket.classList.remove("main-title-show");
          } else if (window.scrollY === 0) {
            // Scrolled to the top
            mainTitle.classList.add("main-title-show");
            mainTitle.classList.remove("main-title-hide");
            navMenu.classList.add("main-title-show");
            navMenu.classList.remove("main-title-hide");
            accountAndBasket.classList.add("main-title-show");
            accountAndBasket.classList.remove("main-title-hide");
            floatingNav.classList.add("main-title-hide");
            floatingNav.classList.remove("main-title-show");
          }

          // Scrolling up
          if (currentScrollTop < lastScrollTop && mainTitle.classList.contains("main-title-hide")) {
            floatingNav.classList.add("main-title-show");
            floatingNav.classList.remove("main-title-hide");
          }
      } else {
          // Reset the classes for smaller screens
          mainTitle.classList.remove("main-title-hide", "main-title-show");
          navMenu.classList.remove("main-title-hide", "main-title-show");
          accountAndBasket.classList.remove("main-title-hide", "main-title-show");
          floatingNav.classList.remove("main-title-hide", "main-title-show");
      }

      lastScrollTop = currentScrollTop; // Update last scroll position
    }

    // Add scroll event listener
    window.addEventListener("scroll", handleScroll);
  }
});