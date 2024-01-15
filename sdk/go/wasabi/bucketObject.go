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

type BucketObject struct {
	pulumi.CustomResourceState

	Acl                pulumi.StringPtrOutput `pulumi:"acl"`
	Bucket             pulumi.StringOutput    `pulumi:"bucket"`
	CacheControl       pulumi.StringPtrOutput `pulumi:"cacheControl"`
	Content            pulumi.StringPtrOutput `pulumi:"content"`
	ContentBase64      pulumi.StringPtrOutput `pulumi:"contentBase64"`
	ContentDisposition pulumi.StringPtrOutput `pulumi:"contentDisposition"`
	ContentEncoding    pulumi.StringPtrOutput `pulumi:"contentEncoding"`
	ContentLanguage    pulumi.StringPtrOutput `pulumi:"contentLanguage"`
	ContentType        pulumi.StringOutput    `pulumi:"contentType"`
	Etag               pulumi.StringOutput    `pulumi:"etag"`
	ForceDestroy       pulumi.BoolPtrOutput   `pulumi:"forceDestroy"`
	Key                pulumi.StringOutput    `pulumi:"key"`
	Metadata           pulumi.StringMapOutput `pulumi:"metadata"`
	Source             pulumi.StringPtrOutput `pulumi:"source"`
	StorageClass       pulumi.StringOutput    `pulumi:"storageClass"`
	VersionId          pulumi.StringOutput    `pulumi:"versionId"`
}

// NewBucketObject registers a new resource with the given unique name, arguments, and options.
func NewBucketObject(ctx *pulumi.Context,
	name string, args *BucketObjectArgs, opts ...pulumi.ResourceOption) (*BucketObject, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Bucket == nil {
		return nil, errors.New("invalid value for required argument 'Bucket'")
	}
	if args.Key == nil {
		return nil, errors.New("invalid value for required argument 'Key'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource BucketObject
	err := ctx.RegisterResource("wasabi:index/bucketObject:BucketObject", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetBucketObject gets an existing BucketObject resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetBucketObject(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *BucketObjectState, opts ...pulumi.ResourceOption) (*BucketObject, error) {
	var resource BucketObject
	err := ctx.ReadResource("wasabi:index/bucketObject:BucketObject", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering BucketObject resources.
type bucketObjectState struct {
	Acl                *string           `pulumi:"acl"`
	Bucket             *string           `pulumi:"bucket"`
	CacheControl       *string           `pulumi:"cacheControl"`
	Content            *string           `pulumi:"content"`
	ContentBase64      *string           `pulumi:"contentBase64"`
	ContentDisposition *string           `pulumi:"contentDisposition"`
	ContentEncoding    *string           `pulumi:"contentEncoding"`
	ContentLanguage    *string           `pulumi:"contentLanguage"`
	ContentType        *string           `pulumi:"contentType"`
	Etag               *string           `pulumi:"etag"`
	ForceDestroy       *bool             `pulumi:"forceDestroy"`
	Key                *string           `pulumi:"key"`
	Metadata           map[string]string `pulumi:"metadata"`
	Source             *string           `pulumi:"source"`
	StorageClass       *string           `pulumi:"storageClass"`
	VersionId          *string           `pulumi:"versionId"`
}

type BucketObjectState struct {
	Acl                pulumi.StringPtrInput
	Bucket             pulumi.StringPtrInput
	CacheControl       pulumi.StringPtrInput
	Content            pulumi.StringPtrInput
	ContentBase64      pulumi.StringPtrInput
	ContentDisposition pulumi.StringPtrInput
	ContentEncoding    pulumi.StringPtrInput
	ContentLanguage    pulumi.StringPtrInput
	ContentType        pulumi.StringPtrInput
	Etag               pulumi.StringPtrInput
	ForceDestroy       pulumi.BoolPtrInput
	Key                pulumi.StringPtrInput
	Metadata           pulumi.StringMapInput
	Source             pulumi.StringPtrInput
	StorageClass       pulumi.StringPtrInput
	VersionId          pulumi.StringPtrInput
}

func (BucketObjectState) ElementType() reflect.Type {
	return reflect.TypeOf((*bucketObjectState)(nil)).Elem()
}

type bucketObjectArgs struct {
	Acl                *string           `pulumi:"acl"`
	Bucket             string            `pulumi:"bucket"`
	CacheControl       *string           `pulumi:"cacheControl"`
	Content            *string           `pulumi:"content"`
	ContentBase64      *string           `pulumi:"contentBase64"`
	ContentDisposition *string           `pulumi:"contentDisposition"`
	ContentEncoding    *string           `pulumi:"contentEncoding"`
	ContentLanguage    *string           `pulumi:"contentLanguage"`
	ContentType        *string           `pulumi:"contentType"`
	Etag               *string           `pulumi:"etag"`
	ForceDestroy       *bool             `pulumi:"forceDestroy"`
	Key                string            `pulumi:"key"`
	Metadata           map[string]string `pulumi:"metadata"`
	Source             *string           `pulumi:"source"`
	StorageClass       *string           `pulumi:"storageClass"`
}

// The set of arguments for constructing a BucketObject resource.
type BucketObjectArgs struct {
	Acl                pulumi.StringPtrInput
	Bucket             pulumi.StringInput
	CacheControl       pulumi.StringPtrInput
	Content            pulumi.StringPtrInput
	ContentBase64      pulumi.StringPtrInput
	ContentDisposition pulumi.StringPtrInput
	ContentEncoding    pulumi.StringPtrInput
	ContentLanguage    pulumi.StringPtrInput
	ContentType        pulumi.StringPtrInput
	Etag               pulumi.StringPtrInput
	ForceDestroy       pulumi.BoolPtrInput
	Key                pulumi.StringInput
	Metadata           pulumi.StringMapInput
	Source             pulumi.StringPtrInput
	StorageClass       pulumi.StringPtrInput
}

func (BucketObjectArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*bucketObjectArgs)(nil)).Elem()
}

type BucketObjectInput interface {
	pulumi.Input

	ToBucketObjectOutput() BucketObjectOutput
	ToBucketObjectOutputWithContext(ctx context.Context) BucketObjectOutput
}

func (*BucketObject) ElementType() reflect.Type {
	return reflect.TypeOf((**BucketObject)(nil)).Elem()
}

func (i *BucketObject) ToBucketObjectOutput() BucketObjectOutput {
	return i.ToBucketObjectOutputWithContext(context.Background())
}

func (i *BucketObject) ToBucketObjectOutputWithContext(ctx context.Context) BucketObjectOutput {
	return pulumi.ToOutputWithContext(ctx, i).(BucketObjectOutput)
}

// BucketObjectArrayInput is an input type that accepts BucketObjectArray and BucketObjectArrayOutput values.
// You can construct a concrete instance of `BucketObjectArrayInput` via:
//
//	BucketObjectArray{ BucketObjectArgs{...} }
type BucketObjectArrayInput interface {
	pulumi.Input

	ToBucketObjectArrayOutput() BucketObjectArrayOutput
	ToBucketObjectArrayOutputWithContext(context.Context) BucketObjectArrayOutput
}

type BucketObjectArray []BucketObjectInput

func (BucketObjectArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*BucketObject)(nil)).Elem()
}

func (i BucketObjectArray) ToBucketObjectArrayOutput() BucketObjectArrayOutput {
	return i.ToBucketObjectArrayOutputWithContext(context.Background())
}

func (i BucketObjectArray) ToBucketObjectArrayOutputWithContext(ctx context.Context) BucketObjectArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(BucketObjectArrayOutput)
}

// BucketObjectMapInput is an input type that accepts BucketObjectMap and BucketObjectMapOutput values.
// You can construct a concrete instance of `BucketObjectMapInput` via:
//
//	BucketObjectMap{ "key": BucketObjectArgs{...} }
type BucketObjectMapInput interface {
	pulumi.Input

	ToBucketObjectMapOutput() BucketObjectMapOutput
	ToBucketObjectMapOutputWithContext(context.Context) BucketObjectMapOutput
}

type BucketObjectMap map[string]BucketObjectInput

func (BucketObjectMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*BucketObject)(nil)).Elem()
}

func (i BucketObjectMap) ToBucketObjectMapOutput() BucketObjectMapOutput {
	return i.ToBucketObjectMapOutputWithContext(context.Background())
}

func (i BucketObjectMap) ToBucketObjectMapOutputWithContext(ctx context.Context) BucketObjectMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(BucketObjectMapOutput)
}

type BucketObjectOutput struct{ *pulumi.OutputState }

func (BucketObjectOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**BucketObject)(nil)).Elem()
}

func (o BucketObjectOutput) ToBucketObjectOutput() BucketObjectOutput {
	return o
}

func (o BucketObjectOutput) ToBucketObjectOutputWithContext(ctx context.Context) BucketObjectOutput {
	return o
}

func (o BucketObjectOutput) Acl() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *BucketObject) pulumi.StringPtrOutput { return v.Acl }).(pulumi.StringPtrOutput)
}

func (o BucketObjectOutput) Bucket() pulumi.StringOutput {
	return o.ApplyT(func(v *BucketObject) pulumi.StringOutput { return v.Bucket }).(pulumi.StringOutput)
}

func (o BucketObjectOutput) CacheControl() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *BucketObject) pulumi.StringPtrOutput { return v.CacheControl }).(pulumi.StringPtrOutput)
}

func (o BucketObjectOutput) Content() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *BucketObject) pulumi.StringPtrOutput { return v.Content }).(pulumi.StringPtrOutput)
}

func (o BucketObjectOutput) ContentBase64() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *BucketObject) pulumi.StringPtrOutput { return v.ContentBase64 }).(pulumi.StringPtrOutput)
}

func (o BucketObjectOutput) ContentDisposition() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *BucketObject) pulumi.StringPtrOutput { return v.ContentDisposition }).(pulumi.StringPtrOutput)
}

func (o BucketObjectOutput) ContentEncoding() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *BucketObject) pulumi.StringPtrOutput { return v.ContentEncoding }).(pulumi.StringPtrOutput)
}

func (o BucketObjectOutput) ContentLanguage() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *BucketObject) pulumi.StringPtrOutput { return v.ContentLanguage }).(pulumi.StringPtrOutput)
}

func (o BucketObjectOutput) ContentType() pulumi.StringOutput {
	return o.ApplyT(func(v *BucketObject) pulumi.StringOutput { return v.ContentType }).(pulumi.StringOutput)
}

func (o BucketObjectOutput) Etag() pulumi.StringOutput {
	return o.ApplyT(func(v *BucketObject) pulumi.StringOutput { return v.Etag }).(pulumi.StringOutput)
}

func (o BucketObjectOutput) ForceDestroy() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *BucketObject) pulumi.BoolPtrOutput { return v.ForceDestroy }).(pulumi.BoolPtrOutput)
}

func (o BucketObjectOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v *BucketObject) pulumi.StringOutput { return v.Key }).(pulumi.StringOutput)
}

func (o BucketObjectOutput) Metadata() pulumi.StringMapOutput {
	return o.ApplyT(func(v *BucketObject) pulumi.StringMapOutput { return v.Metadata }).(pulumi.StringMapOutput)
}

func (o BucketObjectOutput) Source() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *BucketObject) pulumi.StringPtrOutput { return v.Source }).(pulumi.StringPtrOutput)
}

func (o BucketObjectOutput) StorageClass() pulumi.StringOutput {
	return o.ApplyT(func(v *BucketObject) pulumi.StringOutput { return v.StorageClass }).(pulumi.StringOutput)
}

func (o BucketObjectOutput) VersionId() pulumi.StringOutput {
	return o.ApplyT(func(v *BucketObject) pulumi.StringOutput { return v.VersionId }).(pulumi.StringOutput)
}

type BucketObjectArrayOutput struct{ *pulumi.OutputState }

func (BucketObjectArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*BucketObject)(nil)).Elem()
}

func (o BucketObjectArrayOutput) ToBucketObjectArrayOutput() BucketObjectArrayOutput {
	return o
}

func (o BucketObjectArrayOutput) ToBucketObjectArrayOutputWithContext(ctx context.Context) BucketObjectArrayOutput {
	return o
}

func (o BucketObjectArrayOutput) Index(i pulumi.IntInput) BucketObjectOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *BucketObject {
		return vs[0].([]*BucketObject)[vs[1].(int)]
	}).(BucketObjectOutput)
}

type BucketObjectMapOutput struct{ *pulumi.OutputState }

func (BucketObjectMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*BucketObject)(nil)).Elem()
}

func (o BucketObjectMapOutput) ToBucketObjectMapOutput() BucketObjectMapOutput {
	return o
}

func (o BucketObjectMapOutput) ToBucketObjectMapOutputWithContext(ctx context.Context) BucketObjectMapOutput {
	return o
}

func (o BucketObjectMapOutput) MapIndex(k pulumi.StringInput) BucketObjectOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *BucketObject {
		return vs[0].(map[string]*BucketObject)[vs[1].(string)]
	}).(BucketObjectOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*BucketObjectInput)(nil)).Elem(), &BucketObject{})
	pulumi.RegisterInputType(reflect.TypeOf((*BucketObjectArrayInput)(nil)).Elem(), BucketObjectArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*BucketObjectMapInput)(nil)).Elem(), BucketObjectMap{})
	pulumi.RegisterOutputType(BucketObjectOutput{})
	pulumi.RegisterOutputType(BucketObjectArrayOutput{})
	pulumi.RegisterOutputType(BucketObjectMapOutput{})
}