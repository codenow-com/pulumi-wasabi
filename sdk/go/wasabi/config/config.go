// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package config

import (
	"github.com/codenow-com/pulumi-wasabi/sdk/go/wasabi/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

var _ = internal.GetEnvOrDefault

// The access key for API operations. You can retrieve this from the 'Security & Credentials' section of the AWS console.
func GetAccessKey(ctx *pulumi.Context) string {
	return config.Get(ctx, "wasabi:accessKey")
}
func GetAllowedAccountIds(ctx *pulumi.Context) string {
	return config.Get(ctx, "wasabi:allowedAccountIds")
}
func GetAssumeRole(ctx *pulumi.Context) string {
	return config.Get(ctx, "wasabi:assumeRole")
}
func GetEndpoints(ctx *pulumi.Context) string {
	return config.Get(ctx, "wasabi:endpoints")
}
func GetForbiddenAccountIds(ctx *pulumi.Context) string {
	return config.Get(ctx, "wasabi:forbiddenAccountIds")
}

// Explicitly allow the provider to perform "insecure" SSL requests. If omitted,default value is `false`
func GetInsecure(ctx *pulumi.Context) bool {
	return config.GetBool(ctx, "wasabi:insecure")
}

// The maximum number of times an AWS API request is being executed. If the API request still fails, an error is thrown.
func GetMaxRetries(ctx *pulumi.Context) int {
	return config.GetInt(ctx, "wasabi:maxRetries")
}

// The profile for API operations. If not set, the default profile created with `aws configure` will be used.
func GetProfile(ctx *pulumi.Context) string {
	return config.Get(ctx, "wasabi:profile")
}

// The region where AWS operations will take place. Examples are us-east-1, us-west-2, etc.
func GetRegion(ctx *pulumi.Context) string {
	return config.Get(ctx, "wasabi:region")
}

// Set this to true to force the request to use path-style addressing, i.e., http://s3.amazonaws.com/BUCKET/KEY. By
// default, the S3 client will use virtual hosted bucket addressing when possible (http://BUCKET.s3.amazonaws.com/KEY).
// Specific to the Amazon S3 service.
func GetS3ForcePathStyle(ctx *pulumi.Context) bool {
	return config.GetBool(ctx, "wasabi:s3ForcePathStyle")
}

// The secret key for API operations. You can retrieve this from the 'Security & Credentials' section of the AWS console.
func GetSecretKey(ctx *pulumi.Context) string {
	return config.Get(ctx, "wasabi:secretKey")
}

// The path to the shared credentials file. If not set this defaults to ~/.aws/credentials.
func GetSharedCredentialsFile(ctx *pulumi.Context) string {
	return config.Get(ctx, "wasabi:sharedCredentialsFile")
}

// Skip the credentials validation via STS API. Used for AWS API implementations that do not have STS
// available/implemented.
func GetSkipCredentialsValidation(ctx *pulumi.Context) bool {
	return config.GetBool(ctx, "wasabi:skipCredentialsValidation")
}
func GetSkipMetadataApiCheck(ctx *pulumi.Context) bool {
	return config.GetBool(ctx, "wasabi:skipMetadataApiCheck")
}

// Skip requesting the account ID. Used for AWS API implementations that do not have IAM/STS API and/or metadata API.
func GetSkipRequestingAccountId(ctx *pulumi.Context) bool {
	return config.GetBool(ctx, "wasabi:skipRequestingAccountId")
}

// session token. A session token is only required if you are using temporary security credentials.
func GetToken(ctx *pulumi.Context) string {
	return config.Get(ctx, "wasabi:token")
}
