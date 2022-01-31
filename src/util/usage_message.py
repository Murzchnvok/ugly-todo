USAGE_MESSAGE = f"""see the examples below

Show task(s) and note(s):
~$ %(prog)s

 My Board [1/6]

   To-Do
       1.  Attack on Titan Vol. 33 @read
       5.  Clean room @home
       6.  Make a GUI to Ugly-ToDo @dev

   In Progress
       3.  Learn Russian @study @language
       4.  Develop a Book Track app @dev @idea

   Done
       2.  Updated Ugly-ToDo code @code @update

 Notes
     5.  remember to buy the milk


Create a new task ('@' at the beginning of a word means a tag):
~$ %(prog)s -a Create a new Workout plan @health -p 1

 My Board [1/7]

   To-Do
       1.  Attack on Titan Vol. 33 @read
       5.  Clean room @home
       6.  Make a GUI to Ugly-ToDo @dev
       7.  create a new workout plan @health

 ...


Start/stop a task:
~$ %(prog)s -b 7

 My Board [1/7]

   To-Do
       1.  Attack on Titan Vol. 33 @read
       5.  Clean room @home
       6.  Make a GUI to Ugly-ToDo @dev

   In Progress
       3.  Learn Russian @study @language
       4.  Develop a Book Track app @dev @idea
       7.  Create a new Workout plan @health

 ...


Check/uncheck task as complete:
~$ %(prog)s -c 7

 My Board [2/7]

   To-Do
       1.  Attack on Titan Vol. 33 @read
       5.  Clean room @home
       6.  Make a GUI to Ugly-ToDo @dev

   In Progress
       3.  Learn Russian @study @language
       4.  Develop a Book Track app @dev @idea

   Done
       7.  Create a new Workout plan @health
       2.  Updated Ugly-ToDo code @code @update

 ...


Delete task(s) and/or note(s):
~$ %(prog)s -d 5 7 2

 My Board [0/4]

   To-Do
       1.  Attack on Titan Vol. 33 @read
       6.  Make a GUI to Ugly-ToDo @dev

   In Progress
       3.  Learn Russian @study @language
       4.  Develop a Book Track app @dev @idea

 ...


Delete all completed tasks:
~$ %(prog)s --clear


Sort the IDs:
~$ %(prog)s --sort

 My Board [0/4]

   To-Do
       1.  Attack on Titan Vol. 33 @read
       4.  Make a GUI to Ugly-ToDo @dev

   In Progress
       2.  Learn Russian @study @language
       3.  Develop a Book Track app @dev @idea

 ...


You can also use a few options from the rich module:
~$ %(prog)s -n 'Remember to buy the [s blue]milk'

"""
