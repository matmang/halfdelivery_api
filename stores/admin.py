from django.contrib import admin
from .models import Stores

# ? 만든 model 즉, 데이터베이스를 admin 패널에 등재하려면 여기서 코딩한다.
@admin.register(Stores)
class StoresModel(admin.ModelAdmin):
    list_filter = ("category", "store", "menu")
    list_display = ("category", "store", "menu")
