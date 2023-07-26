from django import forms

class CreateNewRating(forms.Form):
    course = forms.CharField(label="Course", max_length=100)
    rating = forms.IntegerField(label="Rating", min_value=1, max_value=10)
    comment = forms.CharField(label="Comment", max_length=1000)