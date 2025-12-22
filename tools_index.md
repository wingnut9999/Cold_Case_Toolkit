# 🧰 CipherTrace Toolkit Index

This file catalogs the core `.py` tools used by CipherTrace GPT for analysis, pattern recognition, and cryptographic work.

---

## 🔐 Cipher & Symbol Tools

### `frequency_analysis.py`
- Performs a frequency count of letters in a text string.
- Outputs a bar graph of letter usage.
- Useful for substitution cipher analysis.

### `caesar_decrypt.py`
- Applies a Caesar cipher decryption using a provided shift value.
- Preserves letter casing and skips non-alpha characters.

### `symbol_lookup.py`
- Looks up known esoteric or symbolic meanings (e.g., ☉ = Sun).
- Symbols stored in an internal dictionary.

---

## 📅 Timeline & Case Tools

### `timeline_stress_test.py`
- Accepts a list of time-stamped events.
- Identifies contradictions where later events are timestamped earlier than prior ones.

---

## 📈 Pattern Recognition Tools

### `pattern_cluster.py`
- Groups dates by repeating month-day patterns.
- Helps identify ritualistic or timed behavior across years.

---

## 🗂️ Usage
These tools can be referenced directly by CipherTrace GPT or invoked during recursive analysis tasks. They are designed to be used together with the data files in:
- `test_cases/`
- `references/`
- `patterns/`
