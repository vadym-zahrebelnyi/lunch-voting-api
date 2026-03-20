from django.contrib import admin
from voting.models import Vote


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ("id", "employee", "menu", "date")
    list_filter = ("date", "menu__restaurant")
    search_fields = ("employee__email", "menu__restaurant__name")
    readonly_fields = ("date",)

    def get_queryset(self, request):
        return (
            super().get_queryset(request).select_related("employee", "menu__restaurant")
        )

    def has_add_permission(self, request):
        return False
