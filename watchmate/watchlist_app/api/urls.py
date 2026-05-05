
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from watchlist_app.api.views import ReviewList, UserReview, WatchListAV, WatchDetailAV,StreamPlateformAV,StreamPlateformDetailAv,ReviewDetail,ReviewCreate,StreamPlateformVS,ProductView,CategoryView,WatchListGV

router= DefaultRouter()
router.register('stream',StreamPlateformVS ,basename='streamplateform')
router.register('product',ProductView ,basename='product')
router.register('breed',CategoryView,basename='breed')



urlpatterns = [
    
    path('list/',WatchListAV.as_view(),name='movie-list'),
    path('<int:pk>',WatchDetailAV.as_view(),name='movie-detail'),
    path('list2/',WatchListGV.as_view(),name='watch-list'),
    
    path('',include(router.urls)),
    
    # path('stream/',StreamPlateformAV.as_view(),name='stream'),
    # path('stream/<int:pk>', StreamPlateformDetailAv.as_view(), name='streamplateform-detail'),
    
    path('review/',ReviewList.as_view(),name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='my_review-detail'),
    path('stream/<int:pk>/review-create',ReviewCreate.as_view(),name='review-creaaate'),
    
    path('stream/<int:pk>/review',ReviewList.as_view(),name='review-list'),
    path('stream/review/<int:pk>',ReviewDetail.as_view(),name='review-detail'),
    path('review/<str:username>/', UserReview.as_view(), name='user-review-detail'),
    
    
    

]
