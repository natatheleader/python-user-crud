from crud import UserService

service = UserService()

# Create a new user
user = service.create_user("john_doe", "password123")
print(user)  # User(username='john_doe', password='password123', active=True)

# Read a user
user = service.read_user("john_doe")
print(user)  # User(username='john_doe', password='password123', active=True)

# Update a user
user = service.update_user("john_doe", "newpassword", False)
print(user)  # User(username='john_doe', password='newpassword', active=False)

# Delete a user
success = service.delete_user("john_doe")
print(success)  # True