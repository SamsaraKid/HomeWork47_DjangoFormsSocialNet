from django import forms

class regform(forms.Form):
    name = forms.CharField(label='Имя')
    ages = (('детский',     '0-12 лет'),
            ('юный',        '13-21 лет'),
            ('молодой',     '22-30'),
            ('средний',     '31-40 лет'),
            ('зрелый',      '41-55 лет'),
            ('пожилой',     '56-70 лет'),
            ('старческий',  '60+ лет'))
    age = forms.TypedChoiceField(choices=ages)
    langs = (('русский', 'Русский'), ('английский', 'English'), ('китайский', '中文'))
    lang = forms.TypedChoiceField(choices=langs)