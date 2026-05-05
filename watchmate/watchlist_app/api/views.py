# from rest_framework import mixins
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.exceptions import ValidationError
from watchlist_app.api.serializers import StreamPlateformSerializers,WactchListSerializer,ReviewSeriliazer,ProductSeriliazer,DogSeriliazer
from watchlist_app.models import StreamPlateform, WactchList,Review,Product,DogCategory
from watchlist_app.api.permissions import AdminOrReadonly, ReviewUserOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from watchlist_app.api.throttle import ReviewCreateThrottle,ReviewListThrottle
from watchlist_app.api.pagination import WatchListPagination



class UserReview(generics.ListAPIView):
     serializer_class=ReviewSeriliazer
    
     def get_queryset(self):
        username=self.kwargs['username']
        return Review.objects.filter(review_user__username=username)
    


class ProductView(viewsets.ViewSet):
    def list(self,request):
        try:
            queryset= Product.objects.all()
            serializer=ProductSeriliazer(queryset,many=True)
            return Response(serializer.data)
        
        except Exception as e:
            print(e)
    
    def retrieve(self,request,pk=None):
        try:     
            prod=Product.objects.get(pk=pk)
            serializer=ProductSeriliazer(prod) 
            return Response (serializer.data)
        except Exception as e:
            print(e)

    def create(self,request):
        try:
            serializer=ProductSeriliazer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
               return Response(serializer.errors)
        except Exception as e:
            print(e)

    def update(self,request,pk):
        try:
            var = request.data
            prod = Product.objects.get(pk=pk)
            serializer=ProductSeriliazer(prod ,data= var) 
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
        
    def delete(self,request,pk):
        try:
            
            prod=Product.objects.get(pk=pk)
            prod.delete()
            return Response("Data delete ho gya")
        except Exception as e:
            print(e)

class CategoryView(viewsets.ViewSet):
    def list(self,request):
        queryset=  DogCategory.objects.all()
        serializer=DogSeriliazer(queryset,many=True)
        return Response(serializer.data)
        
        
    def retrieve(self,request,pk):
        category=DogCategory.objects.get(pk=pk)
        serializer=DogSeriliazer(category)
        return Response(serializer.data)
          
    
    def update(self,request,pk):
        category=DogCategory.objects.get(pk=pk)
        serializer=DogSeriliazer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   
        
    def create(self,request):
        serializer=DogSeriliazer(data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  
        
    def delete(self,request,pk):
        category=DogCategory.objects.get(pk=pk)
        category.delete()
        return Response(" Sucessfully Deleted")

# [concrete view class]-> 
                    #   |

class ReviewCreate(generics.CreateAPIView):
    serializer_class=ReviewSeriliazer
    def get_queryset(self):
        return Review.objects.all
    throttle_classes=[ReviewCreateThrottle]
       
    
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')  
        watch = WactchList.objects.get(pk=pk)
        review_user = self.request.user

        review_queryset = Review.objects.filter(wactchList=watch, review_user=review_user)
        if review_queryset.exists():
            raise ValidationError("BHAI AAP PEHLE HI REVIEW KAR CHUKE HO OR KITNA KAROGE")

        serializer.save(wactchList=watch, review_user=review_user)

     
     

class ReviewList(generics.ListAPIView):
    serializer_class=ReviewSeriliazer
    # permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        pk=self.kwargs['pk']
        return Review.objects.filter(wactchList=pk)
    # throttle_classes=[ReviewListThrottle]
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['review_user__username','active']

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSeriliazer
    permission_classes=[ReviewUserOrReadOnly]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

 
class StreamPlateformVS(viewsets.ModelViewSet):
    
     queryset=StreamPlateform.objects.all()
     serializer_class=StreamPlateformSerializers
     permission_classes=[AdminOrReadonly]
   
class StreamPlateformAV(APIView): 
    permission_classes=[AdminOrReadonly]   
    def get(self,request):
        plateform=StreamPlateform.objects.all()
        
        serializer=StreamPlateformSerializers(plateform,many=True,context={'request':request})
        return  Response(serializer.data)
  
    def post(self,request):
      serializer=StreamPlateformSerializers( data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      else:
          return Response(serializer.errors)
      
class WatchListAV(APIView):
    permission_classes=[AdminOrReadonly]
    def get(self,request):
         movies=WactchList.objects.all()
        
         serializer= WactchListSerializer(movies,many=True)
         return Response(serializer.data)
     
    def post(self,request):
         serializer = WactchListSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
         else:
            return Response(serializer.errors)

class WatchDetailAV(APIView):
    permission_classes=[AdminOrReadonly]
    def get(self,request,pk):
     try:
         movie=WactchList.objects.get(pk=pk)
     except movie.DoesNOtEXIST:
      return Response({'error':'movie not fount'},status=status.HTTP_404_NOT_FOUND) 
     serializer= WactchListSerializer(movie)
     return Response(serializer.data)
        
    def put(self,request,pk):
         movie=WactchList.objects.get(pk=pk)
         serializer=WactchListSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
         else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        movie = WactchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
        
class StreamPlateformDetailAv(APIView):
    def get(self,request,pk):
        try:
         plateform=StreamPlateform.objects.get(pk=pk)
        except StreamPlateform.DoesNotExist:
            return Response({'error':'not found'},status=status.HTTP_404_NOT_FOUND)
        
        serializer=StreamPlateformSerializers(plateform)
        return Response(serializer.data)
    
    def put(self,request,pk):
        plateform=StreamPlateform.objects.get(pk=pk)
        serializer=StreamPlateformSerializers(plateform,data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
     
    def delete(self,request,pk):
        plateform=StreamPlateform.objects.get(pk=pk)
        plateform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class WatchListGV(generics.ListAPIView):
    queryset=  WactchList.objects.all()
    serializer_class=WactchListSerializer
    pagination_class= WatchListPagination
    filter_backends=[filters.SearchFilter]
    search_fields=['title','plateform__name']
    