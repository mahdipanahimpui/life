const fileInput = document.querySelector('input[type="file"]');
const loadingSpinner = document.getElementById("loadingSpinner");
const form = document.querySelector('.order-form');


// اضافه کردن event برای کلیک روی دکمه submit
form.addEventListener('submit', function() {
    if (fileInput.files.length > 0) {
        loadingSpinner.style.display = 'block';
    }
});