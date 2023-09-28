from django.urls import path
from .views import ProductList, DestroyProduct

urlpatterns = [
    path("", ProductList.as_view()),
    path("delete/<int:pk>", DestroyProduct.as_view())
]
