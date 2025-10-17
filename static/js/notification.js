


// مدیریت مودال
function showModal() {
    const modal = document.getElementById('notificationModal');
    modal.classList.add('active');
    document.body.style.overflow = 'hidden'; // جلوگیری از اسکرول صفحه پشت
}

function closeModal() {
    const modal = document.getElementById('notificationModal');
    modal.classList.remove('active');
    document.body.style.overflow = 'auto'; // بازگشت اسکرول
}

// بستن مودال با کلیک خارج از آن
document.getElementById('notificationModal').addEventListener('click', function(e) {
    if (e.target === this) {
        closeModal();
    }
});

// بستن مودال با کلید Escape
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        closeModal();
    }
});

// توابع اصلی
function checkNotification() {
    // بررسی کوکی - اگر کاربر قبلاً بستن موقت زده، نمایش نده
    if (getCookie('notification_dismissed')) {
        return;
    }
    
    fetch('/extra/active-notification/')
        .then(response => response.json())
        .then(data => {
            if (data.exists) {
                // document.getElementById('notificationTitle').textContent = data.title;
                document.getElementById('notificationMessage').textContent = data.message;
                
                // نمایش مودال
                showModal();
            }
        })
        .catch(error => {
            console.error('Error fetching notification:', error);
        });

}

function dismissNotification() {
    // تنظیم کوکی برای 24 ساعت
    setCookie('notification_dismissed', 'true', 10);
    
    // بستن مودال
    closeModal();
}

// توابع کمکی برای کار با کوکی
function setCookie(name, value, days) {
    const expires = new Date();
    expires.setTime(expires.getTime() + (days * 24 * 60 * 60 * 1000));
    document.cookie = `${name}=${value};expires=${expires.toUTCString()};path=/`;
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
    return null;
}

// اجرا پس از لود کامل صفحه
document.addEventListener('DOMContentLoaded', function() {
    setTimeout(checkNotification, 1000);
});
