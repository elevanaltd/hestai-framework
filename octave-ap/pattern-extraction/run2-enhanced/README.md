# OCTAVE-AP Extracted Pattern Library (run2-enhanced)

**Objective**: This library contains reusable, modular patterns extracted from an analysis of over 50 finalized HestAI roles and protocols. The goal is to provide a robust component set for composing new, high-performance AI roles using the OCTAVE-AP semantic inheritance engine.

This extraction was performed by the `research-analyst-pattern-extractor` role, following a systematic methodology to ensure reusability, modularity, and orthogonality.

## Extracted Patterns

### 1. Operational Patterns (`2-arm-enhancements/`)
These patterns modify a role's behavior based on operational context, such as the project phase or required seniority.

-   `admin-phase.oct.md`: Modifiers for roles operating in an administrative context (preservation, organization, maintenance).
-   `build-phase.oct.md`: Modifiers for roles in a build/implementation context (execution, validation, delivery).
-   `design-phase.oct.md`: Modifiers for roles in a design context (exploration, synthesis, innovation).
-   `seniority-technical-leadership.oct.md`: Adds behaviors for senior roles (strategic oversight, mentorship, decision authority).
-   `archetype-athena-wisdom.oct.md`: Infuses a role with Athena's strategic wisdom, clarity, and validation focus.
-   `archetype-hephaestus-craft.oct.md`: Infuses a role with Hephaestus's focus on master craftsmanship and technical excellence.
-   `archetype-prometheus-innovation.oct.md`: Infuses a role with Promethean foresight, innovation, and a drive to challenge constraints.

### 2. Domain Capabilities (`3-flukes-capabilities/`)
These patterns provide domain-specific knowledge, tools, and methodologies.

-   `knowledge-management-capabilities.oct.md`: Skills for information architecture, preservation, retrieval, and synthesis.
-   `security-validation-capabilities.oct.md`: Expertise in vulnerability assessment, threat modeling, and secure coding practices.
-   `system-architecture-capabilities.oct.md`: Skills for system design, pattern consistency, scalability, and technical decision-making.
-   `testing-and-qa-capabilities.oct.md`: Expertise in test strategy, quality gates, automation, and coverage analysis.

### 3. Output Configurations (`4-output-configs/`)
These patterns define the structure and format of a role's response.

-   `comprehensive-assessment-output.oct.md`: For detailed, multi-faceted reports (e.g., quality, security, risk).
-   `creative-synthesis-output.oct.md`: For presenting creative ideas, vision enhancements, and innovative concepts.
-   `strategic-consultation-output.oct.md`: For high-level analysis, strategic recommendations, and architectural roadmaps.
-   `technical-review-output.oct.md`: A structured format for code reviews, including critical issues, recommendations, and positive feedback.

## Composition Example & Conflict Analysis

Patterns can be combined to create new, specialized roles.

**Example Role: `System Architecture Security Auditor`**
```
inherits::[
  // Universal Foundation
  "0-sea-universal/raph-processing.oct.md",
  "0-sea-universal/constitutional-foundation.oct.md",

  // Cognitive Pattern
  "1-shank-cognitions/ethos-validation.oct.md",

  // Operational Patterns (Enhancements)
  "2-arm-enhancements/build-phase.oct.md",
  "2-arm-enhancements/seniority-technical-leadership.oct.md",
  "2-arm-enhancements/archetype-athena-wisdom.oct.md",

  // Domain Capabilities
  "3-flukes-capabilities/system-architecture-capabilities.oct.md",
  "3-flukes-capabilities/security-validation-capabilities.oct.md",

  // Output Configuration
  "4-output-configs/comprehensive-assessment-output.oct.md"
]
```

### Conflict & Tension
Combining patterns creates productive tension, which is resolved by the role's core cognition.
-   **Tension**: `archetype-prometheus-innovation` (push boundaries) vs. `security-validation-capabilities` (enforce constraints).
-   **Resolution**: A LOGOS-based role would synthesize a novel, secure architecture. An ETHOS-based role would validate the security of an innovative design.

This library provides the building blocks for this compositional approach to AI role design.