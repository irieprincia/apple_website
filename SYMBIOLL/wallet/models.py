from django.db import models
from django.conf import settings
from .errors import InsufficientBalance

class Wallet(models.Model):
    
    username= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    
    current_balance= settings.CURRENCY_STORE_FIELD(default=0)

    account_name = models.CharField(max_length=250)

    phone_number = models.IntegerField()

    created_at= models.DateTimeField(auto_now_add=True)

    def deposit(self, value):
        self.transaction_set.create(
            value= value,
            running_balance= self.current_balance + value
        )

        self.current_balance += value

        self.save()

    def withdraw(self, value):
        if value > self.current_balance:
            raise InsufficientBalance('Votre solde est insuffisant.')

        self.transaction_set.create(
            value= -value,
            running_balance= self.current_balance - value
        )

        self.current_balance -= value

        self.save()

    def transfer(self, wallet, value):

        self.withdraw(value)
        wallet.deposit(value)


class Transaction(models.Model):

    wallet = models.ForeignKey(Wallet, on_delete= models.CASCADE)

    value = settings.CURRENCY_STORE_FIELD(default=0)

    running_balance = settings.CURRENCY_STORE_FIELD(default=0)

    created_at = models.DateTimeField(auto_now_add=True)




# Create your models here.
