# Day 2 - 3517. Smallest Palindromic Rearrangement I

## 🎯 Problem
Rearrange the given palindromic string to form the **lexicographically smallest palindrome**.

## 💡 Key Idea
Only the **left half** determines the lexicographical order. Build the left half using characters in sorted order, place the odd-frequency character (if any) in the middle, and mirror the left half.

## 🛠️ Approaches
| Approach | Time | Space |
|----------|------|-------|
| Generate All Permutations | Exponential | O(n) |
| Frequency Count + Greedy ✅ | O(n + k log k) | O(n) |

> `k` = number of distinct characters.

## ✅ Optimal Solution
- Count the frequency of each character.
- Add `freq // 2` copies of each character (sorted) to the left half.
- Place the odd-frequency character in the middle.
- Reverse the left half to form the right half.

## ⚠️ Remember
- The left half decides the lexicographical order.
- Always process characters in sorted order.

## 📖 Learned
- Use **Counter** for frequency counting.
- Construct palindromes using the **half + middle + mirror** pattern.

---

## 📝 Quick Revision

- Count the frequency of each character.
- Build the left half in **sorted order** using `freq // 2`.
- Put the odd-frequency character in the middle.
- Mirror the left half to create the right half.
- **Pattern:** Frequency Count + Greedy + String Construction
- **Time:** `O(n + k log k)` | **Space:** `O(n)`