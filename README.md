# 🚀 ARP Handling in SDN Networks using Mininet and Ryu Controller

---

## 📌 1. Project Overview

This project demonstrates the implementation of **Address Resolution Protocol (ARP) handling in Software Defined Networking (SDN)** using the **Ryu controller** and **Mininet emulator**.

Traditional networks rely on distributed control, whereas SDN centralizes control logic, enabling programmable and flexible networking.

This project showcases:

* ARP packet handling using controller
* Dynamic flow rule installation
* Controlled communication (allow/block)
* Performance analysis using ping and iperf

---

## 🧠 2. Background Concepts

### 2.1 Software Defined Networking (SDN)

SDN separates:

* **Control Plane** → Controller (Ryu)
* **Data Plane** → Switch

### Advantages:

* Centralized control  
* Programmability  
* Dynamic traffic management  

---

### 2.2 Mininet

Mininet is a network emulator that:

* Creates virtual hosts and switches  
* Simulates real network behavior  

Components used:

* `h1`, `h2`, `h3` → Hosts  
* `s1` → Switch  

---

### 2.3 Ryu Controller

Ryu is a Python-based SDN controller that:

* Uses OpenFlow protocol  
* Handles packet events  
* Installs flow rules dynamically  

---

### 2.4 ARP

ARP maps:

IP Address → MAC Address

---

## ❗ 3. Problem Statement

Design an SDN system that:

* Handles ARP packets via controller  
* Enables communication between hosts  
* Implements traffic blocking  
* Demonstrates SDN flexibility  

---

## 🎯 4. Objectives

* Implement ARP handling using Ryu  
* Enable host communication  
* Block traffic (h1 → h2)  
* Analyze performance using ping and iperf  

---

## 🛠 5. Tools & Technologies Used

| Tool | Purpose |
|------|--------|
| Mininet | Network simulation |
| Ryu | SDN Controller |
| OpenFlow | Protocol |
| Python | Logic |
| ping | Testing |
| iperf | Throughput |

---

## 🌐 6. Network Topology

        h1
         |
h2 ---- s1 ---- h3

---

## ⚙️ 7. Approach & Design Decisions

* Controller-based ARP handling  
* Flow rule installation for efficiency  
* Blocking logic to demonstrate control  

---

## ⚙️ 8. Implementation Details

### Controller Logic:

1. Packet interception  
2. MAC learning  
3. ARP handling  
4. Flow rule installation  
5. Blocking logic  

---

### 🔧 Additional Controller (Extended)

A combined controller (`arp_controller.py`) can:

* Handle ARP + forwarding + blocking  
* Reduce multiple file usage  
* Improve control logic  

---

## 🧪 9. Execution Steps & Commands

---

### 🔹 Step 1: Clean Environment

```bash
sudo mn -c
sudo killall -9 ryu-manager
```

---

### 🔹 Step 2: Activate Environment

```bash
source ~/ryu-env/bin/activate
```

---

### 🔹 Step 3: Start Controller (Normal)

```bash
ryu-manager --ofp-tcp-listen-port 6633 arp_handler.py
```

---

### 🔹 Step 4: Start Mininet

```bash
sudo mn --controller=remote,ip=127.0.0.1,port=6633 --topo=single,3 --switch=ovsk,protocols=OpenFlow13
```

---

### 🔹 Step 5: Test Network

```bash
pingall
```

👉 Output: 0% packet loss  

---

### 🔹 Step 6: Host Communication

```bash
h1 ping h2 -c 4
h1 ping h3 -c 4
```

👉 Output: Successful communication  

---

### 🔹 Step 7: Blocking Scenario

Restart controller:

```bash
ryu-manager --ofp-tcp-listen-port 6633 arp_handler_block.py
```

---

### 🔹 Step 8: Test Blocking

```bash
h1 ping h2 -c 4
```

👉 Output: FAIL ❌  

```bash
h1 ping h3 -c 4
```

👉 Output: SUCCESS ✅  

---

### 🔹 Step 9: Throughput Test

```bash
h2 iperf -s &
h1 iperf -c h2
```

---

### 🔹 Step 10: Flow Table

```bash
sudo ovs-ofctl dump-flows s1 -O OpenFlow13
```

---

### 🔹 Step 11: Additional Commands

```bash
net
nodes
dump
```

---

## 🧪 10. Test Scenarios

### ✅ Normal Communication
* All hosts reachable  

### 🚫 Blocked Communication
* h1 → h2 blocked  

---

## 📊 11. Performance Analysis

### Latency:
* Low delay  

### Throughput:
* High bandwidth  
* Drops when blocking applied  

---

## 📋 12. Flow Table Analysis

Flow rules define:

* Match conditions  
* Actions (forward/drop)  

---

## 📸 13. Screenshots

Include:

* pingall  
* ping results  
* blocking output  
* iperf  
* flow table  

---

## 📌 14. Results

* ARP handled successfully  
* Flow rules installed  
* Blocking implemented  
* Performance verified  

---

## ✅ 15. Conclusion

This project demonstrates:

* Centralized SDN control  
* Dynamic rule installation  
* Flexible traffic management  

---

## 💯 Final Outcome

✔ Working SDN network  
✔ ARP handled  
✔ Traffic controlled  
✔ Performance analyzed  

---

🔥 Successfully demonstrates SDN concepts
