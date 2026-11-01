"""Turn the approved upgrade-trees markdown into a DM tree-builder import file.
Usage: python3 md_to_trees.py upgrade-trees.md out.json
The output is the builder's export format ({trees:{id:tree}, order:[ids]}); load it with Trees > Import."""
import json, re, sys

OWNER = {"Dylan": "dylan", "Sika": "sika", "Magnolia": "magnolia", "Beatrix": "beatrix", "Yohan": "yohan", "Melissa": "melissa"}
KIND = {"passive": "passive", "action": "action", "bonus action": "bonus", "reaction": "reaction", "attack": "attack", "free": "free"}
# numeric riders the sheets apply automatically (per rank)
MODS = {"Hardened Hide": {"ac": 1}, "Thick Skin": {"hp": 15}, "Quick Draw": {"init": 2}, "Desert Stride": {"speed": 5},
        "Sunlit Reflexes": {"init": 2}, "Swift Current": {"speed": 5}, "Tidal Reflex": {"init": 2}}

def clean(t):
    t = re.sub(r"~~.*?~~\s*", "", t)                     # drop struck-out old text
    t = re.sub(r"</?mark>", "", t).replace("✏️", "")
    t = t.replace("\\*", "\u2217")                  # escaped asterisk (Verdant*) survives emphasis parsing
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", t)
    t = t.replace("\u2217", "*")
    return re.sub(r"\s+", " ", t).strip()

def plain(t):
    return re.sub(r"<[^>]+>", "", clean(t)).strip()

def cells(line):
    parts = [c.strip() for c in line.strip().strip("|").split("|")]
    return parts

def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def parse(md):
    trees, order = {}, []
    blocks = re.split(r"\n#{1,2} (?=(?:Dylan|Sika|Magnolia|Beatrix|Yohan|Melissa) — )", md)
    for b in blocks[1:]:
        head = b.split("\n", 1)[0]
        who, title = [x.strip() for x in head.split("—", 1)]
        title = re.sub(r"\s*\(.*\)$", "", title)
        m = re.search(r"\*\*Overall: (.+?) · A: (.+?) · B: (.+?)\*\*", b)
        ovdesc, aname, bname = m.group(1), m.group(2).strip(), m.group(3).strip()
        tid = who.lower() + "-tree"
        t = {"kind": "char", "name": who + " — " + title, "owner": OWNER[who], "desc": "",
             "cols": [{"id": "ov", "name": "Overall", "role": "overall", "desc": ovdesc[0].upper() + ovdesc[1:]},
                      {"id": "a", "name": aname, "role": "build", "desc": ""},
                      {"id": "b", "name": bname, "role": "build", "desc": ""}],
             "rungs": [{"lvl": 0, "ov": 0, "cost": 1}, {"lvl": 0, "ov": 2, "cost": 2}, {"lvl": 15, "ov": 5, "cost": 3}, {"lvl": 20, "ov": 9, "cost": 4}],
             "caps": {}, "nodes": []}
        sec = None
        for line in b.split("\n"):
            if line.startswith("### Overall"): sec = "ov"; continue
            if line.startswith("### Build A"): sec = "a"; continue
            if line.startswith("### Build B"): sec = "b"; continue
            if line.startswith("##") or line.startswith("---"):
                if line.startswith("### ") or line.startswith("## ") or line.startswith("---"): sec = None if not line.startswith("### Build") else sec
                continue
            if not sec or not line.startswith("|") or re.match(r"\|\s*-", line) or re.match(r"\|\s*(#|Rung)\s*\|", line):
                continue
            c = cells(line)
            typ = None
            if len(c) == 5:
                pos, name, typ, ranks, eff = c
            else:
                pos, name, ranks, eff = c[:4]
            nm = plain(name)
            nm = re.sub(r"\s*\((effectiveness|damage types|form|structure)\)$", "", nm)
            kind = "passive"
            if typ:
                tk = plain(typ).split("·")[0].strip().lower()
                kind = KIND.get(tk, "passive")
                cost_note = plain(typ).split("·")[1].strip() if "·" in plain(typ) else ""
            else:
                cost_note = ""
            text = clean(eff)
            if not typ:
                low = plain(eff).lower()
                if low.startswith("bonus action"): kind = "bonus"
                elif low.startswith("as an action") or ", as an action" in low[:60]: kind = "action"
            if cost_note:
                text = "<b>" + cost_note + ".</b> " + text
            if pos.strip() == "◆":
                t["caps"][sec] = {"n": nm, "k": kind, "text": text}
                continue
            rk = plain(ranks)
            lvl = 0
            lm = re.search(r"Level\s+(\d+)", rk)
            if lm: lvl = int(lm.group(1))
            rn = int(re.findall(r"\d+", rk)[0]) if re.findall(r"\d+", rk) else 1
            node = {"id": slug(who + "-" + sec + "-" + nm)[:40], "col": sec, "n": nm, "k": kind, "ranks": rn, "text": text, "req": [], "mods": MODS.get(nm, {})}
            if sec == "ov":
                node["cost"] = 1
                if lvl: node["lvl"] = lvl
            else:
                node["rung"] = int(pos)
            t["nodes"].append(node)
        trees[tid] = t
        order.append(tid)
    return {"trees": trees, "order": order}

if __name__ == "__main__":
    md = open(sys.argv[1], encoding="utf-8").read()
    md = md.split("\n## Change list")[0]
    out = parse(md)
    json.dump(out, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for k in out["order"]:
        t = out["trees"][k]
        cnt = {c: len([n for n in t["nodes"] if n["col"] == c]) for c in ("ov", "a", "b")}
        print(k, cnt, "caps:", list(t["caps"]))
