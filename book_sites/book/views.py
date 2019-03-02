from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from gensim.models.doc2vec  import Doc2Vec
from book.models import Book,Catalog,Rating,Like,UserProfile
from book.forms import RatingForm,ProfileForm

from django.contrib.auth.models import User

import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

model = Doc2Vec.load("static/books_doc2vec_model2")

def home(request):
	top=Book.objects.order_by('-score')[0:4]
	top8=Book.objects.order_by('-score')[5:9]
	c=Catalog.objects.order_by('id')
	return render(request,'home.html', { 'top4' : top , 'c' : c , 'top8' : top8})

def catalog(request, pk):
	c=Catalog.objects.get(pk=pk)
	books=Book.objects.filter(catalog_id=c)
	return render(request,'catalog.html' , {'c' : c , 'books' : books })

def book_detail(request,book_id):

	#評分計算
	new_score=Book.objects.get(id=book_id)
	for i,s in Rating.objects.filter(book=book_id).aggregate(Avg('rating')).items():
		if s is not None:
			new_score.score=s
			new_score.save()

	book=get_object_or_404(Book, pk=book_id)
	#book=Book.objects.get(pk=book_id)
	c=Catalog.objects.order_by('id')
	#b=Book.objects.get(pk=book_id)
	
	rating = Rating.objects.filter(book=book).order_by('-pub_date')
	pic = UserProfile.objects.all()

	booklist=[]
	rmd_books=model.most_similar(book_id,topn=5)
	for i in range(0,5):
		booklist.append(Book.objects.get(id=rmd_books[i][0]))
		#booklist.append(get_object_or_404(Book, name=rmd_books[i][0]))
		#booklist.append(rmd_books[i][0])
	form = RatingForm()



	return render(request, 'book_detail.html' , { 'book' : book , 'form' : form , 'c' : c , 'rmd_books' : booklist , 'rating' : rating , 'pic' : pic })

#留言、評分
@login_required
def add_rating(request,book_id):
	
	#book=Book.objects.get(pk=book_id)
	book=get_object_or_404(Book,pk=book_id)
	
	myuser=User.objects.get(pk=request.user.id)

	form = RatingForm(request.POST)

	# 以下這種寫法不可以
	#myuser = request.user
	
	if form.is_valid():
		rating = form.cleaned_data['rating']
		comment = form.cleaned_data['comment']
		#user = form.cleaned_data['user']
		#myuser = request.user
		
		review = Rating()
		review.book = book
		review.user = myuser
		review.rating = rating
		review.comment = comment
		review.pub_date = datetime.datetime.now()
		review.save()
		#print(user.name)
		#print(book.name)

	return HttpResponseRedirect(reverse('book_detail', args = (book.id, )))

	#return render(request,'book_detail.html',{'book' : book, 'form' : form , 'c' : c , 'rmd_books' : booklist , 'rating' : rating })


def contact(request):
	return render(request,'contact.html')

def about(request):
	return render(request,'about.html')
def privacypolicy(request):
	return render(request,'privacypolicy.htm')
#按讚
@login_required
def commentLikes(request,book_id,comment_id):
	rating=get_object_or_404(Rating, pk=comment_id)
	comment =Like.objects.filter(comment=comment_id)
	myuser=User.objects.get(pk=request.user.id)

	if not Like.objects.filter(comment=comment_id).exists() or not Like.objects.filter(comment=comment_id, user=myuser):
		thumb=Like()
		thumb.user=myuser
		thumb.comment=rating
		thumb.save()
		rating.likes+=1
		rating.save()
	else:
		com=Like.objects.filter(comment=comment_id, user=myuser)
		com.delete()
		rating.likes-=1
		rating.save()
	return HttpResponseRedirect(reverse('book_detail', args = (rating.book.id, )))
	#return render(request,'book_detail.html',{'book' : book, 'form' : form , 'c' : c , 'rmd_books' : booklist , 'rating' : rating })

#查看PROFILE
def profile(request,username):
	uProfile = UserProfile.objects.get(user=username)
	rating=Rating.objects.filter(user=username).order_by('-pub_date')
	likeRating=Like.objects.filter(user=username)
	return render(request,'profile.html', {'userP' : uProfile, 'rating' : rating, 'likeRating' : likeRating})

#會員修改資料
@login_required
def editProfile(request):
	
	pForm = ProfileForm(request.POST, request.FILES,  instance=request.user)
	if pForm.is_valid():
		renew=get_object_or_404(UserProfile, user=request.user.id)
		renew.gender = pForm.cleaned_data['gender']
		renew.birth_day = pForm.cleaned_data['birth_day']
		renew.location = pForm.cleaned_data['location']
		renew.bio = pForm.cleaned_data['bio']
		renew.image = pForm.cleaned_data['image']
		renew.save()
		return redirect('/profile')
	else :
		return render(request, 'edit_profile.html', {'pForm' : pForm})
'''
def 解憂雜貨店(request):
	#只取出必要的資料
	rmd_books=model.most_similar(['解憂雜貨店'],topn=5)
	booklist=[]
	for i in range(0,5):
		booklist.append(Book.objects.get(name=rmd_books[i][0]))

	
	return render(request,'read/crime/解憂雜貨店.html',{ 'rmd_books' : booklist })
'''
# Create your views here.
