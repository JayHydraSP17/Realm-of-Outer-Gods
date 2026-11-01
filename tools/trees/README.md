# Upgrade trees: approved v3 data

- `upgrade-trees.md`: the approved design (with the audit highlights still in it).
- `upgrade-trees.json`: the six character trees in the DM builder's export format.
- `md_to_trees.py`: rebuilds the JSON from the markdown: `python3 md_to_trees.py upgrade-trees.md upgrade-trees.json`

## Loading them
1. Open the DM console, go to **Trees**, and click **Export** first if you've built anything there you want to keep (Import replaces the whole draft).
2. Click **Import** and pick `upgrade-trees.json`.
3. Check the trees, then **Save** and **Publish**. Sheets and the Upgrade Trees page update right away.

The tree ids are `dylan-tree`, `sika-tree`, `magnolia-tree`, `beatrix-tree`, `yohan-tree`, `melissa-tree`. Each is owned by the matching sheet. Flat riders (AC, speed, HP, initiative) are set on the nodes. Sheets also look up a few nodes **by name** through `window.trRankOf(name)`, so keep these names if you edit the trees:
Sandstorm Surge, Bottoms Up, Quickened Seal, Swift Inscription, Ancient Script, Harvester Vine, Shooter Vine, Spike Vine, Alchemy Vine, Four Seasons, Sylvan Indulgence, Stocked Satchel, Hardy Seeds.
