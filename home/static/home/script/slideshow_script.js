/* jshint esversion: 11 */
// Slideshow script for homepage.

let newSlides = document.querySelectorAll(".new-slide");
let featuredSlides = document.querySelectorAll(".featured-slide");
let newSlidesIndex = 0;
let featuredSlidesIndex = 0;

// Iterate to next slide and make active.
function showNextNewSlide() {
    newSlides[newSlidesIndex].classList.remove("active");
    newSlidesIndex = (newSlidesIndex + 1) % newSlides.length;
    newSlides[newSlidesIndex].classList.add("active");
}

// Iterate to next slide and make active.
function showNextFeaturedSlide() {
    featuredSlides[featuredSlidesIndex].classList.remove("active");
    featuredSlidesIndex = (featuredSlidesIndex + 1) % featuredSlides.length;
    featuredSlides[featuredSlidesIndex].classList.add("active");
}

// Set initial slides to active.
newSlides[newSlidesIndex].classList.add("active");
featuredSlides[featuredSlidesIndex].classList.add("active");

// Set times for slide changes.
setInterval(() => {
    showNextNewSlide();
}, 6000);

setTimeout(() => {
    setInterval(showNextFeaturedSlide, 6000);
}, 3000);
