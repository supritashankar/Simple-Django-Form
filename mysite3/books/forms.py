from models import Publisher
from django.forms import ModelForm


class PublisherForm(ModelForm):
     class Meta:
         model = Publisher
