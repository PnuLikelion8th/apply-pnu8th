from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .forms import ApplyFormForm
# Create your views here.
def index(request):
    return render(request, 'index.html')


class Apply(CreateView):
    form_class = ApplyFormForm
    template_name = 'apply.html'
    success_url = 'index'

    # def get(self, request, *args, **kwargs):
    #     if self.request.user.is_authenticated:
    #         if self.request.user.profile.nickname == "":
    #             return redirect('profile_update')
    #         else:
    #             self.object = None        
    #             return super().get(request, *args, **kwargs)
    #     else:
    #         return redirect('login_main')


# from django.urls import reverse
# class CommunityUpdate(UpdateView):
#     model = CommunityPost
#     form_class = CommunityPostForm
#     template_name = 'community_create.html'
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         if self.object.author == self.request.user.profile:
#             return super().get(request, *args, **kwargs)
#         else:
#             raise PermissionDenied
#     def get_success_url(self):
#         return reverse('community_detail', kwargs={
#             'pk': self.object.pk,
#         })
    
# from django.urls import reverse_lazy
# class CommunityDelete(DeleteView):
#     model = CommunityPost
#     template_name = 'community_detail.html'
#     success_url = reverse_lazy('community')

#     def post(self, request, *args, **kwargs):
#         if self.request.user.profile == self.get_object().author:
#             return self.delete(request, *args, **kwargs)
#         else:
#             raise PermissionDenied
    
