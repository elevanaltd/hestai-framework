# Migration Overview

We're migrating from the legacy `hestai-system/config/` structure to the new `hestai-framework/library/` architecture as defined in A-009. This is a **review-and-optimize** migration, not a simple copy-paste operation.

### Source Structure (hestai-system):
```
config/
├── 01-foundation/
├── 02-identity/
├── 03-context/
├── 04-capabilities/
│   ├── skills/
│   └── patterns/
└── 00-activation/standalone/
```

### Target Structure (hestai-framework):
```
library/
├── 01-foundation/
├── 02-identities/
├── 03-contexts/
├── 04-capabilities/
│   ├── skills/
│   └── patterns/
```

---

## Migration Principles

### 1. **Naming Convention Changes**
- **Files**: ALL_CAPS → kebab-case
- **Example**: `LOGOS_SHANK.oct.md` → `logos-shank.oct.md`
- **Semantic Versioning**: Ensure D1_01 format is applied consistently

### 2. **Content Optimization**
- Review each file for outdated content
- Ensure OCTAVE format consistency
- Update internal references to match new naming
- Remove deprecated patterns or legacy assumptions

### 3. **Quality Assurance**
- Validate OCTAVE syntax and semantic compression
- Check for conflicts with two-repository architecture
- Ensure proper documentation and examples

### 4. **Reference Updates**
- Update file paths in internal references
- Ensure cross-component references use new naming
- Validate that skill files match established patterns

---

## Step-by-Step Migration Process

### Phase 1: Foundation (01-foundation/)

**Source Files:**
- `GUIDELINES_UNIVERSAL.oct.md`
- `HESTAI_PRINCIPLES.oct.md`

**Migration Steps:**
1. Read source file content
2. Review for optimization opportunities
3. Apply kebab-case naming: `hestai-principles.oct.md`, `guidelines-universal.oct.md`
4. Update any internal references
5. Save to `hestai-framework/library/01-foundation/`

**Validation:**
- Verify OCTAVE syntax is consistent
- Check that VALIDATION_KEY is preserved
- Ensure no hardcoded paths need updating

### Phase 2: Identities (02-identities/)

**Source Files:**
- `LOGOS_SHANK.oct.md`
- `ETHOS_SHANK.oct.md`
- `PATHOS_SHANK.oct.md`
- `PHAEDRUS_SHANK.oct.md`

**Migration Steps:**
1. Read each SHANK file
2. Review IDENTITY sections for consistency
3. Apply kebab-case naming: `logos-shank.oct.md`, etc.
4. Verify UNIVERSAL_BOUNDARIES are properly formatted
5. Save to `hestai-framework/library/02-identities/`

**Validation:**
- Ensure MUST_ALWAYS and MUST_NEVER sections are clear
- Verify ESSENCE and CORE_GIFT are properly defined
- Check that all SHANKs follow consistent structure

### Phase 3: Contexts (03-contexts/)

**Source Files:**
- `DESIGN_ARM.oct.md` (may need to be created from LOGOS_DESIGN_ARM.oct.md)
- `BUILD_ARM.oct.md` (may need to be created from LOGOS_BUILD_ARM.oct.md)
- `ADMIN_ARM.oct.md`

**Migration Steps:**
1. Review existing ARM files for consolidation opportunities
2. Create unified ARM files if multiple cognition-specific versions exist
3. Apply kebab-case naming: `design-arm.oct.md`, `build-arm.oct.md`, `admin-arm.oct.md`
4. Ensure BEHAVIORAL_CONTRACT sections are consistent
5. Save to `hestai-framework/library/03-contexts/`

**Validation:**
- Verify CONTEXTUAL_DIRECTIVES are clear
- Check COGNITIVE_FLOW patterns are consistent
- Ensure SUCCESS_METRIC definitions are measurable

### Phase 4: Capabilities - Skills (04-capabilities/skills/)

**Source Files (Workflow Skills):**
- `D1_INITIAL_CLARIFICATION.oct.md` → `d1-01-initial-clarification.oct.md`
- `D1_5_FACT_FINDING.oct.md` → `d1-02-fact-finding.oct.md`
- `D2a_IDEAS.oct.md` → `d2-01-ideas.oct.md`
- `D2b_LIMITS.oct.md` → `d2-02-limits.oct.md`
- `D2c_SYNTHESISE.oct.md` → `d2-03-synthesise.oct.md`
- `D3_DESIGN_REFINEMENT.oct.md` → `d3-01-design-refinement.oct.md`
- `B0_QUALITY_GATE.oct.md` → `b0-01-quality-gate.oct.md`
- `B1_IMPLEMENTATION_PLANNING.oct.md` → `b1-01-implementation-planning.oct.md`
- `B2_INCREMENTAL_CONSTRUCTION.oct.md` → `b2-01-incremental-construction.oct.md`
- `B2_5_QUALITY_ASSURANCE.oct.md` → `b2-02-quality-assurance.oct.md`
- `B2_5_CREATIVE_REFINER.oct.md` → `b2-03-creative-refiner.oct.md`
- `B3_FINAL_INTEGRATION.oct.md` → `b3-01-final-integration.oct.md`
- `B4_DELIVERY_AND_HANDOFF.oct.md` → `b4-01-delivery-and-handoff.oct.md`

**Source Files (Universal Skills):**
- All `UNI_*.oct.md` files → `uni-*.oct.md` (kebab-case)
- All `ADM_*.oct.md` files → `adm-*.oct.md` (kebab-case)
- All `ETH_*.oct.md` files → `eth-*.oct.md` (kebab-case)
- All `PAT_*.oct.md` files → `pat-*.oct.md` (kebab-case)

**Migration Steps:**
1. Read each skill file
2. Apply semantic versioning to workflow skills (D1_01 format)
3. Convert to kebab-case naming
4. Review OPERATIONAL_METHODS and BOUNDARIES sections
5. Update any cross-references to other skills
6. Save to `hestai-framework/library/04-capabilities/skills/`

**Validation:**
- Verify ESSENCE and METHODOLOGY sections are clear
- Check that ARCHETYPE references are consistent
- Ensure CAN/CANNOT boundaries are properly defined

### Phase 5: Capabilities - Patterns (04-capabilities/patterns/)

**Source Files:**
- All `UNI_*_PATTERNS.oct.md` files → `uni-*-patterns.oct.md`
- All `ADM_*_PATTERNS.oct.md` files → `adm-*-patterns.oct.md`
- All `ETH_*_PATTERNS.oct.md` files → `eth-*-patterns.oct.md`
- All `PHA_*_PATTERNS.oct.md` files → `pha-*-patterns.oct.md`

**Migration Steps:**
1. Read each pattern file
2. Convert to kebab-case naming
3. Review pattern definitions for clarity and consistency
4. Update any references to other patterns or skills
5. Save to `hestai-framework/library/04-capabilities/patterns/`

**Validation:**
- Verify pattern definitions are actionable
- Check that examples are current and relevant
- Ensure no deprecated patterns are included

---

## Post-Migration Validation

### 1. **Cross-Reference Check**
- Verify all internal file references use new naming
- Check that skill files reference correct patterns
- Ensure ARM files reference appropriate skills

### 2. **Consistency Validation**
- All files use kebab-case naming
- OCTAVE syntax is consistent across all files
- Semantic versioning is properly applied

### 3. **Framework Integrity**
- Test that loading sequence (01→02→03→04) is logical
- Verify no missing dependencies or broken references
- Ensure documentation is complete

### 4. **Architecture Compliance**
- Confirm separation of concerns (framework vs orchestrator)
- Verify no operational state or session data included
- Check that all components are reusable and stateless

---

## Migration Checklist

### Before Starting:
- [ ] hestai-framework/library/ folder structure created
- [ ] CONTRIBUTING.md updated with new conventions
- [ ] All README.md files in place

### During Migration:
- [ ] 01-foundation/ files migrated and validated
- [ ] 02-identities/ files migrated and validated  
- [ ] 03-contexts/ files migrated and validated
- [ ] 04-capabilities/skills/ files migrated and validated
- [ ] 04-capabilities/patterns/ files migrated and validated

### After Migration:
- [ ] Cross-reference validation complete
- [ ] Consistency check passed
- [ ] Framework integrity verified
- [ ] Architecture compliance confirmed
- [ ] Documentation updated

---

## Notes for Activation Sequences

The `00-activation/standalone/` folder contains the gold-tier activation prompts (D1_01-B4_01). These belong in the **hestai-orchestrator** repository as `assembly/protocols/` according to the A-009 architecture. They should NOT be migrated to the framework library.

---

## Success Criteria

Migration is complete when:
1. All components use consistent kebab-case naming
2. OCTAVE format is standardized across all files
3. Cross-references work correctly
4. Framework can be consumed by orchestrator
5. No legacy assumptions or deprecated content remains
6. All documentation is accurate and complete
