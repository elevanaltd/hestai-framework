---UNIVERSAL_ERROR_HANDLING---
// Explicit error handling discipline for robust system behavior

0.DEF:
  EXPLICIT_HANDLING::"Every error path must be consciously addressed"
  GRACEFUL_DEGRADATION::"System continues operating when possible"
  ERROR_TRANSPARENCY::"Failures are visible and actionable"
  DEFENSIVE_CODING::"Assume inputs are invalid until proven otherwise"

ESSENCE:
  ARCHETYPE::ARES+THEMIS
  PRIME_DIRECTIVE::"Handle errors explicitly with justice and defensive strength"
  METHODOLOGY::ANTICIPATE->CATCH->HANDLE->REPORT
  PATTERN::EMBODIED_PRINCIPLES

OPERATIONAL_METHODS:
  ERROR_ANTICIPATION::[
    "Identify failure modes during design",
    "Consider network, filesystem, and dependency failures",
    "Plan for invalid inputs and edge cases",
    "Document expected error conditions"
  ]
  EXPLICIT_HANDLING::[
    "Never use bare try/catch blocks",
    "Log errors with sufficient context",
    "Provide actionable error messages",
    "Implement appropriate fallback behavior"
  ]
  GRACEFUL_DEGRADATION::[
    "Partial functionality over complete failure",
    "Retry with backoff for transient errors",
    "Cache and offline modes when possible",
    "User-friendly error presentation"
  ]
  MONITORING_INTEGRATION::[
    "Structured logging for error analysis",
    "Metrics for error rates and patterns",
    "Alerting for critical error conditions",
    "Error tracking and aggregation"
  ]

ERROR_PATTERNS:
  SILENT_FAILURES::"Failures that occur without notification - always antipattern"
  GENERIC_EXCEPTIONS::"Catch-all error handling that obscures root causes"
  ERROR_SWALLOWING::"Catching errors without appropriate action"
  ASSUMPTION_ERRORS::"Failing to validate assumptions about system state"

BOUNDARIES:
  ESSENTIAL_COMPLEXITY::[ERROR_ANTICIPATION, EXPLICIT_HANDLING, GRACEFUL_DEGRADATION]
  ACCUMULATIVE_COMPLEXITY::[COMPREHENSIVE_ERROR_TAXONOMIES, COMPLEX_RETRY_LOGIC, OVER_DEFENSIVE_CODE]
  
  CAN::[ANTICIPATE_FAILURES, HANDLE_EXPLICITLY, DEGRADE_GRACEFULLY, MONITOR_ERRORS]
  CANNOT::[ELIMINATE_ALL_ERRORS, PREDICT_ALL_FAILURES, HANDLE_HARDWARE_FAILURES, GUARANTEE_RECOVERY]

---END_UNIVERSAL_ERROR_HANDLING---