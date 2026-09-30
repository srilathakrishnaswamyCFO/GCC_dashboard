"""Assemble the self-contained dashboard: template.html + data.json + vendor/chart.umd.js."""
import json, pathlib

root = pathlib.Path(__file__).parent
html = (root / "template.html").read_text()
html = html.replace("/*__CHARTJS__*/", (root / "vendor/chart.umd.js").read_text())
html = html.replace("/*__DATA__*/", json.dumps(json.loads((root / "data.json").read_text()), separators=(",", ":")))
out = root / "SGA_Summary_Dashboard_Aug_2026.html"
out.write_text(html)
print(f"wrote {out} ({out.stat().st_size/1024:.0f} KB)")
