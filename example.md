# Parse Overview

Parse results for sentence `Glass does not conduct electricity`

## AMR 

```
(c / conduct-01
    :polarity -
    :ARG0 (g / glass)
    :ARG1 (e / electricity))
```

## UCCA

```
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

## UDS (brief)

```
?a does not conduct ?b
    ?a: Glass
    ?b: electricity
```

## UDS (full)

```
?a does not conduct ?b	[conduct-	root,add_root(conduct/3)_for_dobj_from_(electricity/4),add_root(conduct/3)_for_nsubj_from_(Glass/0),n1,n1,n1,n2,n2,u]
		?a: Glass	[Glass-nsubj,g1(nsubj)]
		?b: electricity	[electricity-dobj,g1(dobj)]

```

## DRS

```
DRS-0( 
	glass( X1 ) NOT( 
		DRS-0( electricity( X1 ) 
			   conduct( E1 ) 
			   Agent( E1 X1 ) 
			   Theme( E1 X1 ) 
			   now( T1 ) 
			   Temp_included( E1 T2 ) Equ( T2 T1 ) ) ) )
```