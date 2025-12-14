# Generated from grammar/ArchDecision.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ArchDecisionParser import ArchDecisionParser
else:
    from ArchDecisionParser import ArchDecisionParser

# This class defines a complete listener for a parse tree produced by ArchDecisionParser.
class ArchDecisionListener(ParseTreeListener):

    # Enter a parse tree produced by ArchDecisionParser#program.
    def enterProgram(self, ctx:ArchDecisionParser.ProgramContext):
        pass

    # Exit a parse tree produced by ArchDecisionParser#program.
    def exitProgram(self, ctx:ArchDecisionParser.ProgramContext):
        pass


    # Enter a parse tree produced by ArchDecisionParser#systemDecl.
    def enterSystemDecl(self, ctx:ArchDecisionParser.SystemDeclContext):
        pass

    # Exit a parse tree produced by ArchDecisionParser#systemDecl.
    def exitSystemDecl(self, ctx:ArchDecisionParser.SystemDeclContext):
        pass


    # Enter a parse tree produced by ArchDecisionParser#typeDecl.
    def enterTypeDecl(self, ctx:ArchDecisionParser.TypeDeclContext):
        pass

    # Exit a parse tree produced by ArchDecisionParser#typeDecl.
    def exitTypeDecl(self, ctx:ArchDecisionParser.TypeDeclContext):
        pass


    # Enter a parse tree produced by ArchDecisionParser#requirementsBlock.
    def enterRequirementsBlock(self, ctx:ArchDecisionParser.RequirementsBlockContext):
        pass

    # Exit a parse tree produced by ArchDecisionParser#requirementsBlock.
    def exitRequirementsBlock(self, ctx:ArchDecisionParser.RequirementsBlockContext):
        pass


    # Enter a parse tree produced by ArchDecisionParser#requirementItem.
    def enterRequirementItem(self, ctx:ArchDecisionParser.RequirementItemContext):
        pass

    # Exit a parse tree produced by ArchDecisionParser#requirementItem.
    def exitRequirementItem(self, ctx:ArchDecisionParser.RequirementItemContext):
        pass


    # Enter a parse tree produced by ArchDecisionParser#constraintsBlock.
    def enterConstraintsBlock(self, ctx:ArchDecisionParser.ConstraintsBlockContext):
        pass

    # Exit a parse tree produced by ArchDecisionParser#constraintsBlock.
    def exitConstraintsBlock(self, ctx:ArchDecisionParser.ConstraintsBlockContext):
        pass


    # Enter a parse tree produced by ArchDecisionParser#constraintItem.
    def enterConstraintItem(self, ctx:ArchDecisionParser.ConstraintItemContext):
        pass

    # Exit a parse tree produced by ArchDecisionParser#constraintItem.
    def exitConstraintItem(self, ctx:ArchDecisionParser.ConstraintItemContext):
        pass



del ArchDecisionParser