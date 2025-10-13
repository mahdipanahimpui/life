document.addEventListener('DOMContentLoaded', function() {
    const otpInput = document.getElementById('otp');
    const verifyOtpBtn = document.getElementById('verifyOtpBtn');
    const resendBtn = document.getElementById('resendBtn');
    const countdownEl = document.getElementById('countdown');


    resendBtn.addEventListener('click', function() {
        window.location.href = this.dataset.url;
    });  
      
    let countdown;
    let timeLeft = 120; // 2 minutes in seconds
    

    
    // مدیریت ورودی OTP
    otpInput.addEventListener('input', function() {
        // فقط اعداد مجاز هستند
        this.value = this.value.replace(/[^0-9]/g, '');
        
        if (this.value.length === 5) {
            this.classList.add('filled');
        } else {
            this.classList.remove('filled');
        }
        
        // بررسی آیا فیلد پر شده است
        verifyOtpBtn.disabled = this.value.length !== 5;
    });
    

    

    
    // شروع تایمر
    function startCountdown() {
        resendBtn.disabled = true;
        updateCountdown();
        
        countdown = setInterval(() => {
            timeLeft--;
            updateCountdown();
            
            if (timeLeft <= 0) {
                clearInterval(countdown);
                resendBtn.disabled = false;
                countdownEl.textContent = '';
            }
        }, 1000);
    }
    
    // به‌روزرسانی تایمر
    function updateCountdown() {
        const minutes = Math.floor(timeLeft / 60);
        const seconds = timeLeft % 60;
        countdownEl.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    }
    
    
    // شروع تایمر هنگام لود صفحه
    startCountdown();
    
    // فوکوس روی input
    otpInput.focus();
});