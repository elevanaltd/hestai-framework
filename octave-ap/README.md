# OCTAVE-AP: Pattern-Based Role Composition System

A pragmatic approach to creating AI roles through validated pattern composition.

## What This Is

OCTAVE-AP lets you build AI roles by combining proven patterns rather than writing everything from scratch. Think of it like LEGO blocks - each pattern is a tested component that can be combined with others to create new roles.

## Current Status

- ✅ Basic pattern library structure
- ✅ Simple inheritance engine (v2)
- ✅ Example patterns for testing
- 🚧 Pattern validation in progress
- 🚧 Learning optimal combinations

## Directory Structure

```
octave-ap/
├── core/                   # Core engine code
│   ├── inheritance_engine_v2.py   # Pattern composition engine
│   └── inheritance_engine.py      # Original version (deprecated)
├── patterns/               # Reusable pattern library
│   ├── 0-sea-universal/    # Universal patterns (all roles)
│   ├── 1-shank-cognitions/ # Thinking patterns (ETHOS/LOGOS/PATHOS)
│   ├── 3-flukes-capabilities/ # Domain capabilities
│   └── 4-output-configs/   # Output format patterns
├── roles/                  # Role definitions (minimal)
├── factory/                # Role creation tools
├── examples/               # Example usage and outputs
└── tests/                  # Test scripts

```

## How It Works

1. **Define a minimal role** (30-40 lines) that inherits patterns:
```yaml
---
name: quality-observer
model: claude-opus-4
description: Quality assessment and validation
---

inherits::[
  0-sea-universal/raph-processing.oct.md,
  1-shank-cognitions/ethos-validation.oct.md,
  3-flukes-capabilities/quality-assessment-matrix.oct.md,
  4-output-configs/quality-observer-output.oct.md
]

ARCHETYPES::ARGUS+THEMIS+ATHENA
MISSION::QUALITY_ASSESSMENT+STANDARDS_VALIDATION
```

2. **Engine expands patterns** into full role (100-150 lines)

3. **Test and validate** the generated role works as expected

## Quick Start

### Create a Role

```python
from core.inheritance_engine_v2 import SemanticInheritanceEngineV2

# Initialize engine
engine = SemanticInheritanceEngineV2('patterns/')

# Expand a role from definition
expanded_role = engine.expand_role_from_file('roles/quality-observer.oct.md')

print(f"Generated {expanded_role.line_count} lines")
print(expanded_role.content)
```

### Test Pattern Combinations

```python
from factory.role_factory import RoleFactory

factory = RoleFactory('patterns/')

# Natural language to role
role = factory.create_role("quality observer for web applications")
```

## Current Patterns

### Universal (0-sea-universal/)
- `raph-processing.oct.md` - Sequential processing directive
- `constitutional-foundation.oct.md` - Core governance (+39% performance)
- `anti-patterns.oct.md` - Common pitfalls to avoid
- `quality-gates.oct.md` - Quality standards

### Cognitions (1-shank-cognitions/)
- `ethos-validation.oct.md` - Constraint/validation thinking
- `logos-synthesis.oct.md` - Technical/building thinking
- `pathos-enhancement.oct.md` - Creative/possibility thinking

### Capabilities (3-flukes-capabilities/)
- `quality-assessment-matrix.oct.md` - Quality evaluation framework
- `code-analysis-matrix.oct.md` - Code review capabilities
- `technical-architecture-matrix.oct.md` - System design patterns

## Development Process

We're currently in the learning phase:

1. **Create roles** using pattern combinations
2. **Test** against expectations
3. **Fine-tune** patterns based on what works
4. **Iterate** until combinations produce reliable results

## Examples

See the `examples/` directory for:
- Generated role outputs
- Comparison with hand-written roles
- Pattern combination experiments

## Testing

Run tests with:
```bash
python tests/test_expansion.py
python tests/compare_quality_observer.py
```

## Contributing

We're learning what patterns work best. When testing:
1. Document which combinations work well
2. Note any conflicts between patterns
3. Suggest improvements to pattern content
4. Share successful role definitions

## Next Steps

- [ ] Validate 12 core pattern combinations
- [ ] Build conflict detection matrix
- [ ] Create pattern selection guide
- [ ] Add performance monitoring