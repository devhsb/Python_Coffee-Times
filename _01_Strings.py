print("A person who never made mistake, never tried anything new. 'Alber Einstein'")

name = " haseeb pjr "
print(name.title())

# Remove left and right spaces
print(name.strip())

# Remove right spaces
print(name.rstrip())

# Remove left spaces
print(name.lstrip())

# Lowercase
print(name.lower())

# Uppercase
print(name.upper())

# Remove prefix
url = "https://www.facebook.com"
print(url.removeprefix('https://'))

# remove suffix
book = 'python_course.pdf'
print(book.removesuffix(".pdf"))


# f-string - compose or combine variables value
first_name = "HaSeeb"
last_name = "Pjr"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name}")