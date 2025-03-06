/* jshint esversion: 11, globalstrict: true, jquery: true */
// Script for delivery timer in product detail views.
function updateTimer() {

    const now = new Date();
    const target = new Date();

    target.setHours(17, 0, 0, 0);

    if (now > target) {
        target.setDate(target.getDate() + 1);
    }

    var delta = target - now;

    var hours = Math.floor((delta % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((delta % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((delta % (1000 * 60)) / 1000);

    if (delta < 61200000) {
        $('#countdown').html(`Order in the next <strong>${hours}h ${minutes}m ${seconds}s</strong> for same day dispatch!`);
    } else {
        $('#countdown').html(`Order in the next <strong>${hours}h ${minutes}m ${seconds}s</strong> for dispatch tomorrow!`);
    }
}

setInterval(updateTimer, 1000);
updateTimer();