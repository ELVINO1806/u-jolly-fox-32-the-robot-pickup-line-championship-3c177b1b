from pathlib import Path

ENTRY = "I ran a million simulations. In every one, I still walk over and say hello first."

output_path = Path("/output/entry.txt")
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(ENTRY, encoding="utf-8")
