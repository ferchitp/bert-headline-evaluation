def recall(caught, missed):
    return caught / (caught + missed)


print(f"2017–2020 recall: {recall(349, 124):.1%}")
print(f"2021–2022 recall: {recall(107, 76):.1%}")
