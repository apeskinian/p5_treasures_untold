window.onload = () => {
    const dashboardModalElement = document.getElementById('dashboard-modal');
    if (dashboardModalElement) {
        const dashboardModal = new bootstrap.Modal(dashboardModalElement);
        dashboardModal.show();
    }
};