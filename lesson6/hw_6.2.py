from prompt_toolkit.styles import default_pygments_style

seconds = int(input("Введите количество секунд: "))
dey_word = ""
days = seconds // 86400
seconds = seconds % 86400
hours = seconds // 3600
seconds = seconds % 3600
minutes = seconds // 60
seconds = seconds % 60
if days == 1:
    word = "день"
elif days % 10 in (2, 3, 4):
    word = "дня"
else:
    word = "дней"
print(f"{days}{word}, {str(hours).zfill(2)}: {str(minutes).zfill(2)}: {str(seconds).zfill(2)}")

