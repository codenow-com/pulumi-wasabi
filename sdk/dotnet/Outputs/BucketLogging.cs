// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Wasabi.Outputs
{

    [OutputType]
    public sealed class BucketLogging
    {
        public readonly string TargetBucket;
        public readonly string? TargetPrefix;

        [OutputConstructor]
        private BucketLogging(
            string targetBucket,

            string? targetPrefix)
        {
            TargetBucket = targetBucket;
            TargetPrefix = targetPrefix;
        }
    }
}
