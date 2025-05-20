from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
  books = Book.objects.all()
  reviews = Review.objects.all()
  context = {
    'books': books,
    'reviews':reviews
  }
  return render(request, 'review/home.html',context)



def reviewPage(request, id):
  book = get_object_or_404(Book, id = id)
  reviews = book.reviews.all()
  
  if request.method == "POST":
    if request.user.is_authenticated:
      rating = request.POST.get('rating')
      comment = request.POST.get('comment')


      existing_review = Review.objects.filter(book = book, user = request.user).first()
      if existing_review:
        messages.errror(request, "You have already reviewed this book.")
      else:
        Review.objects.create(
          book = book,
          user = request.user,
          rating = rating,
          comment = comment
        )
        messages.success(request, "Review Successfully Added.")
        return redirect('reviewPage',id = book.id)
    else:
      messages.error(request, "You should be authenticated to post review")
      return redirect('login')


  
  return render(request, 'review/reviewPage.html',{
    'book': book,
    'reviews': reviews
  })

def userRegister(request):
  if request.method == "POST":
    form = RegistrationForm(request.POST)
    print("form is delivered")
    if form.is_valid():
      print("form is checked")
      user = form.save(commit = False)
      user.set_password(form.cleaned_data["password"])
      user.save()
      return redirect('login')
    else:
      messages.error(request, "Registration Failed")
        
  form = RegistrationForm()
  return render(request, 'review/register.html',{'form': form})

def userLogin(request):
  if request.user.is_authenticated:
    return redirect('home')
  if request.method == "POST":
    print("post activated")
    email = request.POST.get('email')
    password = request.POST.get('password')

    if not email or not password:
      messages.error(request, "Both fields are required")
      return redirect('login')
    
    try:
      user = User.objects.get(email = email)
      print("no email")
    except User.DoesNotExist:
      messages.error(request, "Invalid email or password.")
    
    
    user = authenticate(request, email = email, password = password)

    if user is not None:
      login(request, user)
      return redirect('home')
    
  return render(request, 'review/login.html')

def logoutUser(request):
  logout(request)
  return redirect('login')


