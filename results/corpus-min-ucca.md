# Semantic Parsing Report
__Sentence__:Cats are animals.

```
Loading spaCy model 'en_core_web_md'... Done (12.934s).
corpus-min_0000:
  Light verbs:
    1.22->1.24 [F are]
  Predicate nouns:
    1.21->1.22 [P [C Cats] [F are] ]
  Center:
    1.1->1.2 [C animals]
    1.22->1.23 [C Cats]
  Punctuation:
    1.1->1.3 [U .]
  Participant:
    1.1->1.22 [A [C Cats] [F are] ]
    1.1->1.23 [A Cats]
  Function:
    1.22->1.24 [F are]


```

__Sentence__:Animals have a head.

```
Loading spaCy model 'en_core_web_md'... Done (13.224s).
corpus-min_0001:
  Light verbs:
    1.1->1.2 [F have]
  Predicate nouns:
    1.25->1.26 [P Animals]
  Function:
    1.1->1.2 [F have]
  Participant:
    1.1->1.3 [A [E a] [C head] ]
    1.1->1.26 [A Animals]
  Punctuation:
    1.1->1.4 [U .]
  Elaborator:
    1.3->1.6 [E a]
  Center:
    1.3->1.7 [C head]


```

__Sentence__:Percy is a cat.

```
Loading spaCy model 'en_core_web_md'... Done (13.282s).
corpus-min_0002:
  Light verbs:
    1.1->1.2 [F is]
  Predicate nouns:
    1.25->1.26 [P Percy]
  Function:
    1.1->1.2 [F is]
  Participant:
    1.1->1.3 [A [E a] [C cat] ]
    1.1->1.26 [A Percy]
  Punctuation:
    1.1->1.4 [U .]
  Elaborator:
    1.3->1.6 [E a]
  Center:
    1.3->1.7 [C cat]


```

__Sentence__:Are cats animals?

```
Loading spaCy model 'en_core_web_md'... Done (13.367s).
corpus-min_0003:
  Light verbs:
    1.1->1.2 [F cats]
  Predicate nouns:
    1.24->1.25 [P Are]
  Function:
    1.1->1.2 [F cats]
  State:
    1.1->1.3 [S [E animals] [U ?] ]
  Participant:
    1.1->1.25 [A Are]
  Elaborator:
    1.3->1.5 [E animals]
  Punctuation:
    1.3->1.6 [U ?]


```

__Sentence__:Does Percy have a head?

```
Loading spaCy model 'en_core_web_md'... Done (13.533s).
corpus-min_0004:
  Light verbs:
    1.1->1.2 [F Percy]
  Predicate nouns:
    1.26->1.27 [P Does]
  Function:
    1.1->1.2 [F Percy]
  Participant:
    1.1->1.3 [A [E have] [E a] [C head] ]
    1.1->1.27 [A Does]
  Punctuation:
    1.1->1.4 [U ?]
  Elaborator:
    1.3->1.6 [E have]
    1.3->1.7 [E a]
  Center:
    1.3->1.8 [C head]


```

__Sentence__:Plants are not animals.

```
Loading spaCy model 'en_core_web_md'... Done (13.505s).
corpus-min_0005:
  Light verbs:
    1.1->1.2 [F are]
  Predicate nouns:
    1.25->1.26 [P Plants]
  Function:
    1.1->1.2 [F are]
  Participant:
    1.1->1.3 [A [E not] [C animals] ]
    1.1->1.26 [A Plants]
  Punctuation:
    1.1->1.4 [U .]
  Elaborator:
    1.3->1.6 [E not]
  Center:
    1.3->1.7 [C animals]


```

__Sentence__:Iron conducts electricity.

```
Loading spaCy model 'en_core_web_md'... Done (13.184s).
corpus-min_0006:
  Light verbs:
    1.1->1.2 [F conducts]
  Predicate nouns:
    1.24->1.25 [P Iron]
  Function:
    1.1->1.2 [F conducts]
  State:
    1.1->1.3 [S [E electricity] [U .] ]
  Participant:
    1.1->1.25 [A Iron]
  Elaborator:
    1.3->1.5 [E electricity]
  Punctuation:
    1.3->1.6 [U .]


```

__Sentence__:Glass does not conduct electricity.

```
Loading spaCy model 'en_core_web_md'... Done (13.139s).
corpus-min_0007:
  Light verbs:
    1.1->1.2 [F does]
  Predicate nouns:
    1.26->1.27 [P Glass]
  Function:
    1.1->1.2 [F does]
  Participant:
    1.1->1.3 [A [E not] [E conduct] [C electricity] ]
    1.1->1.27 [A Glass]
  Punctuation:
    1.1->1.4 [U .]
  Elaborator:
    1.3->1.6 [E not]
    1.3->1.7 [E conduct]
  Center:
    1.3->1.8 [C electricity]


```

__Sentence__:An electrical conductor is a vehicle for the flow of electricity.

```
Loading spaCy model 'en_core_web_md'... Done (13.702s).
corpus-min_0008:
  Light verbs:
    1.1->1.2 [F electrical]
  Function:
    1.1->1.2 [F electrical]
    1.1->1.9 [F vehicle]
  Participant:
    1.1->1.3 [A [E conductor] [E is] [C a] ]
    1.1->1.8 [A An]
    1.1->1.10 [A [R for] [E the] [C flow] ]
  Punctuation:
    1.1->1.4 [U .]
  Center:
    1.1->1.8 [C An]
    1.3->1.7 [C a]
    1.10->1.13 [C flow]
  Elaborator:
    1.3->1.5 [E conductor]
    1.3->1.6 [E is]
    1.10->1.12 [E the]
  Relator:
    1.10->1.11 [R for]


```

__Sentence__:Conductor is a person who conducts an orchestra.

```
Loading spaCy model 'en_core_web_md'... Done (13.287s).
corpus-min_0009:
  Light verbs:
    1.1->1.2 [F is]
  Predicate nouns:
    1.29->1.30 [P Conductor]
  Function:
    1.1->1.2 [F is]
  Participant:
    1.1->1.3 [A [E a] [E person] [C who] [E conducts] [E an] [C orchestra] ]
    1.1->1.30 [A Conductor]
  Punctuation:
    1.1->1.4 [U .]
  Elaborator:
    1.3->1.6 [E a]
    1.3->1.7 [E person]
    1.3->1.9 [E conducts]
    1.3->1.10 [E an]
  Center:
    1.3->1.8 [C who]
    1.3->1.11 [C orchestra]


```

__Sentence__:Steve is a conductor.

```
Loading spaCy model 'en_core_web_md'... Done (13.291s).
corpus-min_0010:
  Light verbs:
    1.1->1.2 [F is]
  Predicate nouns:
    1.25->1.26 [P Steve]
  Function:
    1.1->1.2 [F is]
  Participant:
    1.1->1.3 [A [E a] [C conductor] ]
    1.1->1.26 [A Steve]
  Punctuation:
    1.1->1.4 [U .]
  Elaborator:
    1.3->1.6 [E a]
  Center:
    1.3->1.7 [C conductor]


```

__Sentence__:John ingested poison.

```
Loading spaCy model 'en_core_web_md'... Done (13.293s).
corpus-min_0011:
  Light verbs:
    1.1->1.2 [F ingested]
  Predicate nouns:
    1.24->1.25 [P John]
  Function:
    1.1->1.2 [F ingested]
  State:
    1.1->1.3 [S [E poison] [U .] ]
  Participant:
    1.1->1.25 [A John]
  Elaborator:
    1.3->1.5 [E poison]
  Punctuation:
    1.3->1.6 [U .]


```

__Sentence__:John was born in 1990.

```
Loading spaCy model 'en_core_web_md'... Done (13.330s).
corpus-min_0012:
  Light verbs:
    1.1->1.2 [F was]
  Predicate nouns:
    1.26->1.27 [P John]
  Function:
    1.1->1.2 [F was]
  Participant:
    1.1->1.3 [A [E born] [E in] [C 1990] ]
    1.1->1.27 [A John]
  Punctuation:
    1.1->1.4 [U .]
  Elaborator:
    1.3->1.6 [E born]
    1.3->1.7 [E in]
  Center:
    1.3->1.8 [C 1990]


```

__Sentence__:Steve thinks John ingested poison.

```
Loading spaCy model 'en_core_web_md'... Done (13.160s).
corpus-min_0013:
  Light verbs:
    1.1->1.2 [F thinks]
  Predicate nouns:
    1.26->1.27 [P Steve]
  Function:
    1.1->1.2 [F thinks]
  Participant:
    1.1->1.3 [A [E John] [E ingested] [C poison] [U .] ]
    1.1->1.27 [A Steve]
  Elaborator:
    1.3->1.5 [E John]
    1.3->1.6 [E ingested]
  Center:
    1.3->1.7 [C poison]
  Punctuation:
    1.3->1.8 [U .]


```

__Sentence__:Poison kills when eaten.

```
Loading spaCy model 'en_core_web_md'... Done (13.079s).
corpus-min_0014:
  Light verbs:
    1.1->1.2 [F kills]
  Predicate nouns:
    1.25->1.26 [P Poison]
  Function:
    1.1->1.2 [F kills]
  Participant:
    1.1->1.3 [A [E when] [C eaten] ]
    1.1->1.26 [A Poison]
  Punctuation:
    1.1->1.4 [U .]
  Elaborator:
    1.3->1.6 [E when]
  Center:
    1.3->1.7 [C eaten]


```

__Sentence__:Born in a small town, she took the midnight train going anywhere.

```
Loading spaCy model 'en_core_web_md'... Done (12.870s).
corpus-min_0015:
  Light verbs:
    1.1->1.2 [F in]
  Predicate nouns:
    1.35->1.36 [P Born]
  Function:
    1.1->1.2 [F in]
  Participant:
    1.1->1.3 [A [E a] [E small] [C town] ]
    1.1->1.5 [A she]
    1.1->1.7 [A [E the] [E midnight] [C train] [E going] [C anywhere] ]
    1.1->1.36 [A Born]
  Punctuation:
    1.1->1.4 [U ,]
    1.1->1.8 [U .]
  Elaborator:
    1.3->1.10 [E a]
    1.3->1.11 [E small]
    1.7->1.13 [E the]
    1.7->1.14 [E midnight]
    1.7->1.16 [E going]
  Center:
    1.3->1.12 [C town]
    1.7->1.15 [C train]
    1.7->1.17 [C anywhere]


```

__Sentence__:The city councilmen refused the demonstrators a permit because they advocated violence.

```
Loading spaCy model 'en_core_web_md'... Done (12.945s).
corpus-min_0016:
  Light verbs:
    1.1->1.2 [F city]
  Predicate nouns:
    1.34->1.35 [P The]
  Function:
    1.1->1.2 [F city]
  Participant:
    1.1->1.3 [A [E councilmen] [E refused] [C the] ]
    1.1->1.5 [A a]
    1.1->1.7 [A [E because] [E they] [C advocated] [E violence] [U .] ]
    1.1->1.35 [A The]
  Punctuation:
    1.1->1.4 [U demonstrators]
    1.7->1.16 [U .]
  Elaborator:
    1.3->1.9 [E councilmen]
    1.3->1.10 [E refused]
    1.7->1.12 [E because]
    1.7->1.13 [E they]
    1.7->1.15 [E violence]
  Center:
    1.3->1.11 [C the]
    1.7->1.14 [C advocated]


```

__Sentence__:The trophy doesn't fit into the brown suitcase because it's too small.

```
Loading spaCy model 'en_core_web_md'... Done (13.093s).
corpus-min_0017:
  Light verbs:
    1.1->1.2 [F trophy]
  Predicate nouns:
    1.1->1.18 [P The]
  Predicate adjectives:
    1.36->1.37 [P small]
  Function:
    1.1->1.2 [F trophy]
  Participant:
    1.1->1.3 [A [E does] [E n't] [C fit] ]
    1.1->1.5 [A the]
    1.1->1.7 [A [E suitcase] [E because] [C it] [E 's] [C too] ]
    1.1->1.18 [A The]
  Punctuation:
    1.1->1.4 [U into]
    1.1->1.8 [U .]
  Elaborator:
    1.3->1.10 [E does]
    1.3->1.11 [E n't]
    1.7->1.13 [E suitcase]
    1.7->1.14 [E because]
    1.7->1.16 [E 's]
  Center:
    1.3->1.12 [C fit]
    1.7->1.15 [C it]
    1.7->1.17 [C too]


```

__Sentence__:Joan made sure to thank Susan for all the help she had given.

```
Loading spaCy model 'en_core_web_md'... Done (13.404s).
corpus-min_0018:
  Light verbs:
    1.1->1.2 [F made]
  Predicate nouns:
    1.35->1.36 [P Joan]
  Function:
    1.1->1.2 [F made]
  Participant:
    1.1->1.3 [A [E sure] [E to] [C thank] ]
    1.1->1.5 [A for]
    1.1->1.7 [A [E the] [E help] [C she] [C had] [C given] ]
    1.1->1.36 [A Joan]
  Punctuation:
    1.1->1.4 [U Susan]
    1.1->1.8 [U .]
  Elaborator:
    1.3->1.10 [E sure]
    1.3->1.11 [E to]
    1.7->1.13 [E the]
    1.7->1.14 [E help]
  Center:
    1.3->1.12 [C thank]
    1.7->1.15 [C she]
    1.7->1.16 [C had]
    1.7->1.17 [C given]


```

__Sentence__:What states border Texas and have a major river?

```
Loading spaCy model 'en_core_web_md'... Done (13.572s).
corpus-min_0019:
  Light verbs:
    1.1->1.2 [F states]
  Predicate nouns:
    1.31->1.32 [P What]
  Function:
    1.1->1.2 [F states]
  Participant:
    1.1->1.3 [A [E border] [E Texas] [C and] ]
    1.1->1.5 [A a]
    1.1->1.7 [A [E river] [U ?] ]
    1.1->1.32 [A What]
  Punctuation:
    1.1->1.4 [U have]
    1.7->1.13 [U ?]
  Elaborator:
    1.3->1.9 [E border]
    1.3->1.10 [E Texas]
    1.7->1.12 [E river]
  Center:
    1.3->1.11 [C and]


```

__Sentence__:What is the total population of the states that border Texas?

```
Loading spaCy model 'en_core_web_md'... Done (13.139s).
corpus-min_0020:
  Light verbs:
    1.1->1.2 [F is]
  Predicate nouns:
    1.33->1.34 [P What]
  Function:
    1.1->1.2 [F is]
  Participant:
    1.1->1.3 [A [E the] [E total] [C population] ]
    1.1->1.5 [A the]
    1.1->1.7 [A [E that] [E border] [C Texas] ]
    1.1->1.34 [A What]
  Punctuation:
    1.1->1.4 [U of]
    1.1->1.8 [U ?]
  Elaborator:
    1.3->1.10 [E the]
    1.3->1.11 [E total]
    1.7->1.13 [E that]
    1.7->1.14 [E border]
  Center:
    1.3->1.12 [C population]
    1.7->1.15 [C Texas]


```

__Sentence__:What states border states that border states that border states that border Texas.

```
Loading spaCy model 'en_core_web_md'... Done (13.032s).
corpus-min_0021:
  Light verbs:
    1.1->1.2 [F states]
  Predicate nouns:
    1.35->1.36 [P What]
  Function:
    1.1->1.2 [F states]
  Participant:
    1.1->1.3 [A [E border] [E states] [C that] ]
    1.1->1.5 [A states]
    1.1->1.36 [A What]
  Punctuation:
    1.1->1.4 [U border]
    1.1->1.7 [U .]
  Elaborator:
    1.3->1.9 [E border]
    1.3->1.10 [E states]
    1.6->1.12 [E that]
  Center:
    1.3->1.11 [C that]
    1.6->1.13 [C border]
    1.6->1.14 [C states]
    1.6->1.15 [C that]
    1.6->1.16 [C border]
    1.6->1.17 [C Texas]


```

__Sentence__:A laser is used for producing light.

```
Loading spaCy model 'en_core_web_md'... Done (13.089s).
corpus-min_0022:
  Light verbs:
    1.1->1.2 [F laser]
  Predicate nouns:
    1.28->1.29 [P A]
  Function:
    1.1->1.2 [F laser]
  Participant:
    1.1->1.3 [A [E is] [E used] [C for] ]
    1.1->1.5 [A light]
    1.1->1.29 [A A]
  Punctuation:
    1.1->1.4 [U producing]
    1.1->1.6 [U .]
  Elaborator:
    1.3->1.8 [E is]
    1.3->1.9 [E used]
  Center:
    1.3->1.10 [C for]


```

__Sentence__:A leaf absorbs sunlight to perform photosynthesis.

```
Loading spaCy model 'en_core_web_md'... Done (13.503s).
corpus-min_0023:
  Light verbs:
    1.1->1.2 [F leaf]
  Predicate nouns:
    1.28->1.29 [P A]
  Function:
    1.1->1.2 [F leaf]
  Participant:
    1.1->1.3 [A [E absorbs] [E sunlight] [C to] ]
    1.1->1.5 [A photosynthesis]
    1.1->1.29 [A A]
  Punctuation:
    1.1->1.4 [U perform]
    1.1->1.6 [U .]
  Elaborator:
    1.3->1.8 [E absorbs]
    1.3->1.9 [E sunlight]
  Center:
    1.3->1.10 [C to]


```

__Sentence__:A flashlight converts chemical energy into light energy.

```
Loading spaCy model 'en_core_web_md'... Done (13.148s).
corpus-min_0024:
  Light verbs:
    1.1->1.2 [F flashlight]
  Predicate nouns:
    1.29->1.30 [P A]
  Function:
    1.1->1.2 [F flashlight]
  Participant:
    1.1->1.3 [A [E converts] [E chemical] [C energy] [E into] [E light] [C energy] ]
    1.1->1.30 [A A]
  Punctuation:
    1.1->1.4 [U .]
  Elaborator:
    1.3->1.6 [E converts]
    1.3->1.7 [E chemical]
    1.3->1.9 [E into]
    1.3->1.10 [E light]
  Center:
    1.3->1.8 [C energy]
    1.3->1.11 [C energy]


```

__Sentence__:A flashlight emits light.

```
Loading spaCy model 'en_core_web_md'... Done (13.206s).
corpus-min_0025:
  Light verbs:
    1.1->1.2 [F flashlight]
  Predicate nouns:
    1.25->1.26 [P A]
  Function:
    1.1->1.2 [F flashlight]
  Participant:
    1.1->1.3 [A [E emits] [C light] ]
    1.1->1.26 [A A]
  Punctuation:
    1.1->1.4 [U .]
  Elaborator:
    1.3->1.6 [E emits]
  Center:
    1.3->1.7 [C light]


```

__Sentence__:A flashlight requires a source of electricity to produce light.

```
Loading spaCy model 'en_core_web_md'... Done (13.288s).
corpus-min_0026:
  Light verbs:
    1.1->1.2 [F flashlight]
  Predicate nouns:
    1.33->1.34 [P A]
  Function:
    1.1->1.2 [F flashlight]
  Participant:
    1.1->1.3 [A [E requires] [E a] [E [C source] [R of] ] [C electricity] ]
    1.1->1.4 [A [R to] [C produce] [C light] ]
    1.1->1.34 [A A]
  Punctuation:
    1.1->1.5 [U .]
  Elaborator:
    1.3->1.7 [E requires]
    1.3->1.8 [E a]
    1.3->1.9 [E [C source] [R of] ]
  Center:
    1.3->1.10 [C electricity]
    1.4->1.12 [C produce]
    1.4->1.13 [C light]
    1.9->1.15 [C source]
  Relator:
    1.4->1.11 [R to]
    1.9->1.16 [R of]


```

__Sentence__:A light bulb converts electrical energy into light energy when it is turned on.

```
Loading spaCy model 'en_core_web_md'... Done (13.365s).
corpus-min_0027:
  Light verbs:
    1.1->1.2 [F light]
  Predicate nouns:
    1.1->1.4 [S into]
    1.13->1.16 [P when]
    1.38->1.39 [P A]
  Function:
    1.1->1.2 [F light]
    1.13->1.15 [F light]
  Participant:
    1.1->1.3 [A [E bulb] [E converts] [E [C electrical] ... [A [A* A] [F light] ... [P when] [A [E it] [C is] [C turned] [C on] ] [U .] ] ] [R energy] ]
    1.1->1.38 [A [P A] ]
    1.1->1.39 [A A]
    1.9->1.13 [A [A* A] [F light] ... [P when] [A [E it] [C is] [C turned] [C on] ] [U .] ]
    1.13->1.17 [A [E it] [C is] [C turned] [C on] ]
    1.13->1.39 [A A]
  State:
    1.1->1.4 [S into]
    1.37->1.38 [S [P A] ]
  Elaborator:
    1.3->1.7 [E bulb]
    1.3->1.8 [E converts]
    1.3->1.9 [E [C electrical] ... [A [A* A] [F light] ... [P when] [A [E it] [C is] [C turned] [C on] ] [U .] ] ]
    1.17->1.20 [E it]
  Relator:
    1.3->1.10 [R energy]
  Center:
    1.9->1.12 [C electrical]
    1.17->1.21 [C is]
    1.17->1.22 [C turned]
    1.17->1.23 [C on]
  Punctuation:
    1.13->1.18 [U .]


```

__Sentence__:A light bulb requires electrical energy to produce light.

```
Loading spaCy model 'en_core_web_md'... Done (13.178s).
corpus-min_0028:
  Light verbs:
    1.1->1.2 [F light]
  Predicate nouns:
    1.32->1.33 [P A]
  Function:
    1.1->1.2 [F light]
  Participant:
    1.1->1.3 [A [E bulb] [E requires] [C electrical] [E [R energy] [C to] [E [R produce] [C light] [U .] ] ] ]
    1.1->1.33 [A A]
  Elaborator:
    1.3->1.5 [E bulb]
    1.3->1.6 [E requires]
    1.3->1.8 [E [R energy] [C to] [E [R produce] [C light] [U .] ] ]
    1.8->1.12 [E [R produce] [C light] [U .] ]
  Center:
    1.3->1.7 [C electrical]
    1.8->1.11 [C to]
    1.12->1.15 [C light]
  Relator:
    1.8->1.10 [R energy]
    1.12->1.14 [R produce]
  Punctuation:
    1.12->1.16 [U .]


```

__Sentence__:A mirror is used for reflecting light.

```
Loading spaCy model 'en_core_web_md'... Done (13.143s).
corpus-min_0029:
  Light verbs:
    1.1->1.2 [F mirror]
  Predicate nouns:
    1.28->1.29 [P A]
  Function:
    1.1->1.2 [F mirror]
  Participant:
    1.1->1.3 [A [E is] [E used] [C for] [E reflecting] [C light] ]
    1.1->1.29 [A A]
  Punctuation:
    1.1->1.4 [U .]
  Elaborator:
    1.3->1.6 [E is]
    1.3->1.7 [E used]
    1.3->1.9 [E reflecting]
  Center:
    1.3->1.8 [C for]
    1.3->1.10 [C light]


```

__Sentence__:A mirror reflects light.

```
Loading spaCy model 'en_core_web_md'... Done (13.437s).
corpus-min_0030:
  Light verbs:
    1.1->1.2 [F mirror]
  Predicate nouns:
    1.25->1.26 [P A]
  Function:
    1.1->1.2 [F mirror]
  Participant:
    1.1->1.3 [A [E reflects] [C light] ]
    1.1->1.26 [A A]
  Punctuation:
    1.1->1.4 [U .]
  Elaborator:
    1.3->1.6 [E reflects]
  Center:
    1.3->1.7 [C light]


```

__Sentence__:A plant light is used for help plants by mimicking sunlight.

```
Loading spaCy model 'en_core_web_md'... Done (13.213s).
corpus-min_0031:
  Light verbs:
    1.1->1.2 [F plant]
  Predicate nouns:
    1.33->1.34 [P A]
  Function:
    1.1->1.2 [F plant]
  Participant:
    1.1->1.3 [A [E light] [E is] [C used] [E [R for] [C help] [C plants] [C by] [C mimicking] ] [C sunlight] ]
    1.1->1.34 [A A]
  Punctuation:
    1.1->1.4 [U .]
  Elaborator:
    1.3->1.6 [E light]
    1.3->1.7 [E is]
    1.3->1.9 [E [R for] [C help] [C plants] [C by] [C mimicking] ]
  Center:
    1.3->1.8 [C used]
    1.3->1.10 [C sunlight]
    1.9->1.13 [C help]
    1.9->1.14 [C plants]
    1.9->1.15 [C by]
    1.9->1.16 [C mimicking]
  Relator:
    1.9->1.12 [R for]


```

__Sentence__:A plant requires sunlight for photosynthesis.

```
Loading spaCy model 'en_core_web_md'... Done (13.159s).
corpus-min_0032:
  Light verbs:
    1.1->1.2 [F plant]
  Predicate nouns:
    1.28->1.29 [P A]
  Function:
    1.1->1.2 [F plant]
  Participant:
    1.1->1.3 [A [E requires] [E sunlight] [C for] [E [R photosynthesis] [U .] ] ]
    1.1->1.29 [A A]
  Elaborator:
    1.3->1.5 [E requires]
    1.3->1.6 [E sunlight]
    1.3->1.8 [E [R photosynthesis] [U .] ]
  Center:
    1.3->1.7 [C for]
  Relator:
    1.8->1.10 [R photosynthesis]
  Punctuation:
    1.8->1.11 [U .]


```

__Sentence__:A plant requires sunlight to grow.

```
Loading spaCy model 'en_core_web_md'... Done (13.453s).
corpus-min_0033:
  Light verbs:
    1.1->1.2 [F plant]
  Predicate nouns:
    1.27->1.28 [P A]
  Function:
    1.1->1.2 [F plant]
  Participant:
    1.1->1.3 [A [E requires] [E sunlight] [C to] [C grow] ]
    1.1->1.28 [A A]
  Punctuation:
    1.1->1.4 [U .]
  Elaborator:
    1.3->1.6 [E requires]
    1.3->1.7 [E sunlight]
  Center:
    1.3->1.8 [C to]
    1.3->1.9 [C grow]


```

__Sentence__:A prism refracts light.

```
Loading spaCy model 'en_core_web_md'... Done (13.194s).
corpus-min_0034:
  Light verbs:
    1.1->1.2 [F prism]
  Predicate nouns:
    1.25->1.26 [P A]
  Function:
    1.1->1.2 [F prism]
  Participant:
    1.1->1.3 [A [E refracts] [C light] ]
    1.1->1.26 [A A]
  Punctuation:
    1.1->1.4 [U .]
  Elaborator:
    1.3->1.6 [E refracts]
  Center:
    1.3->1.7 [C light]


```

__Sentence__:A rainbow is formed by refraction of light by splitting light into all different colors.

```
Loading spaCy model 'en_core_web_md'... Done (13.599s).
corpus-min_0035:
  Light verbs:
    1.1->1.2 [F rainbow]
  Predicate nouns:
    1.38->1.39 [P A]
  Function:
    1.1->1.2 [F rainbow]
    1.1->1.5 [F of]
  Participant:
    1.1->1.3 [A [E is] [E formed] [C by] ]
    1.1->1.7 [A all]
    1.1->1.8 [A different]
    1.1->1.39 [A A]
    1.4->1.14 [A [R by] [C splitting] [C light] [C into] ]
  State:
    1.1->1.4 [S [C refraction] ... [A [R by] [C splitting] [C light] [C into] ] ... [C colors] [U .] ]
  Center:
    1.1->1.6 [C light]
    1.3->1.12 [C by]
    1.4->1.13 [C refraction]
    1.4->1.15 [C colors]
    1.14->1.19 [C splitting]
    1.14->1.20 [C light]
    1.14->1.21 [C into]
  Elaborator:
    1.3->1.10 [E is]
    1.3->1.11 [E formed]
  Punctuation:
    1.4->1.16 [U .]
  Relator:
    1.14->1.18 [R by]


```

__Sentence__:A reflector is used to reflect light especially on vehicles.

```
Loading spaCy model 'en_core_web_md'... Done (13.321s).
corpus-min_0036:
  Light verbs:
    1.1->1.2 [F reflector]
  Predicate nouns:
    1.33->1.34 [P A]
  Function:
    1.1->1.2 [F reflector]
  Participant:
    1.1->1.3 [A [E is] [E used] [C to] ]
    1.1->1.34 [A A]
    1.4->1.12 [A [R on] [C vehicles] ]
  State:
    1.1->1.4 [S [C reflect] ... [A [R on] [C vehicles] ] [U .] ]
  Relator:
    1.1->1.5 [R light]
    1.12->1.15 [R on]
  Center:
    1.1->1.6 [C especially]
    1.3->1.10 [C to]
    1.4->1.11 [C reflect]
    1.12->1.16 [C vehicles]
  Elaborator:
    1.3->1.8 [E is]
    1.3->1.9 [E used]
  Punctuation:
    1.4->1.13 [U .]


```

__Sentence__:A star is a source of light energy through nuclear reactions.

```
Loading spaCy model 'en_core_web_md'... Done (13.186s).
corpus-min_0037:
  Light verbs:
    1.1->1.2 [F star]
  Predicate nouns:
    1.34->1.35 [P A]
  Function:
    1.1->1.2 [F star]
  Participant:
    1.1->1.3 [A [E is] [E a] [C source] ]
    1.1->1.35 [A A]
    1.4->1.12 [A [R through] [C nuclear] [C reactions] ]
  State:
    1.1->1.4 [S [C of] ... [A [R through] [C nuclear] [C reactions] ] [U .] ]
  Relator:
    1.1->1.5 [R light]
    1.12->1.15 [R through]
  Center:
    1.1->1.6 [C energy]
    1.3->1.10 [C source]
    1.4->1.11 [C of]
    1.12->1.16 [C nuclear]
    1.12->1.17 [C reactions]
  Elaborator:
    1.3->1.8 [E is]
    1.3->1.9 [E a]
  Punctuation:
    1.4->1.13 [U .]


```

__Sentence__:A star is a source of light through nuclear reactions.

```
Loading spaCy model 'en_core_web_md'... Done (13.569s).
corpus-min_0038:
  Light verbs:
    1.1->1.2 [F star]
  Predicate nouns:
    1.32->1.33 [P A]
  Function:
    1.1->1.2 [F star]
  Participant:
    1.1->1.3 [A [E is] [E a] [C source] ]
    1.1->1.33 [A A]
  State:
    1.1->1.4 [S [C of] ... [C nuclear] [C reactions] [U .] ]
  Relator:
    1.1->1.5 [R light]
  Center:
    1.1->1.6 [C through]
    1.3->1.10 [C source]
    1.4->1.11 [C of]
    1.4->1.12 [C nuclear]
    1.4->1.13 [C reactions]
  Elaborator:
    1.3->1.8 [E is]
    1.3->1.9 [E a]
  Punctuation:
    1.4->1.14 [U .]


```

__Sentence__:A solar panel converts sunlight into electricity.

```
Loading spaCy model 'en_core_web_md'... Done (13.271s).
corpus-min_0039:
  Light verbs:
    1.1->1.2 [F solar]
  Predicate nouns:
    1.29->1.30 [P A]
  Function:
    1.1->1.2 [F solar]
  Participant:
    1.1->1.3 [A [E panel] [E converts] [C sunlight] ]
    1.1->1.30 [A A]
  State:
    1.1->1.4 [S [C into] ... [U .] ]
  Relator:
    1.1->1.5 [R electricity]
  Elaborator:
    1.3->1.7 [E panel]
    1.3->1.8 [E converts]
  Center:
    1.3->1.9 [C sunlight]
    1.4->1.10 [C into]
  Punctuation:
    1.4->1.11 [U .]


```

__Sentence__:A white object reflects all visible light.

```
Loading spaCy model 'en_core_web_md'... Done (14.128s).
corpus-min_0040:
  Light verbs:
    1.1->1.2 [F white]
  Predicate nouns:
    1.30->1.31 [P A]
  Function:
    1.1->1.2 [F white]
  Participant:
    1.1->1.3 [A [E object] [E reflects] [C all] ]
    1.1->1.31 [A A]
  State:
    1.1->1.4 [S [C visible] [E [R light] [U .] ] ]
  Elaborator:
    1.3->1.6 [E object]
    1.3->1.7 [E reflects]
    1.4->1.10 [E [R light] [U .] ]
  Center:
    1.3->1.8 [C all]
    1.4->1.9 [C visible]
  Relator:
    1.10->1.12 [R light]
  Punctuation:
    1.10->1.13 [U .]


```

__Sentence__:Absorbing sunlight causes objects to heat.

```
Loading spaCy model 'en_core_web_md'... Done (13.536s).
corpus-min_0041:
  Light verbs:
    1.1->1.2 [F sunlight]
  Predicate nouns:
    1.1->1.4 [S heat]
    1.27->1.28 [P Absorbing]
  Function:
    1.1->1.2 [F sunlight]
  Participant:
    1.1->1.3 [A [E causes] [E objects] [C to] ]
    1.1->1.28 [A Absorbing]
  State:
    1.1->1.4 [S heat]
  Punctuation:
    1.1->1.5 [U .]
  Elaborator:
    1.3->1.7 [E causes]
    1.3->1.8 [E objects]
  Center:
    1.3->1.9 [C to]


```

__Sentence__:A candle is a source of light when it is burned.

```
Loading spaCy model 'en_core_web_md'... Done (13.460s).
corpus-min_0042:
  Light verbs:
    1.1->1.2 [F candle]
    1.14->1.17 [F is]
  Predicate nouns:
    1.36->1.37 [P A]
  Function:
    1.1->1.2 [F candle]
    1.14->1.17 [F is]
  Participant:
    1.1->1.3 [A [E is] [E a] [C source] ]
    1.1->1.37 [A A]
    1.4->1.10 [A [R light] [L when] [H [A it] [F is] [S [C burned] [U .] ] ] ]
    1.14->1.16 [A it]
  State:
    1.1->1.4 [S [C of] [A [R light] [L when] [H [A it] [F is] [S [C burned] [U .] ] ] ] ]
    1.14->1.18 [S [C burned] [U .] ]
  Elaborator:
    1.3->1.6 [E is]
    1.3->1.7 [E a]
  Center:
    1.3->1.8 [C source]
    1.4->1.9 [C of]
    1.18->1.20 [C burned]
  Relator:
    1.10->1.12 [R light]
  Linker:
    1.10->1.13 [L when]
  ParallelScene:
    1.10->1.14 [H [A it] [F is] [S [C burned] [U .] ] ]
  Punctuation:
    1.18->1.21 [U .]


```

__Sentence__:A desert environment usually has a lot of sunlight.

```
Loading spaCy model 'en_core_web_md'... Done (14.710s).
corpus-min_0043:
  Light verbs:
    1.1->1.2 [F desert]
  Predicate nouns:
    1.32->1.33 [P A]
  Function:
    1.1->1.2 [F desert]
  Participant:
    1.1->1.3 [A [E environment] [E usually] [C has] ]
    1.1->1.33 [A A]
    1.4->1.11 [A [R lot] [L of] [C sunlight] ]
  State:
    1.1->1.4 [S [C a] [A [R lot] [L of] [C sunlight] ] ]
  Punctuation:
    1.1->1.5 [U .]
  Elaborator:
    1.3->1.7 [E environment]
    1.3->1.8 [E usually]
  Center:
    1.3->1.9 [C has]
    1.4->1.10 [C a]
    1.11->1.15 [C sunlight]
  Relator:
    1.11->1.13 [R lot]
  Linker:
    1.11->1.14 [L of]


```

__Sentence__:A revolution is when something revolves around something else.

```
Loading spaCy model 'en_core_web_md'... Done (15.814s).
corpus-min_0044:
  Light verbs:
    1.1->1.2 [F revolution]
  Predicate nouns:
    1.32->1.33 [P A]
  Function:
    1.1->1.2 [F revolution]
  Participant:
    1.1->1.3 [A [E is] [E when] [C something] ]
    1.1->1.33 [A A]
    1.4->1.11 [A [R around] [L something] [C else] ]
  State:
    1.1->1.4 [S [C revolves] [A [R around] [L something] [C else] ] ]
  Punctuation:
    1.1->1.5 [U .]
  Elaborator:
    1.3->1.7 [E is]
    1.3->1.8 [E when]
  Center:
    1.3->1.9 [C something]
    1.4->1.10 [C revolves]
    1.11->1.15 [C else]
  Relator:
    1.11->1.13 [R around]
  Linker:
    1.11->1.14 [L something]


```

__Sentence__:A complete revolution of the Earth around the sun takes one Earth year.

```
Loading spaCy model 'en_core_web_md'... Done (15.704s).
corpus-min_0045:
  Light verbs:
    1.1->1.2 [F complete]
  Predicate nouns:
    1.37->1.38 [P A]
  Function:
    1.1->1.2 [F complete]
  Participant:
    1.1->1.3 [A [E revolution] [E of] [C the] ]
    1.1->1.38 [A A]
    1.4->1.12 [A [R around] [L the] [C sun] ]
    1.4->1.13 [A [E one] [E Earth] [C year] ]
  State:
    1.1->1.4 [S [C Earth] [A [R around] [L the] [C sun] ] ... [A [E one] [E Earth] [C year] ] ]
    1.1->1.5 [S takes]
  Punctuation:
    1.1->1.6 [U .]
  Elaborator:
    1.3->1.8 [E revolution]
    1.3->1.9 [E of]
    1.13->1.18 [E one]
    1.13->1.19 [E Earth]
  Center:
    1.3->1.10 [C the]
    1.4->1.11 [C Earth]
    1.12->1.17 [C sun]
    1.13->1.20 [C year]
  Relator:
    1.12->1.15 [R around]
  Linker:
    1.12->1.16 [L the]


```

__Sentence__:A complete revolution of the Earth around the sun takes one solar year.

```
Loading spaCy model 'en_core_web_md'... Done (13.154s).
corpus-min_0046:
  Light verbs:
    1.1->1.2 [F complete]
    1.14->1.17 [F takes]
  Predicate nouns:
    1.38->1.39 [P A]
  Function:
    1.1->1.2 [F complete]
    1.14->1.17 [F takes]
  Participant:
    1.1->1.3 [A [E revolution] [E of] [C the] ]
    1.1->1.39 [A A]
    1.4->1.10 [A [R around] [L the] [H [A sun] [F takes] [S [C one] [C solar] [C year] ] [U .] ] ]
    1.14->1.16 [A sun]
  State:
    1.1->1.4 [S [C Earth] [A [R around] [L the] [H [A sun] [F takes] [S [C one] [C solar] [C year] ] [U .] ] ] ]
    1.14->1.18 [S [C one] [C solar] [C year] ]
  Elaborator:
    1.3->1.6 [E revolution]
    1.3->1.7 [E of]
  Center:
    1.3->1.8 [C the]
    1.4->1.9 [C Earth]
    1.18->1.21 [C one]
    1.18->1.22 [C solar]
    1.18->1.23 [C year]
  Relator:
    1.10->1.12 [R around]
  Linker:
    1.10->1.13 [L the]
  ParallelScene:
    1.10->1.14 [H [A sun] [F takes] [S [C one] [C solar] [C year] ] [U .] ]
  Punctuation:
    1.14->1.19 [U .]


```

__Sentence__:A revolution is when something revolves around something else.

```
Loading spaCy model 'en_core_web_md'... Done (13.157s).
corpus-min_0047:
  Light verbs:
    1.1->1.2 [F revolution]
  Predicate nouns:
    1.32->1.33 [P A]
  Function:
    1.1->1.2 [F revolution]
  Participant:
    1.1->1.3 [A [E is] [E when] [C something] ]
    1.1->1.33 [A A]
    1.4->1.11 [A [R around] [L something] [C else] ]
  State:
    1.1->1.4 [S [C revolves] [A [R around] [L something] [C else] ] ]
  Punctuation:
    1.1->1.5 [U .]
  Elaborator:
    1.3->1.7 [E is]
    1.3->1.8 [E when]
  Center:
    1.3->1.9 [C something]
    1.4->1.10 [C revolves]
    1.11->1.15 [C else]
  Relator:
    1.11->1.13 [R around]
  Linker:
    1.11->1.14 [L something]


```

__Sentence__:A revolution of the moon around the Earth takes 1 month.

```
Loading spaCy model 'en_core_web_md'... Done (13.361s).
corpus-min_0048:
  Light verbs:
    1.1->1.2 [F revolution]
    1.15->1.18 [F 1]
  Predicate nouns:
    1.15->1.19 [S month]
    1.35->1.36 [P A]
  Function:
    1.1->1.2 [F revolution]
    1.15->1.18 [F 1]
  Participant:
    1.1->1.3 [A [E of] [E the] [C moon] ]
    1.1->1.36 [A A]
    1.4->1.11 [A [R the] [L Earth] [H [A takes] [F 1] [S month] ] ]
    1.15->1.17 [A takes]
  State:
    1.1->1.4 [S [C around] [A [R the] [L Earth] [H [A takes] [F 1] [S month] ] ] ]
    1.15->1.19 [S month]
  Punctuation:
    1.1->1.5 [U .]
  Elaborator:
    1.3->1.7 [E of]
    1.3->1.8 [E the]
  Center:
    1.3->1.9 [C moon]
    1.4->1.10 [C around]
  Relator:
    1.11->1.13 [R the]
  Linker:
    1.11->1.14 [L Earth]
  ParallelScene:
    1.11->1.15 [H [A takes] [F 1] [S month] ]


```

__Sentence__:A planet is exposed to the heat of the star around which it revolves.

```
Loading spaCy model 'en_core_web_md'... Done (13.139s).
corpus-min_0049:
  Light verbs:
    1.1->1.2 [F planet]
  Predicate nouns:
    1.35->1.36 [P A]
  Function:
    1.1->1.2 [F planet]
  Participant:
    1.1->1.3 [A [E is] [E exposed] [C to] [C the] [E heat] [E of] [E the] [E star] [E around] [E which] [E it] [C revolves] ]
    1.1->1.36 [A A]
  Punctuation:
    1.1->1.4 [U .]
  Elaborator:
    1.3->1.6 [E is]
    1.3->1.7 [E exposed]
    1.3->1.10 [E heat]
    1.3->1.11 [E of]
    1.3->1.12 [E the]
    1.3->1.13 [E star]
    1.3->1.14 [E around]
    1.3->1.15 [E which]
    1.3->1.16 [E it]
  Center:
    1.3->1.8 [C to]
    1.3->1.9 [C the]
    1.3->1.17 [C revolves]


```

__Sentence__:A satellite orbits a planet.

```
Loading spaCy model 'en_core_web_md'... Done (13.725s).
corpus-min_0050:
  Light verbs:
    1.1->1.2 [F satellite]
  Predicate nouns:
    1.26->1.27 [P A]
  Function:
    1.1->1.2 [F satellite]
  Participant:
    1.1->1.3 [A [E orbits] [E a] [C planet] ]
    1.1->1.27 [A A]
  Punctuation:
    1.1->1.4 [U .]
  Elaborator:
    1.3->1.6 [E orbits]
    1.3->1.7 [E a]
  Center:
    1.3->1.8 [C planet]


```

__Sentence__:Pluto is the planet that is ninth closest to the Sun.

```
Loading spaCy model 'en_core_web_md'... Done (13.229s).
corpus-min_0051:
  Light verbs:
    1.1->1.2 [F is]
  Predicate nouns:
    1.33->1.34 [P Pluto]
  Function:
    1.1->1.2 [F is]
  Participant:
    1.1->1.3 [A [E the] [E planet] [C that] [C is] [E ninth] [C closest] ]
    1.1->1.4 [A [R to] [E the] [E Sun] ]
    1.1->1.34 [A Pluto]
  Punctuation:
    1.1->1.5 [U .]
  Elaborator:
    1.3->1.7 [E the]
    1.3->1.8 [E planet]
    1.3->1.11 [E ninth]
    1.4->1.14 [E the]
    1.4->1.15 [E Sun]
  Center:
    1.3->1.9 [C that]
    1.3->1.10 [C is]
    1.3->1.12 [C closest]
  Relator:
    1.4->1.13 [R to]


```

__Sentence__:A planet rotating causes cycles of day and night on that planet.

```
Loading spaCy model 'en_core_web_md'... Done (13.129s).
corpus-min_0052:
  Light verbs:
    1.1->1.2 [F planet]
  Predicate nouns:
    1.34->1.35 [P A]
  Function:
    1.1->1.2 [F planet]
  Participant:
    1.1->1.3 [A [E rotating] [E causes] [C cycles] [C of] [E day] [C and] ]
    1.1->1.4 [A [R night] [E on] [E that] ]
    1.1->1.35 [A A]
  Punctuation:
    1.1->1.5 [U planet]
    1.1->1.6 [U .]
  Elaborator:
    1.3->1.8 [E rotating]
    1.3->1.9 [E causes]
    1.3->1.12 [E day]
    1.4->1.15 [E on]
    1.4->1.16 [E that]
  Center:
    1.3->1.10 [C cycles]
    1.3->1.11 [C of]
    1.3->1.13 [C and]
  Relator:
    1.4->1.14 [R night]


```

__Sentence__:Earth is the planet that is third closest to the Sun.

```
Loading spaCy model 'en_core_web_md'... Done (13.172s).
corpus-min_0053:
  Light verbs:
    1.1->1.2 [F is]
  Predicate nouns:
    1.33->1.34 [P Earth]
  Function:
    1.1->1.2 [F is]
  Participant:
    1.1->1.3 [A [E the] [E planet] [C that] [C is] [E third] [C closest] ]
    1.1->1.4 [A [R to] [E the] [C Sun] [U .] ]
    1.1->1.34 [A Earth]
  Elaborator:
    1.3->1.6 [E the]
    1.3->1.7 [E planet]
    1.3->1.10 [E third]
    1.4->1.13 [E the]
  Center:
    1.3->1.8 [C that]
    1.3->1.9 [C is]
    1.3->1.11 [C closest]
    1.4->1.14 [C Sun]
  Relator:
    1.4->1.12 [R to]
  Punctuation:
    1.4->1.15 [U .]


```

__Sentence__:what is the name of Justin Bieber's brother?

```
Loading spaCy model 'en_core_web_md'... Done (13.135s).
corpus-min_0054:
  Light verbs:
    1.1->1.2 [F is]
  Predicate nouns:
    1.31->1.32 [P what]
  Function:
    1.1->1.2 [F is]
  Participant:
    1.1->1.3 [A [E the] [E name] [C of] [C Justin] [E Bieber] [C 's] ]
    1.1->1.4 [A [R brother] [U ?] ]
    1.1->1.32 [A what]
  Elaborator:
    1.3->1.6 [E the]
    1.3->1.7 [E name]
    1.3->1.10 [E Bieber]
  Center:
    1.3->1.8 [C of]
    1.3->1.9 [C Justin]
    1.3->1.11 [C 's]
  Relator:
    1.4->1.12 [R brother]
  Punctuation:
    1.4->1.13 [U ?]


```

__Sentence__:What character did Natalie Portman play in star wars?

```
Loading spaCy model 'en_core_web_md'... Done (13.833s).
corpus-min_0055:
  Light verbs:
    1.1->1.2 [F character]
  Predicate nouns:
    1.30->1.31 [P What]
  Function:
    1.1->1.2 [F character]
  Participant:
    1.1->1.3 [A [E did] [E Natalie] [C Portman] [C play] [E in] [C star] ]
    1.1->1.4 [A wars]
    1.1->1.31 [A What]
  Punctuation:
    1.1->1.5 [U ?]
  Elaborator:
    1.3->1.7 [E did]
    1.3->1.8 [E Natalie]
    1.3->1.11 [E in]
  Center:
    1.3->1.9 [C Portman]
    1.3->1.10 [C play]
    1.3->1.12 [C star]


```

__Sentence__:Where did Donald Trump go to college?

```
Loading spaCy model 'en_core_web_md'... Done (13.044s).
corpus-min_0056:
  Light verbs:
    1.1->1.2 [F did]
  Predicate nouns:
    1.28->1.29 [P Where]
  Function:
    1.1->1.2 [F did]
  Participant:
    1.1->1.3 [A [E Donald] [E Trump] [C go] [C to] [E college] [U ?] ]
    1.1->1.29 [A Where]
  Elaborator:
    1.3->1.5 [E Donald]
    1.3->1.6 [E Trump]
    1.3->1.9 [E college]
  Center:
    1.3->1.7 [C go]
    1.3->1.8 [C to]
  Punctuation:
    1.3->1.10 [U ?]


```

__Sentence__:What countries around the world speak french?
```
Loading spaCy model 'en_core_web_md'... Done (13.028s).
corpus-min_0057:
  Light verbs:
    1.1->1.2 [F countries]
  Predicate nouns:
    1.28->1.29 [P What]
  Function:
    1.1->1.2 [F countries]
  Participant:
    1.1->1.3 [A [E around] [E the] [C world] [C speak] [E french] [U ?] ]
    1.1->1.29 [A What]
  Elaborator:
    1.3->1.5 [E around]
    1.3->1.6 [E the]
    1.3->1.9 [E french]
  Center:
    1.3->1.7 [C world]
    1.3->1.8 [C speak]
  Punctuation:
    1.3->1.10 [U ?]


```