from django.db import models


class CmsSlider(models.Model):
    cms_img = models.ImageField(upload_to='sliderimg/')
    cms_title = models.CharField(max_length=200, verbose_name='Заголовок')
    cms_text = models.CharField(max_length=1000, verbose_name='Текст')
    cms_css = models.CharField(max_length=1000, null=True, default='-', verbose_name='CSS class')

    def __str__(self):
        return self.cms_title

    class Meta:
        verbose_name = 'Slide'
        verbose_name_plural = 'Slides'
