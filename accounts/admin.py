from django.contrib import admin
from accounts.models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "head_st",
        "vtm_st",
        "wta_st",
        "mta_st",
        "ctd_st",
        "wto_st",
        "htr_st",
        "dtf_st",
        "mtr_st",
    )
