# coding-practice

個人刷題紀錄，涵蓋 **LeetCode**、**NeetCode**、**Codewars** 三個平台，主要語言為 **Python** 與 **C++**。

## 目錄結構

```
coding-practice/
├── leetcode/                # 依題號整理
│   ├── python/              
│   └── cpp/                 
├── neetcode/                # 依 NeetCode 150 roadmap 主題整理
│   ├── arrays-and-hashing/
│   │   ├── python/          # 0001-two-sum.py
│   │   └── cpp/             # 0001-two-sum.cpp
│   ├── two-pointers/
│   └── ...（18 個主題）
├── templates/               # 解題範本
│   ├── solution.py
│   └── solution.cpp
├── progress.md              # 進度追蹤表
└── README.md
```

## 三個平台的分類邏輯

| 平台 | 分類方式 | 檔名慣例 |
|------|----------|----------|
| LeetCode | 語言 → 題號 | `0001-two-sum.py`（四位數補零方便排序） |
| NeetCode | 主題 → 語言 | `0217-contains-duplicate.py` |

> NeetCode 依 roadmap 主題分，是因為它本身就是按主題循序漸進；LeetCode 題目分散，用語言分層再靠檔名帶題號 / 等級最好維護。

## 使用方式

1. 從 `templates/` 複製對應語言的範本到目標資料夾。
2. 檔名帶上題號或等級與題目 slug（例：`0001-two-sum.py`）。
3. 在檔案頂部的註解區塊填入題目連結、思路與時間 / 空間複雜度。
4. 解完後到 `progress.md` 打勾記錄。

## 命名規則備忘

- LeetCode / NeetCode 題號一律補到 **四位數**（`0001`、`0217`、`1143`），檔案才會照數字順序排列。
- 題目 slug 用小寫、以 `-` 連接（`two-sum`、`longest-substring`）。
- 一題有多解法時，用後綴區分：`0001-two-sum.py`、`0001-two-sum-optimized.py`。
