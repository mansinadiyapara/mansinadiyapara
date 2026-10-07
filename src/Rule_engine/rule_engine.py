class RuleEngine:

    def __init__(self, rules):
        self.rules = rules

    def evaluate(self, input_data):

        results = []

        for rule in self.rules:

            result = rule.evaluate(input_data)

            results.append({
                "rule": rule.__class__.__name__,
                "result": result
            })

        return results