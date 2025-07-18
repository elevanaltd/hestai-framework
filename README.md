# HestAI Framework

**WHAT**: Reusable cognitive components (SHANK, ARM, FLUKE files)  
**NOT**: How to use them (that's in hestai-orchestrator)

## Repository Architecture

### ROLE + SHANK-ARM-FLUKE Model
- **ROLE** (Meta): Job description/anchor name ("Quality Observer", "Ideator")
- **SHANK** (Cognition): Core thinking patterns (logos, pathos, ethos)
- **ARM** (Context): Mission context (design, build, admin)  
- **FLUKE** (Capability): Skills and patterns (1-1 role-skill mapping)

## What Goes Where

### This Repository (hestai-framework)
- ✅ Component library files (.oct.md)
- ✅ OCTAVE format specification
- ✅ Component validation tools
- ✅ LICENSE and basic docs

### Other Repository (hestai-orchestrator)  
- ✅ How to load/use components
- ✅ Activation prompts (*-gold.md)
- ✅ Workflow execution engine
- ✅ User interface and examples

## Structure

```
library/
├── 01-foundation/     # Core principles
├── 02-cognitions/     # SHANK files
├── 03-contexts/       # ARM files
└── 04-capabilities/   # FLUKE files
    ├── skills/
    └── patterns/
docs/
├── reports/           # Framework analysis reports (MANDATORY template usage)
└── guides/            # Documentation and usage guides
```

## Usage

This framework is consumed by `hestai-orchestrator`. Components are combined to create AI agents:

1. **ROLE** defines the job/anchor name (e.g., "Quality Observer")
2. **SHANK** provides the thinking pattern (e.g., ETHOS for validation)
3. **ARM** sets the operational context (e.g., BUILD for implementation)
4. **FLUKE** loads bespoke skills crafted for that specific role

Each role should have a corresponding 1-1 skill mapping for precision.

## Reporting Framework Issues

**MANDATORY TEMPLATE USAGE**: All framework reports MUST use the standardized template at `docs/reports/00-REPORT_TEMPLATE.md`. 

See `docs/reports/README.md` for complete reporting guidelines. Reports without proper template formatting will be rejected.