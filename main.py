from voice_commands import listen_for_command
from mouse_actions import skip_video, replay_video
from logger import log_info, log_error

if __name__ == "__main__":
    while True:
        command = listen_for_command()
        if command:
            if command == "skip":
                log_info("Executing 'skip' command.")
                skip_video()
            elif command == "replay":
                log_info("Executing 'replay' command.")
                replay_video()
            elif command == "stop":
                log_info("Stopping program.")
                break
            else:
                log_error(f"Unrecognized command: {command}")
