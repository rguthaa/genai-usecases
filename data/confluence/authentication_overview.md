```markdown
# Authentication Overview

This document outlines the authentication mechanisms employed within the platform.

## Authentication Methods

*   **Password-Based Authentication:** Utilizes standard username/password credentials. Password hashing implemented using bcrypt with a salt factor of 12. Password complexity requirements enforced (minimum 8 characters, one uppercase, one lowercase, one number, one special character).

*   **Multi-Factor Authentication (MFA):** Supports Time-based One-Time Password (TOTP) via Google Authenticator or similar. MFA is optional but strongly encouraged for privileged accounts. Recovery codes are generated and stored securely upon MFA enablement.

*   **OAuth 2.0:** Supports OAuth 2.0 authorization for third-party applications. Implements the Authorization Code Grant flow. Access tokens have a short lifespan (1 hour) and are refreshed using refresh tokens. Scopes are defined granularly to limit access to specific resources. Refresh tokens expire after 30 days of inactivity.

*   **API Key Authentication:** Used for programmatic access by authorized services. API keys are associated with specific permissions and are rotated periodically. API keys are stored securely and never exposed in client-side code.

## Session Management

Sessions are managed using HTTP-only cookies with the 'Secure' attribute set. Session timeout is set to 30 minutes of inactivity. Sessions are invalidated upon logout.

## Error Handling

Authentication failures are logged with detailed information (IP address, timestamp, user agent) for auditing purposes. Rate limiting is applied to authentication endpoints to prevent brute-force attacks.

## Code Example (Password Hashing)

```java
// Example using BCrypt
String password = "user_password";
String hashedPassword = BCrypt.hashpw(password, BCrypt.gensalt(12));