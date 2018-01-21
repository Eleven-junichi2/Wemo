from django import forms

from .models import Memo


class MemoCreateForm(forms.ModelForm):

    class Meta:
        model = Memo
        fields = ("memo_title", "memo_text")
        widgets = {
            "memo_title": forms.TextInput(
                attrs={"class": "w3-input w3-border"}),
            "memo_text": forms.Textarea(
                attrs={"class": "w3-input w3-border"}),
        }


class MemoUpdateForm(forms.ModelForm):

    class Meta:
        model = Memo
        fields = ("memo_title", "memo_text")
        widgets = {
            "memo_title": forms.TextInput(
                attrs={"class": "w3-input w3-border"}),
            "memo_text": forms.Textarea(
                attrs={"class": "w3-input w3-border"}),
        }
