
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse, request, HttpResponseRedirect
from django.urls import reverse


from . import models
from .forms import CreateUserForm, PostForm, CommentForm
from datetime import datetime, timedelta
from django.utils import timezone
from django.utils.timezone import activate
from django.conf import settings

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='login')
def Home(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            pf = post_form.save(commit=False)
            pf.username = request.user.username
            pf.message = message
            pf.save()
        else:
            print(post_form.errors.as_data())
        
           # Getting the current instance object to display in the template
        return HttpResponseRedirect("/")

    else:
        post_form = PostForm()

    post_object = models.Message.objects.filter(
        is_deleted=False).order_by('-date_posted')

    post_time = models.Message.objects.filter(is_deleted=False)



    # for posts in post_time:
    #     # print("Post-time: ", posts.date_posted)
    #     # print("TimeDelta added: ", posts.date_posted+timedelta(hours=24))
    #     # print("Timezone now: ", timezone.now())
    #     # print(timezone.now() > (posts.date_posted + timedelta(hours=24)))

    #     # remaining_time = (posts.date_posted +
    #     #                   timedelta(hours=24)) - timezone.now()
    #     # print(remaining_time)
    #     if timezone.now() > (posts.date_posted + timedelta(hours=24)):
    #         posts.is_deleted = True
    #         posts.save()
    #     else:
    #         posts.is_deleted = False
    #         posts.save()


    return render(request, 'main/homepage.html', {'post_form': post_form, 'post_object': post_object})


def AboutAnyth(request):
    return render(request, 'main/about-anyth.html')


def Login(request):
    if request.user.is_authenticated:
        return redirect('/')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                
                # if user in models.Person.objects.all():
                #     pass
                # else:
                #     models.Person.objects.create(user=request.user)
                
                return redirect('Home')
            else:
                messages.info(request, 'username or password does not match')
                return HttpResponseRedirect('login.html')
        context = {}
        return render(request, 'login.html', context)


def CreateAccount(request):

    if request.user.is_authenticated:
        return redirect('/')

    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                fname = form.cleaned_data.get('first_name')
                lname = form.cleaned_data.get('last_name')
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password1')
                messages.success(
                    request, 'Account successfully created for ' + username)
                return redirect('login')

        context = {'form': form}
        return render(request, 'create-account.html', context)


def SingleMessage(request, pk):
    message = models.Message.objects.get(id=pk)
    post_object = models.Message.objects.filter(
        is_deleted=False).order_by('?').exclude(id=pk)

    comments = message.comments.filter(active=True).order_by('-created')

    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            new_comment.username = request.user.username
            # Assign the current post to the comment
            new_comment.post = message
            # Save the comment to the database
            new_comment.save()

            return HttpResponseRedirect(request.path_info)
    else:
        comment_form = CommentForm()

    post_time = models.Message.objects.filter(is_deleted=False)



    # for posts in post_time:
    #     # print("Post-time: ", posts.date_posted)
    #     # print("TimeDelta added: ", posts.date_posted+timedelta(hours=24))
    #     # print("Timezone now: ", timezone.now())
    #     # print(timezone.now() > (posts.date_posted + timedelta(hours=24)))

    #     # remaining_time = (posts.date_posted +
    #     #                   timedelta(hours=24)) - timezone.now()
    #     # print(remaining_time)
    #     if timezone.now() > (posts.date_posted + timedelta(hours=24)):
    #         posts.is_deleted = True
    #         posts.save()
    #     else:
    #         posts.is_deleted = False
    #         posts.save()


    

    context = {'message': message,
               'post_object': post_object,
               'comments': comments,
               'comment_form': comment_form}
    return render(request, 'ind-message.html', context)


def Logout(request):
    logout(request)
    return redirect('login')


# def MyCircle(request):
#     # current_user = models.Person.objects.get(user=request.user)
#     # friends = models.Person._meta.get_field('friends')
    
#     # print("Current User: ", current_user)
#     # print("Friends: ", friends)
#     return render(request, 'my-circle.html')

# def MyCircleChats(request, username):
#     return render(request, 'my-circle.html', {'username':username})
