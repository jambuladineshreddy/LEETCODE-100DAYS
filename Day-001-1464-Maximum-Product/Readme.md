## 📝 Quick Revision

- The maximum product comes from the **two largest elements**.
- Track `max1` (largest) and `max2` (second largest) in one traversal.
- If a new largest is found, move the old `max1` to `max2`.
- Use `>=` to correctly handle duplicate maximum values.
- Return `(max1 - 1) * (max2 - 1)`.
- **Pattern:** Track Largest & Second Largest | **Time:** `O(n)` | **Space:** `O(1)`