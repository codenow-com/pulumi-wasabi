// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export function getBucketObjects(args: GetBucketObjectsArgs, opts?: pulumi.InvokeOptions): Promise<GetBucketObjectsResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("wasabi:index/getBucketObjects:getBucketObjects", {
        "bucket": args.bucket,
        "delimiter": args.delimiter,
        "encodingType": args.encodingType,
        "fetchOwner": args.fetchOwner,
        "maxKeys": args.maxKeys,
        "prefix": args.prefix,
        "startAfter": args.startAfter,
    }, opts);
}

/**
 * A collection of arguments for invoking getBucketObjects.
 */
export interface GetBucketObjectsArgs {
    bucket: string;
    delimiter?: string;
    encodingType?: string;
    fetchOwner?: boolean;
    maxKeys?: number;
    prefix?: string;
    startAfter?: string;
}

/**
 * A collection of values returned by getBucketObjects.
 */
export interface GetBucketObjectsResult {
    readonly bucket: string;
    readonly commonPrefixes: string[];
    readonly delimiter?: string;
    readonly encodingType?: string;
    readonly fetchOwner?: boolean;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly keys: string[];
    readonly maxKeys?: number;
    readonly owners: string[];
    readonly prefix?: string;
    readonly startAfter?: string;
}
export function getBucketObjectsOutput(args: GetBucketObjectsOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetBucketObjectsResult> {
    return pulumi.output(args).apply((a: any) => getBucketObjects(a, opts))
}

/**
 * A collection of arguments for invoking getBucketObjects.
 */
export interface GetBucketObjectsOutputArgs {
    bucket: pulumi.Input<string>;
    delimiter?: pulumi.Input<string>;
    encodingType?: pulumi.Input<string>;
    fetchOwner?: pulumi.Input<boolean>;
    maxKeys?: pulumi.Input<number>;
    prefix?: pulumi.Input<string>;
    startAfter?: pulumi.Input<string>;
}
