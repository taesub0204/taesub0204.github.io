import os
import re

directory = "c:/Users/user/Desktop/taesub0204.github.io/_posts"

# Current time is 14:30. We must use times before 14:30 so they aren't "future" posts.
# [회귀, 분류] -> 13:00 ~ 13:09 (Newer, shows up first)
# [트리, 비지도학습] -> 12:00 ~ 12:09 (Older, shows up after)

date_mapping = {
    # [회귀, 분류]
    "1. 선형회귀분석": "2026-06-11 13:09:00 +0900",
    "2. 다중회귀분석": "2026-06-11 13:08:00 +0900",
    "5. 로지스틱회귀분석": "2026-06-11 13:05:00 +0900",
    "7. KNN": "2026-06-11 13:03:00 +0900",
    "8. K_Fold": "2026-06-11 13:02:00 +0900",
    "9. 그리드서치": "2026-06-11 13:01:00 +0900",
    
    # [트리, 비지도학습]
    "2. 앙상블": "2026-06-11 12:08:00 +0900",
    "3. 군집분석_KMeans": "2026-06-11 12:07:00 +0900",
    "4. 군집분석_DBSCAN": "2026-06-11 12:06:00 +0900"
}

for filename in os.listdir(directory):
    if not filename.endswith(".md"):
        continue
    
    filepath = os.path.join(directory, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_date_str = None
    for key, date_val in date_mapping.items():
        if key in filename:
            new_date_str = date_val
            break
            
    if new_date_str:
        new_content = re.sub(r'^date:\s*.*$', f"date:   {new_date_str}", content, flags=re.MULTILINE)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {filename} to {new_date_str}")
