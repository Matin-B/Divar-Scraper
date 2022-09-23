import requests
import config

def send_verification_code(phone_number: int) -> int:
    """
    Send verification code to phone number
    
    :param phone_number: The phone number you want to send the code to
    :type phone_number: int
    """
    data = '{"phone":"%s"}' % (phone_number)

    requests.post(
        'https://api.divar.ir/v5/auth/authenticate',
        headers=config.authenticate_headers,
        data=data
    ).status_code


def authenticate(phone_number: int, verification_code: int) -> str:
    """
    It takes a phone number and a verification code and returns a token.
    Authenticate 
    
    :param phone_number: The phone number you want to send the verification code to
    :type phone_number: int
    :param verification_code: The code you received from the SMS
    :type verification_code: int
    :return: A token
    """
    data = '{"phone":"%s","code":"%s"}' % (phone_number, verification_code)
    response = requests.post(
        'https://api.divar.ir/v5/auth/confirm',
        headers=config.authenticate_headers,
        data=data
    )
    return response.json()["token"]


send_verification_code(9382093203)
token = authenticate(9382093203, 45654)
cookies = {
    'did': '81ab5585-f4a6-457c-b741-8e0a2b51c682',
    
    'city': 'isfahan',
    'token': token,
}



