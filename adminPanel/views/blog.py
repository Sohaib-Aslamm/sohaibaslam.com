from adminPanel.models import userBlog, blog_Review

from django.core.paginator import Paginator

from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required


@login_required(login_url='/user_login')
def adminblog(request):
    if request.method == 'POST':
        reg = userBlog(title=request.POST['title'], heading=request.POST['heading'], tags=request.POST['tags'],
                       quote=request.POST['quote'], quote_by=request.POST['quote_by'],
                       description=request.POST['editor1'],
                       Icon=request.FILES['icon'], created_at=request.POST['created_at'])
        reg.save()
        return redirect('/adminblog')
    else:
        BLGdata = userBlog.objects.values('sNo', 'title', 'heading', 'Icon', 'created_at').order_by('-sNo')
        paginator = Paginator(BLGdata, 10)
        pageNo = request.GET.get('page')
        BLGdataFINAL = paginator.get_page(pageNo)
        totalPages = BLGdataFINAL.paginator.num_pages
        context = {'BLGdata': BLGdataFINAL, 'lastPage': totalPages, 'pageList': [n + 1 for n in range(totalPages)]}
        return render(request, 'adminBlog.html', context)


def user_comments(request):
    comment_data = blog_Review.objects.all()
    return render(request, 'comments.html', {'comment_data': comment_data})