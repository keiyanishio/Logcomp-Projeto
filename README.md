# Logcomp-Projeto

# FLOW LANG 

## EBNF

```
PROGRAM = { STATEMENT };

BLOCK = { "{", STATEMENT, "}"};

STATEMENT = ( λ | ASSIGNMENT | PRINT | CONDITONAL | LOOP | VAR ), "\n" ;

ASSIGMENT = IDENTIFIER, "=", EXPRESSION;

PRINT = "rap", "#", EXPRESSION, "#";

EXPRESSION = TERM, {("+" | "-" | "."), TERM};

TERM = FACTOR, {("*" | "/"), FACTOR };

FACTOR = (("+" | "-" | "!"), FACTOR | NUMBER | LETTER | "(", EXPRESSION, ")" | IDENTIFIER | PRINT, "(", ")");

COMPARISON = (EXPRESSION, ("==" | "<" | ">" | "<=" | ">="), EXPRESSION);

LOGICAL_OPERATOR = (EXPRESSION, ("switch" | "mashup"), EXPRESSION);

VAR = "rhyme", IDENTIFIER, { "bar" | "verse" | "=", EXPRESSION};

LOOP = "flow", ASSIGMENT, ";", EXPRESSION, ";", ASSIGMENT, BLOCK;

CONDITIONAL = "lyrical", EXPRESSION, {"beat", BLOCK|BLOCK};

IDENTIFIER = LETTER, { LETTER | DIGIT | "_"};

NUMBER = DIGIT, { DIGIT };

LETTER = ( a | ... | z | A | .. | Z);

DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 );
```

rhyme -> var 

bar -> int 

verse -> string 

flow -> for

switch -> ||

mashup -> &&

lyrical -> if 

beat -> else



