# 🚀 ARP Handling in SDN using Mininet and Ryu Controller

---

## 📌 1. Project Overview

This project demonstrates the implementation of **Address Resolution Protocol (ARP) handling in Software Defined Networking (SDN)** using the **Ryu Controller** and **Mininet Emulator**.

Unlike traditional networks, SDN separates the control and data planes, enabling centralized control of network behavior. In this project, we implement ARP handling and demonstrate both **normal communication and controlled blocking of traffic**.

---

## 🧠 2. Background Concepts

### 2.1 Software Defined Networking (SDN)

- Control Plane → Controller (Ryu)
- Data Plane → Switch

Advantages:
- Centralized control
- Programmability
- Dynamic traffic management

---

### 2.2 Mininet

- Network emulator
- Creates virtual hosts and switches

Used:
- h1, h2, h3
- s1

---

### 2.3 Ryu Controller

- Python-based SDN controller
- Uses OpenFlow
- Installs flow rules dynamically

---

### 2.4 ARP

Maps:
IP → MAC

---

## ❗ 3. Problem Statement

- Handle ARP packets
- Enable communication
- Block selected traffic
- Demonstrate SDN flexibility

---

## 🎯 4. Objectives

- ARP handling using Ryu
- Enable host communication
- Block h1 → h2
- Analyze using ping

---

## 🛠 5. Tools

- Mininet
- Ryu
- OpenFlow
- Python
- ping

---

## 🌐 6. Topology

        h1
         |
h2 ---- s1 ---- h3

---

## ⚙️ 7. Implementation Details

- Packet interception
- MAC learning
- ARP handling
- Flow rule installation
- Blocking logic

---

### 🔧 Additional Controller (Extended Implementation)

An additional controller (`arp_controller.py`) can be used to combine both forwarding and blocking logic.

It performs:
- ARP handling
- MAC learning
- Forwarding decisions
- Traffic blocking

#### Working:
1. Packet arrives at controller
2. Controller checks type
3. Learns MAC mapping
4. Applies logic:
   - Forward → allow
   - Drop → block
5. Installs flow rule

#### Advantages:
- Single controller for all logic
- Cleaner implementation
- Demonstrates advanced SDN

---

## 🧪 8. Execution

### Start Controller
source ~/ryu-env/bin/activate  
ryu-manager --ofp-tcp-listen-port 6633 arp_handler.py  

### Start Mininet
sudo mn --controller=remote,ip=127.0.0.1,port=6633 --topo=single,3 --switch=ovsk,protocols=OpenFlow13  

---

## 🧪 9. Testing

### Scenario 1
pingall → 0% loss  

### Scenario 2
h1 ping h2 → FAIL  
h1 ping h3 → WORK  

---

## 📋 10. Results

- ARP handled successfully
- Flow rules installed
- Blocking implemented

---

## ✅ 11. Conclusion

SDN enables centralized control and flexible traffic management using Ryu and Mininet.

---

## 💯 Final Outcome

✔ Working network  
✔ ARP handled  
✔ Traffic blocked  

---

