// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package wasabi

import (
	"context"
	"reflect"

	"github.com/codenow-com/pulumi-wasabi/sdk/go/wasabi/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func LookupAccountAlias(ctx *pulumi.Context, opts ...pulumi.InvokeOption) (*LookupAccountAliasResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupAccountAliasResult
	err := ctx.Invoke("wasabi:index/getAccountAlias:getAccountAlias", nil, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of values returned by getAccountAlias.
type LookupAccountAliasResult struct {
	AccountAlias string `pulumi:"accountAlias"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
}

func LookupAccountAliasOutput(ctx *pulumi.Context, opts ...pulumi.InvokeOption) LookupAccountAliasResultOutput {
	return pulumi.ToOutput(0).ApplyT(func(int) (LookupAccountAliasResult, error) {
		r, err := LookupAccountAlias(ctx, opts...)
		var s LookupAccountAliasResult
		if r != nil {
			s = *r
		}
		return s, err
	}).(LookupAccountAliasResultOutput)
}

// A collection of values returned by getAccountAlias.
type LookupAccountAliasResultOutput struct{ *pulumi.OutputState }

func (LookupAccountAliasResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAccountAliasResult)(nil)).Elem()
}

func (o LookupAccountAliasResultOutput) ToLookupAccountAliasResultOutput() LookupAccountAliasResultOutput {
	return o
}

func (o LookupAccountAliasResultOutput) ToLookupAccountAliasResultOutputWithContext(ctx context.Context) LookupAccountAliasResultOutput {
	return o
}

func (o LookupAccountAliasResultOutput) AccountAlias() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAccountAliasResult) string { return v.AccountAlias }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupAccountAliasResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAccountAliasResult) string { return v.Id }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupAccountAliasResultOutput{})
}
