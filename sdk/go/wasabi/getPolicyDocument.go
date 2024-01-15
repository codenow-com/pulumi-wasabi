// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package wasabi

import (
	"context"
	"reflect"

	"github.com/codenow-com/pulumi-wasabi/sdk/go/wasabi/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func GetPolicyDocument(ctx *pulumi.Context, args *GetPolicyDocumentArgs, opts ...pulumi.InvokeOption) (*GetPolicyDocumentResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetPolicyDocumentResult
	err := ctx.Invoke("wasabi:index/getPolicyDocument:getPolicyDocument", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getPolicyDocument.
type GetPolicyDocumentArgs struct {
	OverrideJson *string                      `pulumi:"overrideJson"`
	PolicyId     *string                      `pulumi:"policyId"`
	SourceJson   *string                      `pulumi:"sourceJson"`
	Statements   []GetPolicyDocumentStatement `pulumi:"statements"`
	Version      *string                      `pulumi:"version"`
}

// A collection of values returned by getPolicyDocument.
type GetPolicyDocumentResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id           string                       `pulumi:"id"`
	Json         string                       `pulumi:"json"`
	OverrideJson *string                      `pulumi:"overrideJson"`
	PolicyId     *string                      `pulumi:"policyId"`
	SourceJson   *string                      `pulumi:"sourceJson"`
	Statements   []GetPolicyDocumentStatement `pulumi:"statements"`
	Version      *string                      `pulumi:"version"`
}

func GetPolicyDocumentOutput(ctx *pulumi.Context, args GetPolicyDocumentOutputArgs, opts ...pulumi.InvokeOption) GetPolicyDocumentResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetPolicyDocumentResult, error) {
			args := v.(GetPolicyDocumentArgs)
			r, err := GetPolicyDocument(ctx, &args, opts...)
			var s GetPolicyDocumentResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetPolicyDocumentResultOutput)
}

// A collection of arguments for invoking getPolicyDocument.
type GetPolicyDocumentOutputArgs struct {
	OverrideJson pulumi.StringPtrInput                `pulumi:"overrideJson"`
	PolicyId     pulumi.StringPtrInput                `pulumi:"policyId"`
	SourceJson   pulumi.StringPtrInput                `pulumi:"sourceJson"`
	Statements   GetPolicyDocumentStatementArrayInput `pulumi:"statements"`
	Version      pulumi.StringPtrInput                `pulumi:"version"`
}

func (GetPolicyDocumentOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetPolicyDocumentArgs)(nil)).Elem()
}

// A collection of values returned by getPolicyDocument.
type GetPolicyDocumentResultOutput struct{ *pulumi.OutputState }

func (GetPolicyDocumentResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetPolicyDocumentResult)(nil)).Elem()
}

func (o GetPolicyDocumentResultOutput) ToGetPolicyDocumentResultOutput() GetPolicyDocumentResultOutput {
	return o
}

func (o GetPolicyDocumentResultOutput) ToGetPolicyDocumentResultOutputWithContext(ctx context.Context) GetPolicyDocumentResultOutput {
	return o
}

// The provider-assigned unique ID for this managed resource.
func (o GetPolicyDocumentResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetPolicyDocumentResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o GetPolicyDocumentResultOutput) Json() pulumi.StringOutput {
	return o.ApplyT(func(v GetPolicyDocumentResult) string { return v.Json }).(pulumi.StringOutput)
}

func (o GetPolicyDocumentResultOutput) OverrideJson() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetPolicyDocumentResult) *string { return v.OverrideJson }).(pulumi.StringPtrOutput)
}

func (o GetPolicyDocumentResultOutput) PolicyId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetPolicyDocumentResult) *string { return v.PolicyId }).(pulumi.StringPtrOutput)
}

func (o GetPolicyDocumentResultOutput) SourceJson() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetPolicyDocumentResult) *string { return v.SourceJson }).(pulumi.StringPtrOutput)
}

func (o GetPolicyDocumentResultOutput) Statements() GetPolicyDocumentStatementArrayOutput {
	return o.ApplyT(func(v GetPolicyDocumentResult) []GetPolicyDocumentStatement { return v.Statements }).(GetPolicyDocumentStatementArrayOutput)
}

func (o GetPolicyDocumentResultOutput) Version() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetPolicyDocumentResult) *string { return v.Version }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(GetPolicyDocumentResultOutput{})
}