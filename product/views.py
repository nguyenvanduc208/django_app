from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from rest_framework import mixins, generics
import pprint

pp = pprint.PrettyPrinter(indent=4)
pprint = pp.pprint

# class ProductList(APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductList(mixins.ListModelMixin, mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get(self, request):
        print(">>>")
        print(dir(self))
        print(self.queryset)
        return self.list(request)

    def post(self, request, *args, **kwargs):
        print(">>>  ", self.get_success_headers(self.get_serializer(data=request.data)))
        return self.create(request, *args, **kwargs)
    
    
class DestroyProduct(mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print(">>>>>")
        pprint(kwargs)
        # self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def delete(self, request, *args, **kwargs):
        print(kwargs)
        return self.destroy(request, *args, **kwargs)