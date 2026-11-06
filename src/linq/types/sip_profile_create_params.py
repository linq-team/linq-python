# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SipProfileCreateParams"]


class SipProfileCreateParams(TypedDict, total=False):
    name: Required[str]

    primary_uri: Required[str]
    """Your SIP endpoint as scheme + host, e.g.

    `sips:sip.partner.example`. Must start with `sip:` (UDP) or `sips:` (TLS) — the
    scheme sets the transport. Do not include a user part: we set it to the called
    number on each call (`sip:<called-number>@<your-host>`). A bare host with no
    scheme is rejected.
    """

    backup_uri: str
    """Optional failover SIP URI"""
