# Wasabi Resource Provider

The Wasabi Resource Provider lets you manage [Wasabi](https://wasabi.com) resources.

## Installing

This package is available for several languages/platforms:

### Node.js (JavaScript/TypeScript)

To use from JavaScript or TypeScript in Node.js, install using either `npm`:

```bash
npm install @codenow/wasabi
```

or `yarn`:

```bash
yarn add @codenow/wasabi
```

### Python

To use from Python, install using `pip`:

```bash
pip install codenow_wasabi
```

### Go

To use from Go, use `go get` to grab the latest version of the library:

```bash
go get github.com/codenow-com/pulumi-wasabi/sdk/go/...
```

### .NET

To use from .NET, install using `dotnet add package`:

```bash
dotnet add package Codenow.Wasabi
```

## Configuration

The following configuration points are available for the `wasabi` provider:

- `wasabi:apiKey` (environment: `FOO_API_KEY`) - the API key for `wasabi`
- `wasabi:region` (environment: `FOO_REGION`) - the region in which to deploy resources

## Reference

For detailed reference documentation, please visit [the Pulumi registry](https://www.pulumi.com/registry/packages/wasabi/api-docs/).
