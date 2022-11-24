from django.contrib import admin

from .models import Billing, Company, Customer, Service


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)


class BarInlineBilling(admin.TabularInline):
    model = Billing.services.through


class BillingAdmin(admin.ModelAdmin):
    inlines = [
        BarInlineBilling
    ]
    exclude = ('services',)
    list_display = ('customer', 'company', 'account', 'price', 'date')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Billing, BillingAdmin)
