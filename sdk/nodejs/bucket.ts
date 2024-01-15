// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export class Bucket extends pulumi.CustomResource {
    /**
     * Get an existing Bucket resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BucketState, opts?: pulumi.CustomResourceOptions): Bucket {
        return new Bucket(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'wasabi:index/bucket:Bucket';

    /**
     * Returns true if the given object is an instance of Bucket.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Bucket {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Bucket.__pulumiType;
    }

    public readonly acl!: pulumi.Output<string | undefined>;
    public readonly arn!: pulumi.Output<string>;
    public readonly bucket!: pulumi.Output<string>;
    public /*out*/ readonly bucketDomainName!: pulumi.Output<string>;
    public readonly bucketPrefix!: pulumi.Output<string | undefined>;
    public /*out*/ readonly bucketRegionalDomainName!: pulumi.Output<string>;
    public readonly corsRules!: pulumi.Output<outputs.BucketCorsRule[] | undefined>;
    public readonly forceDestroy!: pulumi.Output<boolean | undefined>;
    public readonly grants!: pulumi.Output<outputs.BucketGrant[] | undefined>;
    public readonly lifecycleRules!: pulumi.Output<outputs.BucketLifecycleRule[] | undefined>;
    public readonly loggings!: pulumi.Output<outputs.BucketLogging[] | undefined>;
    public readonly policy!: pulumi.Output<string | undefined>;
    public /*out*/ readonly region!: pulumi.Output<string>;
    public readonly requestPayer!: pulumi.Output<string>;
    public readonly versioning!: pulumi.Output<outputs.BucketVersioning>;

    /**
     * Create a Bucket resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: BucketArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: BucketArgs | BucketState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as BucketState | undefined;
            resourceInputs["acl"] = state ? state.acl : undefined;
            resourceInputs["arn"] = state ? state.arn : undefined;
            resourceInputs["bucket"] = state ? state.bucket : undefined;
            resourceInputs["bucketDomainName"] = state ? state.bucketDomainName : undefined;
            resourceInputs["bucketPrefix"] = state ? state.bucketPrefix : undefined;
            resourceInputs["bucketRegionalDomainName"] = state ? state.bucketRegionalDomainName : undefined;
            resourceInputs["corsRules"] = state ? state.corsRules : undefined;
            resourceInputs["forceDestroy"] = state ? state.forceDestroy : undefined;
            resourceInputs["grants"] = state ? state.grants : undefined;
            resourceInputs["lifecycleRules"] = state ? state.lifecycleRules : undefined;
            resourceInputs["loggings"] = state ? state.loggings : undefined;
            resourceInputs["policy"] = state ? state.policy : undefined;
            resourceInputs["region"] = state ? state.region : undefined;
            resourceInputs["requestPayer"] = state ? state.requestPayer : undefined;
            resourceInputs["versioning"] = state ? state.versioning : undefined;
        } else {
            const args = argsOrState as BucketArgs | undefined;
            resourceInputs["acl"] = args ? args.acl : undefined;
            resourceInputs["arn"] = args ? args.arn : undefined;
            resourceInputs["bucket"] = args ? args.bucket : undefined;
            resourceInputs["bucketPrefix"] = args ? args.bucketPrefix : undefined;
            resourceInputs["corsRules"] = args ? args.corsRules : undefined;
            resourceInputs["forceDestroy"] = args ? args.forceDestroy : undefined;
            resourceInputs["grants"] = args ? args.grants : undefined;
            resourceInputs["lifecycleRules"] = args ? args.lifecycleRules : undefined;
            resourceInputs["loggings"] = args ? args.loggings : undefined;
            resourceInputs["policy"] = args ? args.policy : undefined;
            resourceInputs["requestPayer"] = args ? args.requestPayer : undefined;
            resourceInputs["versioning"] = args ? args.versioning : undefined;
            resourceInputs["bucketDomainName"] = undefined /*out*/;
            resourceInputs["bucketRegionalDomainName"] = undefined /*out*/;
            resourceInputs["region"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Bucket.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Bucket resources.
 */
export interface BucketState {
    acl?: pulumi.Input<string>;
    arn?: pulumi.Input<string>;
    bucket?: pulumi.Input<string>;
    bucketDomainName?: pulumi.Input<string>;
    bucketPrefix?: pulumi.Input<string>;
    bucketRegionalDomainName?: pulumi.Input<string>;
    corsRules?: pulumi.Input<pulumi.Input<inputs.BucketCorsRule>[]>;
    forceDestroy?: pulumi.Input<boolean>;
    grants?: pulumi.Input<pulumi.Input<inputs.BucketGrant>[]>;
    lifecycleRules?: pulumi.Input<pulumi.Input<inputs.BucketLifecycleRule>[]>;
    loggings?: pulumi.Input<pulumi.Input<inputs.BucketLogging>[]>;
    policy?: pulumi.Input<string>;
    region?: pulumi.Input<string>;
    requestPayer?: pulumi.Input<string>;
    versioning?: pulumi.Input<inputs.BucketVersioning>;
}

/**
 * The set of arguments for constructing a Bucket resource.
 */
export interface BucketArgs {
    acl?: pulumi.Input<string>;
    arn?: pulumi.Input<string>;
    bucket?: pulumi.Input<string>;
    bucketPrefix?: pulumi.Input<string>;
    corsRules?: pulumi.Input<pulumi.Input<inputs.BucketCorsRule>[]>;
    forceDestroy?: pulumi.Input<boolean>;
    grants?: pulumi.Input<pulumi.Input<inputs.BucketGrant>[]>;
    lifecycleRules?: pulumi.Input<pulumi.Input<inputs.BucketLifecycleRule>[]>;
    loggings?: pulumi.Input<pulumi.Input<inputs.BucketLogging>[]>;
    policy?: pulumi.Input<string>;
    requestPayer?: pulumi.Input<string>;
    versioning?: pulumi.Input<inputs.BucketVersioning>;
}
