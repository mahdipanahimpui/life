
document.addEventListener('DOMContentLoaded', function() {
    // مدیریت دکمه‌های نوع سفارش
    const productsSection = document.getElementById('productsSection');
    const productsGrid = document.getElementById('productsGrid');
    const paginationContainer = document.getElementById('paginationContainer');
    const pageNumbers = document.getElementById('pageNumbers');
    const firstPageBtn = document.getElementById('firstPageBtn');
    const prevPageBtn = document.getElementById('prevPageBtn');
    const nextPageBtn = document.getElementById('nextPageBtn');
    const lastPageBtn = document.getElementById('lastPageBtn');
    
    // فیلترها - با توجه به HTML جدید
    const paperType = document.getElementById('paperType');
    const paperSize = document.getElementById('paperSize');
    const circulation = document.getElementById('circulation');
    const colorMode = document.getElementById('colorMode')

    


    // تنظیمات صفحه‌بندی
    let currentPage = 1;
    let totalPages = 1;
    let currentProducts = [];
    const productsPerPage = 8; // 2 ردیف * 4 محصول در هر ردیف
    
    // هنگامی که فیلترها تغییر می‌کنند
    paperType.addEventListener('change', showProducts);
    paperSize.addEventListener('change', showProducts);
    circulation.addEventListener('change', showProducts);
    colorMode.addEventListener('change', showProducts);



// ------------------------------------------------------------
    function createProductCard(product) {
        let base_price= product.base_price 
        if (base_price == 0){
            base_price = 'تماس بگیرید'
        } else {
            base_price = product.base_price.toLocaleString() + ' تومان'
        }

        const card = document.createElement('div');
        card.className = 'product-card';

        card.innerHTML = `
        <div class="product-image">
            <i class="fas fa-file-invoice"></i>
        </div>
        <div class="product-details">
            <h3 class="product-title">${product.title}</h3>
            <p><strong>جنس کاغذ:</strong> ${product.paper_type}</p>
            <p><strong>اندازه:</strong> ${product.paper_size}</p>
            <p><strong>نوع رنگ:</strong> ${product.color_mode}</p>
            <p><strong>تیراژ:</strong> ${product.circulation.toLocaleString()} عدد</p>
            <div class="product-meta">
                <span class="product-price">${base_price}</span>
                <button type="button" class="select-product-btn" data-id="${product.id}" data-url="${product.url}">
                    <a href="${product.url}">مشاهده محصول</a> 
                </button>
            </div>
        </div>
    `
    productsGrid.addEventListener('click', function(e) {
        if (e.target.classList.contains('select-product-btn')) {
            const url = e.target.getAttribute('data-url');
            if (url) {
                window.location.href = url;
            }
        }
    });
        
        return card;
    }
    
    
    function showProducts() {
        productsSection.style.display = 'block';
        
        // دریافت مقادیر فیلترها
        const selectedPaperType = paperType.value;
        const selectedSize = paperSize.value;
        const selectedColorMode = colorMode.value
        const selectedCirculation = circulation.value;
        
        // فیلتر کردن محصولات بر اساس انتخاب‌های کاربر
        currentProducts = productsData.filter(product => {
            const matchesPaperType = selectedPaperType === 'all' || product.paper_type === selectedPaperType;
            const matchesSize = selectedSize === 'all' || product.paper_size === selectedSize;
            const matchesColorMode = selectedColorMode === 'all' || product.color_mode === selectedColorMode;

            const matchesCirculation = selectedCirculation === 'all' || product.circulation === parseInt(selectedCirculation);
            
            return matchesPaperType && matchesSize && matchesColorMode && matchesCirculation;
        });
        
        
        if (currentProducts.length === 0) {
            productsGrid.innerHTML = '<p class="full-width">در صورت یافت نشدن محصول با فیلترهای درخواستی برای سفارش با پشتیبانی تماس بگیرید.</p>';
            paginationContainer.style.display = 'none';
            return;
        }
        
        paginationContainer.style.display = 'flex';
        
        // محاسبه تعداد صفحات
        totalPages = Math.ceil(currentProducts.length / productsPerPage);
        
        // نمایش محصولات صفحه اول
        displayProductsPage(1);
        setupPagination();
    }
    

    
    function displayProductsPage(page) {
        currentPage = page;
        productsGrid.innerHTML = '';
        
        const startIndex = (page - 1) * productsPerPage;
        const endIndex = Math.min(startIndex + productsPerPage, currentProducts.length);
        
        // ایجاد المنت‌های خالی برای حفظ ساختار 4 تایی
        for (let i = startIndex; i < endIndex; i++) {
            const product = currentProducts[i];
            const productCard = createProductCard(product);
            productsGrid.appendChild(productCard);
        }
        
        // اضافه کردن المنت‌های خالی برای کامل کردن ردیف آخر
        const remainingItems = productsPerPage - (endIndex - startIndex);
        if (remainingItems > 0) {
            for (let i = 0; i < remainingItems; i++) {
                const emptyCard = document.createElement('div');
                emptyCard.className = 'product-card empty-card';
                emptyCard.style.visibility = 'hidden';
                productsGrid.appendChild(emptyCard);
            }
        }
        
        updatePaginationButtons();
    }
    

    
    function setupPagination() {
        // پاک کردن شماره صفحات قبلی
        pageNumbers.innerHTML = '';
        
        // ایجاد دکمه‌های شماره صفحه
        for (let i = 1; i <= totalPages; i++) {
            const pageBtn = document.createElement('button');
            pageBtn.className = `pagination-btn ${i === currentPage ? 'active' : ''}`;
            pageBtn.textContent = i;
            pageBtn.addEventListener('click', () => displayProductsPage(i));
            pageNumbers.appendChild(pageBtn);
        }
        
        // اضافه کردن event listener به دکمه‌های کنترل صفحه
        firstPageBtn.addEventListener('click', () => displayProductsPage(1));
        prevPageBtn.addEventListener('click', () => displayProductsPage(currentPage - 1));
        nextPageBtn.addEventListener('click', () => displayProductsPage(currentPage + 1));
        lastPageBtn.addEventListener('click', () => displayProductsPage(totalPages));
        
        updatePaginationButtons();
    }
    
    function updatePaginationButtons() {
        // به روزرسانی وضعیت دکمه‌ها
        firstPageBtn.disabled = currentPage === 1;
        prevPageBtn.disabled = currentPage === 1;
        nextPageBtn.disabled = currentPage === totalPages;
        lastPageBtn.disabled = currentPage === totalPages;
        
        // به روزرسانی دکمه‌های فعال
        const pageBtns = pageNumbers.querySelectorAll('.pagination-btn');
        pageBtns.forEach((btn, index) => {
            if (index + 1 === currentPage) {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });
    }
    

    // نمایش اولیه محصولات
    showProducts();
});