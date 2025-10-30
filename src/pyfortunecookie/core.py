import random

_FORTUNES = [
    "Today is a good day to start small.",
    "A pleasant surprise is waiting for you.",
    "Your code will compile on the first try.",
    "Help others and luck will help you.",
    "Take a short walk; ideas will follow.",
    "A cup of coffee will solve half your problems. ☕",
    "You will soon discover a hidden strength. 💪",
    "Your curiosity is your superpower. 🔍"
]

_PALETTES = {
    "soft": ["peach", "mint", "lavender", "sky", "lemon"],
    "bold": ["crimson", "indigo", "emerald", "amber", "teal"],
    "mono": ["black", "white", "gray"]
}

def get_fortune(rng: random.Random | None = None) -> str:
    """Return a random fortune sentence."""
    rng = rng or random
    return rng.choice(_FORTUNES)

def get_lucky_number(seed: int | None = None, min_value: int = 1, max_value: int = 99) -> int:
    """Return a lucky number (optionally deterministic if seed provided)."""
    if min_value > max_value:
        raise ValueError("min_value must be <= max_value")
    rng = random.Random(seed) if seed is not None else random
    return rng.randint(min_value, max_value)

def get_color(palette: str = "soft", rng: random.Random | None = None) -> str:
    """Return a lucky color from the selected palette."""
    if palette not in _PALETTES:
        raise ValueError(f"Unknown palette '{palette}'. Valid: {', '.join(_PALETTES)}")
    rng = rng or random
    return rng.choice(_PALETTES[palette])
