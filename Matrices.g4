grammar Matrices;

program     : stmt+ ;

stmt        : decl ';'
            | assign ';'
            ;

decl        : 'matrix' ID dims ;

dims        : '[' INT ']' '[' INT ']' ;

assign      : ID '=' expr ;

expr        : expr '*' expr            # MulExpr
            | ID                       # VarExpr
            | '[' row (',' row)* ']'   # MatrixLiteral
            ;

row         : '[' INT (',' INT)* ']' ;

ID          : [a-zA-Z_][a-zA-Z0-9_]* ;
INT         : [0-9]+ ;
WS          : [ \t\r\n]+ -> skip ;
