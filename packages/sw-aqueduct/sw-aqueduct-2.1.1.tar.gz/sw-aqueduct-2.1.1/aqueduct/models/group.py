# -*- coding: utf-8 -*-
from typing import AnyStr, List

from attr import define, field

# Copyright: (c) 2022, Swimlane <info@swimlane.com>
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)
from .base import CreatedByUser


@define
class Group:
    """A Swimlane Group object model"""

    disabled: bool = field()
    id: AnyStr = field()
    name: AnyStr = field()
    description: AnyStr = field(default="")
    createdByUser: CreatedByUser = field(default={})
    createdDate: AnyStr = field(default="")
    modifiedByUser: CreatedByUser = field(default={})
    modifiedDate: AnyStr = field(default="")
    permissions: dict = field(default={})
    roles: List = field(default=[])
    users: List = field(default=[])
    groups: List = field(default=[])

    def __init__(self, **kwargs):
        from ..base import Base
        from ..utils.exceptions import ModelError

        Base().scrub(kwargs)
        try:
            self.__attrs_init__(**kwargs)
        except TypeError as te:
            raise ModelError(err=te, name="Group")

    def __attrs_post_init__(self):
        from ..utils.exceptions import ModelError

        if self.users:
            from .user import UserLight

            user_list = []
            for user in self.users:
                try:
                    user_list.append(UserLight(**user))
                except TypeError as e:
                    raise ModelError(err=e, name="UserLight")
            self.users = user_list
        if self.groups:
            group_list = []
            for group in self.groups:
                try:
                    group_list.append(Group(**group))
                except TypeError as e:
                    raise ModelError(err=e, name="Group")
            self.groups = group_list
        if self.roles:
            from .role import Role

            role_list = []
            for role in self.roles:
                try:
                    role_list.append(Role(**role))
                except TypeError as e:
                    raise ModelError(err=e, name="Role")
            self.roles = role_list
