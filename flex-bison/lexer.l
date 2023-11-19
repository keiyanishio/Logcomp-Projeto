%{
#include <string>
#include <stdio.h>

%}


%%


[ \t]                 ;
[a-zA-Z][a-zA-Z0-9_]*         { return IDENTIFIER;}
\"([^\\\"]|\\.)*\"            { return STRING; }
[0-9]+                        { return INT; }
"rhyme"                       { return VAR; }
"bar"                         { return TYPE; }
"verse"                       { return TYPE; }
"flow"                        { return FOR; }
"lyrical"                     { return IF; }
"beat"                        { return ELSE; }
"Barsize"                     { return SCAN; }
"rap"                         { return PRINT; }
"*"                           { return MULTI; }
"/"                           { return DIV; }
"+"                           { return PLUS; }
"-"                           { return MINUS; }
"("                           { return OPEN; }
")"                           { return CLOSE; }
"="                           { return EQUAL; }
"=="                          { return EQUALCON; }
">"                           { return GT; }
"<"                           { return LT; }
"||"                          { return OR; }
"&&"                          { return AND; }
"!"                           { return NOT; }
"{"                           { return CHAVES_A; }
"}"                           { return CHAVES_F; }
";"                           { return PV; }
"."                           { return CONCAT; }
"rapper"                      { return FUNC; }
"rehearse"                    { return RETURN; }
","                           { return VIRGULA; }
"\n"                          { return NEWLINE; }

.                             {printf("Unknown token!\n"); yyterminate();}

%%
int main() {
    yylex();
    return 0;
}