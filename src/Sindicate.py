class Sindicate:
    def __init__(self, taxPerMonth):
        self.__sindMembers = []
        self.__taxPerMonth = taxPerMonth
        self.__serviceTax = {'Saude':100.00,'Juridico':50.00, 'indenização':150.0}    
    def get_sindMembers(self):
        return self.__sindMembers
    def set_sindMembers(self, membersList):
        self.__sindMembers = membersList    
    def get_taxPerMonth(self):
        return self.__taxPerMonth
    def set_taxPerMonth(self, new_taxPerMonth):
        self.__taxPerMonth = new_taxPerMonth    
    def get_serviceTax(self, tax_type):
        return self.__serviceTax[tax_type]
    def set_serviceTax(self, new_serviceTax, value):
        self.__serviceTax[new_serviceTax] = value
    def id_generetor(self, emp):
        new_id = int(emp.rg[:-4])*17
        return new_id   
    def add_member(self, emp):
        new_id = self.id_generetor(emp)
        self.__sindMembers.append({'id':new_id, 'employee':emp.name})    
    def remove_member(self, emp_sind_id):
        for e in self.__sindMembers:
            if e['id'] == emp_sind_id:
                self.__sindMembers.remove(e['id'])