# 🌐 Networking in the Cloud

## 📖 Introduction
Networking in the cloud involves the communication between servers either privately or publicly. Understanding these concepts is crucial for managing cloud-based infrastructure efficiently.

---

## 🔀 Public vs Private Network
- **Public Network**: Cloud units are accessible publicly using IP addresses or URLs.
- **Private Network**: Units are not publicly accessible but can be accessed via the management console. They must be on the same network for private communication.
- **Cloud Units**: Virtualized resources in the cloud, such as servers, databases, or applications, that operate within public or private networks.

### Load Balancer
- Acts as an intermediary, distributing traffic to multiple web servers.
- Connected to the public network, while web servers communicate with it both publicly and privately.

---

## 🌍 IP Address
- **Definition**: A unique identifier for devices on a network (internet or private).
- **Types**:
  - **IPv4**: Four parts, numbers 0–255, e.g., `69.63.176.13`.
    - Address range: `0.0.0.0` to `255.255.255.255`
    - Limited to ~4.29 billion addresses.
  - **IPv6**: Eight groups of four hexadecimal digits separated by colons, e.g., `2a03:2880:2130:cf05:face:b00c:0:1`.
    - Supports 340 trillion, trillion, trillion addresses.

### Private IP Ranges
- For IPv4:
  - `10.0.0.0` — `10.255.255.255`
  - `172.16.0.0` — `172.31.255.255`
  - `192.168.0.0` — `192.168.255.255`

---

## 🌐 DNS System
- Maps domain names to IP addresses, making it easier to access servers.
- **How It Works**: A DNS server resolves domain names to their respective IP addresses.

---

## 📊 Bandwidth
- **Incoming Bandwidth (Ingress)**: Data coming to the server (e.g., form submissions, file uploads).
- **Outgoing Bandwidth (Egress)**: Data leaving the server (e.g., webpage responses, downloads).

### Uplink and Downlink
- **Uplink**: Network protocol used to send data out of the server.
- **Downlink**: Protocol used to receive incoming data.

---

## 🏁 Conclusion
Key concepts learned:
- Public and private networks.
- IPv4 vs IPv6 and private IP ranges.
- DNS systems for resolving domain names.
- Bandwidth types and uplink/downlink communication.
