from  django.conf.urls import url
from exam import views as examviews
urlpatterns = [
    url("^$",examviews.showtest),
    url("showresult/",examviews.showresult),
]
