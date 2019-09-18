"""cvselector URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from candidates import views
from django.conf import settings
from django.conf.urls.static import static
from candidates.views import CandidateList, JobList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('candidates/', CandidateList.as_view(),name="candidates"),
    path('candidates/<int:candidate_id>', views.candidate_detail,name="candidate_detail"),
    path('jobs/', JobList.as_view(),name="jobs"),
    path('jobs/<int:job_id>', views.jobs_detail,name="job_detail"),

]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    