buttons = document.querySelectorAll('.product-type-btn')

buttons.forEach(function(button) {
    button.addEventListener('click', function() {
        window.location.href = this.dataset.url;
    });
});


