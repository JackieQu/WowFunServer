from django.urls import path, include
from snippet import views
from rest_framework.urlpatterns import format_suffix_patterns

from snippet.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_datail),

    path('snippets2/', views.snippet_list2),
    path('snippets2/<int:pk>/', views.snippet_detail2),

    path('snippets3/', views.SnippetList.as_view()),
    path('snippets3/<int:pk>/', views.SnippetDetail.as_view()),

    path('snippets4/', views.SnippetList2.as_view()),
    path('snippets4/<int:pk>/', views.SnippetDetail2.as_view()),

    path('snippets5/', views.SnippetList3.as_view(), name='snippet-list'),
    path('snippets5/<int:pk>/', views.SnippetDetail3.as_view(), name='snippet-detail'),

    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),

    path('', views.api_root),
    path('snippets5/<int:pk>/highlight/', views.SnippetHightlight.as_view(), name='snippet-highlight'),
]

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns += [
    path('snippets6/', snippet_list, name='snippet-list'),
    path('snippets6/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('snippets6/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('users2', user_list, name='user-list'),
    path('users2/<int:pk>/', user_detail, name='user-detail'),
]

# router = DefaultRouter()
# router.register(r'snippets', views.SnippetViewSet)
# router.register(r'users', views.UserViewSet)

# urlpatterns += [
#     path('', include(router.urls)),
# ]

urlpatterns = format_suffix_patterns(urlpatterns)