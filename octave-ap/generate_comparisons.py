#!/usr/bin/env python3
"""Generate full expansions of OCTAVE-AP roles for comparison with originals"""

from pathlib import Path
from typing import Dict, List
import yaml

class SimpleExpander:
    """Simple pattern expander without complex dependencies"""
    
    def __init__(self, patterns_dir: Path):
        self.patterns_dir = patterns_dir
    
    def load_pattern(self, pattern_path: str) -> str:
        """Load a single pattern file"""
        full_path = self.patterns_dir / pattern_path
        if not full_path.exists():
            raise FileNotFoundError(f"Pattern not found: {pattern_path}")
        return full_path.read_text()
    
    def parse_role(self, role_path: Path) -> Dict:
        """Parse role definition to extract metadata and patterns"""
        content = role_path.read_text()
        
        # Extract metadata
        metadata = {}
        if "---" in content:
            parts = content.split("---", 2)
            if len(parts) >= 2:
                metadata = yaml.safe_load(parts[1])
        
        # Extract inherits
        inherits = []
        if "inherits::[" in content:
            start = content.find("inherits::[") + len("inherits::[")
            end = content.find("]", start)
            inherits_str = content[start:end]
            inherits = [p.strip() for p in inherits_str.split(",") if p.strip()]
        
        # Get role content (everything after metadata)
        role_content = ""
        if "## ROLE_METADATA ##" in content:
            role_content = content[content.find("## ROLE_METADATA ##"):]
        
        return {
            "metadata": metadata,
            "inherits": inherits,
            "content": role_content
        }
    
    def expand_role(self, role_def: Dict) -> str:
        """Expand a role by combining all inherited patterns"""
        expanded_parts = []
        
        # Add metadata header
        meta = role_def["metadata"]
        expanded_parts.append("---")
        expanded_parts.append(f"name: {meta.get('name', 'unnamed')}")
        expanded_parts.append(f"model: {meta.get('model', 'claude-opus-4')}")
        expanded_parts.append(f"description: {meta.get('description', 'No description')}")
        expanded_parts.append("---")
        expanded_parts.append("")
        
        # Process universal patterns first
        universal_patterns = []
        cognitive_patterns = []
        enhancement_patterns = []
        capability_patterns = []
        output_patterns = []
        
        # Categorize patterns
        for pattern_path in role_def["inherits"]:
            if "0-sea-universal" in pattern_path:
                universal_patterns.append(pattern_path)
            elif "1-shank-cognitions" in pattern_path:
                cognitive_patterns.append(pattern_path)
            elif "2-arm-enhancements" in pattern_path:
                enhancement_patterns.append(pattern_path)
            elif "3-flukes-capabilities" in pattern_path:
                capability_patterns.append(pattern_path)
            elif "4-output-configs" in pattern_path:
                output_patterns.append(pattern_path)
        
        # Expand in order
        all_patterns = (universal_patterns + cognitive_patterns + 
                       enhancement_patterns + capability_patterns)
        
        for pattern_path in all_patterns:
            try:
                pattern_content = self.load_pattern(pattern_path)
                expanded_parts.append(pattern_content)
                expanded_parts.append("")
            except FileNotFoundError:
                expanded_parts.append(f"## ERROR: Pattern not found: {pattern_path} ##")
                expanded_parts.append("")
        
        # Add role-specific content
        expanded_parts.append(role_def["content"])
        
        # Add output patterns at the end
        for pattern_path in output_patterns:
            try:
                pattern_content = self.load_pattern(pattern_path)
                expanded_parts.append("")
                expanded_parts.append(pattern_content)
            except FileNotFoundError:
                expanded_parts.append(f"## ERROR: Pattern not found: {pattern_path} ##")
        
        return "\n".join(expanded_parts)

def main():
    base_path = Path(__file__).parent
    patterns_dir = base_path / "patterns"
    roles_dir = base_path / "roles"
    output_dir = base_path / "examples" / "expanded-comparisons"
    
    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Roles to expand
    role_names = [
        "code-review-specialist-ap",
        "ideator-ap",
        "implementation-lead-ap",
        "quality-observer-ap",
        "research-analyst-pattern-extractor-ap",
        "technical-architect-ap"
    ]
    
    expander = SimpleExpander(patterns_dir)
    
    print("Generating Full Role Expansions for Comparison")
    print("=" * 60)
    
    for role_name in role_names:
        print(f"\nProcessing: {role_name}")
        role_path = roles_dir / f"{role_name}.oct.md"
        
        try:
            # Parse role
            role_def = expander.parse_role(role_path)
            print(f"  ✓ Parsed role with {len(role_def['inherits'])} patterns")
            
            # Expand role
            expanded = expander.expand_role(role_def)
            lines = len(expanded.splitlines())
            print(f"  ✓ Expanded to {lines} lines")
            
            # Save expanded version
            output_path = output_dir / f"{role_name}-FULL.md"
            output_path.write_text(expanded)
            print(f"  ✓ Saved to {output_path.name}")
            
        except Exception as e:
            print(f"  ✗ Error: {e}")
    
    print("\n" + "=" * 60)
    print("Summary:")
    print(f"Generated {len(role_names)} expanded roles in {output_dir}")
    print("\nNext steps:")
    print("1. Compare expanded versions with originals in:")
    print("   /Volumes/HestAI/hestai-orchestrator/assembly/protocols/finalised-roles/")
    print("2. Look for alignment in structure, capabilities, and behavior")
    print("3. Identify any missing patterns or divergences")

if __name__ == "__main__":
    main()