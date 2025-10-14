#!/usr/bin/env python3
"""
json_cleanup.py
---------------
Combine all JSON course summaries into one Markdown file
and automatically read summaries from their referenced .txt files.

Usage:
    python json_cleanup.py <path_to_course_summaries>
Output:
    course_overview.md
"""

import os
import sys
import json


def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"⚠️ Failed to load {path}: {e}")
        return None


def read_summary_text(course_dir, summary_filename):
    """Try to read the summary .txt file if available."""
    if not summary_filename:
        return ""
    # Search in course directory subfolders (like Week_1, Week_2, etc.)
    for root, _, files in os.walk(course_dir):
        if summary_filename in files:
            summary_path = os.path.join(root, summary_filename)
            try:
                with open(summary_path, "r", encoding="utf-8") as f:
                    return f.read().strip()
            except Exception as e:
                return f"(⚠️ Could not read summary: {e})"
    return ""


def extract_course_markdown(course_dir, data):
    """Convert one course JSON into markdown, including .txt summaries."""
    title = data.get("course_title", "Untitled Course")
    modules = data.get("modules", {})

    lines = [f"# {title}", "", "## Table of Contents", ""]

    # Collect week numbers
    weeks = []
    for m_data in modules.values():
        for week_key in m_data.keys():
            if week_key not in weeks:
                weeks.append(week_key)

    for week in sorted(weeks, key=lambda x: int(x.split("_")[1])):
        lines.append(f"- [{week.replace('_', ' ').title()}](#{week.lower()})")
    lines.append("")

    # Now print full lesson content
    for m_data in modules.values():
        for week_key, week_info in sorted(m_data.items(), key=lambda x: int(x[0].split("_")[1])):
            lines.append(f"## {week_key.replace('_', ' ').title()}\n")

            for lesson in week_info.get("lessons", []):
                name = lesson.get("name", "")
                summary_file = lesson.get("summary_file")
                summary_text = read_summary_text(course_dir, summary_file)

                lines.append(f"### {name}\n")
                lines.append(summary_text if summary_text else "No summary available.")
                lines.append("\n---\n")

    return "\n".join(lines)


def combine_all_json(base_dir):
    """Combine all JSON files in a directory into one markdown file."""
    combined = ["# combined_all", "", "## Table of Contents", ""]

    for root, _, files in os.walk(base_dir):
        for file in files:
            if not file.endswith(".json"):
                continue
            json_path = os.path.join(root, file)
            data = load_json(json_path)
            if not data:
                continue

            print(f"📘 Processing {file}")
            md = extract_course_markdown(os.path.dirname(json_path), data)
            combined.append(md)
            combined.append("")

    out_path = os.path.join(base_dir, "course_overview.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(combined))
    print(f"\n✅ Combined Markdown written to {out_path}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python json_cleanup.py <folder_path>")
        sys.exit(1)

    base_dir = sys.argv[1]
    if not os.path.isdir(base_dir):
        print(f"❌ Directory not found: {base_dir}")
        sys.exit(1)

    combine_all_json(base_dir)


if __name__ == "__main__":
    main()
