#!/usr/bin/env python3
"""Simple validation of the 5 new role definitions"""

from pathlib import Path
import yaml

def validate_roles():
    """Validate role structure and pattern references"""
    
    base_path = Path(__file__).parent
    roles_dir = base_path / "roles"
    patterns_dir = base_path / "patterns"
    
    test_roles = [
        "infrastructure-security-auditor",
        "api-design-reviewer", 
        "knowledge-curator",
        "testing-strategist",
        "creative-solution-architect"
    ]
    
    print("ROLE VALIDATION REPORT")
    print("=" * 80)
    
    for role_name in test_roles:
        print(f"\n{role_name}:")
        print("-" * len(role_name))
        
        role_path = roles_dir / f"{role_name}.oct.md"
        
        if not role_path.exists():
            print(f"  ✗ Role file not found!")
            continue
        
        # Read role file
        content = role_path.read_text()
        
        # Extract metadata
        if "---" in content:
            parts = content.split("---", 2)
            if len(parts) >= 2:
                try:
                    metadata = yaml.safe_load(parts[1])
                    print(f"  ✓ Name: {metadata.get('name', 'NOT SET')}")
                    print(f"  ✓ Model: {metadata.get('model', 'NOT SET')}")
                    print(f"  ✓ Description: {metadata.get('description', 'NOT SET')[:60]}...")
                except:
                    print(f"  ✗ Failed to parse metadata")
        
        # Extract inherits
        if "inherits::[" in content:
            inherits_start = content.find("inherits::[") + len("inherits::[")
            inherits_end = content.find("]", inherits_start)
            inherits_str = content[inherits_start:inherits_end]
            
            patterns = [p.strip() for p in inherits_str.split(",") if p.strip()]
            print(f"  ✓ Inherits {len(patterns)} patterns:")
            
            # Validate each pattern exists
            missing = []
            for pattern in patterns:
                pattern_path = patterns_dir / pattern
                if pattern_path.exists():
                    print(f"    ✓ {pattern}")
                else:
                    print(f"    ✗ {pattern} - FILE NOT FOUND!")
                    missing.append(pattern)
            
            if missing:
                print(f"  ⚠ Missing {len(missing)} pattern files")
        
        # Check key sections
        sections = {
            "ROLE_METADATA": "## ROLE_METADATA ##" in content,
            "SPECIALIZATION_CONFIGURATION": "## SPECIALIZATION_CONFIGURATION ##" in content,
            "BEHAVIORAL_CUSTOMIZATION": "## BEHAVIORAL_CUSTOMIZATION ##" in content
        }
        
        print(f"  ✓ Sections present:")
        for section, present in sections.items():
            print(f"    {'✓' if present else '✗'} {section}")
        
        # Extract key configurations
        if "ARCHETYPES::" in content:
            arch_line = [line for line in content.split('\n') if line.startswith("ARCHETYPES::")][0]
            print(f"  ✓ {arch_line}")
        
        if "MISSION::" in content:
            mission_line = [line for line in content.split('\n') if line.startswith("MISSION::")][0]
            print(f"  ✓ {mission_line}")
    
    print("\n" + "=" * 80)
    print("PATTERN USAGE SUMMARY")
    print("=" * 80)
    
    # Count pattern usage across all roles
    pattern_usage = {}
    for role_name in test_roles:
        role_path = roles_dir / f"{role_name}.oct.md"
        if role_path.exists():
            content = role_path.read_text()
            if "inherits::[" in content:
                inherits_start = content.find("inherits::[") + len("inherits::[")
                inherits_end = content.find("]", inherits_start)
                inherits_str = content[inherits_start:inherits_end]
                patterns = [p.strip() for p in inherits_str.split(",") if p.strip()]
                
                for pattern in patterns:
                    category = pattern.split('/')[0] if '/' in pattern else 'uncategorized'
                    if category not in pattern_usage:
                        pattern_usage[category] = []
                    pattern_usage[category].append(pattern)
    
    for category in sorted(pattern_usage.keys()):
        patterns = pattern_usage[category]
        unique_patterns = list(set(patterns))
        print(f"\n{category}: {len(unique_patterns)} unique patterns, {len(patterns)} total uses")
        for pattern in sorted(unique_patterns):
            count = patterns.count(pattern)
            print(f"  {count}x {pattern}")

if __name__ == "__main__":
    validate_roles()