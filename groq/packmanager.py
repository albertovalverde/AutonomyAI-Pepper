import qi

def main():
    # Create an instance of the Qi session
    session = qi.Session()

    try:
        # Connect to the robot at the specific address and port
        session.connect("tcp://127.0.0.1:9559")
        print("Connected to the robot.")

        # Get the PackageManager service
        package_manager = session.service("PackageManager")

        if package_manager:
            # Retrieve the list of installed packages
            installed_packages = package_manager.packages()
            
            if installed_packages:
                print("List of installed packages:")
                for package in installed_packages:
                    print(package)
            
            else:
                print("No packages installed.")
            
        else:
            print("PackageManager service not available.")

    except Exception as e:
        print("An error occurred while interacting with the PackageManager service:", e)

    finally:
        # Close the Qi session
        if session is not None:
            session.close()

if __name__ == "__main__":
    main()