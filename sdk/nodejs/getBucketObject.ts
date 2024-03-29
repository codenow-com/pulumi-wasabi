// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export function getBucketObject(args: GetBucketObjectArgs, opts?: pulumi.InvokeOptions): Promise<GetBucketObjectResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("wasabi:index/getBucketObject:getBucketObject", {
        "bucket": args.bucket,
        "key": args.key,
        "range": args.range,
        "versionId": args.versionId,
    }, opts);
}

/**
 * A collection of arguments for invoking getBucketObject.
 */
export interface GetBucketObjectArgs {
    bucket: string;
    key: string;
    range?: string;
    versionId?: string;
}

/**
 * A collection of values returned by getBucketObject.
 */
export interface GetBucketObjectResult {
    readonly body: string;
    readonly bucket: string;
    readonly cacheControl: string;
    readonly contentDisposition: string;
    readonly contentEncoding: string;
    readonly contentLanguage: string;
    readonly contentLength: number;
    readonly contentType: string;
    readonly etag: string;
    readonly expiration: string;
    readonly expires: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly key: string;
    readonly lastModified: string;
    readonly metadata: {[key: string]: string};
    readonly range?: string;
    readonly sseKmsKeyId: string;
    readonly storageClass: string;
    readonly versionId: string;
}
export function getBucketObjectOutput(args: GetBucketObjectOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetBucketObjectResult> {
    return pulumi.output(args).apply((a: any) => getBucketObject(a, opts))
}

/**
 * A collection of arguments for invoking getBucketObject.
 */
export interface GetBucketObjectOutputArgs {
    bucket: pulumi.Input<string>;
    key: pulumi.Input<string>;
    range?: pulumi.Input<string>;
    versionId?: pulumi.Input<string>;
}
