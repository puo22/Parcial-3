from CrudLangVisitor import CrudLangVisitor

class SQLAttributeVisitor(CrudLangVisitor):
    def __init__(self):
        self.catalogo = {}
        self.errores = []

    def visitCreateStmt(self, ctx):
        tabla = ctx.ID().getText()
        if tabla in self.catalogo:
            self.errores.append(f"Tabla '{tabla}' ya existe")
            return
        cols = [col.ID().getText() for col in ctx.colList().colDef()]
        self.catalogo[tabla] = cols
        print(f"CREATE TABLE {tabla} → {cols}")

    def visitSelectStmt(self, ctx):
        tabla = ctx.ID().getText()
        if tabla not in self.catalogo:
            self.errores.append(f"Tabla desconocida: {tabla}")
            return
        if ctx.selectList().getText() == '*':
            cols = self.catalogo[tabla]
        else:
            cols = [id.getText() for id in ctx.selectList().ID()]
            for c in cols:
                if c not in self.catalogo[tabla]:
                    self.errores.append(f"Columna '{c}' no existe en '{tabla}'")
        print(f"SELECT {cols} FROM {tabla}")

    def visitUpdateStmt(self, ctx):
        tabla = ctx.ID().getText()
        if tabla not in self.catalogo:
            self.errores.append(f"Tabla desconocida en UPDATE: {tabla}")
            return
        for item in ctx.setList().setItem():
            col = item.ID().getText()
            if col not in self.catalogo[tabla]:
                self.errores.append(f"Columna '{col}' inválida en SET")
        print(f"UPDATE {tabla}")

    def visitDeleteStmt(self, ctx):
        tabla = ctx.ID().getText()
        if tabla not in self.catalogo:
            self.errores.append(f"Tabla desconocida en DELETE: {tabla}")
            return
        print(f"✅ DELETE FROM {tabla}")
