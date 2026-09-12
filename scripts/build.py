"""Assemble index.html from the template and the data files. Run from anywhere: python3 scripts/build.py"""
import pathlib
root = pathlib.Path(__file__).resolve().parent.parent
t = (root/"scripts/template.html").read_text()
out = (t.replace("/*WORLD_JSON*/", (root/"data/world.json").read_text())
        .replace("/*TOURS_JSON*/", (root/"data/tours.json").read_text())
        .replace("/*COUNTRY_JSON*/", (root/"data/countries_pts.json").read_text()))
(root/"index.html").write_text(out)
print(f"wrote index.html ({len(out)//1024} KB)")
