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

 {attr(4)}My Board{attr(0)} {fg(59)}[0/3]{attr(0)}
   {fg(1)}{attr(0)}  {fg(59)}1. {fg(4)}{fg(7)}  develop a ugly To-Do app {fg(59)}@dev{attr(0)}
   {fg(2)}{attr(0)}  {fg(59)}2. {fg(4)}{fg(7)}  Blader Runner {fg(59)}@read{attr(0)}
   {fg(2)}{attr(0)}  {fg(59)}3. {fg(4)}{fg(7)}  python {fg(59)}@study{attr(0)}

 {attr(4)}Notes{attr(0)}
   {fg(6)}{attr(0)}  {fg(59)}3. {fg(7)}just a reminder{attr(0)}


{attr(1)}Create a new task ('@' at the beginning of a word means a tag):{attr(0)}
~$ {attr(1)}{fg(2)}%(prog)s {fg(4)}-a {fg(6)}develop a ugly To-Do app @dev {fg(4)}-p {fg(6)}1{attr(0)}

 {attr(4)}My Board{attr(0)} {fg(59)}[0/1]{attr(0)}
   {fg(1)}{attr(0)}  {fg(59)}1. {fg(4)}{fg(7)}  develop a ugly To-Do app {fg(59)}@dev{attr(0)}


{attr(1)}Create a new note:{attr(0)}
~$ {attr(1)}{fg(2)}%(prog)s {fg(4)}-n {fg(6)}just a simple note{attr(0)}

 {attr(4)}Notes{attr(0)}
   {fg(6)}{attr(0)}  {fg(59)}1. {fg(7)}just a simple note{attr(0)} 


{attr(1)}Check/uncheck task as complete (can check or uncheck multiples by id):{attr(0)}
~$ {attr(1)}{fg(2)}%(prog)s {fg(4)}-c {fg(6)}2 3{attr(0)}

 {attr(4)}My Board{attr(0)} {fg(59)}[2/3]{attr(0)}
   {fg(1)}{attr(0)}  {fg(59)}1. {fg(4)}{fg(7)}  develop a ugly To-Do app {fg(59)}@dev{attr(0)}
   {fg(2)}{attr(0)}  {fg(59)}2. {fg(2)}{fg(59)}  Blader Runner {fg(59)}@read{attr(0)}
   {fg(2)}{attr(0)}  {fg(59)}3. {fg(2)}{fg(59)}  python {fg(59)}@study{attr(0)}


{attr(1)}Delete a task/note (can delete multiples by id):{attr(0)}
~$ {attr(1)}{fg(2)}%(prog)s {fg(4)}-d {fg(6)}1{attr(0)}

 {attr(4)}My Board{attr(0)} {fg(59)}[2/2]{attr(0)}
   {fg(2)}{attr(0)}  {fg(59)}2. {fg(2)}{fg(59)}  Blader Runner {fg(59)}@read{attr(0)}
   {fg(2)}{attr(0)}  {fg(59)}3. {fg(2)}{fg(59)}  python {fg(59)}@study{attr(0)}


{attr(1)}Delete all completed tasks:{attr(0)}
~$ {attr(1)}{fg(2)}%(prog)s {fg(4)}--clear{attr(0)}

"""