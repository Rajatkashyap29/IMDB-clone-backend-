from django.contrib import admin
from watchlist_app.models import WactchList,StreamPlateform,Review,Product,DogCategory

# Register your models here.
admin.site.register(WactchList),
admin.site.register(StreamPlateform),
admin.site.register(Review)
admin.site.register(Product)
admin.site.register(DogCategory)
