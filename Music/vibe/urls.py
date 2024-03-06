

    # other URL patterns
from django.urls import path
from.import views
urlpatterns=[
    path("checkvibelogin", views.checkvibelogin, name="checkvibelogin"),
    path("checkRegistration",views.checkRegistration,name="checkRegistration"),
    path("checkpackages", views.checkpackages, name="checkpackages"),
    path("viewplaces",views.viewplaces,name="viewplaces"),
    path("changepassword",views.checkChangePassword,name="changepassword"),
    path("logout",views.logout,name="logout"),

path('contactmail',views.contactmail,name='contactmail'),

]



