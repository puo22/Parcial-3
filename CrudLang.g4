grammar CrudLang;

program     : stmt+ ;

stmt        : createStmt ';'
            | selectStmt ';'
            | updateStmt ';'
            | deleteStmt ';'
            ;

createStmt  : 'CREATE' 'TABLE' ID '(' colList ')' ;
colList     : colDef (',' colDef)* ;
colDef      : ID colType ;
colType     : 'INT' | 'VARCHAR' | 'FLOAT' ;

selectStmt  : 'SELECT' selectList 'FROM' ID ('WHERE' expr)? ;
selectList  : '*' | ID (',' ID)* ;

updateStmt  : 'UPDATE' ID 'SET' setList ('WHERE' expr)? ;
setList     : setItem (',' setItem)* ;
setItem     : ID '=' expr ;

deleteStmt  : 'DELETE' 'FROM' ID ('WHERE' expr)? ;

expr        : expr ('=' | '<>' | '<' | '>') expr
            | expr ('+' | '-') expr
            | expr ('*' | '/') expr
            | '(' expr ')'
            | ID
            | STRING
            | INT
            ;

ID          : [a-zA-Z_][a-zA-Z0-9_]* ;
INT         : [0-9]+ ;
STRING      : '\'' (~['\r\n] | '\'\'')* '\'' ;
WS          : [ \t\r\n]+ -> skip ;
COMMENT     : '--' ~[\r\n]* -> skip ;
