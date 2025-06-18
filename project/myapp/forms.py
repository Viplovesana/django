from django import forms
from .models import Student
from django.core.exceptions import ValidationError
import re


#Create your models here.....

# class Studentform(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = '__all__'

class Studentform(forms.Form):
    name = forms.CharField()
    email=forms.EmailField()
    contact=forms.CharField()
    image=forms.ImageField()
    document=forms.FileField() 

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.replace(" ", "").isalpha() :
            raise ValidationError("Name should only contain letters and spaces.")
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.lower().endswith(('@gmail.com','@yahoo.com')):
            raise ValidationError("Only gmail and yahoo addresses are allowed.")
        
        return email

    def clean_contact(self):
        contact = self.cleaned_data.get('contact')
        if not len(contact)==10:
            raise ValidationError("Contact must be a 10-digit number.")
        return contact

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image and image.size > 10 * 1024 * 1024:
            raise ValidationError("Image size should not exceed 2MB.")
        elif image and not image.name.lower().endswith(('.jpeg', '.png','jpg')):
            raise ValidationError("Image must be either .jpeg or .png")
        return image

    def clean_document(self):
        document = self.cleaned_data.get('file')
        if document and not document.name.lower().endswith(('.pdf','.doc','.docx')):
            raise ValidationError("Only PDF.DOC and DOCX files are allowed.")
        return document



    
   #////////////////////////////another method of validation but wrong method/////////////////////////////////
    # def clean(self):
    #     cleaned_data = super().clean()
    #     name = cleaned_data.get('name')
    #     email =cleaned_data.get('email')
    #     contact = cleaned_data.get('contact')
    #     image = cleaned_data.get('image')
    #     document = cleaned_data.get('document')
        

    #     if name and not name.replace(" ", "").isalpha() :
    #         raise ValidationError("Name should only contain letters and spaces.")
        
    #     if email and not email.lower().endswith(('@gmail.com','@yahoo.com')):
    #         raise ValidationError("Only gmail and yahoo addresses are allowed.")
        
    #     if contact and not len(contact)==10:
    #         raise ValidationError("Contact must be a 10-digit number.")
        
    #     if image:
    #         if image.size > 2 * 1024 * 1024:
    #           raise ValidationError("Image size should not exceed 2MB.")
    #         elif image and not image.name.lower().endswith(('.jpeg', '.png','jpg')):
    #           raise ValidationError("Image must be either .jpeg or .png")

    #     if document and not document.name.lower().endswith(('.pdf','.doc','.docx')):
    #           raise ValidationError("Only PDF.DOC and DOCX files are allowed.")
        










class StudentLoginform(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['email','contact']
    


