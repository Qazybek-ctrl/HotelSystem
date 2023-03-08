from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .models import Room, Booking
from .forms import BookingCreateForm

def is_valid_param(par):
    return par != '' and par is not None

class HomeView(ListView):
    template_name = 'bookingapp/home.html'
    queryset = Room.objects.all().order_by('name')

    def get(self, request):
        price_min = request.GET.get('price_min')
        price_max = request.GET.get('price_max')
        seat_min = request.GET.get('seat_min')
        seat_max = request.GET.get('seat_max')
        start_day = request.GET.get('start_day')
        end_day = request.GET.get('end_day')

        sortby = request.GET.get('sortby')
        reset = request.GET.get('res')

        if is_valid_param(start_day) & is_valid_param(end_day):
            booked_rooms = Booking.objects.filter(
                                                Q(start_day__lte=start_day, end_day__gte=start_day) | 
                                                Q(start_day__lte=end_day, end_day__gte=end_day) |
                                                Q(start_day__gte=start_day, end_day__lte=end_day)).values_list('room', flat=True)
            result_rooms = Room.objects.exclude(id__in=booked_rooms)
            self.queryset = result_rooms
        
        if is_valid_param(reset):
            self.queryset = Room.objects.all()

        if is_valid_param(price_min):
            self.queryset = self.queryset.filter(price__gte=price_min)

        if is_valid_param(price_max):
            self.queryset = self.queryset.filter(price__lte=price_max)
        
        if is_valid_param(seat_min):
            self.queryset = self.queryset.filter(seat__gte=seat_min)
        
        if is_valid_param(seat_max):
            self.queryset = self.queryset.filter(seat__lte=seat_max)
        
        if is_valid_param(sortby):
            if sortby == 'price_low':
                self.queryset = self.queryset.order_by('price')
            elif sortby == 'price_high':
                self.queryset = self.queryset.order_by('-price')
            elif sortby == 'seat_low':
                self.queryset = self.queryset.order_by('seat')
            elif sortby == 'seat_high':
                self.queryset = self.queryset.order_by('-seat')
        return super().get(request,)
    
class RoomView(DetailView):
    model = Room
    template_name = 'bookingapp/room.html'
    slug_field = 'name'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['booked_rooms'] = Booking.objects.filter(room__name=self.kwargs.get('slug'))
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        slug = self.kwargs.get('slug')
        queryset = queryset.filter(name=slug)
        return queryset
    

class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingCreateForm
    success_url = reverse_lazy('room')
    template_name = 'bookingapp/booknow.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room_now'] = Room.objects.get(name=self.kwargs['slug'])
        return context

    def dispatch(self, request, *args, **kwargs):
        self.room = Room.objects.get(name=kwargs['slug'])
        self.user = request.user
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        start_day = form.cleaned_data['start_day']
        end_day = form.cleaned_data['end_day']

        if Booking.objects.filter(
            Q(room=self.room) &
            ((Q(start_day__lte=start_day) & Q(end_day__gte=start_day)) |
            (Q(start_day__lte=end_day) & Q(end_day__gte=end_day)) |
            (Q(start_day__gte=start_day) & Q(end_day__lte=end_day)))
        ).exists():
            form.add_error(None, 'this period is unavailable')
            return self.form_invalid(form)
        
        form.instance.room = self.room
        form.instance.user = self.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('room', kwargs={'slug': self.room.name})

    
class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Booking
    success_url = reverse_lazy('room')
    template_name = 'bookingapp/person.html'

    def post(self, request, *args, **kwargs):
        booking = self.get_object()
        booking.delete()
        return redirect('room', slug=booking.room.name)

    def get_success_url(self):
        room_name = self.object.room.name
        return reverse_lazy('room', kwargs={'slug': room_name})

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user, id=self.kwargs['pk'])
    


