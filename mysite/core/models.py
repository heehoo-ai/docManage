from django.db import models


class Category(models.Model):
    name = models.CharField( max_length=10, verbose_name="分类")

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = "分类"

    def __str__(self):
        return self.name

    @classmethod
    def get_navs(cls):
        categories = cls.objects.all()
        print(categories)
        nav_categories = []
        for cate in categories:
            nav_categories.append(cate)
        return {
            'navs': nav_categories,
        }

class Doc(models.Model):
    title = models.CharField(max_length=100, verbose_name="标题")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="上传时间")
    pdf = models.FileField(upload_to='doc/pdfs/')
    # cat = models.ForeignKey(Category, verbose_name="分类", on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)
