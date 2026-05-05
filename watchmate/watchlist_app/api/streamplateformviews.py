# class StreamPlateformVS(viewsets.ViewSet):
#     def list(self,request):
#         queryset=StreamPlateform.objects.all()
#         serializer=StreamPlateformSerializers(queryset,many=True)
#         return Response(serializer.data)
    
    
#     def retrieve(self,request,pk=None):
#         queryset=StreamPlateform.objects.all()
#         watchlist=get_object_or_404(queryset,pk=pk)
#         serializer=StreamPlateformSerializers(StreamPlateform)
#         return Response(serializer.data)
    
#     def create(self,request):
#         serializer=StreamPlateformSerializers( data=request.data)
#         if serializer.is_valid():
#           serializer.save()
#           return Response(serializer.data)
#         else:
#           return Response(serializer.errors)