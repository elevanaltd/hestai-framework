#!/usr/bin/env python3
"""
OCTAVE-AP-2 Matrix Capability Loading System
Complete job-specific specialist loading like Neo downloading kung fu
"""

import os
import yaml
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass

@dataclass
class CognitiveCoreSpec:
    """Immutable cognitive foundation specification"""
    name: str
    cognition_type: str
    core_wisdom: str
    methodology: Dict[str, List[str]]
    constraints: Dict[str, List[str]]
    content: str

@dataclass 
class CapabilityModuleSpec:
    """Complete job-specific capability module specification"""
    name: str
    required_cognition: str
    required_archetypes: List[str]
    analytical_capabilities: Dict[str, str]
    behavioral_synthesis: Dict[str, str] 
    output_configuration: Dict[str, str]
    content: str

@dataclass
class LoadedSpecialist:
    """Complete specialist role after Matrix loading"""
    name: str
    cognition: str
    archetypes: str
    content: str
    line_count: int
    coherence_score: float

class MatrixCapabilityLoader:
    """
    Matrix-style capability loading system
    Loads complete job-specific specialists like Neo downloading skills
    """
    
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.cognitive_cores_path = self.base_path / "cognitive-cores"
        self.capability_modules_path = self.base_path / "capability-modules"
        
        # Caches for performance
        self._cognitive_cores_cache = {}
        self._capability_modules_cache = {}
    
    def load_cognitive_core(self, cognition_type: str) -> CognitiveCoreSpec:
        """Load immutable cognitive core by type (LOGOS/ETHOS/PATHOS)"""
        if cognition_type in self._cognitive_cores_cache:
            return self._cognitive_cores_cache[cognition_type]
        
        core_file = self.cognitive_cores_path / f"{cognition_type.lower()}.oct"
        if not core_file.exists():
            raise FileNotFoundError(f"Cognitive core not found: {cognition_type}")
        
        with open(core_file, 'r') as f:
            content = f.read()
        
        # Parse frontmatter and content
        if content.startswith('---'):
            parts = content.split('---', 2)
            frontmatter = yaml.safe_load(parts[1]) if len(parts) >= 2 else {}
            core_content = parts[2].strip() if len(parts) >= 3 else content
        else:
            frontmatter = {}
            core_content = content
        
        # Extract methodology and constraints from content
        methodology = self._extract_section(core_content, "METHODOLOGY")
        constraints = self._extract_section(core_content, "CONSTRAINTS")
        
        core_spec = CognitiveCoreSpec(
            name=frontmatter.get('cognition', cognition_type),
            cognition_type=cognition_type,
            core_wisdom=self._extract_value(core_content, "CORE_WISDOM"),
            methodology=methodology,
            constraints=constraints,
            content=core_content
        )
        
        self._cognitive_cores_cache[cognition_type] = core_spec
        return core_spec
    
    def load_capability_module(self, module_name: str) -> CapabilityModuleSpec:
        """Load complete capability module specification"""
        if module_name in self._capability_modules_cache:
            return self._capability_modules_cache[module_name]
        
        module_file = self.capability_modules_path / f"{module_name}.oct"
        if not module_file.exists():
            raise FileNotFoundError(f"Capability module not found: {module_name}")
        
        with open(module_file, 'r') as f:
            content = f.read()
        
        # Parse frontmatter and content
        if content.startswith('---'):
            parts = content.split('---', 2)
            frontmatter = yaml.safe_load(parts[1]) if len(parts) >= 2 else {}
            module_content = parts[2].strip() if len(parts) >= 3 else content
        else:
            frontmatter = {}
            module_content = content
        
        module_spec = CapabilityModuleSpec(
            name=module_name,
            required_cognition=frontmatter.get('required_cognition', 'LOGOS'),
            required_archetypes=frontmatter.get('required_archetypes', []),
            analytical_capabilities=self._extract_section(module_content, "ANALYTICAL_CAPABILITIES"),
            behavioral_synthesis=self._extract_section(module_content, "BEHAVIORAL_SYNTHESIS"), 
            output_configuration=self._extract_section(module_content, "OUTPUT_CONFIGURATION"),
            content=module_content
        )
        
        self._capability_modules_cache[module_name] = module_spec
        return module_spec
    
    def load_specialist(self, capability_module_name: str) -> LoadedSpecialist:
        """
        Matrix-style loading: cognitive core + complete capability module = specialist
        Like Neo downloading kung fu - everything needed for the job in one load
        """
        # 1. Load capability module specification
        module = self.load_capability_module(capability_module_name)
        
        # 2. Load required cognitive core
        cognitive_core = self.load_cognitive_core(module.required_cognition)
        
        # 3. Verify cognitive compatibility
        if cognitive_core.cognition_type != module.required_cognition:
            raise ValueError(f"Cognitive incompatibility: {cognitive_core.cognition_type} != {module.required_cognition}")
        
        # 4. Assemble complete specialist
        specialist_content = self._assemble_specialist(cognitive_core, module)
        
        # 5. Calculate coherence metrics
        line_count = len(specialist_content.split('\n'))
        coherence_score = self._calculate_coherence(cognitive_core, module)
        
        return LoadedSpecialist(
            name=f"{module.name}",
            cognition=cognitive_core.cognition_type,
            archetypes="+".join(module.required_archetypes),
            content=specialist_content,
            line_count=line_count,
            coherence_score=coherence_score
        )
    
    def _assemble_specialist(self, core: CognitiveCoreSpec, module: CapabilityModuleSpec) -> str:
        """Assemble complete specialist from cognitive core + capability module"""
        
        # Build frontmatter
        frontmatter = f"""---
name: {module.name}
model: claude-opus-4
description: {module.name} specialist with {core.cognition_type} cognition
---

## MATRIX_LOADED_SPECIALIST ##
COGNITION::{core.cognition_type}
ARCHETYPES::{"+".join(module.required_archetypes)}
CAPABILITY_MODULE::{module.name}

"""
        
        # Add cognitive foundation
        specialist_content = frontmatter + core.content
        
        # Add capability-specific sections
        specialist_content += f"\n\n## SPECIALIST_CAPABILITIES ##\n"
        specialist_content += module.content
        
        return specialist_content
    
    def _calculate_coherence(self, core: CognitiveCoreSpec, module: CapabilityModuleSpec) -> float:
        """Calculate cognitive coherence score between core and module"""
        # Simple coherence calculation - can be enhanced
        cognitive_match = 1.0 if core.cognition_type == module.required_cognition else 0.0
        archetype_count = len(module.required_archetypes)
        archetype_coherence = min(1.0, archetype_count / 4.0)  # Optimal 3-4 archetypes
        
        return (cognitive_match * 0.7) + (archetype_coherence * 0.3)
    
    def _extract_section(self, content: str, section_name: str) -> Dict[str, str]:
        """Extract structured section from content"""
        # Simplified extraction - can be enhanced with proper parsing
        lines = content.split('\n')
        section_data = {}
        in_section = False
        
        for line in lines:
            if f"{section_name}" in line and "##" in line:
                in_section = True
                continue
            elif in_section and line.strip().startswith('##'):
                break
            elif in_section and '::' in line:
                key, value = line.split('::', 1)
                section_data[key.strip()] = value.strip()
        
        return section_data
    
    def _extract_value(self, content: str, key: str) -> str:
        """Extract single value from content"""
        lines = content.split('\n')
        for line in lines:
            if f"{key}::" in line:
                return line.split('::', 1)[1].strip()
        return ""
    
    def list_available_cores(self) -> List[str]:
        """List available cognitive cores"""
        if not self.cognitive_cores_path.exists():
            return []
        return [f.stem.upper() for f in self.cognitive_cores_path.glob("*.oct")]
    
    def list_available_modules(self) -> List[str]:
        """List available capability modules"""
        if not self.capability_modules_path.exists():
            return []
        return [f.stem for f in self.capability_modules_path.glob("*.oct")]

# Convenience function for direct usage
def load_specialist(base_path: str, module_name: str) -> LoadedSpecialist:
    """Convenience function to load a specialist"""
    loader = MatrixCapabilityLoader(base_path)
    return loader.load_specialist(module_name)