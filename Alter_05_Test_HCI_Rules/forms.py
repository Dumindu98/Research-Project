import os
from django import forms
from .models import Rule


class UploadRuleForm(forms.ModelForm):

    ACCESS_TYPES = (
        ('global', 'For Public Use'),
        ('test', 'For Personal Use')
    )

    RULE_CATEGORIES = (
        ('cp', 'Colour Perception'),
        ('pf', 'Perceptual Fluency'),
        ('vg', 'Visual Guidance'),
        ('ac', 'Accessibility')
    )

    title = forms.CharField(label='Rule Name', max_length=50)
    description = forms.CharField(label='Rule Description', max_length=200)
    rule_file = forms.FileField(label='Source File')
    documentation = forms.FileField(label='HCI Advice Documentation')
    tooltip_image = forms.FileField(label='Description Image')
    access_type = forms.RadioSelect(choices=ACCESS_TYPES)
    category = forms.ChoiceField(label='Rule Category', choices=RULE_CATEGORIES)
    rule_name = forms.CharField(required=False)
    image_type = forms.CharField(label='Image MemeType', max_length=50, required=False)
    expand_description = forms.CharField(label='Rule Introduction', max_length=200)

    def clean_rule_name(self):
        name = self.cleaned_data['rule_name']
        print("rule name: ", name)
        return name

    def clean_rule_file(self):
        file = self.cleaned_data['rule_file']
        ext = os.path.splitext(file.name)[1].strip()
        valid_extenstions = ['.py']
        if not ext in valid_extenstions:
            raise forms.ValidationError('Source File (Rule) can upload only with python format.')
        return file

    def clean_documentation(self):
        file = self.cleaned_data['documentation']
        ext = os.path.splitext(file.name)[1].strip()
        valid_extenstions = ['.pdf']
        if not ext in valid_extenstions:
            raise forms.ValidationError('Documentation can upload only with pdf format.')
        return file

    def clean_tooltip_image(self):
        file = self.cleaned_data['tooltip_image']
        ext = os.path.splitext(file.name)[1].strip()
        valid_extenstions = ['.jpg', '.png', 'jpeg']
        if not ext in valid_extenstions:
            raise forms.ValidationError('Invalid Image format!')
        return file

    class Meta:
        model = Rule
        fields = ['title', 'description', 'category', 'access_type', 'rule_name', 'image_type', 'expand_description']
