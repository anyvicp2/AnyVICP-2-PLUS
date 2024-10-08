from django.db import models #type: ignore

class Website(models.Model):
    name = models.TextField(max_length=15)
    domain = models.TextField(max_length=100)
    author = models.TextField(max_length=15)
    createdate = models.DateTimeField(auto_now_add=True)
    icpNumber = models.TextField(max_length=20, null=True)
    status = models.BooleanField(default=True)

    # 有 name, domain, author, createdate, status
    # name 是网站名，domain 是域名，author 是作者，createdate 是创建日期，status 是状态

    def __str__(self):
        return f"[{self.name},{self.domain},{self.author},{self.icpNumber},{self.createdate},{self.status}]"
        # 返回一个字符串，包含网站名、域名、作者、创建日期和状态 (实际上是列表)

class Announcement(models.Model):
    name = models.TextField(max_length=15)
    content = models.TextField(max_length=15)
    author = models.TextField(max_length=15)

    # 有 name, content, author
    # name 是公告名，content 是公告内容，author 是作者

    def __str__(self):
        return f"[{self.name},{self.content},{self.author}]"
        # 返回一个字符串，包含公告名、公告内容和作者 (实际上是列表)