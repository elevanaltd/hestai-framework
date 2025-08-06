#!/usr/bin/env python3
"""
OCTAVE-AP Role Factory
Natural language to complete role prompt generation
"""

import re
from typing import Dict, List, Optional
from pathlib import Path
from dataclasses import dataclass

try:
    from core.inheritance_engine_v2 import SemanticInheritanceEngineV2 as SemanticInheritanceEngine, RoleDefinition
except ImportError:
    from core.inheritance_engine import SemanticInheritanceEngine, RoleDefinition

@dataclass
class RoleIntent:
    """Analyzed intent from natural language request"""
    role_name: str
    cognition: str  # logos, ethos, pathos
    domain: str
    needs_governance: bool
    security_focus: bool
    performance_focus: bool
    specific_config: Dict[str, str]

class IntentAnalyzer:
    """Analyzes natural language requests to determine role requirements"""
    
    COGNITION_PATTERNS = {
        'logos': ['architect', 'technical', 'implementation', 'build', 'synthesis', 'engineering'],
        'ethos': ['quality', 'observer', 'validation', 'assessment', 'compliance', 'audit'],
        'pathos': ['ideator', 'creative', 'enhancement', 'innovation', 'exploration']
    }
    
    DOMAIN_PATTERNS = {
        'technical-architecture': ['architect', 'technical', 'system', 'design'],
        'quality-assessment': ['quality', 'observer', 'assessment', 'validation'],
        'code-analysis': ['code', 'review', 'analysis', 'scan'],
        'implementation-leadership': ['implementation', 'lead', 'build', 'execution'],
        'creative-exploration': ['ideator', 'creative', 'innovation', 'enhancement']
    }
    
    GOVERNANCE_TRIGGERS = ['quality', 'assessment', 'validation', 'compliance', 'audit', 'observer']
    SECURITY_TRIGGERS = ['security', 'vulnerability', 'threat', 'audit', 'scan']
    PERFORMANCE_TRIGGERS = ['performance', 'optimization', 'scalability', 'efficiency']
    
    def analyze_intent(self, request: str) -> RoleIntent:
        """Analyze natural language request to determine role requirements"""
        request_lower = request.lower()
        
        # Determine cognition type
        cognition = self._determine_cognition(request_lower)
        
        # Determine domain
        domain = self._determine_domain(request_lower)
        
        # Extract role name
        role_name = self._extract_role_name(request_lower, cognition, domain)
        
        # Determine enhancement needs
        needs_governance = any(trigger in request_lower for trigger in self.GOVERNANCE_TRIGGERS)
        security_focus = any(trigger in request_lower for trigger in self.SECURITY_TRIGGERS)
        performance_focus = any(trigger in request_lower for trigger in self.PERFORMANCE_TRIGGERS)
        
        # Extract specific configuration
        specific_config = self._extract_specific_config(request)
        
        return RoleIntent(
            role_name=role_name,
            cognition=cognition,
            domain=domain,
            needs_governance=needs_governance,
            security_focus=security_focus,
            performance_focus=performance_focus,
            specific_config=specific_config
        )
    
    def _determine_cognition(self, request: str) -> str:
        """Determine cognitive pattern from request"""
        scores = {}
        
        for cognition, patterns in self.COGNITION_PATTERNS.items():
            score = sum(1 for pattern in patterns if pattern in request)
            scores[cognition] = score
        
        return max(scores, key=scores.get) if max(scores.values()) > 0 else 'logos'
    
    def _determine_domain(self, request: str) -> str:
        """Determine domain capability from request"""
        scores = {}
        
        for domain, patterns in self.DOMAIN_PATTERNS.items():
            score = sum(1 for pattern in patterns if pattern in request)
            scores[domain] = score
        
        return max(scores, key=scores.get) if max(scores.values()) > 0 else 'technical-architecture'
    
    def _extract_role_name(self, request: str, cognition: str, domain: str) -> str:
        """Extract or generate appropriate role name"""
        # Common role name patterns
        if 'quality observer' in request or 'quality assessment' in request:
            return 'quality-observer'
        elif 'code review' in request or 'code analysis' in request:
            return 'code-review-specialist'
        elif 'technical architect' in request or 'system architect' in request:
            return 'technical-architect'
        elif 'implementation lead' in request or 'build lead' in request:
            return 'implementation-lead'
        elif 'ideator' in request or 'creative' in request:
            return 'ideator'
        else:
            # Generate from cognition and domain
            domain_name = domain.split('-')[0]
            return f"{domain_name}-{cognition}"
    
    def _extract_specific_config(self, request: str) -> Dict[str, str]:
        """Extract specific configuration requirements"""
        config = {}
        
        # Extract archetype preferences
        archetype_match = re.search(r'archetype[s]?[:\\s]+([A-Z+\\s]+)', request, re.IGNORECASE)
        if archetype_match:
            config['ARCHETYPES'] = archetype_match.group(1).upper()
        
        # Extract mission focus
        mission_patterns = ['focus on', 'emphasize', 'specialize in', 'prioritize']
        for pattern in mission_patterns:
            match = re.search(f'{pattern}[:\\s]+([^.]+)', request, re.IGNORECASE)
            if match:
                config['MISSION_FOCUS'] = match.group(1).strip()
                break
        
        return config

class RoleFactory:
    """Factory for creating roles from natural language requests"""
    
    def __init__(self, pattern_library_path: str):
        self.engine = SemanticInheritanceEngine(pattern_library_path)
        self.analyzer = IntentAnalyzer()
    
    def create_role(self, request: str) -> str:
        """Natural language to complete role prompt"""
        
        # 1. Analyze request to determine intent
        intent = self.analyzer.analyze_intent(request)
        
        # 2. Build inheritance chain based on intent
        inheritance = self._build_inheritance_chain(intent)
        
        # 3. Create minimal role definition
        role_def = self._create_role_definition(intent, inheritance)
        
        # 4. Expand to full prompt
        expanded_role = self.engine.expand_role(role_def)
        
        return expanded_role.content
    
    def _build_inheritance_chain(self, intent: RoleIntent) -> List[str]:
        """Build inheritance chain based on analyzed intent"""
        inheritance = []
        
        # Always include universal patterns
        inheritance.extend([
            '0-sea-universal/raph-processing.oct.md',
            '0-sea-universal/anti-patterns.oct.md',
            '0-sea-universal/quality-gates.oct.md'
        ])
        
        # Add governance boost if needed
        if intent.needs_governance:
            inheritance.append('0-sea-universal/constitutional-foundation.oct.md')
        
        # Add cognitive pattern
        cognition_mapping = {
            'logos': 'logos-synthesis.oct.md',
            'ethos': 'ethos-validation.oct.md', 
            'pathos': 'pathos-enhancement.oct.md'
        }
        cognition_pattern = cognition_mapping.get(intent.cognition, 'logos-synthesis.oct.md')
        inheritance.append(f'1-shank-cognitions/{cognition_pattern}')
        
        # Add domain capability
        domain_mapping = {
            'technical-architecture': 'technical-architecture-matrix.oct.md',
            'quality-assessment': 'quality-assessment-matrix.oct.md', 
            'code-analysis': 'code-analysis-matrix.oct.md',
            'implementation-leadership': 'implementation-leadership-matrix.oct.md',
            'creative-exploration': 'creative-exploration-matrix.oct.md'
        }
        
        domain_pattern = domain_mapping.get(intent.domain, 'technical-architecture-matrix.oct.md')
        inheritance.append(f'3-flukes-capabilities/{domain_pattern}')
        
        return inheritance
    
    def _create_role_definition(self, intent: RoleIntent, inheritance: List[str]) -> RoleDefinition:
        """Create minimal role definition from intent"""
        
        # Generate archetype combinations based on cognition and domain
        archetype_combinations = {
            ('logos', 'technical-architecture'): 'HEPHAESTUS+ATLAS+PROMETHEUS',
            ('ethos', 'quality-assessment'): 'ARGUS+THEMIS+ATHENA',
            ('logos', 'code-analysis'): 'ATHENA+PROMETHEUS+HEPHAESTUS',
            ('logos', 'implementation-leadership'): 'HEPHAESTUS+ATLAS+HERMES',
            ('pathos', 'creative-exploration'): 'PROMETHEUS+ICARUS+DAEDALUS'
        }
        
        archetypes = archetype_combinations.get(
            (intent.cognition, intent.domain), 
            'ATHENA+PROMETHEUS+HEPHAESTUS'
        )
        
        # Override with specific config if provided
        if 'ARCHETYPES' in intent.specific_config:
            archetypes = intent.specific_config['ARCHETYPES']
        
        # Generate mission based on domain
        mission_templates = {
            'technical-architecture': 'ARCHITECTURAL_SYNTHESIS+TECHNICAL_EXCELLENCE+STRATEGIC_DESIGN',
            'quality-assessment': 'COMPREHENSIVE_QUALITY_ASSESSMENT+SECURITY_VALIDATION+COMPLIANCE_VERIFICATION',
            'code-analysis': 'PREVENT_PRODUCTION_CHAOS+ELEVATE_CODE_EXCELLENCE+SECURITY_ANALYSIS',
            'implementation-leadership': 'TECHNICAL_LEADERSHIP+ARCHITECTURAL_COHERENCE+DELIVERY_EXCELLENCE',
            'creative-exploration': 'BREAKTHROUGH_POSSIBILITIES+EXISTING_CONCEPT_PERFECTION+BOUNDARY_INTEGRITY'
        }
        
        mission = mission_templates.get(intent.domain, 'TECHNICAL_EXCELLENCE+QUALITY_ASSURANCE')
        
        # Create behavioral overrides
        behavioral_overrides = {
            'ARCHETYPES': archetypes,
            'MISSION': mission
        }
        
        # Add focus areas from specific config
        if 'MISSION_FOCUS' in intent.specific_config:
            behavioral_overrides['FOCUS_AREAS'] = intent.specific_config['MISSION_FOCUS']
        
        return RoleDefinition(
            name=intent.role_name,
            model='claude-opus-4',
            description=f"{intent.role_name.replace('-', ' ')} {intent.cognition} {intent.domain}",
            role_type=intent.domain,
            inherits=inheritance,
            behavioral_overrides=behavioral_overrides,
            performance_targets={'min_performance': 0.85}
        )
    
    def list_available_patterns(self) -> Dict[str, List[str]]:
        """List all available patterns by category"""
        patterns_path = Path(self.engine.patterns.patterns_path)
        
        categories = {}
        for category_dir in patterns_path.iterdir():
            if category_dir.is_dir():
                category_name = category_dir.name
                patterns = [f.name for f in category_dir.glob('*.oct.md')]
                categories[category_name] = patterns
        
        return categories

# Example usage and testing
if __name__ == "__main__":
    factory = RoleFactory("/Volumes/HestAI/hestai-framework/octave-ap/patterns")
    
    # Test requests
    test_requests = [
        "quality observer with security focus",
        "technical architect for complex systems", 
        "code review specialist for security",
        "implementation lead for build phase",
        "creative ideator for enhancement"
    ]
    
    for request in test_requests:
        print(f"\nRequest: {request}")
        try:
            role_content = factory.create_role(request)
            print(f"Generated role: {len(role_content.split())} words, {len(role_content.split('\n'))} lines")
            print(f"Preview: {role_content[:200]}...")
        except Exception as e:
            print(f"Error: {e}")