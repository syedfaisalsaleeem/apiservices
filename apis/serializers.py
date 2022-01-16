from rest_framework import serializers

from .models import File, Folder,Document, Topic

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = "__all__"

class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = "__all__"

class GetDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"
        depth = 1

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"


