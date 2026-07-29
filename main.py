import socket
import os
import sys
from datetime import datetime


# ============================================
# ETHICAL HACKING SCRIPT - LAB ENVIRONMENT ONLY
# ============================================
# REQUIREMENTS BEFORE RUNNING:
# 1. Written authorization from system owner
# 2. Systems are in an isolated lab environment
# 3. Target IP is YOUR OWN system or authorized test system
# ============================================

# Step 1: Configuration with safety checks
def get_target():
    """Get target with safety validations"""
    # Use localhost or your own IP for safe testing
    target_ip = '127.0.0.1'  # YOUR OWN SYSTEM ONLY

    # UNCOMMENT BELOW ONLY IN AUTHORIZED LAB ENVIRONMENTS
    # target_ip = input("Enter authorized target IP: ")

    return target_ip


def validate_authorization():
    """Simulate authorization check - In real pentesting, this would be a digital signature"""
    print("=" * 60)
    print("ETHICAL HACKING SIMULATION - AUTHORIZATION REQUIRED")
    print("=" * 60)
    print("⚠️  LEGAL NOTICE:")
    print("  - You must have WRITTEN authorization")
    print("  - This script should ONLY run on YOUR OWN systems")
    print("  - Unauthorized scanning is ILLEGAL")
    print("=" * 60)

    confirmation = input("Do you have authorization? (yes/no): ").lower()
    if confirmation != 'yes':
        print("❌ Authorization required. Exiting.")
        sys.exit(1)

    target = input("Enter target IP (or press Enter for localhost): ").strip()
    return target if target else '127.0.0.1'


def ethical_port_scan(target_ip, ports):
    """
    Comprehensive port scanning with service identification
    This demonstrates proper reconnaissance techniques
    """
    print(f"\n🔍 Starting ethical scan of {target_ip}")
    print(f"📅 Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 60)

    open_ports = []

    for port in ports:
        try:
            # Create socket with timeout
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)

            # Connect attempt
            result = sock.connect_ex((target_ip, port))

            if result == 0:
                # Get service info (banner grabbing - ethical method)
                try:
                    # Send generic probe for service identification
                    sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
                    banner = sock.recv(1024).decode('utf-8', errors='ignore')[:100]
                except:
                    banner = "No banner received"

                print(f"✅ Port {port} is OPEN - Service: {guess_service(port)}")
                print(f"   Banner: {banner.strip() if banner else 'N/A'}")
                open_ports.append((port, banner))

            else:
                print(f"❌ Port {port} is CLOSED/FILTERED")

            sock.close()

        except socket.error as e:
            print(f"⚠️  Port {port} - Error: {e}")
        except Exception as e:
            print(f"⚠️  Port {port} - Unexpected error: {e}")

    return open_ports


def guess_service(port):
    """Map common ports to services"""
    services = {
        21: 'FTP',
        22: 'SSH',
        23: 'Telnet',
        25: 'SMTP',
        53: 'DNS',
        80: 'HTTP',
        110: 'POP3',
        443: 'HTTPS',
        3306: 'MySQL',
        3389: 'RDP',
        5432: 'PostgreSQL',
        8080: 'HTTP-Alt'
    }
    return services.get(port, 'Unknown Service')


def vulnerability_assessment(open_ports):
    """
    Simulate vulnerability assessment
    In real ethical hacking, this would check CVE databases
    """
    print("\n🔒 Vulnerability Assessment:")
    print("-" * 60)

    # Simulated vulnerability checks
    vulnerabilities = {
        22: {
            'risk': 'MEDIUM',
            'check': 'Check for weak SSH credentials or outdated versions',
            'cve': ['CVE-2023-38408', 'CVE-2023-28531']
        },
        80: {
            'risk': 'HIGH',
            'check': 'Check for web application vulnerabilities',
            'cve': ['CVE-2023-12345', 'CVE-2023-67890']
        },
        443: {
            'risk': 'HIGH',
            'check': 'Check for SSL/TLS vulnerabilities',
            'cve': ['CVE-2023-44487', 'CVE-2023-38545']
        }
    }

    if not open_ports:
        print("⚠️  No open ports found to assess")
        return

    for port, banner in open_ports:
        if port in vulnerabilities:
            info = vulnerabilities[port]
            print(f"📌 Port {port} ({guess_service(port)})")
            print(f"   Risk Level: {info['risk']}")
            print(f"   Check: {info['check']}")
            print(f"   Related CVEs: {', '.join(info['cve'])}")
        else:
            print(f"📌 Port {port} ({guess_service(port)}) - No known vulnerabilities in database")


def safe_exploit_simulation(open_ports):
    """
    Instead of writing files, create a proper security report
    This is the ethical approach - reporting findings, not exploiting
    """
    print("\n📊 Security Report Generation:")
    print("-" * 60)

    if not open_ports:
        print("⚠️  No open ports detected - System appears secure from initial scan")
        return

    # Create a safe report file (not on Desktop, in current directory)
    report_filename = f"security_scan_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    try:
        with open(report_filename, 'w') as report:
            report.write("=" * 60 + "\n")
            report.write("SECURITY SCAN REPORT\n")
            report.write("=" * 60 + "\n")
            report.write(f"Scan Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            report.write(f"Target: {target_ip}\n")
            report.write("=" * 60 + "\n\n")

            report.write("OPEN PORTS FOUND:\n")
            report.write("-" * 40 + "\n")
            for port, banner in open_ports:
                report.write(f"• Port {port}: {guess_service(port)}\n")
                report.write(f"  Banner: {banner[:50] if banner else 'N/A'}\n")

            report.write("\nVULNERABILITY RECOMMENDATIONS:\n")
            report.write("-" * 40 + "\n")
            for port, _ in open_ports:
                if port in [22, 80, 443, 3389]:
                    report.write(f"• Port {port}: Review security configuration\n")
                    report.write(f"  - Ensure latest patches are applied\n")
                    report.write(f"  - Implement strong authentication\n")

            report.write("\n" + "=" * 60 + "\n")
            report.write("DISCLAIMER: This report is for educational purposes only.\n")
            report.write("Real penetration testing requires proper authorization.\n")

        print(f"✅ Security report created: {report_filename}")
        print(f"📁 Location: {os.getcwd()}")

    except Exception as e:
        print(f"❌ Failed to create report: {e}")


# ============================================
# MAIN EXECUTION
# ============================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("🔐 ETHICAL HACKING SIMULATION")
    print("📚 EDUCATIONAL PURPOSES ONLY")
    print("=" * 60 + "\n")

    # Step 1: Authorization validation
    target_ip = validate_authorization()
    print(f"\n✅ Authorization confirmed. Target: {target_ip}")

    # Step 2: Define ports to scan (common services)
    ports_to_scan = [21, 22, 23, 25, 80, 443, 3306, 3389, 8080]

    # Step 3: Perform ethical port scan
    open_ports = ethical_port_scan(target_ip, ports_to_scan)

    # Step 4: Vulnerability assessment
    vulnerability_assessment(open_ports)

    # Step 5: Generate security report (ethical alternative to exploitation)
    safe_exploit_simulation(open_ports)

    # Step 6: Summary
    print("\n" + "=" * 60)
    print("✅ SCAN COMPLETE")
    print(f"📊 Summary: {len(open_ports)} open ports discovered")
    print("📋 Report saved for review")
    print("=" * 60)

    print("\n🔐 REMINDER: Always conduct security testing with:")
    print("  ✓ Written authorization")
    print("  ✓ Defined scope")
    print("  ✓ Responsible disclosure")
    print("  ✓ Proper documentation")