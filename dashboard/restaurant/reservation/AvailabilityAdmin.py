from django.contrib import admin

class AvailabilityAdmin(admin.ModelAdmin):
    list_display = (
        "restaurant",
        "date",
        "start_time",
        "end_time",
        "table_number",
        "available_slots",
    )
    list_filter = ("restaurant", "date", "table_number")
    search_fields = ("restaurant__name", "date", "table_number")
    ordering = ["date", "start_time"]
