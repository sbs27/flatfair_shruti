class OrganisationUnitConfig:
    def __init__(self,has_fixed_membership_fee:bool, fixed_membership_fee:int):
        self.has_fixed_membership_fee = has_fixed_membership_fee
        self.fixed_membership_fee = fixed_membership_fee

class OrganisationUnit:
    def __init__(self,name:str, config:OrganisationUnitConfig):
        self.name = name
        self.config = config
        self.parent = None
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
        child.parent = self

def calculate_membership_fee(rent_amount:int, rent_period:str, organisation_unit: OrganisationUnit) ->int:

    # Validation: checking if rent amount is within the specified range
    if rent_period not in ["month", "week"]:
        raise ValueError("Invalid rent period. Expected 'month' or 'week'")
    if rent_period == 'month' and (rent_amount < 11000 or rent_amount > 866000):
        raise ValueError("Invalid rent amount for monthly rent period")
    if rent_period == 'week' and (rent_amount < 2500 or rent_amount > 200000):
        raise ValueError("Invalid rent amount for weekly rent period")

    min_membership_fee = 12000 * 1.2 

    if rent_period =="month":
        one_week_rent = rent_amount * 2.334 #converting monthly rent to weekly
    else:
        one_week_rent = rent_amount 

    if rent_amount <= 12000:
        membership_fee = min_membership_fee 
    else:
        membership_fee = one_week_rent * 1.2 # Membership fee is one week of rent with 20% VAT
    
    current_unit = organisation_unit

    while current_unit is not None:
        if current_unit.config is not None and current_unit.config.has_fixed_membership_fee:
            membership_fee = current_unit.config.fixed_membership_fee
            break
        current_unit = current_unit.parent
    return int(membership_fee)