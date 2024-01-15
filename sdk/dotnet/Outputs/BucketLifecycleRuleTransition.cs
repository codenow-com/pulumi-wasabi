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
    public sealed class BucketLifecycleRuleTransition
    {
        public readonly string? Date;
        public readonly int? Days;
        public readonly string StorageClass;

        [OutputConstructor]
        private BucketLifecycleRuleTransition(
            string? date,

            int? days,

            string storageClass)
        {
            Date = date;
            Days = days;
            StorageClass = storageClass;
        }
    }
}
