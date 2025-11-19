from MatricesVisitor import MatricesVisitor

class Analizador(MatricesVisitor):
    def __init__(self):
        self.vars = {}
        self.errores = []

    def visitDecl(self, ctx):
        n = ctx.ID().getText()
        f = int(ctx.dims().INT(0).getText())
        c = int(ctx.dims().INT(1).getText())
        self.vars[n] = (f, c)

    def visitAssign(self, ctx):
        n = ctx.ID().getText()
        _, d = self.visit(ctx.expr())
        if d:
            self.vars[n] = d

    def visitVarExpr(self, ctx):
        n = ctx.ID().getText()
        if n not in self.vars:
            self.errores.append(f"'{n}' no declarada")
            return None, None
        return None, self.vars[n]

    def visitMatrixLiteral(self, ctx):
        filas = len(ctx.row())
        if filas == 0:
            return None, (0, 0)
        cols = len(ctx.row(0).INT())
        for i in range(filas):
            if len(ctx.row(i).INT()) != cols:
                self.errores.append(" Filas desiguales")
                return None, None
        return None, (filas, cols)

    def visitMulExpr(self, ctx):
        _, (m, n) = self.visit(ctx.expr(0))
        _, (p, q) = self.visit(ctx.expr(1))
        if m is None or p is None:
            return None, None
        if n != p:
            self.errores.append(f"{m}x{n} × {p}x{q} → incompatible")
            return None, None
        print(f"{m}x{n} × {p}x{q} = {m}x{q}")
        return None, (m, q)
