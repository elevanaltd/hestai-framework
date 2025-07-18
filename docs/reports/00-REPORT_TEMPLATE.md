# [REPORT_TYPE] Report: [TITLE]

---

## REPORT_METADATA

**Report ID**: REP[XXX]  
**Generated**: [TIMESTAMP]  
**Analyst**: [ROLE/SYSTEM]  
**Status**: [OPEN/IN_PROGRESS/RESOLVED]  
**Priority**: [CRITICAL/HIGH/MEDIUM/LOW]  
**Scope**: [DESCRIPTION OF ANALYSIS SCOPE]  
**Related Reports**: [LIST OF RELATED REPORT IDS]

---

## EXECUTIVE_SUMMARY

[Brief 2-3 sentence overview of key findings and recommendations]

**Key Metrics**:
- **Total Issues**: [NUMBER]
- **Critical**: [NUMBER]  
- **High**: [NUMBER]
- **Medium**: [NUMBER]
- **Low**: [NUMBER]

---

## FINDINGS

### 1. [FINDING_CATEGORY]
**Impact**: [CRITICAL/HIGH/MEDIUM/LOW]  
**Affected Components**: [LIST]

[Detailed analysis of the finding]

### 2. [FINDING_CATEGORY]  
**Impact**: [CRITICAL/HIGH/MEDIUM/LOW]  
**Affected Components**: [LIST]

[Detailed analysis of the finding]

---

## ACTION_ITEMS

### Critical Actions (Immediate)
- [ ] **[PRIORITY]** [DESCRIPTION] (Assigned: [WHO], Due: [WHEN])
- [ ] **[PRIORITY]** [DESCRIPTION] (Assigned: [WHO], Due: [WHEN])

### High Priority Actions
- [ ] **[PRIORITY]** [DESCRIPTION] (Assigned: [WHO], Due: [WHEN])
- [ ] **[PRIORITY]** [DESCRIPTION] (Assigned: [WHO], Due: [WHEN])

### Medium Priority Actions
- [ ] **[PRIORITY]** [DESCRIPTION] (Assigned: [WHO], Due: [WHEN])

### Low Priority Actions
- [ ] **[PRIORITY]** [DESCRIPTION] (Assigned: [WHO], Due: [WHEN])

---

## RESOLUTION_LOG

**[TIMESTAMP]** - Report REP[XXX] created (By: [ANALYST])  
**[TIMESTAMP]** - [ACTION_TAKEN] (By: [WHO])  
**[TIMESTAMP]** - [STATUS_UPDATE] (By: [WHO])  

---

## APPENDICES

### Appendix A: Technical Details
[Detailed technical information, component specifications, OCTAVE analysis, etc.]

### Appendix B: Evidence
[Supporting evidence, file contents, component interactions, etc.]

### Appendix C: References
[Links to related components, patterns, or framework documentation]

---

## VALIDATION

**Validation Key**: [CONFIRMATION_TOKEN]  
**Analysis Confidence**: [LOW/MEDIUM/HIGH/VERY_HIGH]  
**Recommendations Confidence**: [LOW/MEDIUM/HIGH/VERY_HIGH]  

---

## TEMPLATE_USAGE_NOTES

**REPORT_TYPES**: 
- `COMPONENT` - Component quality/structure analysis
- `OCTAVE` - OCTAVE format compliance review  
- `PATTERN` - Pattern effectiveness analysis
- `INTEGRATION` - Component integration testing
- `VALIDATION` - Framework validation review
- `ARCHITECTURE` - Framework architecture review

**STATUS_VALUES**:
- `OPEN` - New report, no action taken
- `IN_PROGRESS` - Actions being implemented
- `RESOLVED` - All critical/high actions completed
- `CLOSED` - Report archived, no further action needed

**PRIORITY_LEVELS**:
- `CRITICAL` - Framework-breaking issues requiring immediate attention
- `HIGH` - Important issues affecting component quality or usability
- `MEDIUM` - Improvements that enhance framework quality
- `LOW` - Minor optimizations or nice-to-have improvements

**ASSIGNMENT_FORMAT**:
- `FRAMEWORK_ARCHITECT` - Framework architecture specialist
- `COMPONENT_AUTHOR` - Component creator/maintainer
- `OCTAVE_SPECIALIST` - OCTAVE format expert
- `PATTERN_DESIGNER` - Pattern design specialist
- `UNASSIGNED` - Awaiting assignment

**REPORT_ID_FORMAT**:
- `REP001` - First report
- `REP002` - Second report
- `REP[XXX]` - Sequential numbering (REP001-REP999)

---

*Report generated using HestAI Framework Report Template v1.0*  
*Template Location: `/Volumes/HestAI/hestai-framework/docs/reports/00-REPORT_TEMPLATE.md`*