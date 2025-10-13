document.addEventListener('DOMContentLoaded', function() {



    document.getElementById('startNumber').required = true;
    document.getElementById('numberingLocation').required = true;

    // مدیریت آپلود فایل
    const fileUpload = document.getElementById('fileUpload');
    const fileInput = document.getElementById('fileInput');
    const fileNames = document.getElementById('fileNames');
    
    fileUpload.addEventListener('click', function() {
        fileInput.click();
    });
    
    fileInput.addEventListener('change', function() {
        if(this.files.length > 0) {
            let names = '';
            for(let i = 0; i < this.files.length; i++) {
                names += this.files[i].name + '<br>';
            }
            fileNames.innerHTML = names;
        } else {
            fileNames.innerHTML = '';
        }
    });
    
    // امکان کشیدن و رها کردن فایل
    fileUpload.addEventListener('dragover', function(e) {
        e.preventDefault();
        this.style.borderColor = '#4a6cf7';
        this.style.backgroundColor = '#f0f5ff';
    });
    
    fileUpload.addEventListener('dragleave', function(e) {
        e.preventDefault();
        this.style.borderColor = '#ddd';
        this.style.backgroundColor = '#f8faff';
    });
    
    fileUpload.addEventListener('drop', function(e) {
        e.preventDefault();
        this.style.borderColor = '#4a6cf7';
        this.style.backgroundColor = '#f8faff';
        
        if(e.dataTransfer.files.length > 0) {
            fileInput.files = e.dataTransfer.files;
            let names = '';
            for(let i = 0; i < e.dataTransfer.files.length; i++) {
                names += e.dataTransfer.files[i].name + '<br>';
            }
            fileNames.innerHTML = names;
        }
    });
    
    // مدیریت چک‌باکس "بدون شماره" - حل مشکل رنگ انتخابی
    const startNumberInput = document.getElementById('startNumber');
    const numberingLocationInput = document.getElementById('numberingLocation');
    const noNumberCheckbox = document.getElementById('noNumber');
    const noNumberCheckboxLabel = document.getElementById('noNumberCheckbox');
    const colorRadios = document.querySelectorAll('.color-radio');
    const colorRadioLabels = document.querySelectorAll('.color-radio-label');
    
    // ذخیره رنگ انتخابی قبلی
    // let lastSelectedColor = 'red';
    // let lastSelectedColorRadio = document.getElementById('colorRed');

    if (noNumberCheckbox.checked) {
        // غیرفعال کردن فیلد شماره
        startNumberInput.disabled = true;
        numberingLocationInput.disabled = true;
        noNumberCheckboxLabel.classList.add('active');

        startNumberInput.removeAttribute('required');
        numberingLocationInput.removeAttribute('required');

        
        // ذخیره رنگ انتخابی فعلی
        const currentSelected = document.querySelector('.color-radio:checked');
        if (currentSelected) {
            lastSelectedColor = currentSelected.value;
            lastSelectedColorRadio = currentSelected;
        }
        
        // غیرفعال کردن دکمه‌های رنگ
        colorRadios.forEach(radio => {
            radio.disabled = true;
        });
        colorRadioLabels.forEach(label => {
            label.classList.remove('selected');
        });
    }

    let lastSelectedColor = null;
    let lastSelectedColorRadio = null;
    
    noNumberCheckbox.addEventListener('change', function() {
        if (this.checked) {
            // غیرفعال کردن فیلد شماره
            startNumberInput.disabled = true;
            numberingLocationInput.disabled = true;
            noNumberCheckboxLabel.classList.add('active');

            startNumberInput.removeAttribute('required');
            numberingLocationInput.removeAttribute('required');

            
            // ذخیره رنگ انتخابی فعلی
            const currentSelected = document.querySelector('.color-radio:checked');
            if (currentSelected) {
                lastSelectedColor = currentSelected.value;
                lastSelectedColorRadio = currentSelected;
            }
            
            // غیرفعال کردن دکمه‌های رنگ
            colorRadios.forEach(radio => {
                radio.disabled = true;
            });
            colorRadioLabels.forEach(label => {
                label.classList.remove('selected');
            });
        } else {
            // فعال کردن فیلد شماره
            startNumberInput.disabled = false;
            numberingLocationInput.disabled = false;
            noNumberCheckboxLabel.classList.remove('active');


            startNumberInput.setAttribute('required', 'required');
            numberingLocationInput.setAttribute('required', 'required');               
            
            // فعال کردن دکمه‌های رنگ و بازگرداندن انتخاب قبلی
            colorRadios.forEach(radio => {
                radio.disabled = false;
                if (radio.value === lastSelectedColor) {
                    radio.checked = true;
                    radio.nextElementSibling.classList.add('selected');
                } else {
                    radio.nextElementSibling.classList.remove('selected');
                }
            });
        }
    });
    
    // مدیریت رادیو باتن‌های انتخاب رنگ
    let selectedColor; // رنگ قرمز به صورت پیش‌فرض انتخاب شده
    
    colorRadios.forEach(radio => {
        radio.addEventListener('change', function() {
            if (!this.disabled) {
                colorRadioLabels.forEach(label => label.classList.remove('selected'));
                this.nextElementSibling.classList.add('selected');
                selectedColor = this.value;
                lastSelectedColor = selectedColor;
                lastSelectedColorRadio = this;
            }
        });
    });
    
    // مدیریت انتخاب پرفراژ
    const perforationOptions = document.querySelectorAll('.perforation-option');
    perforationOptions.forEach(option => {
        option.addEventListener('click', function() {
            perforationOptions.forEach(opt => opt.classList.remove('selected'));
            this.classList.add('selected');
        });
    });

    

    
    
});