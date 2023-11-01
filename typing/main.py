"""
Main module for the keyboard practice application
Main module is responsible for interacting with the user
Uses other modules for calculations & analyzes

https://docs.google.com/document/d/1iEtVTARQ4FwydgTLak7TYru-S9VWEp9k3Kbgw_NEEsU/edit

"""
import calculations as cl
import getters_setters as gtst

def main():
    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """

    stop = False
    while not stop:
        print("")
        print("1) First level of the test")
        print("2) Second level of the test")
        print("3) Third level of the test")
        print("4) Highscores")
        print("q) Quit.")

        choice = input("--> ")

        if choice == "q":
            print("Bye now")
            stop = True
        
        elif choice == "1":
            print(gtst.lvl_selector("easy.txt"))

        elif choice == "2":
            print(gtst.lvl_selector("medium.txt"))

        elif choice == "3":
            print(gtst.lvl_selector("hard.txt"))
        
        elif choice == "4":
            print(gtst.see_scores("score.txt"))
               
        if not stop:
            input("\nPress enter to continue...")
        

if __name__ == "__main__":
    main()
