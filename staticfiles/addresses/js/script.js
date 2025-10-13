    // داده‌های مراکز استان‌ها برای نقشه
    // const provinceCenters = {
    //     'tehran': [35.6892, 51.3890], // تهران
    //     'alborz': [35.9961, 50.6614], // کرج
    //     'isfahan': [32.6546, 51.6680], // اصفهان
    //     'fars': [29.5918, 52.5837], // شیراز
    //     'khorasan-razavi': [36.2605, 59.6168], // مشهد
    //     'azarbaijan-sharghi': [37.9036, 46.2681], // تبریز
    //     'azarbaijan-gharbi': [37.5527, 45.0759], // ارومیه
    //     'kermanshah': [34.3142, 47.0650], // کرمانشاه
    //     'khozestan': [31.3183, 48.6706], // اهواز
    //     'gilan': [37.2808, 49.5832], // رشت
    //     'mazandaran': [36.5658, 53.0588], // ساری
    //     'golestan': [37.2896, 55.1376], // گرگان
    //     'kordestan': [35.3219, 46.9862], // سنندج
    //     'hamadan': [34.7989, 48.5150], // همدان
    //     'markazi': [33.9811, 50.8639], // اراک
    //     'lorestan': [33.4871, 48.3539], // خرم‌آباد
    //     'qom': [34.6416, 50.8806], // قم
    //     'yazd': [31.8974, 54.3569], // یزد
    //     'kerman': [30.2839, 57.0834], // کرمان
    //     'hormozgan': [27.1836, 56.2666], // بندرعباس
    //     'sistan': [29.4917, 60.8648], // زاهدان
    //     'bushehr': [28.9234, 50.8203], // بوشهر
    //     'zanjan': [36.6769, 48.4963], // زنجان
    //     'ardabil': [38.2493, 48.2963], // اردبیل
    //     'qazvin': [36.2797, 50.0049], // قزوین
    //     'chaharmahal': [32.3256, 50.8644], // شهرکرد
    //     'semnan': [35.5769, 53.3920], // سمنان
    //     'kohgiluyeh': [30.6680, 51.6000], // یاسوج
    //     'ilam': [33.2959, 46.6705], // ایلام
    //     'north-khorasan': [37.4751, 57.3305], // بجنورد
    //     'south-khorasan': [32.8649, 59.2262] // بیرجند
    // };

    // نقشه و موقعیت‌یابی
    let map, marker, defaultLocation = [35.6892, 51.3890]; // تهران
    

    document.addEventListener('DOMContentLoaded', function() {
        // مقداردهی اولیه نقشه
        initMap();
        
            
        
        // اعتبارسنجی کد پستی
        document.getElementById('postalCode').addEventListener('input', function() {
            this.value = this.value.replace(/\D/g, '');
            if (this.value.length > 10) {
                this.value = this.value.slice(0, 10);
            }
        });
        
        
        // اضافه کردن event listener برای جستجو با دکمه Enter
        document.getElementById('mapSearch').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                e.preventDefault();
                searchLocation();
            }
        });
    });

    // تابع مقداردهی نقشه
    function initMap() {
        map = L.map('addressMap').setView(defaultLocation, 13);
        
        // اضافه کردن لایه نقشه OpenStreetMap
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
            maxZoom: 18
        }).addTo(map);
        
        // اضافه کردن نشانگر
        marker = L.marker(defaultLocation, {
            draggable: true,
            autoPan: true
        }).addTo(map);
        

        // // تنظیم موقعیت اولیه بر اساس موقعیت کاربر (در صورت مجوز)
        // if (navigator.geolocation) {
        //     navigator.geolocation.getCurrentPosition(
        //         function(position) {
        //             const userLocation = [position.coords.latitude, position.coords.longitude];
        //             map.setView(userLocation, 15);
        //             marker.setLatLng(userLocation);
        //             updateMarkerPosition();
        //         },
        //         function(error) {
        //         }
        //     );
        // }
        
        const latInput = document.getElementById('lat');
        const lngInput = document.getElementById('lng');
        let initialLocation = defaultLocation;

        if (latInput && lngInput && latInput.value && lngInput.value) {
            // استفاده از مقادیر موجود در inputها
            initialLocation = [parseFloat(latInput.value), parseFloat(lngInput.value)];
            map.setView(initialLocation, 15);
            marker.setLatLng(initialLocation);
            updateMarkerPosition();
        } else if (navigator.geolocation) {
            // درخواست مجوز لوکیشن کاربر
            navigator.geolocation.getCurrentPosition(
                function(position) {
                    const userLocation = [position.coords.latitude, position.coords.longitude];
                    map.setView(userLocation, 15);
                    marker.setLatLng(userLocation);
                    updateMarkerPosition();
                },
                function(error) {
                    console.log('دسترسی به موقعیت مکانی امکان‌پذیر نیست:', error);
                }
            );
        }

        // رویداد برای زمانی که نشانگر حرکت می‌کند
        marker.on('dragend', function() {
            updateMarkerPosition();
        });
        
        // رویداد برای کلیک روی نقشه
        map.on('click', function(e) {
            marker.setLatLng(e.latlng);
            updateMarkerPosition();
        });
    }
    
    // تابع جستجوی مکان
    function searchLocation() {
        const query = document.getElementById('mapSearch').value;
        if (!query) {
            alert('لطفا یک آدرس یا نام مکان را وارد کنید.');
            return;
        }
        
        // استفاده از Nominatim API برای جستجوی مکان
        fetch(`https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(query)}&accept-language=fa`)
            .then(response => response.json())
            .then(data => {
                if (data && data.length > 0) {
                    const result = data[0];
                    const lat = parseFloat(result.lat);
                    const lon = parseFloat(result.lon);
                    
                    map.setView([lat, lon], 15);
                    marker.setLatLng([lat, lon]);
                    updateMarkerPosition();
                    
                    // نمایش نام مکان پیدا شده
                    document.getElementById('mapSearch').value = result.display_name;
                } else {
                    alert('مکانی یافت نشد. لطفا عبارت جستجوی خود را تغییر دهید.');
                }
            })
            .catch(error => {
                console.error('خطا در جستجوی مکان:', error);
                alert('خطا در جستجوی مکان. لطفا دوباره تلاش کنید.');
            });
    }
    
    
    // تابع به‌روزرسانی موقعیت نشانگر
    function updateMarkerPosition() {
        const position = marker.getLatLng();
        document.getElementById('lat').value = position.lat;
        document.getElementById('lng').value = position.lng;

        // در اینجا می‌توانید موقعیت را ذخیره یا استفاده کنید
    }