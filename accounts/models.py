from django.db import models
from django.core.validators import RegexValidator
select_state = (
    ("new york", "New York"),
    ("california", "California"),
    ("iiiinois", "IIIinois"),
    ("texas", "Texas"),
    ("arizona", "Arizona"),
    ("massachusetts", "Massachusetts"),
    ("nevada", "Nevada"),
    ("south carolina", "South Carolina"),   
)
# Create your models here.
class Blog(models.Model):
    # error_css_class = 'error'
    #Id = models.PositiveSmallIntegerField()
    Name = models.CharField(max_length=200)
    Advocate = models.CharField(max_length=200)
    Mobile = models.PositiveBigIntegerField()
    Email = models.EmailField(unique=True)
    Mobile_Updates= models.BooleanField(default=False)
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    CaseNo = models.CharField(max_length=50, blank=True, null=True, validators=[alphanumeric])
    #numeric = RegexValidator(r'^[0-9+]', 'Only digit characters.')
    CaseYear = models.PositiveBigIntegerField()
    #models.CharField(max_length=500, blank=True, validators=[numeric])
    CaseType = models.CharField(max_length=200)
    CourtName = models.CharField(max_length=200)    
    #gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    #CourtArea = models.TextField(max_length=300,null=True,blank = True)
    CourtArea = models.CharField(max_length=30,choices=select_state,default='new york')
    #email = models.EmailField(max_length=50, unique=True, validators=[alphanumeric])
    # Start_Date = models.DateField()
    # End_Date = models.DateField()
    Created_By = models.CharField(max_length=200)
    Created_Date = models.DateTimeField() 
    Modified_By = models.CharField(max_length=200)
    Modified_Date = models.DateTimeField() 
    user_email = models.CharField(max_length=200)
    class Meta:
        db_table = 'blog'
