import qi

def main():
    # Create an instance of the Qi session
    session = qi.Session()

    try:
        print("Connecting to the robot...")
        # Connect to the robot at the specific address and port
        session.connect("tcp://127.0.0.1:9559")
        print("Connected!")

        # Check if the connection was successful
        if session.isConnected():
            print("Successful connection with the robot.")
        else:
            print("Failed to establish a connection with the robot.")

        # Fetch the list of services available on the connected robot
        services = session.services()
        num_services = len(services)
        print("Number of services available: {}".format(num_services))

        # Print the list of available services
        print("List of available services:")
        for service in services:
            print(service)

    except Exception as e:
        print("An error occurred while trying to connect to the robot:", e)

    finally:
        # Close the Qi session
        if session is not None:
            session.close()

if __name__ == "__main__":
    main()