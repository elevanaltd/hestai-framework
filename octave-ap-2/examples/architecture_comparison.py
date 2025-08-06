#!/usr/bin/env python3
"""
Architecture Comparison: OCTAVE-AP-1 vs OCTAVE-AP-2
Demonstrates the advantages of Matrix loading over fragmented inheritance
"""

import sys
from pathlib import Path

# Add core module to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'core'))

from matrix_loader import MatrixCapabilityLoader

def compare_architectures():
    """Compare OCTAVE-AP-1 fragmented inheritance vs OCTAVE-AP-2 Matrix loading"""
    
    print("=" * 80)
    print("ARCHITECTURE COMPARISON: OCTAVE-AP-1 vs OCTAVE-AP-2")
    print("=" * 80)
    
    # OCTAVE-AP-1 Analysis (from existing data)
    ap1_stats = {
        "patterns": 29,
        "directories": 5,
        "inheritance_chain_length": 22,  # From technical-architect-ap.oct.md
        "fake_modularity_percentage": 38,  # From Quality Observer assessment
        "avg_role_size_lines": 209,  # From critical engineer review
        "complexity_score": "HIGH",
        "assembly_method": "Complex semantic inheritance with deduplication"
    }
    
    # OCTAVE-AP-2 Analysis (from current implementation) 
    loader = MatrixCapabilityLoader(str(Path(__file__).parent.parent))
    ap2_stats = {
        "cognitive_cores": len(loader.list_available_cores()),
        "capability_modules": len(loader.list_available_modules()),
        "assembly_components": 2,  # core + module
        "avg_role_size_lines": calculate_average_role_size(loader),
        "complexity_score": "LOW",
        "assembly_method": "Simple Matrix loading (core + module = specialist)"
    }
    
    print("\n📊 QUANTITATIVE COMPARISON")
    print("-" * 40)
    print(f"{'Metric':<25} {'AP-1':<15} {'AP-2':<15} {'Improvement':<15}")
    print("-" * 70)
    print(f"{'Components':<25} {ap1_stats['patterns']:<15} {ap2_stats['cognitive_cores'] + ap2_stats['capability_modules']:<15} {format_improvement(ap1_stats['patterns'], ap2_stats['cognitive_cores'] + ap2_stats['capability_modules'])}")
    print(f"{'Assembly Steps':<25} {ap1_stats['inheritance_chain_length']:<15} {ap2_stats['assembly_components']:<15} {format_improvement(ap1_stats['inheritance_chain_length'], ap2_stats['assembly_components'])}")
    print(f"{'Avg Role Size (lines)':<25} {ap1_stats['avg_role_size_lines']:<15} {ap2_stats['avg_role_size_lines']:<15} {format_improvement(ap1_stats['avg_role_size_lines'], ap2_stats['avg_role_size_lines'], lower_better=True)}")
    print(f"{'Complexity':<25} {ap1_stats['complexity_score']:<15} {ap2_stats['complexity_score']:<15} {'✅ REDUCED':<15}")
    
    print("\n🏗️ ARCHITECTURAL ANALYSIS")
    print("-" * 40)
    
    print("\n🔴 OCTAVE-AP-1 (Fragmented Inheritance):")
    print("   • 29 patterns across 5 directories")
    print("   • 22-step inheritance chain per role") 
    print("   • 38% fake modularity (1:1 pattern mappings)")
    print("   • Complex semantic expansion engine")
    print("   • Separated output configurations")
    print("   • Average 209 lines per role")
    
    print("\n🟢 OCTAVE-AP-2 (Matrix Loading):")
    print("   • 3 immutable cognitive cores")
    print(f"   • {ap2_stats['capability_modules']} complete capability modules")
    print("   • 2-step assembly: core + module = specialist")
    print("   • Job-specific coherence with integrated output")
    print("   • Perfect cognitive-capability alignment")
    print(f"   • Average {ap2_stats['avg_role_size_lines']} lines per role")
    
    print("\n⚡ KEY BREAKTHROUGH ADVANTAGES")
    print("-" * 40)
    
    # Demonstrate coherence scoring
    specialists = ["security-specialist", "technical-architect", "creative-ideator"]
    coherence_scores = []
    
    for module_name in specialists:
        try:
            specialist = loader.load_specialist(module_name)
            coherence_scores.append(specialist.coherence_score)
            print(f"   • {specialist.name}: {specialist.coherence_score:.2f} coherence ({specialist.cognition} cognition)")
        except Exception as e:
            print(f"   • Error loading {module_name}: {e}")
    
    avg_coherence = sum(coherence_scores) / len(coherence_scores) if coherence_scores else 0
    print(f"\n   📈 Average Cognitive Coherence: {avg_coherence:.2f} (vs unmeasured in AP-1)")
    
    print("\n🎯 MATRIX LOADING PARADIGM BENEFITS")
    print("-" * 40)
    print("   ✅ Complete Job Specification (cognition + capabilities + output)")
    print("   ✅ Perfect Context Coherence (thinking aligns with doing)")
    print("   ✅ True Modularity (same core, different specialists)")
    print("   ✅ Simplified Assembly (no inheritance chains)")
    print("   ✅ Measurable Quality (coherence scoring)")
    print("   ✅ Maintainable Architecture (fewer moving parts)")
    
    print("\n" + "=" * 80)
    
    # Calculate overall improvement metrics
    complexity_reduction = calculate_complexity_reduction(ap1_stats, ap2_stats)
    print(f"OVERALL ARCHITECTURE IMPROVEMENT: {complexity_reduction}% complexity reduction")
    print("Matrix loading achieves genuine modularity through job-specific coherence")
    print("=" * 80)

def calculate_average_role_size(loader):
    """Calculate average role size for AP-2 specialists"""
    specialists = loader.list_available_modules()
    total_lines = 0
    
    for module_name in specialists:
        try:
            specialist = loader.load_specialist(module_name)
            total_lines += specialist.line_count
        except Exception:
            continue
    
    return round(total_lines / len(specialists)) if specialists else 0

def format_improvement(old_value, new_value, lower_better=False):
    """Format improvement percentage"""
    try:
        if lower_better:
            improvement = ((old_value - new_value) / old_value) * 100
            symbol = "📉" if improvement > 0 else "📈"
        else:
            improvement = ((new_value - old_value) / old_value) * 100  
            symbol = "📈" if improvement > 0 else "📉"
        
        return f"{symbol} {abs(improvement):.0f}%"
    except (ZeroDivisionError, TypeError):
        return "N/A"

def calculate_complexity_reduction(ap1_stats, ap2_stats):
    """Calculate overall complexity reduction percentage"""
    # Weighted complexity score based on multiple factors
    ap1_complexity = (
        ap1_stats["patterns"] * 0.4 +  # Component count weight
        ap1_stats["inheritance_chain_length"] * 0.3 +  # Assembly complexity weight
        (ap1_stats["avg_role_size_lines"] / 10) * 0.3  # Size complexity weight
    )
    
    ap2_complexity = (
        (ap2_stats["cognitive_cores"] + ap2_stats["capability_modules"]) * 0.4 +
        ap2_stats["assembly_components"] * 0.3 + 
        (ap2_stats["avg_role_size_lines"] / 10) * 0.3
    )
    
    reduction = ((ap1_complexity - ap2_complexity) / ap1_complexity) * 100
    return round(reduction)

if __name__ == "__main__":
    compare_architectures()