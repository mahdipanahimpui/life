document.addEventListener('DOMContentLoaded', function() {




    // مدیریت آپلود فایل

    const frontFileUpload = document.getElementById('frontFileUpload');
    const frontFileInput = document.getElementById('frontFileInput');
    const frontFileNames = document.getElementById('frontFileNames');

// -----------------------------------------------------------------------
    frontFileUpload.addEventListener('click', function() {
        frontFileInput.click();
    });
    
    frontFileInput.addEventListener('change', function() {
        if(this.files.length > 0) {
            let names = '';
            for(let i = 0; i < this.files.length; i++) {
                names += this.files[i].name + '<br>';
            }
            frontFileNames.innerHTML = names;
        } else {
            frontFileNames.innerHTML = '';
        }
    });
    
    // امکان کشیدن و رها کردن فایل
    frontFileUpload.addEventListener('dragover', function(e) {
        e.preventDefault();
        this.style.borderColor = '#4a6cf7';
        this.style.backgroundColor = '#f0f5ff';
    });
    
    frontFileUpload.addEventListener('dragleave', function(e) {
        e.preventDefault();
        this.style.borderColor = '#ddd';
        this.style.backgroundColor = '#f8faff';
    });
    
    frontFileUpload.addEventListener('drop', function(e) {
        e.preventDefault();
        this.style.borderColor = '#4a6cf7';
        this.style.backgroundColor = '#f8faff';
        
        if(e.dataTransfer.files.length > 0) {
            frontFileInput.files = e.dataTransfer.files;
            let names = '';
            for(let i = 0; i < e.dataTransfer.files.length; i++) {
                names += e.dataTransfer.files[i].name + '<br>';
            }
            frontFileNames.innerHTML = names;
        }
    });
    
// ---------------------------------------------------------------------
    const backFileUpload = document.getElementById('backFileUpload');
    const backFileInput = document.getElementById('backFileInput');
    const backFileNames = document.getElementById('backFileNames');

    backFileUpload.addEventListener('click', function() {
        backFileInput.click();
    });

    backFileInput.addEventListener('change', function() {
        if(this.files.length > 0) {
            let names = '';
            for(let i = 0; i < this.files.length; i++) {
                names += this.files[i].name + '<br>';
            }
            backFileNames.innerHTML = names;
        } else {
            backFileNames.innerHTML = '';
        }
    });

    // امکان کشیدن و رها کردن فایل
    backFileUpload.addEventListener('dragover', function(e) {
        e.preventDefault();
        this.style.borderColor = '#4a6cf7';
        this.style.backgroundColor = '#f0f5ff';
    });

    backFileUpload.addEventListener('dragleave', function(e) {
        e.preventDefault();
        this.style.borderColor = '#ddd';
        this.style.backgroundColor = '#f8faff';
    });

    backFileUpload.addEventListener('drop', function(e) {
        e.preventDefault();
        this.style.borderColor = '#4a6cf7';
        this.style.backgroundColor = '#f8faff';
        
        if(e.dataTransfer.files.length > 0) {
            backFileInput.files = e.dataTransfer.files;
            let names = '';
            for(let i = 0; i < e.dataTransfer.files.length; i++) {
                names += e.dataTransfer.files[i].name + '<br>';
            }
            backFileNames.innerHTML = names;
        }
    });

// ---------------------------------------------------------------------

    // const fileUpload = document.getElementById('fileUpload');
    // const fileInput = document.getElementById('fileInput');
    // const fileNames = document.getElementById('fileNames');

    // fileUpload.addEventListener('click', function() {
    //     fileInput.click();
    // });
    
    // fileInput.addEventListener('change', function() {
    //     if(this.files.length > 0) {
    //         let names = '';
    //         for(let i = 0; i < this.files.length; i++) {
    //             names += this.files[i].name + '<br>';
    //         }
    //         fileNames.innerHTML = names;
    //     } else {
    //         fileNames.innerHTML = '';
    //     }
    // });
    
    // // امکان کشیدن و رها کردن فایل
    // fileUpload.addEventListener('dragover', function(e) {
    //     e.preventDefault();
    //     this.style.borderColor = '#4a6cf7';
    //     this.style.backgroundColor = '#f0f5ff';
    // });
    
    // fileUpload.addEventListener('dragleave', function(e) {
    //     e.preventDefault();
    //     this.style.borderColor = '#ddd';
    //     this.style.backgroundColor = '#f8faff';
    // });
    
    // fileUpload.addEventListener('drop', function(e) {
    //     e.preventDefault();
    //     this.style.borderColor = '#4a6cf7';
    //     this.style.backgroundColor = '#f8faff';
        
    //     if(e.dataTransfer.files.length > 0) {
    //         fileInput.files = e.dataTransfer.files;
    //         let names = '';
    //         for(let i = 0; i < e.dataTransfer.files.length; i++) {
    //             names += e.dataTransfer.files[i].name + '<br>';
    //         }
    //         fileNames.innerHTML = names;
    //     }
    // });

});