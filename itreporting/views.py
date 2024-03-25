from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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
    template_name = 'itreporting/issue_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView ):
    model = Issue
    template_name = 'itreporting/issue_form.html'
    fields = ['type', 'room', 'urgent', 'details']

    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 

    model = Issue
    # template_name = 'itreporting/issue_form.html'
    fields = ['type', 'room', 'details']
    
    def test_func(self):
        issue = self.get_object()
        return self.request.user == issue.author
    
    def handle_no_permission(self):
        messages.warning(self.request, 'You are not allowed to edit this post')
        # return reverse('itreporting:issue-detail', kwargs={'pk': self.kwargs['pk']})
        return HttpResponseRedirect(reverse('itreporting:issue-detail', kwargs={'pk': self.kwargs['pk']}))


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Issue
    success_url = '/itreporting/issues'

    def test_func(self):
        issue = self.get_object()
        return self.request.user == issue.author
    
    def handle_no_permission(self):
        messages.warning(self.request, 'You are not allowed to delete this post')
        # return reverse('itreporting:issue-detail', kwargs={'pk': self.kwargs['pk']})
        return HttpResponseRedirect(reverse('itreporting:issue-detail', kwargs={'pk': self.kwargs['pk']}))