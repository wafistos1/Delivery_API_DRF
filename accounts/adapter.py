# from django.conf import settings
# from allauth.account.adapter import DefaultAccountAdapter


# class UserAccountAdapter(DefaultAccountAdapter):

#     def save_user(self, request, user, form, commit=True):
#         """
#         This is called when saving user via allauth registration.
#         We override this to set additional data on user object.
#         """
#         # Do not persist the user yet so we pass commit=False
#         # (last argument)
#         user = super(UserAccountAdapter, self).save_user(request, user, form, commit=False)
#         user.picture = form.cleaned_data.get('picture')
#         user.adress1 = form.cleaned_data.get('adress1')
#         user.phone = form.cleaned_data.get('phone')
#         user.save()