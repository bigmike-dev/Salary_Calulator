
class Employee:
    def __init__(self, hourly_pay, hours_worked, ot_worked):
        self.hourly_pay = hourly_pay
        self.hours_worked = hours_worked
        self.ot_worked = ot_worked

    @property
    def weekly_pay(self):
        return self.hourly_pay * self.hours_worked

    @property
    def monthly_pay(self):
        return self.weekly_pay * 4

    @property
    def yearly_pay(self):
        return self.weekly_pay * 52

    @property
    def weekly_ot(self):
        return self.ot_worked * (self.hourly_pay * 1.5)

    @property
    def pay_with_ot(self):
        return self.weekly_pay + self.weekly_ot

    @property
    def yearly_with_ot(self):
        return self.pay_with_ot * 52

    def __str__(self):
        return (f"\nEmployee information:\n \nWeekly Pay: {self.weekly_pay} \nMonthly Pay: {self.monthly_pay}"
                f"\nYearly Pay: {self.yearly_pay}\n \nWeekly Overtime Pay: {self.weekly_ot} "
                f"\nWeekly Pay with OT: {self.pay_with_ot} \nYearly Pay with OT: {self.yearly_with_ot}")


hourly_pay = float(input("\nEnter hourly pay: "))
hours_worked = float(input("Enter hours worked per week: "))
ot_worked = float(input("Enter any overtime hours worked: "))

employee = Employee(hourly_pay, hours_worked, ot_worked)

print(employee)





