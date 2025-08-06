# OCTAVE-AP Components Library

This directory contains modular components for assembling OCTAVE role prompts.

## Purpose

These components are assembled server-side to create complete 90-150 line role prompts. Each component is designed to be combined inline with others - no inheritance or external references in the final output.

## Structure

```
/components/
  /universal/         # Components used across all roles
  /cognitions/        # Thinking patterns (ETHOS, LOGOS, PATHOS)
  /domains/           # Domain-specific capabilities and outputs
  /archetypes/        # Mythological archetype combinations
```

## Key Principles

1. **Modularity**: Each component is self-contained
2. **Simplicity**: No complex inheritance or references
3. **Assembly**: Components are concatenated inline
4. **Size**: Final prompts are always 90-150 lines

## Usage

Components are assembled by the OCTAVE-AP system based on natural language requests. The assembly process is defined in `/sessions/2025-08-03-OA-ROLE-LOADING/artifacts/OCTAVE-AP-COMPONENT-ASSEMBLY-SPEC.md`.

## Migration from Library

This simplified component approach replaces the complex inheritance model in `/library/`. The key differences:

- **Library**: Complex file references and inheritance
- **Components**: Simple inline assembly

Both are preserved during the transition period.