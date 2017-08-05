from django import forms


class SimpleContactForm(forms.Form):
    contact_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Your name',
                                                                                'class': 'form-control'}))
    contact_email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                                   'placeholder': 'Your email'}))
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control',
                                     'placeholder': 'Content'})
    )


class InterestsForm(forms.Form):
    contact_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Your name',
                                                                                'class': 'form-control'}))
    contact_email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                                   'placeholder': 'Your email'}))
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control',
                                     'placeholder': 'Content'})
    )

    course_and_university = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Course and University'})
    )

    deadline = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))


class ProposalForm(forms.Form):
    contact_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Your name',
                                                                                'class': 'form-control'}))
    contact_email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                                   'placeholder': 'Your email'}))
    organisation = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Your organisation'})
    )
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Thesis title',
                                                                         'class': 'form-control'}))
    description = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control',
                                     'placeholder': 'Thesis description'})
    )

    why_important = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control',
                                     'placeholder': 'Why is it important?'})
    )

    sources = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control',
                                     'placeholder': 'Sources'})
    )

    deadline = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control',
                                     'placeholder': 'Is there anything else you '
                                                    'would like to inform us about?'})
    )
