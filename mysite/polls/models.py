from django.db import models
from django.utils import  timezone
from django.contrib.auth.models import  User
import datetime
# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateField("pub_date")
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
       # return  timezone.now()>=self.pub_date >=timezone.now() -datetime.timedelta(days=1)
        return timezone.now().year >=self.pub_date.year;


class Choice(models.Model):
    question=models.ForeignKey(Question)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


class Bill(models.Model):
    #bill
    bill_date=models.DateField("bill date")
    #set up department- bill one to many relationship
    bill_user =models.ForeignKey(User)
    #seriable
    def __str__(self):
        return "%s,%s" %(self.bill_user.username,self.bill_date)



class  Department(models.Model):
    #model for house department
    bill=models.OneToOneField(Bill)
    #basic location  three level address
    area=models.IntegerField(default=0)
    #basic information
    #properte management


class WaterFee(models.Model):
     #name
    name=models.CharField(max_length=100,default="water")
    #setup department -GasFee relationship
    bill=models.OneToOneField(Bill)
    #start date
    start_date=models.DateField("start date")
    #end date
    end_date=models.DateField("end date")
     #start reading
    start=models.IntegerField(default=0)
    #end reading
    end=models.IntegerField(default=0)
    def __str__(self):
         return "%s:[%s-%s]" % (self.name,self.start_date,self.end_date)
    def tolls(self):
        print("water fee")
        print((self.end-self.start)%23)
        return 2.3*((self.end-self.start)%23)+3.45*((self.end-self.start)%31-(self.end-self.start)%23)+4.6*((self.end-self.start)-(self.end-self.start)%31)

class GasFee(models.Model):
     #name
    name=models.CharField(max_length=100,default="gas")
    #setup department -GasFee relationship
    bill=models.OneToOneField(Bill)
    #start date
    start_date=models.DateField("start date")
    #end date
    end_date=models.DateField("end date")
     #start reading
    start=models.IntegerField(default=0)
    #end reading
    end=models.IntegerField(default=0)

    def __str__(self):
         return "%s:[%s-%s]" % (self.name,self.start_date,self.end_date)
    def tolls(self):
        print(self.end_date.month);
        return ((self.end-self.start)%35)*3.5+((self.end-self.start)-(self.end-self.start)%35)*4;

class ElecFee(models.Model):
    #name
    name=models.CharField(max_length=100,default="electricity")
    #setup department -GasFee relationship
    bill=models.OneToOneField(Bill)
    #start date
    start_date=models.DateField("start date")
    #end date
    end_date=models.DateField("end date")
     #start reading
    start=models.IntegerField(default=0)
    #end reading
    end=models.IntegerField(default=0)

    def __str__(self):
         return "%s:[%s-%s]" % (self.name,self.start_date,self.end_date)
    def tolls(self):
        #calc electricity fee
        return 0.68*(self.end-self.start)

class PropertyManageFee(models.Model):
    #name
    name=models.CharField(max_length=100,default="propertymanage")
    #setup department -GasFee relationship
    bill=models.OneToOneField(Bill)
    #start date
    start_date=models.DateField("start date")
    #end date
    end_date=models.DateField("end date")
    #housing services
    houseService=models.IntegerField(default=0)
    #manatance
    maintenance=24.26;

    def __str__(self):
        return "%s:[%s-%s]" % (self.name,self.start_date,self.end_date)
    def tolls(self):
        return 223.19+self.maintenance+self.houseService








