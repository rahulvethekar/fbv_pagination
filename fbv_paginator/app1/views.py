from django.shortcuts import render
from .models import Article
from django.core.paginator import Paginator
# Create your views here.
def ArticleView(request):

    obj = Article.objects.all()
    paginator = Paginator(obj,3,orphans=1)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    context = {'page_obj':page_object}
    template_name = 'app1/article.html'
    return render(request,template_name,context)


    
