from django.contrib import admin
from .models import Question,Choice,Bill,Department,WaterFee,GasFee,ElecFee,PropertyManageFee
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[
        (None,{'fields':['question_text']}),
        ('Date information',{'fields':['pub_date'],'classes':['collapse']})
    ]
    list_display = ('question_text','pub_date','was_published_recently')
    search_fields = ['question_text']



class GasFeeInLine(admin.TabularInline):
    model = GasFee
    extra = 1

class WaterFeeInLine(admin.TabularInline):
    model = WaterFee
    extra = 1

class ElecFeeInLine(admin.TabularInline):
    model = ElecFee
    extra = 1

class PropertyManageFeeInLine(admin.TabularInline):
    model = PropertyManageFee
    extra = 1

class  BillAdmin(admin.ModelAdmin):
    fieldsets =[
        ("User",{'fields':['bill_user']}),
        ("Date info",{'fields':['bill_date']}),
    ]
    inlines = [WaterFeeInLine,GasFeeInLine,ElecFeeInLine,PropertyManageFeeInLine]

class GasFeeAdmin(admin.ModelAdmin):
    fieldsets =[
        ('Departmet',{'fields':['department']}),
        ("time span",{'fields':['start_date','end_date'],'classes':'wide'}),
        ("Reading",{'fields':['start','end']}),
    ]

class WaterFeeAdmin(admin.ModelAdmin):
    fieldsets =[
        ('Departmet',{'fields':['department']}),
        ("time span",{'fields':['start_date','end_date'],'classes':'wide'}),
        ("Reading",{'fields':['start','end']}),
    ]

class ElecFeeAdmin(admin.ModelAdmin):
    fieldsets =[
        ('Departmet',{'fields':['department']}),
        ("time span",{'fields':['start_date','end_date'],'classes':'wide'}),
        ("Reading",{'fields':['start','end']}),
    ]
class PropertyManageFeeAdmin(admin.ModelAdmin):
    fieldsets =[
        ('Departmet',{'fields':['department']}),
        ("time span",{'fields':['start_date','end_date'],'classes':'wide'}),
    ]


admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Bill,BillAdmin)
admin.site.register(Department)
admin.site.register(WaterFee,WaterFeeAdmin)
admin.site.register(GasFee,GasFeeAdmin)
admin.site.register(ElecFee,ElecFeeAdmin)
admin.site.register(PropertyManageFee,PropertyManageFeeAdmin)

