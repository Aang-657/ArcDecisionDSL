grammar ArchDecision;

// ======================================================
// Parser Rules
// ======================================================

program
    : systemDecl typeDecl requirementsBlock constraintsBlock? 'recommendation' EOF
    ;

systemDecl
    : 'system' ID
    ;

typeDecl
    : 'type' SYSTEM_TYPE
    ;

requirementsBlock
    : 'requirements' '{' requirementItem+ '}'
    ;

requirementItem
    : REQUIREMENT LEVEL
    ;

constraintsBlock
    : 'constraints' '{' constraintItem+ '}'
    ;

constraintItem
    : 'team' LEVEL
    | 'budget' LEVEL
    ;

// =====================
// Lexer Rules (FIXED)
// =====================

SYSTEM_TYPE
    : 'web'
    | 'backend'
    ;

REQUIREMENT
    : 'scalability'
    | 'performance'
    | 'security'
    | 'maintainability'
    ;

LEVEL
    : 'low'
    | 'medium'
    | 'high'
    ;


ID
    : [a-zA-Z_][a-zA-Z0-9_]*
    ;

LINE_COMMENT
    : '//' ~[\r\n]* -> skip
    ;

WS
    : [ \t\r\n]+ -> skip
    ;
