from  django.conf.urls import url
from testapp import views as testappviews
urlpatterns = [
    url("contact/",testappviews.contact),
    url("about/",testappviews.about),
    url("greeting/",testappviews.greeting),
    url("employee/",testappviews.employee_info_view),
]
