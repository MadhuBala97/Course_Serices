from django.db import models
class Contact(models.Model):
	p_id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	subject=models.CharField(max_length=100)
	message=models.CharField(max_length=100)
	def _str_(self):
	    return self.name 
class Register(models.Model):
	p_id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	phoneno=models.CharField(max_length=100)
	image=models.ImageField(upload_to='pics/')
	def _str_(self):
	    return self.name
class Feedback(models.Model):
	p_id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	phoneno=models.CharField(max_length=100)
	feedback=models.CharField(max_length=100)
	def _str_(self):
	    return self.name

class Addservice(models.Model):
	p_id=models.AutoField(primary_key=True)
	stitle=models.CharField(max_length=100)
	sdescribe=models.CharField(max_length=100)
	sprice=models.CharField(max_length=100)
	sduration=models.CharField(max_length=100)
	mcharges=models.CharField(max_length=100)
	def _str_(self):
	    return self.stitle
class Addfeedback(models.Model):
	p_id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	phoneno=models.CharField(max_length=100)
	feedback=models.CharField(max_length=100)
	def _str_(self):
	    return self.name
# Create your models here.
