from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class PayPal(PaymentGateway):
    def pay(self, amount):
        print(f"Paying ${amount} using PayPal")

class Stripe(PaymentGateway):
    def pay(self, amount):
        print(f"Paying ${amount} using Stripe")

class PaymentProcessor:
    def __init__(self, payment_gateway: PaymentGateway):
        self.payment_gateway = payment_gateway

    def pay(self, amount):
        self.payment_gateway.pay(amount)
        paypal = PayPal()
stripe = Stripe()

processor_paypal = PaymentProcessor(paypal)
processor_stripe = PaymentProcessor(stripe)

processor_paypal.pay(100)  
processor_stripe.pay(100)  
