# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetRoleResult',
    'AwaitableGetRoleResult',
    'get_role',
    'get_role_output',
]

@pulumi.output_type
class GetRoleResult:
    """
    A collection of values returned by getRole.
    """
    def __init__(__self__, arn=None, assume_role_policy=None, create_date=None, description=None, id=None, max_session_duration=None, name=None, path=None, permissions_boundary=None, unique_id=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if assume_role_policy and not isinstance(assume_role_policy, str):
            raise TypeError("Expected argument 'assume_role_policy' to be a str")
        pulumi.set(__self__, "assume_role_policy", assume_role_policy)
        if create_date and not isinstance(create_date, str):
            raise TypeError("Expected argument 'create_date' to be a str")
        pulumi.set(__self__, "create_date", create_date)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if max_session_duration and not isinstance(max_session_duration, int):
            raise TypeError("Expected argument 'max_session_duration' to be a int")
        pulumi.set(__self__, "max_session_duration", max_session_duration)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if path and not isinstance(path, str):
            raise TypeError("Expected argument 'path' to be a str")
        pulumi.set(__self__, "path", path)
        if permissions_boundary and not isinstance(permissions_boundary, str):
            raise TypeError("Expected argument 'permissions_boundary' to be a str")
        pulumi.set(__self__, "permissions_boundary", permissions_boundary)
        if unique_id and not isinstance(unique_id, str):
            raise TypeError("Expected argument 'unique_id' to be a str")
        pulumi.set(__self__, "unique_id", unique_id)

    @property
    @pulumi.getter
    def arn(self) -> str:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="assumeRolePolicy")
    def assume_role_policy(self) -> str:
        return pulumi.get(self, "assume_role_policy")

    @property
    @pulumi.getter(name="createDate")
    def create_date(self) -> str:
        return pulumi.get(self, "create_date")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="maxSessionDuration")
    def max_session_duration(self) -> int:
        return pulumi.get(self, "max_session_duration")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def path(self) -> str:
        return pulumi.get(self, "path")

    @property
    @pulumi.getter(name="permissionsBoundary")
    def permissions_boundary(self) -> str:
        return pulumi.get(self, "permissions_boundary")

    @property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> str:
        return pulumi.get(self, "unique_id")


class AwaitableGetRoleResult(GetRoleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRoleResult(
            arn=self.arn,
            assume_role_policy=self.assume_role_policy,
            create_date=self.create_date,
            description=self.description,
            id=self.id,
            max_session_duration=self.max_session_duration,
            name=self.name,
            path=self.path,
            permissions_boundary=self.permissions_boundary,
            unique_id=self.unique_id)


def get_role(name: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRoleResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('wasabi:index/getRole:getRole', __args__, opts=opts, typ=GetRoleResult).value

    return AwaitableGetRoleResult(
        arn=pulumi.get(__ret__, 'arn'),
        assume_role_policy=pulumi.get(__ret__, 'assume_role_policy'),
        create_date=pulumi.get(__ret__, 'create_date'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        max_session_duration=pulumi.get(__ret__, 'max_session_duration'),
        name=pulumi.get(__ret__, 'name'),
        path=pulumi.get(__ret__, 'path'),
        permissions_boundary=pulumi.get(__ret__, 'permissions_boundary'),
        unique_id=pulumi.get(__ret__, 'unique_id'))


@_utilities.lift_output_func(get_role)
def get_role_output(name: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRoleResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
