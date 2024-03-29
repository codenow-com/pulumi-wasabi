// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Wasabi
{
    [WasabiResourceType("wasabi:index/policyAttachment:PolicyAttachment")]
    public partial class PolicyAttachment : global::Pulumi.CustomResource
    {
        [Output("groups")]
        public Output<ImmutableArray<string>> Groups { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("policyArn")]
        public Output<string> PolicyArn { get; private set; } = null!;

        [Output("roles")]
        public Output<ImmutableArray<string>> Roles { get; private set; } = null!;

        [Output("users")]
        public Output<ImmutableArray<string>> Users { get; private set; } = null!;


        /// <summary>
        /// Create a PolicyAttachment resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public PolicyAttachment(string name, PolicyAttachmentArgs args, CustomResourceOptions? options = null)
            : base("wasabi:index/policyAttachment:PolicyAttachment", name, args ?? new PolicyAttachmentArgs(), MakeResourceOptions(options, ""))
        {
        }

        private PolicyAttachment(string name, Input<string> id, PolicyAttachmentState? state = null, CustomResourceOptions? options = null)
            : base("wasabi:index/policyAttachment:PolicyAttachment", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing PolicyAttachment resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static PolicyAttachment Get(string name, Input<string> id, PolicyAttachmentState? state = null, CustomResourceOptions? options = null)
        {
            return new PolicyAttachment(name, id, state, options);
        }
    }

    public sealed class PolicyAttachmentArgs : global::Pulumi.ResourceArgs
    {
        [Input("groups")]
        private InputList<string>? _groups;
        public InputList<string> Groups
        {
            get => _groups ?? (_groups = new InputList<string>());
            set => _groups = value;
        }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("policyArn", required: true)]
        public Input<string> PolicyArn { get; set; } = null!;

        [Input("roles")]
        private InputList<string>? _roles;
        public InputList<string> Roles
        {
            get => _roles ?? (_roles = new InputList<string>());
            set => _roles = value;
        }

        [Input("users")]
        private InputList<string>? _users;
        public InputList<string> Users
        {
            get => _users ?? (_users = new InputList<string>());
            set => _users = value;
        }

        public PolicyAttachmentArgs()
        {
        }
        public static new PolicyAttachmentArgs Empty => new PolicyAttachmentArgs();
    }

    public sealed class PolicyAttachmentState : global::Pulumi.ResourceArgs
    {
        [Input("groups")]
        private InputList<string>? _groups;
        public InputList<string> Groups
        {
            get => _groups ?? (_groups = new InputList<string>());
            set => _groups = value;
        }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("policyArn")]
        public Input<string>? PolicyArn { get; set; }

        [Input("roles")]
        private InputList<string>? _roles;
        public InputList<string> Roles
        {
            get => _roles ?? (_roles = new InputList<string>());
            set => _roles = value;
        }

        [Input("users")]
        private InputList<string>? _users;
        public InputList<string> Users
        {
            get => _users ?? (_users = new InputList<string>());
            set => _users = value;
        }

        public PolicyAttachmentState()
        {
        }
        public static new PolicyAttachmentState Empty => new PolicyAttachmentState();
    }
}
