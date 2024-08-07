# IntegrationAPI/integrationapi/payment.py

from paypalrestsdk import Payment

class PayPalAPI:
    def __init__(self, client_id, client_secret, mode="sandbox"):
        Payment.api_mode = mode
        Payment.client_id = client_id
        Payment.client_secret = client_secret

    def create_payment(self, amount, currency, description):
        try:
            payment = Payment({
                "intent": "sale",
                "payer": {"payment_method": "paypal"},
                "transactions": [{
                    "amount": {"total": amount, "currency": currency},
                    "description": description
                }]
            })
            if payment.create():
                return payment
            else:
                raise Exception(f"PayPal API Error: {payment.error['message']}")
        except Exception as e:
            raise Exception(f"PayPal API Error: {str(e)}")
