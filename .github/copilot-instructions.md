## Quick orientation

This repository is a documentation site built with Hugo using the Docsy theme-as-a-module. The content lives under `content/en/`. The site is not a typical application repository — most work will touch Markdown content, Hugo templates (in `layouts/`), or static assets (`assets/`, `resources/`).

Keep these core entry points in mind:

- `package.json` — npm scripts for local dev and builds. Common commands:
  - `hugo serve`   — local dev server with live reload
  - `hugo`         — build static site into `public/`
  - `npm run test` — runs link checks and other tests
- `hugo.toml` / `config.yaml` — site configuration (content dir is `content/en`, `enableGitInfo = true`, Git branch is `main` via `github_branch`), also declares the Docsy module.
- `go.mod` — declares the Docsy Hugo module import. Do not vendor or modify the module import unless you know Hugo modules.
- `docker-compose.yaml` / `Dockerfile` — a small Docker setup that runs a Hugo server; useful if you prefer containerized local dev. `docker-compose up` will mount the repo and serve on 1313.

## What to prioritize for changes

- Content edits: modify or add Markdown files under `content/en/...`. Keep front-matter keys (title, description, weight) consistent with nearby pages.
- Templates and layout changes: modify files in `layouts/` or `partials/` and test locally with `npm run serve`.
- Assets: SCSS and JS are under `assets/` and processed by Hugo. Don't edit `public/` directly — it is generated.

## Project-specific conventions and gotchas

- Docsy as Hugo module: Docsy is imported through `module.imports` in `hugo.toml`; prefer configuration and layouts in this repo rather than editing the upstream Docsy module.
- Content language is `en` and lives in `content/en/`. When adding pages keep the path structure under `content/en/`.
- `enableGitInfo = true` — Hugo uses Git metadata for `.Lastmod` and related timestamps. Commits affect build metadata; run builds after committing when checking Lastmod changes.
- `public/` is the generated site output. The repo has a `make:public` helper script that initializes `public` as a git worktree if needed — be cautious when changing `public/`.

## Debugging, build, and test workflow

1. For quick local preview while editing content or templates:

   hugo serve

3. Containerized dev (if you prefer Docker):

   docker-compose up --build

   The service maps port `1313` and mounts the working directory to `/src` inside the container.

4. Link checking / tests: `npm run test` delegates to link checks. The link checks may be partially implemented in this repo; inspect `package.json` for any stubs.

## Useful file examples to reference

- `package.json` — shows the exact npm scripts used for serve/build/test (see top-level file).
- `hugo.toml` — site params, module imports, and `github_branch` (set to `main`).
- `content/en/labs/` — examples of lab content and front-matter conventions (weights, description, video embeds).
- `layouts/` and `assets/` — where to change the site HTML and styles.

## Example patterns an AI agent should follow when editing

- When adding new content pages, copy the front-matter style used by nearby pages (title, weight, description). Example: `content/en/labs/design/srp/_index.md` uses `title`, `weight`, and `description` fields.
- If editing templates, run `npm run serve` locally and verify the HTML rendering. Do not push template-only changes without a local check — small template errors can break builds.
- Prefer edits in `layouts/` or `assets/` over modifying the Docsy module upstream.

## Safety and merge guidance

- Don't modify `go.mod` or module imports unless required; Hugo modules are sensitive to versions. If a module update is needed, document the reason in the PR.
- Because `enableGitInfo` is true, prefer creating a small content commit to update `.Lastmod` rather than manually editing timestamps.

## Where to ask for clarification

- Use the repository issues for ambiguous content or policy changes (see `github_repo` in `hugo.toml`).

---
If you'd like, I can now: (1) merge this into the repo as `.github/copilot-instructions.md`, or (2) expand any section (build, Docker, or examples) with exact snippets from package.json or hugo.toml. Which would you prefer?
