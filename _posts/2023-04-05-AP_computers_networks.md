---
toc: true
comments: true
layout: post
title: Computers and Networks (Unit 4)
description: Add Definitions from Unit 4 Computer Systems and Networks
image: /images/apcsp.png
categories: []
type: ap
week: 29
---

## Requirements
> Work through College Board Unit 4... blog, add definitions, and pictures.  Be creative, for instance make a story of Computing and Networks that is related to your PBL experiences this year.


### How a Computer Works
> As we have learned, a computer needs aa program to do something smart.  The sequence of a program initiates a series of actions with the computers Central Processing Unit (CPU). This component is essentially a binary machine focussing on program instructions provided.  The CPU retrieives and stores the data it acts upon in Random Access Memory (RAM). Between the CPU, RAM, and Storage Devices a computer can work with many programs and large amounts of data.

List specification of your Computer, or Computers if working as Pair/Trio
Processor: 11th Gen Intel(R) Core(TM) i5-11320H @ 3.20GHz   2.50 GHz
- <b>Processor GHz</b>: 2.50 GHz
- <b>Memory in GB</b>: 8.00 GB 
- <b>Storage in GB</b>: 220 GB 
- <b>OS</b>: Microsoft Windows 11 Home


Define or describe usage of Computer using Computer Programs. Pictures are preferred over a lot of text.  Use your experience.
- <b>Input devices</b>: These are hardware components that enable users to provide data or instructions to a computer. Examples include a mouse, touchscreen, microphone, and webcam.
- <b>Output devices</b>: These are hardware components that display information processed by a computer to users. Examples include a monitor, printer, and projector.
- <b>File</b>: A file is a collection of data or information that is stored in a specific location on a computer. It can contain various forms of data, such as text, images, audio, and video.
- <b>Program Code</b>: This is a written set of instructions that directs a computer to perform a specific task. It is created using a programming language and compiled into a program file.
- <b>Processes</b>: These are individual programs or tasks that are running on a computer's operating system.
- <b>Ports</b>: These are communication endpoints that facilitate data exchange between devices or applications in a computer network.
- <b>Data File</b>: A data file is a file that contains information or data that can be utilized by a program. Examples include text files, images, and spreadsheets.
- <b>Inspect Running</b>: This refers to the process of examining the code that is currently being executed on a computer to identify and resolve any issues or errors.
- <b>Inspect Variables</b>: This process involves examining the named storage locations or variables in a program's code to understand how they are being utilized and how they are affecting the program's behavior.

![Diagram]({{site.baseurl}}/images/firstpic.png)
![Computer Hardware]({{site.baseurl}}/images/cpu.jpeg)


### The Internet
> Watch/review College Board Daily Video for 4.1.1

- Essential Knowledge
    - A computing device is a physical artifact that can run a program. Some examples include computers, tablets, servers, routers, and smart sensors.
    - A computing system is a group of computing devices and programs working together for a common purpose.
    - A computer network is a group of interconnected computing devices capable of sending or receiving data.
    - A computer network is a type of computing system. 
    - A path between two computing devices on a computer network (a sender and a receiver) is a sequence of directly connected computing devices that begins at the sender and ends at the receiver.
    - Routing is the process of finding a path from sender to receiver.
    - The bandwidth of a computer network is the maximum amount of data that can be sent in a fixed amount of time.
    - Bandwidth is usually measured in bits per second

- Complete Vocabulary Matching Activity.  Incorporate this into your learnings from year.  To analyze measure path and latency use `traceroute` and `ping` commands from Linux Terminal.  

- A <b>Path</b>: A series of directly connected computing devices that starts at the sender and ends at the receiver.
- E <b>Route</b>: The process of determining a path from the sender to the receiver.
- B <b>Computer System</b>: A collection of computing devices that work together towards a common goal.
- C <b>Computer Device</b>: A physical object that is capable of running programs. Examples include computers, tablets, servers, routers, and so on.
- D <b>Bandwidth</b>: The maximum amount of data that can be transmitted within a specific period of time on a computer network.
- F <b>Computer Network</b>: A type of computing system in which a group of interconnected computers can exchange data with one another.
- <mark>Additional Information</mark>: In computer networks, communication occurs via <b>packet switching</b>, whereby a message or file is broken down into packets and transmitted in any order. Each packet contains source and destination information, and they are reassembled at the recipient's device.
![Path and Routing]({{site.baseurl}}/images/pathandrouting.png)

> Watch/review College Board Daily Video 4.1.2

- <b>Complete True of False Questions</b>
1. T 
2. F
3. F
4. T
5. F
6. F
7. T


- Essential Knowledge
    - The internet is a computer network consisting of interconnected networks that use standardized, open (nonproprierary) communication protocols.
    - Access to the internet depends on the ability to connect a computing device to an internet connected device.
    - A protocol is an agreed-upon set of rules that specify the behavior of a system.
    - The protocols used in the internet are open, which allows users to easily connect additional computing devices to the internet.
    - Routing on the internet is usually dynamic; it is not specified in advance
    - The scalability of a system is the capacity for the system to change in size and scale to meet new demands.
    - The internet was designed to be scalable
    - Information is passed through the internet as a data stream. Data streams contain chunks of data, which are encapsulated in packets. 
    - Packets contain a chunk of data and metadata used for routing the packet between the origin and the destination on the internet, as well as for data reassembly.
    - Packets may arrive at the destination in order, out of order, or not at all
    - IP, TCP and UDP are common protocols used on the internet.
    - The world wide web is a system of linked pages, programs, and files.
    - HTTP is a protocol used by the world wide web
    - The world wide web uses the internet

<mark>Extra Notes</mark>

![Model]({{site.baseurl}}/images/model.png)
- <b>Network Access</b>: The physical hardware (such as an internet cable or wifi connection) that provides access to a computer network.
- <b>Internet</b>: A system that uses packets, sender and receiver IP addresses, and routing metadata to enable communication between devices across different computer networks.
- <b>Transport</b>: A layer in the internet protocol stack that includes two primary protocols: TCP, which provides error checking and recovery at the cost of slower performance and a 3-way handshake to verify message delivery, and UDP, which provides faster performance and discards erroneous packets but does not perform error checking.
- <b>Application</b>: Software services that use the internet, such as web services, domain name services, and HTTP/HTTPS (HTTP with added security).
- <b>World-Wide Web</b>: A collection of linked data pages that are accessed through the internet, but is not the same as the internet itself.

- Go over AP videos, vocabulary, and essential knowledge.  Draw a diagram showing the internet and its many levels. A preferred diagram would using your knowledge of frontend, backend, deployment, etc.  Picture would highligh vocabulary by illustration. The below illustration have some ideas

![Full Stack]({{site.baseurl}}/images/fullstack.png)



- Often we draw pictures of machines communicating over the Internet with arrows.  However, the real communication goes through protocol layers and the machine and then is trasported of the network.   For College Board and future Computer Knowledge you should become familiar with the following ...

```
     User Machine  <---> Frontend Server <---> Backend Server
    +-----------+         +-----------+         +-----------+
    |  Browser  |         |  GH Page  |         |   Flask   |
    +-----------+    ^    +-----------+    ^    +-----------+
    |    HTTP   |    |    |    HTTP   |    |    |    HTTP   |
    +-----------+    |    +-----------+    |    +-----------+
    |    TCP    |    |    |    TCP    |    |    |    TCP    |   
    +-----------+    |    +-----------+    |    +-----------+
    |     IP    |    V    |     IP    |    V    |     IP    |
    +-----------+         +-----------+         +-----------+
    |  Network  |  <--->  |  Network  |  <--->  |  Network  |
    +-----------+         +-----------+         +-----------+
```

The "http" layer is an application layer protocol in the TCP/IP stack, used for ***communication between web browsers and web servers***. It is the protocol used for transmitting data over the World Wide Web.

The "transport" layer (TCP) is responsible for providing reliable data transfer between applications running on different hosts.  The TCP protocol segments the data into smaller ***chunks called "segments"***. Each segment contains a sequence number that identifies its position in the original stream of data, as well as other control information such as source and destination port numbers, and checksums for error detection.

The "ip" layer is responsible for packetizing data received from the TCP layer of the protocol stack, and then ***encapsulating the data into IP packets***. The IP packets are then sent to the lower layers of the protocol stack for transmission over the network.

The "network" layer is responsible for ***routing data packets between networks*** using the Internet Protocol (IP). This layer handles tasks such as packet addressing and routing, fragmentation and reassembly, and ***network congestion*** control.


### Fault Tolerance
> Watch both Daily videos for 4.2
- <b>NOT fault tolerant</b>: Doesn’t use many resources, Failure in one network = fatal 
- <b>Fault tolerant</b>: Redundant and uses more resources. But even if one path goes down, a device can communicate with all other devices. Makes network stronger!


- <b>Complete the network activity, summarize your understanding of fault tolerance.</b>
Fault tolerance refers to a network's capacity to resist disruptions. Networks achieve this by utilizing multiple interconnected nodes to ensure that the failure of one or two connections does not result in a system-wide outage. The fault tolerance of a network can be determined by verifying that all devices can communicate with each other even if one path is down.

### Parallel and Distributed Computing
> Review previous lecture on Parallel Computing and watch Daily vidoe 4.3.  Think of ways to make something in you team project to utilize Cores more effectively.  Here are some thoughts to add to your story of Computers and Networks...

<mark>Notes</mark>
- Computer tasks: The goal is to balance tasks across all CPUs evenly and fully utilize them.
- System tasks: This involves scheduling what task to do next, managing hardware, and working with the network.
- User tasks: These tasks are programs selected by the user to execute.
- Sequential Computing: Tasks are performed one after another.
- Parallel Computing: 
    - Programs are broken down into smaller sequential computing tasks, which are performed simultaneously on the same computer.
    - Hardware drives this approach and leads to faster operations, and it is data-driven.
    - The efficiency of parallel computing is measured by comparing the execution time to that of sequential computing.
    - The speed-up time is calculated by dividing the time to complete a task sequentially by the time to complete the same task in parallel.
Distributed Computing:
    - It involves sending tasks from one computer to another and performing a mix of sequential and parallel computing.
    - This approach can solve problems that require more processing time or storage than a single computer can provide, such as Google web search.
    - A network is required for distributed computing to work.

- What is naturally Distributed in Frontend/Backend architecture?  
The frontend and backend are separated into various self-sufficient components in a distributed architecture. As a result, they can be constructed and implemented independently, resulting in faster development, simpler maintenance, and more scalability.

- Analyze this command in Docker: ```ENV GUNICORN_CMD_ARGS="--workers=1 --bind=0.0.0.0:8086"```.   Determine if there is options are options in this command for parallel computing within the server that runs python/gunicorn.  Here is an [article](https://medium.com/building-the-system/gunicorn-3-means-of-concurrency-efbb547674b7)


> Last week we discussed parallel computing on local machine.  There are many options.  Here is something to get parallel computing work with a tool called Ray.
- Review this [article](https://www.anyscale.com/blog/writing-your-first-distributed-python-application-with-ray)...  Can you get parallel code on images to work more effectively?  I have not tried Ray.

There are multiple methods to optimize parallel code for image processing. The first method is to split the image into smaller sections and process each section concurrently. Another approach is to use a parallel image processing library that is specifically designed for this purpose. Alternatively, you can utilize a distributed computing platform to execute the code on multiple machines, which can also enhance performance.

- Code example from ChatGPT using squares.  This might be more interesting if nums we generated to be a lot bigger.

```python
import ray

# define a simple function that takes a number and returns its square
def square(x):
    return x * x

# initialize Ray
ray.init()

# create a remote function that squares a list of numbers in parallel
@ray.remote
def square_list(nums):
    return [square(num) for num in nums]

# define a list of numbers to square
nums = [1, 2, 3, 4, 5]

# split the list into two parts
split_idx = len(nums) // 2
part1, part2 = nums[:split_idx], nums[split_idx:]

# call the remote function in parallel on the two parts
part1_result = square_list.remote(part1)
part2_result = square_list.remote(part2)

# get the results and combine them
result = ray.get(part1_result) + ray.get(part2_result)

# print the result
print(result)

```
