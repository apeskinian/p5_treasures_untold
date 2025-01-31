let newSlides = document.querySelectorAll(".new-slide");
let featuredSlides = document.querySelectorAll(".featured-slide");
let newSlidesIndex = 0;
let featuredSlidesIndex = 0;

function showNextSlide() {
    newSlides[newSlidesIndex].classList.remove("active");
    featuredSlides[featuredSlidesIndex].classList.remove("active");
    newSlidesIndex = (newSlidesIndex + 1) % newSlides.length;
    featuredSlidesIndex = (featuredSlidesIndex + 1) % featuredSlides.length;
    newSlides[newSlidesIndex].classList.add("active");
    featuredSlides[featuredSlidesIndex].classList.add("active");
}

// Initialize first slide
newSlides[newSlidesIndex].classList.add("active");
featuredSlides[featuredSlidesIndex].classList.add("active");

// Change image every 4 seconds
setInterval(showNextSlide, 10000);
