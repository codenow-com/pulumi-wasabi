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
    public sealed class BucketVersioning
    {
        public readonly bool? Enabled;
        public readonly bool? MfaDelete;

        [OutputConstructor]
        private BucketVersioning(
            bool? enabled,

            bool? mfaDelete)
        {
            Enabled = enabled;
            MfaDelete = mfaDelete;
        }
    }
}
