import xml.etree.ElementTree

class Angular(object):
    """docstring for ."""
    filename = ""

    def __init__(self, xml, name):
        self.filename = name
        self.generate_angular(xml)


    def stripInfo(self, elem):
        if elem.tag == 'var':
            return elem.get('name'), elem.get('type')
        elif elem.tag == 'controller' or elem.tag == 'factory' or elem.tag == 'function' or elem.tag == 'module':
            deps = []
            if elem.get('dep'):
                dep = elem.get('dep')
                if ' ' in dep:

                    deps = dep.split(' ')
                else:
                    deps.append(dep)
            return elem.get('name'), deps

    def getFunctions(self, elem):
        fs = []
        for f in elem.findall('function'):
            fs.append(f)
        return fs

    def getVars(self, elem):
        vs = []
        for v in elem.findall('var'):
            vs.append(v)
        return vs

    def getControllers(self, elem):
        cs = []
        for c in elem.findall('controller'):
            cs.append(c)
        return cs

    def getFactories(self, elem):
        fs = []
        for f in elem.findall('factory'):
            fs.append(f)
        return fs

    def create_file(self, filename, code):
        filename += ".js"
        file = open(filename, "w+")
        file.write(code)
        file.close()

    def generate_angular(self, src):
        output = ""
        e = xml.etree.ElementTree.parse(src).getroot()
        m_name, m_dep = self.stripInfo(e)
        output += "angular.module('"+m_name+"', "+str(m_dep)+")\n"
        ctrls = self.getControllers(e)
        facts = self.getFactories(e)
        for ctrl in ctrls:
            deps = ""
            name, dep = self.stripInfo(ctrl)

            for d in dep:
                deps += "$"+d + ","

            output += ".controller('"+ name + "',function(" + deps[:-1] +") {\n"
            funcs = self.getFunctions(ctrl)
            for func in funcs:
                name, dep = self.stripInfo(func)
                deps = ""
                for d in dep:
                    deps += d + ","
                output += "     function "+name+"("+deps[:-1]+") {\n    // Body....\n   }\n"
            vars = self.getVars(ctrl)
            for var in vars:
                name, type = self.stripInfo(var)
                output += "     var "+name+" = "
                if type == 'pojo':
                    output += "{};\n"
                elif type == 'str':
                    output += "\"\";\n"
                elif type == 'bool':
                    output += "false;\n"
                elif type == 'int':
                    output += "0;\n"
            output += "\n})\n"

        for fact in facts:
            deps = ""
            name, dep = self.stripInfo(fact)
            for d in dep:
                deps += "$"+d + ","
            output += ".factory('"+ name + "',function(" + deps[:-1] +") {\n    var out;\n"
            for func in funcs:
                name, dep = self.stripInfo(func)
                deps = ""
                for d in dep:
                    deps += d + ","
                output += "     out."+name+" = function "+name+"("+deps[:-1]+") {\n    // Body....\n   };\n"
            for var in vars:
                name, type = self.stripInfo(var)
                output += "     var "+name+" = "
                if type == 'pojo':
                    output += "{};\n"
                elif type == 'str':
                    output += "\"\";\n"
                elif type == 'int':
                    output += "0;\n"
            output += "\n   return out;\n})\n"
        output += ";"
        self.create_file(self.filename, output)
