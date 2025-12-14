from generated.ArchDecisionParser import ArchDecisionParser
from generated.ArchDecisionVisitor import ArchDecisionVisitor


class ArchDecisionInterpreter(ArchDecisionVisitor):

    def __init__(self):
        self.system_name = None
        self.system_type = None
        self.requirements = {}
        self.constraints = {}

    # system ECommerce
    def visitSystemDecl(self, ctx: ArchDecisionParser.SystemDeclContext):
        self.system_name = ctx.ID().getText()
        return None

    # type web
    def visitTypeDecl(self, ctx: ArchDecisionParser.TypeDeclContext):
        self.system_type = ctx.SYSTEM_TYPE().getText()
        return None

    # scalability high
    def visitRequirementItem(self, ctx: ArchDecisionParser.RequirementItemContext):
        key = ctx.REQUIREMENT().getText()
        value = ctx.LEVEL().getText()
        self.requirements[key] = value
        return None

    # team small / budget medium
    def visitConstraintItem(self, ctx):
        if ctx.getChild(0).getText() == "team":
            self.constraints["team"] = ctx.LEVEL().getText()
        elif ctx.getChild(0).getText() == "budget":
            self.constraints["budget"] = ctx.LEVEL().getText()
        return None

    # recommendation
    def visitProgram(self, ctx: ArchDecisionParser.ProgramContext):
        self.visitChildren(ctx)
        self.generate_recommendation()
        return None

    # ==================================================
    # Decision Logic
    # ==================================================
    def generate_recommendation(self):
        print("\nArchitecture Decision Result")
        print("----------------------------")
        print(f"System Name : {self.system_name}")
        print(f"System Type : {self.system_type}")

        architecture = self.decide_architecture_style()
        api = self.decide_api_style()
        database = self.decide_database()
        deployment = self.decide_deployment()

        print(f"- Architecture Style : {architecture}")
        print(f"- API Style          : {api}")
        print(f"- Database           : {database}")
        print(f"- Deployment         : {deployment}")

    def decide_architecture_style(self):
        scalability = self.requirements.get("scalability", "low")
        team = self.constraints.get("team", "small")

        if scalability == "high" and team != "small":
            return "Microservices"
        return "Monolithic"

    def decide_api_style(self):
        performance = self.requirements.get("performance", "low")

        if performance == "high":
            return "REST"
        return "REST"

    def decide_database(self):
        scalability = self.requirements.get("scalability", "low")

        if scalability == "high":
            return "NoSQL"
        return "Relational"

    def decide_deployment(self):
        budget = self.constraints.get("budget", "low")

        if budget in ["medium", "high"]:
            return "Cloud"
        return "On-Premise"
