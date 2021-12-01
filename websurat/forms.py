from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from django.forms.fields import DateField
from websurat.models import Surat

class DateInput(forms.DateInput):
    input_type = 'date'

#class FormTanggal(forms.Form):
 #   tgl_surat = forms.DateField(widget=DateInput)

class FormSuratKeluar(ModelForm):
    

    class Meta:
        model = Surat
        fields = '__all__'

        widgets={
            'tgl_surat': forms.TextInput({'class':'form-control'}),
            'nomor_surat':forms.TextInput({'class':'form-control'}),
            'jenis_surat':forms.TextInput({'class':'form-control'}),
            'tujuan':forms.TextInput({'class':'form-control'}),
            'perihal':forms.TextInput({'class':'form-control'}),
            'mengetahui':forms.TextInput({'class':'form-control'}),
            'arsip':forms.TextInput({'class':'form-control'}),
            #'ket':forms.Select({'class':'form-control'})
            'ket':forms.TextInput({'class':'form-control'}),
        }