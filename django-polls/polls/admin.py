from django.contrib import admin

# Register your models here.
from .models import Question, Choice

"""
#admin.StackedInline
this param is  as  a stacked structuction to show the param
"""


class ChoiceInline(admin.TabularInline):
    #this is the Model for  children items
    model = Choice
    #empty items number for the future slots
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    # this decide the order of param key
    fields = ["pub_date", "question_text"]
    # fieldset  is higher level  config for
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes':['collapse']})
    ]
    # show the key inline
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # provide the filter for pub_date
    list_filter = ['pub_date']
    # provide a search bar for key
    search_fields = ['question_text']


# regist the Question and  manual setting param for QuestionAdmin
admin.site.register(Question, QuestionAdmin)

# this the most easy way to implement children items
# admin.site.register(Choice)
