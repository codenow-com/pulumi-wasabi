# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AccountPasswordPolicyArgs', 'AccountPasswordPolicy']

@pulumi.input_type
class AccountPasswordPolicyArgs:
    def __init__(__self__, *,
                 allow_users_to_change_password: Optional[pulumi.Input[bool]] = None,
                 hard_expiry: Optional[pulumi.Input[bool]] = None,
                 max_password_age: Optional[pulumi.Input[int]] = None,
                 minimum_password_length: Optional[pulumi.Input[int]] = None,
                 password_reuse_prevention: Optional[pulumi.Input[int]] = None,
                 require_lowercase_characters: Optional[pulumi.Input[bool]] = None,
                 require_numbers: Optional[pulumi.Input[bool]] = None,
                 require_symbols: Optional[pulumi.Input[bool]] = None,
                 require_uppercase_characters: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a AccountPasswordPolicy resource.
        """
        if allow_users_to_change_password is not None:
            pulumi.set(__self__, "allow_users_to_change_password", allow_users_to_change_password)
        if hard_expiry is not None:
            pulumi.set(__self__, "hard_expiry", hard_expiry)
        if max_password_age is not None:
            pulumi.set(__self__, "max_password_age", max_password_age)
        if minimum_password_length is not None:
            pulumi.set(__self__, "minimum_password_length", minimum_password_length)
        if password_reuse_prevention is not None:
            pulumi.set(__self__, "password_reuse_prevention", password_reuse_prevention)
        if require_lowercase_characters is not None:
            pulumi.set(__self__, "require_lowercase_characters", require_lowercase_characters)
        if require_numbers is not None:
            pulumi.set(__self__, "require_numbers", require_numbers)
        if require_symbols is not None:
            pulumi.set(__self__, "require_symbols", require_symbols)
        if require_uppercase_characters is not None:
            pulumi.set(__self__, "require_uppercase_characters", require_uppercase_characters)

    @property
    @pulumi.getter(name="allowUsersToChangePassword")
    def allow_users_to_change_password(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "allow_users_to_change_password")

    @allow_users_to_change_password.setter
    def allow_users_to_change_password(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_users_to_change_password", value)

    @property
    @pulumi.getter(name="hardExpiry")
    def hard_expiry(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "hard_expiry")

    @hard_expiry.setter
    def hard_expiry(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "hard_expiry", value)

    @property
    @pulumi.getter(name="maxPasswordAge")
    def max_password_age(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "max_password_age")

    @max_password_age.setter
    def max_password_age(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_password_age", value)

    @property
    @pulumi.getter(name="minimumPasswordLength")
    def minimum_password_length(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "minimum_password_length")

    @minimum_password_length.setter
    def minimum_password_length(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "minimum_password_length", value)

    @property
    @pulumi.getter(name="passwordReusePrevention")
    def password_reuse_prevention(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "password_reuse_prevention")

    @password_reuse_prevention.setter
    def password_reuse_prevention(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "password_reuse_prevention", value)

    @property
    @pulumi.getter(name="requireLowercaseCharacters")
    def require_lowercase_characters(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "require_lowercase_characters")

    @require_lowercase_characters.setter
    def require_lowercase_characters(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "require_lowercase_characters", value)

    @property
    @pulumi.getter(name="requireNumbers")
    def require_numbers(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "require_numbers")

    @require_numbers.setter
    def require_numbers(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "require_numbers", value)

    @property
    @pulumi.getter(name="requireSymbols")
    def require_symbols(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "require_symbols")

    @require_symbols.setter
    def require_symbols(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "require_symbols", value)

    @property
    @pulumi.getter(name="requireUppercaseCharacters")
    def require_uppercase_characters(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "require_uppercase_characters")

    @require_uppercase_characters.setter
    def require_uppercase_characters(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "require_uppercase_characters", value)


@pulumi.input_type
class _AccountPasswordPolicyState:
    def __init__(__self__, *,
                 allow_users_to_change_password: Optional[pulumi.Input[bool]] = None,
                 expire_passwords: Optional[pulumi.Input[bool]] = None,
                 hard_expiry: Optional[pulumi.Input[bool]] = None,
                 max_password_age: Optional[pulumi.Input[int]] = None,
                 minimum_password_length: Optional[pulumi.Input[int]] = None,
                 password_reuse_prevention: Optional[pulumi.Input[int]] = None,
                 require_lowercase_characters: Optional[pulumi.Input[bool]] = None,
                 require_numbers: Optional[pulumi.Input[bool]] = None,
                 require_symbols: Optional[pulumi.Input[bool]] = None,
                 require_uppercase_characters: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering AccountPasswordPolicy resources.
        """
        if allow_users_to_change_password is not None:
            pulumi.set(__self__, "allow_users_to_change_password", allow_users_to_change_password)
        if expire_passwords is not None:
            pulumi.set(__self__, "expire_passwords", expire_passwords)
        if hard_expiry is not None:
            pulumi.set(__self__, "hard_expiry", hard_expiry)
        if max_password_age is not None:
            pulumi.set(__self__, "max_password_age", max_password_age)
        if minimum_password_length is not None:
            pulumi.set(__self__, "minimum_password_length", minimum_password_length)
        if password_reuse_prevention is not None:
            pulumi.set(__self__, "password_reuse_prevention", password_reuse_prevention)
        if require_lowercase_characters is not None:
            pulumi.set(__self__, "require_lowercase_characters", require_lowercase_characters)
        if require_numbers is not None:
            pulumi.set(__self__, "require_numbers", require_numbers)
        if require_symbols is not None:
            pulumi.set(__self__, "require_symbols", require_symbols)
        if require_uppercase_characters is not None:
            pulumi.set(__self__, "require_uppercase_characters", require_uppercase_characters)

    @property
    @pulumi.getter(name="allowUsersToChangePassword")
    def allow_users_to_change_password(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "allow_users_to_change_password")

    @allow_users_to_change_password.setter
    def allow_users_to_change_password(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_users_to_change_password", value)

    @property
    @pulumi.getter(name="expirePasswords")
    def expire_passwords(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "expire_passwords")

    @expire_passwords.setter
    def expire_passwords(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "expire_passwords", value)

    @property
    @pulumi.getter(name="hardExpiry")
    def hard_expiry(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "hard_expiry")

    @hard_expiry.setter
    def hard_expiry(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "hard_expiry", value)

    @property
    @pulumi.getter(name="maxPasswordAge")
    def max_password_age(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "max_password_age")

    @max_password_age.setter
    def max_password_age(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_password_age", value)

    @property
    @pulumi.getter(name="minimumPasswordLength")
    def minimum_password_length(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "minimum_password_length")

    @minimum_password_length.setter
    def minimum_password_length(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "minimum_password_length", value)

    @property
    @pulumi.getter(name="passwordReusePrevention")
    def password_reuse_prevention(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "password_reuse_prevention")

    @password_reuse_prevention.setter
    def password_reuse_prevention(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "password_reuse_prevention", value)

    @property
    @pulumi.getter(name="requireLowercaseCharacters")
    def require_lowercase_characters(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "require_lowercase_characters")

    @require_lowercase_characters.setter
    def require_lowercase_characters(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "require_lowercase_characters", value)

    @property
    @pulumi.getter(name="requireNumbers")
    def require_numbers(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "require_numbers")

    @require_numbers.setter
    def require_numbers(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "require_numbers", value)

    @property
    @pulumi.getter(name="requireSymbols")
    def require_symbols(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "require_symbols")

    @require_symbols.setter
    def require_symbols(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "require_symbols", value)

    @property
    @pulumi.getter(name="requireUppercaseCharacters")
    def require_uppercase_characters(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "require_uppercase_characters")

    @require_uppercase_characters.setter
    def require_uppercase_characters(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "require_uppercase_characters", value)


class AccountPasswordPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_users_to_change_password: Optional[pulumi.Input[bool]] = None,
                 hard_expiry: Optional[pulumi.Input[bool]] = None,
                 max_password_age: Optional[pulumi.Input[int]] = None,
                 minimum_password_length: Optional[pulumi.Input[int]] = None,
                 password_reuse_prevention: Optional[pulumi.Input[int]] = None,
                 require_lowercase_characters: Optional[pulumi.Input[bool]] = None,
                 require_numbers: Optional[pulumi.Input[bool]] = None,
                 require_symbols: Optional[pulumi.Input[bool]] = None,
                 require_uppercase_characters: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Create a AccountPasswordPolicy resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[AccountPasswordPolicyArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a AccountPasswordPolicy resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param AccountPasswordPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccountPasswordPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_users_to_change_password: Optional[pulumi.Input[bool]] = None,
                 hard_expiry: Optional[pulumi.Input[bool]] = None,
                 max_password_age: Optional[pulumi.Input[int]] = None,
                 minimum_password_length: Optional[pulumi.Input[int]] = None,
                 password_reuse_prevention: Optional[pulumi.Input[int]] = None,
                 require_lowercase_characters: Optional[pulumi.Input[bool]] = None,
                 require_numbers: Optional[pulumi.Input[bool]] = None,
                 require_symbols: Optional[pulumi.Input[bool]] = None,
                 require_uppercase_characters: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AccountPasswordPolicyArgs.__new__(AccountPasswordPolicyArgs)

            __props__.__dict__["allow_users_to_change_password"] = allow_users_to_change_password
            __props__.__dict__["hard_expiry"] = hard_expiry
            __props__.__dict__["max_password_age"] = max_password_age
            __props__.__dict__["minimum_password_length"] = minimum_password_length
            __props__.__dict__["password_reuse_prevention"] = password_reuse_prevention
            __props__.__dict__["require_lowercase_characters"] = require_lowercase_characters
            __props__.__dict__["require_numbers"] = require_numbers
            __props__.__dict__["require_symbols"] = require_symbols
            __props__.__dict__["require_uppercase_characters"] = require_uppercase_characters
            __props__.__dict__["expire_passwords"] = None
        super(AccountPasswordPolicy, __self__).__init__(
            'wasabi:index/accountPasswordPolicy:AccountPasswordPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            allow_users_to_change_password: Optional[pulumi.Input[bool]] = None,
            expire_passwords: Optional[pulumi.Input[bool]] = None,
            hard_expiry: Optional[pulumi.Input[bool]] = None,
            max_password_age: Optional[pulumi.Input[int]] = None,
            minimum_password_length: Optional[pulumi.Input[int]] = None,
            password_reuse_prevention: Optional[pulumi.Input[int]] = None,
            require_lowercase_characters: Optional[pulumi.Input[bool]] = None,
            require_numbers: Optional[pulumi.Input[bool]] = None,
            require_symbols: Optional[pulumi.Input[bool]] = None,
            require_uppercase_characters: Optional[pulumi.Input[bool]] = None) -> 'AccountPasswordPolicy':
        """
        Get an existing AccountPasswordPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AccountPasswordPolicyState.__new__(_AccountPasswordPolicyState)

        __props__.__dict__["allow_users_to_change_password"] = allow_users_to_change_password
        __props__.__dict__["expire_passwords"] = expire_passwords
        __props__.__dict__["hard_expiry"] = hard_expiry
        __props__.__dict__["max_password_age"] = max_password_age
        __props__.__dict__["minimum_password_length"] = minimum_password_length
        __props__.__dict__["password_reuse_prevention"] = password_reuse_prevention
        __props__.__dict__["require_lowercase_characters"] = require_lowercase_characters
        __props__.__dict__["require_numbers"] = require_numbers
        __props__.__dict__["require_symbols"] = require_symbols
        __props__.__dict__["require_uppercase_characters"] = require_uppercase_characters
        return AccountPasswordPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowUsersToChangePassword")
    def allow_users_to_change_password(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "allow_users_to_change_password")

    @property
    @pulumi.getter(name="expirePasswords")
    def expire_passwords(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "expire_passwords")

    @property
    @pulumi.getter(name="hardExpiry")
    def hard_expiry(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "hard_expiry")

    @property
    @pulumi.getter(name="maxPasswordAge")
    def max_password_age(self) -> pulumi.Output[int]:
        return pulumi.get(self, "max_password_age")

    @property
    @pulumi.getter(name="minimumPasswordLength")
    def minimum_password_length(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "minimum_password_length")

    @property
    @pulumi.getter(name="passwordReusePrevention")
    def password_reuse_prevention(self) -> pulumi.Output[int]:
        return pulumi.get(self, "password_reuse_prevention")

    @property
    @pulumi.getter(name="requireLowercaseCharacters")
    def require_lowercase_characters(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "require_lowercase_characters")

    @property
    @pulumi.getter(name="requireNumbers")
    def require_numbers(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "require_numbers")

    @property
    @pulumi.getter(name="requireSymbols")
    def require_symbols(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "require_symbols")

    @property
    @pulumi.getter(name="requireUppercaseCharacters")
    def require_uppercase_characters(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "require_uppercase_characters")

