print('---------- Welcome to the Employee Financial Insights System! ----------')



# Collect user input
name=input("Enter full name: ")
department=input("Enter department: ")
experience=input("Enter years of experience: ")
salary=input("Enter current salary ($): ")



# Convert numeric values
experience=int(experience)
salary=float(salary)


# Perform salary calculations
annual_salary=salary*12 # Compute annual salary
tax_deduction=salary*0.12 # Apply 12% tax
take_home_salary=salary-tax_deduction # Post-tax Salary



# Estimate salary growth over the next 5 years
growth_rate=0.05 # 5% annual increment
year_1=salary*(1+growth_rate)
year_2=year_1*(1+growth_rate)
year_3=year_2*(1+growth_rate)
year_4=year_3*(1+growth_rate)
year_5=year_4*(1+growth_rate)


# Calculate potential Savings assuming 20% of post-tax salary in saved
annual_savings=take_home_salary*0.20
five_year_savings=annual_savings*5



# Display the collected data
print("\n--- Employee Financial Profile ---")
print("Name:",name)
print("Department:",department)
print("Experience (years):",experience)
print(f"Current Monthly Salary: ${salary:.2f}")
print(f"Expected Annual Salary: ${annual_salary:.2f}") 
print(f"Estimated Post-Tax Monthly Salary: ${take_home_salary:.2f}") 
print(f"Projected Salary Growth (Next 5 Years):") 
print(f" Year 1: ${year_1:.2f}") 
print(f" Year 2: ${year_2:.2f}") 
print(f" Year 3: ${year_3:.2f}") 
print(f" Year 4: ${year_4:.2f}") 
print(f" Year 5: ${year_5:.2f}") 
print(f"Potential Annual Savings: ${annual_savings:.2f}") 
print(f"Projected 5-Year Savings: ${five_year_savings:.2f}") 
