d=dict()
class Employee:
	def input(self):
		self.name=input("Enter your name")
		self.address=input("Enter your address")
		self.pan=input("Enter your pan number")
		self.basic=int(input("Enter your basic salary"))
		self.tds=0.10*self.basic
		self.da=0.30*self.basic
		self.hra=0.10*self.basic
		self.deductions=0.20*self.basic
		self.gross_sal=self.basic+self.da+self.hra
		self.net_pay=self.gross_sal-self.deductions-self.tds
		self.update()
	def update(self):
		d.update({ self.name:{
		"name":self.name,
		"address":self.address,
		"pan":self.pan,
		"basic":self.basic,
		"tds":self.tds,
		"da":self.da,
		"hra":self.hra,
		"deductions":self.deductions,
		"gross salary":self.gross_sal,
		"net pay":self.net_pay
		}})
	def search(self,name):
		flag=0
		for key in d:
			if key == name:
				flag=1
				print("Employee found")
				for i in d[key]:
					print(i,d[key][i])
		if flag == 0:
			print("No employee found matching")
	def empprint(self):
		for key in d:
			print(key,d[key])
while(True):
	emp=Employee()
	print("="*61)
	print("\tMenu")
	print("="*61)
	print("\n1.Add employee details\n2.Searh Employee by name\n3.Print  employee details\n4.Exit\n")  
	ch=int(input("Enter your choice "))
	if(ch == 1):
		emp.input()
	elif ch == 2:
		name=input("Enter the name to search")
		emp.search(name)
	elif ch == 3:
		emp.empprint()
	elif ch == 4:
		break
	else:
		print("Enter correct choice")
print("Thank you")
