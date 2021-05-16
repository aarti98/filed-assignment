from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from audio_files.models import SongAudioFileModel, AudiobookAudioFileModel, PodcastAudioFileModel
from audio_files.constant import FILE_TYPES


class CreateAudioFileSerializer(serializers.Serializer):
    file_type = serializers.ChoiceField(choices=FILE_TYPES)
    meta_data = serializers.JSONField()

    def create(self, validated_data):
        # to instantiate Song type serializer
        if validated_data['file_type'] == FILE_TYPES[0]:
            serializer = SongAudioFileCreateUpdateSerializer

        # to instantiate Podcast type serializer
        elif validated_data['file_type'] == FILE_TYPES[1]:
            serializer = PodcastAudioFileCreateUpdateSerializer

        # to instantiate Audiobook type serializer
        else:
            serializer = AudiobookAudioFileCreateUpdateSerializer

        # to send data to serializer and create audio file instance
        serializer = serializer(data=validated_data['meta_data'], context=self.context)
        serializer.is_valid(raise_exception=True)
        return serializer.create(serializer.validated_data)


class UpdateAudioFileSerializer(serializers.Serializer):
    file_type = serializers.ChoiceField(choices=FILE_TYPES)
    meta_data = serializers.JSONField()

    def update(self, instance, validated_data):
        # to instantiate Song type serializer
        if validated_data['file_type'] == FILE_TYPES[0]:
            serializer = SongAudioFileCreateUpdateSerializer

        # to instantiate Podcast type serializer
        elif validated_data['file_type'] == FILE_TYPES[1]:
            serializer = PodcastAudioFileCreateUpdateSerializer

        # to instantiate Audiobook type serializer
        else:
            serializer = AudiobookAudioFileCreateUpdateSerializer

        # to send data to serializer and create audio file instance
        serializer = serializer(data=validated_data['meta_data'], context=self.context, partial=True)
        serializer.is_valid(raise_exception=True)
        return serializer.update(instance, serializer.validated_data)


class SongAudioFileCreateUpdateSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        instance = super().create(validated_data)
        return SongAudioFileCreateUpdateSerializer(instance).data

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        return SongAudioFileCreateUpdateSerializer(instance).data

    class Meta:
        model = SongAudioFileModel
        fields = ['id', 'name', 'duration', 'uploaded_time']


class PodcastAudioFileCreateUpdateSerializer(serializers.ModelSerializer):
    participants = serializers.ListField(
        allow_null=True, max_length=10, required=False
    )

    def validate_participants(self, participants):
        for participant in participants:
            if type(participant) != str:
                raise ValidationError("Participants should be a list of valid strings")

    def create(self, validated_data):
        instance = super().create(validated_data)
        return PodcastAudioFileCreateUpdateSerializer(instance).data

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        return PodcastAudioFileCreateUpdateSerializer(instance).data

    class Meta:
        model = PodcastAudioFileModel
        fields = ['id', 'name', 'duration', 'uploaded_time', 'host', 'participants']


class AudiobookAudioFileCreateUpdateSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        instance = super().create(validated_data)
        return AudiobookAudioFileCreateUpdateSerializer(instance).data

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        return AudiobookAudioFileCreateUpdateSerializer(instance).data

    class Meta:
        model = AudiobookAudioFileModel
        fields = ['id', 'title', 'author', 'narrator', 'duration', 'uploaded_time']


class SongAudioFileListRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongAudioFileModel
        fields = ['id', 'name', 'duration', 'uploaded_time']


class PodcastAudioFileListRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = PodcastAudioFileModel
        fields = ['id', 'name', 'duration', 'uploaded_time', 'host', 'participants']


class AudiobookAudioFileListRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudiobookAudioFileModel
        fields = ['id', 'title', 'author', 'narrator', 'duration', 'uploaded_time']
