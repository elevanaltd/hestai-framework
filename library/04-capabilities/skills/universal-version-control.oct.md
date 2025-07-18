---UNIVERSAL_VERSION_CONTROL---
// Repository management capabilities for disciplined version control, implementing foundational patterns.

ESSENCE:
  ARCHETYPE::CHRONOS+HERMES
  PRIME_DIRECTIVE::"Manage project history with discipline, clarity, and safety by implementing established versioning patterns."
  METHODOLOGY::BRANCH->COMMIT->PUSH->PULL_REQUEST->MERGE
  IMPLEMENTS_PATTERN::EMBODIED_PRINCIPLES

IMPLEMENTED_PATTERNS:
  // This skill is the direct implementation of the wisdom formerly in universal-version-control-patterns.
  STABILITY_PROMISE:
    TRUTH::"Stability commitment transcends edit frequency."
    TENSION::STABILITY _VERSUS_ EVOLUTION->MANAGED_CHANGE
  LIFECYCLE_MANAGEMENT:
    TRUTH::"Document lifecycle determines versioning behavior."
    STATES::[DRAFT, STABLE, DEPRECATED]
  SEMANTIC_PROGRESSION:
    TRUTH::"Semantic versioning communicates change impact."
    CHANGE_TYPES::[PATCH, MINOR, MAJOR]
  CHANGE_DOCUMENTATION:
    TRUTH::"Context prevents arbitrary version inflation."
    TENSION::ARBITRARY_VERSIONING _VERSUS_ DOCUMENTED_RATIONALE->MEANINGFUL_VERSIONS

OPERATIONAL_METHODS:
  // Actionable methods derived from the implemented patterns.
  GIT_WISDOM:
    // Implements: EMPIRICAL_DISCIPLINE
    FLOW::[HISTORY->UNDERSTANDING->MODIFICATION]  // Investigate before acting
    INVESTIGATION_PATTERNS::[
      "git log --oneline -10 before modifying",
      "git grep for related code discovery",
      "git blame to understand feature evolution",
      "git diff --name-only to scope changes"
    ]
  BRANCH_OPERATIONS:
    // Implements: LIFECYCLE_MANAGEMENT
    FLOW::[CREATE->SWITCH->MERGE->PROTECT->CLEANUP]
  COMMIT_STANDARDS:
    // Implements: SEMANTIC_PROGRESSION + CHANGE_DOCUMENTATION
    PRINCIPLES::[ATOMICITY->DESCRIPTION->CONVENTION->CLARITY]
  PR_WORKFLOWS:
    // Implements: STABILITY_PROMISE
    FLOW::[CREATE->REVIEW->RESOLVE_CONFLICTS->SQUASH->REBASE]
  SAFETY_PROTOCOLS:
    // Implements: All patterns
    CHECKS::[BACKUP->REVIEW->DESCRIBE->TEST->NEVER_FORCE_MAIN]

BOUNDARIES:
  ESSENTIAL_COMPLEXITY::[BRANCH_MANAGEMENT, COMMIT_DISCIPLINE, SAFETY_PROTOCOLS]
  ACCUMULATIVE_COMPLEXITY::[DETAILED_WORKFLOWS, COMPREHENSIVE_AUDITING, SPECIFIC_NAMING_CONVENTIONS]
  
  CAN::[MANAGE_REPOSITORIES, CREATE_BRANCHES, HANDLE_VERSION_CONTROL, IMPLEMENT_WORKFLOWS]
  CANNOT::[ACCESS_CREDENTIALS, OVERRIDE_PERMISSIONS, DELETE_CRITICAL_BRANCHES, BYPASS_SECURITY]

---END_UNIVERSAL_VERSION_CONTROL---