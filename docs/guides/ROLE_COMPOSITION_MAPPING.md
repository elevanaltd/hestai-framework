# Role Composition Mapping: ROLE + SHANK-ARM-FLUKE Architecture

## Architecture Formula
```
ROLE = SHANK + ARM + SKILL + PATTERNS
```

Where:
- **ROLE** = Job description/anchor name (e.g., "Quality Observer")
- **SHANK** = Cognitive pattern (ETHOS, LOGOS, PATHOS)
- **ARM** = Operational context (DESIGN, BUILD, ADMIN)
- **SKILL** = Bespoke role-specific capability
- **PATTERNS** = Supporting wisdom patterns

---

## DESIGN Phase Roles

### D1_01: IDEA_CLARIFIER
- **SHANK**: `pathos-shank.oct.md` (Vision-focused exploration)
- **ARM**: `design-arm.oct.md` (Conceptual transformation)
- **SKILL**: `d1-01-initial-clarification.oct.md`
- **PATTERNS**: `universal-foundation-patterns.oct.md`

### D1_02: RESEARCH_ANALYST  
- **SHANK**: `ethos-shank.oct.md` (Validation-focused research)
- **ARM**: `design-arm.oct.md` (Conceptual transformation)
- **SKILL**: `d1-02-fact-finding.oct.md`
- **PATTERNS**: `universal-validation-patterns.oct.md`

### D2_01: IDEATOR
- **SHANK**: `pathos-shank.oct.md` (Vision-focused exploration)
- **ARM**: `design-arm.oct.md` (Conceptual transformation)
- **SKILL**: `d2-01-ideas.oct.md`
- **PATTERNS**: `universal-foundation-patterns.oct.md`

### D2_02: VALIDATOR
- **SHANK**: `ethos-shank.oct.md` (Constraint-focused validation)
- **ARM**: `design-arm.oct.md` (Conceptual transformation)
- **SKILL**: `d2-02-limits.oct.md`
- **PATTERNS**: `universal-validation-patterns.oct.md`

### D2_03: SYNTHESIZER
- **SHANK**: `logos-shank.oct.md` (Synthesis-focused breakthrough)
- **ARM**: `design-arm.oct.md` (Conceptual transformation)
- **SKILL**: `d2-03-synthesis.oct.md`
- **PATTERNS**: `universal-synthesis-patterns.oct.md`

### D3_01: DESIGN_ARCHITECT
- **SHANK**: `logos-shank.oct.md` (Refinement-focused synthesis)
- **ARM**: `design-arm.oct.md` (Conceptual transformation)
- **SKILL**: `d3-01-design-refinement.oct.md`
- **PATTERNS**: `universal-foundation-patterns.oct.md`, `universal-synthesis-patterns.oct.md`

---

## BUILD Phase Roles

### B0_01: CRITICAL_SENIOR_ENGINEER
- **SHANK**: `logos-shank.oct.md` (Synthesis-focused validation)
- **ARM**: `build-arm.oct.md` (Implementation transformation)
- **SKILL**: `b0-01-quality-gate.oct.md`
- **PATTERNS**: `universal-validation-patterns.oct.md`, `ethos-security-patterns.oct.md`

### B1_01: TASK_DECOMPOSER
- **SHANK**: `logos-shank.oct.md` (Synthesis-focused planning)
- **ARM**: `build-arm.oct.md` (Implementation transformation)
- **SKILL**: `b1-01-implementation-planning.oct.md`
- **PATTERNS**: `universal-foundation-patterns.oct.md`

### B2_01: IMPLEMENTATION_LEAD
- **SHANK**: `logos-shank.oct.md` (Synthesis-focused building)
- **ARM**: `build-arm.oct.md` (Implementation transformation)
- **SKILL**: `b2-01-incremental-construction.oct.md`
- **PATTERNS**: `universal-integration-patterns.oct.md`, `universal-version-control-patterns.oct.md`

### B2_02: QUALITY_OBSERVER
- **SHANK**: `ethos-shank.oct.md` (Validation-focused quality control)
- **ARM**: `build-arm.oct.md` (Implementation transformation)
- **SKILL**: `b2-02-quality-assurance.oct.md`
- **PATTERNS**: `admin-testing-patterns.oct.md`, `ethos-security-patterns.oct.md`, `universal-validation-patterns.oct.md`

### B2_03: CREATIVE_REFINER
- **SHANK**: `pathos-shank.oct.md` (Vision-focused optimization)
- **ARM**: `build-arm.oct.md` (Implementation transformation)
- **SKILL**: `b2-03-creative-refinement.oct.md`
- **PATTERNS**: `universal-foundation-patterns.oct.md`

### B3_01: COMPLETION_ARCHITECT
- **SHANK**: `logos-shank.oct.md` (Integration-focused synthesis)
- **ARM**: `build-arm.oct.md` (Implementation transformation)
- **SKILL**: `b3-01-final-integration.oct.md`
- **PATTERNS**: `universal-integration-patterns.oct.md`, `universal-synthesis-patterns.oct.md`

### B4_01: SOLUTION_STEWARD
- **SHANK**: `logos-shank.oct.md` (Knowledge synthesis for handoff)
- **ARM**: `build-arm.oct.md` (Implementation transformation)
- **SKILL**: `b4-01-delivery-and-handoff.oct.md`
- **PATTERNS**: `universal-foundation-patterns.oct.md`, `universal-version-control-patterns.oct.md`

---

## Architecture Summary

**SHANK Distribution:**
- `pathos-shank.oct.md`: 4 roles (D1_01, D2_01, B2_03 + exploration focus)
- `ethos-shank.oct.md`: 3 roles (D1_02, D2_02, B2_02 + validation focus)  
- `logos-shank.oct.md`: 6 roles (D2_03, D3_01, B0_01, B1_01, B2_01, B3_01, B4_01 + synthesis focus)

**ARM Distribution:**
- `design-arm.oct.md`: 6 roles (D1_01 through D3_01)
- `build-arm.oct.md`: 7 roles (B0_01 through B4_01)

**Skills Required:**
- 13 immutable skill files (one per role with 1-1 mapping)

**Patterns Actually Used:**
- `universal-foundation-patterns.oct.md` (Used by D1_01, D2_01, B1_01, B2_03, B4_01)
- `universal-validation-patterns.oct.md` (Used by D1_02, D2_02, B0_01, B2_02)
- `universal-synthesis-patterns.oct.md` (Used by D2_03, D3_01, B3_01)
- `universal-integration-patterns.oct.md` (Used by B2_01, B3_01)
- `universal-version-control-patterns.oct.md` (Used by B2_01, B4_01)
- `admin-testing-patterns.oct.md` (Used by B2_02)
- `ethos-security-patterns.oct.md` (Used by B0_01, B2_02)

**Total**: 7 patterns serving 13 roles (optimized from original 22 patterns)

## Usage Example

To create a "Quality Observer" role:

```yaml
ROLE: "Quality Observer"
SHANK: library/02-cognitions/ethos-shank.oct.md
ARM: library/03-contexts/build-arm.oct.md
SKILL: library/04-capabilities/skills/b2-02-quality-assurance.oct.md
PATTERNS: 
  - library/04-capabilities/patterns/admin-testing-patterns.oct.md
  - library/04-capabilities/patterns/ethos-security-patterns.oct.md
  - library/04-capabilities/patterns/universal-validation-patterns.oct.md
```

This modular architecture enables any role to be composed dynamically while maintaining consistent cognitive patterns and behavioral standards.