import nbformat
import openai
import os
from dotenv import load_dotenv
from crewai_tools import Tool

# Carregar as variáveis do .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Tool para ler o notebook
class ReadNotebookTool(Tool):
    name: str = "read_notebook"
    description: str = "Lê um notebook Jupyter e extrai o conteúdo de código e markdown."

    def __init__(self):
        # Passando a função __call__ para o campo func
        super().__init__(func=self.__call__)

    def __call__(self, file_path: str) -> str:
        with open(file_path, "r", encoding="utf-8") as f:
            notebook = nbformat.read(f, as_version=4)

        content = ""
        for cell in notebook.cells:
            if cell.cell_type == "markdown":
                content += f"## {cell.source}\n\n"
            elif cell.cell_type == "code":
                content += f"```python\n{cell.source}\n```\n\n"
        return content

# Tool para gerar o README usando o conteúdo do notebook
class GenerateReadmeTool(Tool):
    name: str = "generate_readme"
    description: str = "Gera um README.md com base no conteúdo extraído de um notebook."

    def __init__(self):
        # Passando a função __call__ para o campo func
        super().__init__(func=self.__call__)

    def __call__(self, notebook_content: str) -> str:
        prompt = f"Use o conteúdo abaixo extraído de um notebook Jupyter para gerar um README.md descritivo e informativo:\n\n{notebook_content}"
        
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=500,
            n=1,
            stop=None,
            temperature=0.5,
        )
        
        return response.choices[0].text.strip()
