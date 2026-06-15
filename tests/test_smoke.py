from pathlib import Path

from agent_tripwire.main import demo, plant, scan


def test_plant_creates_canary_file(tmp_path: Path) -> None:
    target = plant(tmp_path)
    assert target.exists()
    assert "AGENTTRIPWIRE_GITHUB_TOKEN" in target.read_text(encoding="utf-8")


def test_demo_triggers_finding(tmp_path: Path) -> None:
    findings = demo(tmp_path)
    assert findings
    assert findings[0].name == "AGENTTRIPWIRE_GITHUB_TOKEN"


def test_scan_ignores_canary_source_file(tmp_path: Path) -> None:
    plant(tmp_path)
    assert scan(tmp_path) == []
