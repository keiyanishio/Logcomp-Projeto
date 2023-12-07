# Logcomp-Projeto

# FLOW LANG 

## EBNF

```
PROGRAM = { STATEMENT };

BLOCK = { "{", STATEMENT, "}"};

STATEMENT = ( λ | ASSIGNMENT | PRINT | CONDITONAL | LOOP | VAR | DECLARATION | RETURN_DEC ), "\n" ;

ASSIGMENT = IDENTIFIER, "=", BOOLEXPRESSION;

PRINT = "rap", "(", BOOLEXPRESSION, ")";

EXPRESSION = TERM, {("+" | "-" | "."), TERM};

TERM = FACTOR, {("*" | "/"), FACTOR };

FACTOR = (("+" | "-" | "!"), FACTOR | NUMBER | STRING | "(", EXPRESSION, ")" | IDENTIFIER, [ "(", ( { BOOLEXPRESSION, ( ",", BOOLEXPRESSION| λ ) } | λ ), ")" ] | 
SCAN, "(", ")");

RELEXPRESSION = EXPRESSION, {("==" | "<" | ">"), EXPRESSION};

BOOLEXPRESSION = BOOLTERM, {("||"), BOOLTERM};

BOOLTERM = RELEXPRESSION, {("&&"), RELEXPRESSION};

VAR = "rhyme", IDENTIFIER, { "bar" | "verse" | "=", EXPRESSION};

LOOP = "flow", ASSIGMENT, ";", EXPRESSION, ";", ASSIGMENT, BLOCK;

DECLARATION = "rapper", IDENTIFIER, "(", ( { IDENTIFIER, TYPE, (",", λ) } | λ ), ")", TYPE, BLOCK;

RETURN_DEC = "rehearse", BOOLEXPRESSION; 

CONDITIONAL = "lyrical", EXPRESSION, {"beat", BLOCK|BLOCK};

IDENTIFIER = LETTER, { LETTER | DIGIT | "_"};

NUMBER = DIGIT, { DIGIT };

STRING = ( a | ... | z | A | .. | Z);

DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 );
```

rhyme -> var 

bar -> int 

verse -> string 

flow -> for

lyrical -> if 

beat -> else

barsize -> scanln

rap -> println

rapper -> func

rehearse -> return