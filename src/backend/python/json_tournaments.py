import data_getter
import json


t = data_getter.return_tournaments_with_data()
print(t)
print()

for age_class, tournaments in t.items():
    with open(f"../tournament_data/{age_class}.json", "w", encoding="utf-8") as f:
        for tournament in tournaments:
            json.dump(tournament, f, ensure_ascii=False, indent=4)
