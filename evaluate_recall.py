def recall(caught, missed):
    return caught / (caught + missed)


early_recall = recall(349, 124)
late_recall = recall(107, 76)
drop_in_points = (early_recall - late_recall) * 100

print(f"2017–2020 recall: {early_recall:.1%}")
print(f"2021–2022 recall: {late_recall:.1%}")
print(f"Recall dropped by {drop_in_points:.1f
