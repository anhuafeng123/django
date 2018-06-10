from django.db import models
from userapp.models import BlogUser
from datetime import datetime
#轮播图
class Banner(models.Model):
    title = models.CharField(verbose_name='标题', max_length=50)
    cover = models.ImageField(verbose_name='轮播图', upload_to='static/images/banner')
    link_url = models.URLField(max_length=150, verbose_name='图片链接')
    idx = models.IntegerField(verbose_name='索引')
    is_active = models.BooleanField(verbose_name='是否激活', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name
#博客分类
class BlogCategory(models.Model):
    name = models.CharField(max_length=30, verbose_name='分类名称', default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

#标签
class Tags(models.Model):
    name = models.CharField(verbose_name='标签', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
#博客
class Post(models.Model):
    user = models.ForeignKey(BlogUser, verbose_name='作者')
    category = models.ForeignKey(BlogCategory, verbose_name='博客分类', default=None)
    tags = models.ManyToManyField(Tags, verbose_name='标签')
    title = models.CharField(verbose_name='标题', max_length=30, null=False)
    content = models.CharField(verbose_name='内容', max_length=4000, null=False)
    pub_date = models.DateTimeField(verbose_name='发布时间', default=datetime.now)
    cover = models.ImageField(verbose_name='博客封面', upload_to='static/image/post', default=None)
    views = models.IntegerField(verbose_name='浏览量')
    is_recomment = models.BooleanField(verbose_name='是否推荐博客', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = verbose_name
#评论
class Comment(models.Model):
    user = models.ForeignKey(BlogUser, verbose_name='评论者')
    post = models.ForeignKey(Post, verbose_name='博客')
    content = models.CharField(verbose_name='评论内容', max_length=400)
    pub_date = models.DateTimeField(verbose_name='发布时间', default=datetime.now)

    def __str__(self):
        return self.post.title

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
#友情链接
class FriendlyLink(models.Model):
    title = models.CharField(max_length=30, verbose_name='友情链接标题')
    link = models.URLField(max_length=150, verbose_name='链接地址', default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name
