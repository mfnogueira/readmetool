# import os
# from crewai import Agent, Task, Crew, Process
# from tools.custom_tools import read_notebook_tool, generate_readme_tool

# # Criar o agente de leitura do notebook
# reader = Agent(
#     role="Notebook Reader",
#     goal="Extrair o conteúdo do notebook",
#     tools=[read_notebook_tool],  # Usando a tool personalizada
#     verbose=True,
#     memory=False,
#     backstory=(
#         "Você é um especialista em ler e interpretar notebooks Jupyter. "
#         "Sua tarefa é extrair tanto o código quanto o markdown de forma legível."
#     )
# )

# # Criar o agente gerador de README
# generator = Agent(
#     role="README Generator",
#     goal="Criar um README.md",
#     tools=[generate_readme_tool],  # Usando a tool personalizada
#     verbose=True,
#     memory=False,
#     backstory=(
#         "Você transforma o conteúdo técnico extraído em uma documentação fácil de entender."
#     )
# )

# # Definir a task de leitura
# read_notebook_task = Task(
#     description="Ler e extrair o conteúdo do notebook.",
#     expected_output="Texto com o código e markdown extraído do notebook.",
#     tools=[read_notebook_tool],  # Usando a tool
#     agent=reader,
# )

# # Definir a task de geração do README
# generate_readme_task = Task(
#     description="Usar o conteúdo extraído para criar um README.md.",
#     expected_output="README.md gerado a partir do notebook.",
#     tools=[generate_readme_tool],  # Usando a tool
#     agent=generator,
# )

# # Criar o crew (equipe) que organiza os agentes e as tasks
# crew = Crew(
#     agents=[reader, generator],
#     tasks=[read_notebook_task, generate_readme_task],
#     process=Process.sequential  # Execução sequencial
# )


import os
from crewai import Agent, Task, Crew, Process
from tools.custom_tools import ReadNotebookTool, GenerateReadmeTool

# Instanciar as tools
read_notebook_tool = ReadNotebookTool()
generate_readme_tool = GenerateReadmeTool()

# Criar o agente de leitura do notebook
reader = Agent(
    role="Notebook Reader",
    goal="Extrair o conteúdo do notebook",
    tools=[read_notebook_tool],  # Passando a instância da tool
    verbose=True,
    memory=False,
    backstory=(
        "Você é um especialista em ler e interpretar notebooks Jupyter. "
        "Sua tarefa é extrair tanto o código quanto o markdown de forma legível."
    )
)

# Criar o agente gerador de README
generator = Agent(
    role="README Generator",
    goal="Criar um README.md",
    tools=[generate_readme_tool],  # Passando a instância da tool
    verbose=True,
    memory=False,
    backstory=(
        "Você transforma o conteúdo técnico extraído em uma documentação fácil de entender."
    )
)

# Definir a task de leitura
read_notebook_task = Task(
    description="Ler e extrair o conteúdo do notebook.",
    expected_output="Texto com o código e markdown extraído do notebook.",
    tools=[read_notebook_tool],  # Usando a tool
    agent=reader,
)

# Definir a task de geração do README
generate_readme_task = Task(
    description="Usar o conteúdo extraído para criar um README.md.",
    expected_output="README.md gerado a partir do notebook.",
    tools=[generate_readme_tool],  # Usando a tool
    agent=generator,
)

# Criar o crew (equipe) que organiza os agentes e as tasks
crew = Crew(
    agents=[reader, generator],
    tasks=[read_notebook_task, generate_readme_task],
    process=Process.sequential  # Execução sequencial
)
