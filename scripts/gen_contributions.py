#!/usr/bin/env python3
"""Generate a custom animated contribution heatmap SVG from live GitHub data.

Reads GH_TOKEN and GH_USER from the environment, queries the GitHub GraphQL
contributions calendar, and writes assets/contributions.svg — a brand-styled
animated heatmap with a diagonal wave-reveal, a live pulse on active days, and
a sweeping scanner line. Run locally or via the daily GitHub Action.
"""
import json
import os
import urllib.request

TOKEN = os.environ["GH_TOKEN"]
USER = os.environ.get("GH_USER", "29shivam")

QUERY = """
query($login:String!){
  user(login:$login){
    contributionsCollection{
      contributionCalendar{
        totalContributions
        weeks{ contributionDays{ contributionCount weekday } }
      }
    }
  }
}
"""

req = urllib.request.Request(
    "https://api.github.com/graphql",
    data=json.dumps({"query": QUERY, "variables": {"login": USER}}).encode(),
    headers={"Authorization": f"bearer {TOKEN}", "Content-Type": "application/json"},
)
resp = json.loads(urllib.request.urlopen(req).read())
cal = resp["data"]["user"]["contributionsCollection"]["contributionCalendar"]
total = cal["totalContributions"]
weeks = cal["weeks"]

CELL, GAP = 11, 3
PITCH = CELL + GAP
PAD_L, PAD_T = 22, 54
nweeks = len(weeks)
grid_w = nweeks * PITCH - GAP
grid_h = 7 * PITCH - GAP
W = PAD_L * 2 + grid_w
H = PAD_T + grid_h + 34

mx = max((dd["contributionCount"] for w in weeks for dd in w["contributionDays"]), default=1) or 1


def color(c):
    if c == 0:
        return "#1e293b"
    r = c / mx
    if r <= 0.2:
        return "#0c4a5e"
    if r <= 0.4:
        return "#0e7490"
    if r <= 0.7:
        return "#22d3ee"
    return "#67e8f9"


cells = []
for wi, w in enumerate(weeks):
    for dd in w["contributionDays"]:
        day = dd["weekday"]
        c = dd["contributionCount"]
        x = PAD_L + wi * PITCH
        y = PAD_T + day * PITCH
        # Cells are visible by default (robust without animation); active cells
        # "breathe" as a continuous enhancement when SMIL runs.
        pulse = ""
        if c > 0:
            pdur = round(2.4 + (wi % 5) * 0.15, 2)
            pbegin = round((wi + day) * 0.02, 3)
            pulse = (
                f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2.5" fill="{color(c)}">'
                f'<animate attributeName="opacity" values="1;0.5;1" dur="{pdur}s" '
                f'begin="{pbegin}s" repeatCount="indefinite"/></rect>'
            )
            cells.append(pulse)
        else:
            cells.append(f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2.5" fill="{color(c)}"/>')

s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" fill="none">']
s.append(
    '<defs>'
    '<linearGradient id="scan" x1="0%" y1="0%" x2="100%" y2="0%">'
    '<stop offset="0%" stop-color="#22d3ee" stop-opacity="0"/>'
    '<stop offset="50%" stop-color="#22d3ee" stop-opacity="0.55"/>'
    '<stop offset="100%" stop-color="#22d3ee" stop-opacity="0"/></linearGradient>'
    '<linearGradient id="acc" x1="0%" y1="0%" x2="100%" y2="0%">'
    '<stop offset="0%" stop-color="#22d3ee"/><stop offset="100%" stop-color="#818cf8"/></linearGradient>'
    '<filter id="g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="4"/></filter>'
    '</defs>'
)
s.append(f'<rect width="{W}" height="{H}" rx="12" fill="#0b1120"/>')
s.append(f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="#1e293b"/>')
s.append(
    f'<text x="{PAD_L}" y="30" font-family="Menlo, Consolas, monospace" font-size="17" font-weight="700" fill="#f8fafc">'
    f'<tspan fill="url(#acc)">{total}</tspan> contributions in the last year</text>'
)
s.extend(cells)
s.append(
    f'<rect x="{PAD_L}" y="{PAD_T}" width="26" height="{grid_h}" fill="url(#scan)" opacity="0.9" filter="url(#g)">'
    f'<animateTransform attributeName="transform" type="translate" from="-40 0" to="{grid_w} 0" '
    f'dur="4.5s" begin="2s" repeatCount="indefinite"/></rect>'
)
lx = W - PAD_L - 5 * (CELL + 4) - 60
ly = H - 16
s.append(f'<text x="{lx-8}" y="{ly+9}" font-family="Helvetica,Arial,sans-serif" font-size="11" fill="#64748b" text-anchor="end">Less</text>')
for i, cc in enumerate(["#1e293b", "#0c4a5e", "#0e7490", "#22d3ee", "#67e8f9"]):
    s.append(f'<rect x="{lx + i*(CELL+4)}" y="{ly}" width="{CELL}" height="{CELL}" rx="2.5" fill="{cc}"/>')
s.append(f'<text x="{lx + 5*(CELL+4) + 4}" y="{ly+9}" font-family="Helvetica,Arial,sans-serif" font-size="11" fill="#64748b">More</text>')
s.append("</svg>")

os.makedirs("assets", exist_ok=True)
open("assets/contributions.svg", "w").write("\n".join(s))
print(f"wrote assets/contributions.svg ({total} contributions, {W}x{H})")
