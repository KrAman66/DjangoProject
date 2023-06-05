from django.shortcuts import render

#Register HTML form
from authenticate.forms import UserForm,UserProfileChange

#Login HTML form
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

#FOR Email Credential
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.mail import message, send_mail


@login_required
def home(request):

    if(request.method=='GET'):
        return render(request,'authenticate/base.html')


def user_register(request):
    registered = False 

    if(request.method == 'POST'):
        # when the user clicks the button after providing the input, this becomes true
        user_form = UserForm(request.POST)
        
        if user_form.is_valid():
            # temporarily halt the model save and store the user input in an object
            user = user_form.save(commit=False)
            password = user_form.cleaned_data['password']

            email = request.POST['email']
            print(email)
            # Encrypt the password with an hash function and save back the object
            user.set_password(user.password)
            subject = 'welcom to our app'
            message = 'thanx for joining community'
            from_email = settings.EMAIL_HOST_USER
            to_list = [email]
            fail_silently = True
            user.save()
            send_mail(subject,message,from_email,to_list,fail_silently)
            registered = True
    else:
        user_form = UserForm()

    dict = {
        'user_form' : user_form,
        'registered' : registered
    }
    return render(request,'authenticate/register.html',context=dict)


def user_login(request):
    form = AuthenticationForm()    
    if(request.method == 'POST'):
        form = AuthenticationForm(data=request.POST)
        if (form.is_valid()):
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/auth/success/')

    return render(request,'authenticate/login.html',{'form':form})

@login_required
def success(request):
    return render(request,'authenticate/dashboard.html') 

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/auth/')

@login_required
def user_profile(request):
    return render(request,'authenticate/profile.html')

@login_required
def user_change(request):
    current_user = request.user
    form = UserProfileChange(instance=current_user)
    if(request.method == 'POST'):
        form = UserProfileChange(data=request.POST,instance=current_user)
        if(form.is_valid()):
            form.save()
            form = UserProfileChange(instance=current_user)
            return HttpResponseRedirect('/auth/profile')
    return render(request,'authenticate/user_change.html',{'form':form})
   