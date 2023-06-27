# Prompt user for the file name:
file_name = input("File Name: ").strip().lower()

# Retrieve extension from file name
if "." in file_name:
    extension = file_name.rsplit(".", 1)[1]
else:
    extension = file_name

# Check file extension:
match extension:
    case "gif" | "jpeg" | "jpg" | "png":
        if extension == "jpg":
            extension = "jpeg"
        print("image/" + extension)
    case "pdf" | "zip":
        print("application/" + extension)
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")