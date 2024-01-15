// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Wasabi
{
    [WasabiResourceType("wasabi:index/bucketObject:BucketObject")]
    public partial class BucketObject : global::Pulumi.CustomResource
    {
        [Output("acl")]
        public Output<string?> Acl { get; private set; } = null!;

        [Output("bucket")]
        public Output<string> Bucket { get; private set; } = null!;

        [Output("cacheControl")]
        public Output<string?> CacheControl { get; private set; } = null!;

        [Output("content")]
        public Output<string?> Content { get; private set; } = null!;

        [Output("contentBase64")]
        public Output<string?> ContentBase64 { get; private set; } = null!;

        [Output("contentDisposition")]
        public Output<string?> ContentDisposition { get; private set; } = null!;

        [Output("contentEncoding")]
        public Output<string?> ContentEncoding { get; private set; } = null!;

        [Output("contentLanguage")]
        public Output<string?> ContentLanguage { get; private set; } = null!;

        [Output("contentType")]
        public Output<string> ContentType { get; private set; } = null!;

        [Output("etag")]
        public Output<string> Etag { get; private set; } = null!;

        [Output("forceDestroy")]
        public Output<bool?> ForceDestroy { get; private set; } = null!;

        [Output("key")]
        public Output<string> Key { get; private set; } = null!;

        [Output("metadata")]
        public Output<ImmutableDictionary<string, string>?> Metadata { get; private set; } = null!;

        [Output("source")]
        public Output<string?> Source { get; private set; } = null!;

        [Output("storageClass")]
        public Output<string> StorageClass { get; private set; } = null!;

        [Output("versionId")]
        public Output<string> VersionId { get; private set; } = null!;


        /// <summary>
        /// Create a BucketObject resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public BucketObject(string name, BucketObjectArgs args, CustomResourceOptions? options = null)
            : base("wasabi:index/bucketObject:BucketObject", name, args ?? new BucketObjectArgs(), MakeResourceOptions(options, ""))
        {
        }

        private BucketObject(string name, Input<string> id, BucketObjectState? state = null, CustomResourceOptions? options = null)
            : base("wasabi:index/bucketObject:BucketObject", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing BucketObject resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static BucketObject Get(string name, Input<string> id, BucketObjectState? state = null, CustomResourceOptions? options = null)
        {
            return new BucketObject(name, id, state, options);
        }
    }

    public sealed class BucketObjectArgs : global::Pulumi.ResourceArgs
    {
        [Input("acl")]
        public Input<string>? Acl { get; set; }

        [Input("bucket", required: true)]
        public Input<string> Bucket { get; set; } = null!;

        [Input("cacheControl")]
        public Input<string>? CacheControl { get; set; }

        [Input("content")]
        public Input<string>? Content { get; set; }

        [Input("contentBase64")]
        public Input<string>? ContentBase64 { get; set; }

        [Input("contentDisposition")]
        public Input<string>? ContentDisposition { get; set; }

        [Input("contentEncoding")]
        public Input<string>? ContentEncoding { get; set; }

        [Input("contentLanguage")]
        public Input<string>? ContentLanguage { get; set; }

        [Input("contentType")]
        public Input<string>? ContentType { get; set; }

        [Input("etag")]
        public Input<string>? Etag { get; set; }

        [Input("forceDestroy")]
        public Input<bool>? ForceDestroy { get; set; }

        [Input("key", required: true)]
        public Input<string> Key { get; set; } = null!;

        [Input("metadata")]
        private InputMap<string>? _metadata;
        public InputMap<string> Metadata
        {
            get => _metadata ?? (_metadata = new InputMap<string>());
            set => _metadata = value;
        }

        [Input("source")]
        public Input<string>? Source { get; set; }

        [Input("storageClass")]
        public Input<string>? StorageClass { get; set; }

        public BucketObjectArgs()
        {
        }
        public static new BucketObjectArgs Empty => new BucketObjectArgs();
    }

    public sealed class BucketObjectState : global::Pulumi.ResourceArgs
    {
        [Input("acl")]
        public Input<string>? Acl { get; set; }

        [Input("bucket")]
        public Input<string>? Bucket { get; set; }

        [Input("cacheControl")]
        public Input<string>? CacheControl { get; set; }

        [Input("content")]
        public Input<string>? Content { get; set; }

        [Input("contentBase64")]
        public Input<string>? ContentBase64 { get; set; }

        [Input("contentDisposition")]
        public Input<string>? ContentDisposition { get; set; }

        [Input("contentEncoding")]
        public Input<string>? ContentEncoding { get; set; }

        [Input("contentLanguage")]
        public Input<string>? ContentLanguage { get; set; }

        [Input("contentType")]
        public Input<string>? ContentType { get; set; }

        [Input("etag")]
        public Input<string>? Etag { get; set; }

        [Input("forceDestroy")]
        public Input<bool>? ForceDestroy { get; set; }

        [Input("key")]
        public Input<string>? Key { get; set; }

        [Input("metadata")]
        private InputMap<string>? _metadata;
        public InputMap<string> Metadata
        {
            get => _metadata ?? (_metadata = new InputMap<string>());
            set => _metadata = value;
        }

        [Input("source")]
        public Input<string>? Source { get; set; }

        [Input("storageClass")]
        public Input<string>? StorageClass { get; set; }

        [Input("versionId")]
        public Input<string>? VersionId { get; set; }

        public BucketObjectState()
        {
        }
        public static new BucketObjectState Empty => new BucketObjectState();
    }
}
