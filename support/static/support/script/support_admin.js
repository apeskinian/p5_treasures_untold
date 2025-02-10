window.onload = () => {
    const settingsModalElement = document.getElementById('settings-modal');
    if (settingsModalElement) {
        const settingsModal = new bootstrap.Modal(settingsModalElement);
        settingsModal.show();
    }
};