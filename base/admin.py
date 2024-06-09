from django.contrib import admin
from .models import Transaction

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'description', 'date')
    search_fields = ('user__username', 'description')
    list_filter = ('date',)

admin.site.register(Transaction, TransactionAdmin)