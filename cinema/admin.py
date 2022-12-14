from django.contrib import admin

from cinema.models import Spectator, ScreenCinema, Film, Showtime


class SpectatorAdmin(admin.ModelAdmin):
    list_display = ("username", "wallet", "first_name", "last_name", "email", "is_staff")
    list_display_links = ("username",)
    search_fields = ("username", "first_name", "last_name", "email")


admin.site.register(Spectator, SpectatorAdmin)
admin.site.register(ScreenCinema)
admin.site.register(Film)
admin.site.register(Showtime)
