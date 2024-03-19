from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Issue


def home(request):
    return render(request, 'itreporting/home.html', {'title': 'Welcome' })

def about(request):
    return render(request, 'itreporting/home.html', {'title': 'Welcome'})

def report(request):
   
    daily_report = {'issues': Issue.objects.all(), 'title': 'Issues Reported'}
    return render(request, 'itreporting/report.html', daily_report)

class PostListView(ListView):
    model = Issue
    ordering = ['date_subimtted']
    template_name = 'itreporting/report.html'
    context_object_name = 'issues'
    paginate_by = 10  # Optional pagination

class PostDetailView(DetailView):
    model = Issue
    ordering = ['-date_subimtted']
    template_name = 'itreporting/issue_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Issue
    template_name = 'itreporting/issue_form.html'
    fields = ['type', 'room', 'urgent', 'details']

    def form_valid(self, form): 

        form.instance.author = self.request.user
        return super().form_valid(form)
