from django.shortcuts import get_object_or_404, redirect, render

from conversation.models import Conversation, ConversationMessage
from item.models import Item
from conversation.forms import ConversationMessageForm

# Create your views here.


def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')

    conversations = Conversation.objects.filter(
        item=item.filter(member__in=[request.user]))

    if conversations:
        pass
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.add(request.user)
            conversation.add(request.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            return redirect('item:detail', pk=item_pk)

    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/new.html', {
        'form': form,
    })
