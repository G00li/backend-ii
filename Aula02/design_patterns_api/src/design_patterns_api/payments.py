from abc import ABC
from typing import Protocol

def PaypalPayment():
    pass

def GooglePayPayment():
    pass

def ApplePayPayment():
    pass

def MbwayPayment():
    pass


class PaymentService(Protocol):
    def process(*args, **kwargs):
        return NotImplemented



class PaypalService(PaymentService):
    def process(*args, **kwargs):
        return "Paypal"
    
    

class ApplePayService(PaymentService):
    def process(*args, **kwargs):
        return "Apple Pay"
        

class PaymentGateway:

    registry = {
        "paypal": PaypalService,
        "apple_pay": ApplePayService,
    }

    @classmethod
    def build(cls, method: str) -> PaymentService:
        return cls.registry.get(method, None)()
