from pathlib import Path
file = "sample.txt"
while True:
    print("\n1.Create 2.Write 3.Read 4.Append 5.Display 6.Exit")
    ch = input("Enter choice: ")

    try:
        if ch == "1":
            Path(file).touch()
            print("File Created")

        elif ch == "2":
            with open(file, "w") as f:
                f.write(input("Enter data: "))
            print("Data Written")

        elif ch == "3":
            with open(file, "r") as f:
                print(f.read())

        elif ch == "4":
            with open(file, "a") as f:
                f.write("\n" + input("Enter data: "))
            print("Data Appended")

        elif ch == "5":
            with open(file, "r") as f:
                print("\nFile Contents:")
                print(f.read())

        elif ch == "6":
            break

        else:
            print("Invalid Choice")

    except FileNotFoundError:
        print("File Not Found")

    except Exception as e:
        print("Error:", e)