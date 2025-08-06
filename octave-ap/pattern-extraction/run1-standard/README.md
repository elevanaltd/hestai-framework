# OCTAVE-AP Extracted Pattern Library (run1-standard)

This library contains reusable patterns extracted from existing HestAI roles. These components can be combined to compose new, specialized AI agents with predictable capabilities.

## Pattern Structure

The library is organized into three main categories, following the OCTAVE-AP (SEA-SHANK-ARM-FLUKES) model:

-   **`2-arm-enhancements/`**: Operational contexts that modify a role's behavior (e.g., phase, seniority).
-   **`3-flukes-capabilities/`**: Domain-specific skills and expertise.
-   **`4-output-configs/`**: Standardized output formats for different task types.

These patterns are designed to be combined with a base cognitive pattern (`1-shank-cognitions/`) and universal patterns (`0-sea-universal/`).

## Extracted Patterns

### 2-arm-enhancements (Operational Contexts)

-   `admin-phase.oct.md`: For roles focused on preservation, organization, and maintenance.
-   `build-phase.oct.md`: For roles focused on implementation, construction, and validation.
-   `design-phase.oct.md`: For roles focused on exploration, ideation, and synthesis.
-   `seniority-enhancement.oct.md`: Adds strategic oversight, mentorship, and advanced synthesis capabilities.
-   `archetype-combinations.oct.md`: Defines common archetype pairings and their emergent behaviors.

### 3-flukes-capabilities (Domain Expertise)

-   `documentation-stewardship.oct.md`: For roles managing documentation ecosystems.
-   `security-expertise.oct.md`: For roles requiring security analysis and threat modeling.
-   `testing-expertise.oct.md`: For roles focused on quality assurance and test strategy.
-   `workspace-architecture.oct.md`: For roles that set up and manage project environments.

### 4-output-configs (Output Formats)

-   `creative-ideation-output.oct.md`: For roles generating novel ideas and possibilities.
-   `strategic-synthesis-output.oct.md`: For roles creating architectural blueprints and strategic plans.
-   `technical-analysis-output.oct.md`: For roles performing code reviews, quality assessments, and technical validation.

## Pattern Combination Examples

New roles can be composed by selecting one pattern from each category.

**Example 1: `Infrastructure Security Auditor`**
```
inherits::[
  // Universal
  "0-sea-universal/raph-processing.oct.md",
  "0-sea-universal/constitutional-foundation.oct.md",
  // Cognition
  "1-shank-cognitions/ethos-validation.oct.md",
  // Enhancements
  "2-arm-enhancements/build-phase.oct.md",
  "2-arm-enhancements/seniority-enhancement.oct.md",
  // Capability
  "3-flukes-capabilities/security-expertise.oct.md",
  // Output
  "4-output-configs/technical-analysis-output.oct.md"
]
```

**Example 2: `Junior API Documentation Writer`**
```
inherits::[
  // Universal
  "0-sea-universal/raph-processing.oct.md",
  // Cognition
  "1-shank-cognitions/logos-synthesis.oct.md",
  // Enhancements
  "2-arm-enhancements/admin-phase.oct.md",
  // Capability
  "3-flukes-capabilities/documentation-stewardship.oct.md",
  // Output
  "4-output-configs/technical-analysis-output.oct.md"
]
```

## Conflict Matrix

Certain patterns are designed for different cognitive approaches and may conflict.

| Pattern A | Conflicts with | Pattern B | Rationale |
|---|---|---|---|
| `design-phase.oct.md` | ↔️ | `build-phase.oct.md` | `DESIGN` is divergent (exploration), while `BUILD` is convergent (execution). Using both creates conflicting priorities. |
| `creative-ideation-output.oct.md` | ↔️ | `technical-analysis-output.oct.md` | Ideation output is generative and open-ended; analysis output is structured and conclusive. |
| `seniority-enhancement.oct.md` | ⚠️ | (No base cognition) | Seniority requires a cognitive foundation (ETHOS/LOGOS/PATHOS) to be effective. It enhances, it doesn't replace. |
| `security-expertise.oct.md` | ⚠️ | `pathos-enhancement.oct.md` | Security (ETHOS-heavy) requires rigorous validation, which can conflict with the free exploration of PATHOS. Use with caution. |