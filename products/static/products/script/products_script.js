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
            lamp.classList.add('sparkly-effect')
            isThrottling = true;
            setTimeout(() => {
                movementCount++;
                if (movementCount >= movementThreshold) {
                    triggerEasterEgg();
                    resetRub();
                }
                console.log(movementCount)
                isThrottling = false;
            }, 1000);
        }
    }

    function resetRub() {
        rubbing = false;
        movementCount = 0;
        lamp.classList.remove('rubbing')
        lamp.classList.remove('sparkly-effect')
    }

    function triggerEasterEgg() {
        alert("INTEGRATE REWARD NOW");
    }

    lamp.addEventListener("mouseover", startRubbing);
    lamp.addEventListener("mousemove", trackRub);
    document.addEventListener("mouseout", resetRub);
});