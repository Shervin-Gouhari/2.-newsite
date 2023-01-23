from .models import Article, Comment
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import FormMixin
from .forms import CommentForm, ArticleForm
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.decorators import login_required

# class ArticleCreateView(LoginRequiredMixin, CreateView):
#     model = Article
#     template_name = "articles/create.html"
#     fields = ("title", "body")
    
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

@login_required
def article_create_view(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article_title = form.cleaned_data["title"]
            article_body = form.cleaned_data["body"]
            article_author = request.user
            obj = Article(title=article_title, body=article_body, author=article_author)
            obj.save()
            return HttpResponseRedirect("/" + "articles/" + "detail/" + str(obj.id))
    else:
        form = ArticleForm()
    return render(request, "articles/create.html", {"form": form})
    



# class ArticleListView(ListView):
#     model = Article
#     template_name = "articles/list.html"
    
def article_list_view(request):
    articles = Article.objects.all()
    return render(request, "articles/list.html", {"object_list": articles})


    
        
# class ArticleDetailView(FormMixin, DetailView):
#     model = Article
#     template_name = "articles/detail.html"
#     form_class = CommentForm
    
#     def get_success_url(self):
#         return reverse("detail", kwargs={"pk": self.object.id})
#         # return reverse("detail", args=[str(self.object.id)])
    
#     def get_context_data(self, **kwargs):
#         context = super(ArticleDetailView, self).get_context_data(**kwargs)
#         # context = super().get_context_data(**kwargs)
#         # context = FormMixin.get_context_data(**kwargs)
#         context['form'] = CommentForm(initial={"article": self.object, "writer": self.request.user})
#         return context
    
#     def post(self, *args, **kwargs):
#         self.object = self.get_object()
#         form = self.get_form()
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             pass
        
#     def form_valid(self, form):
#         form.save()
#         return super(ArticleDetailView, self).form_valid(form)

def article_detail_view(request, pk):
    # article = Article.objects.get(id=pk)
    article = get_object_or_404(Article, id=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.writer = request.user  
            obj.article = article
            obj.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()
    return render(request, "articles/detail.html", {"object": article, "form": form})
        
    
    
    
# class ArticleEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Article
#     template_name = "articles/edit.html"
#     fields = ("title", "body")
    
#     def test_func(self):
#         obj = self.get_object()
#         return obj.author == self.request.user

@login_required
def article_edit_view(request, pk):
    article = get_object_or_404(Article, id=pk)
    if request.user == article.author:
        form = ArticleForm(request.POST or None, instance=article)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/" + "articles/" + "detail/" + str(pk))
        return render(request, "articles/edit.html", {"form": form, "object": article})
    else:
        return HttpResponseForbidden()
    
    
    
    
# class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Article
#     template_name = "articles/delete.html"
#     success_url = reverse_lazy("list")
    
#     def test_func(self):
#         obj = self.get_object()
#         return obj.author == self.request.user

@login_required
def article_delete_view(request, pk):
    article = get_object_or_404(Article, id=pk)
    if request.user == article.author:
        if request.method == "POST":
            article.delete()
            return HttpResponseRedirect("/" + "articles/" + "list")
        return render(request, "articles/delete.html", {"object": article})
    else:
        return HttpResponseForbidden()    
    


    
@login_required
def comment_edit_view(request, pk, comment_pk):
    comment = get_object_or_404(Comment, id=comment_pk)
    if request.user == comment.writer:
        form = CommentForm(request.POST or None, instance=comment)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/" + "articles/" + "detail/" + str(pk))
        return render(request, "comments/edit.html", {"form": form, "pk": pk, "comment_pk": comment_pk})
    else:
        return HttpResponseForbidden()    
    
    
    
        
@login_required
def comment_delete_view(request, pk, comment_pk):
    comment = get_object_or_404(Comment, id=comment_pk)
    if request.user == comment.writer:
        if request.method == "POST":
            comment.delete()
            return HttpResponseRedirect("/" + "articles/" + "detail/" + str(pk))
        return render(request, "comments/delete.html", {})
    else:
        return HttpResponseForbidden()
    
