# # Эмуляция awk: извлечение столбца 7 из файла с разделителями
# # в виде пробельных символов
#
# for val in [line.split()[6] for line in open('input.txt')]:
#     print(val)

# # То же самое, но более явный код, который предохраняет результат
# col7 = []
# for line in open('input.txt'):
#     cols = line.split()
#     col7.append(cols[7])
# for item in col7: print(item)


# To же самое, но многократно используемая функция
def awker(file, col):
    return [line.rstrip().split()[col - 1] for line in open(file)]


print(awker('input.txt', 7))  # Список строк
print(', '.join(awker('input.txt', 7)))  # Поместить запятые между строками
