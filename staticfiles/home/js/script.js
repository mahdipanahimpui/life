document.addEventListener('DOMContentLoaded', function() {


    const buttons = document.querySelectorAll('.order-type-btn');
    
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            // جلوگیری از کلیک روی لینک‌های داخلی
            if (!e.target.closest('a')) {
                const url = this.getAttribute('data-value');
                if (url) {
                    window.location.href = url;
                }
            }
        });
    });

    // مودال نمایش تصویر
    const modal = document.getElementById('imageModal');
    const modalImage = document.getElementById('modalImage');
    const modalCaption = document.getElementById('modalCaption');
    const modalClose = document.getElementById('modalClose');
    const galleryItems = document.querySelectorAll('.gallery-item');
    
    // باز کردن مودال با کلیک روی آیتم گالری
    galleryItems.forEach(item => {
        item.addEventListener('click', function() {
            const img = this.querySelector('img');
            const title = this.querySelector('.gallery-item-title');
            const desc = this.querySelector('.gallery-item-desc');
            
            modalImage.src = img.src;
            modalImage.alt = img.alt;
            modalCaption.innerHTML = `<strong>${title.textContent}</strong> - ${desc.textContent}`;
            
            modal.classList.add('show');
            document.body.style.overflow = 'hidden'; // جلوگیری از اسکرول صفحه
        });
    });
    
    // بستن مودال
    modalClose.addEventListener('click', function() {
        modal.classList.remove('show');
        document.body.style.overflow = 'auto'; // فعال کردن مجدد اسکرول
    });
    
    // بستن مودال با کلیک خارج از تصویر
    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            modal.classList.remove('show');
            document.body.style.overflow = 'auto';
        }
    });
    
    // بستن مودال با کلید ESC
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && modal.classList.contains('show')) {
            modal.classList.remove('show');
            document.body.style.overflow = 'auto';
        }
    });
});


 // اضافه کردن id به دکمه‌ها و بخش‌ها برای اسکرول
 document.addEventListener('DOMContentLoaded', function() {
    // گرفتن عناصر مورد نیاز
    const startOrderBtn = document.getElementById('start-order-btn');
    const floatingOrder = document.getElementById('floating-order');

    const galleryBtn = document.getElementById('gallery-btn');
    const orderSection = document.getElementById('order-section');
    const gallerySection = document.getElementById('gallery-section');
    const navbar = document.querySelector('.navbar');
    
    // محاسبه ارتفاع navbar
    const navbarHeight = navbar.offsetHeight;
    
    // تابع برای اسکرول با در نظر گرفتن navbar
    function scrollToSection(element) {
        const elementPosition = element.getBoundingClientRect().top;
        const offsetPosition = elementPosition + window.pageYOffset - navbarHeight - 2; // 20px فاصله اضافی
        
        window.scrollTo({
            top: offsetPosition,
            behavior: 'smooth'
        });
    }
    
    // اضافه کردن رویداد کلیک به دکمه "شروع سفارش"
    startOrderBtn.addEventListener('click', function() {
        scrollToSection(orderSection);
    });

    floatingOrder.addEventListener('click', function() {
        scrollToSection(orderSection);
    });
    
    // اضافه کردن رویداد کلیک به دکمه "نمونه کارها"
    galleryBtn.addEventListener('click', function() {
        scrollToSection(gallerySection);
    });
    
    // همچنین برای لینک‌های navbar
    // document.querySelectorAll('.nav-links a').forEach(link => {
    //     link.addEventListener('click', function(e) {
    //         e.preventDefault();
    //         const targetId = this.getAttribute('href');
    //         const targetSection = document.querySelector(targetId);
            
    //         if (targetSection) {
    //             scrollToSection(targetSection);
    //         }
    //     });
    // });
})

// ;querySelector(targetId);querySelector(targetId);