#!/usr/bin/env python3
"""
OCTAVE-AP-2 Matrix Loading Demonstration
Shows Matrix-style capability loading in action
"""

import sys
import os
from pathlib import Path

# Add core module to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'core'))

from matrix_loader import MatrixCapabilityLoader, LoadedSpecialist

def demonstrate_matrix_loading():
    """Demonstrate Matrix loading capabilities"""
    
    print("=" * 60)
    print("OCTAVE-AP-2 MATRIX LOADING DEMONSTRATION")
    print("=" * 60)
    
    # Initialize Matrix loader
    base_path = Path(__file__).parent.parent
    loader = MatrixCapabilityLoader(str(base_path))
    
    print(f"\n🧠 Available Cognitive Cores: {loader.list_available_cores()}")
    print(f"🎯 Available Capability Modules: {loader.list_available_modules()}")
    
    # Demonstrate loading each specialist type
    specialists = [
        "security-specialist",
        "technical-architect", 
        "creative-ideator"
    ]
    
    for module_name in specialists:
        try:
            print(f"\n{'=' * 40}")
            print(f"Loading: {module_name}")
            print(f"{'=' * 40}")
            
            # Load the specialist
            specialist = loader.load_specialist(module_name)
            
            print(f"✅ Specialist Loaded Successfully!")
            print(f"   Name: {specialist.name}")
            print(f"   Cognition: {specialist.cognition}")
            print(f"   Archetypes: {specialist.archetypes}")
            print(f"   Line Count: {specialist.line_count}")
            print(f"   Coherence: {specialist.coherence_score:.2f}")
            
            # Show content preview (first few lines)
            content_lines = specialist.content.split('\n')[:10]
            print(f"\n📄 Content Preview:")
            for i, line in enumerate(content_lines):
                print(f"   {i+1:2d}: {line}")
            print(f"   ... ({specialist.line_count - len(content_lines)} more lines)")
            
        except Exception as e:
            print(f"❌ Error loading {module_name}: {e}")
    
    print(f"\n{'=' * 60}")
    print("MATRIX LOADING COMPLETE")
    print("Each specialist loaded with complete job-specific capabilities!")
    print(f"{'=' * 60}")

def demonstrate_cognitive_compatibility():
    """Show how cognitive cores align with capability modules"""
    
    print("\n" + "=" * 60)
    print("COGNITIVE COMPATIBILITY DEMONSTRATION")
    print("=" * 60)
    
    loader = MatrixCapabilityLoader(str(Path(__file__).parent.parent))
    
    # Test cognitive-capability alignment
    alignments = [
        ("security-specialist", "ETHOS", "Validation cognition for security assessment"),
        ("technical-architect", "LOGOS", "Synthesis cognition for architectural design"),
        ("creative-ideator", "PATHOS", "Creative cognition for breakthrough thinking")
    ]
    
    for module, expected_cognition, description in alignments:
        try:
            capability_spec = loader.load_capability_module(module)
            cognitive_core = loader.load_cognitive_core(capability_spec.required_cognition)
            
            match = "✅" if cognitive_core.cognition_type == expected_cognition else "❌"
            print(f"{match} {module}:")
            print(f"    Required: {capability_spec.required_cognition}")
            print(f"    Loaded: {cognitive_core.cognition_type}")  
            print(f"    Logic: {description}")
            
        except Exception as e:
            print(f"❌ Error testing {module}: {e}")

if __name__ == "__main__":
    demonstrate_matrix_loading()
    demonstrate_cognitive_compatibility()