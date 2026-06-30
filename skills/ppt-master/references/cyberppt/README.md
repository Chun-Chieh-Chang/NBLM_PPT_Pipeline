# CyberPPT Reference Files

This directory contains the ported reference files from the [CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) project (MIT License).

These files provide MBB-standard evidence analysis, SCR argumentation, visual system specifications, and hybrid PPTX reconstruction strategies for consulting-style presentations.

## Files

| File | Purpose | Integration Point |
|------|---------|-------------------|
| `source-analysis.md` | MBB evidence table, conflict handling, missing info management | Strategist Phase 1 - Evidence Analysis |
| `storyline.md` | SCR argumentation, page architecture, conclusion title testing | Strategist Phase 1 - Storyline Convergence |
| `visual-system.md` | 8 fixed palettes, grid systems, typography hierarchy, density rules | Style Selection Gate |
| `ppt-production.md` | Hybrid reconstruction strategy, complex visual asset admission, editable layer requirements | Executor Phase 3 |
| `quality-assurance.md` | Dual hard gates (editability + visual semantics), 14-layer QA门禁 | Post-Processing Validation |

## Usage

These references are consumed by the standalone `consultant-ppt.md` workflow. When the user requests consulting-style PPT with high information density, the system will:

1. Read all references in this directory before any execution
2. Apply the evidence table format from `source-analysis.md`
3. Generate SCR argumentation per `storyline.md`
4. Lock visual system per `visual-system.md`
5. Execute hybrid reconstruction per `ppt-production.md`
6. Validate with dual gates per `quality-assurance.md`

## License

Original CyberPPT content is licensed under MIT License. See `projects/_temp_cyberppt/LICENSE` for full text.
