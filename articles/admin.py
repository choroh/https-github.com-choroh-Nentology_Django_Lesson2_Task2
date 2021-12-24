from django.contrib import admin
from django.core.exceptions import ValidationError

from .models import Article, Thema, ArticleThema
from django.forms import BaseInlineFormSet


class ArticleThemaInlineFormset(BaseInlineFormSet):
    """
    Если данные не заполнены или оснавных тем отсечено 2 то не сохраняем данные и сообщаем пользователю об ошибке
    Если основноая тема не указана сообщаем пользователю о необходимости выбрать одну основную тему
    """
    def clean(self):
        is_main = False
        for form in self.forms:
        # form.cleaned_data  словарь со всеми данными текущей формы.
            if form.cleaned_data.get('is_main'):
                if not is_main:
                    is_main = True
                else:
                    raise ValidationError('Основная тема возможна только одна.')

            if not is_main:
                raise ValidationError('Укажите основной раздел')

        if len(self.forms) == 0:  # Если не указана тема
            raise ValidationError("Не указана тема")

        return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleThemaInline(admin.TabularInline):
    # Класс для расширенных возможностей страницы административной панели
    model = ArticleThema
    formset = ArticleThemaInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    inlines = [ArticleThemaInline]


@admin.register(Thema)
class ThemaAdmin(admin.ModelAdmin):
    list_display = ['id', 'thema']
    inlines = [ArticleThemaInline]




