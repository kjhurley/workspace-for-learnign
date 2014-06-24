from django.contrib import admin
import polls.models
# Register your models here.

# use tabular inline baseclass to get a nice uncluttered set of input fields
class ChoiceInline(admin.TabularInline):
    model = polls.models.Choice
    extra = 3 # make room for 3 choices on the admin page

class QuestionAdmin(admin.ModelAdmin):
    fieldsets =[
                (None,{'fields':['question_text']}),
                ('Data information',{'fields':['pub_date'],'classes':['collapse']}),
                ]
    inlines = [ChoiceInline]
    list_display = ('question_text','pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(polls.models.Question, QuestionAdmin)
#admin.site.register(polls.models.Choice)




