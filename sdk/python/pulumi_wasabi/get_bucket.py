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
    'GetBucketResult',
    'AwaitableGetBucketResult',
    'get_bucket',
    'get_bucket_output',
]

@pulumi.output_type
class GetBucketResult:
    """
    A collection of values returned by getBucket.
    """
    def __init__(__self__, arn=None, bucket=None, bucket_domain_name=None, bucket_regional_domain_name=None, id=None, region=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if bucket and not isinstance(bucket, str):
            raise TypeError("Expected argument 'bucket' to be a str")
        pulumi.set(__self__, "bucket", bucket)
        if bucket_domain_name and not isinstance(bucket_domain_name, str):
            raise TypeError("Expected argument 'bucket_domain_name' to be a str")
        pulumi.set(__self__, "bucket_domain_name", bucket_domain_name)
        if bucket_regional_domain_name and not isinstance(bucket_regional_domain_name, str):
            raise TypeError("Expected argument 'bucket_regional_domain_name' to be a str")
        pulumi.set(__self__, "bucket_regional_domain_name", bucket_regional_domain_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter
    def arn(self) -> str:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def bucket(self) -> str:
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter(name="bucketDomainName")
    def bucket_domain_name(self) -> str:
        return pulumi.get(self, "bucket_domain_name")

    @property
    @pulumi.getter(name="bucketRegionalDomainName")
    def bucket_regional_domain_name(self) -> str:
        return pulumi.get(self, "bucket_regional_domain_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def region(self) -> str:
        return pulumi.get(self, "region")


class AwaitableGetBucketResult(GetBucketResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBucketResult(
            arn=self.arn,
            bucket=self.bucket,
            bucket_domain_name=self.bucket_domain_name,
            bucket_regional_domain_name=self.bucket_regional_domain_name,
            id=self.id,
            region=self.region)


def get_bucket(bucket: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBucketResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['bucket'] = bucket
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('wasabi:index/getBucket:getBucket', __args__, opts=opts, typ=GetBucketResult).value

    return AwaitableGetBucketResult(
        arn=pulumi.get(__ret__, 'arn'),
        bucket=pulumi.get(__ret__, 'bucket'),
        bucket_domain_name=pulumi.get(__ret__, 'bucket_domain_name'),
        bucket_regional_domain_name=pulumi.get(__ret__, 'bucket_regional_domain_name'),
        id=pulumi.get(__ret__, 'id'),
        region=pulumi.get(__ret__, 'region'))


@_utilities.lift_output_func(get_bucket)
def get_bucket_output(bucket: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBucketResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
