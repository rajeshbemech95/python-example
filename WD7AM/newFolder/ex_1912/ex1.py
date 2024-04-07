def read_text_file(file_path):
   
    with open(file_path, 'r') as file:
        content = file.read()
        return content
        
file_path = 'example.txt'  # Replace with the path to your text file
file_content = read_text_file(file_path)
print(file_content)



