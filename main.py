import os
from dotenv import load_dotenv
from openai import OpenAI

def main():
    # Load environment variables
    load_dotenv()
    
    # Point the OpenAI client to Google's base URL
    client = OpenAI(
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        api_key=os.environ.get("GEMINI_API_KEY")
    )
    
    print("Sending request to Gemini via OpenAI client...")
    try:
        response = client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=[
                {"role": "user", "content": "Say 'OpenAI compatibility is working!'"}
            ]
        )
        print("\nResponse:")
        print(response.choices[0].message.content)
    except Exception as e:
        print(f"\nError using OpenAI compatibility: {e}")


if __name__ == "__main__":
    main()


