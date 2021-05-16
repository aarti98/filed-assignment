from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.exceptions import ValidationError
from rest_framework import viewsets, status, views
from rest_framework.response import Response

from audio_files.constant import FILE_TYPES
from audio_files.models import AudiobookAudioFileModel, SongAudioFileModel, PodcastAudioFileModel
from audio_files.serializers import (CreateAudioFileSerializer, AudiobookAudioFileListRetrieveSerializer,
                                     SongAudioFileListRetrieveSerializer, PodcastAudioFileListRetrieveSerializer,
                                     UpdateAudioFileSerializer)


class AudioFileCreateListViews(views.APIView):
    """
    view to create an audio object given audio file type and metadata
    view to list all objects of a given audio type
    """
    # to create a new object of any given type
    def post(self, request):
        context = {'view': self, 'request': request}

        serializer = CreateAudioFileSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        response = serializer.create(serializer.validated_data)
        return Response(data=response, status=status.HTTP_200_OK)

    def get(self, request, audio_file_type):
        # to get object from song model
        if audio_file_type == FILE_TYPES[0]:
            queryset = SongAudioFileModel.objects.all()
            serializer = SongAudioFileListRetrieveSerializer
        elif audio_file_type == FILE_TYPES[1]:
            queryset = PodcastAudioFileModel.objects.all()
            serializer = PodcastAudioFileListRetrieveSerializer
        elif audio_file_type == FILE_TYPES[2]:
            queryset = AudiobookAudioFileModel.objects.all()
            serializer = AudiobookAudioFileListRetrieveSerializer
        else:
            raise Http404

        data = serializer(queryset, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)


class AudioFileRetrieveUpdateDeleteViewSet(viewsets.ModelViewSet):
    """
    view to get detail of an audio object given its type and id
    view to update detail of an audio object given its type and id and some meta data
    view to delete an audio object given its type and id
    """
    serializer_class = SongAudioFileListRetrieveSerializer
    queryset = SongAudioFileModel.objects.all()

    def get_object(self):
        filter_kwargs = {
            'pk': self.request.parser_context['kwargs']['pk'],
        }
        # to get object from song model
        if self.request.parser_context['kwargs']['audio_file_type'] == FILE_TYPES[0]:
            return get_object_or_404(SongAudioFileModel, **filter_kwargs)
        # to get object from podcast model
        elif self.request.parser_context['kwargs']['audio_file_type'] == FILE_TYPES[1]:
            return get_object_or_404(PodcastAudioFileModel, **filter_kwargs)
        # to get object of audio book type
        elif self.request.parser_context['kwargs']['audio_file_type'] == FILE_TYPES[2]:
            return get_object_or_404(AudiobookAudioFileModel, **filter_kwargs)
        else:
            raise Http404

    def get_serializer_class(self):
        if self.action == 'retrieve':
            # to get data from song model
            if self.request.parser_context['kwargs']['audio_file_type'] == FILE_TYPES[0]:
                return SongAudioFileListRetrieveSerializer
            # to get data from podcast model
            elif self.request.parser_context['kwargs']['audio_file_type'] == FILE_TYPES[1]:
                return PodcastAudioFileListRetrieveSerializer
            # to get data from audio book model
            elif self.request.parser_context['kwargs']['audio_file_type'] == FILE_TYPES[2]:
                return AudiobookAudioFileListRetrieveSerializer
            else:
                return self.serializer_class
        elif self.action == 'partial_update':
            return self.serializer_class
        else:
            return self.serializer_class

    def retrieve(self, request, *args, **kwargs):
        return super(AudioFileRetrieveUpdateDeleteViewSet, self).retrieve(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        audio_object = self.get_object()
        context = {'view': self, 'request': request}
        kwargs['partial'] = True
        request.data['file_type'] = request.parser_context['kwargs']['audio_file_type']
        serializer = UpdateAudioFileSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        response = serializer.update(instance=audio_object, validated_data=serializer.validated_data)
        return Response(data=response, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        return super(AudioFileRetrieveUpdateDeleteViewSet, self).destroy(request, *args, **kwargs)
