// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Wasabi
{
    public static class GetRole
    {
        public static Task<GetRoleResult> InvokeAsync(GetRoleArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetRoleResult>("wasabi:index/getRole:getRole", args ?? new GetRoleArgs(), options.WithDefaults());

        public static Output<GetRoleResult> Invoke(GetRoleInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetRoleResult>("wasabi:index/getRole:getRole", args ?? new GetRoleInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetRoleArgs : global::Pulumi.InvokeArgs
    {
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetRoleArgs()
        {
        }
        public static new GetRoleArgs Empty => new GetRoleArgs();
    }

    public sealed class GetRoleInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetRoleInvokeArgs()
        {
        }
        public static new GetRoleInvokeArgs Empty => new GetRoleInvokeArgs();
    }


    [OutputType]
    public sealed class GetRoleResult
    {
        public readonly string Arn;
        public readonly string AssumeRolePolicy;
        public readonly string CreateDate;
        public readonly string Description;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly int MaxSessionDuration;
        public readonly string Name;
        public readonly string Path;
        public readonly string PermissionsBoundary;
        public readonly string UniqueId;

        [OutputConstructor]
        private GetRoleResult(
            string arn,

            string assumeRolePolicy,

            string createDate,

            string description,

            string id,

            int maxSessionDuration,

            string name,

            string path,

            string permissionsBoundary,

            string uniqueId)
        {
            Arn = arn;
            AssumeRolePolicy = assumeRolePolicy;
            CreateDate = createDate;
            Description = description;
            Id = id;
            MaxSessionDuration = maxSessionDuration;
            Name = name;
            Path = path;
            PermissionsBoundary = permissionsBoundary;
            UniqueId = uniqueId;
        }
    }
}
