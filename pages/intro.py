# from datetime import datetime
# current_date = datetime.now()
# print(f'{current_date.day} is current date')
# #name = input('tell us your name')
# #print('hello')
# #print(name)
# # control k c for commenting out codes...
# full_name = 'Anthony Awoniyi Inumidun'
# your_thought = 'I love my life honestly...'
# print(full_name)
# print(full_name.upper())
# print(full_name.lower())
# print(full_name.capitalize())
# print(full_name.count('n'))

# print(f' Hello, {full_name} {your_thought}')

# price = input("How much did you pay at EDEKA?")
# price_float_number = float(price)
# if price_float_number >= 200:
#     tax = 0.7
# else:
#     tax = 0
# print(f"{tax}, is the tax you have paid at edeka")


# region = input("Which region did you buy from?")
# convert_region = region.lower()
# price = input(f"How much did you pay at WALMART {convert_region}?")
# convert_price = int(price)
# if convert_price >= 200:
#     if convert_region in ("nunavut", "alberta"):
#         tax = 0.07
#     elif convert_region == "ontario":
#         tax = 0.05
#     else:
#         tax = 0.01
#     print(f" You paid {tax} in tax at{convert_region}")

# else:
#     print("No Tax is charged on Products less than 200")

# names = ["Fiwasaye", "Anthony", "Damilola", "Foluwa"]
# names.insert(0, "Bukola")
# print(len(names))
# print(names)

# List are Arrays in Python
# Dictionaries are Oject in Python
# We can create a List of Dictionaries
# people = []
# people = [
#     {"first": "Anthony", "last": "ilufoye"},
#     {"first": "Jongbo", "last": "Olubukola"},
# ]

# print(people)

# For loops in Python
# people = ["Anthony", "Bukola"]

# for name in people:
#     print(name)

#     if people[0] == "Anthony":
#         print(people[0])
#     else:
#         print("No")

# Functions in python


def extract_initials(name):
    initial = name[0:1]
    return initial


first_name = "Anthony"
first_name_initial = extract_initials(first_name)


other_name = "Awoniyi"
other_name_initial = extract_initials(other_name)
print(f" Your initials is: {first_name_initial}{other_name_initial}")

"""Add simulation parameter control
    st.subheader("Simulation Parameters")
    parameter = st.slider("Parameter", min_value=0, max_value=100, value=50)

    # Modify simulation parameters based on user input
    modified_data = data.copy()
    modified_data["parameter"] = modified_data["parameter"] * parameter

    # Display modified results
    st.subheader("Modified Simulation Results")
    st.line_chart(modified_data["value"])

    # Access detailed simulation results
    st.subheader("Detailed Results")
    st.write(data.describe())

    # Export data
    if st.button("Export Data"):
        modified_data.to_csv("simulation_results_modified.csv", index=False)
        st.success("Data exported successfully.")
"""