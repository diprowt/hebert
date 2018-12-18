"""Posts URLs."""

# Django
from django.urls import path

# Views
from posts import views

urlpatterns = [

    path(
        route='',
        view=views.PostsFeedView.as_view(),
        name='feed'
    ),

    path(
        route='posts/nuevo/',
        view=views.CreatePostView.as_view(),
        name='create'
    ),

    # path(
    #     route='posts/nuevo/',
    #     view=views.CreatePostViewxd.as_view(),
    #     name='creates'
    # ),

    # path(
    #     route='posts/buscar/',
    #     view=views.BuscarViews.as_view(),
    #     name='buscar'
    # ),

    # path(
    #     route='posts/♥<int:pk>/',
    #     view=views.PostDetailView,
    #     name='detail'
    # ),

    path(
        route='posts/♥<int:pk>/',
        view=views.PostDetailView,
        name='detail'
    ),

    path(
        route='delete/♥<int:pk>/',
        view=views.PostDeleteView,
        name='delete'
    ),

    path(
        route='edit/♥<int:pk>/',
        view=views.PostEditView.as_view(),
        name='edit'
    )
]
