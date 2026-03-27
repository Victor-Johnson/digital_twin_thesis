# Jetson Orin Nano — device notes

## Hardware
- Module: Jetson Orin Nano 8GB
- Carrier board: Yahboom
- Storage: NVMe SSD (177GB)

## Software
- JetPack: 6.2 (L4T R36.4.7)
- Ubuntu: 22.04.5 LTS
- CUDA: 12.6
- TensorRT: 10.3
- Power mode: MAXN_SUPER (67 TOPS)

## Network
- Tailscale IP: 100.84.38.20
- ROS2 comms: FastDDS unicast over Tailscale
- Config: ~/ros2_config/fastdds_unicast.xml

## Key commands
# Check power mode
sudo nvpmodel -q

# Monitor GPU/CPU/memory live
sudo tegrastats

# Re-enable Super Mode after reboot
sudo nvpmodel -m 0
sudo jetson_clocks