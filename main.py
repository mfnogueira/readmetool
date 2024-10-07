from crew import crew

def main():
    # Iniciar a execução do processo com o caminho para o notebook
    result = crew.kickoff(inputs={"file_path": "notebook.ipynb"})
    print(result)

if __name__ == "__main__":
    main()
