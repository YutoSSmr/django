from django.contrib import admin
from .models import questions
from .models import user_info
from .models import user_result_his

admin.site.register(questions)
admin.site.register(user_info)
admin.site.register(user_result_his)