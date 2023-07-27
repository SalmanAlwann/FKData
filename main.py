from config.utils import *
from config.body import *
clear_screen()
print_banner()

def main():
    flag=False
    while True:
        total_options = len(options)
        selected = 0
        clear_screen()
        print_banner()
        print_menu(selected,options)

        try:
            while True: 
                key = getch()
                if key == "\x1b":  # Arrow keys are represented with escape sequence
                    getch()  # Consume the next character (usually "[")
                    key = getch()
                    if key == "A":  # Up arrow
                        selected = (selected - 1) % total_options
                        clear_screen()
                        print_banner()
                        print_menu(selected,options)
                    elif key == "B":  # Down arrow
                        selected = (selected + 1) % total_options
                        clear_screen()
                        print_banner()
                        print_menu(selected,options)
                elif key == "\r":  # Enter key
                    clear_screen()
                    print_banner()
                    selected_option = options[selected]
                    print(f"\nSelected option: {selected_option}\n")
                    # Call the respective function based on the selected option
                    op = FakeIt(selected_option)
                    #function_mapping[selected_option]()  # Call the associated function
                    break
                elif key == "\x03":  # Ctrl+C
                    # Handle Ctrl+C here
                    clear_screen()
                    print_banner()
                    print(f"\n\t\tCtrl+C detected. Exiting...")
                    flag=True
                    break
            if flag==True:
                break
                

        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
        
if __name__ == "__main__":
        main()