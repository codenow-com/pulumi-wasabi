// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class RolePolicyAttachment extends pulumi.CustomResource {
    /**
     * Get an existing RolePolicyAttachment resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RolePolicyAttachmentState, opts?: pulumi.CustomResourceOptions): RolePolicyAttachment {
        return new RolePolicyAttachment(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'wasabi:index/rolePolicyAttachment:RolePolicyAttachment';

    /**
     * Returns true if the given object is an instance of RolePolicyAttachment.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is RolePolicyAttachment {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === RolePolicyAttachment.__pulumiType;
    }

    public readonly policyArn!: pulumi.Output<string>;
    public readonly role!: pulumi.Output<string>;

    /**
     * Create a RolePolicyAttachment resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RolePolicyAttachmentArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: RolePolicyAttachmentArgs | RolePolicyAttachmentState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as RolePolicyAttachmentState | undefined;
            resourceInputs["policyArn"] = state ? state.policyArn : undefined;
            resourceInputs["role"] = state ? state.role : undefined;
        } else {
            const args = argsOrState as RolePolicyAttachmentArgs | undefined;
            if ((!args || args.policyArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'policyArn'");
            }
            if ((!args || args.role === undefined) && !opts.urn) {
                throw new Error("Missing required property 'role'");
            }
            resourceInputs["policyArn"] = args ? args.policyArn : undefined;
            resourceInputs["role"] = args ? args.role : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(RolePolicyAttachment.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering RolePolicyAttachment resources.
 */
export interface RolePolicyAttachmentState {
    policyArn?: pulumi.Input<string>;
    role?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a RolePolicyAttachment resource.
 */
export interface RolePolicyAttachmentArgs {
    policyArn: pulumi.Input<string>;
    role: pulumi.Input<string>;
}