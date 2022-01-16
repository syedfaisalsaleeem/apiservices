from django.http.response import JsonResponse

from .helper import checkfolderexsist, checktopicexsist, create_folder_db, create_topic_db
from .serializers import FileSerializer, FolderSerializer,DocumentSerializer, GetDocumentSerializer, TopicSerializer
from .models import Folder, Document, Topic

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.decorators import parser_classes

@api_view(['GET'])
def folder_names(request):
    folder = Folder.objects.all()
    serializer = FolderSerializer(folder, many=True)
    return Response(serializer.data)



@api_view(['POST'])
@parser_classes([JSONParser])
def create_folder(request,format=None):
    folder_status = create_folder_db(request.data)
    if folder_status[0]:
        return Response(folder_status[1], status=status.HTTP_201_CREATED)
    else: 
        return Response(folder_status[1], status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@parser_classes([JSONParser])
def create_topic(request,format=None):
    topic_status = create_topic_db(request.data)
    if topic_status[0]:
        return Response(topic_status[1], status=status.HTTP_201_CREATED)
    else: 
        return Response(topic_status[1], status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def listdocuments(request,*args,**kwargs):
    folder_check = kwargs.get('folder',None)
    topic_check = request.GET.get('topic',None)
    if folder_check:
        folder_id = Folder.objects.filter(folder_name=folder_check).first()
        if folder_id:
            if topic_check:
                topic_id = Topic.objects.filter(topics=topic_check).first()
                if topic_id:
                    document = Document.objects.filter(folder_name=folder_id.id).filter(topics=topic_id.id)
                    serializer = GetDocumentSerializer(document, many=True)
                    return Response(serializer.data)
                else:
                    return Response("topic not found",status=status.HTTP_400_BAD_REQUEST)
            else:
                document = Document.objects.filter(folder_name=folder_id.id).all()
                serializer = GetDocumentSerializer(document, many=True)
                return Response(serializer.data)
        else:
            return Response("Folder not found",status=status.HTTP_400_BAD_REQUEST)
    else:
        document = Document.objects.all()
        serializer = GetDocumentSerializer(document, many=True)
        return Response(serializer.data)

@api_view(['POST'])
@parser_classes([JSONParser])
def create_document(request,format=None):
    if request.data.get('folder_name',None):
        try:
            folderexsist = checkfolderexsist(request.data['folder_name'])
            if folderexsist[0]:
                folder_id = folderexsist[1]
            else:
                folder_status_value = create_folder_db(
                    {"folder_name":request.data['folder_name']})
                if folder_status_value[0]:
                    folder_id = folder_status_value[1]['id']
                else: 
                    return JsonResponse({"message":folder_status_value[1]}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({"message":str(e)}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({"message":"folder_name key doesnot exsist in post request"}, status=status.HTTP_400_BAD_REQUEST)

    if request.data.get('topics',None):
        try:
            topic_idlist = checktopicexsist(request.data['topics'])
        except Exception as e:
            return JsonResponse({"message":str(e)+" error in topics key"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({"messsage":"topics key doesnot exsist in post request"}, status=status.HTTP_400_BAD_REQUEST)     

    data = request.data
    data['folder_name'] = folder_id
    data["topics"] = topic_idlist
    document_serializer = DocumentSerializer(data=data)
    if document_serializer.is_valid():
        document_serializer.save()
        return JsonResponse({"message":"Document is created","body":document_serializer.data}, status=status.HTTP_201_CREATED,safe=True) 
    return Response(document_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def listtopics(request):
    topic = Topic.objects.all()
    serializer = TopicSerializer(topic, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def uploadfile(request):

    file_serializer = FileSerializer(data=request.data)
    if file_serializer.is_valid():
        file_serializer.save()
        return JsonResponse({'message':'File is uploaded','body':file_serializer.data}, status=status.HTTP_201_CREATED,safe=True)
    return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


