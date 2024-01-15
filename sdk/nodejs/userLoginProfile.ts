// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class UserLoginProfile extends pulumi.CustomResource {
    /**
     * Get an existing UserLoginProfile resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserLoginProfileState, opts?: pulumi.CustomResourceOptions): UserLoginProfile {
        return new UserLoginProfile(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'wasabi:index/userLoginProfile:UserLoginProfile';

    /**
     * Returns true if the given object is an instance of UserLoginProfile.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is UserLoginProfile {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === UserLoginProfile.__pulumiType;
    }

    public /*out*/ readonly encryptedPassword!: pulumi.Output<string>;
    public /*out*/ readonly keyFingerprint!: pulumi.Output<string>;
    public readonly passwordLength!: pulumi.Output<number | undefined>;
    public readonly passwordResetRequired!: pulumi.Output<boolean | undefined>;
    public readonly pgpKey!: pulumi.Output<string>;
    public readonly user!: pulumi.Output<string>;

    /**
     * Create a UserLoginProfile resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: UserLoginProfileArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: UserLoginProfileArgs | UserLoginProfileState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as UserLoginProfileState | undefined;
            resourceInputs["encryptedPassword"] = state ? state.encryptedPassword : undefined;
            resourceInputs["keyFingerprint"] = state ? state.keyFingerprint : undefined;
            resourceInputs["passwordLength"] = state ? state.passwordLength : undefined;
            resourceInputs["passwordResetRequired"] = state ? state.passwordResetRequired : undefined;
            resourceInputs["pgpKey"] = state ? state.pgpKey : undefined;
            resourceInputs["user"] = state ? state.user : undefined;
        } else {
            const args = argsOrState as UserLoginProfileArgs | undefined;
            if ((!args || args.pgpKey === undefined) && !opts.urn) {
                throw new Error("Missing required property 'pgpKey'");
            }
            if ((!args || args.user === undefined) && !opts.urn) {
                throw new Error("Missing required property 'user'");
            }
            resourceInputs["passwordLength"] = args ? args.passwordLength : undefined;
            resourceInputs["passwordResetRequired"] = args ? args.passwordResetRequired : undefined;
            resourceInputs["pgpKey"] = args ? args.pgpKey : undefined;
            resourceInputs["user"] = args ? args.user : undefined;
            resourceInputs["encryptedPassword"] = undefined /*out*/;
            resourceInputs["keyFingerprint"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(UserLoginProfile.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering UserLoginProfile resources.
 */
export interface UserLoginProfileState {
    encryptedPassword?: pulumi.Input<string>;
    keyFingerprint?: pulumi.Input<string>;
    passwordLength?: pulumi.Input<number>;
    passwordResetRequired?: pulumi.Input<boolean>;
    pgpKey?: pulumi.Input<string>;
    user?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a UserLoginProfile resource.
 */
export interface UserLoginProfileArgs {
    passwordLength?: pulumi.Input<number>;
    passwordResetRequired?: pulumi.Input<boolean>;
    pgpKey: pulumi.Input<string>;
    user: pulumi.Input<string>;
}