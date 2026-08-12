# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ReputationDriverKey"]

ReputationDriverKey: TypeAlias = Literal[
    "low_engagement",
    "overall_conversation_health",
    "volume_spike",
    "new_conversation_rate",
    "opt_out_handling",
    "flagged",
    "other",
]
