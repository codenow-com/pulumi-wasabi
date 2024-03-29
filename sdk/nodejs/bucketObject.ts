// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class BucketObject extends pulumi.CustomResource {
    /**
     * Get an existing BucketObject resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BucketObjectState, opts?: pulumi.CustomResourceOptions): BucketObject {
        return new BucketObject(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'wasabi:index/bucketObject:BucketObject';

    /**
     * Returns true if the given object is an instance of BucketObject.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is BucketObject {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === BucketObject.__pulumiType;
    }

    public readonly acl!: pulumi.Output<string | undefined>;
    public readonly bucket!: pulumi.Output<string>;
    public readonly cacheControl!: pulumi.Output<string | undefined>;
    public readonly content!: pulumi.Output<string | undefined>;
    public readonly contentBase64!: pulumi.Output<string | undefined>;
    public readonly contentDisposition!: pulumi.Output<string | undefined>;
    public readonly contentEncoding!: pulumi.Output<string | undefined>;
    public readonly contentLanguage!: pulumi.Output<string | undefined>;
    public readonly contentType!: pulumi.Output<string>;
    public readonly etag!: pulumi.Output<string>;
    public readonly forceDestroy!: pulumi.Output<boolean | undefined>;
    public readonly key!: pulumi.Output<string>;
    public readonly metadata!: pulumi.Output<{[key: string]: string} | undefined>;
    public readonly source!: pulumi.Output<string | undefined>;
    public readonly storageClass!: pulumi.Output<string>;
    public /*out*/ readonly versionId!: pulumi.Output<string>;

    /**
     * Create a BucketObject resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: BucketObjectArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: BucketObjectArgs | BucketObjectState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as BucketObjectState | undefined;
            resourceInputs["acl"] = state ? state.acl : undefined;
            resourceInputs["bucket"] = state ? state.bucket : undefined;
            resourceInputs["cacheControl"] = state ? state.cacheControl : undefined;
            resourceInputs["content"] = state ? state.content : undefined;
            resourceInputs["contentBase64"] = state ? state.contentBase64 : undefined;
            resourceInputs["contentDisposition"] = state ? state.contentDisposition : undefined;
            resourceInputs["contentEncoding"] = state ? state.contentEncoding : undefined;
            resourceInputs["contentLanguage"] = state ? state.contentLanguage : undefined;
            resourceInputs["contentType"] = state ? state.contentType : undefined;
            resourceInputs["etag"] = state ? state.etag : undefined;
            resourceInputs["forceDestroy"] = state ? state.forceDestroy : undefined;
            resourceInputs["key"] = state ? state.key : undefined;
            resourceInputs["metadata"] = state ? state.metadata : undefined;
            resourceInputs["source"] = state ? state.source : undefined;
            resourceInputs["storageClass"] = state ? state.storageClass : undefined;
            resourceInputs["versionId"] = state ? state.versionId : undefined;
        } else {
            const args = argsOrState as BucketObjectArgs | undefined;
            if ((!args || args.bucket === undefined) && !opts.urn) {
                throw new Error("Missing required property 'bucket'");
            }
            if ((!args || args.key === undefined) && !opts.urn) {
                throw new Error("Missing required property 'key'");
            }
            resourceInputs["acl"] = args ? args.acl : undefined;
            resourceInputs["bucket"] = args ? args.bucket : undefined;
            resourceInputs["cacheControl"] = args ? args.cacheControl : undefined;
            resourceInputs["content"] = args ? args.content : undefined;
            resourceInputs["contentBase64"] = args ? args.contentBase64 : undefined;
            resourceInputs["contentDisposition"] = args ? args.contentDisposition : undefined;
            resourceInputs["contentEncoding"] = args ? args.contentEncoding : undefined;
            resourceInputs["contentLanguage"] = args ? args.contentLanguage : undefined;
            resourceInputs["contentType"] = args ? args.contentType : undefined;
            resourceInputs["etag"] = args ? args.etag : undefined;
            resourceInputs["forceDestroy"] = args ? args.forceDestroy : undefined;
            resourceInputs["key"] = args ? args.key : undefined;
            resourceInputs["metadata"] = args ? args.metadata : undefined;
            resourceInputs["source"] = args ? args.source : undefined;
            resourceInputs["storageClass"] = args ? args.storageClass : undefined;
            resourceInputs["versionId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(BucketObject.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering BucketObject resources.
 */
export interface BucketObjectState {
    acl?: pulumi.Input<string>;
    bucket?: pulumi.Input<string>;
    cacheControl?: pulumi.Input<string>;
    content?: pulumi.Input<string>;
    contentBase64?: pulumi.Input<string>;
    contentDisposition?: pulumi.Input<string>;
    contentEncoding?: pulumi.Input<string>;
    contentLanguage?: pulumi.Input<string>;
    contentType?: pulumi.Input<string>;
    etag?: pulumi.Input<string>;
    forceDestroy?: pulumi.Input<boolean>;
    key?: pulumi.Input<string>;
    metadata?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    source?: pulumi.Input<string>;
    storageClass?: pulumi.Input<string>;
    versionId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a BucketObject resource.
 */
export interface BucketObjectArgs {
    acl?: pulumi.Input<string>;
    bucket: pulumi.Input<string>;
    cacheControl?: pulumi.Input<string>;
    content?: pulumi.Input<string>;
    contentBase64?: pulumi.Input<string>;
    contentDisposition?: pulumi.Input<string>;
    contentEncoding?: pulumi.Input<string>;
    contentLanguage?: pulumi.Input<string>;
    contentType?: pulumi.Input<string>;
    etag?: pulumi.Input<string>;
    forceDestroy?: pulumi.Input<boolean>;
    key: pulumi.Input<string>;
    metadata?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    source?: pulumi.Input<string>;
    storageClass?: pulumi.Input<string>;
}
