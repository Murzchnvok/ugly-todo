import sys

try:
    from colored import attr, fg
except:
    print("You need to install 'colored'")
    print("Run: pip3 install colored --user")
    sys.exit(0)

USAGE_MESSAGE = f"""{attr(1)}see the examples below{attr(0)}

{attr(1)}Show task(s) and note(s):{attr(0)}
~$ {attr(1)}{fg(2)}%(prog)s{attr(0)}

 {attr(1)}My Board {fg(8)}[1/6]{attr(0)}

   {attr(1)}To-Do{attr(0)}
     {fg(2)}  {fg(8)}1. {fg(4)}  {fg(7)}Attack on Titan Vol. 7 {fg(8)}@read{attr(0)}
     {fg(4)}  {fg(8)}3. {fg(4)}  {fg(7)}Blade Runner @read{attr(0)}
     {fg(4)}  {fg(8)}6. {fg(4)}  {fg(7)}develop a fetch app {fg(8)}@dev{attr(0)}

   {attr(1)}In Progress{attr(0)}
     {fg(2)}  {fg(8)}2. {fg(4)}  {fg(7)}update polybar-collection {fg(8)}@dev{attr(0)}
     {fg(1)}  {fg(8)}7. {fg(4)}  {fg(7)}update ugly-weather app {fg(8)}@dev{attr(0)}

   {attr(1)}Done{attr(0)}
     {fg(1)}  {fg(8)}4. {fg(2)}  {fg(8)}update utd to kanban style @dev{attr(0)}

 Notes
   {fg(6)}  {fg(8)}5. {fg(7)}remember to buy the milk{attr(0)}


{attr(1)}Create a new task ('@' at the beginning of a word means a tag):{attr(0)}
~$ {attr(1)}{fg(2)}%(prog)s {fg(4)}-a {fg(6)}develop a ugly To-Do app @dev {fg(4)}-p {fg(6)}1{attr(0)}

 {attr(1)}My Board {fg(8)}[0/2]{attr(0)}

   {attr(1)}To-Do{attr(0)}
     {fg(2)}  {fg(8)}1. {fg(4)}  {fg(7)}clean room {fg(8)}@home{attr(0)}
     {fg(1)}  {fg(8)}2. {fg(4)}  {fg(7)}develop a ugly To-Do app {fg(8)}@dev{attr(0)}


{attr(1)}Start/stop a task:{attr(0)}
~$ {attr(1)}{fg(2)}%(prog)s {fg(4)}-b {fg(6)}2{attr(0)}

 {attr(1)}My Board {fg(8)}[0/2]{attr(0)}

   {attr(1)}To-Do{attr(0)}
     {fg(2)}  {fg(8)}1. {fg(4)}  {fg(7)}clean room {fg(8)}@home{attr(0)}

   {attr(1)}In Progress{attr(0)}
     {fg(1)}  {fg(8)}2. {fg(4)}  {fg(7)}develop a ugly To-Do app {fg(8)}@dev{attr(0)}


{attr(1)}Check/uncheck task as complete:{attr(0)}
~$ {attr(1)}{fg(2)}%(prog)s {fg(4)}-c {fg(6)}2{attr(0)}

 {attr(1)}My Board {fg(8)}[1/2]{attr(0)}

   {attr(1)}To-Do{attr(0)}
     {fg(2)}  {fg(8)}1. {fg(4)}  {fg(7)}clean room {fg(8)}@home{attr(0)}

   {attr(1)}Done{attr(0)}
     {fg(1)}  {fg(8)}2. {fg(2)}   {fg(8)}develop a ugly To-Do app @dev{attr(0)}


{attr(1)}Delete a task/note (can delete multiples by id):{attr(0)}
~$ {attr(1)}{fg(2)}%(prog)s {fg(4)}-d {fg(6)}2{attr(0)}

 {attr(1)}My Board {fg(8)}[0/1]{attr(0)}

   {attr(1)}To-Do{attr(0)}
     {fg(2)}  {fg(8)}1. {fg(4)}  {fg(7)}clean room {fg(8)}@home{attr(0)}


{attr(1)}Delete all completed tasks:{attr(0)}
~$ {attr(1)}{fg(2)}%(prog)s {fg(4)}--clear{attr(0)}

{attr(1)}Sort the ids (old ids: 3, 7, 9, new ids: 1, 2, 3):{attr(0)}
~$ {attr(1)}{fg(2)}%(prog)s {fg(4)}--sort{attr(0)}

"""