def delete_html_tags(html_file, result_file='cleaned.txt'):
    with open(html_file, "r", encoding="utf-8") as file:
        html = file.read()
        clean_text = []
        flag = False
        for char in html:
            if char == "<":
                flag = True
            elif char == ">":
                flag = False
            elif not flag:
                clean_text.append(char)
    clean_text = "".join(clean_text)
    with open(result_file, "w", encoding="utf-8") as file:
        file.write(clean_text)
delete_html_tags("draft (1).html", "cleaned.txt")