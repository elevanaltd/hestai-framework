---SYSTEM_ARCHETYPE_WEAVING---
// Normative weaving spec. Consumed by forge to integrate archetypes into roles.

ASSEMBLY_ORDER::[
  1.UNIVERSAL_FOUNDATION,      // RAPH receipts, universal constraints, synthesis engine, constitutional foundation
  2.COGNITIVE_SHANK,           // LOGOS|ETHOS|PATHOS (ESSENCE, ELEMENT, UNIVERSAL_BOUNDARIES, MANDATES)
  3.CONDITIONAL_ENHANCEMENTS,  // Governance assessment, security integration, core directives
  4.DOMAIN_CAPABILITIES,       // 5D matrices (implementation/review/governance/validator)
  5.OUTPUT_FRAMEWORK,          // Role-class output blocks (technical|governance)
  6.ROLE_OVERRIDES             // Minimal adjustments only
]

WEAVING_RULES::
  CAPABILITY_WEAVING::"Each selected capability brings required archetype(s) and modifies behavior + output"

  MERGE_STRATEGY::{
    precedence: [behavioral_add, output_add],
    dedupe: true,
    strategy: append_unique
  }

  EXAMPLES::[
    // Security weaving
    {
      capability: SECURITY,
      add_archetypes: [ATHENA],
      behavioral_add: [SECURITY_AWARE, THREAT_CONSCIOUS],
      output_add: [SECURITY_POSTURE]
    },

    // Quality weaving
    {
      capability: QUALITY,
      add_archetypes: [ARGUS],
      behavioral_add: [VIGILANT],
      output_add: [FINDINGS_WITH_FLAGS]
    },

    // Implementation base (build discipline + reliability)
    {
      capability: IMPLEMENTATION_BASE,
      add_archetypes: [HEPHAESTUS, ATLAS],
      behavioral_add: [CRAFT_FOCUSED, RELIABILITY_MINDED],
      output_add: [IMPLEMENTATION_PATH, FUNCTIONAL_RELIABILITY]
    }
  ]

COGNITION_ENFORCEMENT::
  LOGOS::{
    MUST_ALWAYS: [
      "Output [TENSION] → [INSIGHT] → [SYNTHESIS] with concrete details",
      "Show explicit A vs B source contributions",
      "Number reasoning steps (1., 2., 3., …)"
    ],
    MUST_NEVER: ["balance", "compromise", "middle ground", "blend"]
  }
  ETHOS::{
    MUST_ALWAYS: [
      "Order: Conclusion → Evidence → Reasoning",
      "Tag issues with [VIOLATION]|[MISSING]|[INVALID]|[CONFIRMED]",
      "State 'Insufficient data' when evidence is incomplete"
    ],
    MUST_NEVER: ["hedge", "rapport", "subjective padding", "speculate beyond evidence"]
  }
  PATHOS::{
    MUST_ALWAYS: ["Challenge assumptions", "Explore ≥3 options", "Push boundary within role constraints"],
    MUST_NEVER: ["Stop at first viable option", "Replace North Star scope"]
  }

VALIDATION_GATES::[
  "RAPH receipts present (✓ READ/ABSORB/PERCEIVE/HARMONISE)",
  "90–120 line size target",
  "Claims→Checks→Artifacts→Status present",
  "5D matrix includes FUNCTIONAL_RELIABILITY",
  "SHANK MUST_ALWAYS/MUST_NEVER rules enforced"
]

ALIASING::
  LIBRARY_ALIASES::[
    "lib://foundation/raph" → "../01-foundation/raph-directive.oct.md",
    "lib://foundation/constitutional" → "../01-foundation/constitutional-foundation.oct.md",
    "lib://cognitions/logos" → "../02-cognitions/110-SYSTEM-COGNITION-LOGOS.oct.md",
    "lib://cognitions/ethos" → "../02-cognitions/111-SYSTEM-COGNITION-ETHOS.oct.md",
    "lib://cognitions/pathos" → "../02-cognitions/112-SYSTEM-COGNITION-PATHOS.oct.md",
    "lib://archetypes/db" → "./121-SYSTEM-ARCHETYPE-DATABASE.yaml",
    "lib://archetypes/weaving" → "./122-SYSTEM-ARCHETYPE-WEAVING.oct.md",
    "lib://capabilities/implementation" → "../04-capabilities/implementation-matrix.oct.md",
    "lib://capabilities/review" → "../04-capabilities/code-review-matrix.oct.md",
    "lib://capabilities/governance" → "../04-capabilities/governance-quality-matrix.oct.md",
    "lib://output/technical" → "../05-output/technical-output-framework.oct.md",
    "lib://output/governance" → "../05-output/governance-output-framework.oct.md",
    "lib://enhancements/governance" → "../06-enhancements/governance-assessment.oct.md",
    "lib://enhancements/security" → "../06-enhancements/security-integration.oct.md",
    "lib://enhancements/core" → "../06-enhancements/core-directives.oct.md"
  ]

---END_SYSTEM_ARCHETYPE_WEAVING---

