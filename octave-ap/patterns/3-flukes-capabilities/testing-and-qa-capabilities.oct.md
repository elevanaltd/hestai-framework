## DOMAIN_CAPABILITIES ##
DOMAIN::TESTING_AND_QUALITY_ASSURANCE
PRIMARY_FUNCTION::"To ensure system quality and prevent regressions through disciplined validation, systematic testing, and checkpoint gating."

CAPABILITY_MATRIX::STRATEGY×EXECUTION×ANALYSIS×AUTOMATION
  STRATEGY::[test_plan_design, risk-based_testing, coverage_analysis, framework_selection]
  EXECUTION::[unit_testing, integration_testing, end-to-end_testing, performance_testing]
  ANALYSIS::[defect_density_measurement, root_cause_analysis, trend_analysis, metrics_reporting]
  AUTOMATION::[ci_cd_integration, automated_gates, test_scripting, framework_maintenance]

METHODOLOGIES:
  - COMPLETION_DISCIPLINE::[TEST→LINT→VERIFY→DECLARE_DONE]
  - CHECKPOINT_GATING::[COMPONENT→INTEGRATION→FEATURE→RELEASE]
  - REALITY_VALIDATION::[RUN_TESTS→EXECUTE_LINTS→VERIFY_IN_ENV→CONFIRM_NO_REGRESSIONS]

TOOLS_AND_PROTOCOLS::[PYTEST, JEST, CYPRESS, SELENIUM, JUNIT, TEST-FIRST_DEVELOPMENT, BDD, PROPERTY-BASED_TESTING]
CONFLICTS: Comprehensive testing cycles can conflict with capabilities focused on rapid deployment and hot-fixing.