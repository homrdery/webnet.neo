# class addForm(forms.ModelForm):
#     action = forms.CharField(widget=forms.HiddenInput(), initial="sub", required=True)
#     mac_addr = forms.ChoiceField(choices=list_mac_addr)
#     # mac_addr = forms.CharField(widget=forms.Select(choices=list_mac_addr))
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.form_action = ''
#         self.helper.layout = Layout(Modal(Field('name'), Field('mac_addr'),Field('action'), Submit("submit", "Оправить", css_class='btn btn-primery float-end'),  css_id="addForm", title='обавить новую запись'
#
#
#     class Meta:
#         model = worker
#         fields = ('name', 'mac_addr', 'data')
