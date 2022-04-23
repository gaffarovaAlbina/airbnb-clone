from re import S
from statistics import mode
from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.RoomType)
class ItemAdmin(admin.ModelAdmin):
    """Кастомная админка для типа комнаты"""

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()

    pass


@admin.register(models.Amenity)
class AmenityAdmin(admin.ModelAdmin):
    """Кастомная админка для удобств комнаты"""

    pass


@admin.register(models.Facility)
class FacilityAdmin(admin.ModelAdmin):
    """Кастомная админка для бытовой техники"""

    pass


@admin.register(models.HouseRule)
class HouseRuleAdmin(admin.ModelAdmin):
    """Кастомная админка для правил проживания"""

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Кастомная админка для фото"""

    list_display = (
        "__str__",
        "get_thumbnail",
    )

    def get_thumbnail(self, obj):

        return mark_safe(f'<img src="{obj.file.url}" width=50/>')

    get_thumbnail.short_description = "Preview"


class PhotoInline(admin.StackedInline):
    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Кастомная админка для комнат"""

    inlines = [
        PhotoInline,
    ]

    fieldsets = (
        (
            "Основная информация",
            {
                "fields": (
                    "name",
                    "description",
                    "country",
                    "city",
                    "address",
                    "price",
                    "room_type",
                )
            },
        ),
        (
            "Время заезда/выезда",
            {
                "fields": (
                    "check_in",
                    "check_out",
                    "instant_book",
                )
            },
        ),
        (
            "Удобства",
            {
                "classes": ("collapse",),
                "fields": (
                    "amenities",
                    "facilities",
                    "house_rules",
                ),
            },
        ),
        (
            "Спальные места",
            {
                "fields": (
                    "beds",
                    "bedrooms",
                    "guests",
                )
            },
        ),
        (
            "Дополнительная информация",
            {"fields": ("host",)},
        ),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "beds",
        "bedrooms",
        "bathrooms",
        "guests",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    list_filter = (
        "host__superhost",
        "instant_book",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    search_fields = (
        "=city",
        "^host__username",
    )

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    raw_id_fields = ("host",)

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photo count"
