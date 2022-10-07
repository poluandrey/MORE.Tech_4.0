from rest_framework.routers import DefaultRouter

from company import views


router = DefaultRouter()
router.register('task', viewset=views.TaskView, basename='task')

urlpatterns = router.urls
