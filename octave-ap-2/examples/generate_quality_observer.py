#!/usr/bin/env python3
"""
Generate Quality Observer Role using OCTAVE-AP-2 Matrix Loading
Demonstrates complete role generation with job-specific capabilities
"""

import sys
from pathlib import Path

# Add core module to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'core'))

from matrix_loader import MatrixCapabilityLoader

def generate_quality_observer_role():
    """Generate complete quality observer role using Matrix loading"""
    
    print("=" * 70)
    print("GENERATING QUALITY OBSERVER ROLE - OCTAVE-AP-2 MATRIX LOADING")
    print("=" * 70)
    
    # Initialize Matrix loader
    base_path = Path(__file__).parent.parent
    loader = MatrixCapabilityLoader(str(base_path))
    
    try:
        # Load quality observer specialist using Matrix paradigm
        print("🔄 Loading quality-observer specialist...")
        specialist = loader.load_specialist("quality-observer")
        
        print("✅ Quality Observer Specialist Generated Successfully!")
        print(f"   📊 Cognition: {specialist.cognition}")
        print(f"   🏛️ Archetypes: {specialist.archetypes}")
        print(f"   📏 Size: {specialist.line_count} lines")
        print(f"   🎯 Coherence: {specialist.coherence_score:.2f}")
        
        # Save the generated role
        output_path = Path(__file__).parent / "quality-observer-matrix-generated.oct.md"
        
        with open(output_path, 'w') as f:
            f.write(specialist.content)
        
        print(f"💾 Role saved to: {output_path}")
        
        # Display role specifications
        print(f"\n📋 ROLE SPECIFICATIONS:")
        print(f"   • Comprehensive quality assessment capabilities")
        print(f"   • Standards validation and compliance evaluation")
        print(f"   • Integrated security evaluation framework")
        print(f"   • Multi-stakeholder reporting structure")
        print(f"   • Evidence-based assessment methodology")
        
        # Display Matrix loading advantages
        print(f"\n⚡ MATRIX LOADING ADVANTAGES:")
        print(f"   ✅ Complete job specification in single load")
        print(f"   ✅ Perfect ETHOS cognition for validation work")
        print(f"   ✅ ATHENA+ARGUS+THEMIS archetypes for comprehensive oversight")
        print(f"   ✅ Integrated output format for multi-stakeholder reporting")
        print(f"   ✅ Evidence-based methodology aligned with validation cognition")
        
        print(f"\n🔍 CAPABILITY HIGHLIGHTS:")
        capability_module = loader.load_capability_module("quality-observer")
        print(f"   • Required Cognition: {capability_module.required_cognition}")
        print(f"   • Archetype Count: {len(capability_module.required_archetypes)}")
        print(f"   • Quality Assessment Matrix: 5 dimensions (Standards, Compliance, Security, Performance, Maintainability)")
        print(f"   • Multi-Stakeholder Framework: Executive, Technical, Compliance, Security, Operations")
        print(f"   • Evidence-Based Methodology: 5-stage validation process")
        
        return specialist
        
    except Exception as e:
        print(f"❌ Error generating quality observer: {e}")
        return None

def demonstrate_role_preview():
    """Show preview of generated role content"""
    
    role_path = Path(__file__).parent / "quality-observer-matrix-generated.oct.md"
    
    if role_path.exists():
        print(f"\n📄 ROLE CONTENT PREVIEW:")
        print("-" * 50)
        
        with open(role_path, 'r') as f:
            lines = f.readlines()
        
        # Show first 25 lines as preview
        for i, line in enumerate(lines[:25]):
            print(f"{i+1:2d}: {line.rstrip()}")
        
        if len(lines) > 25:
            print(f"... ({len(lines) - 25} more lines)")
        
        print("-" * 50)
        print(f"✨ Complete role ready for use!")
    else:
        print("❌ Generated role file not found")

if __name__ == "__main__":
    specialist = generate_quality_observer_role()
    
    if specialist:
        print(f"\n" + "=" * 70)
        demonstrate_role_preview()
        print("=" * 70)