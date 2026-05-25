from tools.basetool import BaseTool

class CalculatorTool(BaseTool):
    name = "calculator"
    description = "Evaluates a mathematical expression and returns the result."
    parameters = {
        "expression": "The math expression to evaluate. Example: 150*4"
    }

    def run(self, parameters: dict) -> str:
        try:
            expression = parameters.get("expression", "")
            # Clean any trailing = signs the LLM might add
            expression = expression.strip().rstrip("=").strip()
            result = eval(expression)
            return str(result)
        except Exception as e:
            return f"Calculator error: {e}"