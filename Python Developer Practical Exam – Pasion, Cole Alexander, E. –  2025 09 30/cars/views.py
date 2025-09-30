from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from django.views import View
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Car
from .forms import CarForm


class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = "cars/create_car_form.html"
    success_url = reverse_lazy("car-list")

    def form_valid(self, form):
        last = Car.objects.order_by("-car_key").first()
        form.instance.car_key = (last.car_key + 1) if last else 1
        messages.success(self.request, "Car created successfully!")
        return super().form_valid(form)


class CarListView(ListView):
    model = Car
    template_name = "cars/index.html"
    context_object_name = "car_list"
    paginate_by = 5

    def get_queryset(self):
        color = self.request.GET.get("color")
        qs = Car.objects.all().order_by("car_key")
        return qs.filter(car_color=color) if color else qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["colors"] = Car.COLORS
        return context


class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = "cars/update_car_form.html"
    success_url = reverse_lazy("car-list")

    def form_valid(self, form):
        messages.success(self.request, "Car updated successfully")
        return super().form_valid(form)


class CarDeleteView(View):
    def post(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        car.delete()
        messages.success(request, "Car deleted successfully.")
        return redirect("car-list")
