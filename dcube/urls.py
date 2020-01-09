from django.urls import path,include
from django.views.generic import TemplateView

from . import views

app_name = 'dcube'

urlpatterns = [
    path('', TemplateView.as_view(template_name='dcube/index.html'), name='index'),
    path('team/', TemplateView.as_view(template_name='dcube/team.html'), name='team'),
    path('publications/', TemplateView.as_view(template_name='dcube/publications.html'), name='publications'),
    path('projects/', TemplateView.as_view(template_name='dcube/projects.html'), name='projects'),
    path('pro/', TemplateView.as_view(template_name='dcube/blog-details.html'), name='each_project'),

    # path('projects/<int:pk>/', views.projects, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]