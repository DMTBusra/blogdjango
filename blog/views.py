from turtle import update
from django.shortcuts import redirect, render,get_object_or_404
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.contrib import messages
from blog.forms import PostForm,CommentForm
from django.urls import reverse_lazy,reverse
from .models import Blog
from django.http import HttpResponseRedirect
# Create your views here.

class HomeView(ListView):
    model=Blog
    form_class= PostForm
    template_name = "users/home.html"
    #ordering = [id]
    ordering=["-created_date"]
    
   
    
# def LikeView(request,pk):
#     post=get_object_or_404(Blog,id=request.POST.get("blog_id"))
#     if post.likes.filter(id=request.user.id).exists():
#         post.likes.remove(request.user)
#     else:
#         post.likes.add(request.user)
#     return HttpResponseRedirect(reverse("detail",args=[str(pk)]))

# class BlogCreateView(CreateView):
#     model= Blog
#     form_class=PostForm
#     template_name="blog/blog_add.html"
#     success_url=reverse_lazy("home")
def BlogCreateView(request):
   form=PostForm(request.POST or None,request.FILES)
   if request.method=="POST":
      form=PostForm(request.POST,request.FILES )
      if form.is_valid() :
         new_creator=form.save(commit=False)
         new_creator.author =request.user
         new_creator.save()
         form.save_m2m()
         messages.success(request, "Post created succesfully!")
         return redirect("home")
   context={
      "form":form
   }
   return render(request,"blog/blog_add.html",context)

def BlogDetailView(request,id):
    blog=Blog.objects.get(id=id)

    form = CommentForm()
    #obj = get_object_or_404(Blog)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = blog
            comment.save()
            return redirect("home")
           # return redirect(request.path)
    context = {
        "blog": blog,
        "form": form
    }
       
    return render(request,"blog/blog_detail.html",context)
    


class BlogUpdateView(UpdateView):
    model= Blog
    template_name="blog/blog_update.html"
    form_class=PostForm
    success_url=reverse_lazy("home")
class BlogDeleteView(DeleteView):
    model=Blog
    template_name="blog/blog_delete.html"
    success_message= "Post deleted!!!"
    success_url=reverse_lazy("home")