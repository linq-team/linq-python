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
from .api_token_created_webhook_event import APITokenCreatedWebhookEvent
from .api_token_deleted_webhook_event import APITokenDeletedWebhookEvent
from .api_token_expired_webhook_event import APITokenExpiredWebhookEvent
from .api_token_renamed_webhook_event import APITokenRenamedWebhookEvent
from .message_delivered_webhook_event import MessageDeliveredWebhookEvent
from .participant_added_webhook_event import ParticipantAddedWebhookEvent
from .payment_succeeded_webhook_event import PaymentSucceededWebhookEvent
from .poll_vote_removed_webhook_event import PollVoteRemovedWebhookEvent
from .team_member_added_webhook_event import TeamMemberAddedWebhookEvent
from .connection_created_webhook_event import ConnectionCreatedWebhookEvent
from .connection_revoked_webhook_event import ConnectionRevokedWebhookEvent
from .payment_authorized_webhook_event import PaymentAuthorizedWebhookEvent
from .api_token_activated_webhook_event import APITokenActivatedWebhookEvent
from .environment_created_webhook_event import EnvironmentCreatedWebhookEvent
from .environment_deleted_webhook_event import EnvironmentDeletedWebhookEvent
from .environment_renamed_webhook_event import EnvironmentRenamedWebhookEvent
from .participant_removed_webhook_event import ParticipantRemovedWebhookEvent
from .poll_reaction_added_webhook_event import PollReactionAddedWebhookEvent
from .contact_card_created_webhook_event import ContactCardCreatedWebhookEvent
from .contact_card_deleted_webhook_event import ContactCardDeletedWebhookEvent
from .contact_card_updated_webhook_event import ContactCardUpdatedWebhookEvent
from .contact_card_received_webhook_event import ContactCardReceivedWebhookEvent
from .phone_number_assigned_webhook_event import PhoneNumberAssignedWebhookEvent
from .phone_number_released_webhook_event import PhoneNumberReleasedWebhookEvent
from .team_member_signed_in_webhook_event import TeamMemberSignedInWebhookEvent
from .environment_line_moved_webhook_event import EnvironmentLineMovedWebhookEvent
from .team_member_signed_out_webhook_event import TeamMemberSignedOutWebhookEvent
from .chat_background_updated_webhook_event import ChatBackgroundUpdatedWebhookEvent
from .chat_group_icon_updated_webhook_event import ChatGroupIconUpdatedWebhookEvent
from .chat_group_name_updated_webhook_event import ChatGroupNameUpdatedWebhookEvent
from .location_sharing_started_webhook_event import LocationSharingStartedWebhookEvent
from .location_sharing_stopped_webhook_event import LocationSharingStoppedWebhookEvent
from .api_token_expiry_scheduled_webhook_event import APITokenExpiryScheduledWebhookEvent
from .zero_day_retention_updated_webhook_event import ZeroDayRetentionUpdatedWebhookEvent
from .phone_number_status_updated_webhook_event import PhoneNumberStatusUpdatedWebhookEvent
from .webhook_subscription_created_webhook_event import WebhookSubscriptionCreatedWebhookEvent
from .webhook_subscription_deleted_webhook_event import WebhookSubscriptionDeletedWebhookEvent
from .webhook_subscription_enabled_webhook_event import WebhookSubscriptionEnabledWebhookEvent
from .chat_background_update_failed_webhook_event import ChatBackgroundUpdateFailedWebhookEvent
from .chat_group_icon_update_failed_webhook_event import ChatGroupIconUpdateFailedWebhookEvent
from .chat_group_name_update_failed_webhook_event import ChatGroupNameUpdateFailedWebhookEvent
from .chat_typing_indicator_started_webhook_event import ChatTypingIndicatorStartedWebhookEvent
from .chat_typing_indicator_stopped_webhook_event import ChatTypingIndicatorStoppedWebhookEvent
from .webhook_subscription_disabled_webhook_event import WebhookSubscriptionDisabledWebhookEvent
from .phone_number_forwarding_updated_webhook_event import PhoneNumberForwardingUpdatedWebhookEvent
from .webhook_subscription_events_updated_webhook_event import WebhookSubscriptionEventsUpdatedWebhookEvent
from .webhook_subscription_target_url_changed_webhook_event import WebhookSubscriptionTargetURLChangedWebhookEvent
from .webhook_subscription_routing_headers_set_webhook_event import WebhookSubscriptionRoutingHeadersSetWebhookEvent
from .webhook_subscription_phone_numbers_updated_webhook_event import WebhookSubscriptionPhoneNumbersUpdatedWebhookEvent
from .webhook_subscription_routing_headers_cleared_webhook_event import (
    WebhookSubscriptionRoutingHeadersClearedWebhookEvent,
)

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
        PhoneNumberAssignedWebhookEvent,
        PhoneNumberReleasedWebhookEvent,
        ConnectionCreatedWebhookEvent,
        ConnectionRevokedWebhookEvent,
        LocationSharingStartedWebhookEvent,
        LocationSharingStoppedWebhookEvent,
        PaymentAuthorizedWebhookEvent,
        PaymentCanceledWebhookEvent,
        PaymentDeclinedWebhookEvent,
        PaymentExpiredWebhookEvent,
        PaymentSucceededWebhookEvent,
        ZeroDayRetentionUpdatedWebhookEvent,
        PhoneNumberForwardingUpdatedWebhookEvent,
        EnvironmentLineMovedWebhookEvent,
        ContactCardCreatedWebhookEvent,
        ContactCardUpdatedWebhookEvent,
        ContactCardDeletedWebhookEvent,
        APITokenCreatedWebhookEvent,
        APITokenRenamedWebhookEvent,
        APITokenExpiryScheduledWebhookEvent,
        APITokenExpiredWebhookEvent,
        APITokenActivatedWebhookEvent,
        APITokenDeletedWebhookEvent,
        EnvironmentCreatedWebhookEvent,
        EnvironmentRenamedWebhookEvent,
        EnvironmentDeletedWebhookEvent,
        WebhookSubscriptionCreatedWebhookEvent,
        WebhookSubscriptionDeletedWebhookEvent,
        WebhookSubscriptionTargetURLChangedWebhookEvent,
        WebhookSubscriptionEnabledWebhookEvent,
        WebhookSubscriptionDisabledWebhookEvent,
        WebhookSubscriptionEventsUpdatedWebhookEvent,
        WebhookSubscriptionPhoneNumbersUpdatedWebhookEvent,
        WebhookSubscriptionRoutingHeadersSetWebhookEvent,
        WebhookSubscriptionRoutingHeadersClearedWebhookEvent,
        TeamMemberAddedWebhookEvent,
        TeamMemberSignedInWebhookEvent,
        TeamMemberSignedOutWebhookEvent,
    ],
    PropertyInfo(discriminator="event_type"),
]
