// مدیریت منوی همبرگری در حالت موبایل
const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');

hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    navLinks.classList.toggle('active');
});

// بستن منو هنگام کلیک روی لینک‌ها
document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
        hamburger.classList.remove('active');
        navLinks.classList.remove('active');
    });
});

// تغییر ظاهر منوبار هنگام اسکرول
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
        navbar.style.height = '70px';
    } else {
        navbar.style.boxShadow = '0 2px 15px rgba(0, 0, 0, 0.1)';
        navbar.style.height = '80px';
    }
});

// شبیه‌سازی افزودن محصول به سبد خرید
const cartCount = document.querySelector('.cart-count');
const floatingCartCount = document.querySelector('.floating-cart-count');
// let count = 

// // تابع برای به روزرسانی تعداد محصولات در سبد خرید
// function updateCartCount() {
//     cartCount.textContent = count;
//     floatingCartCount.textContent = count;
    
//     // ایجاد انیمیشن برای سبد خرید
//     cartCount.style.transform = 'scale(1.3)';
//     floatingCartCount.style.transform = 'scale(1.3)';
//     setTimeout(() => {
//         cartCount.style.transform = 'scale(1)';
//         floatingCartCount.style.transform = 'scale(1)';
//     }, 300);
// }

// // کلیک روی آیکون سبد خرید در منوبار
// document.querySelector('.cart-icon').addEventListener('click', () => {
//     updateCartCount();
// });

// // کلیک روی آیکون سبد خرید در نوار شناور
// document.getElementById('floating-cart').addEventListener('click', function(e) {
//     e.preventDefault();
//     count++;
//     updateCartCount();
//     setActiveButton(this);
// });



// افزودن رویداد برای دکمه‌های شناور
// document.getElementById('floating-order').addEventListener('click', function(e) {
//     e.preventDefault();
//     document.querySelector('.primary-btn').click();
//     setActiveButton(this);
// });

document.getElementById('floating-order').addEventListener('click', function(e) {
    e.preventDefault();
    
    const startOrderBtn = document.getElementById('start-order-btn');
    
    if (startOrderBtn) {
        // اگر دکمه اصلی موجود بود
        startOrderBtn.click();
    } else {
        // اگر دکمه اصلی موجود نبود، از data-url استفاده کن
        const dataUrl = this.getAttribute('data-url');
        if (dataUrl) {
            window.location.href = dataUrl;
        }
    }
    
    setActiveButton(this);
});


document.getElementById('floating-history').addEventListener('click', function(e) {
    window.location.href = this.dataset.url;
    setActiveButton(this);
});

document.getElementById('floating-cart').addEventListener('click', function(e) {
    window.location.href = this.dataset.url;
    setActiveButton(this);
});


// تابع برای تنظیم دکمه فعال
function setActiveButton(button) {
    document.querySelectorAll('.floating-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    button.classList.add('active');
}

// تابع برای اسکرول به بالای صفحه
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// حذف خودکار messages پس از 5 ثانیه
setTimeout(function() {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(alert) {
        alert.style.display = 'none';
    });
}, 5000);


function scrollToSection(element) {
    const elementPosition = element.getBoundingClientRect().top;
    const offsetPosition = elementPosition + window.pageYOffset - navbarHeight - 2; // 20px فاصله اضافی
    
    window.scrollTo({
        top: offsetPosition,
        behavior: 'smooth'
    });
}

const loginBtn = document.getElementById('login')
const logoutBtn = document.getElementById('logout')

if (logoutBtn) {
    logoutBtn.addEventListener('click', function() {
        window.location.href = this.dataset.url;
    });
}


if (loginBtn) {
    loginBtn.addEventListener('click', function() {
        window.location.href = this.dataset.url;
    });
}




