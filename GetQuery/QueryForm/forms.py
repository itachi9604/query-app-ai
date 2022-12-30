from django import forms

LANGUAGE_CHOICES = (
    ('python', 'Python'),
    ('cpp', 'C++'),
    ('c', 'C'),
    ('java', 'Java'),
    ('dart', 'Dart')
)


class QueryFormInputs(forms.Form):
    syntax_for = forms.CharField(max_length=255)
    in_language = forms.ChoiceField(choices=LANGUAGE_CHOICES)
