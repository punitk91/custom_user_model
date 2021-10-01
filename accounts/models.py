from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class MyAccountManger(BaseUserManager):
    def create_user(self,first_name, last_name, username, email, password = None):
        if not email:
            raise ValueError('user must have an email address ')
        
        if not user:
            raise ValueError('user must have an user name ')
        
        user = self.model(
            email = self.normalize_email(email),
            username  = username,
            first_name = first_name,
            last_name = last_name,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user 
    
    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password=password,
            first_name = first_name,
            last_name = last_name,
            
        )
        
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self.db)
        return user
        
        

class Account(AbstractBaseUser):
    #unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100,unique=True)
    email = models.CharField(max_length=100,unique=True)
    region = 
    phone_number = models.CharField(max_length=100,unique=True)
    date_joined = models.CharField(auto_true_now=True)
    last_login = models.DateTimeField(auto_add_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    
    
    username_FIELD = 'uuid'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    objects = MyAccountManger()
    
    
    def __str__(self):
        return self.email
    
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    
    def has_module_perms(self, add_label):
        return True


#Putting this in the same page for now we can put in seprate structure 

class RegionMasterTable(models.model):
    region_id = models.AutoField(primary_key=True,unique=True)
    region_name = models.CharField(max_length=200,null= True)
    region_code = models.CharField(max_length=1000,null=True, blank=True)
    
    def __str__(self):
        return self.region_name

class RegionMappingUser(models.model):
    region_user = models.OneToOneField(Account,default=None, on_delete=models.CASCADE)
    region = models.ForeignKey(RegionMasterTable, default=None,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.region_user)
    
