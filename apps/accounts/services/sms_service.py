import requests
from django.conf import settings


def send_sms_ir(mobile, code):

    mobile_input = mobile # Store original input for logging if needed
    mobile = mobile.strip()

    # Normalize Mobile
    if mobile.startswith('09'):
        normalized_mobile = mobile
    elif mobile.startswith('+989'):
        normalized_mobile = mobile[1:] # Remove '+'
    elif mobile.startswith('989'):
        normalized_mobile = mobile
    else:
        print(f"WARNING: Unexpected mobile number format: {mobile_input}. Proceeding with original format.")
        normalized_mobile = mobile_input

    url = "https://api.sms.ir/v1/send/verify"

    payload = {
        "mobile": normalized_mobile,
        "templateId": int(settings.SMS_IR_VERIFY_TEMPLATE_ID),
        "parameters": [
            {
                "name": "Code",
                "value": str(code)
            }
        ]
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "text/plain",
        "x-api-key": settings.SMS_IR_API_KEY,
        # "x-api-key": api_key,
    }

    try:
        r = requests.post(url, json=payload, headers=headers, timeout=20)

        print("==== SMS.IR VERIFY REQUEST ====")
        print("URL:", url)
        print("HEADERS:", headers)
        print("PAYLOAD:", payload)

        print("==== SMS.IR VERIFY RESPONSE ====")
        print("STATUS:", r.status_code)
        print("BODY:", r.text)

        if r.status_code == 200:
            data = r.json()
            return data.get("status") == 1

        return False

    except requests.RequestException as e:
        print("VERIFY SMS ERROR:", str(e))
        return False


# __________________________________________________________________________
def send_activation_sms(mobile, code):
    result = send_sms_ir(mobile, code)

    return True if result else False
