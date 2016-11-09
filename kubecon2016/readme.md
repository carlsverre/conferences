# Keynotes

## A Cloud Native State of the Union
Dan Kohn, Exec Director, Cloud Native Computing Foundation

- CN State of the Union
- Cloud Native? What is it, where is it going?
- History of the cloud
    - Sun Microsystems profited before the cloud :)
    - Startups, "We need 2 million dollars to get started with the hope that it
      turns into something"
    - Launching a new app, buy hardware!
    - VMWare (2001)
        - popularized virtual machines
    - AWS (2006)
        - Launched EC2
        - "IaaS"
        - No more CapEx, now OpEx
        - Still VMs, just no upfront
    - Heroku (2009)
        - 12 factor application
        - process for building/running a container is opaque, but deploying is just
          "git push heroku"
    - End of proprietary companies
    - OpenStack & other Open Source IaaS (2010)
        - Competes with AWS and VMWare, still based on VMs
        - Pivotal Cloud Foundry Foundation - open source version of Heroku
    - Docker (2013)
        - Thinks of it like TBL creating WWW
        - URLs are not actually that innovative, but gluing it together in the
          right way with great UX makes magic happen
        - Fastest uptake of a developer technology ever
        - Enables isolation, reuse, immutability
    - Cloud Native (Dec 2015)
        - segment applications into microservices
        - packaging each part into its own container
        - dynamically orchestrating those containers to optimize resource
          utilization
        - Google donates Kubernetes to cloud native foundation
- What have we learned?
    - Servers -> VMs -> Buildpacks -> Containers
    - From pets to cattle
    - Provider has migrated from closed source, single vendor to open source,
      cross vendor
- What about PaaS?
    - "80 percent of applications still fit into the PaaS environment"
    - PaaS on top of Cloud Native supports all deployment models
- Why are we here?
    - Value Prop is that Docker is the shit
    - Open source stack enables moving between public or private cloud
    - Scalability -> Google starts 2 billion containers per week
    - Agility and Maintainability -> splitting applications into microservices
      with explicitly described dependencies
    - Central orchestration process that dynamically manages and schedules
      microservices
    - Resiliency
- What can we do better?
    - Diversity in community is low - should be better
    - Documentation is lacking
    - Meh boring section
- What are we doing well?
    - Samsung SDS America joining Cloud Native Computing Foundation
- Software in a Post-Github World
    - No one is impressed today by a software repo, mailing list, or website
    - Foundations need to offer a different set of services
    - CNCF's goal is to be the best place to host cloud native software projects
        - (nit: they are trying to be the cloud version of Apache foundation)
    - CNCF features
        - 20k per year for docs
        - $15M, 1000 node cluster for testing
- Where are we going?
    - Kubernetes Managed Service Provider
        - 3 or more certified engineers
        - business model to support enterprise end users
        - demonstrable activity in the Kube community including active contrib

## Finally, A True Cloud Platform
Sam Ghods, Co-founder of Box

"Kubernetes: Finally a true cloud platform"

- A platform abstracts away a messy problem so you can build on top of it.
- Examples: Linux, Java, Twilio
- Two dimensions to measure platform: Portability & Extensibility
- Linux
    - Runs on (nearly) all hardware
    - Extensibility -> tooling, unix philosophy
- Cloud Infrastructure
    - Overall, pretty bad right now
    - Portability
        - Right now this sucks -> each provider has a diffent implementation of
          each major "feature"
        - Hard to abstract over all the different features
        - "looking at the wrong layer" -> go up a layer to the PaaS stacks
            - issue with PaaS: provide functionality first, abstraction layer
              second
            - end up with proprietary tools, or optimized for a particular
              system
        - When trying to design a "cloud microservice" application - you have to
          think about the underlying system too much
    - Extensibility
        - What kind of tooling can you build against the platform
        - Imagine, different examples of tooling you might want
            - Ex: Visualizer: show all the different apps that are running & their resources
            - Ex: Federator: auto-balances instances of your application across many
              different cloud providers, scale up/down to public cloud depending
              on cost
            - Ex: Operator: Re-size, backup a stateful database, organize a
              distributed system
        - Hard to do these today in an abstract way (works with any system)
        - No incentive to do it? <- not sure why
- He believes there is a solution to all of these things
    - Shows the mesos logo - lots of laughs!
    - Kubernetes!
- Why Kube?
    - Optimized for all infrastructures
    - Known, stable API, you can build incredible tooling against
    - Unparalleled team and community
- Why not mesos or swarm or...
    - team behind Kube is increible, and one of the best
    - For example: Google brings tons of experience and is dedicated
    - Redhat - focused on making it great and improving its on premise compat
      with tons of hardware
    - CoreOS providing backbone to the system (Etcd)
- Kubernetes
    - Portability
        - Abstract your service into a Kube native object that is portable
          between cloud providers
        - Write one spec, submit to any cluster running anywhere and it runs
        - Developer's can work on specs - Ops can deploy them
    - Extensibility
        - Ex: Kube dashboard for visualizing the stack
        - Ex: cluster federation for scaling up/down to different underlying
          platforms
        - Ex: etcd operators -> custom schedulers to organize complex
          distributed system problems
- What is the future?
    - We have the opportunity to do what AWS did for infra but in a more open
      and amazing way

## Backstage with Kubernetes
Chen Goldberg, Director of Engineering, Container Engine & Kubernetes, Google

- Talked a bunch about how the project is organized
- Everything is documented in Github Issues
- Features repository is maintained
    - https://github.com/kubernetes/features
- Starting a new "class 0" getting started online course


## OpenShift is Enterprise-Ready Kubernetes
Chris Wright, VP/Chief Technologist, RedHat

- What are top concerns for container adoption
    - security, scalability, performance, integration, management
    - security is # 1 from a Forrester survey of 151 professionals in various
      companies
- OpenShift is RHEL's version of Kubernetes
    - trusted host -> pointing at RHEL as being a trusted system for a long time
      in big companies
    - RH is investing in container security/verification so that companies can
      do compliance on containers
    - Integrated CI/CD pipeline

## IFNW (If This Now What) - Orchestrating an Enterprise
Michael Ward, Pearson

(Goal: learn about their distributed CD/CI system)
(Goal: Security?  Multi-tenant?  How do developers have access?)

- Pearson has been around for 172 years
    - 40k employees, 70 countries
    - focus is on education
- 70+ datacenters!
    - 36k servers
    - 2k servers
        - up to 30 microservices per application
    - 400+ dev teams
    - When Mike joined: 1:1 build server to dev team
        - like jenkins
- Migrate it to Kubernetes and the Cloud
- Mike Ward is principle architect on Project Bitesize
    - devoperandi.com
    - @devoperandi
- Don't undertake a project unless it is manifestly important and nearly
  impossible.
    - Edwin Land, started Polaroid
- I have not failed.  I've just found 10,000 ways that won't work.
    - Thomas Edison
- Things they built
    - Authz Webhook
    - stackstorm
        - event driven automation platform
    - kubernetes tests
        - testing your infra once its come up
        - how do you know when you deploy an instance of kube that its ready to
          go?
- For the Pearson kube platform - they had lots of goals
    - geo distributed
    - jenkins are cattle
    - automated deploys & a/b deploys
    - reduce costs (45% reduction avg)
    - fast - 5-15% faster with 1/4 of the instances
    - standardization, same build process for all 400+ dev teams
    - ease of use
- Things they are missing right now
    - good feedback loops (clear communication across teams)
    - automated upgrades, A/B deploys of the infrastructure
    - compliance
- Demo: of bitesize
    - creates a kube namespace, and links to a git repo (jenkins reaches out to
      this thing)
    - when devs create namespaces - they are approved by someone with the
      approve_ns permission
    - assign quotas to each namespace automatically
    - jenkins is auto deployed to each namespace
    - looks like each namespace is auto-assigned DNS
    - the namespace repo contains YAML config files to tell jenkins to deploy
      the application
    - three repos per application - config, code, test
    - jenkins config
        - kube integration to spin up build slaves
        - blue/green deploys built in
        - continuous or manual deployment
    - developers don't have to know how to deploy a docker image - jenkins
      builds and pushes the image into the platform
        - NOTE: security here?
    - initial launch
        - seed job in jenkins which reads the config files in the config repo
    - they don't use Dockerfiles - they have an abstract repr of an
        application
    - they basically built their own package manager that integrats with other
      managers like debian repos, maven, etc
    - Service spec seems to be able to declare what URL they want
        - anyone can get any url on pearson.com? wtf
    - The demo takes 9 minutes to deploy itself <- super slow lol
    - Next he adds Mongo and MySQL to the "application"
        - apparently these deploy as virtual machines in AWS rather than
          containers?
    - The MySQL config goes into RDS
- uses cloudformation and third-party resources
    - vault/consul provides security and access
- LOL makes the repo that runs the build system at Pearson open source on stage
    - https://github.com/pearsontechnology/deployment-pipeline-jenkins-plugin
- They use authz for managing ACL inside kubernetes
    - https://github.com/pearsontechnology/bitesize-authz-webhook

## You're Monitoring Kubernetes Wrong
Loris Degioanni, CEO/Founder, Sysdig

- How to build a kube monitoring system
    - start with data
    - pipe into big data engine
    - unicorns and rainbows
- We are in the middle of a big change
    - PCs/Servers -> VMs -> Containers
    - Unit: machine -> machine -> app/service
    - Orchestration: none -> external -> native
    - Architecture: monolithic -> monolithic -> service-based
- Things are becoming more complex (but better)
    - we used to have separate tiers which are deployed and managed independently
    - now everything is thrown into the same infra
    - this makes monitoring hard
- 4 things that are harder now
    1. getting the data
    2. making sense of the data
    3. troubleshooting
        - understanding root cause
    4. people
- Getting the data
    - containers are simple, small, good building blocks
    - they are more opaque! Each one is a magical pony
    - pods
        - primitive that you can collect information about
        - good place to put monitoring containers (inside a pod)
        - this allows you to reduce complexity since the monitoring container
          knows how to monitor the other containers in the pod - but can expose
          a consistent interface
    - sysdig
        - monitors all syscalls in all containers - pod agnostic
        - just need to deploy one "monitor agent" per machine rather than a
          monitor per pod
        - the act of instrumenting infra should be as transparent as possible
    - Guidelines
        - you should not be involved in monitoring instrumentation
        - don't produce anything that ins't a custom metric
            - infra, basic metrics, kernel info, app metrics, database metrics
            - the monitoring system should handle as much as possible
              automatically
        - every metric should be tagged
            - tagging should be integrated with kubernetes
            - people shouldn't tag metrics - tagging should be entirely
              automated
            - ex: this cpu metric came from this container in this pod on this
              host, etc
            - enables segmentation and learning
        - you should collect everything, with no filters
            - don't know what you don't know
- Troubleshooting
    - when you can't figure it out - current solution is to ssh in
        - this might be impossible in modern systems
        - it might be too late
    - Loris does a demo of csysdig
        - shows the containers view
        - hits a container, the view shows the processes running in the
          container and whats going on
        - csysdig has native kubernetes support to collect all information for
          the entire cluster
        - uses another view to collect deployment information
        - drills down from a kube services -> a single nginx worker thread and
          then a single connection and then shows the exact set of syscalls
          executed for the duration of that http request
            - cool to see him do this live, its a pretty mind blowing demo
- People
    - microservices are about people
    - monitoring microservices should be about people too
    - Introducing Sysdig Teams
    - Supports isolation and customization
    - MemSQL was a beta-tester for this
    - They added kube annotation support to teams
        - in a deployment spec he adds a teamMembers annotation with some email
          addresses
        - defines some dashboards, alerts, and a slack channel for alerts
        - configures sysdig alerts as well
    - Demo
        - he does the deployment, which causes an email to be sent to a new
          email account he setup for the demo since the user wasn't already in
          sysdig
        - the user is auto-added to a sysdig team which was created for the
          deployment automatically
        - only things created by the deployment are visible to this new user
        - also the dashboards and alerts are auto-setup as configured

## Lightning talks

- Saw a couple, standing room only
- OpenDNS looks promising as a cloud native alternative to SkyDNS
- Second to last talk showed off deploying Histrix (sp?) (Netflix OSS) on top of
  OpenShift

## Delivering Kubernetes Apps with Helm
Deis & Bitnami
Presenters are all core contributors to Helm

- Correlates kubernetes without Helm as building your own furniture
- Helm is a tool to manage a group of resources as one unit
- NVM this talk is boring - helm is a system to organize templated unit files
- Next!

## Kubernetes Ingress: Your Router, Your Rules
Gerred Dillon, Deis

- Service: semantically related set of resources
    - Not concerned with routing
    - Service defined by label selection
    - represents a semantically related set
    - cares about every member of that set
- Ingress: mapping of external traffic to virtual resource
    - virt host, external ips, domain names, LB rules
    - External ident -> virtual IP -> n pods -> 1 resource
- configuring ingress resources
    - TLS
    - virt host routing
    - path based routing
    - custom rules
    - demo
        - he shows some example Ingress specs, showing off easy routing
          management tls etc (above things)
- If you aren't on GCE - Ingress resources require Ingress controllers
- Ingress decouples your routing rules from your application
- Demo
    - deploys the croc-hunter chart with helm to his kube cluster
        https://github.com/lachie83/croc-hunter/tree/master/charts/croc-hunter
- shows how to build a basic nginx ingress controller
    - most of the code is here: https://github.com/kubernetes/contrib/tree/master/ingress/controllers
- Another demo - integrate staging/prod pipeline to ingress controller
- Uses https://buildkite.com/ for CI/CD
- Shows how you can leverage Helm to easily customize specs depending on
  deployment requirements - this would have helped us with Cirrus

## Case Study: Kubernetes at Comcast
David Arbuckle, Comcast VIPER

- Cloud DVR, what is it?
    - 15 microservices
    - 300 Gbit/s network egress, 7 Tbit/s to disk
    - legal req to store a separate copy of each video for each user
    - 1mil+ DB writes per sec
    - 10+ datacenters in 2017
    - 2500 containers per deploy
- May 2015 - first comcast architecture for this product
    - very complex
    - based on bad existing processes
    - based on vmware which had configuration drift
    - Low confidence of success for deployment
        - "documentation is in the wiki, good luck"
- Goals
    - managable deployments to many environments
    - guaranteed lab / production parity
    - instrumented deployment process to manage risk
    - faster release cycles
    - architectural agility for a greenfield project
- had to choose between the various options (mesos, swarm, nomad, etc)
- Why Kubernetes?
    - Containers
        - configuration + code in same repo
        - versioning semantics for application at specific configuration
        - abstracts away *some* deployment variability
    - Lets them use containers at scale
- Things we had to do
    - undercloud provisioning / undercloud config mgmt
    - IPVS load balancer
    - monitoring + log aggregation
    - docker repo + base images + bug fixes
    - educate users
- Undercloud provisioning: challenge
    - existing deployments exhibiting undercloud configuration drift
    - Kubernetes solves config drift for applications
    - need to solve config drift for Kubernetes
        - as they roll out changes to infra, need to stop and check on the way
          that they aren't introducing new problems
        - things like puppet tend to default to applying config all at once,
          hard to do partial rollout for infra
- Undercloud provisioning: goals
    - source of truth: git
    - upgrade + new deploys are same process
    - support for deployments of databases, object storage
    - avoid any turing complete solutions
        - ?
- Undercloud provisioning: approach
    - git repo binds a site to a config version
    - DHCP and iPXE uses server reboot to rebuild a site
    - CoreOS fleet lays down Kubernetes and other services
    - "The entire set of configuration for an undercloud is an entity"
- Undercloud provisioning: outcome
    - 1000+ physical servers
    - capacity augmentation for kube is fully automated
    - fleet has some drawbacks
        - not a great way to deploy software, all or nothing approach
        - would like to be able to roll out partial site upgrades more easily
        - vender lock in to fleet is painful
    - constraints are a good idea
- Load balancing: challenge
    - ingress didn't exist yet
    - we need 300Gbit/s egress bandwidth
    - solution: IPVS + special sauce
    - austintek.com/LVS...
- Load balancing: approach
    - Client -> IPVS Master -> (choose IPVS backend)
    - master ARPs IP to router
    - master forwards packet to backend
    - backend replies directly to client
    - Optimized for egress bandwidth since you can scale up the backends and
      they don't push data through the master
- Load Balancing: Outcome
    - L4 solution works well
    - Application uses ConfigMap to bind a VIP to a service
    - Ingress limited to 20Gbit/s until we BGP peer with the router
    - scales to 100+ Gbit/s egress per cluster
    - changes applied within 5 seconds
- Logs and monitoring: challenge
    - dev team at the time had no ops experience
    - no dev team in VIPER had EVER instrumented their app with statsd or other
    - no dev team... log aggregation
    - "Ops visibility was orthogonal to feature development"
    - "new tooling requires a cultural shift and a lot of indoctrination"
- Logs and monitoring: approach
    - logs
        - used third party service -> "expensive logging  service"
        - "write your logs to stdout and we will do the hard work"
    - monitoring
        - they use sysdig cloud
        - didn't want to do any instrumentation
- Logs and monitoring: success?
    - too successful?
    - emitting 100s of GBs of logs per day per site, Whoops.
    - there's no replacement for instrumenting an application to emit
      internally-measured telemetry
        - what is my application doing as measured by my application
- Kubernetes Problems
    - user space load balancer
        - sounds like this was fixed by the IPTables LB in modern Kube
    - pod density limitations
        - something like 256 pods per minion, they wanted to have a container
          per channel per viewer?  That seems crazy
    - NAT hairpin mode
        - pod sends request to another container on that node it could hang
        - set a config param in kube proxy to support this type of traffic
- Docker problems
    - cryptic "container doesn't exist" error
    - docker attach hangs containers
        - because they were using this to read logs from stdout from the
          container main process - the reader would fall behind and block the
          process by blocking the stdout pipe
    - docker bridge race condition
        - bad interaction between coros networkd and docker bridge
        - no defensive programming in docker to check to see if the underlying
          device is up
        - shows up as a race between docker setting up the bridge and a third
          party system bringing up a new network device
        - Diamanti might hit this as well?
- Kernel defects
    - github.com/coreos/bugs/issues/1275
    - per-node throughput was limited to < 1Gbit/s
    - interrupts were being processed on all cores
    - workaround pins all interrupts to a single socket by restricting the
      number of network receive queues
- By Oct 2016 they had a fully realized Kube stack
- Success Factors
    - Team
    - Careful technology choices, committing to tech decisions
    - conservative approach to use of features within the stack
    - solving the education gap by collocating teams
    - attempting to devops
- Stumbling blocks
    - Tech issues above
    - NAT hairpinning
    - Managing state
        - especially on premise
- What they need to do better
    - Devops: actually hard
    - Infrastructure responsibility: actually hard
        - don't have anyone lower level than you to blame, especially on premise
    - Saying "No": actually hard
- Where we're going
    - 6 products in progress or finished
    - immutable deployment for kube infra
    - dealing with multi-tenancy reqs
    - scaling beyond 200 nodes, BGP load balancing

- Questions
    - Dealing with state
        - they managed state internally
            - mention MemSQL as "in memory distributed database"
            - also mentioned "object storage"
    - How are they managing SSL
        - they aren't
    - Whats driving IPV6
        - big push in Comcast to move to IPV6
        - set-top boxes are starting to become IPV6 only
    - Whats the dev interface
        - In house CI/CD pipeline called Concourse
        - tool that takes multiple state files and breaks it out into a bunch of
          kube config files
    - How much traffic can we handle per container?
        - Per machine is ~20 Gbit/s
    - How long do containers live
        - application dependente
        - deploy each week which churns the entire cluster
        - 50-100 pods up/down per hour
    - What specific to Kubernetes made this successful
        - fact that Kubernetes artifacts are declarative and stateful
        - made it easy to test in a lab first and then deploy to prod
    - Is kube getting picked up outside of VIPER at Comcast
        - remains to be determined
        - lots of interest throughout Comcast
        - other teams looking to mirror VIPER's success
    - How important is network security between microservices
        - right now not important
        - as they start using Kube in a more multi-tenant way it becomes more
          important
    - Resource management to prevent microservices from colliding with each
      other
        - They will use resource quotas in the future

## Cluster Federation in Kubernetes: Past, Present and the Future
Madhu C.S. & Quinton Hoole, Google

- building blocks
    - network traffic management
    - resource placement
- federation comes with some downsides
    - bandwidth cost can be different, also faster to say inside one cluster
      rather than spanning
- location affinity
    - strictly coupled pods/applications
    - loosely coupled
    - preferentially coupled
    - important to have these distinctions
- what exists
    - talking about ubernetes
    - 100% kube compat (missing some types)
    - Q2 2016
        - basic CP
        - federated services
            - multi-cloud, multi-region
            - service discovery support
                - dns supports "find the closest" shard of that
                  service
    - Q3 2016
        - added support for
            - ingress
            - replicasets
            - namespaces
            - secrets
        - event integration
    - Q4 2016: easier installation, expanded API
        - added support for
            - deployments
            - daemonsets
            - jobs
            - configmaps
        - "much easier control plane installation tools"
- The future
    - Policy-based resource placement
        - overlays policy over application reqs
    - IAM support (RBAC)
        - integration with external IAM, across multiple cloud providers
    - Stateful Apps and federated persisted storage
        - petset integration?
        - cross-cluster data replication, snapshot + restore
    - hybrid cloud federated ingress
        - smart cross-cloud L7 load balancing
    - private federated services
        - private IPs and DNS
    - GUI/Visual layer, etc...
- Demo!
    - created 9 kube clusters in three different regions (3 clusters in
      different zones per region)
    - he deployed the federated control plane (Ubernetes) over the clusters
      already
    - use the regular kubectl CLI to operate a ubernetes cluster since the api
      layer is the same
    - use kube context to make it easy to manage the entire system
    - he has a script which writes the current GCE zone to a html file
    - he mentions that configmaps would be useful to deploy his script to all
      the machines
        - but ubernetes doesn't support configmaps yet
    - He adds the script as base64 encoded data as a secret so it is replicated
      to all clusters via federated secrets
    - Then he launches a replicaset of pods with 9 replicas (one pod should be
      in each cluster)
        - each pod runs nginx and busybox - busybox mounts the script and runs
          it before exiting
    - after deploying the RS he deploys a federated service (same spec api as
      normal)
        - this is replicated to each cluster automatically and the DNS records
          are updated automatically since gcloud auto-exposes DNS for services
    - he connects to a single cluster and sees the RS definition, which for each
      cluster is only set to a desired size of 1
    - next he wants to show that services in a cluster can connect to services
      in another cluster just as if they were in a single cluster
    - he launches busybox in a cluster and attaches to bash inside it
        - inside this he wget's the service dns name, the service LB routes this
          to the closest shard which is the nginx container running in the same
          zone as BB
        - if that shard was down, the service would have routed him to the next
          closest shard
            - how does it determine closeness?
- back to slides
- Cross cluster federation
    - federated replicasets & global L7 ingress
    - the speaker just goes through the previous demo example in slides really
      quick
- How to create a federated control plane
    - Its just a regular kube application that connects back to Ubernetes API
    - FCP is
        - api sever
            - service with public VIP
            - deployment of replicas
        - controller manager
            - deployment of replicas
        - data store (etcd), for registered clusters
        - credentials for the underlying clusters
        - federation config
            - dns provider creds
            - dns zone setup
    - Clusters are defined as a regular kube resource
        - federation/v1beta1
        - kind: Cluster
- Questions
    - Security concerns with federation?
        - story is pretty weak ATM
        - currently federation doesn't really have sec
        - a user provides creds for a cluster to the federation
        - federation gives anyone access to the federation access to the
          underlying cluster
        - future will be multi-tenant users for ubernetes that might support
          credential pushdown?
    - Network policy, how to build ACLs for ingress
        - they work through the kube API
        - anything that kube supports that is reasonable to implement will
          eventually be supported
    - How will HA control plane work?
        - multiple api servers backed by quorum of etcd hosts
        - controller manager will support election/master etc
        - common HA deployment will be multiple clusters in same region but in
          different availability zones
            - due to requirements on low latency for true HA (sync replication
              etc)
