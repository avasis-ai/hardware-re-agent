"""Command-line interface for Hardware Reverse Engineering Agent."""

import click
import json
from typing import Optional

from .malware_engine import (
    MalwareAnalyzer,
    ReportGenerator,
    GhidraBridge,
    SemanticTranslator,
    MalwareBehavior
)


@click.group()
@click.version_option(version="0.1.0", prog_name="hardware-re")
def main() -> None:
    """Hardware Reverse Engineering Agent - Autonomous malware analysis."""
    pass


@main.command()
@click.option("--host", default="localhost", help="Ghidra server hostname")
@click.option("--port", default=13133, help="Ghidra server port")
def config(host: str, port: int) -> None:
    """Show Ghidra configuration."""
    click.echo(f"\n⚙️ Ghidra Configuration")
    click.echo("=" * 60)
    click.echo(f"Host: {host}")
    click.echo(f"Port: {port}")


@main.command()
@click.argument("binary_path")
@click.option("--output", "-o", type=click.Path(), help="Output file path")
def analyze(binary_path: str, output: Optional[str]) -> None:
    """Analyze a binary file for malware behavior."""
    analyzer = MalwareAnalyzer()
    
    try:
        click.echo(f"\n🔍 Analyzing: {binary_path}")
        click.echo("=" * 60)
        
        # Perform analysis
        analysis, report = analyzer.analyze(binary_path)
        
        # Generate text report
        generator = ReportGenerator()
        text_report = generator.generate_text_report(report)
        
        click.echo(text_report)
        
        # Save to file if requested
        if output:
            with open(output, 'w') as f:
                f.write(text_report)
            click.echo(f"\n✅ Report saved to: {output}")
        
    except Exception as e:
        click.echo(f"\n❌ Error: {e}")


@main.command()
@click.argument("binary_path")
@click.option("--json", is_flag=True, help="Output as JSON")
def detailed(binary_path: str, json_output: bool) -> None:
    """Show detailed binary analysis."""
    analyzer = MalwareAnalyzer()
    
    try:
        # Perform analysis
        analysis, report = analyzer.analyze(binary_path)
        
        if json_output:
            click.echo(json.dumps(analysis.to_dict(), indent=2))
        else:
            click.echo(f"\n📊 Binary Analysis Details")
            click.echo("=" * 60)
            click.echo(f"Path: {analysis.binary_path}")
            click.echo(f"Hash: {analysis.binary_hash}")
            click.echo(f"Architecture: {analysis.architecture}")
            click.echo(f"Entry Point: {hex(analysis.entry_point)}")
            
            click.echo(f"\n📦 Import Functions ({len(analysis.import_functions)}):")
            for func in analysis.import_functions:
                click.echo(f"  • {func}")
            
            click.echo(f"\n📤 Export Functions ({len(analysis.export_functions)}):")
            for func in analysis.export_functions:
                click.echo(f"  • {func}")
            
            click.echo(f"\n📑 Sections:")
            for section in analysis.sections:
                click.echo(f"  • {section['name']}: {section['size']} bytes ({section['type']})")
            
            click.echo(f"\n🎯 Detected Behaviors ({len(analysis.detected_behaviors)}):")
            for behavior in analysis.detected_behaviors:
                confidence = analysis.confidence_scores.get(behavior, 0)
                click.echo(f"  • {behavior.value} ({confidence*100:.0f}% confidence)")
        
    except Exception as e:
        click.echo(f"\n❌ Error: {e}")


@main.command()
def demo() -> None:
    """Run malware analysis demo."""
    click.echo("\n🧪 Malware Analysis Demo")
    click.echo("=" * 60)
    
    # Simulate binary analysis
    click.echo("\n🔍 Simulating analysis of sample binary...")
    
    analyzer = MalwareAnalyzer()
    
    # Use a sample binary path for demo
    sample_binary = "sample_malware.exe"
    
    try:
        analysis, report = analyzer.analyze(sample_binary)
        
        click.echo(f"\n✅ Analysis Complete!")
        click.echo(f"   Report ID: {report.report_id}")
        click.echo(f"   Threat Level: {report.threat_level}")
        click.echo(f"   Duration: {report.analysis_duration_seconds:.2f}s")
        
    except Exception as e:
        click.echo(f"\n❌ Demo failed: {e}")


@main.command()
def patterns() -> None:
    """Show security patterns used for detection."""
    click.echo("\n📋 Security Detection Patterns")
    click.echo("=" * 60)
    
    patterns = SemanticTranslator.SECURITY_PATTERNS
    
    for pattern_name, pattern_info in patterns.items():
        click.echo(f"\n{pattern_name.upper()}")
        click.echo(f"  Behavior: {pattern_info['behavior'].value}")
        click.echo(f"  Description: {pattern_info['description']}")
        click.echo(f"  Matched Functions:")
        for func in pattern_info['patterns'][:3]:
            click.echo(f"    • {func}")


def main_entry() -> None:
    """Main entry point."""
    main(prog_name="hardware-re")


if __name__ == "__main__":
    main_entry()
