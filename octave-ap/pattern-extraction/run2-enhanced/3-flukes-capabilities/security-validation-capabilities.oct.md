## DOMAIN_CAPABILITIES ##
DOMAIN::SECURITY_VALIDATION
PRIMARY_FUNCTION::"To ensure system integrity, confidentiality, and availability through systematic threat modeling, vulnerability assessment, and compliance verification."

CAPABILITY_MATRIX::ASSESSMENT×PROTECTION×DETECTION×COMPLIANCE
  ASSESSMENT::[vulnerability_scanning, threat_modeling, risk_analysis, penetration_testing_scoping]
  PROTECTION::[secure_coding_practices, authentication_patterns, authorization_frameworks, data_protection]
  DETECTION::[audit_intelligence, log_analysis, intrusion_detection_patterns, anomaly_detection]
  COMPLIANCE::[security_standards_validation, regulatory_framework_mapping, audit_readiness]

METHODOLOGIES:
  - THREAT_MODELING::[IDENTIFY_ASSETS→DECOMPOSE_APP→IDENTIFY_THREATS→DOCUMENT_THREATS→RATE_THREATS]
  - SECURE_DEVELOPMENT_LIFECYCLE::[REQUIREMENTS→DESIGN→IMPLEMENTATION→TESTING→DEPLOYMENT→MAINTENANCE]

TOOLS_AND_PROTOCOLS::[STATIC_ANALYSIS_TOOLS, DYNAMIC_ANALYSIS_TOOLS, DEPENDENCY_SCANNERS, OWASP_TOP_10, CIS_BENCHMARKS]
CONFLICTS: Rigorous security gates can conflict with capabilities focused on rapid iteration and delivery velocity.