```markdown
# Feature Flag Framework

This document outlines the feature flag framework used within the platform.

## Purpose

*   Feature flags (also known as feature toggles) allow us to enable or disable features in production without deploying new code.
*   This enables us to:
    *   Test new features in production with a limited number of users.
    *   Roll out features gradually to reduce risk.
    *   Quickly disable features if they cause problems.
    *   Experiment with different feature implementations.

## Implementation

*   We use the [LaunchDarkly](https://launchdarkly.com/) or [equivalent] feature flag service.
*   Feature flags are defined and managed through the LaunchDarkly dashboard.
*   The SDK is integrated into the application code to evaluate feature flags at runtime.

## Feature Flag Naming Convention

*   Feature flags should be named using a consistent convention: `[area]-[feature]-[variant]`.
    *   `area`: The area of the application the feature affects (e.g., `checkout`, `search`).
    *   `feature`: A short description of the feature (e.g., `new-payment-method`, `improved-ranking`).
    *   `variant`: Optional suffix to indicate a specific variant of the feature (e.g., `a`, `b`).

## Feature Flag Types

*   **Release Flags:** Used to control the release of new features to users.
*   **Experiment Flags:** Used to run A/B tests and measure the impact of different feature implementations.
*   **Operational Flags:** Used to control system behavior in response to operational events (e.g., disabling a feature during a peak load).
*   **Permissioning Flags:** Used to grant or restrict access to features based on user roles or permissions.

## Code Example (Feature Flag Evaluation)

```java
import com.launchdarkly.sdk.LDClient;
import com.launchdarkly.sdk.LDUser;
import com.launchdarkly.sdk.LDValue;

public class MyClass {
    private LDClient ldClient;

    public MyClass(LDClient ldClient) {
        this.ldClient = ldClient;
    }

    public void myMethod(String userId) {
        LDUser user = new LDUser.Builder(userId).build();
        boolean isEnabled = ldClient.boolVariation("my-new-feature", user, false); // "false" is the default value

        if (isEnabled) {
            // Run the new feature code
        } else {
            // Run the old code
        }
    }
}