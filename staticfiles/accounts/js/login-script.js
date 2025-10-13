document.addEventListener('DOMContentLoaded', function() {
    const phoneForm = document.getElementById('phoneForm');
    const phoneInput = document.getElementById('phone');
    
    // اعتبارسنجی شماره تلفن
    phoneInput.addEventListener('input', function() {
        this.value = this.value.replace(/[^0-9]/g, '');
        if (this.value.length > 11) {
            this.value = this.value.slice(0, 11);
        }
    });
    
    
    // نمایش اعلان
    function showNotification(message, type = 'success') {
        const notification = document.createElement('div');
        notification.className = `notification ${type}`;
        notification.innerHTML = `
            <i class="fas ${type === 'success' ? 'fa-check-circle' : 'fa-exclamation-circle'}"></i>
            <span>${message}</span>
        `;
        
        document.body.appendChild(notification);
        
        // حذف خودکار اعلان پس از 3 ثانیه
        setTimeout(() => {
            if (notification.parentNode) {
                notification.parentNode.removeChild(notification);
            }
        }, 3000);
    }
});