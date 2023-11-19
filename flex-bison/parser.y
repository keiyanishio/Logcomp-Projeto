%{
  #include<stdio.h>
  int yylex();
  void yyerror(const char *s) { printf("ERROR: %s\n", s); }
%}

%token IDENTIFIER STRING INT

%token VAR TYPE

%token IF ELSE FOR PV

%token PRINT SCAN

%token MULTI DIV PLUS MINUS CONCAT

%token OPEN CLOSE CHAVES_A CHAVES_F

%token EQUAL EQUALCON GT LT OR AND NOT 

%token FUNC RETURN VIRGULA

%token NEWLINE

%start program

%%

program: statement
       | program statement
       ;

block: CHAVES_A NEWLINE statement CHAVES_F ;

statement: assignment
         | print
         | conditional
         | loop
         | var 
         | declaration
         | return_dec
         ;

assignment: IDENTIFIER EQUAL boolexpression;

print: OPEN boolexpression CLOSE;

conditional: IF boolexpression block 
           | IF boolexpression ELSE block
           ;

loop: FOR assignment PV boolexpression PV assignment block;

var: VAR IDENTIFIER TYPE
   | VAR IDENTIFIER TYPE EQUAL boolexpression
   ;

declaration: FUNC IDENTIFIER OPEN CLOSE TYPE block
           | FUNC IDENTIFIER OPEN args CLOSE TYPE block
           ; 

args: IDENTIFIER TYPE
    | IDENTIFIER TYPE VIRGULA args
    ;

return_dec: RETURN boolexpression;

boolexpression: boolterm
              | boolterm OR boolterm
              ;

boolterm: relexpression
        | relexpression AND relexpression
        ;

relexpression: expression
             | expression EQUALCON expression
             | expression GT expression
             | expression LT expression
             ;

expression: term
          | term PLUS term
          | term MINUS term
          | term CONCAT term
          ;

term: factor
    | factor MULTI factor
    | factor DIV factor
    ;

factor: INT
      | STRING
      | IDENTIFIER
      | PLUS factor
      | MINUS factor
      | NOT factor
      | OPEN boolexpression CLOSE
      | SCAN OPEN CLOSE
      ;

%%

int main(){
  yyparse();
  return 0;
}