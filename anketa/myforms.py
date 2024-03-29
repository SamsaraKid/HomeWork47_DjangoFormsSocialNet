from django import forms

class RegForm(forms.Form):
    email = forms.EmailField(label='E-mail', initial='q@e.ru')

    name = forms.CharField(label='Имя', initial='q')
    surname = forms.CharField(label='Фамилия', initial='q')
    secondname = forms.CharField(label='Отчество (при наличии)', required=False)

    sexes = (('мужской', '♂️ 	'), ('женский', '♀️ 	'))
    sex = forms.ChoiceField(label='Пол', choices=sexes)

    ages = (('детский',     '0-12 лет'),
            ('юный',        '13-21 лет'),
            ('молодой',     '22-30 лет'),
            ('средний',     '31-40 лет'),
            ('зрелый',      '41-55 лет'),
            ('пожилой',     '56-70 лет'),
            ('старческий',  '60+ лет'))
    age = forms.ChoiceField(label='Возраст', choices=ages)

    langs = (('русский', 'Русский'), ('английский', 'English'), ('китайский', '中文'))
    lang = forms.TypedChoiceField(label='Язык', choices=langs)

    ans = (('нет', 'Нет'), ('да', 'Да'))
    dogperson = forms.ChoiceField(label='Любите собак?', widget=forms.RadioSelect, choices=ans, initial=True)
    catperson = forms.ChoiceField(label='Любите кошек?', widget=forms.RadioSelect, choices=ans, initial=True)
    cooking = forms.ChoiceField(label='Умеете готовить?', widget=forms.RadioSelect, choices=ans, initial=True)

    religs = (('не знаю', 'Не выбрано'),
              ('атеизм', 'Атеизм'),
              ('православие', 'Православие'),
              ('ислам', 'Ислам'),
              ('католичество', 'Католичество'),
              ('буддизм', 'Буддизм'),
              ('иудаизм', 'Иудаизм'),
              ('агностицизм', 'Агностицизм'))
    religion = forms.ChoiceField(label='Религия', choices=religs, required=False)

    info = forms.CharField(label='Информация о вас', widget=forms.Textarea, required=False)

    avatar = forms.ImageField(label='Ваше фото', required=False)

    colors = (('red', 'Красный'), ('orange', 'Оранжевый'), ('yellow', 'Жёлтый'), ('green', 'Зелёный'),
              ('aqua', 'Голубой'), ('blue', 'Синий'), ('purple', 'Фиолетовый'))
    color = forms.ChoiceField(label='Цвет рамки аватара', choices=colors)

    agree = forms.BooleanField(label='Согласие на обработку персональных данных', initial=True)









