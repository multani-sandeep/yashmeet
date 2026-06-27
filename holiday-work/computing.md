# Computing — Holiday Learning Plan (SECONDARY)

**Year 9 result:** Not examined in Y9 mocks (not in mock timetable)  
**Exam Board:** GCSE Computer Science (likely OCR or AQA — confirm with school)  
**Priority:** Secondary. One session per week. Goal is to build the GCSE foundation so Y10 content is not a cold start.

---

## GCSE Computer Science — Core Topics

### 1. Binary and Data Representation

**Binary:** base-2 number system (digits are 0 or 1)

**Converting binary to denary:**
128 · 64 · 32 · 16 · 8 · 4 · 2 · 1 (column values)

Example: 10110010 = 128 + 32 + 16 + 2 = **178**

**Converting denary to binary:**
Divide repeatedly by 2, read remainders upward.
178 ÷ 2 = 89 r 0 · 89 ÷ 2 = 44 r 1 · 44 ÷ 2 = 22 r 0 · 22 ÷ 2 = 11 r 0 · 11 ÷ 2 = 5 r 1 · 5 ÷ 2 = 2 r 1 · 2 ÷ 2 = 1 r 0 · 1 ÷ 2 = 0 r 1
Read upwards: **10110010**

**Binary addition:** same as denary, but 1+1 = 10 (carry the 1)

**Hexadecimal (base 16):** 0–9, then A=10, B=11, C=12, D=13, E=14, F=15
- Used to represent binary more compactly (each hex digit = 4 binary bits)
- Convert: split binary into groups of 4 → convert each group to hex

**Data sizes:** 1 bit → 1 nibble (4 bits) → 1 byte (8 bits) → 1 KB (1024 bytes) → 1 MB → 1 GB → 1 TB

**Text representation:** ASCII assigns a number to each character (e.g. A = 65). Unicode extends this to cover all world languages.

**Image representation:** pixels; bit depth (bits per pixel → more bits = more colours); resolution (pixels per inch)

**Sound representation:** sample rate (samples per second); bit depth (bits per sample); higher values = better quality but larger file size

---

### 2. Algorithms and Problem Solving

**Algorithm:** a step-by-step set of instructions to solve a problem.

**Flowcharts:** use standard symbols
- Oval: start/stop
- Rectangle: process (action)
- Diamond: decision (yes/no)
- Parallelogram: input/output
- Arrow: flow direction

**Pseudocode:** informal but structured language to describe an algorithm (not a real programming language, but follows logic rules).

Example:
```
total ← 0
FOR i ← 1 TO 10
    total ← total + i
NEXT i
OUTPUT total
```

**Search algorithms:**
- **Linear search:** check each element one by one from the start → works on unsorted lists; O(n)
- **Binary search:** check the middle element, discard half, repeat → requires sorted list; much faster for large lists; O(log n)

**Sort algorithms:**
- **Bubble sort:** compare adjacent pairs, swap if out of order, repeat passes → simple but slow for large lists
- **Merge sort:** recursively split list in half, sort each half, merge → fast but uses more memory
- **Insertion sort:** pick next element, insert it in correct position in sorted section → efficient for nearly-sorted lists

**Computational thinking:**
- Decomposition: break a problem into smaller parts
- Abstraction: remove unnecessary detail, focus on what matters
- Pattern recognition: identify similarities across problems
- Algorithm design: create a step-by-step solution

---

### 3. Programming Concepts

Review these core concepts — they apply in any language (Python is common at GCSE).

| Concept | Description | Example |
|---|---|---|
| Variable | Named storage location | name = "Yashmeet" |
| Constant | Value that doesn't change | PI = 3.14159 |
| Sequence | Instructions executed in order | Line by line |
| Selection | IF/ELSE branching | if score > 50: print("Pass") |
| Iteration | WHILE or FOR loops | for i in range(10): |
| Procedure | Named block of code, no return value | def greet(): |
| Function | Named block that returns a value | def square(n): return n*n |
| Parameter | Value passed into a function | square(5) |
| Array/List | Ordered collection of values | scores = [75, 80, 92] |

**String manipulation:** length, concatenation, substring, upper/lower case conversion  
**File handling:** open, read, write, close  
**Error types:** syntax error (typo in code); logic error (code runs but gives wrong answer); runtime error (crashes during execution)

---

### 4. Networks and the Internet

**Types of network:**
- **LAN (Local Area Network):** small geographic area (school, home); uses ethernet cables or Wi-Fi
- **WAN (Wide Area Network):** large geographic area; the internet is the largest WAN

**Network hardware:**
- **Router:** directs data packets between networks; connects LAN to the internet
- **Switch:** connects devices within a LAN; directs data to the correct device
- **NIC (Network Interface Card):** allows a device to connect to a network

**Network topologies:**
- **Bus:** all devices on one cable; cheap but single point of failure
- **Star:** all devices connect to a central switch; most common; failure of one device doesn't affect others
- **Ring:** devices in a circle; data travels in one direction

**The internet:** a global network of networks. Uses the Internet Protocol (IP) to route data.
- **IP address:** unique numerical label for each device (IPv4: 192.168.1.1; IPv6: longer, 128-bit)
- **DNS (Domain Name System):** translates domain names (google.com) into IP addresses
- **HTTP/HTTPS:** protocol for transferring web pages (S = encrypted with SSL/TLS)
- **Packet switching:** data is split into packets, sent by different routes, reassembled at destination

**Wireless networking:** Wi-Fi uses radio waves; Bluetooth for short-range device communication

---

### 5. Cyber Security

**Common threats:**
- **Phishing:** fake emails/websites to steal login credentials
- **Malware:** malicious software — viruses, worms, trojans, ransomware, spyware
- **Brute force attack:** trying every possible password combination
- **SQL injection:** inserting malicious code into a database query via a form field
- **DDoS (Distributed Denial of Service):** flooding a server with requests to make it crash

**Defences:**
- Strong passwords (length + complexity + uniqueness per site)
- Two-factor authentication (2FA)
- Encryption: data scrambled so only authorised parties can read it
- Firewall: monitors and filters network traffic
- Regular software updates: patch known vulnerabilities
- Penetration testing: ethical hacking to find vulnerabilities before attackers do

**Encryption basics:**
- **Symmetric encryption:** same key to encrypt and decrypt (fast; problem: how to share the key?)
- **Asymmetric encryption (public/private key):** public key encrypts, private key decrypts; used in HTTPS

---

## Suggested Session Focus by Week

| Week | Topic |
|---|---|
| 1 (8–14 Jul) | Binary: convert denary ↔ binary; binary addition; hexadecimal |
| 2 (15–21 Jul) | Algorithms: flowcharts, pseudocode, linear and binary search |
| 3 (22–28 Jul) | Sorting algorithms: bubble sort, merge sort (trace through an example by hand) |
| 4 (29 Jul–2 Aug) | Programming concepts: write or trace small pseudocode programs |
| 5 (4–10 Aug) | Networks: LAN/WAN, hardware, topologies, how the internet works |
| 6 (11–17 Aug) | Cyber security: threats and defences; encryption basics |
| 7 (18–24 Aug) | Mixed GCSE Computer Science past paper questions |
