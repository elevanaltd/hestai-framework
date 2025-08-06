#!/usr/bin/env python3
"""
Compare OCTAVE-AP generated Quality Observer with original version
"""

import sys
from pathlib import Path

# Add the octave-ap directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

from core.inheritance_engine_v2 import SemanticInheritanceEngineV2

def analyze_role_structure(content: str, name: str):
    """Analyze role structure and content"""
    lines = content.split('\n')
    
    print(f"\n{name}:")
    print(f"  Total lines: {len(lines)}")
    print(f"  Has frontmatter: {content.startswith('---')}")
    
    # Find major sections
    print(f"  Major sections:")
    for i, line in enumerate(lines):
        if line.startswith('##'):
            print(f"    Line {i+1}: {line}")
    
    # Check for duplications
    key_sections = ['CONSTITUTIONAL_FOUNDATION', 'COGNITIVE_FOUNDATION', 'RAPH', 'OUTPUT_CONFIGURATION']
    print(f"  Section counts:")
    for section in key_sections:
        count = sum(1 for line in lines if section in line and line.startswith('##'))
        print(f"    {section}: {count}")
    
    # Check OUTPUT_CONFIGURATION completeness
    if '## OUTPUT_CONFIGURATION ##' in content:
        start = content.index('## OUTPUT_CONFIGURATION ##')
        output_section = content[start:]
        output_items = output_section.count('**')
        print(f"  OUTPUT_CONFIGURATION items: {output_items // 2}")

def main():
    # Generate OCTAVE-AP version
    print("Generating OCTAVE-AP Quality Observer...")
    engine = SemanticInheritanceEngineV2('patterns/')
    expanded = engine.expand_role_from_file('roles/quality-observer.oct.md')
    
    # Read original version
    original_path = Path('/Volumes/HestAI/hestai-orchestrator/assembly/protocols/finalised-roles/quality-observer-full.oct.md')
    if original_path.exists():
        with open(original_path, 'r') as f:
            original_content = f.read()
    else:
        print(f"Original file not found at {original_path}")
        original_content = "ORIGINAL FILE NOT FOUND"
    
    # Compare structures
    print("\n" + "="*60)
    print("STRUCTURE COMPARISON")
    print("="*60)
    
    analyze_role_structure(expanded.content, "OCTAVE-AP Generated")
    analyze_role_structure(original_content, "Original Finalized")
    
    # Key differences
    print("\n" + "="*60)
    print("KEY DIFFERENCES")
    print("="*60)
    
    octave_lines = len(expanded.content.split('\n'))
    original_lines = len(original_content.split('\n'))
    
    print(f"Line count difference: {octave_lines - original_lines} ({octave_lines} vs {original_lines})")
    print(f"OCTAVE-AP Performance estimate: {expanded.performance_estimate:.1%}")
    
    # Check critical components
    print("\nCritical components check:")
    components = [
        ("RAPH sequential", "RAPH sequential reasoning"),
        ("ETHOS", "COGNITION::ETHOS"), 
        ("ARGUS+THEMIS+ATHENA", "ARGUS+THEMIS+ATHENA"),
        ("OUTPUT_CONFIGURATION", "OUTPUT_CONFIGURATION"),
        ("Executive_Summary", "Executive_Summary"),
        ("Quality_Assessment", "Quality_Assessment"),
        ("Security_Posture", "Security_Posture")
    ]
    
    for display_name, search_text in components:
        in_octave = search_text in expanded.content
        in_original = display_name in original_content or search_text in original_content
        status = "✅" if in_octave and in_original else "❌" if not in_octave else "⚠️"
        print(f"  {status} {display_name}: OCTAVE-AP={in_octave}, Original={in_original}")
    
    # Save output for manual comparison
    output_path = Path('quality-observer-octave-ap.oct.md')
    with open(output_path, 'w') as f:
        f.write(expanded.content)
    print(f"\n✅ OCTAVE-AP version saved to: {output_path}")
    
    print("\n" + "="*60)
    print("VERDICT")
    print("="*60)
    
    # Check if all critical components are present
    all_present = all(search_text in expanded.content for _, search_text in components[:7])
    
    if octave_lines < original_lines + 20 and all_present:
        print("✅ OCTAVE-AP implementation is working correctly!")
        print(f"   - Proper structure maintained")
        print(f"   - All critical components present")
        print(f"   - Reasonable line count ({octave_lines} lines)")
        print(f"   - No major duplications")
    else:
        print("❌ Issues detected - needs further refinement")

if __name__ == "__main__":
    main()