/* jshint esversion: 11, globalstrict: true, jquery: true */
// Magic lamp script that detects if the user 'rubs' the lamp to activate
// the 'magic-lamp' reward.
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
            lamp.classList.add('rubbing');
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
        lamp.classList.remove('rubbing');
    }

    function triggerEasterEgg() {
        var csrfToken = $('meta[name="csrf-token"]').attr('content');
        var url = '/products/activate_reward/activate/magic-lamp/';
        $.post(url, {
            csrfmiddlewaretoken: csrfToken
        })
        .done(function () {
            location.reload();
        });
    }

    if (lamp) {
        lamp.addEventListener("mouseover", startRubbing);
        lamp.addEventListener("mousemove", trackRub);
        document.addEventListener("mouseout", resetRub);
    }
});