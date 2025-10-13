document.addEventListener('DOMContentLoaded', function() {
    const ordersList = document.getElementById('orders-list');
    const pageNumbers = document.getElementById('page-numbers');
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');
    
    const ordersPerPage = 5; // تعداد سفارشات در هر صفحه
    const orderCards = Array.from(ordersList.getElementsByClassName('order-card'));
    const totalPages = Math.ceil(orderCards.length / ordersPerPage);
    let currentPage = 1;
    
    // فرمت‌دهی قیمت‌ها
    function formatPrices() {
        // قیمت‌های محصولات
        const itemPrices = document.querySelectorAll('.item-price');
        itemPrices.forEach(element => {
            const price = parseFloat(element.textContent) || 0;
            element.textContent = price.toLocaleString() + ' تومان';
        });
        
        // قیمت‌های دلیوری
        const deliveryPrices = document.querySelectorAll('.delivery-price');
        deliveryPrices.forEach(element => {
            const price = parseFloat(element.textContent) || 0;
            element.textContent = 'هزینه ارسال:    ' + price.toLocaleString() + ' تومان';
        });
        
        // قیمت‌های کل
        const orderTotals = document.querySelectorAll('.order-total');
        orderTotals.forEach(element => {
            const price = parseFloat(element.textContent) || 0;
            element.textContent = price.toLocaleString() + ' تومان';
        });
    }
    
    // ایجاد دکمه‌های صفحه‌بندی
    function createPaginationButtons() {
        pageNumbers.innerHTML = '';
        
        // نمایش حداکثر 5 دکمه صفحه
        let startPage = Math.max(1, currentPage - 2);
        let endPage = Math.min(totalPages, startPage + 4);
        
        if (endPage - startPage < 4) {
            startPage = Math.max(1, endPage - 4);
        }
        
        for (let i = startPage; i <= endPage; i++) {
            const pageBtn = document.createElement('button');
            pageBtn.className = 'pagination-btn';
            if (i === currentPage) {
                pageBtn.classList.add('active');
            }
            pageBtn.textContent = i;
            pageBtn.addEventListener('click', () => goToPage(i));
            pageNumbers.appendChild(pageBtn);
        }
    }
    
    // رفتن به صفحه مشخص
    function goToPage(page) {
        currentPage = page;
        updateOrdersDisplay();
        updatePaginationButtons();
        createPaginationButtons();
    }
    
    // به‌روزرسانی نمایش سفارشات
    function updateOrdersDisplay() {
        const startIndex = (currentPage - 1) * ordersPerPage;
        const endIndex = startIndex + ordersPerPage;
        
        orderCards.forEach((card, index) => {
            if (index >= startIndex && index < endIndex) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    }
    
    // به‌روزرسانی وضعیت دکمه‌های صفحه‌بندی
    function updatePaginationButtons() {
        prevBtn.disabled = currentPage === 1;
        nextBtn.disabled = currentPage === totalPages;
    }
    
    // رویدادهای دکمه‌های قبلی و بعدی
    prevBtn.addEventListener('click', () => {
        if (currentPage > 1) {
            goToPage(currentPage - 1);
        }
    });
    
    nextBtn.addEventListener('click', () => {
        if (currentPage < totalPages) {
            goToPage(currentPage + 1);
        }
    });
    
    // مقداردهی اولیه
    if (orderCards.length > 0) {
        updateOrdersDisplay();
        updatePaginationButtons();
        createPaginationButtons();
    } else {
        // اگر سفارشی وجود ندارد، صفحه‌بندی را مخفی کن
        document.getElementById('pagination').style.display = 'none';
        
        // پیام عدم وجود سفارش اضافه کن
        const noOrdersDiv = document.createElement('div');
        noOrdersDiv.className = 'no-orders';
        noOrdersDiv.innerHTML = `
            <i class="fas fa-box-open"></i>
            <h3>هیچ سفارشی یافت نشد</h3>
            <p>شما تاکنون سفارشی ثبت نکرده‌اید.</p>
        `;
        ordersList.appendChild(noOrdersDiv);
    }
    
    // فرمت‌دهی قیمت‌ها پس از لود صفحه
    formatPrices();
});