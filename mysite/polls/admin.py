from django.contrib import admin
from .models import Question,Choice
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[
        (None,{'fields':['question_text']}),
        ('Date information',{'fields':['pub_date'],'classes':['collapse']})
    ]
    list_display = ('question_text','pub_date','was_published_recently')
    search_fields = ['question_text']

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
