// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Wasabi
{
    [WasabiResourceType("wasabi:index/rolePolicy:RolePolicy")]
    public partial class RolePolicy : global::Pulumi.CustomResource
    {
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("namePrefix")]
        public Output<string?> NamePrefix { get; private set; } = null!;

        [Output("policy")]
        public Output<string> Policy { get; private set; } = null!;

        [Output("role")]
        public Output<string> Role { get; private set; } = null!;


        /// <summary>
        /// Create a RolePolicy resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public RolePolicy(string name, RolePolicyArgs args, CustomResourceOptions? options = null)
            : base("wasabi:index/rolePolicy:RolePolicy", name, args ?? new RolePolicyArgs(), MakeResourceOptions(options, ""))
        {
        }

        private RolePolicy(string name, Input<string> id, RolePolicyState? state = null, CustomResourceOptions? options = null)
            : base("wasabi:index/rolePolicy:RolePolicy", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing RolePolicy resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static RolePolicy Get(string name, Input<string> id, RolePolicyState? state = null, CustomResourceOptions? options = null)
        {
            return new RolePolicy(name, id, state, options);
        }
    }

    public sealed class RolePolicyArgs : global::Pulumi.ResourceArgs
    {
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("namePrefix")]
        public Input<string>? NamePrefix { get; set; }

        [Input("policy", required: true)]
        public Input<string> Policy { get; set; } = null!;

        [Input("role", required: true)]
        public Input<string> Role { get; set; } = null!;

        public RolePolicyArgs()
        {
        }
        public static new RolePolicyArgs Empty => new RolePolicyArgs();
    }

    public sealed class RolePolicyState : global::Pulumi.ResourceArgs
    {
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("namePrefix")]
        public Input<string>? NamePrefix { get; set; }

        [Input("policy")]
        public Input<string>? Policy { get; set; }

        [Input("role")]
        public Input<string>? Role { get; set; }

        public RolePolicyState()
        {
        }
        public static new RolePolicyState Empty => new RolePolicyState();
    }
}
