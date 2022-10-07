from rest_framework.routers import DefaultRouter

from company import views


router = DefaultRouter()
router.register('task', viewset=views.TaskView, basename='task')
router.register('department', viewset=views.DepartmentView, basename='department')

urlpatterns = router.urls
