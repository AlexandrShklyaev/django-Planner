from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from goals import views

urlpatterns = [
    path("goal_category/create", views.GoalCategoryCreateView.as_view()),
    path("goal_category/list", views.GoalCategoryListView.as_view()),
    path("goal_category/<pk>", views.GoalCategoryView.as_view()),

    path("goal/create", views.GoalCreateView.as_view()),
    path("goal/list", views.GoalListView.as_view()),
    path("goal/<pk>", views.GoalView.as_view()),

    path('goal_comment/create', views.GoalCommentCreateView.as_view()),
    path('goal_comment/list', views.GoalCommentListView.as_view()),
    path('goal_comment/<int:pk>', views.GoalCommentView.as_view()),
]
