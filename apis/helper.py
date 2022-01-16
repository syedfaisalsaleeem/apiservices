from .models import Folder, Topic
from .serializers import FolderSerializer, TopicSerializer


def checkfolderexsist(data):
    folder = Folder.objects.filter(folder_name=data).first()
    if folder:
        return True, folder.id
    else:
        return False, None

def unique_list(data):
    return list(set(data))

def checktopicexsist(data):
    list_topicsid = []
    data = unique_list(data)
    for values in data:
        topic = Topic.objects.filter(topics=values).first()
        if topic:
            list_topicsid.append(topic.id)
        else:
            topicstatus = create_topic_db({"topics":values})
            if topicstatus[0]:
                list_topicsid.append(topicstatus[1]['id'])
            
    
    return list_topicsid 


def create_folder_db(data):
    folder_serializer = FolderSerializer(data=data)
    if folder_serializer.is_valid():
        folder_serializer.save()
        return True, folder_serializer.data
    else:
        return False, folder_serializer.errors

def create_topic_db(data):
    topic_serializer = TopicSerializer(data=data)
    if topic_serializer.is_valid():
        topic_serializer.save()
        return True, topic_serializer.data
    else:
        return False, topic_serializer.errors
