---
description: Pre-pipeline enrichment step powered by Google NotebookLM. Use when the user wants Gemini's grounded analysis, multi-source synthesis, or structured artifact generation as input to PPT Master. Produces Markdown documents that feed directly into SKILL.md Step 1's source conversion.
---

# NotebookLM Enhancement Workflow

> Standalone pre-processing step. Run **before** SKILL.md Step 1 (Source Content Processing) when the user explicitly requests NotebookLM-powered research, synthesis, or artifact generation. Output is Markdown / CSV / JSON shaped to feed `project_manager.py import-sources` directly.

This workflow is **independent**: it owns the source-enrichment step; subsequent SKILL.md steps proceed normally with the produced materials as input.

## When to Run

| User request | Action |
|---|---|
| "use notebooklm", "run notebooklm-enhance", "let Gemini analyze this first", "use notebooklm to synthesize" | Run this workflow |
| "do deep research on [topic]", "summarize these sources with citations", "generate a briefing doc" | Run this workflow |
| Source already in Markdown / PDF / DOCX form, no enhancement requested | Skip — go to SKILL.md Step 1 |
| User only provides a topic name (no files) | Run [`topic-research`](./topic-research.md) instead — it uses IDE web tools which are faster for light research |

## Prerequisites

### 1. Install notebooklm-py

```bash
pip install "notebooklm-py[browser]"
```

On Python 3.13+:

```bash
pip install "notebooklm-py[browser]"
if python -c "import sys; sys.exit(0 if sys.version_info < (3, 13) else 1)"; then
  pip install "notebooklm-py[cookies]"
else
  echo "Skipping [cookies] on Python 3.13+ (rookiepy unavailable). Use 'notebooklm login' interactively."
fi
```

### 2. Authenticate

```bash
notebooklm login   # Opens browser for Google OAuth
notebooklm list    # Verify authentication works
```

If commands fail with auth errors, re-run `notebooklm login`.

### 3. Verify Auth

```bash
notebooklm auth check --test --json
# Expect BOTH "status": "ok" AND "checks.token_fetch": true
```

---

## Step 1: Confirm Enhancement Scope

⛔ **BLOCKING**: present the enhancement scope as a single bundled clarifier and wait for explicit user confirmation.

| Item | Default if user did not specify |
|---|---|
| Input sources | All files in `<project_path>/sources/` (from SKILL.md Step 1 import) |
| Analysis type | `ask` (cited Q&A + structured summary) |
| Artifact types | None by default (user selects) |
| Output language | Match user input |
| Output directory | `<project_path>/notebooklm_output/` |

**Forbidden — itemized confirmation**: do NOT ask each row separately. One bundled clarifier or none.

---

## Step 2: Create Notebook and Add Sources

```bash
# Create a dedicated notebook for this project
notebooklm create "PPT-Enhance: <project_name>"
# Note the notebook_id from output
```

Add sources (choose based on available materials):

| Source Type | Command |
|---|---|
| Local file (PDF / DOCX / MD / TXT) | `notebooklm source add ./path/to/file.pdf` |
| URL | `notebooklm source add "https://..."` |
| YouTube video | `notebooklm source add "https://youtube.com/..."` |
| Google Drive file | `notebooklm source add drive:<file_id>` |
| Pasted text | `notebooklm source add --text "content here"` |

Wait for all sources to finish processing:

```bash
notebooklm source wait <source_id_1> <source_id_2> ...
```

**✅ Checkpoint**: All sources show `ready` status. Proceed to Step 3.

---

## Step 3: Choose Enhancement Actions

Present the following action categories and let the user select one or more. Each action produces distinct artifacts:

### A. Cited Q&A (`ask`)

Best for: extracting key insights, answering specific questions, getting structured summaries with source citations.

```bash
# Single question
notebooklm ask "What are the 5 most important findings? List them with source citations."

# Save answer as note
notebooklm ask "Summarize the strategic recommendations." --save-as-note --note-title "Strategic Recommendations"

# With references (JSON format for machine parsing)
notebooklm ask "Extract all quantitative data points mentioned." --json
```

**Output**: Structured text with citations → save to `<project_path>/notebooklm_output/qa_<N>.md`

### B. Generate Report (`generate report`)

Best for: comprehensive briefing documents, study guides, blog-style overviews.

```bash
# Briefing document
notebooklm generate report --format briefing-doc --wait

# Study guide
notebooklm generate report --format study-guide --wait

# Custom prompt
notebooklm generate report --prompt-file instructions.txt --wait
```

**Output**: Markdown report → save to `<project_path>/notebooklm_output/report.md`

### C. Generate Quiz / Flashcards

Best for: knowledge validation, study material, generating structured content for slide layouts.

```bash
# Generate quiz
notebooklm generate quiz --wait

# Generate flashcards
notebooklm generate flashcards --wait
```

**Download formats**:
```bash
# Quiz as JSON
notebooklm download quiz ./notebooklm_output/quiz.json

# Quiz as Markdown
notebooklm download quiz --format markdown ./notebooklm_output/quiz.md

# Flashcards as JSON
notebooklm download flashcards ./notebooklm_output/flashcards.json
```

### D. Generate Slide Deck

Best for: getting a quick PPTX draft from NotebookLM's Gemini (can be used as reference or starting point).

```bash
notebooklm generate slide-deck --wait
notebooklm download slide-deck ./notebooklm_output/slides.pptx --format pptx
```

**Note**: This produces a separate PPTX via NotebookLM, NOT the PPT Master pipeline output. Useful for comparison or inspiration.

### E. Web Research (`source add-research`)

Best for: supplementing existing sources with fresh web data.

```bash
# Fast mode
notebooklm source add-research "latest market trends in <industry>"

# Deep mode (more thorough, takes longer)
notebooklm source add-research "competitor analysis 2025" --mode deep --wait
```

**Output**: New sources added to the notebook → proceed to Step 3 again for new Q&A.

### F. Source Fulltext Extraction

Best for: getting raw text from processed sources for direct use in PPT Master.

```bash
notebooklm source fulltext <source_id> > ./notebooklm_output/source_fulltext.md
```

---

## Step 4: Collect and Organize Outputs

All outputs land in `<project_path>/notebooklm_output/`:

```
notebooklm_output/
├── qa_1.md                    # Q&A answers with citations
├── qa_2.md
├── report.md                  # Generated briefing/study guide
├── quiz.json                  # Quiz data
├── flashcards.json            # Flashcard data
├── slides.pptx                # Optional NotebookLM-generated deck
├── source_fulltext.md         # Extracted raw text
└── notes/                     # Saved chat notes
    ├── strategic_recommendations.md
    └── key_findings.md
```

**Organize for PPT Master consumption**:

1. Merge all `.md` files into a single enriched source document:
   ```bash
   cat notebooklm_output/qa_*.md notebooklm_output/report.md > <project_path>/sources/enriched_sources.md
   ```

2. Keep original sources intact — NotebookLM outputs are **additive**, not replacements.

3. Update the design spec to note which insights came from NotebookLM (for traceability).

---

## Step 5: Hand-off to Main Pipeline

Output a checkpoint, then continue with SKILL.md Step 1:

```markdown
## ✅ NotebookLM Enhancement Complete
- [ ] Notebook created: "<notebook_title>" (<notebook_id>)
- [ ] Sources added: N files / URLs
- [ ] Enhancement actions completed: A, B, C (select from Step 3)
- [ ] Outputs saved to: <project_path>/notebooklm_output/
- [ ] Enriched source merged: <project_path>/sources/enriched_sources.md
- [ ] **Next**: SKILL.md Step 1 →
  `python3 ${SKILL_DIR}/scripts/project_manager.py init <project_name> --format <format>`
  `python3 ${SKILL_DIR}/scripts/project_manager.py import-sources <project_path> <source_files...> --move`
```

> **Important**: The enriched source document feeds into Step 1's source conversion pipeline. PPT Master will process it through the appropriate converter (`pdf_to_md.py`, `doc_to_md.py`, or direct read for Markdown).

---

## Integration Points with PPT Master

### With Strategist Phase (Step 4)

NotebookLM's cited Q&A and reports provide the Strategist with:
- Pre-analyzed key insights with source citations
- Structured summaries ready for Eight Confirmations
- Quantitative data points extracted from verbose sources
- Alternative perspectives from multi-source synthesis

### With Image Acquisition (Step 5)

NotebookLM can help identify which concepts need visual representation:
- Key metrics → chart templates
- Process flows → diagram templates
- Comparative data → bar/pie/radar charts

### With Topic Research (Pre-SKILL.md)

When the user has source files but wants deeper analysis:
- `topic-research` gathers raw web materials (no auth needed)
- `notebooklm-enhance` synthesizes those materials with Gemini (requires auth)
- Use sequentially: topic-research → notebooklm-enhance → main pipeline

---

## Limitations & Caveats

1. **Rate limits**: Google imposes rate limits on NotebookLM API calls. For large decks with many sources, batch operations and add delays between actions.

2. **Auth required**: Unlike PPT Master's built-in `topic-research` (which uses IDE web tools), NotebookLM requires Google OAuth authentication. Not suitable for headless / CI environments without `NOTEBOOKLM_AUTH_JSON`.

3. **Source count caps**: Per-notebook source limits depend on your Google account tier. Split across notebooks if you hit a cap.

4. **No image generation**: NotebookLM does not produce images. Visual assets still come from PPT Master's `image_gen.py` or `image_search.py`.

5. **Output format**: NotebookLM generates its own PPTX separately from PPT Master. Use it for reference only — the final editable PPTX always comes from PPT Master's pipeline.

6. **Cost**: NotebookLM uses Google's infrastructure. While currently free with Google accounts, API usage may incur costs in the future.

---

## Parallel Safety

When running multiple agents that share NotebookLM:

- Use explicit notebook IDs: `notebooklm -n <notebook_id> ask "..."`
- Or use profiles: `export NOTEBOOKLM_PROFILE=ppt-master-<project_id>`
- See notebooklm-py docs for multi-account setup

---

## License

Original notebooklm-py content is licensed under MIT License.
See: https://github.com/teng-lin/notebooklm-py
