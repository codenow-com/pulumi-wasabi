// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Wasabi
{
    [WasabiResourceType("wasabi:index/userGroupMembership:UserGroupMembership")]
    public partial class UserGroupMembership : global::Pulumi.CustomResource
    {
        [Output("groups")]
        public Output<ImmutableArray<string>> Groups { get; private set; } = null!;

        [Output("user")]
        public Output<string> User { get; private set; } = null!;


        /// <summary>
        /// Create a UserGroupMembership resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public UserGroupMembership(string name, UserGroupMembershipArgs args, CustomResourceOptions? options = null)
            : base("wasabi:index/userGroupMembership:UserGroupMembership", name, args ?? new UserGroupMembershipArgs(), MakeResourceOptions(options, ""))
        {
        }

        private UserGroupMembership(string name, Input<string> id, UserGroupMembershipState? state = null, CustomResourceOptions? options = null)
            : base("wasabi:index/userGroupMembership:UserGroupMembership", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing UserGroupMembership resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static UserGroupMembership Get(string name, Input<string> id, UserGroupMembershipState? state = null, CustomResourceOptions? options = null)
        {
            return new UserGroupMembership(name, id, state, options);
        }
    }

    public sealed class UserGroupMembershipArgs : global::Pulumi.ResourceArgs
    {
        [Input("groups", required: true)]
        private InputList<string>? _groups;
        public InputList<string> Groups
        {
            get => _groups ?? (_groups = new InputList<string>());
            set => _groups = value;
        }

        [Input("user", required: true)]
        public Input<string> User { get; set; } = null!;

        public UserGroupMembershipArgs()
        {
        }
        public static new UserGroupMembershipArgs Empty => new UserGroupMembershipArgs();
    }

    public sealed class UserGroupMembershipState : global::Pulumi.ResourceArgs
    {
        [Input("groups")]
        private InputList<string>? _groups;
        public InputList<string> Groups
        {
            get => _groups ?? (_groups = new InputList<string>());
            set => _groups = value;
        }

        [Input("user")]
        public Input<string>? User { get; set; }

        public UserGroupMembershipState()
        {
        }
        public static new UserGroupMembershipState Empty => new UserGroupMembershipState();
    }
}
