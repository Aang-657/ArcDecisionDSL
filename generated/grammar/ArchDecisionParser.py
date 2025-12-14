# Generated from grammar/ArchDecision.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,15,57,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,0,3,0,19,8,0,1,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,
        1,3,1,3,1,3,4,3,33,8,3,11,3,12,3,34,1,3,1,3,1,4,1,4,1,4,1,5,1,5,
        1,5,4,5,45,8,5,11,5,12,5,46,1,5,1,5,1,6,1,6,1,6,1,6,3,6,55,8,6,1,
        6,0,0,7,0,2,4,6,8,10,12,0,0,53,0,14,1,0,0,0,2,23,1,0,0,0,4,26,1,
        0,0,0,6,29,1,0,0,0,8,38,1,0,0,0,10,41,1,0,0,0,12,54,1,0,0,0,14,15,
        3,2,1,0,15,16,3,4,2,0,16,18,3,6,3,0,17,19,3,10,5,0,18,17,1,0,0,0,
        18,19,1,0,0,0,19,20,1,0,0,0,20,21,5,1,0,0,21,22,5,0,0,1,22,1,1,0,
        0,0,23,24,5,2,0,0,24,25,5,13,0,0,25,3,1,0,0,0,26,27,5,3,0,0,27,28,
        5,10,0,0,28,5,1,0,0,0,29,30,5,4,0,0,30,32,5,5,0,0,31,33,3,8,4,0,
        32,31,1,0,0,0,33,34,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,36,1,
        0,0,0,36,37,5,6,0,0,37,7,1,0,0,0,38,39,5,11,0,0,39,40,5,12,0,0,40,
        9,1,0,0,0,41,42,5,7,0,0,42,44,5,5,0,0,43,45,3,12,6,0,44,43,1,0,0,
        0,45,46,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,48,1,0,0,0,48,49,
        5,6,0,0,49,11,1,0,0,0,50,51,5,8,0,0,51,55,5,12,0,0,52,53,5,9,0,0,
        53,55,5,12,0,0,54,50,1,0,0,0,54,52,1,0,0,0,55,13,1,0,0,0,4,18,34,
        46,54
    ]

class ArchDecisionParser ( Parser ):

    grammarFileName = "ArchDecision.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'recommendation'", "'system'", "'type'", 
                     "'requirements'", "'{'", "'}'", "'constraints'", "'team'", 
                     "'budget'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "SYSTEM_TYPE", "REQUIREMENT", 
                      "LEVEL", "ID", "LINE_COMMENT", "WS" ]

    RULE_program = 0
    RULE_systemDecl = 1
    RULE_typeDecl = 2
    RULE_requirementsBlock = 3
    RULE_requirementItem = 4
    RULE_constraintsBlock = 5
    RULE_constraintItem = 6

    ruleNames =  [ "program", "systemDecl", "typeDecl", "requirementsBlock", 
                   "requirementItem", "constraintsBlock", "constraintItem" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    SYSTEM_TYPE=10
    REQUIREMENT=11
    LEVEL=12
    ID=13
    LINE_COMMENT=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def systemDecl(self):
            return self.getTypedRuleContext(ArchDecisionParser.SystemDeclContext,0)


        def typeDecl(self):
            return self.getTypedRuleContext(ArchDecisionParser.TypeDeclContext,0)


        def requirementsBlock(self):
            return self.getTypedRuleContext(ArchDecisionParser.RequirementsBlockContext,0)


        def EOF(self):
            return self.getToken(ArchDecisionParser.EOF, 0)

        def constraintsBlock(self):
            return self.getTypedRuleContext(ArchDecisionParser.ConstraintsBlockContext,0)


        def getRuleIndex(self):
            return ArchDecisionParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = ArchDecisionParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.systemDecl()
            self.state = 15
            self.typeDecl()
            self.state = 16
            self.requirementsBlock()
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 17
                self.constraintsBlock()


            self.state = 20
            self.match(ArchDecisionParser.T__0)
            self.state = 21
            self.match(ArchDecisionParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SystemDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ArchDecisionParser.ID, 0)

        def getRuleIndex(self):
            return ArchDecisionParser.RULE_systemDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSystemDecl" ):
                listener.enterSystemDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSystemDecl" ):
                listener.exitSystemDecl(self)




    def systemDecl(self):

        localctx = ArchDecisionParser.SystemDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_systemDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(ArchDecisionParser.T__1)
            self.state = 24
            self.match(ArchDecisionParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SYSTEM_TYPE(self):
            return self.getToken(ArchDecisionParser.SYSTEM_TYPE, 0)

        def getRuleIndex(self):
            return ArchDecisionParser.RULE_typeDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeDecl" ):
                listener.enterTypeDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeDecl" ):
                listener.exitTypeDecl(self)




    def typeDecl(self):

        localctx = ArchDecisionParser.TypeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_typeDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(ArchDecisionParser.T__2)
            self.state = 27
            self.match(ArchDecisionParser.SYSTEM_TYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RequirementsBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def requirementItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArchDecisionParser.RequirementItemContext)
            else:
                return self.getTypedRuleContext(ArchDecisionParser.RequirementItemContext,i)


        def getRuleIndex(self):
            return ArchDecisionParser.RULE_requirementsBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequirementsBlock" ):
                listener.enterRequirementsBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequirementsBlock" ):
                listener.exitRequirementsBlock(self)




    def requirementsBlock(self):

        localctx = ArchDecisionParser.RequirementsBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_requirementsBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(ArchDecisionParser.T__3)
            self.state = 30
            self.match(ArchDecisionParser.T__4)
            self.state = 32 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 31
                self.requirementItem()
                self.state = 34 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==11):
                    break

            self.state = 36
            self.match(ArchDecisionParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RequirementItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REQUIREMENT(self):
            return self.getToken(ArchDecisionParser.REQUIREMENT, 0)

        def LEVEL(self):
            return self.getToken(ArchDecisionParser.LEVEL, 0)

        def getRuleIndex(self):
            return ArchDecisionParser.RULE_requirementItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequirementItem" ):
                listener.enterRequirementItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequirementItem" ):
                listener.exitRequirementItem(self)




    def requirementItem(self):

        localctx = ArchDecisionParser.RequirementItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_requirementItem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(ArchDecisionParser.REQUIREMENT)
            self.state = 39
            self.match(ArchDecisionParser.LEVEL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstraintsBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constraintItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArchDecisionParser.ConstraintItemContext)
            else:
                return self.getTypedRuleContext(ArchDecisionParser.ConstraintItemContext,i)


        def getRuleIndex(self):
            return ArchDecisionParser.RULE_constraintsBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstraintsBlock" ):
                listener.enterConstraintsBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstraintsBlock" ):
                listener.exitConstraintsBlock(self)




    def constraintsBlock(self):

        localctx = ArchDecisionParser.ConstraintsBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_constraintsBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(ArchDecisionParser.T__6)
            self.state = 42
            self.match(ArchDecisionParser.T__4)
            self.state = 44 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 43
                self.constraintItem()
                self.state = 46 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==8 or _la==9):
                    break

            self.state = 48
            self.match(ArchDecisionParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstraintItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEVEL(self):
            return self.getToken(ArchDecisionParser.LEVEL, 0)

        def getRuleIndex(self):
            return ArchDecisionParser.RULE_constraintItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstraintItem" ):
                listener.enterConstraintItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstraintItem" ):
                listener.exitConstraintItem(self)




    def constraintItem(self):

        localctx = ArchDecisionParser.ConstraintItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_constraintItem)
        try:
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.match(ArchDecisionParser.T__7)
                self.state = 51
                self.match(ArchDecisionParser.LEVEL)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.match(ArchDecisionParser.T__8)
                self.state = 53
                self.match(ArchDecisionParser.LEVEL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





