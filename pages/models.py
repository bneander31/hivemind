from django.db import models
# from wagtail.contrib.settings.models import BaseSetting, register_setting


# CtaType = (
#     ('Form', 'Form'),
#     ('Call', 'Call'),
# )


FormType = (
    ('button', 'button'),
    ('checkbox', 'checkbox'),
    ('date', 'date'),
    ('email', 'email'),
    ('file', 'file'),
    ('hidden', 'hidden'),
    ('number', 'number'),
    ('password', 'password'),
    ('radio', 'radio'),
    ('range', 'range'),
    ('search', 'search'),
    ('submit', 'submit'),
    ('tel', 'tel'),
    ('text', 'text'),
    ('time', 'time'),
    ('url', 'url'),
    ('week', 'week'),
)

FormMethod = (
    ('post', 'post'),
    ('get', 'get'),
)


# class Cta(models.Model):
#     Name = models.CharField(max_length=100,)
#     Type = models.CharField(choices=CtaType, max_length=10)
#     Link = models.CharField(max_length=500)
#
#     def __str__(self):
#         return self.Name
#
#     class Meta():
#         # ordering = ('created',)
#         get_latest_by = ('created',)
#         verbose_name = 'Call to Action'
#         verbose_name_plural = 'Call to Actions'


class Field(models.Model):
    Type = models.CharField(choices=FormType, max_length=50)
    Name = models.CharField(max_length=250)
    Label = models.CharField(max_length=250)
    FormKey = models.ForeignKey('Form', on_delete=models.CASCADE)

    def __str__(self):
        return self.Name

    class Meta():
        # ordering = ('created',)
        # get_latest_by = ('created',)
        verbose_name = 'Field'
        verbose_name_plural = 'Fields'


class Form(models.Model):
    Name = models.CharField(max_length=150)
    Method = models.CharField(choices=FormMethod, max_length=5)
    # Field = None

    def __str__(self):
        return self.Name

    class Meta():
        # ordering = ('created',)
        # get_latest_by = ('created',)
        verbose_name = 'Form'
        verbose_name_plural = 'Forms'


class Slide(models.Model):
    Image = models.ImageField(upload_to='photos/carousel/%Y/', blank=True, null=True)
    AltText = models.CharField(max_length=75, blank=True, null=True)
    Carousel = models.ForeignKey('Carousel', on_delete=models.CASCADE)

    def __str__(self):
        return self.AltText

    class Meta():
        # ordering = ('created',)
        get_latest_by = ('created',)
        verbose_name = 'Slide'
        verbose_name_plural = 'Slides'


class Carousel(models.Model):
    Slide = None
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

    class Meta():
        # ordering = ('created',)
        get_latest_by = ('created',)
        verbose_name = 'Carousel'
        verbose_name_plural = 'Carousel'


class ColumnInfo(models.Model):
    Title = models.CharField(max_length=75)
    Stat = models.CharField(max_length=25)
    RowKey = models.ForeignKey('ParallaxRow', on_delete=models.CASCADE)

    def __str__(self):
        return self.Title

    class Meta():
        verbose_name = 'Column'
        verbose_name_plural = 'Columns'


class ParallaxRow(models.Model):
    Title = models.CharField(max_length=75)
    Image = models.ImageField(upload_to='photos/parallax/%Y/')

    def __str__(self):
        return self.Title

    class Meta():
        verbose_name = 'Parallax Row'
        verbose_name_plural = 'Parallax Rows'
