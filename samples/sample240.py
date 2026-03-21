def fake_server(path):
    if path == "/":
        return "Home Page"
    elif path == "/about":
        return "About Us"
    elif path == "/login":
        return "Login Page"
    else:
        return "404"

print(fake_server("/"))
print(fake_server("/about"))
