import os
import sys
import uuid
import importlib
import pathlib
import requests

EXAMPLES_DIR = "examples"
EXPECTED = {
    "auth",
    "get_balance",
    "get_bins",
    "list_cards",
    "get_card",
    "generate_card",
    "generate_card_address",
    "update_card_address",
    "update_card_limit",
    "update_card_status",
    "update_card_closing",
    "list_transactions",
    "list_card_transactions",
    "list_internal_txns",
}

def load_env(filepath=".env"):
    if not os.path.exists(filepath):
        return
    with open(filepath) as f:
        for line in f:
            if line.strip() and not line.startswith("#"):
                key, sep, value = line.strip().partition("=")
                if sep and key not in os.environ:
                    os.environ[key] = value

def prompt_api_key():
    print("🔐 Please enter your API key (or create one at https://dashboard.api-card.com/user/api-tokens):")
    return input("API Key: ").strip()

def load_and_run(script_name, api_key):
    try:
        module = importlib.import_module(f"{EXAMPLES_DIR}.{script_name}")
        func_name = next(f for f in dir(module) if not f.startswith("_"))
        func = getattr(module, func_name)

        if "card" in script_name and "generate" not in script_name and "list" not in script_name:
            result = func(api_key, card_id=0)
        elif "generate" in script_name:
            result = func(api_key, {
                "ProgramID": 139,
                "Limit": 1,
                "AddressGenerate": script_name == "generate_card_address",
                "IsTest": True
            })
        else:
            result = func(api_key)

        return True, result
    except Exception as e:
        return False, str(e)

def main():
    print("🧪 API-Card Python Test Runner")
    print("──────────────────────────────")

    load_env()

    # Step 1: Check scripts
    existing_scripts = {f.stem for f in pathlib.Path(EXAMPLES_DIR).glob("*.py")}
    missing_scripts = EXPECTED - existing_scripts

    print(f"📁 Found {len(existing_scripts)} example scripts.")
    if missing_scripts:
        print(f"⚠️ Missing: {', '.join(sorted(missing_scripts))}")
    print("")

    # Step 2: API key
    api_key = os.getenv("API_CARD_API_KEY") or prompt_api_key()

    # Step 3: Test auth
    print("🔍 Testing API key with `auth`...")
    if "auth" not in existing_scripts:
        print("❌ 'auth.py' is missing. Cannot test key.")
        sys.exit(1)

    ok, result = load_and_run("auth", api_key)
    if not ok or not result.get("Good"):
        print("❌ Authentication failed. Check your API key.")
        sys.exit(1)
    print("✅ API key is valid.\n")

    # Step 4: Run scripts
    passed = 0
    failed = 0

    for name in sorted(existing_scripts):
        if name == "auth":
            continue
        print(f"▶️ Running `{name}.py`... ", end="")
        ok, output = load_and_run(name, api_key)
        if ok:
            print("✅ Passed")
            passed += 1
        else:
            print("❌ Failed")
            failed += 1
            print(f"   Error: {output}")

    print("\n🧾 Test Summary")
    print("───────────────")
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {failed}")
    print(f"📂 Total Scripts Run: {passed + failed}")
    if missing_scripts:
        print(f"📄 Missing Scripts: {len(missing_scripts)}")
        for m in sorted(missing_scripts):
            print(f"   - {m}.py")

    print("\n✨ Done.")

if __name__ == "__main__":
    main()
