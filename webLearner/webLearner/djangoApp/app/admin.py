from django.contrib import admin
from .model import PasswordPool
from .model import Homework2
from .model import SimpleBlog
from .model import FinalGrade
#from .models import Author
# Register your models here.
admin.site.register(PasswordPool)
admin.site.register(Homework2)
admin.site.register(SimpleBlog)
admin.site.register(FinalGrade)