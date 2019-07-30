from django.db import models
from django.contrib.auth.models import User
from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	balance = models.FloatField(default=100.0)
	account_type = models.BooleanField(default=False)
	privateKey = models.CharField(max_length=1028, default='0')
	publicKey = models.CharField(max_length=1028, default='0')

	def gen_key_pair(self):
		key = rsa.generate_private_key(
    	backend=crypto_default_backend(),
    	public_exponent=65537,
  	 	key_size=1028
		)	
		self.privateKey = key.private_bytes(
    	crypto_serialization.Encoding.PEM,
    	crypto_serialization.PrivateFormat.PKCS8,
    	crypto_serialization.NoEncryption())
		
		self.publicKey = key.public_key().public_bytes(
    		crypto_serialization.Encoding.OpenSSH,
    		crypto_serialization.PublicFormat.OpenSSH
		)

		self.save()