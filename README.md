# Minimal Corpus for ISDA2022 Paper

## Corpus

A minimal corpus was costructed for semantic parsing task evaluation on isda2022 knowledge.  The corpus captures:

1. Quantitfiers:  universal and existential quantification
2. Negation
3. Logical connectives: conjunction, disjunction and implication
4. Equality
5. More than one variable
6. Questions

## Results

| Formalism             | Parser    |   Results   |
| ---------------------- | --------- | ---- |
| AMR                    | [armlib](https://github.com/bjascob/amrlib)    | [results](https://github.com/martinve/isda2022/blob/main/results/corpus-min-amr.txt) |
| UCCA                   | [TUPA](https://github.com/danielhers/tupa)      |      [results](https://github.com/martinve/isda2022/blob/main/results/corpus-min-ucca.md)|
| UDS | [PredPatt](https://github.com/hltcoe/PredPatt)  |      [brief](https://github.com/martinve/isda2022/blob/main/results/corpus-min-ud-simple.txt) and [full](https://github.com/martinve/isda2022/blob/main/results/corpus-min-ud.txt)|
| DRS | [TreeDRSParsing](https://github.com/LeonCrashCode/TreeDRSparsing/tree/bs_sattn_drssup) | [results](https://github.com/martinve/isda2022/blob/main/results/corpus-min-drs.txt) |

