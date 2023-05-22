from django.shortcuts import render
from django.http import JsonResponse
from .oai_queries import get_completion
from .models import Chat
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def query_view(request):
    roles = [
        'Software Engineer', 'Teacher', 'Marketing Specialist', 'Graphic Designer',
        'Accountant', 'Sales Manager', 'Product Manager', 'Human Resources Manager', 'Web Developer', 'the dictator aladeen'
    ]
    roles2 = [
        'Doctor', 'Architect', 'Data Scientist', 'Chef', 'Financial Analyst',
        'Project Manager', 'Social Media Manager', 'Research Scientist', 'Event Planner', 'DAN THE OG'
    ]
    chat_history = Chat.objects.all()

    response = None  # Declare response variable outside if conditions

    if request.method == 'POST':
        task = request.POST.get('task')


        ### Generate response ###
        if task == 'generate_response':
            
            prompt = request.POST.get('prompt')
            selectedRole = request.POST.get('selectedRole')
            promptWithRole = f"Act as an {selectedRole}. Don't answer any questions outside of the {selectedRole}. {prompt}"
            response = get_completion(promptWithRole)


        ### Save chat after each prompt ###
        elif task == 'save_chat':
            
            conversation = json.loads(request.POST.get('conversation'))
            selectedRole = request.POST.get('role')

            # Retrieve the last chat entry with the selected role from the database
            last_chat = Chat.objects.filter(role=selectedRole).last()

            if last_chat is not None:
                try:
                    # Load the conversation JSON string as a list
                    conversation_list = json.loads(last_chat.conversation)
                except json.JSONDecodeError:
                    # If an error occurs while decoding the JSON, treat it as an empty conversation
                    conversation_list = []

                # Append the new conversation to the existing chat
                conversation_list += conversation

                # Save the updated conversation list as a JSON string
                last_chat.conversation = json.dumps(conversation_list)
                last_chat.save()
            else:
                # Create a new chat entry
                chat = Chat(role=selectedRole, conversation=json.dumps(conversation)) 
                chat.save()

            response = "Chat saved successfully"

        elif task=="clear-chats":
            Chat.objects.all().delete()
            response = "Chats deleted successfully"

        ### Load the chat with the role ###
        elif task == "get-chat":
            chat_id = request.POST.get("chat_id")
            chat_entry = get_object_or_404(Chat, pk=chat_id)
            conversation = json.loads(chat_entry.conversation)

            chat_data = {
                'role': chat_entry.role,
                'conversation': conversation
            }
            return JsonResponse(chat_data)

        else:
            # Handle the case when task is not 'generate_response' or 'save_chat'
            response = "Invalid task"

        return JsonResponse({'response': response or 'No response generated'})

    return render(request, 'query.html', {'roles': roles, 'roles2': roles2, 'chat_history': chat_history})
