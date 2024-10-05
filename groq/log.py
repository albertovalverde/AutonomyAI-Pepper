import qi

def main():
    # Create an instance of the Qi session
    session = qi.Session()

    try:
        # Connect to the robot at the specific address and port
        session.connect("tcp://127.0.0.1:9559")
        print("Connected to the robot.")

        # Get the LogManager service
        log_manager = session.service("LogManager")

        if log_manager:
            # Create a dictionary representing the log message
            log_message = {
                "source": "python_test_script",
                "level": 6,  # Priority 6 (info)
                "message": "Hello, this is a test message from the LogManager service."
            }
            
            # Log the message using the dictionary
            log_manager.log([log_message])

            print("Message logged successfully.")

        else:
            print("LogManager service not available.")

    except Exception as e:
        print("An error occurred while interacting with the LogManager service:", e)

    finally:
        # Close the Qi session
        if session is not None:
            session.close()

if __name__ == "__main__":
    main()