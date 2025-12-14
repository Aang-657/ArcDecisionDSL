# Generated from grammar/ArchDecision.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ArchDecisionParser import ArchDecisionParser
else:
    from ArchDecisionParser import ArchDecisionParser

# This class defines a complete generic visitor for a parse tree produced by ArchDecisionParser.

class ArchDecisionVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ArchDecisionParser#program.
    def visitProgram(self, ctx:ArchDecisionParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArchDecisionParser#systemDecl.
    def visitSystemDecl(self, ctx:ArchDecisionParser.SystemDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArchDecisionParser#typeDecl.
    def visitTypeDecl(self, ctx:ArchDecisionParser.TypeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArchDecisionParser#requirementsBlock.
    def visitRequirementsBlock(self, ctx:ArchDecisionParser.RequirementsBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArchDecisionParser#requirementItem.
    def visitRequirementItem(self, ctx:ArchDecisionParser.RequirementItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArchDecisionParser#constraintsBlock.
    def visitConstraintsBlock(self, ctx:ArchDecisionParser.ConstraintsBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArchDecisionParser#constraintItem.
    def visitConstraintItem(self, ctx:ArchDecisionParser.ConstraintItemContext):
        return self.visitChildren(ctx)



del ArchDecisionParser