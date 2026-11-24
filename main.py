import os
from pathlib import Path
from datetime import datetime
from urllib.parse import quote
from urllib.request import urlopen

def load_api_key():
    env_path = Path(__file__).resolve().parent / ".env"

    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()

            if "=" in line and not line.startswith("#"):
                name, value = line.split("=", 1)
                name = name.strip()
                value = value.strip().strip("\"'")

                if name in {"OPENAI_API_KEY", "GROQ_API_KEY"}:
                    os.environ[name] = value

load_api_key()

def generate_image(prompt):
    print("\nGenerating image... Please wait.")

    try:
        encoded_prompt = quote(prompt)
        url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&nologo=true"

        with urlopen(url, timeout=120) as response:
            image_bytes = response.read()

        # Create output directory
        output_dir = Path("generated_images")
        output_dir.mkdir(exist_ok=True)

        # Save image with a unique filename
        filename = datetime.now().strftime(
            "image_%Y%m%d_%H%M%S.png"
        )
        image_path = output_dir / filename
        image_path.write_bytes(image_bytes)

        print("\nImage generated successfully!")
        print(f"Saved at: {image_path.resolve()}")

    except Exception as error:
        print(f"\nError generating image: {error}")

if __name__ == "__main__":
    print("=== AI Image Generator ===")
    prompt = input("Enter your image prompt: ").strip()

    if prompt:
        generate_image(prompt)
    else:
        print("Please enter a prompt.")