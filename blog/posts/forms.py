from .models import Post
from django.forms import ModelForm

class postForm(ModelForm):
  class Meta:
    model=Post
    # fields='__all__'
   # specify fields to be used
    
    fields = [
      "title",
      "body",
      "images",
      "created_at",
    ]