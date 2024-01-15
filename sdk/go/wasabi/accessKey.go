// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package wasabi

import (
	"context"
	"reflect"

	"errors"
	"github.com/codenow-com/pulumi-wasabi/sdk/go/wasabi/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type AccessKey struct {
	pulumi.CustomResourceState

	EncryptedSecret   pulumi.StringOutput    `pulumi:"encryptedSecret"`
	KeyFingerprint    pulumi.StringOutput    `pulumi:"keyFingerprint"`
	PgpKey            pulumi.StringPtrOutput `pulumi:"pgpKey"`
	Secret            pulumi.StringOutput    `pulumi:"secret"`
	SesSmtpPasswordV4 pulumi.StringOutput    `pulumi:"sesSmtpPasswordV4"`
	Status            pulumi.StringOutput    `pulumi:"status"`
	User              pulumi.StringOutput    `pulumi:"user"`
}

// NewAccessKey registers a new resource with the given unique name, arguments, and options.
func NewAccessKey(ctx *pulumi.Context,
	name string, args *AccessKeyArgs, opts ...pulumi.ResourceOption) (*AccessKey, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.User == nil {
		return nil, errors.New("invalid value for required argument 'User'")
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"secret",
		"sesSmtpPasswordV4",
	})
	opts = append(opts, secrets)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource AccessKey
	err := ctx.RegisterResource("wasabi:index/accessKey:AccessKey", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAccessKey gets an existing AccessKey resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAccessKey(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AccessKeyState, opts ...pulumi.ResourceOption) (*AccessKey, error) {
	var resource AccessKey
	err := ctx.ReadResource("wasabi:index/accessKey:AccessKey", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering AccessKey resources.
type accessKeyState struct {
	EncryptedSecret   *string `pulumi:"encryptedSecret"`
	KeyFingerprint    *string `pulumi:"keyFingerprint"`
	PgpKey            *string `pulumi:"pgpKey"`
	Secret            *string `pulumi:"secret"`
	SesSmtpPasswordV4 *string `pulumi:"sesSmtpPasswordV4"`
	Status            *string `pulumi:"status"`
	User              *string `pulumi:"user"`
}

type AccessKeyState struct {
	EncryptedSecret   pulumi.StringPtrInput
	KeyFingerprint    pulumi.StringPtrInput
	PgpKey            pulumi.StringPtrInput
	Secret            pulumi.StringPtrInput
	SesSmtpPasswordV4 pulumi.StringPtrInput
	Status            pulumi.StringPtrInput
	User              pulumi.StringPtrInput
}

func (AccessKeyState) ElementType() reflect.Type {
	return reflect.TypeOf((*accessKeyState)(nil)).Elem()
}

type accessKeyArgs struct {
	PgpKey *string `pulumi:"pgpKey"`
	Status *string `pulumi:"status"`
	User   string  `pulumi:"user"`
}

// The set of arguments for constructing a AccessKey resource.
type AccessKeyArgs struct {
	PgpKey pulumi.StringPtrInput
	Status pulumi.StringPtrInput
	User   pulumi.StringInput
}

func (AccessKeyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*accessKeyArgs)(nil)).Elem()
}

type AccessKeyInput interface {
	pulumi.Input

	ToAccessKeyOutput() AccessKeyOutput
	ToAccessKeyOutputWithContext(ctx context.Context) AccessKeyOutput
}

func (*AccessKey) ElementType() reflect.Type {
	return reflect.TypeOf((**AccessKey)(nil)).Elem()
}

func (i *AccessKey) ToAccessKeyOutput() AccessKeyOutput {
	return i.ToAccessKeyOutputWithContext(context.Background())
}

func (i *AccessKey) ToAccessKeyOutputWithContext(ctx context.Context) AccessKeyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AccessKeyOutput)
}

// AccessKeyArrayInput is an input type that accepts AccessKeyArray and AccessKeyArrayOutput values.
// You can construct a concrete instance of `AccessKeyArrayInput` via:
//
//	AccessKeyArray{ AccessKeyArgs{...} }
type AccessKeyArrayInput interface {
	pulumi.Input

	ToAccessKeyArrayOutput() AccessKeyArrayOutput
	ToAccessKeyArrayOutputWithContext(context.Context) AccessKeyArrayOutput
}

type AccessKeyArray []AccessKeyInput

func (AccessKeyArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*AccessKey)(nil)).Elem()
}

func (i AccessKeyArray) ToAccessKeyArrayOutput() AccessKeyArrayOutput {
	return i.ToAccessKeyArrayOutputWithContext(context.Background())
}

func (i AccessKeyArray) ToAccessKeyArrayOutputWithContext(ctx context.Context) AccessKeyArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AccessKeyArrayOutput)
}

// AccessKeyMapInput is an input type that accepts AccessKeyMap and AccessKeyMapOutput values.
// You can construct a concrete instance of `AccessKeyMapInput` via:
//
//	AccessKeyMap{ "key": AccessKeyArgs{...} }
type AccessKeyMapInput interface {
	pulumi.Input

	ToAccessKeyMapOutput() AccessKeyMapOutput
	ToAccessKeyMapOutputWithContext(context.Context) AccessKeyMapOutput
}

type AccessKeyMap map[string]AccessKeyInput

func (AccessKeyMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*AccessKey)(nil)).Elem()
}

func (i AccessKeyMap) ToAccessKeyMapOutput() AccessKeyMapOutput {
	return i.ToAccessKeyMapOutputWithContext(context.Background())
}

func (i AccessKeyMap) ToAccessKeyMapOutputWithContext(ctx context.Context) AccessKeyMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AccessKeyMapOutput)
}

type AccessKeyOutput struct{ *pulumi.OutputState }

func (AccessKeyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AccessKey)(nil)).Elem()
}

func (o AccessKeyOutput) ToAccessKeyOutput() AccessKeyOutput {
	return o
}

func (o AccessKeyOutput) ToAccessKeyOutputWithContext(ctx context.Context) AccessKeyOutput {
	return o
}

func (o AccessKeyOutput) EncryptedSecret() pulumi.StringOutput {
	return o.ApplyT(func(v *AccessKey) pulumi.StringOutput { return v.EncryptedSecret }).(pulumi.StringOutput)
}

func (o AccessKeyOutput) KeyFingerprint() pulumi.StringOutput {
	return o.ApplyT(func(v *AccessKey) pulumi.StringOutput { return v.KeyFingerprint }).(pulumi.StringOutput)
}

func (o AccessKeyOutput) PgpKey() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *AccessKey) pulumi.StringPtrOutput { return v.PgpKey }).(pulumi.StringPtrOutput)
}

func (o AccessKeyOutput) Secret() pulumi.StringOutput {
	return o.ApplyT(func(v *AccessKey) pulumi.StringOutput { return v.Secret }).(pulumi.StringOutput)
}

func (o AccessKeyOutput) SesSmtpPasswordV4() pulumi.StringOutput {
	return o.ApplyT(func(v *AccessKey) pulumi.StringOutput { return v.SesSmtpPasswordV4 }).(pulumi.StringOutput)
}

func (o AccessKeyOutput) Status() pulumi.StringOutput {
	return o.ApplyT(func(v *AccessKey) pulumi.StringOutput { return v.Status }).(pulumi.StringOutput)
}

func (o AccessKeyOutput) User() pulumi.StringOutput {
	return o.ApplyT(func(v *AccessKey) pulumi.StringOutput { return v.User }).(pulumi.StringOutput)
}

type AccessKeyArrayOutput struct{ *pulumi.OutputState }

func (AccessKeyArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*AccessKey)(nil)).Elem()
}

func (o AccessKeyArrayOutput) ToAccessKeyArrayOutput() AccessKeyArrayOutput {
	return o
}

func (o AccessKeyArrayOutput) ToAccessKeyArrayOutputWithContext(ctx context.Context) AccessKeyArrayOutput {
	return o
}

func (o AccessKeyArrayOutput) Index(i pulumi.IntInput) AccessKeyOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *AccessKey {
		return vs[0].([]*AccessKey)[vs[1].(int)]
	}).(AccessKeyOutput)
}

type AccessKeyMapOutput struct{ *pulumi.OutputState }

func (AccessKeyMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*AccessKey)(nil)).Elem()
}

func (o AccessKeyMapOutput) ToAccessKeyMapOutput() AccessKeyMapOutput {
	return o
}

func (o AccessKeyMapOutput) ToAccessKeyMapOutputWithContext(ctx context.Context) AccessKeyMapOutput {
	return o
}

func (o AccessKeyMapOutput) MapIndex(k pulumi.StringInput) AccessKeyOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *AccessKey {
		return vs[0].(map[string]*AccessKey)[vs[1].(string)]
	}).(AccessKeyOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*AccessKeyInput)(nil)).Elem(), &AccessKey{})
	pulumi.RegisterInputType(reflect.TypeOf((*AccessKeyArrayInput)(nil)).Elem(), AccessKeyArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*AccessKeyMapInput)(nil)).Elem(), AccessKeyMap{})
	pulumi.RegisterOutputType(AccessKeyOutput{})
	pulumi.RegisterOutputType(AccessKeyArrayOutput{})
	pulumi.RegisterOutputType(AccessKeyMapOutput{})
}