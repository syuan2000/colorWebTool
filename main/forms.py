from django import forms

'''
so the good thing with django is that we don't need to make the html elements like
name field, button
the forms will automatically generate those for us.
'''

class CreateNewList(forms.Form):
    name = forms.CharField(label='Name', max_length=200)
    check = forms.BooleanField(required=False)

