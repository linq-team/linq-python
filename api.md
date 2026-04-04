# Shared Types

```python
from linq.types import (
    ChatHandle,
    LinkPartResponse,
    MediaPartResponse,
    Reaction,
    ReactionType,
    ServiceType,
    TextDecoration,
    TextPartResponse,
)
```

# Chats

Types:

```python
from linq.types import (
    Chat,
    LinkPart,
    MediaPart,
    MessageContent,
    TextPart,
    ChatCreateResponse,
    ChatUpdateResponse,
    ChatLeaveChatResponse,
    ChatSendVoicememoResponse,
)
```

Methods:

- <code title="post /v3/chats">client.chats.<a href="./src/linq/resources/chats/chats.py">create</a>(\*\*<a href="src/linq/types/chat_create_params.py">params</a>) -> <a href="./src/linq/types/chat_create_response.py">ChatCreateResponse</a></code>
- <code title="get /v3/chats/{chatId}">client.chats.<a href="./src/linq/resources/chats/chats.py">retrieve</a>(chat_id) -> <a href="./src/linq/types/chat.py">Chat</a></code>
- <code title="put /v3/chats/{chatId}">client.chats.<a href="./src/linq/resources/chats/chats.py">update</a>(chat_id, \*\*<a href="src/linq/types/chat_update_params.py">params</a>) -> <a href="./src/linq/types/chat_update_response.py">ChatUpdateResponse</a></code>
- <code title="post /v3/chats/{chatId}/leave">client.chats.<a href="./src/linq/resources/chats/chats.py">leave_chat</a>(chat_id) -> <a href="./src/linq/types/chat_leave_chat_response.py">ChatLeaveChatResponse</a></code>
- <code title="get /v3/chats">client.chats.<a href="./src/linq/resources/chats/chats.py">list_chats</a>(\*\*<a href="src/linq/types/chat_list_chats_params.py">params</a>) -> <a href="./src/linq/types/chat.py">SyncListChatsPagination[Chat]</a></code>
- <code title="post /v3/chats/{chatId}/read">client.chats.<a href="./src/linq/resources/chats/chats.py">mark_as_read</a>(chat_id) -> None</code>
- <code title="post /v3/chats/{chatId}/voicememo">client.chats.<a href="./src/linq/resources/chats/chats.py">send_voicememo</a>(chat_id, \*\*<a href="src/linq/types/chat_send_voicememo_params.py">params</a>) -> <a href="./src/linq/types/chat_send_voicememo_response.py">ChatSendVoicememoResponse</a></code>
- <code title="post /v3/chats/{chatId}/share_contact_card">client.chats.<a href="./src/linq/resources/chats/chats.py">share_contact_card</a>(chat_id) -> None</code>

## Participants

Types:

```python
from linq.types.chats import ParticipantAddResponse, ParticipantRemoveResponse
```

Methods:

- <code title="post /v3/chats/{chatId}/participants">client.chats.participants.<a href="./src/linq/resources/chats/participants.py">add</a>(chat_id, \*\*<a href="src/linq/types/chats/participant_add_params.py">params</a>) -> <a href="./src/linq/types/chats/participant_add_response.py">ParticipantAddResponse</a></code>
- <code title="delete /v3/chats/{chatId}/participants">client.chats.participants.<a href="./src/linq/resources/chats/participants.py">remove</a>(chat_id, \*\*<a href="src/linq/types/chats/participant_remove_params.py">params</a>) -> <a href="./src/linq/types/chats/participant_remove_response.py">ParticipantRemoveResponse</a></code>

## Typing

Methods:

- <code title="post /v3/chats/{chatId}/typing">client.chats.typing.<a href="./src/linq/resources/chats/typing.py">start</a>(chat_id) -> None</code>
- <code title="delete /v3/chats/{chatId}/typing">client.chats.typing.<a href="./src/linq/resources/chats/typing.py">stop</a>(chat_id) -> None</code>

## Messages

Types:

```python
from linq.types.chats import SentMessage, MessageSendResponse
```

Methods:

- <code title="get /v3/chats/{chatId}/messages">client.chats.messages.<a href="./src/linq/resources/chats/messages.py">list</a>(chat_id, \*\*<a href="src/linq/types/chats/message_list_params.py">params</a>) -> <a href="./src/linq/types/message.py">SyncListMessagesPagination[Message]</a></code>
- <code title="post /v3/chats/{chatId}/messages">client.chats.messages.<a href="./src/linq/resources/chats/messages.py">send</a>(chat_id, \*\*<a href="src/linq/types/chats/message_send_params.py">params</a>) -> <a href="./src/linq/types/chats/message_send_response.py">MessageSendResponse</a></code>

# Messages

Types:

```python
from linq.types import Message, MessageEffect, ReplyTo, MessageAddReactionResponse
```

Methods:

- <code title="get /v3/messages/{messageId}">client.messages.<a href="./src/linq/resources/messages.py">retrieve</a>(message_id) -> <a href="./src/linq/types/message.py">Message</a></code>
- <code title="patch /v3/messages/{messageId}">client.messages.<a href="./src/linq/resources/messages.py">update</a>(message_id, \*\*<a href="src/linq/types/message_update_params.py">params</a>) -> <a href="./src/linq/types/message.py">Message</a></code>
- <code title="delete /v3/messages/{messageId}">client.messages.<a href="./src/linq/resources/messages.py">delete</a>(message_id) -> None</code>
- <code title="post /v3/messages/{messageId}/reactions">client.messages.<a href="./src/linq/resources/messages.py">add_reaction</a>(message_id, \*\*<a href="src/linq/types/message_add_reaction_params.py">params</a>) -> <a href="./src/linq/types/message_add_reaction_response.py">MessageAddReactionResponse</a></code>
- <code title="get /v3/messages/{messageId}/thread">client.messages.<a href="./src/linq/resources/messages.py">list_messages_thread</a>(message_id, \*\*<a href="src/linq/types/message_list_messages_thread_params.py">params</a>) -> <a href="./src/linq/types/message.py">SyncListMessagesPagination[Message]</a></code>

# Attachments

Types:

```python
from linq.types import SupportedContentType, AttachmentCreateResponse, AttachmentRetrieveResponse
```

Methods:

- <code title="post /v3/attachments">client.attachments.<a href="./src/linq/resources/attachments.py">create</a>(\*\*<a href="src/linq/types/attachment_create_params.py">params</a>) -> <a href="./src/linq/types/attachment_create_response.py">AttachmentCreateResponse</a></code>
- <code title="get /v3/attachments/{attachmentId}">client.attachments.<a href="./src/linq/resources/attachments.py">retrieve</a>(attachment_id) -> <a href="./src/linq/types/attachment_retrieve_response.py">AttachmentRetrieveResponse</a></code>

# Phonenumbers

Types:

```python
from linq.types import PhonenumberListResponse
```

Methods:

- <code title="get /v3/phonenumbers">client.phonenumbers.<a href="./src/linq/resources/phonenumbers.py">list</a>() -> <a href="./src/linq/types/phonenumber_list_response.py">PhonenumberListResponse</a></code>

# PhoneNumbers

Types:

```python
from linq.types import PhoneNumberListResponse
```

Methods:

- <code title="get /v3/phone_numbers">client.phone_numbers.<a href="./src/linq/resources/phone_numbers.py">list</a>() -> <a href="./src/linq/types/phone_number_list_response.py">PhoneNumberListResponse</a></code>

# WebhookEvents

Types:

```python
from linq.types import WebhookEventType, WebhookEventListResponse
```

Methods:

- <code title="get /v3/webhook-events">client.webhook_events.<a href="./src/linq/resources/webhook_events.py">list</a>() -> <a href="./src/linq/types/webhook_event_list_response.py">WebhookEventListResponse</a></code>

# WebhookSubscriptions

Types:

```python
from linq.types import (
    WebhookSubscription,
    WebhookSubscriptionCreateResponse,
    WebhookSubscriptionListResponse,
)
```

Methods:

- <code title="post /v3/webhook-subscriptions">client.webhook_subscriptions.<a href="./src/linq/resources/webhook_subscriptions.py">create</a>(\*\*<a href="src/linq/types/webhook_subscription_create_params.py">params</a>) -> <a href="./src/linq/types/webhook_subscription_create_response.py">WebhookSubscriptionCreateResponse</a></code>
- <code title="get /v3/webhook-subscriptions/{subscriptionId}">client.webhook_subscriptions.<a href="./src/linq/resources/webhook_subscriptions.py">retrieve</a>(subscription_id) -> <a href="./src/linq/types/webhook_subscription.py">WebhookSubscription</a></code>
- <code title="put /v3/webhook-subscriptions/{subscriptionId}">client.webhook_subscriptions.<a href="./src/linq/resources/webhook_subscriptions.py">update</a>(subscription_id, \*\*<a href="src/linq/types/webhook_subscription_update_params.py">params</a>) -> <a href="./src/linq/types/webhook_subscription.py">WebhookSubscription</a></code>
- <code title="get /v3/webhook-subscriptions">client.webhook_subscriptions.<a href="./src/linq/resources/webhook_subscriptions.py">list</a>() -> <a href="./src/linq/types/webhook_subscription_list_response.py">WebhookSubscriptionListResponse</a></code>
- <code title="delete /v3/webhook-subscriptions/{subscriptionId}">client.webhook_subscriptions.<a href="./src/linq/resources/webhook_subscriptions.py">delete</a>(subscription_id) -> None</code>

# Capability

Types:

```python
from linq.types import HandleCheck, HandleCheckResponse
```

Methods:

- <code title="post /v3/capability/check_imessage">client.capability.<a href="./src/linq/resources/capability.py">check_i_message</a>(\*\*<a href="src/linq/types/capability_check_i_message_params.py">params</a>) -> <a href="./src/linq/types/handle_check_response.py">HandleCheckResponse</a></code>
- <code title="post /v3/capability/check_rcs">client.capability.<a href="./src/linq/resources/capability.py">check_RCS</a>(\*\*<a href="src/linq/types/capability_check_RCS_params.py">params</a>) -> <a href="./src/linq/types/handle_check_response.py">HandleCheckResponse</a></code>

# Webhooks

Types:

```python
from linq.types import (
    MessageEventV2,
    MessagePayload,
    ReactionEventBase,
    SchemasMediaPartResponse,
    SchemasMessageEffect,
    SchemasTextPartResponse,
    MessageSentWebhookEvent,
    MessageReceivedWebhookEvent,
    MessageReadWebhookEvent,
    MessageDeliveredWebhookEvent,
    MessageFailedWebhookEvent,
    MessageEditedWebhookEvent,
    ReactionAddedWebhookEvent,
    ReactionRemovedWebhookEvent,
    ParticipantAddedWebhookEvent,
    ParticipantRemovedWebhookEvent,
    ChatCreatedWebhookEvent,
    ChatGroupNameUpdatedWebhookEvent,
    ChatGroupIconUpdatedWebhookEvent,
    ChatGroupNameUpdateFailedWebhookEvent,
    ChatGroupIconUpdateFailedWebhookEvent,
    ChatTypingIndicatorStartedWebhookEvent,
    ChatTypingIndicatorStoppedWebhookEvent,
    PhoneNumberStatusUpdatedWebhookEvent,
    EventsWebhookEvent,
)
```

# ContactCard

Types:

```python
from linq.types import SetContactCard, ContactCardRetrieveResponse
```

Methods:

- <code title="post /v3/contact_card">client.contact_card.<a href="./src/linq/resources/contact_card.py">create</a>(\*\*<a href="src/linq/types/contact_card_create_params.py">params</a>) -> <a href="./src/linq/types/set_contact_card.py">SetContactCard</a></code>
- <code title="get /v3/contact_card">client.contact_card.<a href="./src/linq/resources/contact_card.py">retrieve</a>(\*\*<a href="src/linq/types/contact_card_retrieve_params.py">params</a>) -> <a href="./src/linq/types/contact_card_retrieve_response.py">ContactCardRetrieveResponse</a></code>
- <code title="patch /v3/contact_card">client.contact_card.<a href="./src/linq/resources/contact_card.py">update</a>(\*\*<a href="src/linq/types/contact_card_update_params.py">params</a>) -> <a href="./src/linq/types/set_contact_card.py">SetContactCard</a></code>
