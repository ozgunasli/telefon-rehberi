from django.shortcuts import render
from .models import Guide, Group
from django.views import generic
from django.views.generic import UpdateView, DeleteView, CreateView
from django.shortcuts import get_object_or_404
from .forms import GuideForm, GroupForm


class NumberListView(generic.ListView):
    model = Guide
    template_name = 'phone_list.html'

    def get_queryset(self):
        return Guide.objects.all()


def number_detail(request, pk):
    numbers = get_object_or_404(Guide, pk=pk)
    return render(request, 'phone_detail.html', {'numbers': numbers})


class NumberUpdateView(UpdateView):
    model = Guide
    form_class = GuideForm
    template_name = 'phone_edit.html'
    success_url = '/'

    def get_object(self):
        return Guide.objects.get(pk=self.kwargs['pk'])

    def form_valid(self, form):
        self.objects = form.save(commit=False)
        self.objects.user = self.request.user
        self.objects.save()
        return super().form_valid(form)


class NumberDeleteView(DeleteView):
    model = Guide
    success_url = '/'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class NumberCreateView(CreateView):
    model = Guide
    form_class = GuideForm
    template_name = 'phone_edit.html'
    success_url = '/'

    def form_valid(self, form):
        self.objects = form.save(commit=False)
        self.objects.user = self.request.user
        self.objects.save()
        return super().form_valid(form)


class GroupListView(generic.ListView):
    model = Group
    template_name = 'group_list.html'

    def get_queryset(self):
        return Group.objects.all()


def group_detail(request, pk):
    groups = get_object_or_404(Group, pk=pk)
    return render(request, 'group_detail.html', {'groups': groups})


class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'group_edit.html'
    success_url = '/group'

    def get_object(self):
        return Group.objects.get(pk=self.kwargs['pk'])

    def form_valid(self, form):
        self.objects = form.save(commit=False)
        self.objects.user = self.request.user
        self.objects.save()
        return super().form_valid(form)


class GroupDeleteView(DeleteView):
    model = Group
    success_url = '/group'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'group_edit.html'
    success_url = '/group'

    def get_object(self):
        return Group.objects.get(pk=self.kwargs['pk'])

    def form_valid(self, form):
        self.objects = form.save(commit=False)
        self.objects.user = self.request.user
        self.objects.save()
        return super().form_valid(form)