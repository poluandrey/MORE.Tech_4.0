from rest_framework.routers import DefaultRouter

from user import views

router = DefaultRouter()
router.register('', views.EmployeeView, basename='employee')

urlpatterns = router.urls
