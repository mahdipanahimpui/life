document.addEventListener('DOMContentLoaded', function() {


    const bindingDirection = document.getElementById('bindingDirection')
    bindingDirection.disabled = true
    bindingDirection.removeAttribute('required')

    const glueAttachCheckbox = document.getElementById('glueAttachCheckbox')

    glueAttachCheckbox.addEventListener('change', function() {
        if (this.checked) {
            // غیرفعال کردن فیلد شماره
            bindingDirection.disabled = false
            bindingDirection.setAttribute('required', 'required')
        } else {
            bindingDirection.disabled = true
            bindingDirection.removeAttribute('required')
        }

    });



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

    


});