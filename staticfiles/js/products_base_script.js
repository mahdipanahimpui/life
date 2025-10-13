const orderTypeButtons = document.querySelectorAll('.product-type-btn');


// مدیریت دکمه‌های نوع محصول
orderTypeButtons.forEach(button => {
    button.addEventListener('click', function() {
        // حذف کلاس active از همه دکمه‌ها
        orderTypeButtons.forEach(btn => btn.classList.remove('active'));
        
        // اضافه کردن کلاس active به دکمه کلیک شده
        this.classList.add('active');
        
        // در اینجا می‌توانید منطق تغییر نوع محصول را پیاده‌سازی کنید
        const productType = this.getAttribute('data-value');
    });
});


