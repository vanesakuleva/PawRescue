# from django.shortcuts import render, get_object_or_404
# from django.views import generic as views
# from PawRescue.adoption.models import Adoption
#
#
# class AdoptionDetailView(views.DetailView):
#     model = Adoption
#     template_name = 'adoption/adoption_details.html'
#     context_object_name = 'adoption'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['email'] = self.object.user.email
#         return context
