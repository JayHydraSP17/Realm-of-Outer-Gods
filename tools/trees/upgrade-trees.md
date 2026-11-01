# Upgrade Trees — suggested drafts (v3: audit fixes)

**Every node here is a suggestion.** Rename, rebalance or cut anything.

> **How to read this version:** every change from the audit is wrapped in <mark>✏️ highlighted text</mark>. Text that was removed is shown as ~~struck through~~ right before its replacement. The change list at the bottom has every edit in one place, so you can approve or reject them one at a time.

## Rules recap
- **Any node can have ranks**, shown on the circle as 1/3 → 2/3 → 3/3, like Rivals.
- **Rank costs**
  - **Overall:** every rank costs 1 point.
  - **Build rungs:** rank 1 costs the rung's price (1 / 2 / 3 / 4). **Each extra rank costs 1 point.**
  - You can change the extra-rank cost on any node in the builder.
- **Locks and gates** look at rank 1 only. Taking the first rank of a rung locks its partner, and one rank on the rung before opens the next rung. Capstones need rank 1 on all 4 rungs of a build.
- **Per-rank text:** "per rank" means the same bonus each time. Where the ranks do different things, they're listed as **R1 / R2 / R3**.
- **Rank parity:** both rungs in a pair have the same number of ranks. <mark>✏️ Every pair now matches.</mark>

**Budget:** each Overall track is about **20 points** (rung 4 needs 9). A build with every rank maxed costs about **15**, so a fully built character runs around **35 points**.

---

## Dylan — The Flagbearer of Betrayal
**Overall: tanking (AC, HP, damage taken, damage dealt) · A: Flag · B: Betrayal**

### Overall
| # | Name | Type | Ranks | Effect |
|---|---|---|---|---|
| 1 | **Hardened Hide** | Passive | 3 | **+1 AC** per rank. |
| 2 | **Thick Skin** | Passive | 3 | **+15 max HP** per rank. |
| 3 | **Bescyl's Weight** | Passive | 3 | Destructive Aftershock **+2** per rank. |
| 4 | **Grit** | Passive | 3 | Unyielding grants **+10 temp HP** per rank. |
| 5 | **Blood Price** | Passive | 3 | Fervid Vengeance bonus **+1** per rank at every threshold. |
| 6 | **Pain Ledger** | Passive | 2 | R1: once per round, when a single hit deals 20% of max HP damage, regain **1 battle die**. R2: the threshold drops to 10%. |
| 7 | **Steadfast** | Passive | 1 | Advantage on saves against being knocked prone or forcibly moved. |
| 8 | **Last One Standing** | Passive | 1 · **Level 15** | Bloodthirsty Resolve recharges on a short rest. |

### Build A — Flag
| Rung | Name | Ranks | Effect |
|---|---|---|---|
| 1 | **Deserter's Mire** | 3 | **R1:** unlocks the aura (15 TL). ◄ Allies may Disengage as a free action and ignore the first opportunity attack against them each round. Enemies ► the first time an enemy tries to leave the aura each turn, it is tethered (STR save ends) ~~regaining Dylan 1 battle die~~ <mark>✏️ and Dylan regains 1 battle die</mark>. Trait: Dylan's speed is halved. **R2:** DC increases by PB. **R3:** Allies ignore the first two opportunity attacks. |
| 2 | **Oathbreaker's Toll** | 3 | **R1:** unlocks the aura (30 TL). ◄ When an enemy in the aura dies, every ally regains 1 reaction. Enemies ► when an ally in the aura dies, every enemy loses 1 reaction until the end of its next turn. Trait: Dylan cannot take reactions. **R2:** ~~Reaction reduction increase +1.~~ <mark>✏️ When an enemy in the aura dies, allies also gain +PB on their next attack.</mark> **R3:** ~~Reaction reduction increase +1.~~ <mark>✏️ Enemies who lose a reaction also have disadvantage on Dodge, Block and Parry until the end of their next turn.</mark> |
| 3 | **Coward's Crown** | ~~2~~ <mark>✏️ 3</mark> | **R1:** unlocks the aura (30 TL). ◄ Allies are immune to Frightened and have advantage on saves against forced movement. Enemies ► enemies save against Frightened (Dylan's DC) at the start of each of their turns; Frightened enemies have their speed halved. Trait: Dylan has disadvantage on attacks against any creature that isn't Frightened. **R2: Bravery's Throne:** creatures that aren't Frightened lose Dylan's PB on attack rolls not made against him. <mark>✏️ **R3:** Frightened enemies in the aura take Dylan's PB in psychic damage at the start of their turns, and the aura costs 10 TL less.</mark> |
| 4 | **Martyr's Standard** | 2 | **R1:** unlocks the aura (45 TL). ◄ Damage that would drop an ally to 0 HP leaves them at 1 instead; the excess goes to Dylan. Enemies ► enemies cannot be healed or gain temp HP. Trait: Dylan gains no benefit from resistances or temp HP. **R2:** aura radius **20 → 30 ft**. |
| ◆ | **Banner of Many Treasons** | — | Can plant two auras at once, carrying both traits. Unlocks **Pyrrhic Parade** (50 TL): ◄ allies' crits spill over, dealing the same damage to a second creature within the aura; Enemies ► enemies' crits against allies become normal hits; trait: Dylan can't score crits. |

### Build B — Betrayal
| Rung | Name | Type | Ranks | Effect |
|---|---|---|---|---|
| 1 | **Turncoat's Toll** | Bonus action | 3 | Dylan takes **10% of max HP** as true damage and regains **1 battle die** and **10 TL**. **Per extra rank: +5 TL.** |
| 2 | **Blood Pact** | Bonus action | ~~2~~ <mark>✏️ 3</mark> | ~~An ally~~ <mark>✏️ A willing ally</mark> within 10 ft loses 10% of its max HP. Dylan gains that much temp HP. **R2:** works on two allies at once. **R3:** the sacrificed health rises to 20%. |
| 3 | **I Can Do Worse** | Passive | 3 | *I Can Do Better* deals **+1d6 psychic per rank** on top of its +2d6. **R3:** it skips its cooldown if Dylan hurt himself or an ally with a Betrayal ability this round. |
| 4 | **Traitor's Crown** | Passive | 2 | Each time Dylan or an ally loses 10% HP from a Betrayal ability, Dylan gains +1 Treachery. His next attack gains +10% damage per Treachery (max 5). <mark>✏️ That attack spends all his Treachery.</mark> **R2:** max Treachery **7**. |
| ◆ | **Absolution** | Action | — | Once per long rest: all HP that Dylan and his allies paid to his Betrayal abilities this combat is dealt as true damage, split among enemies in his flag's radius. |

---

## Sika — Mindful Melodies
**Overall: range, effectiveness and duration of melodies · A: Waste Cycle · B: Telepathy**

### Overall
| # | Name | Ranks | Effect |
|---|---|---|---|
| 1 | **Carrying Tune** | 3 | Melody range **+5 ft** per rank (30 → 45 ft). |
| 2 | **Deep Breath** | 3 | **+5 max MP** per rank. |
| 3 | **Crescendo** | 3 | Melody Factor **+4** per rank. |
| 4 | **Practiced Hymns** | 3 | Per rank, choose one hymn: it costs **1 MP less** (min 1). |
| 5 | **Sweeter Melody** | 3 | Sweet Melody heals **+5% of max HP** per rank. |
| 6 | **Long Verse** | 2 | A Masterful Performer pairing lasts **+1 round** per rank. |
| 7 | **Second Voice** | 2 | An extra hymn in the same turn costs **+3 → +2 → +1 MP**. |
| 8 | **Duet** | 1 · **Level 15** | Switching Melodies costs no action, and the new Melody starts free once per combat. |

### Build A — Waste Cycle
| Rung | Name | Type | Ranks | Effect |
|---|---|---|---|---|
| 1 | ~~**Hold Your Liquor**~~ <mark>✏️ **Bottoms Up**</mark> | Passive | 3 | ~~+1 safe drink per rank before she gets Dizzy.~~ <mark>✏️ **R1:** once per turn, when she plays a hymn, she can drink as part of it without using her bonus action. She enters Wasted after drinking **more than four times** instead of three. **R2:** she enters Wasted after drinking **more than five times** (Wasted on the 6th drink), and each drink gives **+8 MP** instead of +5. **R3:** at the start of each combat, if her tally is below 2, it becomes **2**. *Two drinks in one round: the MP stacks, but the CHA doubling and the extra free hymn don't.*</mark> |
| 2 | **Liquid Courage** | Passive | 3 | While she's Dizzy, allies gain +2 to attack rolls. **R2:** ~~Allies gain advantage on attack rolls.~~ <mark>✏️ While she's Dizzy, allies' crit range expands by 1.</mark> **R3:** allies gain +10 Morale at the start of their turn. |
| 3 | **Bar Fight Ballad** | Action | 3 | While Dizzy, each creature within 15 ft makes a CON save or becomes Dizzy (Tier I). Her drink tally resets to 0. **R2:** radius increases to 20 ft. **R3:** Dizzy creatures make a CON save or become Nauseous; the next attack against a Nauseous creature deals Melody Factor damage. |
| 4 | **Hair of the Dog** | Reaction | 2 | When she would become Nauseous, drink instead: no Nauseous, **+10 MP**, and she stays Dizzy. **R2: +15 MP**. |
| ◆ | **Spitting Rhymes** | Passive | — | Once per long rest while Wasted: for 3 rounds every hymn plays at **double effect** and a failed Wasted save can't end her Melody. |

### Build B — Telepathy
| Rung | Name | Type | Ranks | Effect |
|---|---|---|---|---|
| 1 | **Mind Link** | Bonus action · 3 MP | 3 | Link allies telepathically for 1 minute: they can communicate in their heads and share sight (ends if ~~Sika loses concentration~~ <mark>✏️ Sika is incapacitated</mark>). **2 allies, +1 per rank**. |
| 2 | ~~**Intrusive Thought**~~ <mark>✏️ **Second Guess**</mark> | Reaction · 5 MP | 3 | When a creature within 60 ft attacks: WIS save or it has disadvantage and the damage is reduced by 10%. The reduction increases by 5% per rank. |
| 3 | **Thought Theft** | Action · 10 MP | ~~2~~ <mark>✏️ 3</mark> | Choose a creature within 20 ft: WIS save or it loses 5 MP, TL or Ki; ~~Sika gains half as MP (rounded down)~~ <mark>✏️ Sika gains that much MP</mark>. **R2:** it loses 10. **R3:** it loses 15, and the loss comes off its max. |
| 4 | ~~**Shared Mind** (1 rank): when a linked creature fails a mental save, another linked creature (or Sika) can make it instead.~~ <mark>✏️ **Shared Resolve**</mark> | Passive | <mark>✏️ 2</mark> | <mark>✏️ **R1:** once per round, when a linked creature would drop a Morale tier, Sika can spend **5 MP** to hold it: its Morale stops at the bottom of its current tier instead. **R2:** linked creatures can lose at most **20** Morale per round from other creatures' effects (the Swing Cap is normally 30).</mark> |
| ◆ | **Psychic Symphony** | Passive | — | While Mind Link holds 3+ creatures, each hymn also deals **Melody Factor** psychic damage to one enemy in range (once per turn). |

---

## Magnolia — The Radiant Tempest
**Overall: spell range and the fans · A: Aeromancer · B: Perfect Casting**

> Slots and uses belong only to Perfect Casting.

### Overall
| # | Name | Ranks | Effect |
|---|---|---|---|
| 1 | **Long Throw** | 3 | Twin Gales thrown range **+10 ft** per rank. |
| 2 | **Honed Edges** | 3 | Twin Gales damage **+2** per rank. |
| 3 | ~~**voluptuous Body**~~ <mark>✏️ **Allure**</mark> | 3 | ~~Flirtatious DC increases +1 per rank.~~ <mark>✏️ **+1** per rank to her Persuasion roll for Flirtatious.</mark> |
| 4 | **Focused Mind** | 3 | **+2** to concentration saves per rank. |
| 5 | **Quick Draw** | 3 | **+2 initiative** per rank. |
| 6 | **Gale Step** | 2 | R1: Ride the Winds doesn't provoke. R2: Ride the Winds **+15 ft**. |
| 7 | ~~**Wind Sheer**~~ <mark>✏️ **Wind Shear**</mark> | 1 | A creature with a fan swirling around it takes 1 fan weapon die slashing per fan at the start of its turn. |
| 8 | **Tempest Conduit** | 1 · **Level 15** | Spells she casts through the Twin Gales can originate from a swirling fan as if she stood there. ~~Tange~~ <mark>✏️ Range</mark> and area are measured from the fan. |

### Build A — Aeromancer
| Rung | Name | Type | Ranks | Effect |
|---|---|---|---|---|
| 1 | **Fan Lift** | Reaction | 3 | **R1:** when a creature within 15 ft hits her with a melee attack, she flicks a fan beneath it: STR save (her spell DC) or it is **Launched**. The fan returns to her hand. **R2:** the fan rises with it: she makes a free fan strike against it midair (it counts as a juggle hit). **R3:** range **30 ft**, and it also triggers on ranged attacks. |
| 2 | **Square Wave** | Attack | 3 | **R1:** replaces one attack: she rides the wind up to **20 ft** in a straight line (no opportunity attacks) and strikes the first creature with both fans. It counts as a **Launcher**, so the hit launches if it beats the threshold. **R2:** **30 ft**, and it deals **+1 weapon die** against airborne targets. **R3:** after the hit, she can carry on to a second creature within 10 ft and strike it too. |
| 3 | **Royal Storm** | Action | 3 | **R1:** with both fans in hand, she sends them spiralling around her: each creature within **15 ft** makes a DEX save or takes **4d8 slashing** and is pushed 10 ft backwards. The fans return. **R2:** airborne creatures caught in it **stay airborne** and it deals +1 weapon die (it counts as a juggle hit on each). **R3:** radius increases to **25 ft** and crit range against airborne creatures expands by 1. |
| 4 | **Sky Dancer** | Passive | 3 | **R1:** creatures she launched can be juggled for up to **5** hits instead of 3. **R2:** her Critical Air Takedown also applies **Deafening Winds**. **R3:** once per turn she can **Ride the Winds up to a launched creature** for free and attack it from above. |
| ◆ | **Imperial Cyclone** | Action | — | Once per long rest: every enemy within 30 ft makes a STR save or is **Launched**. She then makes one fan strike against each airborne creature (each counts as a juggle hit), and they land **Prone**. |

### Build B — Perfect Casting
| Rung | Name | Type | Ranks | Effect |
|---|---|---|---|---|
| 1 | **Amplified Weave** *(effectiveness)* | Passive | 3 | Each rank unlocks a modification. **R1 Amplify (20 TL):** the spell's damage or healing dice go up one size (d6 → d8 → d10 → d12). **R2 Saturate (25 TL):** area **+10 ft** radius, or double a line's length. **R3 Ascendant (40 TL):** the spell is cast as if from a slot **one level higher**. |
| 2 | **Elemental Fusion** *(damage types)* | Passive | 3 | **R1 Fusion (25 TL):** half the spell's damage becomes a second type of her choice. Each half checks the target's resistances separately. **R2 Resonance (20 TL):** if the target is vulnerable to **either** type, all of the spell's damage counts as that type. **R3 Catalyst (30 TL):** fused damage can trigger **combination statuses** (e.g. Fire + Necrotic = Hellfire). |
| 3 | **Tempered Arcana** *(form)* | Passive | 3 | **R1 Temper (25 TL):** the spell's damage becomes **physical** (bludgeoning, piercing or slashing): magic resistance, anti-magic and counterspells don't affect it, but Block and ADR do. **R2 Spell-Edge (20 TL):** a Tempered spell delivered through **Spellstrike** counts as a weapon hit for on-hit effects, and counts as a **Launcher**. **R3 Veiled Casting (20 TL):** no verbal or somatic components; it can't be Read or interrupted until it lands. |
| 4 | **Weave Mastery** *(structure)* | Passive | 3 | **R1 Reshape (15 TL):** change the spell's area shape (sphere, cone, line or cube), keeping its size. **R2 Sustain (35 TL):** a concentration spell doesn't need concentration for 2 rounds (one at a time). **R3:** modifications that don't change school cost **5 TL less** (min 10). |
| ◆ | **Perfect Harmony** | Passive | — | Once per long rest, she can combine **two school-changing modifications** on one spell, breaking the usual special rule. |

---

## Beatrix — The Harvesting Princess
<mark>✏️ **This whole section was replaced with the finished tree from beatrix-kit-final.** The old one had a blank Bountiful Harvest, Reagent Savant (vines no longer store reagents), the old rung 1–2 ideas, blank Sylvan Oblige rungs and "B: Archery" in the header.</mark>

**Overall: her systems (alchemy, seeds, battalion, precision) · A: Vines · B: Sylvan's Oblige**

> <mark>✏️ **Beatrix is level 12.** Her rung 3 and rung 4 nodes stay locked until levels 15 and 20.</mark>

### Overall
| # | Name | Ranks | Effect |
|---|---|---|---|
| 1 | ~~**Noble Spirit**: Battalion to-hit +2 per rank.~~ <mark>✏️ **Stocked Satchel**</mark> | 3 | <mark>✏️ Adds to her Alchemy Bag's Starting Stock. **R1:** +1 common Poisonous, +1 uncommon Poisonous, +2 uncommon Curative. **R2:** +2 uncommon Reactive, +1 uncommon Poisonous. **R3:** +2 rare Reactive, +1 rare Poisonous, +2 rare Curative.</mark> |
| 2 | **Potent Brews** | 3 | Alchemical creations deal or heal **+2** per rank. |
| 3 | **Hardy Seeds** | 3 | Blooming Vine max HP **+10** per rank. |
| 4 | <mark>✏️ **Precision Shot**</mark> | 3 | Precision chance **+2%** per rank (double crit damage). |
| 5 | **Seed Pouch** | 3 | **R1:** Rapid Growth range **+5 ft**. **R2:** Rapid Growth plants **+1 seed** (stacks with Blooming Forest). **R3:** once per combat, Rapid Growth is a **free action**. |
| 6 | **Deep Roots** | 2 | **R1:** **+1** Rapid Growth use. **R2:** Rapid Growth uses reset after a short rest. |
| 7 | **Quick Hands** | 1 | In combat, she can craft a creation of **Rare or lower** as a **bonus action** (normally Common or Uncommon, as an action). |
| 8 | **Master Alchemist** | 1 · **Level 15** | Once per long rest, halve (rounded down) each ingredient cost to brew a potion or poison. |

### Build A — Vines
| Rung | Name | Ranks | Effect |
|---|---|---|---|
| 1 | **Harvester Vine** | 3 | **R1:** unlocks Harvester **Verdant\***. **R2:** unlocks Harvester **Elder\***. **R3 Bumper Crop:** Harvest the Field rolls **once more** for each Harvester that ended the combat Verdant or Elder. |
| 2 | **Shooter Vine** | 3 | **R1:** unlocks Shooter **Verdant\***. **R2:** unlocks Shooter **Elder\***. **R3 Splitting Thorns:** each thorn that hits splits to a second creature within 10 ft for half damage, and Thorn Launch range becomes **90/270**. |
| 3 | **Spike Vine** | 3 | **R1:** unlocks the Spike job (**Sprout: Root Bed**). **R2:** unlocks Spike **Verdant\*: Thorn Field**. **R3:** unlocks Spike **Elder\*: Impaling Ground**. |
| 4 | **Alchemy Vine** | 3 | **R1:** unlocks the Alchemy job (**Sprout: Bulb**). **R2:** unlocks Alchemy **Verdant\*: Twin Bulb**. **R3:** unlocks Alchemy **Elder\*: Distillery**. |
| ◆ | **Grove Paragon** | — | As an action, once per long rest, she merges **three Elder vines with different jobs** within 30 ft of each other into one Paragon vine. It has their combined HP and Verdant and Elder stats, reach 20 ft, and **every merged job's Elder ability**. It takes **one action per job** each turn. Each job adds a **fusion trait**: **Harvester:** the Sap it makes can go straight into Degree. **Shooter:** its thorns carry its other jobs (an Alchemy creation coats them; Spike seeds a 5 ft root patch where they hit). **Spike:** its root field is centred on it permanently, and its jobs have advantage against creatures in the roots. **Alchemy:** once a round, spraying costs no action. **Degree:** each Sap she spends on it gives +1 (max 10). **Degree 5:** +1 action each turn. **Degree 10:** **Grove's Wrath** (once): every job fires at full effect at once. Lasts until it drops to 0 HP or she finishes a long rest. |

### Build B — Sylvan Oblige
| Rung | Name | Type | Ranks | Effect |
|---|---|---|---|---|
| 1 | **Four Seasons** | Passive | 3 | **R1: unlocks Summer.** When switching to the Bow, until the end of her turn each arrow's crit range expands by 1 per flower on its target (max 3: crits on 17–20). **R2: unlocks Winter.** When switching to the Blades, her next strike freezes the target: its speed drops to 0 and it has disadvantage on its next attack. **R3 Full Bloom:** when she switches, she gets **both** seasons of that form: Bow = Spring + Summer (bloom, then crit off the new flowers), Blades = Autumn + Winter (wither and freeze on the same strike). |
| 2 | **Scavenging Arrow** | Passive | 3 | **R1:** the Bow fires **five** arrows instead of three. <mark>✏️ **R2:** when a coated arrow kills a creature, the coating isn't used up: it also covers her **next** turn (once per turn). **R3:** crits trigger it too (up to 3 times per turn, each adding one more turn of coating).</mark> |
| 3 | **Harvesting Blade** | Passive | 3 | **R1:** the Blades' double-hit temp HP rises to **30%** of the target's max HP. <mark>✏️ **R2:** when she kills a creature with the Blades, she gains **1 common reagent** (once per turn). **R3:** crits trigger it too (up to 3 times per turn).</mark> |
| 4 | **Sylvan Indulgence** | Passive | 3 | <mark>✏️ **R1:** once per turn, she may switch forms again for free, applying the season. **R2:** creatures can carry up to **5** flowers, and Autumn's wither damage becomes **1d10** per flower *(Summer still counts at most 3)*.</mark> **R3:** her first strike after a switch also applies the season(s) of the form she just left. |
| ◆ | **Eternal Cycle** | Passive | — | Once per long rest, for ~~1 minute~~ <mark>✏️ **3 rounds**</mark>, **all four seasons** trigger on **every** strike. |

*Rung locks: Harvester or Four Seasons · Shooter or Scavenging Arrow · Spike or Harvesting Blade · Alchemy or Sylvan Indulgence. Rungs 3 and 4 need level 15 and 20.*

---

## Yohan — The Diamond in the Rough
**Overall: speed, damage and focus · A: Momentum · B: Focus**

### Overall
| # | Name | Ranks | Effect |
|---|---|---|---|
| 1 | **Desert Stride** | 3 | **+5 ft** speed per rank. |
| 2 | **Deep Focus** | 3 | **+2** focus points per rank. |
| 3 | **Sand-Honed Edge** | 3 | Halberd damage **+2** per rank. |
| 4 | **Heavy Grains** | 3 | Each Momentum Die spent deals **+1** damage per rank. |
| 5 | **Sunlit Reflexes** | 3 | **+2 initiative** per rank. |
| 6 | **Quick Breath** | 2 | A short rest returns **+3 focus** per rank. |
| 7 | **Roar of the Horizon** | 1 | When he crits a creature, each creature within 10 ft of it also loses **10 Morale**. |
| 8 | **Second Surge** | 1 · **Level 15** | The first Dragon Surge after each rest doesn't raise its cost. |

### Build A — Momentum Techniques
| Rung | Name | Ranks | Effect |
|---|---|---|---|
| 1 | **Sandstorm Surge** | 3 | **R1:** he can generate up to **4 MD** a round instead of 3. **R2:** Momentum Dice become **d10s**. **R3:** his Momentum Dice cap rises from PB to **PB + 2**, and Rising Dawn no longer halves his movement. |
| 2 | **Dune Line** | 3 | **R1 Long Road:** one turn of up to 45 degrees per turn doesn't break his line. **R2 Carried Wind:** if he ends his turn having moved in a straight line, his Dune stacks carry into his next turn instead of resetting (still resets if he is hit, grappled, or knocked prone). **R3 Desert Wrath:** his Dune stack cap rises from 6 to **9**. At 9 stacks he can spend them all to take an **extra turn** right after this one (~~once per combat~~ <mark>✏️ once per long rest</mark>). |
| 3 | **Haboob** | 3 | **R1 Dune Shelter:** ~~Buried Momentum costs 1 MD per 10 ft instead of per 5 ft.~~ <mark>✏️ while in Buried Momentum, he loses 1 Momentum Die per **10 ft** moved instead of per 5 ft.</mark> **R2:** creatures that fail his Dunewall Charge save are also **Blinded** until the end of their next turn. **R3:** he can change direction once during the charge. |
| 4 | **Dunebreaker** | 3 | **R1 Overspend:** when he uses Dunebreaker Strike, half of the Momentum Dice he spent (rounded down) stay with him. He can spend them on a second Dunebreaker against a different creature this turn, or on anything else that costs MD. **R2:** if Dunebreaker lands on the same attack as his Momentum Finisher, its Momentum Dice deal **double**. **R3 Monolith:** a Dunebreaker or Finisher hit forces a CON save, or the target is **Stunned** until the end of its next turn. |
| ◆ | **Endless Desert** | — | Once per long rest, for **3 rounds**: Momentum Dice never expire, Buried Momentum costs nothing, his Dune stacks never reset, and there's no limit on how many MD he generates a round. When it starts, he gains Momentum Dice up to his cap. |

### Build B — Focus Techniques
| Rung | Name | Ranks | Effect |
|---|---|---|---|
| 1 | **Horizon Arts** | 3 | **R1 Crescent Sweep** (Attack, 1 focus): Hack; one swing hits every creature in a **10 ft arc** in front of him. **R2 Hook & Pull** (Attack, 1 focus): on a Hack hit, he hooks the target with the axe head: pull it **10 ft** toward him, or knock it **Prone**. **R3 Skewer** (1 focus): on a Pierce hit, the target is **pinned** on the spear point. It can't move away from him until it succeeds on a STR save (its action), and his attacks against it get **+2** while it's pinned. |
| 2 | **Stance Mastery** | 3 | **R1:** entering a stance becomes a **free action** (once per turn). **R2:** ~~spend 1 focus to extend a stance for another round.~~ <mark>✏️ keeping the same stance on his next turn costs **1 Ki** instead of 3.</mark> **R3:** he can hold **two stances** at once (paying for both). |
| 3 | **Desert Forms** | 3 | **R1 Crimson Cleave** (Red Dunes): ~~Hack hits also deal PB bleed damage at the start of the target's turn.~~ <mark>✏️ his Bleed deals **+PB** damage, and a creature already Bleeding takes its bleed damage again when he hits it with Hack.</mark> **R2 Sirocco Lance** (Sirocco): after moving 10+ ft, his attacks **ignore half cover**, and the target's Dodge has **disadvantage**. **R3 Scorpion Tail** (Scorpion): his opportunity attacks can **Pierce at 15 ft** reach, and a hit drops the target's speed to **0**. |
| 4 | **Tomb Sentinel** | ~~2~~ <mark>✏️ 3</mark> | **R1:** while in Buried Tomb, Falcon Wing Deflection costs **1 focus**, and he can use it for an **ally within his reach**. **R2:** while in Buried Tomb, creatures that end their turn within his reach take **Hack damage** (no roll). <mark>✏️ **R3:** while in Buried Tomb, allies within his reach can't be pushed, pulled or knocked prone, and gain **+2 AC**.</mark> |
| ◆ | **Vast Horizon** | — | Once per long rest, for **3 rounds** he holds **all four stances** at once, and each halberd attack counts as **both Hack and Pierce**. |

---

## Melissa — Seals of the Ancients
**Overall: speed and dodge · A: Seals · B: Flow State**

### Overall
| # | Name | Ranks | Effect |
|---|---|---|---|
| 1 | **Water Footing** | 3 | **+1** to Dodge checks per rank. |
| 2 | **Swift Current** | 3 | **+5 ft** speed per rank. |
| 3 | **Deep Reserves** | 3 | **+2** Ki per rank. |
| 4 | **Tidal Reflex** | 3 | **+2 initiative** per rank. |
| 5 | **Settled Mind** | 3 | <mark>✏️ Her Maneuver save DC **+1** per rank (a failed save she forces also ticks the creature's seal through Eye of the Storm).</mark> |
| 6 | **Ripple** | 2 | Still Water can be used **+1 time per round** per rank. |
| 7 | **Light Step** | 1 | Her movement doesn't provoke opportunity attacks from creatures she dodged this round. |
| 8 | **Wavebreaker** | 1 · **Level 15** | Uncanny Metabolism also fills her Flow. |

### Build A — Seals
| Rung | Name | Ranks | Effect |
|---|---|---|---|
| 1 | **Swift Inscription** | 3 | **R1:** once per round, placing a seal on a hit **doesn't cost her reaction**. **R2:** she can seal herself as a **free action** (normally a bonus action) and a **willing ally within 5 ft** as a bonus action. **R3:** she can keep **+1 seal** on the field (PB → PB + 1). |
| 2 | **Quickened Seal** | 3 | **R1:** seals advance a tier every **2 ticks** instead of 3 (Tier 6 at 10 ticks). **R2 Resonance:** when a seal advances a tier, one seal within 10 ft gains +1 tick. **R3 Deep Drain:** her seals drain more per tick: **2 × PB** Ki, or ~~WIS × (2x PB)~~ <mark>✏️ **(WIS × PB) + PB**</mark> TL or HP. |
| 3 | **Seal Break** | 3 | Bonus action: **break one of her seals** to unleash it, scaled by its tier. Each rank unlocks a school. **R1 Demonic:** the target takes **WIS × PB necrotic per tier** and has Collapse until the end of its next turn. **R2 Angelic:** the target and allies within 15 ft regain **WIS × PB HP per tier**. **R3 Draconic:** for 1 round the target gains the effect of the **next tier up**, and any Draconic Growth left on the seal converts to ticks on another of her seals. |
| 4 | **Ancient Script** | 2 | New seals start at **Tier 2**. **R2:** Tier 3. *(A head start counts as that tier's ticks, so with Quickened Seal a Tier 3 start is 4 ticks.)* |
| ◆ | **Universal Seal** | — | Once per long rest, place a seal of **every type** on one creature at once. They tick separately, don't count against her cap, and **advance together**: when one gains a tier, they all do. |

### Build B — Flow State
| Rung | Name | Ranks | Effect |
|---|---|---|---|
| 1 | **Counterflow** | ~~2~~ <mark>✏️ 3</mark> | On a successful dodge, spend **1 Flow** to make an unarmed strike against the attacker. **R2:** on a hit, she can spend **2 Flow** to make the target act **last** in the order next round. <mark>✏️ **R3:** the counter strike deals **+1 Martial Arts die** and pushes the target **10 ft**.</mark> |
| 2 | **High Tide** | ~~2~~ <mark>✏️ 3</mark> | Flow max **+1 per rank** (PB → PB + 2). **R2:** she also starts each combat with **2 Flow**. <mark>✏️ **R3:** when she reaches max Flow, she gains **1 Tempo** (once per round).</mark> |
| 3 | **Control the Tide** | 3 | **R1 Seize the Initiative** (2 Flow): at the start of a round, move her turn to the **top** of the order for this round. **R2 Half-Beat** (2 Flow): end her turn early and keep what she hasn't used; take the rest at the end of any creature's turn later this round. **R3 Call the Tempo** (2 Flow, bonus action): one ally who hasn't gone yet moves to **right after her** this round. |
| 4 | **Tsunami** | 2 | When she has at least **3 Flow**, Flurry of Blows makes **+1 strike per rank**. |
| ◆ | **Perfect Flow** | — | Once per long rest, for **3 rounds** the first attack against her each round **automatically misses**, counting as a successful dodge. |

---

## Change list (v2 → v3)

### Dylan
1. Deserter's Mire: typo fix ("and Dylan regains 1 battle die").
2. Oathbreaker's Toll: new R2 (+PB on next attack) and R3 (disadvantage on Dodge, Block, Parry), because most enemies only have 1 reaction.
3. Coward's Crown: Ranks 2 → 3; new R3 (PB psychic to Frightened enemies, aura costs 10 TL less).
4. Blood Pact: Ranks 2 → 3 (your R3 was already written); "willing" ally.
5. Traitor's Crown: the attack spends all Treachery.

### Sika
6. Hold Your Liquor → **Bottoms Up**: drink with a hymn; Wasted on the 5th drink at R1 and the 6th at R2; +8 MP per drink at R2; at R3 her tally starts each combat at 2 or more. Two drinks in a round: MP stacks, CHA doubling and the extra hymn don't.
7. Liquid Courage R2: advantage → +1 crit range.
8. Bar Fight Ballad: unchanged (the tally reset stays).
9. Mind Link: ends if she's incapacitated (not on concentration).
10. Intrusive Thought → **Second Guess**.
11. Thought Theft: Ranks 2 → 3 (your R3 was already written); she gains the full amount.
12. Shared Mind (1 rank) → **Shared Resolve** (2 ranks): holds a linked ally's Morale tier and lowers their Swing Cap. (Mind Ward was cut for being too close to Bardic Inspiration.)

### Magnolia
13. Voluptuous Body → **Allure**, +1 to her Persuasion roll for Flirtatious (it's a contest, not a DC).
14. Typos: Wind Shear, Range.

### Beatrix
15. Whole section replaced with the beatrix-kit-final tree.
16. Eternal Cycle: 1 minute → 3 rounds.
17. Noble Spirit removed; **Stocked Satchel** takes its slot as Overall #1 (ingredients only: no "enough for" notes, no extra item slots). She has 8 Overall nodes again.
18. Level is 12, so rungs 3 and 4 open at 15 and 20.

### Yohan
19. Sandstorm Surge R2: unchanged (d10s). Momentum Dice only get bigger through the tree.
20. Desert Wrath: once per long rest.
21. Haboob R1: reworded (Buried Momentum loses dice per 10 ft; it doesn't cost them).
22. Stance Mastery R2: keeping the same stance costs 1 Ki instead of 3 (stances last until the start of his next turn).
23. Crimson Cleave: Hack already causes Bleed, so it now boosts Bleed instead.
24. Tomb Sentinel: Ranks 2 → 3; new R3 (allies in reach can't be moved, +2 AC).

### Melissa
25. Settled Mind: Maneuver save DC +1 per rank (seals never ask for a save; this feeds Eye of the Storm instead).
26. Deep Drain: TL/HP is now (WIS × PB) + PB.
27. Counterflow: Ranks 2 → 3; new R3 (+1 Martial Arts die, push 10 ft).
28. High Tide: Ranks 2 → 3; new R3 (gain 1 Tempo at max Flow, once per round).

### Rank check after these changes
| Character | Rung 1 | Rung 2 | Rung 3 | Rung 4 |
|---|---|---|---|---|
| Dylan | 3 / 3 | 3 / 3 | 3 / 3 | 2 / 2 |
| Sika | 3 / 3 | 3 / 3 | 3 / 3 | 2 / 2 |
| Magnolia | 3 / 3 | 3 / 3 | 3 / 3 | 3 / 3 |
| Beatrix | 3 / 3 | 3 / 3 | 3 / 3 | 3 / 3 |
| Yohan | 3 / 3 | 3 / 3 | 3 / 3 | 3 / 3 |
| Melissa | 3 / 3 | 3 / 3 | 3 / 3 | 2 / 2 |

## Still to decide
- Nothing open in the trees. <mark>✏️ The repo sheets are the reference: Sika's drink tally clears only on a short or long rest, and she becomes Nauseous only if she extended Wasted.</mark>
