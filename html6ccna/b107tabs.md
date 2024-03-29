###### Table 1-2 TCP/IP Architectural Model and Example Protocols
__|__
--|--
TCP/IP Architecture Layer | Example Protocols
Application | HTTP, POP3, SMTP
Transport| TCP, UDP
Internet | IP, ICMP
Data Link & Physical | Ethernet, 802.11 (Wi-Fi)  
Table end.   

###### Table 1-3 Summary: Same-Layer and Adjacent-Layer Interactions
__|__
--|--
Concept | Description Same-layer interaction on different computers | The two computers use a protocol to communicate with the same layer on another computer. The protocol defines a header that communicates what each computer wants to do.
Adjacent-layer interaction on the same computer | On a single computer, one lower layer provides a service to the layer just above. The software or hardware that implements the higher layer requests that the next lower layer perform the needed function.    

Table end.   
###### Table 1-4 Chapter Review Tracking
__|__|__
--|--|--
Review Element | Review Date(s) | Resource Used
Review key topics || Book, website
Review key terms || Book, website
Answer DIKTA questions || Book, PTP Online     
  
Table end.   
###### Table 2-2 Examples of Types of Ethernet
__|__
--|--
Speed Common Name Informal IEEE
Standard Name
Formal IEEE
Standard Name
Cable Type,
Maximum Length
10 Mbps Ethernet 10BASE-T 802.3 Copper, 100 m
100 Mbps Fast Ethernet 100BASE-T 802.3u Copper, 100 m
1000 Mbps Gigabit Ethernet 1000BASE-LX 802.3z Fiber, 5000 m
1000 Mbps Gigabit Ethernet 1000BASE-T 802.3ab Copper, 100 m
10 Gbps 10 Gig Ethernet 10GBASE-T 802.3an Copper, 100 m
Table end.
Table 2-3 A 10BASE-T and 100BASE-T Pin Pairs Used
Transmits on Pins 1,2 Transmits on Pins 3,6
PC NICs Hubs
Routers Switches
Wireless access point (Ethernet interface) —
Table end.
Table 2-4 A Sampling of IEEE 802.3 10-Gbps Fiber Standards
Standard Cable Type Max Distance*
10GBASE-S MM 400m
10GBASE-LX4 MM 300m
10GBASE-LR SM 10km
10GBASE-E SM 30km
Table end.
Table 2-5 Comparisons Between UTP, MM, and SM Ethernet Cabling
Criteria UTP Multimode Single-Mode
Relative Cost of Cabling Low Medium Medium
Relative Cost of a Switch Port Low Medium High
Approximate Max Distance 100m 500m 40km
Relative Susceptibility to Interference Some None None
Relative Risk of Copying from Cable Emissions Some None None    
   
Table end.   
   
###### Table 2-6 IEEE 802.3 Ethernet Header and Trailer Fields
__|__|__
--|--|--
Field | Bytes | Description
Preamble | 7 | Synchronization.
Start Frame Delimiter (SFD) | 1 | Signifies that the next byte begins the Destination MAC Address field.
Destination MAC Address | 6 | Identifies the intended recipient of this frame.
Source MAC Address | 6 | Identifies the sender of this frame.
Type | 2 | Defines the type of protocol listed inside the frame; today, most likely identifies IP version 4 (IPv4) or IP version 6 (IPv6).
Data and Pad* | 46– 1500 | Holds data from a higher layer, typically an L3PDU (usually an IPv4 or IPv6 packet). The sender adds padding to meet the minimum length requirement for this field (46 bytes).
Frame Check Sequence (FCS) | 4 | Provides a method for the receiving NIC to determine whether the frame   experienced transmission errors.   
   
   
Table end.  

###### Table 2-7 LAN MAC Address Terminology and Features
__|__
--|--
LAN Addressing Term or Feature| Description 
MAC | Media Access Control. 802.3 (Ethernet) defines the MAC sublayer of IEEE Ethernet.
Ethernet address, NIC address, LAN address | Other names often used instead of MAC address. These terms describe the 6-byte address of the LAN interface card.
Burned-in address | The 6-byte address assigned by the vendor making the card.
Unicast address | A term for a MAC address that represents a single LAN interface.
Broadcast address | An address that means “all devices that reside on this LAN right now.”
Multicast address | On Ethernet, a multicast address implies some subset of all devices currently on the   Ethernet LAN.   
   
   
Table end.   
###### Table 2-8 Chapter Review Tracking
__|__|__
--|--|--
Review Element | Review Date(s) | Resource Used
Review key topics || Book, website
Review key terms || Book, website
Answer DIKTA questions || Book, PTP
Review memory tables || Book, website   
   
   
Table end.
###### Table 3-2 Different Names for a Leased Line
__|__
--|--
Name | Meaning or Reference
Leased circuit, Circuit | The words line and circuit are often used as synonyms in telco terminology; circuit makes reference to the electrical circuit between the two endpoints.
Serial link, Serial line | The words link and line are also often used as synonyms. Serial in this case refers to the fact that the bits flow serially and that routers use serial interfaces.
Point-to-point link, Point-topoint line |  These terms refer to the fact that the topology stretches between two points, and two points only. (Some older leased lines allowed more than two
devices.)
T1 | This specific type of leased line transmits data at 1.544 megabits per second (1.544 Mbps).
WAN link, Link | Both of these terms are very general, with no reference to any specific technology.
Private line | This term refers to the fact that the data sent over the line cannot be copied by other telco customers, so the data is private.   
   
   
Table end.
###### Table 3-3 Comparing HDLC Header Fields to Ethernet
__|__|__
--|--|--
HDLC Field | Ethernet Equivalent |  Description
Flag | Preamble, SFD | Lists a recognizable bit pattern so that the receiving nodes realize that a new frame is arriving.
Address | Destination Address | Identifies the destination device.
Control | N/A | Mostly used for purposes no longer in use today for links between routers.
Type Type Identifies the type of Layer 3 packet encapsulated inside the frame.
FCS | FCS | Identifies a field used by the error detection process. (It is the only trailer field in this table.)   
   
   
Table end.
###### Table 3-4 Chapter Review Tracking
__|__|__
--|--|--
Review Element | Review Date(s) | Resource Used
Review key topics || Book, website
Review key terms || Book, website
Answer DIKTA questions || Book, PTP
Review memory tables|| Book, website   
   
   
Table end.
###### Table 4-2 Cisco IOS Software Command Help
__|__
--|--
What You Enter | What Help You Get
? | Provides help for all commands available in this mode.
command ? | With a space between the command and the ?, the switch lists text to describe all the first parameter options for the command.
com? | Lists commands that start with com.
command parm? | Lists all parameters beginning with the parameter typed so far. (Notice that there is no space between parm and the ?.)
command parm<Tab> | Pressing the Tab key causes IOS to spell out the rest of the word, assuming that you have typed enough of the word so there is only one option that begins with that string of characters.
command parm1 ? | If a space is inserted before the question mark, the CLI lists all the next parameters and gives a brief explanation of each.  
   
   
Table end.
###### Table 4-3 Key Sequences for Command Edit and Recall
__|__
--|--
Keyboard Command What Happens
Up arrow or Ctrl+P | This displays the most recently used command. If you press it again, the next most recent command appears, until the history buffer is exhausted. (The P stands for previous.)
Down arrow or Ctrl+N | If you have gone too far back into the history buffer, these keys take you forward to the more recently entered commands. (The N stands for next.)
Left arrow or Ctrl+B | This moves the cursor backward in the currently displayed command without deleting characters. (The B stands for back.)
Right arrow or Ctrl+F | This moves the cursor forward in the currently displayed command without deleting characters. (The F stands for forward.)
Backspace | This moves the cursor backward in the currently displayed command, deleting characters.
   
   
Table end.
###### Table 4-4 Common Switch Configuration Modes
__|__|__
--|--|--
Prompt | Name of Mode | Context-Setting Command(s) to Reach This Mode
hostname(config)# | Global | None—first mode after configure terminal
hostname(config-line)# | Line | line console 0 line vty 0 15
hostname(config-if)# | Interface | interface type number 
hostname(vlan)# | VLAN | vlan number
   
   
Table end.
###### Table 4-5 Names and Purposes of the Two Main Cisco IOS Configuration Files
__|__|__
--|--|--
Configuration Filename |  Purpose | Where It Is Stored
startup-config | Stores the initial configuration used anytime the switch reloads Cisco IOS. | NVRAM
running-config | Stores the currently used configuration commands. This file changes dynamically when someone enters commands in configuration mode. | RAM
   
   
Table end.
###### Table 4-6 Chapter Review Tracking
__|__|__
--|--|--
Review Element | Review Date(s) | Resource Used
Review key topics || Book, website
Review key terms|| Book, website
Repeat DIKTA questions || Book, PTP
Review memory tables || Book, website
Review command tables || Book
   
   
Table end.
###### Table 4-8 Chapter 4 Configuration Commands
__|__
--|--
Command | Mode and Purpose
line console 0 | Global command that changes the context to console configuration mode.
login | Line (console and vty) configuration mode. Tells IOS to prompt for a password (no username).
password pass-value | Line (console and vty) configuration mode. Sets the password required on that line for login if the login command (with no other parameters) is also configured.
interface type port-number | Global command that changes the context to interface mode— for example, interface FastEthernet 0/1.
hostname name | Global command that sets this switch’s hostname, which is also used as the first part of the switch’s command prompt.
exit | Moves back to the next higher mode in configuration mode.
end | Exits configuration mode and goes back to enable mode from any of the configuration submodes.
Ctrl+Z | This is not a command, but rather a two-key combination (pressing the Ctrl key and the letter Z) that together do the same thing as the end command.
  
  
Table end.
###### Table 4-9 Chapter 4 EXEC Command Reference
__|__|__
--|--|--
Command | Purpose
no debug all undebug all | Enable mode EXEC command to disable all currently enabled debugs.
reload | Enable mode EXEC command that reboots the switch or router.
copy running-config startup-config | Enable mode EXEC command that saves the active config, replacing the startup-config file used when the switch initializes.
copy startup-config running-config | Enable mode EXEC command that merges the startup-config file with the currently active config file in RAM.
show running-config | Lists the contents of the running-config file.
write erase erase startup-config erase nvram: | These enable mode EXEC commands erase the startup-config file.
quit | EXEC command that disconnects the user from the CLI session.
show startup-config | Lists the contents of the startup-config (initial config) file.
enable | Moves the user from user mode to enable (privileged) mode and prompts for a password if one is configured.
disable | Moves the user from enable mode to user mode.
configure terminal | Enable mode command that moves the user into configuration mode.
   
   
Table end.
###### Table 5-2 Chapter Review Tracking
__|__|__
--|--|--
Review Element | Review Date(s) | Resource Used
Review key topics || Book, website
Review key terms || Book, website
Repeat DIKTA questions || Book, PTP
Do labs || Book, Sim Lite, blog
Review command tables || Book
   
   
Table end.
###### Table 5-4 Chapter 5 EXEC Command Reference
__|__
--|--
Command | Mode/Purpose/Description
show mac address-table | Shows all MAC table entries of all types
show mac address-table dynamic | Shows all dynamically learned MAC table entries
show mac address-table dynamic vlan vlan-id | Shows all dynamically learned MAC table entries in that VLAN
show mac address-table dynamic address mac-address| Shows the dynamically learned MAC table entries with
that MAC address show mac address-table dynamic interface interface-id | Shows all dynamically learned MAC table entries
associated with that interface show mac address-table count | Shows the number of entries in the MAC table and the total number of remaining empty slots in the MAC table
show mac address-table aging-time | Shows the global and per-VLAN aging timeout for inactive MAC table entries
clear mac address-table dynamic | Empties the MAC table of all dynamic entries
show interfaces status | Lists one line per interface on the switch, with basic status and operating information for each
clear mac address-table dynamic vlan vlan-number interface interface-id address mac-address | Clears (removes) dynamic MAC table entries: either all (with no parameters), or a subset based on VLAN ID, interface ID, or a specific MAC address
  
  
Table end.
###### Table 6-2 Commands Related to the History Buffer
__|__
--|--
Command | Description
show history | An EXEC command that lists the commands currently held in the history buffer.
terminal history size x | From EXEC mode, this command allows a single user to set, just for this one login session, the size of his or her history buffer.
history size x | A configuration command that, from console or vty line configuration mode, sets the default number of commands saved in the history buffer for the users of the console or vty lines, respectively.
  
  
Table end.
###### Table 6-3 Chapter Review Tracking
__|__|__
--|--|--
Review Element | Review Date(s) | Resource Used
Review key topics | Book, website
Review key terms | Book, website
Repeat DIKTA questions | Book, PTP
Review config checklists | Book, website
Do labs | Sim Lite, blog
Review command tables | Book
   
   
Table end.
###### Table 6-5 Login Security Commands
__|__
--|--
Command | Mode/Purpose/Description
line console 0 | Changes the context to console configuration mode.
line vty 1st-vty last-vty | Changes the context to vty configuration mode for the range of vty lines listed in the command.
login | Console and vty configuration mode. Tells IOS to prompt for a password.
password pass-value | Console and vty configuration mode. Lists the password required
if the login command (with no other parameters) is configured. login local | Console and vty configuration mode. Tells IOS to prompt for a username and password, to be checked against locally configured username global configuration commands on this switch or router.
username name secret pass-value | Global command. Defines one of possibly multiple usernames and associated passwords, used for user authentication. Used when the login local line configuration command has been used.
crypto key generate rsa modulus 360..2048 | Global command. Creates and stores (in a hidden location in flash memory) the keys required by SSH.
transport input {telnet  ssh  all  none} | vty line configuration mode. Defines whether Telnet/SSH access is allowed into this switch. Both values can be configured on one command to allow both Telnet and SSH access (the default).
  
  
Table end.
###### Table 6-6 Switch IPv4 Configuration
__|__
--|--
Command | Mode/Purpose/Description
interface vlan number | Changes the context to VLAN interface mode. For VLAN 1, allows the configuration of the switch’s IP address. 
ip address ip-address subnet-mask | VLAN interface mode. Statically configures the switch’s IP address and mask.
ip address dhcp | VLAN interface mode. Configures the switch as a DHCP client to discover its IPv4 address, mask, and default gateway.
ip default-gateway address | Global command. Configures the switch’s default gateway IPv4 address. Not required if the switch uses DHCP.
ip name-server server-ip-1 server-ip-2 … | Global command. Configures the IPv4 addresses of DNS servers, so any commands when logged in to the switch will use the DNS for name resolution.
  
  
Table end.
###### Table 6-7 Other Switch Configuration
__|__
--|--
Command | Mode/Purpose/Description
hostname name | Global command. Sets this switch’s hostname, which is also used as the first part of the switch’s command prompt.
enable secret pass-value | Global command. Sets this switch’s password that is required for any user to reach enable mode.
history size length | Line config mode. Defines the number of commands held in the history buffer, for later recall, for users of those lines.
logging synchronous | Console or vty mode. Tells IOS to send log messages to the user at natural break points between commands rather than in the middle of a line of output.
no logging console | Global command that disables or enables the display of log messages to the console.
exec-timeout minutes seconds | Console or vty mode. Sets the inactivity timeout, so that after the defined period of no action, IOS closes the current user login session.
    
    
Table end.
###### Table 6-8 Chapter 6 EXEC Command Reference
__|__
--|--
Command | Purpose
show running-config | Lists the currently used configuration.
show running-config  begin line vty | Pipes (sends) the command output to the begin command, which only lists output beginning with the first line that contains the text “line vty.”
show dhcp lease | Lists any information the switch acquires as a DHCP client. This includes IP address, subnet mask, and default gateway information.
show crypto key mypubkey rsa | Lists the public and shared key created for use with SSH using the crypto key generate rsa global configuration command.
show ip ssh | Lists status information for the SSH server, including the SSH version.
show ssh | Lists status information for current SSH connections into and out of the local switch.
show interfaces vlan number | Lists the interface status, the switch’s IPv4 address and mask, and much more.
show ip default-gateway | Lists the switch’s setting for its IPv4 default gateway.
terminal history size x | Changes the length of the history buffer for the current user only, only for the current login to the switch.
show history | Lists the commands in the current history buffer.
  
  
Table end.
###### Table 7-2 LAN Switch Interface Status Codes
__|__|__|__
--|--|--|--
Line Status | Protocol Status | Interface Status | Typical Root Cause
administratively down | down | disabled | The shutdown command is configured on the interface.
down | down | notconnect | No cable; bad cable; wrong cable pinouts; speed mismatch; neighboring device is (a) powered off, (b) shutdown, or (c) error disabled.
up | down | notconnect | Not expected on LAN switch physical interfaces.
down | down (errdisabled) | err-disabled | Port security has disabled the interface.
up | up | connected | The interface is working.
  
  
Table end.
###### Table 7-3 Chapter Review Tracking
__|__|__
--|--|--
Review Element | Review Date(s) | Resource Used
Review key topics || Book, website
Review key terms || Book, website
Answer DIKTA questions || Book, PTP
Review command tables || Book
Review memory tables || Website
Do labs || Sim Lite, blog
Table end.
###### Table 7-5 Switch Interface Configuration
__|__
--|--
Command | Mode/Purpose/Description
interface type port-number | Changes context to interface mode. The type is typically Fast Ethernet or Gigabit Ethernet. The possible port numbers vary depending on the model of switch—for example, Fa0/1, Fa0/2, and so on.
interface range type portnumber - end-port-number | Changes the context to interface mode for a range of consecutively numbered interfaces. The subcommands that follow then apply to all interfaces in the range. Command Mode/Purpose/Description
shutdown no shutdown | Interface mode. Disables or enables the interface, respectively.
speed {10  100  1000  auto} | Interface mode. Manually sets the speed to the listed speed or, with the auto setting, automatically negotiates the speed.
duplex {auto  full  half} | Interface mode. Manually sets the duplex to half or full, or to autonegotiate the duplex setting.
description text | Interface mode. Lists any information text that the engineer wants to track for the interface, such as the expected device on the other end of the cable.
no duplex no speed no description | Reverts to the default setting for each interface subcommand of speed auto, duplex auto, and the absence of a description command.
  
  
Table end.
###### Table 7-6 Chapter 7 EXEC Command Reference
__|__
--|--
Command | Purpose
show running-config | Lists the currently used configuration
show running-config interface type number | Displays the running-configuration excerpt of the listed interface and its subcommands only
show mac address-table dynamic
interface type number vlan vlan-id | Lists the dynamically learned entries in the switch’s address (forwarding) table, with subsets by interface and/or VLAN
show mac address-table static interface type number | Lists static MAC addresses and MAC addresses learned or defined with port security
show interfaces type number status | Lists one output line per interface (or for only the listed interface if included), noting the description, operating state, and settings for duplex and speed on each interface show interfaces type number | Lists detailed status and statistical information about all interfaces (or the listed interface only)
show interfaces description | Displays one line of information per interface, with a two-item status (similar to the show interfaces command status), and includes any description that is configured on the interfaces
  
  
Table end.
Table 8-2 Trunking Administrative Mode Options with the switchport mode Command
__|__
--|--
Command Option | Description
access | Always act as an access (nontrunk) port
trunk | Always act as a trunk port
dynamic desirable | Initiates negotiation messages and responds to negotiation messages to dynamically choose whether to start using trunking
dynamic auto | Passively waits to receive trunk negotiation messages, at which point the switch will respond and negotiate whether to use trunking
  
  
Table end.
****** Table 8-3 Expected Trunking Operational Mode Based on the Configured Administrative Modes
__|__|__|__|__
--|--|--|--|--
Administrative Moden| Access | Dynamic Auto | Trunk | Dynamic Desirable
access | Access | Access | Do Not Use1 | Access
dynamic | auto | Access | Access | Trunk | Trunk
trunk | Do Not Use1 | Trunk | Trunk | Trunk
dynamic | desirable | Access | Trunk | Trunk | Trunk
  
  
Table end.
###### Table 8-4 VLAN Lists in the show interfaces trunk Command
__|__|__
--|--|--
List Position | Heading | Reasons
First | VLANs allowed | VLANs 1–4094, minus those removed by the switchport trunk allowed command
Second | VLANs allowed and active… | The first list, minus VLANs not defined to the local switch (that is, there is not a vlan global configuration command or the switch has not learned of the VLAN with VTP), and also minus those VLANs in shutdown mode
Third | VLANs in spanning tree… | The second list, minus VLANs in an STP blocking state for that interface, and minus VLANs VTP pruned from that trunk  
  
  
Table end.
###### Table 8-5 Chapter Review Tracking
__|__|__
--|--|--
Review Element | Review Date(s) | Resource Used
Review key topics || Book, website
Review key terms || Book, website
Answer DIKTA questions || Book, PTP
Review config checklists || Book, website
Review command tables || Book
Review memory tables || Website
Do labs || Sim Lite, blog
Watch video || Website
  
  
Table end.
###### Table 8-7 Chapter 8 Configuration Command Reference
__|__
--|--
Command | Description
vlan vlan-id | Global config command that both creates the VLAN and puts the CLI into VLAN configuration mode
name vlan-name | VLAN subcommand that names the VLAN 
(no) shutdown | VLAN mode subcommand that enables (no shutdown) or disables (shutdown) the VLAN
(no) shutdown vlan vlan-id | Global config command that has the same effect as the (no) shutdown VLAN mode subcommands
vtp mode {server  client  transparent  off} | Global config command that defines the VTP mode
switchport mode {access dynamic {auto  desirable}  trunk} | Interface subcommand that configures the trunking administrative mode on the interface switchport access vlan vlan-id | Interface subcommand that statically configures the interface into that one VLAN
switchport trunk encapsulation {dot1q  isl  negotiate} | Interface subcommand that defines which type of trunking to use, assuming that trunking is configured or negotiated 
switchport trunk native vlan vlanid | Interface subcommand that defines the native VLAN for a trunk port switchport nonegotiate | Interface subcommand that disables the negotiation of VLAN trunking 
switchport voice vlan vlan-id | Interface subcommand that defines the voice VLAN on a port, meaning that the switch uses 802.1Q tagging for frames in this VLAN
switchport trunk allowed vlan
{add  all  except  remove} vlanlist | Interface subcommand that defines the list of allowed
VLANs
  
  
Table end.
###### Table 8-8 Chapter 8 EXEC Command Reference
__|__
--|--
Command | Description
show interfaces interface-id switchport | Lists information about any interface regarding
administrative settings and operational state
show interfaces interface-id trunk | Lists information about all operational trunks (but no other interfaces), including the list of VLANs that can be forwarded over the trunk
show vlan (brief  id vlan-id  name vlan-name  summary) | Lists information about the VLAN
show vlan (vlan) | Displays VLAN information
show vtp status | Lists VTP configuration and status information
  
  
Table end.
###### Table 9-2 Three Classes of Problems Caused by Not Using STP in Redundant LANs
__|__
--|--
Problem | Description
Broadcast storms | The forwarding of a frame repeatedly on the same links, consuming significant parts of the links’ capacities
MAC table instability | The continual updating of a switch’s MAC address table with incorrect entries, in reaction to looping frames, resulting in frames being sent to the wrong locations
Multiple frame transmission | A side effect of looping frames in which multiple copies of one frame are delivered to the intended host, confusing the host
  
  
Table end.
###### Table 9-3 STP/RSTP: Reasons for Forwarding or Blocking
__|__|__
--|--|--
Characterization of Port | STP State | Description
All the root switch’s ports | Forwarding | The root switch is always the designated switch on all connected segments.
Each nonroot switch’s root port | Forwarding | The port through which the switch has the least cost to reach the root switch (lowest root cost).
Each LAN’s designated port | Forwarding | The switch forwarding the Hello on to the segment, with the lowest root cost, is the designated switch for that segment.
All other working ports | Blocking | The port is not used for forwarding user frames, nor are any frames received on these interfaces considered for forwarding.
  
  
Table end.
###### Table 9-4 Fields in the STP Hello BPDU
__|__
--|--
Field | Description
Root bridge ID | The bridge ID of the switch the sender of this Hello currently believes to be the root switch
Sender’s bridge ID | The bridge ID of the switch sending this Hello BPDU
Sender’s root cost | The STP/RSTP cost between this switch and the current root
Timer values on the root switch | Includes the Hello timer, MaxAge timer, and forward delay timer
  
  
Table end.
###### Table 9-5 State of Each Interface
__|__|__
--|--|--
Switch Interface | State | Reason Why the Interface Is in Forwarding State
SW1, Gi0/1 | Forwarding | The interface is on the root switch, so it becomes the DP on that link.
SW1, Gi0/2 | Forwarding | The interface is on the root switch, so it becomes the DP on that link.
SW2, Gi0/2 | Forwarding | The root port of SW2.
SW2, Gi0/1 | Forwarding | The designated port on the LAN segment to SW3.
SW3, Gi0/1 | Forwarding | The root port of SW3.
SW3, Gi0/2 | Blocking | Not the root port and not the designated port.
  
Table end.
##### Table 9-6 Default Port Costs According to IEEE
__|__|__
--|--|--
Ethernet Speed | IEEE Cost: 1998 (and Before) | IEEE Cost: 2004 (and After)
10 Mbps | 100 | 2,000,000
100 Mbps | 19 | 200,000
1 Gbps | 4 | 20,000
10 Gbps | 2 | 2000
100 Gbps | N/A | 200
1 Tbps | N/A | 20
  
Table end.
###### Table 9-7 STP Timers
__|__|__
--|--|--
Timer | Default Value | Description
Hello | 2 seconds | The time period between Hellos created by the root.
MaxAge | 10 times Hello | How long any switch should wait, after ceasing to hear Hellos, before trying to change the STP topology.
Forward delay | 15 seconds Delay that affects the process that occurs when an interface changes from blocking state to forwarding state. A port stays in an interim listening state, and then an interim learning state, for the number of seconds defined by the forward delay timer.
  
Table end.
###### Table 9-8 IEEE STP (Not RSTP) States
__|__|__|__
--|--|--|--
State | Forwards Data Frames? | Learns MACs Based on Received Frames? | Transitory or Stable State?
Blocking | No | No | Stable
Listening | No | No | Transitory
Learning | No | Yes | Transitory
Forwarding | Yes | Yes | Stable
Disabled | No | No | Stable
  
Table end.
###### Table 9-9 Port Roles in RSTP
__|__
--|--
Function | Port Role
Port that begins a nonroot switch’s best path to the root | Root port
Port that replaces the root port when the root port fails | Alternate port
Switch port designated to forward onto a collision domain | Designated port
Port that replaces a designated port when a designated port fails | Backup port
Port that is administratively disabled | Disabled port
  
Table end.
###### Table 9-10 Port States Compared: STP and RSTP
__|__|__
--|--|--
Function | STP State | RSTP State
Port is administratively disabled | Disabled | Discarding
Stable state that ignores incoming data frames and is not used to forward data frames | Blocking | Discarding
Interim state without MAC learning and without forwarding | Listening | Not used
Interim state with MAC learning and without forwarding Learning Learning Stable state that allows MAC learning and forwarding of data frames | Forwarding | Forwarding
  
Table end.
###### Table 9-11 Chapter Review Tracking
__|__|__
--|--|--
Review Element | Review Date(s) | Resource Used
Review key topics || Book, website
Review key terms || Book, website
Answer DIKTA questions || Book, PTP
Review memory tables || Website
  
Table end.
###### Table 10-2 STP Standards and Configuration Options
__|__|__|__|__
--|--|--|--|--
Name | Based on STP or RSTP? | Trees | Original IEEE Standard | Config Parameter
STP | STP | 1 (CST) | 802.1D | N/A
PVST+ | STP | 1/VLAN | 802.1D | pvst
RSTP | RSTP | 1 (CST) | 802.1w | N/A
Rapid | PVST+ | RSTP 1/VLAN | 802.1w | rapid-pvst
MSTP | RSTP | 1 or more1 | 802.1s | mst
  
Table end.
###### Table 10-3 STP/RSTP Configurable Priority Values
__|__|__|__
--|--|--|--
Decimal Value | 16-bit Binary Equivalent | Decimal Value | 16-bit Binary Equivalent
0 | 0000 0000 0000 0000 | 32768 | 1000 0000 0000 0000
4096 | 0001 0000 0000 0000 | 36864 | 1001 0000 0000 0000
8192 | 0010 0000 0000 0000 | 40960 | 1010 0000 0000 0000
12288 | 0011 0000 0000 0000 | 45056 | 1011 0000 0000 0000
16384 | 0100 0000 0000 0000 | 49152 | 1100 0000 0000 0000
20480 | 0101 0000 0000 0000 | 53248 | 1101 0000 0000 0000
24576 | 0110 0000 0000 0000 | 57344 | 1110 0000 0000 0000
28672 | 0111 0000 0000 0000 | 61440 | 1111 0000 0000 0000
  
Table end.
###### Table 10-4 EtherChannel Load Distribution Methods
__|__|__
--|--|--
Configuration Keyword | Math Uses… | Layer
src-mac | Source MAC address | 2
dst-mac | Destination MAC address | 2
src-dst-mac | Both source and destination MAC | 2
src-ip | Source IP address | 3
dst-ip | Destination IP address | 3
src-dst-ip | Both source and destination IP | 3
src-port | Source TCP or UDP port | 4
dst-port | Destination TCP or UDP port | 4
src-dst-port | Both source and destination TCP or UDP port | 4
  
Table end.
###### Table 10-5 Chapter Review Tracking
__|__|__
--|--|--
Review Element | Review Date(s) | Resource Used
Review key topics || Book, website
Review key terms || Book, website
Answer DIKTA questions || Book, PTP
Review config checklists || Book, website
Review command tables || Book
Review memory tables || Website
Do labs || Blog
  
Table end.
###### Table 10-7 Chapter 10 Configuration Command Reference
__|__
--|--
Command | Description
spanning-tree mode {pvst rapid-pvst mst} | Global configuration command to set the STP mode.
spanning-tree (vlan vlan-number) root primary | Global configuration command that changes this switch to the root switch. The switch’s priority is changed to the lower of either 24,576 or 4096 less than the priority of the current root bridge when the command was issued.
spanning-tree (vlan vlan-number) root secondary | Global configuration command that sets this switch’s STP base priority to 28,672.
spanning-tree vlan vlan-id priority priority | Global configuration command that changes the bridge priority of this switch for the specified VLAN.
spanning-tree (vlan vlan-number) cost cost | Interface subcommand that changes the STP cost to the configured value.
spanning-tree (vlan vlan-number) port-priority priority | Interface subcommand that changes the STP port priority in that VLAN (0 to 240, in increments of 16).
channel-group channel-groupnumber mode {auto  desirable  active passive  on} | Interface subcommand that enables EtherChannel on the interface.
  
Table end.
###### Table 10-8 Chapter 10 EXEC Command Reference
__|__
--|--
Command | Description
show spanning-tree | Lists details about the state of STP on the switch, including the state of each port.
show spanning-tree vlan vlan-id | Lists STP information for the specified VLAN.
show etherchannel (channel-groupnumber) {brief  detail  port  portchannel summary} | Lists information about the state of EtherChannels on this switch.
  
Table end.
###### Table 11-2 RFC 1918 Private Address Space
__|__|__
--|--|--
Class of Networks | Private IP Networks | Number of Networks
A | 10.0.0.0 | 1
B | 172.16.0.0 through 172.31.0.0 | 16
C | 192.168.0.0 through 192.168.255.0 | 256
  
Table end.
###### Table 11-3 First 10 Subnets, Plus the Last Few, from 172.16.0.0, 255.255.255.0
__|__|__
--|--|--
Subnet Number | IP Addresses | Broadcast Address
172.16.0.0 | 172.16.0.1 – 172.16.0.254 | 172.16.0.255
172.16.1.0 | 172.16.1.1 – 172.16.1.254 | 172.16.1.255
172.16.2.0 | 172.16.2.1 – 172.16.2.254 | 172.16.2.255
172.16.3.0 | 172.16.3.1 – 172.16.3.254 | 172.16.3.255
172.16.4.0 | 172.16.4.1 – 172.16.4.254 | 172.16.4.255
172.16.5.0 | 172.16.5.1 – 172.16.5.254 | 172.16.5.255
172.16.6.0 | 172.16.6.1 – 172.16.6.254 | | 172.16.6.255
172.16.7.0 | 172.16.7.1 – 172.16.7.254 | 172.16.7.255
172.16.8.0 | 172.16.8.1 – 172.16.8.254 | 172.16.8.255
172.16.9.0 | 172.16.9.1 – 172.16.9.254 | 172.16.9.255
Skipping many…
172.16.254.0 | 172.16.254.1 – 172.16.254.254 | 172.16.254.255
172.16.255.0 | 172.16.255.1 – 172.16.255.254 | 172.16.255.255
  
Table end.
###### Table 11-4 Chapter Review Tracking
__|__|__
--|--|--
Review Element | Review Date(s) | Resource Used
Review key topics | | Book, website
Review key terms | | Book, website
Answer DIKTA questions | | Book, PTP
Review memory tables | | Website
  
Table end.
###### Table 12-2 IPv4 Address Classes Based on First Octet Values
__|__|__
--|--|--
Class | First Octet Values | Purpose
A | 1–126 | Unicast (large networks)
B | 128–191 | Unicast (medium-sized networks)
C | 192–223 | Unicast (small networks)
D | 224–239 | Multicast
E | 240–255 | Reserved (formerly experimental)
  
Table end.
###### Table 12-3 Key Facts for Classes A, B, and C
__|__|__|__
--|--|--|--
_ |Class A | Class B | Class C
First octet range | 1–126 | 128–191 | 192–223
Valid network numbers | 1.0.0.0–126.0.0.0 | 128.0.0.0–191.255.0.0 | 192.0.0.0–223.255.255.0
Total networks | 27 – 2 = 126 | 214 = 16,384 | 221 = 2,097,152
Hosts per network | 224 – 2 | 216 – 2 | 28 – 2
Octets (bits) in network part | 1 (8) | 2 (16) | 3 (24)
Octets (bits) in host part | 3 (24) | 2 (16) | 1 (8)
Default mask | 255.0.0.0 | 255.255.0.0 | 255.255.255.0
  
Table end.
###### Table 12-4 Keep-Reading and Take-Exam Goals for This Chapter’s Topics
__|__|__
--|--|--
_ |After Reading This Chapter | Before Taking the Exam
Focus on… | Learning how | Being correct and fast
Tools Allowed | All | Your brain and a notepad
Goal: Accuracy | 90% correct | 100% correct
Goal: Speed | Any speed | 10 seconds
  
Table end.
###### Table 12-5 Practice Problems: Find the Network ID and Network Broadcast
__|__|__|__|__|__|__
--|--|--|--|--|--|--
IP Address | Class | Network Octets | Host Octets | Network ID | Network Broadcast Address
1 | 1.1.1.1
2 | 128.1.6.5
3 | 200.1.2.3
4 | 192.192.1.1
5 | 126.5.4.3
6 | 200.1.9.8
7 | 192.0.0.1
8 | 191.255.1.47
9 | 223.223.0.1
  
Table end.
###### Table 12-6 Sparse Study Table Version of Table 12-2
__|__|__
--|--|--
Class | First Octet Values | Purpose
A
B
C
D
E
  
Table end.
###### Table 12-7 Sparse Study Table Version of Table 12-3
 __|__|__|__
--|--|--|--
_|Class A | Class B | Class C
First octet range
Valid network numbers
Total networks
Hosts per network
Octets (bits) in network part
Octets (bits) in host part
Default mask
  
Table end.
###### Table 12-8 Chapter Review Tracking
__|__|__
--|--|--
Review Element | Review Date(s) | Resource Used
Review key topics | | Book, website
Review key terms | | Book, website
Answer DIKTA questions | | Book, PTP
Review memory tables | | Website
Practice analyzing classful IPv4 networks | | Website, Appendix D
  
Table end.
###### Table 12-10 Practice Problems: Find the Network ID and Network Broadcast
__|__|__|__|__|__|__
--|--|--|--|--|--|--
_ |IP Address Class | Network Octets | Host Octets | Network ID | Network Broadcast
1 | 1.1.1.1 | A | 1 | 3 | 1.0.0.0 | 1.255.255.255
2 | 128.1.6.5 | B | 2 | 2 | 128.1.0.0 | 128.1.255.255
3 | 200.1.2.3 | C | 3 | 1 | 200.1.2.0 | 200.1.2.255
4 | 192.192.1.1 | C | 3 | 1 | 192.192.1.0 | 192.192.1.255
5 | 126.5.4.3 | A | 1 | 3 | 126.0.0.0 | 126.255.255.255
6 | 200.1.9.8 | C | 3 | 1 | 200.1.9.0 | 200.1.9.255
7 | 192.0.0.1 | C | 3 | 1 | 192.0.0.0 | 192.0.0.255
8 | 191.255.1.47 | B | 2 | 2 | 191.255.0.0 | 191.255.255.255
9 | 223.223.0.1 | C | 3 | 1 | 223.223.0.0 | 223.223.0.255
  
Table end.
###### Table 13-2 Example Conversions: Binary to Prefix
__|__|__
--|--|--
Binary Mask | Logic | Prefix Mask
11111111 11111111 11000000 00000000 | Count 8 + 8 + 2 = 18 binary 1s | /18
11111111 11111111 11111111 11110000 | Count 8 + 8 + 8 + 4 = 28 binary 1s | /28
11111111 11111000 00000000 00000000 | Count 8 + 5 = 13 binary 1s | /13
  
Table end.
###### Table 13-3 Example Conversions: Prefix to Binary
__|__|__
--|--|--
Prefix Mask | Logic | Binary Mask
/18 | Write 18 1s, then 14 0s, total 32 | 11111111 11111111 11000000 00000000
/28 | Write 28 1s, then 4 0s, total 32 | 11111111 11111111 11111111 11110000
/13 | Write 13 1s, then 19 0s, total 32 | 11111111 11111000 00000000 00000000
  
Table end.
###### Table 13-4 Nine Possible Values in One Octet of a Subnet Mask
__|__|__
--|--|--
Binary Mask Octet | Decimal Equivalent | Number of Binary 1s
00000000 | 0 | 0
10000000 | 128 | 1
11000000 | 192 | 2
11100000 | 224 | 3
11110000 | 240 | 4
11111000 | 248 | 5
11111100 | 252 | 6
11111110 | 254 | 7
11111111 | 255 | 8
  
Table end.
###### Table 13-5 Conversion Example: Binary to Decimal
__|__|__
--|--|--
Binary Mask | Logic | Decimal Mask
11111111 11111111 11000000 00000000 | 11111111 maps to 255 11000000 maps to 192 00000000 maps to 0 | 255.255.192.0
11111111 11111111 11111111 11110000 | 11111111 maps to 255 11110000 maps to 240 | 255.255.255.240
11111111 11111000 00000000 00000000 | 11111111 maps to 255 11111000 maps to 248 00000000 maps to 0 | 255.248.0.0
  
Table end.
###### Table 13-6 Conversion Examples: Decimal to Binary
__|__|__
--|--|--
Decimal Mask | Logic | Binary Mask
255.255.192.0 | 255 maps to 11111111 192 maps to 11000000 0 maps to 00000000 | 11111111 11111111 11000000 00000000
255.255.255.240 | 255 maps to 11111111 240 maps to 11110000 | 11111111 11111111 11111111 11110000
255.248.0.0 | 255 maps to 11111111 248 maps to 11111000 0 maps to 00000000 | 11111111 11111000 00000000 00000000
  
Table end.
###### Table 13-7 Keep-Reading and Take-Exam Goals for This Chapter’s Topics
__|__|__
--|--|--
_ |Before Moving to the Next Section | Before Taking the Exam
Focus On… | Learning how | Being correct and fast
Tools Allowed | All | Your brain and a notepad
Goal: Accuracy | 90% correct | 100% correct
Goal: Speed | Any speed | 10 seconds
  
Table end.
###### Table 13-8 Practice Problems: Find the Mask Values in the Other Two Formats
__|__|__
--|--|--
Prefix | Binary Mask | Decimal
_ |11111111 11111111 11000000 00000000 | _
_ |_ |255.255.255.252
/25 | | 
/16 | |
_ |_ |255.0.0.0
_ |11111111 11111111 11111100 00000000 | _
_ |_ |255.254.0.0
/27 | _ | _
  
Table end.
###### Table 13-9 Keep-Reading and Take-Exam Goals for This Chapter’s Topics
__|__|__
--|--|--
_ | Before Moving to the Next Chapter | Before Taking the Exam
Focus On… | Learning how | Being correct and fast
Tools Allowed | All | Your brain and a notepad
Goal: Accuracy | 90% correct | 100% correct
Goal: Speed | Any speed | 15 seconds
  
Table end.
###### Table 13-10 Chapter Review Tracking
__|__|__
--|--|--
Review Element | Review Date(s) | Resource Used
Review key topics | | Book, website
Review key terms | | Book, website
Answer DIKTA questions | | Book, PTP
Review memory tables | | Website
Practice analyzing subnet masks | | Website, Appendix E
  
Table end.
###### Table 13-12 Answers to Problems in Table 13-8
__|__|__
--|--|--
Prefix Binary Mask Decimal
/18 | 11111111 11111111 11000000 00000000 | 255.255.192.0
/30 | 11111111 11111111 11111111 11111100 | 255.255.255.252
/25 | 11111111 11111111 11111111 10000000 | 255.255.255.128
/16 | 11111111 11111111 00000000 00000000 | 255.255.0.0
/8 | 11111111 00000000 00000000 00000000 | 255.0.0.0
/22 | 11111111 11111111 11111100 00000000 | 255.255.252.0
/15 | 11111111 11111110 00000000 00000000 | 255.254.0.0
/27 | 11111111 11111111 11111111 11100000 | 255.255.255.224
  
Table end.
###### Table 13-13 Answers to Problems from Earlier in the Chapter
__|__|__
--|--|--
_ |Problem | /P | Class | N | S | H | 2S | 2H – 2
1 | 8.1.4.5 255.255.254.0 | 23 | A | 8 | 15 | 9 | 32,768 510
2 | 130.4.102.1 255.255.255.0 | 24 | B | 16 | 8 | 8 | 256 | 254
3 | 199.1.1.100 255.255.255.0 | 24 | C | 24 | 0 | 8 | N/A | 254
4 | 130.4.102.1 255.255.252.0 | 22 | B | 16 | 6 | 10 | 64 | 1022
5 | 199.1.1.100 255.255.255.224 | 27 | C | 24 | 3 | 5 | 8 | 30
  
Table end.
###### Table 14-2 Summary of Subnet ID Key Facts
__|__
--|--
Definition | Number that represents the subnet
Numeric Value | First (smallest) number in the subnet
Literal Synonyms | Subnet number, subnet address, prefix, resident subnet
Common-Use Synonyms | Network, network ID, network number, network address
Typically Seen In… | Routing tables, documentation
  
Table end.
###### Table 14-3 Summary of Subnet Broadcast Address Key Facts
__|__
--|--
Definition | A reserved number in each subnet that, when used as the destination address of a packet, causes the device to forward the packet to all hosts in that subnet
Numeric Value | Last (highest) number in the subnet
Literal Synonyms | Directed broadcast address
Broader-Use Synonyms | Network broadcast
Typically Seen In… | In calculations of the range of addresses in a subnet
  
Table end.
###### Table 14-4 Subnet Analysis for Subnet with Address 8.1.4.5, Mask 255.255.0.0
__|__|__
--|--|--
Prefix Length | /16 | 11111111 11111111 00000000 00000000
Address | 8.1.4.5 | 00001000 00000001 00000100 00000101
Subnet ID | 8.1.0.0 | 00001000 00000001 00000000 00000000
Broadcast Address | 8.1.255.255 | 00001000 00000001 11111111 11111111
  
Table end.
Table 14-5 Subnet Analysis for Subnet with Address 130.4.102.1, Mask 255.255.255.0
__|__|__
--|--|--
Prefix Length | /24 | 11111111 11111111 11111111 00000000
Address | 130.4.102.1 | 10000010 00000100 01100110 00000001
Subnet ID | 130.4.102.0 | 10000010 00000100 01100110 00000000
Broadcast Address | 130.4.102.255 | 10000010 00000100 01100110 11111111
  
Table end.
###### Table 14-6 Subnet Analysis for Subnet with Address 199.1.1.100, Mask 255.255.255.0
__|__|__
--|--|--
Prefix Length | /24 | 11111111 11111111 11111111 00000000
Address | 199.1.1.100 | 11000111 00000001 00000001 01100100
Subnet ID | 199.1.1.0 | 11000111 00000001 00000001 00000000
Broadcast Address | 199.1.1.255 | 11000111 00000001 00000001 11111111
  
Table end.
###### Table 14-7 Subnet Analysis for Subnet with Address 130.4.102.1, Mask 255.255.252.0
__|__|__
--|--|--
Prefix Length | /22 | 11111111 11111111 11111100 00000000
Address | 130.4.102.1 | 10000010 00000100 01100110 00000001
Subnet ID | 130.4.100.0 | 10000010 00000100 01100100 00000000
Broadcast Address | 130.4.103.255 | 10000010 00000100 01100111 11111111
  
Table end.
###### Table 14-8 Subnet Analysis for Subnet with Address 199.1.1.100, Mask 255.255.255.224
__|__|__
--|--|--
Prefix Length | /27 | 11111111 11111111 11111111 11100000
Address | 199.1.1.100 | 11000111 00000001 00000001 01100100
Subnet ID | 199.1.1.96 | 11000111 00000001 00000001 01100000
Broadcast Address | 199.1.1.127 | 11000111 00000001 00000001 01111111
  
Table end.
###### Table 14-9 Practice Problems: Find Subnet ID and Broadcast Address, Easy Masks
__|__|__|__|__
--|--|--|--|--
_ | IP Address | Mask | Subnet ID | Broadcast Address
1 | 10.77.55.3 | 255.255.255.0
2 | 172.30.99.4 | 255.255.255.0
3 | 192.168.6.54 | 255.255.255.0
4 | 10.77.3.14 | 255.255.0.0
5 | 172.22.55.77 | 255.255.0.0
6 | 1.99.53.76 | 255.0.0.0
  
Table end.
###### Table 14-10 Practice Problems: Find Subnet ID, Difficult Masks
__|__|__|__
--|--|--|--
Problem | IP Address | Mask | Subnet ID
1 | 10.77.55.3 | 255.248.0.0
2 | 172.30.99.4 | 255.255.192.0
3 | 192.168.6.54 | 255.255.255.252
4 | 10.77.3.14 | 255.255.128.0
5 | 172.22.55.77 | 255.255.254.0
6 | 1.99.53.76 | 255.255.255.248
  
Table end.
###### Table 14-11 Keep-Reading and Take-Exam Goals for This Chapter’s Topics
__|__|__
--|--|--
_ | Before Moving to the Next Chapter | Before Taking the Exam
Focus On… | Learning how | Being correct and fast
Tools Allowed | All | Your brain and a notepad
Goal: Accuracy | 90% correct | 100% correct
Goal: Speed | Any speed | 20–30 seconds
  
Table end.
###### Table 14-12 Reference Table: DDN Mask Values, Binary Equivalent, Magic Numbers, and Prefixes
__|__|__|__|__|__|__|__|__
--|--|--|--|--|--|--|--|--
Prefix, interesting octet 2 | /9 | /10 | /11 | /12 | /13 | /14 | /15 | /16
Prefix, interesting octet 3 | /17 | /18 | /19 | /20 | /21 | /22 | /23 | /24
Prefix, interesting octet 4 | /25 | /26 | /27 | /28 | /29 | /30
Magic number | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1
DDN mask in the interesting octet | 128 | 192 | 224 | 240 | 248 | 252 | 254 | 255
   
Table end.
###### Table 14-13 Chapter Review Tracking
__|__|__
--|--|--
Review Element | Review Date(s) | Resource Used
Review key topics | | Book, website
Review key terms | | Book, website
Answer DIKTA questions | | Book, PTP
Review memory tables | | Website
Practice mask analysis | | Website, Appendix F
Practice analyzing existing subnets | | Website, Appendix F
  
Table end.
###### Table 14-15 Answers to Problems in Table 14-9
__|__|__|__|__
--|--|--|--|--
_ |IP Address | Mask | Subnet ID | Broadcast Address
1 | 10.77.55.3 | 255.255.255.0 | 10.77.55.0 | 10.77.55.255
2 | 172.30.99.4 | 255.255.255.0 | 172.30.99.0 | 172.30.99.255
3 | 192.168.6.54 | 255.255.255.0 | 192.168.6.0 | 192.168.6.255
4 | 10.77.3.14 | 255.255.0.0 | 10.77.0.0 | 10.77.255.255
5 | 172.22.55.77 | 255.255.0.0 | 172.22.0.0 | 172.22.255.255
6 | 1.99.53.76 | 255.0.0.0 | 1.0.0.0 | 1.255.255.255
  
Table end.
###### Table 14-16 Answers to Problems in Table 14-10
__|__|__|__
--|--|--|--
_ |IP Address | Mask | Subnet ID
1 | 10.77.55.3 | 255.248.0.0 | 10.72.0.0
2 | 172.30.99.4 | 255.255.192.0 | 172.30.64.0
3 | 192.168.6.54 | 255.255.255.252 | 192.168.6.52
4 | 10.77.3.14 | 255.255.128.0 | 10.77.0.0
5 | 172.22.55.77 | 255.255.254.0 | 172.22.54.0
6 | 1.99.53.76 | 255.255.255.248 | 1.99.53.72
  
Table end.
###### Table 14-17 Answers to Problems in the Section “Subnet Broadcast Address Practice Problems”
__|__|__|__
--|--|--|--
_ | Subnet ID | Mask | Broadcast Address
1 | 10.72.0.0 | 255.248.0.0 | 10.79.255.255
2 | 172.30.64.0 | 255.255.192.0 | 172.30.127.255
3 | 192.168.6.52 | 255.255.255.252 | 192.168.6.55
4 | 10.77.0.0 | 255.255.128.0 | 10.77.127.255
5 | 172.22.54.0 | | 255.255.254.0 | 172.22.55.255
6 | 1.99.53.72 | 255.255.255.248 | 1.99.53.79
  
Table end.
###### Table 15-2 Interface Status Codes and Their Meanings
__|__|__
--|--|--
Name | Location | General Meaning
Line status  | First status code | Refers to the Layer 1 status. (For example, is the cable installed, is it the right/wrong cable, is the device on the other end powered on?)
Protocol status | Second status code | Refers generally to the Layer 2 status. It is always down if the line status is down. If the line status is up, a protocol status of down is usually caused by a mismatched data-link layer configuration.
  
Table end.
###### Table 15-3 Typical Combinations of Interface Status Codes
__|__|__
--|--|--
Line Status | Protocol Status | Typical Reasons
Administratively down | Down | The interface has a shutdown command configured on it.
Down | Down | The interface is not shutdown, but the physical layer has a problem. For example, no cable has been attached to the interface, or with Ethernet, the switch interface on the other end of the cable is shut down, or the switch is powered off, or the devices on the ends of the cable use a different transmission speed.
Up | Down | Almost always refers to data-link layer problems, most often configuration problems. For example, serial links have this combination when one router was configured to use PPP and the other defaults to use HDLC.
Up | Up | Layer 1 and Layer 2 of this interface are functioning.
  
Table end.
###### Table 15-4 Key Commands to List Router Interface Status
__|__|__|__
--|--|--|--
Command | Lines of Output per Interface | IP Configuration Listed | Interface Status Listed?
show ip interface brief | 1 | Address | Yes
show protocols (type number) | 1 or 2 | Address/mask | Yes
show interfaces (type number) | Many | Address/mask | Yes
  
Table end.
###### Table 15-5 Chapter Review Tracking
__|__|__
--|--|--
Review Element | Review Date(s) | Resource Used
Review key topics | | Book, website
Review key terms | | Book, website
Answer DIKTA questions | | Book, PTP
Review command tables | | Book
Review memory tables | | Website
Do labs | | Blog
Watch video | | Website
  
Table end.
###### Table 15-7 Chapter 15 Configuration Command Reference
__|__
--|--
Command | Description
interface type number | Global command that moves the user into configuration mode of the named interface.
ip address address mask | Interface subcommand that sets the router’s IPv4 address and mask.
(no) shutdown | Interface subcommand that enables (no shutdown) or disables (shutdown) the interface.
duplex {full  half  auto} | Interface command that sets the duplex, or sets the use of IEEE autonegotiation, for router LAN interfaces that support multiple speeds.
speed {10  100  1000} | Interface command for router Gigabit (10/100/1000) interfaces that sets the speed at which the router interface sends and receives data.
description text | An interface subcommand with which you can type a string of text to document information about that particular interface.
  
Table end.
###### Table 15-8 Chapter 15 EXEC Command Reference
__|__
--|--
Command | Purpose
show interfaces (type number)  | Lists a large set of informational messages about each interface, or about the one specifically listed interface.
show ip interface brief | Lists a single line of information about each interface, including the IP address, line and protocol status, and the method with which the address was configured (manual or Dynamic Host Configuration Protocol (DHCP)).
show protocols (type number) | Lists information about the listed interface (or all interfaces if the interface is omitted), including the IP address, mask, and line/protocol status.
  
Table end.
###### Table 16-2 Analysis of Address Ranges for the Subnets in Example 16-8
__|__
--|--
Subnet/Prefix | Address Range
172.16.1.1/32 | 172.16.1.1 (just this one address)
172.16.1.0/24 | 172.16.1.0 – 172.16.1.255
172.16.0.0/22 | 172.16.0.0 – 172.16.3.255
172.16.0.0/16 | 172.16.0.0 – 172.16.255.255
0.0.0.0/0 | 0.0.0.0 – 255.255.255.255 (all addresses)
  
Table end.
###### Table 16-3 Descriptions of the show ip route Command Output
__|__|__|__
--|--|--|--
Item | Idea | Value in the Figure | Description
1 | Classful network | 10.0.0.0/8 | The routing table is organized by classful network. This line is the heading line for classful network 10.0.0.0; it lists the default mask for Class A networks (/8).
2 | Number of subnets | 13 subnets | The number of routes for subnets of the classful
network known to this router, from all sources, including local routes—the /32 routes that match each router interface IP address.
3 | Number of masks | 5 masks The number of different masks used in all routes known to this router inside this classful network.
4 | Legend code | C, L, O | A short code that identifies the source of the routing information. O is for OSPF, D for EIGRP, C for Connected, S for static, and L for local. (See Example 16-8 for a sample of the legend.)
5 | Prefix (Subnet ID) | 10.2.2.0 | The subnet number of this particular route.
6 | Prefix length (Mask) | /30 | The prefix mask used with this subnet.
7 | Administrative distance | 110  |If a router learns routes for the listed subnet from more than one source of routing information, the router uses the source with the lowest administrative distance (AD).
8 | Metric | 128 | The metric for this route.
9 | Next-hop router | 10.2.2.5 | For packets matching this route, the IP address of the next router to which the packet should be forwarded.
10 | Timer | 14:31:52 | For OSPF and EIGRP routes, this is the time since the route was first learned.
11 | Outgoing interface | Serial0/0/1 | For packets matching this route, the interface out which the packet should be forwarded.
  
Table end.
###### Table 16-4 Chapter Review Tracking
__|__|__
--|--|--
Review Element | Review Date(s) | Resource Used
Review key topics | | Book, website
Review key terms | | Book, website
Answer DIKTA questions | | Book, PTP
Review command tables | | Book
Do labs | | Blog
  
Table end.
###### Table 16-6 Chapter 16 Configuration Command Reference
__|__
--|--
Command | Description
ip address ip-address mask | Interface subcommand that assigns the interface’s IP address
interface type number.subint | Global command to create a subinterface and to enter configuration mode for that subinterface (no) ip routing | Global command that enables (ip routing) or disables (no ip routing) the routing of IPv4 packets on a router or Layer 3 switch
ip route prefix mask {ip-address  interface-type interface-number} (distance) (permanent) | Global configuration command that creates a static route
  
Table end.
###### Table 16-7 Chapter 16 EXEC Command Reference
__|__
--|--
Command | Description
show ip route | Lists the router’s entire routing table
show ip route (connected static  ospf) | Lists a subset of the IP routing table
show ip route ip-address | Lists detailed information about the route that a router matches for the listed IP address
show arp, show ip arp | Lists the router’s IPv4 ARP table
clear ip arp (ip-address) | Removes all dynamically learned ARP table entries, or if the command lists an IP address, removes the entry for that IP address only
  
Table end.
###### Table 17-2 Chapter Review Tracking
__|__|__
--|--|--
Review Element | Review Date(s) | Resource Used
Review key topics | | Book, website
Review key terms | | Book, website
Repeat DIKTA questions | | Book, PTP
Review config checklists | | Book, website
Review command tables | | Book
Do labs | | Blog
Watch video | | Website
  
Table end.
###### Table 17-4 Chapter 17 Configuration Command Reference
__|__|__
--|--|--
Command |  Description
interface type number.subint | Router global command to create a subinterface and to enter configuration mode for that subinterface
encapsulation dot1q vlan-id (native) | Router subinterface subcommand that tells the router to use 802.1Q trunking, for a particular VLAN, and with the native keyword, to not encapsulate in a trunking header
(no) ip routing | Global command that enables (ip routing) or disables (no ip routing) the routing of IPv4 packets on a router or Layer 3 switch
interface vlan vlan-id | A switch global command on a Layer 3 switch to create a VLAN interface and to enter configuration mode for that VLAN interface sdm prefer lanbase-routing | Command on some Cisco switches that reallocates forwarding chip memory to allow for an IPv4 routing table
(no) switchport | Layer 3 switch subcommand that makes the port act as a Layer 2 port (switchport) or Layer 3 routed port (no switchport)
interface port-channel channelnumber | A switch command to enter PortChannel configuration mode and also to create the PortChannel if not already created 
channel-group channel-number mode {auto / desirable / active / passive / on} | Interface subcommand that enables EtherChannel on the interface
  
Table end.
###### Table 17-5 Chapter 17 EXEC Command Reference
__|__|__
--|--|--
Command | Description
show ip route | Lists the router’s entire routing table
show ip route (connected) | Lists a subset of the IP routing table
show vlans | Lists VLAN configuration and statistics for VLAN trunks configured on routers
show interfaces (interface type number) | Lists detailed status and statistical information, including IP address and mask, about all interfaces (or the listed interface only)
show interfaces (interface type number) status | Among other facts, for switch ports, lists the access VLAN or the fact that the interface is a trunk; or, for routed ports, lists “routed”
show interfaces interface-id switchport | For switch ports, lists information about any interface regarding administrative settings and operational state; for routed ports, the output simply confirms the port is a
routed (not switched) port
show interfaces vlan number | Lists the interface status, the switch’s IPv4 address and mask, and much more 
show etherchannel (channelgroup-number) summary | Lists information about the state of EtherChannels on this switch, including whether the channel is a Layer 2 or Layer 3 EtherChannel
  
Table end.
###### Table 18-1 Chapter Review Tracking
__|__|__
--|--|--
Review Element | Review Date(s) | Resource Used
Review key topics | | Book, website
Review key terms | | Book, website
Watch video | | Website
  
Table end.
###### Table 19-2 IP IGP Metrics
__|__|__
--|--|--
IGP | Metric | Description
RIPv2 | Hop count | The number of routers (hops) between a router and the destination subnet
OSPF | Cost | The sum of all interface cost settings for all links in a route, with the cost defaulting to be based on interface bandwidth
EIGRP | Calculation based on
bandwidth and delay | Calculated based on the route’s slowest link and the cumulative delay associated with each interface in the route
  
Table end.
###### Table 19-3 Interior IP Routing Protocols Compared
__|__|__|__
--|--|--|--
Feature | RIPv2 | EIGRP | OSPF
Classless/sends mask in updates/supports VLSM | Yes | Yes | Yes
Algorithm (DV, advanced DV, LS) | DV | Advanced DV | LS
Supports manual summarization | Yes | Yes | Yes
Cisco-proprietary | No | Yes1 | No
Routing updates are sent to a multicast IP address | Yes | Yes | Yes
Convergence | Slow | Fast | Fast
  
Table end.
###### Table 19-4 Default Administrative Distances
__|__
--|--
Route Type | Administrative Distance
Connected | 0
Static | 1
BGP (external routes (eBGP)) | 20
EIGRP (internal routes) | 90
IGRP | 100
OSPF | 110
IS-IS | 115
RIP | 120
EIGRP (external routes) | 170
BGP (internal routes (iBGP)) | 200
DHCP default route | 254
Unusable | 255
  
Table end.
###### Table 19-5 Stable OSPF Neighbor States and Their Meanings
__|__|__
--|--|--
Neighbor State | Term for Neighbor | Term for Relationship
2-way | Neighbor | Neighbor Relationship
Full | Adjacent Neighbor Fully Adjacent Neighbor | Adjacency
  
Table end.
###### Table 19-6 Comparing R1’s Three Alternatives for the Route to 172.16.3.0/24
__|__|__
--|--|--
Route | Location in Figure 19-11 | Cumulative Cost
R1–R7–R8 | Left | 10 + 180 + 10 = 200
R1–R5–R6–R8 | Middle | 20 + 30 + 40 + 10 = 100
R1–R2–R3–R4–R8 | Right | 30 + 60 + 20 + 5 + 10 = 125
  
Table end.
###### Table 19-7 OSPF Design Terminology
__|__
--|--
Term | Description
Area Border Router (ABR) | An OSPF router with interfaces connected to the backbone area and to at least one other area
Backbone router | A router connected to the backbone area (includes ABRs)
Internal router | A router in one area (not the backbone area)
Area | A set of routers and links that shares the same detailed LSDB information, but not with routers in other areas, for better efficiency
Backbone area | A special OSPF area to which all other areas must connect—area 0
Intra-area route | A route to a subnet inside the same area as the router
Interarea route | A route to a subnet in an area of which the router is not a part
  
Table end.
###### Table 19-8 The Three OSPFv2 LSA Types Seen with a Multiarea OSPF Design
__|__|__|__
--|--|--|--
LSA Name | LSA Type | Primary Purpose | Contents of LSA
Router | 1 | Describe a router | RID, interfaces, IP address/mask,
current interface state (status)
Network | 2 | Describe a network that has a DR  | DR and BDR IP addresses, subnet ID, mask
Summary | 3 | Describe a subnet in another area | Subnet ID, mask, RID of ABR that advertises the LSA
  
Table end.
###### Table 20-2 Example OSPF network Commands on R3, with Expected Results
__|__|__
--|--|--
Command | Logic in Command | Matched Interfaces
network 10.1.0.0 0.0.255.255 | Match addresses that begin with 10.1 | G0/0.1 G0/0.2 G0/0/0 G0/1/0 G0/2/0
network 10.0.0.0 0.255.255.255 | Match addresses that begin with 10 | G0/0.1 G0/0.2 G0/0/0 G0/1/0 G0/2/0
network 0.0.0.0 255.255.255.255 | Match all addresses | G0/0.1 G0/0.2 G0/0/0 G0/1/0 G0/2/0
network 10.1.13.0 0.0.0.255 | Match addresses that begin with 10.1.13 | G0/1/0
network 10.1.13.1 0.0.0.0 | Match one address: 10.1.13.1 | G0/1/0
  
Table end.
###### Table 20-3 Faster Interfaces with Equal OSPF Costs
__|__|__|__
--|--|--|--
Interface | Interface Default Bandwidth (Kbps) | Formula (Kbps) | OSPF Cost
Serial | 1544 Kbps | 100,000 / 1544 | 64
Ethernet | 10,000 Kbps | 100,000 / 10,000 | 10
Fast Ethernet | 100,000 Kbps | 100,000/100,000 | 1
Gigabit Ethernet | 1,000,000 Kbps | 100,000/1,000,000 | 1
10 Gigabit Ethernet | 10,000,000 Kbps | 100,000/10,000,000 | 1
100 Gigabit Ethernet | 100,000,000 Kbps | 100,000/100,000,000 | 1
  
Table end.
###### Table 20-4 Chapter Review Tracking
__|__|__
--|--|--
Review Element | Review Date(s) | Resource Used:
Review key topics | | Book, website
Review key terms | | Book, website
Answer DIKTA questions | | Book, PTP
Review Config Checklists | | Book, website
Review command tables | | Book
Do labs | | Blog
  
Table end.
###### Table 20-6 Chapter 20 Configuration Command Reference
__|__
--|--
Command | Description
router ospf process-id | Router subcommand that enters OSPF configuration mode for the listed process.
network ip-address wildcardmask area area-id | Router subcommand that enables OSPF on interfaces matching the address/wildcard combination and sets the OSPF area.
ip ospf process-id area areanumber | Interface subcommand to enable OSPF on the interface and to assign the interface to a specific OSPF area.
ip ospf cost interface-cost | Interface subcommand that sets the OSPF cost associated with the interface.
bandwidth bandwidth | Interface subcommand that directly sets the interface bandwidth (Kbps).
auto-cost referencebandwidth number | Router subcommand that tells OSPF the numerator in the Reference_bandwidth / Interface_bandwidth formula used to calculate the OSPF cost based on the interface bandwidth.
router-id id | OSPF command that statically sets the router ID.
interface loopback number | Global command to create a loopback interface and to navigate to interface configuration mode for that interface.
maximum-paths number-ofpaths | Router subcommand that defines the maximum number of equal-cost routes that can be added to the routing table.
passive-interface type number | Router subcommand that makes the interface passive to OSPF, meaning that the OSPF process will not form neighbor relationships with neighbors reachable on that interface.
passive-interface default | OSPF subcommand that changes the OSPF default for interfaces to be passive instead of active (not passive).
no passive-interface type number | OSPF subcommand that tells OSPF to be active (not passive) on that interface or subinterface.
default-information originate (always) | OSPF subcommand to tell OSPF to create and advertise an OSPF default route, as long as the router has some default route (or to always advertise a default, if the always option is configured).
  
Table end.
###### Table 20-7 Chapter 20 EXEC Command Reference
__|__
--|--
Command | Description
show ip ospf | Lists information about the OSPF process running on the router, including the OSPF router ID, areas to which the router connects, and the number of interfaces in each area.
show ip ospf interface brief | Lists the interfaces on which the OSPF protocol is enabled (based on the network commands), including passive interfaces.
show ip ospf interface (type number) | Lists a long section of settings, status, and counters for OSPF operation on all interfaces, or on the listed interface, including the Hello and Dead Timers.
show ip protocols | Shows routing protocol parameters and current timer values.
  
Table end.
###### Table 21-2 Two OSPF Network Types and Key Behaviors
__|__|__
--|--|--
Network Type Keyword | Dynamically Discovers Neighbors | Uses a DR/BDR
broadcast | Yes | Yes
point-to-point | Yes | No
  
Table end.
###### Table 21-3 Neighbor Requirements for OSPF
__|__|__
--|--|--
Requirement | Required for OSPF | Neighbor Missing if Incorrect
Interfaces must be in an up/up state. | Yes | Yes
Access control lists (ACL) must not filter routing protocol messages. | Yes | Yes
Interfaces must be in the same subnet. | Yes | Yes
They must pass routing protocol neighbor authentication (if configured). | Yes | Yes
Hello and hold/dead timers must match. | Yes | Yes
Router IDs (RID) must be unique. | Yes | Yes
They must be in the same area. | Yes | Yes
OSPF process must not be shut down. | Yes | Yes
Neighboring interfaces must use same MTU setting. | Yes | No
Neighboring interfaces must use same OSPF network type. | Yes | No
  
Table end.
###### Table 21-4 OSPF Neighbor Requirements and the Best show/debug Commands
__|__
--|--
Requirement | Best show Command
Hello and dead timers must match. | show ip ospf interface
They must be in the same area. | show ip ospf interface brief
RIDs must be unique. | show ip ospf
They must pass any neighbor authentication. | show ip ospf interface
OSPF process must not be shut down. | show ip ospf, show ip ospf interface
  
Table end.
###### Table 21-5 Chapter Review Tracking
__|__|__
--|--|--
Review Element | Review Date(s) | Resource Used:
Review key topics | | Book, website
Review command tables | | Book
Review memory tables | | Website
Watch video | | Website
  
Table end.
###### Table 21-7 Chapter 21 Configuration Command Reference
__|__
--|--
Command | Description
ip ospf hello-interval seconds | Interface subcommand that sets the interval for periodic Hellos
ip ospf dead-interval number | Interface subcommand that sets the OSPF dead timer
passive-interface type number | Router subcommand, for both OSPF and EIGRP, that tells the routing protocol to stop sending Hellos and stop trying to discover neighbors on that interface
ip ospf priority value | Interface subcommand that sets the OSPF priority, used when electing a new DR or BDR
ip ospf network {broadcast / point-to-point} | Interface subcommand used to set the OSPF network type on the interface
(no) shutdown | An OSPF configuration mode command to disable (shutdown) or enable (no shutdown) the OSPF process
  
Table end.
###### Table 21-8 Chapter 21 show Command Reference
__|__
--|--
Command | Description
show ip protocols | Shows routing protocol parameters and current timer values, including an effective copy of the routing protocols’ network commands and a list of passive interfaces
show ip ospf interface brief | Lists the interfaces on which the OSPF protocol is enabled (based on the network commands), including passive interfaces
show ip ospf interface (type number) | Lists detailed OSPF settings for all interfaces, or the listed interface, including Hello and dead timers and OSPF area
show ip ospf neighbor | Lists neighbors and current status with neighbors, per interface
show ip ospf | Lists a group of messages about the OSPF process itself, listing the OSPF Router ID in the first line
show interfaces | Lists a long set of messages, per interface, that lists configuration, state, and counter information
  
Table end.
###### Table 22-2 IPv6 Routing Protocols
__|__|__
--|--|--
Routing Protocol | Defined By | Notes
RIPng (RIP next generation) | RFC | The “next generation” is a reference to a TV series, Star Trek: the Next Generation.
OSPFv3 (OSPF version 3) | RFC | The OSPF you have worked with for IPv4 is actually
OSPF version 2, so the new version for IPv6 is OSPFv3.
EIGRPv6 (EIGRP for IPv6) | Cisco | Cisco owns the rights to the EIGRP protocol, but Cisco also now publishes EIGRP as an informational RFC.
MP BGP-4 (Multiprotocol BGP version 4) | RFC | BGP version 4 was created to be highly extendable; IPv6 support was added to BGP version 4 through one such enhancement, MP BGP-4.
  
Table end.
###### Table 22-3 Hexadecimal/Binary Conversion Chart
__|__|__|__
--|--|--|--
Hex | Binary | Hex | Binary
0 | 0000 | 8 | 1000
1 | 0001 | 9 | 1001
2 | 0010 | A | 1010
3 | 0011 | B | 1011
4 | 0100 | C | 1100
5 | 0101 | D | 1101
6 | 0110 | E | 1110
7 | 0111 | F | 1111
  
Table end.
###### Table 22-4 IPv6 Address Abbreviation and Expansion Practice
__|__
--|--
Full | Abbreviation
2340:0000:0010:0100:1000:ABCD:0101:1010 |
_ |30A0:ABCD:EF12:3456:ABC:B0B0:9999:9009
2222:3333:4444:5555:0000:0000:6060:0707_
_ |3210::
210F:0000:0000:0000:CCCC:0000:0000:000D |
_ |34BA:B:B::20
FE80:0000:0000:0000:DEAD:BEFF:FEEF:CAFE |
_ |FE80::FACE:BAFF:FEBE:CAFE
  
Table end.
###### Table 22-5 Finding the IPv6 Prefix from an Address/Length Value
__|__
--|--
Address/Length | Prefix
2340:0:10:100:1000:ABCD:101:1010/64
30A0:ABCD:EF12:3456:ABC:B0B0:9999:9009/64
2222:3333:4444:5555::6060:707/64
3210::ABCD:101:1010/64
210F::CCCC:B0B0:9999:9009/64
34BA:B:B:0:5555:0:6060:707/64
3124::DEAD:CAFE:FF:FE00:1/64
2BCD::FACE:BEFF:FEBE:CAFE/64
  
Table end.
###### Table 22-6 Finding the IPv6 Prefix from an Address/Length Value
__|__
--|--
Address/Length | Prefix
34BA:B:B:0:5555:0:6060:707/80
3124::DEAD:CAFE:FF:FE00:1/80
2BCD::FACE:BEFF:FEBE:CAFE/48
3FED:F:E0:D00:FACE:BAFF:FE00:0/48
210F:A:B:C:CCCC:B0B0:9999:9009/40
34BA:B:B:0:5555:0:6060:707/36
3124::DEAD:CAFE:FF:FE00:1/60
2BCD::FACE:1:BEFF:FEBE:CAFE/56
   
Table end.
###### Table 22-7 Chapter Review Tracking
__|__|__
--|--|--
Review Element | Review Date(s) | Resource Used
Review key topics | Book, website
Review key terms | Book, website
Repeat DIKTA questions | Book, PTP
Review command tables | Book
Review memory table | Book, website
  
Table end.
###### Table 22-8 Key Topics for Chapter 22
__|__|__
--|--|--
Key Topic Element | Description | Page Number
List | Similarities between IPv4 and IPv6 | 527
List | Rules for abbreviating IPv6 addresses | 531
List | Rules for expanding an abbreviated IPv6 address | 532
List | Process steps to find an IPv6 prefix, based on the IPv6 address and prefix length | 533
  
Table end.
###### Table 22-9 Answers to Questions in the Earlier Table 22-4
__|__
--|--
Full | Abbreviation
2340:0000:0010:0100:1000:ABCD:0101:1010 | 2340:0:10:100:1000:ABCD:101:1010
30A0:ABCD:EF12:3456:0ABC:B0B0:9999:9009 | 30A0:ABCD:EF12:3456:ABC:B0B0:9999:9009
2222:3333:4444:5555:0000:0000:6060:0707 | 2222:3333:4444:5555::6060:707
3210:0000:0000:0000:0000:0000:0000:0000 | 3210::
210F:0000:0000:0000:CCCC:0000:0000:000D | 210F::CCCC:0:0:D
34BA:000B:000B:0000:0000:0000:0000:0020 | 34BA:B:B::20
FE80:0000:0000:0000:DEAD:BEFF:FEEF:CAFE | FE80::DEAD:BEFF:FEEF:CAFE
FE80:0000:0000:0000:FACE:BAFF:FEBE:CAFE | FE80::FACE:BAFF:FEBE:CAFE
  
Table end.
###### Table 22-10 Answers to Questions in the Earlier Table 22-5
__|__
--|--
Address/Length | Prefix
2340:0:10:100:1000:ABCD:101:1010/64 | 2340:0:10:100::/64
30A0:ABCD:EF12:3456:ABC:B0B0:9999:9009/64 | 30A0:ABCD:EF12:3456::/64
2222:3333:4444:5555::6060:707/64 | 2222:3333:4444:5555::/64
3210::ABCD:101:1010/64 | 3210::/64
210F::CCCC:B0B0:9999:9009/64 | 210F::/64
34BA:B:B:0:5555:0:6060:707/64 | 34BA:B:B::/64
3124::DEAD:CAFE:FF:FE00:1/64 | 3124:0:0:DEAD::/64
2BCD::FACE:BEFF:FEBE:CAFE/64 | 2BCD::/64
  
Table end.
###### Table 22-11 Answers to Questions in the Earlier Table 22-6
__|__
--|--
Address/Length | Prefix
34BA:B:B:0:5555:0:6060:707/80 | 34BA:B:B:0:5555::/80
3124::DEAD:CAFE:FF:FE00:1/80 | 3124:0:0:DEAD:CAFE::/80
2BCD::FACE:BEFF:FEBE:CAFE/48 | 2BCD::/48
3FED:F:E0:D00:FACE:BAFF:FE00:0/48 | 3FED:F:E0::/48
210F:A:B:C:CCCC:B0B0:9999:9009/40 | 210F:A::/40
34BA:B:B:0:5555:0:6060:707/36 | 34BA:B::/36
3124::DEAD:CAFE:FF:FE00:1/60 | 3124:0:0:DEA0::/60
2BCD::FACE:1:BEFF:FEBE:CAFE/56 | 2BCD:0:0:FA00::/56
  
Table end.
###### Table 23-2 Some Types of IPv6 Addresses and Their First Hex Digit(s)
__|__
--|--
Address Type | First Hex Digits
Global unicast | 2 or 3 (originally); all not otherwise reserved (today)
Unique local | FD
Multicast | FF
Link local | FE80
  
Table end.
###### Table 23-3 Chapter Review Tracking
__|__|__
--|--|--
Review Element | Review Date(s) | Resource Used
Review key topics | | Book, website
Review key terms | | Book, website
Answer DIKTA questions | | Book, PTP
Review memory table | | Website
  
Table end.
###### Table 24-2 IPv6 EUI-64 Address Creation Practice
__|__|__
--|--|--
Prefix | MAC Address | Unabbreviated IPv6 Address
2001:DB8:1:1::/64 | 0013.ABAB.1001
2001:DB8:1:1::/64 | AA13.ABAB.1001
2001:DB8:1:1::/64 | 000C.BEEF.CAFE
2001:DB8:1:1::/64 | B80C.BEEF.CAFE
2001:DB8:FE:FE::/64 | 0C0C.ABAC.CABA
2001:DB8:FE:FE::/64 | 0A0C.ABAC.CABA
  
Table end.
###### Table 24-3 Key IPv6 Local-Scope Multicast Addresses
__|__|__|__
--|--|--|--
Short Name | Multicast Address | Meaning | IPv4 Equivalent
All-nodes | FF02::1 | All-nodes (all interfaces that use IPv6 that are on the link) | 224.0.0.1
All-routers | FF02::2 | All-routers (all IPv6 router interfaces on the link) | 224.0.0.2
All-OSPF, All-OSPF-DR | FF02::5, FF02::6 | All OSPF routers and all OSPF-designated routers, respectively | 224.0.0.5, 224.0.0.6
RIPng Routers | FF02::9 | All RIPng routers | 224.0.0.9
EIGRPv6 Routers | FF02::A | All routers using EIGRP for IPv6 (EIGRPv6) | 224.0.0.10
DHCP Relay Agent | FF02::1:2 | All routers acting as a DHCPv6 relay agent | None
  
Table end.
###### Table 24-4 IPv6 Multicast Scope Terms
__|__|__|__
--|--|--|--
Scope Name | First Quartet | Scope Defined by… | Meaning
Interface-Local | FF01 | Derived by Device Packet remains within the device. Useful for internally sending packets to services running on that same host.
Link-Local | FF02 | Derived by Device Host that creates the packet can send it onto the link, but no routers forward the packet.
Site-Local | FF05 | Configuration on Routers Intended to be more than Link-Local, so routers forward, but must be less than Organization-Local; generally meant to limit packets so they do not cross WAN links.
Organization-Local | FF08 | Configuration on Routers Intended to be broad, probably for an entire company or organization. Must be broader than Site-Local.
Global | FF0E | No Boundaries No boundaries.
  
Table end.
###### Table 24-5 Summary of IPv6 Address Types and the Commands That Create Them
__|__|__
--|--|--
Type | Prefix/Address Notes | Enabled with What Interface Subcommand
Global unicast | Many prefixes | ipv6 address address/prefix-length ipv6 address prefix/prefix-length eui-64
Unique Local | FD00::/8 | ipv6 address prefix/prefix-length eui-64
Link local | FE80::/10 | ipv6 address address link-local Autogenerated by all ipv6 address commands Autogenerated by the ipv6 enable command
All hosts multicast | FF02::1 | Autogenerated by all ipv6 address commands
All routers multicast | FF02::2 | Autogenerated by all ipv6 address commands
Routing protocol multicasts | Various | Added to the interface when the corresponding routing protocol is enabled on the interface
Solicited-node multicast | FF02::1:FF /104 | Autogenerated by all ipv6 address commands
  
Table end.
###### Table 24-6 Chapter Review Tracking
__|__|__
--|--|--
Review Element | Review Date(s) | Resource Used
Review key topics | | Book, website
Review key terms | | Book, website
Answer DIKTA questions | | Book, PTP
Review command tables | | Book
Review memory tables | | Website
Do labs | | Blog
Watch video | | Website
  
Table end.
###### Table 24-8 Chapter 24 Configuration Command Reference
__|__
--|--
Command | Description
ipv6 unicast-routing | Global command that enables IPv6 routing on the router.
ipv6 address ipv6-address/ prefix-length (eui-64) | Interface subcommand that manually configures either the entire interface IP address or a /64 prefix with the router building the EUI-64 format interface ID automatically.
ipv6 address ipv6-address/ prefix-length (anycast) | Interface subcommand that manually configures an address to be used as an anycast address.
ipv6 enable | Command that enables IPv6 on an interface and generates a linklocal address.
ipv6 address dhcp | Interface subcommand that enables IPv6 on an interface, causes the router to use DHCP client processes to try to lease an IPv6 address, and creates a link-local address for the interface.
  
Table end.
###### Table 24-9 Chapter 24 EXEC Command Reference
__|__
--|--
Command | Description
show ipv6 route (connected) (local) Lists IPv6 routes, or just the connected routes, or just the local routes.
show ipv6 interface (type number) | Lists IPv6 settings on an interface, including link-local and other unicast IP addresses (or for the listed interface).
show ipv6 interface brief (type number) | Lists interface status and IPv6 addresses for each interface (or for the listed interface).
  
Table end.
###### Table 24-10 Answers to IPv6 EUI-64 Address Creation Practice
__|__|__
--|--|--
Prefix | MAC Address | Unabbreviated IPv6 Address
2001:DB8:1:1::/64 | 0013.ABAB.1001 | 2001:DB8:1:1:0213:ABFF:FEAB:1001
2001:DB8:1:1::/64 | AA13.ABAB.1001 | 2001:DB8:1:1:A813:ABFF:FEAB:1001
2001:DB8:1:1::/64 | 000C.BEEF.CAFE | 2001:DB8:1:1:020C:BEFF:FEEF:CAFE
2001:DB8:1:1::/64 | B80C.BEEF.CAFE | 2001:DB8:1:1:BA0C:BEFF:FEEF:CAFE
2001:DB8:FE:FE::/64 | 0C0C.ABAC.CABA | 2001:DB8:FE:FE:0E0C:ABFF:FEAC:CABA
2001:DB8:FE:FE::/64 | 0A0C.ABAC.CABA | 2001:DB8:FE:FE:080C:ABFF:FEAC:CABA
  
Table end.
###### Table 25-2 IOS Defaults for Administrative Distance
__|__
--|--
Route Source | Administrative Distance
Connected routes | 0
Static routes | 1
NDP | 2
EIGRP | 90
OSPF | 110
RIP | 120
Unknown or unbelievable | 255
  
Table end.
###### Table 25-3 NDP Function Summary
__|__|__|__|__
--|--|--|--|--
Function | Protocol Messages | Who Discovers Info | Who Supplies Info | Info Supplied
Router discovery | RS and RA | Any IPv6 host | Any IPv6 router | Link-local IPv6 address of router
Prefix/length discovery | RS and RA | Any IPv6 host | Any IPv6 router | Prefix(es) and associated prefix lengths used on local link
Neighbor discovery | NS and NA | Any IPv6 host | Any IPv6 host | Link-layer address (for example, MAC address) used by a neighbor
Duplicate Address Detection | NS and NA | Any IPv6 host | Any IPv6 host | Simple confirmation whether a unicast address is already in use
  
Table end.
###### Table 25-4 Chapter Review Tracking
__|__|__
--|--|--
Review Element | Review Date(s) | Resource Used
Review key topics | | Book, website
Answer DIKTA questions | | Book, PTP
Review command tables | | Book
Review memory tables | | Book, website
Do labs | | Blog
  
Table end.
###### Table 25-6 Chapter 25 Configuration Command Reference
__|__
--|--
Command | Description
ipv6 route prefix/length nexthop-address | Global command to define an IPv6 static route to a nexthop router IPv6 address.
ipv6 route prefix/length outgoing-interface | Global command to define an IPv6 static route, with packets forwarded out the local router interface listed in the command.
ipv6 route prefix/length outgoing-interface next-hopaddress | Global command to define an IPv6 static route, with both the next-hop address and local router outgoing interface listed.
ipv6 route ::/0 {(next-hopaddress) (outgoing-interface)} | Global command to define a default IPv6 static route.
ipv6 address autoconfig (default) | Interface subcommand that tells the router to use SLAAC to find/build its own interface IPv6 address, and with the default parameter, to add a default route with a next hop of the router that responds with the RA message.
  
Table end.
###### Table 25-7 Chapter 25 EXEC Command Reference
__|__
--|--
Command | Description
show ipv6 route (connected / local / static) | Lists routes in the routing table.
show ipv6 route address | Displays detailed information about the route this router uses to forward packets to the IPv6 address listed in the command.
show ipv6 neighbors | Lists the contents of the IPv6 neighbor table, which lists the MAC address associated with IPv6 addresses on common subnets.
  
Table end.
###### Table 26-2 Frequency Unit Names
__|__|__
--|--|--
Unit | Abbreviation | Meaning
Hertz | Hz | Cycles per second
Kilohertz | kHz | 1000 Hz
Megahertz | MHz | 1,000,000 Hz
Gigahertz | GHz | 1,000,000,000 Hz
  
Table end.
###### Table 26-3 Basic Characteristics of Some IEEE 802.11 Amendments
__|__|__|__|__
--|--|--|--|--
Amendment | 2.4 GHz | 5 GHz | Max Data Rate | Notes
802.11-1997 | Yes | No | 2 Mbps | The original 802.11 standard ratified in 1997
802.11b | Yes | No | 11 Mbps | Introduced in 1999
802.11g | Yes | No | 54 Mbps | Introduced in 2003
802.11a | No | Yes | 54 Mbps | Introduced in 1999
802.11n | Yes | Yes | 600 Mbps | HT (high throughput), introduced in 2009
802.11ac | No | Yes | 6.93 Gbps | VHT (very high throughput), introduced in 2013
802.11ax | Yes | Yes | 4x 802.11ac | High Efficiency Wireless, Wi-Fi6; expected late 2019; will operate on other bands too, as they become available
  
Table end.
###### Table 26-4 Chapter Review Tracking
__|__|__
--|--|--
Review Element | Review Date(s) | Resource Used
Review key topics | | Book, website
Review key terms | | Book, website
Answer DIKTA questions | | Book, PTP
Review memory tables | | Website
  
Table end.
###### Table 27-2 Summary of WLC Deployment Models
__|__|__|__|__
--|--|--|--|--
Deployment Model | WLC Location (DC, Access, Central, AP) | APs Supported | Clients Supported | Typical Use
Unified | Central | 6000 | 64,000 | Large enterprise
Cloud | DC | 3000 | 32,000 | Private cloud
Embedded | Access | 200 | 4000 | Small campus
Mobility Express | Other | 100 | 2000 | Branch location
Autonomous | N/A | N/A | N/A | N/A
  
Table end.
###### Table 27-3 Chapter Review Tracking
__|__|__
--|--|--
Review Element | Review Date(s) | Resource Used
Review key topics | | Book, website
Review key terms | | Book, website
Answer DIKTA questions | | Book, PTP
Review memory tables | | Website
  
Table end.
###### Table 28-2 Comparing WPA, WPA2, and WPA3
__|__|__|__
--|--|--|--
Authentication and Encryption Feature Support | WPA | WPA2 | WPA3*
Authentication with Pre-Shared Keys? | Yes | Yes | Yes
Authentication with 802.1x? | Yes | Yes | Yes
Encryption and MIC with TKIP? | Yes | No | No
Encryption and MIC with AES and CCMP? | Yes | Yes | No
Encryption and MIC with AES and GCMP? | No | No | Yes
  
Table end.
###### Table 28-3 Review of Wireless Security Mechanisms and Options
__|__|__|__
--|--|--|--
Security Mechanism | Type | Type Expansion | Credentials Used
Authentication Methods | Open | Open Authentication | None, other than 802.11 protocol
Authentication Methods | WEP | Wired Equivalent Privacy | Static WEP keys
Authentication Methods | 802.1x/EAP (Extensible Authentication Protocol) | LEAP | Lightweight EAP | Deprecated; uses dynamic WEP keys
Authentication Methods | 802.1x/EAP (Extensible Authentication Protocol) | EAP-FAST EAP Flexible Authentication by Secure Tunneling | Uses protected access credential (PAC)
Authentication Methods | 802.1x/EAP (Extensible Authentication Protocol) | PEAP | Protected EAP AS authenticated by digital certificate
Authentication Methods | 802.1x/EAP (Extensible Authentication Protocol) | EAP-TLS EAP Transport Layer Security |  Client and AS authenticated by digital certificate
Privacy & Integrity Methods | TKIP | TKIP | Temporal Key Integrity Protocol |  N/A
Privacy & Integrity Methods | CCMP | Counter/CBC-MAC Protocol | N/A
Privacy & Integrity Methods | GCMP | Galois/Counter Mode Protocol | N/A
  
Table end.
###### Table 28-4 Chapter Review Tracking
Review Element Review Date(s) Resource Used
Review key topics Book, website
Review key terms Book, website
Answer DIKTA questions Book, PTP
Review memory tables Website
Table end.
###### Table 29-2 Layer 2 WLAN Security Type
Option Description
None Open authentication
WPA+WPA2 Wi-Fi protected access WPA or WPA2
802.1x EAP authentication with dynamic WEP
Static WEP WEP key security
Static WEP + 802.1x EAP authentication or static WEP
CKIP Cisco Key Integrity Protocol
None + EAP Passthrough Open authentication with remote EAP authentication
Table end.
###### Table 29-3 Chapter Review Tracking
Review Element Review Date(s) Resource Used
Review key topics Book, website
Review key terms Book, website
Answer DIKTA questions Book, PTP
Table end.
