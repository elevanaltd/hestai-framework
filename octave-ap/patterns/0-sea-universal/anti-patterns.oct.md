ANTI_PATTERN_PREVENTION::[
  HELPFUL_OVERREACH::{TRIGGER:creating_multiple_files, PREVENTION:PAUSE→ASK→LIST→WAIT→IMPLEMENT, SCOPE:file_creation},
  SCOPE_CREEP::{TRIGGER:adding_unrequested_features, PREVENTION:validate_against_original_scope, SCOPE:feature_additions},
  CONTEXT_DESTRUCTION::{TRIGGER:deleting_history_comments, PREVENTION:preserve_context_git_handles_versions, SCOPE:version_control},
  ASSUMPTION_OVER_REALITY::{TRIGGER:ignoring_codebase_patterns, PREVENTION:codebase>documentation>training_data, SCOPE:implementation_decisions},
  PREMATURE_OPTIMIZATION::{TRIGGER:optimizing_without_metrics, PREVENTION:measure_first_optimize_second, SCOPE:performance_tuning},
  ARCHITECTURE_EROSION::{TRIGGER:bypassing_established_patterns, PREVENTION:maintain_architectural_consistency, SCOPE:design_integrity},
  TECHNICAL_DEBT_ACCUMULATION::{TRIGGER:quick_fixes_over_proper_solutions, PREVENTION:address_root_causes, SCOPE:code_quality}
]