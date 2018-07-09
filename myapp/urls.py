from django.conf.urls import url

from myapp.views import SexCountAPIView, UserDataAPIView

urlpatterns = [
    url(r'^get_sex_count', view=SexCountAPIView.as_view(), name="get_sex_count"),
    url(r'^get_user_data', view=UserDataAPIView.as_view(), name="get_user_data"),
]
