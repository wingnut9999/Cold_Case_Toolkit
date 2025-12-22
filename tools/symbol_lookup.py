symbol_dict = {
    "☉": "Sun – consciousness, identity, truth",
    "☽": "Moon – intuition, mystery, the unconscious",
    "✝": "Cross – sacrifice, burden, intersection",
    "Δ": "Delta – change, transformation, triangle/pyramid"
}

def symbol_lookup(symbol):
    return symbol_dict.get(symbol, "Unknown symbol")
