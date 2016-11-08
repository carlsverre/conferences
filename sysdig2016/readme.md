# Workshop 1 (trace01.scap)

Who is hacking?
sysdig -c topconns sysdig -c topconns fd.port=22
syslog -c spy_syslog proc.name=sshd

Solution = 10.1.1.123

# Workshop 2 (trace02.scap)

Find the failing HTTP request.
What is wrong with them

~/sysdig/sysdig-ccwfs $ sysdig -r trace02.scap -c httplog | grep response_code=5
2016-10-22 11:25:33.729330185 < method=GET url=10.1.1.40/ response_code=503 latency=0ms size=213B
2016-10-22 11:25:34.955081576 < method=GET url=10.1.1.40/ response_code=503 latency=0ms size=213B

use csysdig to look for the bad request

# Workshop 3 (trace03.scap)

sysdig -c topscalls
sysdig -c topprocs_errors
sysdig proc.pid=2132 and evt.type=close
sysdig -r trace03.scap -p "%proc.cmdline" proc.name=python
sysdig -r trace03.scap -c echo_fds proc.name=python and fd.name contains "script.py"

---

# Building a Chisel

This was a super cool talk in which the speaker built a chisel live on stage to
essentially extract a file from a trace file. This worked by the user specifying
the file descriptor, then the chisel looks for the open, set of writes and the
close - buffering the file as it goes in memory.  At close it writes it out to a
user specified location.

---

# Brendan Greggk - Designing Tracing Tools

- He is working on tools for BPF (and bcc)
- Talk is going to be about how to go through building a tracing tool and
  figuring out what goes into it.

SLIDES: http://www.slideshare.net/brendangregg/designing-tracing-tools-67693476

## Methodologies

- brendangregg.com/methodology.html
- At syscall layer:
    - workload characterization
        - trace connect()/accept()
        - exec()/open()
        - read()/write() - look at the size histogram
    - latency analysis
        - read()/write() latency histogram
    - USE method
        - network utilization per thread
        - syscall errors

"Eliminate dumb (unneeded) workloads first"

"Easy to invent tracing tools that track far too much"

Instead pick three -> Utilization, Saturation, Errors - the USE method
brendangregg.com/usemethod.html

## CLI Tracing Tools

He uses 6 different templates of output (see slides)

(demo)

Plays with the sysdig lab (trace files)

Things he likes about working in the CLI:

- leverage the scrollback buffer to easily cross reference different command outputs
- copy and paste chunks of things around easily
- after solving an issue copy the output of `history` to easily share with
  others or record work in a ticket
- combine unix tools to help investigation

(end demo)

- Template 1: Per event output
- opensnoop command snoops files which syscalls are operating on
- Template 2: Thresholding
- sysdig -c fileslower 1
    - print events that are slower than some threshold
- Template 3: interval summary
    - example stat, top
    - dcstat - directory cache stats
- Template 4: count summary
    - frequency count based on some filter
    - ex: funccount 'vfs'
- Template 5: histogram summary
    - ex: biolatency - tracing block device I/O
- Template 6: heatmap summary
    - ex: spectrogrm
    - ex: sysdig chisel subsecoffset.lua
    - for each second - shows all of the events that woke up at some offset in
      the second

"Know what already exists, and what doesn't"

"If the Kernel already has some counters built in [use those]"

Performance tools incur overhead! Test and measure to see if it is acceptable.

"If you can't write the workload, you can't write the tool"

## Visualizations

- Tables - good in GUI due to easy filtering/sorting/etc
- Line graphs - something thats hard to do in the CLI and get the detail required
- Histograms - can do on CLI - but more detail and more compelling in GUI
- Heat Maps

---

# Loris Degioanni - Advanced Application Debugging
@lorisdegio

- Talk is going to focus on tracers
- Actively inject events into the sysdig stream (in addition to syscalls for ex)
- You can mark the beginning and end of *spans*
    - function calls
    - requests
- write event to /dev/null
    - this helps the feature be container friendly - no privileged mode needed
- low instrumention overhead (<1ns)
- Tracer events are always composed of an enter/exit event - correlated by ID,
  called a span

He shows off some cool examples of using tracing.  Its super easy - just write
something like `::foo::` (there are around 5 domains of data separated by `:`)

- Once you have defined spans - one thing you can do is filter for only events
  which were run within the span. This is HUGE

```
sysdig evtin.span.tags=my_span
```

Format of the data written to /dev/null:

```
<direction>:<ID>:<tag1>.<tag2>...:<argname1>=<val1>,<argname2>=<val2>...
```


Moving on, Loris shows off a new JS based tool he hacked together.  It is a
chisel which collects the information you want, then packages it together into a
simple static webapp that renders an interactive flamegraph for each span.  VERY
COOL - and using a chisel to build the app is so great.

More info:
https://github.com/draios/sysdig/wiki/Tracers

---

# Matthew Garrett - Building Trustworthy Containers

"Convenience often beats security"

- If your entire business model requires building a service - it can often trump
  security in the short term
- How can we ensure security wins?
- Make the secure solution the better solution.
- Great example of ensuring that security is also a more convenient and better
  solution: ssh versus rsh
- Another solution: LetsEncrypt solving SSL
- Bad example: SELinux, Seccomp
- Containers give us well-defined interfaces
- Abstraction: containers are usually built to communicate over IP with another
  container - the unit of abstraction helps encourage container developers do
  write things in this way.
- We can grant containers only the capabilities they need - essentially
  containers are solving the problem which SELinux tried to solve.
- We can grant containers only the capabilities they need - essentially
  containers are solving the problem which SELinux tried to solve.
- Containers move much security to the runtime - you can apply a policy to a
  workload rather than an individual process
- "sudo setenforce 0"
- "c makes it very easy to make you bad at writing c"
- How can we trust containers?  How can we verify that bundled libraries in
  containers don't have vulnerable libraries
- static analysis works for securing docker containers
- "not all openssl use is equally security critical"
    - This is something I think people often overlook!
- Huge win here - you no longer need to verify that 30 pieces of software work
  with the new version of OpenSSL - you just need to upgrade the containers
  which actually use openssl in a security context
- "No security feature provides meaningful security if the layers below it are
  not secure."
    - Turtles all the way down
- Next he talks about some of the interesting solutions to ensure security at
  the OS/Kernel/HW levels
    - ChromeOS - verifiable system with immutable sections that can prove the
      rest of the system is correct in a cryptographic manner
    - "Trusted Computing"
- Signed container images
    - The contents of this container at some point of time was signed by someone
      (you might trust).  If you have a container which is signed you know that
      it is the exact set of contents that the signer saw.
    - Signed containers does not imply trusted - for example a signed container
      may contain an OpenSSL vulnerability - such that it had to be replaced in
      prod at a later time with another signed container which doesn't have the
      vulnerability
        - the point here is that automated systems should have their trusted
          signatures rolled when you roll out security updates such that an
          attacker can't roll back to an earlier version of the container which
          may contain some compromisable piece of software
- Using TPM its possible to ensure that the set of containers which *can* run is
  exactly the set of containers which we *currently* trust.  When we deploy new
  containers we can invalidate the signatures for the previous containers which
  may contain some security flaw.
- Conclusion is that it's possible to trust containers in a distributed
  container system

---

# Mark Stemm - Intro to Falco

- Analogy - home security prevents intrusion
    - lots of things that prevent access
    - other things that *detect* access
- a behavioral activity monitor
    - define sysdig filters to detect activity you want to monitor
    - define notification methods - files, stdout, syslog, etc
- falco connects to the sysdig probe just like the sysdig clients do
    - pushes down filters into the probe
    - anything matching the filters moves into the alerting engine where it can
      be pushed out to one of the supported notification integrations
    - notifications can basically go anywhere since at the end of the day you
      can just have falco call an arbitrary command with some args
- falco uses a yaml file to define all of the macros, lists and rules
    - each rule defines the filter, output and priority (among some other meta
      properties)
    - all active rules are combined into a gigantic single sysdig filter by
      combining rules with OR

Challenge:
Find the IP address thats doing something funky

send a slack message via api to the webhook in the public slack channel
output should include ip address, finder and something else
