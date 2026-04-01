# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "SyncListChatsPagination",
    "AsyncListChatsPagination",
    "SyncListMessagesPagination",
    "AsyncListMessagesPagination",
]

_T = TypeVar("_T")


class SyncListChatsPagination(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    chats: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        chats = self.chats
        if not chats:
            return []
        return chats

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class AsyncListChatsPagination(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    chats: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        chats = self.chats
        if not chats:
            return []
        return chats

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class SyncListMessagesPagination(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    messages: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        messages = self.messages
        if not messages:
            return []
        return messages

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class AsyncListMessagesPagination(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    messages: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        messages = self.messages
        if not messages:
            return []
        return messages

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})
