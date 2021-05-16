from django.urls import re_path

from audio_files.views import AudioFileCreateListViews, AudioFileRetrieveUpdateDeleteViewSet

urlpatterns = [
    re_path(
        r'^audio_files/?$',
        AudioFileCreateListViews.as_view(),
        name='audio_file_create_view'
    ),
    re_path(
        r'^(?P<audio_file_type>[a-z_]+)/?$',
        AudioFileCreateListViews.as_view(),
        name='audio_file_list_view'
    ),
    re_path(
        r'^(?P<audio_file_type>[a-z_]+)/(?P<pk>[0-9]+)?$',
        AudioFileRetrieveUpdateDeleteViewSet.as_view({
            'patch': 'partial_update',
            'get': 'retrieve',
            'delete': 'destroy'
        }),
        name='audio_file_update_detail_delete_view'
    )
]
