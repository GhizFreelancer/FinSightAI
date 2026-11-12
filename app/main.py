from app.core.config import APP_NAME, APP_VERSION,DEBUG

def main():
    print(f"Welcome to {APP_NAME}")
    print(f"Version: {APP_VERSION}")
    print(f"Debug mode: {DEBUG}")


if __name__ == "__main__":
    main()