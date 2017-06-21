from django import forms

PUBLISH_CHOICES = (
    ('', ''),
    ('publish', 'Publish'),
    ('draft', 'Draft'),
)

class ProductForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField()
    publish = forms.ChoiceField(choices=PUBLISH_CHOICES, required=False)
    # class Meta:
    #     fields = [
    #         'title',
    #         'description',
    #         'price',
    #     ]

    # clean is from django
    # clean_<field_name> clean specific field
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 1:
            raise forms.ValidationError('Price Must Be Higher than 1')
        else:
            return price

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) <=3:
            raise forms.ValidationError('Title too small')
        else:
            return title
