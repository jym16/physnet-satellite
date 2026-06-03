# Edition template update

The data-driven edition template `templates/edition.qmd.j2` was rewritten to follow the uploaded Quarto Markdown structure.

Main changes:

- Uses `:::{ .landing-title }` for the title block.
- Uses `.event-summary` for date, time, venue, and room.
- Uses `.speaker-grid` and `.speaker-card .with-photo` for speakers.
- Uses `.program-list` and `.program-item` for the schedule.
- Uses collapsible `<details><summary>Abstract</summary>` blocks.
- Uses `.keyword-list`, `.organizer-grid`, and `.archive-note`.
