import cohere
from dotenv import load_dotenv
import os
from safe_executor import run_command

load_dotenv()
api_key = os.getenv("COHERE_API_KEY")
co = cohere.Client(api_key)

def get_shell_command(prompt):
    response = co.generate(
        model='command-r-plus',
        prompt=f"Translate this to a Linux shell command: {prompt}",
        max_tokens=100,
        temperature=0.3
    )
    return response.generations[0].text.strip()

if __name__ == "__main__":
    user_input = input("Enter task (e.g., 'find all jpgs'): ")
    shell_command = get_shell_command(user_input)

    print(f"\n[>] Suggested command:\n{shell_command}")
    confirm = input("\nRun this command? (y/n): ").lower()
    if confirm == 'y':
        run_command(shell_command)
    else:
        print("[x] Cancelled.")
