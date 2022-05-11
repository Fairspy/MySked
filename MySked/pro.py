
from .models import Event
import symbl
from datetime import date

def process(local_path):
    entities = [
        {
            "customType": "custom_type",
            "text": "entity_name"
        }
    ]
    params = {
        'name': "Meeting",
        "detectEntities": "true",
        "entities":entities,
        'enableSpeakerDiarization': "true",
        "diarizationSpeakerCount": "3"
    }
# Process audio file
    conversation_object = symbl.Video.process_file(file_path=local_path)
#print(conversation_object.get_messages())
#print(conversation_object.get_action_items())
    data = conversation_object.get_action_items()
    data1 = data.__dict__
    print(data1)
    meet = data1['_action_items']
    for i in meet:
        sub = i.__dict__
        task = (sub['_text'])
        for j in sub['_entities']:
            su = j.__dict__
            if(su['_value']):
                time = su['_value']
            else:
                time = date.today()
            events = Event(
                title = task,
                start_time = time
            )
            events.save()



