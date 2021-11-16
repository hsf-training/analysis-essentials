# Analysis automation with Snakemake

{% objectives "Learning Objectives" %}

- Learn what analysis automation is and how it helps with analysis preservation
- Learn how to create a pipeline with Snakemake

{% endobjectives %}

## Documentation and environments

You can find full documentation for Snakemake [at this link](https://snakemake.readthedocs.io/en/stable/index.html), you can also ask any questions you have on the [~reproducible](https://mattermost.web.cern.ch/lhcb/channels/reproducible) channel on mattermost.

Snakemake is best-run at LHCb using the `lb-conda` environment.
This environment comes with very recent versions of ROOT, python, cmake, g++, snakemake, *etc.* ready to use.
In general it is recommended that if you are running non-lhcb software (*e.g.*, code you've written yourself for your analysis) it should be done with `lb-conda`.

{% callout "accessing the `lb-conda` environment" %}

To have access to `lb-conda` you must first have sourced `LbEnv`.
This is done by default on lxplus, otherwise it is done with `source /cvmfs/lhcb.cern.ch/lib/LbEnv` (assuming [cvmfs](https://cvmfs.readthedocs.io/en/stable/) is installed).

The default environment can be entered with the command `lb-conda default`,
where `default` is the name of the environment.
This will enter you into an interactive bash shell.

> The full list of available environments can be found by running `lb-conda --list`.

You can optionally pass a command after the environment name,
*e.g.*, `lb-conda default foo`,
which will run the `foo` command in the environment and then exit.
(This is similar to the behaviour of [`lb-run`](https://twiki.cern.ch/twiki/bin/view/LHCb/SoftwareEnvTools).)

If you want your `.bashrc` file commands to be available in the created environment,
you can run `lb-conda default bash -c 'bash --rcfile ~/.bashrc'`.
Be careful if you do this--it can lead to conflicts in the environment.

{% endcallout %}

More infomation on using `lb-conda` can be found [here](https://gitlab.cern.ch/lhcb-core/lbcondawrappers/-/blob/master/README.md).

You can now check if Snakemake is working by calling `snakemake --help` in the `lb-conda default` environment.

## Basic Tutorial

### What is a workflow?

When performing an analysis, you typically start with some set of input files
containing the data you are interested in
and want to end up with some set of output files containing the results of your
measurements.
A workflow is what gets you from the input to the output.

Let us consider a simple example.
Create a new directory to work in and generate some fake input files:
```bash
mkdir basic_tutorial
cd basic_tutorial
mkdir input
touch input/{a..z}.in
ls inputs/
```
You should see a list of empty files named `a.in`, `b.in`, ..., and `z.in`.

{% challenge "Perform the workflow" %}

Add the text `My name is a.` to the end of `input/a.in`
and save it as `output/a.out` without modifying `input/a.in`.
Do this for each file in `input/`.

{% solution "Solution" %}

You could open each file, type the appropriate text
(*e.g.*, `My name is a.`, `My name is b.`, *etc.*),
and save it as the appropriate output file,
but since this is such a simple workflow,
we can easily make the shell do it for us:

```bash
mkdir -p output  # make the directory if needed
for file in input/*.in; do
  noext="${file%.in}"  # drop the extension
  name="${noext##input/}"  # drop the directory
  ofile="output/${name}.out"  # declare output file name
  cat "$file" > "$ofile"  # create output file with contents of input file
  echo "My name is $name." >> "$ofile"  # append the required text
done
```

{% endsolution %}

{% endchallenge %}

Congratulations, you've just defined and executed a workflow!

### Why use a workflow management system?

> “The Snakemake workflow management system is a tool
> to create reproducible and scalable data analyses”

The example workflow above is very simple,
but you can probably imagine more complicated ones.
Suppose you wanted to adjust your input files in more complicated ways,
had multiple types of input or output files,
or wanted to do calculations that didn't depend on just one input file.
Or suppose that your calculations took a long time
and you only wanted to re-run them if the inputs had changed.
These are all reasons to use a workflow management system.

- A workflow management system allows you to:
  - Keep a record of how your scripts are used
    and what their input dependencies are
  - Run multiple steps in sequence, parallelising where possible
  - Automatically detect if something changes and then reprocess data if needed
- Using a workflow management system forces you to:
  - Keep your code and your locations in order
  - Structure your code so that it is user-independent
  - Standardise your scripts
    - Bonus: Standardised scripts can sometimes be used across analyses!

If you have ever performed an HEP analysis
or looked at the code for someone else's analysis,
you probably understand why the above features are so useful.

Snakemake allows you to create a set of rules, each one defining a "step" of your analysis.
The rules need to be written in a file called `Snakefile`.
For each step you need to provide:

- The *input*: Data files, scripts, executables or any other files.
- The expected *output*. It's not required to list all possible outputs.
  Just those that you want to monitor
  or that are used by a subsequent step as inputs.
- A *command* to run to process the input and create the output.

The basic rule is:
```python
rule myname:
    input: "myinput1", "myinput2"
    output: "myoutput"
    shell: "Some command to go from in to out"
```

Let's give it a try with our simple example above.
In the same `basic_tutorial` directory,
let us first remove all our hard work by running
```bash
rm -rf output/
```
Now, we create our `Snakefile`.
In your favorite text editor,
open a new file called `Snakefile` and type
```python
rule name_files:
    input: "input/a.in"
    output: "output/a.out"
    shell: "cat input/a.in > output/a.out && echo 'My name is a.' >> output/a.out"
```
Snakemake now knows how to create `output/a.out`.

You can run it by calling
```bash
snakemake output/a.out --cores 1
```
This tells Snakemake that you want to generate `output/a.out` if needed
and to use only one computing core to do so.
After running it,
you should see output like:
```text
Building DAG of jobs...
Using shell: /cvmfs/lhcbdev.cern.ch/conda/envs/default/2021-09-07_04-06/linux-64/bin/bash
Provided cores: 1 (use --cores to define parallelism)
Rules claiming more threads will be scaled down.
Job stats:
job           count    min threads    max threads
----------  -------  -------------  -------------
name_files        1              1              1
total             1              1              1

Select jobs to execute...

[Mon Nov 15 18:30:25 2021]
rule name_files:
    input: input/a.in
    output: output/a.out
    jobid: 0
    resources: tmpdir=/tmp/username

[Mon Nov 15 18:30:26 2021]
Finished job 0.
1 of 1 steps (100%) done
Complete log: /afs/cern.ch/user/u/username/basic_tutorial/.snakemake/log/2021-11-15T183022.449488.snakemake.log
```
Here, we see that Snakemake selected the rule `name_files` to create `output/a.out`.
Calling `cat output/a.out`,
we see that the expected file was created with the appropriate text.
Notice that we did not have to tell Snakemake to create the `output/` directory;
Snakemake took care of it automatically.

Now, run `snakemake output/a.out --cores 1` again.
You should see output like:
```text
Building DAG of jobs...
Nothing to be done.
Complete log: /afs/cern.ch/user/u/username/basic_tutorial/.snakemake/log/2021-11-15T183344.711303.snakemake.log
```
Since `output/a.out` already exists, Snakemake did not try to create it again.

We still have files b-z to create.
We could create 25 more rules, one for each of the remaining files,
but Snakemake provides a feature called `wildcards` so we don't have to.
We edit our `Snakefile` to read
```python
rule name_files:
    input: "input/{name}.in"
    output: "output/{name}.out"
    shell: "cat {input} > {output} && echo 'My name is {wildcards.name}.' >> {output}"
```

Take a moment to understand what is happening in this rule declaration.
Wildcards are defined in `output`
and can then be accessed in `input` and `shell`.
**All wildcards must be present in `output`.**
We are essentially telling Snakemake that this is a rule that can create
files of the form `output/{name}.out`;
we cannot specify wildcards in `input` that are not present in `output`
because Snakemake will not know what they should be.

> Notice that the wildcard `name` appears as `{name}`
> in the declaration of `input` and `output`
> but as `{wildcards.name}` in the declaration of `shell`.
> This is an unavoidable quirk of how Snakemake works,
> and you must remember it to avoid errors.

Snakemake can now handle all of our input and output.
Run
```bash
snakemake output/{a..z}.out --cores 4
```
and notice that Snakemake has created all the output,
just as we did manually before.

Snakemake has many features that our original solution,
simply running a shell script, does not,
but one is particularly obvious in this case:
Since we told Snakemake to run with 4 cores,
it created (up to) 4 output files at once.
We didn't have to wait for each output file to be created one-by-one;
we were able to take advantage of our computing power
to perform multiple tasks *at the same time*.
This built-in parallelism is one of the nicest features
of using a workflow manager.

> You can see how many cores are on the machine you're using by calling
> `nproc` from the command line.
> If you're on lxplus, there should be 10.
> If you want Snakemake to use all of them,
> you can use `--cores all`.
> **This is bad practice on a shared machine**, like on lxplus;
> you should leave some computing resources available to other users
> so that they can at least log in.

We can tell Snakemake which files to create from within our Snakefile.
At the beginning of the file, add
```python
rule name_all:
    input: [f"output/{chr(x)}.out" for x in range(ord('a'), ord('z') + 1)]
```

> Notice that we have used python list-comprehension
> to declare the input files for rule `name_all`.
> Snakemake is python-based,
> so you can execute arbitrary python code anywhere in your `Snakefile`
> if you want to.
> Also notice that we have given a list as the input instead of a file name;
> Snakemake can handle both.

We have declared a new rule, `name_all`, at the beginning of the file
with all our required output files listed as `input`
and no `output` files declared.
Snakemake interprets the first rule in the `Snakefile` as the default rule,
and Snakemake will run it if no other output is requested.
If we remove `output/`,
```bash
rm -r output/
```
and run Snakemake again, this time without specifying any output,
```bash
snakemake --cores 4
```
we see that `output/` is produced the same as before.

Congratulations, you've just defined a workflow using Snakemake!

### Re-running rules

We saw above that if an output file already exists,
Snakemake will not create it again.
If you call `snakemake --cores 4` now,
you should see that it exits without running anything,
since all the files in `output/` already exist.
Now call
```bash
touch -m input/a.in
```
to update the modification time of `input/a.in` and run Snakemake again.
Now, you should see that Snakemake runs `name_files` just once to create `output/a.out`.
It does not try to create any of the other files,
and it creates `output/a.out` even though it already exists.
This is because we listed `input/a.in` as an input;
since it had been modified since the creation of `output/a.out`,
and we told `output/a.out` depended on `input/a.in`,
Snakemake decided `output/a.out` needed to be updated
and ran `name_files` again.

We can force the re-running of rules
using the `--force` or `-f` command-line argument.
Calling
```bash
snakemake output/a.out --cores 4 -f
```
will tell Snakemake to create `output/a.out` regardless of modification times.
If we want to re-run the whole workflow, we can use `--forceall`.

{% callout "Always do a dry run!" %}

Since Snakemake relies on modification times to decide which rules to run,
using version control software (such as git) can become complicated,
as files are routinely modified and then returned to their original form.
You can find a solution [here](https://snakemake.readthedocs.io/en/stable/project_info/faq.html?highlight=git#git-is-messing-up-the-modification-times-of-my-input-files-what-can-i-do).

Regardless of whether you use version control,
**always do a dry run before executing your workflow!**
You can do this by calling Snakemake with
the `--dry-run` or `-n` command-line argument,
which will print the rules Snakemake would execute
but prevents them from actually being executed.
If you have many rules and don't want to fill up your terminal with output,
you can use the `--quiet` or `-q` command-line argument in addition to `-n`
to print just a summary.

It's worth reiterating because this can easily become an issue
for complicated workflows
and it will save you a lot of wasted time:
**Always run with `-n` first!**

{% endcallout %}

### Chaining rules

We can also tell our `Snakefile` how to create our input files.
In our simple example here,
our inputs are just empty files in the `input/` directory,
which we created above by calling `touch input/{a..z}.in`.
Let's create a rule to do this for us.

{% challenge "Create the input" %}

Add a rule to `Snakefile` that can create
`input/a.in`, `input/b.in`, ..., and `input/z.in`.

{% solution "Solution" %}

Add a rule like the following to your `Snakefile`:
```python
rule create_input:
    output: "input/{name}.in"
    shell: "touch {output}"
```
You can name it anything you like and use any wildcard you want;
it will work regardless.

To check your solution, run
```bash
rm -rf input/ output/
snakemake --cores 4
```
Snakemake should create both the input and the output.

{% endsolution %}

{% endchallenge %}

Take a moment to understand what has happened.
We told Snakemake we wanted to generate `output/a.out`, ..., `output/z.out`,
and it knew to create `input/a.in`, ..., `input/z.in`
because the rule `name_files` depends on them.

We can make this dependency more explicit.
Modify `name_files` to read
```python
rule name_files:
    input: rules.create_input.output
    output: "output/{name}.out"
    shell: "cat {input} > {output} && echo 'My name is {wildcards.name}.' >> {output}"
```
As long as it is declared after rule `create_input`
and all of the wildcards of `create_input` are also declared in `name_files`,
this should produce the same output as before.

Notice that we could also just ask Snakemake to produce `input/a.in`
without reqesting `output/a.out`;
as far as Snakemake is concerned,
`input/a.in` is just another file it knows how to produce.

You can see the whole working `Snakefile` [here](code/basic_tutorial/Snakefile).

### The limits of wildcards

Our [`Snakefile`](code/basic_tutorial/Snakefile)
isn't limited to creating `output/a.out`, ..., `output/z.out`.
Trying calling
```bash
snakemake output/hello_world.out --cores 4
```
and observe what happens.
Snakemake has created `input/hello_world.in` and `output/hello_world.out`.

Now try
```bash
snakemake output/foo.bar --cores 4
```
This time, Snakemake raises a `MissingRuleException`;
this is because the extension `.bar` doesn't match the `output`
for rule `name_files`, which expects the `.out` extension.

{% challenge "Allow arbitrary output file extensions" %}

Teach `Snakefile` how to create an output file with any file extension.

{% solution "Solution" %}

Modify `name_files` to read:
```python
rule name_files:
    input: rules.create_input.output
    output: "output/{name}.{ext}"
    shell: "cat {input} > {output} && echo 'My name is {wildcards.name}.' >> {output}"
```
Notice that this doesn't affect the `input` file extension,
which is still `.in`.
Now, if you run
```bash
snakemake output/foo.bar --cores 4
```
Snakemake should generate `input/foo.in` and `output/foo.bar`

{% endsolution %}

{% endchallenge %}

As you can see from this challenge,
Snakemake allows `input` and `output` files to be of any type;
you could be creating `.root` files, `.gif` files, or `.docx` files
and Snakemake will execute regardless.

## Advanced Tutorial

An example. If you want to copy some text from a file called `input.txt` to `output.txt` you can do:

```python
rule copy:
    input: 'input.txt'
    output: 'output.txt'
    shell: 'cp input.txt output.txt'
```

You can even avoid typos by substituting variables instead of typing the filenames twice:

```python
rule merge_files:
    input: 'input_1.txt', 'input_2.txt'
    output: 'output.txt'
    shell: 'cat {input[0]} > {output} && cat {input[1]} >> {output}'
```

Input and output can also be parametrised using wildcards:

```python
rule copy_and_echo:
    input: 'input/{filename}.txt'
    output: 'output/{filename}.txt'
    shell: 'echo {wildcards.filename} && cp {input} {output}'
```

If you then make another rule with `output/a_file.txt` and `output/another_file.txt` as inputs they will be automatically created by the `copy_and_echo` rule.

```python
rule all:
     input: 'output/a_file.txt', 'output/another_file.txt'
```

This allows for rules to be reusable, for example to make a rule that can be used to process data with from different years or polarities.

Notice that:

* Inputs and outputs can be of any type
* You can provide python code after the tags. e.g. `input: glob("*.root")`
* Python functions can also be used as an input
* If a single file is used as an input/output, one can ommit the index when refering to the input/output.
* Wildcards must always be present in the output of a rule (else it wouldn't be possible to know what they should be)

Snakemake can also take an output of the previous rule as an input:

```python
rule create_file:
    output: 'test_file.txt'
    shell:
       'echo test > {output}'

rule copy_file:
    input: rules.create_file.output
    output: 'copied_test.txt'
    shell:
       'cp {input} {output}'
```

{% challenge "Write a snakefile with a single rule" %}


To try out download:

```bash
$ wget https://github.com/hsf-training/analysis-essentials/raw/master/snakemake/code/tutorial.tar
$ tar -xvf tutorial.tar
```

You will find one containing names and phone numbers. You can make one rule that, given a name extracts the line with the phone of that person.

To do this in a shell you can use `grep`, which is a command that lists all lines in a file containing a certain text.

```bash
$ grep ciao test.txt
ciao a tutti
```

{% endchallenge %}

### Usage and basic behaviour

And now that your `Snakefile` is done it's time to run! Just type

```bash
snakemake rulename_or_filename --cores 1
```


This will:
1. Check that the inputs exist
   * If inputs exists &rarr; 2)
   * If inputs do not exist or have changed snakemake will check if there is an other rule that produces them &rarr; Go back to 1)
2. Run the command you defined in `rulename_or_filename` (or the rule that generates the filename that is given) usin 1 core
3. Check that the output was actually produced.

Note, that one must specify the number of cores being used in snakemake.

Comments, which rules are run:
* If want to run a chain of rules only up to a certain point just put the name of the rule up to which you want to run on the snakemake command.
* If you want a rule to be "standalone" just do not give its input/outputs as outputs/inputs of any other rule
* It is normal practice to put as a first rule a dummy rule that only takes as inputs all the "final" outputs you want to be created by any other rule. In this way when you run just `snakemake` with no label it will run all rules (in the correct order).

{% challenge "Make a snakefile with at least 3 rules connected to each other and run them in one go" %}


In the tutorial folder you find two files containing addresses, and phone numbers.
You can make rules that, given a name, `grep` the address and phone and then one other rule to merge them into your final output file.

If we do this for “Luca”, it can be represented by the following graph:

[![DAG](img/DAG_single-wide.png)](img/DAG_single.png)

Which could be achieved using this shell script:

```bash
grep Luca inputs/addresses.txt > output/Luca/myaddress.txt
grep Luca inputs/phones.txt > output/Luca/myphone.txt
cat output/Luca/myaddress.txt > output/Luca/data.txt && cat output/Luca/myphone.txt >> output/Luca/data.txt
```

_But it does not have to be this, any other task is fine, be creative!_


{% endchallenge %}

{% challenge "Use wildcards" %}


Following on from the previous challenge use wildcards to make it so that any name can be used, such as “Fred”

```bash
snakemake output/Fred/data.txt --cores 1
```

{% solution "Solution" %}


See `Snakefile` in the `simple_solution` folder [here](code/tutorial.tar).

{% endsolution %}

{% endchallenge %}

Comments, partial running:

* If part of the input is already present and not modified the corresponding rule will not run
Note that if you put your code into the inputs snakemake will detect when your code changes and automatically rerun the corresponding rule!
* If you want to force running all rules even if part of the output is present use `snakemake --forceall`
* If you want to check the snakemake rules chain without actually running them use `snakemake -n`

{% challenge "Explore the snakemake behaviour" %}

In the previous example try deleting one of the intermediate files, rerun snakemake and see what happens

{% endchallenge %}



{% callout "snakemake utility functions" %}


Snakemake provides a lot of utils functions, some of the most common ones are described here.
* `expand` : returns a python list that is filled according to the possible wildcards values.
For example, an python expression `['output/{}/file.txt'.format(name) for name in names]` can be replaced with `expand('output/{name}/file.txt', name = names)` in the inputs.
* `temp`: specifies that the output file is temporary. For example, `temp('file.root')` will be deleted as the last rule that uses it as an input has finished.
* `directory`: specifies that the output is a directory rather than a file. For example, `directory('output/plots')`. Snakemake 6+ will not create this directory automatically, as it happens with the output files. One way around it is to have a `mkdir` in the `shell` before excuting the main command or having a special rule that creates all necessary directories. Note, that when the snakemake rule falls all outputs are being deleted including the directories.

{% endcallout %}

### Sub-labels

Inside the pre-defined tags you can add custom subtags as in this example.

```python
rule run_some_py_script:
    input:
        exe = 'myscript.py',
        data = 'mydata.root',
        extra = 'some_extra_info.txt',
    output: 'output.txt'
    shell: 'python {input.exe} {input.data} --extra {input.extra} > {output}'
```

So this will effectively launch the command:

```bash
python myscript.py mydata.roo --extra some_extra_info.txt > output.txt
```

The `--extra` is not necessary. It's just to illustrate how python scripts options can be used.

{% challenge "Code as input" %}

Add your python script to the inputs than make some modifications to it, rerun snakemake and see what happens.

{% endchallenge %}



### Run and shell

You have two ways to specify commands. One is `shell` that assumes shell commands as shown before.
The other is `run` that instead directly takes python code (Careful it's python3!).

For example the copy of the file as in the previous example can be done in the following way.

```python
rule dosomething_py:
    input: 'myfile.txt'
    output: 'myoutput.txt'
    run:
        with open(str(input), 'rt') as fi:
            with open(str(output), 'wt') as fo:
                fo.write(fi.read())
```

And finally you can mix! Namely you can send shell commands from python code.
This is useful, in particular if you have to launch the same shell command on more inputs.

```python
rule dosomething_pysh:
    input:
        code = 'mycode.exe',
        data = ['data1.root', 'data2.root']
    output: 'plot1.pdf', 'plot2.pdf'
    run:
        for f in input.data:
            shell('./{input.code} %s' % f)
```
Note the list brackets in the `output.data` to highlight the fact that the data output is a list.
If the brackets were absent, snakemake would not allow this rule to run, assuming that the `"data2.root"` is the next positional output.
In snakemake positional inputs/outputs have to be positioned before the keyword (labeled) inputs/outputs.

{% challenge "Use run instead of shell" %}

Rewrite your previous file using a python script to run the search and use `run` to run on both phones and addresses in the same rule

{% solution "Solution" %}

An example solution can be found [here](code/Snakefile).
Although it's fine if you have done it a different way.

{% endsolution %}

{% endchallenge %}

### Config files

Often you want to run the same rule on different sample or with different options for your scripts.
This can be done in snakemake using config files written in [yaml](https://learn.getgrav.org/advanced/yaml).

For example let's put the datafiles in a cfg.yaml file

```python
data:
    - 'data1.root'
    - 'data2.root'
```

Now in your Snakefile you can load this config file and then its content will be available into the rules as a dictionary called "config". Yes, it seems black magic, but it works! Your Snakefile will look like this

```python
configfile: '/path/to/cfg.yaml'

rule dosomething_pysh:
    input:
        code = 'mycode.exe',
        data = config['data'],
    output: ['plot1.pdf', 'plot2.pdf']
    run:
        for f in input:
            shell('./{input.code} %s' % f)
```

The config dictionary can be used anywhere, also inside the shell command or even outside a rule.

{% challenge "Make a config file" %}

Put the inputs of your script into a config file

{% endchallenge %}

### Includes

The Snakefile can quickly grow to a monster with tens of rules. For this reason it's possible to split them into more files and then include them into the Snakefile. For example you might have a `fit_rules.snake` and `efficiency_rules.snake` and then your Snakefile will look like this:

```python
include: /path/to/fit_rules.snake
include: /path/to/efficiency_rules.snake
```

The order of the includes is irrelevant.

{% challenge "Use includes" %}

Move your rules to other files and include them

{% solution "Solution" %}


You can find a solution in the `more_complete_solution` folder, which you can find [here](code/tutorial.tar).

{% endsolution %}

{% endchallenge %}

### Reports

As well as executing rules snakemake is also able to produce _reports_. These are html files and can contain information such as a diagramisation of your DAG as well as statistics about the run time of your rules and summaries of your outputs. To include a file in the report simply add the `report` flag to it e.g.

```python
rule myRule:
	input:
 		SomeFile.root
	output:
 		report(Output.pdf) # this will now be included in the report
	shell:
  		python RuleForExecution.py {input}
```

N.B. the reporting feature does not work with files already marked as `temp`

To produce the report you first run the `snakemake` command as you normally would.
Then run the exact same command again adding the `--report` flag as the first argument to your snakemake command.

A command such as `snakemake --report report.html` will produce a report containing everything.
By constrast `snakemake fig1.pdf --report report-short.html` will produce a short report of just that one target.

Some screenshots of what a report may look like are shown below. Information in the report includes: a graph showing the DAG of the completed jobs, each node of this graph can be clicked to show the rule in more detail; the time taken to run each job; and a summary of all the produced files.

Ideally every plot which is included in an ana note would have a report explaining how it was made.

[![Reporting DAG](img/Reporting_DAG.png)](img/Reporting_DAG.png)
[![Reporting stats](img/Reporting_stats.png)](img/Reporting_stats.png)
[![Reporting rule](img/Reporting_rule.png)](img/Reporting_rule.png)

For more information on using reports as well as more examples, see the snakemake documentation [here](https://snakemake.readthedocs.io/en/stable/snakefiles/reporting.html).

<!-- TODO add this section once the linked page is finished
### Workflow preservation

https://lhcb-dpa.web.cern.ch/lhcb-dpa/wp6/workflow-preservation.html
-->
