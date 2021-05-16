from django.contrib import admin
from audio_files.models import SongAudioFileModel, AudiobookAudioFileModel, PodcastAudioFileModel


class SongAudioFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']


class PodcastAudioFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']


class AudioBookAudioFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author']
    search_fields = ['id', 'title', 'author']


admin.site.register(SongAudioFileModel, SongAudioFileAdmin)
admin.site.register(PodcastAudioFileModel, PodcastAudioFileAdmin)
admin.site.register(AudiobookAudioFileModel, AudioBookAudioFileAdmin)
