# Example: Assembling a Quality Observer Role

## Request
"I need a quality observer for code assessment"

## Component Selection
1. `universal/frontmatter.oct` (with role-specific values)
2. `universal/raph-directive.oct` 
3. `cognitions/ethos.oct` (with ARGUS+THEMIS+ATHENA)
4. `universal/constitutional.oct` (governance role)
5. `domains/quality-assessment.oct`
6. `universal/anti-patterns.oct`

## Assembly Process

The system would:
1. Load each component file
2. Replace placeholders ({{ROLE_NAME}}, {{GOVERNANCE_ARCHETYPES}})
3. Concatenate in order
4. Validate total lines (should be ~112 lines)

## Result
A complete role prompt identical to CURRENT-QUALITY-OBSERVER.md

## Key Point
All components are assembled inline - no file references or inheritance markers appear in the final output. The AI receives one complete, self-contained prompt.