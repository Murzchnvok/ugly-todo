<h1 align="center">Ugly To-Do</h1>
<h3 align="center">A nice way to create tasks and save notes offline from your terminal!</h3>
<div align="center">
    <img src="https://github.com/Murzchnvok/ugly-todo/blob/main/screenshots/utd.png?raw=true" />
</div>

<p>This tool do just what I wanted it to do, but it's opensource and unlicense, so feel free to create your own version of this.</p>

## Install

### PIP (recommended)

```bash
pip3 install -U utd
```

### Manual

Clone the repo:

```bash
git clone https://github.com/Murzchnvok/ugly-todo
```

Go to the ugly-todo folder and install the requirements:

```bash
pip3 install -r requirements.txt
```

Create **bin** folder in the **$HOME** directory (if it doesn't exist):

```bash
mkdir $HOME/bin/
```

_Add the **bin** folder to the **$PATH** variable!_

Now create a symlink to the **main.py** script:

```bash
ln -s $HOME/ugly-todo/src/main.py $HOME/bin/utd
```

## Usage

Help menu:

```bash
utd -h
```

Add a simple task:

```bash
utd -a simple task
```

Add a task with tag(s):

```bash
utd -a simple task with @tag
```

Add a task with tag(s) and priority:

```bash
utd -a not important task @tag @whatever -p 3
```

Add a note:

```bash
utd -n Keep Calm and STUDY
```

## You might be interested

- [utd (made in rust)](https://github.com/kawaki-san/utd-rs)
- [Taskbook (task and notes command line)](https://github.com/klaussinani/taskbook)
