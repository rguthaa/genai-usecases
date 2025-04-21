```markdown
# API Versioning Strategy

This document outlines the API versioning strategy for the platform.

## Versioning Scheme

*   We use semantic versioning (SemVer) for our APIs (MAJOR.MINOR.PATCH).
    *   MAJOR: Incompatible API changes.
    *   MINOR: New functionality added in a backward-compatible manner.
    *   PATCH: Bug fixes or security patches that do not change the API.

## Versioning Method

*   We use URI versioning: the API version is included in the URL path (e.g., `/api/v1/users`, `/api/v2/products`).

## Deprecation Policy

*   Deprecated APIs will be announced at least 6 months prior to removal.
*   A clear migration path will be provided for users of deprecated APIs.
*   Deprecated APIs will continue to be supported until the announced removal date.
*   A `Deprecation` header will be included in the response for deprecated APIs, indicating the API version and the recommended replacement.

## Compatibility

*   We strive to maintain backward compatibility whenever possible.
*   New features and enhancements are typically added as new endpoints or optional parameters to existing endpoints.
*   When breaking changes are necessary, we will release a new major version of the API.

## Code Example (API Versioning)

```java
@RestController
@RequestMapping("/api/v1/users")
public class UserControllerV1 {
    // ...
}

@RestController
@RequestMapping("/api/v2/users")
public class UserControllerV2 {
    // ...
}