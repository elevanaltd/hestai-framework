#!/usr/bin/env python3
"""
OCTAVE-AP Semantic Inheritance Engine V2
Fixed version addressing duplication and formatting issues
"""

import os
import yaml
from pathlib import Path
from typing import List, Dict, Any, Optional, Set
from dataclasses import dataclass

@dataclass
class RoleDefinition:
    """Minimal role definition with inheritance chain"""
    name: str
    model: str = "claude-opus-4"
    description: str = ""
    role_type: str = ""
    inherits: List[str] = None
    archetypes: str = ""
    mission: str = ""
    behavioral_overrides: Dict[str, str] = None
    output_specialization: Dict[str, str] = None
    performance_targets: Dict[str, float] = None

@dataclass
class ExpandedRole:
    """Complete role after expansion"""
    content: str
    metadata: RoleDefinition
    line_count: int
    performance_estimate: float

class PatternLibrary:
    """Manages pattern storage and retrieval"""
    
    def __init__(self, patterns_path: str):
        self.patterns_path = Path(patterns_path)
        self._pattern_cache = {}
    
    def load_pattern(self, pattern_path: str) -> str:
        """Load pattern content with caching"""
        if pattern_path in self._pattern_cache:
            return self._pattern_cache[pattern_path]
        
        full_path = self.patterns_path / pattern_path
        if not full_path.exists():
            raise FileNotFoundError(f"Pattern not found: {pattern_path}")
        
        with open(full_path, 'r') as f:
            content = f.read()
        
        self._pattern_cache[pattern_path] = content
        return content

class SemanticExpander:
    """Expands patterns into coherent content"""
    
    def expand_patterns(self, pattern_paths: List[str], library: PatternLibrary) -> str:
        """Expand inheritance chain into cohesive content with proper ordering"""
        expanded_sections = []
        output_config_section = None
        
        for pattern_path in pattern_paths:
            pattern_content = library.load_pattern(pattern_path)
            
            # Check if this is an output configuration pattern
            if '4-output-configs' in pattern_path or '## OUTPUT_CONFIGURATION ##' in pattern_content:
                # Save output config for the end
                output_config_section = pattern_content
            else:
                expanded_sections.append(pattern_content)
        
        # Add output configuration at the end if present
        result = '\n\n'.join(expanded_sections)
        if output_config_section:
            result += '\n\n' + output_config_section
            
        return result

class DynamicEnhancer:
    """Injects performance-critical enhancements based on role context"""
    
    ENHANCEMENT_CATALOG = {
        'governance_boost': {
            'pattern': '0-sea-universal/constitutional-foundation.oct.md',
            'performance_gain': 0.39,
            'triggers': ['quality', 'validation', 'assessment', 'observer'],
            'description': 'Constitutional foundation providing governance structure'
        },
        'security_integration': {
            'pattern': '2-arm-enhancements/security-integration.oct.md',
            'performance_gain': 0.15,
            'triggers': ['security', 'vulnerability', 'threat', 'audit'],
            'description': 'Security-aware pattern integration'
        }
    }
    
    def select_enhancements(self, role_config: RoleDefinition, already_included: Set[str]) -> List[Dict[str, Any]]:
        """Select appropriate enhancements based on role characteristics"""
        selected = []
        
        # Analyze role name, description, and type for trigger words
        text_to_analyze = f"{role_config.name} {role_config.description} {role_config.role_type}".lower()
        
        for enhancement_id, enhancement in self.ENHANCEMENT_CATALOG.items():
            # Skip if pattern already included in inheritance chain
            pattern_name = enhancement['pattern']
            if pattern_name in already_included:
                continue
                
            for trigger in enhancement['triggers']:
                if trigger in text_to_analyze:
                    selected.append(enhancement)
                    break
        
        return selected
    
    def inject_enhancements(self, base_content: str, role_config: RoleDefinition, 
                          library: PatternLibrary, already_included: Set[str]) -> str:
        """Dynamically inject performance boosters without duplication"""
        enhancements = self.select_enhancements(role_config, already_included)
        enhanced_content = base_content
        
        for enhancement in enhancements:
            try:
                pattern_content = library.load_pattern(enhancement['pattern'])
                enhanced_content += f"\n\n## DYNAMIC_ENHANCEMENT: {enhancement['description']} ##\n"
                enhanced_content += pattern_content
                already_included.add(enhancement['pattern'])
            except FileNotFoundError:
                # Enhancement pattern not found, skip silently
                continue
        
        return enhanced_content

class SemanticInheritanceEngineV2:
    """
    Fixed inheritance engine addressing duplication and formatting issues
    """
    
    def __init__(self, pattern_library_path: str):
        self.patterns = PatternLibrary(pattern_library_path)
        self.expander = SemanticExpander()
        self.enhancer = DynamicEnhancer()
    
    def load_role_definition(self, role_path: str) -> RoleDefinition:
        """Load minimal role definition from .oct.md file"""
        with open(role_path, 'r') as f:
            content = f.read()
        
        # Parse frontmatter
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                frontmatter = yaml.safe_load(parts[1])
                body = parts[2].strip()
            else:
                frontmatter = {}
                body = content
        else:
            frontmatter = {}
            body = content
        
        # Parse inheritance and overrides from body
        inherits = []
        behavioral_overrides = {}
        output_specialization = {}
        archetypes = ""
        mission = ""
        
        # Parse multi-line inheritance
        lines = body.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line.startswith('inherits::['):
                # Handle multi-line inheritance
                inherit_text = line.replace('inherits::[', '')
                if inherit_text.endswith(']'):
                    # Single line
                    inherit_text = inherit_text.replace(']', '')
                    inherits = [p.strip(' "\',') for p in inherit_text.split(',') if p.strip()]
                else:
                    # Multi-line - collect until closing bracket
                    i += 1
                    while i < len(lines) and not lines[i].strip().endswith(']'):
                        inherit_text += ' ' + lines[i].strip()
                        i += 1
                    if i < len(lines):
                        inherit_text += ' ' + lines[i].strip().replace(']', '')
                    inherits = [p.strip(' "\',') for p in inherit_text.split(',') if p.strip()]
            elif line.startswith('ARCHETYPES::'):
                archetypes = line.split('::', 1)[1]
            elif line.startswith('MISSION::'):
                mission = line.split('::', 1)[1]
            elif '::' in line and not line.startswith('#'):
                key, value = line.split('::', 1)
                if 'BEHAVIORAL' in key.upper():
                    behavioral_overrides[key] = value
                elif 'OUTPUT' in key.upper():
                    output_specialization[key] = value
            i += 1
        
        return RoleDefinition(
            name=frontmatter.get('name', ''),
            model=frontmatter.get('model', 'claude-opus-4'),
            description=frontmatter.get('description', ''),
            inherits=inherits,
            archetypes=archetypes,
            mission=mission,
            behavioral_overrides=behavioral_overrides,
            output_specialization=output_specialization
        )
    
    def _build_complete_role(self, expanded_patterns: str, role_def: RoleDefinition) -> str:
        """Build complete role with proper structure and frontmatter"""
        
        # Start with proper frontmatter
        frontmatter = f"""---
name: {role_def.name}
model: {role_def.model}
description: {role_def.description}
---
"""
        
        # Add role metadata section if needed
        role_specific = ""
        
        if role_def.archetypes or role_def.mission:
            role_specific += "\n## ROLE_CONFIGURATION ##\n"
            if role_def.archetypes:
                role_specific += f"ARCHETYPES::{role_def.archetypes}\n"
            if role_def.mission:
                role_specific += f"MISSION::{role_def.mission}\n"
        
        # Add behavioral customizations
        if role_def.behavioral_overrides:
            role_specific += "\n## BEHAVIORAL_CUSTOMIZATION ##\n"
            for key, value in role_def.behavioral_overrides.items():
                role_specific += f"{key}::{value}\n"
        
        # Add output specializations 
        if role_def.output_specialization:
            role_specific += "\n## OUTPUT_SPECIALIZATION ##\n"
            for key, value in role_def.output_specialization.items():
                role_specific += f"{key}::{value}\n"
        
        # Combine all parts
        complete_role = frontmatter + expanded_patterns
        
        # Insert role-specific content after the cognitive foundation but before output config
        if role_specific:
            # Find where to insert (after cognitive patterns, before output)
            lines = complete_role.split('\n')
            insert_point = -1
            
            for i, line in enumerate(lines):
                if '## OUTPUT_CONFIGURATION ##' in line or '## OUTPUT_STRUCTURE' in line:
                    insert_point = i
                    break
            
            if insert_point > 0:
                lines.insert(insert_point, role_specific)
                complete_role = '\n'.join(lines)
            else:
                complete_role += role_specific
        
        return complete_role
    
    def expand_role(self, role_definition: RoleDefinition) -> ExpandedRole:
        """
        Main expansion method with deduplication and proper formatting
        """
        if not role_definition.inherits:
            raise ValueError("Role definition must specify inheritance chain")
        
        # Track what patterns have been included to prevent duplication
        included_patterns = set(role_definition.inherits)
        
        # 1. Expand inherited patterns in order
        expanded_patterns = self.expander.expand_patterns(
            role_definition.inherits, 
            self.patterns
        )
        
        # 2. Apply dynamic enhancements (only if not already included)
        enhanced_content = self.enhancer.inject_enhancements(
            expanded_patterns,
            role_definition,
            self.patterns,
            included_patterns
        )
        
        # 3. Build complete role with proper structure
        complete_role = self._build_complete_role(enhanced_content, role_definition)
        
        # 4. Calculate metrics
        line_count = len(complete_role.split('\n'))
        performance_estimate = min(0.877, line_count / 112.0 * 0.877)
        
        return ExpandedRole(
            content=complete_role,
            metadata=role_definition,
            line_count=line_count,
            performance_estimate=performance_estimate
        )
    
    def expand_role_from_file(self, role_path: str) -> ExpandedRole:
        """Convenience method to expand role from file"""
        role_def = self.load_role_definition(role_path)
        return self.expand_role(role_def)