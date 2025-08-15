from django import forms

class CreateForm (forms.Form):
    username = forms.CharField(label='username',error_messages={'required': 'Incorrect Username'})
    password = forms.CharField(label='password',error_messages={'required': 'Incorrect Password'})


class Calculator(forms.Form):
    value1 = forms.IntegerField(label='value1',  error_messages= {'required' : 'value must be integer'})

    value2 = forms.IntegerField(label='value2' , error_messages= {'required' : 'value must be integer'})
    
    choices = [
        ('+','sum'),
        ('-','subtract'),
        ('*','product'),
        ('/','divide'),
    ]
    operator = forms.ChoiceField(label='operator', choices=choices)




class Even_Odd(forms.Form):
    Value = forms.IntegerField(label='Value',error_messages={'required': 'Enter Integer'})



class Worksheet(forms.Form):
    Subject1 = forms.IntegerField( label='Subject1', error_messages={'required': 'Enter Integer'} , max_value=100 )
    Subject2 = forms.IntegerField( label='Subject2', error_messages={'required': 'Enter Integer'} )
    Subject3 = forms.IntegerField( label='Subject3', error_messages={'required': 'Enter Integer'} )
    Subject4 = forms.IntegerField( label='Subject4', error_messages={'required': 'Enter Integer'} )
    Subject5 = forms.IntegerField( label='Subject5', error_messages={'required': 'Enter Integer'} )
