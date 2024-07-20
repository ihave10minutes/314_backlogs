# GUI for Memory Sequence.
# Last edited 9th July, 4pm
# Latest Changes: Added center, rearranged GUI buttons

import tkinter as tk
import B3S2_FunctionStorage as fs

main = tk.Tk()
main.title("Team C GUI")

tabLabelMA3=tk.Label(main,text="GRANDMA3", font="20" )
ma3_91_btn = tk.Button(main, text="Suspense (91)", bg="GREEN",command=fs.MA3_Seq91,width=20,height=4)
ma3_92_btn = tk.Button(main, text="Station Start (92)", bg="GREEN", command=fs.MA3_Seq92,width=20,height=4)
ma3_93_btn = tk.Button(main, text="Hard (93)", bg="GREEN", command=fs.MA3_Seq93,width=20,height=4)
ma3_94_btn = tk.Button(main, text="Easy (94)", bg="GREEN", command=fs.MA3_Seq94,width=20,height=4)
ma3_95_btn = tk.Button(main, text="Laser Preparation (95)", bg="GREEN", fg="YELLOW",command=fs.MA3_Seq95,width=20,height=4)
ma3_96_btn = tk.Button(main, text="Lose (96)", bg="GREEN", command=fs.MA3_Seq96,width=20,height=4)
ma3_97_btn = tk.Button(main, text="Win (97)", bg="GREEN", command=fs.MA3_Seq97,width=20,height=4)
ma3_clear_btn = tk.Button(main, text="Clear", bg="GREEN", command=fs.MA3_Clear,width=20,height=4)

tabLabelREA=tk.Label(main,text="REAPER", font="20" )
rea_easy_btn = tk.Button(main, text="Easy", bg="RED",command=fs.REA_JumpEasy,width=20,height=4)
rea_hard_btn = tk.Button(main, text="Hard", bg="RED",command=fs.REA_JumpHard,width=20,height=4)
rea_win_btn = tk.Button(main, text="Win", bg="RED",command=fs.REA_JumpWin,width=20,height=4)
rea_lose_btn = tk.Button(main, text="Lose", bg="RED",command=fs.REA_JumpLose,width=20,height=4)
rea_sample_btn = tk.Button(main, text="Sample", bg="RED",command=fs.REA_JumpSampleBeat,width=20,height=4)
rea_playpause_btn = tk.Button(main, text="Play/Pause", bg="RED",command=fs.REA_PlayPause,width=20,height=4)
rea_suspense_btn = tk.Button(main, text="Suspense (Lights)", bg="RED",command=fs.REA_JumpSuspense,width=20,height=4)
rea_bgm_btn = tk.Button(main, text="BGM", bg="RED",command=fs.REA_JumpBGM,width=20,height=4)

tabLabelSeq=tk.Label(main,text="SEQUENCE", font="20" )
seq_intro_btn=tk.Button(main, text="BGM Sequence (Intro)", bg="BLUE",fg="YELLOW",command=fs.SEQ_Intro,width=20,height=4)
seq_orange_btn=tk.Button(main, text="Suspense", bg="BLUE",command=fs.SEQ_OrangeBtn,width=20,height=4)
seq_easy_btn=tk.Button(main, text="Easy Level", bg="BLUE",command=fs.SEQ_Easy,width=20,height=4)
seq_hard_btn=tk.Button(main, text="Hard Level", bg="BLUE",command=fs.SEQ_Hard,width=20,height=4)
seq_win_btn=tk.Button(main, text="Win Sequence", bg="BLUE",command=fs.SEQ_Win,width=20,height=4)
seq_lose_btn=tk.Button(main, text="Lose Sequence", bg="BLUE",command=fs.SEQ_Lose,width=20,height=4)
seq_sample_btn=tk.Button(main, text="Sample Beat", bg="BLUE",fg="YELLOW",command=fs.SEQ_SampleBeat,width=20,height=4)
seq_blackout_btn=tk.Button(main, text="Blackout", bg="BLACK", fg="WHITE",command=fs.SEQ_Blackout,width=20,height=4)

tabLabelMA3.grid(row=0, column=0)
ma3_91_btn.grid(row=1, column=0)
ma3_92_btn.grid(row=2, column=0)
ma3_93_btn.grid(row=3, column=0)
ma3_94_btn.grid(row=4, column=0)
ma3_96_btn.grid(row=5, column=0)
ma3_97_btn.grid(row=6, column=0)
ma3_95_btn.grid(row=7, column=0)
ma3_clear_btn.grid(row=8, column=0)

tabLabelREA.grid(row=0, column=1)
rea_easy_btn.grid(row=1, column=1)
rea_hard_btn.grid(row=2, column=1)
rea_win_btn.grid(row=3, column=1)
rea_lose_btn.grid(row=4, column=1)
rea_sample_btn.grid(row=5,column=1)
rea_suspense_btn.grid(row=6, column=1)
rea_bgm_btn.grid(row=7, column=1)
rea_playpause_btn.grid(row=8, column=1)

tabLabelSeq.grid(row=0, column=2)
seq_intro_btn.grid(row=1,column=2)
seq_orange_btn.grid(row=2, column=2)
seq_easy_btn.grid(row=3, column=2)
seq_hard_btn.grid(row=4, column=2)
seq_win_btn.grid(row=5, column=2)
seq_lose_btn.grid(row=6, column=2)
seq_sample_btn.grid(row=7, column=2)
seq_blackout_btn.grid(row=8, column=2)

main.mainloop()