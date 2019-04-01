from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages

def create_object_log(obj,user_id,action_flag,form=None, message=None):          
       
    is_logging = False
    
    if action_flag == "add" :
        action_flag = ADDITION
        change_message = "New Object Add"
        is_logging = True
    elif action_flag == "edit" :
        action_flag = CHANGE
        change_message = "Object changed"
        is_logging = True
    elif action_flag == "delete" :
        action_flag = DELETION
        change_message = str(obj.__dict__)
        is_logging = True
        
    if form :
        if form.has_changed():
            # change_message = "Changed fields : " + ", ".join(form.changed_data)
            i=0
            logmass =[]
            for x in form.changed_data:
                logmass.append(form.changed_data[i] + " = " + str(form.initial[form.changed_data[i]]))
                i=i+1
            change_message = "Changed fields and Intial data : " + " , ".join(logmass)
            is_logging = True
        else :
            is_logging = False
            
    if is_logging :
        LogEntry.objects.log_action(
            user_id = user_id.id,
            content_type_id = ContentType.objects.get_for_model(obj).id,
            object_id = obj.id,
            object_repr = "",
            change_message = message or change_message ,
            action_flag = action_flag,
        )
        
def get_history_for_object(obj, user=None):
    content_type_id = ContentType.objects.get_for_model(obj).id
    entry = LogEntry.objects.filter(content_type_id = content_type_id,
                                   object_id = obj.id)
    if user and user.profile.profile_type == "U":
        entry = entry.exclude(action_flag = 8)
    return entry