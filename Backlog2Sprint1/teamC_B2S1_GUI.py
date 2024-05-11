import tkinter as tk

main = tk.Tk()
main.title("Team C L-ISA Controller")

tabLabel=tk.Label(main,text="TEAM C GUI", font="20" )
snapshotone_btn = tk.Button(main, text="Snapshot ONE", bg="GREEN")
snapshottwo_btn = tk.Button(main, text="Snapshot TWO", bg="RED")
snapshotthree_btn = tk.Button(main, text="Snapshot THREE", bg="BLUE")
snapshotfour_btn = tk.Button(main, text="Snapshot FOUR", bg="YELLOW")


tabLabel.grid(row=0,column=0,columnspan=2)
snapshotone_btn.grid(row=1,column=0)
snapshottwo_btn.grid(row=1,column=1)
snapshotthree_btn.grid(row=2,column=0)
snapshotfour_btn.grid(row=2,column=1)

main.mainloop()