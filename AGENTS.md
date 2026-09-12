# User Preferences & Workflow Guidelines

## Browser Automation & Web Tasks
- **Kimi WebBridge / Browser Extension**: Always use the local Kimi WebBridge daemon (`http://127.0.0.1:10086`) and extension to interact with web pages, apps, and services directly inside the user's real Google Chrome browser.
- **Account Setups & SSO**: When setting up new accounts or authenticating services (e.g., ElevenLabs, Higgsfield, and future platforms), use the user's active Google SSO session (`plskynech@gmail.com`) and complete onboarding flows autonomously end-to-end without requiring manual terminal intervention.

## Thesis & Document Review Marker Conventions (Odborná práce / Typst)
When working on the thesis manuscript (`mono-OdbornaPrace`), agents must strictly adhere to the visual review marker protocol:
- **Clean / Unmarked Text (No highlight / white background)**:
  - Represents finalized author text, verbatim student drafts, or text that has been reviewed, rewritten in the author's voice, and accepted.
  - Never wrap finalized text in highlight markers.
  - When the user requests to "remove marker", cleanly unwrap the text without altering its content or formatting.
- **Yellow Callout (`#alert[...]` / `#struct-alert[...]` — 📐 *Strukturální upozornění:* )**:
  - Highlights structural flaws, depth imbalances (e.g. 1-sentence subsections), missing component decompositions, topic duplications across chapters, outline mismatches, or underrepresented appendices.
  - Removed once the section or chapter structure is reorganized, expanded, or consolidated.
- **Yellow Highlight (`#ai[...]` / `#highlight(fill: yellow)[...]`)**:
  - Marks AI-generated drafts or expansions that have **not yet been reviewed or adopted** by the author.
  - Indicates that the text requires human scrutiny, verification, or rewording by the author.
  - Removed once the author approves or rewrites the passage.
- **Green Callout (`#note[...]` — 💡 *Návrh na vylepšení:*)**:
  - Highlights constructive improvement recommendations, structural enhancements, suggested diagrams, or practical connections to DarkFactory.
  - When a suggestion is incorporated, implement the change and delete the `#note[...]` callout block.
- **Red Callout (`#issue[...]` — ⚠️ *Chyba / Nesrovnalost k opravě:*)**:
  - Highlights factual inaccuracies, conceptual misconceptions (e.g., ReAct meaning "Read and Act" instead of "Reasoning and Acting"), terminology blunders, logical gaps, grammatical/typing errors, and duplicate content (e.g., duplicate config files across chapters).
  - Explicitly states the error and what needs correction.
  - Removed once the underlying defect is resolved in the manuscript.
- **Typst Formatting & Stability**:
  - Avoid fragile external diagramming packages that trigger runtime panics (e.g., incompatible Fletcher/CeTZ versions). Prefer clean vector SVGs in `img/`.
  - Watch out for escape sequences in Typst (e.g., do not use `\r` in math/text; use unicode `→` or `$arrow$`).
