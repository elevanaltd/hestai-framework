# Contributing to HestAI Framework

## Overview

The HestAI Framework is a library of reusable cognitive components for AI system design. Components follow the SHANK-ARM-FLUKE architecture and are written in OCTAVE format.

## Component Structure

### ROLE (Meta)
- Job description/anchor name (e.g., "Quality Observer", "Ideator")
- Not stored as files - defined at assembly time by orchestrator
- Should have 1-1 mapping with bespoke skills

### SHANK (Cognition)
- Immutable cognitive patterns defining HOW the agent thinks
- Location: `library/02-cognitions/`
- Naming: `{cognition}-shank.oct.md` (e.g., `logos-shank.oct.md`)

### ARM (Context)
- Mission-specific operational context
- Location: `library/03-contexts/`
- Naming: `{phase}-arm.oct.md`

### FLUKE (Capabilities)
- Skills and patterns for specific domains
- Location: `library/04-capabilities/`
- Naming: `{category}-{specific-name}.oct.md`
- Skills should be bespoke-crafted for each role

## OCTAVE Format

All components use OCTAVE v2.0 format. Reference the syntax specification at `/Users/shaunbuswell/dev/octave/specs/octave-syntax.oct.md`.

Key rules:
- Use `KEY::VALUE` for assignment
- Use `KEY:` for nested structures with 2-space indentation
- Use `---name---` and `---end-name---` for document boundaries
- **Naming**: If it's a `.oct.md` file, use kebab-case. Otherwise, use UPPER_SNAKE_CASE.

## Contribution Process

1. **Understand the Architecture**: Review the Odyssean Anchor specification
2. **Follow OCTAVE Syntax**: Ensure proper formatting and validation
3. **Maintain Separation**: Keep cognition (SHANK) separate from capabilities (ARM/FLUKE)
4. **Role-Skill Mapping**: Ensure each role has a corresponding bespoke skill
5. **Test Integration**: Verify components work within the system
6. **Document Changes**: Update relevant specifications and examples

## Quality Standards

- Components must validate against OCTAVE syntax
- Cross-references must be accurate
- **Naming**: `.oct.md` files use kebab-case, all other files use UPPER_SNAKE_CASE
- Content must preserve semantic meaning
- No broken internal references

## Getting Help

- Review existing components for patterns
- Check OCTAVE specification for syntax questions
- Consult Odyssean Anchor guide for architecture questions