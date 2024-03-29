// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * The provider type for the wasabi package. By default, resources use package-wide configuration
 * settings, however an explicit `Provider` instance may be created and passed during resource
 * construction to achieve fine-grained programmatic control over provider settings. See the
 * [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
 */
export class Provider extends pulumi.ProviderResource {
    /** @internal */
    public static readonly __pulumiType = 'wasabi';

    /**
     * Returns true if the given object is an instance of Provider.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Provider {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === "pulumi:providers:" + Provider.__pulumiType;
    }

    /**
     * The access key for API operations. You can retrieve this from the 'Security & Credentials' section of the AWS console.
     */
    public readonly accessKey!: pulumi.Output<string | undefined>;
    /**
     * The profile for API operations. If not set, the default profile created with `aws configure` will be used.
     */
    public readonly profile!: pulumi.Output<string | undefined>;
    /**
     * The region where AWS operations will take place. Examples are us-east-1, us-west-2, etc.
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * The secret key for API operations. You can retrieve this from the 'Security & Credentials' section of the AWS console.
     */
    public readonly secretKey!: pulumi.Output<string | undefined>;
    /**
     * The path to the shared credentials file. If not set this defaults to ~/.aws/credentials.
     */
    public readonly sharedCredentialsFile!: pulumi.Output<string | undefined>;
    /**
     * session token. A session token is only required if you are using temporary security credentials.
     */
    public readonly token!: pulumi.Output<string | undefined>;

    /**
     * Create a Provider resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ProviderArgs, opts?: pulumi.ResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        {
            if ((!args || args.region === undefined) && !opts.urn) {
                throw new Error("Missing required property 'region'");
            }
            resourceInputs["accessKey"] = args ? args.accessKey : undefined;
            resourceInputs["allowedAccountIds"] = pulumi.output(args ? args.allowedAccountIds : undefined).apply(JSON.stringify);
            resourceInputs["assumeRole"] = pulumi.output(args ? args.assumeRole : undefined).apply(JSON.stringify);
            resourceInputs["endpoints"] = pulumi.output(args ? args.endpoints : undefined).apply(JSON.stringify);
            resourceInputs["forbiddenAccountIds"] = pulumi.output(args ? args.forbiddenAccountIds : undefined).apply(JSON.stringify);
            resourceInputs["insecure"] = pulumi.output(args ? args.insecure : undefined).apply(JSON.stringify);
            resourceInputs["maxRetries"] = pulumi.output(args ? args.maxRetries : undefined).apply(JSON.stringify);
            resourceInputs["profile"] = args ? args.profile : undefined;
            resourceInputs["region"] = args ? args.region : undefined;
            resourceInputs["s3ForcePathStyle"] = pulumi.output(args ? args.s3ForcePathStyle : undefined).apply(JSON.stringify);
            resourceInputs["secretKey"] = args ? args.secretKey : undefined;
            resourceInputs["sharedCredentialsFile"] = args ? args.sharedCredentialsFile : undefined;
            resourceInputs["skipCredentialsValidation"] = pulumi.output(args ? args.skipCredentialsValidation : undefined).apply(JSON.stringify);
            resourceInputs["skipMetadataApiCheck"] = pulumi.output(args ? args.skipMetadataApiCheck : undefined).apply(JSON.stringify);
            resourceInputs["skipRequestingAccountId"] = pulumi.output(args ? args.skipRequestingAccountId : undefined).apply(JSON.stringify);
            resourceInputs["token"] = args ? args.token : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Provider.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Provider resource.
 */
export interface ProviderArgs {
    /**
     * The access key for API operations. You can retrieve this from the 'Security & Credentials' section of the AWS console.
     */
    accessKey?: pulumi.Input<string>;
    allowedAccountIds?: pulumi.Input<pulumi.Input<string>[]>;
    assumeRole?: pulumi.Input<inputs.ProviderAssumeRole>;
    endpoints?: pulumi.Input<pulumi.Input<inputs.ProviderEndpoint>[]>;
    forbiddenAccountIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Explicitly allow the provider to perform "insecure" SSL requests. If omitted,default value is `false`
     */
    insecure?: pulumi.Input<boolean>;
    /**
     * The maximum number of times an AWS API request is being executed. If the API request still fails, an error is thrown.
     */
    maxRetries?: pulumi.Input<number>;
    /**
     * The profile for API operations. If not set, the default profile created with `aws configure` will be used.
     */
    profile?: pulumi.Input<string>;
    /**
     * The region where AWS operations will take place. Examples are us-east-1, us-west-2, etc.
     */
    region: pulumi.Input<string>;
    /**
     * Set this to true to force the request to use path-style addressing, i.e., http://s3.amazonaws.com/BUCKET/KEY. By
     * default, the S3 client will use virtual hosted bucket addressing when possible (http://BUCKET.s3.amazonaws.com/KEY).
     * Specific to the Amazon S3 service.
     */
    s3ForcePathStyle?: pulumi.Input<boolean>;
    /**
     * The secret key for API operations. You can retrieve this from the 'Security & Credentials' section of the AWS console.
     */
    secretKey?: pulumi.Input<string>;
    /**
     * The path to the shared credentials file. If not set this defaults to ~/.aws/credentials.
     */
    sharedCredentialsFile?: pulumi.Input<string>;
    /**
     * Skip the credentials validation via STS API. Used for AWS API implementations that do not have STS
     * available/implemented.
     */
    skipCredentialsValidation?: pulumi.Input<boolean>;
    skipMetadataApiCheck?: pulumi.Input<boolean>;
    /**
     * Skip requesting the account ID. Used for AWS API implementations that do not have IAM/STS API and/or metadata API.
     */
    skipRequestingAccountId?: pulumi.Input<boolean>;
    /**
     * session token. A session token is only required if you are using temporary security credentials.
     */
    token?: pulumi.Input<string>;
}
