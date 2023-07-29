

1.	The script can be found in 

https://github.com/thanujyennaytelus/guiautomation	

2.	There will be 4 files the present vesion that are working are 

•	Gui_work.py
•	Gui_work_new.py
•	Replay_work.py
•	Replay_work_new.py


3.	The GUI_work will have two options to record the screen on what is happening and to save that activity in a json file that will be used by the replay program to mimic the excat things that are done
  




4.	When the screen record option is hit the gui actions will be recored in actions.json and will be updated for each entry


 



5.	These activities will be updated for every single entry so if there are any particular tasks that need to be used regularly.


 



6.	The Json file consists of the mouse location x,y , keyboard inputs are gathered using pynput module for each character


7.	The replay_work_new.py has the import option for an excel sheet, this will be used to mimic the actions if a ‘ctrl+v’ is detected in the actions.js file

 

8.	This any action can be done by modifying the replay program with the elements in the excel file 


9.	The demonstration of how to use these programs will be found in the below drive link.

10.	 The new updated gui_work_new.py program consists of additional functionality of starting the recording to capture the input by pressing ‘Ctrl+q’ and stopping the recording by pressing ‘Ctrl+m’





11.	This takes away the condition where the action.json file consists of the trace path of hovering and interacting with the gui application window.
12. Install the required modules using the requirements.txt file 

Issues and updates: 

1)	Addition of the button on the number of times the replay should work 
2)	There will be a freeze or jitter by the keyboard and mouse after replay is done as the pynput module has some inconsistencies.
3)	There should not be any activity done once the replay is hit
4)	Accuracy of the tracking can be increased
5)	Need to update the code with notify options so that the user will know the recording is started and stopped
6)	Windows, Gmail may see this program  as a virus so we need to give correct administrative access for it to run.




