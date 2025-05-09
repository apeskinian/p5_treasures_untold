/* jshint esversion: 11, jquery: true */
// Show toasts
$('.toast').each(function (toastEl) {
    var toast = new bootstrap.Toast(this);
    toast.show();
});

// Stop the realm collapse menu from triggering the dropdowns
document.querySelector('#by-realm-menu-mobile a').addEventListener('click', function (event) {
    event.stopPropagation();
});

// Sort items selector mobile
$('#sort-selector-mobile').change(function () {
    var selector = $(this);
    var currentUrl = new URL(window.location);
    var selectedVal = selector.val();

    if (selectedVal != 'reset') {
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
});

// Product filter menu mobile
const currentParamsMobile = new URLSearchParams(window.location.search);
const searchValueMobile = currentParamsMobile.get('q');
const sortValueMobile = currentParamsMobile.get('sort');
const directionValueMobile = currentParamsMobile.get('direction');
const baseUrlMobile = '/products/';
var filterStockList = [];
var filterRealmList = [];
var filterNewList = [];

$('#submit-filter-mobile').click(function () {
    $('#filter-form-mobile input[type="checkbox"]').each(function () {
        if ($(this).is(':checked')) {
            if ($(this).attr('name') == 'new') {
                filterNewList.push($(this).val());
            } else if ($(this).attr('name') == 'stock') {
                filterStockList.push($(this).val());
            } else if ($(this).attr('name') == 'realm') {
                filterRealmList.push($(this).val());
            }
        }
    });

    var queryList = [];
    if (searchValueMobile !== null) {
        queryList.push(`q=${encodeURIComponent(searchValue)}`);
    }
    if (filterNewList.length > 0) {
        queryList.push(`${filterNewList}`);
    }
    if (filterStockList.length > 0) {
        queryList.push(`stock=${filterStockList}`);
    }
    if (filterRealmList.length > 0) {
        queryList.push(`realm=${filterRealmList}`);
    }
    if (sortValueMobile !== null) {
        queryList.push(`sort=${encodeURIComponent(sortValue)}`);
    }
    if (directionValueMobile !== null) {
        queryList.push(`direction=${encodeURIComponent(directionValue)}`);
    }
    const queryString = queryList.length > 0 ? `?${queryList.join('&')}` : '';
    const url = `${baseUrlMobile}${queryString}`;
    window.location.replace(url);
});

// sort items selector 
$('#sort-selector').change(function () {
    var selector = $(this);
    var currentUrl = new URL(window.location);
    var selectedVal = selector.val();

    if (selectedVal != 'reset') {
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
});

// product filter menu
const currentParams = new URLSearchParams(window.location.search);
const searchValue = currentParams.get('q');
const sortValue = currentParams.get('sort');
const directionValue = currentParams.get('direction');
const baseUrl = '/products/';
var filterStockList = [];
var filterRealmList = [];
var filterNewList = [];

$('#submit-filter').click(function () {
    $('#filter-form input[type="checkbox"]').each(function () {
        if ($(this).is(':checked')) {
            if ($(this).attr('name') == 'new') {
                filterNewList.push($(this).val());
            } else if ($(this).attr('name') == 'stock') {
                filterStockList.push($(this).val());
            } else if ($(this).attr('name') == 'realm') {
                filterRealmList.push($(this).val());
            }
        }
    });

    var queryList = [];
    if (searchValue !== null) {
        queryList.push(`q=${encodeURIComponent(searchValue)}`);
    }
    if (filterNewList.length > 0) {
        queryList.push(`${filterNewList}`);
    }
    if (filterStockList.length > 0) {
        queryList.push(`stock=${filterStockList}`);
    }
    if (filterRealmList.length > 0) {
        queryList.push(`realm=${filterRealmList}`);
    }
    if (sortValue !== null) {
        queryList.push(`sort=${encodeURIComponent(sortValue)}`);
    }
    if (directionValue !== null) {
        queryList.push(`direction=${encodeURIComponent(directionValue)}`);
    }
    const queryString = queryList.length > 0 ? `?${queryList.join('&')}` : '';
    const url = `${baseUrl}${queryString}`;
    window.location.replace(url);
});

// Hide main title on scroll and reappear when scrolled to top
document.addEventListener("DOMContentLoaded", function () {
    const mainTitle = document.querySelector("#main-title");
    const navMenu = document.querySelector("#navigation-menu");
    const accountAndBasket = document.querySelector("#account-and-basket");
    const topNav = document.querySelector(".top-nav");
    const floatingNav = document.querySelector(".floating-top-nav");
    const scrollButton = document.querySelector('#scroll-button');

    let lastScrollPositionFromTop = 0;

    if (!mainTitle || !topNav || !navMenu || !accountAndBasket || !floatingNav) return;

    // Define handleScroll function
    function handleScroll() {
        let currentScrollPositionFromTop = window.scrollY;

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
                if (scrollButton) {
                    scrollButton.classList.remove('scroll-button-hide');
                }
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
                if (scrollButton) {
                    scrollButton.classList.add('scroll-button-hide');
                }
            }
            // Scrolling up
            if (currentScrollPositionFromTop < lastScrollPositionFromTop && mainTitle.classList.contains("main-title-hide")) {
                floatingNav.classList.add("main-title-show");
                floatingNav.classList.remove("main-title-hide");
            }
        } else {
            const navBottom = topNav.getBoundingClientRect().bottom;
            if (navBottom <= 0) {
                scrollButton.classList.remove('scroll-button-hide');
            } else if (window.scrollY === 0) {
                scrollButton.classList.add('scroll-button-hide');
            }
            // Reset the classes for smaller screens
            mainTitle.classList.remove("main-title-hide", "main-title-show");
            navMenu.classList.remove("main-title-hide", "main-title-show");
            accountAndBasket.classList.remove("main-title-hide", "main-title-show");
            floatingNav.classList.remove("main-title-hide", "main-title-show");
        }

        lastScrollPositionFromTop = currentScrollPositionFromTop; // Update last scroll position
    }

    // Check if the 'fading-nav-page' class is present
    if (document.body.classList.contains('fading-nav-page')) {
        // Add scroll event listener
        window.addEventListener("scroll", handleScroll);
        window.addEventListener('scroll', adjustMarginBottom);
        window.addEventListener('load', adjustMarginBottom);
    }
});

// scroll to top button
$('.scroll-link').click(function (e) {
    e.preventDefault();
    window.scrollTo(0, 0);
});

// Set scrollbutton bottom margin so that is does not go below the products div
function adjustMarginBottom() {
    const scrollButton = document.querySelector('#scroll-button');
    const footer = document.querySelector('footer');
    const supportLinksDiv = document.querySelector('#support-links');
    const supportSocialDiv = document.querySelector('#support-social');
    const supportNewsletterDiv = document.querySelector('#support-newsletter');

    if (!scrollButton || !footer) return;

    const viewportHeight = window.innerHeight;
    let combinedHeight = footer.offsetHeight + 4;

    if (supportLinksDiv) {
        combinedHeight = footer.offsetHeight + supportLinksDiv.offsetHeight;
        if (window.innerWidth < 576) {
            combinedHeight += supportNewsletterDiv.offsetHeight + supportSocialDiv.offsetHeight;
        } else if (window.innerWidth < 768) {
            combinedHeight += supportNewsletterDiv.offsetHeight;
        }
    }

    const scrollY = window.scrollY;

    const distanceFromBottom = document.documentElement.scrollHeight - (scrollY + viewportHeight);

    if (distanceFromBottom <= combinedHeight) {
        let offset = combinedHeight - distanceFromBottom;
        let maxMargin = 600;
        scrollButton.style.marginBottom = `${Math.min(offset, maxMargin)}px`;
    } else {
        scrollButton.style.marginBottom = "0px";
        if (window.innerWidth < 768) {
            scrollButton.style.marginBottom = "60px";
        }
    }
}