// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Wasabi
{
    public static class GetBucketObject
    {
        public static Task<GetBucketObjectResult> InvokeAsync(GetBucketObjectArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetBucketObjectResult>("wasabi:index/getBucketObject:getBucketObject", args ?? new GetBucketObjectArgs(), options.WithDefaults());

        public static Output<GetBucketObjectResult> Invoke(GetBucketObjectInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetBucketObjectResult>("wasabi:index/getBucketObject:getBucketObject", args ?? new GetBucketObjectInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetBucketObjectArgs : global::Pulumi.InvokeArgs
    {
        [Input("bucket", required: true)]
        public string Bucket { get; set; } = null!;

        [Input("key", required: true)]
        public string Key { get; set; } = null!;

        [Input("range")]
        public string? Range { get; set; }

        [Input("versionId")]
        public string? VersionId { get; set; }

        public GetBucketObjectArgs()
        {
        }
        public static new GetBucketObjectArgs Empty => new GetBucketObjectArgs();
    }

    public sealed class GetBucketObjectInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("bucket", required: true)]
        public Input<string> Bucket { get; set; } = null!;

        [Input("key", required: true)]
        public Input<string> Key { get; set; } = null!;

        [Input("range")]
        public Input<string>? Range { get; set; }

        [Input("versionId")]
        public Input<string>? VersionId { get; set; }

        public GetBucketObjectInvokeArgs()
        {
        }
        public static new GetBucketObjectInvokeArgs Empty => new GetBucketObjectInvokeArgs();
    }


    [OutputType]
    public sealed class GetBucketObjectResult
    {
        public readonly string Body;
        public readonly string Bucket;
        public readonly string CacheControl;
        public readonly string ContentDisposition;
        public readonly string ContentEncoding;
        public readonly string ContentLanguage;
        public readonly int ContentLength;
        public readonly string ContentType;
        public readonly string Etag;
        public readonly string Expiration;
        public readonly string Expires;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Key;
        public readonly string LastModified;
        public readonly ImmutableDictionary<string, string> Metadata;
        public readonly string? Range;
        public readonly string SseKmsKeyId;
        public readonly string StorageClass;
        public readonly string VersionId;

        [OutputConstructor]
        private GetBucketObjectResult(
            string body,

            string bucket,

            string cacheControl,

            string contentDisposition,

            string contentEncoding,

            string contentLanguage,

            int contentLength,

            string contentType,

            string etag,

            string expiration,

            string expires,

            string id,

            string key,

            string lastModified,

            ImmutableDictionary<string, string> metadata,

            string? range,

            string sseKmsKeyId,

            string storageClass,

            string versionId)
        {
            Body = body;
            Bucket = bucket;
            CacheControl = cacheControl;
            ContentDisposition = contentDisposition;
            ContentEncoding = contentEncoding;
            ContentLanguage = contentLanguage;
            ContentLength = contentLength;
            ContentType = contentType;
            Etag = etag;
            Expiration = expiration;
            Expires = expires;
            Id = id;
            Key = key;
            LastModified = lastModified;
            Metadata = metadata;
            Range = range;
            SseKmsKeyId = sseKmsKeyId;
            StorageClass = storageClass;
            VersionId = versionId;
        }
    }
}
