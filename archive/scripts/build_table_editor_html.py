#!/usr/bin/env python3
"""Generate an editable HTML table from templates/D-distilled-understanding-full.md.
Run this, then open templates/D-distilled-understanding-table-editor.html in a browser."""
import json
import re

MD_PATH = "templates/D-distilled-understanding-full.md"
OUT_HTML = "templates/D-distilled-understanding-table-editor.html"

with open(MD_PATH, "r", encoding="utf-8") as f:
    lines = f.readlines()

table_lines = [L for L in lines if L.strip().startswith("|") and L.strip().endswith("|")]

def parse_row(line):
    parts = [p.strip().replace("\\|", "|") for p in line.split("|")]
    if len(parts) < 3:
        return None
    return parts[1:-1]

rows = [parse_row(L) for L in table_lines if parse_row(L)]
if not rows:
    raise SystemExit("No table rows found")

# Escape for embedding in HTML: </script> and unicode
def embed_json(obj):
    s = json.dumps(obj, ensure_ascii=False)
    s = s.replace("</script>", "<\\/script>")
    s = s.replace("<script", "<\\u0073cript")
    return s

data_js = embed_json(rows)

html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>D. Distilled Understanding – Table Editor</title>
  <style>
    body { font-family: system-ui, sans-serif; margin: 12px; background: #1e1e1e; color: #ddd; }
    .toolbar { margin-bottom: 12px; display: flex; gap: 8px; align-items: center; flex-wrap: wrap; }
    .toolbar button { padding: 8px 14px; cursor: pointer; border-radius: 6px; border: 1px solid #555; background: #333; color: #eee; }
    .toolbar button:hover { background: #444; }
    .toolbar button.primary { background: #0a6; color: #fff; border-color: #0a6; }
    table { border-collapse: collapse; width: 100%; table-layout: fixed; font-size: 12px; }
    th, td { border: 1px solid #555; padding: 6px 8px; vertical-align: top; overflow: auto; max-height: 120px; }
    td[contenteditable="true"] { background: #2a2a2a; min-width: 60px; }
    td[contenteditable="true"]:focus { outline: 2px solid #0a6; outline-offset: -2px; }
    th { background: #333; position: sticky; top: 0; }
    tr:nth-child(even) td { background: #252525; }
    .status { color: #8f8; font-size: 13px; margin-left: 8px; }
    .instructions { margin-bottom: 12px; color: #999; font-size: 13px; }
  </style>
</head>
<body>
  <div class="instructions">
    Edit any cell in the table. Use <strong>Merge selected cells</strong> (select 2+ cells, then click) to merge. 
    <strong>Copy as Markdown</strong> copies the full table to the clipboard so you can paste into the .md file in Cursor.
  </div>
  <div class="toolbar">
    <button type="button" id="mergeBtn">Merge selected cells</button>
    <button type="button" id="unmergeBtn">Unmerge cell</button>
    <button type="button" id="copyMdBtn" class="primary">Copy as Markdown</button>
    <button type="button" id="downloadBtn">Download as .md</button>
    <span class="status" id="status"></span>
  </div>
  <div style="overflow: auto; max-height: calc(100vh - 140px);">
    <table id="tbl"></table>
  </div>
  <script>
    var TABLE_DATA = ''' + data_js + ''';
    var table = document.getElementById("tbl");
    var statusEl = document.getElementById("status");
    function showStatus(msg) { statusEl.textContent = msg; setTimeout(function(){ statusEl.textContent = ""; }, 3000); }
    function buildTable() {
      table.innerHTML = "";
      TABLE_DATA.forEach(function(row, ri) {
        var tr = document.createElement("tr");
        row.forEach(function(cell, ci) {
          var td = document.createElement(ri < 2 ? "th" : "td");
          td.contentEditable = "true";
          td.dataset.row = ri;
          td.dataset.col = ci;
          td.textContent = cell || "";
          tr.appendChild(td);
        });
        table.appendChild(tr);
      });
    }
    buildTable();
    document.getElementById("copyMdBtn").onclick = function() {
      var ncols = 0;
      for (var i = 0; i < table.rows[0].cells.length; i++) {
        var c = table.rows[0].cells[i];
        ncols += c.colSpan || 1;
      }
      var spanDown = [];
      for (var i = 0; i < ncols; i++) spanDown[i] = 0;
      var lines = [];
      for (var ri = 0; ri < table.rows.length; ri++) {
        var tr = table.rows[ri];
        var line = [];
        var col = 0;
        for (var ci = 0; ci < tr.cells.length; ci++) {
          var cell = tr.cells[ci];
          while (col < ncols && spanDown[col] > 0) {
            line.push("");
            spanDown[col]--;
            col++;
          }
          var content = (cell.textContent || "").trim().replace(/\\\\/g, "\\\\\\\\").replace(/\\|/g, "\\\\|");
          var cspan = cell.colSpan || 1;
          var rspan = cell.rowSpan || 1;
          line.push(content);
          for (var k = 1; k < cspan; k++) line.push("");
          for (var k = 0; k < cspan; k++) spanDown[col + k] = rspan - 1;
          col += cspan;
        }
        while (col < ncols) {
          line.push("");
          if (spanDown[col] > 0) spanDown[col]--;
          col++;
        }
        lines.push("| " + line.map(function(s){ return s; }).join(" | ") + " |");
      }
      var md = lines.join("\\n");
      navigator.clipboard.writeText(md).then(function() { showStatus("Copied to clipboard. Paste into your .md file."); });
    };
    document.getElementById("downloadBtn").onclick = function() {
      var ncols = 0;
      for (var i = 0; i < table.rows[0].cells.length; i++) ncols += table.rows[0].cells[i].colSpan || 1;
      var spanDown = [];
      for (var i = 0; i < ncols; i++) spanDown[i] = 0;
      var lines = [];
      for (var ri = 0; ri < table.rows.length; ri++) {
        var tr = table.rows[ri];
        var line = [];
        var col = 0;
        for (var ci = 0; ci < tr.cells.length; ci++) {
          var cell = tr.cells[ci];
          while (col < ncols && spanDown[col] > 0) { line.push(""); spanDown[col]--; col++; }
          var content = (cell.textContent || "").trim().replace(/\\\\/g, "\\\\\\\\").replace(/\\|/g, "\\\\|");
          var cspan = cell.colSpan || 1, rspan = cell.rowSpan || 1;
          line.push(content);
          for (var k = 1; k < cspan; k++) line.push("");
          for (var k = 0; k < cspan; k++) spanDown[col + k] = rspan - 1;
          col += cspan;
        }
        while (col < ncols) { line.push(""); if (spanDown[col] > 0) spanDown[col]--; col++; }
        lines.push("| " + line.join(" | ") + " |");
      }
      var md = lines.join("\\n");
      var a = document.createElement("a");
      a.href = "data:text/markdown;charset=utf-8," + encodeURIComponent(md);
      a.download = "D-distilled-understanding-full-table.md";
      a.click();
      showStatus("Downloaded.");
    };
    document.getElementById("mergeBtn").onclick = function() {
      var sel = window.getSelection();
      if (!sel.rangeCount) { showStatus("Select two or more cells first."); return; }
      var range = sel.getRangeAt(0);
      var cells = [];
      var walker = document.createTreeWalker(range.commonAncestorContainer, NodeFilter.SHOW_ELEMENT, null, false);
      var node;
      while (node = walker.nextNode()) {
        if (node.tagName === "TD" || node.tagName === "TH") cells.push(node);
      }
      if (cells.length < 2) {
        var start = range.startContainer;
        var el = start.nodeType === 3 ? start.parentElement : start;
        if (el && (el.tagName === "TD" || el.tagName === "TH")) cells = [el];
        var end = range.endContainer;
        var el2 = end.nodeType === 3 ? end.parentElement : end;
        if (el2 && (el2.tagName === "TD" || el2.tagName === "TH") && el2 !== el) cells.push(el2);
      }
      cells = cells.filter(function(c, i, a) { return a.indexOf(c) === i; });
      if (cells.length < 2) { showStatus("Select two or more cells (e.g. drag or Shift+click)."); return; }
      var first = cells[0];
      var firstRow = first.parentNode.rowIndex;
      var firstCol = first.cellIndex;
      var last = cells[cells.length - 1];
      var lastRow = last.parentNode.rowIndex;
      var lastCol = last.cellIndex;
      var rowspan = lastRow - firstRow + 1;
      var colspan = lastCol - firstCol + 1;
      var text = first.textContent.trim();
      for (var i = 1; i < cells.length; i++) {
        text += " " + (cells[i].textContent || "").trim();
        cells[i].parentNode.removeChild(cells[i]);
      }
      first.rowSpan = rowspan;
      first.colSpan = colspan;
      first.textContent = text;
      showStatus("Merged " + cells.length + " cells.");
    };
    document.getElementById("unmergeBtn").onclick = function() {
      var sel = window.getSelection();
      var node = sel.anchorNode;
      var el = node && node.nodeType === 3 ? node.parentElement : node;
      if (!el || (el.tagName !== "TD" && el.tagName !== "TH")) { showStatus("Click inside a merged cell to unmerge."); return; }
      var r = el.rowSpan || 1, c = el.colSpan || 1;
      if (r <= 1 && c <= 1) { showStatus("Cell is not merged."); return; }
      var tr = el.parentNode;
      var isTh = el.tagName === "TH";
      var tag = isTh ? "th" : "td";
      el.rowSpan = 1;
      el.colSpan = 1;
      for (var cr = 0; cr < r; cr++) {
        var row = cr === 0 ? tr : tr.parentNode.rows[tr.rowIndex + cr];
        for (var cc = (cr === 0 ? 1 : 0); cc < c; cc++) {
          var newCell = document.createElement(tag);
          newCell.contentEditable = "true";
          newCell.textContent = "";
          row.insertBefore(newCell, row.cells[el.cellIndex + (cr * c) + cc]);
        }
      }
      showStatus("Unmerged.");
    };
  </script>
</body>
</html>
'''

with open(OUT_HTML, "w", encoding="utf-8") as f:
    f.write(html)
print("Wrote", OUT_HTML)
print("Open this file in your browser (Chrome, Firefox, Safari) to edit the table.")
print("Use 'Copy as Markdown' then paste the table section into D-distilled-understanding-full.md in Cursor.")