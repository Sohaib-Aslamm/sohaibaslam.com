from django.contrib import admin
from adminPanel.models import *

# Register your models here.


class Portfolio(admin.ModelAdmin):
    pass


admin.site.register(About, Portfolio)
admin.site.register(Experience, Portfolio)
admin.site.register(Education, Portfolio)
admin.site.register(LangSkill, Portfolio)
admin.site.register(Portfolios, Portfolio)
admin.site.register(Recommendations, Portfolio)
admin.site.register(SocialMedia, Portfolio)
admin.site.register(userBlog, Portfolio)
admin.site.register(hello, Portfolio)
