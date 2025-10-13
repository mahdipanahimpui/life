// تابع به‌روزرسانی تعداد محصول
checkEmptyCart();



document.getElementById('continueShopping').addEventListener('click', function() {
    window.location.href = this.dataset.url;
    });





const buttons = document.querySelectorAll('.remove-order');

buttons.forEach(function(button) {
    button.addEventListener('click', function() {
        window.location.href = this.dataset.url;
    });
});
    
// تابع به‌روزرسانی مبلغ کل
function updateTotal() {
    let total = 0;
    const items = document.querySelectorAll('.cart-item');
    
    items.forEach(item => {
        const priceText = item.querySelector('.cart-item-price').textContent;
        const price = parseInt(priceText.replace(/,/g, ''));
        
        total += price;
    });
    
    // نمایش مبلغ نهایی
    document.getElementById('total').textContent = total.toLocaleString() + ' تومان';
}

// تابع بررسی خالی بودن سبد خرید
function checkEmptyCart() {
    const cartItems = document.querySelector('.cart-items');
    if (cartItems.children.length === 0) {
        const emptyHTML = `
            <div class="empty-cart">
                <i class="fas fa-shopping-cart"></i>
                <h3>سبد خرید شما خالی است</h3>
                <p>می‌توانید برای مشاهده محصولات و افزودن آنها به سبد خرید به صفحه محصولات مراجعه کنید.</p>

            </div>
        `;
        cartItems.innerHTML = emptyHTML;
        
        // مخفی کردن بخش خلاصه سفارش و دکمه‌ها
        document.querySelector('.order-summary').style.display = 'none';
        document.querySelector('.checkout-btn').style.display = 'none';
        document.getElementById('continueShopping').textContent = 'صفحه محصولات'
    }
}

// مقداردهی اولیه
document.addEventListener('DOMContentLoaded', function() {
    updateTotal();
});