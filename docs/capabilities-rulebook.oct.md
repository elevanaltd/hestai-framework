===CAPABILITIES_RULEBOOK===
// Stewarded by HERMES, Validated by ETHOS
// This is the single source of truth for creating HestAI capability files.
// Updated for hestai-framework library structure and kebab-case naming.

META:
  NAME::CAPABILITIES_RULEBOOK
  TYPE::STANDARD_DOCUMENT
  VERSION::"v3.1"
  PURPOSE::"A canonical, synthesized rulebook for HestAI Skill, Pattern, and Guideline authoring using sequential append format."
  REFERENCES::["/library/01-foundation/guidelines-universal.oct.md"]

0.DEF:
  // Operators
  ASSIGN::"::"
  COMMENT::"//"
  PROGRESS::"->"
  SYNTHESIS::"+"
  TENSION::"_VERSUS_"

---

## SECTION 0: SEQUENTIAL APPEND FORMAT OVERVIEW

The HestAI system uses a **sequential append format** to eliminate redundant headers and metadata when files are processed together during role activation. This format significantly reduces token overhead while maintaining clear parsing boundaries.

0.1_FORMAT_RATIONALE:
  PROBLEM::REDUNDANT_STRUCTURE
  EVIDENCE::"Each META block consumed ~250 tokens across 32+ files = 8,000+ wasted tokens"
  SOLUTION::SEQUENTIAL_APPEND_FORMAT
  BENEFIT::"70% reduction in structural overhead"

0.2_FORMAT_RULES:
  FOUNDATION_FILES::"Use full ===NAME=== format (HESTAI_PRINCIPLES, GUIDELINES_UNIVERSAL)"
  CAPABILITY_FILES::"Use sequential ---NAME--- format"
  PROCESSING_ORDER::"Foundation → Identity → Context → Capabilities"
  CONCATENATION::"Files are logically appended during activation sequence"

0.3_MIGRATION_IMPACT:
  DEPRECATED::"META blocks with NAME, TYPE, VERSION, COMPATIBILITY, PURPOSE fields"
  PRESERVED::"All operational content, patterns, and functionality"
  ENHANCED::"Cleaner file structure, reduced cognitive load, faster processing"

---

## SECTION 1: UNIVERSAL REQUIREMENTS (All Capability Types)

1.1_FILE_STRUCTURE:
  HEADER_FORMAT::"---NAME_IN_CAPS---"
  FOOTER_FORMAT::"---END_NAME_IN_CAPS---"
  RULE:MUST::"Header must be the first non-comment line."
  RULE:MUST::"Footer must be the last line."
  RULE:MUST::"Header and Footer name MUST exactly match the capability name."
  RULE:MUST::"Only foundation files (HESTAI_PRINCIPLES, GUIDELINES_UNIVERSAL) use full ===NAME=== format."

1.2_FILENAME_CONVENTION:
  SIMPLE_RULE::"If it's a .oct.md file, use kebab-case. Otherwise, use UPPER_SNAKE_CASE."
  EXAMPLES:
    FRAMEWORK_COMPONENTS::"kebab-case.oct.md" // logos-shank.oct.md, universal-patterns.oct.md
    EVERYTHING_ELSE::"UPPER_SNAKE_CASE.ext" // README.md, CONTRIBUTING.md, LICENSE
  HEADERS::"Always use UPPER_SNAKE_CASE (e.g., ---MY_SKILL---) for parsing consistency."
  RATIONALE::"Single decision point based on file extension eliminates confusion."

1.3_NAMING_CONVENTION:
  SKILLS::"The name should be concise and avoid redundant suffixes like '_SKILL'. Universality is defined by `COMPATIBILITY::ANY_ROLE`, not the filename."
  PATTERNS::"If a single pattern, use its name. If a collection, a `_PATTERNS` suffix is acceptable."
  GUIDELINES::"The name MUST start with `GUIDELINES_` followed by the context (e.g., `GUIDELINES_BUILD_PHASE`)."
  MIGRATION_NOTE::"Framework components (.oct.md) use kebab-case. Documentation files use UPPER_SNAKE_CASE."

1.4_METADATA:
  SECTION_NAME::META
  RULE:DEPRECATED::"META blocks are removed in sequential append format."
  REPLACEMENT::"Essential metadata converted to comments below header."
  RATIONALE::"Eliminates redundant structure when files are processed sequentially."

1.5_COMPATIBILITY_TRACKING:
  RULE:OPTIONAL::"Compatibility information may be preserved in comments if needed for specific use cases."
  RULE:MUST::"Role-specific capabilities should be clearly indicated in the filename or comment."
  RATIONALE::"Sequential loading eliminates need for explicit compatibility metadata."

---

## SECTION 2: CAPABILITY TEMPLATES

### 2.1 SKILL TEMPLATE
// Skills define *how* a role performs an action.

  REQUIRED_SECTIONS::[ESSENCE, OPERATIONAL_METHODS, BOUNDARIES]
  OPTIONAL_SECTIONS::[0.DEF]
  
  HEADER_COMMENT::"// Brief description of skill purpose and type"
  
  ESSENCE:
    PURPOSE::"Defines the core identity and archetypal nature of the skill."
    EXAMPLE_KEYS::[ARCHETYPE, PRIME_DIRECTIVE, METHODOLOGY]

  OPERATIONAL_METHODS:
    PURPOSE::"The 'how' of the skill, defined with semantic precision. Can contain nested subsections for clarity."

  BOUNDARIES:
    PURPOSE::"The non-negotiable operational limits."
    REQUIRED_SUBSECTIONS::[CAN, CANNOT]
    FORMAT::"List of strings."

### 2.2 DECLARATIVE SKILL TEMPLATE
// A special skill type that defines constraints and anti-patterns.

  REQUIRED_SECTIONS::[ESSENCE, NEGATIVE_CONSTRAINTS, ANTI_PATTERNS]
  
  HEADER_COMMENT::"// Brief description of declarative constraints"
    
  ESSENCE:
    PURPOSE::"Defines the core identity and purpose of the declarative rules."

  NEGATIVE_CONSTRAINTS:
    PURPOSE::"Explicit 'do not' rules for pre-response validation."
    
  ANTI_PATTERNS:
    PURPOSE::"Defines behavioral patterns to avoid, with symptoms and corrections."

### 2.3 PATTERN TEMPLATE (Single Pattern)
// Patterns capture universal wisdom and relationships between forces.

  REQUIRED_SECTIONS::[ARCHETYPAL_FOUNDATION, BEHAVIORAL_MANIFESTATIONS, RELATIONSHIPS]

  HEADER_COMMENT::"// Brief description of pattern domain and scope"

  ARCHETYPAL_FOUNDATION:
    PURPOSE::"The core mythological forces at play."
    EXAMPLE_KEYS::[PRIMARY_FORCES, CORE_TENSION]

  BEHAVIORAL_MANIFESTATIONS:
    PURPOSE::"The pattern's expression in the system."
    EXAMPLE_KEYS::[ESSENCE, ARCHETYPAL_TRUTH, POSITIVE_BEHAVIORS]

  RELATIONSHIPS:
    PURPOSE::"How this pattern interacts with the system's network of ideas."
    EXAMPLE_KEYS::[REINFORCES, CONFLICTS_WITH, ENABLES]

### 2.4 PATTERN COLLECTION TEMPLATE
// A file containing multiple related patterns.

  REQUIRED_SECTIONS::[PATTERN_DEFINITIONS, RELATIONSHIPS]
  OPTIONAL_SECTIONS::[0.DEF]

  HEADER_COMMENT::"// Brief description of pattern collection theme"

  PATTERN_DEFINITIONS:
    PURPOSE::"The main section containing all pattern definitions, often grouped by sub-category."

  RELATIONSHIPS:
    PURPOSE::"How the collection as a whole interacts with the system."

### 2.5 GUIDELINE TEMPLATE
// Guidelines provide clear, non-negotiable operational laws.

  REQUIRED_SECTIONS::[PRINCIPLES, ANTI_PATTERNS, PATTERN_REFERENCES]

  HEADER_COMMENT::"// Brief description of guideline domain and authority"

  PRINCIPLES:
    PURPOSE::"The core rules of this guideline."
    STRUCTURE::"PRINCIPLE_NAME: RULE::\"...\" RATIONALE::\"...\""

  ANTI_PATTERNS:
    PURPOSE::"What to avoid, defined with archetypal clarity."
    STRUCTURE::"ANTI_PATTERN_NAME: SYMPTOM::\"...\" CONSEQUENCE::\"...\" ARCHETYPE::\"...\""

  PATTERN_REFERENCES:
    PURPOSE::"Connects this guideline to the broader pattern network."

---

## SECTION 3: VALIDATION CHECKLIST

// To be used by HERMES and ETHOS when validating a capability file.

3.1_FILE_STRUCTURE:
  - [ ] Header uses ---NAME--- format (unless foundation file).
  - [ ] Footer uses ---END_NAME--- format.
  - [ ] Header and Footer names match filename base.
  - [ ] All required sections for the capability type are present.

3.2_SYNTAX:
  - [ ] All assignments use `::` with no surrounding spaces.
  - [ ] All lists are correctly formatted (no trailing commas).
  - [ ] Indentation is consistently 2 spaces.

3.3_STRUCTURE:
  - [ ] No META blocks present (sequential append format).
  - [ ] Essential information captured in header comments.
  - [ ] Content structure matches capability type requirements.

===END_CAPABILITIES_RULEBOOK===