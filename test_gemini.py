import os

from dotenv import load_dotenv



load_dotenv(
    ".env",
    override=True
)



key=os.getenv(
    "GEMINI_API_KEY"
)



if key:

    print(
        "KEY FOUND ✅"
    )

    print(
        key[:10]
    )


else:

    print(
        "KEY NOT FOUND ❌"
    )