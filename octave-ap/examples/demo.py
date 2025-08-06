#!/usr/bin/env python3
"""
OCTAVE-AP Interactive Demo
Try the semantic inheritance system with different role requests
"""

import sys
from pathlib import Path

# Add the octave-ap directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

from core.inheritance_engine import SemanticInheritanceEngine
from factory.role_factory import RoleFactory

def demo_role_expansion():
    """Demo: Expand a predefined role from minimal definition"""
    print("🔧 Demo 1: Role Expansion from Minimal Definition")
    print("=" * 60)
    
    patterns_path = str(Path(__file__).parent / "patterns")
    engine = SemanticInheritanceEngine(patterns_path)
    
    # Show the minimal definition first
    role_path = Path(__file__).parent / "roles" / "technical-architect.oct.md"
    
    print("📝 Minimal role definition (30 lines):")
    with open(role_path, 'r') as f:
        content = f.read()
        lines = content.split('\n')
        for i, line in enumerate(lines[:20], 1):  # Show first 20 lines
            print(f"  {i:2d}→ {line}")
        if len(lines) > 20:
            print(f"  ... and {len(lines) - 20} more lines")
    
    print(f"\n🚀 Expanding role...")
    expanded = engine.expand_role_from_file(str(role_path))
    
    print(f"✅ Result:")
    print(f"   Original: {len(content.split(chr(10)))} lines")
    print(f"   Expanded: {expanded.line_count} lines")
    print(f"   Performance: {expanded.performance_estimate:.1%}")
    print(f"   Size: {len(expanded.content):,} characters")
    
    print(f"\n📄 Expanded content preview (first 500 chars):")
    print("   " + "─" * 50)
    print("   " + expanded.content[:500].replace('\n', '\n   '))
    print("   " + "─" * 50)
    print("   ... (content continues)")

def demo_natural_language():
    """Demo: Create roles from natural language"""
    print("\n\n🎯 Demo 2: Natural Language Role Creation")
    print("=" * 60)
    
    patterns_path = str(Path(__file__).parent / "patterns")
    factory = RoleFactory(patterns_path)
    
    test_requests = [
        "quality observer with security focus",
        "creative ideator for breakthrough innovations", 
        "technical architect for microservices",
        "code reviewer focused on performance optimization"
    ]
    
    for i, request in enumerate(test_requests, 1):
        print(f"\n{i}. Request: '{request}'")
        
        try:
            role_content = factory.create_role(request)
            lines = len(role_content.split('\n'))
            words = len(role_content.split())
            
            print(f"   ✅ Generated: {lines} lines, {words} words")
            
            # Show a snippet of what was generated
            preview = role_content.split('\n')[:10]
            print(f"   📄 Preview:")
            for line in preview:
                if line.strip():
                    print(f"      {line[:60]}{'...' if len(line) > 60 else ''}")
            
        except Exception as e:
            print(f"   ❌ Failed: {e}")

def demo_pattern_exploration():
    """Demo: Show what patterns are available"""
    print("\n\n🔍 Demo 3: Available Patterns")
    print("=" * 60)
    
    patterns_path = Path(__file__).parent / "patterns"
    
    for category_dir in sorted(patterns_path.iterdir()):
        if category_dir.is_dir():
            print(f"\n📁 {category_dir.name}/")
            
            patterns = list(category_dir.glob('*.oct.md'))
            for pattern in sorted(patterns):
                # Get pattern size
                size = len(pattern.read_text())
                print(f"   📄 {pattern.name:<40} ({size:,} chars)")

def interactive_test():
    """Let user try their own requests"""
    print("\n\n🎮 Demo 4: Try Your Own Role Request")
    print("=" * 60)
    
    patterns_path = str(Path(__file__).parent / "patterns")
    factory = RoleFactory(patterns_path)
    
    print("Enter a role request (or 'quit' to exit):")
    print("Examples:")
    print("  - 'security auditor for web applications'")
    print("  - 'performance optimizer for database systems'")
    print("  - 'creative strategist for product design'")
    
    while True:
        try:
            request = input("\n🎯 Your request: ").strip()
            
            if request.lower() in ['quit', 'exit', 'q']:
                break
                
            if not request:
                continue
            
            print(f"🔄 Processing '{request}'...")
            
            role_content = factory.create_role(request)
            lines = len(role_content.split('\n'))
            words = len(role_content.split())
            
            print(f"✅ Generated role: {lines} lines, {words} words")
            
            # Offer to show full content
            show_full = input("📄 Show full content? (y/n): ").strip().lower()
            if show_full.startswith('y'):
                print("\n" + "=" * 80)
                print(role_content)
                print("=" * 80)
            else:
                # Show just the key sections
                lines_list = role_content.split('\n')
                print("\n📋 Key sections:")
                in_section = False
                current_section = ""
                
                for line in lines_list[:50]:  # First 50 lines
                    if line.startswith('##'):
                        current_section = line.strip()
                        print(f"   {current_section}")
                        in_section = True
                    elif line.startswith('MISSION::') or line.startswith('ARCHETYPES::'):
                        print(f"   {line.strip()}")
                        
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("🧪 OCTAVE-AP Interactive Demo")
    print("Semantic Inheritance System for AI Role Creation")
    print("=" * 80)
    
    try:
        # Run all demos
        demo_role_expansion()
        demo_natural_language() 
        demo_pattern_exploration()
        interactive_test()
        
        print("\n\n🎉 Demo complete!")
        print("The OCTAVE-AP system is ready for production use.")
        
    except KeyboardInterrupt:
        print("\n\n👋 Demo interrupted. Thanks for trying OCTAVE-AP!")
    except Exception as e:
        print(f"\n❌ Demo error: {e}")
        print("Check that all files are in place and try again.")