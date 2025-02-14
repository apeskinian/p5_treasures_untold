// Magic Lamp rubbing detection
document.addEventListener("DOMContentLoaded", function () {
    const magicLampModalElement = document.getElementById('magic-lamp-modal');
    const magicLampModal = new bootstrap.Modal(magicLampModalElement);
    
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
                console.log(movementCount)
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

        $.ajax({
            url: '/products/activate_reward/',
            type: 'POST',
            data: JSON.stringify({ 'reward': 'magic-lamp' }),
            contentType: 'application/json',
            headers: { 'X-CSRFToken': csrfToken },  // 🔹 Add CSRF token here
            success: function () {
                magicLampModal.show();  // Show modal on success
            },
            error: function () {
                alert("Something went wrong! Please try again.");
            }
        });
    }

    lamp.addEventListener("mouseover", startRubbing);
    lamp.addEventListener("mousemove", trackRub);
    document.addEventListener("mouseout", resetRub);
});