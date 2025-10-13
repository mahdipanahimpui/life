from kavenegar import *

def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('64545054412F51657732476350447A326E56445A4B442F664E61794A30725A46417A63757236557A5676773D')
    
        params = {
            'sender': '2000660110',
            'receptor': phone_number,
            'message': f'کد تایید شما: {code} \n چاپ‌لِس، ChapLes.ir'
        }

        response = api.sms_send(params)
        print(response)
    
    except APIException as e:
        print(e)
    
    except HTTPException as e:
        print(e)
          


# python3 
# text = b'APIException[] ....'
# b.decode('utf-8')