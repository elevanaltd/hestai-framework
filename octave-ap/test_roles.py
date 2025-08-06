#!/usr/bin/env python3
"""Test script for validating the 5 newly created roles"""

import os
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.inheritance_engine_v2 import InheritanceEngine
from core.pattern_library import PatternLibrary
from core.semantic_expander import SemanticExpander

def test_role_generation():
    """Test generation of the 5 new roles"""
    
    # Initialize components
    base_path = Path(__file__).parent
    pattern_library = PatternLibrary(base_path / "patterns")
    engine = InheritanceEngine()
    expander = SemanticExpander(pattern_library)
    
    # Test roles
    test_roles = [
        "infrastructure-security-auditor",
        "api-design-reviewer", 
        "knowledge-curator",
        "testing-strategist",
        "creative-solution-architect"
    ]
    
    results = {}
    
    for role_name in test_roles:
        print(f"\n{'='*60}")
        print(f"Testing role: {role_name}")
        print(f"{'='*60}")
        
        role_path = base_path / "roles" / f"{role_name}.oct.md"
        
        try:
            # Parse role definition
            role_def = engine.parse_role(role_path)
            print(f"✓ Parsed role definition")
            print(f"  - Inherits {len(role_def['inherits'])} patterns")
            
            # Expand patterns
            expanded = expander.expand_role(role_def)
            print(f"✓ Expanded role successfully")
            print(f"  - Generated {len(expanded.splitlines())} lines")
            
            # Validate structure
            has_metadata = "## ROLE_METADATA ##" in expanded
            has_specialization = "## SPECIALIZATION_CONFIGURATION ##" in expanded
            has_behavioral = "## BEHAVIORAL_CUSTOMIZATION ##" in expanded
            has_output = "## OUTPUT" in expanded
            
            print(f"✓ Structure validation:")
            print(f"  - Metadata section: {'✓' if has_metadata else '✗'}")
            print(f"  - Specialization: {'✓' if has_specialization else '✗'}")
            print(f"  - Behavioral: {'✓' if has_behavioral else '✗'}")
            print(f"  - Output config: {'✓' if has_output else '✗'}")
            
            # Check for duplications
            sections = expanded.split("##")
            section_counts = {}
            for section in sections:
                if section.strip():
                    header = section.split('\n')[0].strip()
                    section_counts[header] = section_counts.get(header, 0) + 1
            
            duplicates = [k for k, v in section_counts.items() if v > 1]
            if duplicates:
                print(f"✗ Found duplicate sections: {duplicates}")
            else:
                print(f"✓ No duplicate sections found")
            
            # Save expanded role
            output_path = base_path / "examples" / "expanded" / f"{role_name}-expanded.md"
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(expanded)
            print(f"✓ Saved expanded role to examples/expanded/")
            
            results[role_name] = {
                "success": True,
                "lines": len(expanded.splitlines()),
                "patterns": len(role_def['inherits']),
                "has_all_sections": all([has_metadata, has_specialization, has_behavioral, has_output]),
                "no_duplicates": len(duplicates) == 0
            }
            
        except Exception as e:
            print(f"✗ Error generating role: {e}")
            results[role_name] = {
                "success": False,
                "error": str(e)
            }
    
    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    
    for role, result in results.items():
        if result["success"]:
            status = "✓" if result["has_all_sections"] and result["no_duplicates"] else "⚠"
            print(f"{status} {role}: {result['patterns']} patterns → {result['lines']} lines")
        else:
            print(f"✗ {role}: {result['error']}")
    
    # Pattern usage analysis
    print(f"\n{'='*60}")
    print("PATTERN USAGE ANALYSIS")
    print(f"{'='*60}")
    
    pattern_usage = {}
    for role_name in test_roles:
        role_path = base_path / "roles" / f"{role_name}.oct.md"
        try:
            role_def = engine.parse_role(role_path)
            for pattern in role_def['inherits']:
                pattern_usage[pattern] = pattern_usage.get(pattern, 0) + 1
        except:
            pass
    
    # Sort by usage
    sorted_patterns = sorted(pattern_usage.items(), key=lambda x: x[1], reverse=True)
    
    print("\nMost used patterns:")
    for pattern, count in sorted_patterns[:10]:
        print(f"  {count}x {pattern}")
    
    print("\nUnique patterns (used only once):")
    unique = [p for p, c in sorted_patterns if c == 1]
    for pattern in unique:
        print(f"  - {pattern}")

if __name__ == "__main__":
    test_role_generation()