# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'BucketCorsRule',
    'BucketGrant',
    'BucketLifecycleRule',
    'BucketLifecycleRuleExpiration',
    'BucketLifecycleRuleNoncurrentVersionExpiration',
    'BucketLifecycleRuleNoncurrentVersionTransition',
    'BucketLifecycleRuleTransition',
    'BucketLogging',
    'BucketVersioning',
    'GetGroupUserResult',
    'GetPolicyDocumentStatementResult',
    'GetPolicyDocumentStatementConditionResult',
    'GetPolicyDocumentStatementNotPrincipalResult',
    'GetPolicyDocumentStatementPrincipalResult',
]

@pulumi.output_type
class BucketCorsRule(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "allowedMethods":
            suggest = "allowed_methods"
        elif key == "allowedOrigins":
            suggest = "allowed_origins"
        elif key == "allowedHeaders":
            suggest = "allowed_headers"
        elif key == "exposeHeaders":
            suggest = "expose_headers"
        elif key == "maxAgeSeconds":
            suggest = "max_age_seconds"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in BucketCorsRule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        BucketCorsRule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        BucketCorsRule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 allowed_methods: Sequence[str],
                 allowed_origins: Sequence[str],
                 allowed_headers: Optional[Sequence[str]] = None,
                 expose_headers: Optional[Sequence[str]] = None,
                 max_age_seconds: Optional[int] = None):
        pulumi.set(__self__, "allowed_methods", allowed_methods)
        pulumi.set(__self__, "allowed_origins", allowed_origins)
        if allowed_headers is not None:
            pulumi.set(__self__, "allowed_headers", allowed_headers)
        if expose_headers is not None:
            pulumi.set(__self__, "expose_headers", expose_headers)
        if max_age_seconds is not None:
            pulumi.set(__self__, "max_age_seconds", max_age_seconds)

    @property
    @pulumi.getter(name="allowedMethods")
    def allowed_methods(self) -> Sequence[str]:
        return pulumi.get(self, "allowed_methods")

    @property
    @pulumi.getter(name="allowedOrigins")
    def allowed_origins(self) -> Sequence[str]:
        return pulumi.get(self, "allowed_origins")

    @property
    @pulumi.getter(name="allowedHeaders")
    def allowed_headers(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "allowed_headers")

    @property
    @pulumi.getter(name="exposeHeaders")
    def expose_headers(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "expose_headers")

    @property
    @pulumi.getter(name="maxAgeSeconds")
    def max_age_seconds(self) -> Optional[int]:
        return pulumi.get(self, "max_age_seconds")


@pulumi.output_type
class BucketGrant(dict):
    def __init__(__self__, *,
                 permissions: Sequence[str],
                 type: str,
                 id: Optional[str] = None,
                 uri: Optional[str] = None):
        pulumi.set(__self__, "permissions", permissions)
        pulumi.set(__self__, "type", type)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if uri is not None:
            pulumi.set(__self__, "uri", uri)

    @property
    @pulumi.getter
    def permissions(self) -> Sequence[str]:
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def uri(self) -> Optional[str]:
        return pulumi.get(self, "uri")


@pulumi.output_type
class BucketLifecycleRule(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "abortIncompleteMultipartUploadDays":
            suggest = "abort_incomplete_multipart_upload_days"
        elif key == "noncurrentVersionExpiration":
            suggest = "noncurrent_version_expiration"
        elif key == "noncurrentVersionTransitions":
            suggest = "noncurrent_version_transitions"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in BucketLifecycleRule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        BucketLifecycleRule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        BucketLifecycleRule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 enabled: bool,
                 abort_incomplete_multipart_upload_days: Optional[int] = None,
                 expiration: Optional['outputs.BucketLifecycleRuleExpiration'] = None,
                 id: Optional[str] = None,
                 noncurrent_version_expiration: Optional['outputs.BucketLifecycleRuleNoncurrentVersionExpiration'] = None,
                 noncurrent_version_transitions: Optional[Sequence['outputs.BucketLifecycleRuleNoncurrentVersionTransition']] = None,
                 prefix: Optional[str] = None,
                 transitions: Optional[Sequence['outputs.BucketLifecycleRuleTransition']] = None):
        pulumi.set(__self__, "enabled", enabled)
        if abort_incomplete_multipart_upload_days is not None:
            pulumi.set(__self__, "abort_incomplete_multipart_upload_days", abort_incomplete_multipart_upload_days)
        if expiration is not None:
            pulumi.set(__self__, "expiration", expiration)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if noncurrent_version_expiration is not None:
            pulumi.set(__self__, "noncurrent_version_expiration", noncurrent_version_expiration)
        if noncurrent_version_transitions is not None:
            pulumi.set(__self__, "noncurrent_version_transitions", noncurrent_version_transitions)
        if prefix is not None:
            pulumi.set(__self__, "prefix", prefix)
        if transitions is not None:
            pulumi.set(__self__, "transitions", transitions)

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="abortIncompleteMultipartUploadDays")
    def abort_incomplete_multipart_upload_days(self) -> Optional[int]:
        return pulumi.get(self, "abort_incomplete_multipart_upload_days")

    @property
    @pulumi.getter
    def expiration(self) -> Optional['outputs.BucketLifecycleRuleExpiration']:
        return pulumi.get(self, "expiration")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="noncurrentVersionExpiration")
    def noncurrent_version_expiration(self) -> Optional['outputs.BucketLifecycleRuleNoncurrentVersionExpiration']:
        return pulumi.get(self, "noncurrent_version_expiration")

    @property
    @pulumi.getter(name="noncurrentVersionTransitions")
    def noncurrent_version_transitions(self) -> Optional[Sequence['outputs.BucketLifecycleRuleNoncurrentVersionTransition']]:
        return pulumi.get(self, "noncurrent_version_transitions")

    @property
    @pulumi.getter
    def prefix(self) -> Optional[str]:
        return pulumi.get(self, "prefix")

    @property
    @pulumi.getter
    def transitions(self) -> Optional[Sequence['outputs.BucketLifecycleRuleTransition']]:
        return pulumi.get(self, "transitions")


@pulumi.output_type
class BucketLifecycleRuleExpiration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "expiredObjectDeleteMarker":
            suggest = "expired_object_delete_marker"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in BucketLifecycleRuleExpiration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        BucketLifecycleRuleExpiration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        BucketLifecycleRuleExpiration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 date: Optional[str] = None,
                 days: Optional[int] = None,
                 expired_object_delete_marker: Optional[bool] = None):
        if date is not None:
            pulumi.set(__self__, "date", date)
        if days is not None:
            pulumi.set(__self__, "days", days)
        if expired_object_delete_marker is not None:
            pulumi.set(__self__, "expired_object_delete_marker", expired_object_delete_marker)

    @property
    @pulumi.getter
    def date(self) -> Optional[str]:
        return pulumi.get(self, "date")

    @property
    @pulumi.getter
    def days(self) -> Optional[int]:
        return pulumi.get(self, "days")

    @property
    @pulumi.getter(name="expiredObjectDeleteMarker")
    def expired_object_delete_marker(self) -> Optional[bool]:
        return pulumi.get(self, "expired_object_delete_marker")


@pulumi.output_type
class BucketLifecycleRuleNoncurrentVersionExpiration(dict):
    def __init__(__self__, *,
                 days: Optional[int] = None):
        if days is not None:
            pulumi.set(__self__, "days", days)

    @property
    @pulumi.getter
    def days(self) -> Optional[int]:
        return pulumi.get(self, "days")


@pulumi.output_type
class BucketLifecycleRuleNoncurrentVersionTransition(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "storageClass":
            suggest = "storage_class"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in BucketLifecycleRuleNoncurrentVersionTransition. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        BucketLifecycleRuleNoncurrentVersionTransition.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        BucketLifecycleRuleNoncurrentVersionTransition.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 storage_class: str,
                 days: Optional[int] = None):
        pulumi.set(__self__, "storage_class", storage_class)
        if days is not None:
            pulumi.set(__self__, "days", days)

    @property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> str:
        return pulumi.get(self, "storage_class")

    @property
    @pulumi.getter
    def days(self) -> Optional[int]:
        return pulumi.get(self, "days")


@pulumi.output_type
class BucketLifecycleRuleTransition(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "storageClass":
            suggest = "storage_class"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in BucketLifecycleRuleTransition. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        BucketLifecycleRuleTransition.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        BucketLifecycleRuleTransition.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 storage_class: str,
                 date: Optional[str] = None,
                 days: Optional[int] = None):
        pulumi.set(__self__, "storage_class", storage_class)
        if date is not None:
            pulumi.set(__self__, "date", date)
        if days is not None:
            pulumi.set(__self__, "days", days)

    @property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> str:
        return pulumi.get(self, "storage_class")

    @property
    @pulumi.getter
    def date(self) -> Optional[str]:
        return pulumi.get(self, "date")

    @property
    @pulumi.getter
    def days(self) -> Optional[int]:
        return pulumi.get(self, "days")


@pulumi.output_type
class BucketLogging(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "targetBucket":
            suggest = "target_bucket"
        elif key == "targetPrefix":
            suggest = "target_prefix"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in BucketLogging. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        BucketLogging.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        BucketLogging.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 target_bucket: str,
                 target_prefix: Optional[str] = None):
        pulumi.set(__self__, "target_bucket", target_bucket)
        if target_prefix is not None:
            pulumi.set(__self__, "target_prefix", target_prefix)

    @property
    @pulumi.getter(name="targetBucket")
    def target_bucket(self) -> str:
        return pulumi.get(self, "target_bucket")

    @property
    @pulumi.getter(name="targetPrefix")
    def target_prefix(self) -> Optional[str]:
        return pulumi.get(self, "target_prefix")


@pulumi.output_type
class BucketVersioning(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "mfaDelete":
            suggest = "mfa_delete"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in BucketVersioning. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        BucketVersioning.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        BucketVersioning.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 enabled: Optional[bool] = None,
                 mfa_delete: Optional[bool] = None):
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if mfa_delete is not None:
            pulumi.set(__self__, "mfa_delete", mfa_delete)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="mfaDelete")
    def mfa_delete(self) -> Optional[bool]:
        return pulumi.get(self, "mfa_delete")


@pulumi.output_type
class GetGroupUserResult(dict):
    def __init__(__self__, *,
                 arn: str,
                 path: str,
                 user_id: str,
                 user_name: str):
        pulumi.set(__self__, "arn", arn)
        pulumi.set(__self__, "path", path)
        pulumi.set(__self__, "user_id", user_id)
        pulumi.set(__self__, "user_name", user_name)

    @property
    @pulumi.getter
    def arn(self) -> str:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def path(self) -> str:
        return pulumi.get(self, "path")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> str:
        return pulumi.get(self, "user_id")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> str:
        return pulumi.get(self, "user_name")


@pulumi.output_type
class GetPolicyDocumentStatementResult(dict):
    def __init__(__self__, *,
                 actions: Optional[Sequence[str]] = None,
                 conditions: Optional[Sequence['outputs.GetPolicyDocumentStatementConditionResult']] = None,
                 effect: Optional[str] = None,
                 not_actions: Optional[Sequence[str]] = None,
                 not_principals: Optional[Sequence['outputs.GetPolicyDocumentStatementNotPrincipalResult']] = None,
                 not_resources: Optional[Sequence[str]] = None,
                 principals: Optional[Sequence['outputs.GetPolicyDocumentStatementPrincipalResult']] = None,
                 resources: Optional[Sequence[str]] = None,
                 sid: Optional[str] = None):
        if actions is not None:
            pulumi.set(__self__, "actions", actions)
        if conditions is not None:
            pulumi.set(__self__, "conditions", conditions)
        if effect is not None:
            pulumi.set(__self__, "effect", effect)
        if not_actions is not None:
            pulumi.set(__self__, "not_actions", not_actions)
        if not_principals is not None:
            pulumi.set(__self__, "not_principals", not_principals)
        if not_resources is not None:
            pulumi.set(__self__, "not_resources", not_resources)
        if principals is not None:
            pulumi.set(__self__, "principals", principals)
        if resources is not None:
            pulumi.set(__self__, "resources", resources)
        if sid is not None:
            pulumi.set(__self__, "sid", sid)

    @property
    @pulumi.getter
    def actions(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter
    def conditions(self) -> Optional[Sequence['outputs.GetPolicyDocumentStatementConditionResult']]:
        return pulumi.get(self, "conditions")

    @property
    @pulumi.getter
    def effect(self) -> Optional[str]:
        return pulumi.get(self, "effect")

    @property
    @pulumi.getter(name="notActions")
    def not_actions(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "not_actions")

    @property
    @pulumi.getter(name="notPrincipals")
    def not_principals(self) -> Optional[Sequence['outputs.GetPolicyDocumentStatementNotPrincipalResult']]:
        return pulumi.get(self, "not_principals")

    @property
    @pulumi.getter(name="notResources")
    def not_resources(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "not_resources")

    @property
    @pulumi.getter
    def principals(self) -> Optional[Sequence['outputs.GetPolicyDocumentStatementPrincipalResult']]:
        return pulumi.get(self, "principals")

    @property
    @pulumi.getter
    def resources(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "resources")

    @property
    @pulumi.getter
    def sid(self) -> Optional[str]:
        return pulumi.get(self, "sid")


@pulumi.output_type
class GetPolicyDocumentStatementConditionResult(dict):
    def __init__(__self__, *,
                 test: str,
                 values: Sequence[str],
                 variable: str):
        pulumi.set(__self__, "test", test)
        pulumi.set(__self__, "values", values)
        pulumi.set(__self__, "variable", variable)

    @property
    @pulumi.getter
    def test(self) -> str:
        return pulumi.get(self, "test")

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")

    @property
    @pulumi.getter
    def variable(self) -> str:
        return pulumi.get(self, "variable")


@pulumi.output_type
class GetPolicyDocumentStatementNotPrincipalResult(dict):
    def __init__(__self__, *,
                 identifiers: Sequence[str],
                 type: str):
        pulumi.set(__self__, "identifiers", identifiers)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def identifiers(self) -> Sequence[str]:
        return pulumi.get(self, "identifiers")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")


@pulumi.output_type
class GetPolicyDocumentStatementPrincipalResult(dict):
    def __init__(__self__, *,
                 identifiers: Sequence[str],
                 type: str):
        pulumi.set(__self__, "identifiers", identifiers)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def identifiers(self) -> Sequence[str]:
        return pulumi.get(self, "identifiers")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")


