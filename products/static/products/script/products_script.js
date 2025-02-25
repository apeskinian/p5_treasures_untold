// Magic Lamp rubbing detection
document.addEventListener("DOMContentLoaded", function () {
    
    const lamp = document.getElementById("magic-lamp");
    let rubbing = false;
    let movementCount = 0;
    const movementThreshold = 5;
    let isThrottling = false;

    function startRubbing() {
        rubbing = true;
        movementCount = 0;
    }

    function trackRub(event) {
        if (rubbing && !isThrottling) {
            lamp.classList.add('rubbing')
            isThrottling = true;
            setTimeout(() => {
                movementCount++;
                if (movementCount >= movementThreshold) {
                    triggerEasterEgg();
                    resetRub();
                }
                isThrottling = false;
            }, 1000);
        }
    }

    function resetRub() {
        rubbing = false;
        movementCount = 0;
        lamp.classList.remove('rubbing')
    }

    function triggerEasterEgg() {
        var csrfToken = $('meta[name="csrf-token"]').attr('content');
        var url = '/products/activate_reward/activate/magic-lamp/';
        $.post(url, {
            csrfmiddlewaretoken: csrfToken
        })
        .done(function () {
            location.reload();
        })
    }

    if (lamp) {
        lamp.addEventListener("mouseover", startRubbing);
        lamp.addEventListener("mousemove", trackRub);
        document.addEventListener("mouseout", resetRub)
    }
});


// scroll to top button
$('.scroll-link').click(function(e) {
    window.scrollTo(0,0);
})

// Set scrollbutton bottom margin so that is does not go below the products div
function adjustMarginBottom() {
    const scrollButton = document.querySelector('#scroll-button');
    const footer = document.querySelector('footer');
    const supportLinksDiv = document.querySelector('#support-links');
    const supportSocialDiv = document.querySelector('#support-social');
    const supportNewsletterDiv = document.querySelector('#support-newsletter');
  
    if (!scrollButton || !footer || !supportLinksDiv || !supportSocialDiv || !supportNewsletterDiv) return;
  
    const viewportHeight = window.innerHeight;
  
    let combinedHeight = footer.offsetHeight + supportLinksDiv.offsetHeight + 4;
    if (window.innerWidth < 576) {
        combinedHeight += supportNewsletterDiv.offsetHeight + supportSocialDiv.offsetHeight;
    } else if (window.innerWidth < 768) {
        combinedHeight += supportNewsletterDiv.offsetHeight;
    }

    const scrollY = window.scrollY;
  
    const distanceFromBottom = document.documentElement.scrollHeight - (scrollY + viewportHeight);
  
    if (distanceFromBottom <= combinedHeight) {
      let offset = combinedHeight - distanceFromBottom;
      console.log(offset)
      let maxMargin = 600;
      scrollButton.style.marginBottom = `${Math.min(offset, maxMargin)}px`;
    } else {
      scrollButton.style.marginBottom = "0px";
      if (window.innerWidth < 768) {
            scrollButton.style.marginBottom = "60px";
        }
    }
  }

window.addEventListener('scroll', adjustMarginBottom);
window.addEventListener('load', adjustMarginBottom);