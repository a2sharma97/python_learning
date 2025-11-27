user_one_details = {"abhishek", "sharma", "developer"}
user_two_details = {"khushi", "sharma", "designer"}

# union
all_users = user_one_details | user_two_details

print(f'All users: {all_users}')

common_in_user = user_one_details & user_two_details
print(f"Common users: {common_in_user}")

uncommon_in_user_one = user_one_details - user_two_details
print(f"Uncommon details of user one: {uncommon_in_user_one}")