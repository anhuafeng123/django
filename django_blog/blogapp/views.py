from django.shortcuts import render
from .models import Banner, Post, BlogCategory, Comment, FriendlyLink, Tags
from django.views.generic.base import View
from django.db.models import Q
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
#首页

def index(request):
    banner_list = Banner.objects.all()
    # 去数据库里面取出所有　推荐的文章
    recomment_list = Post.objects.filter(is_recomment=True)
    for recoment in recomment_list:
        recoment.content = recoment.content[:100] + '......'

    #倒叙
    post_list = Post.objects.order_by('-pub_date')
    for post in post_list:
        post.content = post.content[:160] + '......'


    # 博客分类
    blogcategory_list = BlogCategory.objects.all()

    # 最新评论博客列表
    comment_list = Comment.objects.order_by('-pub_date')
    new_comment_list = []
    for test in comment_list:
        if test.post not in new_comment_list:
            new_comment_list.append(test.post)
    # 友情链接
    friendlylink_list = FriendlyLink.objects.all()
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        pagea = 1

    p = Paginator(post_list, per_page=5, request=request)
    post_list = p.page(page)
    ctx = {
        'banner_list': banner_list,
        'recomment_list': recomment_list,
        'post_list': post_list,
        'blogcategory_list': blogcategory_list,
        'new_comment_list': new_comment_list,
        'friendlylink_list': friendlylink_list

    }
    return render(request, 'index.html', ctx)




#列表页
def lista1(request,tcv=-1,fen=-1):
    tcv = int(tcv)
    fen = int(fen)
    post_list = None
    if tcv != -1:
        post_list=Post.objects.filter(tags=tcv)
    elif fen != -1:
        post_list = Post.objects.filter(category=fen)
    else:
        post_list = Post.objects.order_by('-pub_date')
    for post in post_list:
        post.content = post.content[:160] + '......'
    try:
        pagea = request.GET.get('page', 1)
    except PageNotAnInteger:
        pagea = 1

    p = Paginator(post_list, per_page=5, request=request)
    post_list = p.page(pagea)

    banner_list = Banner.objects.all()
    # 去数据库里面取出所有　推荐的文章
    recomment_list = Post.objects.filter(is_recomment=True)
    for recoment in recomment_list:
        recoment.content = recoment.content[:100] + '......'

    # 博客分类
    blogcategory_list = BlogCategory.objects.all()

    # 最新评论博客列表
    comment_list = Comment.objects.order_by('-pub_date')
    new_comment_list = []
    for test in comment_list:
        if test.post not in new_comment_list:
            new_comment_list.append(test.post)

    # 友情链接
    friendlylink_list = FriendlyLink.objects.all()
    #标签
    tags_list=Tags.objects.all()
    now_tags_list = []
    for t in tags_list:
        count = len(t.post_set.all())
        now_tags_list.append({'name':t.name,'id':t.id,'count':count})

    ctx = {
        'banner_list': banner_list,
        'recomment_list': recomment_list,
        'post_list': post_list,
        'blogcategory_list': blogcategory_list,
        'new_comment_list': new_comment_list,
        'friendlylink_list': friendlylink_list,
        'tags_list':now_tags_list,
    }
    return render(request, 'list.html', ctx)
#搜索
class SearchView(View):
    def get(self,request):
        pass
    def post(self,request):
        kw = request.POST.get('keyword')
        post_list =Post.objects.filter(Q(title__icontains=kw)|Q(content__icontains=kw))
        for post in post_list:
            post.content = post.content[:160] + '......'
        banner_list = Banner.objects.all()
        # 去数据库里面取出所有　推荐的文章
        recomment_list = Post.objects.filter(is_recomment=True)
        for recoment in recomment_list:
            recoment.content = recoment.content[:100] + '......'

        # 倒叙
        # post_list = Post.objects.order_by('-pub_date')
        # for post in post_list:
        #     post.content = post.content[:160] + '......'

        # 博客分类
        blogcategory_list = BlogCategory.objects.all()

        # 最新评论博客列表
        comment_list = Comment.objects.order_by('-pub_date')
        new_comment_list = []
        for test in comment_list:
            if test.post not in new_comment_list:
                new_comment_list.append(test.post)

        # 友情链接
        friendlylink_list = FriendlyLink.objects.all()
        # 标签
        tags_list = Tags.objects.all()

        ccx = {
            'banner_list': banner_list,
            'recomment_list': recomment_list,
            'post_list': post_list,
            'blogcategory_list': blogcategory_list,
            'new_comment_list': new_comment_list,
            'friendlylink_list': friendlylink_list,
            'tags_list': tags_list,

        }

        return render(request,'search.html',ccx)
def show(request,sh=-1):
    cht = int(sh)
    if cht != -1:
        post_list=Post.objects.get(id=cht)
    else:

        post_list=Post.objects.filter(is_recomment=True).order_by('-views')
        #要显示的博客对象
        post_list = post_list[0]





    tag_list=post_list.tags.all()

    comment_list = Comment.objects.order_by('-pub_date')
    new_comment_list = []
    for test in comment_list:
        if test.post not in new_comment_list:
            new_comment_list.append(test.post)

#相关推荐
    tuijian = post_list.category
    tuijian_list =Post.objects.filter(category=tuijian)

    ctx={
            'post':post_list,
            'new_comment_list': new_comment_list,
            'tag_list':tag_list,
            'tuijian_list':tuijian_list,
        }
    return render(request,'show.html',ctx)


