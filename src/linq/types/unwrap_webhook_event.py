# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .poll_read_webhook_event import PollReadWebhookEvent
from .poll_sent_webhook_event import PollSentWebhookEvent
from .poll_failed_webhook_event import PollFailedWebhookEvent
from .chat_created_webhook_event import ChatCreatedWebhookEvent
from .message_read_webhook_event import MessageReadWebhookEvent
from .message_sent_webhook_event import MessageSentWebhookEvent
from .poll_updated_webhook_event import PollUpdatedWebhookEvent
from .poll_received_webhook_event import PollReceivedWebhookEvent
from .message_edited_webhook_event import MessageEditedWebhookEvent
from .message_failed_webhook_event import MessageFailedWebhookEvent
from .poll_delivered_webhook_event import PollDeliveredWebhookEvent
from .reaction_added_webhook_event import ReactionAddedWebhookEvent
from .payment_expired_webhook_event import PaymentExpiredWebhookEvent
from .poll_vote_added_webhook_event import PollVoteAddedWebhookEvent
from .message_received_webhook_event import MessageReceivedWebhookEvent
from .payment_canceled_webhook_event import PaymentCanceledWebhookEvent
from .payment_declined_webhook_event import PaymentDeclinedWebhookEvent
from .reaction_removed_webhook_event import ReactionRemovedWebhookEvent
from .message_delivered_webhook_event import MessageDeliveredWebhookEvent
from .participant_added_webhook_event import ParticipantAddedWebhookEvent
from .payment_succeeded_webhook_event import PaymentSucceededWebhookEvent
from .poll_vote_removed_webhook_event import PollVoteRemovedWebhookEvent
from .connection_created_webhook_event import ConnectionCreatedWebhookEvent
from .connection_revoked_webhook_event import ConnectionRevokedWebhookEvent
from .payment_authorized_webhook_event import PaymentAuthorizedWebhookEvent
from .participant_removed_webhook_event import ParticipantRemovedWebhookEvent
from .poll_reaction_added_webhook_event import PollReactionAddedWebhookEvent
from .contact_card_received_webhook_event import ContactCardReceivedWebhookEvent
from .chat_background_updated_webhook_event import ChatBackgroundUpdatedWebhookEvent
from .chat_group_icon_updated_webhook_event import ChatGroupIconUpdatedWebhookEvent
from .chat_group_name_updated_webhook_event import ChatGroupNameUpdatedWebhookEvent
from .location_sharing_started_webhook_event import LocationSharingStartedWebhookEvent
from .location_sharing_stopped_webhook_event import LocationSharingStoppedWebhookEvent
from .phone_number_status_updated_webhook_event import PhoneNumberStatusUpdatedWebhookEvent
from .chat_background_update_failed_webhook_event import ChatBackgroundUpdateFailedWebhookEvent
from .chat_group_icon_update_failed_webhook_event import ChatGroupIconUpdateFailedWebhookEvent
from .chat_group_name_update_failed_webhook_event import ChatGroupNameUpdateFailedWebhookEvent
from .chat_typing_indicator_started_webhook_event import ChatTypingIndicatorStartedWebhookEvent
from .chat_typing_indicator_stopped_webhook_event import ChatTypingIndicatorStoppedWebhookEvent

__all__ = ["UnwrapWebhookEvent"]

UnwrapWebhookEvent: TypeAlias = Annotated[
    Union[
        MessageSentWebhookEvent,
        MessageReceivedWebhookEvent,
        MessageReadWebhookEvent,
        MessageDeliveredWebhookEvent,
        MessageFailedWebhookEvent,
        MessageEditedWebhookEvent,
        ReactionAddedWebhookEvent,
        ReactionRemovedWebhookEvent,
        PollReceivedWebhookEvent,
        PollSentWebhookEvent,
        PollDeliveredWebhookEvent,
        PollReadWebhookEvent,
        PollUpdatedWebhookEvent,
        PollFailedWebhookEvent,
        PollVoteAddedWebhookEvent,
        PollVoteRemovedWebhookEvent,
        PollReactionAddedWebhookEvent,
        ParticipantAddedWebhookEvent,
        ParticipantRemovedWebhookEvent,
        ChatCreatedWebhookEvent,
        ChatGroupNameUpdatedWebhookEvent,
        ChatGroupIconUpdatedWebhookEvent,
        ChatGroupNameUpdateFailedWebhookEvent,
        ChatGroupIconUpdateFailedWebhookEvent,
        ChatTypingIndicatorStartedWebhookEvent,
        ChatTypingIndicatorStoppedWebhookEvent,
        ChatBackgroundUpdatedWebhookEvent,
        ChatBackgroundUpdateFailedWebhookEvent,
        ContactCardReceivedWebhookEvent,
        PhoneNumberStatusUpdatedWebhookEvent,
        ConnectionCreatedWebhookEvent,
        ConnectionRevokedWebhookEvent,
        LocationSharingStartedWebhookEvent,
        LocationSharingStoppedWebhookEvent,
        PaymentAuthorizedWebhookEvent,
        PaymentCanceledWebhookEvent,
        PaymentDeclinedWebhookEvent,
        PaymentExpiredWebhookEvent,
        PaymentSucceededWebhookEvent,
    ],
    PropertyInfo(discriminator="event_type"),
]
