from django.urls import path
from .views import CarCreateView, CarListView, CarUpdateView, CarDeleteView

urlpatterns = [
    path("", CarListView.as_view(), name="car-list"),
    path("create/", CarCreateView.as_view(), name="car-create"),
    path("update/<int:pk>/", CarUpdateView.as_view(), name="car-update"),
    path("delete/<int:pk>/", CarDeleteView.as_view(), name="car-delete"),
]
