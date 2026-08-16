CLAIM_KEYWORDS = [
    # Treatment / Cure claims
    "cure",
    "cures",
    "cured",
    "curing",
    "treat",
    "treats",
    "treated",
    "treatment",
    "heal",
    "heals",
    "healed",
    "healing",
    "fix",
    "fixes",
    "repair",
    "restore",
    "recover",
    "recovery",

    # Disease elimination claims
    "reverse",
    "reverses",
    "reversed",
    "regenerate",
    "regenerates",
    "remove",
    "removes",
    "eliminate",
    "eliminates",
    "eradicate",
    "destroy",
    "kill",

    # Prevention claims
    "prevent",
    "prevents",
    "prevention",
    "protect",
    "protects",
    "avoid",
    "avoids",
    "reduce risk",
    "lower risk",

    # Medication replacement claims
    "replace",
    "replaces",
    "replacement",
    "alternative to",
    "instead of",
    "rather than",
    "without medication",
    "without drugs",
    "no need for",
    "stop taking",
    "quit medication",
    "stop medicine",
    "replace medicine",
    "replace drugs",

    # Guaranteed / exaggerated claims
    "guaranteed",
    "guarantee",
    "100%",
    "always",
    "never",
    "instant",
    "instantly",
    "immediately",
    "permanent",
    "permanently",
    "miracle",
    "miraculous",
    "magic",
    "secret",

    # Effect claims
    "boost",
    "boosts",
    "increase",
    "increases",
    "improve",
    "improves",
    "enhance",
    "enhances",
    "strengthen",
    "strengthens",
    "detox",
    "cleanse",
    "flush out",

    # Weight loss claims
    "lose weight",
    "burn fat",
    "fat burning",
    "melt fat",
    "rapid weight loss",
    "fast weight loss",

    # Cancer related claims
    "fight cancer",
    "prevent cancer",
    "cancer cure",
    "cancer treatment",
    "kill cancer cells",

    # Blood sugar / diabetes claims
    "lower blood sugar",
    "control diabetes",
    "reverse diabetes",
    "cure diabetes",
    "diabetes cure",

    # Heart / blood pressure claims
    "lower blood pressure",
    "reduce cholesterol",
    "clean arteries",
    "unclog arteries",

    # Immune system claims
    "boost immunity",
    "boost immune system",
    "strengthen immunity",

    # Disease claims
    "treat disease",
    "cure disease",
    "all diseases",
    "any disease",
    "chronic disease cure",
]
class ExtractClaim:
    @staticmethod
    def __split_sentences(sentences):
        return sentences.split(".")
    @staticmethod
    def extract_claim(text):
        text = text.lower()
        sentences=ExtractClaim.__split_sentences(text)
        for sentence in sentences:
                if not sentence.strip():
                    continue
                keywords = []
                for keyword in CLAIM_KEYWORDS:

                    if keyword in sentence:
                        keywords.append(keyword)
                if keywords:
                    return {
                        "claim": sentence.strip(),
                        "keyWords": keywords
                    }
        return None
        
