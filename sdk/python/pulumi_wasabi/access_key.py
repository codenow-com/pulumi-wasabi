# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AccessKeyArgs', 'AccessKey']

@pulumi.input_type
class AccessKeyArgs:
    def __init__(__self__, *,
                 user: pulumi.Input[str],
                 pgp_key: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AccessKey resource.
        """
        pulumi.set(__self__, "user", user)
        if pgp_key is not None:
            pulumi.set(__self__, "pgp_key", pgp_key)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def user(self) -> pulumi.Input[str]:
        return pulumi.get(self, "user")

    @user.setter
    def user(self, value: pulumi.Input[str]):
        pulumi.set(self, "user", value)

    @property
    @pulumi.getter(name="pgpKey")
    def pgp_key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "pgp_key")

    @pgp_key.setter
    def pgp_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pgp_key", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


@pulumi.input_type
class _AccessKeyState:
    def __init__(__self__, *,
                 encrypted_secret: Optional[pulumi.Input[str]] = None,
                 key_fingerprint: Optional[pulumi.Input[str]] = None,
                 pgp_key: Optional[pulumi.Input[str]] = None,
                 secret: Optional[pulumi.Input[str]] = None,
                 ses_smtp_password_v4: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AccessKey resources.
        """
        if encrypted_secret is not None:
            pulumi.set(__self__, "encrypted_secret", encrypted_secret)
        if key_fingerprint is not None:
            pulumi.set(__self__, "key_fingerprint", key_fingerprint)
        if pgp_key is not None:
            pulumi.set(__self__, "pgp_key", pgp_key)
        if secret is not None:
            pulumi.set(__self__, "secret", secret)
        if ses_smtp_password_v4 is not None:
            pulumi.set(__self__, "ses_smtp_password_v4", ses_smtp_password_v4)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if user is not None:
            pulumi.set(__self__, "user", user)

    @property
    @pulumi.getter(name="encryptedSecret")
    def encrypted_secret(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "encrypted_secret")

    @encrypted_secret.setter
    def encrypted_secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encrypted_secret", value)

    @property
    @pulumi.getter(name="keyFingerprint")
    def key_fingerprint(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "key_fingerprint")

    @key_fingerprint.setter
    def key_fingerprint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_fingerprint", value)

    @property
    @pulumi.getter(name="pgpKey")
    def pgp_key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "pgp_key")

    @pgp_key.setter
    def pgp_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pgp_key", value)

    @property
    @pulumi.getter
    def secret(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "secret")

    @secret.setter
    def secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret", value)

    @property
    @pulumi.getter(name="sesSmtpPasswordV4")
    def ses_smtp_password_v4(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ses_smtp_password_v4")

    @ses_smtp_password_v4.setter
    def ses_smtp_password_v4(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ses_smtp_password_v4", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "user")

    @user.setter
    def user(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user", value)


class AccessKey(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 pgp_key: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a AccessKey resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccessKeyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a AccessKey resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param AccessKeyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccessKeyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 pgp_key: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AccessKeyArgs.__new__(AccessKeyArgs)

            __props__.__dict__["pgp_key"] = pgp_key
            __props__.__dict__["status"] = status
            if user is None and not opts.urn:
                raise TypeError("Missing required property 'user'")
            __props__.__dict__["user"] = user
            __props__.__dict__["encrypted_secret"] = None
            __props__.__dict__["key_fingerprint"] = None
            __props__.__dict__["secret"] = None
            __props__.__dict__["ses_smtp_password_v4"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["secret", "sesSmtpPasswordV4"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(AccessKey, __self__).__init__(
            'wasabi:index/accessKey:AccessKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            encrypted_secret: Optional[pulumi.Input[str]] = None,
            key_fingerprint: Optional[pulumi.Input[str]] = None,
            pgp_key: Optional[pulumi.Input[str]] = None,
            secret: Optional[pulumi.Input[str]] = None,
            ses_smtp_password_v4: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            user: Optional[pulumi.Input[str]] = None) -> 'AccessKey':
        """
        Get an existing AccessKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AccessKeyState.__new__(_AccessKeyState)

        __props__.__dict__["encrypted_secret"] = encrypted_secret
        __props__.__dict__["key_fingerprint"] = key_fingerprint
        __props__.__dict__["pgp_key"] = pgp_key
        __props__.__dict__["secret"] = secret
        __props__.__dict__["ses_smtp_password_v4"] = ses_smtp_password_v4
        __props__.__dict__["status"] = status
        __props__.__dict__["user"] = user
        return AccessKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="encryptedSecret")
    def encrypted_secret(self) -> pulumi.Output[str]:
        return pulumi.get(self, "encrypted_secret")

    @property
    @pulumi.getter(name="keyFingerprint")
    def key_fingerprint(self) -> pulumi.Output[str]:
        return pulumi.get(self, "key_fingerprint")

    @property
    @pulumi.getter(name="pgpKey")
    def pgp_key(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "pgp_key")

    @property
    @pulumi.getter
    def secret(self) -> pulumi.Output[str]:
        return pulumi.get(self, "secret")

    @property
    @pulumi.getter(name="sesSmtpPasswordV4")
    def ses_smtp_password_v4(self) -> pulumi.Output[str]:
        return pulumi.get(self, "ses_smtp_password_v4")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def user(self) -> pulumi.Output[str]:
        return pulumi.get(self, "user")

